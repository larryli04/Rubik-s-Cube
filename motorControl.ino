// test
// Define pin connections & motor's steps per revolution
#include <AccelStepper.h>


const int stepPin[] = {0, 2, 4, 6, 8, 10};
const int dirPin[] = {1, 3, 5, 7, 9, 11};
const int revLength[] = {200};
int x = 0;
int count = 0;
int y = 0;
int c = 0;
int n;
int arr[5];


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
  Serial.setTimeout(3);
  // Declare pins as Outputs
  for(int i = 0; i < 6; i++) {
    pinMode(stepPin[i], OUTPUT);
    pinMode(dirPin[i], OUTPUT);
  }
  for(int i = 0; i < 6; i++) {
    digitalWrite(stepPin[i], LOW);
  }

  while (!Serial.available() and x==0) {
    x = Serial.readString().toInt();
  }
  Serial.print("Recieved message: ");
  Serial.print(x);
  Serial.print("\n");
  
  while(x) {
    arr[c] = x%10;
    x /= 10;
    c++;
  }
  x = 5;
  c = 0;
  // x is also zero at this point
  n = sizeof(arr) / sizeof(arr[0]);
  reverseArray(arr, 0, n-1);
 
  for(int i = 0; i < 5; i++) {
    Serial.print(arr[i]);
  }
  
}
void loop()
{
  
  
  y = 3;
  Serial.print(y);
  // Serial.print(q);
  // read from q to determine which motor is spun
  //y=q;
  //random(6);
  
  // Set motor direction clockwise
  digitalWrite(dirPin[y], HIGH);

  // Spin motor slowly
  for(int i = 0; i < (200/4); i++)
  {
    digitalWrite(stepPin[y], HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin[y], LOW);
    delayMicroseconds(1000);
  }
  delay(500);
  if(count<4) {
    count = count + 1;
  }
  else {
    count = 0;
    x = 0;
    memset(&arr[0], 0, sizeof arr);
    while (!Serial.available() and x==0) {
      x = Serial.readString().toInt();
    }
    Serial.print("Recieved new message: ");
    Serial.print(x);
    Serial.print("\n");
  
    while(x) {
     arr[c] = x%10;
     x /= 10;
      c++;
     }
    x = 5;
    c = 0;
    // x is also zero at this point
    n = sizeof(arr) / sizeof(arr[0]);
    reverseArray(arr, 0, n-1);
 
    
  }
}
