import random
import json

# Define some template data
monuments = [
    "Colosseum", "Eiffel Tower", "Great Wall of China", "Statue of Liberty",
    "Pyramids of Giza", "Louvre", "Sydney Opera House", "Taj Mahal",
    "Acropolis of Athens", "Tower of London"
]

app_issues = [
    "The app keeps freezing on my iPhone.",
    "The Android app is very slow when loading audio tours.",
    "The mobile app crashes whenever I try to make a booking.",
    "I can’t log in to my account on the desktop version."
]

complaints = [
    "I bought a ticket for {monument}, but I haven't received my audio tour.",
    "I bought the tour, but the audio guide for {monument} isn’t appearing in my account.",
    "I haven’t received any email confirmation after purchasing a ticket for {monument}.",
    "I would like a refund for the {monument} audio tour I didn’t receive."
]

refund_responses = [
    "We apologize for the inconvenience. If you haven't received your audio tour for {monument}, please check your spam folder. If it's still missing, we can resend it or process a full refund. Contact us at refunds@worldaudiotours.com.",
    "We sincerely apologize. Please check your junk mail for the confirmation of your {monument} tour. If you can't find it, contact us at refunds@worldaudiotours.com for a full refund or resending the audio guide."
]

# Define customer support details
support_email = "support@worldaudiotours.com"
support_phone = "+1-800-123-4567"

# Generate dataset
faq_dataset = []

# Example 1: Product-related questions
for i in range(1, 3000):
    monument = random.choice(monuments)
    faq_dataset.append({
        "id": i,
        "question": f"Can I purchase an audio tour for the {monument} through WorldAudioTours?",
        "answer": f"Yes, you can purchase an audio tour for the {monument} along with your ticket through our webpage or app. Visit www.worldaudiotours.com or contact us at {support_email} for assistance."
    })

# Example 2: App issue-related questions
for i in range(3001, 5000):
    issue = random.choice(app_issues)
    faq_dataset.append({
        "id": i,
        "question": f"{issue} What should I do?",
        "answer": f"We’re sorry for the trouble. Please make sure that your app is updated to the latest version. If the problem persists, feel free to reach out to us at {support_email} or call us at {support_phone} for further assistance."
    })

# Example 3: Complaints and refund requests
for i in range(5001, 8000):
    monument = random.choice(monuments)
    complaint = random.choice(complaints).format(monument=monument)
    refund_response = random.choice(refund_responses).format(monument=monument)
    faq_dataset.append({
        "id": i,
        "question": f"{complaint}",
        "answer": f"{refund_response} If you need further assistance, you can also reach us at {support_phone}."
    })

# Example 4: Booking platform-related questions
platforms = ["Booking.com", "GetYourGuide", "Viator", "Expedia"]
for i in range(8001, 10000):
    platform = random.choice(platforms)
    monument = random.choice(monuments)
    faq_dataset.append({
        "id": i,
        "question": f"I made a purchase via {platform} for a tour of the {monument}, but I didn’t receive the confirmation email.",
        "answer": f"We apologize for the issue. Please check your spam or junk mail folder. If you still cannot find it, contact us at bookings@worldaudiotours.com or call {support_phone}, and we'll be happy to resend your confirmation or offer a refund."
    })

# Export the generated data to a JSON file
try:
    with open("faq_dataset.json", "w") as json_file:
        json.dump(faq_dataset, json_file, indent=4)
    print("Dataset created successfully! Check the file faq_dataset.json.")
except Exception as e:
    print(f"An error occurred: {e}")
