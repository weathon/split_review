## Human Reviewer 1

### Summary
This paper introduces GMD-25, a benchmark designed to assess compositional generalisation in machine-learning interatomic potentials (MLIPs). The authors propose four carefully structured tasks—Length Extrapolation, Functional Group Composition, Duplication, and Combination—to examine whether models can generalise to unseen molecules by recombining known structural motifs.

### Strengths
The four tasks are conceptually clear and interpretable, each corresponding to a concrete physical generalisation challenge (length, duplication, functional-group recombination).

### Weaknesses
The benchmark evaluation relies almost entirely on models from 2018–2022 (SchNet, PaiNN, DimeNet++, GemNet). These models are now well-known baselines but no longer representative of the current frontier in MLIPs. The inclusion of EquiFormer-V2 is appreciated, but as a relatively unstable and non-conservative Transformer variant, it cannot represent the practical performance envelope of modern MLIPs.

Recent architectures such as MACE (Batatia et al., NeurIPS 2022), NequIP (Batzner et al., Nature Comm 2022), eSCN (2024), and ViSNet (2023) have become de facto standards for equivariant force fields and would provide a much stronger reference point. As a result, the current experimental section cannot convincingly support claims about state-of-the-art generalisation behavior.

While the four tasks are conceptually appealing, they remain relatively simple from the perspective of modern models, such as MACE and eSCN. For example, the Length Extrapolation and Functional Group Duplication tasks involve only small organic chains with linear motifs; these are unlikely to challenge advanced equivariant models that already generalise well across chain lengths and simple functional groups.

Without testing stronger models on more demanding tasks, it is hard to judge whether the observed generalisation gaps are fundamental or simply reflect underpowered baselines.

The manuscript lacks a clear justification of whether all models were tuned to their best configuration, and whether they were trained with equal computational budgets. Including stronger baselines makes this aspect even more important.

### Questions
See Section Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper proposes a new benchmark dataset for interatomic potentials, testing the generalizability on the chemical space.

### Strengths
- The problem addressed is topical, and the field of machine learning potential model development would benefit from an innovative benchmark dataset that specifically focuses on the generalization ability.
- The paper is well structured, with the focuses and emphasis of the introduced dataset clearly conveyed.
- The benchmark of the state-of-the-art architectures is extensive.

### Weaknesses
- MAE for forces is not a great measure of force discrepancy as it is not rotationally invariant.
- The authors could use slightly more introduction to the idea of functional groups and chemical diversity to the ICLR readers who are not experts in chemistry.
- I feel like the technical results introduced to the machine learning community represented by the ICLR readership is perhaps limited. This paper might be more suitable for publication in a field-specific journal.

### Questions
- Could you explain a bit more why you chose the somewhat new GFN2-xTB method, as opposed to more popular methods?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper introduces GMD-25, a benchmark for testing compositional generalisation of machine-learning force fields.  It defines four out-of-distribution (OOD) tasks where models are trained on molecules of one type and tested on related but disjoint molecules.  The authors generate molecular dynamics trajectories for a set of small organic molecules, then compute reference energies and forces using the GFN2-xTB semi-empirical method. The key finding is that all models achieve low error on in-distribution data but suffer a dramatic accuracy drop on OOD test sets. The paper concludes that current MLFFs may primarily interpolate training data and highlights the need for more physically-driven models with better transferability

### Strengths
1. The paper targets a relevant gap: existing MLFF benchmarks typically train and test on the same molecules, leaving generalisation untested.
2. The authors emphasize reproducibility: the full dataset, splits, and training framework will be released upon acceptance
3. The paper is easy to read

### Weaknesses
1. The benchmark uses GFN2-xTB to label energies and forces. GFN2-xTB is a semi-empirical tight-binding method (not a high-level ab initio method).  While the authors describe it as “more accurate” and “robust”, it is well known that GFN2 is significantly less accurate than DFT or higher-level quantum calculations. In standard MLFF benchmarks, one typically uses DFT to obtain reference forces. Using a semi-empirical method likely introduces non-negligible error/noise into the labels, which may confound the evaluation of generalisation. The paper does not quantify the error of GFN2-xTB itself nor justify that it is “accurate enough” for this purpose.
2. Although a few classical MLFF architectures is included, the model selection omits several important recent advances. In particular, foundation or large pre-trained models, e.g. UMA, JMP, MACE, are explicitly excluded. The authors argue this is to avoid “memorisation” effects, but excluding such models greatly limits the relevance of the results to the current state of the field.  Many state-of-the-art force fields now use massive pre-training then finetuning to improve generalisation.  By not evaluating any pre-trained MLFFs, the paper’s conclusions apply only to a narrow slice of older models.  In practice, practitioners would likely use a pre-trained model for OOD tasks, so the benchmark’s insight into realistic performance is limited. 
3. The paper is essentially a dataset and benchmark rather than a new modeling method. The idea of splitting training/test molecules to test extrapolation is natural and has been explored. While GMD-25 is carefully constructed, it mostly evaluates known phenomena (models overfit to training molecules) and does not introduce fundamentally new theory or techniques. In its current form, the contribution is mainly empirical. Given this, the benchmark may be more appropriate for a dataset/benchmark track. Furthermore, the tasks focus on fairly simple organic molecules (linear alkanes and functionalized variants).  It is not clear how well the conclusions would extend to more complex chemistries (e.g. heteroatom-rich systems, inorganic materials, 3D conformers, etc.).

### Questions
1. Why was GFN2-xTB chosen for generating the ground-truth energies and forces? Can the authors provide evidence that GFN2-xTB labels are sufficiently accurate (e.g. by comparison to DFT on a subset)? How might any inaccuracies in GFN2-xTB affect the benchmark results?
2. The authors excluded “foundation” or pre-trained MLFF models from evaluation ￼. Could the authors discuss how a top pre-trained model (e.g. UMA) would be expected to perform on these tasks? Are there plans to include such models to more fully assess state-of-the-art generalisation?
3. The proposed benchmark is well organized, but it essentially constitutes a new dataset/experimental protocol. Can the authors clarify what novel insights or techniques this work offers beyond the dataset itself? In particular, how does GMD-25 advance our understanding of MLFF generalisation compared to existing datasets like MD17 or ANI-1? Why is it presented as a main-conference contribution rather than a dataset track?
4. The tasks involve specific chemical classes (e.g. alkanes, alcohols, acids). How sensitive are the results to these choices? Would the authors expect similar findings if the benchmark included, say, aromatic systems or biomolecules? In other words, how broadly do the authors expect the large generalisation gaps to extend?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
The paper introduces a new benchmark for evaluating compositional generalization in machine learning force fields (MLFFs). It defines four types of tasks, each targeting different aspects of out-of-distribution (OOD) behavior and evaluates five representative models (GNNs and Transformers) on force and energy prediction errors for both in-distribution (ID) and OOD settings. The study finds that all models experience significant degradation in performance when tested on OOD data, underscoring the difficulty of achieving robust generalization in MLFFs.

### Strengths
The OOD generalization of MLFFs is  a crucial area of research.
Decomposing generalising in composition to well structured 4 tasks is commendable.

### Weaknesses
Limitations and suggestions:

a) Scope of generalization: While compositional generalization is addressed, extending the benchmark to temperature variations, allotropic forms, and non-polymeric systems would improve its coverage. Limiting the dataset to small organic molecules is restrictive.

b) Missing state-of-the-art (SOTA) models: The benchmark omits newer high-performing models listed on resources such as the MatBench Discovery Leaderboard(https://matbench-discovery.materialsproject.org/). Including a few top-performing models would make the comparison more comprehensive.

c)Architectural bias analysis: Although the conclusion claims that the benchmark can reveal architectural biases, the paper lacks clear analysis or discussion explaining why certain architectures perform differently.

d)In Figure 4g, GemNet’s energy error appears similar for ID and OOD? I would expect considerably better performance on ID as for other models.

e)In Figure 2,  SchNet performs poorly on force MAE but achieves the lowest energy MAE. Please explain this divergence.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4