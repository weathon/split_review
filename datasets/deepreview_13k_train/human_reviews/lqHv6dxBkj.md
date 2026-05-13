# SLoPe: Double-Pruned Sparse Plus Lazy Low-Rank Adapter Pretraining of LLMs

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
We propose \ours, a Double-Pruned \underline{\textbf{S}}parse Plus Lazy \underline{\textbf{{Lo}}}w-rank Adapter \underline{\textbf{P}}r\underline{\textbf{e}}training method for LLMs that improves the accuracy of sparse LLMs while accelerating their  pretraining and inference and reducing their memory footprint.
Sparse pretraining of LLMs reduces the accuracy of the model, to overcome this, prior work uses dense models during fine-tuning.
\ours improves the accuracy of sparsely pretrained models by adding low-rank adapters in the final 1\% iterations of pretraining without adding significant overheads to the model pretraining and inference. In addition, \ours uses a double-pruned backward pass formulation that prunes the transposed weight matrix using N:M sparsity structures to enable an accelerated sparse backward pass.
\ours accelerates the training and inference of models with billions of parameters up to $\trainspeedup\times$ and $\inferencespeedup\times$ respectively (OPT-33B and OPT-66B) while reducing their memory usage by up to $\trainmemory\times$ and $\inferencememory\times$ for training and inference respectively.\footnote{Code and data for \ours is available at: \url{https://bit.ly/slope-llm}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces SLOPE, a novel pretraining method aimed at improving the efficiency of large language models (LLMs) by combining sparsity and low-rank approximations. SLOPE employs double-pruning techniques—applying N:M sparsity masks during both forward and backward passes—and introduces lazy low-rank adapters in the final training stages. The double-pruning approach reduces memory and computational overheads, while the lazy low-rank adapters help maintain model accuracy by mitigating the quality loss from sparsity.

### Strengths
1. This is a technical solid article that designs optimized CUDA kernels that jointly optimize Nvidia 2:4 sparse kernels and low-rank calls through efficient tiling and scheduling.

2. SLOPE yields up to 1.25x faster training and 1.54x faster inference on models with billions of parameters, with a memory reduction of up to 63% during training.

### Weaknesses
1. Structured and semi-structured sparsity with low-rank adapters, are not new concepts in the literature (e.g., see Losparse [1]).

2. This article lacks an introduction to related work and baseline methods, such as FST. Readers unfamiliar with the field may find it challenging to follow the content.

3. Could you provide results on additional zero-shot datasets in GLUE beyond MMLU, ARC-c, and OpenBookQA for GPT-2 when comparing SR-STE?


[1] Li, Yixiao, et al. "Losparse: Structured compression of large language models based on low-rank and sparse approximation." In International Conference on Machine Learning, pp. 20336-20350. PMLR, 2023.

Minor: 
1. L 430 typo of "accuracy"

2. The bold values in the Tables are misleading:

Table 1: Why are some values of FST also bolded?

Table 3: Why are the values of SR-STE not bolded on the MMLU dataset?

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces double-pruned sparsity, a technique that applies two rounds of N:M sparsity to the weight matrices of a neural network: one for accelerated forward pass and another on the transpose of the already N:M sparse matrix for an accelerated backward pass. The proposed method is combined with LoRA-tuning in the final 0.01 iterations of pre-training resulting in the method termed Double-Pruned Sparse Plus Lazy Low-rank Adapter Pre-training (SLoPE). The authors use efficient tiling of upsample tensors and kernel fusion to reduce overhead, resulting in further boost in training and inference speed. They show that their approach results in speedup and memory reduction of pre-training LLMs of various sizes. They also show their method improves zero-shot accuracy of GPT2-small compared to a sparse pre-training baseline.

### Strengths
1-The proposed double-pruned N:M sparsity for both forward and backward acceleration offers a novel perspective on N:M
sparsity, improving flexibility compared to existing transposable N:M masks.

2-The tiling and kernel fusion solution that integrates LoRAs with sparse weights for enhanced efficiency is interesting.
The authors effectively demonstrate the acceleration and memory reduction benefits of their approach across various models, outperforming FST [1].

3- The method achieves performance surpassing SR-RTE[2] and approaches that of a densely pre-trained model in tasks like MMLU, Arch Challenge, and OpenQA.

[1] Accelerating Transformer Pre-Training with 2:4 Sparsity, Hu et all, ICML 2024

[2] Learning N:M Fine-grained Structured Sparse Neural Networks from Scratch, Zhou et. all, ICLR 2021

### Weaknesses
1- The most significant weakness is the limited evaluation of how the proposed sparsity impacts performance. The sparse pre-training method negatively affects performance, and the use of a static sparse matrix further limits flexibility. While the authors claim this does not hinder flexibility, more evidence across a broader range of downstream tasks is needed to support this claim. Given the inherent trade-off between speed and performance, the current experiments do not sufficiently demonstrate the method's effectiveness. Table 3 should include more tasks (tasks in FST[1]) to give the reader a clearer understanding of the impact.

2- Even in the limited downstream task evaluation, some important baselines are missing. The authors put FST in parentheses after SR-STE in the text, although these are distinct methods: FST refers to [1] while ST-RTE is [2]. Zero-shot FST results in their own setting on these tasks are not reported. Additionally, while comparing their method to a larger dense model may be unfair, it would be informative to see how a smaller dense model performs without sparse pre-training.

3- The impact of LoRA fine-tuning in the final iterations appears minimal. The benchmarks (MMLU, Arch Challenge, and OpenQA) are not reported for the LoRA ablations. Since a major contribution of this work is the tiling and kernel fusion solution designed to mitigate issues caused by adding LoRAs, it is concerning that adding LoRAs seems to have little effect, especially based on the current results.

### Questions
1-The authors show that their method is faster than FST during pre-training, which is expected since FST dynamically searches for a mask, whereas their method uses a static one, making the training column in Table 1 clear. However, the inference column of Table 1 suggests that their method is also faster than FST for inference. All sparse pre-training methods use the full model for inference. Does this imply that their method uses the sparse matrix for inference (e.g., during zero-shot evaluations)? Then what is the point of sparse pre-training? In the table caption, it’s mentioned that "the lack of inference speedup in FST is due to the final dense pre-training during the final iterations, resulting in a dense model for inference." Could the authors clarify if you have included fine-tuning on a downstream task as inference? and how are the SLOPE values in the inference columns calculated?

2-Is flash attention used for the baselines as well (line 312)?

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
4

### Summary
This paper proposes SLoPE, a Double-Pruned Sparse Plus Lazy Low-rank Adapter pretraining method that improves the accuracy and accelerates training and inference of sparse LLMs. By incorporating a low-rank adapter during the final 1% of pretraining iterations, the model accuracy is well maintained. Experimental results show that the proposed method significantly speedups in both pretraining and inference phases and efficiently reduces memory footprint.

### Strengths
1. The authors propose a double-pruned backward pass to improve model quality and reduce mask search overhead. They introduce additional low-rank adapters in the final 1% iterations of pretraining and improving model capacity.

2. The paper is well-written and easy to follow up. The finding of adding low-rank adapter in the last 1% iterations achieving better performance is interesting!

### Weaknesses
1. Why does introducing additional zeros in an N:M pattern during the computation of the input gradient in the backward pass of the first 99% of iterations not severely affect accuracy? Specifically, how does the dynamic change of zero locations across iterations ensure convergence to the original input gradients, and what is the theoretical basis for this convergence? What are the limitations of this approach, especially if the pruning pattern is not truly random across iterations?

2. The memory footprint for the pretraining should be higher than for inference, so why are the memory footprint reduction multiples similar? In the backward pass, calculating weight gradient involves a dense computation. While double-pruning reduces the computation of input gradients, the overall memory reduction should be more substantial. It is unclear how the additional memory overhead of storing transposed weights and binary masks during pretraining is accounted for in the reported memory savings. A more detailed breakdown of memory usage during both pretraining and inference is needed to justify the reported savings.

3. As discussed in section 2.2, the authors introduce a hyperparameter to balance the memory footprint, computational efficiency, and model quality. In the experiments on the effects of low-rank adapters, ranks are set to 4,16, and 64. Why weren’t larger ranks used? Since the low-rank adapter is only applied in the final 1% of iterations, the computational overhead should be minimal. What is the relationship between the rank of the adapter and the final model performance, and is there a point of diminishing returns?

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
3
