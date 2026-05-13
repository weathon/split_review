# LDAdam: Adaptive Optimization from Low-Dimensional Gradient Statistics

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
This strategy keeps the optimizer's memory footprint to a fraction of the model size. LDAdam relies on a new projection-aware update rule for the optimizer states that allows for transitioning between subspaces, i.e., estimation of the statistics of the projected gradients. 
To mitigate the errors due to low-rank projection, LDAdam integrates a new generalized error feedback mechanism, which explicitly accounts for both gradient and optimizer state compression. 
We prove the convergence of LDAdam under standard assumptions, and show that LDAdam allows for accurate and efficient fine-tuning and pre-training of language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a new optimization algorithm to train large (language) models.
Like the recent GaLore algorithm, the proposed algorithm is a variation of ADAM, that performs updates in a lower-dimensional space, to store lower-dimensional quantities to be more memory-efficient.
As I understand (and as written by the authors), the real meat behind this kind of algorithm is the choice of the projection to obtain a meaningful lower-dimensional subspace that is both efficient to compute/store and a good enough approximation of the gradient. The proposed algorithm retains the desirable memory-efficient properties of GaLore, while almost matching the generalization performance of ADAM. Convergence proofs and exhaustive experiments on text benchmarks are provided.

### Strengths
The paper is overall easy to follow, the idea is interesting, and seems to empirically works great.

### Weaknesses
I see that the authors provide some running times and memory metrics in Appendix B, but it seems to me that this part should be more exhaustive in order to prove the proposed algorithm useful.
I know this is hard to monitor for algorithms on GPU, but could authors provide graphs similar to Figure 1, but with running times? and memory usage? with ADAM, GaLore, and LDADAM (proposed).
In other words, could authors provide graphs with perplexity as a function of runtime and perplexity as a function of memory usage? Even if these required graphs will be imperfect for a lot reasons, I think they are crucial to gain insights and potentially prove usefulness.

### Questions
see Weaknesses

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
The paper proposes a new memory-efficient training algorithm based on Adam via efficient projection onto subspaces. The proposed method enjoys non-asymptotic theoretical rate of convergence and demonstrate good experimental results in training large language models (LLMs).

### Strengths
The paper is well-written and the contribution is clear. The algorithm is novel with theoretical convergence. The experiments indicates that the new approach is performing not only better than GaLore, but also better than the vanilla Adam for some parameter settings.

### Weaknesses
 (Please respond to the "Questions" directly) The computational time of proposed method is not clear; Some discussion on the theoretical results is needed.

### Questions
Overall I think this is a work with interesting observations and methods. I have the following concerns and questions (I'm happy to increase my evaluation if the authors address the issues):

1. To my understanding, GaLore doesn't employ SVD step for every iteration in order to save computation overheads. On the contrary, the proposed method would need a Gram-Schmidt process and several extra steps for updating the momentums and gradients. A major conern is the computation overhead of this proposed method. I udnerstand that the memory consumption is roughly the same as GaLore, yet I'm curious about the time required for training LLMs both in theory and in all the experiment settings using the proposed method.
2. The convergence results in Theorem 1 and 2 are similar to that of full-rank Adagrad/Adam. To my understanding, the low rank parameter $r$ only plays a role in the constant $q_r$? If so, can the author comment on how to choose such $r$ and if the theory has any implication on the choice of $r$. In particular, if $r=m$ and the method reduce back to the original Adam, can we say any matching result with the analysis on the original Adam?
3. This question is related to the previous one. The experiments show that LDAdam is even better than original Adam in some cases (Table 3 with $r=512$, Table 4 with $r=256$). Can the authors expand on the discussion of "regularization effect of compression" or provide some references? It's still not very clear to me right now.
4. Any experiment on even larger LLMs such as Llama 1b or 7b? I'm curious what will happen if the model is large and the training is conducted in parallel on multiple GPUs.

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
This paper on LDAdam addresses a crucial challenge in training large models: reducing memory consumption of optimizers without sacrificing model quality. The key innovation is the introduction of a lower-dimensional subspace optimization approach, where adaptive optimization occurs within constrained dimensions. The optimizer, though operating in a subspace, ensures exploration across the entire parameter space, thereby maintaining model expressivity while being memory efficient.

### Strengths
1. **Projection-Aware Update Rule**: LDAdam uses a projection-aware update rule to transition between subspaces. This rule allows it to estimate the gradient statistics even after dimensional reduction, adapting efficiently to changes in the subspace basis without losing essential gradient information.

2. **Generalized Error Feedback Mechanism**: To address inaccuracies from low-rank projections, LDAdam introduces a unique error feedback mechanism that accounts for both gradient and optimizer state compression. This mechanism reintroduces projection errors in subsequent iterations, ensuring stability in updates and helping LDAdam match the performance of uncompressed optimizers.

3. **Convergence and Memory Efficiency**: The paper provides a proof of LDAdam’s convergence under standard assumptions. With this design, LDAdam achieves a significantly reduced memory footprint. In practical terms, LDAdam’s optimizer states require only a fraction of the memory needed by Adam, making it feasible to train large language models in resource-constrained environments.

### Weaknesses
Liang et al. [1] provide a convergence analysis for GaLore and related algorithms without relying on a 'stable-rank' assumption. Since LDAdam aligns with this framework, I recommend citing [1] for its convergence insights. Additionally, a comparison of LDAdam’s convergence analysis with [1], specifically on the impact of removing the 'stable-rank' assumption, would help clarify the authors’ theoretical contributions. The original GaLore paper supports gradient accumulation, contrary to the authors' claim. I suggest they clarify this point, either correcting the claim or explaining any differences in their interpretation or implementation of GaLore to avoid potential misunderstandings.

### Questions
The original GaLore paper supports gradient accumulation, contrary to the authors' claim. I suggest they clarify this point, either correcting the claim or explaining any differences in their interpretation or implementation of GaLore to avoid potential misunderstandings.

Good paper, I suggest acceptance.

### Soundness
2

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
4

### Summary
Thin paper introduces a novel memory-efficient low-dimensional Adam optimizer for training large models. Specifically, the authors propose a new projection-aware update for the optimizer states that allows for transitioning between subspaces. They also perform block power iteration to at each step to efficiently and accurately project the gradient and optimizer states. To reduce the error caused by the low-rank projection, this work leverages a new generalized error feedback mechanism that accounts for both gradient and optimizer state compression. The authors theoretically analyze the convergence rates for different objectives. To validate the proposed algorithm, the authors present extensive experimental results on different datasets with the comparison to different baselines.

### Strengths
1. The investigated topic is quite interesting and critical, particularly when LLMs are popular in every area. A memory-efficient optimizer is required to conduct computationally efficient fine-tuning.
2. The paper is easy to follow and the presentation in this work is clear.
3. This work presents in-depth theoretical analysis for the proposed algorithm and show the explicits the convergence rate.
4. The empirical evidence to validate the proposed algorithm look extensive and thorough.
5. The comparison between the proposed method and baselines is technically convincing.

### Weaknesses
1. Assumption 2 is a quite strong assumption for the gradient, which may limit the applicability of the proposed algorithm. Until now, most existing algorithms have relaxed this assumption in their works such that this assumption imposes some weaknesses to the proposed algorithm. Specifically, the assumption of a bounded gradient norm, while common, can be restrictive in practice, especially when dealing with complex loss landscapes. The analysis should explore the sensitivity of the convergence results to violations of this assumption, perhaps by considering alternative conditions such as bounded variance or a weaker growth condition.
2. In this work, the authors have mentioned that GaLore is the closest work. Though we have seen the authors have shown in detail how the proposed algorithm differs, it would be great to include a technical discussion for the difference between them in terms of convergence rate. That way, it is clearer to directly show the exact theoretical difference. A more detailed comparison of the convergence rates, including a discussion of the specific constants and dependencies on problem parameters, would be beneficial. This would help clarify the practical implications of the theoretical differences between the two methods.
3. In the practical view of the algorithm, the authors use Gram-Schmidt process to calculate $\mathcal{U}_t$. However, the process has numerical instability, computational intensity, and even inaccuracies. If this process fails, how can the authors guarantee that there always exists a feasible and reliable $\mathcal{U}_t$ for the subsequent steps? The reliance on the Gram-Schmidt process, while straightforward, raises concerns about numerical stability, especially in high-dimensional settings. The authors should discuss potential failure modes and propose alternative orthogonalization techniques or error handling strategies to ensure the robustness of the algorithm.
4. Although the experimental results look promising, how to validate the theoretical conclusions from Theorem 1 and Theorem 2, particularly, the impact of the compression ratio? The authors need to present some ablation studies for the proposed algorithm. Specifically, the experiments should include a systematic analysis of how the compression ratio affects the convergence rate and the final performance. This should include varying the rank of the low-rank approximation and observing the corresponding changes in training dynamics and generalization performance.

### Questions
1. How to relax the bounded gradient assumption in the study?
2. How to guarantee a feasible $\mathcal{U}_t$ if Gram-Schmidt process fails?
3. How to validate the theoretical conclusions from both theorems?

### Soundness
3

### Presentation
3

### Contribution
3
