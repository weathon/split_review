# Low-Rank Compression of Language Models Via Differentiable Rank Selection

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Approaches for large-language model compression using low-rank decomposition have made strides, particularly with the introduction of activation and loss-aware Singular Value Decomposition (SVD) that improve the trade-off between decomposition rank and downstream task performance. Despite these advancements, a persistent challenge remains—selecting the optimal ranks for each layer to jointly optimize compression rate and downstream task accuracy. Current methods either rely on heuristics that can yield sub-optimal results due to their limited discrete search space or are gradient-based but are not as performant as heuristic approaches without post-compression fine-tuning. To address these issues, we propose Learning to Low-Rank Compress (LLRC), a gradient-based approach which directly learns the weights of masks that select singular values in a fine-tuning-free setting. Using a calibration dataset of just 3,000 documents, this training architecture teaches the model to select fewer and fewer singular values while minimizing the divergence of intermediate activations from the original model. Our approach outperforms competing fine-tuning-free rank selection approaches, such as Sensitivity-based Truncation Rank Searching (STRS), Adaptive Rank Selection (ARS), and LLM-Pruner on Llama-2-7B, Llama-3-8B, Gemma-7B, and Llama-2-13B across various compression rates on common-sense reasoning and open-domain question-answering tasks.For instance, with a compression rate of 20%, our approach outperforms the competitive STRS on MMLU, BoolQ, and OpenbookQA by 12%, 3.5%, and 4.4%, respectively, using Llama-2-13B. More remarkably, our fine-tuning-free approach consistently outperforms LLM-Pruner, even after fine-tuning, on NQ-Open, MMLU, BoolQ, and OpenbookQA with Llama-2-7B.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to improve the performance of low-rank compression for LLM. To achieve this goal, they propose learning optimal ranks on 3,000 articles using multiple loss functions. Experimental results show that it performs better than previous SVD methods.

### Strengths
- The learnable mask mechanism has a higher potential compared to heuristic algorithms. 

- The experimental results are positive, outperforming previous SVD methods

### Weaknesses
- sloppy formatting. The reference to the table is missing in line 452. AUTHOR CONTRIBUTIONS and ACKNOWLEDGMENTS sections have not been removed. The authors should check their manuscript more carefully.
- cannot outperform LLM Pruner. LLM Pruner requires only a small amount of data (e.g., 128 articles) for fine-tuning to achieve better results.
- no ablation study on multiple loss functions. The authors used three loss functions but did not verify their effects in the experiments.

### Questions
What is the setting of LLM Pruner in Table 2? LLM Pruner has multiple configurations, and the authors did not specify which one was used. Additionally, if training is performed after compression (like LLM Pruner), can better results be obtained?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to compressing large language models (LLMs) using low-rank approximation. The key innovation is the introduction of a learnable masking mechanism within the Singular Value Decomposition (SVD), which dynamically selects eigenvalues and eigenvectors during the low-rank approximation process. Unlike traditional methods that rely on a fixed rank and select only the top-K components with the largest eigenvalues, this approach uses learnable masking parameters to optimize rank allocation based on loss constraints. This flexibility allows the model to allocate rank to components with smaller eigenvalues when beneficial, making the compression more adaptive and potentially more effective.

### Strengths
1. Clear idea. The motivation is good and the solution is reasonable. 
2. The writing is clear and easy to follow

### Weaknesses
My primary concern is the trade-off between compression and model quality. While the model achieves some compression, it sacrifices quality significantly. A 20% reduction in parameters leads to a notable degradation in performance. Although the paper attempts to show improvements over certain baselines, a more meaningful comparison would be with a non-compressed model of similar size. For instance, if the method can compress an 8B model to 3B while still outperforming a standard 3B model, it would be valuable in practice. Otherwise, the utility of the compressed model for real-world applications seems limited. I recommend the authors address this comparison in Table 1 and incorporate a discussion on it within the paper.

Additionally, among the various benchmarks, MMLU deserves particular attention, as its results are mixed when comparing the proposed approach with STRS. The substantial drop in MMLU performance, despite the limited compression rate, raises concerns about the effectiveness of the method.

Certain design choices in the paper also need clarification. For example, the paper applies an average of the learnable weights in the L_compression loss, yet averaging can be highly sensitive to extreme negative values. Exploring alternative approaches could enhance robustness, and it would strengthen the paper if the authors could justify why this choice is optimal.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present LLRC, a novel approach for compressing large language models (LLMs) using adaptive low-rank decomposition via Singular Value Decomposition (SVD). LLRC introduces a differentiable rank selection mechanism that dynamically identifies the optimal compression rate per layer, balancing performance retention and model efficiency.

### Strengths
1. The use of multi-objective loss functions, including distillation and total variation loss, helps LLRC retain high performance even at high compression rates, making it effective for deployment in resource-constrained environments.

2. By freezing the main model weights and only learning the mask layer, LLRC reduces the computational burden during training, making it more efficient than traditional compression methods.

### Weaknesses
1. The method is similar to structured pruning approaches, such as Sheared LLaMA (https://arxiv.org/abs/2310.06694), yet these works are neither cited nor compared against, which limits the paper’s contextual grounding.

2. When comparing with pruning and distillation methods, the paper does not choose the most competitive or state-of-the-art approaches, making it unclear how LLRC performs against the best available compression techniques.

3.Based on my own empirical experience, datasets like BoolQ and PIQA often exhibit high variance in performance, which can obscure the true effectiveness of a compression method. In contrast, MMLU is generally more scientifically consistent and reliable for evaluating language models. The paper shows that the proposed method does not yield a notable improvement over STRS on MMLU, and in fact, it lags behind STRS on the LLaMA-3-8B model. This limitation on a stable and rigorous benchmark like MMLU raises questions about the robustness of the method, particularly when applied to more demanding or scientifically rigorous evaluation tasks.

### Questions
1. Given that datasets like BoolQ and PIQA are known for high variance in performance across different checkpoints, how did you approach checkpoint selection for these evaluations? Did you adopt any specific strategy, such as averaging performance across multiple checkpoints or selecting based on a validation set, to mitigate potential fluctuations and ensure fair comparison across methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the rank selection problem in the context of low-rank decomposition in language model compression. Prior researches on low-rank decomposition mainly focus on better reconstructing the weight matrix or output activation while assuming the same compression rate is shared across all modules. Instead, this work proposes LLRC(Learning to Low-Rank Compress), which insert learnable masks into each linear layer for selecting singular values for compression. The method starts with Activation-aware SVD to obtain the initial factorized form of weight matrices, then utilize Gumbel Sigmoid to transform mask variables into continuous binary mask. The training objective consists of three sub-parts, which are Compression Loss, Distillation Loss, And Total Variation Loss. After training on a 3,000 documents calibration dataset, the learned masks variables are used for selecting the ultimate singular values to preserve. Experiment evaluation are performed using Base LLM(LLaMa2-7B and LLaMa3-8B) on five zero-shot commonsense reasoning and question answering tasks. Results demonstrate moderate improvements compared to previous rank selection methods.

### Strengths
1. The training process of LLRC is efficient, as it only requires gradient updates on the singular value masking variables.
2. LLRC is able to adaptively allocate rank budget to weight matrices, allowing for flexible model parametrization.

### Weaknesses
1. The writing of this paper needs significant improvement. There are considerable amount of typos, grammar error, and formatting issues in the submission, e.g., Line 94, Line 195, Line 226, Line 262, Line 355, Line 452, Figure 2&3(out of margin). Also note the repetitive description as in Line 255-257 and Line 284-286.
2. The novelty of LLRC is limited. The idea of using learnable pruning mask variables to select ranks of SVD-based factorization has been previously explored[1]. The major difference only lies in LLRC is applied on LLM and on task-agnostic setting.
3. The downstream performance of compressed model is unsatisfactory, given that the compression rate is merely 20%. Moreover, LLRC does not exhibit consistent superiority over prior rank selection methods, according Table 1.
4. This paper lacks  experimental validation of the effectiveness of LLRC on instruction-tuned models besides the base versions.
5. The compression rate reported in the submission is relatively low and the performance degradation induced by compression clearly outweigh the efficiency gain.



[1]. Structured Pruning of Large Language Models. *EMNLP 2020*.

### Questions
See weakness above.

### Soundness
2

### Presentation
1

### Contribution
1
