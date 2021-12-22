// test
// Define pin connections & motor's steps per revolution

const int dirPin[] = {12, 2, 4, 6, 8, 10};
const int stepPin[] = {13, 3, 5, 7, 9, 11};
const int dir[] = {HIGH, HIGH, HIGH, LOW, HIGH, LOW};
const int revLength[] = {200};
int y = 0;
int c = 0;
int n;
int arr[5];
int input;

void reverseArray(int arr[], int start, int end)
{
    int temp;
    while (start < end)
    {
        temp = arr[start];  
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }  
} 
void setup()
{
  Serial.begin(9600);
  
  // Declare pins as Outputs
  for(int i = 0; i < 6; i++) {
    pinMode(stepPin[i], OUTPUT);
    pinMode(dirPin[i], OUTPUT);
  }
  for(int i = 0; i < 6; i++) {
    digitalWrite(stepPin[i], LOW);
  }

}
void loop()
{
  if (Serial.available() > 0) {

    // read the oldest byte in the serial buffer:

    input = Serial.read();

    // if it's a capital H (ASCII 72), turn on the LED:
    if(input=='B') { //GREEN
      y = 0;
    } else if(input=='D'){ //WHITE
      y = 1;
    } else if(input=='U'){ //YELLOW
      y = 2;
    } else if(input=='L'){ //ORANGE
      y = 3;
    } else if(input=='R'){ //RED
      y = 4;
    } else if(input=='F'){ //BLUE
      y = 5;
    }
    
    
    
    // Set motor direction clockwise
    digitalWrite(dirPin[y], dir[y]);
  
    // Spin motor slowly
    
    for (int i = 0; i < (200 / 4); i++) {
      digitalWrite(stepPin[y], HIGH);
      delayMicroseconds(3000);
      digitalWrite(stepPin[y], LOW);
      delayMicroseconds(3000);
    }
    delay(1000);
  }
}
