import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

st.title("📍➕Find Nearby Hospitals")
st.text(" ")
st.text(" ")

city = st.text_input('Enter your area name and city :')
place_type = st.selectbox("Select Place Type", ["Hospitals", "Clinics"])
radius = st.slider("Select Radius (in kilometers)", 1, 50, 10)

if st.button("Find Nearby Places"):
    def get_user_location():
        try:
            loc = Nominatim(user_agent='GetLoc')
            getLoc = loc.geocode(city)
            return getLoc.latitude, getLoc.longitude
        except:
            st.error("Error: Unable to detect your location.")
            return None, None

    lat, lon = get_user_location()

    if lat is not None and lon is not None:
        geolocator = Nominatim(user_agent="nearby_search")
        location = geolocator.reverse((lat, lon))
        st.write(f"\nYour current location: \n {location}\n")

        query = f"{place_type} near {lat}, {lon}"
        try:
            places = geolocator.geocode(query, exactly_one=False, limit=None)
            if places:
                st.write(f"\nNearby {place_type.lower()} are:\n")
                for place in places:
                    place_coords = (place.latitude, place.longitude)
                    place_distance = geodesic((lat, lon), place_coords).kilometers
                    if place_distance <= radius:
                        st.write(f"{place.address} ({place_distance:.2f} km)")
            else:
                st.warning(f"No nearby {place_type.lower()} found for the given type.")
        except:
            st.error("Error: Unable to fetch nearby places.")
