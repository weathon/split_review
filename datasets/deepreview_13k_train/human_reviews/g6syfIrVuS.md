# Local Loss Optimization in the Infinite Width: Stable Parameterization of Predictive Coding Networks and Target Propagation

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Local learning, which trains a network through layer-wise local targets and losses, has been studied as an alternative to backpropagation (BP) in neural computation. However, its algorithms often become more complex or require additional hyperparameters because of the locality, making it challenging to identify desirable settings in which the algorithm progresses in a stable manner.
To provide theoretical and quantitative insights, we introduce the maximal update parameterization ($\mu$P) in the infinite-width limit for two representative designs of local targets: predictive coding (PC) and target propagation (TP). We verified that $\mu$P enables hyperparameter transfer across models of different widths.
Furthermore, our analysis revealed unique and intriguing properties of $\mu$P that are not present in conventional BP. By analyzing deep linear networks, we found that PC's gradients interpolate between first-order and Gauss-Newton-like gradients, depending on the parameterization.  
We demonstrate that, in specific standard settings, PC in the infinite-width limit behaves more similarly to the first-order gradient.
For TP, even with the standard scaling of the last layer, which differs from classical $\mu$P, its local loss optimization favors the feature learning regime over the kernel regime.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
This paper investigates local learning methods for neural networks as alternatives to backpropagation. It specifically focuses on predictive coding (PC) and target propagation (TP). The authors introduce maximal update parameterization (µP) for PC and TP in the infinite-width limit to enable hyperparameter transfer across different model widths, aiming to stabilize local loss optimization. They analyze deep linear networks to show that PC’s gradient transitions between first-order and Gauss-Newton-like gradients depending on parameterization. For TP, they find that µP favors feature learning over the kernel regime, a distinction from traditional BP.

### Strengths
- The paper is well-written. 
- The problem is conceptually well motivated.
-  The manuscript includes both rigorous proofs and empirical experiments that validate the findings. 
- The observation that the optimal learning rate does not depend on the order of width is interesting. 
- The disappearance of the kernel regime in TP is interesting.

### Weaknesses
1. The derivation of $\mu P$ assumes one-step gradient 
2. The derivation also assumes linear networks 
3. It is unclear how the findings extend to more general settings

### Questions
1. In the preliminaries I can't find any definition for $\mathcal{L}$, I assume it is the loss function, are there any particular assumptions about it? 
2. A precise definition of the Maximal Update Parametrization in the text would be useful, especially for readers unfamiliar with the related work. 
3. In equation 5, where is $\psi$ defined? 
4. Could the authors provide a more precise definition of stable training dynamics? 
5. Is the transfer of learning rates also observed for Cross Entropy loss? 
6. How sensitive are $\mu P$  and $\mu$Transfer to different initialization schemes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The submission presents derivation of the initialization and step-size scaling required to achieve hyperparameter transfer across width using the $\mu P$ parameterization in the infinite width limit for two local learning algorithms, predictive coding and target propagation.

### Strengths
To my knowledge, the results are new as the infinite width limit has not received as much attention for local learning as for the typical backpropagation-based methods. The objectives of the paper are clear and the paper executes on its premises. The experimental results support the claim that the derived parameterization does achieve hyperparameter transfer.

### Weaknesses
The paper deals with two very specialized subjects, local learning and infinite-width limits. As a result, it has a difficult job in making its argument clear to a general audience. The current writing makes a reasonable attempt, but there are still points that can be clarified to help guide the reader that might be only be vaguely familiar with one of the topic. I give a list of specifics in the questions below.

The discussion of the implications of the $\mu P$ parameterization for PC after corollary 4.3 and in §4.3, on the impact of the free parameter $\gamma$, is very technical. It is not clear what the broader implications of $\gamma = 0$ or $\gamma = 1$ or the fact that the the PC gradients are more similar to those of standard backprop GD or GNT. A higher-level description of what the parameter $\gamma$ represents, and what it means to be closer to 0 or 1, would help the reader grasp the importance of the results.

- It would be worth to explicitly state that, by definition, $\mu P$ depends on the algorithm used, and therefore needs to be derived to figure out what $\mu P$ means in the context of PC and TP, which is the contribution of this paper. The sentence before the list of contributions leaves the "$\mu P$ depends on the algorithm" part implicit.

- The word "inference" is heavily overloaded in ML and a clarifying note as to what it means for PC in §2 would help. This is adressed later in §3.1 but a short parenthetical might be worth including.

- "The parameterization that induces the feature learning regime is called $\mu P$" This phrasing implies that there is a unique parameterization that induces feature learning. It seems that the authors instead mean that "$\mu P$ induces the feature learning regime"?

- "The training dynamics are referred to as stable when they neither vanish nor explore as the network width increases" What quantitiy should neither vanish nor explode?

- "the parameterization that achieves this [non-vanishing and non-exploding] is called a stable parameterization" The phrasing as "the parameterization that achieves this" implies that this parameterization is unique. Is this what is meant or should it be "a"?

- In table 1; reminding the reader of what the parameters $b_l$, $c_l$ and $\gamma_l$ would help, e.g. $b_l$: initialization of the weights, $c_l$: scaling of the step-size. Adding a legend would help remind the reader of what SP, SGD, GNT, PC and TP mean.

- Line 271-272 "the $\mu P$ of BP can be directly transferred to PC" should also mention "and leads to parameter transfer across width", as this is what the figure shows.

- Please add that $\theta_l = 2a_l + c_l$ to the statement of Thm 4.1, assuming that those parameters indeed have the same meaning as in Prop 3.3.

- An additional experiment showing that the $\mu P$ for SGD does not lead to hyperparameter transformer on PC without FPA would strenghten the claim that the $\mu P$ for PC is necessary

- It is not clear whether the difference between GD, (S)GD and SGD is intended to meaningful or whether they are used interchangeably. If it is not, would it make sense to standardize to GD or (S)GD?

- Figure 2 should explicitly state what is being compared; The cosine similarity measures the similarity between what and what?

### Questions
The discussion of the implications of the $\mu P$ parameterization for PC after corollary 4.3 and in §4.3, on the impact of the free parameter $\gamma$, is very technical. It is not clear what the broader implications of $\gamma = 0$ or $\gamma = 1$ or the fact that the the PC gradients are more similar to those of standard backprop GD or GNT. A higher-level description of what the parameter $\gamma$ represents, and what it means to be closer to 0 or 1, would help the reader grasp the importance of the results.

- It would be worth to explicitly state that, by definition, $\mu P$ depends on the algorithm used, and therefore needs to be derived to figure out what $\mu P$ means in the context of PC and TP, which is the contribution of this paper. The sentence before the list of contributions leaves the "$\mu P$ depends on the algorithm" part implicit.

- The word "inference" is heavily overloaded in ML and a clarifying note as to what it means for PC in §2 would help. This is adressed later in §3.1 but a short parenthetical might be worth including.

- "The parameterization that induces the feature learning regime is called $\mu P$"
  This phrasing implies that there is a unique parameterization that induces feature learning. It seems that the authors instead mean that "$\mu P$ induces the feature learning regime"?

- "The training dynamics are referred to as stable when they neither vanish nor explore as the network width increases"
  What quantitiy should neither vanish nor explode?

- "the parameterization that achieves this [non-vanishing and non-exploding] is called a stable parameterization"
  The phrasing as "the parameterization that achieves this" implies that this parameterization is unique. Is this what is meant or should it be "a"?

- In table 1; reminding the reader of what the parameters $b_l$, $c_l$ and $\gamma_l$ would help, e.g. $b_l: initialization of the weights, $c_l$: scaling of the step-size. Adding a legend would help remind the reader of what SP, SGD, GNT, PC and TP mean.

- Line 271-272 "the $\mu P$ of BP can be directly transferred to PC" should also mention "and leads to parameter transfer across width", as this is what the figure shows.

- Please add that $\theta_l = 2a_l + c_l$ to the statement of Thm 4.1, assuming that those parameters indeed have the same meaning as in Prop 3.3.

- An additional experiment showing that the $\mu P$ for SGD does not lead to hyperparameter transformer on PC without FPA would strenghten the claim that the $\mu P$ for PC is necessary 

- It is not clear whether the difference between GD, (S)GD and SGD is intended to meaningful or whether they are used interchangeably. If it is not, would it make sense to standardize to GD or (S)GD?

- Figure 2 should explicitly state what is being compared; The cosine similarity measures the similarity between what and what?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work studies parameterisation for local learning algorithms: for predictive coding and target propagation. The main goal is to understand maximal update parameterization ($\mu P$), which allows transfer of hyperparameters across different widths. Authors prove optimal $\mu P$ from one step of descent or for linear networks. Experimental results are provided based on Fashion MNIST.

### Strengths
Authors give a thorough analysis of parametrization in local learning, motivated by previous progress of $\mu P$ in backpropagation. The question is well-motivated by the fact that model sizes for local learning are increasing, thus it is important to understand which parameterizations are robust to scaling up the models. 

Experimental results on FashionMNIST confirm theoretical findings.

### Weaknesses
Presentation of the paper can be improved, in particular the notation section. Choice of $\mathcal{L}$ is not introduced, notation for $\gamma_l$ should be defined before Section 3.1. Also, $\bar \gamma_L$ is an important quantity, but is only defined implicitly in Theorem 4.1.

Both sections on PC and TP were a bit hard to follow (for someone outside of the field): In PC, for example, Equation (3) should also be complemented by the case $\ell = L - 1$.

In Table 1, adding references to prior work and highlighting new contributions will be helpful.

### Questions
How is $\eta'_l$ chosen in Equation (8)? Is it tuned in the experiments?

Figure 3: what is the cause of sharp loss increase in the loss of wide networks when $\bar \gamma_L < -1$? Is there some theoretical explanation? Can be it that for $\bar \gamma_L = -1$, training would also diverge for wide enough network?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers maximal update parameterization for local learning, an alternative to backpropagation for optimizing neural networks. In particular, the authors consider predictive coding and target propagation. 

The authors develop theory to show that hyperparameters can be transferred between networks of differing widths, matching existing guarantees for backpropagation, which helps reduce the amount of computation required for training with local learning. Further, they prove that under certain assumptions, target learning reduces to gradient descent, which implies that backpropagation and local learning will converge to the same model.

### Strengths
Originality: I’m not so familiar with this subfield, but in so far as I can tell, this work seems very novel as it seems to be the first work to introduce $\mu$P for local learning. The authors provide theoretical guarantees showing that it is possible to reduce the required amount of hyperparameters in local learning. 

Quality: The theoretical results are well-justified by detailed proofs in the appendix and references to prior works. The authors provide empirical justification on real-world datasets as well.

Significance: The paper is significant as it provides justification on why local learning can match performance of models trained by back-propagation.

### Weaknesses
The content is rather inaccessible as the assumed knowledge is too specific for a broad conference such as ICLR. I have background in mean-field networks, but not local learning or $\mu$P. It would be useful to add a brief appendix on these as a background (beyond what is already described in Section 3) to help the reader understand the paper.

The paper is also hard to follow due to the amount of abbreviations. It would also be useful to add backreferences for the techniques F-ini and FPA in lines 158, 162.

Some of the theorems are missing assumptions, notation, or intuition. For example, in Prop. 3.3 (line 250), what are $\delta_l$, $e_L$? In Cor. 4.3 (line 350), why do we need $a_L + b_L = 1$?

The experimental results are on relatively small datasets, e.g. FashionMNIST and CIFAR10: it would be nice to have validation on CIFAR100 as well.

### Questions
Line 200: what is abc-parametrization?

Line 278: what is $M^{\overline{\gamma}_L}$?

Line 309: what is $\mu$Transfer? A reference here would be helpful.

What would the challenges be in extending the analysis to non-linear networks? 

[HRSS19 Mean-field Langevin dynamics and energy landscape of neural networks, arXiv preprint arXiv:1905.07769] studies infinite-width neural networks via the lens of mean-field Langevin dynamics. Would it be possible to study local learning through this lens, and could this potentially mitigate the requirement to develop a tensor program (line 535)?

### Soundness
3

### Presentation
1

### Contribution
3
