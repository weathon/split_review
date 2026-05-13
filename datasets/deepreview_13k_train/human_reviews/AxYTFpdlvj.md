# Graph Decoding via Generalized Random Dot Product Graph

- Decision: Reject
- Scores: 1, 1, 3, 3

## Abstract
Graph Neural Networks (GNNs) have established themselves as the state-of-the-art methodology for a multitude of graph-related tasks, including but not limited to link prediction, node clustering, and classification. Despite their efficacy, the performance of GNNs in encoder-decoder architectures is often constrained by the limitations inherent in traditional decoders, particularly in the reconstruction of adjacency matrices.

In this paper, we introduce a novel graph decoding approach through the use of the Generalized Random Dot Product Graph (GRDPG) as a generative model for graph decoding. This novel methodology enhances the performance of encoder-decoder architectures across a range of tasks, owing to GRDPG's better capability to capture structures embedded within adjacency matrices.

To  evaluate our approach, we design a benchmark focused on graphs of varying sizes, thereby enriching the diversity of existing benchmarks for link prediction and node clustering tasks. Our experiments span a variety of tasks, encompassing both traditional benchmarks and specialized domains such as molecular graphs.

The empirical results show the capability of GRDPG on faithfully capturing properties of the original graphs while simultaneously improving the performance metrics of encoder-decoder architectures. By addressing the subtleties involved in adjacency matrix reconstruction, we  elevate the overall performance of GNN-based architectures, rendering them more robust and versatile for a wide array of real-world applications, with special regard on molecular graphs.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose to use a GRDPG-based decoder, instead of the classical RDPG or inner-product decoder, in the framework of GAEs and GVAEs.

The introduction of the paper is very good. However, the rest of the paper is very repetitive, and the important details are missing.

I think that four pages to describe the impact of negative eigenvalues is too much. And the paper jumps from the description of the GRDPG (Section 3) to the experiments (Section 4), without explaining the proposed method, architecture, or something.

### Strengths
The introduction is very good, as said before. And the idea of using GRDPGs as decoder architecture is interesting, but I think it needs more work.

### Weaknesses
Throughout the paper, the authors insist on non-bipartite graphs, as if it was a requirement or something. Even for showing the existence of graphs with negative eigenvalues, while it would have made much more sense to say, "bipartite graphs have spectra of $A$ symmetric around 0".

In this sense, Section 2.2 (and Appendix A) are not needed at all.

The GRPDG method requires knowing in advance the number of positive/negative eigenvalues, so it's very important to know how the authors addressed this. Is it always the same? Is it chosen for each dataset? How? 
If I guessed correctly, the authors try several different values of $q$ (for each dataset maybe?) and keep the result with the best performance.
The lack of information on this crucial part is not acceptable.

In the preliminary section, the description for the GAE loss functions says the expectation with respect to some q, which is not defined before.

Minor comments:
 - the equations are part of the text. The punctuation after the equation is missing in general.

### Questions
In the preliminary section, the description for the GAE loss functions says the expectation with respect to some q, which is not defined before.

Minor comments:
 - the equations are part of the text. The punctuation after the equation is missing in general.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a modification to the decoder, i.e. the dot product of the existing graph encoder-decoder framework called GRDPG. It intends to empower the decoder to represent the adjacency with negative eigenvalues. Experiments show some improvement.

### Strengths
- The proposed method can be flexibly applied on any existing dot-product-based reconstruction functions.
- Experiments show some improvement somehow.

### Weaknesses
 - The paper is skeptically to be considered as lacking good structure, especially the connection between the dot product and its deficiency of presenting negative eigenvalues.
- Very often the sentences are repeated, presenting the same meaning, e.g. the first two paragraphs on page 2, the fourth paragraph on page 3, and so on.
- Typos are quite frequent, e.g. the third equation $p(Z|X,A \$ (also there is no index for all equations or formulas except those in the method), $Z=z_i^Tz_j$, and so on.
- The experimental results are not convincing, especially on the structure perception link prediction task, and also the random seeds and variances are missing to report.
- Overall, the quality of the paper is far below the requirements of ICLR.

### Questions
- My first question is that it would be nice to make sure that the existing papers that hold the semi-positive defined assumption of the probability of reconstruction is entailed by its assumption of undirected graphs.
- It is highly recommended to further investigate which type of $I_{p,q}$ works best for different graph structures.
- Why is node clustering an appropriate experiment to verify the model? Should it be more related to the task of graph structure perception?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduce a graph decoder by employing the Generalized Random Dot Product Graph (GRDPG) as a generative model for graph decoding. This methodology significantly enhances the performance of encoder-decoder architectures across a range of tasks.

### Strengths
1. Clear and straightforward illustraction of method.

### Weaknesses
1. Novelty is limited.  Equation (3), the center of the method, has been proposed in [1]. The application of the GRDPG to graph decoding, while potentially useful, does not represent a significant theoretical advancement, given the existing work on the GRDPG model itself.

2. The meaning of negative eigenvalue in adjacency matrix remains unclear. Does it corresponds to some specific substructure or some graph statistics? The paper does not provide any theoretical justification or empirical evidence to support the interpretation of negative eigenvalues, leaving a gap in understanding the model's behavior. Specifically, how do these negative eigenvalues impact the graph structure and the generative process?

3. Uncertainties are not provided in experiment results. The absence of standard deviations or confidence intervals makes it difficult to assess the statistical significance of the reported results. This lack of uncertainty quantification hinders the reproducibility and reliability of the findings.

4. Though this work proposes a decoder, generation tasks are not included in experiments. The experiments focus solely on reconstruction tasks, which do not fully validate the generative capabilities of the proposed decoder. A more comprehensive evaluation should include tasks such as graph generation or link prediction to demonstrate the decoder's ability to produce novel graph structures.

### Questions
1. Lorentz model in hyperbolic GNN [1] also uses a diagonal matrix with $\pm 1$. Could you please compare your Equation 3 with hyperbolic GNNs?

2. What is the detailed meaning of negative eigenvalues in graph? Some specific graph structures?

3. Can use approximate graph laplacian matrix ($L=D-A$) instead of adjacency matrix to avoid the positive-semi definite problem?

[1] Menglin Yang, Min Zhou, Zhihao Li, Jiahong Liu, Lujia Pan, Hui Xiong, Irwin King. Hyperbolic Graph Neural Networks: A Review of Methods and Applications. CoRR abs/2202.13852.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper identifies the problem of the current GNN's inability to reconstruct a graph whose adjacency matrix has negative eigenvalues. It then proposes a method to manually negate several entries of the embedding vectors of nodes to allow negative eigenvalue. Experimental results show consistent improvement across datasets.

### Strengths
The identified problem is interesting and allowing models to generate an adjacency matrix with negative eigenvalues is a critical task. The authors explain the intuition behind the negative eigenvalue adjacency matrix well.

### Weaknesses
The presentation needs significant improvement. The use of bold/unbold letters to represent vectors is inconsistent, and some subscripts are missing.  While the core idea is interesting, it is poorly presented. As the authors emphasize the importance of the negative eigenvalues 
and mention irregularity in graphs multiple times, there is no support for how often and when negative eigenvalues appear. (Though toy examples are provided in the appendix.) Some justification should be presented, either empirically obtained from data or theoretically quantified.

The proposed method is also without in-depth analysis. While the proposed matrix multiplication does allow negative eigenvalues, the effectiveness is unclear and never justified in the paper. Also, the negate matrix is manually picked, which is not flexible for more graphs (as the authors acknowledged in the conclusion). The paper lacks a rigorous analysis of how the proposed method impacts the spectral properties of the generated adjacency matrix beyond simply allowing for negative eigenvalues. There is no discussion about the distribution of these negative eigenvalues, their magnitudes, or their potential impact on downstream tasks. Furthermore, the method's reliance on a manually chosen negation matrix is a significant limitation, as it provides no guidance on how to select this matrix for different graph structures or datasets.

### Questions
- The experiments only compared the proposed method with the backbone GNN. However, the advances recent GNN significantly outperforms GAE on various tasks. How does the proposed method compare to those methods.

- Does the generated matrix indeed have negative eigenvalues? If so, does the original matrix that the GNN is trained on also contain negative eigenvalues?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
