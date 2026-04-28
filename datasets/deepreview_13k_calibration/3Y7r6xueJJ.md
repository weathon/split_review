# Continual Learning in the Presence of Spurious Correlations: Analyses and a Simple Baseline

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Most continual learning (CL) algorithms have focused on tackling the stability-plasticity dilemma, that is, the challenge of preventing the forgetting of past tasks while learning new ones. However, we argue that they have overlooked the impact of knowledge transfer when the training dataset of a certain task is biased — namely, when the dataset contains some spurious correlations that can overly influence the prediction rule of a model. In that case, how would the dataset bias of a certain task affect the prediction rules of a CL model for future or past tasks? In this work, we carefully design systematic experiments using three benchmark datasets to answer the question from our empirical findings. Specifically, we first show through two-task CL experiments that standard CL methods, which are oblivious of the dataset bias, can transfer bias from one task to another, both forward and backward. Moreover, we find out this transfer is exacerbated depending on whether the CL methods focus on stability or plasticity. We then present that the bias is also transferred and even accumulates in longer task sequences. Finally, we offer a standardized experimental setup and a simple, yet strong plug-in baseline method, dubbed as group-class Balanced Greedy Sampling (BGS), which are utilized for the development of more advanced bias-aware CL methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While most continual learning (CL) algorithms focus on the stability-plasticity trade-off, this study highlights the overlooked impact of dataset bias on knowledge transfer. Through systematic experiments on three benchmark datasets, the authors show that standard CL methods can transfer bias between tasks, affecting both forward and backward learning. The degree of bias transfer depends on whether the CL methods prioritize stability or plasticity. Bias transfer accumulates in longer task sequences. To address this issue, the authors propose a standardized experimental setup and introduce a simple yet effective baseline method called Group-class Balanced Greedy Sampling (BGS).

### Strengths
- Amongst the works that look at CL and distribution shift, this is the one of the first papers to do an empirical study on impact of dataset bias on three different forms of CL: task-IL, domain-IL and class-IL. 

- The authors do a good job of structuring their findings, by first illustrating results in the two task case, followed by multiple tasks in a sequence. The metrics for bias (BMR/DCA) and CL (normalized $\mathcal{F}-\mathcal{I}$) are clearly defined.  In general the presentation is good, and the writing is clear. Particularly, experiment results in section 4 and 5 are well presented with easy to read plots. 

- The CKA analysis done on representations of penultimate layer (Sec 4.3) strengthens the empirical results observed.

- The proposed baseline (group-class balanced greedy sampling) is fairly simple and combines ideas from GDumb and DFR. The algorithm presents significantly lower BMR over CL baselines in class-IL and task-IL settings.

### Weaknesses
 - The datasets used for the experiments are small scale and synthetic. Using more natural datasets that evolve over time, e.g. FMoW dataset from Wilds benchmark, or other datasets from the Time-Wilds paper would be helpful. In some of these datasets, there is also group/attribute information that can be used to measure bias. The current synthetic datasets, while useful for initial exploration, lack the complexity and real-world nuances that could reveal further limitations of the proposed method and baselines. For instance, the controlled nature of the bias in the synthetic datasets might not fully capture the more intricate and subtle forms of bias present in real-world data, potentially leading to an overestimation of the method's effectiveness.

- The paper can be improved with experiments that use a pretrained model (like CLIP), and then perform continual learning. It would be interesting to see if the same trends hold, or are they amplified/diminished with respect to forward/backward bias transfer. The current experiments are limited to models trained from scratch, which might not reflect the behavior of models that have already learned rich representations from large-scale datasets. Exploring the impact of pre-trained models would provide a more comprehensive understanding of how bias transfer interacts with existing knowledge and could reveal whether pre-training mitigates or exacerbates the observed effects.

- I understand that theoretical analysis is not always feasible or even helpful, but for spurious correlations there exist simple settings/distributions in the SC literature where the SC induces failure even in linear models (see [1, 2, 3]). Extending these frameworks to the CL setting and then proving formal claims about forward/backward bias transfer can make the claims in this paper much stronger and build understanding to develop mitigation strategies and algorithms. The lack of theoretical grounding makes it difficult to generalize the empirical findings and understand the fundamental mechanisms driving bias transfer in continual learning. A theoretical framework could provide insights into the conditions under which bias transfer is more likely to occur and how it can be effectively mitigated.

### Questions
- In figure 4, for row 1, why does the CKA value drop even when bias of T1 is zero?
- In figure 5, how does PackNet do on backward transfer?
- Also can authors comment on why ER does much better than LWF and PackNet in general?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper revolves around the subject of bias transfer in continual learning (CL). The authors develop an experimental framework examining six CL strategies using two evaluation metrics across three scenarios, ensuring comprehensive analysis of the problem. Their findings show that CL techniques, unaware of dataset bias, can transfer such biases in both forward and backward directions. In response to this issue, they suggest a novel approach, Group-class Balanced Greedy Sampling (BGS), aimed at mitigating bias transfer. This paper is unique in the sense that it deliberates on the existence of spurious correlations in the CL context and calls for attention to develop bias-aware mechanisms in CL.

### Strengths
- The authors address an often-overlooked issue of bias transfer in CL and provide a well-motivated argument adopting a fresh perspective in the field of CL.
- Their analysis is fairly extensive, using six CL methods with three different scenarios.
- The novelty of the proposed BGS method to mitigate bias without requiring any additional hyperparameter tuning enhances the paper's contribution.
- The empirical evidence that reveals the existence of bias transfer in CL and its subsequent impact on the tasks makes a significant contribution to the field.

### Weaknesses
 - While the empirical investigation of CL provides valuable insights, the novelty of findings and proposed BGS approach could be more explicitly addressed considering existing similar work in the domain.
- The main limitation of this paper lies in the diversity of the samples used. The authors base their experiments on three benchmark datasets, all of which are synthetically created for Continual Learning (CL). From personal observation, it has been noted that such models can perform adequately even with a few hundred examples, contradicting the need for the 2000 or 4000 examples that BGS involves. By conducting tests in more authentic scenarios (such as shift in time/linguistic diversity, or the nature of the sequence to sequence task (like going from question answering to machine translation to paraphrasing etc)), a stronger foundation of support for the results could be established.
- The paper's dual research goals are compressed into a limited amount of space, making comprehensive comprehension challenging. More in-depth discussion or a more detailed layout for the proposed BGS method would be beneficial.
- The underlying mechanisms contributing to bias transfer are not entirely delved into in the paper.

### Questions
- The role and impact of the stability-plasticity trade-off on bias transfer in CL could be more thoroughly explored.
- The experimental design lacks uniformity across all three CL scenarios and should strive for a standardized evaluation protocol.
- It would be insightful to know if the bias transfer problem exists in substantial real-world applications (as shared in weaknesses) and what limitations exist in the experimental setup.
- Why did you use LWF + Group DRO as a comparison in Tables 1(a) and 1(b) when ER is better performing than LWF? Could you share your rationale here?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the impact of spurious correlations in the CL setting. Through comprehensive experiments, it confirms the existence of bias transfer in CL, affecting model predictions in both forward and backward directions. Then, they establish standard experimental settings, bias-aware CL scenarios, and evaluation protocols and introduce a practical baseline method called "Group-class Balanced Greedy Sampling (BGS)" for advancing bias-aware CL techniques.

### Strengths
1.    This article has a clear motivation. I also agree that investigating spurious correlations is a highly worthwhile topic in the CL setting.
2.    The related work section of the article provides an excellent summary of the relationship between CL methods and spurious correlations.
3.    The paper's approach to investigating bias awareness from three distinct angles, i.e., model bias, the relative focus on the Stability-Plasticity trade-off, and bias transfer, is comprehensive and convincing.

### Weaknesses
1.    The readability of the paper could be improved. The abstract and introduction should be revised to provide a more engaging and clearer overview of the research. 
2.    The paper introduces the Bias-flipped Mis-classification Rate (BMR) and the Difference of Classwise Accuracy (DCA) as metrics, but it lacks a detailed comparison of these metrics on the proposed benchmark datasets. It would be valuable to provide an in-depth analysis of how these metrics perform under different scenarios.
3.    Table 1 should include further comparisons of CL baselines. A more comprehensive analysis of the performance of other CL baselines on the proposed benchmark datasets would provide a stronger basis for evaluating the proposed method.
4.    While this paper introduces the BALANCED GREEDY SAMPLING (BGS) method, its novelty appears to be limited. The paper could benefit from a more thorough exploration of innovative techniques in the bias-aware CL domain.
5.    The experimental analysis and the overall structure of the paper should be enhanced. This paper reads more like a forward-looking exploration of bias-aware scenarios rather than a comprehensive research work. It would be beneficial to present a more detailed and rigorous experimental analysis.

### Questions
1.    Can the paper provide a more detailed comparison between its proposed methods BGS and the GDumb and DFR CL methods to highlight their differences in addressing bias-aware CL scenarios?
2.    Does Table 1 in the paper, which indicates a significant improvement in bias-aware CL scenarios when using the BGS method, imply that BGS may be less robust in scenarios with larger datasets, as increasing data has a limited impact on model improvement in all three scenarios?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the impacts of spurious correlations in the continual learning setting.

First, the paper defines the experimental setups and evaluation metrics for investigating the issue of bias transfer.

Then, the paper conducts experiments, arguing that bias exists and existing CL approaches cannot handle the bias. This is done first for the case of two tasks, and then generalized to longer task sequences.

Next, the paper proposes a method to address the bias. The method consists of retraining the last linear layer using a balanced set of data samples.

### Strengths
Omitted.

### Weaknesses
In my humble opinion, the paper has several weaknesses:

- The paper has limited novelty. In particular, the proposed problem is a basic combination of continual learning and bias of machine learning models. The proposed approach is a direct variant of Kirichenko et al. (2023). An analogy would be that the paper derives a corollary from a theorem in prior work. 
- In the experimental setting, the paper changes the input data by skewing them towards gray-scale images (or colored) images. This creates several issues:
  - This setup makes the experiments artificial, human-made, and synthetic. The practical relevance is to be evidenced.
  - The notation of bias is subjective. The way the paper changes the input data is just to make a shift of distribution or create subclasses from existing classes, rather than creating any bias. Retraining the last layer using a balanced set of data would of course improve in this case as it reduces the performance gap between (sub)classes and improves DCA. Therefore, the story the paper tries to convey is in my eyes a word game that is not convincing.

### Questions
I have no specific questions

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
