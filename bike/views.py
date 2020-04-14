from django.shortcuts import render, redirect, get_object_or_404
from .models import AccidentPoint
from django.contrib.auth.forms import UserCreationForm
from .models import Hospital
from .models import Streetlight
from .models import MapQueries
from .models import PolyAccidentProximity
from .models import PolyHospitalProximity
from .models import Poly_Streetlight_Proximity
from .forms import MapQueryForm
from django.views.generic import TemplateView, ListView


def hello_maps(request):
    accidents = AccidentPoint.objects.all()
    hospitals = Hospital.objects.all()
    streetlights = Streetlight.objects.all()

    print("before post")
    if request.method == 'POST':
        print("in post if loop")
        form = MapQueryForm(request.POST)
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

            nearby_accident_arr = request.POST.get("nearby_accidents").split()
            nearby_hospital_arr = request.POST.get("nearby_hospitals").split()
            nearby_streetlights_arr = request.POST.get("nearby_streetlights").split()

            try:
                new_map_query.save()
                print('query saved')

            except:
                print("query not saved")

            for accident_id in nearby_accident_arr:
                new_accident_proximity = PolyAccidentProximity()
                new_accident_proximity.query = new_map_query
                accident = AccidentPoint.objects.get(pk=accident_id)
                new_accident_proximity.accident = accident

                try:
                    new_accident_proximity.save()
                    print('accident proximity saved')
                except:
                    print('accident proximity not saved')

            for hospital_id in nearby_hospital_arr:
                new_hospital_proximity = PolyHospitalProximity()
                new_hospital_proximity.query = new_map_query
                hospital = Hospital.objects.get(pk=hospital_id)
                new_hospital_proximity.hospital = hospital

                try:
                    new_hospital_proximity.save()
                    print('hospital proximity saved')
                except:
                    print('hospital proximity not saved')

            for streetlight_id in nearby_streetlights_arr:
                new_streetlight_proximity = Poly_Streetlight_Proximity()
                new_streetlight_proximity.query = new_map_query
                streetlight = Streetlight.objects.get(pk=streetlight_id)
                new_streetlight_proximity.streetlight = streetlight

                try:
                    new_streetlight_proximity.save()
                    print('streetlight proximity saved')
                except:
                    print('streetlight proximity not saved')
        else:
            print("form not valid")
    else:
        print('not a post request')
        form = MapQueryForm()

    return render(request, 'index.html', {'accidents': accidents,
                                          'hospitals': hospitals,
                                          'streetlights': streetlights,
                                          'form': form})


def login(request):
    form = UserCreationForm()
    return render(request, 'login.html', {"form": form})


def get_queries(request, id):
    query = MapQueries.objects.filter(author_id=id)
    return render(request, 'users/queries.html', {'query': query})

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
