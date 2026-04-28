# Local convergence of simultaneous min-max algorithms  to differential equilibrium on Riemannian manifold

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 6, 6, 1, 6

## Abstract
We study min-max algorithms to solve zero-sum differential games on
Riemannian manifold.
Based on the notions of
differential Stackelberg equilibrium
and differential Nash equilibrium on Riemannian manifold,
we analyze the local convergence of 
two representative deterministic simultaneous algorithms $\tau$-GDA and $\tau$-SGA
to such equilibrium.
Sufficient conditions are obtained to establish their linear convergence rates 
by Ostrowski theorem on manifold and spectral analysis. 
The $\tau$-SGA algorithm is extended from
the symplectic gradient-adjustment method in Euclidean space
to avoid strong rotational dynamics in $\tau$-GDA.
In some cases, we obtain a faster convergence rate of $\tau$-SGA 
through an asymptotic analysis which is valid when 
the learning rate ratio $\tau$ is big.
We show numerically how the insights obtained from the
convergence analysis may improve
the training of orthogonal Wasserstein GANs using 
stochastic $\tau$-GDA and $\tau$-SGA on simple benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the analysis of the local convergence of two-time-scale $\tau$-GDA and $\tau$-SGA methods to the differential Stakelberg equilibrium (DSE) of Euclidean min-max problem to the Riemannian min-max problem. This paper first generalizes the notion of DSE in the Euclidean space to the Riemannian manifold (in Section 2.1), using a local coordinate chart. Then, the authors provide a sufficient condition (in Theorem 3.1) for the fixed point method to have a local linear convergence. Based on Theorem 3.1, this paper shows a specific sufficient condition for the $\tau$-GDA to locally linearly converge to DSE in Theorem 3.2. In addition, the authors generalize $\tau$-SGA for Riemannian min-max problem, which is originally developed to mitigate undesirable rotational dynamics encountered by $\tau$-GDA in the Euclidean space. In the Euclidean space, extragradient (or optimistic gradient) method is widely used to relieve such rotational behavior, but its Riemannian version, named RCEG, is computationally expensive. This paper claims that their $\tau$-SGA equipped with auto-differentiation may have computational benefit over RCEG. Experiments on a toy example and a more realistic Orthogonal WGAN problem empirically confirm this paper's theoretical findings.

### Strengths
Existing results on local convergence to DSE and DNE in nonconvex-nonconcave min-max problems in Euclidean space are crucial. Thus, while its extension to Riemannian manifolds may seem straightforward, it is a significant and non-trivial advancement. Although I was not able to check all the details of the proof, the parts I checked looked correct.

### Weaknesses
Missing preliminaries for non-experts on Riemannian manifold: For example, adding the definition of Riemannian gradient/Hessian/cross-gradient, the role of local coordinate chart and the relation between $f$ and $\bar{f}$ would help readers to better understand the context. Specifically, the paper dives directly into using local coordinate charts without clearly explaining why this is necessary for defining gradients and Hessians on manifolds, and how these relate to the function $f$ defined on the manifold. The distinction between the function on the manifold and its representation in local coordinates, and how this affects the analysis, is not made clear enough for a reader unfamiliar with Riemannian geometry.

lines 45-47 could be improved to better explain this paper's focus on differential equilibriums (DNE and DSE). This could have been local Nash and local minimax points. Then why differential equilibrium? The paper should clarify why it focuses on differential Stackelberg equilibria (DSE) and differential Nash equilibria (DNE) rather than local Nash or minimax points. The motivation for this specific choice of equilibrium concept is not sufficiently explained, especially given that the local convergence analysis could potentially be applied to other equilibrium concepts.

Table 1 is confusing: What is your focus here? The title should be more specific to make a point. Isn't Nash equilibrium found by Zhang et al. (2023) DNE? This is not clear in the table. Also, your result is local (both in optimality and convergence) while others might be global. I am not sure whether local/global should be discussed in the table, but I am sure that this table needs to be reorganized and rewritten. The table lacks a clear purpose and does not effectively highlight the contributions of this paper compared to existing work. The distinction between DNE and other forms of Nash equilibrium is not clearly made, and the table does not specify whether the results are local or global, making it difficult to understand the paper's contribution.

I suggest rewriting Definition 3.1 to make it more explicit that it defines local linear convergence. The current definition is not immediately clear to someone not already familiar with the concept of local linear convergence. It would benefit from more explicit language to clarify that it is defining a specific type of convergence rate.

line 276: Were you trying to say that $M$ with eigenvalues with only negative real parts?

lines 524-525: I don't follow what do you mean here.

### Questions
- lines 45-47 could be improved to better explain this paper's focus on differential equilibriums (DNE and DSE). This could have been local Nash and local minimax points. Then why differential equilibrium? 
- Table 1 is confusing: What is your focus here? The title should be more specific to make a point. Isn't Nash equilibrium found by Zhang et al. (2023) DNE? This is not clear in the table. Also, your result is local (both in optimality and convergence) while others might be global. I am not sure whether local/global should be discussed in the table, but I am sure that this table needs to be reorganized and rewritten.
- I suggest rewriting Definition 3.1 to make it more explicit that it defines local linear convergence.
- line 276: Were you trying to say that $M$ with eigenvalues with only negative real parts?
- lines 524-525: I don't follow what do you mean here.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the local convergence of the deterministic τ-GDA and τ-SGA algorithms to differentiable equilibria in min-max games on Riemannian manifolds. Using the Ostrowski theorem, sufficient conditions on the algorithm hyperparameters (in particular, on the learning ratio τ) are given for linear-rate local convergence to Differentiable Stackelberg Equilibria (DSE) for both τ-GDA and Asymptotic τ-SGA (an approximation to τ-SGA that is amenable to easier analysis). Local convergence to Differentiable Nash Equilibria (DNE) is also given for τ-GDA.

This paper marks the first time that τ-SGA has been written for Riemannian manifolds, and the authors put it forth as an algorithm that can solve the problem of τ-GDA’s slow convergence rate in certain settings. Both theory and example are given to show that Asymptotic τ-SGA can be locally convergent at a smaller τ compared to τ-GDA, and with a faster rate; moreover, in Euclidean space the rate guarantee outperforms that of the extra-gradient method, which has been used to overcome the slow convergence rate of τ-GDA but is costly in Riemannian space. Experiments also show that the gap between Asymptotic τ-SGA and the true τ-SGA is small, so the theoretical results should also hold for the more natural τ-SGA.

Finally, the paper applies stochastic τ-GDA and τ-SGA to train orthogonal Wasserstein GANs with a discriminator parametrized in the Stiefel manifold. It is shown that even with good initialization a small τ may cause τ-GDA to oscillate with high amplitude, but that τ-SGA can converge even at those small values of τ.

### Strengths
Overall, this paper seems like a significant algorithmic contribution with sound theoretical grounding. The authors extend known, tight local convergence results for τ-GDA from Euclidean space to Riemannian manifolds and introduce τ-SGA to the context of Riemannian manifolds. Both in theory and practice τ-SGA is shown convincingly to be able to achieve (local convergence) in settings where τ-GDA cannot, highlighting its usefulness in this setting of Riemannian min-max problems with minimal assumptions (just f twice continuously differentiable).

The paper is generally well written. The sections on differentiable equilibria, algorithms, and local convergence read especially well, with much background and explanation given to readers. Motivations and the context of prior work and clearly written.

### Weaknesses
While it is clearly stated in the introduction that global convergence is difficult to achieve in this setting and local convergence (to differentiable equilibria) may be all we can get theoretically, it is not clear what these limitations mean, or are expected to mean, in practice. The experiments are set up to show local convergence after good initialization, but it is not clear what the good initialization entails or if τ-SGA can be used when you are not near a DSE. Also maybe some comment could be made about the existence and significance of DSE in the settings provided (e.g., the Wasserstein GANs), and about other methods for doing min-max Riemannian optimization in these setting (e.g., over Steifel manifolds).

I also find the writing of the GAN experiments and their setups/parameters/initialization a bit terse and less clearly written than what comes before, with a few things in particular lacking explanation. I ask some questions about this below.

From the experiments, it seems like τ-SGA is used as a sort of “last mile” algorithm to guarantee fast convergence after good initialization/pretraining (either via ansatz in the analytical examples of Figure 1 or via τ-GDA for the GANs). Is this a reasonable interpretation of the authors’ proposed use of τ-SGA, and is there any reason that τ-GDA—in particular, alternating τ-GDA—is used to pretrain the GANs?

In Theoerems 3.2 and 3.4, after the main statements there are additional (“furthermore…”) statements for when γ is fixed exactly depending on L_g/L_s. Is this reasonable given that L_g depends on the DSE, which is not known in advance? (Maybe this is not so important, but as it is written I am not sure what the significance of these “furthermore” statements is.)

τ-SGA has an additional hyperparameter θ (or μ) to tune compared to τ-GDA, and in the GAN example of Table 2 a “suitable choice” of θ seems to have been made. Does the value of θ matter much, and how is it chosen?

I am not so familiar with the way “retraction” is used in Section 3.1, though it does not affect much as the algorithms are easily understood. Perhaps some quick definition or source could be given?

### Questions
From the experiments, it seems like τ-SGA is used as a sort of “last mile” algorithm to guarantee fast convergence after good initialization/pretraining (either via ansatz in the analytical examples of Figure 1 or via τ-GDA for the GANs). Is this a reasonable interpretation of the authors’ proposed use of τ-SGA, and is there any reason that τ-GDA—in particular, alternating τ-GDA—is used to pretrain the GANs?

In Theoerems 3.2 and 3.4, after the main statements there are additional (“furthermore…”) statements for when γ is fixed exactly depending on L_g/L_s. Is this reasonable given that L_g depends on the DSE, which is not known in advance? (Maybe this is not so important, but as it is written I am not sure what the significance of these “furthermore” statements is.)

τ-SGA has an additional hyperparameter θ (or μ) to tune compared to τ-GDA, and in the GAN example of Table 2 a “suitable choice” of θ seems to have been made. Does the value of θ matter much, and how is it chosen?

I am not so familiar with the way “retraction” is used in Section 3.1, though it does not affect much as the algorithms are easily understood. Perhaps some quick definition or source could be given?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Using the concepts of DSE and DNE on Riemannian manifolds, the author derives conditions on the range of τ and learning rate of x to ensure linear convergence of τ-GDA to DSE and DNE.

It introduces a novel algorithm τ-SGA to enhance the convergence of τ-GDA, allowing a broader range of τ for convergence when τ is large, and achieving faster local convergence than τ-GDA.

Applying these insights, the author improves the training of orthogonal Wasserstein GANs. Numerical results show that enhanced convergence of stochastic τ-GDA and τ-SGA can improve the learned generator on simple benchmarks.

### Strengths
This article provides sufficient conditions for the local convergence of τ-GDA and τ-SGA to differential equilibrium on a Riemannian manifold, where the author proves a linear convergence rate of τ-GDA to DSE and DNE, depending on the spectral radius of the Jacobian at equilibrium. THe author introduces τ-SGA on Riemannian manifolds to further improve this rate.

### Weaknesses
 - Some key terms could benefit from further explanation or intuitive insights. For example, the linear transformations in (9) and (10), specifically the role of \(DT^*\), lack sufficient explanation regarding their connection to the Riemannian geometry and how they relate to the update rules of \(\tau\)-GDA and \(\tau\)-SGA. The connection between the spectral radius of \(DT^*\) and the convergence rate is not clearly established.

- It appears that several theorems are extensions of those from the Euclidean case. The paper does not adequately discuss the challenges in extending these results to Riemannian manifolds. What specific properties of Riemannian manifolds necessitate the use of retractions and how do these impact the analysis, compared to the simpler Euclidean case? The paper should highlight the key differences in the analysis and why the extensions are non-trivial.

- Given the author's claim of linear convergence rates for the proposed methods, the experimental section lacks a rigorous analysis of these rates. While the authors claim linear convergence, there is no direct measurement of the convergence rate in the experiments, nor a comparison to the theoretical predictions. The experiments should include a quantitative analysis of the convergence rate to validate the theoretical claims.

- Question for Theorem 3.1. (Ostrowski Theorem on manifold)

 - The author indicates that the theorem is analogous to the theorem in the Euclidean case. However, the paper does not explicitly state the Euclidean version of the theorem, making it difficult to assess the analogy. Is the Euclidean version of the theorem also based on the spectral radius of a linear transformation similar to (9), and how does the Jacobian matrix in the Euclidean case relate to the operator \(DT^*\) on the manifold?

 - What is the size of the local convergence radius around ( \(x^*\), \(y^*\))? The paper does not provide any insight into how this radius is determined or how it depends on the problem parameters. A discussion of the factors influencing the size of this region is needed.

 - How can one ensure that the initialization lies within this local neighborhood? Does the initialization used in experiments satisfy this requirement? The paper lacks a discussion on initialization strategies and their impact on convergence. It is unclear if the initializations used in the experiments are within the theoretical convergence region.

 - What is the reasoning behind assuming a small spectral radius for \(DT^*\)? The paper does not provide a clear justification for this assumption. It is not clear under what conditions this assumption is valid and how it affects the practical performance of the proposed algorithms.

### Questions
Question for Theorem 3.1. (Ostrowski Theorem on manifold)

- The author indicates that the theorem is analogous to the theorem in the Euclidean case. Is the Euclidean version of the theorem also based on the spectral radius of a linear transformation similar to (9)? 

- What is the size of the local convergence radius around ( 𝑥*, 𝑦*)? 

- How can one ensure that the initialization lies within this local neighborhood? Does the initialization used in experiments satisfy this requirement? 

- What is the reasoning behind assuming a small spectral radius for 𝐷𝑇* ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
1

### Summary
This paper studies min-max algorithms to solve zero-sum differential games on Riemannian
manifold

### Strengths
No

### Weaknesses
This paper does not have any interesting parts. Firstly, the Riemannian optimization is not practical. Furthermore, could you show some practical utilization of your algorithms?

I think that this manuscript contributes nothing in science expect some hard understanding of mathematical symbols.

### Questions
I think that this manuscript contributes nothing in science expect some hard understanding of mathematical symbols.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the local convergence of simultaneous minimax algorithms to differential Stackelberg equilibrium (DSE) and differential Nash equilibrium (DNE) on Riemannian manifolds. The authors study two representative deterministic algorithms, $\tau$-GDA and $\tau$-SGA. For $\tau$-GDA, they derive sufficient conditions for convergence to DSE and DNE. For $\tau$-SGA, they analyze an asymptotic variant and demonstrate a faster convergence rate to DSE under specific conditions. Furthermore, the authors conduct numerical experiments to explore the behavior of stochastic versions of the two algorithms.

### Strengths
1. **Significance**: This paper addresses the more general nonconvex-nonconcave setting, extending previous results to Riemannian manifolds.
2. **Comprehensiveness**: It provides a range of results by examining two types of equilibrium points, two algorithms, and extensive numerical results.

### Weaknesses
1. **Limited Comparative Analysis and Interpretation**: The relationship and comparative insights between the theoretical results could be strengthened. Here are some examples.
* (i) The paper examines two equilibrium points, DSE and DNE, where DNE is a subclass of DSE with stricter definitions. Convergence to DNE would be expected to require fewer restrictions or achieve a faster rate. Theorems 3.2 and 3.3 support the former expectation, as the range of $\tau$ in Theorem 3.3 is broader than in Theorem 3.2, yet no convergence rate is provided for Theorem 3.3. A more detailed comparison of the convergence rates, potentially highlighting the trade-offs between the generality of DSE and the stricter conditions of DNE, would enhance the theoretical contribution. Specifically, quantifying the convergence rate for Theorem 3.3 and analyzing its dependence on the problem parameters would provide a clearer understanding of the conditions under which each equilibrium point is preferable.
* (ii) The authors seem to aim to show the superiority of $\tau$-SGA over  $\tau$-GDA. However, by comparing Theorems 3.2 and 3.4, the range of $\tau$ ensuring convergence for asymptotic $\tau$-SGA exceeds that of $\tau$-GDA only if $\| C + \theta BB^\top \| < \| C \|$. Further discussion on practical ways to ensure this condition or examples where it holds would be helpful. For instance, analyzing the structure of matrices $B$ and $C$ that satisfy this condition, or providing specific problem instances where this inequality naturally arises, would strengthen the argument. Additionally, there is no theoretical counterpart to Theorem 3.3 for $\tau$-SGA. While $\tau$-SGA is proposed to avoid rotational dynamics, this advantage is demonstrated only in numerical results (e.g., Figure 1), not theoretically, leaving theoretical support insufficient. Establishing a theoretical result analogous to Theorem 3.3 for $\tau$-SGA, even under specific conditions, would provide a more complete comparison.

2. **Unclear Analysis for (Asymptotic) $\tau$-SGA**: 
* (i) In line 327, the asymptotic analysis requires $\theta$ to be of constant order. The introduction of parameters $\mu$ and $\tau+1$ in Eqs. 12 and 13, however, seems to contradict this requirement if they are meant to vary with $\tau$. Clarifying the relationship between $\theta$, $\mu$, and $\tau$, and explicitly stating the assumptions made on each parameter during the asymptotic analysis, would improve the rigor of the derivation. For instance, if $\mu$ is intended to scale with $\tau$ in a specific way, this should be clearly defined and justified.
* (ii) If the authors aim to show the superiority of $\tau$-SGA, Theorem 3.4 alone is insufficient, and Figure 1's simple example is not enough to establish the similarity between $\tau$-SGA and its asymptotic variant. The claim "Theorem 3.4 is valid for $\tau$-SGA" in line 363 lacks rigor. If deriving a theoretical result for $\tau$-SGA is challenging, additional numerical experiments for the asymptotic $\tau$-SGA$ should at least be provided, demonstrating its convergence behavior across a wider range of problems and parameter settings. Furthermore, a more rigorous justification for applying the asymptotic result to the non-asymptotic $\tau$-SGA, perhaps through a sensitivity analysis or a bound on the approximation error, would significantly strengthen the claim.

### Questions
1. In line 277, what is the order of $\gamma^{\cdot}(M)$? Could the authors provide an intuitive explanation of this function?
2. The computation of $\tau$-SGA involves a matrix-vector product. Are the benefits sufficient to justify the additional computational cost?

### Soundness
3

### Presentation
3

### Contribution
3
