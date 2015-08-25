
// Show green button when system ready
// When button is pressed flash red LEDs

int switchState = 0;

void setup() {
  pinMode(2, INPUT);  // Button
  pinMode(3, OUTPUT); // Green LED
  pinMode(4, OUTPUT); // Red LED
  pinMode(5, OUTPUT); // Red LED
}

void loop() {
  switchState = digitalRead(2);
  if (switchState == LOW) {
    // the button is not pressed
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
  } else {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);

    delay(250); // wait for a quarter second
    // toggle the LEDs
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    delay(250); // wait for a quarter second
  }

} // back to beginning of loop
