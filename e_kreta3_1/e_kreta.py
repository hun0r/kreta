import e_kreta3_1.kreta_base3 as k_base
import e_kreta3_1.dc as dc
import hashlib

class SchoolClass:
    """represents a Class where u have classmates and etc."""
    def __init__(self,students:dict[str,"Diak"]={},egyeb:dict={},klik:str|int='')->None:
        self.students:dict["Diak"]=students
        if students!=[]:
            sess:k_base.session=students.values()[0].session
            self.groups:list[dc.CSOPORT10]=sess.getGroups()
            Uids=[group.OsztalyFonok.Uid for group in self.groups if group.OsztalyFonok.Uid]
            Ofok=[sess.getClassMaster(Uid) for Uid in Uids]
            self.Ofok=Ofok
        else: 
            self.Ofok=[]
            self.groups:list[dc.CSOPORT10]=[]
        
        # klik regulator
        if isinstance(klik,int) or not klik.startswith("klik"): klik="klik"+str(klik)
        #when not set must be set manually
        self.klik=klik
        self.groups=set(sum([student.session.getGroups() for student in  students.values()],[]))
        self.egyeb=egyeb
    
    def __del__(self)->None:
        for student in self.students.values():
            student.__del__()
    
    @classmethod
    def fromDict(cls,data:dict)->"SchoolClass":
        """used to load from a dict/json"""
        students={name:Diak.fromDict(student) for name,student in data["students"].items()}
        egyeb=data["egyeb"]
        cls(students,egyeb)
    
    def data(self)->dict:
        """store to dict (so u can dump to json)"""
        return {
            "students":{name:student.data() for name,student in self.students.items()},
            "egyeb":self.egyeb
        }
    
    def add_student(self,name:str,student:"Diak")->"Diak":
        """add class mate"""
        self.students[name]=student
        return student
    def add_students(self,students:list["Diak"])->list["Diak"]:
        """add class mates"""
        for student in students: self.add_student(student)
        return students
    def log_new_student_in(self,userName:str|int,pwd:str|int)->"Diak":
        """log new class inmate in and add as classmate"""
        return self.add_student(Diak(k_base.session.login(userName,pwd,self.klik)))

class Diak:
    """layer on session so a student exists even if logged out"""
    def __init__(self,session:k_base.session|None=None,egyeb:dict={})->None:
        """make from session or create empty log in later"""
        self.MyID=session.MyID if session else None
        self.session=session
        self.info=self.session.getStudent() if self.session else None
        self.egyeb:dict=egyeb
        self.is_logged_in=bool(session)
    
    def __del__(self)->None:
        self.session.__del__()
    
    @classmethod
    def fromDict(cls,data:dict)->"Diak":
        """used to load from a dict/json"""
        session=k_base.session.fromDict(data["session"])
        egyeb=data["egyeb"]
        cls(session,egyeb)

    def data(self)->dict:
        """store to dict (so u can dump to json)"""
        return {
            "session":self.session.data(),
            "egyeb":self.egyeb
        }
    def login(self,userName: str|int,pwd:str|int,klik:str|int)->None:
        """log in if created empty or logged out"""
        # arg regulator
        if isinstance(userName,int): userName=str(userName)
        # check if session of the user    
        if self.MyID!=hashlib.sha256(userName.encode('utf-8')).hexdigest():
            raise Exception("this login info is incorrect for this user")
        else: self.__init__(k_base.session.login(userName,pwd,klik),egyeb=self.egyeb)
    
    def log_out(self,level:int=0)->None:
        """log out:\n
        lvl0: del session\n
        lvl1: empty info\n
        lvl2: basically become a fresh, sessionless\n
        lvl3: delete self"""
        if level>=0: del self.session
        if level>=1: self.info=None
        if level>=2: self.MyID=""
        if level>=3: del self
        self.is_logged_in=False
        
    