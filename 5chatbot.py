# Restaurant ChatBot (Console Version)

def get_response(msg):
    msg = msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Welcome to Customer Bites! How can I assist you today?"
    elif "menu" in msg or "food" in msg or "dishes" in msg:
        return "We offer Indian, Chinese, and Italian cuisines. Would you like to see our veg or non-veg options?"
    elif "veg" in msg:
        return "Our popular veg dishes include Paneer Butter Masala, Veg Biryani, and Veg Manchurian."
    elif "non-veg" in msg or "nonveg" in msg:
        return "Our best non-veg options are Chicken Biryani, Butter Chicken, and Fish Curry."
    elif "hours" in msg or "timing" in msg or "open" in msg:
        return "We are open from 10 AM to 11 PM, all days of the week."
    elif "book" in msg or "reserve" in msg or "reservation" in msg:
        return "You can reserve a table by calling +919632587415-FOOD or booking through our website."
    elif "delivery" in msg or "home delivery" in msg:
        return "Yes, we deliver within a 10 km radius. You can order online or via food delivery apps."
    elif "location" in msg or "address" in msg:
        return "We are located at 123 Flavor Street, Food City."
    elif "price" in msg or "cost" in msg or "rate" in msg:
        return "Our dishes range from Rs200 to Rs970. Let me know if you want specific pricing."
    elif "bye" in msg or "goodbye" in msg:
        return "Thank you for visiting Customer Bites. Have a delicious day!"
    else:
        return "I'm sorry, could you please clarify your request?"

# Chat Loop
print(" Welcome to Customer Bites ChatBot! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break
