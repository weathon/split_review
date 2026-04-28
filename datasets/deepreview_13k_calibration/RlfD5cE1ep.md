# Feature Normalization Prevents Collapse of Non-contrastive Learning Dynamics

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Contrastive learning is a self-supervised representation learning framework, where two positive views generated through data augmentation are made similar by an attraction force in a data representation space, while a repulsive force makes them far from negative examples.
  Non-contrastive learning, represented by BYOL and SimSiam, further gets rid of negative examples and improves computational efficiency.
  While learned representations may collapse into a single point due to the lack of the repulsive force at first sight, \cite{Tian2021ICML} revealed through the learning dynamics analysis that the representations can avoid collapse if data augmentation is sufficiently stronger than regularization.
  However, their analysis does not take into account commonly-used \emph{feature normalization}, a normalizer before measuring the similarity of representations, and hence excessively strong regularization may collapse the dynamics, which is an unnatural behavior under the presence of feature normalization.
  Therefore, we extend the previous theory based on the L2 loss by considering the cosine loss, which involves feature normalization.
  We show that the cosine loss induces sixth-order dynamics (while the L2 loss induces a third-order one), in which a stable equilibrium dynamically emerges even if there are only collapsed solutions with given initial parameters.
  Thus, we offer a new understanding that feature normalization plays an important role in robustly preventing the dynamics collapse.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the dynamics of non-contrastive self-supervised learning (e.g. BYOL, SimSiam etc.) and shows how feature normalization can play a role in preventing the collapse of all representations to a single point. By studying this in the infinite dimensional limit, the paper shows, that with the cosine loss, the training dynamics are different from that with L2 loss.

### Strengths
1. The technical analysis appears rigorous and reasonably clear to follow.

### Weaknesses
1. Considering the majority of the analysis assumes norms of all features are nearly same, due to the high dimensional limit, I do not see how this analysis can show the effects of feature normalization on non-contrastive learning. The assumption that feature norms are nearly identical seems to directly contradict the goal of studying the impact of feature normalization, which is intended to address variations in feature magnitudes. If the analysis is performed under the assumption that these magnitudes are already uniform, it is unclear how the results can be generalized to scenarios where feature normalization is actually needed. This makes the connection between the theoretical analysis and the practical implications of feature normalization quite weak.

2. Moreover, the notions of "6-th order dynamics"and "3rd order dynamics" are not sufficiently explained in the paper. The paper introduces these terms without providing a clear definition or intuition for what these orders represent in terms of the training dynamics. It is not clear what is meant by the dynamics being of a certain order, and how this relates to the convergence behavior or stability of the learning process. This lack of clarity makes it difficult to assess the significance of the results.

3. Most importantly, I'm not convinced this an interesting problem to study in the context of prior work providing key understanding regarding how non-contrastive SSL training dynamics work. While the paper claims to study the cosine loss, it is not clear how this analysis provides fundamentally new insights beyond what is already known about the training dynamics of non-contrastive learning. The paper needs to better articulate the specific gap in the literature that it is addressing and why the analysis of cosine loss is crucial for understanding non-contrastive SSL.

### Questions
1. Considering the majority of the analysis assumes norms of all features are nearly same, due to the high dimensional limit, I do not see how this analysis can show the effects of feature normalization on non-contrastive learning. Can the authors explain why they believe this analysis is showing anything meaningful about feature normalization. 

2. Practically, are there any differences in the conclusions of the training dynamics of the cosine loss and the L2 loss? (while they may be of "different orders").

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article proposes an extension of the theory of non-contrastive learning (BYOL, SimSiam) to consider the cosine loss rather than the L2 loss, showing how feature normalization changes from third-order dynamics to sixth-order. 
They show that three regimes exist depending on the norms of the layers, which results in a shift between the three regimes as the norms decrease until the stable regime, where the eigenmodes converge.

### Strengths
This article presents an improvement other than the theoretical framework of non-contrastive learning using solely the Euclidian loss.
The paper is well-written and easy to follow. The assumptions taken are relatively well justified and allow for an interesting analysis.

### Weaknesses
 **Previous literature** There have been recent contributions to the literature of non-contrastive learning which do take into account the cosine loss, and which are not referenced in this article. In particular, Halvagal et al., Implicit variance regularization in non-contrastive SSL, 2023. The eigenmode dynamics seem extremely similar (after some changes in the notation) and it seems extremely important to me that the authors compare themselves to this article. The authors also do not seem to have a similar conclusion on the implicit variance regularization that Halvagal et al. focus on.

 **Regimes** The three regimes found in Section 5.2. seem to have been found solely by categorizing the regimes experimentally shown in Figure 2 while reading, which seems like a weak justification for those regimes. A clearer analysis of the equilibrium points at least in the Appendix seems necessary. 

The authors claim that as the norms decrease, the regimes fall to the stable one. However, in the stable regime, the norms will increase as the eigenmodes increase to the saddle point $p^+$. Is there a risk of the acute and stable regimes alternating between each other? 

 **Experiments** Numerical experiments on the SimSiam model remain on linear networks in Section 5.4. A similar Figure to Figure 6 for a real network such as ResNet (maybe only focusing on the linear projection head) would help confirm the theoretical findings in the linear case. Otherwise, the link with a real SimSiam network remains relatively limited, except for the weight decay argument.

 **Figure 6c** I also find Figure 6.c. hard to read. Are the intervals the theoretical intervals using the values of the norms? In this case, what is the theoretical value of the saddle point? Having the values of a single eigenmode gives very little information on the values of the spectrum of $W$. Do all the values stay relatively constant like here?

### Questions
The notion of Thermodynamic limit is novel to me in optimization and needs to be further explained. How is it different from the Neural Tangent Kernel regime, is it the constant ratio $\alpha$?

Do the authors have more intuition on the role of the exponential moving average in BYOL with their new findings?

Small remarks:
* Intro: "Folklore says" is a somewhat strange way to quote an article.
* Sec 4. Assumption 2. $Σ = I $ seems superfluous to add after $D = N(0, I)$.
* After Lemma 3: $\Phi x'$ is not defined. 
* Equation (5): $\hat H$ is not defined.
* After Equation (9): "unite learning rate"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper follows the previous setting in Tian et al. (2021) which explores simplified modeling for non-contrastive learning. It posits the representation model as an identity function, with both the projection layer and prediction layer streamlined into linear components. What distinguishes this study from its predecessors is the exploration of the commonly used cosine loss in practical applications. By applying these simplifications and introducing additional assumptions, the authors demonstrate that the norms tend to concentrate around some constants, which helps to simplify the learning dynamics with feature normalization. With further assumptions, the paper disentangles the learning dynamics into the sixth-order eigenmode dynamics in which a stable equilibrium emerges even if there is no stable equilibrium with the initial parametrization and regularization strength.

### Strengths
- The paper is well-written and easy to follow.
- This work proves that the feature norm concentrates around a constant with proper parameter initialization.

### Weaknesses
1. Some of the assumptions are quite stringent, especially since this paper is not pioneering work, and they may not provide much reference value for practical non-contrastive learning with negative pairs. 
2. Assumptions 2 and 3 in section 4 are rather strict. Assumption 2 requires that the input data follow an isotropic Gaussian distribution, which is hard to accept in practical situations. Perhaps a mixture of isotropic Gaussians could be considered. Assumption 3 pertains to the width-infinite limit.
3. In section 5, the authors consider the norms of these linear layers as constants (Assumption 5). This assumption, however, is still far from providing a real dynamic analysis for the cosine loss. Since feature normalization may not guarantee convexity, smoothness, and Lipschitzness, its dynamic analysis should focus on proving the convergence rather than simplifying its complexity to obtain closed-formed dynamics. The existing conclusions do not provide much contribution and insight to understanding non-contrastive learning dynamics.
4. The relevant numerical results still do not fully validate the reasonableness of these assumptions, such as the increasing error between $W$ and $W^\top$, and the decrease in $N_{\phi}$ and $N_{\psi}$. Therefore, while I appreciate the authors for using Hanson-Wright inequality to demonstrate that some norms concentrate, it is still not particularly remarkable.

### Questions
Please see weakness

### Soundness
3 good

### Presentation
3 good

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
This paper represents an extension of prior work in the field of Self-Supervised Learning (SSL) theory, with a specific emphasis on elucidating how non-contrastive SSL methods prevent the issue of feature collapse. The paper's primary focus centers on the examination of the final feature normalization step and its role in the underlying dynamics. The authors furnish compelling evidence concerning the dynamics of the underlying eigenmodes, and the theory finds support through numerical simulations.

### Strengths
1. This paper addresses an important and relatively underexplored issue regarding the role of feature normalization in non-contrastive Self-Supervised Learning (SSL). The authors demonstrate that the normalization step introduces sixth-order dynamics, resulting in the dynamic emergence of a stable equilibrium, even when dealing with initially collapsed solutions.

2. The authors present compelling evidence, and their underlying assumptions appear to be quite reasonable.

3. Numerical simulations validate the predictions made by the theory.

### Weaknesses
I would anticipate the theoretical framework to align with the behavior observed in real datasets. However, the paper does not investigate the dynamics in more complex scenarios.

### Questions
The authors mentioend BarlowTwins and VICReg. They effectively are still contrastive. How do you think their 'feature normalization' behavior is related?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
