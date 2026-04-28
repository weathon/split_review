# Adaptive Methods through the Lens of SDEs: Theoretical Insights on the Role of Noise

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
\noindent
Despite the vast empirical evidence supporting the efficacy of adaptive optimization methods in deep learning, their theoretical understanding is far from complete. This work introduces novel SDEs for commonly used adaptive optimizers: SignSGD, RMSprop(W), and Adam(W). These SDEs offer a quantitatively accurate description of these optimizers and help illuminate an intricate relationship between adaptivity, gradient noise, and curvature. Our novel analysis of SignSGD highlights a noteworthy and precise contrast to SGD in terms of convergence speed, stationary distribution, and robustness to heavy-tail noise. We extend this analysis to AdamW and RMSpropW, for which we observe that the role of noise is much more complex. Crucially, we support our theoretical analysis with experimental evidence by verifying our insights: this includes numerically integrating our SDEs using Euler-Maruyama discretization on various neural network architectures such as MLPs, CNNs, ResNets, and Transformers. Our SDEs accurately track the behavior of the respective optimizers, especially when compared to previous SDEs derived for Adam and RMSprop. We believe our approach can provide valuable insights into best training practices and novel scaling rules.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a theoretical analysis of adaptive optimization methods—specifically SignSGD, AdamW, and RMSpropW—through the lens of stochastic differential equations (SDEs), unveiling the intricate interplay between adaptivity, gradient noise, and curvature. Key contributions include:

- **SignSGD Dynamics:** Identification of three distinct phases in SignSGD’s dynamics, with noise inversely affecting both convergence rates of the loss and the iterates.
- **Enhanced SDE Models:** Derivation of new and improved SDEs for AdamW and RMSpropW, leading to a novel batch size scaling rule and an examination of the stationary distribution and stationary loss value in convex quadratic settings.

The derivation of new SDEs for SignSGD, AdamW, and RMSpropW provides a solid foundation for understanding the dynamics of these optimizers.

### Strengths
Strengths includes:
- **Intriging Insights:** Identifying three distinct phases in SignSGD dynamics and the inverse relationship between noise and convergence rates offer valuable perspectives on optimizer behavior.
- **Practical Implications:** Introducing a novel batch size scaling rule and examining stationary distributions have direct implications for better training practices in deep learning.
- **Clear background:** The preliminaries and background information provided in the appendix enhance the readability and understanding of the main results.
- **Validation:** Theoretical findings are supported by extensive experimental evidence across various neural network architectures, including MLPs, CNNs, ResNets, and Transformers.

### Weaknesses
 - **Unclear Terminology and Notation:** Certain terms and symbols used in the paper are not clearly defined, which may lead to confusion. What does $\mathbb{P}$ represent in Theorem 3.2? How is the error function defined in Corollary 3.3? Does Lemma 3.7 explicitly establish the stationary distribution of SignSGD?

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

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
This paper investigates the learning dynamics of adaptive optimizers in machine learning.  The authors analyze a simplified model, $f(x) = x^THx$, with noisy gradients defined as $g_\gamma = \nabla f(x) + \gamma$, where $\gamma$ is sampled from a distribution like a Gaussian. Focusing on SGD, sign-SGD,  and AdamW, they demonstrate that the learning dynamics can be effectively approximated by a stochastic differential equation (SDE) of the form $X_t = \text{function}(X_t)$. This allows them to analyze the first and second moments of $X_t$ for these optimizers as $t$ approaches infinity.  The authors support their theoretical findings with experiments on practical models like ResNets and small Transformers, trained on MNIST, CIFAR, and Shakespeare datasets.

While generally well-written, mathematically sound and provide many insights, the paper's reliance on a simplified model and unrealistic noise design limits its applicability.


--- updates --- 

Thank you for the clarifications. While I believe this work warrants a score of 7, I understand that's not an available option.  Considering that other reviewers have mostly given scores of 6, I am raising my score to 8 to better reflect the paper's merit.

### Strengths
- generally well-written 

- mathematically seems sound, though i didn't check the proof 

- papper contains rich set of results that may be insightful for practicioners. 

- theoretical results are supported by real networks, though on

### Weaknesses
 * The toy model is too simple and far from practical. I would expect at least a linear regression model with a random (Gaussian) design. Specifically, the analysis focuses on a quadratic function, $f(x) = x^THx$, which lacks the complexities of real-world loss landscapes. This simplification makes it difficult to generalize the findings to more complex models and optimization scenarios. A more realistic model, such as linear regression with a random Gaussian design matrix, would provide a more robust foundation for the analysis.
* The noise design is artificial and unrealistic. It doesn't capture practical batch noise, which depends on the loss, parameters, and changes over time. The current noise function uses a time-independent, identical distribution. In practice, the noise in stochastic gradient descent is highly dependent on the batch of data used and the current parameter values. This temporal and parameter dependency is crucial for understanding the behavior of optimizers, and the current noise model fails to capture this. A more realistic noise model should incorporate these dependencies to better reflect real-world scenarios.
*  Experiments use full batch with synthetic (Gaussian) noise instead of mini-batches, which is consistent with the paper's problem setup but unrealistic. This choice of using full batch gradients with synthetic noise does not align with the typical use of adaptive optimizers in deep learning, where mini-batch stochastic gradients are the norm. This discrepancy limits the practical relevance of the experimental results and makes it difficult to assess the true performance of the optimizers under realistic conditions.
* The paper is overly dense, with little intuition provided for the theorems and proofs. It also relies heavily on in-line equations, hindering readability. The lack of intuitive explanations for the theoretical results makes it challenging for readers to grasp the key ideas without delving into the technical details. The heavy use of in-line equations further compounds this issue, making the paper difficult to follow and understand.

### Questions
* The notation $\nabla f_\gamma$ is unclear and could be misinterpreted as $\nabla (f_\gamma)$. 
* All algorithms in the paper use full batch gradients with added noise, which is misleading and doesn't accurately reflect real-world implementations of algorithms like Adam.
* It would be beneficial to generalize the results to mini-batch linear regression with random Gaussian design, similar to the approach in https://arxiv.org/abs/2405.15074.
* The paper should provide more intuition behind the proof of Theorem 3.2 to help readers understand the key ideas without having to delve into the appendix.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work is centered on introducing novel SDEs for adaptive optimizers. Under weak assumptions, they derive SDE for SignSGD and compare it against vanilla SGD to show three different phases in the dynamics of SignSGD. They also show an inverse relationship between noise and convergence rate for SGD which is in contrast to the quadratic effect on loss & variance observed for SGD. They also analyze decoupled weight decay and compare it against SignSGD.

### Strengths
The paper has introduced A rigorous mathematical framework of SDEs for SignSGD and its comparison against commonly used adaptive optimizers like ADAMW. They also characterize a relationship between noise and convergence rates for SignSGD and SGD. Also, the framework is used to understand decoupled weight decay efficacy and infer the effect of noise on such approaches. Their analysis is followed by relevant experiments.

### Weaknesses
Major weakness

1. Line 245-246. The definitions of 'signal' and 'noise' need to be explicitly specified in this context. The current characterization of 'signal' in these lines does not make sense. $Y_t$ line 199 defined signal-to-noise ratio but I don't see what is being referred to in lines 245-246 and what part is being referred to as "large". The entire paragraph here should be rephrased to better connect it to the surrounding content as it currently seems disconnected, or poorly worded.

2. Line 245: "SNR is large, meaning SignSGD behaves like SignGD": This claim is unsupported. You should provide the reasoning or evidence that supports this claim, such as referencing relevant equations, prior results, or additional explanation. Specifically, the connection between a large SNR and the convergence behavior of SignSGD needs to be more explicitly detailed. Simply stating that it behaves like SignGD is insufficient; the mechanism through which this occurs should be clarified.

3. Figure 2 referred to in line 249: Hard to understand. Please provide details about the loss function/landscape, dimensionality, and any other relevant parameters used to generate Figure 2.  Lacks description of the setting used to plot figures. The figure should be accompanied by a thorough explanation of the experimental setup, including the specific optimization problem being solved, the initialization strategy, and the range of parameter values explored. Without this context, the figure's relevance and implications are unclear.

4. In general, (not commenting on technical soundness), the paper is very hard to follow and poorly structured. 
- Need to provide brief intuitive explanations before each lemma, highlighting its significance and key takeaways in order to understand what the authors want to convey.
- In section 3, authors should be more rigorous about introducing notation. There are unnecessary references to related work mentions which should be pushed somewhere else.  A comprehensive introduction of notation in the upcoming lemmas or some useful background should be introduced. Since the main argument is around novel SDEs, more introductory material on SDEs and their relevance to optimization algorithms before presenting the main results.

5. Section 3.1.1 - authors should ensure all new notation is properly introduced before it is used in lemmas, either by adding definitions as terms first appear or by including a notation section at the beginning of 3.1.1. For example, the notation for the stochastic differential equations should be defined before the lemmas are presented, so the reader can follow the mathematical arguments more easily.

6. Line 412: Decoupled weight decay. 
- Clarify why decoupled weight decay is considered key in this context. The paper should provide a clear rationale for focusing on decoupled weight decay, explaining its significance in the broader context of optimization and why its analysis is crucial for understanding the behavior of adaptive optimizers.
- Provide a more explicit link between their analysis and the claim about stabilization at high noise levels. Currently, the authors' analysis to support this is not evident. The analysis should explicitly demonstrate how decoupled weight decay contributes to stabilization, possibly by showing how it affects the dynamics of optimization in the presence of high noise.
- Include specific equations or results that demonstrate the stabilization effect of decoupled weight decay. The paper should include the relevant equations or results that directly support the claim of stabilization, making it easier for the reader to understand the mechanism behind this effect.

7. The authors should include key experimental results in the main paper, selecting the most important figures or tables that support their main claims, while potentially moving more detailed results to an appendix if space is an issue. The current presentation makes it difficult to assess the empirical validity of the theoretical results. The paper should prioritize the most relevant experimental results and include them in the main body, while moving less critical results to an appendix.

### Questions
I am not quite sure what is the key message (takeaway) of SDE analysis for decoupled weight decay analysis. They are known to be more effective than their vanilla counterparts. Is there a key message here that helps improve our understanding of adaptive optimizers? Also, is the analysis valid only for convex quadratics in this case?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work derives a novel SDE (of weak approximation order 1, under Gaussian gradient noise Z) for the SignSGD optimizer, and using this SDE, uncovers three phases of dynamics with distinct behaviours. They show theoretically that the effect of noise on SignSGD differs from SGD, and that SignSGD is more resilient to high levels of noise. Further, they show that when Z is heavy-tailed noise, the associated SDEs for SignSGD take a very similar form, further highlighting SignSGD's resilience to high levels of noise. They then derive SDEs (of weak approximation order 1) for AdamW and RMSpropW under much less restrictive assumptions than previous work, and find that decoupled weight decay has an important role in stabilization of dynamics at high noise levels. They also provide empirical validations of their theoretical results.

### Strengths
Results are presented very clearly and interpretations are made clear

Use numerical integrators to verify that their derived SDEs match the associated discrete-time optimizers across a diverse range of relevant setups

Technical assumptions appear much less restrictive than other works

### Weaknesses
Mostly theoretical, with practical implications of findings underexplored; do the findings tell you anything about how the studied optimizers can be improved, tuned, etc.?

Form of stochastic gradient appears unjustified. Is the noise Z being additive, and distributed as a Gaussian or heavy-tailed, accurate to practice?

### Questions
For Lemma 3.4 (line 199), since Y_t \in R^d, is the condition e.g. |Y_t| > 3/2 denoting the absolute value treated element-wise, like |(Y_t)_i| > 3/2, or does |Y_t| denote the norm of Y_t?

### Soundness
4

### Presentation
4

### Contribution
3
