from dataclasses import dataclass
@dataclass
class OSZTALYCSOPORT1:
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		)
@dataclass
class OSZTALYFONOK1:
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		)
@dataclass
class RENDSZERMODULOK2:
	IsAktiv: bool = None
	Tipus: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["IsAktiv"] if "IsAktiv" in d else None,
		d["Tipus"] if "Tipus" in d else None,
		)
@dataclass
class TAGSAGOK2:
	BesorolasDatuma: str = None
	KisorolasDatuma: None = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["BesorolasDatuma"] if "BesorolasDatuma" in d else None,
		d["KisorolasDatuma"] if "KisorolasDatuma" in d else None,
		)
@dataclass
class OSZTALYCSOPORT2:
	Uid: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class CSATOLMANYOK2:
	azonosito: int = None
	fajlNev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["fajlNev"] if "fajlNev" in d else None,
		)
@dataclass
class MODJA3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class TIPUS3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class TANULOJELENLET3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class ERTEKFAJTA3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class OKTATASNEVELESIFELADAT3:
	Uid: str = None
	Nev: str = None
	Leiras: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Nev"] if "Nev" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		)
@dataclass
class TANTARGY3:
	Uid: str = None
	Kategoria: "KATEGORIA3" = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		KATEGORIA3.fromDict(d["Kategoria"]) if "Kategoria" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class KATEGORIA3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class OKTATASNEVELESIKATEGORIA3:
	Uid: str = None
	Nev: str = None
	Leiras: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Nev"] if "Nev" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		)
@dataclass
class IGAZOLASTIPUSA3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class ALLAPOT3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class MOD3:
	Uid: str = None
	Leiras: str = None
	Nev: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Leiras"] if "Leiras" in d else None,
		d["Nev"] if "Nev" in d else None,
		)
@dataclass
class ORA3:
	KezdoDatum: str = None
	VegDatum: str = None
	Oraszam: int = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["KezdoDatum"] if "KezdoDatum" in d else None,
		d["VegDatum"] if "VegDatum" in d else None,
		d["Oraszam"] if "Oraszam" in d else None,
		)
@dataclass
class CIMZETTLISTA4:
	azonosito: int = None
	kretaAzonosito: int = None
	nev: str = None
	tipus: "TIPUS5" = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["kretaAzonosito"] if "kretaAzonosito" in d else None,
		d["nev"] if "nev" in d else None,
		TIPUS5.fromDict(d["tipus"]) if "tipus" in d else None,
		)
@dataclass
class BANKSZAMLA4:
	BankszamlaSzam: None = None
	BankszamlaTulajdonosTipusId: None = None
	BankszamlaTulajdonosNeve: None = None
	IsReadOnly: bool = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["BankszamlaSzam"] if "BankszamlaSzam" in d else None,
		d["BankszamlaTulajdonosTipusId"] if "BankszamlaTulajdonosTipusId" in d else None,
		d["BankszamlaTulajdonosNeve"] if "BankszamlaTulajdonosNeve" in d else None,
		d["IsReadOnly"] if "IsReadOnly" in d else None,
		)
@dataclass
class INTEZMENY4:
	Uid: str = None
	RovidNev: str = None
	Rendszermodulok: list["RENDSZERMODULOK2"] = None
	TestreszabasBeallitasok: "TESTRESZABASBEALLITASOK5" = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["RovidNev"] if "RovidNev" in d else None,
		[RENDSZERMODULOK2.fromDict(v) for v in d["Rendszermodulok"]] if "Rendszermodulok" in d else None,
		TESTRESZABASBEALLITASOK5.fromDict(d["TestreszabasBeallitasok"]) if "TestreszabasBeallitasok" in d else None,
		)
@dataclass
class STATUSZ5:
	azonosito: int = None
	kod: str = None
	rovidNev: str = None
	nev: str = None
	leiras: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["kod"] if "kod" in d else None,
		d["rovidNev"] if "rovidNev" in d else None,
		d["nev"] if "nev" in d else None,
		d["leiras"] if "leiras" in d else None,
		)
@dataclass
class GONDVISELOK5:
	EmailCim: str = None
	Nev: str = None
	Telefonszam: str = None
	IsTorvenyesKepviselo: bool = None
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["EmailCim"] if "EmailCim" in d else None,
		d["Nev"] if "Nev" in d else None,
		d["Telefonszam"] if "Telefonszam" in d else None,
		d["IsTorvenyesKepviselo"] if "IsTorvenyesKepviselo" in d else None,
		d["Uid"] if "Uid" in d else None,
		)
@dataclass
class TIPUS5:
	azonosito: int = None
	kod: str = None
	rovidNev: str = None
	nev: str = None
	leiras: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["kod"] if "kod" in d else None,
		d["rovidNev"] if "rovidNev" in d else None,
		d["nev"] if "nev" in d else None,
		d["leiras"] if "leiras" in d else None,
		)
@dataclass
class TESTRESZABASBEALLITASOK5:
	IsDiakRogzithetHaziFeladatot: bool = None
	IsTanorakTemajaMegtekinthetoEllenorzoben: bool = None
	IsOsztalyAtlagMegjeleniteseEllenorzoben: bool = None
	ErtekelesekMegjelenitesenekKesleltetesenekMerteke: int = None
	KovetkezoTelepitesDatuma: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["IsDiakRogzithetHaziFeladatot"] if "IsDiakRogzithetHaziFeladatot" in d else None,
		d["IsTanorakTemajaMegtekinthetoEllenorzoben"] if "IsTanorakTemajaMegtekinthetoEllenorzoben" in d else None,
		d["IsOsztalyAtlagMegjeleniteseEllenorzoben"] if "IsOsztalyAtlagMegjeleniteseEllenorzoben" in d else None,
		d["ErtekelesekMegjelenitesenekKesleltetesenekMerteke"] if "ErtekelesekMegjelenitesenekKesleltetesenekMerteke" in d else None,
		d["KovetkezoTelepitesDatuma"] if "KovetkezoTelepitesDatuma" in d else None,
		)
@dataclass
class EUGYINTEZES_UZENET_RESZLETES5:
	azonosito: int = None
	isElolvasva: bool = None
	isToroltElem: bool = None
	tipus: "TIPUS5" = None
	uzenet: "UZENET9" = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["isElolvasva"] if "isElolvasva" in d else None,
		d["isToroltElem"] if "isToroltElem" in d else None,
		TIPUS5.fromDict(d["tipus"]) if "tipus" in d else None,
		UZENET9.fromDict(d["uzenet"]) if "uzenet" in d else None,
		)
@dataclass
class EUGYINTEZES_UZENET8:
	azonosito: int = None
	uzenetAzonosito: int = None
	uzenetKuldesDatum: str = None
	uzenetFeladoNev: str = None
	uzenetFeladoTitulus: str = None
	uzenetTargy: str = None
	hasCsatolmany: bool = None
	isElolvasva: bool = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["uzenetAzonosito"] if "uzenetAzonosito" in d else None,
		d["uzenetKuldesDatum"] if "uzenetKuldesDatum" in d else None,
		d["uzenetFeladoNev"] if "uzenetFeladoNev" in d else None,
		d["uzenetFeladoTitulus"] if "uzenetFeladoTitulus" in d else None,
		d["uzenetTargy"] if "uzenetTargy" in d else None,
		d["hasCsatolmany"] if "hasCsatolmany" in d else None,
		d["isElolvasva"] if "isElolvasva" in d else None,
		)
@dataclass
class DOLGOZAT9:
	BejelentesDatuma: str = None
	Datum: str = None
	Modja: "MODJA3" = None
	OrarendiOraOraszama: int = None
	RogzitoTanarNeve: str = None
	TantargyNeve: str = None
	Temaja: str = None
	OsztalyCsoport: "OSZTALYCSOPORT1" = None
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["BejelentesDatuma"] if "BejelentesDatuma" in d else None,
		d["Datum"] if "Datum" in d else None,
		MODJA3.fromDict(d["Modja"]) if "Modja" in d else None,
		d["OrarendiOraOraszama"] if "OrarendiOraOraszama" in d else None,
		d["RogzitoTanarNeve"] if "RogzitoTanarNeve" in d else None,
		d["TantargyNeve"] if "TantargyNeve" in d else None,
		d["Temaja"] if "Temaja" in d else None,
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]) if "OsztalyCsoport" in d else None,
		d["Uid"] if "Uid" in d else None,
		)
@dataclass
class ISKOLA9:
	instituteId: int = None
	instituteCode: str = None
	name: str = None
	city: str = None
	url: str = None
	advertisingUrl: str = None
	informationImageUrl: str = None
	informationUrl: str = None
	featureToggleSet: dict = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["instituteId"] if "instituteId" in d else None,
		d["instituteCode"] if "instituteCode" in d else None,
		d["name"] if "name" in d else None,
		d["city"] if "city" in d else None,
		d["url"] if "url" in d else None,
		d["advertisingUrl"] if "advertisingUrl" in d else None,
		d["informationImageUrl"] if "informationImageUrl" in d else None,
		d["informationUrl"] if "informationUrl" in d else None,
		d["featureToggleSet"] if "featureToggleSet" in d else None,
		)
@dataclass
class UZENET9:
	azonosito: int = None
	kuldesDatum: str = None
	feladoNev: str = None
	feladoTitulus: str = None
	szoveg: str = None
	targy: str = None
	statusz: "STATUSZ5" = None
	cimzettLista: list["CIMZETTLISTA4"] = None
	csatolmanyok: list["CSATOLMANYOK2"] = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["azonosito"] if "azonosito" in d else None,
		d["kuldesDatum"] if "kuldesDatum" in d else None,
		d["feladoNev"] if "feladoNev" in d else None,
		d["feladoTitulus"] if "feladoTitulus" in d else None,
		d["szoveg"] if "szoveg" in d else None,
		d["targy"] if "targy" in d else None,
		STATUSZ5.fromDict(d["statusz"]) if "statusz" in d else None,
		[CIMZETTLISTA4.fromDict(v) for v in d["cimzettLista"]] if "cimzettLista" in d else None,
		[CSATOLMANYOK2.fromDict(v) for v in d["csatolmanyok"]] if "csatolmanyok" in d else None,
		)
@dataclass
class CSOPORT10:
	Uid: str = None
	Nev: str = None
	OsztalyFonok: "OSZTALYFONOK1" = None
	OsztalyFonokHelyettes: None = None
	OktatasNevelesiFeladat: "OKTATASNEVELESIFELADAT3" = None
	OktatasNevelesiKategoria: "OKTATASNEVELESIKATEGORIA3" = None
	OktatasNevelesiFeladatSortIndex: int = None
	IsAktiv: bool = None
	Tipus: str = None
	Tagsagok: list["TAGSAGOK2"] = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"] if "Uid" in d else None,
		d["Nev"] if "Nev" in d else None,
		OSZTALYFONOK1.fromDict(d["OsztalyFonok"]) if "OsztalyFonok" in d else None,
		d["OsztalyFonokHelyettes"] if "OsztalyFonokHelyettes" in d else None,
		OKTATASNEVELESIFELADAT3.fromDict(d["OktatasNevelesiFeladat"]) if "OktatasNevelesiFeladat" in d else None,
		OKTATASNEVELESIKATEGORIA3.fromDict(d["OktatasNevelesiKategoria"]) if "OktatasNevelesiKategoria" in d else None,
		d["OktatasNevelesiFeladatSortIndex"] if "OktatasNevelesiFeladatSortIndex" in d else None,
		d["IsAktiv"] if "IsAktiv" in d else None,
		d["Tipus"] if "Tipus" in d else None,
		[TAGSAGOK2.fromDict(v) for v in d["Tagsagok"]] if "Tagsagok" in d else None,
		)
@dataclass
class IGAZOLAS12:
	IgazolasAllapota: str = None
	IgazolasTipusa: "IGAZOLASTIPUSA3" = None
	KesesPercben: None = None
	KeszitesDatuma: str = None
	Mod: "MOD3" = None
	Datum: str = None
	Ora: "ORA3" = None
	RogzitoTanarNeve: str = None
	Tantargy: "TANTARGY3" = None
	Tipus: "TIPUS3" = None
	OsztalyCsoport: "OSZTALYCSOPORT1" = None
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["IgazolasAllapota"] if "IgazolasAllapota" in d else None,
		IGAZOLASTIPUSA3.fromDict(d["IgazolasTipusa"]) if "IgazolasTipusa" in d else None,
		d["KesesPercben"] if "KesesPercben" in d else None,
		d["KeszitesDatuma"] if "KeszitesDatuma" in d else None,
		MOD3.fromDict(d["Mod"]) if "Mod" in d else None,
		d["Datum"] if "Datum" in d else None,
		ORA3.fromDict(d["Ora"]) if "Ora" in d else None,
		d["RogzitoTanarNeve"] if "RogzitoTanarNeve" in d else None,
		TANTARGY3.fromDict(d["Tantargy"]) if "Tantargy" in d else None,
		TIPUS3.fromDict(d["Tipus"]) if "Tipus" in d else None,
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]) if "OsztalyCsoport" in d else None,
		d["Uid"] if "Uid" in d else None,
		)
@dataclass
class ERTEKELES16:
	ErtekeloTanarNeve: str = None
	ErtekFajta: "ERTEKFAJTA3" = None
	Jelleg: str = None
	KeszitesDatuma: str = None
	LattamozasDatuma: None = None
	Mod: "MOD3" = None
	RogzitesDatuma: str = None
	SulySzazalekErteke: int = None
	SzamErtek: int = None
	SzovegesErtek: str = None
	SzovegesErtekelesRovidNev: None = None
	Tantargy: "TANTARGY3" = None
	Tema: str = None
	Tipus: "TIPUS3" = None
	OsztalyCsoport: "OSZTALYCSOPORT1" = None
	Uid: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["ErtekeloTanarNeve"] if "ErtekeloTanarNeve" in d else None,
		ERTEKFAJTA3.fromDict(d["ErtekFajta"]) if "ErtekFajta" in d else None,
		d["Jelleg"] if "Jelleg" in d else None,
		d["KeszitesDatuma"] if "KeszitesDatuma" in d else None,
		d["LattamozasDatuma"] if "LattamozasDatuma" in d else None,
		MOD3.fromDict(d["Mod"]) if "Mod" in d else None,
		d["RogzitesDatuma"] if "RogzitesDatuma" in d else None,
		d["SulySzazalekErteke"] if "SulySzazalekErteke" in d else None,
		d["SzamErtek"] if "SzamErtek" in d else None,
		d["SzovegesErtek"] if "SzovegesErtek" in d else None,
		d["SzovegesErtekelesRovidNev"] if "SzovegesErtekelesRovidNev" in d else None,
		TANTARGY3.fromDict(d["Tantargy"]) if "Tantargy" in d else None,
		d["Tema"] if "Tema" in d else None,
		TIPUS3.fromDict(d["Tipus"]) if "Tipus" in d else None,
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]) if "OsztalyCsoport" in d else None,
		d["Uid"] if "Uid" in d else None,
		)
@dataclass
class DIAK16:
	AnyjaNeve: str = None
	Cimek: list[list] = None
	Gondviselok: list["GONDVISELOK5"] = None
	IntezmenyAzonosito: str = None
	IntezmenyNev: str = None
	Nev: str = None
	SzuletesiDatum: str = None
	SzuletesiEv: int = None
	SzuletesiHonap: int = None
	SzuletesiNap: int = None
	SzuletesiHely: str = None
	SzuletesiNev: str = None
	TanevUid: str = None
	Uid: str = None
	Bankszamla: "BANKSZAMLA4" = None
	Intezmeny: "INTEZMENY4" = None

	@classmethod
	def fromDict(cls,d):
		return cls(d["AnyjaNeve"] if "AnyjaNeve" in d else None,
		d["Cimek"] if "Cimek" in d else None,
		[GONDVISELOK5.fromDict(v) for v in d["Gondviselok"]] if "Gondviselok" in d else None,
		d["IntezmenyAzonosito"] if "IntezmenyAzonosito" in d else None,
		d["IntezmenyNev"] if "IntezmenyNev" in d else None,
		d["Nev"] if "Nev" in d else None,
		d["SzuletesiDatum"] if "SzuletesiDatum" in d else None,
		d["SzuletesiEv"] if "SzuletesiEv" in d else None,
		d["SzuletesiHonap"] if "SzuletesiHonap" in d else None,
		d["SzuletesiNap"] if "SzuletesiNap" in d else None,
		d["SzuletesiHely"] if "SzuletesiHely" in d else None,
		d["SzuletesiNev"] if "SzuletesiNev" in d else None,
		d["TanevUid"] if "TanevUid" in d else None,
		d["Uid"] if "Uid" in d else None,
		BANKSZAMLA4.fromDict(d["Bankszamla"]) if "Bankszamla" in d else None,
		INTEZMENY4.fromDict(d["Intezmeny"]) if "Intezmeny" in d else None,
		)
@dataclass
class ORAREND_ORA21:
	Allapot: "ALLAPOT3" = None
	BejelentettSzamonkeresUids: list = None
	BejelentettSzamonkeresUid: None = None
	Datum: str = None
	HelyettesTanarNeve: None = None
	IsTanuloHaziFeladatEnabled: bool = None
	KezdetIdopont: str = None
	Nev: str = None
	Oraszam: int = None
	OraEvesSorszama: int = None
	OsztalyCsoport: "OSZTALYCSOPORT2" = None
	HaziFeladatUid: None = None
	IsHaziFeladatMegoldva: bool = None
	TanarNeve: str = None
	Tantargy: "TANTARGY3" = None
	TanuloJelenlet: "TANULOJELENLET3" = None
	Tema: str = None
	TeremNeve: str = None
	Tipus: "TIPUS3" = None
	Uid: str = None
	VegIdopont: str = None

	@classmethod
	def fromDict(cls,d):
		return cls(ALLAPOT3.fromDict(d["Allapot"]) if "Allapot" in d else None,
		d["BejelentettSzamonkeresUids"] if "BejelentettSzamonkeresUids" in d else None,
		d["BejelentettSzamonkeresUid"] if "BejelentettSzamonkeresUid" in d else None,
		d["Datum"] if "Datum" in d else None,
		d["HelyettesTanarNeve"] if "HelyettesTanarNeve" in d else None,
		d["IsTanuloHaziFeladatEnabled"] if "IsTanuloHaziFeladatEnabled" in d else None,
		d["KezdetIdopont"] if "KezdetIdopont" in d else None,
		d["Nev"] if "Nev" in d else None,
		d["Oraszam"] if "Oraszam" in d else None,
		d["OraEvesSorszama"] if "OraEvesSorszama" in d else None,
		OSZTALYCSOPORT2.fromDict(d["OsztalyCsoport"]) if "OsztalyCsoport" in d else None,
		d["HaziFeladatUid"] if "HaziFeladatUid" in d else None,
		d["IsHaziFeladatMegoldva"] if "IsHaziFeladatMegoldva" in d else None,
		d["TanarNeve"] if "TanarNeve" in d else None,
		TANTARGY3.fromDict(d["Tantargy"]) if "Tantargy" in d else None,
		TANULOJELENLET3.fromDict(d["TanuloJelenlet"]) if "TanuloJelenlet" in d else None,
		d["Tema"] if "Tema" in d else None,
		d["TeremNeve"] if "TeremNeve" in d else None,
		TIPUS3.fromDict(d["Tipus"]) if "Tipus" in d else None,
		d["Uid"] if "Uid" in d else None,
		d["VegIdopont"] if "VegIdopont" in d else None,
		)
