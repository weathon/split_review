# Accelerating 3D Molecule Generation via Jointly Geometric Optimal Transport

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
This paper proposes a new 3D molecule generation framework, called GOAT, for fast and effective 3D molecule generation based on the flow-matching optimal transport objective. Specifically, we formulate a geometric transport formula for measuring the cost of mapping multi-modal features (e.g., continuous atom coordinates and categorical atom types) between a base distribution and a target data distribution. Our formula is solved within a joint, equivariant, and smooth representation space. This is achieved by transforming the multi-modal features into a continuous latent space with equivariant networks. In addition, we find that identifying optimal distributional coupling is necessary for fast and effective transport between any two distributions. We further propose a mechanism for estimating and purifying optimal coupling to train the flow model with optimal transport. By doing so, GOAT can turn arbitrary distribution couplings into new deterministic couplings, leading to an estimated optimal transport plan for fast 3D molecule generation. The purification filters out the subpar molecules to ensure the ultimate generation quality. We theoretically and empirically prove that the proposed optimal coupling estimation and purification yield transport plan with non-increasing cost. Finally, extensive experiments show that GOAT enjoys the efficiency of solving geometric optimal transport, leading to a double speedup compared to the sub-optimal method while achieving the best generation quality regarding validity, uniqueness, and novelty.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Because of the known multi-modal (Cartesian coordinates and other features) distribution issue in molecule generation and distribution coupling issue, the paper proposed an optimal molecule transport (OMT) algorithm based on optimal transport (OT) in Flow Matching (FM) on latent codes encoded by equivariance autoencoder.

### Strengths
1. **Clear problem statement**: optimal transport of multi-modal probability and distribution coupling in the specific case of molecule generation are well-known problems and to be addressed. The writing provides enough information for general readers to comprehend. 
The experiments seem abundant to make the effectiveness of the method stand. 
2. Table 4 is crucial for the core statement of this paper, which is that Optimal Molecule Transport (OMT) is important for faster and better molecule generation based on optimal transport (OT) of Flow Matching (FM). From the numbers there, it seems justified.

### Weaknesses
1. I do not see why after equivariance autoencoder mapping to the latent space, we thus have a unified optimal permutation. In equation (5), we still have the same \pi for both coordinates and features right? The reasoning for this part is missing. Specifically, it's unclear how the EAE's latent space inherently enforces a unified permutation across both geometric (coordinates) and feature modalities. The paper needs to elaborate on the mechanism that ensures the optimal permutation found in the latent space translates to a meaningful and unified permutation in the original space, considering the different nature of coordinates and features.
2. I am not sure the distribution coupling, $\Gamma$ is a correct terminology used in this paper. The distribution coupling should be referring to pairing points between two distributions, rather than pairing within one pair of data sample by permutation, rotation and translation. The current usage seems to conflate the concept of optimal transport coupling between distributions with the geometric transformations within a single molecule. The paper should clarify whether $\Gamma$ represents a coupling between the noise and data distributions, or if it is a coupling within a single molecule instance under geometric transformations, and justify the chosen terminology.
3. Maybe limited novelty: In EquiFM[1], we know the idea of equivariant optimal transport (EOT) is proposed, which has a large overlapping with the core contributions of this paper. Can this paper’s main contributions be concluded as  EOT + Equivariant Autoencoder? If so, the novelty of paper may be limited. The paper needs to clearly delineate the novel contributions beyond the combination of existing techniques. The introduction of flow refinement and purification needs to be more clearly defined and differentiated from existing optimal transport methods, particularly in the context of equivariant flows.
4. Is Geometric Probability Distribution a formal terminology in molecule generation community? I do not see it is widely adopted in other related work and it can be misunderstood with geometric distribution. The paper should either provide a clear definition and justification for this term, or consider using a more standard terminology to avoid confusion. The current usage lacks clarity and could be misinterpreted by readers familiar with standard probability distributions.
5. The abbreviation EAE in line 251 pops out without specification (I am assuming it is referring to Equivaraint Autoencoder?)

### Questions
Based on the listed weakness points above, I want to ask following questions:

1. Why using equivariance autoencoder to produce latent codes can yield in unified permutation? 
2. Can I assume your paper is based on the already on-the-shelf work which proposed EOT and EAE? If so, what is your major novel improvement scientifically based on that? If not, please clarify why.
3. Please clarify the terminology issues on point 2 and point 4 mentioned above in the weakness part.

I will adjust my rating to the paper based on the answers to the above questions during rebuttal and discussion phase.

### Soundness
2

### Presentation
3

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
This paper proposes a 3D molecule generation framework which formulates a geometric transport formula for
measuring the cost of mapping multi-modal features (e.g., continuous atom coordinates and categorical atom types) between a base distribution and a target data distribution. They further propose a flow refinement and purification mechanism for optimal coupling identification, which filters out the subpar molecules to ensure the ultimate generation quality.

### Strengths
1. The problem setup is well-motivated. The OT path and equivariance properties are indeed needed in diffusion models/flow matching methods for fast sampling process. 

2. The empirical performance is strong in terms of various metrics. The proposed methods is good in both generation quality and inference steps.

### Weaknesses
1. In Eq. (5), the authors seem to sample permutation, rotation, and translation matrix. Does this mean that the model is not strictly equivariant but approximately equivariant? In other words, the equivariance is learned from data augmentation but not learned by construction.

2. I am wondering maybe it is possible to distill the trained model, like rectified flow, to have even faster inference (1 to 5 steps). I am especially curious to see the generation quality of distillation + purification.

### Questions
Please refer to weaknesses.

I honestly do not know much about the literature on molecule generation so my confidence would not be high. I am happy to check other reviewers' opinions.

### Soundness
3

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
This paper introduces a novel framework for accelerating 3D molecule generation, named GOAT, which leverages the principles of flow-matching optimal transport to efficiently generate molecules with improved quality and speed.

### Strengths
1. I think that using optimal transport to optimize the training process of diffusion models is a very clever and reasonable design, especially when applied to scenarios like molecular generation, where the generation efficiency of diffusion models can be a concern.
2. I'm glad that the paper points out the optimal transport optimization might bring extra computational cost, especially those involving rotation and permutation, can be computationally intensive. However , it's inevitable, but it's a great trial.
3. The framework achieves the satisfiable downstream generation quality regarding validity, uniqueness, and novelty, which are crucial metrics in molecule generation.

### Weaknesses
1. While the paper includes some ablation studies, a more comprehensive set of experiments could provide further insights into the contribution of each component of the framework. Specifically, the ablation study lacks a detailed analysis of the impact of the equivariant autoencoder on the final molecular generation quality and efficiency. It would be beneficial to see how the model performs without this component, particularly in terms of transport cost and generation time, to fully understand its contribution.
2. The training process itself may be time-consuming, which could be a drawback for some applications, though as mentioned in strengths, it's inevitable.

### Questions
1. It would be interesting if the paper could provide a comparison of the distance between generated molecules and the initial state, with/without the use of optimal transport.
2. The use of optimal transport may raise concerns about the diversity of the generated molecules. This could be addressed by generating N molecules and comparing the coverage of the reference conformation set within a specified distance threshold (you can refer to the design of this criterion in papers like GeoDiff[1]).
[1] Xu, Minkai, et al. "Geodiff: A geometric diffusion model for molecular conformation generation"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to molecule generation by introducing a variation of optimal transport for multimodal features within a general flow-matching objective. An equivariant neural network is utilized to transform these multimodal features into a latent space, where multimodal data optimal transport is applied. The results show that this method outperforms existing models like EquiFM and EDM, and it also demonstrates superior computational speed compared to other models.

### Strengths
1. **Significant Theoretical Development in Joint Optimal Transport:**

The theoretical advancement of joint optimal transport presented in the paper has the potential to greatly impact future flow-matching (FM)-based model development. This innovation could propel the entire field of molecule and conformer generation toward faster and more efficient methods.

2. **Emphasis on Performance Improvement and Comprehensive Comparisons:**

The paper places a strong focus on performance enhancement and provides thorough performance comparisons with models like EquiFM, EDM, and others. Since dataset conformations are obtained through computational methods, there is an upper bound on computational cost beyond which applying AI is not justified. The proposed model addresses this by improving performance while staying within acceptable computational limits.

### Weaknesses
1. **Comparison with Recent Edge-Modeling Methods and Potential Integration of Edge Features:**

Some recent models, such as JODO and EQGAT-Diff, have achieved better performance by explicitly modeling edges in molecular graphs. Including comparisons with these models would strengthen your paper. Moreover, adding edge features to your joint optimal transport framework seems feasible and could unlock the full potential of your method. Additionally, a more recent model called Semla Flow (a preprint published in June 2024) demonstrates superior accuracy and speed. Comparing your approach with these methods would greatly enhance the value of the proposed latent optimal transport (OT) technique.

2. **Concerns About Atom Stability Metric and 3D Evaluation:**

While the task is 3D molecule generation, there is no real evaluation of 3D coordinates for unconditional molecule generation in your paper. The term "atom stability" is mentioned without a clear definition. Given that you report an 86.5% figure for the GEOM Drugs dataset, I assume this refers to 3D atom stability. This metric is based on comparing bond lengths with tabulated values, allowing a tolerance of about 0.5 Å. The issue is that only 2.8% of GEOM Drugs molecules fully comply with these criteria, making the metric potentially misleading. I strongly encourage avoiding the propagation of this metric in new papers. The optimal distances between atoms are primarily defined by the potential energy landscape underlying the data—for GEOM Drugs, it's GFN2-xTB—and depending on atom configurations, deviations in bond lengths can exceed 10%.

3. **Difficulty in Claiming State-of-the-Art Performance:**

Related to the first point, it is difficult to claim that this method achieves state-of-the-art (SOTA) performance because it has not been compared with some other relevant methods mentioned above, including MiDi. Including such comparisons would strengthen the claim of achieving SOTA performance.

### Questions
1. Could you provide a more comprehensive evaluation of the generated 3D molecular structures?
I acknowledge that determining the most effective 3D metric is an open and important question. There are several possible solutions you might consider:
- The approach uses the Wasserstein distance between the distributions of bond lengths and bond angles. Some papers, like MiDi, have implemented this method. However, be cautious, as a single poorly predicted molecule can significantly skew the metric due to the way MiDi implemented it.
- SemlaFlow, for example, proposes using the optimization energy drop with the MMFF94 force field as a measure. Given that your ground truth data is based on GFN-xTB calculations, it might be more appropriate to assess the energy drop using GFN-xTB, as it aligns with the potential energy landscape of your dataset.
- Models like JODO and others have utilized MMD for bond angles, bond lengths, and torsion distributions, focusing only on the most frequent bonds and angles. While none of these metrics are perfect, they are generally more informative and insightful than relying solely on 3D atom stability.

The important part here is to ensure that when comparing models, you use exactly the same implementation of these metrics to obtain a reliable comparison. By incorporating these additional evaluations, you can provide a more thorough and insightful assessment of the geometric accuracy of your generated molecular structures. If I am adding one of these, I would rather do it on GEOM-Drugs dataset because it is much more realistic, for QM9 it is quite fast to compute GFN-xTB geometry optimization, and a lot of these molecules do not have considerable variability of 3D structure. 

2. Could you perform comparisons with recent models like EQGAT-Diff, JODO, or SemlaFlow? I'm especially interested in a comparison with SemlaFlow because both papers place significant emphasis on improving the performance of molecule generation and utilize the flow matching objective. The main difference is that your approach performs flow matching in latent space, while SemlaFlow conducts diffusion explicitly on bonds, atoms, and coordinates.

It would be greatly appreciated if you could compare your method with SemlaFlow in terms of:
- Topological Metrics: Such as 2D molecule stability, validity, or introduced significance.
- 3D Metrics: Possibly using some of the metrics described in previous comments (e.g., bond angles, torsion distributions).
- Performance Metrics: Considering that both models generate molecules of similar size, metrics like the average time to generate a molecule would be insightful.

Additionally, could you discuss the advantages of your method over the version of flow matching used in SemlaFlow? Providing a brief discussion of the key algorithmic differences between your proposed method and SemlaFlow's flow matching approach—focusing on how these differences might impact performance or computational efficiency—would enhance the understanding of your contributions.

### Soundness
3

### Presentation
3

### Contribution
3
