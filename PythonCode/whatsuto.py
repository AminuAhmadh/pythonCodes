# Send automated message on whatsApp at specified time

import pywhatkit

# this will open whatsapp web and send the message to the number at specified time (hour, minute)
pywhatkit.sendwhatmsg('+234-Phone-number', 'Message you want to send here', 11,33)