/*
 * Author: Ioan George Istrate
 * Info:   Battleship Command Panel for Battleship Python Game
 * Github: https://github.com/iistrate/Battleship
 *
*/

int turn = 0;
int val = 0;

//led setup
const int gameStatus = 11;
const int gameOver = 12;
  //led ships
  const int submarine = 3;
  const int destroyer = 5;
  const int cruiser = 6;
  const int battleship = 9;
  const int carrier = 10;

void setup() {
  Serial.begin(9600);
  
  //setup leds
  pinMode(gameStatus, OUTPUT);
  pinMode(gameOver, OUTPUT);
  pinMode(submarine, OUTPUT);
  pinMode(destroyer, OUTPUT);
  pinMode(cruiser, OUTPUT);
  pinMode(battleship, OUTPUT);
  pinMode(carrier, OUTPUT);
}

void loop() {
  //read values from Serial Port
  val = Serial.read();
  
  if (val == '1') {
    digitalWrite(gameStatus, HIGH);
  }
  else if (val == '0') {
    digitalWrite(gameOver, HIGH);
    digitalWrite(gameStatus, LOW);    
  }
  else if (val == '3') {
    digitalWrite(submarine, HIGH);
  }
  //Serial.println(val);
  delay(1); 
  
  turn++;
}
