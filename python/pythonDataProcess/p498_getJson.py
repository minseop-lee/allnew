import json

def get_Json_data():
    filename = 'jumsu.json'
    myfile = open(filename, 'rt', encoding='utf-8')
    print(type(myfile))
    print('-' * 100)

    myfile = myfile.read()
    print(type(myfile))
    print('-' * 100)

    jsondata = json.loads(myfile)
    print(type(jsondata))
    print('-' * 100)

    for oneitem in jsondata:
        print(oneitem.keys())
        print(oneitem.values())
        print('이름 :', oneitem['name'])
        kor = float(oneitem['kor'])
        eng = float(oneitem['eng'])
        math = float(oneitem['math'])
        total = kor + eng + math

        print('국어 : ', kor)
        print('영어 : ', eng)
        print('수학 : ', math)
        print('총점 : ', total)

        if 'hello' in oneitem.keys():
            message = oneitem['hello']
            print('message : ', message)

        _gender = oneitem['gender'].upper()

        if _gender == "M":
            gender = '남자'
            print('성별 : ', gender)
        elif _gender == "F":
            gender = '여자'
            print('성별 : ', gender)
        else:
            print('미정')
    print('-' * 100)

if __name__=='__main__':
    get_Json_data()