# Exploring Finite Groups through Python
## About

As the name suggests, this project aims to explore properties of finite groups through python.



## **Key Features:**

- Check if the provided structure forms a Group.
- Gives Identity element, and inverse of each element.
- Verifies if Group is Abelian, Cyclic
- Cayley Table Generation
- Subgroup Identification
- Centre Determination

## Working On Ideas

- ~~Add functions to obtain a * b, a * b^-1, a^n~~
- ~~More info about groups like generators, normal subgroups~~
- Add functionality like external direct product, quotient group.
- Add popular groups like Z_n, U_m, S(n), A(n), D(n) to easily initialize at go.
- Further generalise it for rings, fields, ufds, pids.
- visualizing datasets formed for this module for different groups.
- incorporate groups formed using matrices.

### Dependencies: 

- python3
- numpy

# Current Functionality

### Initialise a Group

```python
# example
from GROUP import GROUP
Z_5 = GROUP(elements=[0,1,2,3,4], expression='(a+b)%5')

```

### Functions

- g.info(): Provides all the info about the group
- get_cayley_table(): Calculate the Cayley table for the group.
- is_closed(): Check if the group operation is closed.
- is_identity(): Determine if the group has an identity element.
- is_inverse(): Check for the existence of inverses and self-invertible elements.
- is_group(): Check if the given set forms a group.
- is_abelian(): Check if the group is abelian (commutative).
- is_cyclic(): Check if the group is cyclic.
- get_not_self_invertible(): Return elements that are not self-invertible.
- get_subgroups(): Find all subgroups of the group.
- get_centre(): Find the centre of the group.
- evaluate(a,b): gives a*b
- a_power_n(a,n): Finds a^n for +,-ve value of n
- get_normal_subgroups(): Find all normals subgroups of the group.
- generators: gives all the generators

## Example Usage:

```python
from GROUP import GROUP
U_15 = GROUP(elements= [1, 2, 4, 7, 8, 11, 13, 14], expression='(a*b)%15')
U_15.info()

```

### Output:

```python
Is Group:  True
Elements:  [1, 2, 4, 7, 8, 11, 13, 14]
Order:  8
Cayley Table: 
 [[ 1.  2.  4.  7.  8. 11. 13. 14.]
 [ 2.  4.  8. 14.  1.  7. 11. 13.]
 [ 4.  8.  1. 13.  2. 14.  7. 11.]
 [ 7. 14. 13.  4. 11.  2.  1.  8.]
 [ 8.  1.  2. 11.  4. 13. 14.  7.]
 [11.  7. 14.  2. 13.  1.  8.  4.]
 [13. 11.  7.  1. 14.  8.  4.  2.]
 [14. 13. 11.  8.  7.  4.  2.  1.]]
Identity Exist:  True
Identity:  1
Inverses exist:  True
Inverses:  [[1, 1], [8, 2], [4, 4], [13, 7], [11, 11], [14, 14]]
Self Invertible Elements:  [1, 4, 11, 14]
Not Self Invertible Elements:  [2, 7, 8, 13]
Is Abelian:  True
Is Cyclic:  False
Subgroups:  [[], [1], [1, 2, 4, 7, 8, 11, 13, 14], [1, 4], [1, 2, 4, 8], [1, 11], [1, 4, 7, 13], [1, 14], [1, 4, 11, 14]]
Centre:  [1, 2, 4, 7, 8, 11, 13, 14]
```

## **Contribution**

Contributions are welcome! Feel free to fork the repo.

## **License**

This project is licensed under the [MIT License.](https://github.com/priyanshupant/group-theory/blob/main/LICENSE)
