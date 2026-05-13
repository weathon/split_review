# Gated Delta Networks: Improving Mamba2 with Delta Rule

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited.  To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta update rule for precise memory modifications. We observe that these mechanisms are complementary—gating enables rapid memory erasure while the delta rule facilitates targeted updates. Building on this insight, we introduce the gated delta rule and develop a parallel training algorithm optimized for modern hardware. Our proposed architecture, Gated DeltaNet, consistently surpasses existing models like Mamba2 and DeltaNet across multiple benchmarks, including language modeling, common-sense reasoning, in-context retrieval, length extrapolation, and long-context understanding. We further enhance performance by developing hybrid architectures that combine Gated DeltaNet layers with sliding window attention or Mamba2 layers, achieving both improved training efficiency and superior task performance

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
To mitigate quadratic scaling with sequence length of standard Transformers, Linear Transformers with kernelized dot-product linear attention are proposed. In this paper, the authors propose Gated DeltaNet, which leverages the gating mechanism from Mamba2 and the delta update rule from DeltaNet. The hybrid architecture of Gated DeltaNet, SWA, Mamba2 layers outperforms baselines in language modeling, reasoning, and recall-intensive tasks.

### Strengths
- This paper is well-organized and clearly written.
- Their presentation, especially highlighting contribution points, was good to understand and follow.
- The proposed method is simple, but seems effective in various tasks.

### Weaknesses
 - How are the baselines trained? Those few-shot performance look a little lower than other papers (like Mamba). And also, could you compare with some other well-pretrained Transformer models to show the effectiveness of the proposed architecture?
- State sizes of Gated DeltaNet H1 and H2 seem much larger than all the other baselines---models that use SWA have the larger sizes. In case of Gated DeltaNet (with 256 state size) performance looks similar to Mamba2 and DeltaNet, where the gated delta rule can be seen as having minimal impact on performance. Also, as Samba already shows a very good performance, I guess the performance gain would come from hybrid structure, not from gated delta rule itself.
- I suggested the authors to compare efficiency of models, which is an important factor for a new architecture.
- In length extrapolation experiments, why does Gated DeltaNet show robust performance while Mamba2 and DeltaNet show higher perplexity as the length grows. Gated DeltaNet is the combination of both methods.

### Questions
- There are some typos in Section 3.1 (e.g., L.239 or L.256).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the limitations of linear Transformers in handling long sequences and recall-intensive tasks. While linear Transformers reduce computational complexity compared to traditional Transformers, they often struggle with tasks that require remembering and recalling information over extended contexts. Authors focus on (1) Gating Mechanism: Allows the model to adaptively forget irrelevant information by applying a dynamic decay to the hidden state. This enables fast and efficient memory erasure but may not precisely target specific memories. (2) Delta Update Rule: Enables precise and targeted updates to memory by selectively replacing old key-value pairs with new ones, to propose a new approach called Gated Delta Rule, which combines the strengths of both mechanisms.

### Strengths
## Strengths

1. This paper propose a new linear Transformer that implements the gated delta rule, allowing for more effective memory management over long sequences.
2. The authors extend the delta rule's parallel algorithm to incorporate gating, ensuring hardware-efficient training using chunkwise parallelism and tensor core acceleration.
3. Experiments demonstrate that Gated DeltaNet can outperforms existing models like Mamba2 (which uses gating) and DeltaNet (which uses the delta rule) on various tasks.

### Weaknesses
## Weakness

1. The paper lacks an in-depth theoretical analysis of why the combination of gating and the delta rule improves memory capacity and how it affects the model's ability to handle long sequences, providing theoretical insights regarding the memory retention and forgetting properties of GatedDeltaNet would strengthen the paper's contributions. Specifically, the paper does not delve into the mathematical properties of the gating mechanism in conjunction with the delta update. It would be beneficial to analyze how the gating function's parameters influence the memory update and decay process. For instance, what is the impact of different gating function shapes (e.g., sigmoid, tanh) on the model's ability to retain relevant information while discarding irrelevant data? Furthermore, a formal analysis of the stability of the update rule, particularly in the context of long sequences, is missing. This analysis should explore whether the combined update rule prevents the vanishing or exploding gradient problem, which is crucial for effective training.

2. Although the authors claims that Gated DeltaNet generalizes better to longer sequences than DeltaNet / Mamba2, the experimental results on length extrapolation are limited (only one analysis on PG19). The evaluation focuses on sequences up to a certain length without exploring the model's performance on substantially longer sequences. Expanding the extrapolation experiments to include much longer sequences would provide stronger evidence. The current evaluation does not sufficiently demonstrate the model's ability to handle very long-range dependencies. For example, the paper could include tasks that require the model to remember information across thousands or tens of thousands of tokens. Moreover, the paper should include a more diverse set of extrapolation tasks, such as those involving structured data or complex reasoning, to show the generalizability of the proposed method.

### Questions
1. Could you provide quantitative metrics on the computational efficiency of Gated DeltaNet compared to other models, such as training/inference speed and memory consumption?

I will read the rebuttal in the discussion period and adjust my evaluation.

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
The paper introduces Gated DeltaNet as an enhancement to linear transformers, combining two memory management mechanisms: the gating mechanism from Mamba2 and the delta update rule from DeltaNet. Linear transformers, known for efficiency, often struggle with recall-intensive tasks. The gating mechanism enables flexible, rapid memory clearance, while the delta rule allows for targeted updates. By integrating these, Gated DeltaNet achieves both efficient memory erasure and selective memory retention, addressing limitations faced by linear transformers in handling extended sequences and complex memory recall tasks.

The proposed model demonstrates superior performance compared to Mamba2 and DeltaNet across various tasks, including language modeling, commonsense reasoning, and associative-recall. Additionally, the study explores hybrid models that combine Gated DeltaNet with sliding window attention or Mamba2 layers to further improve retrieval capacity. Extensive experiments validate the effectiveness of the gated delta rule, highlighting its advantage in managing memory over long sequences and maintaining hardware efficiency through chunkwise parallelism for training.

### Strengths
This paper gives detailed and structured introduction to a series of d^2 linear attention model e.g. GLA, DeltaNet and Mamba2, following a newly proposed Gated DeltaRule as its main contribution.  The improvements of delta rule can be considered as one strength in this paper, with a scalar-values decay term for easy training. Also, the UT transform for using Tensor Core with high-efficiency serves as a mitigation to the extended WY representation is unique, yet could be an individual interest to the community.

 The motivation for combining gating with the delta rule is compelling, showing how these two mechanisms address specific weaknesses in memory management. The writing in this paper is generally clear, structured, and detailed.

### Weaknesses
One weakness of the paper lies in the use of a scalar-value decay term, which, while intended to enhance memory management, does not consistently outperform Mamba2 in associative recall tasks. As seen in Table 2, although Gated DeltaNet shows a slight improvement in average accuracy across six associative recall tasks, Mamba2 still performs better in three of them. This raises questions about the efficacy of the decay term in improving recall performance. Intuitively, adding a decay term implies a rigid truncation of information over time, which may not necessarily benefit associative recall tasks that rely on longer memory retention. Providing case studies that track changes in hidden states during tasks could clarify the impact of the decay term on associative recall. Such insights would help to understand how the decay term influences memory retention and retrieval processes within the model, making the improvement more transparent and justifiable.

Another issue concerns the length extrapolation experiments involving DeltaNet. The paper would benefit from clearly labeling the four model types and specifying the experimental setup in detail. For example, it appears that DeltaNet performs even worse than Mamba in extrapolation, which contradicts findings from other experiments within the paper. This inconsistency suggests that additional clarification on the model configurations, including whether any of the models employed a hybrid architecture, is necessary. Given that attention mechanisms offer significant advantages in associative recall capabilities, it is essential to specify if the models were using sliding window attention or other hybrid elements, as this could substantially influence the results and better contextualize the model comparisons.

Typo:
- line 256, "As we can see in ." need a reference?
- line 313, 319, 334, "Training" -> "Training."
- line 374, "State size is strongly correlated with final performance." need a \paragraph{}.

### Questions
1. Is there any visualized results or case studies about why the introduction of scalar value decay term resulted in following improvements in downstream task like AR?

2. How about the training / inference speed e.g. throughput comparing with DeltaNet, Mamba2, and hybrid model e.g. Samba?

3. Does the UT transform really helps the acceleration of training? How about some ablation studies on w/ and w/o the UT transform?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes Gated DeltaNet, a novel model architecture combing gated recurrent mechanism and Delta update rule. Gated DeltaNet support chunk-parallel computation as efficiency optimization. Besides simple Gated DeltaNet, the paper also discuses the hybrid design with Sliding-Window Attention or Mamba layers.

In experiments, the paper shows strong modeling capability of Gated DeltaNet. First, Gated DeltaNet outperforms Transformer and other linear-complexity models in language modeling and zero-shot downstream tasks. Second, Gated DeltaNet shows a strong length-extrapolation ability in language modeling. In ablation studies, the paper makes comparisons with other design choices.

### Strengths
1. The paper is well written, showing the connection and improvement with previous works.

2. Gated DeltaNet makes kernel optimization to achieve better training and inference throughput, which is essential for downstream application and community reproduction.

3. Gated DeltaNet shows strong performance than other linear-complexity models, which is a good academic contribution in model architecture area.

### Weaknesses
1. This paper does not discuss the performance on long-context tasks. Since the quadratic complexity only matters when the sequence is long, long-context performance is the most important metric for linear-complexity models.

2. This paper does not compare Gated DeltaNet with other linear-complexity models on training and inference efficiency. Since Delta-rule is harder for parallel computation, there may be a trade-off between performance and computation cost.

### Questions
How do you think the application scenario of linear-complexity models? Since it is going to be common sense that linear complexity makes a sacrifice on long-context capability.

### Soundness
3

### Presentation
3

### Contribution
3
