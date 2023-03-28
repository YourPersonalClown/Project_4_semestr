import streamlit as st
import pandas as pd
import numpy as np
import streamlit_folium as sf
import folium
from DB_work import *

# pipreqs



st.set_page_config(page_title='ТЕСТ',page_icon=":bar_chart",layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# print(pd.DataFrame([55.7522, 37.6156], columns = ['lat', 'ln']))

START_COORDINATES = (52.2978, 104.296)

# with left_column:
#     ...
#     # st.map(pd.DataFrame(START_COORDINATES).T.rename(columns={0 : 'lat', 1 : 'lon'}))


# with right_column:
#     ...

# query = "SELECT * FROM test_table where Route = 0"

route_number = st.sidebar.number_input('Номер маршрута', min_value = 0, max_value = 9999, value = 0 if 'route_number' not in st.session_state else st.session_state.route_number)
route_type = st.sidebar.select_slider('Тип транспорта', ['Автобус', 'Трамвай', 'Троллейбус'], value = 'Автобус' if 'route_type' not in st.session_state else st.session_state.route_type)

if st.sidebar.button('Поиск', key = 'search_button_1'):
    st.session_state.update({  'route_type': route_type, 'route_number': route_number})

    DB_object = DB_ORM()

    way_got = DB_object.get_route(route_num = route_number, route_type_ = route_type)

    # st.write(way_got)


    if way_got:
        # st.write(way_got)

        # Создайте карту
        map = folium.Map(location=START_COORDINATES, zoom_start=12)


        for counter in range(len(way_got)):
            # print(line)
            line = way_got[counter]

            if counter == 0:
                folium.PolyLine(line).add_to(map)
                folium.Marker(line[0]).add_to(map)
                folium.Marker(line[-1]).add_to(map)
            
            elif counter == len(way_got) -1:            # Возможно, неверно
                folium.PolyLine(line).add_to(map)
                folium.Marker(line[0]).add_to(map)
                folium.Marker(line[-1]).add_to(map)

            else:
                folium.PolyLine(line).add_to(map)
                folium.Marker(line[-1]).add_to(map)

            

            


        # with open('K:\Downloads\Загрузки Яндекс\map.geojson', 'r') as temp:
        #     loaded = json.loads(temp.read())['features']

        # loaded = loaded[::-1]

        # for line in loaded:
        #     line = [points[::-1] for points in line['geometry']['coordinates']]

        #     folium.PolyLine(line).add_to(map)
        #     folium.Marker(line[0]).add_to(map)
        #     folium.Marker(line[-1]).add_to(map)



        # folium.PolyLine([point[::-1] for point in way_got['coordinates']]).add_to(map)

        # print(way_got['coordinates'])

        # # Нарисуйте точки на карте
        # for coord in coordinates:
        #     folium.Marker(coord).add_to(map)

        # Выведите карту на экран
        sf.folium_static(map)

        DB_object.connection_close()
    
    else:
        st.write("Выбранный маршрут не найден")

