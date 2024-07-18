import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


st.markdown("""
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Calibri&display=swap');
			html, body, [class*="css"]  {
			font-family: 'Calibri', serif;
			}
			</style>""" ,unsafe_allow_html=True)


st.title("Hello")


name=st.text_input('Name', placeholder='Your Name')
age=st.number_input('Age',1,100,1)
st.header('Carbon Activity Tracker')

st.markdown("""---""")

# Sourced from greenspector.com https://greenspector.com/en/social-media-2021/ 
#one user/day: 165.6 gEqCO2
social=st.select_slider('Social Media Usage',['Active','Average','Negligible'])
if social=='Active':
    c_social=165.6
if social=='Average':
    c_social=165.6*0.60
if social=='Negligible':
    c_social=165.6*0.10
st.markdown("""---""")

#https://www.iea.org/commentaries/the-carbon-footprint-of-streaming-video-fact-checking-the-headlines
#https://news.mit.edu/2021/how-to-reduce-environmental-impact-next-virtual-meeting-0304#:~:text=One%20hour%20of%20streaming%20or,size%20of%20an%20iPad%20Mini.
#441g per hour, average is 2 hour for Netflix, 1 hour for Youtube, 30 mins for others.
video=st.select_slider('Streaming Videos Usage',['Active','Average (2 hours)','Negligible'])
if video=='Active':
    c_video=350*8
if video=='Average (2 hours)':
    c_video=350*3.5
if video=='Negligible':
    c_video=350*1

st.markdown("""---""")
#4. Sending selfie - 0.1g - https://www.inverse.com/article/4088-what-is-the-carbon-footprint-of-a-single-snapchat
photo=st.slider('Sharing Photography',0,20,1)
c_photo=0.1*photo
st.markdown("""---""")
#5. Streaming music
# https://expressiveaudio.com/blogs/audio-advent/audio-advent-day-1-the-environmental-impact-of-listening-to-music#:~:text=Research%20has%20shown%20that%20producing,and%20a%20CD%20requires%2058g.
# 58/5 = 13.6 per hour.
music=st.select_slider('Streaming Music Usage',['Active','Average (2.5 hours)','Negligible'])
if music=='Active':
    c_music=13.6*8
if music=='Average (2.5 hours)':
    c_music=13.6*3.5
if music=='Negligible':
    c_music=13.6*1
st.markdown("""---""")
#6. Virtual Meeting - 1000g - 1 hour
#https://news.mit.edu/2021/how-to-reduce-environmental-impact-next-virtual-meeting-0304#:~:text=One%20hour%20of%20streaming%20or,size%20of%20an%20iPad%20Mini.
meet=st.slider('Virtual Meetings in hour ',0,8,1)
c_meet=meet*160
st.markdown("""---""")
#7. Searches https://greenspector.com/en/search-engines/
search=st.slider('Estimate Searches',0,100,10,10)
c_search=int(0.178*search)
st.markdown("""---""")
#8. Using computer - 68.6g - 1 hour
# https://8billiontrees.com/carbon-offsets-credits/carbon-footprint-of-a-laptop/#:~:text=Carbon%20Footprint%20of%20Desktop%3A%20What,electricity%20consumed%20(Image18).
computer=st.slider('Computer Hours',0,24,1)
c_computer=int(68.6*computer)
st.markdown("""---""")
#9. Traveling -
# https://www.gov.uk/government/statistical-data-sets/energy-and-environment-data-tables-env#greenhouse-gas-emissions-env02 ENV0701 - https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1129875/env0701.ods
st.caption('Traveling')
miles=st.number_input('Kilometers',1,1000)
#	1. Car - 5244g - 23 miles
#	2. Bus - 2300g - 23 miles
#	3. Train - 1840g - 23 miles
type=st.select_slider('Type',['Walk/Cycle', 'Fuel Car','Electric Car','Bus','Railway'])
if type=='Walk/Cycle':
    c_travel=0
if type=='Fuel Car':
    c_travel= int((0.171 + 0.041) * miles)
if type=='Electric Car':
    c_travel=  int((0.066) * miles)
if type=='Bus': 
    c_travel= int((0.044 + 0.011) * miles)
if type=='Railway':
    c_travel=  int((0.057 + 0.014) * miles)
st.markdown("""---""")
#9. Coffee/Tea - 21g - 1 cup
#https://www.peacefuldumpling.com/coffee-vs-tea-carbon-footprint-of-your-daily-brew
cup=st.slider('Cups of Coffee/Tea',0,10,0,1)
c_cup=cup*21
st.markdown("""---""")
# https://shrinkthatfootprint.com/food-carbon-footprint-diet/
diet=st.select_slider('Diet Type',['Vegan', 'Vegetarian', 'No Beef', 'Average', 'Meat Lover'])
if diet=='Vegan':
    c_diet=4109
if diet=='Vegetarian':
    c_diet=4657
if diet=='No Beef':
    c_diet=5205
if diet=='Average':
    c_diet=6849
if diet=='Meat Lover':
    c_diet=9041
st.markdown("""---""")
c=c_social + c_cup + c_diet + c_travel +c_search + c_computer + c_meet + c_photo + c_music + c_video

#     agree = st.checkbox("I have filled out the information.")
#     now = datetime.now()
#     date = now.strftime("%d/%m/%Y")
#     if agree:
#         text2 = "\n\n\nSocial Media: {} hours with CO2e : {} grams\n\nStreaming: {} hours with CO2e : {} grams\n\nSending Selfie: {} photos with CO2e : {} grams\n\nMusic: {} hours with CO2e : {} grams\n\nMeeting: {} hours with CO2e : {} grams\n\nSearches: {} searches with CO2e : {} grams\n\nComputer: {} hours with CO2e : {} grams\n\nTraveling: {} km with {} vehicle type with CO2e : {} grams\n\n\n ".format(social,c_social,video,c_video,photo,c_photo,music,c_music,meet,c_meet,search,c_search,computer,c_computer,miles,type,c_travel)
#         text1 = '\nDaily Carbon Activity\n\nBy- {} \n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTotal Carbon Activity: {} grams'.format(name,c)
#         img_name = 'Output.png'
#         background= Image.open('./data/Background.jpg')
#         color = 'dark_blue'  # grey,light_blue,blue,orange,purple,yellow,green
#         font = 'data/font/Forum-Regular.ttf'
#         background = write_image(background, colors[color], text1, text2)
#         background.save(img_name)
        
#         if st.button('Submit'):
#             db.carbon.insert_many([{"name" : name, "age": age, "Social Media": c_social, "Streaming": c_video, "Sending Photos": c_photo, "Streaming Music": c_music, "Virtual Meetings": c_meet, "Google Searches": c_search, "Computer Hours": c_computer, "Traveling": c_travel, "Coffe/Tea Intake": c_cup, "Food Intake(Diet)": c_diet, "Total Carbon Footprint": c, "Date": date}])
#             with open("Output.png", "rb") as file:
#                 btn = st.download_button(
#                 label="Download Output",
#                 data=file,
#                 file_name="Output.png",
#                 mime="image/png"
#             )

# if nav=='Carbon Footprint Leaderboard':
#     data = pd.DataFrame(list(carbon.find()))
#     data.drop('_id', axis=1, inplace=True)
#     keyword=st.text_input('Name', placeholder='Your Name')
#     st.caption('Same as the name you entered for tracking activity')
#     df = data[data['name'].str.contains(keyword)]
#     df.sort_values(by=['Total Carbon Footprint'], inplace=True, ascending=False)
#     df.set_index('Date', inplace=True) 
#     st.dataframe(df[['name','age','Total Carbon Footprint']])
#     df.drop('Total Carbon Footprint', axis=1, inplace=True)
#     df.drop('age', axis=1, inplace=True)
#     st.pyplot(df.plot.bar(stacked=True).figure)

# if nav=='Carbon Footprint History':
#     st.write('Carbon Footprint History')
#     data = pd.DataFrame(list(carbon.find()))
#     data.drop('_id', axis=1, inplace=True)
#     data.sort_values(by=['Total Carbon Footprint'], inplace=True, ascending=False)
#     st.dataframe(data)



if st.button('Submit'):
    # Load the custom background image
    background_path = 'data/Carbon-Activity.png'  # Path to your background image
    background = Image.open(background_path)

    # Initialize the drawing context
    draw = ImageDraw.Draw(background)

    # Define the text and font
    text = "Hello, World!"
    text2 = "Huy"
    font_path = 'data/fonts/Montserrat-Regular.ttf'  # Path to a .ttf font file
    font_size = 100  # Increase the font size
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the position for the text
    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
    width, height = background.size
    x = (width - textwidth) / 2
    y = (height - textheight) / 2

    # Draw the text on the image
    draw.text((x, y-600), text, fill='black', font=font)
    draw.text((x, y-500), text, fill='black', font=font)
    draw.text((x, y-400), text, fill='black', font=font)
    draw.text((x, y-300), text, fill='black', font=font)
    draw.text((x, y-200), text, fill='black', font=font)
    draw.text((x, y-100), text, fill='black', font=font)
    draw.text((x, y), text, fill='black', font=font)
    # Save the image
    output_path = 'output_image.png'
    background.save(output_path)

    # Show the image
    background.show()