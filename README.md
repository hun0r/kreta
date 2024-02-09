# e-kréta V3 api handler
## use
### session
fast description:  
  -session is the heart of the api handler  
  -for simple programs its enough  
use:  
  -login (classmethod)  
  -has to and from dict converters: fromDict() and data()  
  -use the api links  
  -auto logs out when deleted  
### Diak
fast desription:  
  -basically wraps the session in a second layer so the object dosent dissapier when logged out  
use:  
  -can be defined by session  
    -when none specified starts as logged out  
    -set .session to add session later  
    -or use login()  
    -MyID is used to not store the userName and still tell if session belongs to Diak   
  -access session commands throught .session (tell me if i should make it subclass of session somehow)  
  -has to and from dict converters: fromDict() and data()  
  -read on the rest of the funcs in doc str or code  
### SchoolClass
fast description:  
  -a second wrap around Diak  
  -used to store lot of Diaks in groups by Class tho no check is yet implemented  
use:  
  -define by dict[name:student] and klik  
  -u need to re inisialize every now and than so groups is up to date (later will fix)  
  -access students by .students[name] (tell me if i should make Schoolclass a dict subclass)  
## main todo list
  -dataclass to all responses  
  -data() to all dataclasses  
  -finding out how to indent in ReadMe
