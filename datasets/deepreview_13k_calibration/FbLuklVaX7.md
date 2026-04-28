# Node Classification in the Heterophilic Regime via Diffusion-Jump GNNs

- Decision: Reject
- Avg Score: 4.00
- Scores: 8, 1, 3

## Abstract
In the heterophilic regime (HR), vanilla GNNs learn latent spaces where nodes with different labels may have similar embeddings. As a result, the performance of node classification degrades significantly in this context. However, existing metrics for heterophily count local discontinuities instead of characterizing heterophily in a structural way. In the ideal (homophilic) regime, nodes belonging to the same community have the same label: most of the nodes are harmonic (their unknown labels result from averaging those of their neighbors given some labeled nodes). Harmonic solvers are natural minimizers of the Laplacian Dirichlet energy. Therefore, a homophilic network is more harmonic than any heterophilic version of the same network. In other words, heterophily can be seen as a “loss of harmonicity”. In this paper, we define “structural heterophily” in terms of the ratio between the harmonicity of the network (Laplacian Dirichlet energy) and the harmonicity of its homophilic version (the so-called “ground” energy).

In this paper, we also propose a novel GNN model (Diffusion-Jump GNN) that bypasses structural heterophily by “jumping” through the network in order to relate distant homologs. However, instead of using hops as standard High-Order (HO) GNNs (MixHop) do, our jumps are rooted in a structural well-known metric: the diffusion distance. Given the diffusion distances matrix (DM), we explore different orders of
distances wrt each node (closest node, second closest node, etc.) in parallel. Each parallel exploration defines a “jump” that masks the network: it is a new graph that feeds a vanilla GNN layer. Consequently, different GNNs attend to different slices of the DM. As a result, we allow distant homologs to have similar embeddings in (at least) one of the jumps. In addition, as the final embedding of each node depends on the concatenation of its parallel embeddings, we can capture the explainability of each jump via learnable coefficients.

Since computing the DM is the core of this method, our main
contribution is that we learn both the diffusion distances and the
“coefficients” of the edges associated with each jump, thus defining
“learnable structural filters”. In order to learn the DM, we exploit
the fact that diffusion distances have a spectral interpretation.
Instead of computing the eigenvectors of the Laplacian, we learn
orthogonal approximations of the Fiedler vector solving a
trace-ratio optimization problem while the prediction loss is minimized. This leads to an interplay between a Dirichlert loss, which
captures low-frequency content, and a prediction loss which refines
that content leading to empirical eigenfunctions. Finally, our experimental results show that we are very competitive with the SOTA both in homophilic and heterophilic datasets, even in large graphs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the challenges of node classification in heterophilic settings. A key issue identified is the potential for standard GNNs to produce similar embeddings for nodes even if they possess different labels in such regimes. To tackle this, the paper introduces the Diffusion-Jump GNN, a novel model designed to bridge distant homophiles through a "jump" mechanism. This jump is distinct from typical high-order GNNs and is anchored on a structural metric known as the diffusion distance. The paper provides a detailed experiment to validate the model based on multiple datasets and several other different types of models and achieves SOTA on some of the datasets

### Strengths
1. The paper provides a comprehensive investigation into the challenges faced by standard GNNs in heterophilic environments, offering a fresh perspective on understanding and quantifying heterophily.
2. The Diffusion-Jump GNN is described in great depth, covering both the mathematical and conceptual foundations. This level of detail facilitates a clear understanding and potential implementation by researchers.
3. By conducting experiments using the same data splits as previous studies, the paper ensures fairness and comparability in the results. Additionally, the provision of hyperparameters and the use of early stopping strategies add reliability to the experiments.

### Weaknesses
1. Some mathematical formulas and concepts within the paper may be challenging for non-experts. A more simplified explanation or background could make it more accessible to a broader audience.
2. The Diffusion-Jump GNN might introduce computational complexities, especially related to diffusion distances. This could be a concern in resource-constrained settings or applications requiring real-time responses. Specifically, the computation of the full diffusion matrix, which scales quadratically with the number of nodes, could be a significant bottleneck for larger graphs. Furthermore, the eigen-decomposition required to obtain the diffusion distances can also be computationally expensive.
3. Given the complex mathematics and concepts of the Diffusion-Jump GNN, it might not be as intuitive or interpretable as some simpler GNN models. This could impact the acceptance and trust in the model, especially in scenarios where interpretability is crucial. The 'jump' mechanism, while novel, lacks a clear, intuitive explanation in terms of node interactions, making it harder to understand why it works and when it might fail.
4. The paper does not delve deeply into the stability of training the model. Some GNN models might be susceptible to issues like vanishing or exploding gradients, which could affect the training efficiency of the Diffusion-Jump GNN. The interplay between the Dirichlet loss and the classification loss during training is not fully explored, and it's unclear how sensitive the model is to the choice of hyperparameters related to these losses.

### Questions
1. Given the potential computational complexities, how efficient and scalable is the Diffusion-Jump GNN when dealing with large graphs, e.g., those with millions of nodes and edges?
2. How would the Diffusion-Jump GNN be adjusted or modified when faced with graphs having multiple types of nodes and edges or other intricate structures? Is the method versatile enough for these complex scenarios?
3. Are there plans to further optimize the Diffusion-Jump GNN for better performance or reduced computational demand? Is there potential to extend this method to other graph tasks like graph classification or link prediction?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to learn latent graph connections to deal with heterophilic graph datasets.

### Strengths
Difficult to judge due to poor presentation.

### Weaknesses
1. The paper is poorly written with important notations not defined and explained. This makes it very difficult to judge the contributions of the paper. Examples include the issues raised in the following questions.

1. The paper seems to be written in a hurry and not proofread. It is not ready for submission.

### Questions
1. The abstract is too long and does not capture concisely the contributions of the paper. This is not how an abstract should be written.

1. What is the difference between $f_{\Theta}$ and $f_\theta$? There are notation confusions throughout.

1. In (1), what is $\ell$ and is this the same as $\ell^*$ defined previously?

1. On page 4, from the phrase "Consequently, the jump hierarchy defines a succession of unstable states" onwards, the terms have not been explained clearly. What are "unstable states"? What is an "expansion"? 

1. The section "Exploration by Parallel Jumping" needs to be rewritten for clarity. What are "structural" filters? Why are there $K+1$ of them? How do you choose $K$? The authors seem to want to say that they are learning a graph filter but instead tries to bring in confusing jargon. 

1. How is the proposed approach different from graph rewiring?

### Soundness
1 poor

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
This paper studies the node classification problem, especially for graphs with low homophily. Overall, the proposed method is to learn a set of filter/propagation matrices, called "Jump" in this paper; then it propagates messages based on every Jump separately and aggregates node representations from Jumps together for node classification. Another contribution of this paper is a newly proposed homophily/heterophily measure called "Structural Heterophily".

### Strengths
S1. The performance of the proposed method is good, or at least comparable to the SOTAs. (Table 1 and 2).

S2. The code is released which ensures the reproducibility of this paper.

S3. Figure 8 is clear to understand and I suggest moving Figure 8 to the main content for better illustration.

### Weaknesses
W1. The main drawback of this paper is its organization and presentation, which can be improved.

W2. Some statements/claims from this paper seem problematic and not accurate. E.g., in Eq. (2), seems the propagation matrix/Jumps $J^k$ cannot be strictly termed as filters according to the definition from the graph signal processing [1]. Specifically, if they are constructed according to Eqs (2) and (4), they may not share the same set of eigenvectors with the original adjacency matrix. Furthermore, the claim that these 'Jumps' act as filters is not sufficiently justified, particularly given that the learned weights $C_k$ are applied to edges, not directly to the spectral components of the graph signal. This distinction is crucial in the context of graph signal processing, where filters typically operate on the spectral domain.

W3. The novelty of this paper is not outstanding. From a high-level view, the idea of a filter bank (i.e., a set of filters/propagation matrix) is included in many existing works, e.g., [2-5]. Also, the proposed heterophily measure "Structural Heterophily" is related to the existing measure "edge homophily". The difference between the "Structural Heterophily" and edge homophily is that (1) the numerator of the former is the # of different-label connected node pairs, and the numerator of the enumerator of the latter is the # of same-label connected node pairs; (2) the denominator of the former is topology smoothness and the denominator of the latter is the total # of edges. The connection between the proposed structural heterophily and the spectral properties of the graph is not clearly established, making its theoretical justification weak.

W4. In my view, some content is not necessary to be included in the paper, and it may distract readers from the main contribution. E.g., the introduction section includes too much technical content, which is not thoroughly explained within the Intro section, and is not helpful for readers to understand the whole story and the core idea. I suggest authors rewrite a part of them with more plain but intuitive language.

### Questions
Q1. In the 2nd paragraph of Section 2, it mentioned "$l^*=\arg\min l^T\Delta l$, where $l*$ is the smoothest labeling of V after propagating l(B) to l(U) through the edges of the graph". I think this is not accurate. Solely based on the context provided in this paragraph, the $l^*$ should be a vector whose entries are all the same.

Q2. In the 4th paragraph of Section 2, it mentioned "We need to infer a hidden graph $G'=(V,E')$. However, the term hidden graph $G'$ is not used a lot and it is not clear how to infer this hidden graph. What is the relationship between the hidden graph $G'$ and the "Jumps"?

Q3. What is the advantage of Structural Heterophily compared with existing homophily/heterophily measures? Also, according to the statement "For $R > 1$ the graph is heterophilic", so only $R=1$ the graph is homophilic? I think the statement is not accurate.

Q4. On the top of Page 4, it mentioned "unstable states u1, u2," and $\bar{A}_1, \bar{A}_2, \dots$. What are those vectors and adjacency matrices? How to obtain them from the context? In the paragraph next, it mentioned "if we relabel the white node, ....., the new Fiedler vector ul leading to the labeling l does no longer induce a sharp step function". It is confusing since the Fiedler vector should only be determined by the graph topology, and not related to the labeling of nodes. In addition, what is the "sharp step function"?

Q5. In Section 3, what is the relationship/difference between $f_{\Theta}$ and $f_{\theta}$?

Q6. In a subsection named "Exploration by Parallel Jumping", the Jumps $J^k$ is presented as a tuple with three elements, but according to the context, the Jumps $J^k$ should be a matrix with the same shape as the adjacency matrix, which is confusing.

Q7. From Section 4.1 we know the nontrivial eigenvectors $\mathbf{U}$ are approximated by $\mathbf{U}=f_\theta(\mathbf{A})$, and obtained by SGD optimizing the Eq. (3). Why not directly set the whole $\mathbf{U}$ matrix as a free parameter and optimize it directly? What is the benefit of parametrizing it with input as $\mathbf{A}$? The design for this part is not clearly explained.

Q8. On page 9, it claimed that "our method needs higher frequency eigenfunctions in order to capture the extreme degree variability of this dataset". Any reference or evidence?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
