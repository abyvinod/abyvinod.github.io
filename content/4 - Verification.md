title: What is verification?
date: 2017-1-8
tags: Verification
category: Control Theory
author: Abraham Vinod
summary: Discussing the two view points in verification --- the computer science view point and the controls view point

## Verification 

Formal verification is the process of mathematically checking that the behavior
of a system, described using a formal model, satisfies a given property, also
described using a formal model. The two models may or may not be the same, but
must share a common semantic interpretation. The ability to carry out formal
verification is strongly affected by the model of computation, which determines
decidability and complexity bounds[^EdwardIEEE1997].

Loosely, verification is meant to provide guarantees of safety (nothing bad will
happen), liveness (task completion --- eventually something good will happen)
for safety critical systems and other systems that need guarantees of their
    proper operations. These are generally embedded systems which have
    components that evolve continuously in time and discrete in time. Therefore,
    researchers generally use hybrid dynamical systems framework to model the
    system. 

Historically, there has been two approaches in dealing with the problem of
verification.

### Control theory point of view

Verification is posed as a reach avoid problem where the objective is identify
the initial conditions and the corresponding control policies under which the
hybrid system will hit a target set while avoiding an unsafe set over a finite
time horizon. The problem also depends on whether the hybrid system is
stochastic/deterministic and continuous-/discrete-time system. For discrete-time
stochastic hybrid systems[^myInterest], the control policies try to maximize the probability
of achieving the reach avoid objective[^SummersAutomatica2010].

For stochastic hybrid
systems, the problem is posed as a Markov decision process and use dynamic
programming to identify the initial conditions and the optimal control policies.
However, due to the curse of dimensionality, the application of verification is
mostly limited to low dimensional systems. Active research is being done on
developing approximations and exact methods to do verification of
high-dimensional systems.


### Computer science point of view  


Disclaimer: I have only seen the research from this point of view from the
sidelines. In other words, I am no expert on this point of view. I would like to
acknowledge Sumanth's contributions for helping improve this section. 

For hybrid systems, it is not straightforward to apply traditional formal
methods for verification, such as model checking[^ClarkeBook1999] and deductive
verification[^KaufmannBook2000], to hybrid systems since these methods were
originally developed for circuits, and communication protocols
and usually require extensive search of all reachable states.  However, this is
not possible as the states in hybrid systems are uncountable[^LinBook2000]. One
approach used in this camp tackle the problem by modeling the hybrid system as a
finite state automation using abstraction techniques. Other approaches include
using SMT solvers and probabilistic model checkers[^Caution]. Do check out these
interesting links ---
[Distinguishing Decision Procedure vs SMT solver vs Theorem prover vs Constraint
solver](http://cs.stackexchange.com/questions/14946/distinguish-decision-procedure-vs-smt-solver-vs-theorem-prover-vs-constraint-sol)
and [dReach](http://dreal.github.io/dReach/). Some good books in these topics
are [Klaus Schneider's Verification of reactive
systems](http://www.springer.com/us/book/9783540002963), [Gerard J. Holzmann's
Design And Validation Of Computer
Protocols](https://www.amazon.com/Design-Validation-Computer-Protocols-Holzmann/dp/0135399254),
and [Amir Pneuli's books](http://cs.nyu.edu/cs/faculty/pnueli/books.html).

## Conclusion

Irrespective of the approach, the goal of these two research camps are the same
--- provide concrete proof that our intuition-based designs/heuristics will
actually be safe.


<!--
[^MitchellLvlSet]: [https://www.cs.ubc.ca/~mitchell/ToolboxLS/](https://www.cs.ubc.ca/~mitchell/ToolboxLS/)
For deterministic continuous-time systems, the reach-avoid problem can solved
using Level set toolbox methods[^MitchellLvlSet]. -->

[^EdwardIEEE1997]: [Proceedings of IEEE 1997, Edward et.  al](ieeexplore.ieee.org/document/558710)
[^SummersAutomatica2010]: [Automatica 2010, Summers et.
al](http://linkinghub.elsevier.com/retrieve/pii/S0005109810003547)
[^myInterest]: This is the type of systems I work with.
[^ClarkeBook1999]: [Model checking by Clarke et. al, 1999](dl.acm.org/citation.cfm?id=332656)
[^KaufmannBook2000]: [Computer Aided Reasoning: An Approach by Kaufmann et.  al.](http://dl.acm.org/citation.cfm?id=555902)
[^LinBook2000]: [Hybrid Dynamical Systems: An Introduction to Control and Verification, Lin et.  al](www.nowpublishers.com/article/Details/SYS-001)
[^Caution]: At this point, I am really out of my depth. 
