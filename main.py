import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if message.content.lower() == "hola! que tipo de bot eres?":
        await message.channel.send(
            "Hola! Soy un bot que habla sobre los autos eléctricos y a gasolina conectado con el tema de contaminación."
        )

    if message.content.lower() == "explicame un poco sobre la comparacion entre estos dos tipos de autos":
        await message.channel.send(
            "Los autos eléctricos son más eficientes y no producen emisiones directas, lo que los hace más ecológicos. "
            "En cambio, los autos a gasolina tienen mayor autonomía y son más accesibles, pero generan contaminación y dependen de combustibles fósiles."
        )

    if message.content.lower() == "cuales son las principales marcas de cada tipo de autos?":
        tesla_image = "https://media.discordapp.net/attachments/1335328870559121521/1335328955623936121/file-AxXFyYLs7MRnGTwPgCMK8J.png?ex=679fc580&is=679e7400&hm=a3eb3a3beddd12409c20f95dac5758479116a30104891f3a1b9cff5f2695cd0b&=&format=webp&quality=lossless&width=702&height=702"
        byd_image = "https://cdn.discordapp.com/attachments/1335328870559121521/1335328962293006429/file-XhDgmjMBKonFb6SiVJyvDH.png?ex=679fc581&is=679e7401&hm=3a8f248c71c86e396260ddf2caa7f3792acbdb517c5a1cf42d75de387bdc8fde&"
        volkswagen_image = "https://media.discordapp.net/attachments/1335328870559121521/1335328979304845380/file-C44WXzLnYxCbkifsqtJUF8.png?ex=679fc585&is=679e7405&hm=e75f2de54d58023c3dd55f21ef6a99b9d7aa95d455efbf253adb8d98dc8b7ad6&=&format=webp&quality=lossless&width=1248&height=702"
        chevrolet_image = "https://cdn.discordapp.com/attachments/1335328870559121521/1335328988486434826/file-HNEvXm1RCrjkFWznBaXc3Z.png?ex=679fc588&is=679e7408&hm=05f183383ce2ca5f76d6662ccbf4f7502624cee8af55cf79a7a91fd8311ae8fa&"

        await message.channel.send(tesla_image)
        await message.channel.send(
            "Tesla, fundada en 2003, es pionera en el desarrollo de autos eléctricos de alta gama. "
            "Entre sus modelos más populares se encuentran el Model S, Model 3, Model X y Model Y, conocidos por su tecnología avanzada y autonomía superior."
        )

        await message.channel.send(byd_image)
        await message.channel.send(
            "BYD (Build Your Dreams), una compañía china fundada en 1995, es líder en vehículos eléctricos accesibles. "
            "Sus modelos como el BYD Dolphin y Tang EV son populares por su precio competitivo y eficiencia."
        )

        await message.channel.send(volkswagen_image)
        await message.channel.send(
            "Volkswagen, fundada en 1937 en Alemania, es una de las marcas más icónicas en autos a gasolina. "
            "Modelos como el Golf y el Passat han sido líderes en ventas globales durante décadas."
        )

        await message.channel.send(chevrolet_image)
        await message.channel.send(
            "Chevrolet, una marca estadounidense fundada en 1911, es conocida por sus autos robustos y confiables. "
            "Modelos como el Chevrolet Camaro y la Silverado han dejado una huella importante en la industria automotriz."
        )

    if message.content.lower() == "que ventajas y desventajas tiene cada tipo de auto?":
        tesla_charging_image = "https://media.discordapp.net/attachments/1335328870559121521/1335331501713395883/file-4HoN5UcQ3XNSFa5SfxaT5J.png?ex=679fc7df&is=679e765f&hm=b118f9b93dcb9dc82dbdd0a966171e80e3ef1b704edb41fe3d9897a9e13ad050&=&format=webp&quality=lossless&width=452&height=350"
        chevrolet_image = "https://media.discordapp.net/attachments/1335328870559121521/1335331513457184809/file-Sy5dDKGjuZYKkYgqT6jhz7.png?ex=679fc7e2&is=679e7662&hm=f55c328c735cb7e451b6ae5a35699254c70cee958409b353c2f8404aa62ee805&=&format=webp&quality=lossless"

        await message.channel.send(tesla_charging_image)
        await message.channel.send(
            "Esta imagen muestra un Tesla cargando en una estación de carga. Los autos eléctricos son silenciosos, "
            "no generan emisiones directas, y tienen costos operativos más bajos. Sin embargo, dependen de estaciones de carga "
            "y la autonomía es limitada en comparación con los autos a gasolina."
        )

        await message.channel.send(chevrolet_image)
        await message.channel.send(
            "Este es un auto a gasolina de Chevrolet. Los autos a gasolina son más accesibles, tienen mayor autonomía, "
            "y la infraestructura para repostar es ampliamente disponible. Sin embargo, generan emisiones contaminantes "
            "y tienen costos operativos más altos debido al precio del combustible."
        )

    if message.content.lower() == "gracias por tu ayuda!":
        await message.channel.send(
            "¡De nada! Espero haberte ayudado a entender un poco más sobre los autos eléctricos y a gasolina. "
            "Recuerda que tus elecciones pueden contribuir a reducir la contaminación del planeta. "
            "¡Hasta pronto!"
        )

    await bot.process_commands(message)

bot.run("MTMzNTMyMzA1ODA3MTkyODkxNQ.GLAHMK.tJQxd_wLSe1qajbKUhMPwoLcjcX-Ff4KfgjVGM")
