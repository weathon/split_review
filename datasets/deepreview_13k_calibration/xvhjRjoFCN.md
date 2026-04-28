# BiXT: Perceiving Longer Sequences With Bi-Directional Cross-Attention Transformers

- Decision: Reject
- Avg Score: 4.33
- Scores: 6, 6, 1

## Abstract
We present a novel bi-directional Transformer architecture (\arch) which scales linearly with input size in terms of computational cost and memory consumption, but does not suffer the drop in performance or limitation to only one input modality seen with other efficient Transformer-based approaches. \arch~is inspired by the Perceiver architectures but replaces iterative attention with an efficient bi-directional cross-attention module in which input tokens and latent variables attend to each other simultaneously, leveraging a naturally emerging attention-symmetry between the two. This approach unlocks a key bottleneck experienced by Perceiver-like architectures and enables the processing and interpretation of both semantics (`what') and location (`where') to develop alongside each other over multiple layers -- allowing its direct application to dense and instance-based tasks alike. By combining efficiency with the generality and performance of a full Transformer architecture, \arch~can process longer sequences like point clouds, text or images at higher feature resolutions and achieves competitive performance across a range of tasks like point cloud part segmentation, semantic image segmentation, image classification, hierarchical sequence modeling and document retrieval.\hphantom{l} Our experiments demonstrate that \arch~models outperform larger competitors by leveraging longer sequences more efficiently on vision tasks like classification and segmentation\ignore{ImageNet and ADE20K}, and perform on par with full Transformer variants on sequence modeling and document retrieval -- but require 28\% fewer FLOPs and are up to $8.4\times$ faster.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a bi-directional cross-attention Transformer (BiXT) that can process long sequences efficiently and effectively by using a small set of latent vectors to represent the ‘what’ and input tokens to represent the ‘where’ of the data. At the core of BiXT is the bi-directional cross-attention module that simultaneously refines latent vectors and input tokens. Compared to sequential cross-attention, the bi-directional cross-attention module leverages the symmetry of attention patterns between latent vectors and input tokens to reduce computational cost and memory consumption.  The authors evaluate BiXT on image classification, semantic image segmentation, and point cloud part segmentation.  They show that BiXT outperforms comparable methods in the low-FLOP regime and can easily integrate modality-specific components to improve performance further.

### Strengths
1. The proposed bi-directional cross-attention has a simple and neat design
2. Evaluations are conducted on two modalities, i.e., images and point clouds.
3. The paper is well-written, hence easy to follow

### Weaknesses
1. Despite the simple and neat design, the strength of the proposed method, bi-directional cross-attention, is unclear. Compared to using two uni-directional cross-attention modules sequentially, the system-level accuracy, FLOPs, and memory requirements are all similar (Table 1 on page 6). It is not clear what advantage the bi-directional approach offers over a sequential approach, given that the computational costs are nearly identical. The authors should provide more insight into the specific benefits of their approach, such as reduced parameter count or improved convergence speed, beyond the claim of leveraging symmetry. A more detailed analysis of the attention patterns and their impact on performance is needed to justify the bi-directional design choice.

2. Insufficient comparison with some of the latest vision backbones. The methods in image classification (Table 2) and semantic segmentation (Table 3) are somewhat outdated. Many works were proposed to overcome the quadratic complexity of multi-head self-attention, such as MaxViT [1], BiFormer [2], and especially DualViT [3], which has a very similar design to BiXT. The performances of BiXT are not attractive if these approaches are included in comparison. Why are these methods not comparable with BiXT? Specifically, the lack of comparison with DualViT, which also employs a dual-path architecture, is a significant oversight. The authors should clarify why these methods, especially those with similar architectural designs, are not included in the comparative analysis, and justify the choice of baselines.

3. Lack of experiments with larger models. It is unclear why the comparisons are positioned in a low-FLOP regime (Table 2). BiXT seems not to be specially designed for lightweight models, and the budgets of BiXT-Ti/8 and BiXT-Ti/4 in the final section of Table 2 are sufficient to cover training larger models with more parameters. It may be better to demonstrate the effect of model scaling. The authors should explore the performance of BiXT with larger model sizes and demonstrate its scalability. The current focus on low-FLOP models limits the understanding of the method's potential and its competitiveness with state-of-the-art models.

### Questions
See the weaknesses part. Overall, I appreciate the simple and neat design of the bi-directional cross-attention. Still, I would like more clarification on its strengths and the experimental settings in the rebuttal. I will raise my rating if these concerns are addressed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research paper provides an enhancement to the Perceiver architecture that employs latent queries for the distillation of input tokens. The main novelty introduced is a bidirectional cross-attention module aimed at reducing computational demands. The authors analyze an architecture that iteratively stacks query-to-token and token-to-query cross-attention modules and find symmetry between these two attention values, suggesting that these two iteratively stacked modules can be merged into one. Therefore, a new bidirectional transformer architecture that only scales linearly with the input tokens as a means of dealing with general modal input data. This replacement results in a reduction of computational cost by approximately one-third, compared to iterative stacking cross-attentions, while also achieving higher accuracies.

The improved method demonstrates an impressive 82.0% accuracy for classification tasks on ImageNet-1K using compact models. These models require only a small fraction of the FLOPS compared to the original Perceiver. The paper also provides verification tests on more generalized input modalities, reinforcing the versatility and effectiveness of the proposed enhancements to the Perceiver architecture.

### Strengths
1. The idea of introducing bidirectional attention to replace the iterative stacking cross attention is both innovative and simple. 
2. The way that the authors present their idea is also appreciated. An analog between the latent queries and "what" queries, and that between the input tokens and the "where" information, is first presented. Then, the symmetry between the "what" and "where" tokens are exemplified to suggest the improvement of the bidirectional attention. Overall, I enjoy reading this paper, and it is easy to follow.
3. The bi-directional cross-attention is effective in reducing the computational cost of the Perceiver architecture and increasing its performance. It achieves the same performance with only a fraction of FLOPS.

### Weaknesses
- Despite its effectiveness, the motivation is more from an intuitive analogy of "what" and "where" tokens than a comprehensive theoretical or experimental conclusion. Only an image classification task is presented when analyzing the symmetry between iterative cross attentions between "what" and "where" tokens. There could also exist many others scenarios, where these cross attention value may violate the symmetry property. For example, the “what” tokens would attend to the context background tokens when detecting small object in the image, whereas these attended “where” tokens would more likely to attend to other “what” tokens in the next cross attention. Therefore, it is less convincing to conclude the “symmetry” behavior of the “what” and “where” tokens from a single illustration.
    
- It is surprising and strange in Table 1(a) that the most performance gain is brought by the naive approach that sequentially stacking two cross attentions with reverse orders by exchanging the query and key positions (+ 11 acc); whereas bidirectional only brings in an additional 0.8 acc. This result seems a bit contradictory with the emphasis of the paper on the bi-directional attention. In this regard, a more important part about the reason of the largely improved performance of the sequential cross attention deserves more detailed analysis. Specifically, this phenomenon would highlight the importance of refining the image tokens instead of fixing them as in Perceiver.
    
- The FLOPSs and Params reported in Table 1(a) is confusing. The FLOPSs and Params of bi-directional cross attention are even larger than that of sequential cross attention. However,  it is described that the implementation of bidirectional cross attention saves 1/3 parameters compared to naive sequential cross attention. Results in Table 1(a) contradicts this statement.

### Questions
See the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a Bi-Directional cross-attention to model the interactions of the visual tokens. Experiments on ImageNet1K and ShapeNetPart are performed to evaluate the effectiveness of the proposed method.

### Strengths
1. This paper is well-written and easy to follow.

### Weaknesses
1. The novelty is limited. Cross-attention has been widely used for years and the proposed method is simply some combination of cross-attention operation. The paper does not sufficiently articulate the specific differences or advantages of their bi-directional approach over existing cross-attention mechanisms, especially in terms of the underlying mathematical formulations or algorithmic implementations. It's unclear what specific modifications or insights lead to the claimed efficiency gains.

2. The experimental results are not very impressive. The accuracy on ImageNet is only 82.0, which is not competitive. The paper lacks a thorough comparison against state-of-the-art methods, particularly those that also utilize attention mechanisms. The reported accuracy is not placed in context of the broader landscape of image classification models, and there is no discussion of why the method does not achieve higher accuracy, such as potential limitations in the architecture or training procedure.

### Questions
see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
