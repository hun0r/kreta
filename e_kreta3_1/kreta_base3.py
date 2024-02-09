import hashlib
import base64
import hmac
import requests

from datetime import datetime, timedelta

from e_kreta3_1 import dc

# set default headers
headers = {"User-Agent": "hu.ekreta.student/3.0.4/7.1.2/25"}
# url format
URL="https://<klik>.e-kreta.hu/ellenorzo/V3"


class session:
    """base of the api represents a KRETA login"""
    def __init__(self,access_token:str,refresh_token:str,nonce:str,idp_api:"IdpApiV1",url:str,MyID:str)->None:
        """please dont use by hand"""
        self.MyID=MyID
        self.access_token:str=access_token
        self.refresh_token:str=refresh_token
        self.nonce:str=nonce
        self.idp_api:IdpApiV1=idp_api
        self.url:str=url
        self.headers:dict= {
            "Authorization": f"Bearer {self.access_token}",
            "User-Agent": "hu.ekreta.tanulo/1.0.5/Android/0/0",
        }
    def __del__(self)->None:
        self.close()
    @classmethod
    def login(cls,userName: str|int,pwd:str|int,klik:str|int)->"session":
        """Login user"""
        if isinstance(userName,int): userName=str(userName)
        if isinstance(pwd,int) or len(pwd)==8: pwd=str(pwd)[:4]+"-"+str(pwd)[4:6]+"-"+str(pwd)[6:]
        if isinstance(klik,int) or not klik.startswith("klik"): klik="klik"+str(klik)
        idp_api=IdpApiV1(KRETAEncoder())
        nonce=idp_api.getNonce()
        try: r=idp_api.login(userName,pwd,klik,nonce)
        except: raise ValueError("invalid userName/pwd")
        access_token,refresh_token=r["access_token"],r["refresh_token"]
        return cls(access_token,refresh_token,nonce,idp_api,URL.replace("<klik>",klik),hashlib.sha256(userName.encode("utf-8")).hexdigest())
    
    @classmethod
    def fromDict(cls,d:dict)->"session":
        """used to load from a dict/json"""
        cls(d["access_token"],d["refresh_token"],d["nonce"],IdpApiV1(KRETAEncoder()),d["url"],d["MyID"])
    
    def data(self)->dict:
        """store to dict (so u can dump to json)"""
        return {"access_token":self.access_token,
           "refresh_token":self.refresh_token,
           "nonce":self.nonce,
           "url":self.url,
           "MyID":self.MyID
           }
    
    def refresh(self)->None:
        """refresh access token should run automatically"""
        klik=self.url[8:-11]
        r=self.idp_api.extendToken(self.refresh_token,klik)
        self.access_token,self.refresh_token=r["access_token"],r["refresh_token"]
        self.headers["Authorization"]=f"Bearer {self.access_token}"
    
    def close(self)->None:
        """log out of KRETA"""
        self.idp_api.revokeRefreshToken(self.refresh_token)
    
    # 31 painfull api requests
    def deleteBankAccountNumber(self)->requests.Response:# no. 1
        try:
            return requests.delete(f'{self.url}/sajat/Bankszamla', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.url}/sajat/Bankszamla', headers=self.headers).text
    def deleteReservation(self, uid : str)->requests.Response:# no. 2
        try:
            return requests.delete(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    def downloadAttachment(self, uid : str)->str:# no. 3
        try:
            return requests.get(f'{self.url}/sajat/Csatolmany/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Csatolmany/{uid}', headers=self.headers).text
    def getAnnouncedTests(self, Uids : str = None)->list[dc.DOLGOZAT9]:# no. 4
        try:
            return [dc.DOLGOZAT9.fromDict(doga) for doga in 
                requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
                }, headers=self.headers).json()
            ]
        except:
            self.refresh()
            return [dc.DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
            }, headers=self.headers).json()]
    def getAnnouncedTests(self, datumTol : str = None, datumIg : str = None)->list[dc.DOLGOZAT9]:# no. 5
        try:
            return [dc.DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getClassAverage(self, oktatasiNevelesiFeladatUid : str, tantargyUid : str = None):# no. 6
        try:
            return requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/OsztalyAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid,
                'tantargyUid': tantargyUid
            }, headers=self.headers).json()
    def getClassMaster(self, Uids : str):# no. 7
        try:
            return requests.get(f'{self.url}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
    def getConsultingHour(self, uid : str):# no. 8
        try:
            return requests.get(f'{self.url}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
    def getConsultingHours(self, datumTol : str = None, datumIg : str = None)->list:# no. 9
        try:
            return requests.get(f'{self.url}/sajat/Fogadoorak', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Fogadoorak', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    def getDeviceGivenState(self) -> bool or None:# no. 10
        try:
            return bool(requests.get(f'{self.url}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
        except:
            self.refresh()
            return bool(requests.get(f'{self.url}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
    def getEvaluations(self)->list[dc.ERTEKELES16]:# no. 11
        try:
            return [dc.ERTEKELES16.fromDict(e) for e in requests.get(f'{self.url}/sajat/Ertekelesek', headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.ERTEKELES16.fromDict(e) for e in requests.get(f'{self.url}/sajat/Ertekelesek', headers=self.headers).json()]
    def getGroups(self)->list[dc.CSOPORT10]:# no. 12
        try:
            return [dc.CSOPORT10.fromDict(i) for i in requests.get(f'{self.url}/sajat/OsztalyCsoportok', headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.CSOPORT10.fromDict(i) for i in requests.get(f'{self.url}/sajat/OsztalyCsoportok', headers=self.headers).json()]
    def getGuardian4T(self):# no. 13
        try:
            return requests.get(f'{self.url}/sajat/GondviseloAdatlap', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/GondviseloAdatlap', headers=self.headers).json()
    def getHomework(self, id : str):# no. 14
        try:
            return requests.get(f'{self.url}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
    def getHomeworks(self, datumTol : str = None, datumIg : str = None):# no. 15
        try:
            return requests.get(f'{self.url}/sajat/HaziFeladatok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/HaziFeladatok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    def getLEPEvents(self):# no. 16
        try:
            return requests.get(f'{self.url}/Lep/Eloadasok', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/Lep/Eloadasok', headers=self.headers).json()
    def getLesson(self, orarendElemUid : str = None):# no. 17
        try:
            return dc.ORAREND_ORA21.fromDict(requests.get(f'{self.url}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json())
        except:
            self.refresh()
            return dc.ORAREND_ORA21.fromDict(requests.get(f'{self.url}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json())
    def getLessons(self, datumTol : str = None, datumIg : str = None):# no. 18
        try:
            return [dc.ORAREND_ORA21.fromDict(i) for i in requests.get(f'{self.url}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.ORAREND_ORA21.fromDict(i) for i in requests.get(f'{self.url}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getNotes(self, datumTol : str = None, datumIg : str = None):# no. 19
        try:
            return requests.get(f'{self.url}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    def getNoticeBoardItems(self):# no. 20
        try:
            return requests.get(f'{self.url}/sajat/FaliujsagElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/FaliujsagElemek', headers=self.headers).json()
    def getOmissions(self, datumTol : str = None, datumIg : str = None)->list[dc.IGAZOLAS12]:# no. 21
        try:
            return [dc.IGAZOLAS12.fromDict(i) for i in requests.get(f'{self.url}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.IGAZOLAS12.fromDict(i) for i in requests.get(f'{self.url}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getRegistrationState(self)->str:# no. 22
        """probably a str bool i didnt test it yet"""
        try:
            return requests.get(f'{self.url}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.url}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
    def getSchoolYearCalendar(self):# no. 23
        try:
            return requests.get(f'{self.url}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
    def getStudent(self)->dc.DIAK16:# no. 24
        try:
            return dc.DIAK16.fromDict(requests.get(f'{self.url}/sajat/TanuloAdatlap', headers=self.headers).json())
        except:
            self.refresh()
            return dc.DIAK16.fromDict(requests.get(f'{self.url}/sajat/TanuloAdatlap', headers=self.headers).json())
    def getSubjectAverage(self, oktatasiNevelesiFeladatUid : str):# no. 25
        try:
            return requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json()
    def getTimeTableWeeks(self):# no. 26
        try:
            return [dc.ORAREND_ORA21.fromDict(i) for i in requests.get(f'{self.url}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()]
        except:
            self.refresh()
            return [dc.ORAREND_ORA21.fromDict(i) for i in requests.get(f'{self.url}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()]
    def postBankAccountNumber(self, BankszamlaSzam : str, BankszamlaTulajdonosNeve : str, BankszamlaTulajdonosTipusId : str, SzamlavezetoBank : str):# no. 27
        try:
            return requests.post(f'{self.url}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
    def postContact(self, email, telefonszam):# no. 28
        try:
            return requests.post(f'{self.url}/sajat/Elerhetoseg', data={
                'email': email,
                'telefonszam': telefonszam
            }, headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/sajat/Elerhetoseg', data={
                'email': email,
                'telefonszam': telefonszam
            }, headers=self.headers).text
    def postCovidForm(self):# no. 29
        try:
            return requests.post(f'{self.url}/Bejelentes/Covid', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/Bejelentes/Covid', headers=self.headers).text
    def postReservation(self, uid : str):# no. 30
        try:
            return requests.post(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    def updateLepEventPermission(self, EloadasId : str, Dontes : bool):# no. 31
        try:
            return requests.post(f'{self.url}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text

def span(tól,ig)->(str,str):
    """used to take e.g. Homework from a span not id"""
    today=datetime.now()
    tólDate=today-timedelta(days=tól)
    igDate=today-timedelta(days=ig)
    return tólDate.strftime("%Y-%m-%d"), igDate.strftime("%Y-%m-%d")

# not mine
# Az E-Kréta API-hoz szükséges Nonce kezelő
class KRETAEncoder:
    def __init__(self) -> None:
        self.KeyProd = "baSsxOwlU1jM".encode("utf-8")

    def encodeRefreshToken(self, refreshToken)->str:
        return self.encodeKey(refreshToken)

    def createLoginKey(self, userName, instituteCode, nonce)->str:
        loginKeyPayload = instituteCode.upper() + nonce + userName.upper()
        return self.encodeKey(loginKeyPayload)

    def encodeKey(self, payload: str)->str:
        return base64.b64encode(
            hmac.new(
                self.KeyProd, payload.encode("utf-8"), digestmod=hashlib.sha512
            ).digest()
        ).decode("utf-8")

# Az E-Kréta API-hoz szükséges kommunikáció kezelő
class IdpApiV1:
    def __init__(self, kretaEncoder: KRETAEncoder, proxies: dict = None) -> None:
        self.kretaEncoder = kretaEncoder
        self.proxies = proxies

    def extendToken(self, refresh_token: str, klik: str) -> dict: 
        refresh_token_data = {
            "refresh_token": refresh_token,
            "institute_code": klik,
            "grant_type": "refresh_token",
            "client_id": "kreta-ellenorzo-mobile-android",
            "refresh_user_data": False,
        }

        refreshTokenHeaders = headers.copy()
        refreshTokenHeaders.update(
            {
                "X-AuthorizationPolicy-Key": self.kretaEncoder.encodeRefreshToken(
                    refresh_token
                ),
                "X-AuthorizationPolicy-Version": "v2",
            }
        )

        return requests.post(
            "https://idp.e-kreta.hu/connect/token",
            data=refresh_token_data,
            headers=refreshTokenHeaders,
            proxies=self.proxies,
        ).json()

    def getNonce(self) -> str or None:
        return requests.get(
            "https://idp.e-kreta.hu/nonce", headers=headers
        ).text

    def login(
        self, userName: str, password: str, institute_code: str, nonce: str
    ) -> dict:
        try:
            login_data = {
                "userName": userName,
                "password": password,
                "institute_code": institute_code,
                "grant_type": "password",
                "client_id": "kreta-ellenorzo-mobile-android",
            }

            loginHeaders = headers.copy()
            loginHeaders.update(
                {
                    "X-AuthorizationPolicy-Nonce": nonce,
                    "X-AuthorizationPolicy-Key": self.kretaEncoder.createLoginKey(
                        userName, institute_code, nonce
                    ),
                    "X-AuthorizationPolicy-Version": "v2",
                }
            )

            return requests.post(
                "https://idp.e-kreta.hu/connect/token",
                data=login_data,
                headers=loginHeaders,
                proxies=self.proxies,
            ).json()
        except Exception as e:
            print(e, " :kabbe a faszom")

    def revokeRefreshToken(self, refresh_token: str):
        try:
            revokeRefreshTokenData = {
                "token": refresh_token,
                "client_id": "kreta-ellenorzo-mobile-android",
                "token_type": "refresh token",
            }

            return requests.post(
                "https://idp.e-kreta.hu/connect/revocation",
                data=revokeRefreshTokenData,
                headers=headers,
                proxies=self.proxies,
            ).text
        except Exception as e:
            print(e)
if __name__=="__main__":
    # tests here
    pass