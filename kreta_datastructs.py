from dataclasses import dataclass
@dataclass
class OSZTALYCSOPORT:
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		)
@dataclass
class OSZTALYCSOPORT:
	Uid: str
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["Nev"],
		)
@dataclass
class RENDSZERMODULOK:
	IsAktiv: bool
	Tipus: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["IsAktiv"],
		d["Tipus"],
		)
@dataclass
class MOD:
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
class MODJA:
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
class TIPUS:
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
class ALLAPOT:
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
class KATEGORIA:
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
class ERTEKFAJTA:
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
class TANULOJELENLET:
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
class IGAZOLASTIPUSA:
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
class TESTRESZABASBEALLITASOK:
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
class ORA:
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
class TANTARGY:
	Uid: str
	Kategoria: KATEGORIA
	Nev: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		KATEGORIA(d["Kategoria"]),
		d["Nev"],
		)
@dataclass
class GONDVISELOK:
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
class BANKSZAMLA:
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
class INTEZMENY:
	Uid: str
	RovidNev: str
	Rendszermodulok: list(RENDSZERMODULOK)
	TestreszabasBeallitasok: TESTRESZABASBEALLITASOK

	@classmethod
	def fromDict(cls,d):
		return cls(d["Uid"],
		d["RovidNev"],
		[RENDSZERMODULOK(v) for v in d["Rendszermodulok"]],
		TESTRESZABASBEALLITASOK(d["TestreszabasBeallitasok"]),
		)
@dataclass
class ISKOLA:
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
class DOLGOZAT:
	BejelentesDatuma: str
	Datum: str
	Modja: MODJA
	OrarendiOraOraszama: int
	RogzitoTanarNeve: str
	TantargyNeve: str
	Temaja: str
	OsztalyCsoport: OSZTALYCSOPORT
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["BejelentesDatuma"],
		d["Datum"],
		MODJA(d["Modja"]),
		d["OrarendiOraOraszama"],
		d["RogzitoTanarNeve"],
		d["TantargyNeve"],
		d["Temaja"],
		OSZTALYCSOPORT(d["OsztalyCsoport"]),
		d["Uid"],
		)
@dataclass
class IGAZOLAS:
	IgazolasAllapota: str
	IgazolasTipusa: IGAZOLASTIPUSA
	KesesPercben: None
	KeszitesDatuma: str
	Mod: MOD
	Datum: str
	Ora: ORA
	RogzitoTanarNeve: str
	Tantargy: TANTARGY
	Tipus: TIPUS
	OsztalyCsoport: OSZTALYCSOPORT
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["IgazolasAllapota"],
		IGAZOLASTIPUSA(d["IgazolasTipusa"]),
		d["KesesPercben"],
		d["KeszitesDatuma"],
		MOD(d["Mod"]),
		d["Datum"],
		ORA(d["Ora"]),
		d["RogzitoTanarNeve"],
		TANTARGY(d["Tantargy"]),
		TIPUS(d["Tipus"]),
		OSZTALYCSOPORT(d["OsztalyCsoport"]),
		d["Uid"],
		)
@dataclass
class DIAK:
	AnyjaNeve: str
	Cimek: list(list)
	Gondviselok: list(GONDVISELOK)
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
	Bankszamla: BANKSZAMLA
	Intezmeny: INTEZMENY

	@classmethod
	def fromDict(cls,d):
		return cls(d["AnyjaNeve"],
		d["Cimek"],
		[GONDVISELOK(v) for v in d["Gondviselok"]],
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
		BANKSZAMLA(d["Bankszamla"]),
		INTEZMENY(d["Intezmeny"]),
		)
@dataclass
class ERTEKELES:
	ErtekeloTanarNeve: str
	ErtekFajta: ERTEKFAJTA
	Jelleg: str
	KeszitesDatuma: str
	LattamozasDatuma: None
	Mod: MOD
	RogzitesDatuma: str
	SulySzazalekErteke: int
	SzamErtek: int
	SzovegesErtek: str
	SzovegesErtekelesRovidNev: None
	Tantargy: TANTARGY
	Tema: str
	Tipus: TIPUS
	OsztalyCsoport: OSZTALYCSOPORT
	Uid: str

	@classmethod
	def fromDict(cls,d):
		return cls(d["ErtekeloTanarNeve"],
		ERTEKFAJTA(d["ErtekFajta"]),
		d["Jelleg"],
		d["KeszitesDatuma"],
		d["LattamozasDatuma"],
		MOD(d["Mod"]),
		d["RogzitesDatuma"],
		d["SulySzazalekErteke"],
		d["SzamErtek"],
		d["SzovegesErtek"],
		d["SzovegesErtekelesRovidNev"],
		TANTARGY(d["Tantargy"]),
		d["Tema"],
		TIPUS(d["Tipus"]),
		OSZTALYCSOPORT(d["OsztalyCsoport"]),
		d["Uid"],
		)
@dataclass
class ORA:
	Allapot: ALLAPOT
	BejelentettSzamonkeresUids: list
	BejelentettSzamonkeresUid: None
	Datum: str
	HelyettesTanarNeve: None
	IsTanuloHaziFeladatEnabled: bool
	KezdetIdopont: str
	Nev: str
	Oraszam: int
	OraEvesSorszama: int
	OsztalyCsoport: OSZTALYCSOPORT
	HaziFeladatUid: None
	IsHaziFeladatMegoldva: bool
	TanarNeve: str
	Tantargy: TANTARGY
	TanuloJelenlet: TANULOJELENLET
	Tema: str
	TeremNeve: str
	Tipus: TIPUS
	Uid: str
	VegIdopont: str

	@classmethod
	def fromDict(cls,d):
		return cls(ALLAPOT(d["Allapot"]),
		d["BejelentettSzamonkeresUids"],
		d["BejelentettSzamonkeresUid"],
		d["Datum"],
		d["HelyettesTanarNeve"],
		d["IsTanuloHaziFeladatEnabled"],
		d["KezdetIdopont"],
		d["Nev"],
		d["Oraszam"],
		d["OraEvesSorszama"],
		OSZTALYCSOPORT(d["OsztalyCsoport"]),
		d["HaziFeladatUid"],
		d["IsHaziFeladatMegoldva"],
		d["TanarNeve"],
		TANTARGY(d["Tantargy"]),
		TANULOJELENLET(d["TanuloJelenlet"]),
		d["Tema"],
		d["TeremNeve"],
		TIPUS(d["Tipus"]),
		d["Uid"],
		d["VegIdopont"],
		)
