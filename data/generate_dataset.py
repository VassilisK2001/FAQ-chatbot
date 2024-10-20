import random
import json

# Sample data for questions and answers
customer_support_email = "support@audiotours.com"
customer_support_phone = "+1-800-555-0199"

# Categories and their corresponding questions and answers
product_questions = [
    ("What audio tours do you offer?", "We offer a variety of audio tours for historical monuments worldwide, including the Colosseum, Eiffel Tower, and more."),
    ("Can I purchase audio tours individually?", "Yes, you can purchase audio tours individually or as a package."),
    ("Are the audio tours available in multiple languages?", "Yes, our audio tours are available in several languages including English, Spanish, French, and German."),
    ("What is the duration of the audio tours?", "The duration varies by tour, but most are between 1 to 2 hours long."),
    ("Do you provide headphones with the audio tours?", "No, we recommend using your own headphones for the best experience."),
    ("Are the audio tours suitable for children?", "Yes, our tours are designed to be engaging and educational for all ages."),
    ("Can I access the audio tours offline?", "Yes, once downloaded, you can access the audio tours offline."),
    ("How do I redeem a purchased audio tour?", "You can redeem your purchased audio tour in the app by entering your code or accessing it from your account."),
    ("Is there a trial available for the audio tours?", "Currently, we do not offer trials, but you can preview some content in our app."),
    ("Are there discounts for group purchases?", "Yes, we offer discounts for groups of 10 or more."),
    ("Do you offer gift cards for audio tours?", "Yes, we offer gift cards that can be purchased on our website."),
    ("What is included in the price of an audio tour?", "The price includes the audio files and any associated maps or guides."),
    ("Can I download the audio tours to my device?", "Yes, you can download the audio tours to your device for offline use."),
    ("Are there any special promotions for audio tours?", "We often have promotions during holidays and special events. Check our website for current offers."),
    ("How can I find the audio tours for specific monuments?", "You can search for specific monuments using our app or website."),
    ("Do your audio tours include maps?", "Yes, most of our audio tours come with interactive maps to help you navigate."),
    ("Are the audio tours narrated by professionals?", "Yes, all our audio tours are narrated by experienced professionals."),
    ("Can I share the audio tour with someone else?", "Audio tours are tied to your account and cannot be shared, but you can recommend them."),
    ("What devices are compatible with your audio tours?", "Our audio tours are compatible with most smartphones, tablets, and computers."),
    ("Are there any age restrictions for audio tours?", "No, there are no age restrictions, but parental guidance is recommended for younger children."),
    ("How do I upgrade to a premium audio tour?", "You can upgrade to a premium audio tour in the app by selecting the desired tour and paying the difference."),
]

app_questions = [
    ("Is the mobile app available for both Android and iOS?", "Yes, our app is available on both platforms for download."),
    ("How do I download the audio tours app?", "You can download the app from the Google Play Store or Apple App Store."),
    ("Can I create an account on the mobile app?", "Yes, you can easily create an account within the app."),
    ("How do I log in to my account on the app?", "Open the app and enter your credentials on the login page."),
    ("What should I do if the app crashes?", "If the app crashes, try restarting your device or reinstalling the app."),
    ("How can I provide feedback about the app?", "You can provide feedback through the feedback section in the app or email us directly at {}.".format(customer_support_email)),
    ("Is there a desktop version of the audio tours app?", "Currently, we only offer a mobile app; however, you can access audio tours via our website."),
    ("How do I change my account settings in the app?", "Go to the settings section in the app to update your account information."),
    ("Can I sync my purchases between the app and website?", "Yes, your purchases will sync across the app and website if you use the same account."),
    ("How do I receive updates for the mobile app?", "Updates are automatically available in the app store, or you can enable notifications in the app settings."),
    ("What should I do if I forget my app password?", "Use the 'Forgot Password' option on the login screen to reset it."),
    ("Is there a help section in the app?", "Yes, there's a help section accessible from the main menu of the app."),
    ("Can I listen to audio tours directly in the app?", "Absolutely! All audio tours can be played directly from the app."),
    ("How do I contact support through the app?", "You can contact support through the 'Help' section in the app or by calling {}.".format(customer_support_phone)),
    ("Does the app work without an internet connection?", "Yes, once downloaded, the audio tours can be accessed offline."),
    ("How can I report bugs in the app?", "You can report bugs through the feedback section or by emailing our support team at {}.".format(customer_support_email)),
    ("Can I customize my audio tour preferences in the app?", "Yes, you can customize your preferences in the settings section of the app."),
    ("What is the app's return policy?", "Our return policy allows for refunds within 14 days of purchase."),
    ("Does the app have user-generated content?", "No, currently our app does not support user-generated content."),
    ("How do I view my purchase history in the app?", "Your purchase history can be viewed in your account settings."),
]

app_complaints = [
    ("The app keeps crashing on my device.", "We're sorry for the inconvenience. Please try updating the app or reinstalling it. If the issue persists, contact us at {}.".format(customer_support_email)),
    ("I can't log into my account on the mobile app.", "Please check your credentials and ensure you're using the correct login method."),
    ("The app is running very slowly.", "We apologize for the slow performance. Please check your internet connection and try again."),
    ("I'm not receiving notifications from the app.", "Ensure that notifications are enabled in your device settings."),
    ("The audio quality in the app is poor.", "We're sorry to hear that. Please check your device's audio settings."),
    ("The app is not syncing with my purchases.", "Please log out and back into your account to refresh your purchases."),
    ("I can't find the audio tours I purchased in the app.", "Please check your library in the app for purchased tours."),
    ("The app keeps freezing during playback.", "We apologize for this issue. Try restarting the app or your device."),
    ("I can't update the app on my device.", "Please ensure you have enough storage space and try again."),
    ("I have issues with payment processing in the app.", "If you're having payment issues, please contact our support team for assistance at {}.".format(customer_support_email)),
    ("The app does not support my device.", "Please check the app's compatibility requirements on our website."),
    ("I received an error message while using the app.", "Please take note of the error message and contact support for help."),
    ("The app layout is confusing.", "We appreciate your feedback! Please let us know how we can improve the layout."),
    ("The app is not displaying the correct language.", "You can change the language in the settings menu of the app."),
    ("The map feature in the app is not working.", "We apologize for the inconvenience. Please ensure location services are enabled."),
    ("The app does not load my favorites.", "Please check if you're logged into your account to view favorites."),
    ("The search function in the app is not effective.", "Thank you for your feedback. We're continuously working to improve our search functionality."),
    ("I want to remove ads from the app.", "Currently, we do not offer an ad-free version of the app."),
    ("The app does not provide enough information about the tours.", "Thank you for your input! We will consider adding more detailed descriptions."),
    ("I can't change my profile picture in the app.", "Please check if you're following the correct steps in the settings menu."),
    ("The app is not allowing me to share my tours.", "Sharing features are not available currently, but we appreciate your suggestion."),
]

audio_tour_complaints = [
    ("I didn't receive the audio tour after purchase.", "We're sorry for the inconvenience. Please check your email for the download link. If you don't see it, contact us at {}.".format(customer_support_email)),
    ("The audio tour I received is not the one I ordered.", "We apologize for this mix-up. Please contact support at {} for a resolution.".format(customer_support_email)),
    ("I would like a refund for my audio tour purchase.", "We can help you with that. Please refer to our refund policy and contact support at {}.".format(customer_support_email)),
    ("The audio tour is incomplete.", "We apologize for the inconvenience. Please let us know which tour you're having issues with, and contact us at {}.".format(customer_support_email)),
    ("I'm having trouble accessing the audio tour I bought.", "Please ensure you are logged into the correct account. If the issue persists, contact support at {}.".format(customer_support_email)),
    ("The audio tour is not compatible with my device.", "Please check our website for compatibility requirements or contact support."),
    ("I want to change my audio tour selection after purchase.", "Unfortunately, changes cannot be made after purchase, but please contact support for assistance."),
    ("The audio tour format is not what I expected.", "Please let us know what you were expecting, and we can assist you."),
    ("I can't pause or resume my audio tour.", "Try checking your app settings or restarting the app."),
    ("The audio tour is missing key information.", "We appreciate your feedback! Please let us know which tour needs improvement."),
    ("I want to report a problem with the audio tour content.", "Thank you for letting us know. Please provide details, and we will investigate."),
    ("I'm unable to share the audio tour with a friend.", "Currently, sharing features are not available, but we appreciate your suggestion."),
    ("The audio tour did not match the description on the website.", "We apologize for the discrepancy. Please contact support to address this issue."),
    ("I want to receive updates on new audio tours.", "You can sign up for our newsletter on our website to receive updates."),
    ("I found an error in the audio tour content.", "Thank you for reporting this! We will correct any inaccuracies as soon as possible."),
    ("How do I get a refund for an unused audio tour?", "Please refer to our refund policy and contact support for further assistance."),
    ("The audio tour does not include all the stops mentioned.", "We apologize for any omissions. Please check your tour details, and let us know if there's an issue."),
]

# Generate 100 questions and answers
faq_pairs = []

# Ensuring that each category contributes equally to the dataset
while len(faq_pairs) < 100:
    # Randomly select one question and answer from each category
    for questions, answers in [
        (product_questions, "product"),
        (app_questions, "app"),
        (app_complaints, "app_complaint"),
        (audio_tour_complaints, "audio_tour_complaint")
    ]:
        # Sample one question and its answer
        question, answer = random.choice(questions)
        faq_pairs.append({
            "question": question,
            "answer": answer
        })

# Shuffle the dataset
random.shuffle(faq_pairs)

# Write the dataset to a JSON file
with open("faq_dataset.json", "w") as f:
    json.dump(faq_pairs, f, indent=4)

print("Generated FAQ dataset with 100 question-answer pairs in 'faq_dataset.json'")
