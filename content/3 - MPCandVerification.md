Title: Similarities between model predictive control and verification theory
date: 2017-1-9
tags: Verification, Model Predictive Control
category: Control Theory
author: Abraham Vinod
summary: Surprising overlap between two subfields of control theory

One of my major research projects is on verification of dynamical systems.
Specifically, I am interested in characterizing the set of initial conditions
for a given dynamical system which can be driven such that the state reaches a
    certain target subset of the state space while avoiding certain unsafe
    subsets of the state space --- the reach-avoid objective. Needless to say,
    solving this problem manifests in a lot of real-world challenges where a
    certificate of task completion and/or safety is required.

As always, I thought (wrongly) this field was insular in the sense that it is a
unique problem worked on only by my peers.

The other day, I was reading an Automatica paper[^GoulartAutomatica2006]. This well-written paper in the robust MPC literature
discusses optimal control problems on linear systems with disturbance with a
reach-avoid like objective (Polytopic target and safe sets).
<!--- Some interesting results (at least I was not aware of it):
+ Two parameterizations of the control policies discussed--- Affine state-feedback parameterization (ASFP) and affine disturbance feedback parameterization (ADFP)
+ ASFP is desired, but the resulting optimal control formulation is generally nonconvex
+ ADFP is equivalent to ASFP and the resulting optimal control formulation is actually convex (and tractable).
+ Guarantees of constraint satisfaction for MPC based on open loop control in a receding time horizon requires invariance conditions on the terminal set --- Assumption 1 in the paper.
-->

On the other hand, a similar effort was done in the verification
side[^verificationBlogPost] which proposed a time-dependent differential game
setup to answer the question of reach-avoid objective[^MitchellTAC2005].

It is interesting to see totally different takes on essentially the same
problem.

[^GoulartAutomatica2006]: [Automatica 2006, Goulart et. al
](http://www.sciencedirect.com/science/article/pii/S0005109806000021)
[^MitchellTAC2005]: [Transactions on Automatic Control 2005, Mitchell et. al](http://ieeexplore.ieee.org/document/1463302/)
[^verificationBlogPost]: My familiarity is on [verification from control theory
point of view]({filename}4 - Verification.md).
