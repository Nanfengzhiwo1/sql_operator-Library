from sql_operator import *

database_path="E:/1/collect.db"

sql_oper=sql_operator(database_path)

# get_key=sql_oper.search("Items","name","apple","price")

# print(get_key)

# ismatch=sql_oper.match_key("Comments","commentator","Newton")

# print(ismatch)

# kwargs={
#     "name":"pear",
#     "price":"22$",
#     "date":"2024_05_21"
# }
# sql_oper.insert("Items",**kwargs)
# sql_oper.commit()

# sql_oper.update("Items","id","2","price","2$")
# sql_oper.commit()

get_col=sql_oper.get_column("date","Items")
print(get_col)