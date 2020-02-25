#sys is an module which is used for command line argunments in this program

import sys

class URL_Short:
    
    #url_list is an dictionary that storing the urls
    
    url_list = {}
    
    # url_id is an id for urls

    url_id = int(input("\nEnter a larger integer number : "))
     

    def shortener_url(self,url):
        
        # if part is to check the url is already present in the url_list[] dictionary

        if url in self.url_list:
            short_url = self.encode_url(self.url_list[url])
        
        else:
            self.url_list[str(url)] = self.url_id
            short_url = self.encode_url(self.url_id)
            self.url_id+=859674    
        
        return "short_url/"+str(short_url)
    
    def encode_url(self, url_id):
        
        #The characters to encode the url by base of 62 times instead of base 10 i.e, (0,1,2 ... 9,10)
        
        char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        ret = []

        # To pick the characters from the string char base on index value that we get from id % 62

        while (url_id > 0):
            val = url_id % len(char)
            ret.append(char[val])
            url_id//=len(char)

        # Here the value has to be reversed and has to join the list we use join()
        
        return "".join(ret[::-1])

# obj is an instance of the class
obj = URL_Short()

if len(sys.argv) == 2:

    # open is used to open a file and returns an file object

    fo = open(sys.argv[1], "r")
    
    #Loop to read the urls one by one from file 
    for line in fo:
        print(obj.shortener_url(line))
    
    #closing the openned file

    fo.close()

# If the urls file name is not passed it will display an error message

else:
    print("Pass the file name as argunment\n")
