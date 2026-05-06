Matchup is a type that represents a matchup game between two Team objects. It is a tree like structure

Order of a node is how far along the tree it is whichever round it is. This has a corespondants between these probability in order which are probmakeconfsemi, probmakeconfchamp, probmaketitlegame, probwintitle. With each value indicating the probability that a team is going to make it to the next round. 
These values are extracted from the POWER_INDEX_DATA_JSON and can be acquired for a team with the get_attribute function.

For each node / matchup in the tree

Have a list_A that indicates all the possible teams that could make it to be Team A
Have a list_B that indicates all the possible teams that could make it to be Team B

We want to solve for the probabilities of a certain team in A beating a certain team in B. So that would be len(list_A) * len(list_B) unknown variables.
We need to construct a system of equations into a matrix and then solve for that.

First construct the equations for team A advancing the order+1 round. The right side of the equal sign will be the probablity that team A makes it to the order+1 round which can be gathered from the get_attribute function. This will be the C part of the Ax=C linear equation.
The left side of the equation will be the sum for each team B, the probability that it makes it this order of a round multiplied by the unknown variable which is the probability that this particular team A beats this particular team B.

Next construct the equations for team B advancing to the order+1 round. The equations will be the exact same but instead we are multiplying each probability of A making it to that round multiplied by 1 minus the unkown variable which is the probability this particular team A beats this particular team B.

Use these matrices to solve a system of equations.

Print out the matchup odds that have been calculated by the equations.

This will give us A x B unknowns and A + B equations. This means the system will be under constrained in some scenarios, in that situation, simply skip this node.