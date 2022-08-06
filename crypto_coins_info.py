import requests
import json


crypto = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Ccardano%2Cethereum%2Csolana%2Cmatic%2C&vs_currencies=inr%2Cinr%2Cinr%2Cinr%2Cinr%2C')
price_crypto_inr = crypto.json()

cardano = str(price_crypto_inr['cardano']['inr'])
bitcoin = str(price_crypto_inr['bitcoin']['inr'])
solana = str(price_crypto_inr['solana']['inr'])
ethereum = str(price_crypto_inr['ethereum']['inr'])
# print(solana)
def message_btc():
  
  message1 = '🚀 $BTC: ' + bitcoin + 'rs'
  return(message1)

def message_eth():
  message2 = '🚀 $ETH: ' + ethereum + 'rs'
  return(message2)

def message_ada():
  message3 = '🚀 $ADA: ' + cardano + 'rs'
  return(message3)