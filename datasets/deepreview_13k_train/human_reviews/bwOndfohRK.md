# Neural networks on Symmetric Spaces of Noncompact Type

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Recent works have demonstrated promising performances of neural networks on hyperbolic spaces and symmetric positive definite (SPD) manifolds. These spaces belong to a family of Riemannian manifolds referred to as symmetric spaces of noncompact type. In this paper, we propose a novel approach for developing neural networks on such spaces. Our approach relies on a unified formulation of the distance from a point to a hyperplane on the considered spaces. We show that some existing formulations of the point-to-hyperplane distance can be recovered by our approach under specific settings. Furthermore, we derive a closed-form expression for the point-to-hyperplane distance in higher-rank symmetric spaces of noncompact type equipped with G-invariant Riemannian metrics. The derived distance then serves as a tool to design fully-connected (FC) layers and an attention mechanism for neural networks on the considered spaces. Our approach is validated on challenging benchmarks for image classification, electroencephalogram (EEG) signal classification, image generation, and natural language inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes neural network structures on symmetric spaces of noncompact types, such as hyperbolic spaces or symmetric positive-definite (SPD) matrix manifolds. For this purpose, an expression for the distance between a point and a hyperplane is derived and utilized to generalize the Euclidean fully connected (FC) layer and attention layer. The proposed neural network is applied to various problems to demonstrate its performance advantages.

### Strengths
- The proposed ideas of generalizing FC and attention layer to symmetric spaces are novel and seem reasonable. 
- They are also general enough to incorporate both hyperbolic spaces and SPD manifolds, which are non-Euclidean spaces of interest and frequent use in ML.
- Most mathematical derivations seem rigorous (I could not follow all the details).
- The paper made a great effort to show the empirical benefits of the proposed neural network by considering diverse benchmarks.

### Weaknesses
 - Understanding this paper requires a solid background in the geometry of symmetric spaces, and Section 3.2, in particular, is highly abstract and challenging to follow. This complexity may reduce the paper’s accessibility for a broader machine learning audience. Maybe incorporating the materials about decomposition equations from Appendix G.1 to G.3 in the manuscript, along with an explanation of their significance, would improve readability.
- The methods to forward propagate the FC layer and attention layer are explained, but it is not clearly defined what the inputs, outputs, dimensionalities, and trainable parameters of each layer are. Including equations or diagrams that summarize these details would enhance clarity. Additionally, there is limited discussion on the backward propagation process in each layer, particularly regarding gradient calculations. It would be helpful to specify whether gradient computation is feasible and, if so, describe the method.
- The rationale for considering both PEM and G-invariant metrics, as well as the differences between using each metric is not sufficiently discussed. A brief comparison of PEM and G-invariant metrics, with an overview of their respective strengths and limitations within the proposed neural network architecture, would help readers understand the motivation for including both metrics and their potential effects on network performance.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a framework for calculating point-to-hyperplane distances within symmetric spaces of noncompact type. Building upon this theoretical foundation, the authors propose novel manifold learning blocks tailored for neural networks, particularly designing fully connected (FC) layers and an attention mechanism applicable to these spaces. The paper demonstrates the effectiveness of this approach through numerical experiments, particularly on EEG classification tasks.

### Strengths
1. The work presents a well-constructed theoretical basis by generalizing point-to-hyperplane distance formulations on symmetric spaces of noncompact type, encompassing both hyperbolic and SPD manifolds. This unified approach is a notable advancement that addresses the limitations in existing methodologies which often focus on narrower manifold types (e.g., Nguyen & Yang, 2023). The paper’s theoretical contribution strengthens its foundation, offering a comprehensive framework applicable across various symmetric spaces, potentially enhancing applications in machine learning on non-Euclidean geometries .
2. The experimental results, particularly on EEG datasets, demonstrate the approach’s capability. Despite minor performance gains, the proposed model achieves competitive accuracy, and in some cases, it outperforms existing methods such as EEG-TCNet, Graph-CSPNet, and MBEEGSE. This highlights the framework’s potential for real-world applications in EEG signal processing.

### Weaknesses
Sections 4.5.1 and 4.5.2, which are the core practical contributions of this work, are difficult to follow. While the theoretical sections are clearly presented, the implementation of the proposed FC layers and attention mechanism in symmetric spaces feels briefly discussed and lacks an intuitive explanation. A more thorough discussion, with a step-by-step breakdown or additional illustrative examples, would greatly improve accessibility and clarity. Specifically, the paper does not provide sufficient detail on how the abstract mathematical operations translate into concrete computational steps within a neural network. For example, the construction of the FC layer based on Proposition 4.12 lacks a clear explanation of how the exponential map and the action of the group K are implemented in practice. Similarly, the attention mechanism lacks a detailed explanation of how the attention weights are computed and applied within the non-Euclidean space. The description of the backpropagation process for these layers is also missing, which is crucial for understanding how these layers can be trained effectively. Without these details, it is difficult to assess the practical feasibility and the computational cost of the proposed approach.

### Questions
1. In Line 143, Add references following “Iwasawa decomposition of G” to provide readers with foundational context.
2. In Line 233, Correct “\(\Vert\ldot\Vert\)” to “\Vert\cdot\Vert” for accuracy in notation.
3. In Corollary 4.3, There seems to be an extraneous dot in the formula. 
4. In Definition 4.5, Shouldn’t the definition of “addition” assume an abelian group structure for coherence with traditional addition in symmetric spaces?
5. In Definition 4.7, The formula for “ g = k \exp(\mu) ” in line 342 could benefit from an intuitive explanation.
6. In Proposition 4.12, The construction of the FC layer from this proposition is not immediately intuitive. Adding a diagram or further expanding on its practical implications would help readers grasp the proposed structure better.
7.  Is there complexity analysis for the two proposed blocks. such as in the supp.?

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
The paper presents a new method for defining neural networks on symmetric spaces of noncompact type. The method is derived by deriving consider how hyperplanes are defined in such spaces and how point-to-hyperplane distance can be computed. This follows from expressing inner products via Busemann functions. This is then used for defining neural networks be generalizing the observation that affine functions in Euclidean space can be expressed as a function of a point-to-hyperplane distance. By replacing quantities in Euclidean space with their symmetric space counter parts, linear layers are defined to define neural networks on these spaces.

### Strengths
- The approach provide a novel generalization of defining neural networks in the more general symmetric space of noncompact type. It is very appealing that the approach can be utilized on several types manifolds (Section 4.3)
- The paper provides is mostly written well to explain the technical background of the material (caveat below).
- Experimental results seem promising.

### Weaknesses
 - The connection between the proposed approach and previous ones are not exactly clear. Mostly in how / why the are different (see Questions)
- I think the narrative of eventually defining the FC layers in section 4.5 (and the attention mechanism) could be improved. Particularly, the I feel like the connection of expressing affine functions via point-to-hyperplane distances should be further elaborated (L396-404)



### Questions
Questions / Remarks:

1. What are the specific connection between the proposed formulation versus the previous approaches presented in Table 1. I may be incorrect, but my understanding is that Ganea et al., 2018b is specialized for Hyperbolic spaces; and the b-distance approach is the Busemann function specialized to Hyperbolic spaces via Section 4.3 / Corollary 4.3. Is there a deeper reason why the point-to-hyperplane distances would not reduce to be the same? A reason for this question is that my initial perception was that the proposed look into symmetric spaces generalized the hyperbolic space, and thus when specializing to hyperbolic spaces one should obtain the same distance function. In summary, it would be great if you could provide a detailed summary / comparison for why the distances obtained in Ganea et al. 2018b differs from those obtained through your Busemann function approach.

2. Unsure if it is the original citation for the technique of affine maps as point-to-hyperplane distance functions, but Ganea et al., 2018b cites "Hyperplane margin classifiers on the multinomial manifold" by Lebanon & Lafferty. To this end, it would be useful to add this citation to Section 2.1 and perhaps further elaborate on the historical development of using point-to-hyperplane distances for affine maps.

Typos / Minor Mistakes:
 - Definition of hyperbolic distance is incorrect on Line 106. There is a type in the inner term's denominator. It should be "$(1 - \Vert x \Vert^2)$, the squared is in the wrong position.
 - wFM used on Line 470 before defined (in appendix Line 1192).
 - Missing "." punctuation on Line 425.

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
The paper presents a new formulation for the distance between a point and a hyperplane in symmetric spaces, i.e., spaces that generalize the commonly used hyperbolic spaces and the manifold of SPD matrices. Based on this distance, new FC and attention components of neural networks on such symmetric spaces are proposed. These neural networks are then demonstrated in the context of hyperbolic spaces and the SPD manifold, showing an advantage in performance compared to other existing methods.

### Strengths
- **Solid Mathematical Foundation**: The paper introduces new definitions grounded in a well-developed mathematical framework.
- **New Neural Network Architecture**: The authors propose a new neural network design, including fully connected (FC) layers and an attention mechanism, that operate on symmetric spaces, extending the current capabilities of neural networks in non-Euclidean geometries.

### Weaknesses
 - **Presentation and Organization**: The paper's structure is fragmented, making it challenging to follow and fully appreciate its main contributions. Specifically:
    - **Sections 2 and 3** contain too many short, disconnected paragraphs or subsections that do not establish a cohesive narrative or logical organization. The lack of clear transitions between these short segments makes it difficult to grasp the overall flow of the mathematical development. The reader is left to piece together the connections, which hinders understanding.
    - **Section 4** would benefit from being divided into two distinct parts: one focused on the mathematical framework and the other on the proposed neural network. Since the neural network is the primary outcome, separating these would clarify the focus. The current structure mixes the theoretical underpinnings with the practical application, making it harder to distinguish the core contributions of each.
    - Additional minor structural suggestions:
        - **Section 4.3**: Consider renaming the section titled "Examples" to make its purpose clearer. A more descriptive title would help the reader understand the content of this section.
        - **Figure 2(b)**: Rotating this figure by 90 degrees could improve readability. The current orientation makes it difficult to interpret the figure's content.

- **Experimental Results**: Some limitations in the experimental study reduce the impact of the findings:
    - **Section 5.1**: There are many other datasets with a clearer hierarchical structure that typically benefit more from hyperbolic space representation. For example, gene expression and word-document datasets are often considered as benchmarks of embedding in hyperbolic space. Therefore, the choice of CIFAR-10 and CIFAR-100 as benchmarks is questionable and should be explained, especially considering the marginal improvements reported in Table 2. The lack of a clear rationale for using these datasets weakens the experimental validation.
    - **Section 5.2**: There are multiple differences between the proposed methods and the baselines, with several moving parts. It remains unclear which component contributes most to the observed (marginal) improvement. Consider conducting an ablation study to isolate the effects of the different components. This would help clarify which aspects are most responsible for the performance improvements. Without such an analysis, it is difficult to determine the true source of the gains.
    - **Runtime Analysis**: Since the accuracy improvements are relatively small, including runtime metrics alongside accuracy would provide a fuller perspective on the method's practical benefits. The computational cost of the proposed method needs to be considered to assess its overall utility.

- **Limitations Statement**: The limitation statement at the end is very specific and could be extended to cover broader aspects of the proposed framework, e.g., scalability and practical applicability. The current statement is too narrow and does not address all potential limitations of the method.

### Questions
- Could the authors provide clarification on the choice of CIFAR-10 and CIFAR-100 datasets in light of the results and the available alternative datasets with stronger hierarchical structures?
- Please explain why more hierarchical datasets were not included.

### Soundness
2

### Presentation
1

### Contribution
3
