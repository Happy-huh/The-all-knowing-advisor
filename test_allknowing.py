from allknowing import *

def test_wolf():
    assert wolf('hello') == 'Hello, human.'
    assert wolf('do you have emotions') == 'I am capable of universal computation; that I can say.'
    assert wolf('what is chatGPT') == 'city population | 35627 people (country rank: 38th) (2006 estimate)'

def test_wikiped():
    assert wikiped('what is python') == 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.Python consistently ranks as one of the most popular programming languages.\n\n'
    assert wikiped('hello') == 'In religion and folklore, hell is a location or state in the afterlife in which evil souls are subjected to punitive suffering, most often through torture, as eternal punishment after death. Religions with a linear divine history often depict hells as eternal destinations, the biggest examples of which are Christianity and Islam, whereas religions with reincarnation usually depict a hell as an intermediary period between incarnations, as is the case in the dharmic religions. Religions typically locate hell in another dimension or under Earth\'s surface. Other afterlife destinations include heaven, paradise, purgatory, limbo, and the underworld.\nOther religions, which do not conceive of the afterlife as a place of punishment or reward, merely describe an abode of the dead, the grave, a neutral place that is located under the surface of Earth (for example, see Kur, Hades, and Sheol). Such places are sometimes equated with the English word hell, though a more correct translation would be "underworld" or "world of the dead". The ancient Mesopotamian, Greek, Roman, and Finnic religions include entrances to the underworld from the land of the living.'

def test_payment_per_time():
    assert payment_per_time(1675129301.4595802,1675129541.4595802) == 8.0
    assert payment_per_time(15700,15760) == 2.0
    assert payment_per_time(10,70) == 2.0

def test_tts_str():
    assert tts_str('Invalid input try again') == 'Invalid input try again'
    assert tts_str('Let\'s do this some other time goodbye') == 'Let\'s do this some other time goodbye'
    assert tts_str('what question would you want to ask me') == 'what question would you want to ask me'    

def test_tts_file():
    assert tts_file('introduction') == 'Good day! I am wolfram|Alpha the all knowing advisor, I possess knoweldge on every topic and have answers to any question you ask of me. \nYou can ask me any question or engage me in a conversation but any which it be, gaining enlightenment does not come cheap. \nYou will be charged a compulsry fee of $2 per minute. \nYou can ask me any question of your choice by typing question or engage me in a discussion by typing chat or quit this program by typing quit case insensitively.\nAnd also if you choose to converse with me you can still ask specific questions by typing \'know\' in single quotaion marks then your question and I will answer. \nYou can quit chatting anytime by pressing control + d.'
    txt = open('answer.txt')
    x = txt.read()
    assert tts_file('answer') == x