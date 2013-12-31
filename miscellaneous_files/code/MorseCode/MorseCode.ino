
void setup() {                
  // initialize the digital pin as an output.
  // Pin 13 has an LED connected on most Arduino boards:
  pinMode(13, OUTPUT);  
}

// My sister and I spent a few hours attempting to write a script 
// turns letters into morse code LED blinks.  We got it to compile
// but not to behave as desired, and spent most of our time debugging.

 
int newArray[3];  // Global variables are super useful when your language
                  // doesn't even let you return arrays.

void loop() {    // Yes I know this whole thing is very poorly abstracted. 
  getLetter('S');
  things();
  darkLikeMySoul(3000);
  getLetter('O');
  things();
  darkLikeMySoul(3000);
  getLetter('S');
  things();
  
}

void things() {
  lightUpPlease(newArray[0]);
  darkLikeMySoul(1000);
  lightUpPlease(newArray[1]);
  darkLikeMySoul(1000);
  lightUpPlease(newArray[2]);  
}

void getLetter(char Letter) {
  
  String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  int letterIndex = letters.indexOf(Letter);
  
  // We were going to fill the whole thing in before we spent two hours debugging.  :(
  int morseLetters[][3] = {{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{3000,3000,3000},{},{},{},{1000,1000,1000},{},{},{},{},{},{},{}};
  newArray[0] = morseLetters[letterIndex + 1][0];   // You can't assign arrays to arrays in Processing/C!  That's kind of neat in a frustrating way.
  newArray[1] = morseLetters[letterIndex + 1][1];
  newArray[2] = morseLetters[letterIndex + 1][2];
}

void lightUpPlease(int length) {
 digitalWrite(13,HIGH);
 delay(length);
}

void darkLikeMySoul(int length) {
 digitalWrite(13,LOW);
 delay(length);
} 

