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
- Add popular groups like ~~Z_n, U_m, K4, Q8, S(n), A(n),~~  D(n) to easily initialize at go.
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
# defining function
def mod_5(a,b):
    return (a+b)%5

GROUP({0,1,2,3,4},mod_5 ).info()

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
- generators: gives all the generator
- is_simple(): Checks if group is simple
- visualize(): Visualizing cayley tables as images.

## Example Usage:

```python
from GROUP import GROUP
from define import Z, U, K4, Q8

GROUP(Z(7).elements, Z(7).function).info()
print('\n')
GROUP(U(15).elements, U(15).function).info()
print('\n')
GROUP(K4().elements, K4().function).info()
print('\n')
GROUP(Q8().elements, Q8().function).info()
print('\n')
GROUP(S(3).elements, S(3).function).info()


```

### Output:

```python
Is Group:  True
Elements:  {0, 1, 2, 3, 4, 5, 6}
Order:  7
Cayley Table: 
 [[0. 1. 2. 3. 4. 5. 6.]
 [1. 2. 3. 4. 5. 6. 0.]
 [2. 3. 4. 5. 6. 0. 1.]
 [3. 4. 5. 6. 0. 1. 2.]
 [4. 5. 6. 0. 1. 2. 3.]
 [5. 6. 0. 1. 2. 3. 4.]
 [6. 0. 1. 2. 3. 4. 5.]]
Identity Exist:  True
Identity:  0
Inverses exist:  True
Inverses:  {(4, 3), (6, 1), (5, 2), (0, 0)}
Self Invertible Elements:  {0}
Not Self Invertible Elements:  {1, 2, 3, 4, 5, 6}
Is Abelian:  True
Is Cyclic:  True
Subgroups:  [{0}, {0, 1, 2, 3, 4, 5, 6}]
Centre:  {0, 1, 2, 3, 4, 5, 6}
Generators:  {1, 2, 3, 4, 5, 6}
Normal Subgroups:  [{0}, {0, 1, 2, 3, 4, 5, 6}]
Is Simple:  True


Is Group:  True
Elements:  {1, 2, 4, 7, 8, 11, 13, 14}
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
Inverses:  {(4, 4), (14, 14), (13, 7), (1, 1), (8, 2), (11, 11)}
Self Invertible Elements:  {1, 11, 4, 14}
Not Self Invertible Elements:  {8, 2, 13, 7}
Is Abelian:  True
Is Cyclic:  False
Subgroups:  [{1}, {1, 4}, {8, 1, 2, 4}, {1, 11}, {1, 4, 13, 7}, {1, 14}, {1, 11, 4, 14}, {1, 2, 4, 7, 8, 11, 13, 14}]
Centre:  {1, 2, 4, 7, 8, 11, 13, 14}
Generators:  set()
Normal Subgroups:  [{1}, {1, 4}, {8, 1, 2, 4}, {1, 11}, {1, 4, 13, 7}, {1, 14}, {1, 11, 4, 14}, {1, 2, 4, 7, 8, 11, 13, 14}]
Is Simple:  False


Is Group:  True
Elements:  {'y', 'e', 'x', 'z'}
Order:  4
Cayley Table: 
 [['e' 'y' 'z' 'x']
 ['y' 'e' 'x' 'z']
 ['z' 'x' 'e' 'y']
 ['x' 'z' 'y' 'e']]
Identity Exist:  True
Identity:  e
Inverses exist:  True
Inverses:  {('x', 'x'), ('y', 'y'), ('e', 'e'), ('z', 'z')}
Self Invertible Elements:  {'y', 'e', 'x', 'z'}
Not Self Invertible Elements:  set()
Is Abelian:  True
Is Cyclic:  False
Subgroups:  [{'e'}, {'y', 'e'}, {'e', 'x'}, {'e', 'z'}, {'y', 'e', 'x', 'z'}]
Centre:  {'y', 'e', 'x', 'z'}
Generators:  set()
Normal Subgroups:  [{'e'}, {'y', 'e'}, {'e', 'x'}, {'e', 'z'}, {'y', 'e', 'x', 'z'}]
Is Simple:  False


Is Group:  True
Elements:  {'-i', 'k', '-k', '-j', '1', '-1', 'j', 'i'}
Order:  8
Cayley Table: 
 [['1' '-1' 'i' '-i' 'j' '-j' 'k' '-k']
 ['-1' '1' '-i' 'i' '-j' 'j' '-k' 'k']
 ['i' '-i' '-1' '1' 'k' '-k' '-j' 'j']
 ['-i' 'i' '1' '-1' '-k' 'k' 'j' '-j']
 ['j' '-j' '-k' 'k' '-1' '1' 'i' '-i']
 ['-j' 'j' 'k' '-k' '1' '-1' '-i' 'i']
 ['k' '-k' 'j' '-j' '-i' 'i' '-1' '1']
 ['-k' 'k' '-j' 'j' 'i' '-i' '1' '-1']]
Identity Exist:  True
Identity:  1
Inverses exist:  True
Inverses:  {('-1', '-1'), ('-k', 'k'), ('-i', 'i'), ('1', '1'), ('-j', 'j')}
Self Invertible Elements:  {'-1', '1'}
Not Self Invertible Elements:  {'-i', 'k', '-k', '-j', 'j', 'i'}
Is Abelian:  False
Is Cyclic:  False
Subgroups:  [{'1'}, {'-1', '1'}, {'-i', '-1', 'i', '1'}, {'-j', '-1', 'j', '1'}, {'-k', '-1', 'k', '1'}, {'-i', 'k', '-k', '-j', '1', '-1', 'j', 'i'}]
Centre:  {'-1', '1'}
Generators:  set()
Normal Subgroups:  [{'1'}, {'-1', '1'}, {'-i', '-1', 'i', '1'}, {'-j', '-1', 'j', '1'}, {'-k', '-1', 'k', '1'}, {'-i', 'k', '-k', '-j', '1', '-1', 'j', 'i'}]
Is Simple:  False

Is Group: True
Elements: {0, 1, 2, 3, 4}
Order: 5
Cayley Table: [[0. 1. 2. 3. 4.]
 [1. 2. 3. 4. 0.]
 [2. 3. 4. 0. 1.]
 [3. 4. 0. 1. 2.]
 [4. 0. 1. 2. 3.]]
Identity Exist: True
Identity: 0
Inverses exist: True
Inverses: {(3, 2), (4, 1), (0, 0)}
Self Invertible Elements: {0}
Not Self Invertible Elements: {1, 2, 3, 4}
Is Abelian: True
Is Cyclic: True
Subgroups: [{0}, {0, 1, 2, 3, 4}]
Centre: {0, 1, 2, 3, 4}
Generators: {1, 2, 3, 4}
Normal Subgroups: [{0}, {0, 1, 2, 3, 4}]
Is Simple: True

{'Is Group': True,
 'Elements': {permutation.Permutation(2, 3, 1),
  permutation.Permutation(2, 1),
  permutation.Permutation(3, 1, 2),
  permutation.Permutation(3, 2, 1),
  permutation.Permutation(1, 3, 2),
  permutation.Permutation()},
 'Order': 6,
 'Cayley Table': array([[permutation.Permutation(), permutation.Permutation(2, 1),
         permutation.Permutation(1, 3, 2),
         permutation.Permutation(3, 1, 2),
         permutation.Permutation(2, 3, 1),
         permutation.Permutation(3, 2, 1)],
        [permutation.Permutation(2, 1), permutation.Permutation(),
         permutation.Permutation(2, 3, 1),
         permutation.Permutation(3, 2, 1),
         permutation.Permutation(1, 3, 2),
         permutation.Permutation(3, 1, 2)],
        [permutation.Permutation(1, 3, 2),
         permutation.Permutation(3, 1, 2), permutation.Permutation(),
         permutation.Permutation(2, 1), permutation.Permutation(3, 2, 1),
         permutation.Permutation(2, 3, 1)],
        [permutation.Permutation(3, 1, 2),
         permutation.Permutation(1, 3, 2),
         permutation.Permutation(3, 2, 1),
         permutation.Permutation(2, 3, 1), permutation.Permutation(),
         permutation.Permutation(2, 1)],
        [permutation.Permutation(2, 3, 1),
         permutation.Permutation(3, 2, 1), permutation.Permutation(2, 1),
         permutation.Permutation(), permutation.Permutation(3, 1, 2),
         permutation.Permutation(1, 3, 2)],
        [permutation.Permutation(3, 2, 1),
         permutation.Permutation(2, 3, 1),
         permutation.Permutation(3, 1, 2),
         permutation.Permutation(1, 3, 2), permutation.Permutation(2, 1),
         permutation.Permutation()]], dtype=object),
 'Identity Exist': True,
 'Identity': permutation.Permutation(),
 'Inverses exist': True,
 'Inverses': {(permutation.Permutation(), permutation.Permutation()),
  (permutation.Permutation(1, 3, 2), permutation.Permutation(1, 3, 2)),
  (permutation.Permutation(2, 1), permutation.Permutation(2, 1)),
  (permutation.Permutation(2, 3, 1), permutation.Permutation(3, 1, 2)),
  (permutation.Permutation(3, 2, 1), permutation.Permutation(3, 2, 1))},
 'Self Invertible Elements': {permutation.Permutation(2, 1),
  permutation.Permutation(3, 2, 1),
  permutation.Permutation(1, 3, 2),
  permutation.Permutation()},
 'Not Self Invertible Elements': {permutation.Permutation(2, 3, 1),
  permutation.Permutation(3, 1, 2)},
 'Is Abelian': False,
 'Is Cyclic': False,
 'Subgroups': [{permutation.Permutation()},
  {permutation.Permutation(2, 1), permutation.Permutation()},
  {permutation.Permutation(1, 3, 2), permutation.Permutation()},
  {permutation.Permutation(2, 1),
   permutation.Permutation(1, 3, 2),
   permutation.Permutation()},
  {permutation.Permutation(2, 3, 1),
   permutation.Permutation(3, 1, 2),
   permutation.Permutation()},
  {permutation.Permutation(3, 2, 1), permutation.Permutation()},
  {permutation.Permutation(2, 1),
   permutation.Permutation(3, 2, 1),
   permutation.Permutation()},
  {permutation.Permutation(3, 2, 1),
   permutation.Permutation(1, 3, 2),
   permutation.Permutation()},
  {permutation.Permutation(2, 3, 1),
   permutation.Permutation(2, 1),
   permutation.Permutation(3, 1, 2),
   permutation.Permutation(3, 2, 1),
   permutation.Permutation(1, 3, 2),
   permutation.Permutation()}],
 'Centre': {permutation.Permutation()},
 'Generators': set(),
 'Normal Subgroups': [{permutation.Permutation()},
  {permutation.Permutation(2, 3, 1),
   permutation.Permutation(3, 1, 2),
   permutation.Permutation()},
  {permutation.Permutation(2, 3, 1),
   permutation.Permutation(2, 1),
   permutation.Permutation(3, 1, 2),
   permutation.Permutation(3, 2, 1),
   permutation.Permutation(1, 3, 2),
   permutation.Permutation()}],
 'Is Simple': False}

```

## Group Visualization

### Integers under addition modulo, Z<sub>n</sub>

<img src="https://github.com/priyanshupant/group-theory/assets/50315906/9301910f-4b0d-4b79-8d87-a1ab7656a483" width="300" ><img src="https://github.com/priyanshupant/group-theory/assets/50315906/d5e2c7ed-ef51-4aab-a9ac-2709ab1133be" width="300" ><img src="https://github.com/priyanshupant/group-theory/assets/50315906/a282d2ee-a68e-4a69-91fb-07d74df12a79" width="300" >


### Integers under multiplication modulo, U<sub>n</sub>

<img src="https://github.com/priyanshupant/group-theory/assets/50315906/aa9de9b8-8b3f-4867-a05d-fdb8bf65a2fe" width="300" ><img src="https://github.com/priyanshupant/group-theory/assets/50315906/504aab43-ad9f-4a17-9649-298b3582a332" width="300" ><img src="https://github.com/priyanshupant/group-theory/assets/50315906/91449964-98de-42fb-8675-0d6d5a645ede" width="300" >


### Klein's four group, K<sub>4</sub>
![image](https://github.com/priyanshupant/group-theory/assets/50315906/1783341c-7860-4f19-b56d-d1448eb5cdb1)


### Quaternion group, Q<sub>8</sub>
![image](https://github.com/priyanshupant/group-theory/assets/50315906/c4dff4a9-9bfe-48ef-b7f1-7cece11e5703)


### Symmetry group, S<sub>n</sub>
![image](https://github.com/priyanshupant/group-theory/assets/50315906/f5b7337b-125b-4f8e-a910-33d09e734689)
![image](https://github.com/priyanshupant/group-theory/assets/50315906/73e25ae0-d84a-498b-b08c-f6f499f3bf56)




## **Contribution**

Contributions are welcome! Feel free to fork the repo.

## **License**

This project is licensed under the [MIT License.](https://github.com/priyanshupant/group-theory/blob/main/LICENSE)
