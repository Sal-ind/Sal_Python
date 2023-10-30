import os
import datetime as dt
print("last accessed time",os.path.getatime("D:/demo"))
print("last modified time",os.path.getmtime("D:/demo"))
accsess_date=dt.datetime.fromtimestamp(os.path.getatime('D:/demo')).strftime('%y-%m-%d')
accsess_modified=dt.datetime.fromtimestamp(os.path.getmtime('D:/demo')).strftime('%y-%m-%d')
print(accsess_date)
print(accsess_modified)
