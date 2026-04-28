# Stochastic Vision Transformers with Wasserstein Distance-Aware Attention

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Self-supervised learning is one of the most promising approaches to acquiring knowledge from limited labeled data. Despite the substantial advancements made in recent years, self-supervised models have posed a challenge to practitioners, as they do not readily provide insight into the model's confidence and uncertainty. Tackling this issue is no simple feat, primarily due to the complexity involved in implementing techniques that can make use of the latent representations learned during pre-training without relying on explicit labels.
Motivated by this, we introduce a new stochastic vision transformer that integrates uncertainty and distance awareness into self-supervised learning (SSL) pipelines. Instead of the conventional deterministic vector embedding, our novel stochastic vision transformer encodes image patches into elliptical Gaussian distributional embeddings. Notably, the attention matrices of these stochastic representational embeddings are computed using Wasserstein distance-based attention, effectively capitalizing on the distributional nature of these embeddings. Additionally, we propose a regularization term based on Wasserstein distance for both pre-training and fine-tuning processes, thereby incorporating distance awareness into latent representations.
We perform extensive experiments across different tasks such as in-distribution generalization, out-of-distribution detection, dataset corruption, semi-supervised settings, and transfer learning to other datasets and tasks. Our proposed method achieves superior accuracy and calibration, surpassing the self-supervised baseline in a wide range of experiments on a variety of datasets. Our code is in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper focuses on self-supervised learning by considering the model’s confidence and uncertainty, it proposes a new stochastic vision transformer that integrates uncertainty and distance awareness into a pipeline by a Wasserstein distance-based attention. The method is evaluated using various tasks.

### Strengths
The motivation is clear and convincing, the method seems nice and the methods are evaluated on various tasks.

### Weaknesses
n/a

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a stochastic vision transformer that integrates uncertainty and distance awareness into self-supervised learning (SSL) pipelines. The core idea is to encode image patches into elliptical Gaussian distributional embeddings, and use Bures-Wasserstein to calculate the (dis)similarity between encoded patches and define a Wasserstein-based attention. The authors demonstrate the performance of their proposed method across different tasks such as in-distribution generalization, out-of-distribution detection, dataset corruption, semi-supervised settings, and transfer learning to other datasets and tasks.

### Strengths
* The idea of stochastic token embedding and Wasserstein-based attention mechanism is interesting, and timely. 

* The paper is written clearly and it is straightforward to follow.

### Weaknesses
 * My main criticism of this paper is the experimental results.

  * First, the experimental results are limited as the experiments only focus on small-scale datasets, namely CIFAR-10 and CIFAR-100. The results will be much more conclusive if the author reports results on larger-scale datasets, e.g., imagenet, or at least datasets with larger images (e.g., mini-imagenet, or tiny-imagenet). The lack of experiments on larger datasets makes it difficult to assess the scalability and practical applicability of the proposed method. The current results do not sufficiently demonstrate the method's effectiveness in more complex scenarios.
  * Secondly, in most of the experiments, the results either match the baselines or are only marginally superior. Additionally, the method is more than twice as costly in terms of time when compared to the baseline (~4hrs vs ~9hrs). Compounding the issue, I couldn't determine if the results are reported as an average over K runs. The marginal improvements, coupled with the significant increase in computational cost, raise concerns about the practical utility of the method. Without a clear advantage in performance, the increased computational burden is difficult to justify. Furthermore, the absence of information regarding the number of runs makes it hard to assess the statistical significance of the reported results.

  Respectfully, the results section of this paper is significantly below the standards of an average ICLR paper, and I encourage the authors to work on improving this section to increase their impact.  

* There are several typos throughout the formulations that make me question the rigor of the paper.
   * Equation (4) is $W_2^2(z_1,z_2)$ and not $W_2(z_1,z_2)$. The same goes for all equations that use $W_2$.
   * Equation (10), did you mean to write: $\mathcal{L}_p-\lambda log(\sigma(-W_2^2 (z_{out},f_z(y^+))))$?

### Questions
*  In Equation (10), why do you consider only positive samples? Wouldn't a generalized version using both negative and positive samples (similar to the classic works like SimCLR) be better? In other words, something like the following:

  $$-\lambda_1 log(\sigma(-W_2^2 (z_{out},f_z(y^+))))+\lambda_2 log(\sigma(-W_2^2 (z_{out},f_z(y^-)))) $$

  where if you set $\lambda_2=0$ you will recover the only positive sample case.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper adopts a stochastic transformer architecture that uses distributional embedding and Wasserstein distance-based attention mechanism for self-supervised learning pipelines. The contrastive regularization terms are added to the training objective.

### Strengths
- The paper is well-written and concise.
- The paper investigates an important research question, which can potentially interest many researchers.

### Weaknesses
 - More explanations needed for baselines. e.g. For the baseline MC-Dropout, it only mentions the dropout regularization applied during pre-training, and the ratio is set to 0.3; but for MC dropout, the dropout is applied at both training and test time, and there is no detail for the testing. 
- The performance is not convincing enough. The improvement is not significant, and according to the ablation study, it also seems very sensitive to the hyperparameters. 
- It's not proper for the paper to say 'We propose a stochastic transformer architecture with distributional embedding......', since the distributional embeddings and Wasserstein distance-based attention mechanism are the same as Fan et al., 2022.

### Questions
Why set dropout ratio as 0.3 for the MC-Dropout baseline? Isn't it slightly higher than the common options?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
