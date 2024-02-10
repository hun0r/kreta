# e-kréta V3 api handler  
  - install: `pip install e_kreta_hun0r`
  - handle the kreta api without haveing to find all the links  
  - structure the responses so u dont need an example to tell the keys  
  - group users  
## usage  
### on the level of session (for simple programs handeling only your account)  
  - represents a kreta login
  - auto revokes refreshtoken when deleted

login/create instance:  
```python
from e_kreta3_1 import kreat_base3 as k_base
MySession=k_base.session.login(userName,pwd,klik)
```
  - all args are auto formatted:
    - kreta username is an int in str format so if it gets an int it runs str(username)
    - pwd is an int/date as str format: year-month-day auto adds the '-' if gets int/str without it
    - klik is an 'klik'+str(int) when int/str without it is passed auto adds that

fromDict() and data():
```python
data=Mysession.data()
Mysesssion=k_base.session.fromDict(data)
```
  - converts to dict and back for storage in like a json  

the 31 api requests:
```python
tol,ig=k_base.span(-2,7)
homeworks=Mysession.getHomeworks(tol,ig)
```
  - span returns an array of 2 dates of days days from today
  - all funcs i hope are understandible because i dont want to describe them all
  - some return a dataclass some a dict if u get a dict open a response with the template for this issue

### on the level of Diak
  - represents a user even when that use is logged out
  - access api requests through .session
  - auto revokes refreshtoken when deleted

login/make instance:
```python
from e_kreta3_1 import e_kreta, kreta_base
User=e_kreta.Diak(kreta_base.session(username,pwd,klik))
#or
User=e_kreta.Diak()
User.login(username,pwd,klik)
```
  - define from session or start empty
  - if started empty or logged out use login
    - same regulators as in session
    - if it was logged in checks if username is same as last time
    - MyID is the username hashed and no usable login info is stored

log out:
```python
User.log_out(level)
```
  - levels
    - 0: log out of session
    - 1: remove info
    - 2: forget who it was (basically same state when started empty)
    - 3: delete self
  - all sets is_logged_in to false

fromDict and data:
  - same use as in session

### on the level of SchoolClass
  - represents a class
  - helps organise users if there are a lot of them
  - has problems not yet recomended
  - access students by name from .students

make instance:
```python
from e_kreta3_1 import e_kreta
MyClass=e_kreta.SchoolClass(students,klik=klik)
```
  - defined from students and klik
    - students is a dict[name/id:Diak]
    - klik is regulated to its format and is used for logging in new users

add student and login student funcs:
```python
MyClass.add_student(name/id,Diak)
MyClass.addstudents(dict[name/id:Diak])
MyClass.log_new_student_in(name/id,username,pwd)
```
  - name is str
  - add_student() adds one student
  - add_students() updates the students dict
  - log_new_student_in logs new student in adds to class
  - all return the student/students that it logged in

fromDict and data:
  - same use as in all

known errors:
  - no real check if a student belongs there
  - have to re run the init to have up to date data

## known errors and what may be coming
  - no dataclass for many requests (open issue if u find one and can show a sample of the response)
  - no data funcs for the dataclasses
  - SchoolClass has problems
  - even bigger grouping (School)
  - SchoolClass -> dict subclass
  - Diak -> session subclass












