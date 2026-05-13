# Dynamic Low-Rank Sparse Adaptation for Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 3, 3

## Abstract
Despite the efficacy of network sparsity in alleviating the deployment strain of Large Language Models (LLMs), it endures significant performance degradation. Applying Low-Rank Adaptation (LoRA) to fine-tune the sparse LLMs offers an intuitive approach to counter this predicament, while it holds shortcomings include: 1) The inability to integrate LoRA weights into sparse LLMs post-training, and 2) Insufficient performance recovery at high sparsity ratios. In this paper, we introduces dynamic $\textbf{Lo}$w-rank $\textbf{S}$parse $\textbf{A}$daptation $\textbf{(LoSA)}$, a novel method that seamlessly integrates low-rank adaptation into LLM sparsity within a unified framework, thereby enhancing the performance of sparse LLMs without increasing the inference latency. In particular, LoSA dynamically sparsifies the LoRA outcomes based on the corresponding sparse weights during fine-tuning, thus guaranteeing that the LoRA module can be integrated into the sparse LLMs post-training. Besides, to achieve the optimal sparse model architecture, LoSA leverages Representation Mutual Information (RMI) as an indicator to determine the importance of layers, thereby dynamically determining the optimal layer-wise sparsity rates during fine-tuning. Predicated on this, LoSA adjusts the rank of the LoRA module based on the variability in layer-wise reconstruction errors, allocating an appropriate fine-tuning for each layer to reduce the output discrepancies between dense and sparse LLMs. Extensive experiments tell that LoSA can efficiently boost the efficacy of sparse LLMs within a few hours, without introducing any additional inferential burden. For example, LoSA reduced the perplexity of sparse LLaMA-2-7B by $\textbf{68.73}$$\downarrow$ and increased zero-shot accuracy by $\textbf{16.32}$%$\uparrow$, achieving a $\textbf{2.60$\times$}$ speedup on CPU and $\textbf{2.23$\times$}$ speedup on GPU, requiring only $\textbf{45 minutes}$ of fine-tuning on $\textbf{a single}$ NVIDIA A100 80GB GPU. Code is available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces LoSA (dynamic Low-rank Sparse Adaptation), a novel method for fine-tuning sparse Large Language Models (LLMs). LoSA addresses the performance degradation often observed in sparse LLMs by integrating low-rank adaptation (specifically inspired by LoRA) directly into the sparsity process.  It does so by dynamically sparsifying the low-rank adaptation outcomes to ensure compatibility with the sparse LLM weights and enable merging post-training.  Furthermore, LoSA uses Representation Mutual Information (RMI) to dynamically adjust layer-wise sparsity rates and allocates the rank of low-rank adaptation based on layer-wise reconstruction errors.  Experiments on various LLMs (LLaMA variants, OPT, Vicuna) demonstrate that LoSA significantly improves perplexity and zero-shot accuracy compared to existing sparsity methods and LoRA, while maintaining inference speedup.

### Strengths
* Addresses a relevant problem: Performance degradation in sparse LLMs is a known issue, and LoSA offers a practical solution.

* Novelty: Integrating sparsification into the low-rank adaptation process and dynamically adjusting sparsity/rank based on RMI and reconstruction errors are novel ideas.

* Strong empirical results: The experimental results show consistent improvements across various LLMs and sparsity levels.

* Inference efficiency: LoSA preserves the inference speed advantages of sparsity by merging the adapted weights.

### Weaknesses
na

### Questions
1. Can you comment (qualitiatively) on the applicability of the mutual information based layer-sensitivity method to other compression techniques -- e.g., would it work for quantization, or if we were jointly quantizing and sparsifying?

2. You have a brief section on N:M sparsity, where you fix M=8. How easy is it to extend this to also determine the right value of M for different layers? Relatedly, any notes on smaller values of M (like M=4, found in Nvidia GPUs as 2:4 sparsity)?

3. Can you add more color to the cost of your proposed method during training (i.e., impact on training time). There is an annotation that it takes 48 seconds for LLama-2-7B. Can you clarify: (i) what is the relative contribution to the overall step time, (ii) if the computations are performed in every step (or less frequently like every k steps -- or if it is possible to do it less frequently).

### Soundness
3

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
4

### Summary
This paper propose an adaption method for fine-tuning a dense LLM resulting into a sparse LLM which is more powerful and faster. The proposed algorithm works on sparsity design and low rank allocation. Experiements are evaluated on LLaMA and OPT models to demonstrate the better model performance and faster inference speed while comparing with other method at the same sparsity rate.

### Strengths
1. reasonable motivation, studying the sparsification of LLM while applying LoRA. 
2. clear problem formulation and related work introduction at each subproblem. 
3. detailed and summarized pseudocode for connecting each step and explaining the overall algorithm. 
4. strong and promising experimental results on LLMs regarding both model performance and speedup.

### Weaknesses
1. the algorithm consists of many heuristics and is lack of step by step derivation, e.g., Eq. 7 and Eq. 9
2. some experiment details are missing and unclear.

3. section "RMI for Sparsity" with Eq. 2 and Eq. 3 are not used in the proposed algorithm which can confuse readers for their purpose. this paper could shorten this presentation. 
4. Eq. 7 has a hidden assumption that higher rank setting can help reduce reconstruction loss. According to Eq. 1, under current problem formulation, higher rank does not change anything given the sparsity mask M. Thus, the design of Eq. 7 is not useful. Similarly, this question also applies to Eq. 9. Why Eq. 9 is performed at each step and what happens if Eq. 9 became too large?
5. It is unclear how rank increase and decrease is implemented in practice. For example, if current rank is 3 and you want to increase to 4, do you initialize the additional vector randomly? if current rank is 4 and you want to decrease to 3, do you perform rank reduction by singular values magnitude (if you use svd)? 
6. It should be discussed the computation complexity. In particular, the sparsity mask computation can be slow. Given the algorithm is executed at each fine-tuning step, the overall computation time should be reported. 
7. Experiment result table report "SparseGPT with LoSA", while the Algorithm 1 input is dense weight of LLM. Which part of dense weight of SparseGPT you work on?
8. Which layer of LLM and weight matrix (Q,K,V, etc) you run experiment with?
9. What is the outcome of SparseGPT with LoRA? Does it become a dense LLM? If so, what does sparsity 50% mean for SparseGPT with LoRA?
10. Is there any guideline for setting fine-tuning steps? In Table 1, T=5, why 5 steps can be sufficient for completing LoRA training?

### Questions
1. section "RMI for Sparsity" with Eq. 2 and Eq. 3 are not used in the proposed algorithm which can confuse readers for their purpose. this paper could shorten this presentation. 
2. Eq. 7 has a hidden assumption that higher rank setting can help reduce reconstruction loss. According to Eq. 1, under current problem formulation, higher rank does not change anything given the sparsity mask M. Thus, the design of Eq. 7 is not useful. Similarly, this question also applies to Eq. 9. Why Eq. 9 is performed at each step and what happens if Eq. 9 became too large?
3. It is unclear how rank increase and decrease is implemented in practice. For example, if current rank is 3 and you want to increase to 4, do you initialize the additional vector randomly? if current rank is 4 and you want to decrease to 3, do you perform rank reduction by singular values magnitude (if you use svd)? 
4. It should be discussed the computation complexity. In particular, the sparsity mask computation can be slow. Given the algorithm is executed at each fine-tuning step, the overall computation time should be reported. 
5. Experiment result table report "SparseGPT with LoSA", while the Algorithm 1 input is dense weight of LLM. Which part of dense weight of SparseGPT you work on?
6. Which layer of LLM and weight matrix (Q,K,V, etc) you run experiment with?
7. What is the outcome of SparseGPT with LoRA? Does it become a dense LLM? If so, what does sparsity 50% mean for SparseGPT with LoRA?
8. Is there any guideline for setting fine-tuning steps? In Table 1, T=5, why 5 steps can be sufficient for completing LoRA training?

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
The paper proposes Dynamic Low-Rank Sparse Adaptation (LoSA). This framework enhances sparse Large Language Models (LLMs) by integrating low-rank adaptation (LoRA) into the sparsity framework with dynamically adjusted layer-wise sparsity rates and rank allocations. LoSA utilizes representation mutual information (RMI) to determine layer importance for sparsity and reconstruction errors to allocate ranks, which purportedly improves performance without increasing inference latency.  Experimental results demonstrate that LoSA achieves considerable gains in accuracy, perplexity, and inference efficiency across various architectures and sizes.

### Strengths
1.  LoSA introduces a combined dynamic sparsity and rank adjustment mechanism for fine-tuning sparse LLMs. Using RMI for layer-wise sparsity rate determination and reconstruction errors for rank allocation seems a reasonable approach for preserving model performance under sparse conditions. Moreover, trying to match the sparsity pattern of the adaptation path BA and the pre-trained weight W is novel. 
   
2. Comprehensive Empirical Evaluation: The paper’s experiments cover multiple architectures (LLaMA, Vicuna, OPT) and sizes, presenting results across different sparsity ratios. Performance improvements in both perplexity (Table 1) and zero-shot accuracy (Table 2) underscore LoSA’s adaptability across models and contexts, although some improvements at lower sparsity rates are modest.

3. Inference Efficiency: LoSA reportedly achieves significant inference speedups, which is crucial for deploying LLMs in resource-constrained environments. The throughput gains shown in Table 9 demonstrate LoSA’s potential in reducing inference latency compared to other sparsification methods, although these gains are achieved using specific sparse inference engines.

### Weaknesses
1. The paper lacks comparisons with adaptive LoRA methods like AdaLoRA and SoRA, which are critical for evaluating LoSA’s performance among recent dynamic rank approaches. Without these comparisons, LoSA’s relative advantage remains unclear. Furthermore, the experimental setup for comparison should be carefully considered, as simply applying existing methods to a different model size may not be sufficient. It is crucial to ensure that the hyperparameters for these baselines are optimized for the specific LLM size and sparsity level used in the LoSA experiments, rather than using default or previously reported settings from smaller models.

2.  The optimization setup in Eq. 5 (Section 2.2) assigns higher sparsity rates to layers with higher importance, which contradicts standard practices that seek to preserve the most important layers. This questionable logic may weaken the model’s representational power and suggest a potential flaw in LoSA’s sparsity allocation strategy. Specifically, the paper does not provide a clear justification for why the layers deemed more important by RMI should be pruned more aggressively. This approach could lead to a suboptimal trade-off between sparsity and performance, as the most informative layers are potentially being disproportionately affected.

3. The paper does not clearly explain how LoSA ensures consistency in sparsity across LoRA weights (BA matrices) and model weights (W matrices). Given the critical need for alignment in the sparse structure, the mechanism by which LoSA achieves this alignment is unclear, especially in the context of using SparseGPT or Wanda. This missing detail may complicate LoSA’s practical applicability. It is not sufficient to simply state that the same mask is applied; the specific implementation details of how this mask is generated and applied to both the base weights and the LoRA weights need to be clarified, especially considering the different shapes and dimensions of these matrices.

4. While some ablation studies are presented, further analysis is needed on the soundness and effectiveness of the RMI-based sparsity and reconstruction-based rank allocation across different architectures. The current ablation study does not sufficiently explore the sensitivity of LoSA to different architectural choices or hyperparameter settings. A more comprehensive analysis should include a wider range of model architectures and a systematic exploration of how the RMI and reconstruction error metrics behave under different conditions.

### Questions
1   - Could authors provide results comparing LoSA with adaptive LoRA baselines like AdaLoRA and SoRA? These comparisons would help clarify how LoSA performs relative to other dynamic sparsity approaches.

2- In Eq. 5, why is the sparsity rate set to increase with the layer importance score? This setup seems counterintuitive since it would sparsify important layers more, potentially impacting the model’s performance. Could you explain this choice and its implications?

3- How does LoSA ensure consistent sparsity patterns between the LoRA (BA) and LLM (W) weights? Does the method sparsify entire rows or columns to maintain this alignment, or is there another approach? Further detail would clarify how LoSA integrates with existing sparse methods like SparseGPT and Wanda.

4- It would be helpful if authors could also elaborate on the computational overhead introduced by the RMI and reconstruction error-based adaptations. Specifically, how does this additional computation scale with model size?

 5- Could authors also clarify the interpretability of RMI as a sparsity allocation metric? While the Information Bottleneck principle supports its use, it would be helpful to see additional justification or experiments demonstrating that RMI consistently aligns with real layer importance (e.g., gradient-based layer importance) across diverse architectures.

6- Given that LoSA’s speedups are measured using specific sparse inference engines (e.g., DeepSparse, nm-vllm), how generalizable are these results to other deployment environments?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an approach called "Dynamic Low-Rank Sparse Adaptation" (LoSA) that seeks to address the challenges of performance degradation associated with sparsifying LLMs. The paper introduces a unified framework that combines low-rank adaptation with sparsity, aiming to improve efficiency while maintaining model performance.

### Strengths
1. The paper offers extensive experimental results across various models (e.g., LLaMA-2, Vicuna, OPT) and datasets.

2. The authors provide an explanation of their methodology, from dynamic sparsification to adaptive rank allocation.

### Weaknesses
1. This paper ignores previous works [1-4] on sparse PEFT using Low-Rank Adaptation. I did not see any comparisons or discussions with previous similar works. It's extremely hard to tell if this work has enough contributions to the area since the author choose such narrow baselines (SparseGPT, Wanda).

2. Without through discussions with previous similar works, it's hard to judge the novelty of this work.

3. The author could also compare with some latest works of LLM post-training pruning works.

4. The improvements over baselines are incremental, some of them are very marginal.

### Questions
Please check the weakness. Please provide comprehensive experimental results and discussions.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces dynamic Low-rank Sparse Adaptation (LoSA), a method that integrates low-rank adaptation into LLM sparsity within a unified framework, thereby enhancing the performance of sparse LLMs without increasing the inference latency. In particular, LoSA dynamically sparsifies the LoRA outcomes based on the corresponding sparse weights during fine-tuning, thus guaranteeing that the LoRA module can be integrated into the sparse LLMs post-training. Besides, LoSA leverages Representation Mutual Information (RMI) as
an indicator to determine the importance of layers, thereby efficiently determining the layer-wise sparsity rates during fine-tuning. Predicated on this, LoSA adjusts the rank of the LoRA module based on the variability in layer-wise reconstruction errors, allocating an appropriate fine-tuning for each layer to reduce the output discrepancies between dense and sparse LLMs.

### Strengths
Extensive experiments tell that LoSA can efficiently boost the efficacy of sparse LLMs within a few hours, without introducing any additional inferential burden. For example, LoSA reduced the perplexity of sparse LLaMA-2-7B by 68.73 and increased zero-shot accuracy by
16.32%, achieving a 2.60× speedup on CPU and 2.23× speedup on GPU.

### Weaknesses
The novelty may be limited. This paper proposes three improvements including dynamic sparsity rates across layers with RMI, dynamic rank allocation, and progressive pruning. Theses ideas have been known to be effective for pruning. For example, [A1] atomically determines the   layer-wise sparsity ratio and [A2,A3] uses MI (and HSIC) in model pruning.  [A4,A5] investigates rank allocation. Progressive pruning has been commonly used in pruning and proved to be effective such as [A6,A7]. It mentions to merge sparse lora with sparse weights for actual acceleration. This idea is straightforward and [A7] already investigates sparse lora with sparse weights so that they can be merged. The adoption of RMI generally follows [Zheng et al., An Information Theory-inspired Strategy for
Automatic Network Pruning, 2021]. It seems to change the CNN model to LLMs with almost the same RMI method in [Zheng et al, 2021].  The technical contribution may be limited. It is better to highlight the unique contributions.

The baseline is not enough. The proposed method is a finetuning method. SparseGPT and wanda are PTQ methods without finetuning. It may not be fair to compare with  SparseGPT or wanda. The actual baseline only has lora. It may be better to compare with other finetuning based pruning methods for LLMs such as [A7], LLM-pruner or SliceGPT. Although most methods are structured pruning, it is easy to adapt the proposed method for structured pruning with such as wanda-sp of structured mask. It adopts multiple improvements and it is not surprising to be better than the naïve lora. It may be better to compare with related works focusing on pruning and finetuning LLMs.

The setting with  2:8 or mixed 2:8 sparsity may not be solid. The GPU compiler can accelerate a specific N:M sparsity such as 2:4. It may not be able to accelerate 2:8 or mixed 2:8 sparsity. The experiments for this part only demonstrate the accuracy performance. But the actual acceleration may be limited without the support from compiler.  It may be better to discuss  this setting.

The lora in the baseline finetunes the whole model so that the model is not sparse if merged. It may be a bit strange to compare between a dense model with lora and a sparse model with losa. It may be better to provide a new baseline such as SparseGPT + sparse lora or wanda + sparse lora. The sparse lora can be merged with the sparse model. It should be a more direct baseline with uniform sparsity rates and the same ranks in the merged model, in contrast to the dynamic sparsity and dynamic ranks. It may be more reasonable to compare the speed of this baseline and the proposed method as they are both sparse.

### Questions
see the weakness.

It is better to highlight the unique contributions. 

 It may be better to compare with related works focusing on pruning and finetuning LLMs. 

 It may be better to discuss  this setting. 

The baseline can be improved.

### Soundness
3

### Presentation
2

### Contribution
2
