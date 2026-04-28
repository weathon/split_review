# Topological Zigzag Spaghetti for Diffusion-based Generation and Prediction on Graphs

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Diffusion models have recently emerged as a new powerful machinery for generative artificial intelligence on graphs, with applications ranging from drug design to knowledge discovery. However, despite their high potential, most, if not all, currently existing graph diffusion models are limited in their ability to holistically describe the intrinsic {\it higher-order} topological graph properties, which obstructs model generalizability and adoption for downstream tasks. We propose to address this fundamental challenge and extract the latent salient topological graph descriptors at different resolutions by leveraging zigzag persistence. We develop a new computationally efficient topological summary, zigzag spaghetti (ZS), which delivers the most inherent topological properties {\it simultaneously over a sequence of graphs at multiple resolutions}. We derive theoretical stability guarantees of ZS and present the first attempt to integrate
dynamic topological information into graph diffusion models. Our extensive experiments on %9 benchmark datasets for 
graph classification and prediction tasks suggest that ZS has a high promise not only to enhance performance of graph diffusion models, with gains up 10\%, but also to substantially booster model robustness under uncertainties.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces zigzag spaghetti (ZS), a novel topological summary designed to enhance diffusion models for graph-based generative AI by capturing higher-order topological properties. Using zigzag persistence, ZS extracts key topological descriptors across multiple resolutions in dynamic graphs, addressing limitations in current models' generalizability. Theoretical stability guarantees for ZS are provided, and it represents the first integration of dynamic topological information in graph diffusion models. Experiments across nine benchmark datasets demonstrate that the proposed method improves performance even up to 10%.

### Strengths
1) The proposed method is very interesting and novel. The paper tackles an important topic introducing concepts from computational topology to generative diffusion models for graphs. The motivation behind the idea is clearly communicated and provided.

2) The paper is well written providing a good introduction to the different concepts adopted in the study.

3) The experimental set-up is very strong including multiple baselines with the method outperforming all of the them across all datasets. Furthermore, there are experiments validating the robustness of the method and the computational cost. The paper is very complete on the experimental set-up

### Weaknesses
1) The proposed method is not scalable which is rather a limitation. Zigzag persistence introduces additional complexity due to the need for forward and backward inclusions in the filtration sequence, which can become costly for large or dense graphs. Specifically, the computation of zigzag modules involves tracking the evolution of homology groups through a sequence of nested simplicial complexes, requiring significant memory and processing time, especially when dealing with large graphs where the number of simplices grows rapidly. This computational burden is further exacerbated by the need to consider multiple resolutions, as the zigzag persistence calculation must be performed for each resolution level, compounding the computational cost.

### Questions
- I would like to ask the authors if recent efforts in scaling graph diffusion models could benefit also their approach as well. For instance, could techniques such as sparse attention or hierarchical modeling, commonly used in recent large-scale graph diffusion models, be adapted to improve the scalability of the zigzag spaghetti approach?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates diffusion models on graph generation and prediction. To capture the high-order topological graph properties during diffusion, the authors propose to leverage the zigzag persistence. In particular, a computation-efficient topological summary metric zigzag spaghetti (ZS) is developed over a sequence of graphs at multiple resolutions with theoretical stability guarantees. Experimental results confirm the effectiveness of ZS as a plausible metric for graph diffusion models.

### Strengths
1. This paper develops a practical method to capture the topological properties of generated graphs at various resolutions.

2. Theoretical stability guarantees are provided.

3. Extensive experimental results confirm the effectiveness of ZS as a plausible metric for graph diffusion models.

### Weaknesses
1. Some illustrations for zigzag persistence and zigzag filtration curves in Section 3 can benefit the convey of the content.

2. Some sentences are not precise, e.g., “M is the number of the” in line 162. Actually, M is a set in the paper.

3. Proposition 3.2 seems to be a simple derivation from proposition 3.2 of Chen et al. (2022). Please further clarify the significance of this proposition. Meanwhile, there exist explicit notation errors in Proposition 3.2 between PDz_alpha_k and PDz’_alpha_k, which should be avoided in the submission.

4. The bootstrap version of ZS is proposed. However, no theoretical analysis of accuracy is provided due to the inherent challenges. I would suggest the authors provide some empirical results or analyses at least.

5. Zigzag spaghetti is proposed as computation efficiency, which remains unclear from a theoretical perspective. Please justify this by comparing its time complexity with existing metrics.

6. Figure 1 is proposed to illustrate the proposed ZS. I suggest the authors provide the necessary explanations for better clarity.

### Questions
Please refer to the weakness part.

### Soundness
3

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
This paper addresses the a critical limitation in current graph diffusion models by introducing a novel approach to capture higher-order topological properties. Such higher-order topological properties can be captured using time-aware topological summary zigzag spaghetti (ZS), which leverages zigzag persistent homology. Stability of the obtained ZS has been guaranteed with respect to Wasserstein distance. The paper also introduces zigzag spaghetti-based encoder (ZS-ENC) to incorporate ZS into diffusion models. The applicability of ZS has been tested on various settings demonstrating improvements in different metrics.

### Strengths
- This paper attempts to incorporate zigzag persistence homology into generative diffusion model.
- Theoretical stability of zigzag spaghetti has been addressed
- Applicability of zigzag spaghetti has been demonstrated in different settings

### Weaknesses
The soundness of the paper seems to need a bit of improvement. For instance, notations might need a little more description. ($\omega$ from section 3 and 3.1 seems to be referring to different object). Also, definition of mathematical object can help the understanding of the paper (union of two graphs mentioned). More detailed description of figures and tables can improve the readability.

### Questions
- What is the difference between $\mathcal{G}_t$ and $\mathcal{G}^t$ in Sec. 3?
- Can you describe how you obtained $\omega_i$ in Sec. 3.1
- How is Sec. 4.1 related to the methodology of your paper?

### Soundness
3

### Presentation
3

### Contribution
3
