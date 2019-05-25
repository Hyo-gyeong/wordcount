from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') #render함수 : 3개의 인자까지 받을 수 있음 1. request라는 객체 (약간 고정적) 받음 2.template의 이름을 인자로 받음 3.선택적으로, 사전형객체(dictionary형)인자로 받음

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] #home에서 입력한 데이터를 표현하는 방법, 지정해준 이름(fulltext)을 이용//받아온 데이터 전체를 나타냄//text라는 변수에 담아서 표현해줘야함 , text는 get-넘겨받은 값 fulltext대표하는 값
    words = text.split()#text변수를 공백기준으로 나눠서, word라는 변수에 넣어주기
    ##############
    word_dictionary = {} #하나의 빈 사전 만들기 -> 반복문 돌려서 이 안에 넣기
    
    for word in words: #word = 반복문 변수, words = list에 해당하는 것 
        if word in word_dictionary:#반복문 변수 즉, 단어가 빈 사전에 있으면 
            #증가시켜주자! increase
            word_dictionary[word]+=1
        else: #처음 보는 단어라면?!
                # add to dictionary
            word_dictionary[word]=1 #해당하는 word를 key값 삼아서 해당 value를 1로 측정해라
    ##############
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()}) #위에서 받은fulltext 데이터를 반환하고 싶음, 3번째인자는 선택적으로 사전형(키값 : value(실재로 표현하고자 하는 값))으로 적어줌
    #임의로 full이라는 key값을 정해줌, full이라는 key값이 text라는 value값을 대표함//키값의 이름을 total이라고 짓고 단어의 길이 = len(words)를 반환!
    #사전형 자료를 '쌍'으로 보내주는 파이썬 문법! .items{}