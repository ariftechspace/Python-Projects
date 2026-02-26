🔐 Caesar Cipher:   
This is a simple implementation of the Caesar Cipher, one of the oldest and most well-known encryption techniques. It allows you to encode (encrypt) or decode (decrypt) messages by shifting the letters of the alphabet.


📜 How it Works:  
-You choose whether to encode or decode.  
-Enter your message.  
-Enter a shift number (how many letters you want to move in the alphabet).  
-The program shifts only the letters while leaving spaces, numbers, and symbols unchanged.  
-You can run the program as many times as you like until you type n to quit.  


▶️ Example run:  
Type 'encode' to encrypt, type 'decode' to decrypt:  
encode  
Type your message:  
hello world!  
Type the shift number:  
5  
Here is the encoded result: mjqqt btwqi!  
Type 'y' if you want to continue, or type 'n' if you do not want to:  
n  
GOODBYE 👋  


📝 Notes:  
-Only letters a-z are shifted.  
-Numbers, spaces, and symbols stay the same.  
-Shift numbers larger than 26 are automatically wrapped (e.g., shift=30 works like shift=4).  
-The program will keep running until you choose to exit.  
