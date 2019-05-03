from django.shortcuts import render, redirect,loader
from django.http import HttpResponse
import sqlite3
from sqlite3 import Error
from django.urls import reverse

#class HomePageView(TemplateView):
  #  template_name = 'home.html'
    
#class AboutPageView(TemplateView):
    #template_name = 'about.html' 
    



def signIn(request):
 
   
 username= request.POST.get('username')
 password= request.POST.get('password')
 
 if username=="nqubeko":
  
  return redirect('/Clients/',)
 else:
  return HttpResponse(username)
  
  
  
  

#client Viewdef clients(request):
 
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 cur.execute("SELECT * FROM Client")
 
 rows = cur.fetchall()
 
 for row in rows:
  

  return render(request,  'Clients.html',{'email':rows}) 
 
 
#addclient View
def addClient(request):
 if request.method== 'POST':
  
  name= request.POST['clientName']
  contactPerson= request.POST['contactPerson']
  contactNumber= request.POST['contactNumber']
 
 
 
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "INSERT INTO Client (clientName, contactPerson, contactNumber)VALUES ('"+ name +"', '"+ contactPerson +"', '"+ contactNumber +"');"
 
 cur.execute(query)
 conn.commit()
 
 
  
 
 return HttpResponse(request, name)
  
 



#project View
def projects(request):
  
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 cur.execute("SELECT * FROM Project")
 
 rows = cur.fetchall()
 
 for row in rows:
  
 
  return render(request,  'Projects.html',{'email':rows})
 
#edit Client
def editClient(request):
 
 if request.method == 'POST':
  clientName= request.POST['clientName']
  contactPerson= request.POST['contactPerson']
  contactNumber= request.POST['contactNumber']
  
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "UPDATE Client SET clientName = '"+clientName+"', contactPerson = '"+contactPerson+"',contactNumber = '"+contactNumber+"' WHERE clientName='"+clientName+"' ;"
   
 cur.execute(query)

 
 conn.commit()
 return HttpResponse(request, clientName)

#delete Project
def deleteProject(request):
 
 if request.method == 'POST':
  projectName= request.POST['projectName']

  
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "DELETE FROM Project WHERE projectName='"+projectName+"' ;"
   
 cur.execute(query)

 
 conn.commit()
 return HttpResponse(request, projectName)

#delete Client
def deleteClient(request):
 
 if request.method == 'POST':
  clientName= request.POST['clientName']

  
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "DELETE FROM Client WHERE clientName='"+clientName+"' ;"
   
 cur.execute(query)

 
 conn.commit()
 return HttpResponse(request, clientName)

#edit Project
def editProject(request):
 
 if request.method == 'POST':
  projectName= request.POST['projectName']
  clientName= request.POST['clientName']
  status= request.POST['status']
  
  
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "UPDATE Project SET projectName = '"+projectName+"', clientName = '"+clientName+"',status = '"+status+"' WHERE projectName='"+projectName+"' ;"
   
 cur.execute(query)

 
 conn.commit()
 return HttpResponse(request, projectName)

 

#Home View
def homes(request):

 return render(request,  'home.html')


def addProject(request):
 if request.method== 'POST':
  
  projectName= request.POST['projectName']
  clientName= request.POST['clientName']
  status= request.POST['status']
 
 
 
 database = "db.sqlite3.db"
 
 print("connected")
 try:
  conn = sqlite3.connect(database)
  print("connected")
 
 except Error as e:
  print(e)    
 cur = conn.cursor()
 query = "INSERT INTO Project (projectName, clientName, status)VALUES ('"+ projectName+"', '"+ clientName+"', '"+ status +"');"
 
 cur.execute(query)
 conn.commit()
 
 
  
 
 return HttpResponse(request, projectName) 
 


 