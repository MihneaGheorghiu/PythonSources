SIMULATING THE ACTIVITY INSIDE THE PARLAMENT

This program simulates the activity of the parlament for 3 days.

I used python under Windows.

Code was written in notepad++ to easily follow the identation.

To run it I used run->cmd

command: python tema1.py n m > out.txt

I used in general 50 for n and 20 for the cabins (5 cabins at only one of the subpoints)

Also, 50 - 2 * 20 = 10 MPs that count, easy to identify.

out.txt-> redirecting to a file to be able to follow the whole output that has 50KB and follow the MPs/cabins

Implementation idea: threads for each MP (a class that extends thread), lock for each cabin (defined class), a reentry barier for each time when it's necesary to wait for all MPs to move to the next stept( similar to that from little book o semaphores).
	Cod is easy to follow given that dividing in 5 stages that contain the prints with the effect at each step, that's why I have few commentarii. The program has an instruction block in which it takes the starting values and creates a list of MPs and one of cabins. Then each thread goes through the 5 stages along the 3 days.(in fction run()).

