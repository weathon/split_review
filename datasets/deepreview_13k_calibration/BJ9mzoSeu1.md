# Personalized Federated Learning via Variational Massage Passing

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Conventional federated learning (FL) aims to train a unified machine learning model that fits data distributed across various agents. However, statistical heterogeneity arising from diverse data resources renders the single global model trained by FL ineffective for all clients. Personalized federated learning (pFL) has been proposed to primarily address this challenge by tailoring individualized models to each client's specific dataset while integrating global information during feature aggregation. Achieving efficient pFL necessitates the accurate estimation of global feature information across all the training data. Nonetheless, balancing the personalization of individual models with the global consensus of feature information remains a significant challenge in existing approaches. 
In this paper, we propose pFedVMP, a novel pFL approach that employs variational message passing (VMP) to design feature aggregation protocols.  By leveraging the mean and covariance, pFedVMP yields more precise estimates of the distributions of model parameters and global feature centroids. Additionally, pFedVMP is effective in boosting training accuracy and preventing overfitting by regularizing local training with global feature centroids. Extensive experiments on heterogeneous data conditions demonstrate that pFedVMP surpasses state-of-the-art methods in both effectiveness and fairness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a Bayesian approach to dealing with personalized federated learning (pFL). In particular, a "shared" base model is learned to map inputs to representations and each client learns a local head model to turn those representations into prediction outputs. In their approach, distributions of parameters of the base and head models are learned. In addition, the distribution of the representations are considered via a GMM (mixing on true labels). Locally, updates for the base, head, and GMM are learned. For global aggregation the base and GMM models are updated. The paper consider the case where the relevant distribution of the base and head models are Gaussians. Their approach is tested across various vision datasets.

### Strengths
- The approach shows promising experimental results, showing better results than the baselines reported
- The overall approach make intuitive sense, combining ideas from pFL and Bayesian FL.

### Weaknesses
 - The primary weakness of the paper is in part of its presentation. This is particularly the case for Section 4 where conceptual optimization goals is mixed in with practical simplifications. Specifically, the transition between the abstract optimization problems (P1-3) and their concrete implementations is not clearly delineated, making it hard to follow the derivation.
 - In addition, there are no detailed derivation for some of the quantities used (in main text nor appendix). For example, the specific form of the local update equations, particularly how the Gaussian Mixture Model (GMM) parameters are updated, is not explicitly derived.



### Questions
Questions + Remarks:

1. $p({\theta}^{\\rm b}, \\{ \theta_n^{\\rm h} \\}, \\{ z_k \\}, S)$ is a distribution over parameters (+ representations) and samples $S$. But, as far as I can tell from the equations, the surrogate distribution $q$ being consider is only over parameters (+ representations). As such, it is unclear how the KL-divergences are being evaluated, eg, (P1) including the argmin.
Please provide clarity on this support issue of the distributions and how the KL-divergence is being evaluated.

2. From what I understand, when (P1) is referred in text, it only refers to the parameter updates and not the variational / KL-divergence aspect over the equation. This is rather unclear in Section 4.2.
Please clarify this (P1), perhaps by presenting the entire optimization in multiple line (labeling as (P1a) and (P1b) for instance).

3.  I think additional clarity in the text should also be added to distinguish section which are considering the update of parameters in (P1) (Section 4.3) vs updates on the distribution in (P2) (Section 4.2 & 4.3). This aspect is also mixed in Section 4.3.1. It may be worth splitting this subsubsection into two separate subsubsections, one for local updates on the parameters and one for local updates on the distributions.

4. Is (P2) and (P3) equivalent (when restricting optimization to local parameter etc)? Line 269-270 says that the optimization is converted. Does this imply equivalence?

5. The soundness of going from (P3) to (8) is a bit unclear. Could you please elaborate on the derivation (which I believe is just maximizing (7)) and why it is "low-cost implementation of SG-MCMC".

6. (P2) seems to be imprecise. In particular, the second term in the KL is not a normalized distribution? In particular, several "prior" distribution seem to be missing in (P2) and the accompanying text. Please clarify this.
It would also be useful for completeness to include a derivation of the specific factorization you are using; and its subsequent use in (P3).

---

Minor:
 - References were cut off from the main text.
 - The subscript of the max in (1) and (P1) is not very nice. Maybe having the subscript fully under the "max" would improve readability of these equations.
 - $\\mathcal{Z}_{k,n}$ seems to be incorrect on line 160 (should have $k$ instead of $y_k$)
 - I think \bigcup $\\bigcup$ is typically used over \cup $\\cup$ for indexed unions.
 - (1) and 2) on line 42 - 44 are not consistent
 - Line 240 in denominator, there is a missing bracket
 - (P1-3) should be on the RHS to be consistent with equation numbering (maybe via \tag)
 - Figure 3, missing space after "Upper:"

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a personalized federated learning algorithm based on Bayesian estimation. The core idea is that clients learn a global shared model while they train a personalized head.

### Strengths
Personalization in federated learning by splitting the model into two parts such that one part is learned globally while the head is learned locally is proved to be effective. The contribution and motivation of the paper is clear.

### Weaknesses
The novelty of the paper is not high in my opinion. The core idea has been proposed before in the literature. One of the first work that I know which employ the same idea for personalized federated learning is FedRep of Collins et al., (2021). However, Collins et al., (2021) solves the problem using optimization. It seems that this paper solves the problem using Bayesian. Furthermore, Bayesian federated learning has been studied extensively before. Although, the paper compares the proposed algorithm against set of baselines, I think the paper misses the comparison with FedRep which is closely related to the study of this paper. The paper does not clearly articulate the specific advantages of using a Bayesian approach over optimization-based methods for this particular problem of personalized federated learning with a split model architecture. It is not clear how the Bayesian treatment of the global feature centroids provides a significant advantage over simply using the mean of the feature centroids as a regularizer, especially given the computational overhead of Bayesian methods. The paper also lacks a detailed discussion on the sensitivity of the proposed method to the choice of prior distributions and hyper-parameters, which is a critical aspect of Bayesian methods.

### Questions
I am not expert at Bayesian learning and I cannot evaluate the novelty of this work in this aspect. Can you explain the key differences between your proposed algorithm prior Bayesian federated learning? My concern is that if we can apply prior Bayesian federated learning to solve the problem which has been already studied by convex optimization techniques.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
pFedVMP is a personalized federated learning approach that uses variational message passing to enhance feature aggregation, yielding more precise model parameter estimates and improving training accuracy and fairness under heterogeneous data conditions.

### Strengths
This paper provides a nice numerical study with SOTA baselines with interpretation, ablation study, and fairness analysis.

### Weaknesses
First of all, there is a typo in the title of this paper: "Massage Passing" should be "Message Passing"...

W1. The Bayesian benchmark models are not included in the comparison.

W2. The computational cost seems to be high, especially with high-dimensional features.

W3. The selection of hyperparameters needs justification.

W4. There is a lack of theoretical guarantees for the proposed method.

### Questions
Q1. The paper presents extensive comparisons with various methods in federated representation learning but fails to include benchmark models within the framework of Bayesian federated learning, for example, BNFed, pFedGP, pFedBayes, FedPA, FedEP, QLSD, and others. This weakens the argument for the superiority of the proposed method in the Bayesian context.

Q2. The pFedVMP algorithm involves numerous matrix inversions in each communication round (especially in Equation 12), which can lead to a significant computational burden, particularly with high-dimensional features. It is essential to evaluate the computational cost relative to other methods and propose reasonable solutions to mitigate these costs.

Q3. The algorithm contains several hyperparameters, such as those in Equations 8 and 10. A more in-depth study on the impact of these hyperparameters and a clear justification for their selection is necessary.

Q4. There is a lack of theoretical guarantees for the proposed method.

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
- This paper presents a personalizd federated learning methods, called pFedVMP, as a new solution to tailed personalized model for local clients. The core idea is to model both the centorids of parameters and features.

### Strengths
- The combination of modeling both feature space and parameter space seems to be good as shown in the reported results of the experiments.

### Weaknesses
 - The main ideas of pFedVMP, modeling parameters and feature centroids, are not new. A Bayesian perspective is either an well-explored areas in federated learning.
- Even tough this area is well-explored in recent years, most of the baselines in the experiments are not the newest, which make it hard to believe to be SOTA. Moreover, the most related works are not included as a baseline of Bayesian Federated Learning.
    1. Related and new baselines are recommended as followings: feature modeling [1,2] and parameter modeling [3,4].
    2. MOON [1] has similar claims about feature centroids modeling, and however is not discussed.
    3. PRIOR [4] emphasizes the importance of global prior information which is the parameter centroid, which has not been discussed yet.
    4. More comparison about works after year 2023 should be added beyond FedPAC (ICLR 2023) in order to be claimed as SOTA.
- Some words, e.g., leveraging second-order statistical information, are confusing in the federated learning. The ambiguous words in this comprehensive field can refer to second-order moments, covariance matrices, or second-order gradients, Hessian matrices.

### Questions
- What's the main difference between the propoed pFedVMP and the methods use GMM to model the feature centroids or parameter centeroids?
- The main claim, the global feature centroids is important, is already a common sense in the literature of federated learning, which is first systematically claimed and proven by MOON [1] as far as I know. What's more?
- If the difference is clearly explained, a positive rating is considered.

[1] Model-contrastive federated learning. CVPR 2021

### Soundness
3

### Presentation
2

### Contribution
2
