# Overcoming Data Inequality across Domains with Semi-Supervised Domain Generalization

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
While there have been considerable advancements in machine learning driven by extensive datasets, a significant disparity still persists in the availability of data across various sources and populations. This inequality across domains poses challenges in modeling for those with limited data, which can lead to profound practical and ethical concerns. In this paper, we address a representative case of data inequality problem across domains termed Semi-Supervised Domain Generalization (SSDG), in which only one domain is labeled while the rest are unlabeled. We propose a novel algorithm, ProUD, which can effectively learn domain-invariant features via domain-aware prototypes along with progressive generalization via uncertainty-adaptive mixing of labeled and unlabeled domains. Our experiments on three different benchmark datasets demonstrate the effectiveness of ProUD, outperforming all baseline models including single domain generalization and semi-supervised learning. Source code will be released upon acceptance of the paper.

  \keywords{Data inequality \and Domain generalization \and Semi-supervised learning \and Semi-supervised domain generalization}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a new algorithm (ProUD) for the problem of semi-supervised domain generalization. In this problem setting, 
we have K different domains, and we have access to labeled data for 1 domain and unlabeled data for the remaining K-1 domains.
The goal is to solve a learning problem with respect to all domains, by leveraging information from both the labeled data and the unlabeled data. This is an important problem, as labeled data may be unavailable for some source domains (a possible case of data inequality).

The paper proposes a new algorithm to solve this task. The algorithm combines different ideas, some are new, and some are an adaptation from previous work, to provide an accurate solution to this problem. Most of the important techniques involve pseudo-labeling to provide labels to the unlabeled data, and a method called Domain mix that tries to control and manage the contribution for very uncertain pseudo-labeling (very important in the first steps of the algorithm, where the pseudo-labels are not going to be precise).

The authors run extensive different experiments on real datasets, comparing their method to a wide range of baselines in the literature. They find that their methods perform on average better than all the baselines. They also run ablation studies to understand and assess the impact of the most important components of their architecture.

### Strengths
The paper addresses a very important problem: studying situations when we have limited access to labeled data is of paramount importance in practice.

From my perspective, the algorithm has two strengths. (1) it combines different techniques in order to provide a good solution to this problem, and it verifies that each of those individual components plays an important role in the ablation study, (2) it provides extensive analysis and comparison with the state-of-the-art to verify the superiority of their method.

Apart from a few details (see Weaknesses and comments below), I think the presentation of the paper is good.

### Weaknesses
It is not clear to me why your architecture only learns a single model, and what is the motivation behind it. Although there may be domain-invariant features that we can learn from multiple sources, different features may provide different information depending on the domain. 
As an example assume that there are two features f_A and f_B,  domain A may get a very good classification from a feature f_A (and not f_B), and domain B may get a very good classification from a feature f_B (and not f_A). In this case, it would make more sense to build different models that can exploit different features across the different domains. In your algorithm, this means that we keep the feature extractor g equal, but we build a function h for each different domain (similar strategies are also applied in ZSL).

In the data inequality model, some data sources may have a different number of examples. In particular, it could be that we have access to comparatively fewer data points for a given unlabeled domain. It looks to me that your model gives the same weight to each sample from each domain. In this case, if an unlabeled domain t is unrepresented (we have less data  N_t from it), then your model would still suffer from a data inequality issue, as the loss would be less influenced by the fewer samples on this unlabeled domain.


On the experiments:
- Is it the accuracy with respect to a held-out dataset? Or is the model evaluated on the same unlabeled data that is also used during training?
- Why is the accuracy averaged over the last 5 train epochs rather than only on the last epoch?
- I cannot find an explanation on how the hyper-parameters are chosen for your algorithms (is there a validation step?), and how the hyper-parameters are chosen for the baseline algorithms. I think this is important when evaluating methods on a new dataset (without overfitting due to the choice of the hyper-parameters).
- I believe that the standard deviation for the average accuracy is not reported. In particular, you obtain an average accuracy over 3 runs (with 3 different seeds), but it is not clear what is the variance of this value, which is important for comparison with other methods. (The reported STD is across the domain combinations rather than on the 3 seeded runs).

### Questions
(1) See the question above on the experiments, in particular for the standard deviation, hyper-parameters, and the choice of how the accuracy is reported.

(2) See the points above on the proposed model/architecture. Why do you learn a single model for each domain, and how do you handle the case when an unlabeled domain is under-represented (it has fewer samples than other unlabeled domains)?

------------



A couple of suggestions:
- "dist is a function to measure the cosine distance" -> "dist is the cosine distance". 
- It would be useful for the reader to get some intuitions behind some equations (in simple words), such as (1) and (3).
- I would add a very synthetic explanation of what a "prototype" is for clarity.
- I would briefly clarify that the shift that you are considering is only on the distribution of the features (unless I am missing something), but the classification problem is the same across all tasks.
- There are other settings that are "similar" to this that would maybe be worth discussing in the introduction / related work as further motivation. One setting is Zero-shot Learning (ZSL), where we do not have access to unlabeled data for the other domains (and the classification may change, and one is provided with a description of the classes). Another setting is (programmatic) weak supervision, where the goal is to design simple rules to label an unlabeled domain, and pseudo-labeling and noise-aware losses are also used (e.g., see [A]).

[A]: Ratner, Alexander, et al. "Snorkel: Rapid training data creation with weak supervision." Proceedings of the VLDB Endowment. International Conference on Very Large Data Bases. Vol. 11. No. 3. NIH Public Access, 2017.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a practically important problem called Semi-Supervised Domain Generalization (SSDG), where the multiple source domains contain both labeled samples and unlabelled samples. Its goal is to generalize the model trained on the source domains to an unseen target domain. To address this issue, the authors propose a novel algorithm called ProUD, which leverages domain-aware prototypes and uncertainty-adaptive mixing strategies.

### Strengths
1. **[The problem of this paper is critical in practice.]** In the previous studies under domain generalization, they always assume that labels of multiple source domains are available. However, it is sometimes infeasible to obtain such perfect source domains, which gives rise to the importance of SSDG.
2. **[This paper is well written and easy to follow.]** Background, motivation, details about the proposed method,  and experiments are well introduced.

### Weaknesses
1. **[The proposed method is lack of novelty.]** Essentially, the proposed method is still a combination of DA +DG. The step for assigning pseudo labels for unlabelled source domains can be regarded as DA, while the step for learning domain-invariant representations via a contrastive loss can be regarded as DG. Tools used in each step, such as pseudo-labeling and contrastive loss, are also widely used in methods for DA and DG. The combination of these techniques, while potentially effective, does not present a fundamentally new approach to the problem.
2. **[Motivation of this proposed method is unclear.]** It is unclear why the authors propose this specific combination of techniques. The paper does not adequately explain the research gap for current studies on SSDG that this particular method aims to fill. What specific limitations of existing approaches does this method address, and why is the chosen combination of DA and DG techniques the most suitable solution?
3. **[The proposed method is not explored deeply.]** Firstly, this paper does not provide a theoretical analysis to certify the effectiveness of the proposed method. Furthermore, it is unclear how the accuracy of pseudo-labels affects the final performance. In detail, in Equation (6), you mix labeled and unlabeled samples with the same class, whose performance may heavily rely on the quality of the pseudo labels. The paper lacks a thorough investigation into the sensitivity of the method to the quality of these pseudo-labels. Additionally, the t-SNE Visualization does not clearly demonstrate the specific contribution of Equation (8); it is not clear if the representation is primarily driven by this equation or other aspects of the method.

### Questions
1. How do you choose the value of the threshold $\lambda^*$?
2. Can you provide insights to answer the questions in Weakness 2 and Weakness 3?

### Soundness
2 fair

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
The paper proposes a new problem setting across domains termed Semi-Supervised Domain Generalization (SSDG), in which only one domain is labeled while the rest are unlabeled. The paper proposed a semi-supervised learning method called ProUD, by leveraging domain-aware prototypes, uncertainty adaptive mixing strategies, and pseudo labels. The authors conduct experiments on three datasets (PACS, Digits-DG, Office-Home) to demonstrate the effectiveness of ProUD.

### Strengths
- The paper proposes an interesting setting Semi-Supervised Domain Generalization (SSDG), in which only one domain is labeled while the rest are unlabeled. In the introduction, the paper lists some data inequality scenarios where SSDG may be used (Table 1). 
- It is a good try to introduce semi-supervised learning to the domain generalization community, e.g., how to construct pseudo labels.

### Weaknesses
 - The major concern, from my perspective, is the experiments section. (1) The paper misses many important benchmark datasets, such as VLCS, TerraInc, and DomainNet. See detail in DomainBed [1]. In particular, DomainBed is an important benchmark. (2) The paper fails to compare lots of state-of-the-art methods. The latest works compared in the paper are published in 2021. There are lots of good works in 2022 and 2023 that should be included, such as [2,3,4] and many more. Specifically, the paper should include comparisons to methods that utilize pre-trained models and more recent domain generalization techniques. (3) The results in Table 2, Table 3, and Table 4 cannot even show that ProUD outperforms EID by a large margin. The performance gains are marginal, and it is not clear if the proposed method ProUD is significantly better than existing methods. The lack of substantial improvement makes the practical utility of the method questionable.
- Some minor weaknesses. (1) The proposed methods need domain labels for domain-aware prototypes. This will restrict the methods when applied to the application. It would be good to consider whether there is a way to generalize the method to be domain label-free. The reliance on domain labels limits the applicability of the method in scenarios where such labels are not readily available. (2) The methods are simple and trivial. In my understanding, PML loss (Equation 8) is pretty similar to SupCon [5]. The core idea of using prototypes and contrastive loss is not novel. (3) It would be good if the paper could introduce some theoretical analysis to give more insights or intuition about the ProUD. The lack of theoretical justification makes it difficult to understand the underlying mechanisms of the proposed method.

### Questions
See the weakness above.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses a representative case of data inequality problem across domains termed Semi-Supervised Domain Generalization (SSDG), in which only one domain is labeled while the rest are unlabeled. It proposes a novel algorithm, ProUD, designed for progressive generalization across domains by leveraging domain-aware prototypes and uncertaintyadaptive mixing strategies.

### Strengths
1. The direction of the research in the paper is meaningful and has the potential to generate positive impact.

2. The description of the algorithm in the paper is clear, making it easy to read and reproduce.

3. The description of experimental settings in the appendix is detailed.

### Weaknesses
1. The paper is not well-written, as the algorithm lacks both theoretical support and adequate explanation, making it difficult to understand the authors' rationale behind the algorithm design.
2. The experiment, as it stands currently, is not sufficiently refined for the following reasons: 1). The datasets used in the experiment are all simple and small-scale; 2). On some datasets, the performance improvement compared to EID is relatively small, and the choice of random seed is not general enough; 3). There is only one partition for each dataset, and the proportions are not uniform (9:1 and 8:2). The author did not provide an explanation for the choice of different partitions.

### Questions
1. The algorithm uses prototypes obtained from soft labels when acquiring pseudo-labels (Equation 1), and prototypes obtained from hard labels are used in subsequent calculations of uncertainty and loss functions (Equation 3). What is the reason for these choices, and what is the difference in effectiveness between the two types of prototypes?

2. How was Equation 7 derived, and what is the rationale behind choosing it?

3. What is the improvement brought about by data augmentation, and how would the results compare if all algorithms used the same number of data augmentations in the comparison?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
