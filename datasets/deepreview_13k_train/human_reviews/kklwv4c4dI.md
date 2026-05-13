# Local Composite Saddle Point Optimization

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Distributed optimization (DO) approaches for saddle point problems (SPP) have recently gained in popularity due to the critical role they play in machine learning (ML). Existing works mostly target smooth unconstrained objectives in Euclidean space, whereas ML problems often involve constraints or non-smooth regularization, which results in a need for composite optimization. Moreover, although non-smooth regularization often serves to induce structure (e.g., sparsity), standard aggregation schemes in distributed optimization break this structure. Addressing these issues, we propose Federated Dual Extrapolation (FeDualEx), an extra-step primal-dual algorithm with local updates, which is the first of its kind to encompass both saddle point optimization and composite objectives under the distributed paradigm. Using a generalized notion of Bregman divergence, we analyze its convergence and communication complexity in the homogeneous setting. Furthermore, the empirical evaluation demonstrates the effectiveness of FeDualEx for inducing structure in these challenging settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose an Algorithm FeDualEx for solving composite saddle point problems under distributed settings. The proposed algorithm is inspired from the dual extrapolation algorithm while using a proximal operator which they define using the generalized Bregman divergence defined for saddle functions. They analyze this algorithm under homogeneous settings and derive its convergence rate for the duality gap. They also study the special cases when the number of clients equals 1, where the convergence rate of FeDualEx matches the existing rates known in the literature. The study also demonstrates that solving using the dual extrapolation has advantages of learning better sparse solutions than solving the primal.

### Strengths
The paper studies federated learning of composite saddle point problems, for which there does not seem to be much existing work. The proposed convergence rates. 

(Novelty) The paper proposes a new bregman divergence for saddle functions and its associated proximal operator, which are used in the dual extrapolation steps. 

(Clarity) The main results are presented well and contrasted to the related ones. The experimental results illustrate the benefit of solving using the federated dual extrapolation over methods such as Federated Mirror Prox. The comparison to the sequential algorithms also help to position the contributions in relation to the existing work.

### Weaknesses
The algorithm is similar that of Federated Dual Averaging (Yuan et.al.) while incorporating the dual extrapolation strategy over the newly defined Bregmen divergence and the proximal operators. The challenges associated with adapting the above strategy over FeDualAvg doesn't seem to be conveyed well in the paper. Specifically, while the paper introduces a new Bregman divergence and proximal operator, it does not sufficiently articulate why existing definitions are inadequate for the composite saddle point problem in the distributed setting. The analysis would benefit from a more detailed explanation of the specific technical hurdles that arise when attempting to apply standard dual extrapolation techniques, and why the proposed definitions are necessary to overcome these hurdles. The paper should provide a more rigorous discussion of how the composite terms in the analysis are handled, and why previous approaches fail to produce telescoping terms, leading to accumulation of errors.

From the motivations perspective, some examples of practical setups which required distributed learning of saddle point formulations would be useful in appreciating the contributions better. While the paper mentions GANs and multi-agent RL, it would be beneficial to include a more detailed discussion of specific applications and how the proposed algorithm addresses their challenges. For example, a discussion of how the algorithm handles the non-convexity of GANs or the non-stationarity of multi-agent RL environments would be helpful.

### Questions
Questions / Comments
Is it possible to have a similar algorithm only using the generalized bregman divergence on x ? 
Some discussion on the relation between the variables z=(x,y) and ς would help since the former already includes a primal and dual pair. 

To improve the clarity, one may include convexity assumptions of the functions involved while the main problem is defined in (1).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study composite saddle-point problems in a Federated learning setup. They propose distributed gradient methods with local updates, which they call Federated Dual Extrapolation. They provide convergence analysis and communication complexity in the homogeneous case.

### Strengths
The authors propose a new method, for which they provide convergence analysis. This method has their own interest.

### Weaknesses
Table 1 presents the previous and current results strangely:
1) First of all, to compare the obtained complexity for the proposed method with the previous result in a strongly-convex concave case, it should be used standard regularization trick.
2) From my point of you, when complexity contains several terms, each of them should be added. 

About Table 2, The authors claim that "The sequential version of FeDualEx leads to the stochastic dual extrapolation for CO and yields, to our knowledge, the first convergence rate for the stochastic optimization of composite SPP in non-Euclidean settings ." It is not true, there is a wide field related to operator splitting in deterministic and stochastic cases. Look at this paper please https://epubs.siam.org/doi/epdf/10.1137/20M1381678. 

Also, compared to the previous works, the authors use bounded stochastic gradient assumption and homogeneity of data. In many federated learning papers, those assumptions are avoided. Despite that the authors write "Assumption e is a standard assumption", it would be better to provide analysis without it to have more generality. 

In Theorem 1, and Theorem 2, the final result contains mistakes in complexity, because some of them were done in the proof. 
The first mistake is made in theorem 3 and repeats in the main theorem. Please look at the last inequality on page 40:
To make $3\eta^2\beta^2 -1 \leq 0$, the stepsize should be chosen in the following way: $\eta \leq \frac{1}{\sqrt{3}\beta}$. This will change the complexity of the methods. The same was done in the proof of Theorems 1, and 2. Please see Lemma 3, 17.

The second mistake is made in the proof of Lemma 13, in the last two inequalities, where should be $\dots\sqrt{2V^l_z(\cdot)} \leq \dots \sqrt{B}$. This thing also will change the final complexity.

The appendix is hard to read in terms of the order of Lemmas. I think it would be better if the numeration of Lemmas had a strict order (for example, after Lemma 5 lemma 6 follows.)

Other things dealing with weaknesses, please, see in questions.

### Questions
1. In section 4, it is unclear how you define $\ell_{r,k}$. Could you add an exact expression for it from the appendix to the main part? 

Small typos:
1. on the bottom of page 5 in the second argmin the bracket is missed. 
2. In definition 4, $t\eta$ is missed in the formula for subgradient.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes FeDualEx a federated primal-dual algorithm for solving distributed composite saddle point problems. The authors consider a homogeneous setting and provide convergence guarantees achieved by FeDualEx when the objective function is convex-concave. The authors also evaluate the proposed algorithm experimentally on synthetic and real datasets.

### Strengths
Overall. the paper is well written with the ideas clearly explained. The proposed algorithm is well-motivated and backed by strong theoretical guarantees. The experiments show the effectiveness of the proposed approach.

### Weaknesses
- The authors have missed an important reference [R1] which considers a nonconvex composite optimization and develops Douglas-Rachford Splitting Algorithms for solving the problem.

- The authors should also discuss [R2] and [R3] which consider a non-convex composite problem but in a decentralized setting and without local updates. Also, in contrast to the duality-based approach taken by the authors, the works [R2] and [R3] propose primal algorithms that directly update the parameters using proximal stochastic gradient descent. The dual approach proposed by the authors is justified by the "curse of primal averaging". A question I have is why the algorithms [R2] and [R3] seem to work even though they are primal algorithms.

- Why are the guarantees presented in the paper independent of the number of clients? The effect of the number of clients should be discussed after the main results. Importantly, does the proposed algorithm achieve linear speed-up with the number of clients in the network?

- In the initial part of the paper the authors refer to the distance-generating function to be strictly convex but later it is assumed to be strongly convex. It is advisable to call it strongly convex from the beginning.

- Define $h_1$, $h_2$ in Definition 3.

- After Definition 3, the authors mention that the previous approaches that add the composite term to the Bregman divergence may not work for dual extrapolation as certain parts of the analysis break down. Can the authors be more specific about what they mean here?

### Questions
See the weaknesses section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
