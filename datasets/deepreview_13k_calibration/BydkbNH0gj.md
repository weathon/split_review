# LESS IS MORE: HIGH-VALUE DATA SELECTION FOR VISUAL INSTRUCTION TUNING

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Visual instruction tuning is the key to building large vision language mod-
els (LVLMs), which can greatly improve the task generalization and solving capa-
bilities by learning a mixture of instruction data from diverse visual tasks. Previ-
ous work mostly collects multiple existing visual instruction datasets via heuristic
ways for training (even more than a million instructions), which may introduce
data redundancy and enlarge the training cost. To investigate this issue, we con-
duct a series of empirical studies, which reveal a significant redundancy within the
visual instruction datasets, and show that greatly reducing the amount of instruc-
tions from several tasks even do not affect the performance. Based on the findings,
we propose a high-value data selection approach $\textbf{TIVE}$, to eliminate redundancy
within the visual instruction data and reduce the training cost. In TIVE, we first
estimate the instance influence score on its corresponding task, and the task dif-
ficulty score, based on the gradient-based influence functions. Then, we leverage
the two kinds of scores to determine the task proportion within the selected visual
instruction subset, and select high-value instances for each task, respectively. Ex-
periments on various LVLMs show that our approach using only about 15% data
can achieve comparable average performance to the full-data fine-tuned model
across eight benchmarks, even surpassing it on four of the benchmarks. Our code
and data will be publicly released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper concentrates on reducing the data redundancy of instruction-following MLLMs. The authors show that pruning a certain ratio of specific training data has a slight influence on the overall accuracy. Based on the observation, the authors present a data selection approach named TIVE. The data selection strategy is based on estimating task difficulty and instance influence. Then the gradient features are used for selection. The authors integrate the approach on several MLLM backbones including LLaVA-1.5, LLaVA-LLaMA3, Mini-Gemini, etc. Experiments on multimodal benchmarks show an increase compared with random selection.

### Strengths
1. The experiments are complete across various MLLM backbones, including Vicuna, Phi, and LLaMA3, and architectures, including LLaVA-1.5, SVIT-Mix, and Mini-Gemini. The authors also show comparisons with baselines / advanced MLLMs. 
2. The performance meets the full baselines with only 10% to 30% training data, which shows the effectiveness of TIVE.
3. The paper is well written and the formulation periods are clear.

### Weaknesses
1. The main weakness lies in the design of the approach, especially regarding the computation costs. In my recognition, the inference operation based on the gradients and other selection operations are costly, even meets the original training cost. This makes the contribution of the pruning method weak. Specifically, the gradient computation for the entire dataset, even with dimensionality reduction, is computationally intensive. The subsequent calculations of task difficulty and instance influence, which involve multiple passes through the data, further exacerbate this issue. The paper lacks a detailed analysis of the time complexity of each step, making it difficult to assess the practical feasibility of the proposed method.
2. The selection based on gradients is a posterior probability, which means choosing the hard samples as prior knowledge. This may be unfair for the comparisons against baselines. The method inherently biases the selection towards samples that are difficult for the initial warm-up model, potentially leading to a skewed representation of the overall data distribution. This raises questions about the generalizability of the model trained on the selected data, as it might overfit to the specific challenges highlighted by the gradient-based selection.
3. The overall performance in Table 1 against backbone models is weak, only shows significant improvement on the SciQA benchmark, and gains accuracy drop or fair on other benchmarks (may be due to experiment uncertainty). This may mean the selection approach is sub-optimal. The lack of consistent improvements across all benchmarks suggests that the proposed selection method might not be universally effective. The observed performance variations across different datasets raise concerns about the robustness of the approach and its applicability to diverse multimodal tasks.

### Questions
See the weakness part. The authors are encouraged to answer such questions.
1. Regarding weakness 1, the authors are encouraged to provide the actual time cost for TIVE and fair comparisons with full training for LLaVA-1.5.
2. The accuracy drop for TIVE is significant compared with the baseline. 
3. The authors could explain the design of gradient inference in detail and show the relations with the original training data and the backbone.
Therefore, I recommend rejecting this manuscript in its current version. I would like to increase my score if the authors could address the issues above or provide more results against approaches with similar targets.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work studied the redundancy problem in the visual instruction tuning dataset for LVLMs. It proposed a high-value data selection approach TIVE, to eliminate redundancy within the visual instruction data and reduce the training cost. HIVE can effectively reduce the training data size of different VLM instruction tuning datasets across different models without compromising the overall performance.

### Strengths
The observation of the dataset redundancy problem aligns with the community's observations.
The proposed TIVE method sounds reasonable.
The authors conduct extensive experiments with detailed analysis to demonstrate the effectiveness of the method and its components.

### Weaknesses
1. Though the experiments are comprehensive, there are several points to further discuss or clarify in the method. See questions.
2. The authors need to provide a further discussion on the overall cost of the method: as TIVE needs the reference model trained with warmup data, the selection of TIVE is generally model-specific. TIVE needs to compute the LoRA gradient over all samples in the pool, then this cost is close to training on all of the data with LoRA. Tuning the hyper-parameters of TIVE would give another dimension of complexity if there are no default hyper-parameters. From this perspective, this method may fail to reduce the overall training costs. If so, it needs to target improving the final performance (without insisting on 15% of data) and discuss more about how to achieve this (what proportion of data is the best?). If not, the corresponding additional cost should be discussed.

### Questions
1. In algorithm 1, the task influence is calculated in a nested for loop, with a overall complexity $O(|D_i|^2)$ for each task. A question is, could the author first use one pass to aggregate the average of the normalized gradients and then use another pass to calculate the score? This will reduce the complexity to linear. Will this cause numerical instability or it doesn't? Originally, was the gradients stored or re-computed?
2. Are the influence scores' gradient of a sample computed over all tokens in it and do average, or only on outputs part? 
3. In the line 301, $\lambda$ is introduced as "We use a hyperparameter $\lambda$ to control the temperature of the weight distribution". However, how actually it is used is presented in Line 871 in appendix. The ablation of $\lambda$ appears before readers know how actually it is used. The ordering of this part needs further consideration.

### Soundness
3

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
The paper investigates redundancy within visual instruction datasets used for fine-tuning large vision-language models (LVLMs). It presents an empirical analysis which reveals that reducing the instruction data does not significantly impact model performance, suggesting the potential for data reduction. To address this, the authors propose TIVE, a novel method that selects high-value data based on task difficulty and instance influence using gradient-based techniques. Experiments demonstrate that TIVE can achieve comparable or even superior results to full-data models while using only 15% of the dataset. The proposed method provides a more efficient approach to visual instruction tuning by minimizing training costs and redundancy.

### Strengths
1.  The paper introduces a well-justified and innovative method, TIVE, that addresses data redundancy in visual instruction datasets for LVLMs. 
2. The motivation for addressing redundancy is well explained, and the proposed solution is logically developed based on detailed empirical findings.
3. The authors provide thorough empirical evidence demonstrating the existence of redundancy within current visual instruction datasets, supporting the motivation for their approach.

### Weaknesses
1. The paper does not sufficiently discuss the potential limitations of the TIVE approach, such as its scalability to even larger datasets or its applicability to different types of multimodal tasks.
2. I have some concerns regarding the data selection approach. In the earlier stages of machine learning, data and feature selection were widely popular. However, recent trends show that using larger models with bigger datasets tends to yield remarkable generalization capabilities. I hope the authors can address this concern in their rebuttal.

### Questions
Please refer to weakness part

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the issue of data redundancy in visual instruction tuning for building large vision language models (LVLMs). Through empirical studies, it reveals significant redundancy within visual instruction datasets and proposes a high-value data selection approach named TIVE. TIVE estimates instance influence scores and task difficulty scores based on gradient-based influence functions to select a representative subset of data, reducing training costs while achieving comparable performance to full-data fine-tuned models on multiple benchmarks.

### Strengths
1. The paper addresses a crucial problem in the field of LVLMs data redundancy in visual instruction tuning. This is an important issue as it can lead to increased training costs and potential overfitting.
2. The authors conduct a series of experiments to demonstrate the existence of data redundancy and the effectiveness of their proposed method. The analysis includes pruning the amount of instructions from different tasks and evaluating the performance on various benchmarks, providing strong evidence for their claims.
3. The proposed TIVE method is innovative, considering both instance influence and task difficulty scores for data selection. This holistic approach takes into account the characteristics of different tasks and instances, making it more effective than traditional data selection methods.

### Weaknesses
1. Lack of in-depth analysis of task characteristics: Although the paper considers task difficulty in its method, it could provide a more in-depth analysis of the characteristics of different tasks and how they affect data redundancy and model performance. Specifically, the paper does not delve into the nuances of each task type (e.g., VQA, grounding, conversation) and how their inherent properties contribute to the observed redundancy. A more granular analysis, perhaps examining the distribution of concepts, complexity of reasoning, or the diversity of visual content within each task, would strengthen the findings.
2. Why does Instance Influence consider the gradients of other samples (Formula 1)? Is it for the normalized comparison of all samples in Formula 2?
3. A significant limitation of the current study is the lack of ablation experiments to evaluate the relative importance of instance selection versus task selection. The paper would be strengthened by comparing the proposed method against two baseline scenarios: one using only instance influence for global selection without task-level grouping, and another applying task selection first followed by random sampling or established methods like GraNd within each selected task. Such comparisons would help quantify the individual contributions of these two selection mechanisms and provide stronger justification for the proposed two-stage approach. Furthermore, the paper lacks a clear explanation of how the task difficulty scores are derived and how they relate to the instance influence scores. It is unclear if these scores are learned or pre-defined, and how they interact during the data selection process.

### Questions
Is there any example analysis to see how the samples that were filtered out compare to those that were retained?

### Soundness
2

### Presentation
3

### Contribution
3
