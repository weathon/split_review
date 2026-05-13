# Speed Limits for Deep Learning

- Decision: Reject
- Scores: 3, 6, 8, 6

## Abstract
State-of-the-art neural networks require extreme computational power to train. It is therefore natural to wonder whether they are optimally trained. Here we apply a recent advancement in stochastic thermodynamics which allows bounding the speed at which one can go from the initial weight distribution to the final distribution of the fully trained network, based on the ratio of their Wasserstein-2 distance and the entropy production rate of the dynamical process connecting them. Considering both gradient-flow and Langevin training dynamics, we provide analytical expressions for these speed limits for linear and linearizable neural networks, e.g. Neural Tangent Kernel (NTK). Remarkably, given some plausible scaling assumptions on the NTK spectra and spectral decomposition of the labels-- learning is optimal in a scaling sense. Our results are consistent with small-scale experiments with Convolutional Neural Networks (CNNs) and Fully Connected Neural networks (FCNs) on CIFAR-10, showing a short highly non-optimal regime followed by a longer optimal regime.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The goal of the paper is to explore a notion of training time efficiency in deep learning through the lens of optimal transport and stochastic thermodynamics. The main technical tool is the Benamou-Brenier formula in optimal transport theory, which casts the $L^2$-Wasserstein distance $(W_2$) between initial and final distributions ($\mu_0$ and $\mu_T$) as the minimum of a specific cost functional over smooth paths $(\mu_t)_{0\leq t\leq T}$ induced by time-dependent potentials. The formula provides a lower bound on the transport time (T) in terms of $W_2$ and path-dependent cost.

The authors apply this bound to Langevin dynamics and gradient flow, focusing on linear and kernel regression. They propose to use (a tractable limit of) the bound as a metric for 'training speed inefficiency' in deep learning. Experiments with CNNs trained on small subsets of CIFAR10 with full batch gradient descent on mean squared loss reveal an initial 'inefficient' training phase, corresponding to an alignment of the NTK to the target, followed  by a phase where learning becomes 'efficient,' as evidenced by the training time saturating the proposed bound.

### Strengths
The paper introduces an innovative perspective by leveraging the speed limit concept from optimal transport theory to shed light on the training efficiency in deep learning. Given the importance and challenge of characterizing the training speed and efficiency of neural networks,  new theoretical insights in this topic are timely and have the potential for significant impact.

### Weaknesses
## Significance

### Narrowness of the theoretical setting

Only two setups have been studied: linear regression and NNs in the NTK regime. This is a significant limitation, as the NTK regime, with its infinite-width assumptions, often fails to capture the complexities of finite-width neural networks used in practice. The continuous-time SGD assumption is also a strong simplification that does not accurately model the discrete updates of practical SGD, which could lead to qualitatively different behaviors. The authors do not address how the derived training time lower bound, $T_{SL}$, obtained in the NTK regime, would compare to a similar bound derived for finite-width NNs. It is unclear whether $T_{SL}$ would be larger or smaller, and how the scaling with network size would be affected.

### Motivation

Given the theoretical framework, the connection of this work to the practical challenges in deep learning is not clear. It is not evident how this work could be used to improve optimization algorithms or to obtain theoretical guarantees applicable to real-world scenarios. The paper does not address whether the proposed framework could be used to analyze the performance of different optimizers or to guide the design of more efficient training strategies. The practical implications of this theoretical analysis are not well-defined.



### Questions
**Miscalleneous**

* In Eq (7), (27), (28): the Wasserstein distance should be squared. 

* Deriving (6) from (5) may not be straightforward, as the term $\nabla_\theta \ln p$ in the integrand of (5) might depend on $\beta$. Additionally, while the derivation of (5) from (41) in Appendix A.6 is acknowledged, the derivation of (41) appears to lack normalization factors (log Z+/Z-) corresponding to the forward and backward distributions. It's not immediately clear to me if these factors cancel each other out.

### Soundness
2 fair

### Presentation
1 poor

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
This paper proposes a study of the "time" it takes for a neural network (NN) to travel from its initialization distribution to its final distribution (after training). The study is based on of the transport of the distribution of the parameters and the related evolution of the entropy of the system. To use this theoretical framework, it is necessary to do some assumptions: continuous-time training, full-batch optimization, simplified models (linear regression, Neural Tangent Kernel (NTK) setting), etc.

This theoretical study comes with a series of experiments, with a setting as close as possible as the theoretical assumptions (small learning rates, full-batch gradient descent). The experimental results are not entirely consistent with the theoretical predictions. The authors claim that the "training time" they have computed theoretically is close to the actual training time of NNs in the experiments.

### Strengths
## Originality

To my knowledge, this work is original. But I am not a specialist of statistical physics applied to NNs.

## Clarity

The authors made the effort to make their paper understandable to the reader who would not be a specialist in statistical physics applied to NNs. Overall, the paper is easy to read.

## Quality

The experimental section, despite being narrow (only one setting has been tested), provides enough results to evaluate the significance and the limitation of the theoretical section.

### Weaknesses
It is unclear if the near optimal scaling efficiency result applies to large realistic models and datasets. The CIFAR-10 study used very small networks. It would be very nice to see an empirical example with a larger scope.

Further, it would be nice to be more explicit of how much of the entropy production is due to the presence of nonzero initial weights. It would be nice to cover the case of either the perceptron or the NTK starting with $\theta_0 = 0$.

It is rather unclear whether there are any takeaways from practitioners. Its not strictly necessary that their should be, but given the title one is left to wonder whether there are possible statements that can be made about the compute-optimal frontier.

### Questions
Main questions:
 * motivation: can we use this work to evaluate the quality of an optimizer?
 * stronger results: how does the $T_{SL}$ obtained in the NTK limit relate to some "$T_{SL}$" in the finite width setting?
 * experimental setup: the authors claim that a learning rate of $10^{-5}$ is small and apply the NTK setting to Myrtle-5; how to justify these choices? Is $10^{-5}$ really small enough? is Myrtle-5 wide enough to consider that we are in the NTK regime?

Other questions:
 * Eqn (10) is difficult to interpret: in the proof, the effective learning rate is $\eta/n$; how such a proof can be interpreted in the limit $n \rightarrow \infty$?
 * I may have misunderstood one point: Figure 1.b seems to indicate that the training time is about $10$-$30$ times larger than $T_{SL}$. We are far from the "$O(1)$" factor written in the claims... while it is true that the ratio of the trajectory lengths (Fig. 1.e) is of order 1. How to solve this contradiction?
 * it is clear to me that the result written in Eqn. (10) depends on the distribution of the data. To obtain such a result, the data are assumed to be Gaussian. It is then not surprising that Fig. 1.d contradicts Eqn. (10), since CIFAR-10 images are far from being Gaussian vectors.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies recent advances in stochastic thermodynamics to analyze the efficiency of training neural networks. It derives analytical expressions relating the speed limit (minimum training time) to the Wasserstein 2-distance between initial and final weight distributions and the entropy production. For linear regression and neural networks in the NTK regime, exact formulas are provided for the quantities involved in the speed limit. Under plausible assumptions on the NTK spectrum (power law behavior) and residue (defined as the target minus the initial prediction), NTKs exhibit near-optimal training efficiency in the scaling sense. Small-scale experiments on CIFAR-10 qualitatively support the theoretical findings.

### Strengths
I think this is a technically sound paper that makes good contributions. The application of stochastic thermodynamics concepts to neural network training is novel. I have not seen it before in prior literature. The analysis done in the paper is insightful and to the best of my knowledge seems mathematically rigorous. The results on optimal scaling efficiency are intriguing. The writing is clear and relatively compact. It seems like the relevant prior works cited correctly. Moreover this paper provides a good literature review on various different topics across entropy production and the various bounds on that quantity.

### Weaknesses
1. I am not sure about the significance of this theoretical investigation. It seems that the paper only considers the lower bound of the time that goes from an initial parameter state to a target parameter state. It does not tell us information about e.g. the time lower bound to get to a near-stable parameter state, or the time lower bound to get to near-zero potential. The analysis appears to focus solely on the time required to transition between two arbitrary parameter states, without providing insights into the convergence behavior towards a stationary point, which is often the primary concern in optimization. Furthermore, the practical implications of this bound are unclear, as it is not immediately obvious how it relates to the actual training dynamics and convergence to a useful solution.

2. Characterizing the speed limit using the Wasserstein-2 distance is not easily interpretable since it is in general hard to compute the Wasserstein-2 distance. The paper seems only able to derive interpretable results under limiting conditions like no noise or infinite parameters. The reliance on the Wasserstein-2 distance as a measure of distance between parameter distributions is problematic due to its computational intractability in general settings. The paper's ability to derive meaningful results only in simplified scenarios, such as those with no noise or infinite parameters, limits the practical applicability of the theoretical framework. The lack of a clear connection between the derived bounds and the behavior of optimization in realistic scenarios hinders the usefulness of the results.

3. The models considered in this paper are fairly simple. Both the linear regression and the learning under NTK assumption are linear models and are not representative of deep learning in general. The analysis is limited to linear models, specifically linear regression and neural networks under the Neural Tangent Kernel (NTK) regime. These models are not representative of the complexities of deep learning, where non-linearities and feature learning play a crucial role. The theoretical framework does not address the challenges posed by non-convex optimization and feature learning in deep neural networks, which are critical for practical applications.

4. The writing of the paper can be improved. I hope to see formal theorems in the paper stating the main contribution, and notations need to be clearly stated. For instance, I am not sure what is $Z_T$ and $Z_0$ in Eq. (4). There is also no related works section. The absence of clearly stated theorems makes it difficult to assess the main contributions of the paper. The lack of clarity in notation, such as the definition of $Z_T$ and $Z_0$ in Eq. (4), hinders the understanding of the presented results. Additionally, the omission of a related works section makes it challenging to position the paper's contributions within the existing literature.

### Questions
It's interesting that power law scalings in the target (ie in the residues) seem to imply an inefficiency factor that grows with dataset size. Can the authors comment on whether this is representative of realistic datasets? 

The initial transient period seems important. The current characterization is that the low modes are learned very quickly during this period, however many other things are also happening. For one, the kernel could be drastically realigning its eigenstructure (as in e.g. Atanasov Bordelon Pehlevan https://arxiv.org/abs/2111.00034). Relatedly, it would be interesting to see these empirical results for the NN as the feature learning parameter (as in $\alpha$ in Chizat and Bach https://arxiv.org/abs/1812.07956) is varied. 

It seems strange that in the high noise regime the formalism tells the perceptron learns in "zero time" when really its unable to learn at all. Am I understanding this correctly? 

To the best of my understanding, the only setting in which the W2 distance enters practically is when the marginals are delta functions. So it only is realized as the 2-norm in weight space. Is there any use to the optimal transport formalism beyond this?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This problem considers the continuous dynamic of gradient-based learning problems. Studying the problem from a thermodynamic perspective, the paper derives a lower bound on the time for a process to go from an initial state to a target state using Wasserstein-2 distance. The paper further considers two realizations of the problem, namely the linear regression and the NTK, and presents the implication of the result under various limiting scenarios.

### Strengths
1. It seems an interesting idea to connect the machine learning optimization dynamic with notions in thermodynamics.

2. The paper provides interesting interpretations of the speed limit in linear regression and NTK learning.

### Weaknesses
1. I am not sure about the significance of this theoretical investigation. It seems that the paper only considers the lower bound of the time that goes from an initial parameter state to a target parameter state. It does not tell us information about e.g. the time lower bound to get to a near-stable parameter state, or the time lower bound to get to near-zero potential.

2. Characterizing the speed limit using the Wasserstein-2 distance is not easily interpretable since it is in general hard to compute the Wasserstein-2 distance. The paper seems only able to derive interpretable results under limiting conditions like no noise or infinite parameters.

3. The models considered in this paper are fairly simple. Both the linear regression and the learning under NTK assumption are linear models and are not representative of deep learning in general.

4. The writing of the paper can be improved. I hope to see formal theorems in the paper stating the main contribution, and notations need to be clearly stated. For instance, I am not sure what is $Z_T$ and $Z_0$ in Eq. (4). There is also no related works section.

### Questions
Given the conclusion in the paper that in the NTK regime the dynamic in the paper achieves a rate that is almost optimal, is this contradicting the fact that the continuous heavy-ball dynamic achieves a faster rate to converge to the stable point (see, e.g. https://link.springer.com/article/10.1007/s1022-01164-w)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
