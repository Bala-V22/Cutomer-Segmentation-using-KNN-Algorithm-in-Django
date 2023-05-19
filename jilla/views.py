from django.shortcuts import render
import pymysql
import pickle


con = pymysql.connect(host='localhost', user='root',password = "jillabala",db='customer')
mycursor = con.cursor()

global id


def reg(request):
    return render(request, ("html/register.html"))

def data(request):
    if request.method == "POST":
        name = request.POST['name']
        gmail = request.POST['email']
        age = int(request.POST['age'])
        gender= request.POST['gender']
        income = int(request.POST['income'])
        password = request.POST['password']
 
    
    sql = "INSERT INTO first_project (name, email_id, gender, age, income, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, gmail, gender, age, income, password)
    mycursor.execute(sql, val)
    con.commit()

     
    return render(request, "html/register.html", {'name': name}) 

def log(request):
    
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        mycursor.execute('SELECT * FROM first_project WHERE name = %s AND password = %s', (username, password))
        account = mycursor.fetchone()
        global lid
        lid=list(account)
        print(account)
        id=lid[0]

        if account:
            
            print("done")
            machine_learning()
            if kmean==0:
                return render(request, "html/home 1b.html")
            elif kmean==1:
                return render(request, "html/home 2b.html")
            elif kmean==2:
                # return render(request, "html/home.html")
                pass
            else:
                # return render(request, "html/home.html") 
                pass

        else:
            
            print("fail")
            return render(request, ("html/register.html"))

    
def machine_learning():
    Sex=lid[3]
    Age=lid[4]
    Income=lid[5]

    if Sex == "male":
        Sex=0
    else:
        Sex=1 
    if Sex==1:
        if Age<25:
            Marital_status=1   #1 Means unMarried
        else:
            Marital_status=0   #0 Means Married 
    else:
        if Age<28:
            Marital_status=1   #1 Means unMarried
        else:
            Marital_status=0   #0 Means Married 

    if Income > 150000:
        Occupation=2
    elif Income > 100000:
        Occupation=1
    else:
        Occupation=0

    if Occupation == 0:
        Settlement_size=0
    elif Income > 150000:
        Settlement_size=2           
    else:
        import random
  
        Settlement_size= random.randint(1, 2)
    print(Marital_status)    
    print(Settlement_size)    
    print(Occupation)
    pickled_model = pickle.load(open('jilla/Source to train and app/Customer Segmentation/model.pkl', 'rb'))
    predict=pickled_model.predict([[Sex,Marital_status,Age,Income,Occupation,Settlement_size]])
    global kmean
    print(predict)
    kmean=predict

def home(request):
    return render(request, ("html/home.html"))

    