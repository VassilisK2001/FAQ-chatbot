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

# New scenarios
payment_issues = [
    "I’m having trouble completing my payment, what should I do?",
    "Can I use PayPal for my purchase?",
    "My credit card was declined when I tried to buy a ticket.",
    "Is it safe to enter my credit card information on your site?"
]

group_booking = [
    "Do you offer discounts for group bookings?",
    "Can I book tickets for a family of six?",
    "Is there a special rate for educational tours for schools?",
]

account_questions = [
    "How can I reset my password?",
    "I forgot my account details. What should I do?",
    "How can I update my personal information?",
    "Is there a way to delete my account?"
]

# Complaints
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

# Example 1: Product-related questions (with rephrasing)
for i in range(1, 3000):
    monument = random.choice(monuments)
    faq_dataset.append({
        "id": i,
        "question": f"Is it possible to buy an audio tour for the {monument} on the WorldAudioTours website?",
        "answer": f"Yes, you can purchase an audio tour for the {monument} along with your ticket through our webpage or app. Visit www.worldaudiotours.com or contact us at {support_email} for assistance."
    })

# Example 2: App issue-related questions (with rephrasing)
for i in range(3001, 5000):
    issue = random.choice(app_issues)
    faq_dataset.append({
        "id": i,
        "question": f"How can I resolve the issue of my iPhone app freezing?",
        "answer": f"We’re sorry for the trouble. Please make sure that your app is updated to the latest version. If the problem persists, feel free to reach out to us at {support_email} or call us at {support_phone} for further assistance."
    })

# Example 3: New payment issues
for i in range(5001, 6000):
    issue = random.choice(payment_issues)
    faq_dataset.append({
        "id": i,
        "question": issue,
        "answer": f"Please ensure your payment information is correct. If you're still having trouble, contact our support at {support_email} or call {support_phone}."
    })

# Example 4: Group booking questions
for i in range(6001, 7000):
    group_question = random.choice(group_booking)
    faq_dataset.append({
        "id": i,
        "question": group_question,
        "answer": f"Yes, we offer group discounts! Please contact us at {support_email} for more information."
    })

# Example 5: User account questions
for i in range(7001, 8000):
    account_question = random.choice(account_questions)
    faq_dataset.append({
        "id": i,
        "question": account_question,
        "answer": f"To reset your password, visit the 'Forgot Password' section on our login page, or reach out to support at {support_email}."
    })

# Example 6: Complaints and refund requests
for i in range(8001, 9000):
    monument = random.choice(monuments)
    complaint = random.choice(complaints).format(monument=monument)
    refund_response = random.choice(refund_responses).format(monument=monument)
    faq_dataset.append({
        "id": i,
        "question": f"{complaint}",
        "answer": f"{refund_response} If you need further assistance, you can also reach us at {support_phone}."
    })

# Example 7: Booking platform-related questions
platforms = ["Booking.com", "GetYourGuide", "Viator", "Expedia"]
for i in range(9001, 10000):
    platform = random.choice(platforms)
    monument = random.choice(monuments)
    faq_dataset.append({
        "id": i,
        "question": f"I made a purchase via {platform} for a tour of the {monument}, but I didn’t receive the confirmation email.",
        "answer": f"We apologize for the issue. Please check your spam or junk mail folder. If you still cannot find it, contact us at bookings@worldaudiotours.com or call {support_phone}, and we'll be happy to resend your confirmation or offer a refund."
    })

# Shuffle the dataset
random.shuffle(faq_dataset)

# Export the shuffled dataset to a JSON file
try:
    with open("shuffled_faq_dataset.json", "w") as json_file:
        json.dump(faq_dataset, json_file, indent=4)
    print("Shuffled dataset created successfully! Check the file shuffled_faq_dataset.json.")
except Exception as e:
    print(f"An error occurred: {e}")
