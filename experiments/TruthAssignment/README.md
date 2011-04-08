Truth Assigments in Classical Propositional Logic
=================================================


Author: [Adolfo Neto](http://twitter.com/adolfont)


Objective
---------

To implement truth assignments for classical propositional logic formulas.


What is a Truth Assigment?
--------------------------

There are two definitions of truth assignments in [1]. 

### First definition

The first definition says that a truth assignment is a function from the set of propositions (P)
to the set of truth-values {0, 1} (a proposition is also called an atomic formula).

Therefore, a valuation v can be written as:

v: P -> {0, 1}

#### An example of a valuation

Given that P={p1, p2, p3}. A valuation v1 can be defined as:

- v1(p1)=0
- v1(p2)=1
- v1(p3)=1

### Second definition

The second definition extends the definition of truth assignments to be functions from the set of formulas (L_LPC)
to the set of truth-values.

The valuation of a non-atomic formula can be obtained form the valuation of the atomic formulas that are its 
subformulas. For any non-atomic formula P:

- v(!P) = 1 - v(P)
- v((P&Q)) = 1 if and only if v(P)=1 and v(Q)=1. Otherwise, v((P&Q))=0.
- v((P|Q)) = 1 if v(P)=1 or v(Q)=1. Otherwise, v((P|Q))=0.
- v((P->Q)) = 0 if v(P)=1 and v(Q)=0. Otherwise, v((P->Q))=1.


#### A second example of a valuation

Given that P={p1, p2, p3}. A valuation v2 can be defined as:

- v2(p1)=1
- v2(p2)=1
- v2(p3)=0

From this definition we can extend v2, for instance, to the following composite formulas:

- v2(!p1)=0
- v2(!!p1)=1
- v2(!!!p1)=0
- v2((p1&p2))=1
- v2((p1->p3))=0
- v2((p1->!p3))=1
- v2((!p1|!p2))=0
- v2(((p1->!p3)->(!p1|!p2)))=0


References
----------

[1] SILVA, Flávio S. C. da; FINGER, Marcelo; MELO, Ana C. V. de. Lógica para Computação. São Paulo: Thomson Learning, 
2006.



