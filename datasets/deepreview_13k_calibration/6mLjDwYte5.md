# Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Sparse Mixture-of-Experts (MoE) is a neural architecture design that can be utilized to add learnable parameters to Large Language Models (LLMs) without increasing inference cost. Instruction tuning is a technique for training LLMs to follow instructions. We advocate combining these two approaches, as we find that MoE models benefit more from instruction tuning than dense models. In particular, we conduct empirical studies across three experimental setups: (i) Direct finetuning on individual downstream tasks devoid of instruction tuning; (ii) Instruction tuning followed by in-context few-shot or zero-shot generalization on downstream tasks; and (iii) Instruction tuning supplemented by further finetuning on individual downstream tasks. In the first scenario, MoE models overall underperform dense models of identical computational capacity. This narrative, however, dramatically changes with the introduction of instruction tuning (second and third scenario), used independently or in conjunction with task-specific finetuning.
    Our most powerful model, \shortname{}$_\textsc{32b}$, surpasses the performance of \flanpalm$_\textsc{62b}$ on four benchmark tasks, while using only a third of the FLOPs. The advancements embodied by \shortname{} inspire a reevaluation of the design principles of large-scale, high-performance language models in the framework of task-agnostic learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the role of instruction tuning in whether mixture of experts models outperform dense models on language tasks. It turns out that instruction tuned mixture of experts performs better than dense models.

### Strengths
1) This paper does not really present a new algorithm or theory, but is mostly a large collection of experiments showing under what conditions the proposed Flan-MoE model performs well. With that being said, the number and thoroughness of the experiments and ablations is quite impressive. 
2) The authors acknowledge limitations of MoE models and show to mitigate them, i.e. using auxiliary loss to mitigate overfitting

### Weaknesses
I don't see any

### Questions
1) The authors state that MoE can be used to add learnable parameters to LLMs "without increasing inference cost." I think this is somewhat confusing. Increased memory usage is as much of a "cost" as increased FLOPs or latency.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
MoE model is a sparse model architecture that can be utilized to scale the number of parameters without significantly increasing the computation cost. In this research, the authors conducted experiments comparing dense models with MoE models using instruction tuning. The results indicate that combining sparse MoE models and instruction tuning leads to a significant enhancement in model performance, surpassing dense models across various datasets.

### Strengths
+ This paper tries to apply the instruction tuning to the context of MoE models for downstream tasks. The experimental results demonstrate the combination has great potential to improve the performance of large language models.

+ The authors conducted comprehensive experiments on various sparse and dense models to support their claim, and in most cases, the combination of instruction tuning and MoE models shows strong performance over other models.

### Weaknesses
 + Lack of clear motivation. The motivation behind the combination of MoE with instruction tuning requires further discussion. While it is acknowledged that instruction tuning and MoE models can outperform dense models or fine-tuning MoE, it will be beneficial to provide some insights into why these approaches were chosen.

+ The presentation of this paper needs some improvements. Some grammar things could be improved in the explanation and discussion of the key component of this paper. 

+ The impact of the combination design (instruction tuning and MoE) on training and inference time should have more discussion.

### Questions
1. I understand the performance of instruction tuning on MoE models, but can you please provide any analysis or insight about the reasons behind such good performance? Does it help improve the routing strategy, expert specialization, or something else?

2. The author claims that these advancements are attained without necessitating an increase in computational resources or even reducing the resource requirements. I am confused about how it can reduce resource requirements in the training and inference time. Can you discuss more about the details of the process?

### Soundness
3 good

### Presentation
2 fair

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
This paper studies the benefits of applying instruction-tuning to MoE models. It presents a series of instruction fine-tuned MoE models, called FLAN-MoE, which have shown superior performance over task-specific fine-tuned MoE and their corresponding dense models.

### Strengths
1. This is a timely study, given that fine-tuning large-scale pre-trained MoE models for specific tasks is quite challenging.

2. The paper provides relatively comprehensive studies of MoE models with instruction tuning, demonstrating that MoE models can benefit from additional instruction tuning.

3. The findings are well-documented, including a range of MoEs sizes and discussions on limitations and failure cases.

### Weaknesses
1. While several MoE models have been tested, the conclusion about the necessity of the instruction-tuning stage is not convincingly demonstrated. For instance, the addition of this instruction-tuning stage can introduce additional training and tuning costs, e.g., in comparison to using just task-specific fine-tuning. Is it possible that the performance improvement can also come from this extra training cost?

2. Related to the training cost, the paper claims that its improvement does not stem from increased computational resources or memory requirements. However, this is a bit confusing because instruction fine-tuning in this paper clearly uses a large set of datasets for training, which incurs training costs. Yet no direct report in terms of the training cost is included in the paper. To be more convincing, a detailed report on how the proposed method affects training costs should be included.

3. Some parts of the paper lack clarity. See detailed questions below.

### Questions
1. Some statements made by the paper are rather confusing. For example, the paper states, “However, we show that conventional, task-specific finetuning MoE models lead to suboptimal performance, often even worse than finetuning dense models with the same computational cost. One of the possible reasons is the discrepancy between general pretraining and task-specific finetuning.” However, regardless of whether the model architecture is dense or sparse, isn't there always a discrepancy between pre-training and task-specific fine-tuning?

2. When the paper says the FLAN-MoE “does not come from increased computation resources or memory requirements,” what does it mean? Does it refer to computation and memory requirements during training/inference compared to compute-equivalent dense/MoE models? 

3. The paper says, “We demonstrate that in the absence of instruction tuning, MoE models fall short in performance when compared to dense models on downstream tasks.” However, this seems to be contradictory to some prior studies. For example, https://arxiv.org/pdf/2112.10684.pdf shows that MoE models can outperform compute-equivalent dense models on supervised fine-tuning tasks. 

4. What is the difference between FLAN-MoE and MoE in Section 4.1? 

5. The paper does not seem to describe the model architecture of FLAN-MoE adequately. The only one mentioned is ST-MoE-32B. It would be interesting to see how different pre-trained MoE models would affect the conclusion.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrates that large scale instruction tuning (using the FLAN data) of sparse mixture-of-expert (MoE) models before finetuning on downstream task data is crucial for MoE to beat comparable dense models (in terms of inference FLOPs).  Merely performing finetuning with MoE on downstream task data without instruction tuning beforehand underperforms directly finetuning a dense model (without instruction tuning), whereas the addition of the instruction tuning stage to the MoE model causes it to outperform dense models with the equivalent training procedure.  At all model scales, MoE outperforms comparable dense models whenever the instruction tuning phase is present, whereas MoE without instruction tuning underperforms.

### Strengths
**Originality:** As far as I know the significance of instruction tuning for MoE has not been studied extensively in the manner this paper puts forward.

**Quality:** The claims are plausible and well supported.  The authors conducted comprehensive ablations across model scales, # of tasks for instruction tuning, MoE expert selection method, # of experts, etc.  There is no reason to question the central claim.

**Contribution:** The contribution is to provide high quality data towards the effect of large scale instruction tuning for MoE models in relation to dense models with a comparable number of inference FLOPs.  They demonstrate that instruction tuning may be essential for MoE models to succeed.

### Weaknesses
 **Weaknesses:**  There is little insight into what is causing the failure of direct finetuning of MoE models on downstream task data.  It could be that MoE models have higher capacity to overfit, however it is unclear if instruction tuning is preventing this or if there are other factors at hand.  More conceptual insight would be nice, however I do not view this as a major weakness. The paper does not explore the potential interaction between the routing strategy and the observed performance differences. It's possible that certain routing mechanisms are more susceptible to overfitting or require specific pre-training conditions to function effectively. The study also lacks an analysis of the impact of different instruction tuning datasets on the final performance of the MoE models. It is not clear if the observed benefits are specific to the FLAN dataset or if they generalize to other instruction tuning datasets. Furthermore, the paper does not provide a detailed analysis of the computational cost associated with instruction tuning, which is a crucial factor for practical applications of MoE models. It would be beneficial to understand the trade-offs between the computational overhead of instruction tuning and the resulting performance gains.

### Questions
*Figure 1 (right):* It is not a big deal but can be a bit confusing that the T5 and Flan-T5 green and blue bars are included for each number of experts as these are independent of the number of experts.

*Table 1:* Why not show Switch and GS performance at the 32G FLOP scale?

*Figure 3:* Why not label the orange and blue curves by model size, at least in the caption?

*Figure 6:* How is expert utilization measured?

**Notes and minor details:**

*Typo:* “benefits from a richer repertoire of specialized sub-networks .” (extra space before period)
 
*Figure 2 caption:* “Average zero performance” --> “Average zero shot performance?”
 
Add period after paragraph title “Routing Strategy” for formatting consistency.
 

Typo near bottom of page 8: “issue may stes” → “issue may stem”

*Appendix p. 15*
“We present a detailed learning efficiency experiment in Figure 7 across number of steps. It shows that MoE starts to outperform Dense counterparts right after 25k steps with instruction tuning.”

* There are no labels for the lines in the figure, thus it’s impossible to tell which is the dense model and which is the MoE model

*Appendix p. 15:* “We leave the study of scaling decoder-only FLAN-MOE as future works.” --> “We leave the study of scaling decoder-only FLAN-MOE to future work.”

*Appendix p. 15:*

“but yield worse performance” → “but yields worse performance”

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
