# Couple of objective rules for effective coding

 1. A function should be short. In fact, it should only do **one** thing.
    - In practice, it means that no more meaningful methods can be extracted from that function.
    - A function shouldn't really be longer than ~5 lines

 2. Function names should be verbs (longer is better if it explains what the function does)

 3. Please use parameter names when calling a function (this makes the code more readable since the reader no longer needs to memorize each functions' parameters)

 4. Try to avoid passing *booleans* and *output arguments* (arguments meant solely for creating outputs) into functions. 
    - For booleans - just create separate functions for each case
    - For output arguments - nobody can read that, duh


5. Principle of least surprise - make sure that your code is not surprising

6. Avoid switch statements -> use objects instead

7. Clean up side-effects (when something works for some reason)

8. Avoid duplicate code
    - for code - use functions with arguments
    - for loops - create a lambda object and then call it every time you need that loop

9. Make the code express itself instead of writing comments

