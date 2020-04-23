from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json

url = "https://covid19.mathdro.id/api"

response = requests.get(url).json()
 
res2 = requests.get("https://covid19.mathdro.id/api/countries").json()

res2 = res2.get('countries','')

countries = []

for i in res2:

    countries.append(i.get('name',''))
    

daily = requests.get("https://covid19.mathdro.id/api/daily").json()

con=[]
det=[]
date=[]

for i in daily:
    con.append(i.get('confirmed','').get ('total',''))
    det.append(i.get('deaths','').get('total',''))
    date.append(i.get('reportDate',''))

context ={

      'confirmedCases': response.get('confirmed','').get('value',''),
      'recoveredCases': response.get('recovered','').get('value',''),
      'deathCount': response.get('deaths','').get('value',''),
      'countries':countries,
      'confirmed': con,
      'deaths': det,
      'date': date,
      'bar': False
      
     }

def home(request):
    return render(request,'app/index.html',context)

def countryData(request):
    if request.method == 'POST':
         country = request.POST['dropdown']
         print(country)
         response = requests.get('https://covid19.mathdro.id/api/countries/' + country).json()
         print(response)
         res2 = requests.get("https://covid19.mathdro.id/api/countries").json()
         res2 = res2.get('countries','')
         countries = []
         for i in res2:
            countries.append (i.get("name",''))
         if country=='Nothing':
             return redirect('/')
         context = {
             'confirmedCases': response.get('confirmed','').get('value',''),
             'recoveredCases': response.get('recovered','').get('value',''),
             'deathCount': response.get('deaths','').get('value',''),
             'countries':countries, 
             'countryName':country, 
             'bar': True 

             
         }
            
         return render(request,'app/index.html',context)
    else:
        return redirect('/')
