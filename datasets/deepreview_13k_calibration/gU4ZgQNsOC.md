# Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Pretraining large language models (LLMs) on vast and heterogeneous datasets is crucial for achieving state-of-the-art performance across diverse downstream tasks. However, current training paradigms treat all samples equally, overlooking the importance or relevance of individual samples throughout the training process. Existing reweighting strategies, which primarily focus on group-level data importance, fail to leverage fine-grained instance-level information and do not adapt dynamically to individual sample importance as training progresses. In this paper, we introduce novel algorithms for dynamic, instance-level data reweighting aimed at improving both the efficiency and effectiveness of LLM pretraining. Our methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples at the current training stage. In particular, our framework allows us to systematically devise reweighting strategies deprioritizing redundant or uninformative data, which we find tend to work best. 
Furthermore, we develop a new theoretical framework for analyzing the impact of loss-based reweighting on the convergence of gradient-based optimization, providing the first formal characterization of how these strategies affect convergence bounds. We empirically validate our approach across a spectrum of tasks, from large-scale LLM pretraining to smaller-scale linear regression problems, demonstrating that loss-based reweighting can lead to faster convergence and improved performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a dynamic, instance-level data reweighting approach aimed at enhancing the efficiency and effectiveness of large language model (LLM) pretraining. Traditional LLM training paradigms apply uniform sampling to datasets, ignoring individual sample importance. Current reweighting strategies are mostly group-level and lack the adaptability required for instance-specific optimization during training. The authors propose a novel approach that reweights samples dynamically based on their loss values, helping the model to focus on more informative samples. They also provide a new theoretical framework for analyzing how loss-based reweighting impacts convergence rates, demonstrating that deprioritizing low-loss samples leads to faster convergence and improved performance. Empirical results confirm the effectiveness of this approach across various tasks, from large-scale LLM pretraining to smaller problems like linear regression.

### Strengths
1. Innovative Instance-Level Reweighting Mechanism: The paper introduces a fine-grained, instance-level reweighting strategy, which addresses the limitations of traditional group-level reweighting methods. 

2. Theoretical Framework for Convergence Analysis: The authors provide a novel theoretical framework that explicitly characterizes the effect of loss-based reweighting on convergence bounds. This contribution not only supports the empirical findings but also adds a theoretical foundation that enhances the credibility of the proposed approach.

### Weaknesses
1. Although the authors state that the proposed method is designed for LLM pretraining, the evaluation is conducted solely on QA tasks. Generally, QA tasks are simpler than generation or reasoning tasks. Therefore, the benefits of pretraining LLMs may not be adequately assessed under this setting. The evaluation should include more complex tasks that can better demonstrate the capabilities of the pretrained model, such as text generation, summarization, or complex reasoning tasks that require multi-step inference.

2. Experimental settings. In the experimental section, the authors evaluate only on smaller language models, specifically GPT-2 models with fewer than 1 billion parameters. Typically, effective LLM pretraining methods should demonstrate scalability to models with at least 10 billion parameters to ensure practical applicability. Consequently, the practicality of the proposed method is not fully substantiated in this study. The lack of experiments on larger models leaves open the question of whether the observed benefits will translate to models of practical interest.

3. There are several typos in this paper. For example, "LANGGUAGE" should be 'Language'. "fined-grained" should be "fine-grained". "deprioritize redundant or uninformative data" should be "deprioritizing redundant or uninformative data".

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces novel algorithms for dynamic, instance-level data reweighting aimed at improving the efficiency and effectiveness of large language model (LLM) pretraining. The proposed methods adjust the weight of each training sample based on its loss value in an online fashion, allowing the model to dynamically focus on more informative or important samples during different training stages. The paper also provides a theoretical framework for analyzing the impact of these reweighting strategies on the convergence of gradient-based optimization.

### Strengths
(1) The paper introduces an innovative and practical methodology for dynamically reweighting training samples based on their loss values, which could significantly enhance the efficiency and effectiveness of LLM pretraining.

(2) The empirical findings are robust, demonstrating that the proposed reweighting strategies lead to faster convergence and improved performance across a variety of tasks and model scales.

(3) The proposed algorithms can be seamlessly integrated into existing training pipelines with little to no computational overhead, making them highly practical for real-world applications.

### Weaknesses
 (1) The paper might benefit from additional implementation details to enable reproducibility of the study, especially for the proposed reweighting algorithms.

(2) While the evaluation is comprehensive, further ablation studies could strengthen the paper by isolating the impact of different components of the proposed methods.

(3) It would be helpful to have more detailed discussions comparing the proposed methods with other widely-known reweighting or data selection techniques beyond those already mentioned.

### Questions
1. Could you provide more detailed implementation steps for the dynamic reweighting algorithms? Specifically, information on how to normalize the losses, apply the reweighting strategies, and integrate these into existing training pipelines would be beneficial for reproducibility.
﻿
2. The curriculum adjustment mechanism using a temperature parameter is an interesting aspect of your approach. Could you provide more details or results on how different values of the temperature parameter affect the performance and convergence of the model? This would help in understanding the sensitivity and effectiveness of this component.

3. Your theoretical analysis mentions that the reweighting schemes avoid overfitting to outliers. Could you provide empirical evidence or additional discussion on how well your methods handle outliers in practice, especially compared to other robust optimization techniques?
﻿
4. Your results indicate that the benefits of your reweighting strategies are more pronounced in larger models. Could you provide more insights or hypotheses on why this might be the case? Additionally, discussing any observed limitations or challenges when applying these strategies to smaller models would be helpful.

### Soundness
3

### Presentation
2

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
The paper presents a framework for dynamically reweighting training samples in large language model (LLM) pretraining based on loss values. This approach contrasts with traditional uniform sampling by adjusting sample importance during training, allowing the model to focus on more informative data and deprioritize redundant samples. The authors introduce three reweighting strategies, each designed to emphasize specific portions of the loss distribution, and establish a theoretical foundation for their effectiveness on model convergence. Experimental results show that these methods lead to faster convergence and improved performance on various benchmarks, especially when combined with existing domain-level reweighting methods like DoGE and DoReMi.

### Strengths
- Originality: The paper introduces a novel approach to LLM pretraining by leveraging instance-level, dynamic reweighting based on loss values. Also, the theoretical results justify the methods.

- Quality: The paper combines theoretical analysis with empirical results across multiple benchmarks. The authors provide convergence bounds and use diverse model scales to demonstrate the generalization and scalability.

- Clarity: The methodology and notations are well-defined, with clear mathematical formulation and supporting visualizations.

- Significance: The paper’s instance-level reweighting method enhances training efficiency and model performance. Its compatibility with existing domain-level techniques (e.g., DoGE, DoReMi) highlights its practical value

### Weaknesses
1. **Clarity**: The statement “where $L>0$ is the smoothness parameter” under Equation (7) is unclear since $L$ does not show up in Equation (7) and could benefit from further explanation.
2. **Benchmark Choice**: The choice of benchmarks (LogiQA, LogiQA 2, SciQA, PiQA) is not well-justified. Testing on additional benchmarks like MMLU, ARC, hellaswag, boolq and TruthfulQA could strengthen the few-shot evaluation.
3. **Baseline Comparisons**: Table 1 lacks a direct comparison with baseline methods (DoGE and DoReMi), which would provide valuable context for the effectiveness of the proposed approach.
4. **Theoretical Assumptions**: The assumption that the maximum weight is capped at $2/M$ may be too strict, particularly in data selection scenarios with fewer than half the dataset selected. Justification for this assumption's practicality is needed.
5. **Efficiency Discussion**: The paper could better address the efficiency benefits of the proposed methods compared to DoGE and DoReMi, especially regarding computation and implementation costs.

### Questions
1. **Benchmark Justification**: Could you elaborate on the selection of LogiQA, LogiQA 2, SciQA, and PiQA as benchmarks? Testing additional benchmarks, such as MMLU, ARC, hellaswag, boolq, and TruthfulQA, could further strengthen the few-shot performance evaluation.

2. **Baseline Comparisons**: Including DoGE and DoReMi as baselines in Table 1 would provide useful context on the effectiveness of the proposed approach. Would you consider adding this comparison?

3. **Justification for $2/M$**: The theoretical assumption cap on maximum weight at $2/M$ seems restrictive. Could you provide further justification or discuss how this assumption holds in practical applications?

4. **Efficiency Discussion**: A deeper comparison of computational and implementation efficiency relative to DoGE and DoReMi could underscore the practical advantages of your method. Could you expand on this?

### Soundness
3

### Presentation
4

### Contribution
3
