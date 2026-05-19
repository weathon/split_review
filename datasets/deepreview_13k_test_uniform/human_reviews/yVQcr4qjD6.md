# Robust Function-Calling for On-Device Language Model via Function Masking

- Decision: Accept
- Scores: 6, 6, 8, 6, 8

## Abstract
Large language models have demonstrated impressive value in performing as autonomous agents when equipped with external tools and API calls. Nonetheless, effectively harnessing their potential for executing complex tasks crucially relies on enhancements in their function-calling capabilities. This paper identifies a critical gap in existing function-calling models, where performance varies significantly across benchmarks, often due to being misled by specific naming conventions. To address such an issue, we introduce Hammer, a novel family of foundation models specifically engineered for on-device function calling. Hammer employs an augmented dataset that enhances models' sensitivity to irrelevant functions and incorporates function masking techniques to minimize misleading. Our empirical evaluations reveal that Hammer not only outperforms larger models but also demonstrates robust generalization across diverse benchmarks, achieving state-of-the-art results. Our open-source contributions include a specialized dataset for irrelevance detection, a tuning framework for enhanced generalization, and the Hammer models, establishing a new standard for function-calling performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study introduces Hammer, a novel family of foundation models designed to enhance function-calling capabilities in large language models (LLMs). The authors developed a specialized dataset comprising 7,500 instances to improve the models' sensitivity to irrelevant functions. By shifting the focus from function names and parameters to their descriptions, the Hammer models aim to reduce the likelihood of misinterpretation, thereby enhancing generalization across diverse benchmarks. Experimental results indicate that Hammer models achieve superior performance across various benchmarks.

### Strengths
1. The work effectively identifies the issue of naming variability in function-calling LLMs and incorporates training methods to address it.
2. Hammer models utilize an augmented dataset to handle null function-calling cases.
3. The study conducts comprehensive evaluations, demonstrating that Hammer consistently performs well across diverse benchmarks, establishing it as a reliable open-source model for function calling.

### Weaknesses
1. The proposed methods may inherit potential biases inherent in LLMs. The sampled "Masked Data" can degrade in performance when encountering function names or parameters that differ significantly from those seen during training. This dependency may limit its effectiveness in applications where naming conventions vary widely.
2. There are potential overfitting concerns. The authors do not provide a thorough data contamination analysis for the newly created dataset.
3. Whether the performance boosting comes from the effectiveness of the proposed pipeline or the Qwen model itself remains questionable. According to the results of ``API-Bank’’ columns in Table 5, when using the same base model, Deepseek-Coder-7B, it is not as effective as the xLAM variant. Authors could have Qwen models trained with xLAM datasets to further elaborate it.
4. The presentation of results is not well-organized. Comprehensive tables are difficult to follow and analyze, making it challenging to verify the effectiveness of each component. Authors could break down the long tables into smaller and more focused  ones. Also, for figure 3, author could have the examples shown in function masking to be larger and more compact.

### Questions
1. Could the authors provide a more detailed analysis of function name issues? Specifically, how many failed cases are due to function or parameter name errors? Figure 2 does not clearly convey this information. Authors may consider an error type analysis with detailed tables isolating the number of failure cases due to function name/ arguments name/ other error types.
2. It would be beneficial for the authors to analyze how many failed cases result from irrelevant function calls. The urgency of this issue is not apparent in the current version. 
3. Based on the results in Table 5, it is difficult to verify the effectiveness of the proposed pipeline compared to xLAM variants. Suggestions could refer to weakness item 3.
4. While Table 1 shows that Hammer achieves impressive results on AST evaluations, the comparitive performance boosting across other benchmarks in Table 2 does not show the same level of improvement. Is there any analysis to explain this discrepancy? Authors could provide discuss potential reasons for the discrepancy and propose additional experiments or analyses that could help explain the varying levels of improvement observed.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Hammer, a family of lightweight models for function-calling tasks that addresses the problem of inconsistent performance across different benchmarks. The authors propose a function masking technique during training and an irrelevance-augmented dataset to improve model robustness and generalization. Experiments show that Hammer achieves competitive performance compared to larger models like GPT-4 on various benchmarks.

### Strengths
1. The function masking technique is an innovative solution to reduce model dependency on naming conventions. The empirical results show this approach helps achieve more consistent performance across different benchmarks.
2. The authors conduct extensive experiments across multiple benchmarks and provide detailed ablation studies on masking ratios and irrelevance detection. The evaluation is thorough and well-documented with clear performance metrics.
3. The work addresses a real-world problem in function-calling models and provides a lightweight solution suitable for on-device deployment. The improved generalization capability has significant practical value.

### Weaknesses
1. The authors replace function names with random strings, but don’t explore using semantically similar names. This approach may be overly aggressive since function names often contain valuable semantic information that could be preserved while still improving generalization
2. While the paper demonstrates Hammer’s superior performance, it lacks detailed analysis of other potential contributing factors beyond the masking technique. The choice of base model and other training details could significantly impact the results
3. More detailed error patterns analysis would be beneficial to understand the model and baseline failure patterns across different benchmarks

### Questions
1. Have you tried replacing function names with semantically similar ones instead of random strings? This could be more meaningful since function names are important features in practice and descriptions and parameters may sometimes be missing. In some usage scenarios LLMs need to infer functionality from names alone.
2. Could you provide more insights into other factors contributing to Hammer’s performance? Have you tried using DeepSeek models as base models (just like xLAM) instead of just Qwen? This would be helpful to understand what specific aspects of the base model selection impacted results. Also, it would be beneficial to know if there are other training tricks beyond data augmentation.
3. For Table 1’s inconsistent performance across benchmarks, I am curious why does xLAM perform well on three benchmarks but poorly on two others? Could the authors provide some error pattern analysis and related insights?

Minor things: the observations in the paper might be related to the code data contamination problem as well, where the memorization of func names / orders could impact the generalization ability. Ref: https://arxiv.org/pdf/2402.05980

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors studied large language models' function calling and tool use abilities. The authors not only identified a critical gap in existing function-calling models, where the model is often misled by specific naming of functions and arguments. 
To address the issue, the authors present a novel tunning framework that masks the function name and arguments; this results in a family of various new open-source function calling models called Hammer and also a new specialized dataset for irrelevance detection. These models achieves state of the art performance on open benchmark and leaderboards such as Berkeley function calling (BFCL).

### Strengths
- The authors identified a very important issue of the current existing open source function calling models such as xlam.
- Based on the issue, the method that the authors proposed makes a lot of sense and indeed achieves very good performance.
- The model and dataset will be open source later, which would benefit the community a lot.

### Weaknesses
- The method is specifically designed for function calling problems; it is unclear whether some other domains will also benefit the tunning framework;
- I am not sure how this strategy is specifically related to on-device language models; It can also be applied to larger models, and it would be really great to see the performance of larger models such as 70B llama if they are applied with this method; 
- For the cases where there is little description, I am not sure if we can still leverage the masking strategy.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Hammer, a novel family of language models specifically designed for function-calling tasks. The authors identify a critical limitation in existing models: their performance varies significantly across benchmarks due to being misled by function and parameter naming conventions. To address this, they propose a function masking technique during training and augment the training data with irrelevant detection examples. Their empirical results show that Hammer models achieve state-of-the-art performance across multiple benchmarks, particularly impressive for their parameter count, with the 7B parameter version competing with much larger models including GPT-4 on certain metrics.

### Strengths
1. The problem identification is well-motivated and articulated.
2. The evaluations are comprehensive, covering multiple benchmarks and including detailed ablation studies on both masking ratios and irrelevance detection data proportions.

### Weaknesses
1. The paper doesn't include the comparison with some recent relevant baselines (e.g., ToolBench, API-Bank).
2. There are no ablation studies on the effect of different description formats/lengths on model performance.
3. There’s no discussion of potential failure modes or edge cases where function masking might perform worse than traditional approaches.
4. The random string generation process for masking isn't fully specified - different approaches to generating random strings could affect reproducibility.
5. The exploration of the trade-off between masking and maintaining semantic meaning in function names is limited.

### Questions
How does the function masking technique affect the model's zero-shot generalization to entirely new API schemas or documentation formats not seen during training?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the problem of inconsistent performance across benchmarks in current function-calling models, which often arises from different function and parameter names. The authors developed an augmented dataset and proposed a novel function masking method that guide the model to focus more on function descriptions, instead of names, thereby enhancing its robustness and generalization capabilities across diverse benchmarks.

### Strengths
1. This paper identifies a significant challenge in current function calling models that is both practical and impactful, particularly as the function calling models are increasingly deployed in real-world applications where robustness and accuracy are essential.

2. The proposed method is simple but effective, which addresses the problem thoroughly. The method guides the model to focus on function descriptions rather than names. Also, the method is potentially replicable and offers inspiration for ai safety practitioners in other fields who seek to improve model robustness.

3. The evaluations are thorough and effectively demonstrate the method’s applicability to real-world use cases. 

4. The authors consider irrelevance detection, which is essential in practical applicaitons, as it reduces the risk of incorrect or unnecessary function calls and enhances reliability.

### Weaknesses
The paper claims that the model is designed for on-device function calling; however, it lacks sufficient explanations or evaluation results to demonstrate its efficiency or performance in such scenarios. The authors did not discuss the hardware configurations required to run the model on edge devices or address potential resource constraints. Additionally, the authors did not provide evaluation results regarding inference time, which are essential for assessing the model’s practicality in real-world, resource-limited environments.

### Questions
see weakness

### Soundness
4

### Presentation
3

### Contribution
3
