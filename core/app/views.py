# -*- encoding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import PostForm,OBDForm,CarForm
from .models import Post,PostOBD,PostCar
from django.shortcuts import render, redirect
from django.contrib import messages
from collections import OrderedDict
from .import fusioncharts

@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PostForm()
    return render(request,'site-register.html',{'form':form})
def show(request):
    posts = Post.objects.order_by('-id');
    return render(request,"configurations.html",{'posts':posts})
def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request,'edit-site-register.html', {'post':post})
def update(request, id):
    post = Post.objects.get(id=id)
    # form = OBDForm(request.POST, instance = post)
    # if form.is_valid():
    #     form.save()
    #     return redirect("/show")
    # return render(request, 'edit-site-register.html', {'post': post})
    if request.method == "POST" :
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            # After the operation was Update
            messages.success(request, 'Update successful!')
            # redirect to some other page
            return redirect("/show")
        # After the operation was fail
        message = 'Something we are wrong!'
        return render(request, 'edit-site-register.html',{'message':message,'post':form})
def destroy(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/show")

def newOBD(request):
    if request.method == "POST":
        form = OBDForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showOBD')
            except:
                pass
    else:
        form = OBDForm()
    return render(request,'OBD-register.html',{'form':form})
def showOBD(request):
    posts = PostOBD.objects.order_by('-id');
    return render(request,"OBD_configurations.html",{'posts':posts})
def editOBD(request, id):
    post = PostOBD.objects.get(id=id)
    return render(request,'OBD_edit_register.html', {'post':post})
def updateOBD(request, id):
    post = PostOBD.objects.get(id=id)
    form = OBDForm(request.POST, instance = post)
    if form.is_valid():
        form.save()
        return redirect("/showOBD")
    return render(request, 'OBD_edit_register.html', {'post':form})
def destroyOBD(request, id):
    post = PostOBD.objects.get(id=id)
    post.delete()
    return redirect("/showOBD")

def newCar(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showCar')
            except:
                pass
    else:
        form = CarForm()
    return render(request,'car_asset_register.html',{'form':form})

def showCar(request):
    posts = PostCar.objects.order_by('-id')
    return render(request,"car_asset_configurations.html",{'posts':posts})
def editCar(request, id):
    post = PostCar.objects.get(id=id)
    return render(request,'car_asset_edit_register.html', {'post':post})
def updateCar(request, id):
    post = PostCar.objects.get(id=id)
    form = CarForm(request.POST, instance = post)
    if form.is_valid():
        form.save()
        return redirect("/showCar")
    return render(request, 'car_asset_edit_register.html', {'post':form})
def destroyCar(request, id):
    post = PostCar.objects.get(id=id)
    post.delete()
    return redirect("/showCar")


def chart(request):
    # Create an object for the angualar gauge using the FusionCharts class constructor
    angularGauge = fusioncharts.FusionCharts("angulargauge", "ex1", "450", "270", "chart-1", "json",
                                # The data is passed as a string in the `dataSource` as parameter.
                                """{  
                                    "chart": {
                                        "caption": "OBD RPM Value",
                                        "lowerLimit": "0",
                                        "upperLimit": "4000",
                                        "showValue": "1",
                                        "numberSuffix": " RPM",
                                        "theme": "fusion",
                                        "showToolTip": "0"
                                    },
                                    "colorRange": {
                                        "color": [{
                                            "minValue": "0",
                                            "maxValue": "500",
                                            "code": "#F2726F"
                                        }, {
                                            "minValue": "50",
                                            "maxValue": "750",
                                            "code": "#FFC533"
                                        }, {
                                            "minValue": "75",
                                            "maxValue": "1000",
                                            "code": "#62B58F"
                                        }]
                                    },
                                    "dials": {
                                        "dial": [{
                                            "value": "1600"
                                        }]
                                    }
                                }""")
    # Alternatively, you can assign this string to a string variable in a separate JSON file
    # and pass the URL of that file to the `dataSource` parameter.
    return render(request, 'dashboard.html', {'output': angularGauge.render(), 'chartTitle': 'RPM'})

def MapView(request):
    return render(request,"map.html")