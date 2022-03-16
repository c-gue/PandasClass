## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
step1 = np.full((4,3),2)
print(step1)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
step2 = np.arange(0,111,10).reshape(3,4)
print(step2) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
step3 = step2.reshape(4,3)
print(step3)

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
step4 = step3 * 3
print(step4)

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
#step5 = step1 * step2
## This errored out... why? Different shapes
#print(step5)

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
step6 = step1 * step3
## this worked! why?
print(step6)



