# E(3)-equivariant models cannot learn chirality: Field-based molecular generation

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
Obtaining the desired effect of drugs is highly dependent on their molecular geometries. Thus, the current prevailing paradigm focuses on 3D point-cloud atom representations, utilizing graph neural network (GNN) parametrizations, with rotational symmetries baked in via E(3) invariant layers. We prove that such models must necessarily disregard chirality, a geometric property of the molecules that cannot be superimposed on their mirror image by rotation and translation. Chirality plays a key role in determining drug safety and potency. To address this glaring issue, we introduce a novel field-based representation, proposing reference rotations that replace rotational symmetry constraints. The proposed model captures all molecular geometries including chirality, while still achieving highly competitive performance with E(3)-based methods across standard benchmarking metrics.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tackles the limitations of E(3)-invariant features in modeling chirality, as mirror symmetry is inherently implied in such features. The authors first provide a theoretical motivation, illustrating why E(3)-invariant features are inadequate for representing chirality. They then propose using fields to model molecular graphs, learning these fields through a reverse diffusion process. The effectiveness of their approach is benchmarked on the QM9 and Geom datasets.

### Strengths
Chiral awareness in E(3)-invariant architectures is essential for accurately modeling molecular properties. I appreciate the authors’ approach of representing molecules as collections of fields corresponding to atoms and bonds. These fields, as probability densities, closely mirror the quantum mechanics formalism than point clouds, where molecules are wavefunctions. This aligns with methods like Density Functional Theory (DFT), which models charge density and provides a more expressive representation than point clouds. However, the impact on memory overhead from this approach warrants further investigation. Overall, I found this paper to be well-written, clearly delineating previous work, the contributions of this study, and its limitations.

### Weaknesses
The impact of this approach on memory overhead requires further investigation. How does the memory overhead compare to point cloud representations? Could you provide insights on how memory usage scales with increasing molecule size and greater diversity of atom and bond types?

### Questions
Please see weakness.

### Soundness
3

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
3

### Summary
This paper proposes to generate molecules by representing them as functions in 3D space. Each atom is represented as a gaussian distribution centered at the atom position. The bonds are represented similarly with the center of the gaussian being placed at the center of the bonds. Compared to  such a representation can learn the chirality since it bears the reflection invariance. Experiments are conducted on QM9 and GEOM.

### Strengths
- Since most deep learning methods use GNNs for molecules, using CNNs is novel.
- As stated by the authors, capturing chirality is important for representing molecules. And GNN-based methods may have difficulty in breaking  the reflections symmetry.

### Weaknesses
 - Although alignment methods are employed, the proposed method cannot guarantee the rotation invariance. Specifically, while the authors align molecules based on their principal axes, this alignment is deterministic and does not account for the continuous nature of rotations. This means that a slight perturbation in the input molecule's geometry could lead to a significantly different alignment, and thus a different representation, which is not ideal for a rotation-invariant model. This lack of robustness to small changes in orientation is a significant limitation.
- As shown in table 2, the molecule graph quality metric is not good on the QM9 dataset. In particular, the atom type distribution (TV_a) is significantly worse than other methods. This indicates that the model struggles to accurately reproduce the correct distribution of atom types, which is a critical aspect of molecular generation. While the authors achieve competitive results on other metrics like MST and bond type distribution (TV_b), the poor performance on TV_a raises concerns about the overall quality of the generated molecules.

### Questions
- What's the trade-off between losing rotation invariance and gaining the ability of learning chirality?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors identify a critical limitation in current E(3)-equivariant models for 3D molecular generation: they cannot properly account for molecular chirality, which is crucial for drug efficacy and safety. To address this, they introduce a field-based representation approach that replaces rotational symmetry constraints with reference rotations, allowing their model to correctly capture chiral properties while maintaining competitive performance with existing E(3)-based methods. They provide theoretical proofs showing why E(3)-equivariant models must necessarily ignore chirality, and demonstrate empirically that their method (FMG) achieves state-of-the-art performance in molecular neutrality while successfully capturing chiral properties, though at the cost of increased computational complexity for larger molecules.

### Strengths
The work identifies and addresses a fundamental limitation in current E(3)-equivariant models regarding chirality, which has been largely overlooked in previous research. Besides, it provides original theoretical proofs about the inherent limitations of E(3)-equivariant models in handling chirality.

The overall quality is high, reflected by the rigorous theoretical foundation with formal proofs about E(3) invariance and chirality (Propositions 1-3) and comprehensive empirical validation on standard benchmarks (QM9 and GEOM datasets). Well-structured presentation with clear motivation and problem statement. Ablation studies and

### Weaknesses
The first weakness is the method's computational complexity scales with the volume of the 3D grid (H×W×D), making it potentially intractable for larger molecules. As the author mentioned chirality in amino acids, will be a bottleneck for implementing the model in bio- and pharma-tasks. The current implementation requires high-resolution grids to maintain accuracy, leading to significant memory requirements. The scaling issue is a major concern, especially when considering that the grid resolution directly impacts the accuracy of the field representation; finer grids lead to better accuracy but drastically increase computational cost. This makes the method less practical for larger molecules, which are common in biological and pharmaceutical applications. Another limitation is the analysis of field parameter sensitivity (σ, γ) is not very clear. The lack of a systematic exploration of how these parameters affect the model's performance makes it difficult to understand the robustness of the method. The choice of these parameters seems somewhat arbitrary, and it is not clear how they should be tuned for different molecular systems. The analysis should include a more detailed investigation of the impact of these parameters on the model's ability to capture molecular properties and generate realistic structures.

### Questions
1. Could adaptive grid resolutions or sparse representations help reduce memory requirements while maintaining accuracy?
2. How sensitive is the model's performance to the choice of field parameters (σ, γ)? What's the theoretical basis for choosing these values?
3. Why did the authors choose 0.33Å resolution for the grid, and how would different resolutions affect the quality-efficiency trade-off?
4. How might this approach be extended to other molecular properties beyond chirality? 
5. Since chirality is a crucial property of molecules that are involved in drug discovery, is there any specific case that the author can provide on the FMG? Other than that, some properties that are not related to the chirality of the molecule (i.e. orbital energies), why FMG outperforms?
6. Can this model be utilized in total synthesis and retrosynthesis?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a field-based diffusion method for molecule generation that is not invariant with respect to the chirality of the generated molecules. Recognizing that chirality is a critical property influencing the bioactivity of molecules—with several famous examples underscoring its impact on molecular toxicity and drug efficacy—the approach addresses an important aspect of molecular design.

The results demonstrate comparable performance to EDM and MiDi in terms of molecule validity and stability. The authors also highlight molecular neutrality as an important metric for generated molecules. Furthermore, they assess MMFF energies for the 3D molecules and compute the Wasserstein distance between the bond length distributions and bond angle distributions of the generated molecules and those of the dataset molecules.

### Strengths
The authors proposed a novel approach to molecular generation using field representations and developed a required theoretical background for the approach. The authors prove challenges to incorporate the same restriction in current E(3) equivariant models.

### Weaknesses
1. Overstated Claims of State-of-the-Art Performance: Although the paper claims to achieve state-of-the-art (SOTA) performance, it falls significantly behind previously published models such as JODO, EQGAT-Diff, and the more recent Semla-Flow—all of which were published before ICLR 2025. The performance gap is quite substantial. For larger and more realistic molecules in the GEOM Drugs dataset, only 16% have all valid atoms according to the paper's model, whereas other models are approaching perfect scores on these metrics.

2. Equivariance Requirement Not Essential for High Performance: Some models that operate directly in E(3) space are eliminating the need for equivariance. For instance, Simplified Scalable Conformer Generation (MCF) demonstrates significant performance improvements in conformer generation without the requirement for equivariance. While MCF tackles a slightly different task, it illustrates that we can develop equivariance-unaware models for molecular modeling that achieve genuine SOTA performance.

3. Incorrect Basis for Neutrality Metrics: The neutrality metrics in the paper are based on inaccurate assertions. Specifically, the statement: "Atom neutrality is the percentage of atoms with a formal charge of 0, while molecules are neutral if all their atoms are neutral." is incorrect. For example, nitromethane has charged oxygen and nitrogen atoms but is an overall neutral molecule. Atoms within a molecule can carry formal charges that balance out, resulting in a neutral molecule despite individual atoms being charged.

4. Inadequate and Incomplete 3D Structure Evaluation: The evaluation of the 3D structures is poor and incomplete. The paper only compares distribution differences for bond lengths, angles, and energies. These benchmarks are difficult to interpret and can be significantly affected by a single outlier result. Depending on the implementation—for example, in MiDi's implementation—one problematic molecule can drastically alter the results. Even with these limitations, the model does not outperform MiDi on these benchmarks.

5. Overstated Importance of Chirality Awareness in the Model: The emphasis on chirality awareness in the model may be overstated. 3D molecule generation serves as a foundational model for structure-based drug design or molecular docking. In these applications, the provided environment (such as a protein or part of a protein) creates asymmetric restrictions on the generated molecule, naturally leading to the production of the appropriate enantiomer. Additionally, in conditional generation, the classifier itself can learn chirality in a simpler way.

### Questions
Questions to the Authors:

1. Your model underperforms compared to JODO, EQGAT-Diff, and Semla-Flow but claims SOTA performance. Can you add a comparison to one of these models?

2. Since non-equivariant models like MCF achieve high performance, can you check whether it still cannot distinguish chiral conformers?

3. Your neutrality metric seems inaccurate (or at least description) (e.g., nitromethane is neutral despite charged atoms). Can you address this issue?

4. Is the strong focus on chirality awareness justified when environmental factors often determine enantiomer generation in practice?

### Soundness
2

### Presentation
3

### Contribution
3
