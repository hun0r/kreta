import hashlib
import base64
import hmac
import requests

from datetime import datetime, timedelta

from kreta_datastructs import *

# set default headers
headers = {"User-Agent": "hu.ekreta.student/3.0.4/7.1.2/25"}
# url format
URL="https://<klik>.e-kreta.hu/ellenorzo/V3"

class session:
    def __init__(self,access_token:str,refresh_token:str,nonce:str,idp_api:"IdpApiV1",url:str):
        self.access_token:str=access_token
        self.refresh_token:str=refresh_token
        self.noone:str=nonce
        self.idp_api:IdpApiV1=idp_api
        self.url:str=url
        self.headers:dict= {
            "Authorization": f"Bearer {self.access_token}",
            "User-Agent": "hu.ekreta.tanulo/1.0.5/Android/0/0",
        }
    def __del__(self):
        self.close()
    @classmethod
    def login(cls,userName: str|int,pwd:str|int,klik:str|int)->"session":
        if isinstance(userName,int): userName=str(userName)
        if isinstance(pwd,int) or len(pwd)==8: pwd=str(pwd)[:4]+"-"+str(pwd)[4:6]+"-"+str(pwd)[6:]
        if isinstance(klik,int) or not klik.startswith("klik"): klik="klik"+str(klik)
        idp_api=IdpApiV1(KRETAEncoder())
        nonce=idp_api.getNonce()
        try: r=idp_api.login(userName,pwd,klik,nonce)
        except: raise ValueError("invalid userName/pwd")
        access_token,refresh_token=r["access_token"],r["refresh_token"]
        return cls(access_token,refresh_token,nonce,idp_api,URL.replace("<klik>",klik))
    @classmethod
    def load(cls,d:dict)->"session":
        cls(d["access_token"],d["refresh_token"],d["nonce"],IdpApiV1(KRETAEncoder()),d["url"])
    def data(self)->dict:
        return {"access_token":self.access_token,
           "refresh_token":self.refresh_token,
           "nonce":self.nonce,
           "url":self.url
           }
    def refresh(self)->None:
        klik=self.url[8:-11]
        r=self.idp_api.extendToken(self.refresh_token,klik)
        self.access_token,self.refresh_token=r["access_token"],r["refresh_token"]
        self.headers["Authorization"]=f"Bearer {self.access_token}"
    def close(self)->None:
        self.idp_api.revokeRefreshToken(self.refresh_token)
        self.refresh_token=None
        self.access_token=None
        self.headers=''
    def deleteBankAccountNumber(self):
        try:
            return requests.delete(f'{self.url}/sajat/Bankszamla', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.url}/sajat/Bankszamla', headers=self.headers).text
    def deleteReservation(self, uid : str):
        try:
            return requests.delete(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.delete(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    def downloadAttachment(self, uid : str):
        try:
            return requests.get(f'{self.url}/sajat/Csatolmany/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Csatolmany/{uid}', headers=self.headers).text
    def getAnnouncedTests(self, Uids : str = None):
        try:
            return [DOLGOZAT9.fromDict(doga) for doga in 
                requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
                }, headers=self.headers).json()
            ]
        except:
            self.refresh()
            return [DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'Uids': Uids
            }, headers=self.headers).json()]
    def getAnnouncedTests(self, datumTol : str = None, datumIg : str = None):
        try:
            return [DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [DOLGOZAT9.fromDict(doga) for doga in requests.get(f'{self.url}/sajat/BejelentettSzamonkeresek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getClassAverage(self, oktatasiNevelesiFeladatUid : str, tantargyUid : str = None):
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
    def getClassMaster(self, Uids : str):
        try:
            return requests.get(f'{self.url}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/felhasznalok/Alkalmazottak/Tanarok/Osztalyfonokok', params={
                'Uids': Uids
            }, headers=self.headers).json()
    def getConsultingHour(self, uid : str):
        try:
            return requests.get(f'{self.url}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Fogadoorak/{uid}', headers=self.headers).json()
    def getConsultingHours(self, datumTol : str = None, datumIg : str = None):
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
    def getDeviceGivenState(self) -> bool:
        try:
            return bool(requests.get(f'{self.url}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
        except:
            self.refresh()
            return bool(requests.get(f'{self.url}/TargyiEszkoz/IsEszkozKiosztva', headers=self.headers).text)
    def getEvaluations(self):
        try:
            return [ERTEKELES16.fromDict(m) for m in  requests.get(f'{self.url}/sajat/Ertekelesek', headers=self.headers).json()]
        except:
            self.refresh()
            return [ERTEKELES16.fromDict(m) for m in  requests.get(f'{self.url}/sajat/Ertekelesek', headers=self.headers).json()]
    def getGroups(self):
        try:
            return [OSZTALYCSOPORT2.fromDict(g) for g in requests.get(f'{self.url}/sajat/OsztalyCsoportok', headers=self.headers).json()]
        except:
            self.refresh()
            return [OSZTALYCSOPORT2.fromDict(g) for g in requests.get(f'{self.url}/sajat/OsztalyCsoportok', headers=self.headers).json()]
    def getGuardian4T(self):
        try:
            return [GONDVISELOK5.fromDict(g) for g in requests.get(f'{self.url}/sajat/GondviseloAdatlap', headers=self.headers).json()]
        except:
            self.refresh()
            return [GONDVISELOK5.fromDict(g) for g in requests.get(f'{self.url}/sajat/GondviseloAdatlap', headers=self.headers).json()]
    def getHomework(self, id : str):
        try:
            return  requests.get(f'{self.url}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/HaziFeladatok/{id}', headers=self.headers).json()
    def getHomeworks(self, datumTol : str = None, datumIg : str = None):
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
    def getLEPEvents(self):
        try:
            return requests.get(f'{self.url}/Lep/Eloadasok', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/Lep/Eloadasok', headers=self.headers).json()
    def getLesson(self, orarendElemUid : str = None):
        try:
            return ORA21.fromDict(requests.get(f'{self.url}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json())
        except:
            self.refresh()
            return ORA21.fromDict(requests.get(f'{self.url}/sajat/OrarendElem', params={
                'orarendElemUid': orarendElemUid
            }, headers=self.headers).json())
    def getLessons(self, datumTol : str = None, datumIg : str = None):
        try:
            return [ORA21.fromDict(o) for o in requests.get(f'{self.url}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [ORA21.fromDict(o) for o in requests.get(f'{self.url}/sajat/OrarendElemek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getNotes(self, datumTol : str = None, datumIg : str = None)->list[ERTEKELES16]:
        try:
            return [ERTEKELES16.fromDict(e) for e in requests.get(f'{self.url}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
        except:
            self.refresh()
            return [ERTEKELES16.fromDict(e) for e in requests.get(f'{self.url}/sajat/Feljegyzesek', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()]
    def getNoticeBoardItems(self):
        try:
            return requests.get(f'{self.url}/sajat/FaliujsagElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/FaliujsagElemek', headers=self.headers).json()
    def getOmissions(self, datumTol : str = None, datumIg : str = None):
        try:
            return requests.get(f'{self.url}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Mulasztasok', params={
                'datumTol': datumTol,
                'datumIg': datumIg
            }, headers=self.headers).json()
    def getRegistrationState(self):
        try:
            return requests.get(f'{self.url}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
        except:
            self.refresh()
            return requests.get(f'{self.url}/TargyiEszkoz/IsRegisztralt', headers=self.headers).text
    def getSchoolYearCalendar(self):
        try:
            return requests.get(f'{self.url}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Intezmenyek/TanevRendjeElemek', headers=self.headers).json()
    def getStudent(self):
        try:
            return DIAK16.fromDict(requests.get(f'{self.url}/sajat/TanuloAdatlap', headers=self.headers).json())
        except:
            self.refresh()
            return DIAK16.fromDict(requests.get(f'{self.url}/sajat/TanuloAdatlap', headers=self.headers).json())
    def getSubjectAverage(self, oktatasiNevelesiFeladatUid : str):
        try:
            return ERTEKELES16.fromDict(requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json())
        except:
            self.refresh()
            return ERTEKELES16.fromDict(requests.get(f'{self.url}/sajat/Ertekelesek/Atlagok/TantargyiAtlagok', params={
                'oktatasiNevelesiFeladatUid': oktatasiNevelesiFeladatUid
            }, headers=self.headers).json())
    def getTimeTableWeeks(self):
        try:
            return requests.get(f'{self.url}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
        except:
            self.refresh()
            return requests.get(f'{self.url}/sajat/Intezmenyek/Hetirendek/Orarendi', headers=self.headers).json()
    def postBankAccountNumber(self, BankszamlaSzam : str, BankszamlaTulajdonosNeve : str, BankszamlaTulajdonosTipusId : str, SzamlavezetoBank : str):
        try:
            return requests.post(f'{self.url}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/sajat/Bankszamla', data=f'BankAccountNumberPostDto(bankAccountNumber={BankszamlaSzam}, bankAccountOwnerType={BankszamlaTulajdonosTipusId}, bankAccountOwnerName={BankszamlaTulajdonosNeve}, bankName={SzamlavezetoBank})', headers=self.headers).text
    def postContact(self, email, telefonszam):
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
    def postCovidForm(self):
        try:
            return requests.post(f'{self.url}/Bejelentes/Covid', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/Bejelentes/Covid', headers=self.headers).text
    def postReservation(self, uid : str):
        try:
            return requests.post(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/sajat/Fogadoorak/Idopontok/Jelentkezesek/{uid}', headers=self.headers).text
    def updateLepEventPermission(self, EloadasId : str, Dontes : bool):
        try:
            return requests.post(f'{self.url}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text
        except:
            self.refresh()
            return requests.post(f'{self.url}/Lep/Eloadasok/GondviseloEngedelyezes', data=f'LepEventGuardianPermissionPostDto(eventId={EloadasId}, isPermitted={str(Dontes)})', headers=self.headers).text

def span(tól,ig)->(str,str):
    today=datetime.now()
    tólDate=today-timedelta(days=tól)
    igDate=today-timedelta(days=ig)
    return tólDate.strftime("%Y-%m-%d"), igDate.strftime("%Y-%m-%d")
# not mine
# Az E-Kréta API-hoz szükséges Nonce kezelő
class KRETAEncoder:
    def __init__(self) -> None:
        self.KeyProd = "baSsxOwlU1jM".encode("utf-8")

    def encodeRefreshToken(self, refreshToken):
        return self.encodeKey(refreshToken)

    def createLoginKey(self, userName, instituteCode, nonce):
        loginKeyPayload = instituteCode.upper() + nonce + userName.upper()
        return self.encodeKey(loginKeyPayload)

    def encodeKey(self, payload: str):
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
    user=session.login()
    with open("getTimeTableWeeks","w") as f:
        print(user.getTimeTableWeeks(),file=f)
    with open("getGroups","w") as f:
        print(user.getGroups(),file=f)
    with open("getHomeworks","w") as f:
        print(user.getHomeworks(span(-60,1)),file=f)
    with open("getGuardian4T","w") as f:
        print(user.getGuardian4T(),file=f)
    with open("getLessons","w") as f:
        print(user.getLessons(span(-1,6)),file=f)
    with open("getNotes","w") as f:
        print(user.getNotes(span(-60,0)),file=f)
    with open("getEvaluations","w") as f:
        print(user.getEvaluations(),file=f)
    with open("getStudent","w") as f:
        print(user.getStudent(),file=f)
    with open("getOmissions","w") as f:
        print(user.getOmissions(span(-30,0)),file=f)
    print("Done!")
