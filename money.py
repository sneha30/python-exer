def findmoney(x):
    
        where =x.find('$')
        start_of_price = where +1
        #print (start_of_price)
        end_of_price = start_of_price + 4
        #print (end_of_price)
        price = x[start_of_price:end_of_price]
        print(price)

def findprice(x):
        str = x.split(" ")
        price=[]
        for st in str:
                if st.startswith('$'):
                        price.append(st)
        print price
        
findmoney("the value of raisins is $114.25 ")
findprice("the value of raisins is $114.25 and caches is $34.45")
        

price("the value of raisins is $114.25 ")
price("the value of raisins is $114.25 and caches is $34.45")      

