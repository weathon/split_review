# On the Implicit Bias of Adam

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In previous literature, backward error analysis was used to find ordinary differential equations (ODEs) approximating the gradient descent trajectory. It was found that finite step sizes implicitly regularize solutions because terms appearing in the ODEs penalize the two-norm of the loss gradients. We prove that the existence of similar implicit regularization in RMSProp and Adam depends on their hyperparameters and the training stage, but with a different ``norm'' involved: the corresponding ODE terms either penalize the (perturbed) one-norm of the loss gradients or, conversely, impede its reduction (the latter case being typical). We also conduct numerical experiments and discuss how the proven facts can influence generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Backward error analysis is used to find ODEs approximating convergence trajectories by optimization algorithms. Previous works have been done on Gradient Descent to show that it has implicit regularization properties since the terms in the ODEs penalize the Euclidean norm of the gradients. This paper studies a similar problem but for adaptive algorithms such as Adam and RMSProp. It shows that Adam and RMSProp also have similar implicit regularization properties.

### Strengths
- The paper provides detailed backward error analysis for both Adam and RMSProp. The author is able to show that Adam has bias terms that penalize $1-$ norm, $2-$ norm, or $-1-$ norm depending on the settings of $\beta_1$ and $\beta_2$ in Adam.

- The paper's result in the implicit bias might help explain the difference in the generalization ability of Adaptive Algorithms and GD algorithms.

- The numerical experiments confirm the theoretical results.

- The paper is well-written overall.

### Weaknesses
 - Some of the graphs are a bit confusing since the $x$ and $y$ axes are not labeled carefully. More explanation and discussion on these graphs would be appreciated. 

- Some transformer tasks might be helpful to see if we can see consistent behaviors in the $1-norm$ across different domains. If I'm not mistaken, Adam generalizes better than SGD in transformer related tasks which slightly contradicts the first conclusion in the discussion section.

### Questions
- Can the authors explain more about Figure 2 and Figure 3? I'm a bit confused about what these graphs are about and how we can see the change of the $1-norm$ from them.

- Are the norms plotted in section 6 the norms in the final iterate of training?

- Is full batch required to observe the same behaviors of the norm and $\rho, \beta$ as in section 6? Can we do mini-batches instead?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is about the implicit bias of Adam.
It does so by studying ODEs such as the gradient flow and the properties of their discretizations.
The approach is based on backward error analysis (Barret & Dherin 2021), which consists in considering a modified version of the ODE, where the modification is done so that the iterates of gradient descent lie closer to the curve traced by the continuous flow solution.

### Strengths
- The topic of the paper, implicit bias of first order algorithms, is an active field of research with many recent results. So far, characterizing the implicit bias of Adam and other preconditioned methods has not been easy.
- The paper, to my understanding, seems to present a novel result corroborated by some empirical evidence in dimension 2.

### Weaknesses
 - The writing of the paper seems subpar to me, and would benefit from being thoroughly proofread. In some locations it sounded very informal/colloquial, eg "which is ``eaten'' by the gradient".
- The analysis, though interesting, is also handwavy: see questions below.

- In many places, statements are made informally that are to translate into rigorous mathematical terms:
  - how do the authors characterize/show/test if "$\epsilon$ is very large compared to all squared gradient components"? What if it's smaller at the beginning, they becomes larger as the algorithm converges to an interpolating solution?
  - How does penalizing the norm of the gradient lead to flat minima (Sec 4 discussion)? Since the gradient is 0 at optimum, don't $f$ and $f  + ||\nabla f||^2$ have the same set of minimizers? and doesn't this still hold when the 2 norm is replaced by any other norm?
  - similarly, in the experiment, why is the perturbed 1 norm close to 0 at convergence? It seems the authors are performing early stopping, but that precisely means that implicit regularization is not happening, and that the model overfits.
  - In the numerical illustrations, is it possible to display more than 3 curves/ values of $h$ and $\beta$? In particular, for limiting values, why isn't the red cross attained if there is implicit bias?
  - The figure are not averaged across multiple runs to account for randomness

- (contribution summary, third bullet point)?  Why do the authors consider that Adam does not have an implicit bias, despite having a bias term in the backward analysis ODE. It seems to me that the meaning of "implicit regularization", eg in eq 1.is the same as "bias term" mentioned page 2, but then the statement "Adam has no implicit regularization" is unclear.

### Questions
In many places, statements are made informally that are to translate into rigorous mathematical terms:
- how do the authors characterize/show/test if "$\epsilon$ is very large compared to all squared gradient components"? What if it's smaller at the beginning, they becomes larger as the algorithm converges to an interpolating solution?
- How does penalizing the norm of the gradient lead to flat minima (Sec 4 discussion)? Since the gradient is 0 at optimum, don't $f$ and $f  + ||\nabla f||^2$ have the same set of minimizers? and doesn't this still hold when the 2 norm is replaced by any other norm?
- similarly, in the experiment, why is the perturbed 1 norm close to 0 at convergence? It seems the authors are performing early stopping, but that precisely means that implicit regularization is not happening, and that the model overfits.
- In the numerical illustrations, is it possible to display more than 3 curves/ values of $h$ and $\beta$? In particular, for limiting values, why isn't the red cross attained if there is implicit bias?
- The figure are not averaged across multiple runs to account for randomness

- (contribution summary, third bullet point)?  Why do the authors consider that Adam does not have an implicit bias, despite having a bias term in the backward analysis ODE. It seems to me that the meaning of "implicit regularization", eg in eq 1.is the same as "bias term" mentioned page 2, but then the statement "Adam has no implicit regularization" is unclear.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the implicit bias of Adaptive Gradient Methods (especially RMSProp and ADAM) based on the modified equation of those methods derived by backward error analysis (Sections 2 and 3). As pointed out by the authors (in Related Work), given that research has primarily been conducted on Batch GD, SGD, and SGD with momentum, it is timely to explore the Adaptive Gradient Method. The authors demonstrated that ADAM implicitly penalizes (perturbed) one-norm of gradient depending on $\varepsilon$ scale (Section 2) and empirically verified it (Sections 5 and 6).

### Strengths
* The overall contents are easily understandable.
* A timely issue, ADAM's modified loss, is addressed in the paper.
* Though I did not review all the content in the Supplementary material, it appears technically correct.
* The authors validated their findings using a Toy problem (Section 5) and practical neural networks (Section 6).

### Weaknesses
 * While the overall content is easily comprehensible, specific details are inaccessible unless one reviews the supplementary material. Specifically, many theoretical works provide a sketch of the proof in the main paper to explain the techniques newly considered/developed by the authors and clarify how they differ from existing techniques. This paper lacks such details.

* In addition, the experimental setup in Section 6 is not self-contained and has elements that seem arbitrary, making cherry-picking possible.
  * In Section 6, the authors refer to Ma et al. (2022) to conduct experiments for the stable oscillation regime when $\rho$ and $\beta$ are "sufficiently close". How do you define "sufficiently close"? Most ML practitioners are familiar with situations where $\rho$ (0.99~0.999) is larger than $\beta$ (0.9). As the authors suggest, is this a spike regime or a stable oscillation regime? There should be a discussion for such questions within Section 6, but the authors merely refer to Ma et al. (2022) without providing specific details.
  * In Figures 4 and 5, the authors fixed $h$, $\beta$, and $\rho$ at certain values and ran experiments by varying other parameters. What is the basis for these fixed values? While $h$ is fixed at different values (7.5e-5 and 1e-4) without specific mention, proper empirical evidence should warrant experimentation across various values. Moreover, for $\beta$ and $\rho$, they shouldn't just experiment with a single value. Instead, they should test multiple values and demonstrate consistent backing of their theoretical results.

* The concept of ADAM's modified loss is timely. However, it seems that the resulting modified loss doesn't explain the differences between traditional ADAM and SGD. For example, as the authors mentioned, ADAM often provides worse generalization performance and sharper solutions than SGD. Yet, in NLP tasks using Transformers, ADAM significantly outperforms SGD [1,2]. Such observations lead to two natural questions regarding the authors' study:
  * If one tunes the hyperparameters of ADAM based on the discovered implicit bias, can they reproduce results where SGD performs better?
  * Can the authors explain scenarios where ADAM outperforms SGD using their discovered implicit bias (e.g., can they argue that the proposed perturbed one-norm regularization is more suitable for Self-Attention in Transformers than for Convolutions in ResNet?)

### Questions
The questions needed to improve the paper are included in the Weakness section. 
If the questions are addressed appropriately, I am willing to raise the score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors apply the backward error analysis method to find ODEs that determine continuous trajectories which are close to the discrete trajectories of the popular Adam and RMSProp adaptive gradient-based algorithms.  They succeed in doing this up to a discrepancy which is second-order in the step size, for variants of the two algorithms depending on whether the numerical stability hyperparameter $\varepsilon$ is inside or outside the square root in the step equation, and for both mini-batch and full-batch cases.  The main result for Adam uncovers three different regimes that penalise the positive one-norm of the gradient, or the negative one-norm of the gradient, or the squared two-norm of the gradient, depending on whether the squared gradient momentum hyperparameter $\rho$ is greater than the gradient momentum hyperparameter $\beta$ or not, and whether $\varepsilon$ is small or large compared with the components of the gradient (the latter two cases correspond to early or late phases of the training, respectively).  Some of the results in the literature are derived as special cases of the theorems in this work.  The paper also reports some numerical experiments that seem to confirm the theoretical results as well as suggest that the one-norm of the gradient is inversely correlated with generalisation.

### Strengths
The introduction conveys clearly the place of this work in relation to the literature.

The summary of the main result in the full-batch case is helpful, and so are the discussion, the illustration using the bilinear model, and the suggestions of future directions.

The proofs are provided in the supplementary appendix, together with details of the numerical experiments.

### Weaknesses
The introduction is a little dry.

The statement of the main result that follows its summary in the full-batch case is difficult to parse, and its connection with the summary that precedes it is not obvious.  A minor point is that equation 10 should not end with a full stop.

### Questions
Can you say more about the graphs in Figure 1?  Why are we plotting the integral, and what can we conclude from the shapes of the various curves?

What can you say about the situation when the numerical stability hyperparameter $\varepsilon$ (or rather its square root) is neither small nor large in relation to the components of the gradient?  Can that be the case for a long period of the training?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
