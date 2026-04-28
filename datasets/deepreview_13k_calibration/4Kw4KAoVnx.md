# Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
While fine-tuning large language models (LLMs) for specific tasks often yields impressive results, it comes at the cost of memory inefficiency due to back-propagation in gradient-based training. Memory-efficient Zeroth-order (MeZO) optimizers, recently proposed to address this issue, only require forward passes during training, making them more memory-friendly. However, compared with exact gradients, ZO-based gradients usually exhibit an estimation error, which can significantly hurt the optimization process, leading to slower convergence and suboptimal solutions. In addition, we find that the estimation error will hurt more when adding to large weights instead of small weights. Based on this observation, this paper introduces Sparse MeZO, a novel memory-efficient zeroth-order optimization approach that applies ZO only to a carefully chosen subset of parameters. We propose a simple yet effective parameter selection scheme that yields significant performance gains with Sparse-MeZO. Additionally, we develop a memory-optimized implementation for sparse masking, ensuring the algorithm requires only inference-level memory consumption, allowing Sparse-MeZO to fine-tune LLaMA-30b on a single A100 GPU. Experimental results illustrate that Sparse-MeZO consistently improves both performance and convergence speed over MeZO without any overhead. For example, it achieves a 9% absolute accuracy improvement and 3.5x speedup over MeZO.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Sparse-MeZO, a memory-efficient zeroth-order optimization (ZO) technique for fine-tuning LLM by selectively optimizing a subset of parameters, rather than all. Based on MeZO, Sparse-MeZO introduces a sparse mask that targets smaller, noise-resilient weights, thereby mitigating gradient estimation noise, improving convergence speed, and reducing memory usage. Key results demonstrate Sparse-MeZO’s efficiency, achieving faster convergence and improved performance over MeZO, with the ability to fine-tune models like LLaMA-30b on limited hardware resources (e.g., a single A100 GPU).

### Strengths
1. Incorporating sparsity and MeZO is an interesting direction for performance improvement. 

2. The paper offers good empirical validation, showing clear improvements over baseline methods across a range of fine-tuning tasks.

3. The paper is structured logically, making it easy to follow the motivation and methodology

### Weaknesses
1. The paper lacks details on how thresholds for selecting small-magnitude weights are determined, how they vary across tasks, and whether they require re-tuning for different settings. Specifically, the method for determining the threshold for 'small' weights is not clearly defined. It's unclear if a fixed threshold is used across all layers or if it's dynamically adjusted. The paper should specify whether the threshold is an absolute value or a relative percentile, and how this choice impacts performance. Furthermore, it is not clear if the threshold is a hyperparameter that requires tuning for different tasks and datasets.

2. It’s not clear if masking and selecting small-magnitude weights specifically benefit zeroth-order optimization more than generic fine-tuning (first-order methods). Since subset selection often improves generalization, it would be needed to evaluate this effect. The paper should include a comparison of the proposed masking strategy with first-order optimization methods to isolate the benefits specific to zeroth-order optimization. It is important to determine whether the performance gains are due to the masking strategy itself or the combination of masking and zeroth-order optimization.

3. There is no specific numbers regarding the computational overhead introduced by dynamic masking and threshold calculation. The paper should quantify the computational cost of generating the dynamic mask at each iteration, including the time for threshold calculation and mask application. This analysis should be compared to the computational cost of the base MeZO method to understand the trade-offs.

4. The motivation for why zeroth-order optimization particularly benefits from small-magnitude weights lacks enough theoretical or empirical support. An ablation study showing this effect more clearly would strengthen the argument. The paper should provide a more detailed analysis of why small-magnitude weights are more suitable for zeroth-order optimization, potentially through an ablation study that compares the impact of updating weights of different magnitudes.

### Questions
1. Could the authors clarify the computational cost associated with generating the dynamic mask at each iteration and how it compares to MeZO in practice? such as a wall-clock time wise comparison similar to Figure 1

2. How sensitive is Sparse-MeZO’s performance to the choice of layer-wise sparsity threshold, and what considerations guided the threshold selection?

3. Can you provide detailed threshold hyperparameters for reproducibility?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Sparse MeZO, a memory-efficient optimization method for fine-tuning large language models. By selectively applying zeroth-order updates to a carefully chosen subset of parameters, it reduces estimation errors inherent in zeroth-order methods. This approach improves both performance and convergence speed without increasing memory usage, enabling efficient fine-tuning of large models like LLaMA-30b on limited hardware resources.

### Strengths
- Interesting Idea: Proposes Sparse MeZO, selectively applying zeroth-order optimization to improve memory efficiency.- 
- Good Performance: Achieves significant gains in accuracy and convergence speed over existing methods.
- Simple but Efficient Algorithm: Offers a straightforward yet effective approach for fine-tuning large models on limited hardware.

### Weaknesses
Some details need to be clarify, as explained in Questions

- Mask Updates per Iteration: Are the masks updated in each iteration? The concept of dynamic masking appears similar to Dynamic Sparse Training (DST), where the frequency of mask updates is a critical factor affecting performance [1,2]

- Can Sparse MeZO be integrated with LoRA, similar to how MeZO has been combined with LoRA in previous work?

-  When claiming the 3.5× speed-up in Figure 1, are both methods using the same learning rate, or does the speed-up depend on differing learning rates?

-  Determining the masks is a key component of this work, and the authors use a simple magnitude-based method. Do you believe that employing more advanced methods like Wanda [3] or SparseGPT [4] could further enhance performance?

### Questions
- Mask Updates per Iteration: Are the masks updated in each iteration? The concept of dynamic masking appears similar to Dynamic Sparse Training (DST), where the frequency of mask updates is a critical factor affecting performance [1,2]

- Can Sparse MeZO be integrated with LoRA, similar to how MeZO has been combined with LoRA in previous work?

-  When claiming the 3.5× speed-up in Figure 1, are both methods using the same learning rate, or does the speed-up depend on differing learning rates?

-  Determining the masks is a key component of this work, and the authors use a simple magnitude-based method. Do you believe that employing more advanced methods like Wanda [3] or SparseGPT [4] could further enhance performance?

[1] Do we actually need dense over-parameterization? in-time over-parameterization in sparse training, ICML 2021

[2] Rigging the Lottery: Making All Tickets Winners， ICML 2020

[3] A Simple and Effective Pruning Approach for Large Language Models, ICLR2024

[4] SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot

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
4

### Summary
This work proposes zeroth order memory-efficient optimization with sparse updates of model parameters for fine-tuning. Sparse updates are shown to facilitate better convergence than vanilla MeZO. The introduced method is evaluated on several tasks from SuperGLUE and several model architectures - Llama-1, Mistral, OPT.

### Strengths
* The fact that instability is caused by the noisy optimization of weights with large magnitude appears to be a useful practical insight. 

* SparseMeZO consistently improves upon dense MeZO optimization in different setups. 

* The proposed memory-efficient implementation of S-MeZO incurs almost zero memory overheads relative to original MeZO and allows tuning large models on a single GPU.

### Weaknesses
 * The overall contribution is incremental as the work adds additional sparsification steps on top of the MeZO optimization algorithm. 

* Evaluation setup is outdated (as for Fall 2024). Llama-1 and Mistral-v0.1 were released more than a year ago, and current models (Llama-3, Llama-3.1, Qwen-2.5, gemma-2) have advanced dramatically in terms of quality since then. In addition, I would suggest testing the approach on a more challenging and representative fine-tuning setup, such as instruction tuning on Alpaca/OASST or any other instruction fine-tuning dataset to fully appreciate the efficacy of SparseMeZO. 

* Some important baselines are not taken into consideration. PEFT adapters (LoRA, DoRA) allow for significant memory reduction on optimizer states. Memory footprint on activations and gradients is not very large for relatively short sequences (which is the case for SuperGLUE tasks) and small batches. In addition, it can be further decreased by gradient accumulation at the cost of additional compute. I would suggest adding comparison with these options and reporting memory usage in Table 3.

### Questions
* Given a fixed training budget does SparseMeZO outperform fine-tuning with adapters (+ gradient accumulation)?

* I think it would be insightful to add a comparison between the gradient updates with standard SGD optimization and SparseMeZO on a smaller scale model (say of size ~1B parameters).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper builds on the Memory-efficient Zeroth-order optimizer (MeZO) and introduces a new method, called Sparse MeZO. While MeZO is successful in training a neural network only with forward passes and by estimating the batch gradient using a finite difference scheme, there is still a significant gap between MeZO and common first-order methods. The authors aim to narrow this gap by updating only a sparse subset of the model parameters in each iteration. In particular, they propose to only update the smallest weights in each layer. They provide efficient implementations of doing so and show that Sparse MeZO performs better than multiple baselines, including MeZO.

### Strengths
The paper is well motivated, the approach is novel and the results are convincing. I particularly enjoyed the writing style and clear structure of the paper, it was mostly easy to follow, enjoyable to read and the reader was not left with many questions. The proposed method is interesting, however there are open questions, which I will discuss below. Overall, I think this is a good paper that however needs to resolve several questions before being suited for publication.

### Weaknesses
While I appreciate research in this important field, I have several concerns regarding soundness, clarity and contribution of the work, which I explain in detail below. I hope that these remarks are helpful in improving the work and I am happy to discuss my evaluation.

### Soundness
- In Figure 2b, you compare the potential loss increase on a different batch than the one used by MeZO, you then conclude that "zeroth-order gradient estimates suffer from overfitting or noise" (Line 189). I think to really conclude this, you would need to compare the MeZO gradient on a batch with the actual gradient on the same batch. The very same statement could be true for e.g. SGD, especially if the batch size is small and the variance of the gradient is high. I would greatly appreciate to see this figure instead or in addition to Figure 2b (potentially in appendix).
- In Line 197, you write that "all parameters share the same value". What is meant by this? The formula you say that "is used to estimate the gradient" only gives the magnitude of the multiplier, the actual gradient vector is given by $z$, where definitely not all elements are the same. Apart from that being a false premise, you then conclude that not all parameters are optimized in the true gradient direction, which I found a surprising statement. As far as I understand it, MeZO or variants randomly sample a direction along which the gradient is estimated, constrained to that particular direction. It will with very high probability not be anywhere close to the true gradient direction, by virtue of the fact that you are random sampling the directional derivative.  Please clarify this, maybe I am mistaken here.
- In the same paragraph, you somehow derive that "small weights are less impacted by noise corruption and can generalize better" - it is not clear to my why you derive this conclusion, is it just by the fact that you empirically find this to work better? What is the mathematical intuition or even justification for this statement? I think to resolve this soundness issue, you have to answer to very important questions: First of all, why does it make sense to use less weights in the first place? For First-order Optimization this would be absurd, what is the difference here? Why should this work better than using all weights? And secondly, why would exactly the smallest weights have the highest impact? I could potentially follow this argument if you were actually sparsifying the computed gradient, then one could argue with Taylor approximation or the like, but you are not doing this, you are instead sparsifying the weights. Why?
- Figure 4 highlights the effect of sparsity on the final performance. It is not clear why this curve looks like this and why that would make sense. The authors should clarify why they think that sparsity in the weights during gradient estimation helps (apart from providing empirical evidence that is performs better). What sparsity 70% performs bad, then sparsity 75% performs pretty good, and sparsity 80% performs worse again seems very arbitrary and not intuitive. In the worst case, this is just a noise artifact.


### Clarity and Experimental Validation
- Line 123: What is "SPSA"? Is this defined anywhere in the paper?
- In Line 260, you explain how you determine the mask. Why don't you set the threshold dynamically in each iteration? It's efficient and seems like the obvious thing to do.
- In Table 1, you report values for MeZO-LoRA. While I might have a vague idea of what that could be, this seems to be nowhere explained nor defined. Is this known from the literature or was this just missed?
- Are the numbers in the tables reported with respect to the same overall runtime or number of iterations? If MeZO variants are faster than e.g. FT, it would be nice to see how they compare on the same runtime.
- In the appendix (e.g. F), you refer to Lemma 3.2. What exactly is this, where is this defined? The same holds for the following appendix sections, I think these are referring to theorems/lemmata that do not exist or are not defined with the same numbering style. Please clarify.

### Contribution
- As outlined above, I think the contribution of the work is a major issue here. I fully acknowledge that Sparse MeZO achieves better results and is in that sense a meaningful contribution. However, the derivation of the method seems to be at least somewhat vague, it lacks justification apart from achieving better results. There is not much insight to gain since the paper lacks mathematical justifications, or at least intuitions. The derivation from gradient noise seems to be not very rigorous, at least to me. I hope that the authors can convince me otherwise.


### Minor Remarks
- Section 4.1 uses \citet everywhere where I think \citep is intended, this hinders readability.
- Line 483: There is a typo, I guess it should be "on a single A100 GPU".

### Questions
See above.

### Soundness
2

### Presentation
4

### Contribution
2
