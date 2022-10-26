class dataCas:
  Cas = '''This Bot will rephrase the sentences:
            
Normal Version: can you help me find some product
Cooler Version: At your service, dear. That’s what my job is.

Normal Version: I can’t find any Samsung phone
Cooler Version: Don’t fret dear. What am I here for. I will help you find what you are looking for.

Normal Version: I am looking for some place near me to get food that I want.
Cooler Version: Sure dear, allow me to help you. What are your food preferences?

Normal Version: I am looking for a property near my workplace
Cooler Version: sure, makes sense. Let me look through all that we have.

Normal Version: Not getting any thing I am looking for!!
Cooler Version: Cool down dear. That's why I am here, to help you get your job done.

Normal Version: 5000 was that last months bill including electricity
Cooler Version: Thank you for letting me help! The last months bill was 5000 which included electricity charges as well.

Normal Version: 
'''

  def getCas(self):
    return self.Cas 
  def setCas(self, CasVal):
    self.Cas = CasVal