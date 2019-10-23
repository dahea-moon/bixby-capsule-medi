from math import cos, pi


def Bound(langt, longt):
    lat_change = 20 / 111.2
    lng_change = abs(cos(langt * (pi/180)))
    result = {
        "langt_min": langt - lat_change,
        "longt_min": longt - lng_change,
        "langt_max": langt + lat_change,
        "longt_max": longt + lng_change,
    }
    return result
