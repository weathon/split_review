# Test like you Train in Implicit Deep Learning

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Implicit deep learning has recently gained popularity with applications ranging from meta-learning to Deep Equilibrium Networks~(DEQs).
In its general formulation, it relies on expressing some components of deep learning pipelines implicitly, typically via a root equation called the inner problem.
In practice, the solution of the inner problem is approximated during training with an iterative procedure, usually with a fixed number of inner iterations.
During inference, the inner problem needs to be solved with new data.
A popular belief is that increasing the number of inner iterations compared to the one used during training yields better performance.
In this paper, we question such an assumption and provide a detailed theoretical analysis in a simple setting.
We demonstrate that overparametrization plays a key role: increasing the number of iterations at test time cannot improve performance for overparametrized networks.
We validate our theory on an array of implicit deep-learning problems.
DEQs, which are typically overparametrized, do not benefit from increasing the number of iterations at inference while meta-learning, which is typically not overparametrized, benefits from it.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies when increasing the number of fixed-point iterations in implicit deep learning during test time improves performance. In implicit deep learning, the network must _implicitly_ minimize the objective $\ell(z(\theta))$. Specifically, the network parameters $\theta$ control some intermediary output $z(\theta)$ which tends to be the solution of some inner rootfinding problem $f(z, \theta, D_{train}) = 0$. The solution $z(\theta)$ is often identified through some $N$ fixed-point updates during training, then during test time, the solution is updated using test data using more fixed-point updates. This helps in certain applications like meta-learning and not others like DEQ. 

The paper attempts to prove that this difference (helping in certain cases and not others) can be explained by the degree $\theta$ is overparameterized for the inner problem. They prove lower bounds for how much the training loss can change when changing the number of fixed-point iterations for an affine inner problem.

### Strengths
- The paper is generally clear and easy to follow. 
- Excluding a couple minor things (bullet points below), the proofs in Appendix Section A for the main theorems in the main body seem to be correct. 
    - Between Eq. 22 and 23, it says “Therefore $z_{N+1}$ is also in the range of $K^\top$, should say $z_{N+1} - z_0$. 
    - Eq 30 has some problems with the signs, although the final form Eq 31 seems to be correct. 
- The empirical results in Figures 2/3 seem to support their hypothesis that overparameterization leads to less improvements with more inner updates.

### Weaknesses
 - As already pointed out by the authors, there is a major inconsistency between what the paper tries to prove and what is actually proven. During inference, the inner optimization is conducted on the _test data_. However, the paper’s results are only showing how the _training_ loss can fluctuate with the number of inner optimization updates. The problem with this relaxation is because it interferes directly with the paper’s core result, that network overparametrization is why more inner optimization steps do not help. One can imagine in the overparametrized setting, the test loss/inner problem could be significantly different from the training loss/inner problem, causing an analysis on just the training loss to fall apart. I may be misunderstanding the paper however, and so I vote for a low score with low confidence.

- I think the authors can be more precise about what they mean by overparametrization. Formally, they do define it as $d_x < d_	heta$ in Corollary 1, but it might be good to clarify how $d_x$ scales for the different applications (DEQ, meta-learning) in the main body. Is this definition related to the classic usage of the term “overparametrization” as the number of parameters being larger than the number of training data in linear models? And the word overparametrization is a bit thrown around loosely in the paper. 

- Figure 4 plots $D(N, \Delta N)$ of the training loss for different levels of “overparameterization” which they measure using the training loss (lower training loss → more expressive model). They conclude from the experiment that “The lower the training loss, the higher the $D(N, \Delta N)$”. This comparison seems a bit unfair and requires normalizing $D(N, \Delta N)$ with respect to the training loss. For a loss lower bounded by 0 (like most losses), if the training loss is already small, the lowest possible improvement with more fixed point iterations $D(N, \Delta N)$ obviously gets smaller. 


- There’s some minor spacing issue of Figure 2

### Questions
- What is “convergence” plotted in FIgure 2?
- I am not too familiar with meta-learning literature and am a bit confused about doing the fixed-point iterations during inference, specifically for meta-learning. As implied by Equation 5, it seems to require access to test labels..Is the inner optimization during inference conducted on the test data using labels?

### Soundness
2 fair

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
This paper focuses on the inner iterations overfitting problem of overparameterized models in implicit deep learning, and provides theoretical results in a simplified affine setting to show that increasing the number of iterations at test time cannot improve
performance for overparametrized models. Two typical implicit deep learning methods, DEQ and iMAML, are considered in the paper. Experiments on diverse tasks verifies the theorem on both DEQ and iMAML.

### Strengths
1. The paper is well written and easy to follow.
2. The definition and analysis of inner iterations overfitting problem is novel and will be helpful for future researches on implicit deep learning.

### Weaknesses
Experiments can be further improved. Fore example, 
- it only considers the case where $N$ is fixed while $\Delta N$ varies (e.g., Figure 2 & 3). Does the conclusion hold for other choices of $N$?
- Theorem 1 is validated on a small scale dataset. It will be helpful to validate it on real dataset.

### Questions
See the section of Weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates implicit deep learning, particularly in meta-learning and Deep Equilibrium Networks (DEQs). A common belief is that increasing the number of iterative solutions (inner iterations) during inference improves performance. This study challenges that notion, providing a theoretical analysis that highlights overparametrization as a crucial factor. The findings reveal that overparametrized networks, like DEQs, don't benefit from extra iterations at inference, while meta-learning does.

### Strengths
The topic is interesting, and the paper clearly states the motivation, system model, and assumptions.

### Weaknesses
1. It is hard to interpret the meaning of main theorems. For example, Eq. (9) in Theorem 1 contains orthogonal projections and $E_N$ while their values are unknown. The lack of clarity regarding the specific nature of the orthogonal projection (i.e., onto which subspace?) and the dependence of $E_N$ on the network parameters and training data makes it difficult to assess the practical implications of the theorem. Furthermore, the theorem's statement lacks sufficient context to understand the conditions under which the bound would be meaningful or practically achievable. It is unclear how these terms relate to the actual iterative process within the implicit layers, making the result difficult to interpret.

2. The tightness of the bounds shown in these theorems is not discussed. It will be beneficial to use a figure to compare the actual value and the analytical bound. Without an analysis of the bound's tightness, it's difficult to gauge its practical relevance. A loose bound might not provide much insight, while a tight bound would be more informative. The absence of empirical validation or comparison against actual performance makes it challenging to determine the practical utility of the derived bounds. A figure comparing the theoretical bound with empirical results would be extremely beneficial.

### Questions
The major questions I have are about $D(N,\Delta N)$, i.e., the change of the training loss after changing number of inner iterations by $\Delta N$ for a fixed learned $\theta^{\*,N}$. First, this definition seems problematic because when $N$ changes, $\theta^{\*,N}$ should change. In other words, we should not fix $\theta^{\*,N}$. Second, this is on training loss, not the test loss. The relationship between training loss and test loss is not trivial, especially when overparameterized. In the paper, the authors claim that "This quantity is a proxy for the increase in test loss, provided we have access to enough training data", which I doubt since the meaning of "enough training data" is very vague (or even contradictory) in the context of overparameterization.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
