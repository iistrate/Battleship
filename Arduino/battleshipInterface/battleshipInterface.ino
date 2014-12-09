/*
 * Author: Ioan George Istrate
 * Info:   Battleship Command Panel for Battleship Python Game
 * Github: https://github.com/iistrate/Battleship
 *
*/

//blink funciton
void blink(const int ship, const int blinkNr = 3) {
  for (int i = 0; i < blinkNr; i++) {
    digitalWrite(ship, HIGH);
    delay(150);
    digitalWrite(ship, LOW);
    delay(150);
  }
}

int turn = 0;
int val = 0;

//led setup
const int gameStatus = 11;
const int gameOver = 12;
  //led ships
  const int submarine = 3;
    //hitpoints
    static int sHitpoints = 1;
  const int destroyer = 5;
    //hitpoints
    static int dHitpoints = 2;  
  const int cruiser = 6;
    //hitpoints
    static int cHitpoints = 3;  
  const int battleship = 9;
    //hitpoints
    static int bHitpoints = 4;  
  const int carrier = 10;
    //hitpoints
    static int caHitpoints = 5;  
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
  if (val == '0') {
    digitalWrite(gameOver, HIGH);
    digitalWrite(gameStatus, LOW);    
  }
  if (val == '2') {
    sHitpoints = (sHitpoints - 1) >= 0 ? (sHitpoints - 1) : 0;
    if (sHitpoints > 0) {
      blink(submarine);
    }
    else {
      digitalWrite(submarine, HIGH);
    } 
  }
  if (val == '3') {
    dHitpoints = (dHitpoints - 1) >= 0 ? (dHitpoints - 1) : 0;
    if (dHitpoints > 0) {
      blink(destroyer);
    }
    else {
      digitalWrite(destroyer, HIGH);
    }   
  }
  if (val == '4') {
    cHitpoints = (cHitpoints - 1) >= 0 ? (cHitpoints - 1) : 0;
    if (cHitpoints > 0) {
      blink(cruiser);
    }
    else {
      digitalWrite(cruiser, HIGH);
    }   
  }
  if (val == '5') {
    bHitpoints = (bHitpoints - 1) >= 0 ? (bHitpoints) - 1 : 0;
    if (bHitpoints > 0) {
      blink(battleship);
    }
    else {
      digitalWrite(battleship, HIGH);
    }  
  }
  if (val == '6') {
    caHitpoints = (caHitpoints - 1) >= 0 ? (caHitpoints - 1) : 0;
    if (caHitpoints > 0) {
      blink(carrier);
    }
    else {
      digitalWrite(carrier, HIGH);
    }
  }  
  //Serial.println(val);
  delay(1);   
  turn++;
}
