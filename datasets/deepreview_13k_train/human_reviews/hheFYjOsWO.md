# MC-MoE: Mixture Compressor for Mixture-of-Experts LLMs Gains More

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Mixture-of-Experts large language models (MoE-LLMs) marks a significant step forward of language models, however, they encounter two critical challenges in practice: \textbf{1)} expert parameters lead to considerable memory consumption and loading latency; and \textbf{2)} the current activated experts are redundant, as many tokens may only require a single expert.
Motivated by these issues, we investigate the MoE-LLMs and make two key observations: \textbf{a)} different experts exhibit varying behaviors on activation reconstruction error, routing scores, and activated frequencies, highlighting their differing importance, and \textbf{b)} not all tokens are equally important-- only a small subset is critical.
Building on these insights, we propose \textbf{MC-MoE}, a training-free \textbf{M}ixture-\textbf{C}ompressor for \textbf{MoE}-LLMs, which leverages the significance of both experts and tokens to achieve an extreme compression.
First, to mitigate storage and loading overheads, we introduce \emph{Pre-Loading Mixed-Precision Quantization (PMQ)}, which formulates the adaptive bit-width allocation as a Linear Programming (LP) problem, where the objective function balances multi-factors reflecting the importance of each expert. 
Additionally, we develop \emph{Online Dynamic Pruning (ODP)}, which identifies important tokens to retain and dynamically select activated experts for other tokens during inference to optimize efficiency while maintaining performance.
Our \textbf{MC-MoE} integrates static quantization and dynamic pruning to collaboratively achieve extreme compression for MoE-LLMs with less accuracy loss, ensuring an optimal trade-off between performance and efficiency.
Extensive experiments confirm the effectiveness of our approach. For instance, at 2.54 bits, MC-MoE compresses 76.6\% of the model, with only a 3.8\% average accuracy loss. During dynamic inference, we further reduce activated parameters by 15\%, with a performance drop of less than 0.6\%. Remarkably, MC-MoE even surpasses floating-point 13b dense LLMs with significantly smaller parameter sizes, suggesting that mixture compression in MoE-LLMs has the potential to outperform both comparable and larger dense LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposed two designs for efficient MoE inference: PMQ and ODP. PMQ conducts mix-precision quantization of experts, and ODP essentially prunes experts depending on certain critical tokens.

### Strengths
- MoE efficiency is a relatively under explored area in comparison to general, dense LLMs. This work is a welcomed addition.
- Two proposed designs are able to deliver decent task performance, especially for PMQ over BSP in Table 2.

### Weaknesses
 - The novelty of the proposed work is limited, as both mixed-precision quantization and token-dependent expert pruning are well-explored avenues for efficient MoE inference.
- Potential lack of baseline: BSP is the only truly relevant comparison to PMQ due to its mixed-precision approach. No pruning comparisons are provided for ODP.
- Most datasets used in Table 2 are common-sense intelligence tasks. Extensive literature across various fields has shown that such tasks (and ppl) are relatively robust and can achieve substantial compression gains. I would like to see more challenging tasks evaluated, such as GSM8k, HumanEval and LongBench.
- The efficiency evaluation seems somewhat rough. The registered speedup does not correspond to the featured task. I would like to see comprehensive reports on latency, throughput (across different tasks, compression rates, and batch sizes), and memory.

I also have a few formatting suggestions:
- Please consider adding highlights in Figure 3, as you have done in Figure 4. It is difficult to identify the discussion substance by reading coordinates on a small diagram.
- The LM-Eval column in Table 4 is not defined, though I understand it refers to the tasks in Table 2.
- Not that it matters much, but the authors may want to know that the proper way to use left and right quotation marks in LaTeX is `` and '', respectively. Currently, only right quotation marks are being used.

### Questions
-  I don't seem to find much connection between the PMQ and ODP part of the submitted work. Are they standalone to each other?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes MC-MoE, a training-free Mixture-Compressor for MoE-LLMs that applies the significance of experts and tokens to perform deep compression, incentivized by optimization space to improve upon memory consumption of expert heads' parameters and redundancies of activated heads. To alleviate saving and loading overheads, the authors devised the Pre-Loading Mixed-Precision Quantization stage for adaptive memory allocation. Following up with Online Dynamic Pruning (ODP) stage, this method dynamically selects significant tokens to elevate inference efficiency while maintaining model performance, achieving extreme compression.

### Strengths
1. Pre-loading is an intuitive yet effective method to cope with overheads in loading expert parameters.
2. This method leveraged the uneven features learned by different expert heads as guidance to optimize quantization effort with integer programming while providing valid expert significance analysis to defend the assumption.
3. This method introduced token relevance from the attention heat map to the criterion of parameter pruning, offering salient pruning instructions without utilizing external clues.

### Weaknesses
While this research adopts weight-only pruning, we encourage the authors to compare the effectiveness of other popular pruning methods in the second stage to demonstrate the weight-only pruning is sufficient and effective among all methods selected.

### Questions
While the performance scores of PMQ across benchmarks were mostly robust, those of ARC-c and MMLU were relatively meager. Would the authors like to provide an in-depth analysis of these two tasks, regarding potential challenges PMQ had on particular patterns/features?

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
4

### Summary
This paper introduces MC-MoE, a novel compression framework for Mixture-of-Experts (MoE) Large Language Models that combines static mixed-precision quantization with dynamic pruning. The approach consists of two main components: Pre-Loading Mixed-Precision Quantization (PMQ), which allocates different bit-widths to experts based on their importance, and Online Dynamic Pruning (ODP), which identifies and protects critical tokens while dynamically pruning less important experts during inference. Through extensive experiments, the authors demonstrate that their method can greatly compress the model without too much accuracy loss.

### Strengths
1. The proposed PMQ method innovatively considers multiple factors (activation reconstruction error, routing scores, and frequencies) in determining bit-width allocation.
2. The paper presents a comprehensive solution that addresses both static model compression and dynamic inference optimization.
3. The authors provide extensive empirical validation across multiple benchmarks and model sizes, demonstrating the method’s robustness and scalability.

### Weaknesses
1. The paper lacks ablation studies on the impact of different hyperparameters (μ threshold, protection ratio) on model performance.
2. The paper does not adequately address the potential compounding effects of quantization errors across multiple MoE layers, particularly in deeper networks where error propagation could be more significant.
3. The paper lacks a comprehensive error analysis to identify which types of tasks or linguistic phenomena are most affected by the compression techniques.
4. The computational overhead of the token importance calculation in ODP is not thoroughly analyzed, which could be significant for real-time applications.

### Questions
1. The authors do not provide sufficient analysis of the robustness of their compression method under different input sequence lengths, which is crucial for practical deployment scenarios.
2. The generalizability of the proposed methods to other MoE architectures with different routing mechanisms is not discussed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents MC-MoE, a training-free Mixture-Compressor for Mixture-of-Experts LLMs, which is designed to address memory consumption and redundancy challenges. MC-MoE combines Pre-Loading Mixed-Precision Quantization and Online Dynamic Pruning to compress MoE-LLMs. Wxperiments show that MC-MoE maintains high performance.

### Strengths
Conducts lots of experiments to verify the accuracy drop of the proposed method

### Weaknesses
My major conerns are the motivation and practical benefit of the proposed method:

1. What is the "metric" for measuring the speedup in Table 4? Is it latency or throughput? What is the input length and output length in your benchmark setting?

2. What is the target platform of the proposed method? Cloud or edge? The main advantage of SMoE models over dense models is that they scale better in term of computation [1]. Under the same "act." param. size, SMoE is better than the dense counterpart (but non-act. experts still take GPU HBM to store). Thus it is very important to carefully design the distributed inference infrastructure to translate the theoretical benefits of SMoE to real system benefts. For example in [1], it discussed the expert load balance, pipeline parallelism, and large batch size to keep GPU busy. I did not see the discussion of the side effects of mixed precision, since it will worse the load balance, especially when the number of experts is large. If your targeted use case is on the edge, what benefits does an SMoE model offer over a dense model?

3. In practical applications, it's extremely challenging to keep GPUs fully utilized. The techniques discussed in this paper—weight-only quantization and dynamic pruning—introduce irregular computation patterns. These irregularities lead to load imbalances across GPU cores, making it difficult to maintain GPU utility. Moreover, these methods tend to perform worse with larger batch sizes. However, using large batch sizes is essential in practice to achieve optimal performance with SMoE models [1]. Therefore, while these techniques aim to improve efficiency, they may actually hinder performance due to the introduced irregularities and their incompatibility with large batch sizes required by SMoE.

In single GPU setting, how did you serve MoE model? Do you use a "for loop" to iterate over all tokens for the same expert, then reshape to the original input?

I am questioning the motivation for using the MoE model in a resource-constrained environment. Generally, the running speed of an MoE model is approximately equivalent to that of a dense model that is twice its act. size—*but only if you have good system support* (like Mistral-8x7B versus Llama-2-13B), but at the cost of much larger model size. From your  profiling results, Mixtral 8*7b	 is even twice slower than a Llama-2-13B and much larger than it. Then why would I want to use it in the resource-constrained environment?

Also, comparing the accuracy of different models is irrelevant in the context of compression work. These models are trained on different datasets, so accuracy comparisons are not meaningful. For instance, if I were to use LLaMA-3.1-8B, it would likely outperform Llama-2-13B.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
