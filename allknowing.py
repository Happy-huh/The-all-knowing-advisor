import wolframalpha
import wikipedia
import pyttsx3
import sys
import time

def main():
    allknowing()
        
def tts_str(var):
    print(var)
    txt_to_speech = pyttsx3.init()
    txt_to_speech.say(var)
    txt_to_speech.runAndWait()
    return var

def tts_file(text):
    txt = open(f'{text}.txt')
    x = txt.read()
    print(x)
    txt_to_speech = pyttsx3.init()
    txt_to_speech.say(x)
    txt_to_speech.runAndWait()
    txt.close()
    return x

def wolf(text):
    app_id = 'X5GGVX-WLW9UJRL8T'
    client = wolframalpha.Client(app_id)

    ans = client.query(text)
    ans = next(ans.results).text
    with open('answer.txt', 'w') as a:
        a.write(ans)
    with open('history.txt', 'a') as a:
        a.write(ans)
    tts_file('answer')
    return ans

def wikiped(text):
    ans = wikipedia.summary(text)

    with open('answer.txt', 'w') as a:
        a.write(ans)

    with open('history.txt', 'a') as a:
        a.write(ans)
    tts_file('answer')
    return ans

def payment_per_time(start,finish):
    ans = finish-start
    ans = (ans/60) * 2
    return ans

def allknowing():
    tts_file('introduction')

    while True:
        cont = input('question/quit/chat: ').lower().strip()
        if cont != 'question' and cont != 'chat' and cont != 'quit':
            tts_str('Invalid input try again')
        else:
            break
    
    if cont == 'quit':
        tts_str('Let\'s do this some other time goodbye')
    elif cont == 'question':
        start = time.time()
        tts_str('what question would you want to ask me')
        text = input("what question would you want to ask me: ").lower().strip()
        try:
            wikiped(text)
        except:
            tts_str('Sorry I don\'t have an answer to your question. Please try being more specific next time')
            finish = time.time()
            bill = payment_per_time(start,finish)
            tts_str(f'i could not answer your question but I still have to charge you though your bill is {bill:.2f} dollars')
            return
        finish = time.time()
        bill = payment_per_time(start,finish)
        bill = f'nice question your bill is {bill:.2f} dollars'
        tts_str(bill)
    else:
        start = time.time()
        try:
            while True:
                try:
                    text = input("(Type quit to quit) What do you wanna say: ").lower().strip()
                    if text == 'quit':
                        break
                    if text.startswith("'know'"):
                        wikiped(text)
                    else:
                        try:
                            wolf(text)
                        except:
                            wikiped(text)
                except:
                    tts_str('sorry I don\'t have an answer to this question ask something else.')
        except EOFError:
            pass
        finish = time.time()
        bill = payment_per_time(start,finish)
        bill = f'nice chatting with. Your bill is {bill:.2f} dollars'
        tts_str(bill)


if __name__ == "__main__":          
    main()