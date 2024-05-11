import sqlite3
# add quotes to element in list
def add_quotes_to_list(list):
    return ['"' + str(element) + '"' for element in list]

# convert list[tuple] 2 list(str)
def list_tupl2list_str(list):
    str_list=[]
    try:
        for tupl in list:
            str_data=''.join(tupl)
            str_list.append(str_data)
        return str_list
    # if number in tuple
    except:
        str_data=','.join('%s' %tupl for tupl in list)
        str_list=str_data.split(',')
        return str_list
    
class sql_operator:
    def __init__(self,path) -> None:
        self.con=sqlite3.connect(path)
        self.cur=self.con.cursor()
        

    def search(self,table:str,limit_key:str,limit_value:str,key:str)->str:
        """
        Search the value in database table

            table:Table name
            limit_key:Key of the constraint
            limit_value:Value of the constraint
            key:The key that corresponds to the value

            E.g:    "SELECT key FROM table WHERE limit_key = limit_value "
        """
        self.cur.execute(f"SELECT {key} FROM {table} WHERE {limit_key} ='{limit_value}'")
        result_tup =self.cur.fetchone()
        # print(result_tup)
        result=str(result_tup[0])

        return result
    
    def match_key(self,table:str,key:str,key_value:str) -> bool:
        """
        Match the key in database table

            table:Table name
            key:Search for key word
            key_value:The word's value

            E.g:    "SELECT key FROM table WHERE key = key_value "
        """
        match_data=f"SELECT {key} FROM {table} WHERE {key}='{key_value}'"
        self.cur.execute(match_data)
        result=self.cur.fetchone()
        if result:
            print("T")
            return True
        else:
            print("F")
            return False
    

    def insert(self,table:str,**kwargs:dict)->None:
        """
        Insert the data in database table
            
            table:Table name
            **kwargs:A dict to store keys and value

            E.g:    kwargs={"key":"Tom","source":"acgz.xyz","date":"20240101_09:50:46","submitter":"liu","is_valid":"1"}
                    'INSERT INTO table ("key","source","date","submitter","is_valid") VALUES ("Tom","acgz.xyz","20240101_09:50:46","liu","1")'
        """
        keys=','.join(list(kwargs.keys()))
        values=','.join(add_quotes_to_list(list(kwargs.values())))
        # print(keys,values)
        insert_data=f'insert into {table} ({keys}) values({values})'
        self.cur.execute(insert_data)
        # print(insert_data)
        self.con.commit()
        


    def update(self,table:str,limit_key:str,limit_value:str,key:str,value:str)->None:
        """
        Update the data in database table

            table:Table name
            limit_key:Key of the constraint
            limit_value:Value of the constraint
            key: The key that corresponds to the value
            value: Value of the update

            E.g:    ' update table set key= value where limit_key = limit_value '
        """
        update_data=f'update {table} set {key}="{value}" where {limit_key}="{limit_value}" '
        self.cur.execute(update_data)
        # print(update_data)
        self.con.commit()

    def get_column(self,key:str,table:str)->list:
        '''
        Get the column datas by the key from datatable 

            key:The key that corresponds to the value
            table:Table name

            E.g:    "select key from table"
        '''
        self.cur.execute(f'''select {key} from {table}''')
        temp_keys=self.cur.fetchall()
        keys=list_tupl2list_str(temp_keys)
        return keys
