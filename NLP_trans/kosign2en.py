import googletrans

def korean_sign_language_to_korean(sentence):
    words = sentence.split()
    # 주어-목적어-동사 순서로 변경
    new_order = [words[0], words[2], words[1]]
    new_sentence = ' '.join(new_order)
    return new_sentence

translator = googletrans.Translator()

# 사용자로부터 한국 수어에 해당하는 문장 입력 받기

## 입력 예시 : 몸 건강 부탁하다 ( 몸 건강하세요 )
korean_sign_language_sentence = input("한국 수어로 된 문장을 입력하세요: ")
korean_sentence = korean_sign_language_to_korean(korean_sign_language_sentence)
print("한국 수어에서 한국어로 변환된 문장:", korean_sentence)

# 한국어를 영어로 번역
result1 = translator.translate(korean_sentence, dest='en')
print("한국어에서 영어로 번역된 문장:", result1.text)

# 추가적인 번역 과정이 필요한 경우, 아래 코드를 사용
# 영어를 다시 한국어로 번역
user_input2 = result1.text
result2 = translator.translate(user_input2, dest='ko')
print("영어에서 다시 한국어로 번역된 문장:", result2.text)

# 한 번 더 한국어를 영어로 번역
user_input3 = result2.text
result3 = translator.translate(user_input3, dest='en')
print("한국어에서 다시 영어로 번역된 문장:", result3.text)

# 마지막으로 영어를 다시 한국어로 번역
user_input4 = result3.text
result4 = translator.translate(user_input4, dest='ko')
print("영어에서 마지막으로 한국어로 번역된 문장:", result4.text)

##두번 번역한 이유 : 더 자연스러운 문장을 만들기 위함
