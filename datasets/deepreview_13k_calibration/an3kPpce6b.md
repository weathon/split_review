# Steering 3D Molecule Generation in Data-Sparse Regions via Distributional Physical Priors

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Can we train a 3D molecule generator using data from dense regions to generate samples in sparse regions? This challenge can be framed as an out-of-distribution (OOD) generation problem. Existing works on OOD generation primarily focus on property shifts. However, the distribution shifts may come from structural variations in molecules, such as certain types of scaffolds, dubbed as physical priors. This work introduces a novel and principled diffusion-based generative framework, termed _GODD_, which enables training a generator on data-abundant distributions to generalize to data-scarce distributions under structure shifts. Specifically, we propose utilizing a designated equivariant asymmetric autoencoder to capture distributional physical priors. The asymmetric module allows generalization to unseen, out-of-distribution structural variations. As these captured physical priors represent distinct distributions, they can steer the generation of samples that are not in dense regions. We demonstrate that with these encoded structural-grained distributional physical priors, _GODD_ does not need to train with any molecules from the sparse regions. We conduct extensive experiments across various out-of-distribution molecule generation tasks using benchmark datasets. Compared to alternative baselines, our approach shows a significant improvement of up to 65.6\% in success rate, defined based on molecular validity, uniqueness, and novelty. Additionally, we show that our generative framework, steered by physical priors, can be readily adapted to canonical fragment-based drug design tasks, exhibiting promising performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the generation of OOD molecules with rare scaffolds, this work proposes a diffusion framework conditioned on physical priors from molecular fragments. The model comprises an equivariant autoencoder that encodes the 3D molecular fragment graph into equivariant and invariant latent representations as physical priors, and a diffusion model that generates molecules conditioned on the priors. The authors test the method on OOD ring and scaffold structures and show superior performance than existing methods.

### Strengths
1. This work focuses on the challenging and poorly explored problem of generating 3D molecules from the low-data domains. The proposed model shows promising results across several tasks. 
2. The authors provide comprehensive analysis on the generation results.
3. The authors also propose multiple useful evaluation metrics that could facilitate future studies on the subject.

### Weaknesses
1. From the presented generation examples, the scaffold seems to constitute a large proportion of the molecule. Thus, it is possible that the model actually learns to directly modify the given scaffold locally (as the scaffold is almost a valid molecule already) instead of really transferring the knowledge of relations between scaffolds and the full molecule structure from the data rich domain. Some additional analysis are needed to prove the claim (see Questions).  
2. The actual application of the method is somewhat limited as a pre-defined scaffold structure needs to be provided to the model.

### Questions
Major:
1. For molecules with a large number of rings, the variations of ring structure is exponentially larger. How is the input scaffold selected for the generation of molecules >10 rings?
2. Since the scaffold information is provided as a condition, not explicitly enforced, it is possible that the scaffold is edited (e.g. slight changes in atom types and coordinates) during the generation due to the stochastic nature of DDPM. From Fig 11, it seems to be quite common. How is the proportion and coverage calculated with those cases?
3. For linker design tasks, the initial structures are two molecular fragments. In this scenario, how is the scaffold defined and provided to the diffusion model?
4. Following the previous question, if the model could work with disconnected scaffold in linker design, would it also work with incomplete scaffolds? (e.g. providing an increasing proportion of the fragment to the diffusion model).
5. As mentioned in "limitations", a known scaffold structure needs to be provided. Is it possible to generalize it to randomly generated OOD scaffold structures?

Minor:
1. The authors name the prior as “physical”, while it is actually learned only from the 3D structure of the fragments. What is “physical” about it?
2. For molecules with a large number of rings, the variations of ring structure is exponentially larger. How is the input scaffold selected for the generation of molecules >10 rings?
3. As $f_h$ only has 1 dimension per atom, is the representation expressive enough? Would the model benefit from higher dimensionality?
4. How is the atom number determined when sampling $z_{x,T}$, $z_{h,T}$?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Geometric Out-of-Distribution Diffusion Model (GODD), a framework for generating 3D molecular structures in data-sparse regions by framing the challenge as an out-of-distribution (OOD) generation problem. It introduces an asymmetric encoder-decoder architecture that captures distributional physical priors from molecular fragments, enabling the model to generalize to unseen structural variations without additional training on OOD data. By leveraging these physical priors to guide the denoising process, the framework significantly improves the success rate of generating valid and chemically relevant molecules, demonstrating its effectiveness in fragment-based drug design tasks and ensuring the preservation of geometric properties through SE(3)-equivariance.

### Strengths
1. The paper introduces a method to solve the OOD generalizability problem with current SOTA diffusion models, enhancing the generation of valid 3D molecular structures in data-sparse regions.
2. The paper introduces geometric OOD and formulate distributional physical priors from molecular fragments, enabling effective capture and utilization of structural information to guide the generation process.
3. The paper is well-written, featuring clear presentation and thorough theoretical analysis that demonstrates the SE(3)-equivariance of the physical priors, ensuring geometric consistency in the generated molecules.

Overall I think this is an interesting work and open up new exploration and opportunities for AI for drug discover in terms of OOD and generalization ability.

### Weaknesses
1. The practical implications and real-world application scenario in drug discovery of geometric OOD are not clear, so the authors should explain more about the use case of their framework in this context.
2. The paper primarily focuses on OOD generation related to shifts on molecule fragments, which could be limited to scenarios where the general structure of fragments is not clear. This focus might not address more complex OOD scenarios where the entire molecular scaffold is novel, rather than just variations in fragment placement or orientation. The method's effectiveness in generating molecules with entirely new ring systems or core structures, which are often the targets in drug discovery, remains unclear.

### Questions
Please see weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the problem of sampling molecules given a sub-structure (fragment). The outlined approach could be an important tool in computer-aided drug-design, in particular in fragment based discovery. 

The approach is formulated as a denoising diffusion probabilistic model for sampling molecules conditioned on a learned embedding of a scaffold (confusingly named a 'physical prior') -- but essentially is a learned generative 'unmasking' or 'inpainting' task. The embedding is achieved by using an 'asymmetric equivariant auto encoder,' as the noise-prediction model.  

Minor comments:
In 2.2, line 160, a weight is defined but it is not used anywhere.

### Strengths
a. Good performance compared to baselines.

### Weaknesses
 a. Overly complicated and pompous presentation considering the method. It is unclear whether authors are trying to obscure the simplicity in the method by invoking overly convoluted language.  For example use "physical prior" to denote a learned embedding used to guide/steer generation.
b. Proofs on the equivariance are presented as new, yet are simple (trivial?) extensions of well known proofs in the field, and there are no references to the original work e.g. Kohler et al ICML 2020 and others. Can the authors perhaps clarify the connection to this previous work and highlight how what they present is different?
c. While the proposed method beats a range of baselines, it is unclear whether results are good enough to be useful in a practical setting. The dataset which would be a useful benchmark for a method like this, the molecular stability should be at least 50%. On QM9 which is arguably not a helpful benchmark for this task, e.g. fragment based drug design, the method barely reaches this level.

### Questions
1. I do not understand the statement that molecular stability is close to 0% on the GEOM-DRUG baseline. It is reported for most standard molecular generation tasks, benchmarks you compare against have ~80-92% AS for unconditional sampling. Are you referring to the 'OOD' generation task? That seems to be the case since the atom stability is very low (Table 3), so low in fact that it is unlikely that any molecules that are generated are even valid. It seems like the comparison is nearly meaningless. For QM9 the results are better, but still far from being utile in a practical setting, since QM9 is unlikely to be used for fragment based drug discovery.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a framework capable of generating molecules in out-of-domain distributions, specifically, those OOD distributions driven by scaffold and ring structures. The framework utilizes an asymmetric autoencoder to capture distributional physical priors (specifically, point-wise latent representations) and employs these priors to guide downstream generative models. The authors demonstrate the effectiveness of their approach through extensive experiments on the QM9, GEOM-DRUG and GEOM-LINK datasets.

### Strengths
1. Tackling the task of generating OOD molecules, specifically focusing on scaffolds not seen during training, is a valuable and practically important challenge, especially in applications like drug design. This work makes significant progress in formulating and addressing this problem.
2. The experimental performance of the proposed GODD framework shows promising results.
3. The codes that the authors provide seem well organized and ready-to-run (though I did not try to reproduce it).

### Weaknesses
1. Ambiguous Statements: The definitions of $p_\theta(z_x, z_h, f_x, f_h)$ and $\epsilon_\theta(z_x, z_h, t, f_x, f_h)$ are unclear. Specifically, how are $f_x$ and $f_h$ integrated into the noisy point clouds $z_x$ and $z_h$, and how does the EGNN ($\epsilon_\theta$) operate on this mixed point cloud? This is a critical aspect of the method but is not discussed in sufficient detail (correct me if I missed something). Additionally, Figure 1 is somewhat confusing: It depicts the physical prior as a global-level representation, whereas it is actually a latent point cloud, which is conceptually quite different (lots of previous and concurrent work has managed the first case).
2. Potentially Unfair Comparisons: The experimental comparisons may be somewhat skewed. For example, in Tables 2 and 3, models like EDM, GeoLDM, and EquiFM condition on nothing, so it’s not surprising that the percentage (P%) of OOD generation is small, which likely reflects the rarity of OOD structures in the overall distribution. This is even pronounced when these models weren’t even trained on the entire dataset. While the authors attempt to construct comparable baselines such as C-EDM, conditioning on a single number seems less fair compared to the geometry elements (referred to as physical priors) that GODD conditions on. In fact, these geometry elements are the targets we aim to generate, so evaluating the partition of these elements in the output when they are taken as input may not be as fair. Furthermore, the inclusion of methods like EDM, which are not designed for conditional generation, is questionable for a fair comparison in this context.

### Questions
See “Weaknesses”.

### Soundness
3

### Presentation
2

### Contribution
3
