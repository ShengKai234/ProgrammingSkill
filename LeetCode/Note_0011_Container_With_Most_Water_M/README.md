# LeetCode 0011 - Container With Most Water
In this case, the approuch is that the area formed between the two lines will limited by the heighter and shorter line.
Futher, the farther between the two lines, more will be the area obtained.
I take the two points, one at the beggining and another at the end of array. Futher, we maintain a variable `max_area` to store the maximun area obtained till now.
At every step, update the `max_area` and move the pointer to the shorter line towards the other end of one step