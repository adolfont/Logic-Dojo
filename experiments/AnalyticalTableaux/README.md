An Analytical Tableaux Prover for Classical Propositional Logic
===============================================================

Author: [Adolfo Neto](http://twitter.com/adolfont)


Objective
-----------------------------------------------

The objective of this experiment is to build an 
[analytical tableaux](http://en.wikipedia.org/wiki/Method_of_analytic_tableaux) prover for classical propositional
logic.

It will receive as input a sequence of signed formulas and it will output a proof tree.


Examples
--------

* Input - a sequence of signed formulas:

<pre>
T A
T A->B
F B
</pre>

* Output - a proof tree:

<pre>
T A
T A->B
F B
 F A
 x

 T B
 x
</pre>


