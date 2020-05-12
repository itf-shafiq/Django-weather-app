from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    zipcode = request.POST.get('search')
    r = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + str(zipcode) + '&distance=25&API_KEY=5FF06660-FD29-41D4-8980-3664904731E0')
    json_data = json.loads(r.content)

    if request.method == "POST":

        if json_data[0]['Category']['Name'] == "Good":
            category_description = "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif json_data[0]['Category']['Name'] == "Moderate":
            category_description =  "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif json_data[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif json_data[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif json_data[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif json_data[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous"
            
        return render(request, 'index.html',{
            'data': json_data,
            'category_description': category_description,
            'category_color': category_color


        })

    else:
        r = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=5FF06660-FD29-41D4-8980-3664904731E0')
        json_data = json.loads(r.content)
        if json_data[0]['Category']['Name'] == "Good":
            category_description = "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"

        elif json_data[0]['Category']['Name'] == "Moderate":
            category_description =  "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif json_data[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "usg"
        elif json_data[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif json_data[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif json_data[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous"
            
        return render(request, 'index.html',{
            'data': json_data,
            'category_description': category_description,
            'category_color': category_color


        })
        
    

def about(request):
    return render(request, 'about.html')