# Adaptive Pruning of Pretrained Transformer via Differential Inclusions

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Large transformers have demonstrated remarkable success, making it necessary to compress these models to reduce inference costs while preserving their performance. Current compression algorithms prune transformers at fixed compression ratios, requiring a unique pruning process for each ratio, which results in high computational costs. In contrast, we propose pruning of pretrained transformers at any desired ratio within a single pruning stage, based on a differential inclusion for a mask parameter. This dynamic can generate the whole regularization solution path of the mask parameter, whose support set identifies the network structure. Therefore, the solution path identifies a Transformer weight family with various sparsity levels, offering greater flexibility and customization.In this paper, weintroduce such an effective pruning method, termed SPP (Solution Path Pruning). To achieve effective pruning, we segment the transformers into paired modules, including query-key pairs, value-projection pairs, and sequential linear layers, and apply low-rank compression to these pairs, maintaining the output structure while enabling structural compression within the inner states. Extensive experiments conducted on various well-known transformer backbones have demonstrated the efficacy of SPP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to prune pretrained transformers at any desired ratio within a single pruning stage. The proposed method enjoys a theoretical analysis to guarantee the global convergence. Extensive experiments validate the effectiveness of the proposed method.

### Strengths
1. This paper is motivated well. The method for any desired pruning ratio is needed in many real-world applications. And the proposed method is able to achieve this.
2. This paper identifies the limitation of Lasso and develops a differential inclusion-based method to achieve various compression ratio pruning. 
3. There is a sound theoretical analysis to guarantee the global convergence of the method. A detailed proof is included in the appendix.
4. Experimental results are strong. Many experiments are conducted, including ViTs for image classification, CLIP, and even large language models.

### Weaknesses
1. Although the authors claim the proposed method significantly reducing the cost of model pruning. The training cost is not reported in this paper. It is better to introduce how long the search stage is. And make a comparison for training cost between different methods.
2. The ablation studies are weak. Experiments demonstrate the strong performance of the proposed SPP. But it is hard for the reader to figure out why the proposed method is effective. More ablation studies are needed. For example, make comparison for weight-based pruning and mask-based pruning. Why does the weight-based pruning not be applicable to the Transformer? What if using Lasso for the searching stage. By optimizating Eq. 7, Lasso is able to achieve different level of sparsity during training.

### Questions
1. For pruning large language models, why to combine the propsed SPP with the RIA pruning metric? However, pruning CV models (ViTs and CLIP) does not use pruning metric. What is the difference between pruning CV models and LLMs?
2. In line 207, it seems that the dimension is d_1 rather than d.

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
3

### Summary
The paper proposes SPP (Solution Path Pruning), a novel approach to mask-based pruning for pretrained transformers. SPP leverages differential inclusions to create a dynamic solution path that produces a range of sparsity levels in a single pruning stage, eliminating the need for multiple retraining steps for different compression ratios. The method applies fine-grained, pair-wise shared masks across transformer layers, including attention heads and MLP layers, achieving high flexibility and model performance retention. SPP is tested on various datasets and transformer backbones, showing efficiency improvements with minimal accuracy loss.

### Strengths
**Adaptive Solution Path for Pruning**  
   - Unlike traditional mask-based pruning, SPP generates models with different sparsity levels in a single pruning run, allowing for a Transformer Weight Family adaptable to varying hardware or performance needs without retraining.

**Flexible, Fine-Grained Pruning Strategy**  
   - SPP’s pair-wise shared mask strategy applies pruning at the smallest functional units within transformers (e.g., query-key and value-output pairs), allowing for greater flexibility and effectiveness in compression compared to conventional methods.

**Reduced Computational Cost**  
   - The SPP method reduces the need for repeated pruning stages, resulting in significant cost savings, especially for large-scale transformer models.

### Weaknesses
 **Marginal Improvement Over Existing Methods**
   - Although the method introduces adaptive pruning, it does not fundamentally change the mask-based pruning paradigm. The improvements, while novel in terms of execution, may appear incremental compared to existing mask-based and structural pruning strategies. The core idea of using differential inclusions to generate a solution path is interesting, but the practical benefits in terms of final model performance and compression ratios need to be more substantial to justify the added complexity. The paper needs to demonstrate a clear advantage over simpler, more established methods, especially in scenarios where the adaptive nature of the pruning is not a critical requirement.

**Lack of Broad Comparison with Other Mask-Based Methods**
   - The paper does not provide an in-depth comparison with other advanced mask-based pruning techniques, making it difficult to fully assess SPP's advantages in performance and efficiency. Specifically, the paper lacks a thorough analysis against methods that also explore fine-grained pruning or those that use similar mask-sharing strategies. A more comprehensive comparison should include metrics such as the number of parameters pruned, the computational cost of pruning, and the final model performance across a range of sparsity levels. Without this, it is hard to determine if the method offers a significant improvement over existing techniques.

### Questions
- How does the method scale to very large transformers (e.g., GPT-3 scale)?
- What is the stability of the solution path across different random seeds?
- How sensitive is the method to the choice of hyperparameters κ and λ?
- Can this method be extended to dynamic/runtime pruning scenarios?

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
3

### Summary
This paper presents a pruning method of pretrained transformers at any desired ratio within a single pruning stage, based on a differential inclusion for a mask parameter.

### Strengths
1.	Clear motivation.
2.	The theoretical proof and experiment are quite sufficient.

### Weaknesses
1.  The results of ablation studies are insufficient to demonstrate the effectiveness of the proposed method for the following reasons: 1) For DeiT-Small and Swin-Tiny models, the proposed SPP achieves higher accuracy with more parameters and higher or equal FLOPS, which does not indicate that SPP is superior. 2) Conducting experiments solely with the DessiLBI method lacks generalizability. 
2.  Figure 1 and tables lack legends and comments.
3.  "FLOPs" is generally not written as "Flops" when used as an abbreviation for "floating point operations".

### Questions
1.	The manuscript does not describe how low-rank compression can be applied to paired modules of transformers.
2.	The reviewer is concerned about the actual running time of the proposed method and how much its efficiency improves compared to methods with a single pruning rate.
3.	There seem to be some errors in the details of the manuscript, for example, "Specifically, note that for each element i, V (i) ≤ 1 if V (i) = 0, and is equal to 1 when it becomes non-zeros".

### Soundness
3

### Presentation
3

### Contribution
3
