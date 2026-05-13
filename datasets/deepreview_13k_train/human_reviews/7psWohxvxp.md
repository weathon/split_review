# Exploring a Principled Framework for Deep Subspace Clustering

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Subspace clustering is a classical unsupervised learning task, built on a basic assumption that high-dimensional data can be approximated by a union of subspaces (UoS). Nevertheless, the real-world data are often deviating from the UoS assumption. To address this challenge, state-of-the-art deep subspace clustering algorithms attempt to jointly learn UoS representations and self-expressive coefficients. However, the general framework of the existing algorithms suffers from feature collapse and lacks a theoretical guarantee to learn desired UoS representation. In this paper, we present a Principled fRamewOrk for Deep Subspace Clustering (PRO-DSC), which is designed to learn structured representations and self-expressive coefficients in a unified manner. Specifically, in PRO-DSC, we incorporate an effective regularization on the learned representations into the self-expressive model, and prove that the regularized self-expressive model is able to prevent feature space collapse and the learned optimal representations under certain condition lie on a union of orthogonal subspaces. Moreover, we provide a scalable and efficient approach to implement our PRO-DSC and conduct extensive experiments to verify our theoretical findings and demonstrate the superior performance of our proposed deep subspace clustering approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper studied deep subspace clustering. Existing deep subspace clustering methods suffer from feature collapse, where learned representations collapse into subspaces with dimensions much lower than the ambient space. The paper proposes to add a loss term that alleviates this issue, which is backed up with some theoretical study and experiments on real-world dataset.

### Strengths
1. Experiments on synthetic and real-world datasets are comprehensive, and the reviewer appreciate that.  Synthetic experiments: what happens when you add an additional subspace? Case 1: the subspace is 0-dimensional (points centered around a centroid) Case 2: you add a another curve as you have around the great circle, but now put it vertically. The subspaces will be intersecting. I am not expecting the methods to outperform anything, this is just for understanding the method better.

### Weaknesses
1. The reviewer is concerned with the novelty of the paper. The main motivation of the paper is the observation from Haeffele el al. 2021 that if one learns a representation and apply a subspace clustering type of loss on the representations, then the representations tend to collapse. Therefore, the paper proposes to incorporate an additional term (equation 3) into the loss to prevent collapse. This theme of combining subspace clustering loss and (equation 3) has been explored before: In Ding et al 2023, they used a combination of (equation 3) and the subspace clustering loss in Ma et al 2007. One could go ahead and try many different subspace clustering loss functions, but the contribution seems incremental apriori. If one reads the introduction of that paper, it appears that the motivation was rather similar to this one, but no discussion was given in the current paper.
2. The reviewer is also concerned with the theoretical contributions.
    1. Lemma 1 and its proof is not a contribution, as the paper clearly states they are from Haeffele et al. 2021.
    2. It is difficult to connect Theorem 1 with the main objective (equation 5). In particular, it is unclear at the optimality of (equation 5), whether (and why) the optimal Lagrangian multiplier nu satisfies the conditions in Theorem 1. The condition on the Lagrangian multiplier $\nu$ seems somewhat detached from the actual optimization problem, and it's not clear how one would verify this condition in practice, or how it relates to the convergence of the algorithm.
    3. Theorem 3: I do not quite understand the statement.
        1. First, apriori there might be multiple solutions to PRO-DSC. When you say ‘the’ optimal solution, what do you mean? Do you mean you have a sufficient condition, such that there exists ‘one’ optimal solution such that some ideal properties hold on this solution? Or do you mean ‘all’ optimal solutions
        2. Second, I am a bit confused on Z, C vs Z^*, C^*. Gamma is defined to permute (or ‘align’) columns of Z, but on line 238 they are used to permute Z^*. Is Gamma a function of Z or Z^*? In the sufficient condition <(I-C)(I-C)^T, G-G^*>, should it be C^* instead? Or even a step back: how is C defined in Theorem 3?
        3. It is unclear what how to interpret sufficient condition <(I-C)(I-C)^T, G-G^*>, e.g., how does it connect with Z^* lying in a union of subspaces or C^* being correctly connecting points only from the same subspace. It might strengthen the result a bit if there is a simple case (e.g., the subspaces are independent or orthogonal, points being uniformly spread within each subspace) where such conditions hold.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a Principled fRamewOrk for Deep Subspace Clustering (PRO-DSC), which is designed to learn structured representations and self-expressive coefficients in a unified manner. First, PRO-DSC incorporates an effective regularization into self-expressive model to prevent the catastrophic representation collapse with theoretical justification. Second, PRO-DSC demonstrated that it is able to learn structured representations that form a desirable UoS structure, and also developed an efficient implementation based on reparameterization and differential programming. Comprehensive experiments verify the superiority of the proposed model.

### Strengths
1.The paper is well-written and technically sound.  
2.The experiments are comprehensive.

### Weaknesses
1.What are the limitations and failed cases of the proposed method? Some discussion needed.
2.There may be insufficient implementation details provided, hindering reproducibility of the study and making it challenging for other researchers to replicate the results. Such as, the results for PRO-DSC are averaged over three trials (with±std), what about other methods? Their results are the best or mean? As I know, some methods like k-means and SC are sensitive to the initialization, their results are recorded by the best or mean in some runs with different initializations? A fair experimental setting is necessary.  
3.The subspace description coefficients and manifold parts provided in the article are based on existing research results and lack sufficient innovation.

### Questions
1.What are the limitations and failed cases of the proposed method? Some discussion needed.
There may be insufficient implementation details provided, hindering reproducibility of the study and making it challenging for other researchers to replicate the results. Such as, the results for PRO-DSC are averaged over three trials (with±std), what about other methods? Their results are the best or mean? As I know, some methods like k-means and SC are sensitive to the initialization, their results are recorded by the best or mean in some runs with different initializations? A fair experimental setting is necessary.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the deep subspace clustering problem. The general framework of the existing algorithms suffers from feature collapse and lacks a theoretical guarantee to learn the desired UoS representation. This paper presents a principled framework for deep subspace clustering (PRO-DSC), which is designed to learn structured representations and self-expressive coefficients in a unified manner. The motivation is clear, and the experimental performance of the proposed model is also good.

### Strengths
1.	The motivation is clear.
2.	The proposed method has strong theoretical support. 
3.	The problem that needs to be solved is important, and the proposed method is reasonable.

### Weaknesses
In Eq. (4), it needs to be clarified why the logdet term is adopted. Is it only used to solve the representation collapse problem? Are there any other methods that can solve this collapse problem? More importantly, what are the underlying physical meanings of this term?

In Table 2, although the proposed methods seem to have the best performance. Some really SOTA deep clustering methods are not compared, like 
[1] Learning Representation for Clustering Via Prototype Scattering and Positive Sampling, 2023 TPAMI.
[2] Towards Calibrated Deep Clustering Network, 2024 Arxiv.

Ablation studies should be performed to check the effectiveness of each component of the proposed method.

### Questions
See the weakness.

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
Deep subspace clustering methods usually encounter the challenge of feature collapse and lack theoretical guarantees for learning representations that form a union of subspaces (UoS) structure. To address these issues, this paper presents a principled framework for deep subspace clustering (PRO-DSC). The framework incorporates an effective regularization on the learned representations to prevent feature space collapse. Furthermore, theoretical analysis demonstrates that PRO-DSC can yield representations of a UoS structure under certain conditions. Experimental results show the effectiveness of the proposed method.

### Strengths
1. This work presents an effective method to prevent feature collapse and addresses the lack of theoretical guidance for learning representations with a UoS structure. An efficient implementation is presented to alleviate the computational burden of self-expressive learning.
2. The work is sound from a technical perspective. It combines solid theoretical proof and empirical evidence. 
3. Experiments on synthetic and real-world data are conducted to evaluate the effectiveness. Meanwhile, both quantitative and qualitative results are provided for comparison.
4. Overall, this paper is well-written and thoughtfully structured.

### Weaknesses
1. As one of the main challenges this work focuses on is learning UoS representations, I suggest the authors emphasize the significance of this challenge by clarifying the associated consequences and providing empirical observations to support it. Specifically, the paper should elaborate on why learning representations that do not conform to a UoS structure is detrimental to subspace clustering, and provide examples of how this manifests in practice, such as increased within-cluster variance or poor separation between clusters. 
2. Since the proposed PRO-DSC is designed as a framework, I expect further discussion and experimentation on its scalability and extensibility. The paper should include a more detailed analysis of the computational complexity of the proposed method, especially with respect to the size of the input data and the number of subspaces. Furthermore, it should explore how the framework can be adapted to different types of data and different network architectures. 
3. I have several questions and concerns regarding the experimental parts:
    1) Why is only the proposed method run multiple times for evaluation, while other methods seem to be tested only once? Additionally, why is the method run only three times? Repeating the evaluation 10 times is commonly preferred for more reliable results. It is important to understand if the proposed method's performance is consistent across different runs, and if the reported results are not due to random initialization. The lack of consistent evaluation across all methods makes it difficult to draw definitive conclusions.
    2) Why are only image datasets used for evaluation? I suggest testing the performance on a wider range of datasets, such as the Reuters and UCI HAR datasets. The paper should demonstrate the generalizability of the proposed method to different types of data, including text and time-series data, which have different characteristics and may pose different challenges for subspace clustering.
    3) Most of the comparison methods used in experiments are outdated. Please consider adding two more state-of-the-art subspace clustering methods for comparison, such as AGCSC [1] and SAGSC [2]. The paper should compare the proposed method with the most recent and competitive methods in the field to demonstrate its superiority.
    4) Why do the comparison methods differ between experiments in Tables 1 and 2? The paper should provide a clear explanation for why different sets of comparison methods are used in different experiments, and justify the choices made.
    5) In the synthetic data experiments, why is DSCNet used as the representative SEDSC method rather than the more competitive, recent SENET? The paper should justify the choice of baseline method and explain why a more recent and competitive method was not used.

### Questions
I have several questions and concerns regarding the experimental parts:
1) Why is only the proposed method run multiple times for evaluation, while other methods seem to be tested only once? Additionally, why is the method run only three times? Repeating the evaluation 10 times is commonly preferred for more reliable results.
2) Why are only image datasets used for evaluation? I suggest testing the performance on a wider range of datasets, such as the Reuters and UCI HAR datasets.
3) Most of the comparison methods used in experiments are outdated. Please consider adding two more state-of-the-art subspace clustering methods for comparison, such as AGCSC [1] and SAGSC [2].
4) Why do the comparison methods differ between experiments in Tables 1 and 2?
5) In the synthetic data experiments, why is DSCNet used as the representative SEDSC method rather than the more competitive, recent SENET?

[1] Wei, Lai, et al. "Adaptive graph convolutional subspace clustering." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

[2] Wang, Libin, et al. "Attention reweighted sparse subspace clustering." Pattern Recognition, 139 (2023): 109438.

### Soundness
3

### Presentation
3

### Contribution
3
