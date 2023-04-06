#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
# Creating Dictionary to store data
available_products = {1001: {"name": "avocado", "price": 230,
                             "category": "grocery",
                             "quantity": 10, "date": "10/03/2021"},
                      1002: {"name": "lotion", "price": 250,
                             "category": "beauty & personal",
                             "quantity": 100,
                             "date": "15/07/2021"},
                      1003: {"name": "pain reliever", "price": 500,
                             "category": "health",
                             "quantity": 200, "date": "12/04/2021"},
                      1004: {"name": "dry pasta", "price": 20,
                             "category": "grocery",
                             "quantity": 50, "date": "27/06/2021"},
                      1005: {"name": "toothbrush", "price": 700,
                             "category": "beauty & personal",
                             "quantity": 100,
                             "date": "30/01/2021"},
                      1006: {"name": "halloween candy", "price": 33,
                             "category": "grocery",
                             "quantity": 56, "date": "22/02/2021"},
                      1007: {"name": "mascara", "price": 765,
                             "category": "beauty & personal",
                             "quantity": 70,
                             "date": "11/03/2021"},
                      1008: {"name": "capsicum", "price": 764,
                             "category": "grocery",
                             "quantity": 90, "date": "16/02/2021"},
                      1009: {"name": "blush", "price": 87,
                             "category": "beauty & personal",
                             "quantity": 50, "date": "17/07/2021"},
                      1010: {"name": "granola bars", "price": 24,
                             "category": "grocery", "quantity": 60,
                             "date": "20/05/2021"},
                      }
js=json.dumps(available_products)
userdict1={'U1':{'P1':{'date':'23/03/2023','amount':'3000','sucess':'done'},'P2':{'date':'29/03/2023','amount':'1000','sucess':'failed'}},
          'U2':{'P1':{'date':'25/03/2023','amount':'6000','sucess':'done'}}}
ujs=json.dumps(userdict1)
# main function of admin functionalities
def admin():
    print("===welcome to admin page ====")
    
    while(1):
        print("1. Display all products with their details")
        print("2. Display specific product with details")
        print("3. Insert product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Display User purchase report")
        print("7. Exit")
        print("8. Delete all database")
        print("Enter your choice")
        
        n=int(input())
        if(n==1):
            display_alldata()
        elif(n==2):
            display_product()
        elif(n==3):
            insert_product()
        elif(n==4):
            update_product()
        elif(n==5):
            delete_product()
        elif(n==6):
            purchase_report()
        elif(n==7):
            return
        elif(n==8):
            delete_db()
        else:
            print("Enter a valid choice")

# function to display all data
def display_alldata():
    import pandas as pd
    import json
    from IPython.display import display
    
    print("enter 0 for displaying data in order of insertion /n enter 1 for displaying data categorywise")
    n=int(input())
    if n==0:
        data=json.loads(js)
        table1=pd.DataFrame(columns=['ID','name','price','category','quantity','date'])
        for i in data.keys():
            temp=pd.DataFrame(columns=['ID'])
            temp['ID']=[i]
            for j in data[i].keys():
                temp[j]=data[i][j]
            table1=pd.concat([table1,temp],axis=0)           
            table1=table1.reset_index(drop=True)
        display(table1)
    elif n==1:
        data=json.loads(js)
        table1=pd.DataFrame(columns=['ID','name','price','category','quantity','date'])
        cate=[]
        for i in data.keys():
            temp=pd.DataFrame(columns=['ID'])
            temp['ID']=[i]
            for j in data[i].keys():
                temp[j]=data[i][j]
                if j=='category':
                    cate.append(data[i][j])
            table1=pd.concat([table1,temp],axis=0)
            table1=table1.reset_index(drop=True)
            cate=set(cate)
            cate=list(cate)
        for k in cate:
            temp=pd.DataFrame()
            temp=table1[table1['category']==k]
            display(temp)
        
    else:
        print("enter valid input")
                

def display_product():
    import pandas as pd
    from IPython import display
    df3=pd.read_json(js)
    print("enter the productid to search")
    search=int(input())
    for i in df3:
        if i==search:
            print(df3[i])


def insert_product():
        import pandas as pd
        import json
        data=json.loads(js)
        print("enter key of the product")
        keyvalue=str(input())
        if keyvalue not in data.keys():
            print("product name")
            name=input()
            print("product price")
            price=input()
            print("product category")
            category=input()
            print("quantity")
            quantity=input()
            print("date")
            date=input()
            data[keyvalue]={'name':name,'price':price,'category':category,'quantity':quantity,'date':'date'}
            print(data)
        else:
            print("enter unique key")


def delete_product():
    import pandas as pd
    import json
    data=json.loads(js)
    print("enter key of product to be deleted")
    key=input()
    if key in data.keys():
        del data[key]
    else:
        print("key not found")
    print(data)
        
        
def update_product():
    import pandas as pd
    import json
    data=json.loads(js)
    print("0: update all attributes of product 1: Update particular attribute of product 2: exit")
    n=int(input())
    if n==0:
        print("enter product key")
        key=input()
        if key in data.keys():
            print("product name")
            name=input()
            print("product price")
            price=input()
            print("product category")
            category=input()
            print("quantity")
            quantity=input()
            print("date")
            date=input()
            data[key]={'name':name,'price':price,'category':category,'quantity':quantity,'date':'date'}
            print(data)
    elif n==1:
        print("enter product key")
        key=input()
        if key in data.keys():
            print("enter attribute to be changed")
            attr=input()
            print("attribute value to be changed")
            attr_val=input()
            data[key][attr]=attr_val
            print(data)
    else:
        return
            

def purchase_report():
    import os.path
    import pandas as pd
    import json
    # if(os.path.isfile("user_data.json") is False):
    #     print("no user reports are present")
    #     return
    user_data=json.loads(ujs)
    
#     fd=open("user_data.json",'r')
#     txt=fd.read()
#     user_data=json.load(txt)
#     fd.close()
    
    print("0: To check all Bills 1: To check bills of specific user")
    n=int(input())
    if n==1:
        print("enter userId")
        i=input()
        temp=pd.DataFrame()
        table=pd.DataFrame()
        if i in user_data.keys():
            for j in user_data[i].keys():
                d=dict()
                d['userId']=i
                d['purchasenumber']=j
                for k in user_data[i][j]:
                    d[k]=user_data[i][j][k]
                temp=temp.append(d,ignore_index=True)
                d=dict()
            table=pd.concat([temp,table])
        table=table.reset_index(drop=True)
        print(table)
    elif n==0:
        for i in user_data.keys():
            print("user_id:",i)
            for j in user_data[i].keys():
                print("purchase Id:",j)
                for k in user_data[i][j].keys():
                    print(k,user_data[i][j][k])
    else:
        print("Please enter valid choice")
                

admin()



