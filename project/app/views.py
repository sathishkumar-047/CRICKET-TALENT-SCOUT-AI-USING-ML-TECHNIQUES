from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Players
from .forms import Players_information_form
import numpy as np
import joblib
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import UserPredictModel

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np

from tensorflow import keras
from PIL import Image, ImageOps
from . import forms

from sklearn.metrics import precision_recall_curve
from django.shortcuts import render
from django.core.mail import EmailMessage
from . models import UserPredictModel

def landing_page(request):
    return render(request, 'app/1_landingpage.html')

@login_required(login_url='userlogin')
def index(request):
    return render(request, 'app/3_index.html')

@login_required(login_url='userlogin')
def problem_statement(request):
    return render(request, 'app/info_sport.html')


# This is personal information form submission
@login_required(login_url='userlogin')
def player_information(request):
    
    if request.method == 'POST':
        print('Data is valid')
        form = Players_information_form(request.POST, request.FILES)
        if form.is_valid():
            print('Personal form is valid')
            form.save()
            return redirect('player_dashboard')
    else:
        form = Players_information_form()      
    return render(request, 'app/5_personal_information.html', {'form':form})

@login_required(login_url='userlogin')
def team(request):
    return render(request, 'app/6_team.html')

@login_required(login_url='userlogin')
def sport_shot_database(request):
    models = UserPredictModel.objects.all()
    return render(request, 'app/sport_shot_database.html', {'models': models})



def sport_shot_model(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserPredictModel.objects.latest('id')
        models = keras.models.load_model('D:/ITPDL12-FINAL/ITPDL12-FINAL CODING/Deploy/project/app/sport_shot.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("D:/ITPDL12-FINAL/ITPDL12-FINAL CODING/Deploy/project/media/images/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['Address_for_golf','Drive_for_cricket','Finish_for_golf','Impact_for_golf','legglance_flick_for_cricket', 'Mid-Backswing_for_golf', 'Mid-Downswing_for_golf', 'Mid-Follow-Through_for_golf', 'pullshot_for_cricket', 'sweep_for_cricket', 'Toe-up_for_cricket', 'Top_for_golf']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'Address_for_golf':
            print(a)
            a = 'Address_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Drive_for_cricket':
            print(a)
            a = 'Drive_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Finish_for_golf':
            print(a)
            a = 'Finish_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Impact_for_golf':
            print(a)
            a = 'Impact_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'legglance_flick_for_cricket':
            print(a)
            a = 'legglance_flick_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Mid-Backswing_for_golf':
            print(a)
            a = 'Mid-Backswing_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Mid-Downswing_for_golf':
            print(a)
            a = 'Mid-Downswing_for_golf'
            b = 'Shot represent in Golf sports'

        elif a == 'Mid-Follow-Through_for_golf':
            print(a)
            a = 'Mid-Follow-Through_for_golf.'
            b = 'Shot represent in Golf sports'
        
        elif a == 'pullshot_for_cricket':
            print(a)
            a = 'pullshot_for_cricket'
            b = 'Shot represent in Cricket sports'
        
        elif a == 'sweep_for_cricket':
            print(a)
            a = 'sweep_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Toe-up_for_cricket':
            print(a)
            a = 'Toe-up_for_cricket'
            b = 'Shot represent in Cricket sports'

        elif a == 'Top_for_golf':
            print(a)
            a = 'Top_for_golf'
            b = 'Shot represent in Golf sports'
       
        data = UserPredictModel.objects.latest('id')
        data.label = a
        data.save()

        
        return render(request, 'app/sport_shot_output.html',{'form':form,'obj':obj,'predict':a,'des':b})
    else:
        form = forms.UserPredictForm()
    return render(request, 'app/sports_shot_model.html',{'form':form})



@login_required(login_url='Authorlogin')
def player_dashboard(request):
    users = Players.objects.all()
    context = {
        'users': users,
        }
    return render(request, 'app/player_database.html', context)


@login_required(login_url='Authorlogin')
def player_database(request):
    users = Players.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'auth/3_Database.html', context)



Model1 = joblib.load('app/player_performences12.pkl')  
# players performence
from . forms import  UserRegisterForm,Patient_info_Form,Patient_info_Form1
def Deploy_9(request):
    if request.method == 'POST':
        form = Patient_info_Form(request.POST)
        if form.is_valid():
            # Extract cleaned data from form
            Country = form.cleaned_data['Country']
            CapStatus = form.cleaned_data['CapStatus']
            Innings = form.cleaned_data['Innings']
            Runs = form.cleaned_data['Runs']
            Balls = form.cleaned_data['Balls']
            Average = form.cleaned_data['Average']
            SR = form.cleaned_data['SR']
            Fifites = form.cleaned_data['Fifites']
            hundreds = form.cleaned_data['hundreds']
            Fours = form.cleaned_data['Fours']
            Sixes = form.cleaned_data['Sixes']
            Notout = form.cleaned_data['Notout']
            PlayerRole = form.cleaned_data['PlayerRole']
            
            
            # Prepare features for prediction
            features = np.array([[ Country, CapStatus, Innings, Runs, Balls, Average, SR, Fifites, hundreds, Fours, Sixes ,Notout ,PlayerRole]])
        
            print(features)   
            # Predict using the loaded model
            prediction = Model1.predict(features)
            prediction = prediction[0]
            print(prediction)   
    
            
            if prediction == 0:
                a="High Perfomence"
            elif prediction == 1:
                a="Average Perfomence"
            elif prediction == 2:
                a="Low Perfomence"
    
            
            # Save data to database
            instance = form.save(commit=False)
            instance.Class = a
            instance.save()
            
            # Render output page with prediction result
            return render(request, 'players/5_Teamates.html', {'prediction_text': a})
    else:
        form = Patient_info_Form()
    
    return render(request, 'players/9_Deploy.html', {'form': form})


from .models import Patient_info

def players_DB(request):
    patients = Patient_info.objects.all()
    return render(request, 'players/players_DB.html', {'patients': patients})


#batman acution model
Model = joblib.load('app/batsman_auction.pkl')  

def Batsman(request):
    if request.method == 'POST':
        form = Patient_info_Form1(request.POST)
        if form.is_valid():
            specialism_value = request.POST.get('Specialism')
            a = None
            # Extract cleaned data from form
            Specialism = form.cleaned_data['Specialism']
            Innings = form.cleaned_data['Innings']
            Avg = form.cleaned_data['Avg']
            SR = form.cleaned_data['SR']
            Fifties = form.cleaned_data['Fifties']
            Hundreds = form.cleaned_data['Hundreds']
            Fours = form.cleaned_data['Fours']
            Sixes = form.cleaned_data['Sixes']
            Runs = form.cleaned_data['Runs']
            Balls = form.cleaned_data['Balls']
            NotOuts = form.cleaned_data['NotOuts']

            
            
            # Prepare features for prediction
            features = np.array([[ Specialism, Innings, Avg, SR, Fifties, Hundreds, Fours, Sixes, Runs, Balls , NotOuts]])
        
            print(features)   
            # Predict using the loaded model
            prediction1 = Model.predict(features)
            prediction1 = prediction1[0]
            print(prediction1)   
    
            
            if prediction1 == 1:
                a="unsold"
               
            elif prediction1 == 0:
                a="sold"
               
       
    
            
            # Save data to database
            instance = form.save(commit=False)
            instance.Class = a
            instance.save()
              # Map numeric value to readable label
            specialism_label = {
                '0': 'ALL-ROUNDER',
                '1': 'BATSMAN',
                '2': 'WICKETKEEPER'
            }.get(specialism_value, 'Unknown Specialism')
            
            # Render output page with prediction result
            return render(request, 'players/batsman_output.html', {'prediction_text1': a ,'Specialism':specialism_label})
    else:
        form = Patient_info_Form1()
    
    return render(request, 'players/Batsman_input.html', {'form': form })

from . models import Patient_info1

def batsmans_DB(request):
    patients = Patient_info1.objects.all()
    return render(request, 'players/batsman_DB.html', {'patients': patients})


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render

# Load data once at the top (global for this file)
df = pd.read_csv("app/batsmen.csv")

def analy(request):
    # Unique dropdown values
    firstnames = df['FirstName'].unique()
    specialisms = df['Specialism'].unique()
    reserves = df['Reserve'].unique()

    # Get selections from request
    selected_firstname = request.GET.get('firstname')
    selected_specialism = request.GET.get('specialism')
    selected_reserve = request.GET.get('reserve')

    chart = None

    if selected_firstname and selected_specialism and selected_reserve:
        # Filter DataFrame based on selected values
        filtered_df = df[
            (df['FirstName'] == selected_firstname) &
            (df['Specialism'] == selected_specialism) &
            (df['Reserve'] == selected_reserve)
        ]

        if not filtered_df.empty:
            plt.figure(figsize=(10, 5))

            # Create melted DataFrame to plot 'Runs', 'Hundreds', and 'Balls' in one barplot
            melt_df = filtered_df.melt(id_vars=['Innings'], value_vars=['Runs','SR','Balls','Sixes','Fours'],
                                       var_name='Metric', value_name='Value')

            sns.barplot(data=melt_df, x='Innings', y='Value', hue='Metric')

            plt.title(f"Performance of {selected_firstname} ({selected_specialism}, {selected_reserve})")
            plt.xlabel("Innings")
            plt.ylabel("Value")
            plt.legend(title="Metric")

            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            chart = base64.b64encode(image_png).decode('utf-8')
            plt.close()

    return render(request, 'app/an.html', {
        'firstnames': firstnames,
        'specialisms': specialisms,
        'reserves': reserves,
        'selected_firstname': selected_firstname,
        'selected_specialism': selected_specialism,
        'selected_reserve': selected_reserve,
        'chart': chart,
    })
