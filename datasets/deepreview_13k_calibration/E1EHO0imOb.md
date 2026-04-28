# Scaling FP8 training to trillion-token LLMs

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
We train, for the first time, large language models using FP8 precision on datasets up to 2 trillion tokens --- a 20-fold increase over previous limits. Through these extended training runs, we uncover critical instabilities in FP8 training that were not observable in earlier works with shorter durations. We trace these instabilities to outlier amplification by the SwiGLU activation function. Interestingly, we show, both analytically and empirically, that this amplification happens only over prolonged training periods, and link it to a  SwiGLU weight alignment process. To address this newly identified issue, we introduce Smooth-SwiGLU, a novel modification that ensures stable FP8 training without altering function behavior. We also demonstrate, for the first time, FP8 quantization of both Adam optimizer moments. Combining these innovations, we successfully train a 7B parameter model using FP8 precision on 256 Intel Gaudi2 accelerators, achieving on-par results with the BF16 baseline while delivering up to a $\sim 34 \%$ throughput improvement.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents new findings and addresses key challenges in large-scale FP8 training for LLMs on modern hardware that supports FP8 operations. The authors identified that one major challenge in scaling FP8 training is the occurrence of sporadic, high-magnitude activations. They pinpoint SwiGLU as the main source of these extreme outliers, providing the novel insight that a weight alignment process during training leads to substantial SwiGLU activations (as discussed in Section 4.1). To address this issue and stabilize large-scale FP8 training, the authors propose a smooth-SwiGLU activation function. This approach prevents outliers in the quantization of inputs to the last linear layer with an efficient per-channel scaling for better parallelism.

### Strengths
1. The paper demonstrates opportunities and challenges in scaling FP8 training to trillion-token scale using LLaMA2 architecture. In particular, the authors identify that with SwiGLU (which is an important to contemporary LLMs), weight alignment issues can induce large-magnitude outliers and result in training stability issue that poses significant challenge for FP8's limited dynamic range.

2. Extensive experiment results are provided, showing the proopsed Smooth-SwiGLU training with FP8 optimizer (moment 1: E4M3,moment 2: E4M3) is able to converge to baseline FP16 training. 

3. Experiments show around 30% improvement in training throughput, which provides significant energy saving for large-scale training.

4. Paper writing and presentation are clear with well identified bottleneck and detailed solutions.

### Weaknesses
1. The paper has an extensive discussion about how feedforward SwiGLU affect FP8 training stability. However, there is no mention about how other model components like RMSNorm, MHA/GQA affect training stability. Could the authors also discuss whether each of the other model components affect FP8 training stability and provide quantitative results? Specifically, it would be beneficial to see a breakdown of the contribution of each component to the overall instability, perhaps by selectively disabling FP8 quantization in different parts of the model and observing the impact on training convergence. This would help isolate the root causes of instability more precisely.

2. It seems the SwiGLU weight alignment issue explains the occurrence of huge-magnitude outliers. However, can the authors comment more on the sporadic nature of these outliers? Is SwiGLU held accountable for that as well? It's not entirely clear why these outliers appear only sporadically during training, and a deeper analysis of the conditions that trigger them would be valuable. For instance, do these outliers correlate with specific input sequences or training stages, and how does the weight alignment evolve over time to cause these sporadic events?

### Questions
I would like to ask the authors for several clarifications:

1. If I understand correctly, smooth-SwiGLU does not directly address the weight alignment problem. Rather, it is an alternative implementation specifically designed for FP8 training, which circumvents the overflow issue by preventing outliers in the inputs to the last linear layer. Is this accurate?

2. Figure 2 (b) on the dynamics of $\mathbf w_1$ and $\mathbf w_2$ norm correlation is insightful and interesting. Is the dynamics based on llama2's trianing hypermaraters? Do the authors have additional empirical results on how these dynamics change with different training hyperparameters?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel approach to training large language models (LLMs) using FP8 precision on datasets of up to 2 trillion tokens, revealing critical instabilities associated with FP8 training that were not observable in prior studies. It identifies that the SwiGLU activation function amplifies outliers over prolonged training, leading to instability. To mitigate this, the authors propose Smooth-SwiGLU, a modified activation function that maintains stability without altering performance. The paper also introduces FP8 quantization for both Adam optimizer moments, significantly improving memory usage and training throughput.

### Strengths
Very interesting findings!

The introduction of Smooth-SwiGLU and the quantization of Adam optimizer moments are significant advancements in the FP8 training methodology.

The paper provides thorough experimental results demonstrating the effectiveness of the proposed techniques, achieving comparable performance to BF16 with improved training throughput.

Successfully training models on datasets up to 2 trillion tokens sets a new benchmark for FP8 training, addressing scalability issues in LLMs.

### Weaknesses
While the findings are significant, their applicability to other model architectures beyond those tested (like LLaMA2) could be explored further.



### Questions
How do the results generalize to other activation functions beyond SwiGLU?

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
3

### Summary
This paper proposed a practical solution for quantized (FP8) training over trillion tokens.

The paper conduct LLM training over a real big 2 trillion dataset and found swiglu is the main cause of instability when training using FP8, thus proposed a optimized and smoothed method called smooth-swiglu.

Smooth-swiglu in together with FP8, the authors achieve good model convergence on 2 trillion token dataset for llm training

### Strengths
Training LLM on trillion-token big dataset makes the paper result solid.

Adopting a pure FP8 adam optimizer (both two momentum are fp8) and make training converge is good contribution. 

Identify swiglu cause model training instability and optimized as a smooth-swiglu is another contribution.

### Weaknesses
1 ) Paper novelty is limited. The only thing new is adding a scaling factor on top of swiglu may not be a big novelty. Previous work already study similar smooth method on activation functions. e.g., Swish, SMU as smooth function for relu.

[1] swish: https://arxiv.org/pdf/1710.05941

[2] SMU: https://arxiv.org/pdf/2111.04682

2 ) FP8 optimizer contribution is just extending previous 1 momentum using FP8 to both momentum using FP8 may lack a bit novelty here. For example, Figure 5 shows empirical study for both FP8 momentum on llama2 100m, it shows second momentum using E5M2 format achieve similar model loss curve as bf16. But how does it generalize to bigger models (more practical models like llama 8b 70b)? Is second momentum always need larger dynamic range rather than higher precision?

3 ) The only baseline is from this paper[3], how does this approach compared with nvidia transformer engine fp8. There is no comparison in either design or evaluation results. Please include a comparison with NVIDIA's Transformer Engine FP8 implementation, both in terms of methodology and empirical results. This comparison would provide valuable context for the paper's contributions.

[3]FP8-LM: Training FP8 Large Language Models

4 ) Billion level token training is almost sufficient for most LLM downstream tasks (e.g. Apple [4]). This trillion-token improvement may not have wide application scenarios. Please discuss more on potential use cases where trillion-token training might be beneficial, and how this paper's method scales compared to existing approaches at different dataset sizes.

[4] Apple Intelligence Foundation Language Models https://arxiv.org/pdf/2407.21075

### Questions
How does this paper compare with nvidia transformer-engine's fp8 training with automatic mixed precision?

In table 3, why micro batch is 1? The reason for doing quantization is to support larger batch training (higher throughput), if limiting to micro-batch as 1, it is almost impossible to get good throughput/token per sec numbers.

In table 4, deepspeed zero-1 itself would reducing some GPU memory footprint compared with pure pytorch DDP. Why use zero1 not 2 or 3?

In figure 6, why bf16 loss curve has more spikes compared with FP8 + Smooth-SwiGLU + FP8 Optimizer? to me, I think bf16 should have better and more smooth loss curve compared with any FP8 methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper 1) identifies instability issues in FP8 training for large language models (LLMs) on trillion-token-scale datasets, 2) links the root cause to the alignment of two weight matrices of the SwiGLU neuron, and 3) proposes Smooth SwiGLU to mitigate outliers in the activations. Smooth SwiGLU achieves this by applying scaling factors before and after the last linear layer of the MLP components. Furthermore, they compared different FP8 formats to obtain the best configuration for the FP8 optimizer. The method successfully stabilizes FP8 LLM training on trillion-token-scale datasets and delivers a 5.1% throughput improvement over the baseline on 256 Intel Gaudi2 accelerators.

### Strengths
1. The paper uses comprehensive experiments and analysis to link the instabilities in FP8 training to SwiGLU weight alignment.
2. The paper provides an efficient implementation of Smooth-SwiGLU.
3. The paper is well-written.

### Weaknesses
1. The motivation of Smooth SwiGLU is that "While disabling quantization of the SwiGLU output effectively prevents divergence, it reduces the potential acceleration benefits of FP8". However, "FP8 + Smooth SwiGLU" is only 5.1% faster than the "FP8 + SwiGLU output BF16". Given that the performance gap is relatively small and the experiments were conducted only on Intel Gaudi2, it would be helpful to compare the two variants on more hardware configurations (i.e., NVIDIA and AMD GPUs) to verify whether the performance gap persists. The reported 5.1% throughput improvement is marginal, especially considering the added complexity of the Smooth SwiGLU method. It is unclear if this small gain justifies the introduction of a new technique, particularly if the performance benefit does not generalize across different hardware platforms. The lack of results on other hardware architectures makes it difficult to assess the practical value of the proposed method.
2. Table 2 currently only compares the accuracy and perplexity between the proposed FP8 and the standard BF16 configurations. To provide a more comprehensive evaluation, it would be beneficial to include additional comparisons, such as 'FP8 + Smooth SwiGLU,' 'FP8 + SwiGLU output BF16,' and 'FP8 + SwiGLU output BF16 + FP8 Optimizer'. If evaluating these variants is challenging or unnecessary, please provide the corresponding discussion. The absence of these comparisons makes it difficult to isolate the impact of Smooth SwiGLU and the FP8 optimizer. Without these results, it's hard to determine whether the observed performance gains are due to the Smooth SwiGLU modification or the FP8 optimizer, or a combination of both. A more granular analysis is needed to understand the contribution of each component.

### Questions
When training larger models, do similar issues arise earlier or later?

### Soundness
3

### Presentation
4

### Contribution
3
