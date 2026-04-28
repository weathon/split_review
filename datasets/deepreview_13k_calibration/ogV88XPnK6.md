# Graph neural processes and their application to molecular functions

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Neural processes (NPs) are models for meta-learning which output uncertainty estimates. So far, most studies of NPs have focused on low-dimensional datasets of highly-correlated tasks. While these homogeneous datasets are useful for benchmarking, they may not be representative of realistic transfer-learning. In particular, applications in scientific research may prove especially challenging due to the potential novelty of meta-testing tasks. Drug discovery is one such research area that is characterized by sparse datasets of many functions on a shared molecular space. In this paper, we study the application of graph NPs to drug discovery with DOCKSTRING, a diverse dataset of docking scores. Graph NPs show competitive performance in few-shot learning tasks relative to supervised learning baselines common in chemoinformatics, as well as alternative techniques for transfer learning and meta-learning. In order to increase meta-generalization to divergent test functions, we propose fine-tuning strategies that adapt the parameters of NPs. We find that adaptation can substantially increase NPs' regression performance while maintaining good calibration of uncertainty estimates. Finally, we present a Bayesian optimization experiment which showcases the potential advantages of NPs over GPs in molecular applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study Graph NP's performance in few-shot learning tasks, and propose fine-tuning strategies to further improve GNP's regression performance while maintaining good calibration. They also present a Bayesian optimization case study to showcase GNP's potential advantages.

### Strengths
1. Writing: Well-organized, easy-to-follow paper.
2. Significance: Show that graph NPs are competitive in molecular few-shot learning tasks.

### Weaknesses
1. Applicability: Focuses on regression tasks only despite abundant data and baselines in classification. The choice of regression limits the scope of the study, especially given the availability of established classification benchmarks in molecular property prediction. The paper does not adequately justify why classification was not explored, which is a more common task in this domain.
2. Novelty: Fine-tuning NPs during meta-testing are not novel contributions. While the paper demonstrates the effectiveness of fine-tuning, the approach itself is not a significant methodological advancement. The fine-tuning strategy is relatively straightforward and does not introduce any new techniques or insights into the workings of Graph Neural Processes.

### Questions
1. Why didn't you extend Graph NPs into the classification setting, where the amount of data and baselines is abundant?
2. Could you explain the results presented in Figure F.1, where the $R^2$ did not decrease as the percentage of training points sampled increase?
3. Have you considered studying the impact of context/target set randomization on calibration of uncertainty estimates?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies meta-learning approaches for molecular tasks, and focuses on introducing neural process (NP) for this application. Apart from building different NP models (CNP,LNP) for molecules, taking fingerprints (FPs) or molecular graphs (MGs) as input features, this paper emphasizes the challenge of meta-generalization in molecular tasks. To close to real world molecular applications, it sets up experiments with an unusual meta-learning setting: the correlation between training and testing tasks are controlled at a low degree, and the size of context varies in a large range. To deal with, this paper proposes to combine gradient-based adaptation (MAML, fine-tuning) with NP model. The authors tailor DOCKSTRING dataset, and detail empirical results show that MG-CNPc(fine-tuned) has a performance advantage in most cases.

### Strengths
1.	This paper comprehensively study NP-based models on molecular tasks, including different NP variants, different molecular features, different additional adaptation strategies.

2.	It pointed out the challenge that tasks are highly diverse in real world molecular applications. And propose additional adaptation steps should be adopted based on NP models to increase the meta-generalizability.

3.	Data processing and empirical results are shown in detail. It looks convincing that the proposed method could show advantage with such setting.

### Weaknesses
1. Lack of novelty. As a representative amortized meta-learner, NP has been widely studied. This paper adopts the most conventional NP models on molecular tasks. “NP+gradient steps” is also a popular way to improve meta-learning performance by combining two adaptation strategies. (in similar fields, there is [1]). It seems little technical contribution in this paper.

2. The authors propose that existing datasets are highly homogeneous across tasks, while in reality the task diversity should be considered. However, there lacks evidence in this paper. No empirical results of existing popular datasets (e.g., fs-mol[2], moleculenet[3]), nor comparing them with real-world cases are provided.

3. Lack of benchmark datasets and baselines. Since the proposed is following a standard meta-learning setting, existing few-shot molecular property prediction methods [4,5,6], should be considered. Among them, [5] is also applicable for regression task, which should be compared on DOCKSTRING. And the proposed method should also be applicable for classification tasks, so it should be tested on [2][3], and compared with [4,5,6].

4. Poor organization of related works. The related works mix everything (i.e. datasets, methods) together, which are hard to read.

### Questions
Please refer to weaknesses.

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
Meta-learning is crucial in fields such as biology, where a variety of test functions exist and sparse data is typical. Additionally, uncertainty measures are typically of interest, to aid in deciding which of the predictions should undergo costly experimental validation. In this work, the authors benchmark deep neural process, a type of deep models that also model uncertainty, for few-shot learning. The authors show that even small modifications to the test functions can massively affect meta-generalization, and use two approaches to address this: fine-tuning and a single step of gradient descent on a MAML-trained neural process. They benchmark neural processes in DOCKSTRING, a dataset of docking scores of 260k ligands against 58 diverse proteins, using molecular fingerprints and graphs as input representations.

### Strengths
-	The work is nice and easy to follow
-	Elegant and simple experiment to show the disruption of meta-generalization with divergent test functions (Figure 1)
-	Provides useful take-aways in few-shot learning experiments

### Weaknesses
 - Restricted evaluation to DOCKSTRING

### Questions
Surprisingly, I don’t have any questions regarding the work itself. It was very clear, easy to follow, and thorough in the evaluation of deep NPs for few-shot learning in DOCKSTRING. I believe this is an important work in benchmarking deep NPs that would be of great use to the community.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach based on graph neural processes for meta learning for drug discovery. The authors suggest replacing the MLP encoder of vanilla latent/deterministic neural processes with a graph neural network in order to capture higher-order interactions between the input covariables which in this case are atomic and atom-atom bond features. In addition, they propose a fine-tuning approach to adapt parameters after meta-training and an adoption of model-agnostic meta learning for NPs.

### Strengths
- Phrasing the problem of drug discovery as a meta-learning problem and using graph neural networks as encoders for neural processes is in the reviewer's opinion both original and reasonable.
- The paper is well written and easy to follow, and the problems of meta-learning in drug discovery is well delineated.
- The approach of fine-tuning is intuitive and seems reasonable.

### Weaknesses
 - The main contribution of the paper is the usage of vanilla NPs with an encoder that is an adapted graph neural network of a previously introduced method [1] . In total, the contribution seems too incremental and too little.
- The description of the methodology itself (molecular graph attentive encoder) is not detailed enough and very superficial (in total 5 lines of the entire manuscript). Specifically, the exact architecture of the GNN, including the number of layers, the type of attention mechanism used (e.g., self-attention, graph attention), and the specific aggregation functions, are not provided. This lack of detail makes it difficult to reproduce the results and assess the novelty of the approach.
- The fine-tuning and MAML approaches for parameter adaption described in the paper are of little novelty. In addition, the theoretical benefit and motivation of the MAML tuning is not clear to the reviewer since NPs can generally already be considered as meta learnerns.? Empirically, the MAML tuning sometimes improves and sometimes worsens predictive performance (see, e.g., Table~1 FP-CNP with FP-CNP (MAML) or MG-LNP with MG-LNL (MAML)). The lack of a clear theoretical justification for why MAML should be beneficial, given the meta-learning nature of NPs, is a significant weakness.
- The experimental section seems very thin and more evaluations with missing competing methods should be made. See, e.g., [2] as a reference. The absence of comparisons against other state-of-the-art meta-learning methods for molecular property prediction makes it difficult to assess the true performance of the proposed approach. The experimental setup also lacks details on hyperparameter tuning and the specific datasets used.
- The reference section is incomplete and sometimes incorrect. For instance, the "Attention is all you need" paper is from 2017 and not from 2023 and misses the conference information.
- The authors fail to cite relevant literature on graph neural processes, e.g. [3].

### Questions
- Some clarifications of the math of the encoder structure or an illustrative figure would in the reviewer's opinion improve the quality of the manuscript. While background on NPs is explained in sufficient detail (both in the main manuscript as well as the appendix), the actual method is not described at all.
- The authors could evaluate the case where a NP has both a latent and deterministic encoder. See, e.g., [2]
- As far as I can tell, the authors do not compare themselves against recent methods such as in [1]. Is this true and if so is there any reason for that?
- LNPs are generally harder to train then CNPs. Is the poor performance of LNPs due to this fact or how can it be explained? Is it because the authors seemed to have trained only for a fixed number of iterations and not until converge (see Appendix C3.7)?

[1] https://arxiv.org/abs/2205.02708
[2] https://arxiv.org/abs/1901.05761

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
