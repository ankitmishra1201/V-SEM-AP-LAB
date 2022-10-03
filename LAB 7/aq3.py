import textwrap

f=open("input.txt","r+")
value=f.read()

width=int(input("Enter width: "))
  
# Wrap this text.
wrapper = textwrap.TextWrapper(width=width)
  
string = wrapper.fill(text=value)
  
print (string)