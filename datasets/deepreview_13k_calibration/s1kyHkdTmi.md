# An Evolved Universal Transformer Memory

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Prior methods propose to offset the escalating costs of modern foundation models by dropping specific parts of their contexts with hand-designed rules, while attempting to preserve their original performance.
We overcome this trade-off with \implname (\implacro), introducing a learned network for memory management that improves \textit{both} the performance and efficiency of transformers.
We \textit{evolve} \implacro atop pre-trained transformers to provide different latent contexts focusing on the most relevant information for individual layers and attention heads.
\implacro are universally applicable to any model using self-attention as they condition exclusively on the values in the produced attention matrices. 
Learning \implacro on a small set of problems, we achieve substantial performance improvements across multiple long-context benchmarks while cutting the model's input contexts up to a fraction of the original sizes. %
We show the generality of our conditioning enables zero-shot transfer of \implacro trained \textit{only} on language to entirely new transformer architectures even across input modalities, with their benefits carrying over to vision and reinforcement learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
They propose a learned strategy for maintaining the size of your KV cache. An auxiliary model utilizes the attention map to produce a score of how important each key-value pair is for predicting future tokens. This model is small (1-layer transformer). They train this auxiliary model using the attention maps of Llama 3 8B for long-context language tasks, but show that this auxiliary model is compatible with other models (Llama 3 70B) and can transfer to other modalities (video). The KV cache management reduces the memory of the cache, but performance does not decrease by much, sometimes improving upon using the full cache.

### Strengths
The algorithmic design seems sound and seems to perform well based on their results. It’s interesting that the auxiliary model can then transfer to other models and modalities. I liked some of their ablation studies, such as showing that NAMM drops more tokens from later layers than earlier layers. This seems to imply that there is much more to learn from attention scores than what manually-designed algorithms do.

### Weaknesses
There are a couple problems with the paper presentation (missing citations) + rigor of their experiments. I highly recommend that these problems are addressed for the score to be raised.


There are some problems with the flow of the paper due to many of the details being relegated to the Appendix.
- The related works paragraph in the main body is a bit too short, and poses NAMM to be the first method to propose a learned black-box strategy. However, previous works already do this. For example, Pyramid-BERT [1] does exactly that, and DMC [2] proposes a continual pre-training objective.
- Please include limitations of the method in the main body or refer to the Appendix section where you do somewhere.
- Limitations should also address the computational complexity of this method. How slow is NAMM compared to other methods?
- There should be an algorithm block in the main body detailing exactly how NAMM is used during inference. The written description is too vague. Especially include details such as the 512-chunking that is detailed in the Appendix.
- There are no details of exactly how the auxiliary model is trained in the main body or the appendix, except for a sentence mentioning that the auxiliary model optimizes the performance of 3 benchmarks. Please detail the exact objective somewhere.


Weaknesses in experiments:
- They should report the computational complexity of NAMM, how much longer is it to do inference using NAMM versus other baselines? In other words, how expensive is it to generate scores from the auxiliary model for each attention layer?
- A result that they particularly emphasize in this paper is that models do better on long-context benchmarks with NAMM cache management over utilizing the full KV cache. That makes sense, the auxiliary model seems to pick out the most important tokens as the aux model is _trained on long-context benchmarks itself_. However, I worry that the significance of these results is not rigorously tested and may simply be because they do not use any fine-tuning strategy to adapt the  base model to long-context tasks, as it is standard to do in practice.
  - All the reported results apply NAMM on top of a Llama-3-8B model that they adapt to use long-context using “NTK-aware positional interpolation,” a zero-shot method that can be found in a Reddit post. I am not aware of the validity or the limitations of this approach. They should also apply NAMM on top of standard long-context models already out there, such as Mistral 7b with 32k context. Does NAMM still do significantly better?
   - NAMM is only compared against L2 and H2O, but it should also compare against other finetuning strategies e.g. DMC, and strategies that also utilize the attention scores explicitly such as FastGen [3].
- The degree to which each baseline prunes the KV cache varies significantly, so it is hard to tell whether NAMM has better performance on benchmarks simply because it does not prune the cache to the degree the other baselines do. It would be good to actually control the hyperparameters of each method, such as the threshold at which a key-value pair is pruned, such that performance between methods is compared for some fixed cache size. Ideally, there should be a plot depicting this with x axis as cache size and y axis as performance.

### Questions
1. Paper seems to imply they transform the attention map after applying the causal mask. Is this true? If so, what is STFT doing exactly? Is it doing anything meaningful? 
2. How important is it to use the  fourier transformation to the signals instead of the original attention map?
3. I found the intuition for the gradient analysis section fairly confusing, and I am not sure what the takeaway is or why the quantities they measure matter. I wish this was better motivated, or it could be moved to the Appendix.

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
4

### Summary
Transformers are known to suffer from quadratic memory blow-ups. This paper attempts to make Transformers more efficient by using Neural Attention Memory Models (NAMMs). This involves pruning the KV cache memory using NAMMs.

### Strengths
1. The idea behind the contribution is simple and easy to understand.
2. NAMMs can be zero-shot transferred to other Transformers, which is quite interesting.
3. The benchmarks are diverse (but not comprehensive as discussed in weakness 2).

### Weaknesses
1. Pruning is lossy, meaning that it results in losing some of the information in the KV cache memory. For example, during the pruning process, you may very well discard information that the model could have found useful later on. This is a fundamental limitation of any pruning-based approach, as the discarded information could potentially be critical for downstream tasks. The risk is particularly high when the pruning strategy is not perfectly aligned with the model's information needs, which is difficult to achieve in practice. For instance, if the model relies on specific tokens in the early context to resolve ambiguities later in the sequence, pruning those tokens could lead to significant performance degradation. The challenge lies in identifying which tokens are truly redundant and which are essential for maintaining model accuracy.
2. KV cache memory pruning (more broadly KV cache management) has been investigated in the last couple of years, and while the authors compare against some of them, like H2O and L2, they do not discuss or compare against some of the other relevant work. Some of the relevant work (in language modelling) include:
   - Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs, ICLR 2024
   - CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving, SIGCOMM 2024

I appreciate that comparing against so many related works can be cumbersome. However, it is crucial that the authors discuss the related work and either compare their work against them or discuss why they are not comparable.

### Questions
Please see the weaknesses.

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
The paper proposes Neural Attention Memory Models (NAMMs), a network learned via evolution (CMA-ES) that can be applied to Transformers, reducing the number of tokens needed (KV-cache) at inference time. 
Results show that NAMMs outperform recent methods for pruning the KV-cache and occasionally improves the performance of the base model.

### Strengths
The performance gains using NAMMs over H2O are significant. 

Improving the performance using NAMMs over the base model is impressive.

### Weaknesses
H2O has some advantages over NAMMs. Notably, H2O does not require any new training. In contrast, NAMMs are trained using evolution. As such, NAMMs may require significantly more compute. The paper, however, lacks information regarding the computational resources needed by the method.

Furthermore, in practice, we care about the cache size and inference computational complexity. It is unclear how (1) the performance of NAMMs fare when varying the cache size and (2) the complexity (runtime and memory) of applying NAMMs at inference time.

Several details are missing to understand if the idea will generalize to other models. In this paper, only Llama 3 8B was considered. However, in contrast, the H2O paper considered several architectures (e.g., OPT, LLaMA, and GPT-NeoX), showing their idea generalizes across architectures. However, in this case, it's unclear how NAMMs performance will generalize across different language models. 

The results on Decision Transformer (DT) are odd considering that several papers (e.g., the original DT and Online DT papers) showed results that are significantly better than what is reported in Table 7. 

Benchmarks in the paper are mentioned by name (e.g., Long Bench, InfiniteBench, LongVideoBench, MLVU, D4RL etc...) without concrete details (e.g., types of tasks in the benchmarks' datasets). It is unclear to readers who are unfamiliar with the various fields.

### Questions
The cache size is important for complexity. However, in practice, what we actually care about is the empirical runtime and memory complexities. What is the runtime and memory needed to process new tokens compared to that of the baselines (e.g., H2O)?

Evolution is typically expensive to train using. What are the computational resources used to train NAMMs in terms of the runtime and memory?

Considering that language models get significantly larger than 8B, it is important that the idea generalizes to larger settings. How would the resources needed to train and perform inference scale with the size of the base models?

When pruning, the size of the cache size affects the performance significantly. In practice, we may want to select an optimal cache size that trades off performance and computational resources. In this paper, only 1 cache size was chosen for each dataset. How was this cache size determined for each model? And why are the results reported for only a single cache size? 

Relatedly, in H2O, plots are shown with the x-axis being the cache size (ratio) and y-axis being the performance. As a result, we can see the performance trade-off with respect to the cache size. Could you elaborate on why the results were not shown the same way? And could you include these plots?

Could you include details in the Appendix regarding the various datasets (e.g., Long Bench, InfiniteBench, LongVideoBench, MLVU, D4RL etc...)?

The paper runs experiments on D4RL using Decision Transformers. However, the reported results are significantly worse than what is reported in many papers (e.g., original DT paper, Online DT, Aaren, etc..). Could you elaborate on why this is the case? Could you add details regarding the experimental setup that resulted in these numbers?

For the LongBench results, the overall numbers are reported as "All tasks". However, a subset of the tasks are used for training NAMM. Reporting "All tasks" seems unfair for evaluating generalization. Instead, could you report separate aggregate scores for (1) the tasks used in training and (2) the held-out tasks not used in training, to more clearly show generalization performance."



Interestingly, using NAMM improves over even the base model in several cases. What is your intuition as to why there's such a large improvement in some cases?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on optimizing the memory management of Transformers. The authors introduce the NAMMs (Neural Attention Memory models) method, which employs trainable parameters to learn the importance of token column vectors. By removing less important tokens, this approach reduces resource requirements and enhances efficiency. The effectiveness of the proposed method is validated through experiments conducted on multiple datasets.

### Strengths
1. The paper is well-structured with a clear logical flow, making it easy for readers to follow. Figures are appropriately placed alongside the relevant text, contributing to a harmonious overall layout. The experimental results are effectively highlighted and processed, allowing readers to easily grasp the key points. This is a significant strength of the paper.

2. The NAMMs method proposed in the paper achieves a reduction in model parameter size, which facilitates training.

3. The architecture introduced by the authors is straightforward and easily reproducible. Extensive experiments have been conducted to substantiate its effectiveness, further validating the claims made in the paper.

### Weaknesses
1 My understanding is that the method involves the fusion of column vectors for all tokens (3.1 169）. However, if the dimensionality is too high, could this lead to substantial additional computational time? Please provide some computational complexity analysis or empirical runtime comparisons. Specifically, how does the computational cost of the STFT and EMA operations scale with the input sequence length and the dimensionality of the attention vectors? It is important to understand if these operations introduce a bottleneck, especially for very long sequences.

2 Removing tokens with importance scores <0 implies that the number of removed tokens may vary each time. How can the consistency of dimensions be guaranteed? Without consistent dimensions, subsequent training would be impossible. Does this require an additional constraint? I feel this point was not clearly explained in the paper. (How is the following issue implemented？)
 a.How they handle varying numbers of removed tokens in practice
 b.If there are any mechanisms to ensure dimension consistency
 c.Whether any additional constraints are used. The paper needs to clarify how the model handles the dynamic nature of the KV cache size after token removal. Does the model dynamically adjust its internal structures, or are there padding or masking techniques used to maintain consistent tensor shapes during training and inference?

3 In my understanding, compression is performed before assessing the importance of tokens. Would it be possible to compare the effects without compression? It seems that compression also has its advantages. Please conduct an ablation study specifically comparing performance with and without the compression step. It's crucial to understand the individual contributions of the compression step and the token selection mechanism. An ablation study should isolate the impact of each component on the final performance. For example, what is the performance if the raw attention values are directly used for token importance scoring, without any compression?

4.Could you list specific learning rates, parameter settings, and other details? Publishing the experimental code would also be beneficial. (Please provide the following materials.)
 a.A table of hyperparameters used for each experiment
 b.Any details on hyperparameter tuning processes
 c.Information on where to access their code or if they plan to release it This would give readers a clearer picture of how to reproduce the results. It is essential to provide a complete set of hyperparameters, including those for the STFT and EMA, along with the optimization algorithm used for training the NAMMs. Details on the search space and the tuning strategy are also needed.

### Questions
1 Removing tokens with importance scores <0 implies that the number of removed tokens may vary each time. 

 2.How can the consistency of dimensions be guaranteed? Without consistent dimensions, subsequent training would be impossible. 

3.Does this require an additional constraint? I feel this point was not clearly explained in the paper.

4.In my understanding, compression is performed before assessing the importance of tokens. Would it be possible to compare the effects without compression? It seems that compression also has its advantages.

5.Could you list specific learning rates, parameter settings, and other details? Publishing the experimental code would also be beneficial.

### Soundness
2

### Presentation
3

### Contribution
3
