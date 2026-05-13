# Be More Diverse than the Most Diverse: Online Selection of Diverse Mixtures of Generative Models

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
The availability of multiple training algorithms and architectures for generative models requires a selection mechanism to form a single model over a group of well-trained generation models. The selection task is commonly addressed by identifying the model that maximizes an evaluation score based on the diversity and quality of the generated data. However, such a best-model identification approach overlooks the possibility that a mixture of available models can outperform each individual model. In this work, we explore the selection of a mixture of multiple generative models and formulate a quadratic optimization problem to find an optimal mixture model achieving the maximum of kernel-based evaluation scores including kernel inception distance (KID) and Renyi kernel entropy (RKE). To identify the optimal mixture of the models using the fewest possible sample queries, we propose an online learning approach called *Mixture Upper Confidence Bound (Mixture-UCB)*. Specifically, our proposed online learning method can be extended to every convex quadratic function of the mixture weights, for which we prove a concentration bound to enable the application of the UCB approach. We prove a regret bound for the proposed Mixture-UCB algorithm and perform several numerical experiments to show the success of the proposed Mixture-UCB method in finding the optimal mixture of text-based and image-based generative models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Given a group of generative models, this paper studies the problem of improving the diversity (and quality) of generated outputs by combining them into an (optimal) mixture. The authors present the Mixture-UCB framework, encompassing two specific algorithms, Mixture-UCB-CAB and Mixture-UCB-OGD, designed by iteratively optimizing a quadratic objective (wrt the mixture weights) on kernel-based eval metrics and efficiently formulating the mixture of models under an online bandit setting. Specific metrics include Kernel Inception Distance (KID) and Rényi Kernel Entropy (RKE). Theoretical regret bounds have provided adequate support for Mixture-UCB-CAB, and experimental evaluations demonstrate the advantages of both algorithms across various datasets and model types.

### Strengths
1. The paper is generally well-written and well-structured, with clear definitions and visualizations.
2. The focus on mixtures of generative models to achieve superior diversity (and quality) appears innovative and addresses a limitation in traditional model selection approaches, which aim to find only a single best-performing model. Being able to customize the support size of the mixture is a good plus. 
3. The theoretical analysis for Mixture-UCB-CAB is well-formulated and provides near-optimal guarantees (i.e., up to logarithmic factors of $m$ and $T$).
4. The diverse experiments demonstrate the algorithms' practical applications and performance gains, especially in exciting domains such as text-to-image generation.

### Weaknesses
1. While Mixture-UCB-OGD seems computationally more efficient than Mixture-UCB-CAB, the absence of a theoretical guarantee akin to Theorem 2 for CAB leaves an open question about its convergence and reliability. Specifically, the lack of a formal proof regarding the convergence of the online gradient descent (OGD) update rule in the context of the kernel-based objective function is a significant concern. The algorithm's reliance on empirical performance without a clear understanding of its convergence properties makes it difficult to assess its robustness and potential failure modes.
2. Linear mixtures show their ability to enhance diversity. Still, the data distributions might produce mixtures that lack coherence, as some of the visual examples hint at (e.g., in Figure 3, the mixture model generated both realistic and unrealistic car images). In other words, optimizing the single diversity metric may not capture users' needs (e.g., a model that can generate images of cars with different sizes, poses, coloring styles, and backgrounds may be more natural to be said "diverse"). The issue is that the current diversity metrics, such as KID and RKE, might not fully capture the nuances of what a user perceives as diverse. For instance, a mixture that combines outputs from a photorealistic model and a cartoonish model might score high on these metrics, but the resulting images might not be semantically coherent or useful for a specific application.
3. The mixture model approach may not be suitable for memory-efficient use cases, such as deployment on end devices like smartphones or smart home modules. Storing, updating, and switching among multiple generative models (e.g., this might require loading new parameters into memory) could significantly increase memory requirements and other costs, making the approach impractical for some critical applications. A possible mitigation strategy could be distilling a mixture of large models into a single, smaller-scale model, thereby retaining the benefits of the mixture while reducing resource needs. The practical challenges of managing multiple models, including the overhead of loading and switching between them, are not fully addressed, especially in resource-constrained environments.

### Questions
Could the authors kindly consider the weaknesses highlighted above and share any thoughts, feedback, or responses they might have? Also, I wonder about the typical scenarios where the mixture models fail to improve diversity or quality.

### Soundness
3

### Presentation
3

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
This paper aims to solve the online selection task over a group of well-trained generation models. It explores the selection of a mixture of multiple generative models and formulate a quadratic optimization problem to optimize the kernel-based evaluation scores including kernel inception distance (KID) and Renyi kernel entropy (RKE). Specifically, it proposes an online learning approach called Mixture Upper Confidence Bound (Mixture-UCB). Theoretically, regret analysis is provided for one method (Mixture-UCB-CAB). Experimental results illustrate the effectiveness of the proposed method for text-based and image-based generative models.

### Strengths
1. Overall, this paper is well-written and easy to follow.
2. The proposed method (Mixture-UCB) is somehow novel, although it is inspired by classical UCB in the multi-armed bandit setting.
3. Theoretical results about the regret bound are provided for the proposed Mixture-UCB-CAB. The proof seems right although I have not checked the proof line-by-line.
4. Empirical results illustrate the effectiveness of the proposed method in finding the optimal mixture of text-based and image-based generative models.

### Weaknesses
1. I am afraid that the online selection of well-trained generative models might have few applications because it is already costly for the (large) generative model inference, then why do we need online selection rather than batch selection? Discussions about practical applications can be added. Specifically, the paper does not clearly articulate scenarios where the computational overhead of maintaining and updating the mixture weights online is justified over a simpler batch selection approach. For instance, if the generative models are static and the data distribution is not changing, a single batch evaluation might be sufficient. The paper needs to provide a more compelling argument for the necessity of online selection, perhaps by considering dynamic environments or non-stationary data distributions.
2. Experimental results show that Mixture-UCB-OGD might be better than Mixture-UCB-CAB. However, theoretical guarantees about Mixture-UCB-OGD are missing. I know it might be more challenging and more detailed discussions can be added to clarify why. The lack of theoretical guarantees for Mixture-UCB-OGD, despite its empirical performance, is a significant weakness. The paper should discuss the potential risks associated with using an algorithm without theoretical backing. For example, under what conditions might Mixture-UCB-OGD perform poorly, and how can we mitigate these risks? Furthermore, the paper should explore the possibility of providing at least some partial theoretical analysis, even if a full regret bound is not feasible, such as convergence analysis or stability analysis.

### Questions
In practice, FID metric is widely-used in the evaluation of generative models. Can this paper cover this metric and why?

### Soundness
2

### Presentation
3

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
In this paper, the authors focus on the online selection of generative models, and in particular, the optimal linear mixture among a set of such models.
The problem appears novel, and the authors make interesting connections to the maximization of some kernel-based scores and multi-armed bandit. 
Based on this, the authors propose Algorithms 1 and 2 to solve this online selection of mixture efficiently, with performance guarantee given in Theorem 1 and 2, respectively. (Although I have some concerns on the settings and theoretical results, see below).
These methods can be used for widely used kernel inception distance (KID) and Renyi kernel entropy (RKE), and are tested on realistic image and text data in Section 6.

### Strengths
* The paper consider online selection of generative mixture models, which, to the best of knowledge, is a novel problem of interest.
* By making interesting connection to kernel-based scores and multi-armed bandit, the authors propose efficient methods to solve the above problem, with some theoretical guarantee. 
* Experiments on realistic data are provided, showing the practical applicability of the proposed approaches.

### Weaknesses
 * It would be great to discuss the limitation of the proposed approach, see below for my detailed comments/questions.
* some settings and theoretical results need clarification, see below for my detailed comments/questions.

* The problem appears novel, so I believe it makes sense to better motivative it. For example, in which context are we interested in picking a model to generate a sample at each round, why it is of interest to use "the fewest possible sample queries"? How the proposed method performs in an offline setting, with respect to performance and/or scalability? The motivation for online selection is not entirely clear; a more concrete scenario would be beneficial. For instance, are the generative models being updated over time, or is the goal to adapt to a changing data distribution? The practical implications of minimizing sample queries should also be better explained. Is this primarily for computational efficiency, or are there other constraints, such as limited access to the generative models?
* When summarizing the contribution of this paper, could the authors also provide (forward) pointers to the precise results? For example, "proposing an online learning framework in Section ??". I personally believe that this may facilitate the interested readers to quickly grasp the main contribution of the paper.
* Is the working assumption of linearly mixed model somewhat restrictive? Is there something else in the literature, or even such linear combination is (the first time) proposed by the authors in this paper? In fact, on the top row of Figure 3, there is a linearly mixtured "dog" that appears a bit bizarre: is this due to some limitation of this linear mixture? The use of a linear mixture of generative models, while simplifying the problem, may not fully capture the potential of combining diverse models. It would be useful to discuss the limitations of this approach, particularly in scenarios where the underlying data distributions are complex or multimodal. Are there alternative approaches to combining generative models that could be considered, and what are the trade-offs?
* I personally find Theorem 1 a bit surprising: To me, kernel matrix "estimation" problem plus some online selection problem, and solving the former problem in general requires a lot of samples to have a tight spectral norm control on the estimated kernel matrix. I believe that the authors avoid this issue by assuming/focusing on the case of bounded. Could the authors comment more on this? For example, does this bounded kernel/loss function setting limit the practical interest of the proposed methods? Also, could the authors comment on the observed sample size $n_i$ for the proposed OGD method to make sense? We do not see this in Theorem 2 and this has an impact on the computational complexity I believe? The theoretical results rely on the assumption of bounded kernel/loss functions, which may not hold in all practical scenarios. The implications of this assumption on the applicability of the proposed methods should be discussed in more detail. Specifically, how sensitive are the performance guarantees to violations of this assumption? Furthermore, the sample size $n_i$ for the OGD method is not explicitly addressed in Theorem 2, and its impact on computational complexity and convergence should be clarified.
* a tiny side remark: Figure 3 appears in the main text but commented in the appendix.

### Questions
Below are a few questions and/or comments.

1. The problem appears novel, so I believe it makes sense to better motivative it. For example, in which context are we interested in picking a model to generate a sample at each round, why it is of interest to use "the fewest possible sample queries"? How the proposed method performs in an offline setting, with respect to performance and/or scalability?
2. When summarizing the contribution of this paper, could the authors also provide (forward) pointers to the precise results? For example, "proposing an online learning framework in Section ??". I personally believe that this may facilitate the interested readers to quickly grasp the main contribution of the paper.
3. Is the working assumption of linearly mixed model somewhat restrictive? Is there something else in the literature, or even such linear combination is (the first time) proposed by the authors in this paper? In fact, on the top row of Figure 3, there is a linearly mixtured "dog" that appears a bit bizarre: is this due to some limitation of this linear mixture? 
4. I personally find Theorem 1 a bit surprising: To me, kernel matrix "estimation" problem plus some online selection problem, and solving the former problem in general requires a lot of samples to have a tight spectral norm control on the estimated kernel matrix. I believe that the authors avoid this issue by assuming/focusing on the case of bounded. Could the authors comment more on this? For example, does this bounded kernel/loss function setting limit the practical interest of the proposed methods? Also, could the authors comment on the observed sample size $n_i$ for the proposed OGD method to make sense? We do not see this in Theorem 2 and this has an impact on the computational complexity I believe?
5. a tiny side remark: Figure 3 appears in the main text but commented in the appendix.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main goal of this work is to maximize the diversity of generated samples by selecting not a single but a mixture of generative models. Formulating first a population loss of quadratic form that can translate into evaluation scores including kernel inception distance (KID) and Renyi kernel entropy (RKE), this article proposes two online algorithms based on continuum-armed bandit and gradient descent, to find the optimal mixture through minimizing an upper confidence bound of the quadratic population loss.  Experiments show that the proposed algorithms are efficient at approaching the optimal mixture.

### Strengths
* This paper is well written and easy to follow.

* The theoretical framework underlying the proposed algorithms is well grounded.

* Extensive experiments were carried out to demonstrate the performance of the proposed algorithms.

### Weaknesses
 * According to the literature review of this article, there seems to be little interest in finding a good mixture of different generative models. Indeed, if the goal is to approach the target distribution, it makes more sense to select the single best generative model than to use a mixture of different generative models, which are usually trained in an independent manner, therefore unlikely to complement each other. This is especially true when considering that the generative models are optimized independently, making it improbable that they will each specialize in different modes of a multimodal target distribution. In such cases, a mixture could easily degrade the overall quality of the generated samples.

* It is true that when the objective is to find the single best generative model, the online approach can help prevent sampling from suboptimal models. However, as using a mixture of generative models requires sampling from all member models, the online approach seems to be less useful in this setting. The online approach might be beneficial if the optimal mixture is sparse, but this is not the main focus of the paper. Furthermore, the paper does not provide a clear justification for why an online approach is necessary when the goal is to find an optimal mixture, as opposed to a single best model.

### Questions
* Can the authors find some other works that also aim to find good mixtures of generative models, and compare their method to these works?

* Can the authors provide the quality scores Density (Naeem et al., 2020). and Precision (Kynkaanniemi et al., 2019) in the experiments that they conducted?

* Small question regarding Lines 257&259: is $\hat{L}(\mathbf{a};\mathbf{x}^{(t)})-(\mathbf{\epsilon}^{(t)})^{\rm T}\mathbf{a})$ a lower or upper bound of $L(\mathbf{a})$?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper study online selection for generative models, in order to generate diverse samples. The authors formulated the problem as a mixture multi armed bandit problem and developed two algorithms for that: Mixture-UCB-CAB and Mixture-UCB-OGD. The authors developed theoretical guarantees for the Mixture-UCB-CAB algorithm. The authors conduct many experiments to show the efficacy of their developed methods.

### Strengths
It's interesting to see the authors formulated the generative model selection problem as an online selection problem. The authors also developed two algorithms for this new setting and provide theoretical guarantees for one of them. Experimental results demonstrate the efficacy of the proposed algorithms.

### Weaknesses
1. Since this is a new problem, can authors provide more motivations for online selection of generative models, e.g., how important is the ability to generate diverse samples? And how important is to save samples in the selection process.
2. The authors provide a convergence guarantee for Mixture-UCB-CAB in Thm 2. For comparison, what is the rate of convergence for the offline approach that randomly generate $T$ samples and then optimize over $\alpha$?
3. Does Thm 1 holds for all $\alpha$? Also, the guarantee in Thm 2 doesn't suffer the curse of dimensionality even if the algorithm is selection $\alpha \in R^m$; can authors explain why does that happen?
4. Compared to standard bandit problem where one gets an intermediate regret term at each round, it seems that the studied problems gets $O(t)$ (averaged) terms (the first Eq in Section 5), and all these terms are related to the previous selections $x_1, \cdots, x_{t-1}$. Can authors elaborate how do they deal with these terms in the analysis? What are some technical contributions?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3
