# DELIFT: Data Efficient Language model Instruction Fine-Tuning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Fine-tuning large language models (LLMs) is essential for enhancing their performance on specific tasks but is often resource-intensive due to redundant or uninformative data. To address this inefficiency, we introduce \sysn{} (Data Efficient Language model Instruction Fine-Tuning), a novel algorithm that systematically optimizes data selection across the three key stages of fine-tuning: (1) instruction tuning, (2) task-specific fine-tuning (e.g., reasoning, question-answering), and (3) continual fine-tuning (e.g., incorporating new data versions). Unlike existing methods that focus on single-stage optimization or rely on computationally intensive gradient calculations, \sysn{} operates efficiently across all stages. Central to our approach is a pairwise utility metric that quantifies how beneficial a data sample is for improving the model's responses to other samples, effectively measuring the informational value relative to the model's current capabilities. By leveraging different submodular functions applied to this metric, \sysn{} selects diverse and optimal subsets that are useful across all stages of fine-tuning. Experiments across various tasks and model scales demonstrate that \sysn{} can reduce the fine-tuning data size by up to 70\% without compromising performance, offering significant computational savings and outperforming existing methods in both efficiency and efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents DELIFT, Data Efficient Language model Instruction Fine-Tuning, a method to select and prune fine-tuning data for three stages - initial instruction tuning, task-specific fine-tuning, and continual fine-tuning. One of the contributions of the paper is a utility-based kernel to quantify the importance of a data point in the presence of another data point used as an in-context learning (ICL) sample. The authors further use various submodular functions (Facility Location - FL, Facility Location Mutual Information - FLMI, and Facility Location Conditional Gain - FLCG) for the three fine-tuning stages defined above. The main core of DELIFT comprises of a greedy algorithm to iteratively select data points that provide the maximum marginal gain with respect to the chosen submodular function. DELIFT shows clear gains over various baselines for all three stages of fine-tuning using the Phi-3 (3.8B params) and Qwen-2 (72B params).

### Strengths
- The paper proposes a novel utility metric function to measure mutual information of data points and their relevance. The authors further highlight the benefit of this choice by comparing against sentence embedding based metrics. DELIFT performs better compared to DELIFT used with SE.
- The authors build targeted modular functions for each stage (FL for standard IFT, FLMI for task-specific FT, and FLCG for continual FT), catering to the optimization objectives for these 3 stages.
- DELIFT is able to retain and sometimes improve performance over the full fine-tuning by pruning out 70% of the full data.

### Weaknesses
 - Since the authors use post-trained models like Phi-3-mini-128k-instruct and Qwen2-72B-Instruct as the starting point, aren't the three stages described and the followup experiments basically a part of continual fine-tuning? I would be interested to see the effect of DELIFT when starting from base models and see if the method is able to prune out fine-tuning data for IFT starting from scratch.
- The authors present the results on ICL and QLoRA fine-tuning but not the full parameter fine-tuning. Are there diminishing gains with full model fine-tuning? I would like to see the results corresponding to those too.
- What's the computational cost for the data selection algorithm since it involves doing forward passes over the language model and not use cheap embedding models to compute the probability distributions. How does it compare it with the fine-tuning stage involving QLoRA. 
- Weakness 1 is further enhanced when results for use case 2 are presented, where fine-tuning actually leads to drop in performance on MMLU, where it doesn't make sense to do any task-specific fine-tuning at all. And I don't trust the results on MT-Bench since it's a very small dataset and the error bars would be huge. To mitigate this weakness, I would suggest the authors to try task-specific fine-tuning on say some reasoning dataset and then track the performance on benchmarks like MATH/GSM8K/ARC-Challenge etc.

### Questions
Other than the questions listed in the weaknesses, here are few clarifying questions for the authors:

1. For computing the metric in equation 2, are the probability vectors ($d$ dimension) from all predicted tokens (say $x$ tokens) concatenated to form a vector of dimension $x * d$ and then the equation 2 is applied?
2. Minor typo in Figure 2 (should be LAJ scores instead of LJA scores).
3. Can some other baselines be also included like [1] and [2].


[1] DEFT-UCS: Data Efficient Fine-Tuning for Pre-Trained Language Models via Unsupervised Core-Set Selection, Das et al., 2024.

[2] Text Quality-Based Pruning for Efficient Training of Language Models, Sharma et al., 2024.

### Soundness
3

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
3

### Summary
This paper addresses the challenge of selecting optimal data for fine-tuning large language models (LLMs). The authors propose a pairwise utility metric to assess the value of each sample based on the model's current performance and the relevance of other samples in the dataset. They introduce three variations of a facility location (FL) function to guide data selection at different fine-tuning stages, including (i) a vanilla FL function to prioritize diversity in general instruction fine-tuning, (ii) a mutual information-based FL function to select data that is diverse and relevant to a target task for task-specific fine-tuning, and (iii) a conditional gain-based FL function to select data that complements previously used data for continual fine-tuning. Experiments on two instructional models, Phi-3-mini and Qwen2-72B, demonstrate that the proposed methods outperform existing data selection techniques across all three fine-tuning stages.

### Strengths
- Data selection for LLM fine-tuning is a timely research problem, particularly in light of the growing model sizes, data availability, and resource constraints.
- The paper discusses the varying criteria for data selection across fine-tuning stages. The proposed method can be customized for different fine-tuning objectives.

### Weaknesses
 - The utility metric in Equation 1 is calculated based on in-context learning (ICL) gains, which may not directly translate to improvements in fine-tuning performance. Is there supporting literature to justify the use of ICL-derived utility in this context? Specifically, the ICL gain is measured by the change in the probability of the correct answer given an in-context example. This is a very indirect measure of how useful a sample will be for fine-tuning, which directly updates model weights based on gradients.
- It remains unclear how the utility gain measured through ICL reflects sample diversity in the semantic space. Since utility values are computed only once at the beginning of the data selection process, they may not capture changes in the model's performance after fine-tuning on the current selected subset. This static approach to data selection may miss opportunities to adapt to the evolving model during fine-tuning. The utility metric, based on ICL, is a measure of how much a single example helps a model answer another question, but this does not necessarily indicate that the example is diverse or that it will be useful for fine-tuning.
- The experimental design would benefit from comparisons with additional diversity-based baselines (e.g., clustering). Analysis of the selected examples across different methods would provide insights into the strengths and weaknesses of each approach. A more detailed analysis of the types of examples selected by each method, and how they differ, would be very helpful.
- A more thorough ablation analysis on the FL functions is needed. Do the additional terms for each fine-tuning stage significantly contribute to the results? Would the vanilla FL perform adequately across all stages? Evaluating this would help clarify the need for distinct data selection strategies at each fine-tuning stage. It's not clear if the added complexity of the mutual information and conditional gain terms is necessary, or if the vanilla FL function is sufficient.

### Questions
- In equation 3-5, what is $s_ij$? Is it the utility-based kernel $UF_ij$? Is it recomputed after each selection round? 
- For Equation 1, how is the ground truth distribution determined? The description of "a vector of ones for each token to signify perfect predictions" needs further clarification.
- The latex template of the submitted manuscript appears modified, as it lacks line numbers in the left margin.
- Why are instruction-finetuned models used for the experiments rather than pre-trained models, especially given that the first use case is instruction fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose a data selection method named DELIFT. DELIFT first employs a pairwise utility metric to quantify how beneficial a data sample is for improving the model's responses to other samples. Basing on the pairwise utility metric, DELIFT leverages 3 specially designed submodular functions to conduct diverse subsets that are useful across the instruction tuning, task-specific fine-tuning and continual fine-tuning. Experiments across various tasks and model scales demonstrate that DELIFT can reduce the fine-tuning data size by up to 70% without compromising performance, offering significant computational savings and outperforming existing methods in both efficiency and efficacy.

### Strengths
1. **Effective performance of DELIFT** In this paper, the authors design a utility-based kernel to quantify the informativeness of data. Based on this, the authors further design submodular functions for instruction data selection, targeting Instruction Tuning, Task-specific Fine-Tuning, and Continual Fine-Tuning. This method has been proven effective in all three stages and outperforms other model-dependent baselines.

### Weaknesses
1. **Related Work not Discussed** In Entropy Law [1], the authors also addressed the instruction data selection problem from the perspective of informativeness (entropy) and quantifies the relationship between data compression ratio and model performance; However, [1] is not discussed in this paper.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
3
