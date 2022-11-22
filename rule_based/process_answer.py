import pandas as pd


chatbot_data = pd.read_excel("chatbot_data.xlsx")

chat_dic = {}
row = 0
for rule in chatbot_data["rule"]:
    chat_dic[row] = rule.split('|')
    row+=1
def chat(request):
    for k,v in chat_dic.items():
        index=-1
        for word in v:
            try:
                if index == -1:
                    index = request.index(word)
                else:
                    if index <request.index(word, index):
                        index = request.index(word, index)
                    else:
                        index = -1
                        break
            except ValueError:
                index = -1
                break
        if index >-1:
            return chatbot_data["response"][k]
    return "다시 말씀해주세요."

while True:
    req = input("대화를 입력하세요.")
    if req == "exit":
        break
    else :
        print("", chat(req))
