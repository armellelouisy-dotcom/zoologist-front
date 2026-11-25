import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)



"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""

#location = st.radio('Select a location', ('Biscoe', 'Dream', 'Torgersen'))
location = st.radio('Location:', ['Biscoe','Dream','Torgersen'])
#st.write(location)

bill_length = st.number_input('bill length (in mm)')
bill_depth = st.number_input('bill depth (in mm)')
flipper_length = st.number_input('flipper length (in mm)')
body_mass = st.number_input('Body mass (in g)')
sex = st.radio('Sex:', ['Male','Female'])



"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""

API_URL = 'https://zoo-api-29674705916.europe-west1.run.app/predict'

params = {
    "island": location,
    "bill_length_mm": bill_length,
    "bill_depth_mm": bill_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "sex": sex,
}


response = requests.get(API_URL, params=params)
#st.title(response.json())  # => {wait: 64}


result = response.json()
species = result.get("prediction")

st.header(f"Mon pingouin est un {species} !")
