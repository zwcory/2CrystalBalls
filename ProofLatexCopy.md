# 2 Crystal Ball Set Up

You are given 2 crystal balls, and a multiple storey building. For the sake of the example this building will be 100 floors. You are tasked with finding out what the lowest floor is, where dropping the crystal ball will break from. The balls are identical and do not weaken while surviving drops. I.E if the 'break floor' is floor 24, dropping the ball from any floor below would never break it, and any floor above would always break it. We can look at the floors as a sorted list of Booleans.


# Initial Approaches
### Half way drop
One may initially think to drop the ball from the 50th floor and see whether it breaks or not. If it does break we know the break floor is the 50th floor or lower. To find the break floor we would have to start from the bottom and 'walk' each floor until it breaks. If it didn't break from the 50th floor drop we know the break floor is higher than 50 so we can drop it from the 75th floor and repeat our previous steps. The worst case scenario here is always going to be  $0.5(n)$ steps, where n is the number of floors (or length of the list). So this gives us a time complexity of $O(n)$ - a linear time complexity.

### $n/X$ Drops
Next we could try jumping a tenth of $n$ until the ball breaks, then go back to the last safe drop, and walk up until we find the break floor. Here the worst case scenario is $0.2(n)$ (10 Initial jumps and then 'walking' up the last floors). However, as we drop constants in time complexity we drop the 0.2, and it gives us a time complexity of $O(n)$ . Linear again albeit a better worst case scenario than the previous approach.

### $ \sqrt{n} $ Drops
As the previous approaches have both shown a linear time complexity, changing the jumps based on a pre-determined fraction of $n$ will always give us a linear time complexity. A solution to this issue is to take the square root of $n$, and jump by that amount until it breaks, go back to the last safe drop and walk up until we find our break floor. In the case of the 100-floor building, this approach will give us the break floor in the same number of iterations of a $0.1(n)$ approach but if the building is taller (or list is bigger), $\sqrt{n}$ will give us fewer steps than $0.1(n)$. Take a 10,000-floor building, $\sqrt{n}$ gives us a worst case scenario of 200 steps (100 jumps + 100 by walking) while $0.1(n)$ gives us a worst case scenario of 1010 (10 jumps + 1000 by walking). This approach, of $O(\sqrt{n})$ time complexity, was the approach I was taught when I came across this problem for the first time, and now I will prove it to be the most efficient, while considering what would happen if instead of making jumps by $\sqrt{n}$ floors each time we could make jumps by a different fractional power of $n$.
# Findings
## Fractional Powers of $n$ and their time complexity
If we think of the size of the jumps we make as $n^a$, we can think of $\sqrt{n}$ as $n^{1/2}$. This will allow us to easily modify the roots of $n$ we jump by, and notice how the time complexity changes.

To begin with we will increase the size of the jumps we make by increasing $a$ to $2/3$. In the case of the 100-floor building, we will make jumps of 21 (floor of 21.544...), giving us a total of 5 jumps, and the worst case scenario of 25 steps (in the case of 100, the worst case would be when the break floor is at 84 - 4 jumps, and 21 steps by walking up). This worst case scenario is worse than $n^{1/2}$, so naturally the time complexity should be higher.

Next we could try to lower $a$ to $1/3$. In the case of the 100-floor building we will then jump by 4 (floor of 4.641...), giving us 25 jumps, and only having to walk by 4 after finding the last safe drop. The worst case scenario here gives us 29 steps, 9 higher than $n^{1/2}$, so naturally the time complexity must be higher.

So if both increasing and decreasing $a$ gives us a higher time complexity, then the algorithm is most efficient when $1/3 < a < 2/3$, but how do we know if a value of $a = 1/2$ is the best?

We need to find an equation that gives us the number of steps depending on the value of $a$ and $n$. For this part we won't be flooring any values to allow us to rearrange the equation. If we set $n$ to 64 (so that $n^{1/2}$, $n^{1/3}$ and $n^{2/3}$ are whole numbers) we can find then derive an equation for the worst case scenario of $n^a$.

- $64^{1/2}$ gives us a jump amount of 8, therefore 8 jumps and 8 steps from walking, a WCS of 16.
- $64^{1/3}$ gives us a jump amount of 4, therefore 16 jumps and 4 steps from walking, a WCS of 20.
- $64^{2/3}$ gives us a jump amount of 16, therefore 4 jumps and 16 steps from walking, a WCS of 20

Those of you who have a background in maths will probably have already spotted the pattern, and a simple rewrite of the jump amounts and walking steps will reveal the equation giving us our WCS.

- $64^{1/2}$ - jumps of 8 ($64^{1/2}$), and walking steps of 8 ($64^{1/2}$)
- $64^{1/3}$ - jumps of 4 ($64^{1/3}$), and walking steps of 16 ($64^{2/3}$) or ($64^{1-(1/3)}$)
- $64^{2/3}$ - jumps of 16 ($64^{2/3}$), and walking steps of 4 ($64^{1/3}$) or ($64^{1-(2/3)}$)

So our WCS scenario is $\text{WCS} = n^a + n^{1-a}$. If we rewrite this equation as a graph we could then differentiate to find the minimum, and a value of $a$ that most optimizes our algorithm.
See the [differential equation](MathematicalProof.md) for details.

While [graphing](https://www.desmos.com/calculator/sm2ib2fgzm) the WCS equation for $a = 1/3$ and $2/3$, and the graphs for the floored values, it's clear that when we floor the jump amount we get a discrepancy from the ideal line, with jump amounts of $n^{1/3}$ giving a higher WCS than jump amounts of $n^{2/3}$. This is because by flooring the smaller amount, we are losing a larger percentage of the jump, leading to extra jumps. Take our first example of 100 floors. $100^{1/3}$ gives a jump amount of 4.64..., floored its 4. The floored jump amount gives us 25 jumps instead of 21.544... Jump amounts of $100^{2/3}$ gives us 21.544... and a floored value of 21, both giving us a value between 4 and 5, so we don't have to make any jumps. Although this does not affect anything, as we have now found the ideal value of $a$ to be $1/2$ I still found it interesting.

[Graphing](https://www.desmos.com/calculator/sm2ib2fgzm) for $a = 1/2$ shows us something interesting, where the floored values for the jump amount leads to a better WCS than none floored values. The reason for this is when the final jump takes us over our final floor, we do not have to walk through as many floors to find the break floor. i.e in a building with 109 floors, the floored jump amount is 10, and although jumping passed 109 takes 11 jumps, it's only a maximum 9 walking steps to find the break floor, giving us 20 steps, for 108 it would only be 8 walking steps from 100th floor to the 108th, giving us 19. If the break floor was on the 100th, then after 10 jumps, and 10 walking steps, we are back to our WCS. Why this is interesting is because the value of $n$ grows and the time complexity remains the same.

Speaking of time complexity, here is how both increasing and decreasing the jump size leads to a higher time complexity.

- For $a = 1/2$, we have the equation of $n^{1/2} + n^{1-(1/2)} = n^{1/2} + n^{1/2} = 2n^{1/2}$. Dropping the constant of 2 we end up with $O(n^{1/2})$
- For $a = 1/3$, $n^{1/3} + n^{2/3}$. As $n$ grows, $n^{1/3}$ becomes insignificant so we drop it, giving us $O(n^{2/3})$
- For $a = 2/3$, $n^{2/3} + n^{1/3}$. As $n$ grows, $n^{1/3}$ becomes insignificant so we drop it, giving us $O(n^{2/3})$

Thanks for reading!
If you learned something from this, or if you enjoyed reading this, follow me on linkedin [add link here ] and comment "Crystal balls are cool" on the post that brought you here!