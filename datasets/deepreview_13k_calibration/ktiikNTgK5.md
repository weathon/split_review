# Compresso: Structured Pruning with Collaborative Prompting Learns Compact Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
\vspace{-2ex}

Despite the remarkable success of  Large Language Models (LLMs), the massive size poses significant deployment challenges, particularly on resource-constrained hardware. While existing LLM compression methods focus on quantization, pruning remains relatively unexplored due to the high cost of training-based approaches and data collection challenges. One-shot pruning methods, although cost-effective and data-free, have become dominant in LLM pruning, but lead to performance decline under the structured pruning setting. 
In this work, we introduce a new paradigm for structurally pruning LLMs, called \textit{{\sysname}}. Our approach, through the collaboration of the proposed resource-efficient pruning algorithm and the LLM itself, learns optimal pruning decisions during the training process. {\sysname} addresses the challenges of expensive training costs and data collection by incorporating  Low-Rank Adaptation (LoRA) into the $L_0$ regularization during the instruction tuning process. Then, we further augment the pruning algorithm by introducing a \textit{collaborative prompt} that fosters collaboration between the LLM and the pruning algorithm, significantly boosting the overall performance.  To this end,  {\sysname} prunes LLaMA-7B to 5.4B, maintaining original performance and even surpassing LLaMA-7B in reading comprehension by 2.62\%. Extensive experiments demonstrate that  {\sysname} significantly outperforms one-shot pruning baselines across various sparsity ratios, achieving up to 2.21\%, 11.43\%, 7.04\%, and 4.81\% higher scores on the commonsense reasoning, reading comprehension, MMLU, and BBH benchmarks, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a one-shot structured pruning method, called Compresso, for Large Language Models (LLMs). Compresso incorporates Low-Rank Adaptation (LoRA) into the L0 regularization during the instruction tuning process, and it also fosters collaboration between the LLM and the pruning algorithm. The evaluation shows that Compresso outperforms LLM-Pruner on several datasets.

### Strengths
1. The writing is clear.
2. The authors evaluated 7 benchmarks to show that Compresso outperforms LLM-Pruner.

### Weaknesses
1. In Equation 3, what $d_h$ denotes is not explained;  Similarly, In Equation 5, what $\lambda1$ and $\lambda2$ denote is not explained.
2. Some references or empirical evidence is needed to support it is the common practice of setting l to -0.1, r to 1.1, and β to 2.
3. In Section 4, it would be better if the authors could provide some insights, rather than only listing the numbers.
4. Demonstrating the theoretical underpinnings of Compresso would greatly enhance the paper.
5. This paper claims that LLM-Pruner is the only LLM structured pruning work. However, this claim appears to be open to question. The related works [1-7] that structurally prune LLMs are not mentioned or compared.
6. There are some typos in the paper, e.g. “We introduce LoRA intro pruning in a novel manner. Formally”.

### Questions
1. Is it possible to compare Compresso with the related works (mentioned above)?
2. In Section 3.3, the authors claim that this paper introduces LoRA into pruning in a novel manner”. Can you explain the main difference between LoRA used in fine-tuning LLMs and the way used in pruning in this paper?
3. Although Compresso is a one-shot pruning method, can the performance of LLMs be improved if we do Compresso iteratively?
4. How to adjust the hyperparameters λ1 and λ2 using the AdamW optimizer? Can authors provide more details or an ablation study about that?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a structured pruning method for large language models (LLMs) named Compresso. The work leverages the LoRA to achieve efficient training-based pruning. The work adopts $L_0$ reparameterization to enable differentiable masks to be jointly optimized with learnable parameters. Moreover, the work tries to prune with the proposed prompt to enhance the pruning results. The experimental result shows that Compresso can prune LLaMA-7B to a 5.4B size while maintaining the performance on zero-shot commonsense reasoning and reading comprehension, as well as few-shot MMLU and BBH benchmarks.

### Strengths
- The writing is clear and easy to understand.
- This research focuses on structured pruning for Language Model Models (LLMs), which can reduce the cost of making predictions without requiring specialized hardware support.
- The research employs many techniques to make the training-based pruning effective and reduce its costs.

### Weaknesses
 - The work lacks novelty as many parts are taken from existing works such as LoRA and differentiable masks.
- The proposed collaborative prompt is interesting, but the empirical study fails to support it convincingly. The ablation study in Table 6 is inconsistent, and it is recommended to perform the Compresso without prompting on both training and inference. Additionally, the lack of analysis or discussion on collaborative prompts prevents readers from fully understanding it.
- The main experiment only includes one baseline, which makes the results less convincing.
- There needs to be more explanation or discussion of the performance improvement without post fine-tuning in Table 7.
- Equation 3 contains many undefined symbols and requires further clarification.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces Compresso, a novel method designed to prune models during the instruction tuning phase. The experiments conducted across various datasets demonstrate that Compresso outperforms existing pruning methods in Large Language Models (LLMs).

### Strengths
The paper is articulate and follows a clear, logical structure, making it accessible and easy to comprehend.
The integration of collaborative pruning prompts is a unique and innovative approach, distinguishing this work from existing pruning methods.

### Weaknesses
The baseline method utilized in this study fine-tunes the model using the Alpaca dataset, whereas this paper employs the GPT4-Alpaca dataset for fine-tuning, which is inherently more robust. Given the significance of the instruction tuning dataset's quality in LLMs, it is imperative for the authors to present performance metrics post-application of the GPT4-Alpaca dataset. 
Incorporating the system pruning prompt during the inference phase substantially increases inference costs. This discrepancy makes the comparison with traditional pruned models somewhat skewed and potentially unfair. The authors should provide a detailed analysis of the overhead introduced by the pruning prompt, including its impact on latency and throughput. Furthermore, the authors are encouraged to broaden their experimental scope to include other sparse patterns (e.g., unstructured and N:M sparse patterns) to further validate the efficiency of the pruning prompt. This is crucial to demonstrate the general applicability of the method across different pruning techniques. 
Minor Issues:
Certain assertions within the paper lack sufficient backing. For instance, the claim "To our knowledge, we are the first to apply instruction tuning to weight pruning"

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Main Contributions:
* Introduction of a new paradigm for structurally pruning Large Language Models (LLMs), named Compresso.
* Utilization of Low-Rank Adaptation (LoRA) and L0 regularization for resource-efficient training-based pruning.
* Development of a collaborative pruning prompt that fosters better communication between the LLM and the pruning algorithm, thereby enhancing performance.

Main Innovations:
* Low-Rank Adaptation (LoRA) in L0 Regularization: A resource-efficient method that addresses high training costs and data collection challenges by tuning learnable binary masks to decide whether to retain or prune sub-modules like heads, FFN dimensions, etc.
* Collaborative Pruning Prompt: Unlike existing approaches that treat the LLM as a passive entity subject to various compression algorithms, this prompt makes the LLM an active participant in the pruning process, resulting in improved performance.
* Automated Layer-wise Sparsity Ratios: Compresso learns optimal sparsity ratios across different layers, unlike one-shot pruning methods that use uniform sparsity.

Significance:
* Resource Efficiency: Addresses the critical challenge of deploying large models on resource-constrained hardware without sacrificing performance.
* Benchmarking: Sets a new standard in the pruning of LLMs by outperforming one-shot pruning methods on multiple benchmarks.
* Practical Applicability: The approach is particularly useful for applications requiring high-performance LLMs on resource-limited platforms, offering a balanced trade-off between size and performance.
* Enhanced Understanding: The collaborative prompt innovation also hints at the growing capability of LLMs to understand and adapt to complex operational instructions, opening avenues for more sophisticated, dynamic interactions between algorithms and models.

Setting:
* Dataset: GPT4-Alpaca
* Epochs: 7 (1 for fine-tuning, 5 for pruning, 1 for mask optimization)
* Optimizer: AdamW with initial learning rate 5e-5, batch size of 8
* Hardware: 4 Nvidia V100 GPUs
* Target Models: LLaMA-7B pruned to 5.4B, 5B, and 4.5B
* Evaluation: Zero-shot commonsense reasoning, Reading comprehension, and Few-shot learning

Main Results:
* Zero-shot Commonsense Reasoning: Compresso retains up to 96% of the original LLaMA-7B's performance.
* Zero-shot Reading Comprehension: Compresso pruned models outperform the original LLaMA-7B by up to 3.91%.
* Few-shot learning: Compresso significantly outperforms the baseline (LLM-Pruner) on MMLU and BBH benchmarks, retaining up to 87% of LLaMA-7B's capability.

Ablation Study:
* Dataset selection matters a lot for the performance of the pruned models.
In summary, Compresso demonstrates superior performance in pruning LLaMA-7B across zero-shot and few-shot benchmarks compared to the baseline LLM-Pruner.

Conclusions:
* Compresso effectively prunes the LLaMA-7B model down to 5.4B parameters while maintaining, or even enhancing, its original performance.
* Compresso outperforms one-shot pruning methods across various benchmarks like commonsense reasoning, reading comprehension, MMLU, and BBH.
* Training-based pruning methods like Compresso show promise in overcoming the limitations of one-shot pruning in the context of LLMs.

### Strengths
* High Retention of Performance: The pruned models retain a high percentage of the original LLaMA-7B's capability across multiple domains, such as commonsense reasoning and reading comprehension. This indicates that the pruning technique is highly effective without compromising performance.
* Versatility Across Domains: Unlike other works that only focus on specific tasks like perplexity or commonsense reasoning, this paper evaluates the pruned models across multiple domains. They examine zero-shot commonsense reasoning, reading comprehension, and few-shot learning capabilities, making the results more generalizable.
* Outperforms Existing Methods: The paper shows that their method, Compresso, consistently outperforms the existing structured pruning baseline (LLM-Pruner) in all aspects and settings. This includes zero-shot and few-shot evaluations.
* Efficiency: The method is efficient enough to be trained on 4 Nvidia V100 GPUs, which could be considered a relatively modest hardware setting for such large-scale models. This indicates that the method is not just effective but also practical.
* Impact of Pruning Data: The ablation study indicates that the choice of dataset for the pruning process can greatly impact the effectiveness of the technique. This adds a new dimension to the study of model pruning and could be a valuable insight for future research.

### Weaknesses
 * on-Existent Discussion on Limitations: While the paper does provide a robust set of experiments and results, there is a lack of discussion regarding the limitations of the proposed methods. Understanding the boundaries of the method's applicability is crucial for both academic and industrial settings. Specifically, the paper does not discuss the computational cost of the pruning process itself, which could be a limiting factor for very large models. Furthermore, the paper does not explore the sensitivity of the method to different hyperparameter settings, which could impact the reproducibility of the results.

* The ablation study indicates that the choice of dataset for the pruning process can greatly impact the effectiveness of the technique. Which also indicates that the pruned model might be not ideal for the data and use-cases not appeared in the instruction tuning process. The paper does not explore the potential for catastrophic forgetting of capabilities not present in the pruning dataset. This is a critical concern, as the pruned model might lose its ability to perform tasks that were not part of the instruction tuning dataset.

* clearly description of which parts are pruned are expected. The paper lacks a detailed analysis of the specific architectural changes resulting from the pruning process. While the overall parameter reduction is mentioned, the paper does not provide a layer-by-layer breakdown of which attention heads and FFN dimensions are pruned. This makes it difficult to understand the impact of pruning on the model's internal representation and limits the ability to generalize the findings to other models.

### Questions
* if the choice of dataset for the pruning process can greatly impact the effectiveness of the technique as the ablation part indicates in this manuscript, then is the pruning still meaningful in LLMs, given that the instruction tuning dataset might always be insufficient?

* clearly description of which parts are pruned are expected. And how much acceleration benefit can be derived from the proposed pruning algorithm?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
