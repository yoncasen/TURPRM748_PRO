
# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('M2L1/text.txt', 'r', encoding='utf-8')
text = f.read()
print(text*3)
f.close()

# Daha kısa bir versiyonu:
with open('M2L1/text.txt', 'r', encoding='utf-8') as f:
     print(f.read())

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
f = open('metinbelgesi.txt', 'w', encoding='utf-8')
text = 'Yonca'
f.write(text)
f.close()

# with open('images/cat.jpg', 'rb') as f:
#         picture = discord.File(f)

import os
print(os.listdir('M2L1/bot/images'))