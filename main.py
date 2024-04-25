import telebot

# Conexión con nuestro BOT
TOKEN = '7091268048:AAFZli9Pe4671WBklpVfBtIBLw6mM-kjmCU'
bot = telebot.TeleBot(TOKEN)

# Mensajes para cada comando
mensaje_formulario = "Puedes completar el formulario para la próxima fecha en la Bombonera aquí: https://forms.gle/pJM2ZqXwoxrYjXqS6"

mensaje_info = """Hola! Soy Bot Entradas Boca Juniors y soy RE bostero como vos, soy el bot de entradas Boca Juniors! Voy a ayudarte a sacar plateas y palcos para ir a la cancha!

🔷 Nuestro equipo reserva entradas para partidos de Boca exclusivamente PARA SOCIOS (activos o adherentes) a través del Abono Solidario.

🔶 Me pedís y te mando un formulario para que nos pases tus datos de cuenta y contacto. Cuando comienza la venta de entradas, intentamos reservarte una platea según lo que completaste en el formulario. Te avisamos por WhatsApp cuando comenzamos a buscar y cuando conseguimos la reserva. Luego, podés pagar la entrada como si la hubieras reservado vos mismo.

🔷 Es fundamental que completen UN FORMULARIO POR ENTRADA REQUERIDA en lugar de avisarnos algo como "Necesito 2 entradas". Una vez confirmada la compra, tu carnet queda habilitado automáticamente para el ingreso al estadio. Los invitados deben retirar sus entradas con el carnet del socio y su DNI en la Bombonera el día del partido.

🔶 Nuestro servicio tiene un costo adicional de $6.000 por entrada para el Torneo Local, que se paga después de confirmar la compra de las plateas

🔷 No revendemos ni alquilamos carnets, solo ayudamos a los socios a obtener entradas.

🔶 Una vez concretada la compra de tu platea o de tu invitado nos envías el comprobante o por WhatsApp: 11-6300-5028 O por Instagram: entradasbocajrs_

🔷 Los precios estimados para marzo de 2024, además del costo de nuestro servicio, son los siguientes:
- 1ra bandeja/platea baja: $56.870 a $72.160
- 2da bandeja/platea media: $56.870 a $72.160
- 3ra bandeja/platea alta: $30.690 a $36.960
- Torres: $60.500 a $77.550
- Palcos: $54.000 a $87.000
- Plateas preferenciales: $129.910 en adelante
- El club cobra un adicional para las entradas de invitado, que arranca en $7.000 y aumenta dependiendo de la bandeja"""

mensaje_cvu = """El cvu correspondiente para realizar el pago es:
---
0000003100033473731173
---"""

# Creación de comandos
@bot.message_handler(commands=['start'])
def enviar_comandos(message):
    bot.reply_to(message, "Los comandos que entiendo son:\n"
                          "/formulario para pasarte el formulario de la próxima fecha en la bombonera\n"
                          "/info: para pasarte más información sobre nuestro servicio\n"
                          "/cvu: para pasarte el cvu correspondiente para la transferencia luego de comprar tu platea")

@bot.message_handler(commands=['formulario'])
def enviar_formulario(message):
    bot.reply_to(message, mensaje_formulario)

@bot.message_handler(commands=['info'])
def enviar_info(message):
    bot.reply_to(message, mensaje_info)

@bot.message_handler(commands=['cvu'])
def enviar_cvu(message):
    bot.reply_to(message, mensaje_cvu)

# Manejador de mensajes para responder a cualquier otro comando
@bot.message_handler(func=lambda m: True)
def handle_other(message):
    bot.reply_to(message, "Los comandos que entiendo son:\n"
                          "/formulario para pasarte el formulario de la próxima fecha en la bombonera\n"
                          "/info: para pasarte más información sobre nuestro servicio\n"
                          "/cvu: para pasarte el cvu correspondiente para la transferencia luego de comprar tu platea")
# Ejecutar el bot
if __name__ == "__main__": 
    bot.polling(none_stop=True)
