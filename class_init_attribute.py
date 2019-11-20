class Person:
    def __init__(self, name, age, address):
        self.hello ="안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        self.thankyou= "감사합니다."

    def greeting(self):
        print('{0} 저는 {1}입니다. \n주소는 {2}입니다. \n나이는 {3}입니다. \n이상입니다 {4}'.format(self.hello, 
        self.name, self.address, self.age, self.thankyou))

if __name__ =='__main__':
    maria = Person('이대형', 29, '공주시 우금티로')

    maria.greeting()



   
