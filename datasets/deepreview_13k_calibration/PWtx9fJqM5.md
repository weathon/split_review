# A Study of Necessity & Sufficiency of Linear Transformations in the Attention Mechanism

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Scaled Dot Product Attention (SDPA) is the backbone of many modern
  deep-learning models. It is so versatile that it has been used in
  natural language, vision, and multi-modal domains with very little
  change compared to its original formulation. This paper studies the linear transformations used in SDPA. To this end, we introduce three variants of the attention mechanism by removing consecutive linear transformations or adding an extra one. We name these variants Optimized ($W^V$ removed),
  Efficient ($W^V$ and $W^K$ removed), and Super Attention ($W^V$ and $W^K$ removed and $W^A$ introduced) to simplify comparison when referring to them. In addition to providing the mathematical intuition behind these choices, we evaluate these variants on several datasets of varying size and complexity in vision and text modalities for predictive and generative tasks. Optimized and
  Efficient variants have one and two matrix multiplications fewer
  per head, respectively, and 25\% and 50\% fewer parameters,
  respectively, than standard SDPA. However, the performance change compared to difference in parameter count is small. Super Attention introduces a new linear transformation
  on the values, transforming them from the left. It outperforms
  standard SPDA in both modalities by up to 10\%
  while having one fewer matrix multiplication per head and 25\% fewer
  parameters than standard SPDA. Consequently, it is also faster than standard SDPA.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces three alternative formulations for the self-attention mechanism with the objective of reducing the number of parameter of the standard attention mechanism while keeping similar level of performance. The three formulations are based on two principles: (i) composing linear transformations do not increase linear expressivity (ii) it should be beneficial to linearly align inputs along the sequence dimensions before applying self attention. The formulations are benchmarked on vision and languages tasks on different datasets, while keeping the scale of the models smaller for computational capability reasons.

### Strengths
- The paper investigates on overlooked aspects of the self attention mechanism in mutliheaded attention architectures. In terms of expressivity the Optimized and Efficient alternatives are well posed alternatives, and the super attention one is an interesting alternative.

- These observations may be impactful, given that transforms are the default choices in many branches of deep learning, and could help explaining some of the reasons behind of post hoc head pruning of attention networks [a] . 

    -  [a] Voita, Elena, et al. "Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned." ACL


- The paper is well written and clear.

### Weaknesses
 - Experiments have not been performed at a larger scale to compare with standard performance of transformers on the datasets. This limits a lot the evaluation of the proposed alternatives implementations of attentions as the performance and scale of the problem is far from the original one.

 - The redundancy properties analyzed are proper of the self attention mechanism in the multi head setting. This should be specified in the introductory and method section, as methods as cross attention for example, should not be affected by the observations made.


 - While the efficient and optimized attention mechanism are well posed in terms of expressivity, the training dynamics of the network might actually benefit from the redundancy and overparametrization of the standard self attention mechanism, especially with large datasets. Given that this is to be verified, also in the small scale setting (LoRA) overparametrization has shown to be effective for training convergence and generalization, for example in: 

    - Yaras, Can, et al. "Compressible Dynamics in Deep Overparameterized Low-Rank Learning & Adaptation.", ICLR 2024


- It might be useful to check and discuss the following paper which is related to the second principle and the Super Attention mechanism proposed :

     - Cordonnier, Jean-Baptiste, Andreas Loukas, and Martin Jaggi. "Multi-head attention: Collaborate instead of concatenate."

*Minor*

I spotted some typos: 

Line 323, Captions fo tables 1,2,3: "Apendix" -> "Appendix"

### Questions
- How are the generalization performances of the model affected by the reduction of parameters? For example its transferability performances (fine-tuning the model on other tasks/dataset):  with larger scale scale experiment available it might have been interesting to look at the generalization performance of the parameter reduced models on different tasks for example of ViTs on the VTAB benchmark [a]

     - [a] Zhai, Xiaohua, et al. "A large-scale study of representation learning with the visual task adaptation benchmark. arXiv 2019." arXiv 

- Why does accuracy on validation set on CIFAR and Imagenet is lower than test accuracy in Table 1? 

- Could you report standard deviation across the different seeds of training for CIFAR and MNIST datasets in Table 1?

### Soundness
2

### Presentation
3

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
The paper presents three alterations to the standard attention mechanism that is widely used in transformer-style neural network architectures across much of machine learning.  These variants are different methods to replace linear projections in the attention block with a slicing operation that groups different columns together as an analog of attention heads with improved efficiency.  The paper evaluates these three variants on several vision and language benchmarks, and shows improvements in efficiency with at least no worse performance.

### Strengths
- The paper is well written, and the claims are appropriately scaled to the results demonstrated in the evaluation.  
- The evaluations are thorough given constraints on computational budget, and cover several benchmarks where transformer-inspired architectures have been effective.  
- The proposed changes to the attention mechanism are easily understood, and motivated with high-level principles that help explain the design process.

### Weaknesses
 - The paper could improve with a better discussion of relevant related work.  Currently the related work section focuses heavily on quantization, which seems only distantly relevant to the proposed approach.  I would have appreciated a more thorough comparison of the proposed methods with relevant literature that seeks to modify the attention mechanism for better efficiency:  eg Performer, Linformer, RKWV.
- Although the linear part of the attention block is under-studied, I would argue that this is partly because the attention itself (with its quadratic scaling with context length) is the primary bottleneck. The paper does not sufficiently address the fact that the proposed methods do not fundamentally change the quadratic complexity of the attention mechanism, which is the dominant computational cost for longer sequences. The focus on linear projection efficiency, while valuable, risks overshadowing the more pressing issue of quadratic scaling.
- The runtime gains reported in smaller settings do not seem to hold up with larger models and longer sequence lengths. (Fig 5)

### Questions
- How far can you push the efficiency gains with these different methods of attention?  For example, with the optimized variant, can you further reduce parameters/runtime by increasing the number of slices (or heads?) used?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces three efficient variants of Scaled Dot Product Attention (SDPA) that reduce computational costs and parameters by adjusting the linear transformations in them. Tested across vision and NLP tasks, these variants maintain or enhance performance while achieving faster inference.

### Strengths
1. The approach is simple and well-explained
2. Evaluation covers a broad range of tasks spanning different modalities. 
3. Complexity analysis is comprehensive

### Weaknesses
I am not an NLP expert and am less familiar with NLP tasks, so my focus is primarily on the architecture and vision tasks.

1. Lack of Strong Baselines: The paper primarily compares against standard attention, which is a highly under-optimized baseline. For vision tasks, it would be more informative to include stronger, more optimized baselines such as Swin, MetaFormer, MaxViT, or EfficientNet. Since your method modifies the attention mechanism, it could be integrated into these attention-based or hybrid architectures, which would reveal how your proposed changes perform in comparison to already optimized attention modules.

2. Absence of End-to-End Training on ImageNet-1K: The goal of the proposed models seems to be achieving parameter efficiency without sacrificing expressiveness. However, fine-tuning on ImageNet-1K alone may not fully validate this. Superior performance on smaller datasets (e.g., CIFAR-100, MNIST) and fine-tuned ImageNet-1K can sometimes reflect lower expressiveness, as reduced architectures naturally avoid overfitting on simpler datasets. While removing components from the standard ViT could reduce redundancy, recent hybrid models like MetaFormer and NAT, which use standard ViT only in the later layers, demonstrate that the later layers often require more expressive power. Testing your method on such stronger baselines might show that similar gains are less achievable when the baseline model is already well-optimized and not overly redundant.

3. Limited Analysis Beyond Complexity: While the paper focuses on the complexity benefits of the proposed method, it would be insightful to explore how the learned representations change. For instance, comparing attention maps and MLP activations between standard attention and your optimized attention variants could reveal additional insights into the effects of these architectural modifications.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
