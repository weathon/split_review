# Fast Crystal Tensor Property Prediction: A General O(3)-Equivariant Framework Based on Polar Decomposition

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Predicting the tensor properties of crystalline materials is a fundamental task in materials science. Unlike single-value property prediction, which is inherently invariant, tensor property prediction requires maintaining $O(3)$ group tensor equivariance. This equivariance constraint often introduces tremendous computational costs, necessitating specialized designs for effective and efficient predictions. 
To address this limitation, we propose a general $O(3)$-equivariant framework for fast crystal tensor property prediction, called {\em GoeCTP}. 
Our framework is efficient as it does not need to impose equivalence constraints onto the network architecture. Instead, {\em GoeCTP} captures the tensor equivariance with a simple external rotation and reflection (R\&R) module based on polar decomposition. The crafted external R\&R module can rotate and reflect the crystal into an invariant standardized crystal position in space without introducing extra computational cost. We show that {\em GoeCTP} is general as it is a plug-and-play module that can be smoothly integrated with any existing single-value property prediction framework for predicting tensor properties. Experimental results indicate that {\em GoeCTP} achieves higher prediction performance and runs 13$\times$ faster compared to existing state-of-the-art methods in elastic benchmarking datasets, underscoring its effectiveness and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents GoeCTP, a novel O(3)-equivariant framework for predicting tensor properties of crystalline materials. The key innovation is using polar decomposition to handle tensor equivariance through an external rotation and reflection (R&R) module, rather than building it into the network architecture.

### Strengths
1. Novel use of polar decomposition for handling tensor equivariance
2. Strong theoretical foundation with clear mathematical proofs
3. Clear illustrations and explanations of complex concepts

### Weaknesses
1. Limited discussion of potential limitations or failure cases
2. Only two datasets are used.1.

### Questions
1. What are the limitations of using polar decomposition for this application? Are there edge cases where it might not work well?

2. How does the method perform on different types of crystal structures beyond those tested?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose an O(3)-equivariant framework, GoeCTP, for crystal tensor prediction. GoeCTP utilizes polar decomposition to rotate and reflect the crystal into a standardized invariant position in space. The orthogonal matrix obtained from the polar decomposition is used to achieve equivariant tensor property predictions. The GoeCTP method achieves higher quality prediction results and runs more than 13× faster on the elastic benchmarking dataset.

### Strengths
1. GoeCTP is plug-and-play as it can be readily integrated with any existing single-value property prediction network for predicting tensor properties. 
2. GoeCTP does not introduce excessive computational overhead.

### Weaknesses
1. The article has limited contributions in terms of methodological innovation, as the methods and main structure used by the authors are derived from DiffCSP++[1] and Comformer[2]. For detail, the polar decomposition method used may have been inspired by DiffCSP++, while the code implementation adopts the structure of Comformer.   
2. The article does not clearly explain why Equation 2 needs to be satisfied. It is suggested that the authors provide more background or explanation regarding the physical or mathematical significance of Equation 2 in relation to tensor property prediction. This would help readers better understand the importance of this equation within the proposed framework.   
3. There are some citation issues in lines 339-340 of the article.

### Questions
1. Is it the case that all tensor properties need to satisfy Equation 2, or only certain tensor properties? Why？Please provide specific examples of tensor properties, indicating which properties need to satisfy Equation 2 and which do not, along with an explanation of the underlying reasons for this distinction. This would help deepen the understanding of the method's applicability and limitations.

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
4

### Summary
This paper proposes a novel approach intended to achieve O(3) tensorial equivariance by transforming crystal structures into standardized positions, so that neural networks do not need to satisfy equivariance during prediction. The invariant predictions are then mapped back to equivariant outputs. While the goal of O(3) equivariant predictions is notable, prior work has already addressed this problem with established solutions, including ETGNN's vector outer product and GMTNet's equivariant networks. Additionally, existing techniques, such as frame averaging and minimal frame averaging, can be employed to achieve O(3) tensor equivariance effectively. Moreover, this work does not consider space group constraints, which are crucial for tensorial properties in crystallography. As such, the novelty and contribution of this work are limited and do not meet the standards for acceptance at current form.

### Strengths
1. An alternative approach is proposed to achieve tensor O(3) equivariance. If used, it is faster than equivariant network based O(3) equivariant predictions like GMTNet.

### Weaknesses
 1. **Lack of Consideration for Space Group Constraints**

Space group constraints, which are fundamental in determining the tensor properties of crystals, are not accounted for in this work. No experimental results are provided to verify whether the proposed method can generate predictions that align with these constraints. Crystals exhibit unique tensor characteristics that are intrinsically tied to their crystal class or space group, and ignoring these symmetries is a significant oversight. For example, in cubic systems, the dielectric tensor should have only diagonal elements, and any off-diagonal components should be zero. The method needs to explicitly demonstrate that it respects these constraints, rather than simply being invariant to space group operations.

2. **Limited Improvement in Performance**

The integration of the proposed module does not enhance eComformer’s performance beyond achieving O(3) equivariance, as shown in Table 4. Other alternatives, such as ETGNN, frame averaging, and minimal frame averaging, also achieve O(3) equivariance but were not discussed or compared in this work. A more thorough discussion and comparative analysis of technical contributions and novelty would be beneficial. Specifically, the performance gains over minimal frame averaging appear marginal, suggesting that the core contribution is limited.

3. **Absence of Experiments on Piezoelectric Tensors**

The work lacks experiments on piezoelectric tensors, which are especially sensitive to space group constraints. Including these experiments would strengthen the evaluation of the proposed approach’s applicability across tensorial properties with varying sensitivity to symmetry constraints. Piezoelectric tensors often have more complex symmetry requirements than dielectric or elastic tensors, making them a crucial test case.

4. **Performance on Elastic Tensors**

The performance of the proposed method on elastic tensors is significantly lower than GMTNet's original results. This suggests potential limitations in the approach’s effectiveness. The discrepancy in performance compared to a well-established baseline raises concerns about the method's robustness and generalizability.

5. **Efficiency Gains Not Attributable to Proposed Method**

The efficiency gains claimed largely derive from the use of the lightweight eComformer, not the proposed approach. Similar speed-ups could be achieved by combining eComformer with other O(3) equivariant methods such as ETGNN’s vector outer-product approach or minimal frame averaging. The paper needs to clearly isolate the efficiency contribution of the proposed method from the base model.

### Questions
As listed above in Weaknesses.

### Soundness
2

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
3

### Summary
The paper introduces a method for predicting how crystals react to forces applied from different directions, a challenge that requires maintaining consistency regardless of the crystal's orientation in space. 

The proposed method uses a sound mathematical technique (polar decomposition) to standardize crystal positions, enabling faster and more accurate predictions of these directional properties (known technically as tensor properties) while respecting the physics principle of orientation independence (technically called O(3) group equivariance). 

The proposal is significantly faster and more accurate than existing approaches, especially for predicting how materials deform under stress or respond to electric fields.

### Strengths
1. The pre-processing step of standardizing crystal positions through polar decomposition is significant for multiple reasons. It ensures equivariance, simplifies model architecture, and preserves tensor properties across different orientations through an additional step.
2. The method achieves 13x speed improvement over prior methods in predicting tensor properties.
3. The paper effectively explains O(3)-equivariance in crystal tensor prediction through clear organisation, helpful diagrams, and accessible mathematical explanations, making sophisticated concepts understandable even to non-specialists.

### Weaknesses
1. The paper focuses primarily on quantitative metrics (e.g. Frobenius norm and EwT percentages) to demonstrate the method's effectiveness. However, there is a lack of qualitative insights into how the method affects real-world predictions. Including case studies or qualitative analyses where the method's predictions are compared to known physical properties of materials would strengthen the practical significance.
2. Evaluation is carried out on two specific datasets for dielectric and elastic tensor prediction. While the results are promising, these datasets may not cover the full range of tensor property prediction challenges. Testing on a broader variety of materials, including more extreme cases, would strengthen the claim of generalisability.
3. As the authors discuss between lines 137 and 142, " the requirements for O(3) equivariance typically differ from the O(3)-equivariance
defined in the general molecular studies." Because of these specific requirements, the scope and the applicability of the proposed polar decomposition are limited.

### Questions
1. Were there qualitative case studies where the proposed method's predictions were compared to known real-world material properties, such as elastic or dielectric responses of specific materials?
2. Were there plans to test the proposed method on other datasets, especially those involving more complex or extreme tensor property cases (e.g., materials with highly anisotropic properties or rare crystal structures)? 
3. Why was the dataset "Piezo" that was tested in a prior work [Yan et al.] not tested in this paper?
4. What explains the discrepancy in the number of samples in the "Elastic" dataset between the prior work [Yan et al.] and this paper? The prior work [Yan et al.] reports 14,220 samples in Table 1, while this paper reports 25,110 samples in Table 1 on line 364.
5. Could the specific requirements of O(3) equivariance for crystalline materials limit the use of polar decomposition? Additionally, how did these differences impact the potential generalisation of the proposed method to molecular systems, where O(3) equivariance is defined differently?

[Yan et al.] [A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction, In ICML 2024](https://openreview.net/forum?id=BOFjRnJ9mX).

### Soundness
3

### Presentation
3

### Contribution
2
