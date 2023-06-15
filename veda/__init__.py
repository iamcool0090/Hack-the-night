import glob, os
from pathlib import Path
from . import db

cursor,conn = db.connect()
cursor.execute("DROP TABLE IF EXISTS FILES")


sql ='''CREATE TABLE FILES(
   PATH CHAR(200),
   NAME CHAR(100),
   CT_TIME CHAR(50)
)'''


cursor.execute(sql)



# print(__file__)
# for files in glob.glob("veda/data/pdf_files/*"):
#         files.replace('/','\\')

##get every file with is respective directory
for dir in glob.glob("veda/data/*"):
    for file in glob.glob(dir.replace('\\','/') + "/*"):
        
        #TODO 
            #update file path in sqlite 
            #update dir in sqlite
            #update metadata related to file in sqlite
        
        file = file.replace('\\','/')
        dir = dir.replace('\\','/')
        #gets all the stats related to the files 
        file_stat = os.stat(file.replace('\\','/'))

        sql = 'INSERT INTO FILES(PATH,NAME,CT_TIME) VALUES (?,?,?)'
        file_path = str(Path(__file__).parent.parent) + '\\' + file.replace('/', '\\')
        name = Path(file_path).name
        ct_time = os.stat(file_path).st_ctime
        cursor.execute(sql, (file_path, name, ct_time))
        print(file_path)

conn.commit()

#Closing the connection
conn.close()

print()