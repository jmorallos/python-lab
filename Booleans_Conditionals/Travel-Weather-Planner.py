distance_mi = 2
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = True

short_distance = distance_mi < 1
medium_distance = 1 < distance_mi <= 6
long_distance = distance_mi > 6

if short_distance:
    if not is_raining:
        print(True)
    else:
        print(False)
elif medium_distance:
    if not is_raining and has_bike:
        print(True)
    else:
        print(False)
elif long_distance:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
else:
    print(False)
