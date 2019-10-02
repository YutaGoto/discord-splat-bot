import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$splat'):
        if message.content.endswith('$splat'):
            return

        command = message.content.split()[1]
        if command != 'gachi' and command != 'league':
            return

        url = 'https://spla2.yuu26.com/' + command + '/now'
        r = requests.get(url)
        splat_result = r.json()['result'][0]
        embed = discord.Embed(title=splat_result['rule'], description='〜'.join([splat_result['start'], splat_result['end']]))
        embed.set_thumbnail(url="https://www.nintendo.co.jp/switch/aab6a/sp/assets/images/footer_totop.png")
        embed.add_field(name=splat_result['maps_ex'][0]['name'], value='がんばれ', inline=True)
        embed.add_field(name=splat_result['maps_ex'][1]['name'], value='いかちゃん', inline=True)
        await message.channel.send(embed=embed)

client.run('Access token')
