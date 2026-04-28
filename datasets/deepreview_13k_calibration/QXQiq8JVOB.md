# Hamiltonian Mechanics of Feature Learning: Bottleneck Structure in Leaky ResNets

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
We study Leaky ResNets, which interpolate between ResNets ($\tilde{L}=0$)
and Fully-Connected nets ($\tilde{L}\to\infty$) depending on an 'effective
depth' hyper-parameter $\tilde{L}$. In the infinite depth limit,
we study 'representation geodesics' $A_{p}$: continuous paths in
representation space (similar to NeuralODEs) from input $p=0$ to
output $p=1$ that minimize the parameter norm of the network. We
give a Lagrangian and Hamiltonian reformulation, which highlight the
importance of two terms: a kinetic energy which favors small layer
derivatives $\partial_{p}A_{p}$ and a potential energy that favors
low-dimensional representations, as measured by the 'Cost of Identity'.
The balance between these two forces offers an intuitive understanding
of feature learning in ResNets. We leverage this intuition to explain
the emergence of a bottleneck structure, as observed in previous work:
for large $\tilde{L}$ the potential energy dominates and leads to
a separation of timescales, where the representation jumps rapidly
from the high dimensional inputs to a low-dimensional representation,
move slowly inside the space of low-dimensional representations, before
jumping back to the potentially high-dimensional outputs. Inspired
by this phenomenon, we train with an adaptive layer step-size
to adapt to the separation of timescales.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the feature learning dynamics in Leaky ResNets, a variant of ResNets with tunable skip connections, by examining how the network’s representations evolve under an "effective depth" parameter, \tilde L. The authors identify a bottleneck phenomenon, where which high-dimensional inputs compress into low-dimensional representations before expanding back to high-dimensional outputs. The study cast the depth-dynamics of the network representation in Lagrangian and Hamiltonian form, defining kinetic and potential energy terms to explain the aforementioned bottleneck phenomenon. In particular, the authors introduce the "cost of identity" (COI) as a measure of dimensionality within the network, relating it to the Hamiltonian through a separation of timescales argument in the limit of large \tilde L, identifying a "fast" initial/final phase of compression/decompression and a "slow", low-dimensional phase for the representation geodesics of the network.

### Strengths
1. The paper introduces the reader to the main concepts in an incremental and understandable way, relating these quantities in a clear way, and clearly explains the results it presents, clearly stating their limitations. The results are proven rigorously.
2. The paper features the occurrence of the "bottleneck phenomenon" in leaky resnets by elegantly framing the representation geodesics into a Lagrangian and Hamiltonian framework and analyzing the resulting dynamics in the large L limit. While the Hamiltonian formulation was admittedly developed in a previous reference, the definition of a family of networks indexed by the parameter \tilde L and the identification of a separation of timescales in its dynamics is both nontrivial and original.
3. The decomposition of the Lagrangian into a "potential energy" and "kinetic energy" terms appeals to the intuition and allows to identify different regimes in the propagation of representations in the network. Furthermore, the "cost of identity" is clearly related to the potential energy, and the landscape is studiet in some detail.
4. The authors provide numerical experiments that illustrate nicely some of the results presented in the paper.

### Weaknesses
1. The paper could benefit from a revision of the main results' statements. For example, in Theorem 4 "for sequence" could be interpreted as "for A sequence" or "for ANY sequence". It is also unclear if the second display should hold for all $p$'s. Furthermore, section 2.1 feels a bit rushed with respect to the nicely paced exposition in the rest of the paper, especially in the motivation for some statements.
2. Theorem 4 is stated for constant \gamma, but the authors mention that it might be of interest to adapt $\gamma$ as a function of $p$. In this sense, it is unclear what the relationship between the two statements is, and if a similar results as in Theorem 4 should hold when $\gamma$ depends on $p$. 
3. The decomposition of the Hamiltonian at the beginning of Section 2.1 seems to follow from its definition at the end of section 1.5. This decomposition is central to the following analysis, so it would be helpful if the authors could show the main steps of this derivation.
4. It is not always transparent from the statement of Theorem 4 and the subsequent discussion what the scaling of the various quantities are in $\tilde L$, so it is not always clear if the bounds that the theorem presents are tight. For instance, one may naively expect that the term $\ell_{\gamma,\tilde L}$ might be of order $1/\gamma$, inheriting from the (worst-case) scaling of the norm in the integral. Choosing $\gamma = 1/\tilde L$ would result in term on the LHS of the first expression in Theorem 4 that is $O(1)$ (killing the term \gamma c). 
5. It is not clear how much of the assumptions made in the discussion contained in Section 2 are actually respected in practical scenarios. The simulations seem to corroborate the results presented in the main theorems, but it is difficult to assess how generic this behavior is in practice.

### Questions
1. Please expand why is it natural to scale $\gamma_p$ with $\|K_p\|$ and how this relates 
2. Please describe the scaling in \tilde L of the quantities in Theorem 4
3. Is the "naive" intuition presented in pt. 4. of the "weaknesses" section valid? If no, why? If yes, is the bound optimal in some sense, i.e., why can we not get rid of that $O(1)$ term?
4. Why can we safely assume that the length $\ell_{\gamma, \tilde L}$ is uniformly bounded in \tilde L if we choose $\gamma = 1/\tilde L$?
5. Can you please expand on how generic are the assumptions made in the main body of section 2?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on Leaky ResNets, which interpolate between ResNets and FCNNs. It reformulates the optimization of Leaky ResNets into Lagrangian and Hamiltonian forms, highlighting the significance of kinetic and potential energy terms related to the cost of identity. The work provides an explanation for the emergence of the bottleneck structure in ResNets and proposes an adaptive layer step-size training approach. However, the connection between the analysis of the bottleneck structure and the Leaky ReLU network could be more explicit, and the practical implications of the proposed method are not entirely clear.

### Strengths
1. **Theoretical novelty**: The paper offers a novel theoretical perspective on understanding the behavior of neural networks, specifically the bottleneck structure, through the lens of Hamiltonian mechanics. This provides a new framework for analyzing and potentially optimizing network architectures.
2. **Clear explanations**: The concepts of cost of identity, kinetic energy, and potential energy are well-defined and effectively related to the network's dynamics. This helps in building an intuitive understanding of the forces at play during feature learning.

### Weaknesses
**Limited empirical evaluation**: The experimental setup is relatively simplistic and based on synthetic data. The impact of the proposed method appears to be marginal as indicated by the figures, raising questions about its practical significance and generalizability to more complex real-world scenarios.
2. **Connection to Leaky ReLU network**: The link between the in-depth analysis of the bottleneck structure and the Leaky ReLU network is not clearly elucidated. It is not evident how the unique characteristics of the Leaky ReLU activation function contribute to or interact with the observed phenomena. 
3. **Lack of practical problem focus**: It is unclear what practical problem the paper is primarily addressing. While the exploration of the bottleneck structure is interesting theoretically, the practical benefits and applications of enhancing or understanding this behavior are not well-articulated.

### Questions
1. Could you further clarify the relationship between the Leaky ReLU activation and the emergence of the bottleneck structure?  
2. In the context of practical applications, what are the potential advantages of explicitly considering the bottleneck structure and the proposed training method? Are there specific domains or tasks where this could have a more significant impact?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors study the evolution of the feature representation $(A_p)_p$ across layers of an infinite-depth 
Leaky ResNet. First, they show that the $l^2$-regularization term in the loss function can be approximately decomposed into
two terms --- Cost of Identity (COI) and kinetic energy --- which favor low-dimensional $A_p$ and $A_p$ with a small 
layer derivative $\partial_p A_p$, respectively. By analyzing the interplay of these two quantities and the corresponding 
Hamiltonian, the authors show that when the effective depth is large, the behavior of $(A_p)_p$ can be classified into 
two types: when the COI/rank of $A_p$ is small (resp. large), $A_p$ will change quickly (resp. slowly). Finally, they 
propose a discretization scheme for infinite-depth Leaky ResNet based on this observation.

### Strengths
The observations and the interpretation of the COI and kinetic energy are interesting. In particular, by leveraging the 
conservation of the Hamiltonian, the authors uncover a trade-off between a large intermediate dimension and a 
rapidly evolving intermediate representation. This trade-off appears fundamental and could potentially lead to 
new algorithm (such as the discretization scheme the authors provide in Section 3) and/or offer new insights into 
the inner feature representation of Leaky ResNets.

### Weaknesses
* This paper seems to be a collection of observations based on the intuitions surrounding the COI and kinetic energy. 
  It is unclear whether these observations can lead to meaningful implications for any theoretical or empirical problem. 
  In addition, the formal results in this paper require additional assumptions and/or certain approximations and do 
  not precisely match the intuitive arguments. 
  It would be helpful if the authors could at least provide a toy example to illustrate the validity of the intuitions 
  and the usefulness of the results in this paper. 
* The argument and results mainly focus on the $l^2$-regularization term and do consider the regression part of the loss. 
  It is unclear if the observations in this paper would still hold when the network needs to actually 
  use the representations to fit the target function. 
* The structure of the paper could be improved. It might be good to gather the main results in one place and 
  explain their relationship, rather than having them scattered across different sections, separated by more technical 
  results.

### Questions
* See the Weakness part of the review.
* Could you explain the derivation (the backward equation and the joint dynamics) at the top of page 7?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors consider a particular limit of residual networks which they term "Leaky ResNets" with an $L_2$ weight regularization term, which they relate to an effective depth of this network. By a change of variables into the representation space, they rewrite the behavior of the representations into a Lagrangian formulation with certain boundary conditions. They split the Lagrangian into three terms
1. A potential term which they call "cost of identity" (COI) which prefers small representations
2. A kinetic term that prefers slowly changing representations
3. A cross-term that they claim to be unimportant. 

They then show that the COI has some relationship to well-known norms and show that strict local minima might be preferred due to their separation from saddle points. 

At this stage they derive a Hamiltonian which explains both the forward and reverse dynamics of the network. They use the form of $H$ to argue that some layers will correspond to slow and others to fast dynamics, while the dimension of the limiting representations then allow an approximation of the Hamiltonian.

They close with a discussion of adaptive discretization schemes to convert these ODEs into neural networks, along with a student-teacher example showing that adaptive size leads to better test accuracy.

### Strengths
This paper develops the Lagrangian and Hamiltonian perspectives on leaky ResNets in a transparent way and offers important qualitative arguments about their structure. Furthermore the setting they consider isn't so removed from a realistic case -- in particular the data is not treated with undue approximation and results are general.

### Weaknesses
The critical weakness of this paper is its presentation. For one, it is not clear what is novel, particularly in light of the fact that the Hamiltonian and Lagrangian formulations have been discussed before (though the derivation is the most transparent I have seen in my review). Additionally, the idea of the "cost of identity" in general is well known, so more care could be taken to contextualize the background and new contribution. The second impediment to understanding this contribution is the somewhat poor presentation of the work. 

1. Some claims are made without a clear foundation, such as those about the "middle term " on line 171 or the source of cancellations in the Lagrangian on line 207.
2. The relationship between the action at line 161 and the Hamiltonian at line 335 and the other at line 372 is unclear. 
3. The discussion in the final three pages of the "main contributions" (line 342) is incomplete. For example, it's unclear why better discretization is better and in what cases we may expect this kind of adaptive re-discretization to be helpful.

### Questions
1. Why does the limiting representation have to be an integer?
2. Can we derive the Hamiltonian directly from the Lagrangian in the normal way?
3. Are the introduction of the action and two Hamiltonians novel (in that they either haven't appeared in this way before, or that the derivation is particularly transparent, or in some other way)? 
4. Why are the behaviors of the representations at the endpoints unimportant when the representations are not necessarily fixed at the endpoints as $A_1$ is a dynamical quantity?
5. What is the "physical" interpretation of a negative (unbounded from below) potential energy?
6. Is there a standard way to solve the equations of notion at 331 given that we have boundary conditions for $A$ at 0 and $B$ at 1?

### Soundness
2

### Presentation
2

### Contribution
3
