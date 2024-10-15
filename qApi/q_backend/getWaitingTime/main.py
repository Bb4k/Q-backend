import populartimes
import requests


def get_average_time(data):
    sum_of_time = 0
    for time in data:
        sum_of_time += time
    return sum_of_time / 24


def get_popular_times(indexes):
    API_KEY = "AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk"
    results = []

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.71431500000001,"
        "-74.007766&radius=1&type=establishment,restaurant,food,"
        "point_of_interest&key=AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk")
    res = populartimes.get_id(API_KEY, response.json()["results"][3]["place_id"])["populartimes"]

    for i in range(0, len(res)):
        results.append(get_average_time(res[i]["data"]))

    output = []
    for i in indexes:
        output.append(results[i])

    return output


# 0 not busy
# 1 medium
# 2 busy
def get_status(input):
    output = []
    for i in input:
        if i <= 10:
            output.append(0)
        elif 10 < i < 15:
            output.append(1)
        else:
            output.append(2)
    return output


def get_average_waiting_time(indexes):
    API_KEY = "AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk"
    results = []

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.03182570008868,"
        "-114.03564931981444&radius=10000&type=establishment,restaurant,food,"
        "point_of_interest&key=AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk")
    results.append(populartimes.get_id(API_KEY, response.json()["results"][9]["place_id"])["time_spent"])
    results.append(populartimes.get_id(API_KEY, response.json()["results"][15]["place_id"])["time_spent"])

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.0304818,"
        "-114.0974779&key=AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk&radius=100000")

    results.append(populartimes.get_id(API_KEY, response.json()["results"][15]["place_id"])["time_spent"])

    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.7960398,"
        "-73.9873398&key=AIzaSyDgHoeyFbYmD7z70Dn8x5a-hSMsSd0KVBk&radius=1000000")

    results.append(populartimes.get_id(API_KEY, response.json()["results"][16]["place_id"])["time_spent"])

    output = []
    for i in indexes:
        output.append(results[i])

    return output


if __name__ == "__main__":
    print(get_status(get_popular_times([0, 1, 2, 3])))
    print(get_average_waiting_time([0, 1, 2, 3]))
