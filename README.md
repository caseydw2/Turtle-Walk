# Turtle-Walk
The turtle_walk function outputs a path of a walk that changes direction each step. 

The turtle_walk was inspired by [this Numberphile video](https://youtu.be/kMBj2fp52tA). "Turtle" in the video is in reference to a program that intakes simple instructions. turtle_walk can be thought of as a discreet version of [Euler Spirals](https://en.wikipedia.org/wiki/Euler_spiral). 

The walk begins with one step and with &theta; = 0. Then at step two, the "turtle" turns by a given &Delta;&theta; (&theta; = &theta; + &Delta;&theta;). At step three the "turtle" turns by 2&Delta;&theta; (&theta; = &theta; + 2&Delta;&theta;). At step four, it turns 3&Delta;&theta; (&theta; = &theta; + 3&Delta;&theta;), and so on.

Here is a curve where &Delta;&theta; = 1

![Turtle Walk 100,1,1000](https://user-images.githubusercontent.com/74943315/154849113-7db4485c-fd18-4273-8bf5-1e94e8250ebe.png)

The walk is extremely sensitive to small pertibations to &Delta;&theta. As an example, below is the path where &Delta;&theta; = 1.01

![Turtle Walk 100,1 01,2000,(20000, 20000)](https://user-images.githubusercontent.com/74943315/154869340-9530ba56-0392-4416-a90c-3b88e210f64d.png)
