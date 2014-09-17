# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 11:12:35 2014

@author: aminic
"""

class PasswordGenerator:
    '''
    密码生成器
    '''
    #参与密码的字符类型序列
    digitalChars=('0','1','2','3','4','5','6','7','8','9')
    letterChars=('a','b','c','d','e','f','g',
                 'h','i','j','k','l','m','n',
                 'o','p','q','r','s','t',
                 'u','v','w','x','y','z',
                 'A','B','C','D','E','F','G',
                 'H','I','J','K','L','M','N',
                 'O','P','Q','R','S','T',
                 'U','V','W','X','Y','Z')
    specialChars=('`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+',
    '[','{',']','}','\\','|',';',':','\'','',',','<','.','>','/','?',']')
    
    #字符类型
    hasDigital=None
    hasLetter=None
    hasSpecialChar=None
    
    #生成密码字符列表
    generatePasswordChars=[]
    #密码长度
    passwordLength=None
    #生成密码
    password=[]
    
    def __init__(self,passwordLength=8,hasDigital=False,hasLetter=False,hasSpecialChar=False):
        '''
        passworldLength:密码长度
        hasDigital:是否有数字
        hasLetter:是否有字母
        hasSpecialChar:是否有特殊字符
        '''
        self.hasDigital=hasDigital
        self.hasLetter=hasLetter
        self.hasSpecialChar=hasSpecialChar
        self.passwordLength=passwordLength
        
        def InitGenerator():
            if self.hasDigital==False and self.hasLetter==False and self.hasSpecialChar==False:
                return
            if self.hasDigital==True:
                self.generatePasswordChars.extend(self.digitalChars)
            if self.hasLetter==True:
                self.generatePasswordChars.extend(self.letterChars)
            if self.hasSpecialChar==True:
                self.generatePasswordChars.extend(self.specialChars)
        
            self.password=[self.generatePasswordChars[0]]*self.passwordLength        
        
        InitGenerator()
        
    def getCurrentPassword(self):
        return self.password
    
    def getNextPassword(self):
        
        if self.isEnd()==True:
            return self.password
            
        def carryChar():
            index=len(self.password)-1
                
            while True:
                if self.password[index] ==self.generatePasswordChars[-1]:
                    self.password[index]=self.generatePasswordChars[0]
                    index-=1
                    continue
                
                genIndex=self.generatePasswordChars.index(self.password[index])
                
                nextChar=self.generatePasswordChars[genIndex+1]
                self.password[index]=nextChar
                return self.password
                
        return carryChar()
                
    def isEnd(self):
        if self.password==[self.generatePasswordChars[-1]]*self.passwordLength:
            return True
        return False
        
########################################
        
def test_onlyDigital():
    g=PasswordGenerator(8,True,False,False)
    print 'generate password chars',g.generatePasswordChars
    print 'current password',g.getCurrentPassword()
    
    fp=open('d:\\code.txt','w')
    while g.isEnd()==False:
        code=g.getNextPassword()
        fp.writelines(code)
        fp.writelines('\n')
    fp.close()
        
if __name__=='__main__':
    print'##################'
    print'####TEST'
    print'##################'
    test_onlyDigital()
    