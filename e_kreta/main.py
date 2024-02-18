from . import kreta_base as k_base
from . import dc
import hashlib

class SchoolClass:
    """represents a Class where u have classmates and etc."""
    def __init__(self,students:dict[str,"Diak"]={},egyeb:dict={},klik:str|int='')->None:
        """recommended to start with klik only

        Args:
            students (dict[str,&quot;Diak&quot;], optional): dict of name:student. Defaults to {}.
            egyeb (dict, optional): extra data to bundle with the class. Defaults to {}.
            klik (str | int, optional): auto formatted recomended to specify. Defaults to ''.
        """
        self.students:dict[str,"Diak"]=students
        if students!=[]:
            sess:k_base.session=students.values()[0].session
            Uids=[group.OsztalyFonok.Uid for group in sess.getGroups() if group.OsztalyFonok.Uid]
            Ofok=[sess.getClassMaster(Uid) for Uid in Uids]
            self.Ofok=set(Ofok)
        else: 
            self.Ofok=set()
        
        self.klik=k_base.klik_formatter(klik)
        self.groups=set(sum([student.session.getGroups() for student in  students.values()],[]))
        self.egyeb=egyeb
    
    def __del__(self)->None:
        for student in self.students.values():
            student.__del__()
    
    @classmethod
    def fromDict(cls,data:dict)->"SchoolClass":
        """Loads the Class from a dict. Get the dict from .data()

        Args:
            data (dict): dict to load from

        Returns:
            SchoolClass: loaded instance
        """
        students={name:Diak.fromDict(student) for name,student in data["students"].items()}
        egyeb=data["egyeb"]
        cls(students,egyeb)
    
    def data(self)->dict:
        """get data to json serializible dict to store and later load

        Returns:
            dict: data for storage and to pass to fromDict()
        """
        return {
            "students":{name:student.data() for name,student in self.students.items()},
            "egyeb":self.egyeb
        }
    
    def add_student(self,name:str,student:"Diak")->"Diak":
        """add student to Class. Only works if student is logged in

        Be careful!:
            no check is implemented to check the students class yet
            
            only School is checked
        
        Args:
            name (str): name of the student to be accessed with
            student (Diak): students Diak obj

        Raises:
            Exception: student doesnt go to this school.

        Returns:
            Diak: the student that was logged in
        """
        if student.MySchoolID!=self.klik: raise Exception(f'sudent {name} doesnt go to this school')
        self.students[name]=student
        self.groups.update(student.session.getGroups())
        return student
    def add_students(self,students:dict[str,"Diak"])->dict[str,"Diak"]:
        """adds students from a dict with .add_student()
        
        for more information see that command

        Returns:
            dict[str,Diak]: same as input
        """
        for name,student in students.items(): self.add_student(name,student)
        return students
    def log_new_student_in(self,userName:str|int,pwd:str|int)->"Diak":
        """log in a student and add to class

        Args:
            userName (str | int): username
            pwd (str | int): password

        Returns:
            Diak: the student that was logged in
        """
        return self.add_student(Diak(klik=self.klik,session=k_base.session.login(userName,pwd,self.klik)))

class Diak:
    """layer on session so a student can exists even if logged out"""
    def __init__(self,klik,session:k_base.session|None=None,egyeb:dict={})->None:
        """make sure to set klik

        Args:
            session (k_base.session | None, optional): session of the student. Defaults to None.
            egyeb (dict, optional): extra data to bundle with the student. Defaults to {}.
            klik (str): klik id required to later add to a Class.
        """
        self.MySchoolID=k_base.klik_formatter(klik)
        self.MyID=session.MyID if session else None
        self.session=session
        self.info=self.session.getStudent() if self.session else None
        self.egyeb:dict=egyeb
        self.is_logged_in=bool(session)
    
    def __del__(self)->None:
        self.session.__del__()
    
    @classmethod
    def fromDict(cls:"Diak",data:dict)->"Diak":
        """Load a student from a dict made by .data()

        Args:
            cls (Diak): _description_
            data (dict): dict

        Returns:
            Diak: the loaded student
        """
        session=k_base.session.fromDict(data["session"])
        egyeb=data["egyeb"]
        klik=data["klik"]
        Diak(klik=klik,session=session,egyeb=egyeb)

    def data(self)->dict:
        """make a dict from the student

        Returns:
            dict: dict that u can load() from
        """
        return {
            "session":self.session.data() if self.session else None,
            "egyeb":self.egyeb,
            "klik":self.MySchoolID
        }
    def login(self,userName: str|int,pwd:str|int,klik:str|int,error:bool=False)->None:
        """create session instance if logged out

        Args:
            userName (str | int): userName
            pwd (str | int): password
            klik (str | int): klik id
            error (bool, optional): deletes session first used when logged in but session isnt working. Defaults to False.

        Raises:
            Exception: raised when the userName is not the users userName
            ValueError: raised for incorrect login info
        """
        # arg regulator
        userName=k_base.User_name_formatter(userName)
        if self.session: print('already logged in')
        if error: del self.session
        # check if session of the user
        if self.MyID!=hashlib.sha256(userName.encode('utf-8')).hexdigest():
            raise Exception("this login info is incorrect for this user")
        else: self.__init__(k_base.session.login(userName,pwd,klik),egyeb=self.egyeb,klik=klik)
    
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
        

