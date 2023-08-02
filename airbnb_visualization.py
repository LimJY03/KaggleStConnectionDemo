import streamlit as st
import pydeck as pdk

coordinate_dict = {
    'Asheville': (35.5951, -82.5515),
    'Austin': (30.2711, -97.7437),
    'Boston': (42.3601, -71.0589),
    'Broward County': (26.1901, -80.3659),
    'Cambridge': (42.3736, -71.1097),
    'Chicago': (41.8781, -87.6298),
    'Clark County': (36.214, -115.013),
    'Columbus': (39.9623, -83.0007),
    'Denver': (39.7392, -104.9903),
    'Hawaii': (20.7984, -156.3319),
    'Jersey City': (40.7282, -74.0776),
    'Los Angeles': (34.0522, -118.2437),
    'Nashville': (36.1627, -86.7816),
    'New Orleans': (29.9511, -90.0715),
    'New York City': (40.7128, -74.006),
    'Oakland': (37.8044, -122.2711),
    'Pacific Grove': (36.6177, -121.9166),
    'Portland': (45.5202, -122.6742),
    'Rhode Island': (41.5801, -71.4774),
    'Salem': (42.5195, -70.8967),
    'San Clara Country': (37.3541, -121.9552),
    'Santa Cruz County': (37.0454, -121.957),
    'San Diego': (32.7157, -117.1611),
    'San Francisco': (37.7749, -122.4194),
    'San Mateo County': (37.4969, -122.3331),
    'Seattle': (47.6062, -122.3321),
    'Twin Cities MSA': (44.9778, -93.265),
    'Washington D.C.': (38.9072, -77.0379)
}

def show_3d_map(map_data) -> None:
    '''Display 3D Map'''

    col1, col2 = st.columns([1, 4])

    with col1:

        with st.form('airbnb_dist'):

            city = st.selectbox('Select a city', coordinate_dict.keys())
            room = []
            
            if st.checkbox('Shared Room', value=True): room.append('Shared room')
            if st.checkbox('Entire Home/Apt', value=True): room.append('Entire home/apt')
            if st.checkbox('Hotel Room', value=True): room.append('Hotel room')
            if st.checkbox('Private Room', value=True): room.append('Private room')
            
            st.form_submit_button('Display', use_container_width=True)

    coords = map_data[(map_data['city'] == city) & 
                      (map_data['room_type'].isin(room))][['latitude', 'longitude']]

    latitude, longitude = coordinate_dict[city]

    with col2:

        st.info('Height of bar represents the number of airbnb in that area')

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=latitude,
                longitude=longitude,
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=coords,
                    get_position='[longitude, latitude]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=coords,
                    get_position='[longitude, latitude]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
