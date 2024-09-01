import pywhatkit as kit
import time
import pyautogui
import keyboard as k

# List of phone numbers
phone_numbers = [
    "+201068807406",
    "+201061642252",
    "+201116836112", 
]

# Message to send
message = (
    "- استني عندك وكفايه scroll علي الفيس والانستجرام😠\n\n"
    "بتدور علي فرصه انك تتعلم وتطور من نفسك بس كلو بمبالغ صعبه؟💸😔\n\n"
    "طب استعد عشان تتحدي نفسك وتكتشف مهاراتك🔥💪🏻\n\n"
    "سمعت عن إيڤينت Ai catalyst؟\n\n"
    "تعالي اكلمك عنو شويه🤩\n"
    "جايبين احسن اسبيكرز ف🔥 ( Ai, data science, cybersecurity, web development, iot )\n\n"
    "- هو event يوم اه بس هتعرف معلومات هتتعلمها ف سنين 🫱🏻‍🫲🏻\n"
    "- يوم حافل بنشاطات وفاعليات وworkshops كتير جداا\n"
    "- عندك فرصه تقابل ناس خبيره ف المجال وتعرف منهم اكتر 🤩\n"
    "- كمان هتتعرف علي ناس ف سنك واكبر منك واصغر منك وتزود دايره معارفك\n"
    "ده غير كتير وكتير  بس هنسيبك تتفاجئ يومها 🫣🤩\n"
    "طبعا مستنيني اقولك الحق احجز تذكرتك من هنا وتخش تتفاجئ بأسعار تخض\n\n"
    "-بس اعذرني هصدمك واقولك انو for free🔥\n\n"
    "كل المطلوب منك تقدم هنا 👇🏻\n"
    "https://forms.gle/qUjrYcjcAik5ihNW8\n\n"
    "مستنينك يوم الجمعه 23/8 في جامعه النيل من 9 الصبح\n\n"
    "📍Location : https://maps.app.goo.gl/Gvpscg1XRZMTEjKr8?g_st=iw\n\n"
    "يلا مستني اي الفرصه مبتجيش مرتين 🔥"
)

# Iterate over the list of phone numbers



for phone_number in phone_numbers:
    try:
        # Send the WhatsApp message instantly
        kit.sendwhatmsg_instantly(phone_number, message , 30 , True)
        
        # Wait a brief moment to ensure the WhatsApp window opens
        time.sleep(5)  # Increased to ensure the message is sent properly

        # Click to focus on the message input field
        pyautogui.click(1050, 950)
        time.sleep(1)  # Shortened time

        # Press 'Enter' to send the message
        k.press_and_release('enter')

        # Wait briefly before sending the next message
        time.sleep(10)  # Increased delay to avoid getting flagged

    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")

print("All messages sent!")
