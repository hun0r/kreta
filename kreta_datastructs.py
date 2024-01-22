from dataclasses import dataclass
@dataclass
class OSZTALYCSOPORT1:
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		)
@dataclass
class OSZTALYCSOPORT2:
	Uid: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Nev"],
		)
@dataclass
class RENDSZERMODULOK2:
	IsAktiv: bool
	Tipus: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["IsAktiv"],
		d["Tipus"],
		)
@dataclass
class MOD3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class TIPUS3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class MODJA3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class ALLAPOT3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class KATEGORIA3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class ERTEKFAJTA3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class IGAZOLASTIPUSA3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class TANULOJELENLET3:
	Uid: str
	Leiras: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Leiras"],
		d["Nev"],
		)
@dataclass
class ORA3:
	KezdoDatum: str
	VegDatum: str
	Oraszam: int

	@classmethod
	def fromDict(cls,d):
		return cls(d["KezdoDatum"],
		d["VegDatum"],
		d["Oraszam"],
		)
@dataclass
class TANTARGY3:
	Uid: str
	Kategoria: KATEGORIA3
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		KATEGORIA3.fromDict(d["Kategoria"]),
		d["Nev"],
		)
@dataclass
class GONDVISELOK5:
	EmailCim: str
	Nev: str
	Telefonszam: str
	IsTorvenyesKepviselo: bool
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["EmailCim"],
		d["Nev"],
		d["Telefonszam"],
		d["IsTorvenyesKepviselo"],
		d["Uid"],
		)
@dataclass
class TESTRESZABASBEALLITASOK5:
	IsDiakRogzithetHaziFeladatot: bool
	IsTanorakTemajaMegtekinthetoEllenorzoben: bool
	IsOsztalyAtlagMegjeleniteseEllenorzoben: bool
	ErtekelesekMegjelenitesenekKesleltetesenekMerteke: int
	KovetkezoTelepitesDatuma: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["IsDiakRogzithetHaziFeladatot"],
		d["IsTanorakTemajaMegtekinthetoEllenorzoben"],
		d["IsOsztalyAtlagMegjeleniteseEllenorzoben"],
		d["ErtekelesekMegjelenitesenekKesleltetesenekMerteke"],
		d["KovetkezoTelepitesDatuma"],
		)
@dataclass
class BANKSZAMLA4:
	BankszamlaSzam: None
	BankszamlaTulajdonosTipusId: None
	BankszamlaTulajdonosNeve: None
	IsReadOnly: bool

	@classmethod
	def fromDict(cls,d):
		return cls(d["BankszamlaSzam"],
		d["BankszamlaTulajdonosTipusId"],
		d["BankszamlaTulajdonosNeve"],
		d["IsReadOnly"],
		)
@dataclass
class INTEZMENY4:
	Uid: str
	RovidNev: str
	Rendszermodulok: list(RENDSZERMODULOK2)
	TestreszabasBeallitasok: TESTRESZABASBEALLITASOK5

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["RovidNev"],
		[RENDSZERMODULOK2.fromDict(v) for v in d["Rendszermodulok"]],
		TESTRESZABASBEALLITASOK5.fromDict(d["TestreszabasBeallitasok"]),
		)
@dataclass
class ISKOLA9:
	instituteId: int
	instituteCode: str
	name: str
	city: str
	url: str
	advertisingUrl: str
	informationImageUrl: str
	informationUrl: str
	featureToggleSet: dict

	@classmethod
	def fromDict(cls,d):
		return cls(d["instituteId"],
		d["instituteCode"],
		d["name"],
		d["city"],
		d["url"],
		d["advertisingUrl"],
		d["informationImageUrl"],
		d["informationUrl"],
		d["featureToggleSet"],
		)
@dataclass
class DOLGOZAT9:
	BejelentesDatuma: str
	Datum: str
	Modja: MODJA3
	OrarendiOraOraszama: int
	RogzitoTanarNeve: str
	TantargyNeve: str
	Temaja: str
	OsztalyCsoport: OSZTALYCSOPORT1
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["BejelentesDatuma"],
		d["Datum"],
		MODJA3.fromDict(d["Modja"]),
		d["OrarendiOraOraszama"],
		d["RogzitoTanarNeve"],
		d["TantargyNeve"],
		d["Temaja"],
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]),
		d["Uid"],
		)

@dataclass
class IGAZOLAS12:
	IgazolasAllapota: str
	IgazolasTipusa: IGAZOLASTIPUSA3
	KesesPercben: None
	KeszitesDatuma: str
	Mod: MOD3
	Datum: str
	Ora: ORA3
	RogzitoTanarNeve: str
	Tantargy: TANTARGY3
	Tipus: TIPUS3
	OsztalyCsoport: OSZTALYCSOPORT1
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["IgazolasAllapota"],
		IGAZOLASTIPUSA3.fromDict(d["IgazolasTipusa"]),
		d["KesesPercben"],
		d["KeszitesDatuma"],
		MOD3.fromDict(d["Mod"]),
		d["Datum"],
		ORA3.fromDict(d["Ora"]),
		d["RogzitoTanarNeve"],
		TANTARGY3.fromDict(d["Tantargy"]),
		TIPUS3.fromDict(d["Tipus"]),
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]),
		d["Uid"],
		)
@dataclass
class DIAK16:
	AnyjaNeve: str
	Cimek: list(list)
	Gondviselok: list(GONDVISELOK5)
	IntezmenyAzonosito: str
	IntezmenyNev: str
	Nev: str
	SzuletesiDatum: str
	SzuletesiEv: int
	SzuletesiHonap: int
	SzuletesiNap: int
	SzuletesiHely: str
	SzuletesiNev: str
	TanevUid: str
	Uid: str
	Bankszamla: BANKSZAMLA4
	Intezmeny: INTEZMENY4

	@classmethod
	def fromDict(cls,d):
		return cls(d["AnyjaNeve"],
		d["Cimek"],
		[GONDVISELOK5.fromDict(v) for v in d["Gondviselok"]],
		d["IntezmenyAzonosito"],
		d["IntezmenyNev"],
		d["Nev"],
		d["SzuletesiDatum"],
		d["SzuletesiEv"],
		d["SzuletesiHonap"],
		d["SzuletesiNap"],
		d["SzuletesiHely"],
		d["SzuletesiNev"],
		d["TanevUid"],
		d["Uid"],
		BANKSZAMLA4.fromDict(d["Bankszamla"]),
		INTEZMENY4.fromDict(d["Intezmeny"]),
		)
@dataclass
class ERTEKELES16:
	ErtekeloTanarNeve: str
	ErtekFajta: ERTEKFAJTA3
	Jelleg: str
	KeszitesDatuma: str
	LattamozasDatuma: None
	Mod: MOD3
	RogzitesDatuma: str
	SulySzazalekErteke: int
	SzamErtek: int
	SzovegesErtek: str
	SzovegesErtekelesRovidNev: None
	Tantargy: TANTARGY3
	Tema: str
	Tipus: TIPUS3
	OsztalyCsoport: OSZTALYCSOPORT1
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["ErtekeloTanarNeve"],
		ERTEKFAJTA3.fromDict(d["ErtekFajta"]),
		d["Jelleg"],
		d["KeszitesDatuma"],
		d["LattamozasDatuma"],
		MOD3.fromDict(d["Mod"]),
		d["RogzitesDatuma"],
		d["SulySzazalekErteke"],
		d["SzamErtek"],
		d["SzovegesErtek"],
		d["SzovegesErtekelesRovidNev"],
		TANTARGY3.fromDict(d["Tantargy"]),
		d["Tema"],
		TIPUS3.fromDict(d["Tipus"]),
		OSZTALYCSOPORT1.fromDict(d["OsztalyCsoport"]),
		d["Uid"],
		)
@dataclass
class ORA21:
	Allapot: ALLAPOT3
	BejelentettSzamonkeresUids: list
	BejelentettSzamonkeresUid: None
	Datum: str
	HelyettesTanarNeve: None
	IsTanuloHaziFeladatEnabled: bool
	KezdetIdopont: str
	Nev: str
	Oraszam: int
	OraEvesSorszama: int
	OsztalyCsoport: OSZTALYCSOPORT2
	HaziFeladatUid: None
	IsHaziFeladatMegoldva: bool
	TanarNeve: str
	Tantargy: TANTARGY3
	TanuloJelenlet: TANULOJELENLET3
	Tema: str
	TeremNeve: str
	Tipus: TIPUS3
	Uid: str
	VegIdopont: str

	@classmethod
	def fromDict(cls,d):
		return cls(ALLAPOT3.fromDict(d["Allapot"]),
		d["BejelentettSzamonkeresUids"],
		d["BejelentettSzamonkeresUid"],
		d["Datum"],
		d["HelyettesTanarNeve"],
		d["IsTanuloHaziFeladatEnabled"],
		d["KezdetIdopont"],
		d["Nev"],
		d["Oraszam"],
		d["OraEvesSorszama"],
		OSZTALYCSOPORT2.fromDict(d["OsztalyCsoport"]),
		d["HaziFeladatUid"],
		d["IsHaziFeladatMegoldva"],
		d["TanarNeve"],
		TANTARGY3.fromDict(d["Tantargy"]),
		TANULOJELENLET3.fromDict(d["TanuloJelenlet"]),
		d["Tema"],
		d["TeremNeve"],
		TIPUS3.fromDict(d["Tipus"]),
		d["Uid"],
		d["VegIdopont"],
		)
