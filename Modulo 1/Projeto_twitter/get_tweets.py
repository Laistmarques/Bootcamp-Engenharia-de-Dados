import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

#Cadastrar as chaves de acesso
consumer_key = 'ynsSn7y24LnzUryBC6Q7diYli'
consumer_secret = '4yyzDPbuuqjM8LOaWGdgzUx4B6gHHZq2rxye5RB19Cg7WVWcGZ'

access_token = '1367458767118434309-o5Tjx13PxDUmIUeTAnZ9oVqRIFQkFv'
access_token_secret = 'ejzfmNP3pddLt2f49ZxMfPcEIBYh2KxbYknfSsFlcJzbe'

#Definir um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
out = open(f'collected_tweet_{data_hoje}.txt', 'w')

#Implementar uma classe para conexão com o Twitter

class MyListener(StreamListener):
    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + '\n')
        return True

    def on_error(self, status):
        print(status)


#Implementar nossa função MAIN
if __name__ == '__main__':
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Trump'])
