# Novel Quadratic Constraints for Extending LipSDP beyond Slope-Restricted Activations

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Recently, semidefinite programming (SDP) techniques have shown great promise in providing accurate Lipschitz bounds for neural networks. Specifically, the LipSDP approach (Fazlyab et al., 2019) has received much attention and provides the least conservative Lipschitz upper bounds that can be computed with polynomial time guarantees. However, one main restriction of LipSDP is that its formulation requires the activation functions to be slope-restricted on $[0,1]$, preventing its further use for more general activation functions such as GroupSort, MaxMin, and Householder. One can rewrite MaxMin activations for example as residual ReLU networks. However, a direct application of LipSDP to the resultant residual ReLU networks is conservative and even fails in recovering the well-known fact that the MaxMin activation is 1-Lipschitz. Our paper bridges this gap and extends LipSDP  beyond slope-restricted activation functions. To this end, we provide novel quadratic constraints for GroupSort, MaxMin, and Householder activations via leveraging their underlying properties such as sum preservation. Our proposed analysis is general and provides a unified approach for estimating $\ell_2$ and $\ell_\infty$ Lipschitz bounds for a rich class of neural network architectures, including non-residual and residual neural networks and implicit models,  with GroupSort, MaxMin, and Householder activations. Finally, we illustrate the utility of our approach with a variety of experiments and show that our proposed SDPs generate less conservative Lipschitz bounds in comparison to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considered the problem of estimating the Lipschitz constant of neural networks with different kinds of activations that are not slope-restricted. Particularly, the authors investigated multi-layer (residual) networks applied with the GroupSort and Householder activations. The paper followed the idea of thge LipSDP formulation of the Lipschitz parameter estimation problem, and the main contribution is that the authors devised a new quadratic constrained that can deal with GroupSort and Householder which are not slope-restricted. In addition, the authors conducted empirical experiments which showed that the new formulation with quadratic cosntraints outperforms traditional matrix-product algorithms in terms of the accuracy of the estimated Lipschitz parameter.

### Strengths
The paper is written clearly and the authors provided useful intuiation.

The new quadratic constraints enabled us to estimate the Lipschitz constants of neural networks with GroupSort or Householder activations with higher accuracy compared to traditional algorithms.

In addition, the authors considered both $\ell_2$ and $\ell_\infty\to\ell_1$ lipschitz constants.

### Weaknesses
The result seems to be weak since the quadratic constraints only applied to 2 specific activations. It would be more interesting if it can be applied to a class of activaitons. The current approach, while novel for GroupSort and Householder activations, lacks generality. The core contribution is limited by its narrow scope, as it does not provide a framework that can be easily extended to other non-slope-restricted activations. This limits the impact of the work, as the developed constraints are highly specialized. The paper would benefit from a discussion on the limitations of the proposed quadratic constraints and potential avenues for generalizing the approach to a broader class of activations. For instance, it is unclear whether the proposed method can be adapted to other activation functions with similar characteristics, such as those involving sorting or other non-linear operations. The lack of a clear path for generalization significantly reduces the practical applicability of the proposed method.

### Questions
How does the new formaulation compare to the original LipSDP for MaxMin networks in terms of computational efficiency/runtime?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents new semi-definite programs for computing upper-bounds on
the Lipschitz constants of deep neural networks with gradient-preserving
activations.  The authors derive new quadratic constraints which extend the
state-of-the-art LipSDP framework to Lipschitz estimation with the GroupSort,
MaxMin, and Householder activation functions; these activations were previously
not covered by LipSDP since they do not satisfy the slope-restricted property.
The authors then extend their approach to compute Lipschitz constants in the
$\ell_\infty$ norm and show how to apply their results to neural networks with
residual connections. Experiments confirm the empirical performance of the
proposed SDPs.

### Strengths
This is an interesting submission which extends the existing LipSDP framework
for estimating Lipschitz constants of neural networks to new activation
functions. The authors use the quadratic constraint approach from control
theory to obtain polynomial-time algorithms for the GroupSort and Householder 
activations (these generalize the MaxMin activation). As only naive estimation
approaches previously existed for these activations, this contribution is fairly
strong and represents the major strength of this paper.

Other notable strengths are the following:

- The proposed SDPs yield upper-bounds for small networks which are close to
    those obtained by brute-force search over the activation space, particularly
    for the $\ell_2$-norm. Moreover, the bounds are much tighter than those
    obtained using operator norms.

- The methodology is presented clearly and the manuscript is polished.

### Weaknesses
The major limitation of this work is the restriction to Householder and
GroupSort activations. The utility of extending the LipSDP framework to these
activation depends directly on the how interesting the problem of Lipschitz
estimation is for neural networks using these architectures. While the authors
state that such activations are becoming popular for the design of Lipschitz
neural networks, no concrete examples are provided. I am also concerned about
the following:

- The basic idea of LipSDP was developed by Fazlyab et al. (2019) while the 
    extension to estimation in the $\ell_\infty$ norm is from Wang et al. (2022).
    The main theoretical contribution of this work is to develop new quadratic
    constraints which fit into those frameworks, rather than build significantly
    on top of them. Thus, the paper may be somewhat incremental in nature.

- The authors do not provide the computation time for the naive baseline method
    for approximating Lipschitz constants based on operator norms (MP),
    so it is not clear what the trade-off between computation and accuracy is
    for the proposed method.

I am hesitant to recommend this submission for acceptance without additional 
evidence that the Householder and GroupSort activations are of practical
interest for Lipschitz estimation (see "Questions").
Moreover, this paper is outside of my research area so it is difficult for me
to judge its theoretical novelty; I did not check the proofs for correctness
for the same reason. Given this, and the smaller issues raised above, I am
 on the fence regarding this submission.

### Questions
As noted above, I am not a expert on Lipschitz constant estimation for neural
networks nor have I made use of algorithms from this area. Given this, can the
authors please provide additional details on why the GroupSort and Householder
activations are of particular interest for Lipschitz constant estimation? Since
these activations are the exclusive focus of the paper, I feel there must be an
immediate desire from the community to solve this problem in practice for
the paper to have a significant impact.

I would also appreciate it if the authors could provide running times for the
naive estimation strategies in Table 1; this well help contextualize the cost
of LipSDP-NSR and clarify the trade-off between accuracy and compute time. 

Finally, perhaps the authors can comment on the difficulty of deriving
the quadratic constraints for the SDPs. This will help me understand the novelty
of the theoretical contributions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends the method of estimating the Lipschitz constant of a neural network using semidefinite programming (SDP) to the networks with non-slope-restricted activations functions such as GroupSort, Maxmin, and Householder. The SDP formulations are proposed for estimating $l_2$ and $l_\infty/l_1$ Lipschitz constants for various network architectures.

### Strengths
1. well-written, easy to follow even for a non-expert.
2. The extension of LipSDP to GroupSort, Maxmin, and Householder activations is new.

### Weaknesses
The main concern I have is that this paper seems to be an extension of two works Fazlyab'19 and Wang'22 to the case of having sum-preserving activations like GroupSort, Maxmin, and Householder, which seems incremental. The core idea of using semidefinite programming (SDP) to estimate Lipschitz constants is not new, and the paper's contribution lies primarily in adapting this framework to handle these specific activation functions. While the authors provide SDP formulations for $l_2$ and $l_\infty/l_1$ Lipschitz constants, the novelty seems limited to the specific constraints derived for GroupSort, Maxmin, and Householder. The paper does not sufficiently address the practical implications of these extensions, such as whether these new formulations lead to tighter bounds compared to existing techniques or whether they offer any computational advantages. It is unclear if the proposed method provides a significant improvement over simply using existing Lipschitz estimation techniques in conjunction with a relaxation or approximation of these activations.

### Questions
1. How frequently are GroupSort, Maxmin, and Householder being used in practice? If they are not so popular, why we are studying LipSDP for them?
2. This is merely a comment. The results would be more interesting and valuable if using GroupSort, Maxmin, and Householder activations have some implicit bias towards having an NN with a smaller Lipschitz constant.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
