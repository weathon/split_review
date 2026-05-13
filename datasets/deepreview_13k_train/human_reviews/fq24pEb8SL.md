# Weighted-Reward Preference Optimization for Implicit Model Fusion

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
While fusing heterogeneous open-source LLMs with varying architectures and sizes can potentially integrate the strengths of different models, existing fusion methods face significant challenges, such as vocabulary alignment and merging distribution matrices. These procedures are not only complex but also prone to introducing noise and errors. In this paper, we propose an implicit fusion method, Weighted-Reward Preference Optimization (WRPO), which leverages preference optimization between the source LLMs and the target LLM to transfer their capabilities effectively. WRPO eliminates the need for vocabulary alignment and matrix fusion and can be efficiently scaled to accommodate various LLMs. To address distributional deviations between the source and target LLMs, WRPO introduces a progressive adaptation strategy that gradually shifts reliance on preferred examples from the target LLM to the source LLMs. Extensive experiments on the MT-Bench, AlpacaEval-2, and Arena-Hard benchmarks demonstrate that WRPO consistently outperforms existing knowledge fusion methods and various fine-tuning baselines. When applied to LLaMA3-8B-Instruct as the target model, WRPO achieves a length-controlled win rate of 55.9\% against GPT-4-Preview-1106 on AlpacaEval-2 and a win rate of 46.2\% against GPT-4-0314 on Arena-Hard.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to align the LLM prediction from multiple source models to a target model. Specifically, it focuses on fuse multiple heterogeneous LLMs and combine their preference into the target one. Technically, it proposes a weighted-reward strategy to implicitly fuse the source models. Experiments on several evaluation benchmarks show the method effectiveness.

### Strengths
1. LLM alignment is popular and valuable research topic, especially aligning heterogenous models into a target one.
2. The proposed weighted-reward is a straightforward to to achieve an implicit model fusion process.
3. Comprehensive evaluation supports the paper statement with rich analysis.

### Weaknesses
1. Adding an analysis of alignment efficiency and ablation will be helpful, what is the difference of using different source models? if multiple source models are used, will it increase the alignment cost?
2. Some analysis parts can be more informative such as figure 3 and 4. Including more analysis and make them dense will further enhance the draft.

### Questions
Please refer to the weaknesses section above.

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
This paper introduces Weighted-Reward Preference Optimization (WRPO), an implicit model fusion approach for large language models (LLMs) that bypasses the need for complex vocabulary alignment and distribution merging found in traditional fusion methods. WRPO uses a weighted reward mechanism and a progressive adaptation strategy to smoothly transfer preference weights from the target model to source models. Benchmark results on AlpacaEval-2 and MT-Bench show that WRPO consistently outperforms traditional fusion and preference optimization methods, marking it as a promising advancement in LLM model fusion.

### Strengths
1. WRPO effectively introduces implicit model fusion, bypassing the need for complex vocabulary alignment and distribution merging, a significant advancement over traditional methods.
2. The novel reward mechanism balances contributions from source and target models and helps mitigate distributional discrepancies, leading to a smoother optimization process.

### Weaknesses
1. The success of WRPO appears to depend heavily on the choice and quality of source models, yet the paper does not fully address criteria or strategies for selecting these source models, which could be a limiting factor in practice. The paper lacks a systematic exploration of how different source model characteristics (e.g., size, architecture, training data) impact the final performance. For example, are there specific types of models that consistently lead to better fusion results, or is it highly task-dependent? This makes it difficult to assess the generalizability of the approach.
2. The need for dynamic tuning of the fusion coefficient introduces complexity, and the paper does not sufficiently detail how this parameter was optimized across different datasets and tasks. The paper does not specify the range of values explored for the fusion coefficient, nor does it provide a clear rationale for the chosen optimization strategy. Furthermore, the paper does not discuss the sensitivity of the results to variations in the tuning process, which is crucial for practical implementation.
3. While WRPO is more efficient than traditional methods, it still requires significant computational resources for training and fine-tuning, especially when handling multiple large LLMs, which may limit its accessibility. The paper does not provide a detailed breakdown of the computational costs associated with different stages of the WRPO pipeline, such as the initial sampling from source models, the reward model evaluation, and the actual training of the target model. This lack of transparency makes it difficult to assess the practical feasibility of the approach.
4. Although WRPO is presented as a robust method, more ablation studies could have provided a clearer understanding of the specific impact of each component, particularly the fusion coefficient and its progressive adjustment. The paper lacks a systematic analysis of the individual contributions of the reward mechanism and the progressive adaptation strategy. For example, it is unclear how much each component contributes to the overall performance gains, and whether the method is robust to variations in these components.

### Questions
1. How sensitive is WRPO to the selection of source LLMs? Could varying the quality and diversity of source models affect the final performance, and if so, what are the selection criteria?
2. What are the specific criteria or methods used for tuning the fusion coefficient? How was it determined for different tasks, and does it require extensive hyperparameter optimization?
3. Could WRPO be applied to multilingual or cross-domain tasks where distributional shifts might be more pronounced, and if so, are any modifications required?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the progress of fusing heterogeneous open-source LLMs with varying architecture and size. They then summarise the challenges in this scenario, including vocabulary alignment and merging distribution matrices. To solve these challenges, they propose an implicit fusion method, Weighted-Reward Preference Optimization (WRPO), which eliminates the need for vocabulary alignment and matrix distribution and improves the performance on multiple benchmarks.

### Strengths
1. The paper explores the direction of improving the capabilities of individual models by combining the strength of multiple LLMs, which has potential benefits to improve the ability of individual models.
2.  They propose a novel implicit fusion method that eliminates the need for vocabulary alignment and matrix fusion.
3. Extensive experiments demonstrate the effectiveness of proposed methods in multiple aspects.

### Weaknesses
1. Although the proposed methods demonstrate a certain degree of improvement on AlpacaEval-2 and Arena-Hard, they only have weak influences in MT-Bench. This weakens the generalization of the proposed methods.
2. The object of the proposed WRPO is to increase the likelihood of a preferred response while decreasing the occurrence of the dispreferred response. Preferred responses come from source and target models and dispreferred responses only come from the source model, which means dispreferred responses from the source model will not influence training. Whether some potential small experiments that support this phenomenon as it is intuitively we not only need to learn recognition capability in correct data but also learn exclusion ability.
3. Although the experiment section provides some interpretation, it lacks an in-depth analysis of the rationale behind the proposed phenomenon, such as, how WRPO achieves a balance between effectiveness and efficiency.
4. They lack the discussion of limitations and future work.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
