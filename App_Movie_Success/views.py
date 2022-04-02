from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.http import JsonResponse
# Create your views here.
def base(request):
    return render(request, "base.html", {})


def home(request):
    return render(request, "home.html", {})


def UserRegisteration(request):
    if request.method == "POST":
        F_name = request.POST['fname']
        L_name = request.POST['lname']
        Age = request.POST['Age']
        U_mobile = request.POST['phone']
        U_email = request.POST['Eid']
        U_username = request.POST['uname']
        U_password = request.POST['pwd']
        Image = request.FILES['img']
        if  UserDetails.objects.filter(Email = U_email ,Username = U_username).exists():
            myObjects = UserDetails.objects.all().filter(Email = U_email ,Username = U_username )
            name = myObjects[0].Username
            messages.error(request,'Already Registered Please Login')
            return render(request,'Login.html',{})
        else:
            users = UserDetails(Firstname = F_name, Lastname= L_name, Phone =  U_mobile, Email =  U_email, Username = U_username, Password= U_password,Image=Image,Age=Age)
            users.save()
            #messages.info(request,'Registered Sucessfully')
            return render(request,'Login.html',{})
    else:
        return render(request,'UserRegisteration.html',{})
    return render(request,"UserRegisteration.html", {})

def Login(request):
    if request.method == "POST":
        C_name = request.POST['U_name']
        C_password = request.POST['U_pwds']
        if UserDetails.objects.filter(Username=C_name, Password=C_password).exists():
            user = UserDetails.objects.all().filter(Username=C_name, Password=C_password)
            messages.info(request, 'logged in')
            request.session['UserId'] = user[0].id
            request.session['type_id'] = 'User'
            request.session['UserType'] = C_name
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            messages.info(request, 'Please Register')
            return redirect("/UserRegisteration")
    else:
        return render(request,'Login.html',{})
    return render(request,'Login.html',{})
    return render(request, "Login.html", {})

def AdminLogin(request):
    if request.method == "POST":
        A_username = request.POST['A_name']
        A_password = request.POST['A_pwds']
        if admindata.objects.filter(Username = A_username,Password = A_password).exists():
            ad = admindata.objects.get(Username=A_username, Password=A_password)
            print('d')
            #messages.info(request,'Your login is Sucessfull')
            request.session['type_id'] = 'Admin'
            request.session['UserType'] = 'Admin'
            request.session['login'] = "Yes"
            return redirect("/")
        else:
            print('y')
            messages.error(request, 'Error wrong username/password')
            return render(request, "Adminlogin.html", {})
    else:
        return render(request, "Adminlogin.html", {})
  

def Predict(request):
    if request.method == "POST":
        MovieName = request.POST.get('MovieName')
        print(MovieName)
        MovieActor = request.POST.get('Actor')
        print(MovieActor)
        MovieActress = request.POST.get('Actress')
        print(MovieActress)
        MovieDirector = request.POST.get('Director')
        print(MovieDirector)
        MovieProducer = request.POST.get('Producer')
        print(MovieProducer)
        MovieMusic = request.POST.get('Music')
        print(MovieMusic)
        MarketBudget = request.POST.get('Budget')
        print(MarketBudget)
        MovieWriter = request.POST.get('Writer')
        print(MovieWriter)
        MovieDate = request.POST.get('Dates')
        Dates = MovieDate.split('-')
        Day = Dates[2]
        Year = Dates[0]
        MovieGenre = request.POST.get('Genre')
        print(MovieGenre)
        count = MovieData.objects.all().count()
        print(count)
        HIT = MovieData.objects.all().filter(SuccessStatus="HIT").count()
        print("HIT",HIT)
        FLOP = MovieData.objects.all().filter(SuccessStatus="FLOP").count()
        print("FLOP",FLOP)
        SUPERHIT = MovieData.objects.all().filter(SuccessStatus="SUPERHIT").count()
        print("SUPERHIT",SUPERHIT)

        print(count)


        if count > 0:
            Packages = MovieData.objects.all()
            ArrName = [] 
            ArrActor  = []
            ArrActress = []
            ArrDirector = []
            ArrProducer = []
            ArrMusic  = []
            ArrBudget = []
            ArrResult = []
            ArrWriter = []
            ArrGenre = []
            ArrDay = []
            ArrYear = []

            #ArrDate = []

            '''MovieName = format(MovieName)
            MovieActor = format(MovieActor)
            MovieActress = format(MovieActress)
            MovieDirector = format(MovieDirector)
            MovieProducer = format(MovieProducer)
            MovieMusic = format(MovieMusic)
            MarketBudget = format(MarketBudget)
            MovieWriter = format(MovieWriter)
            MovieGenre = format(MovieGenre)

            print('MovieName',MovieName)
            print('MovieActor',MovieActor)
            print('MovieActress',MovieActress)
            print('MovieDirector',MovieDirector)
            print('MovieProducer',MovieProducer)
            print('MovieMusic',MovieMusic)
            print('MarketBudget',MarketBudget)
            print('MovieWriter',MovieWriter)'''

            for line in Packages:
                ArrName.append(format(line.MovieName))
                ArrActor.append(format(line.MovieActor))
                ArrActress.append(format(line.MovieActress))
                ArrDirector.append(format(line.MovieDirector))
                ArrProducer.append(format(line.MovieProducer))
                ArrMusic.append(format(line.MovieMusic))
                ArrBudget.append(format(line.MarketBudget))
                ArrWriter.append(format(line.MovieWriter))
                ArrResult.append(format(line.SuccessStatus))
                ArrGenre.append(format(line.MovieGenre))
                ArrDay.append(format(line.Day))
                ArrYear.append(format(line.Year))


          

            le = preprocessing.LabelEncoder()
            print(ArrResult)
            '''MovieName_encoded=le.fit_transform(ArrName)
            last_MovieName = MovieName_encoded[-1]
            MovieName_encoded = MovieName_encoded[:-1]
            print(MovieName_encoded)'''

            '''MovieActor_encoded=le.fit_transform(ArrActor)
            last_MovieActor = MovieActor_encoded[-1]
            MovieActor_encoded = MovieActor_encoded[:-1]
            print(MovieActor_encoded)

            MovieActress_encoded=le.fit_transform(ArrActress)
            last_MovieActress = MovieActress_encoded[-1]
            MovieActress_encoded = MovieActress_encoded[:-1]
            print(MovieActress_encoded)


            MovieDirector_encoded=le.fit_transform(ArrDirector)
            last_MovieDirector = MovieDirector_encoded[-1]
            MovieDirector_encoded = MovieDirector_encoded[:-1]
            print(MovieDirector_encoded)

            MovieProducer_encoded=le.fit_transform(ArrProducer)
            last_MovieProducer = MovieProducer_encoded[-1]
            MovieProducer_encoded = MovieProducer_encoded[:-1]
            print(MovieProducer_encoded)

            MovieMusic_encoded=le.fit_transform(ArrMusic)
            last_MovieMusic = MovieMusic_encoded[-1]
            MovieMusic_encoded = MovieMusic_encoded[:-1]
            print(MovieMusic_encoded)

            MarketBudget_encoded=le.fit_transform(ArrBudget)
            last_MarketBudget = MarketBudget_encoded[-1]
            MarketBudget_encoded = MarketBudget_encoded[:-1]
            print(MarketBudget_encoded)


            MovieWriter_encoded=le.fit_transform(ArrWriter)
            last_MovieWriter = MovieWriter_encoded[-1]
            MovieWriter_encoded = MovieWriter_encoded[:-1]
            print(MovieWriter_encoded)'''


            MovieActor_encoded=ArrActor
            MovieActress_encoded=ArrActress
            MovieDirector_encoded=ArrDirector
            MovieProducer_encoded=ArrProducer
            MovieMusic_encoded=ArrMusic
            MarketBudget_encoded=ArrBudget
            MovieWriter_encoded=ArrWriter
            MovieGenre_encoded=ArrGenre
            MovieDay_encoded=ArrDay
            MovieYear_encoded=ArrYear
            


            temp1 = list(zip(MovieActor_encoded,MovieActress_encoded,MovieDirector_encoded,MovieProducer_encoded,MovieMusic_encoded,MarketBudget_encoded,MovieWriter_encoded,MovieGenre_encoded,MovieDay_encoded,MovieYear_encoded))
            model = LogisticRegression(multi_class='multinomial', solver='newton-cg')
            #print(model)
            model.fit(temp1, ArrResult)
            #LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(temp1, ArrResult)
            #score = model.evaluate(temp1,ArrResult)
            #print(score)

            predicted= model.predict([[int(MovieActor),int(MovieActress),int(MovieDirector),int(MovieProducer),int(MovieMusic),int(MarketBudget),int(MovieWriter),int(MovieGenre),int(Day),int(Year)]])
            print("Result :",predicted)
            answer = predicted
            print("before",answer)
            answer = str(answer)[1:-1]
            print("answer",answer)
            #answer = int(float(answer))
            #print(answer)
            sentence = MovieName +' '  + 'will be a' +' '+ answer +' '+ 'film'
            print(sentence)

              

        #register = TrainingData(Bedroomes = Bedroomes,BuiltupArea = BuiltupArea,Furnished = Furnished,Parking = Parking,WaterTiming = WaterTiming,Swimmingpool = Swimmingpool,Security =Security,Club =Club,Playarea   = Playarea,Fire = Fire,Gas =Gas,Lift = Lift,StationDistance =StationDistance,SchoolDistance= SchoolDistance,Result =Value,City = City)
        #register.save()

        data = {
        'respond': sentence
        }
        return JsonResponse(data)







        return redirect('/Login')
    else:
        return render(request, "Predict.html", {})







def AddTrainingData(request):
    if request.method == "POST":
        MovieName = request.POST['M_name']
        MovieProducer = request.POST['M_Producer']
        MovieDirector = request.POST['M_Director']
        MovieActor = request.POST['M_actor']
        MovieActress = request.POST['M_actress']
        MovieMusic = request.POST['M_Mdirector']
        MarketBudget = request.POST['M_budget']
        Date = request.POST['M_date']
        Dates = Date.split('-')
        Day = Dates[2]
        Year = Dates[0]
        print(Day + Year)

        SuccessStatus = request.POST['M_success']
        MovieWriter = request.POST['M_Writer']
        MovieGenre = request.POST['M_genre']
        data = MovieData(MovieName=MovieName.upper(),MovieProducer=MovieProducer,MovieDirector=MovieDirector,MovieActor=MovieActor,MovieActress=MovieActress,MovieMusic=MovieMusic,MarketBudget=MarketBudget,SuccessStatus=SuccessStatus,MovieWriter = MovieWriter,MovieGenre = MovieGenre,Day = Day,Year = Year)
        data.save()
        messages.info(request,'Data Added Successfully')
        return redirect('/AddTrainingData')
    else:
        return render(request,'AddTrainingData.html',{})

def Logout(request):
    Session.objects.all().delete()
    return redirect("/")


    



#https://ieeexplore.ieee.org/document/9596138/figures#figures