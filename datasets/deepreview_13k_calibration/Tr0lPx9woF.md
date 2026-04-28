# Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
With the rapid growth of large language models (LLMs), there is increasing demand for memory and computation in LLMs. Recent efforts on post-training pruning of LLMs aim to reduce the model size and computation requirements, yet the performance is still sub-optimal. 
In this paper, we present a plug-and-play solution for post-training pruning of LLMs.
The proposed solution has two innovative components: 1) **Relative Importance and Activations (RIA)**, a new pruning metric that jointly considers the weight and activations efficiently on LLMs, and 2) **Channel Permutation**, a new approach to maximally preserves important weights under N:M sparsity.
The two proposed components can be readily combined to further enhance the N:M semi-structured pruning of LLMs.
Our empirical experiments show that RIA alone can already surpass all existing post-training pruning methods on prevalent LLMs, e.g., LLaMA ranging from 7B to 65B. Furthermore, N:M semi-structured pruning with channel permutation can even outperform the original LLaMA2-70B on zero-shot tasks, together with practical speed-up on specific hardware.
Our code is available at: https://github.com/biomedical-cybernetics/Relative-importance-and-activation-pruning

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the growing demand for efficient memory and computation in large language models (LLMs). Existing post-training pruning methods have attempted to reduce model size and computation but have not achieved optimal performance. The paper introduces a plug-and-play solution for post-training pruning of LLMs, featuring two innovative components: 1) Relative Importance and Activations (RIA), a novel metric that efficiently considers weight and activations in LLMs, and 2) Channel Permutation, a new approach to maximize the preservation of important weights with N:M sparsity. These components can be combined to enhance N:M structured pruning of LLMs. Empirical experiments demonstrate that RIA alone surpasses existing pruning methods on various LLMs. Moreover, N:M structured pruning with channel permutation can even outperform the original LLaMA2 70B on zero-shot tasks, while providing practical speed-up on specific hardware.

### Strengths
- Consider both weights and activations for unstructured pruning in LLMs is novel.
- Particularly, the consideration of relative weight importance is a novel approach.
- Channel permutation is a simple yet effective method for achieving N:M sparsity.

### Weaknesses
The reviewer recognizes the novelty and simplicity of the overall approach but has raised substantial concerns. The main issues pertain to the weaknesses in the baselines, which make it challenging for me to be convinced of the effectiveness of the proposed method. Moreover, the motivation and analysis provided appear to be inadequate. For example, concerning the former issue, the following questions come to mind: even if the proposed method can enhance the performance of N:M sparsity-based approaches, are N:M sparsity-based methods genuinely effective? Are they superior to contextual sparsity-based methods?

I describe specific questions and suggestions regarding concerns as follows:

- Insufficient experimental support for motivation: This paper argues the existence of 'channel corruption' asserting that removing input/output channels results in decreased performance as observed in prior works. However, the paper lacks empirical evidence to substantiate this claim. It would be valuable if the authors could include preliminary experiments to provide a basis for their motivation.
- According to AWQ [1], activation-aware weight quantization, which selects important weights based on activation distribution rather than weight distribution, outperforms traditional weight-based quantization. Inspired it, the reviewer suggests that it would be meaningful to consider baseline methods based on activation-based weight pruning for comparison. Therefore, the authors might incorporate and compare unstructured pruning based solely on activations in Table 2.
- In addition to the comparisons with N:M sparsity methods in Table 4 and Table 5, it is advisable to include a comparison with other structured pruning techniques in terms of performance and inference speed improvement. For instance, including a method like Dejavu [2] in the comparison would enhance the comprehensiveness of the evaluation.
- What is the relevance of the experiments in Figure 2 to the claim that activation outliers exist independently of the dataset and model's parts? The reviewer thinks that even if activation values exhibit a high correlation between two datasets, it is possible that activation outliers can be eliminated. Therefore, it would be helpful to clarify the connection between Figure 2 and the claim about activation outliers.
- Can we expect additional performance improvements when combined with post-training quantization methods such as Smooth Quant [3] or AWQ [1]?

[Minor]
- Why is the title "plug-and-play"?
- The hyperlink in the 6-page appendix seems to be incorrect.

### Questions
Please address the concerns in Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Main Contribution:
- The paper proposes two new methods for efficient post-training pruning of large language models (LLMs):
    1) Relative Importance and Activation (RIA), a new pruning metric that considers both weight and activation information to determine weight importance. 
    2) Channel Permutation, a method to maximize retention of important weights when converting a model to N:M sparsity for hardware acceleration.

Novelty:
- RIA provides better pruning performance than prior state-of-the-art methods by avoiding pruning entire channels and using activations to assess weight importance.  
- Channel Permutation reformulates the input channel permutation problem as a linear sum assignment problem, allowing efficient optimization using the Hungarian algorithm.

Experiments:
- Experiments conducted on LLMs including LLaMA, LLaMA-2, and OPT ranging from 7B to 70B parameters.
- Tasks: Language modeling (Wikitext-2 perplexity) and zero-shot classification (5 commonsense datasets).
- Compared RIA to magnitude pruning, SparseGPT, and Wanda for unstructured pruning.  
- Evaluated Channel Permutation combined with RIA and other methods under N:M sparsity.

Results:
- RIA outperforms prior state-of-the-art post-training pruning methods in both unstructured and N:M sparsity settings.
- Channel Permutation further improves performance under N:M sparsity by efficiently finding better channel arrangements.
- Together, RIA and Channel Permutation provide an effective pipeline for LLM pruning and acceleration with negligible performance loss.

Conclusion:
- RIA and Channel Permutation establish new state-of-the-art results for efficient one-shot post-training pruning of LLMs.
- The proposed methods enable practical acceleration and size reduction of large models.

### Strengths
1. Proposes two novel methods (RIA and Channel Permutation) that provide state-of-the-art performance for post-training pruning of large language models.

2. Comprehensive experiments conducted on multiple popular LLMs across a range of model sizes from 7B to 70B parameters.

3. Evaluated on diverse tasks including language modeling and zero-shot classification to demonstrate generalization. 

4. Provides both theoretical analysis and empirical results to demonstrate the efficiency and efficacy of the proposed techniques.

5. RIA and Channel Permutation can be readily combined into an effective pipeline for practical LLM pruning and acceleration, with negligible performance loss.

### Weaknesses
 Overall the manuscript has solid contributions, but expanding the variety of models, tasks, and languages could strengthen the demonstrated effectiveness. Testing scalability and comparing to other recent techniques would also help round out the evaluation. But within the chosen scope, the paper delivers valuable advancements for efficient LLM pruning.

* For "We employ 128 samples from the C4 dataset":
using only 128 samples from C4 as the calibration data is quite limited. With so few samples, the activation statistics may not sufficiently capture the full distribution. The concern is that the activation patterns derived from such a small subset might not accurately represent the broader range of activations that the model would encounter during real-world inference, potentially leading to suboptimal pruning decisions. This is particularly relevant for large language models, where activation distributions can be highly complex and dependent on the input context.

### Questions
* what is the channel here in the Transformer models? Transformer models does not have channel or column.

* for ""We employ 128 samples from the C4 dataset", is it possible/worth to do the experiments on a larger and more diverse calibration set (128 might be limited)?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
* The paper introduces a relative importance pruning metric which leads to more uniform pruning patterns.
* The paper proposes to apply channel permutations found by a scalable heuristic in order to relax the pattern restrictions imposed by n:m pruning.
* Both techniques are evaluated on Llama models for perplexity and zero-shot tasks.

### Strengths
* The proposed techniques are relatively simple to implement in practice and in particular the channel reordering seems to be quite effective.
* The paper is easy to understand and provides clear visualizations of the key algorithms.
* Evaluation is carried out on strong Llama models and not just on older OPT ones.
* The Appendix contains interesting additional studies like combining RIA with SparseGPT reconstruction.
* The paper also considers practical acceleration of sparse models in Table 5.

### Weaknesses
 * The observation that encouraging a more uniform sparsity pattern is beneficial was also made by Wanda, RIA seems to be an extension of that (also across columns). Similarly, that permutation reordering can be helpful for n:m sparsity was found by [Pool & Yu, 2021], this paper only introduces a simpler but more scalable heuristic for finding such a permutation, based on average activation values. While there is some novelty, it is not particularly high.
* For unstructured sparsity, the improvements of RIA over prior work are relatively small at around 0.1-0.2 points in perplexity. The impact of the more advanced linear sum assignment permutation method also seems rather minor. At the same time, perplexity increases from the dense baseline are still quite large, especially for 2:4. Hence, it is not clear how useful the corresponding sparse models would be in practice.
* There does not appear to be any code in the Supplementary. I hope the authors plan to open-source their work to aid reproducability.

### Questions
* How does 4:8 perform with channel permutations in the setup of Table 3?
* Did you carry out any additional ablation studies around parameter a other than Table 2? I am curious if a = 0.5 is generally the sweet spot or if it was just picked for simplicity.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a post-training N:M pruning solution for LLMs. The method is built upon two components: (1) relative importance and activation, which considers both the weights and activations within LLMs for a better weight importance estimation; and (2) channel permutation, which can better preserve important weights under n:m sparsity through rearranging channel orders. Experiment results demonstrate the effectiveness of the proposed method and its superiority over existing baselines.

### Strengths
1. The channel permutation and the Hungarian algorithm are novel techniques, and the experiments demonstrate the effectiveness under n:m sparsity
2. The paper is easy to follow, and the authors conduct extensive experiments.

### Weaknesses
1. The first technique, relative importance, and activation, seems to be an incremental improvement. 
2. In Section 5.3, which discusses N:M sparsity, I was anticipating experimental results on smaller LLMs such as Llama2-7b, and a higher sparsity ratio than 50%. This would potentially highlight the advantages of the proposed method over SparseGPT and Wanda more effectively. Could the authors provide their insights on this?
3. Regarding the inference latency under n:m sparsity, I would like to suggest that instead of providing layer-wise speedup, the authors could consider providing end-to-end latency for the pruned LLMs. My reason for this suggestion is that I am curious about whether n:m sparsity is indeed an effective structured pruning pattern within LLMs, especially when compared to pure structured pruning methods such as LLM-Pruner. Could the authors provide their perspective on this?

### Questions
Please refer to the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
