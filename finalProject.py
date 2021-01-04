text = open('sample_text.txt','r').read()
textList = text.split()
nextdict = {}


def main():
    sentence = ""
    for i in range(0,len(textList)-1):
        
        if textList[i] not in nextdict.keys():                  #checking if a word already exist in the dictionary or not
            nextdict[textList[i]] = {textList[i+1]:1}           #if it doesn't exist then we add the word and next word as a key value pair in dictionary with count 1 
            
        else:                                                               #if the word exist in the dict
                if textList[i+1] not in nextdict[textList[i]].keys():      #we check for the dictionary for the corresponding word, and if the key value doesn't exist, we add new key value pair 
                    nextdict[textList[i]].update({textList[i+1]:1})
                else:
                    k=nextdict[textList[i]][textList[i+1]]                      #if the key,value pair exist then we simply update its count
                    nextdict[textList[i]][textList[i+1]]=k+1
                    
 
    #print("---",nextdict[textList[1]])
    #print("----",nextdict[textList[1]].keys())
    
    ip=input("ENTER WORD : ");
    ip.lower()
    ip = ip.split()              
    inputText = ip[-1]
    prevWord = ""
    
    
    while(inputText!="."):
        
        sentence = sentence + " " + inputText
        logic(inputText)
        
        prevWord = inputText
        inputText=input("ENTER WORD : ");
        
        
       
        if inputText in nextdict[prevWord].keys():
                
            count = nextdict[prevWord][inputText]           #if word user has typed is in the dictionary of the previously typed word then we just increment its count
            nextdict[prevWord][inputText] = count+1         #reason behind increasing the count is that there are high chances of user using that word again, so instead of decreasing the count we increase the count so that the most used words always gets into the suggestions
        
        else:
            nextdict[prevWord].update({inputText:1})        ##if the word is not in the dictionary of prev word then we just add the entered word in the dictionary of the previously typed word
            
        
    if "." in inputText:
        print(f'The Sentence is : {sentence}.')
    
    

def logic(inputText):
    
        
    
    
        if inputText in nextdict.keys():                
            k=list(nextdict[inputText].keys())              #the possible words that can come after the word user has given as input
            z=list(nextdict[inputText].values())
        
            max1 = 0
            words=[]                                    #contains the possible words that might appear after the given input
            prob = []
            
            
            l = len(k)          # not all the words will always have three words to suggest, so based on the words it have to suggest we show those only
            total = l
            
            
            if(l>=3):
            
                for i in range(0,len(z)):
                    if z[i]>z[max1]:
                        max1=i
                                
                        
                prob1 = round(float(z[max1]/total),3)
                
                prob.append(str(prob1))
               
                words.append(k[max1])                           #we always pick the top 3 words
                del z[max1]
                del k[max1]                                     #remove the word from the list so that we dont use it again
            
                l = l-1
            
            
            max1=0
            
            if(l>=2):
            
            
                for i in range(0,len(z)):
                    if z[i]>z[max1]:
                        max1=i
                        
                prob2 = round(float(z[max1]/total),3)
                prob.append(str(prob2))

                words.append(k[max1])
                del z[max1]
                del k[max1]
                
                l = l-1
                
            max1=0
            
            if(l>=1):
            
                for i in range(0,len(z)):
                    if z[i]>z[max1]:
                        max1=i
                
                prob3 = round(float(z[max1]/total),3)
                
                prob.append(str(prob3))
              

                words.append(k[max1])
                del z[max1]
                del k[max1]
            
            suggest = "Suggestions : {"
           
            
            for i in range(0,len(words)):
                suggest = suggest + " " + words[i] + ":" + "(" + prob[i] + ")"
                
            print(suggest)
        
        else:
            nextdict[inputText] = {}
               
if __name__=='__main__':
    main()
        