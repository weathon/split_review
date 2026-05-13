# BESA: Pruning Large Language Models with Blockwise Parameter-Efficient Sparsity Allocation

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Large language models (LLMs) have demonstrated outstanding performance in various tasks, such as text summarization, text question-answering, and etc. While their performance is impressive, the computational footprint due to their vast number of parameters can be prohibitive. 
Existing solutions such as SparseGPT and Wanda attempt to alleviate this issue through weight pruning. However, their layer-wise approach results in significant perturbation to the model's output and requires meticulous hyperparameter tuning, such as the pruning rate, which can adversely affect overall model performance.
To address this, this paper introduces a novel LLM pruning technique dubbed blockwise parameter-efficient sparsity allocation (BESA) by applying a blockwise reconstruction loss. In contrast to the typical layer-wise pruning techniques, BESA is characterized by two distinctive attributes: i) it targets the overall pruning error with respect to individual transformer blocks, and ii) it allocates layer-specific sparsity in a differentiable manner, both of which ensure reduced performance degradation after pruning.
Our experiments show that BESA achieves state-of-the-art performance, efficiently pruning LLMs like LLaMA1, and LLaMA2 with 7B to 70B parameters on a single A100 GPU in just five hours.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the weight pruning problem of large language models. In order to solve the problems of significant output disturbance and the need for careful hyperparameters tuning in existing layer-wise methods, a novel LLM pruning technique named block-wise parameter-efficient sparsity allocation (BESA) is proposed, with two distinctive characters: minimizing pruning error for individual blocks and ensuring the layer-specific sparsity differentiable. Finally, this paper verified the performance and efficiency of the method through detailed experiments on strong baselines.

### Strengths
This paper introduces a novel approach, BESA, for compressing Large Language Models through block-wise pruning with a differentiable sparsity allocation, which maintains the performance of LLMs well and improves computational efficiency compared to existing methods. Besides, this paper is well written, clearly explaining the method of block-wise tuning and parameter-efficient sparsity learning through detailed mathematical and textual expression. Finally, credible experimental design and solid experimental results and increase the credibility of the paper.

### Weaknesses
There may be a few things that need to be modified or clarified clearly. In page 3 BLOCK-WISE PRUNING equation (1), it is better to add the meaning of “W” together with “M, F, X, …”; Since the article mentioned that existing methods require meticulous hyperparameter tuning, adding the sensitivity of some vital hyperparameters of the proposed model and clarify the advantage in the appendix will make this paper more convincing.

### Questions
1)Considering the abstract mentions existing methods require meticulous hyperparameter tuning, it would be better to study the vital hyperparameter’s sensitivity of the proposed method and experiments are needed, which will make this paper more convincing. 
2) Due to the uniqueness of the proposed method BESA, which seeks the optimal pruning rate for each layer, compared to existing methods, will implementing specialized neural network accelerators (ViTCoD in the experiments) consume additional time or make model faster than others?

### Soundness
4 excellent

### Presentation
3 good

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
The paper presents a novel pruning technique called Blockwise Parameter-Efficient Sparsity Allocation (BESA) for compressing large language models (LLMs). BESA aims to address the computational footprint and memory consumption issues associated with LLMs by optimizing pruning rates across different layers in a differentiable manner. The proposed method achieves state-of-the-art performance in pruning various LLMs, such as LLaMA1 and LLaMA2, and efficiently prunes them on a single A100 GPU.

### Strengths
- BESA is the first differentiable pruning algorithm for LLMs, which allows for efficient optimization of pruning rates across layers.
- The method is parameter-efficient and easy to optimize, exhibiting high efficiency and effectiveness in pruning various LLMs.
- BESA achieves state-of-the-art performance in pruning various LLMs, such as LLaMA1 and LLaMA2, with reduced performance degradation after pruning.
- The proposed method can be jointly optimized with weight-only quantization techniques, further enhancing the compression ratio and efficiency of LLMs.

### Weaknesses
- The paper does not provide a detailed analysis of the trade-offs between different pruning rates and their impact on model performance, which could be useful for understanding the optimal pruning strategy.
- The paper does not provide a comprehensive comparison of BESA with other pruning techniques, such as structured pruning, which could help in understanding the relative strengths and weaknesses of the proposed method.

### Questions
NA

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
The authors propose a blockwise model pruning framework for compressing LLMs, which searches for optimal pruning rates for each layer in a differentiable manner. The authors have done experiments on different models and datasets.

### Strengths
1. The authors demonstrate the practical speedup of the pruned model in a hardware simulator.
2. The method is parameter-efficient and easy to optimize.
3. The authors have done extensive experiments on language modeling and few-shot learning benchmark datasets. The authors also explore models with different numbers of parameters from 7b to 70b.

### Weaknesses
1. It would be better to involve the computational cost of attention weight in Table 4.
2. It would be better to have an ablation study of block-wise pruning. Maybe directly pruning all the models instead of layer by layer.
3. There has been a lot of research on pruning in CV and NLP. The baselines are far from complete, such as "The Lottery Ticket Hypothesis" and its following works. While considering not much work on LLM, I would not penalize too much on it.

Overall, I think the experiments are solid. The novelty is ok, but it would be better to explore more classical pruning methods.

### Questions
The model seems not significantly better than SparseGPT with a smaller number of parameters. Could you have significant test?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a novel method for blockwise pruning of LLMs. It was evaluated with generation tasks, as well as for zero-shot downstream tasks, and outperformed SparseGPT and Wanda baselines.

### Strengths
- The proposed method outperformed recent baselines.
- The motivation for this research is clear, and the proposed method is helpful for practitioners.

### Weaknesses
Authors claimed BESA has different advantages compared to other baselines. E.g., the fact that BESA differentiably optimizes masks, unlike SparseGPT. However, it is not clear whether other methods could or could not use such specific techniques and what makes BESA better than them. The current ablation study does not answer these questions.

### Questions
Please refer to the weaknesses Section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
