import unittest
import os
import csv
import data_loader

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) # set absolute path to .py

class TestDataLoader(unittest.TestCase):
    def test_check_numeric_string_is_num(self):
        self.assertTrue(data_loader.is_num('10.0'), '"10.0" is a num')

    def test_check_non_numeric_string_is_not_num(self):
        self.assertFalse(data_loader.is_num('s'), '"s" is not a num')
    
    def write_temp_csv(self, filepath: str, data: list) -> None:
        with open(filepath, 'w') as fake_csv:
            fake_writer = csv.writer(fake_csv)
            fake_writer.writerows(data)

    def test_load_artists_csv(self):
        data = [
            ['Artist','Genres','Songs','Popularity','Link'],
            ['$uicideboy$','Rap; Hip Hop','300','5.0','/suicideboys/']
        ]
        file_path = os.path.join(CURRENT_FILE_PATH, './temp.csv')
        self.write_temp_csv(file_path, data)      
        result = [{'name': '$uicideboy$', 'genres': ['Rap', 'Hip Hop'], 'songs': 300, 'popularity': 5.0, 'link': '/suicideboys/'}]
        self.assertEqual(data_loader.load_csv(file_path)[1], result, 'Artists csv is not loading correctly')
        os.remove(file_path)

    def test_load_lyrics_csv(self):
        data = [
            ['ALink','SName','SLink','Lyric','language'],
            ['/suicideboys/','Center Core Never More','/center-core-never-more/','''You did good, $lick
It's a smash
(Smoke that pound, 'nother pound)
(Smoke that pound, 'nother)
(Smoke that pound, 'nother pound)
(Takin' a sip from the)
(Smoke that pound, 'nother pound)
(Smoke that pound, 'nother)
Diamonds hit like Pop Rocks, we got too hot, lightin' blunts with lava
We don't do the drama, but the Oscars where I'm posted at
Grammys on my neck, shoot for the stars, I swear to God on that
I'ma need you to stand on that, I'm tryna tap in with your almanac
Wavy homies hated, I got demons in my basement
Nigga might piss me off, I'ma lay his ass down on the pavement
Dreads swangin', smokin' Jamaican, lookin' for all my payments
Paper chasin', Haitian, move the chains like fourth and inches
(Bad shit), I'm here to slay 'em
All this lean, bitch, I can't feel my body (yeah, yeah)
All these pills, bitch, I can't feel my body (yeah, yeah)
Ain't no love in my heart, I don't feel nobody (ah)
Keep it to myself, I might lose it, can't catch a body
White dove, fly high, throw my threes up in the sky
Throw my threes around my eyes and then I call it my disguise
Masked off, I'm just out here with a raw face
Ask me how I been and I draw blanks
Hold tight 'til my claws break
Full metal jacket kinda heavy (heavy)
At the bottom of the fuckin' lake, I parked my Chevy
(Yeah) waiting to die but I wasn't born ready (nah)
Shaking up my life, I'm just tryna hold steady
Birds of a feather flock together (yeah)
Grey the fucking gang, ain't no one could do it better (Grey)
Two odd numbers right behind the fucking letter
Me, $lick and Germ our alliance is forever
I just popped a pill (pill), pull up with the deal (deal)
Pistol whip a pussy, have 'em looping on the reel (reel)
Wood-grain wheel (wheel), chromed out rims (rim)
Million dollar deals, sign my name as "H-I-M" (wetto)
Tales from the North (North), back from the dead
Hard to feel for a pussy when these thorns in my hand (Northside)
Two story grave (grave), trauma on my wrists (wrist)
Three fingers high, other three in my bitch (bitch)
I got problems that won't go away (guess who?)
Don't understand 'cause I been hitting pay (yeah)
Lord, I pray that my bitch gay (I just want a threesome)
New opps but my clique Grey (Grey)''','en']
        ]
        file_path = os.path.join(CURRENT_FILE_PATH, './temp.csv')
        self.write_temp_csv(file_path, data)      
        result = [{'artist_link': '/suicideboys/', 'song_name': 'Center Core Never More', 'song_link': '/center-core-never-more/', 'lyric': 'You did good, $lick\nIt\'s a smash\n(Smoke that pound, \'nother pound)\n(Smoke that pound, \'nother)\n(Smoke that pound, \'nother pound)\n(Takin\' a sip from the)\n(Smoke that pound, \'nother pound)\n(Smoke that pound, \'nother)\nDiamonds hit like Pop Rocks, we got too hot, lightin\' blunts with lava\nWe don\'t do the drama, but the Oscars where I\'m posted at\nGrammys on my neck, shoot for the stars, I swear to God on that\nI\'ma need you to stand on that, I\'m tryna tap in with your almanac\nWavy homies hated, I got demons in my basement\nNigga might piss me off, I\'ma lay his ass down on the pavement\nDreads swangin\', smokin\' Jamaican, lookin\' for all my payments\nPaper chasin\', Haitian, move the chains like fourth and inches\n(Bad shit), I\'m here to slay \'em\nAll this lean, bitch, I can\'t feel my body (yeah, yeah)\nAll these pills, bitch, I can\'t feel my body (yeah, yeah)\nAin\'t no love in my heart, I don\'t feel nobody (ah)\nKeep it to myself, I might lose it, can\'t catch a body\nWhite dove, fly high, throw my threes up in the sky\nThrow my threes around my eyes and then I call it my disguise\nMasked off, I\'m just out here with a raw face\nAsk me how I been and I draw blanks\nHold tight \'til my claws break\nFull metal jacket kinda heavy (heavy)\nAt the bottom of the fuckin\' lake, I parked my Chevy\n(Yeah) waiting to die but I wasn\'t born ready (nah)\nShaking up my life, I\'m just tryna hold steady\nBirds of a feather flock together (yeah)\nGrey the fucking gang, ain\'t no one could do it better (Grey)\nTwo odd numbers right behind the fucking letter\nMe, $lick and Germ our alliance is forever\nI just popped a pill (pill), pull up with the deal (deal)\nPistol whip a pussy, have \'em looping on the reel (reel)\nWood-grain wheel (wheel), chromed out rims (rim)\nMillion dollar deals, sign my name as "H-I-M" (wetto)\nTales from the North (North), back from the dead\nHard to feel for a pussy when these thorns in my hand (Northside)\nTwo story grave (grave), trauma on my wrists (wrist)\nThree fingers high, other three in my bitch (bitch)\nI got problems that won\'t go away (guess who?)\nDon\'t understand \'cause I been hitting pay (yeah)\nLord, I pray that my bitch gay (I just want a threesome)\nNew opps but my clique Grey (Grey)', 'language': 'en'}]
        self.assertEqual(data_loader.load_csv(file_path)[1], result, 'Lyrics csv is not loading correctly')
        os.remove(file_path)

    def test_link_lyrics_with_artists(self):
        lyrics = [{'artist_link': '/ivete-sangalo/', 'song_name': 'Arerê', 'song_link': '/ivete-sangalo/arere.html', 'lyric': 'Tudo o que eu quero nessa vida,\nToda vida, é\nÉ amar você\nAmar você\n\nO seu amor é como uma chama acesa\nQueima de prazer\nDe prazer\n\nEu já falei com Deus que não vou te deixar\nVou te levar pra onde for\nQualquer lugar\nJá fiz de tudo pra não te perder\n\nArerê,\nUm lobby, um hobby, um love com você\nArerê,\nUm lobby, um hobby, um love com você\n\nCai, cai, cai, cai, cai pra cá\nHey, hey, hey\nTu-do,tu-do, vai rolar', 'language': 'pt'},
                 {'artist_link': '/ivete-sangalo/', 'song_name': 'Se Eu Não Te Amasse Tanto Assim', 'song_link': '/ivete-sangalo/se-eu-nao-te-amasse-tanto-assim.html', 'lyric': 'Meu coração\nSem direção\nVoando só por voar\nSem saber onde chegar\nSonhando em te encontrar\nE as estrelas\nQue hoje eu descobri\nNo seu olhar\nAs estrelas vão me guiar\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração\n\nHoje eu sei\nEu te amei\nNo vento de um temporal\nMas fui mais\nMuito além\nDo tempo do vendaval\nNos desejos\nNum beijo\nQue eu jamais provei igual\nE as estrelas dão um sinal\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração...', 'language': 'pt'}]
        artists = [{'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}]
        result = [{'artist_link': '/ivete-sangalo/', 'song_name': 'Arerê', 'song_link': '/ivete-sangalo/arere.html', 'lyric': 'Tudo o que eu quero nessa vida,\nToda vida, é\nÉ amar você\nAmar você\n\nO seu amor é como uma chama acesa\nQueima de prazer\nDe prazer\n\nEu já falei com Deus que não vou te deixar\nVou te levar pra onde for\nQualquer lugar\nJá fiz de tudo pra não te perder\n\nArerê,\nUm lobby, um hobby, um love com você\nArerê,\nUm lobby, um hobby, um love com você\n\nCai, cai, cai, cai, cai pra cá\nHey, hey, hey\nTu-do,tu-do, vai rolar', 'language': 'pt', 'artist': {'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}},
                 {'artist_link': '/ivete-sangalo/', 'song_name': 'Se Eu Não Te Amasse Tanto Assim', 'song_link': '/ivete-sangalo/se-eu-nao-te-amasse-tanto-assim.html', 'lyric': 'Meu coração\nSem direção\nVoando só por voar\nSem saber onde chegar\nSonhando em te encontrar\nE as estrelas\nQue hoje eu descobri\nNo seu olhar\nAs estrelas vão me guiar\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração\n\nHoje eu sei\nEu te amei\nNo vento de um temporal\nMas fui mais\nMuito além\nDo tempo do vendaval\nNos desejos\nNum beijo\nQue eu jamais provei igual\nE as estrelas dão um sinal\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração...', 'language': 'pt', 'artist': {'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}}]
        self.assertEqual(data_loader.link_lyrics_with_artists(lyrics, artists), result, 'Wrong link of the data')    

unittest.main()