import streamlit as st
from src.core.planner import TravelPlanner

st.set_page_config(page_title="Travel Itinerary Planner", page_icon=":airplane:", layout="centered")
st.title("AI Travel Itinerary Planner")
st.write("Plan your perfect day trip with the help of AI! Enter your destination city and interests to get a personalized itinerary.")

with st.form("itinerary_form"):
    city = st.text_input("Destination City", placeholder="e.g., Paris")
    interests = st.text_input("Your Interests (comma separated)", placeholder="e.g., art, food, history")
    submit_button = st.form_submit_button(label="Generate Itinerary")

    if submit_button:
        planner = TravelPlanner()

        if not city or not interests:
            st.warning("Please provide both destination city and your interests in that destination.")

        try:
            planner.set_city(city)
            planner.set_interests(interests)
            planner.create_itinerary()
            st.subheader("📄 Your Personalized Itinerary")
            st.markdown(planner.itinerary)
        except Exception as e:
            st.error(f"An error occurred: {e}")