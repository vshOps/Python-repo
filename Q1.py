print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')


# Install an external module and use it to perform an operation of your Choice
import pyttsx3
engine = pyttsx3.init()
engine.say("sarita tum bohot sundar ho")
engine.runAndWait()


# write a python program to print the contents of ddirectory using the os module .
import os

# Specify the directory path
directory_path = "."

# List and print all files and folders in the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)



n=int(input("Enter number of pages: "))
pages=list(map(int,input("Enter page reference string: ").split()))
frames=int(input("Enter number of frames: "))

memory=[]
recent={}
faults=0
for i in range(n):
    if pages[i] not in memory:
        if len(memory)<frames:
            memory.append(pages[i])
        else:
            lru=min(recent,key=recent.get)
            idx=memory.index(lru)
            memory[idx]=pages[i]
            del recent[lru]
        faults+=1
    recent[pages[i]]=i
    print(memory)
print("Total Page Faults:",faults)