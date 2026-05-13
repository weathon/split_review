# Training-Free Activation Sparsity in Large Language Models

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Activation sparsity can enable practical inference speedups in large language models (LLMs) by reducing the compute and memory-movement required for  matrix multiplications during the forward pass. 
However, existing methods face limitations that inhibit widespread adoption. Some approaches are tailored towards older models with ReLU-based sparsity, while others require extensive continued pre-training on up to hundreds of billions of tokens. 
This paper describes \oursmethod (\textbf{T}raining-Fre\textbf{e} \textbf{A}ctivation Sparsity in \textbf{L}LMs), a simple training-free method that applies magnitude-based activation sparsity to hidden states throughout the entire model. \oursmethod achieves 40-50\% model-wide sparsity with minimal performance degradation across Llama-2, Llama-3, and Mistral families, with sizes varying from 7B to 70B. We improve existing sparse kernels and demonstrate wall-clock decoding speed-ups of up to 1.53× and 1.8× at 40\% and 50\% model-wide sparsity. \oursmethod is compatible with weight quantization, enabling further efficiency gains. 
\vspace{-2mm}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors introduce TEAL, a training-free method for inducing activation sparsity in LLMs, achieving 40-50% sparsity with minimal performance loss and up to 1.8× speed-up in decoding. Unlike previous methods, TEAL works across all model layers, supports modern activation functions, and is compatible with quantization for additional efficiency.

### Strengths
- TEAL achieves high sparsity (40-50%) without retraining, resulting in faster execution (up to 1.8× speed-up) with minimal performance degradation.

- A range of experiments across various models and model sizes shows that TEAL consistently outperforms other methods, demonstrating its robustness and general applicability

- The proposed method is designed to work seamlessly with newer models that use modern activation functions like SwiGLU, making it applicable to the latest LLM architectures.

### Weaknesses
 - Although TEAL is adapted for compatibility with newer activation functions like SwiGLU, the core concept of magnitude-based pruning is similar to prior work, which may limit its perceived innovation and contribution.
- The paper does not mention whether the code is available for reproducibility.



### Questions
**1. Calibration Set vs. Evaluation Set for Pruning Decisions:**
 - If I understand correctly, the decision to prune specific activations in TEAL is based on a calibration set, with the assumption that this set is representative enough for generalization. However, is it possible that an activation deemed unimportant (and thus pruned) based on the calibration set might behave differently on a different dataset?
 - It appears that C4 is used as the calibration set, while WikiText is used for evaluation. How similar are these datasets in structure and distribution? If you were to repeat the experiment on a different evaluation dataset, would you still observe the same levels of performance degradation?

**2. Pruning Effectiveness in Highly Optimized Newer Models:**

- In line 298, could it be that newer models are using their capacity more fully, meaning that fewer activations are redundant and available for pruning? If so, does this suggest that newer architectures could achieve comparable complexity with fewer parameters, making further compression both unnecessary and less effective?
- In this scenario, how would TEAL still provide an advantage? Could you explain the benefits of TEAL for cases where newer models are already highly optimized?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel sparsification method called TEAL (Training-Free Activation Sparsity in LLMs) which aims to boost up inference speeds of a contemporary LLMs. It zeros out p-th layer-wise percentile of activations closest to 0 in all of the linear projection layers of the Transformer block. Specifically, it is catered to architectures with GeLU, SwiGLU and GeGLU activations (e.g. Llama and Mistral) which do not exhibit large level of natural sparseness, as opposed to older model families (e.g. GPT and OPT) with high sparseness induced by ReLU. The approach doesn't demand extensive fine-tuning or continual pre-training, as the sparsification is applied in online fashion to activations of the model during each forward pass. Only inexpensive greedy search over limited number of hyper-parameters is required to adapt the technique to a model.

The authors conduct experiments with several model families of different sizes, benchmarking speed, perplexity and reasoning abilities of models augmented with different degrees of TEAL activation sparsity. The results indicate that the method substantially increases inference  speeds while retaining good modeling and reasoning abilities of the models.

### Strengths
* The paper successively addresses an important and relevant applied  problem: how to speed up inference of **contemporary** and widely used architectures of LLMs such as Llama model family with no or minimal quality loss. 

* Suggested solution is conceptually simple, and authors supply custom Triton kernels which makes their method suitable for easy adoption.

* The paper is clear, legible and easy to follow. The results are solid, and the contribution is sound.

* The authors analyze and visualize activation distributions for recent and largely popular Llama-3-8B architecture which gives an intuitive ground for justifying not only their own online training-free activation sparsity, but also various other existing and future algorithms.

* The authors apply sparsity to all weight matrices in a Transformer block as compared to competing approach (CATS, [1]). TEAL induces greater overall sparsity with lesser degradation of performance. 

* The method is shown to work well in practice in conjunction with another extremely popular approach to accelerating the inference of LLMs: weight quantization.

[1] Donghyun Lee, Jaeyong Lee, Genghan Zhang, Mo Tiwari, and Azalia Mirhoseini. CATS: Context- aware thresholding for sparsity in large language models. In First Conference on Language Modeling, 2024.

### Weaknesses
1. It would be nice to include formal definitions to various matrices (such as $W_{up}$ and $W_{down}$) and layers (MLP, SwiGLU) which are referred to throughout the work.

2. There are no comparisons with structured and semi-structured pruning (e.g. Mask-LLM [1] which was originally evaluated on the same benchmarks with Llama-2 models). Overall, it would be intriguing and instructive to compare differences in quality/ speed, and trade-offs between the TEAL and unstructured/ semi-structured/ structured pruning, and active sparsity inducing algorithms. Specifically, the lack of comparison with semi-structured pruning techniques, which offer a balance between performance and hardware efficiency, is a notable gap. The paper should explore how TEAL's performance and speed compare to methods like 2:4 sparsity, which is gaining traction for its hardware acceleration potential.

3. In particular, comparison with fine-tuning free ReLUfication [2] seems to be a little bit unfair to the spirit of the method as it’s intended by the paper’s authors to be used with fine-tuning or continual pretraining. It would be nice to either completely discard this comparison in Table 1 or to replace it with a stronger baseline, such as full ReLUfication with fine-tuning.

### Questions
1. Line 107: Which recent work?

2. Could the authors please explicitly explain why activation sparsity error in figure 8 increases with the batch size? Does the algorithm nullify the activations independently across different samples of a batch or activations are zeroed according to some aggregate statistics?

3. It is mentioned in the paper that the efficient low-level Triton kernel is implemented based on Deja vu kernel [1]. Is it possible to apply that kernel directly to the task of sparsifying SwiGLU and GeGLU transformers, and if it is, how it fares against the proposed method in terms of quality?

4. The paper seems to imply but not to explicitly state that the result of (SiLU(xWgate ) ⊙ xWup is also sparsified. Are there any other places where activation sparsity is applied but not mentioned? 


[1] Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, and Beidi Chen. Deja vu: Contextual sparsity for efficient llms at inference time, 2023. URL https://arxiv.org/abs/2310.17157.

### Soundness
4

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
This paper introduces TEAL, a novel magnitude-based pruning approach to achieve activation sparsity in Large Language Models (LLMs). It focuses on LLaMA-architecture LLMs with SiLU-like activation functions, identifying activation sparsity patterns through a greedy search method that does not require continued pre-training. The experiments demonstrate that TEAL achieves comparable performance on both accuracy and inference speed.

### Strengths
- The paper provides a high-quality exploration of sparsity patterns in SiLU-like activations, which are widely used in modern LLMs.
- The greedy search-based solution presented is straightforward yet effective.
- The authors demonstrate the accuracy results on several common downstream tasks at various scales LLMs, and the end-to-end throughput experiments show the practical value of TEAL in certain scenarios.

### Weaknesses
 - While the main focus is on Llama-like LLMs, discussing the applicability of TEAL to other architectures, such as [Mixture-of-Experts](https://arxiv.org/abs/1701.06538) and [Mamba](https://arxiv.org/abs/2312.00752), would enhance the paper's scope. Specifically, the paper should address how the magnitude-based pruning would interact with the conditional computation in MoE layers, where different experts are activated based on the input. Similarly, for Mamba, it is unclear how the selective state space model would be affected by the proposed pruning method, given that the hidden states are recurrently updated.
- The paper lacks a detailed analysis of the memory footprint of the TEAL method, especially in long context scenarios. The analysis should include not just the memory required for storing the histograms and thresholds, but also any additional memory overhead during the pruning process itself, such as temporary buffers or intermediate results. Furthermore, the paper should discuss how the memory footprint scales with the model size and sequence length, and whether the memory overhead becomes a bottleneck for very large models or very long sequences.


### Questions
- In Figure 3 (right), why is the theoretical Latency higher than TEAL at small sparsity levels?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes TEAL, a training-free activation sparsification technique for Large Language Model (LLM) acceleration. Modern LLMs adopt more sophisticated activation functions in lieu of ReLU, thus their activations are no longer naturally sparse. TEAL is built upon the observation that the distribution of the inputs to the weight matrices closely follows either a Gaussian or Laplace distribution. The magnitude based sparsification follows, where the threshold is chosen by a block-level greedy optimization process based on the $\ell_2$ error. The whole process does not involve back propagation. The customized GPU kernel attributes the acceleration of LLMs on the NVIDIA A6000 and A100 GPUs.

### Strengths
1. The paper is well-written and easy to follow. The challenge is stated clearly and addressed properly.
2. The proposed method achieves meaningful progress on the activation sparsification of the non-ReLU functions in the training-free setting.
3. The sparsified models show actual throughput improvement on the widely used GPUs. Overall, the proposed scheme seems quite practical and can be easily adopted by others.

### Weaknesses
A couple of minor concerns are listed below. 
1. Although I understand that the paper focuses on the training-free scheme, providing a discussion and/or experimental results on fine-tuned sparse activation models could make the paper stronger and more interesting. Since a couple of baseline papers (CATS and Relufication) adopt training or fine-tuning steps in their pipelines, I am curious about how much improvement a simple fine-tuning method, such as parameter-efficient fine-tuning (e.g., LoRA), using a moderate number of tokens (possibly <100K), can bring to TEAL. If post-sparsification fine-tuning is prohibited due to the attributes of TEAL, this should be discussed in the paper.
2. The standard deviation of the sparsity by TEAL is not reported. Since the sparsity level changes from input to input, providing more statistical information can help in understanding the proposed method better.

### Questions
1. Are there any limitations or difficulties caused by TEAL when it comes to training or fine-tuning the sparsified model?
2. Does the Triton kernel need to be rewritten for different GPU architectures?
3. In Table 3, how was the inference speed tested? Was it tested on autoregressive text generation? If so, what are the lengths of the given and the generated text?
4. Does the sparsity level change based on the domain of the text (e.g., code, novel, scientific paper, etc.)?

### Soundness
3

### Presentation
3

### Contribution
3
