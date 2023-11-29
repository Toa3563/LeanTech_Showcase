# Showcase
## About
The purpose of this program is to calcute the exact change of an entered USD amount. 
For example if $15.39 was entered.
The minumum amount should be given back.
          1-$10
          1-$5
          1-$0.25
          1-$0.1
          4-0.04

I built this program in Python (PYCHARM)

## Program Explanation
In my Main I Use a while loop to make it so the user can continue putting input if they want to. This makes the program easier to look for mistakes in output as well.

In my Input I used a while True loop along with a try and except to validate the input to make sure you weren't able to enter anything but a number.
There is also a round to make so only 2 decimals will be able to pass through.
for example if you put 1.3333, only 1.33 would pass through.

In my Calc(Calculation) I used a while loop that ran when the User Input was NOT zero. In the loop the user's input would run through if statements finding whether it was above the currency(100,50,20,10,5,1,0.25,0.1,0.05,0.01) in the if statement. If it is it would divide the input by the currency amount and round down to give the the amount of currency that can go into it. Then the rounded amount of currency would be subtracted from the input and ran through the loop until the input = 0.
For example:
152.75 would run through the $100 currency if statement and get 1 $100; then 1 $50, and so on and so fourth.
This works for any amount entered.

In my Output I Printed all the possible USD currencies regardless of whether it was used or not. This further clarifies that it is giving you the exact amount as it is not using the other currencies.
An ouput would look like this:
  1-hundred
  0-fifty
  2-twenties
  ...
  0-pennies
At the bottom of the output is a loop with a continue input to ask whether they would like to continue or stop. Answering N would break the program and answering Y would make you run through the program again.

## Complications
Creating the calculation loop was a lot harder than anticipated. The idea I came up with is what I concluded with but when I first thought of it I didn't know how to do it. The first attempt of running through the if statements; it kept showing 0 in the output for all of them. I used debug and I couldn't figure out what the problem was. I decided to rebuild in the same format but focusing on any problems and running 1 if statement at a time. I found that putting them in if and else statements instead of elif statements was the problem. I also had to do a -0.5 on the round statement to ensure that it would round down.
One other complication was that for some reason in the if statement for $1 it would round to 0 and output 4 quarters. Only when it was $1. I didn't understand it cause when I ran it in debug and it showed 0.5 after the round so it should round up. However I fixed it by subtracting 0.49999 and it works. Wierd fix for a wierd problem.
  

  
