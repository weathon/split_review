# FreeCG: Free the Design Space of Clebsch-Gordan Transform for Machine Learning Force Fields

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
\vspace{-0.3cm}
Machine Learning Force Fields (MLFFs) are of great importance for chemistry, physics, materials science, and many other related fields. The Clebsch–Gordan Transform (CG transform) effectively encodes many-body interactions and is thus an important building block for many models of MLFFs. However, the permutation-equivariance requirement of MLFFs limits the design space of CG transform, that is, intensive CG transform has to be conducted for each neighboring edge and the operations should be performed in the same manner for all edges. This constraint results in reduced expressiveness of the model while simultaneously increasing computational demands.
To overcome this challenge, we first implement the CG transform layer on the permutation-invariant abstract edges generated from real edge information. We show that this approach allows complete freedom in the design of the layer without compromising the crucial symmetry. Developing on this free design space, we further propose group CG transform with sparse path, abstract edges shuffling, and attention enhancer to form a powerful and efficient CG transform layer. Our method, known as \textit{\textbf{FreeCG}}, achieves state-of-the-art (SOTA) results in force prediction for MD17, rMD17, MD22, and is well extended to property prediction in QM9 datasets with several improvements greater than 15$\%$ and the maximum beyond 20$\%$. The extensive real-world applications showcase high practicality. FreeCG introduces a novel paradigm for carrying out efficient and expressive CG transform in future geometric neural network designs. To demonstrate this, the recent SOTA, QuinNet, is also enhanced under our paradigm. Code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes FreeCG, a method that implements the CG transform layer on the permutation-invariant abstract edges, which allows complete freedom in the design of the layer without compromising the overall permutation equivariance. This can greatly improve the model’s expressiveness and decrease the computational demands.

### Strengths
- This paper uses invariance transitivity with permutation-invariant abstract edges to solve the narrowness design space of CG transform.
- This work further proposes a FreeCG model that contains Group CG transform with sparse path, abstract edges shuffling, and Attention enhancer to improve the representation power and efficiency.
- The model shows good performance on several small molecule datasets.

### Weaknesses
 - In Table 2, FreeCG is not effective in energy prediction on the rMD17 dataset. Could authors elaborate more on this?
- In Table 4, other competitive baselines such as equiformerV2 should be included for a comprehensive comparison. 
- The datasets used in this paper are quite small and the results are sometimes not robust to evaluate the model performance, such as QM9. I would like to see the force and energy prediction performance on a large dataset such as OC20, to better understand the effective and efficiency of the FreeCG.

### Questions
- Please refer to the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an approach to address the computational inefficiency of Clebsch-Gordan (CG) transforms in rotation-translation equivariant graph neural networks (EGNNs). Leveraging the invariance transitivity property, the proposed method, FreeCG, implements the CG transform layer on permutation-invariant abstract edges, enabling a more flexible layer design without compromising permutation equivariance. Additional architectural modifications are introduced to enhance model efficiency, with extensive empirical results demonstrating FreeCG’s performance.

### Strengths
1. FreeCG could reduce the computational overhead of CG transforms and enhance expressivity by incorporating several architectural improvements.
2. FreeCG achieves competitive or superior performance across multiple benchmarks and demonstrates compatibility with various EGNN architectures.

### Weaknesses
1. FreeCG’s approach to freeing CG transform space with abstract edges resembles the customized tensor product mechanism used in Allegro (see Eq. 13 in [1]). Allegro applies CG transforms to geometric features of a pair (similar to FreeCG’s node features) and environment embeddings of the pair (similar to FreeCG’s abstract edges from neighbors). While FreeCG focuses on atom-wise message passing with greater interaction between atom features and abstract edges, further clarification is needed on the specific advantages of FreeCG over Allegro, particularly concerning how the permutation-invariant abstract edges offer a distinct advantage over Allegro's approach which also uses pair-wise features and environment embeddings.
2. Introducing sparse paths may come with a trade-off in expressivity. The authors should provide a more detailed ablation study to analyze the impact of sparse paths on both computational efficiency and model performance, including a breakdown of performance at different levels of sparsity, and how this impacts the model's ability to capture long-range interactions.
3. Results in Table 5 are somewhat unclear. If the final FreeCG model uses the best-performing modules, it should have a group number of 32, which conflicts with the number 8 reported in Table 7. Additionally, the ablations indicate that the primary performance improvement is due to increased group numbers, suggesting that the other modules’ contributions may be limited. It would be beneficial to see a more granular analysis of the contribution of each module, including the group shuffling and attention mechanisms, to better understand their individual impact on performance.
4. Certain aspects of the methodology require additional clarity: a) Some notations are under-defined, e.g., $N$ in line 227, $\bar{E_i^L}$, and $d\bar{E_i^{L+1}}$ in line 277. b) The relationship between $d\bar{E_i^{L+1}}$ and $\bar{E_i^{L+1}}$ in line 277 is unclear, and more details are needed on how $\bar{E_i^L}$ is constructed in the first layer, specifically how the initial abstract edge features are initialized and what information they encode.

### Questions
1. For abstract edge shuffling, did the authors try using a linear layer to mix different channels of $\hat{E}_i^L$? Linear mixing could enhance information exchange effectively in this case.
2. Did the authors consider applying FreeCG to more representative tensor product-based EGNNs? This could further validate the method’s efficacy.

### Soundness
2

### Presentation
2

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
The paper introduces a novel approach to Machine Learning Force Fields (MLFFs) that leverages permutation-invariant hidden features for efficient computation. These permutation-invariant features are aggregated over high-irreducible (high-irrep) edge features with attention weights, forming what is referred to as the “abstract edge” in the paper. The Clebsch-Gordan (CG) transformation is applied within each layer, and these permutation-invariant hidden features serve as the input of the kernel function for the CG transformation layer.

To improve the efficiency of the CG product, the authors propose a grouped CG transformation, which operates similarly to a group convolution. Additionally, to enhance the utility of the abstract edge, they introduce abstract edge shuffling and an Attention Enhancer mechanism.

### Strengths
- The paper includes extensive experiments in the MLFF domain, providing empirical solid support for the model’s performance.

- By aggregating high-irreducible (high-irrep) edge features with attention-weighted, permutation-invariant hidden features (abstract edges), the model achieves robust and flexible representations.

### Weaknesses
 - The paper’s organization and readability could be improved. In particular, modified margins between paragraphs, figures, titles, and subtitles reduce overall readability.

- The paper does not adequately address  $\text{SO}(3)$ -equivariance, a critical concept in equivariant GNNs. Typically, in Clebsch-Gordan (CG) transformations, a radial distance-based kernel function is used to ensure  $\text{SO}(3)$ -equivariance. However, FreeCG may lack  $\text{SO}(3)$ -equivariance, as the aggregation of abstract edges is based on a weighted summation over components of each irreps. While this aspect is unclear, explicitly showing how the model achieves  $\text{SO}(3)$ -equivariance would enhance understanding. If the model does not fully satisfy  $\text{SO}(3)$ -equivariance, it would be helpful to justify using abstract edges within the CG transformation layer.

- The paper should include recent results in Table 2 to demonstrate the model’s state-of-the-art (SOTA) status. Specifically, adding comparisons with Graph ACE [1] and PONITA would strengthen the claim.

[1] Bochkarev, Anton, Yury Lysogorskiy, and Ralf Drautz. "Graph Atomic Cluster Expansion for Semilocal Interactions beyond Equivariant Message Passing." Physical Review X 14.2 (2024): 021036.

[2] Bekkers, Erik J., et al. "Fast, Expressive $\mathrm {SE}(n) $ Equivariant Networks through Weight-Sharing in Position-Orientation Space." The Twelfth International Conference on Learning Representations.

- In Equation (26), the model employs a summation over all permutations, which may constrain the model complexity to  O(N \times N!) . To fully discuss the model’s efficiency, scalability with respect to the number of atoms should also be considered.

- Information about what kinds of loss are used is omitted.

- On page 5,  $N$  appears undefined and may be a typo; perhaps it should be  $Z$ .

- In Figure 3, the shaded regions impair readability; using a transparent background or adjusting the shading would improve clarity.

- Unnecessary line breaks are present in Appendix equations (7) and (15).

- Table 8 is unnecessarily expanded to fill the entire line width.

### Questions
- How does the model ensure the SO(3) equivariance?
- Why was the AIMD-Chig dataset chosen for memory usage and inference speed benchmarks?
- Why does abstract edge shuffling improve the model? A brief discussion on the role of shuffling is needed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduced an informative and efficient model utilizing high-order irreps and CG transform. This model achieves state-of-the-art (SOTA) results in force prediction for MD17, rMD17, and MD22. However, while the authors asserted that this work represented a new paradigm for CG transform that can be integrated with other models, such as QuinNet, to enhance performance, the experimental results do not support this claim.

### Strengths
The paper proposed an informative and efficient model with high-order irreps and CG transform.

The model achieved state-of-the-art (SOTA) results in force prediction for MD17, rMD17, MD22.

### Weaknesses
Although the author claimed that this work presented a new paradigm for CG transform that can be combined with other models, such as QuinNet, to achieve better performance, the experimental results did not demonstrate this. Simply analyzing the training curves did not allow readers to determine the impact of adding or removing FreeCG on QuinNet. Furthermore, while other models were trained for 3000 epochs, QuinNet was only trained for 1000 epochs. At this point, there is no clear advantage for QuinNet+FreeCG, and readers cannot ascertain whether extended training would improve QuinNet's performance.

For MILP, both model execution speed and memory usage are critically important. The proposed method seems to significantly increase the computational complexity of the model. It is crucial to include a comparison of the number of parameters and training speed.

### Questions
For MILP, both model execution speed and memory usage are critically important. The proposed method seems to significantly increase the computational complexity of the model. It is crucial to include a comparison of the number of parameters and training speed.

### Soundness
3

### Presentation
2

### Contribution
3
