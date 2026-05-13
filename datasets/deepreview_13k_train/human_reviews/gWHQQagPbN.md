# Beyond 2:4: Exploring V:N:M Sparsity for Efficient Transformer Inference on GPUs

- Decision: Reject
- Scores: 6, 6, 6, 5, 6

## Abstract
To date, 2:4 sparsity has stood as the only sparse pattern that can be accelerated using sparse tensor cores on GPUs. In practice, 2:4 sparsity often possesses low actual speedups ($\leq 1.3$) and requires fixed sparse ratios, meaning that other ratios, such as 4:8, 8:16, or those exceeding 50\% sparsity, do not incur any speedups on GPUs.
Recent studies suggest that V:N:M sparsity is promising in addressing these limitations of 2:4 sparsity. 
This sparsity divides a weight matrix into multiple V$\times$M blocks, pruning (M-4) columns within each block and applying 2:4 sparsity to the remaining columns. V:N:M sparsity inherently encompasses 2:4 sparsity but allows for higher and more flexible pruning ratios, typically resulting in greater practical speedups.
However, regarding accuracy, the effects of V:N:M sparsity on broader Transformer models, such as vision Transformers and large language models (LLMs), are largely unexamined. Moreover, Some specific issues related to V:N:M sparsity, such as how to select appropriate V and M values, remain unresolved.
In this study, we thoroughly investigate the application of V:N:M sparsity in vision models and LLMs across multiple tasks, from pretaining to downstream tasks. We propose three key approaches to enhance the applicability and accuracy of V:N:M-sparse Transformers, including heuristic V and M selection, V:N:M-specific channel permutation and three-staged LoRA training techniques.
Experimental results show that, with our methods, the DeiT-small achieves lossless accuracy at 64:2:5 sparsity, while the DeiT-base maintains accuracy even at 64:2:8 sparsity. In addition, the fine-tuned LLama2-7B at 64:2:5 sparsity performs comparably or better than training-free 2:4 sparse alternatives on downstream tasks. More importantly, V:N:M-sparse Transformers offer a wider range of speedup-accuracy trade-offs compared to 2:4 sparsity.
Overall, our exploration largely facilitates the V:N:M sparsity to act as a truly effective acceleration solution for Transformers in cost-sensitive inference scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the use of V:N:M sparsity in Transformer models and proposes three key methods to enhance its performance: heuristic V and M selection, V:N:M channel permutation, and a three-stage LoRA training technique. The experimental results demonstrate that V:N:M sparsity offers a broader range of speedup-accuracy trade-offs compared to traditional 2:4 sparsity.

### Strengths
1. This paper introduces a comprehensive framework that generates highly accurate V:N:M-sparse Transformers under different constraints, allowing users to balance the system performance and model accuracy.

2. The paper addresses key challenges in applying V:N:M sparsity by introducing three innovative techniques: heuristic V and M selection, V:N:M channel permutation, and a three-stage LoRA training technique. 

3. Experiments show superior performance of proposed methods.

### Weaknesses
1. The paper lacks a comparison with the latest related works, which limits its ability to contextualize the advantages and innovations within the current research landscape, such as [1]. Moreover, please also report the model performance without sparsity in Figure 4,5,7,8,9 to show the influence of introducing model sparsity. 

2. The experiments in this paper are limited to small-scale models, such as ViT, DeiT, and Llama-7B. It does not extensively explore the performance on larger models, like ViT-Huge or LLaMA models with higher parameter counts, where the effectiveness of the sparsity method might vary.

3. The work would be stronger if it provided performance benchmarks for Llama2-7B on pretraining benchmarks, such as MMLU or GSM-8k, to give a more comprehensive evaluation of the model's capabilities across a broader set of important benchmarks. If computational resources are limited, consider performing post-training on Llama2-7B to demonstrate the applicability of this paper's methods.

### Questions
This paper propose three techniques, including heuristic V and M selection, V:N:M channel permutation, and a three-stage LoRA training technique. Please further explain the relationship between these techniques, are they complementary, sequential, or something else?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores applying V:N:M sparsity to the weight parameters of transformer-based models, which can well retain accuracy while harvest inference speedup from sparse tensor cores in advanced GPUs. To achieve this, the authors propose three techniques to convert a dense transformer into a V:N:M sparse model, including a heuristic method for selecting V and M values, V:N:M-specific channel permutation, and a three-stage LoRA training approach for LLMs. They conduct extensive experiments on mainstream transformers, including DeiT, Swin Transformer, and Llama2-7B, across multiple tasks, demonstrating that their method outperforms naive 2:4 sparsity versions. Overall, this paper could be a good empirical contributions, paving the way for V:N:M sparsity compression for Transformers.

### Strengths
This paper is well-written and easy to follow. It integrates multiple techniques to accelerate V:N:M-sparse transformers. While the novelty of each technique is somewhat limited, the resulting performance improvements are substantial.
For theory strengths, the paper formulates the selection of V and M value as an optimization problem, balancing accuracy with speedup constraints. To solve this efficiently, they propose a two-phase sifting process to identify the optimal (V, M) combinations; Moreover, it adapts channel permutation to V:N:M sparsity, applying it to both the input and output of weight matrices to enhance accuracy for low training budgets. Finally, to ensure stable training of V:N sparse transformers, the authors integrate a three-stage LoRA training approach, consisting of Dense LoRA, Sparse LoRA with a dynamic mask, and Sparse LoRA with a fixed mask.

### Weaknesses
1. While it's intuitive that a smaller M results in lower sparsity in the sparse transformers, the process for excluding certain (V, M) combinations is unclear. Additionally, there is insufficient evidence in the paper demonstrating that mask diversity (MD) improves transformer accuracy. The paper lacks a clear explanation of how the two-phase sifting process effectively narrows down the (V, M) search space, and the justification for using MD as the final selection criterion is not sufficiently supported by empirical evidence. Specifically, it's not clear why MD should be preferred over simply selecting the (V, M) combination with the highest parameter count that meets the speedup constraint.
2. In Definition 1, the objective is to maximize accuracy under speedup constraints s. However, there should be experimental evidence demonstrating that the chosen V and M values meet these constraints. The paper does not explicitly show that the selected (V, M) pairs consistently achieve the desired speedup targets across different models and batch sizes. The connection between the optimization problem and the actual speedup achieved by the selected (V, M) values is not clearly established through experimental results.
3. In Section 5.4, although V:N:M sparse Llama2 outperforms RIA and Wanda, it still suffers significant accuracy loss compared to the dense counterpart. For instance, HellaSwag accuracy drops from 57.23 to 42.88, and ARC-C from 43.3 to 34.3. The magnitude of the accuracy drop raises concerns about the practical applicability of the proposed method, especially for tasks where high accuracy is crucial. The paper should provide a more thorough analysis of the trade-offs between speedup and accuracy, and perhaps explore techniques to mitigate this accuracy loss.
4. Equation (3) lacks the description of $\overline{M}_{t-1}$
5. In section 4.3, the definitions of $Mv$, $Wv$, $Bv$ and $ Av$ are unclear. Also, it would better to disclose detailed LoRA configurations in the three-staged LoRA training experiments (section 5.4) , such as dynamic sparse mask initialization, the interval of updating sparse masks, the actual training iteration assignment two different stages etc.
6. Figure 3 does not intuitively illustrate "in the absence of regularization, frequent updates to the masks can negatively impact the gradient flow of V:N:M sparse Transformers during fine-tuning". Additionally, adding a comprehensive empirical study would make it more convincing to draw the conclusion that "the iterations for the first two stages should not exceed 10% of the total iterations."

### Questions
1. For large language models (LLMs), latency is not solely determined by FLOPs; it is typically constrained by memory bandwidth and access patterns. In Definition 1, is the measured speedup based on a batch size of 1? Furthermore, when varying the batch size, will this lead to different V and M sparsity values? 
2. Can channel permutation enhance the performance of SR-STE training or LoRA training?
3. How is the regularization coefficient $\lambda$ in equation (3) tuned to improve training stability?

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
The paper addresses the limitations of 2:4 sparsity, by thoroughly investigating the application of V:N:M sparsity in vision models and LLMs across multiple tasks. The authors propose methods for selecting optimal V and M values and introduce techniques like V:N channel permutation and a three-stage LoRA training method, designed to enhance the accuracy and applicability of V:N Transformers, particularly in vision and language models.

### Strengths
1. The paper goes beyond theoretical contributions by proposing practical methods to improve the deployment of V:N:M
sparsity. Techniques like heuristic selection of V and M values, channel permutation, and three-staged LoRA training are thoughtfully designed to optimize accuracy-speedup trade-offs, even with limited training resources.
2. The authors validate their approach across multiple benchmarks, including vision Transformers and large language models (LLMs), demonstrating that V:N:M sparsity can achieve high speedups with minimal accuracy loss.

### Weaknesses
1. The heuristic method for selecting V and M values may not work for extensive Transformers models. My concerns are that even in the paper the proposed methods can achieve lossless performance on specific model DeiT-base and LLama2-7B. But what are the expected results on other models? The method's reliance on mask diversity (MD) might not generalize well across diverse architectures and scales, especially as the number of parameters increases significantly in larger models. The paper lacks a detailed analysis of how the proposed heuristic scales with model size and complexity, and whether the observed performance on smaller models can be extrapolated to larger ones.
2. The novelty and originality may not be enough. This paper is more like an engineering implementation technique. Authors may need to explain originality more. The paper's contribution seems to be primarily in the application of V:N:M sparsity and the specific techniques used to make it work, rather than in the introduction of fundamentally new concepts or theoretical insights. The techniques, while practically useful, might be seen as incremental improvements rather than groundbreaking innovations. The paper needs to more clearly articulate the theoretical underpinnings and the unique aspects of its approach compared to existing sparsity techniques.

### Questions
1. The heuristic method for selecting V and M values may not work for extensive Transformers models. My concerns are that even in the paper the proposed methods can achieve lossless performance on specific model DeiT-base and LLama2-7B. But what are the expected results on other models?
2. The novelty and originality may not be enough. This paper is more like an engineering implementation technique. Authors may need to explain originality more. 
3. "V:N:M-specific channel permutation, which improves the accuracy of V:N:M-sparse Transformers". Why channel permutation can improve accuracy? 
4. "a higher MD leads to better Transformer accuracy" Is this claim from extensive experiments or other places?

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
3

### Summary
The conventional 2:4 sparsity has been the only sparse pattern capable of accelerating GPU sparse tensor cores, and its performance was well-established. 
However, the paper claims that 2:4 sparsity has limitations, such as low actual speedups and support for only fixed sparsity ratios. 
To address this, the paper adopts the V:N:M approach. 
V:N:M sparsity combines n:m pruning with structured pruning and claims to overcome the fixed 50% pruning ratio limitation of traditional 2:4 sparsity.

### Strengths
1. Figure 1 is well-drawn and easy to understand.
2. The experiments conducted on the ViT model and LLM model are excellent.

### Weaknesses
1. [Novelty] I am not sure about the differences between this paper and the Venom paper [1]. Wasn't V:N:M proposed in the Venom paper [1]? How does it differ from Venom [1]?
2. The Venom paper proposed a GPU kernel for speedup sparse model on GPUs. how does this paper handle processing on the GPU? Does it propose a dedicated GPU kernel? If so, what are the differences compared to the Venom [1] GPU kernel?
3. The title of the paper includes "Transformer"—what specific characteristics of Transformers does it take into account?
4. Looking at Table 5, the caption lacks sufficient explanation. For instance, a clear description of "$\Delta$" is necessary in the caption.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies accuracy and speedup tradeoff of V:N:M sparse Transformers. It introduces a heuristic method for parameter selection, a channel permutation approach for low budget training and a three-stage LoRA training procedure applicable to various scenarios. Experimental results show that the proposed methods significantly accelerate the V:N:M sparse Transformers while maintaining lossless accuracy compared to 2:4 sparsity.

### Strengths
1. The authors propose three training approaches to enhance the applicability and accuracy of V:N:M sparse Transformers. They present a heuristic V and M selection method to find the tradeoff between accuracy and speedup for V:N:M sparse Transformers. To improve the accuracy within limited training budgets, they introduce a channel permutation approach. Finally, they introduce a Dense-Dynamic-Fixed mask training procedure to maintain the model accuracy.

2. The paper is well-written and easy to follow up. The introduction and motivation are clear and well-organized. The experiments are comprehensive.

### Weaknesses
1. Why is the paper claimed that only a 2:4 sparse pattern can be accelerated by sparse tensor cores? I have some doubts about it. One could write a custom CUDA kernel and accelerate based on the indices of the weights.
2. How did you implement the kernel using sparse tensor core? For higher sparsity (like 2:12, 2:24), the observed speedup falls short of the theoretical speedup, possibly due to inefficiencies in the implementation. Moreover, would you consider using cusparse/cublas or other CUDA kernels to compare speedup with the proposed method at highly sparsity?
3. In Fig.4(a), the authors compare accuracy improvement under similar speedup conditions. In my view, more parameters generally lead to higher accuracy, so it would be fairer to compare accuracy at the same sparsity. Fig.4(a) shows how V and M selection impacts the accuracy and speedup of V:N:M sparse Transformers. However, the V:N:M setting in Fig.8 differs. Does this imply that V and M selection is not applied in Fig.8?

### Questions
Please see the above.

### Soundness
3

### Presentation
3

### Contribution
3
