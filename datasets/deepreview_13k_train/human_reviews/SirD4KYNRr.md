# Invariant Attention: Provable Clustering Under Transformations

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Attention mechanisms play a crucial role in state-of-the-art vision architectures, enabling them to rapidly identify relationships between distant image patches. Conventional attention mechanisms do not incorporate other structural properties of images, such as invariance to geometric transformations, instead learning these properties from data. In this paper, we introduce a novel mechanism, Invariant Attention, which, like standard attention, captures image similarity, but with the additional guarantee of being agnostic to geometric transformations. We provide theoretical assurance and empirical verification that invariant attention is far more successful than standard kernel attention on multi-class, transformed vision data, and illustrate its potential to correctly cluster transformed data with intra-class variation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new attention mechanism called invariant attention. The paper shows that the proposed attention has theoretical guarantees and can be applied to solve image clustering problems.

### Strengths
-This paper aims to improve the attention mechanism, which is the foundation in the widely used transformer architecture.

-This paper provides extensive theoretical analysis for the proposed attention mechanism.

### Weaknesses
 -The experiments are not sufficient to support the claims. First, there is no comparison with previous works in the experimental section. Second, there is no quantitative result. Without those, I cannot judge the if the proposed technic is useful or not and the significance of the proposed method.

 -I cannot find the theoretical proof that shows that "the Invariant Attention is far more successful than standard kernel attention". I might miss this part because I am not an expert in theoretical ML.

### Questions
-I cannot find the theoretical proof that shows that "the Invariant Attention is far more successful than standard kernel attention". I might miss this part because I am not an expert in theoretical ML.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an addition to self-attention that is invariant to various transformations. Mainly, while self-attention is based on the similarity between two entities, the proposed method is based on the maximum similarity between transformed samples. Essentially, the framework proposes replacing $k(x,y)$ with $max_{T_1,T_2} k(T_1(x),T_2(y))$. This way, any transformation $T$ applied to samples $x,y$ does not influence the similarity. Additional non-linearities or learnable parameters are ignored. Two results are proved: 1. The proposed invariant attention results in a unique solution (up to transformation) 2. The procedure converges.

### Strengths
Strong Points:

- The invariance of machine learning models is an important topic, useful for generalization and sample efficiency.
- The method seems technically correct.

### Weaknesses
Weak Points:

- There are no details on how to obtain the optimal transformations from 2.6. How to obtain these transformations is crucial. Without an efficient way to obtain them, the proposed method cannot be applied in practice. The lack of a concrete algorithm or practical approach to solve the maximization problem over the transformation group makes the theoretical contribution difficult to assess. It is unclear if the maximization can be solved in closed form or if an iterative optimization method is needed, and in that case, what are the convergence properties and computational costs.

- The method does not involve actual feature learning. It's hard to argue the importance of the method for machine learning methods when there is no actual representation learning happening. The proposed method focuses solely on the similarity calculation between transformed inputs, neglecting the learning of feature representations that are typically a core component of most machine learning models. The lack of feature learning limits the applicability of the method to scenarios where the input features are already well-defined and discriminative.

- The experiments are extremely simple: 6 transformations of the same image or 10 MNIST samples. These might be good for a first step to see that the method/implementation is sound, but more validations are needed for a novel machine learning method. The experiments do not provide sufficient evidence of the method's effectiveness in realistic scenarios. The limited scale and diversity of the datasets used do not allow for a proper evaluation of the method's generalization capabilities and robustness to different types of transformations.

- “Invariant Attention, enforces invariance under unknown transformations of the domain by optimizing over these transformations” How general are the transformations that Invarian Attention can optimize over? What kind of transformations can be optimized in practice? The paper does not specify the limitations of the transformation groups that can be used. It is unclear if the method can handle non-rigid transformations, or if it is limited to a specific set of transformations like affine or Euclidean transformations. This limitation makes it difficult to assess the practical applicability of the method in real-world scenarios where complex transformations are common.

### Questions
Typo? It seems like equation 3.1 needs two indices, one for sample $v_i$ and one for transformation $\tau_j$. Also, the number of samples and number of transformations should be different.

Minor: There are some broken references. E.g “distance given by (??))”

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for calculating attention between images (or image patches), which is invariant to some pre-defined set of transformations. The attention mechanism itself is formulated as kernel attention, and the kernel is constructed to be invariant to a set of transformations. The paper states that iteratively applying their attention mechanism clusters the provided samples into their invariant means, and provides some theoretical guarantees of convergence of this procedure. Authors claim that their findings could help build novel, data-efficient, invariant attention mechanisms implemented into modern vision Transformer networks.

### Strengths
The proposed method has a nice clustering quality, in which it tends to cluster similar images together. This feature is proved theoretically and empirically. However, the proof is questionable.

### Weaknesses
The paper is very poorly written and looks raw. Apart from the large number of typos, and repetitions (which I will list separately), there are some major issues with the statements themselves.

1. The problem of the paper is not clear to me. What are the problems where the Invariant Attention is needed? Will it increase the overall data efficiency of ViT-type models? How is the clustering property helpful in this case? The paper does not clearly articulate the scenarios where invariant attention would be a significant advantage over existing methods. The connection between the clustering property and the claimed benefits for Vision Transformers (ViTs) is not well-established, leaving the reader to speculate about the practical implications.
2. There are no proofs of the theorems and claims, and not even a sketch of the proof or an idea is provided. Though the authors claim to put it in the appendix, it is not possible right now to review the correctness. The definition of “infimal convex combination reach”, which is an important part of the theory, is not provided even on an intuitive level. The lack of proof sketches makes it impossible to assess the validity of the theoretical results. The absence of an intuitive explanation for key concepts like “infimal convex combination reach” further hinders understanding.
3. At the same time, there is a lot of redundancy. Some almost self-evident claims are explained in long, like the fact that the invariant mean is indeed invariant under image transformations, which is evident from its close form. The paper spends excessive time on trivial observations, such as the invariance of the invariant mean, which could be easily deduced from the definition. This unnecessary elaboration distracts from the more critical and less obvious aspects of the method.
4. It is not clearly stated which transformations are admissible. Authors claim that their method works for any transformation set, but provide theoretical guarantees only in the case of the T=SE(2). At the same time, they state that Invariant Attention enforces invariance under unknown transformations of the domain, which is clearly misleading, and the transformation set should be known beforehand to construct the kernel. The paper lacks clarity on the scope of admissible transformations. While claiming generality, the theoretical guarantees are limited to SE(2). The claim about enforcing invariance under *unknown* transformations is misleading, as the transformation set must be known to construct the kernel.
5. The optimization procedure for finding invariant mean is not fully described. How are the transformation vectors \tau_i parametrized in each experiment? Exactly, what parameters are we optimizing, and how? It would be nice to have a clearly described algorithm in the form of pseudo-code or something like that. Also, no information about the time complexity or needed resources is provided in the experiment part. The optimization process for finding the invariant mean is not detailed, specifically how the transformation parameters are represented and updated. The absence of a clear algorithm, pseudo-code, and time complexity analysis makes it difficult to understand the practical implementation and resource requirements.
6. Not a learnable algorithm. Though the authors claim that they are currently working at implementing learnable weights inside Invariant Attention, its real applicability to modern visual transformer models in the presented form is questionable. It requires running an optimization procedure for each attention head and each pair of image patches only to calculate the kernel weights. This is also dependent on the dimension and complexity of the transformation set and will require training separate models for different symmetry groups. The issue is not addressed in the paper. The proposed method requires an optimization procedure for each attention head and image patch pair, making it computationally expensive and potentially impractical for large-scale ViT models. The dependence on the transformation set's dimension and complexity further limits its applicability.
7. Novelty. The kernel attention mechanism was earlier introduced by (Tsai et. al., 2019), and the kernel used in the calculations was described by (Liu et.al, 2021), so the only novel part is in the theoretical results of the paper, which are not significant enough. It is no wonder that we will identify clusters in the data when the data itself is composed of the groups of samples varied through transformations, and we seek to find these exact transformations to match two samples. The paper does not adequately highlight its novelty. The core mechanism and kernel used are based on existing work, with the theoretical results being the only novel aspect. The clustering results are not surprising given the nature of the data and the optimization process.

### Questions
1. Could you describe possible applications of the Invariant Attention for real-world data?
2. Your results (Theorem 3.1) are formulated for SE(2) explicitly. How is that transferable to other groups of transformations?
3. What kind of structural properties are preserved or exploited by Invariant Attention? How will it help in prediction? May invariance to transformations actually harm the prediction quality, when the focus is on orientation, for example? Like classifying the right arrow and left arrow, for example.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents invariant attention that can cluster images invariant to geometric transformations. It introduces an invariant kernel that computes the maximum similarity between two images after optimizing over transformations. This allows computing meaningful attention weights between transformed images. In addition, the paper presents a theoretical foundation for the approach, demonstrating its efficacy through some simple experiments.

### Strengths
1. A new attention mechanism that incorporates invariance properties.
2. The paper provides a solid theoretical foundation for the properties of invariant attention with proof.
3. While the concept of invariance is not a new idea, it remains crucial for the transformer architecture.

### Weaknesses
1. While the paper presents mathematical formulations specific to its method, it's not immediately clear how this approach can be adapted or generalized to ViT or other transformer architectures. The current formulation of invariant attention seems tightly coupled to the specific kernel and optimization process described, making it difficult to directly integrate into existing transformer blocks without significant modifications. This lack of modularity limits its practical applicability.
2. The proposed method is still based on dynamic kernels [1, 2, 3]. Why the kernels based on averaging are better than previous attempts? The paper does not provide a clear comparison to existing dynamic kernel methods, particularly those that utilize averaging or other aggregation techniques. A more detailed analysis of the advantages of the proposed max-similarity kernel over these alternatives is needed. Specifically, it's unclear how the max operation impacts the stability and convergence of the attention mechanism compared to averaging.
3. Current empirical validation is limited - more quantitative experiments ($e.g.,$ overall accuracy over MNIST) would strengthen the claims. In addition,  more qualitative results on complex image datasets ($e.g.,$ CIFAR100) or the impact of downstream tasks would be useful. The experiments are currently limited to simple transformations and do not demonstrate the method's effectiveness on more complex datasets with real-world variability. The lack of quantitative metrics, such as classification accuracy, makes it difficult to assess the practical benefits of the proposed approach. Furthermore, the absence of downstream task evaluation limits the understanding of its potential impact.
4. (Minor) There are numerous instances of "??", likely due to the separate submission of the main text and supplementary material. Also, there are some typos ($e.g.,$ in theorem 4.1, " invariant attention"). The authors should proofread carefully.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
