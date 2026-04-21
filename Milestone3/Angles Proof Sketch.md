# Angles Proof Sketch

What follows is a sketch of what will make it into the final paper. This proof demonstrates when rhombuses in a Temperature-1  aTAM system can do computation. This covers only rational major angles of the rhombus.

## Preliminaries 

If we can rotate a rhombus such that it is less than the "dead angle," we can construct a bit-reading gadget, and thus demonstrate that the rhombus can be used to simulate computation. 

The question then is, can we split the dead angle? If we can, what rotation of the rhombus do we need?

The dead angle is defined like so:
$$D_A = 2\beta \mod{180} $$
Note that any angle we can create will be of the form $n\beta \text{ mod }180$ . 

Now note what happens if we split the dead angle in half:
$$\frac{1}{2}D_A = \frac{2\beta \text{ mod } 180}{2} \rightarrow$$
$$\frac{2\beta \text{ mod } 180}{2}\equiv \beta \mod{90}$$
via modular congruence. Also note that: $$\beta + 90 \text{ mod } 90 \equiv \beta \mod{90}$$ Therefore, if we can construct $\beta + 90$, we can split $D_A$, the dead angle, in half.

---
## Proof By Case for Constructing $90\degree$  

If $\beta$ is a rational angle, there will be a finite number of rotations $k$ that bring us back to 180. The total number of rotations is then expressible like so:
$$k\beta \mod{180}\equiv 0$$

Because $k$ is an integer, it will either be even or odd. 
### Even Case:

We can rewrite $k$ as some number $n$ times 2. If we substitute from above and divide by two: 
$$2n\beta \mod{180} \equiv 0 \rightarrow \frac{1}{2}2n\beta \mod{90} \equiv \frac{0}{2} \rightarrow$$
$$n\beta \mod{90} \equiv 0$$
We can now see that if we rotate $\beta$ exactly $n$ times we can make an angle that is congruent to 0 mod 90, in other words, $90\degree$. 

This shows that after $k/2$ rotations, we will create 90 degrees. Because we split the dead angle in half at $\beta + 90$, this means we can always split the dead angle in half in the even case. 

### Odd Case:

Doing the same division by two, but now writing $k$ as odd number $2n+1$:
$$(2n+1)\beta \mod{180}\equiv 0 \rightarrow \frac{1}{2}(2n+1)\beta \mod{180} \equiv \frac{0}{2} \rightarrow$$

$$n\beta + \frac{1}{2}\beta \mod{90} \equiv 0$$
We see that we only create $90\degree$ after $n$ rotations *plus a fractional rotation.* Recall that any rotation we can make is of the form $n\beta$. In the odd case, we cannot construct $90\degree$. We cannot split the dead angle in half.

## Proof By Induction that a Half-Split is the Only Option 

Is it possible to split the dead angle into a fraction other than a half? 
### Induction:

Let's write our division of the dead angle in a more general form, subbing in "2" for "$n+1$."

n+1 substitution:
$$\frac{1}{n+1}D_A = \frac{2}{n+1}\beta \mod{\frac{180}{n+1}}$$
Base Case n=1:
$$\frac{1}{n+1}D_A = \frac{2}{n+1}\beta \mod{\frac{180}{n+1}} \rightarrow$$
$$\frac{1}{2} D_A = \frac{2}{2}\beta \mod{\frac{180}{2}} \rightarrow$$
$$\frac{1}{2}D_A = \beta \mod{90}$$
Which is what we had before. 

Notice that for any number $n > 1$, i.e any division of $D_A$ smaller than $1/2$, the rotation of beta we need is $< 1$. It will be $2/3, \ 2/4,\  2/5,$ etc. Therefore it is always a fraction, and we cannot do fractional rotations. 

## Conclusion

The only way we can split $D_A$ with a rational angle $\beta$ is by half, and this occurs only when the total rotations $k$ is even, and the rhombus that splits $D_A$ is always after $k/2 + 1$ rotations.

$Q.E.D\ \blacksquare$








