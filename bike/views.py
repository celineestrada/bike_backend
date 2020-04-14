from django.shortcuts import render, redirect
from .models import AccidentPoint
from django.contrib.auth.forms import UserCreationForm
from .models import Hospital
from .models import Streetlight
from .models import MapQueries
from .models import PolyAccidentProximity
from .forms import MapQueryForm


def hello_maps(request):
    accidents = AccidentPoint.objects.all()
    hospitals = Hospital.objects.all()
    streetlights = Streetlight.objects.all()

    print("before post")
    if request.method == 'POST':
        print("in post if loop")
        form = MapQueryForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            print("form is valid")
            new_map_query = MapQueries()
            new_map_query.origin = request.POST.get("origin")
            new_map_query.origin_lat = request.POST.get("origin_lat")
            new_map_query.origin_lng = request.POST.get("origin_lng")
            new_map_query.destination = request.POST.get("destination")
            new_map_query.destination_lat = request.POST.get("destination_lat")
            new_map_query.destination_lng = request.POST.get("destination_lng")
            new_map_query.polyline = request.POST.get("polyline")
            new_map_query.score = request.POST.get("score")
            new_map_query.author = request.user

            try:
                new_map_query.save()
                print('query saved')

                for accident in accidents:
                    new_accident_proximity = PolyAccidentProximity()
                    new_accident_proximity.query = new_map_query
                    new_accident_proximity.accident = accident
                    #new_accident_proximity.difference = calculateDistance(accident, )

            except:
                print("query not saved")
            # To-do: change redirect!
    else:
        print("hit else")
        form = MapQueryForm()

    return render(request, 'index.html', {'accidents': accidents,
                                          'hospitals': hospitals,
                                          'streetlights': streetlights,
                                          'form': form})


def login(request):
    form = UserCreationForm()
    return render(request, 'login.html', {"form": form})

    # def register(request):
    #     if request.method == 'POST':
    #         form = UserRegisterForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             username = form.cleaned_data.get('username')
    #             messages.success(request, f'Your account has been created! You are now able to login!')
    #             return redirect('login')

# def show_markers(request):
#    accidents = AccidentPoint.objects.all()
#    return render(request, 'index.html', {'accidents': accidents})
