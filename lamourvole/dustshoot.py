import re

def dustshoot(arg1) :
  text = re.sub('\（[^\）]*\）', '', arg1)
  cleantext = re.sub('[\t\n\r\f\v]', '', text)
  cleanedtext = re.sub('\u3000', '　', cleantext)
  return re.findall('「([^」]*)」', cleanedtext)
