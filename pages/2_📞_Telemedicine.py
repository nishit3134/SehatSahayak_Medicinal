import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyperclip  # Import pyperclip for clipboard operations

# Define a Streamlit title and description
st.title("🧑‍⚕️Consult a Doctor (beta)")
st.write("Elevate your healthcare experience with our app. Effortlessly book online appointments with doctors, bringing expert medical advice directly to you, anytime you need it.")

# Get user input for email address and password
mail_address = st.text_input("Enter your Gmail email address :")
password = st.text_input("Enter your password:", type="password")

# Create date and time input widgets for the meeting
meeting_date = st.date_input("Select meeting date :")
meeting_time = st.time_input("Select meeting time :")

# Initialize a variable to store the meeting link
meeting_link = ""

# Create a button to start the automation
if st.button("Schedule a meet"):
    # Create chrome instance
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    driver = webdriver.Chrome(options=opt)

    try:
        # Login to Google account
        st.write("Logging in...")
        driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
        driver.find_element(By.ID, "identifierId").send_keys(mail_address)
        driver.find_element(By.ID, "identifierNext").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        time.sleep(2)
        driver.find_element(By.ID, "passwordNext").click()
        time.sleep(2)
        driver.get('https://google.com/')
        time.sleep(2)

        # Go to Google Meet
        st.write("Opening Google Meet...")
        driver.get('https://meet.google.com/xby-zehb-ncf')
        time.sleep(5)

        # Ask to join the meeting if required
        try:
            ask_to_join_button_xpath = '//*[@id="yDmH0d"]/div[9]/div[3]/div[2]/div/div[3]/div/span/span'
            driver.find_element(By.XPATH, ask_to_join_button_xpath).click()
        except:
            pass

        # Get the current URL (Google Meet link)
        meeting_link = driver.current_url

        # Close the Chrome instance when finished
     #   driver.quit()
        st.write("Meeting automation completed.")
        
        # Set the meeting link
        #meeting_link = current_url  # Use the current URL

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Display the meeting link
if meeting_link:
    st.text("Meeting Link (copyable): " + meeting_link)
    
    # Create a button to copy the link to clipboard
    copy_button = st.button("Copy Link to Clipboard")
    if copy_button:
        pyperclip.copy("https://meet.google.com/xby-zehb-ncf?pli=1")
        st.write("Link Copied to Clipboard!")