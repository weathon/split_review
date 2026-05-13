# Generalized Smooth Stochastic Variational Inequalities:  Almost Sure Convergence and Convergence Rates

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
This paper focuses on solving a stochastic variational inequality (SVI) problem under relaxed smoothness assumption for a class of structured non-monotone operators. The SVI problem has attracted significant interest in the machine learning community due to its immediate application to adversarial training and multi-agent reinforcement learning. In many such applications, the resulting operators do not satisfy the smoothness assumption. To address this issue, we focus on the generalized smoothness assumption and consider two well-known stochastic methods with clipping, namely, projection and Korpelevich. For these clipped methods, we provide the first almost-sure convergence results without making any assumptions on the boundedness of either the stochastic operator or the stochastic samples. Furthermore, we provide the first in-expectation convergence rate results for these methods under a relaxed smoothness assumption.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on stochastic variational inequality (SVI) problems involving non-monotone operators. Applying clipping to projected gradient descent and extragradient methods establishes almost-sure convergence and in-expectation convergence rates under generalized smoothness conditions, without boundedness assumptions.

### Strengths
This work relaxes several assumptions:
- uses a relaxed notion of L-Lipschitzness, called $\alpha$-symetric operator.
- does  not rely on the assumptions of bounded noise and bounded gradients

### Weaknesses
 - Proposition 2.2. is written for an operator, and is taken from Proposition 1 in (Chen et al. 2023a). The latter is for a gradient of a real-valued function, the former is for an operator that is a more general vector field. It is unclear if Proposition 1 in (Chen et al. 2023a) directly extends to non-gradient field operators. The first equivalence (eq. 9) in  (Chen et al. 2023a) already fails for vector fields. Also, since the proof for (9) in  (Chen et al. 2023a) also relies on ODEs it involves solving the integral involving $h$ therein that contains a vector field. Could you please elaborate?


- Provide citations for the Extragradient and the Popov method.

- It is confusing that Chen et al 2023 is cited twice with the same title and authors.

# Writing

*Structure.* The contributions are listed in related works; perhaps introduce a paragraph.

*Abstract.* 
- After reading the abstract I could not tell which setup this paper focuses on. It mentions "structured non-monotone operators" but it should be more specific. 
- I could not tell which methods the paper focuses on. It states "well-known stochastic methods with clipping, namely, projection and Korpelevich". The former can be combined with all methods, so I was confused. For the latter, it is common to use 'extragradient'. Please use projected gradient descent (PGD) and projected extragradient throughout the paper. However, even with this change, the abstract is still confusing, as it gives the impression that you are focusing on problems beyond monotonicity, for which PGD last iterate does not converge; clarify if you are focusing on last, average, or best iterate.
After reading the abstract, I could not tell what rate you get and whether it matches the lower bound? Please add that.


*Other.* 
- Use citing with brackets when needed
- line 49 missing citation for Adam 
- line 57 missing citation for adaptive methods
- line 71 typo

### Questions
Please see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on solving stochastic variational inequalities which do not satisfy the typical regularity (Lipschitz continuity) and structural assumptions (monotonicity). More precisely, the authors in order to extend the notion of Lipschitz continuity they consider the class of $\alpha-$ asymmetric operators (introduced by Chen 2023). Furthermore, their extension of non-monotonicity, they consider operators which satisfy the so-called $p$-quasi sharpness property. This structural assumption actually can be seen as a local type relaxation of strong convexity relative to the solutions.
To that end, the authors investigate under these assumption the behaviour of (stochastic) projected gradient descent and extra-gradient algorithm run with stochastic clipped step-sizes. In doing so, they provide asymptotic and non-asymptotic convergence guarantees for each respective method

### Strengths
The paper is clearly written and easy to follow. Furthermore the math supporting the main contribution of the paper, namely the theoretical convergence guarantees for two classical optimization algorithmic schemes run with stochastic clipped methods seems solid.
Moreover, as far as my knowledge goes the particular result are novel in the literature.
Finally, the numerical/experimental part seems clear and supports the theoretical results

### Weaknesses
Concerning the weaknesses, three observations are in order:

1.  The key innovation, compared to the variational coherent literature is the introduction of two independent samplings per iteration. In my opinion this needs further clarifications on how it affects the complexity of the rates both in theory and in the numerical experiments. Specifically, while the use of two samples might lead to unbiased estimates, the practical implications on computational cost and wall-clock time need to be thoroughly investigated. For instance, a detailed comparison with single-sample methods in terms of convergence rate per unit of computational effort would be beneficial. Furthermore, the theoretical analysis should explicitly quantify the increase in oracle calls and how this impacts the overall complexity bounds, especially when considering the stochastic nature of the problem.

2. The under study relaxation of the Lipschitz continuity of the (VI) defining operator introduces some extra parameters which require an additional tuning effort (see the respective non-asymptotic convergence rate theorems). This fact requires an additional discussion concerning the practical efficiency of the methods. The parameters $L_0$, $L_1$, $K_0$, $K_1$, and $K_2$ are crucial for the convergence analysis, and the paper should provide more guidance on how to estimate or choose these parameters in practice. The sensitivity of the algorithms to these parameters should also be investigated, as a poor choice could lead to significantly worse performance. A discussion on adaptive methods for parameter selection or robust methods that are less sensitive to these parameters would be valuable.

3. The case of $p>2$ the respective guarantees are given with respect to the expected best distance.  To that end, this prohibits the proposal (due to the stochastic nature of the methods) of an actual output rule of the respective methods. The reliance on expected best distance for $p>2$ is a significant limitation, as it does not provide a practical way to select a solution from the sequence of iterates. A more practical convergence result would be to show convergence of the average iterate, which is a more tangible quantity. The paper should also discuss the implications of this limitation and potentially propose alternative output rules that can be used in practice, or provide a theoretical justification for why the best iterate is the most appropriate measure in this context.

### Questions
See weaknesses section.

### Soundness
3

### Presentation
2

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
The paper considers $L_0,L_1$-smooth stochastic variational inequalities satisfying a generalization of strong monotonicity/coherence called $p$-quasi sharpness.
For both a clipped variant of projection stochastic gradient method and the projected stochastic extragradient method they show:

- $\mathcal O(1/k)$ rates in expectation for the last iterate when $p=2$ (strongly coherent problems), matching the one under (standard) Lipschitz continuity (e.g. Hsieh et al. 2019b)
- $\mathcal O(k^{-2(1-q)/p})$ rates for the best iterate for $q\in (1,1/2)$. 
- With a Robbins-Monro stepsize factor they show almost sure convergence.

Both methods uses two gradient computations since the gradient method requires the clipping to be performed with a fresh sample.

### Strengths
- The paper reads very easily and is transparent about contributions
- Relaxing smoothness assumptions for VIs seems like an interesting direction

### Weaknesses
 - Assuming $p$-quasi sharpness seems like a strong assumption since even (clipped) gradient descent suffice in this setting, making it close to the minimization case. In light of this the result does not seem particularly surprising. The authors should provide a more detailed discussion of the implications of this assumption and perhaps provide examples of problems that satisfy this condition but are not amenable to standard gradient descent methods. Furthermore, the connection to existing notions of sharpness should be made more explicit.
- considering that gradient descent suffice I do not understand the motivation for considering the extragradient variant. It would be helpful if the authors could elaborate on the benefit/reason. I could see it being interesting if clipped extragradient also have a guarantees for bilinear or convex-concave problems (in which case the guarantee would only be for the average in light of e.g. Hsieh et al. 2020), but this is not currently provided. The authors should clarify whether the proposed extragradient method recovers known convergence rates for bilinear or convex-concave problems, even if only in an average sense. The current analysis does not seem to provide any advantage for the extragradient method over the clipped gradient method.
- Even the clipped gradient method requires 2 gradient computations, which seems unconventional (cf. e.g. Gorbunov et al. 2022). It would be interesting if the additional gradient call could be removed. The authors should discuss the necessity of the two-sample approach in more detail. Specifically, it would be helpful to understand if this is a fundamental requirement of the analysis or if it is an artifact of the proof technique. A discussion of the practical implications of this additional gradient call is also warranted.

Minor:

- l. 481 maybe don't state that p-quasi-sharp is a wide class, consider the (weak) Minty variational inequality also mentioned later.
- l. 489 $\mu < 0$ does not seems to correspond to the weak Minty variational inequality (you need the operator evaluation on the right hand side instead of solution distance). It might be worth also providing a reference.

Typos:

- l. 99 stepszies -> stepsizes
- l. 105 should be $O(k^{-1})$
- l. 75 thr -> the

### Questions
- Eq. 9: could you elaborate why you need a fresh sample? Is this an artifact of the analysis?
- It is curious that Popov's method dominates all other methods in the experiments:
     - Is there any intuition for why this is the case? 
    - It is not clear to me how the clipping is performed for Popov since each update involves to gradients (the old and new). Is the old gradient clipped with a fresh sample, such that the number of gradient calls are the same as for the clipped version of the gradient/extragradient method?
     - What is the difficulty in analysing a clipped version of Popov's method under generalization smoothness? 
- It seems strange that a large choice of $q$ improves performance, while the theory suggests otherwise. What are possible explanations?
- As a sanity check do you recover Theorem 2.5 of Koloskova et al. (2023) in the strongly convex deterministic case?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on solving Stochastic Variational Inequalities (SVI) under a generalized smoothness assumption. More specifically, the authors analyze two methods, the Projection method and the Korpelevich method, in the quasi-sharp regime. The asymptotic convergence of both algorithms is established under the general smoothness assumption. In addition, the authors provide theoretical guarantees for the last iterate and establish the rate of convergence of both methods. Experimental results compare the two methods, validating the theoretical results for different stepsizes.

### Strengths
- The convergence is established under an assumption that is more general than smoothness.
- The paper establishes asymptotic convergence for two algorithms in the quasi-sharp setting.
- The associated rates of convergence are provided for each algorithm.

### Weaknesses
 - Even though the paper provides a good amount of previous work on the topic, the positioning of the new results in the established literature is not done sufficiently. It would be nice to have a comparison of the provided convergence rates for the two methods with existing results. For example, one can compare the rate of the Projection method with the algorithm in [1] in the special setting of minimax problems.
- Based on the start of Section 3, it seems that two stochastic oracles are needed in the Projection method for the analysis to go through. This approach seems to require double the number of stochastic oracles than the classical Stochastic Projected Gradient Descent Ascent (or Stochastic Projection method with one oracle per iteration), which is not favorable. The practical implications of this increased oracle complexity should be discussed further, especially in settings where oracle calls are computationally expensive.
- It would be nice to have a comparison between the two methods, Projection algorithm and Korpelevich method. Even though there is a reference to that in the Experimental section, a precise comparison of the two algorithms and their rate after providing the rates of convergence would be beneficial to have. A more detailed theoretical comparison, highlighting the specific scenarios where one method might outperform the other, would strengthen the paper.
- The assumption on bounded variance of the stochastic oracles might be strong in some settings. This assumption limits the applicability of the proposed methods to scenarios where the stochastic gradients exhibit relatively stable behavior. The paper should discuss the potential impact of this assumption and explore possible relaxations or alternative assumptions.

Some Typos:
- In the introduction (line 57): “normalizedChen et al. (2023b)” the reference is not correctly inserted.
- In section 1.1: “SVIs Jelassi et al. (2022)” the reference is not correctly inserted.
- In section 1.1: “Generalized Smooth Optimization In Zhang et al. (2019)” the reference needs to be correctly inserted.
- In section 3.2, it is mentioned “Then, from Theorem 4.4 we obtain”. However, I think that Theorem 3.4 was meant to be mentioned.

### Questions
- Since the analysis of the stochastic projection method seems to require two stochastic oracles, one for the update step and one for the computation of the stepsize, the total number of stochastic oracles needed would be twice the number of oracles the same method would require when analyzed without the generalized smoothness assumption. Do you think that this is a limitation of the current proof technique or it is required in general for establishing convergence under the more relaxed smoothness condition?
- Which of the two methods, stochastic Projection or Stochastic Korpelevich, should be preferred in the quasi-sharp regime?

### Soundness
3

### Presentation
3

### Contribution
3
