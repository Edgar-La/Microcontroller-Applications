int muestras = 300;
int senal[300];

void setup()
{
  Serial.begin(9600);
}


void loop()
{
    for(int i=0;i<muestras;i++)
      senal[i] = analogRead(A0);

      
    for(int i=100;i<muestras;i++)
    {
      Serial.print(senal[i]);
      Serial.println();
      if ( i == muestras-1)
        while(true){}
    }
}
