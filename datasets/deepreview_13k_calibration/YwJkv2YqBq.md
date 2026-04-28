# Nesterov acceleration in benignly non-convex landscapes

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
While momentum-based optimization algorithms are commonly used in the notoriously non-convex optimization problems of deep learning, their analysis has historically been restricted to the convex and strongly convex setting. In this article, we partially close this gap between theory and practice and demonstrate that virtually identical guarantees can be obtained in optimization problems with a `benign' non-convexity. We show that these weaker geometric assumptions are well justified in overparametrized deep learning, at least locally. Variations of this result are obtained for a continuous time model of Nesterov's accelerated gradient descent algorithm (NAG), the classical discrete time version of NAG, and versions of NAG with stochastic gradient estimates with purely additive noise and with noise that exhibits both additive and multiplicative scaling.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an analysis of NAG that proves accelerated convergence rates in some non-convex scenarios, using assumptions on the loss function inspired by overparameterized deep learning. The authors analyze continuous time with deterministic gradients, discrete time with deterministic gradients, and discrete time with stochastic gradients (and multiplicative noise), showing accelerated convergence rate (better dependence on condition number) compared to gradient descent/gradient flow.

### Strengths
1. The paper is very clearly written. Previous work is totally explained and the authors are very straightforward when describing their novel contribution (Lines 42-51 and Lines 106-107).
2. The convergence rates are a clear improvement upon previous work, which either achieves similar rates with stronger assumptions or achieves a non-accelerated rate for gradient flow under a similar setting as this work (aiming condition).
3. The authors are straightforward about the limitations of their work, which I appreciate. In Lines 253-260, they mention that their global assumption on the loss geometry can only be guaranteed locally. Still, it seems that the assumptions are weaker than previous works (e.g. quasar convexity), so I think that this is acceptable.

I want to mention to other reviewers/AC that I am not too familiar with this particular line of work, so I am slightly less confident about the technical contribution of this submission. However, according to my best judgement, the contribution seems worthy of publication.

### Weaknesses
1. The assumptions are inspired by overparameterized deep learning, but are unlikely to be completely accurate. This authors already comment on one instance of this (Lines 253-260). Another instance is the requirement that the objective is $C^1$-smooth (Line 114), which is not satisfied by non-smooth activation functions. Specifically, while the authors acknowledge the local nature of their global assumption on loss geometry, the assumption of $C^1$ smoothness is a more significant limitation. Many common activation functions, such as ReLU, are not continuously differentiable, and while the objective might be smooth almost everywhere, the lack of continuous differentiability could pose problems for the analysis. This is a minor weakness compared to the strengths of the paper.



### Questions
1. I'm not sure to what degree the proof of Theorem 7 requires novel techniques. The authors mention (Line 324) that their overall proof strategy is common, and the contribution comes from their Lemma 1. I am not too familiar with this line of work, so it is hard for me to judge the novelty and non-triviality of Lemma 1. Can you elaborate on the technical contribution of Lemma 1?
2. Do you believe that similar ideas could be used for non-smooth objectives in future work? For example, the objective function for training a ReLU network with squared loss is almost everywhere continuously differentiable, instead of continuously differentiable (as required by your assumption #1). Could this gap be addressed with the kind of techniques used in this paper, or might this setting require entirely an entirely different approach?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the convergence rate of momentum-based optimization methods under more general conditions than (strong) convexity. Motivated by existing works, the authors assume a localized version of strong convexity that allows for multiple local minimizers. The authors provide examples of such objective functions and also show empirically that the assumption is reasonable in deep learning applications. By considering a continuous-time ODE, the authors characterize the behavior of momentum-based method and prove accelerated rate compared with standard GD. The setting of stochastic optimization is also considered as an extension.

### Strengths
1. Overall I think this is a nice paper with interesting contributions to the optimization community. I like the writing style of this paper, especially for the concise introduction and discussions of relevant works.

2. This paper justifies the superiority of momentum methods under weaker assumptions than strong convexity. Moreover, the assumptions made in this paper are supported by empirical evidence.

### Weaknesses
While I do not check all the proofs, the paper does not seem to have many novel technical contributions compared with existing works on ODE modeling of optimization algorithms. I'm not sure if this should be considered as a weakness, since the results themselves are interesting.

### Questions
I do not have any questions for this work.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents convergence analysis of Nesterov Acceleration for nonconvex functions. Some (geometric) assumptions weaker than PL inequality are employed to derive convergence results for NAG.

### Strengths
There are some works have been reviewed in the literature, both from the line of momentum algorithms, and the geometry of deep neural networks. The paper is well-organized.

### Weaknesses
1. To the best of my knowledge, both from theoretical and practical perspectives, the momentum methods commonly used in deep learning are based on the Polyak Heavy-ball method, not Nesterov acceleration. However, the paper under review focuses more on Nesterov acceleration, while mentioning motivation from deep learning without any references. Could the author carefully provide sufficient references to support this motivation?

2. The main contributions of the paper in comparison with related references is unclear. Could you state them more explicitly, discuss them in greater detail?

3. The paper lacks a thorough literature review. For example, a unified convergence analysis for momentum algorithms has already been considered in Josz et al. (https://epubs.siam.org/doi/abs/10.1137/23M1545720?journalCode=sjope8). Could the authors please address this paper carefully and consider the references therein to better position their contribution within the literature on Nesterov acceleration? 

4. The assumptions in Section 2.1 seem too strong, as they imply the PL inequality. Recent works, such as Josz et al. mentioned above, require only the KL inequality, which holds for a significantly larger class of functions encountered frequently.

5. What is the connection between your continuous-time and discrete-time analyses? While the discrete-time analysis is of primary interest, the purpose of including the continuous-time analysis is unclear, aside from serving as additional motivation. If the continuous-time analysis can be directly applied to derive results for discrete time, its inclusion is entirely appropriate. However, if it is independent of the discrete-time analysis, I do not think it should be included unless carefully justified.

6. The numerical experiments are too simple. Could you include additional experiments on practical classes of nonconvex functions, such as those commonly found in deep learning?

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Motivated by nonconvexity of deep learning objectives, this paper studies the  heavy ball method under relaxed convexity assumptions. The continuous time, discrete time and stochastic algorithms are investigated. Some toy experiments are presented to illustrate how the convexity assumptions hold in practice.


------- AFTER REBUTTAL -------


**I raise my score to 6. The author(s) present interesting and sufficiently new contributions, but the paper needs strong revisions in terms of presentation and redaction.**

### Strengths
Benign convexity of machine learning problems is an interesting direction in order to understand why gradient methods may converge well in practice.

### Weaknesses
The author(s) confuse the assumptions used in the related work by Aujol et al., titled "Convergence Rates of the Heavy Ball Method for Quasi-Strongly Convex Optimization," published in SIAM Journal on Optimization in 2022.

In the introduction, the authors claim that "strong quasar-convexity" is used in Aujol et al. (2022). This condition appears to be stronger than the one used by the authors, referred to as Assumption 4, which the authors now describe as "strong convexity with respect to the closest minimizer."

However, Aujol et al. (2022) already use Assumption 4. Their assumption is not quasar-convexity, as mistakenly stated in the introduction, but rather strong convexity with respect to the projection onto the minimizing set, which corresponds to the closest minimizer (see equation (4) in Aujol et al., 2022). As a result, all of the theoretical contributions presented by the authors already exist in the literature. For example, Theorem 7 replicates the convergence rates from [Theorem 1, Aujol et al., 2022].

Furthermore, the authors conflate Nesterov's acceleration with the heavy ball method throughout the paper, although they are two distinct algorithms. The paper focuses on the heavy ball method, not Nesterov's acceleration.

The literature review is still confusing. For instance Aujol et al. assume weak quasi convexity with respect to the closest minimizer and Guminov et al. assume weak quasi convexity to a fixed minimizer. In the introduction it is claimed that these papers use the same hypothesis, which is inaccurate.

The deep learning aspect is really incomplete. The experiments on some minimizer $w$ (only one) to observe the convexity of the loss along the gradient direction, can be highly imprecise given that the analysis is close to the minimizing set. This has some illustrative value, but this is not sufficient to provide an experimental evidence.

Additionally, the introduction needs to be polished. The main elements which have to be exposed there are: (i) the motivations in deep learning; which is mainly the connection with overparameterized models, and (ii) a clear literature review of convergence guarantees under weak convexity assumptions (nonuniquess of minimizers etc). The current introduction is disorganized, jumping between topics like accelerated methods, PL condition, NTK, Hessian eigenvalues, gradient method, nonsmooth optimization, heavy ball, KL inequality, time discretization, strong quasar convexity, implicit bias, and finally the contributions.

Some of the language is overblown. For example, the claim that "In general deep learning applications, the set of minimizers of the loss function is a (generally curved) manifold" is too broad. Can this be claimed for any model? Also, the statement that "We have proved that first order momentum-based methods accelerate convergence in a much more general setting than convex optimization" is too general, while the work focuses on particular notions of weak convexity and a specific landscape geometry. Similarly, the phrase "with many geometric features motivated by realistic loss landscapes in deep learning" is an overstatement. Some works on overparameterized neural networks may motivate the use of such geometric features, but the word "realistic" seems too strong.

Finally, there is a lack of insight into the proof techniques in the main paper. The authors mention that the main difficulty lies in controlling the "tangential motion" but do not explain how this is achieved or how it connects with the assumptions. The proof techniques could contribute to the ML/optimization community from a theoretical perspective, but the current presentation makes them difficult to access.

### Questions
I suggest the authors to better compare their work with the related works.

### Soundness
1

### Presentation
1

### Contribution
2
