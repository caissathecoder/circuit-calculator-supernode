# Supernode Circuit Calculator
A simple supernode circuit calculator using Python 3.7, cmath, numpy, PyQt5. Algorithm used: Modified Nodal Analysis (MNA)

## About
#### Technological University of the Philippines - Manila
#### College of Engineering
#### Electronics Engineering Department
A.Y. 2019-2020 - Second Semester

ACECE 6 | Electrical Circuits II

BSECE 2A

Instructor: Mr. Lejan Alfred Enriquez, ECE

## Members
- Paulino, Beaver B. 
- De Luna, Allyze Marie M.
- Soriano, Toni Rose M.
- Palabrica, Reneleo Martin S.
- Buenavista, John Marco P.
- Butlig, Dexter N.

## Language Used
Python 3.7

## Library Used
- cmath
- numpy
- PyQt5

## Algorithm Used
Modified Nodal Analysis with Reactive Elements


# What is Modified Nodal Analysis (MNA)?
MNA applied to a circuit with only passive elements (such as resistors, capacitors, and inductors) and independent current and voltage sources results in a matrix of the form:
**Ax=B**

### The A matrix
- is (n+m)x(n+m) in size, and consists only of known quantities.
- the nxn part of the matrix:
  1. has only passive elements
  2. elements connected to ground (appear only to diagonal)
  3. elements not connected to the ground and off-diagonal terms.
- the rest of matrix A (mxm) contains only 1, -1, and 0. (other values are considered if there are dependent current and/or voltage sources).

### The x matrix:
- an (n+m)x1 vector, consists of unknown quantities.
- the top n elements are the n node voltages.
- the bottom m elements are the m independent elements.

### The B matrix: 
- an (n+m)x1 vector, consists of known quantities.
- the top n elements are either 0 or the sum and difference of independent current sources in the circuit.
- the bottom m elements represent the m independent voltage sources in the circuit.

The circuit can be solved by a simple matrix manipulation: **x=A^(-1)B**
