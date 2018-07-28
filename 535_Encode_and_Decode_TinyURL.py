
# coding: utf-8

class Codec:
    import string
    letters = string.ascii_letters + string.digits  #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    full2tiny = {}
    tiny2full = {}
    global_counter = 0
 
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
 
        if longUrl in self.full2tiny:
            return 'http://tinyurl.com/' + self.full2tiny[longUrl]
        
        suffix = ''
        dec = self.global_counter
        if dec == 0:
            suffix += self.letters[0]
        while dec:
            suffix += self.letters[dec % 62]
            dec //= 62
        
        self.full2tiny[longUrl] = suffix
        self.tiny2full[suffix] = longUrl
        self.global_counter += 1
        return 'http://tinyurl.com/' + suffix
 
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        suffix = shortUrl.split('/')[-1]
        if suffix in self.tiny2full:
            return self.tiny2full[suffix]
        else:
            return None
        
if __name__ == "__main__":
    from time import time
    codec = Codec()
    t = time()
    print('TinyURL = %s\nLongURL = %s\ntime = %.3fms'%(codec.encode('Hello'), codec.decode(codec.encode('Hello')), (time() - t) * 1000))