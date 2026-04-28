# Ultra-Sparse Memory Network

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
It is widely acknowledged that the performance of Transformer models is exponentially related to their number of parameters and computational complexity. While approaches like Mixture of Experts (MoE) decouple parameter count from computational complexity, they still face challenges in inference due to high memory access costs. This work introduces UltraMem, incorporating large-scale, ultra-sparse memory layer to address these limitations. Our approach significantly reduces inference latency while maintaining model performance. We also investigate the scaling laws of this new architecture, demonstrating that it not only exhibits favorable scaling properties but outperforms traditional models. In our experiments, we train networks with up to 20 million memory slots. The results show that our method achieves state-of-the-art inference speed and model performance within a given computational budget.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Motivated by the high memory access cost bottleneck of Mixtures of Experts (MoEs) for Large Language Model (LLM) inference, the authors propose an alternative methodology, UltraMem, based on Product Ley Memory (PKM) which improves memory access above MoEs, but suffers in performance compared to them. The authors make several observations to improve the vanilla PKM methodology, basing their method on this baseline. The authors then not three problems with the PKM architecture, notably that it does not scale to large value sizes, product key decomposition biases retrieval, and unbalanced GPU computation/communication for large models. The authors propose to decompose the large memory layer of PKM into many smaller memory layers distributed across layers, allowing execution of memory and transformer layers to overlap. The authors propose to use a Tucker decomposition instead of the product key decomposition of PKM. Finally, rather than explicitly maintaining a large memory table for values, the authors propose a virtual memory approach. The authors evaluate UltraMem across several tasks compared to dense and an MoE equivalent model, and compare the performance across these tasks, along with the inference and memory accesses for each, demonstrating significantly faster inference with similar performance to an MoE model.

### Strengths
* Memory access is perhaps the main bottleneck in inference for contemporary hardware, and so this is a well-motivated and impactful direction to be exploring.
* The results appear to show impressive improvements over Mixtures of Experts (MoEs) in inference time and memory access while maintaining validation loss/perplexity. 
* The authors methodology is detailed and thoughtful, for example deriving the correct initialization for their method (which would appear to also apply somewhat to PKM).
* Many of the figures/graphics themselves are good in design and would be helpful to understanding the methodology if it wasn't for the other serious issues with readability and captions (see below).
* Changes to PKM (before the UltraMem specific changes) are listed in 2.2 as the bag of tricks that improve PKM's performance, and are separate from the author's proposed UltraMem structure. It would be beneficial if more papers took such an approach to be clear about the differences between improved training methodology for baseline methods and a newly proposed method. Ablation in particular is nice about being clear how these changes improve baseline PKM performance.
* Real-world inference and memory access results on GPU hardware.
* Large-scale experiments, in particular results are evaluated on various model sizes, from 151M param up to 1.6B. FLOPS for the sparse models.

### Weaknesses
Overall the paper reads poorly, more as a collection of experimental details and results rather than a cohesive story. I know that's frustrating and perhaps vague feedback to get as an author but I think it's really important to point out as it makes the paper quite hard to read as it is, and reduces the impact of the author's work. To be clear, I do appreciate the experimental and methodological details themselves. However, I believe the authors could do the work much more justice by taking a step back and framing their research story better. In particular, I would recommend focusing first on section 3 as higher-level motivation of the method before diving into building on top of PKM.
* All the figures containing the majority of results, and some of the methodology figures (Fig 4) are **far** too small. They are so small that the figures are completely unreadable on paper. I measured the font sizes in the figures out of curiousity, and most of the fonts are 2-3pt!
* Given that the proposed method is largely based on PKM, PKM should be a baseline in the results. The authors mention PKM's "..effectiveness is significantly inferior to that of MoE.", without explaining on what measures this is true, or giving the reader to make that judgement in the results. I don't actually doubt the authors on this, but it must be demonstrated in the experiments.
* While as noted above it's great that the "bag of tricks" for PKM is listed, along with the ablation, it also would seem important that the performance of the improved PKM should be evaluated as a baseline over just vanilla PKM, and compared with the improvements from the author's proposed method.
* The related work is **far** too short given all the work done in this field, much of which is referred to by the authors and built upon in the proposed method. To be honest I'm never a fan of related-work at the end of the paper, but I feel like this paper in particular would have greatly benefited by the related work coming before the methodology rather than at the end of the paper, as instead of having to bring up related work throughout the paper as it is built upon, it could have just been earlier summarized and then referenced throughout, allowing the story to focus on the methodology more clearly.
* Relies too much on validation loss/perplexity for the evaluation of whether generalization performance is maintained in the main paper/figures. The authors do have six other metrics for tasks in Table 1 and figures in the appendix for these tasks (which they should explain better in the paper/background rather than quickly citing all of them in a list). Given that the authors are in a sense proposing a form of sparsity, and given the results of Jaiswal et al. for pruning (Compressing LLMs: The Truth is Rarely Pure and Never Simple, ICLR 2024) I believe it's more important to focus on the performance in task-specific measures.

### Questions
Suggestions:
* Focus on the high-level motivation before diving into details of methodology and experiments.
* Move the related work up front in the paper, and put in background required for your method. Include MoEs, PKM, Tucker decompositions, Megatron, any background relevant to IVE and MCS, etc.
* Fix readability of all the text in the figures.
* Figure 2 (and to some extent Figure 3) are poorly labelled/captioned, and it's largely left to the reader to figure out what each side represents and how it's related to the method. At a minimum label the subfigures or describe in caption what left/right are. Would also suggest positioning floats at top of page.
* When including a large table of metrics (i.e. in Table 1), it's helpful to the reader to explain whether lower or higher is better for each, e.g. with an arrow in the header.

### Soundness
4

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
This paper proposes a novel deep learning architecture called UltraMem, designed to reduce memory access costs during the inference process of large language models, thereby improving inference efficiency. The core innovation of UltraMem lies in its introduction of an ultra-sparse memory layer, which allows the model to activate only a small number of necessary memory units when processing tasks. This approach reduces the number of memory accesses, effectively lowering inference latency. Specifically, , UltraMem surpasses MoE with the same parameters and computation as model capacity increases.

### Strengths
1. This paper introduces the UltraMem architecture, which demonstrates innovation by significantly reducing inference latency while maintaining computational efficiency. 
2. The paper presents extensive experiments comparing the performance of UltraMem with traditional models (such as MoE and dense models), verifying UltraMem’s advantages in inference speed, memory access costs, and scalability. 
3. The experiments show that UltraMem’s memory access volume grows much more slowly with batch size compared to MoE, enhancing its practical utility.

### Weaknesses
1. The paper lacks references and descriptions of the architecture diagrams within the main text. For example, each step in Figure 4 is not referenced in the text. Additionally, certain terms in the architecture diagrams, such as “fetch values,” are not explained in the text, making the paper difficult to follow.
2. The paper claims that the proposed UltraMem method has stronger scalability. However, UltraMem was only tested on models with 151M, 680M, and 1.6B parameters, without experiments on larger models, such as the 6.5B model or beyond. This parameter range is insufficient to fully verify UltraMem’s scalability in large-scale models. It is recommended to extend the experimental scale to explore UltraMem’s performance and scalability at extremely large parameter sizes (e.g., 10B and above).
3. Several modules proposed in the paper, such as Implicit Value Expansion (IVE) and Multi-Core Scoring (MCS), collectively enhance UltraMem’s performance. However, the independent effects of each module are not adequately evaluated. For instance, Table 2 provides ablation experiments but lacks detailed analysis of the independent effects of key modules like IVE and MCS across different tasks or sparsity settings. It is recommended to expand on Table 2 by adding experiments that assess the independent impact of each optimization module on model accuracy.
4. Figure 4 illustrates the process of Tucker decomposition but lacks analysis of how different decomposition parameters, such as rank r, affect model accuracy. To clarify the impact of different Tucker decomposition configurations on model performance, it is recommended to include more comprehensive ablation experiments to quantify Tucker decomposition’s specific role in UltraMem. Additionally, experiments should be added to analyze the effects of different values of E in the IVE method on experimental results.

### Questions
see weakness.

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
In this paper, the authors propose UltraMem, a memory-efficient method designed to replace MLP layers or Mixture of Experts (MoE) in Transformer architectures, particularly for large language models. UltraMem builds on a refined Product Key Memory (PKM), utilizing a 2D grid structure with row-column key decomposition to reduce retrieval costs. Additionally, it employs Tucker Decomposition to further minimize memory usage and computational overhead. Experiments across various language tasks demonstrate UltraMem’s promising effectiveness and efficiency.

### Strengths
This paper addresses an interesting and impactful problem with practical applications in large language model (LLM) research.

- The authors propose an alternative, memory-efficient approach to achieving the performance of Mixture of Experts (MoE) models.
- They introduce a sparse memory access mechanism and a 2D Product Key Memory structure, which restricts memory access to only the most relevant slots, enhancing efficiency.
- **Scalability**: The use of Tucker Decomposition improves the scalability of the method, allowing it to handle larger models effectively.
- **Experiments**: The experiments demonstrate promising results, achieving comparable performance to MoE models of similar scale while maintaining greater memory efficiency.

### Weaknesses
Although the idea presented in this paper is novel, the experimental performance assessment shows some limitations:

1. **Lack of a Proper Baseline**: The authors do not use a well-established MoE baseline to evaluate the performance of their method. Since UltraMem is proposed as a memory-efficient alternative to MoE, it would be beneficial to compare it against real-world MoE implementations from existing open-source models, providing a more comprehensive analysis. The absence of a direct comparison with a widely recognized MoE model makes it difficult to ascertain the true advantages of UltraMem in practical scenarios. For example, comparing against models like Switch Transformers or similar architectures would provide a clearer picture of its relative performance.

2. **Limited Experiments with Popular Models**: The experiments primarily use custom models, limiting the generalizability of the results. It would be valuable to assess UltraMem’s effectiveness on popular open-source models like Llama, Mistral, or others. This is crucial because the performance of a novel method can vary significantly across different model architectures and pre-training datasets. Demonstrating its efficacy on established models would greatly enhance the credibility and applicability of the proposed approach.

3. **Limited Analysis of Sparsity Levels**: The paper could benefit from a deeper investigation into the effects of different sparsity levels on memory efficiency and performance, as this is a key component of UltraMem’s approach. The current analysis lacks a detailed exploration of how varying sparsity levels impact both the computational overhead and the model's accuracy, which is essential for understanding the trade-offs involved in using UltraMem.

### Questions
here are some minor writing issues, such as in Line 094, where it states 'introduce the origin large memory.' These should be easy to address.

My main questions and observations are:

1. **Comparison with Fine-Grained Mixture of Experts**: How does this method compare to fine-grained Mixture of Experts as in [1], where the hidden dimension is split between experts?
2. **Training Speed**: How does UltraMem’s training speed compare to that of MoE?
3. **Placement of UltraMem Blocks**: On what basis were the positions of the UltraMem blocks within the architecture chosen?
4. **Figure Quality**: Improving the quality of the figures and plots would enhance clarity.

**Suggestions**:

1. It would be beneficial to conduct experiments with popular open-source models like Llama-3.2-1B, Mistral, or others.
2. Since Section 3, "Why UltraMem Instead of MoE," discusses UltraMem’s advantages over MoE, it would be valuable to include experiments demonstrating that UltraMem consistently outperforms MoE in real-world scenarios, using a comprehensive baseline model for comparison.
3. Additionally, an ablation study comparing UltraMem's memory efficiency and performance against MoE based on [1] would further strengthen the analysis if applicable.

[1] *Scaling Laws for Fine-Grained Mixture of Experts*.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel layer designed to increase model size efficiently. Specifically, the approach refines the existing PKM method and incorporates TDQKR as a sparse method to enhance performance. Additionally, it proposes implicit value expansion to address memory access challenges in large models. A comparative analysis of memory access between the proposed method and MOE is also provided. Experimental results demonstrate significant performance improvements.

### Strengths
1. The techniques proposed in this paper are novel. On one hand, the paper thoroughly studies the techniques in PKM, offering valuable empirical insights for future research. On the other hand, it integrates algorithms with memory management to address the memory access issue.   
2. The paper includes an efficiency analysis focused on memory access.
3. Experimental results show that the method significantly outperforms existing approaches on large models, being up to six times faster than MOE at the same scale.

### Weaknesses
1. The writing could be improved, particularly since it introduces concepts beyond the domain of algorithms. These should be better explained as background information. For example, the implicit value expansion technique is somewhat confusing when the paper discusses virtual and physical memory, and could benefit from further clarification. Specifically, the paper needs to clarify how the 'virtual' experts are actually implemented in hardware, and how this relates to the physical memory access patterns. The description lacks detail on how the proposed method avoids the overhead of repeatedly loading the same parameters from memory when accessing different virtual experts. A more detailed explanation of the memory layout and access patterns would be beneficial.

2. The experimental results in the main paper do not fully support the claims made in the methods section. First, while the paper asserts that the method improves PKM, there is no direct comparison except for validation loss. The paper should include a direct comparison of training time, memory usage, and throughput with PKM, not just validation loss. Second, although the paper claims that its memory access method outperforms MOE, this is only demonstrated in the appendix. The main table merely shows FLOPs and model parameters, which do not sufficiently illustrate the method's advantages (including the running time). The main paper should include a comparison of inference speed and memory access patterns between the proposed method and MOE, especially under different batch sizes and model sizes. The current presentation makes it difficult to assess the practical benefits of the proposed method.

### Questions
1. The proposed IVE aims to reduce memory access. Given that it handles the general form of matrix multiplication, could it also be applied to MoE or other methods that involve extensive memory access?

### Soundness
3

### Presentation
2

### Contribution
3
