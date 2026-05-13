# Supervised and Semi-Supervised Diffusion Maps with Label-Driven Diffusion

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
In this paper, we introduce Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM), which transform the well-known unsupervised dimensionality reduction algorithm, Diffusion Maps, into supervised and semi-supervised learning tools. The proposed methods, SDM and SSDM, are based on our new approach that treats the labels as a second view of the data. This unique framework allows us to incorporate ideas from multi-view learning. Specifically, we propose constructing two affinity kernels corresponding to the data and the labels. We then propose a multiplicative interpolation scheme of the two kernels, whose purpose is twofold. First, our scheme extracts the common structure underlying the data and the labels by defining a diffusion process driven by the data and the labels. This label-driven diffusion produces an embedding that emphasizes the properties relevant to the label-related task. Second, the proposed interpolation scheme balances the influence of the two kernels. We show on multiple benchmark datasets that the embedding learned by SDM and SSDM is more effective in downstream regression and classification tasks than existing unsupervised, supervised, and semi-supervised nonlinear dimension reduction methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper extends traditional diffusion maps by integrating label information to create supervised and semi-supervised versions, known as Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM). The core algorithm involves constructing two affinity kernels—one for the data and one for the labels. These affinity matrices are then combined using an alternating diffusion (AD) approach, which extracts the shared structure between data and labels, producing embeddings that incorporate label information. Theoretical analysis and experimental results on several real datasets demonstrate that the proposed methods outperform existing unsupervised and supervised algorithms in classification accuracy and regression error.

### Strengths
The strengths of the paper are as follows:

- Presentation: The paper is well-written and easy to follow, with clear introductions to the background, problem formulation, and related work. The proposed method is thoroughly described and demonstrated.

- Originality: The proposed method is both novel and conceptually sound. The problem is well-motivated by highlighting that unsupervised manifold learning does not fully utilize label information, often resulting in sub-optimal performance. Introducing the alternating diffusion approach with an additional parameter $t$ for fusing and balancing data and label information is an effective and innovative idea.

- Theory: The theoretical analysis, while based on several fundamental assumptions, is valuable and provides important insights.

### Weaknesses
My concern to this paper mainly falls onto the following three aspects:

- **Lack of Discussion on the Geometric Similarity Assumption**: A fundamental assumption in the proposed method is the strong geometric similarity between the data and labels. However, it is unclear how this similarity impacts the method's performance. For instance, if the labels are only weakly correlated with the data geometry, would the proposed method perform worse than traditional unsupervised algorithms? An empirical or theoretical study on this factor would be invaluable as a guide for real-world applications. Currently, no such study exists, and all experiments seem to assume this strong similarity.

- **Computational Complexity and Dataset Scale**: Given that the computational complexity increases with training data size, this could be a critical factor in determining the method’s applicability. A quantitative complexity analysis of the proposed method, and possibly other baseline methods, would be beneficial, in addition to the runtime reported in Table 5. Moreover, the real datasets in the paper are relatively small (<4k samples), which may not reflect the scale commonly encountered in real applications. It would be informative to evaluate both performance and runtime as dataset size grows, particularly examining the differences between SDM and SSDM under larger-scale conditions.

- **Performance Comparison between SDM and SSDM**: Given that computational complexity is crucial and that SSDM is more computationally efficient than SDM, a direct performance comparison between SDM and SSDM would be valuable. It’s important to understand if SDM consistently outperforms SSDM despite the higher complexity, or if there are cases where SSDM could exceed SDM’s performance—particularly when the geometry of the test data is beneficial in constructing the data affinity matrix.

### Questions
See weakness above.

### Soundness
3

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
This paper introduces two novel methods for manifold learning: Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM), which extend the traditional Diffusion Maps framework to supervised and semi-supervised settings. Unlike prior methods, SDM and SSDM treat labels as a secondary data modality, employing principles from multimodal manifold learning to better capture the structure of labeled data. The authors propose constructing a separate affinity kernel for the labels, enabling the model to represent the geometry of labels along with the data. Using an Alternating Diffusion (AD) approach, they introduce a kernel interpolation scheme that combines data and label affinity kernels. This creates a “label-driven diffusion” process, approximating a continuous two-step diffusion on the manifold that emphasizes features relevant to the task. 

The main contributions are as follows: 

1. Multi-View Approach: SDM and SSDM incorporate labels as an additional information source, enhancing the manifold learning process. 
2. New Kernel Interpolation Scheme: A method for combining affinity kernels to reveal shared structures between data and labels while controlling their respective contributions. 
3. Experimental Validation: Results show that SDM and SSDM outperform existing nonlinear manifold learning methods across several benchmark datasets, highlighting their effectiveness.

### Strengths
This paper introduces Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM), extending Diffusion Maps to supervised and semi-supervised learning by treating labels as an additional data modality. This innovative approach uses a two-step diffusion process, first on the labels and then on the data, enabling a “label-driven diffusion” that highlights task-relevant structures. The paper presents a rigorous kernel interpolation scheme to merge data and label affinities, supported by strong theoretical justification and validated through experiments on benchmark datasets. The methodology is clear, original, and impactful, making this a valuable contribution to manifold learning.

### Weaknesses
Diffusion processes are often computationally intensive, especially on large datasets. The paper would benefit from an analysis of the scalability of the proposed methods. Discussing time complexity, memory requirements, and potential optimizations or parallelization strategies could make this approach more practical for large-scale applications. Furthermore, a comparison of computational costs between SDM/SSDM and other manifold learning methods would provide a clearer picture of their efficiency.

### Questions
see weaknesses

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
The paper proposes Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM) as extensions of the classical Diffusion Maps algorithm. By treating labels as a secondary view of the data, the authors employ a multi-view learning framework to enhance the dimensionality reduction process. The proposed methods introduce a multiplicative kernel interpolation scheme to integrate data and label information. Experimental results on benchmark datasets are used to demonstrate the effectiveness of SDM and SSDM compared to existing manifold learning techniques.

### Strengths
1) The paper presents a clear motivation for addressing the limitations of traditional manifold learning methods that lack mechanisms to incorporate label information.
2) Treating labels as an additional data modality and leveraging a multi-view framework can provide some new insights to the community.
3) Both empirical and theoretical analyses are provided to justify the proposed method.

### Weaknesses
1. While the multi-view framework and the label-driven diffusion are interesting, they rely heavily on existing concepts, such as Alternating Diffusion and classical kernel methods. Thus, the novelty of the proposed SDM and SSDM methods appears limited, as they mainly extend well-established techniques. The core idea of using labels as a secondary view is not entirely new, as similar concepts have been explored in other multi-view learning contexts. The specific implementation of multiplicative kernel interpolation, while effective, does not introduce a fundamentally novel mathematical framework, but rather adapts existing kernel combination techniques. The paper should more clearly delineate the specific novel contributions beyond the application of existing methods to this particular problem.
2. Given that the paper relies heavily on older references with minimal discussion of more contemporary work, are there recent advancements in manifold learning? The paper does not adequately address recent developments in manifold learning, particularly those that incorporate label information or address scalability issues. There are newer methods that may offer better performance or efficiency, and these should be discussed and compared against. For example, methods that use deep learning for manifold learning or those that focus on preserving local structure in high-dimensional spaces should be considered. The lack of discussion on these recent advancements makes it difficult to assess the true contribution of the proposed methods.
3. There is no discussion on how the proposed methods scale with larger datasets (e.g. MNIST [1] with 70000 samples) or in higher-dimensional spaces (Toxicity [2] with 1203 features), which is crucial for practical applications. The computational complexity of the proposed methods is not analyzed, and the paper lacks any empirical evidence of the methods' performance on large datasets. This is a significant limitation, as many real-world datasets are large and high-dimensional. The paper should include a detailed analysis of the time and space complexity of the proposed methods and provide experimental results on larger datasets to demonstrate their scalability.
4. The related work section lacks a comprehensive overview in multi-view learning [3,4]. The related work section does not adequately cover the breadth of multi-view learning techniques. The paper should discuss other relevant methods, such as co-training, canonical correlation analysis (CCA), and multi-view deep learning approaches, to provide a more complete context for the proposed methods. The absence of these discussions limits the reader's understanding of the novelty and contribution of the proposed approach within the broader field of multi-view learning.
5. The computational complexity of the proposed methods is not well-handled, with larger computational complexity compared with other methods. The paper does not provide a clear analysis of the computational complexity of the proposed methods. It is important to understand how the computational cost scales with the number of samples and the dimensionality of the data. A comparison with the computational complexity of other manifold learning methods should also be provided to assess the efficiency of the proposed approach.

### Questions
Please refer to the weakness list.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes constructing two affinity kernels corresponding to the data and the labels. The authors then propose a multiplicative interpolation scheme of the two kernels, whose purpose is twofold. First, their scheme extracts the common structure underlying the data and the labels by defining a diffusion process driven by the data and the labels. This label-driven diffusion produces an embedding that emphasizes the properties relevant to the label-related task. Second, the proposed interpolation scheme balances the influence of the two kernels. We show on multiple benchmark datasets that the embedding learned by SDM and SSDM is more effective in downstream regression and classification tasks than existing unsupervised, supervised, and semi-supervised nonlinear dimension reduction methods.

### Strengths
1. Originality. This paper presents Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM), which are supervised and semi-supervised variants of Diffusion Maps. Unlike existing supervised and semi-supervised manifold learning methods,
the authors present a new approach, where they view the labels as an additional data modality and employ concepts of multimodal manifold learning. Concretely, the authors propose to construct a separate affinity kernel for the labels, allowing us to capture the underlying geometry of the labels in addition to that of the data. 
2. Quality and Clarity. There are no technical errors, and the presentation and writing are satisfied.
3. Significance. The authors show on multiple benchmark datasets that the embedding learned by SDM and SSDM is more effective in downstream regression and classification tasks than existing unsupervised, supervised, and semi-supervised nonlinear dimension reduction methods.

### Weaknesses
I am absolutely not in this field and the comments from me are not relatively professional. The comments in the following are just raised from the presentation or organization.                       

1. The authors are expected to give the figure of the framework based on Supervised Diffusion Maps (SDM) and Semi-Supervised Diffusion Maps (SSDM) and highlight the major differences between the proposed method and the most related work.

2. The authors use a new subsection termed alternating diffusion in Background part. However, there are just small amount of lines in this subsection. I think the authors can further improve this aspect for this paper.

3. For the evaluation results, the authors report NMSE for regression and Misclassification Rate for classification based on S/SDM for supervised SDM and semi-supervised SSDM on the given datasets. I think the authors can add more datasets for comparison in the experiment.

4. In the conclusion part, the authors explore the futher work by exploring the utility and adaptation of fusion of data and label kenels. The authors can add a new subsection to discuss the futher work in details here.

### Questions
1. Why the authors reduce the original data dimensionality to a range of 1 to 30 dimensions for each dataset and algorithm in the experiment?

2. Why the authors choose Euclidean distance in the data kernel and angular distance in the label kernel?

### Soundness
2

### Presentation
2

### Contribution
2
