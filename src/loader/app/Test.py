import unittest
import data_loader

class Test(unittest.TestCase):
    def test_link_songs_with_artists(self):
        songs = [{'artist_link': '/ivete-sangalo/', 'song_name': 'Arerê', 'song_link': '/ivete-sangalo/arere.html', 'lyric': 'Tudo o que eu quero nessa vida,\nToda vida, é\nÉ amar você\nAmar você\n\nO seu amor é como uma chama acesa\nQueima de prazer\nDe prazer\n\nEu já falei com Deus que não vou te deixar\nVou te levar pra onde for\nQualquer lugar\nJá fiz de tudo pra não te perder\n\nArerê,\nUm lobby, um hobby, um love com você\nArerê,\nUm lobby, um hobby, um love com você\n\nCai, cai, cai, cai, cai pra cá\nHey, hey, hey\nTu-do,tu-do, vai rolar', 'language': 'pt'},
                 {'artist_link': '/ivete-sangalo/', 'song_name': 'Se Eu Não Te Amasse Tanto Assim', 'song_link': '/ivete-sangalo/se-eu-nao-te-amasse-tanto-assim.html', 'lyric': 'Meu coração\nSem direção\nVoando só por voar\nSem saber onde chegar\nSonhando em te encontrar\nE as estrelas\nQue hoje eu descobri\nNo seu olhar\nAs estrelas vão me guiar\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração\n\nHoje eu sei\nEu te amei\nNo vento de um temporal\nMas fui mais\nMuito além\nDo tempo do vendaval\nNos desejos\nNum beijo\nQue eu jamais provei igual\nE as estrelas dão um sinal\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração...', 'language': 'pt'}]
        artists = [{'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}]
        result = [{'artist_link': '/ivete-sangalo/', 'song_name': 'Arerê', 'song_link': '/ivete-sangalo/arere.html', 'lyric': 'Tudo o que eu quero nessa vida,\nToda vida, é\nÉ amar você\nAmar você\n\nO seu amor é como uma chama acesa\nQueima de prazer\nDe prazer\n\nEu já falei com Deus que não vou te deixar\nVou te levar pra onde for\nQualquer lugar\nJá fiz de tudo pra não te perder\n\nArerê,\nUm lobby, um hobby, um love com você\nArerê,\nUm lobby, um hobby, um love com você\n\nCai, cai, cai, cai, cai pra cá\nHey, hey, hey\nTu-do,tu-do, vai rolar', 'language': 'pt', 'artist': {'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}},
                 {'artist_link': '/ivete-sangalo/', 'song_name': 'Se Eu Não Te Amasse Tanto Assim', 'song_link': '/ivete-sangalo/se-eu-nao-te-amasse-tanto-assim.html', 'lyric': 'Meu coração\nSem direção\nVoando só por voar\nSem saber onde chegar\nSonhando em te encontrar\nE as estrelas\nQue hoje eu descobri\nNo seu olhar\nAs estrelas vão me guiar\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração\n\nHoje eu sei\nEu te amei\nNo vento de um temporal\nMas fui mais\nMuito além\nDo tempo do vendaval\nNos desejos\nNum beijo\nQue eu jamais provei igual\nE as estrelas dão um sinal\n\nSe eu não te amasse tanto assim\nTalvez perdesse os sonhos\nDentro de mim\nE vivesse na escuridão\nSe eu não te amasse tanto assim\nTalvez não visse flores\nPor onde eu vi\nDentro do meu coração...', 'language': 'pt', 'artist': {'name': 'Ivete Sangalo', 'genres': ['Pop', ' Axé', ' Romântico'], 'songs': 313, 'popularity': 4.4, 'link': '/ivete-sangalo/'}}]
        self.assertEqual(data_loader.link_songs_with_artists(songs, artists), result, 'Wrong link of the data')        

unittest.main()