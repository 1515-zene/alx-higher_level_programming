#!/usr/bin/python3 
LockedClass = import('101-locked_class').LockedClass 

lc = LockedClass() 
lc.first_name = "John" 
try: 
    lc.last_name = "Snow" 
except Exception as e: 
    print("[{}] {}".format(e.class.name, e))
