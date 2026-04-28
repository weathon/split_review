# Sparse MoE as a New Treatment: Addressing Forgetting, Fitting, Learning Issues in Multi-Modal Multi-Task Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Sparse Mixture-of-Experts (SMoE) is a promising paradigm that can be easily tailored for multi-task learning. Its conditional computing nature allows us to organically allocate relevant parts of a model for performant and efficient predictions. However, several under-explored pain points persist, especially when considering scenarios with both multiple modalities and tasks: 1 $\textit{{Modality Forgetting Issue.}}$ Diverse modalities may prefer conflicting optimization directions, resulting in ineffective learning or knowledge forgetting; 2 $\textit{{Modality Fitting Issue.}}$ Current SMoE pipelines select a fixed number of experts for all modalities, which can end up over-fitting to simpler modalities or under-fitting complex modalities; 3 $\textit{{Heterogeneous Learning Pace.}}$ The varied modality attributes, task resources ($\textit{i.e.,}$ the number of input samples), and task objectives usually lead to distinct optimization difficulties and convergence. Given these issues, there is a clear need for a systematic approach to harmonizing multi-model and multi-task objectives when using SMoE. We aim to address these pain points, and propose a new $\underline{S}$parse $\underline{M}$oE framework for $\underline{M}$ulti-$\underline{M}$odal $\underline{M}$ulti-task learning, $\textit{a.k.a.}$, $\texttt{SM$^4$}$, which ($1$) disentangles model spaces for different modalities to mitigate their optimization conflicts; 
($2$) automatically determines the modality-specific model size ($\textit{i.e.}$, the number of experts) to improve fitting; and ($3$) synchronizes the learning paces of disparate modalities and tasks based on training dynamics in SMoE like the entropy of routing decisions. Comprehensive experiments validate the effectiveness of $\texttt{SM$^4$}$, which outperforms previous state-of-the-art across $3$ task groups and $11$ different modalities with a clear performance margin ($\textit{e.g.}$, $\ge 1.37\%$) and a substantial computation reduction ($46.49\% \sim 98.62\%$). Code is included in the supplement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach that incorporates routing in the training of general-purpose models for multimodal and multi-task learning to address heterogeneity across modalities and tasks. The overall idea is relatively straightforward. A subset of datasets from MultiBench were used in their evaluation.

### Strengths
+ The performance of the proposed method on included datasets seems impressive based on numbers reported in the paper.
+ Solid study on the behavior of the proposed method. Plots in Figure 2 are good illustrations, right to the points.

### Weaknesses
 - The description of proposed method is very difficult to follow. I have no idea how the method works from just reading the paper. For example, it does not clearly state what are exactly the experts and where they come from. I cannot get much from Figure 1. It seems that experts are grouped. But I was not able to find a discussion why/how they are grouped. 

- The motivation of ALP is not clear to me. Does unstable routing policy just mean changes in the policy across iterations? Such change does not necessarily link to the routing distribution entropy.  

- Comparing Table 2 with Table 3 of Liang, et al., 2022, there is large difference in the performance of HighMMT on same datasets. A discussion of where the discrepancy coming from is needed.

### Questions
- What are the criteria/considerations used in selecting datasets/tasks for evaluation? There are many other tasks and modalities in MultiBench. How the proposed method works for those? 

In addition, refer to the list of weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel framework, SM^4, based on sparse Mixture-of-Exports and designed for multi-modal multi-task learning. Notably, the algorithms address three 3 critical issues in the field: modality forgetting, overfitting to simple modalities, and unaligned learning paces in multi-tasks. The main idea is to disentangle information and adjust model capacities by enforcing sparsity and employing attention models. In the experiments, SM^4 shows the best performance, greatly reduced computational cost, and the ability of mitigating the 3 pain points.

### Strengths
1. This work is well-motivated and addresses important issues in multi-modal and multi-task learning via reasonable algorithms. The evaluations and analyses are also detailed, confirming the impact of this work.
2. The conducted analyses not only prove the effectiveness of the framework SM^4 but also establish solid evaluation protocol for follow-up works.
3. The writing is impressive. The authors do a great job on presenting the complicated settings and methods, making the article both informative and easy to follow. Also, the experiment settings are thoroughly reported.

### Weaknesses
My concerns are mostly about the experiments.
1. The authors employ MultiBench for evaluation, while the metrics of robustness and training cost are ignored. This raises 2 concerns:
* a. Without checking robustness, it is unclear if the trained model is robust to missing or noisy modalities, which shall be an important criterion in multimodal learning.
* b. The trade-off between training cost and model performance of SM^4 is unclear. In particular, deciding number of experts for each modality seems to be time-consuming. I suppose checking the trade-off and comparing SM^4 with simple methods such as early/late can help measuring the practical value of this work more precisely.
2. The reported performance of MultiBench models in Table 2 may be overly simplified. As the complexities of the MultiBench models greatly vary, simply reporting the aggregated performance (e.g., the range) makes it difficult to position SM^4 in this regard. Also, the dependencies between efficiency and performance are ignored, similar to the issue in weakness 1.b. A candidate method could be the 2D visualization adopted by MultiBench and is used for studying trade-offs.
3. Minor typo: YR-FUNNY in Table 1.

### Questions
1. Following the weaknesses, I am wondering if the authors consider reporting the training cost, robustness, and the trade-offs?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes SM$^4$ for the Multi-Modal Multitask Learning problem. Particularly, SM$^4$ focuses on the challenges of i) modality forgetting; ii) modality fitting; and iii) heterogeneous learning pace. SM$^4$ introduces several advances to the vanilla Sparse Mixture of Experts (SMoE) techniques, including employing SMoE in both the dense and multi-head self attention layers, implementing the adaptive expert allocation and adaptive learning pace mechanisms. SM$^4$ show promising results compared to SOTA baselines on the MultiBench benchmarks. Authors also conducted various ablation studies to explore different characteristics of SM$^4$.

### Strengths
- Multi-modal Multi-task learning is an important emerging problem in both research and industry. 
- The proposed method  achieved encouraging performance against SOTA baselines.
- The experiments are quite comprehensive where the complexities and ablation studies are included. There are some exceptions that I will mention in the Weakness section.
- Implementation is available.

### Weaknesses
 * My most critical concern of this work is the proposed method is quite ad-hoc and heuristic, especially in the AEA and ALP modules.
    + **AEA**: First, the strategy introduces an additional hyper-parameter: $n$ - number of iterations to monitor the loss. It is unclear how sensitive the results will be with respect to $n$, and there are no guideline to select $n$. Looking at Algorithm 2, it seems like AEA employs a pre-training phase to decide $k_j$ for each modality independently. However, this does not take into account the interaction of multitask learning when the modalities are learned together. There are also no constraints to enforce that all experts are utilized, i.e. $\sum_j k_j = N$. Lastly, in Figure 2-3, it is unclear why larger training-validation loss gap can lead to better generalization. When this gap is large, the model is either underfitted or overfitted rather than achieved better generalization.  The precise mechanism of how the training loss and validation loss are measured and compared to determine the expert allocation is not clearly specified. The algorithm's reliance on a single epoch's loss for this decision seems insufficient, as a single epoch may not provide a stable or reliable estimate of the model's performance, especially in the early stages of training. The lack of a clear stopping criterion for the expert allocation process is also concerning.
    + **ALP**: it is unclear what "learning pace" mean in this context, i.e. is it the learning rate or some components that directly influence the training trajectory? The description of how the routing entropy influences the learning pace is also vague, and it's unclear whether this is a per-modality learning rate adjustment or a more complex mechanism.  The algorithm's adaptive learning pace lacks a clear theoretical justification. The connection between routing entropy and learning rate adjustment is not well-established, and the method seems to rely on heuristics without a strong foundation.

* Table 1 and 2 are quite unclear, what is the "setting" here referred to, is it the dataset size, or the model size? For example, in Table 2, SM$^4$ Medium - AV-MNIST has 1.23M params while the same method in the large setting has 0.76M params. The results of HighMMT seems to be quite different from the original, which requires further investigations.

* Other suggestions: Figure 2 is not nice, please consider using subfigure, e.g. 2a, 2b, etc. instead of the current presentation.

### Questions
- Clarifications regarding the AEA, ALP modules, and the settings in Table 1 & 2.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work tackles multi-modal multi-task learning with sparse mixture-of-experts. The authors identify three problems, namely modality forgetting, modality fitting and heterogeneous learning pace. The proposed method combines solutions for the three problems and shows competitive empirical performance against the SoTA.

### Strengths
This work identifies three important questions in multi-modal multi-task learning, namely forgetting, fitting and learning. Furthermore, the work proposes a framework that can solve the three problems simultaneously.

### Weaknesses
1. The novelty of the work is limited. To solve the modality forgetting problem, the authors deploy load and importance balancing loss. To solve the other two problems, the authors use standard hyperparameter tuning methods. It is unclear which part is truly originated from the authors.

2. The connection of the three problems is not organic. Although those three questions indeed exist in multi-modal multi-task learning, the authors do not point out how those problems are related. It seems that the authors tackle those three problems separately and in turn get a better result.


### Questions
I am confused about the results in 5. What does 32N mean? Intuitively, increasing N should lead to good performance, and 32N is indeed the largest in the table, so it is not surprising that it has the best result. What is the message to convey here?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
