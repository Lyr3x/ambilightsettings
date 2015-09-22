# ambilightsettings
My personal ambilight/boblight setup:

- WS2801 (i think the newer one) => 50 LED's
- Arduino UNO Rev. 3
- 2A Power Supply
- 2.1mm Power Supplay Adapter
- 37" TV

## Wiring
Follow the wiring Setup at: https://learn.adafruit.com/adalight-diy-ambient-tv-lighting/wiring-1

## Arduino 

I've runned the Adalight software before, but my Leds just flickering with it. After hours of research i found a Thread with a Solution
There are new chips integrated in the WS2801 where the LEDstream.ino from adalight wont work perfectly. If you use the FastLED.h (often used with WS2811) it will work fine.

You find the modified LEDstream and the FastLED library in this repository

## Boblight Config
The boblight.conf in this repo is my personal configuration. Maybe it will not work perfect for you.

### Prefix
You need to change your prefix maybe to this settings:

```
25 LEDs:     41 64 61 00 18 4D 
50 LEDs:     41 64 61 00 31 64 
75 LEDs:     41 64 61 00 4A 1F 
100 LEDs:    41 64 61 00 63 36 
125 LEDs:    41 64 61 00 7C 29 
150 LEDs:    41 64 61 00 95 C0 
175 LEDs:    41 64 61 00 AE FB 
200 LEDs:    41 64 61 00 C7 92
```

