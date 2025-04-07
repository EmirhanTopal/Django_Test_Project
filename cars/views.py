from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

cars_collections = {
    "nissan": "R34",
    "mercedes": "Cla200",
    "bmw": "M4 Coupe",
    "maserati": "Gran Tourismo",
    "toyota": "Supra",
    "porsche": "GT3 RS",
    "ferrari": None
}

def ft_default_cars_page(request):
    my_cars = list(cars_collections.keys()) #listenin key lerini al
    # for l_cars in my_cars:
    #     capitalize_l_cars = l_cars.capitalize()
    #     cars_path = reverse("all-cars", args=[l_cars])
    #     list_items += f"<li><a href=\"{cars_path}\">{capitalize_l_cars}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "cars/index.html", {
        "cars": my_cars
    })


def ft_general_cars_by_number(request, cars):
    cars_list = list(cars_collections.keys())
    if cars > len(cars_collections) or cars <= 0:
        return HttpResponseNotFound("Car is not founded and out of array")
    redirect_cars = cars_list[cars - 1]
    reverse_cars_url = reverse("all-cars", args=[redirect_cars])
    return HttpResponseRedirect(reverse_cars_url)

def ft_general_cars(request, cars):
    output_message = None
    #if cars == "nissan":
    #    output_message = "R34"  
    #elif cars == "Toyota":
    #    output_message = "Supra"
    #elif cars == "Mercedes":
    #    output_message = "Cla200"
    #elif cars == "Bmw":
    #    output_message = "M4 Coupe"
    #else:
    #    return HttpResponseNotFound("Car is not founded")
    try:
        output_message  = cars_collections[cars]
        return render(request, "cars/car.html", {
            "render_text": output_message,
            "render_title": "R34 Sevdalısı"
            })
        # response_data = f"<h1>{output_message}</h1>"
        # response_data = render_to_string("cars/car.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Car is not founded</h1>")