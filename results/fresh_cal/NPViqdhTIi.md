Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper adapts a Gzip-based, parameter-free text classification method (Jiang et al., 2022) to molecular property prediction. It extends the method with multiprocessing, class-weighted kNN, a weighted-kNN regressor (Equation 3), multimodal input concatenation (SMILES + protein sequences), and MolZip-Vec—a scheme that bins 200 RDKit numerical descriptors into Unicode characters and concatenates them with the SMILES string. The method is evaluated on MoleculeNet classification/regression tasks and PDBbind binding-affinity prediction against ChemBERTa-1/2, GROVER_large, and several GNN baselines. The core claim is that compression-based methods can reach the performance of early-generation chemical transformers without any GPU training or hyperparameter tuning.

## Strengths

1. **Parameter-free method that matches early chemical transformers on a subset of tasks, requiring no GPU training.** MolZip outperforms ChemBERTa-1 on 3 of 4 classification tasks and matches GROVER_large on BBBP and HIV (Table 1). On regression, MolZip-Vec beats ChemBERTa-2 (MLM) on 3 of 4 datasets (Table 2). On PDBbind, MolZip surpasses all GraphDTA, GCN, GAT, and GIN baselines (Table 3). These results directly support the paper's central claim that a compression-based approach can be surprisingly competitive with early deep learning baselines while being entirely training-free.

2. **Substantive extensions beyond the original NLP-only Gzip method.** The paper extends Jiang et al. (2022) to weighted-kNN regression (Equation 3), class-weighted classification for imbalanced datasets (Equation 2), and multimodal inputs via concatenation of SMILES with amino acid sequences for protein-ligand binding affinity prediction (§3.1, §2.3). These are non-trivial extensions that broaden applicability to core chemical ML tasks.

3. **MolZip-Vec: a novel string-based encoding of numerical descriptors that demonstrably improves regression performance.** Binning 200 RDKit molecular descriptors and mapping them to non-ASCII Unicode characters (avoiding collision with SMILES' ASCII character set) enables the compression algorithm to jointly model structure and precomputed properties. MolZip-Vec consistently improves over plain MolZip on all four regression tasks in Table 2, with the benefit scaling with training set size (Fig. A.2 referenced). This is a specific, testable methodological contribution.

4. **Practical open-source implementation.** The reported implementation supports multiprocessing, multi-class classification, class-weighting, SMILES augmentation, and alternative string representations (DeepSMILES, SELFIES). The low-resource advantage is underscored by the 43h 55m total benchmark time on a single consumer CPU (§3.3).

## Weaknesses

### Fatal
None.

### Major

- **Data splits are not explicitly stated for MolZip/MolZip-Vec evaluations, creating ambiguity in the central comparisons.** The paper reports that baseline GROVER results are from Zhou et al. (2023) "based on scaffold splits" and that other baselines are taken from published papers, but it never explicitly states which train/validation/test split (scaffold, random, or other) was used when running MolZip and MolZip-Vec on the same datasets. While the context ("benchmark the proposed methodology using the MoleculeNet benchmark," line 21) and awareness of split choice (scaffold splits mentioned for GROVER baselines) make it likely that standard scaffold splits were used, the omission means the comparison is not fully reproducible from the manuscript alone. For a paper whose headline empirical claim rests on cross-method comparisons, this is a significant reporting gap that must be closed.

### Minor

- **Results are reported as point estimates without any measure of variability.** Tables 1–3 show single AUROC/RMSE values with no error bars, confidence intervals, or even a statement about whether results are from a single fixed split or multiple seeds. For a deterministic method on a fixed split this is less concerning than for stochastic baselines, but the choice of split introduces variability. Since several comparisons are close (e.g., MolZip vs. GROVER on BBBP: 0.886 vs. 0.886), the absence of variability information makes it difficult to assess whether differences are meaningful.

- **No hyperparameter sensitivity analysis for k in kNN or bin count in MolZip-Vec.** The choices k=5 (classification) and k=25 (regression) are stated without justification or ablation (e.g., a line plot of performance vs. k). Similarly, 256 bins for descriptor encoding is asserted as "empirically suitable" without any sensitivity analysis. These are small ablations that would significantly strengthen the paper's empirical foundation.

- **The open-source library is referenced but unnamed and not linked.** The paper states the method is released "through an open-source Python library" (line 14) but provides no name, repository URL, or citation. While anonymity may be a concern in the submission format, this limits immediate reproducibility assessment.

- **The runtime comparison is incomplete for the "low-resource" claim.** The paper reports total benchmark time (43h 55m) on a single CPU but does not compare this to the training + inference time of the baselines (which require GPU hours). A wall-clock comparison would substantially strengthen the case for practical utility.

### Trivial
None.

## Nice-to-Haves

- **Deeper analysis of why MolZip-Vec degrades classification but improves regression.** The paper observes this asymmetry but only speculates briefly (§2.3: "hinting at the importance of a relatively fuzzy representation"). An ablation varying descriptor inclusion across tasks would be informative.
- **Quantitative evaluation of the chemical information retrieval claim.** The TMAP visualization (Figure 1) is qualitative; a retrieval precision/recall experiment would substantiate the claim of practical utility for ultra-large database search.
- **A scaling plot showing prediction time vs. dataset size**, directly addressing the acknowledged limitation of high time complexity.

## Removed Points

The following points raised by the reviewer(s) were removed with justification:

- *Criticism that Molformer-XL is selectively excluded, making the "transformers" comparison misleading.* **Removed because:** The paper explicitly states the exclusion of Molformer-XL and its rationale (§2, line 21: "in order to compare architectures that represent early efforts on the respective methodologies"). The paper's claims are consistently scoped to "baseline implementations of transformers" (line 36) and "baseline BERT- and GAT-based transformers" (Conclusion, line 133). This is transparent and appropriate, not misleading.

- *Concern that concatenating Unicode characters could interfere with compression patterns.* **Removed because:** This is speculative. The paper's claim about character collision avoidance is factually correct (SMILES uses ASCII; MolZip-Vec uses non-ASCII Unicode) and the compression-pattern concern is not tested or supported by evidence from the paper.

- *"The discussion of SMILES vs. DeepSMILES vs. SELFIES... the decision to report only non-augmented results while observing strong augmentation gains in regression creates inconsistency."* **Removed because:** The paper explicitly justifies this choice — "to be compatible with the results reported for the classification tasks" (line 43) — which is a reasonable consistency decision.

- *Strength about "practical utility for chemical database retrieval."* **Downgraded from standalone strength to a qualitative observation; moved here because** the evidence is limited to a single TMAP visualization without quantitative retrieval metrics.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel angle that the paper itself does not already articulate. The key insight — that Gzip compression distance on SMILES strings captures enough molecular structure to compete with early neural models — is the paper's own finding.

## Suggestions

1. **Explicitly state the data split protocol.** In the first paragraph of Section 2, add a sentence: "For all MoleculeNet benchmarks, we used the standard scaffold split (80/10/10 train/validation/test)." For PDBbind, specify the dataset version (v2016 or whichever was used) and split.
2. **Add variability estimates.** Report results over 3–5 random scaffold-seeded splits, or at minimum state that results are from the single standard split.
3. **Add a brief sensitivity analysis** for k in kNN (e.g., a mini-table or line plot for one dataset showing performance at k=3,5,10,25,50) and for bin count (e.g., 64, 128, 256, 512).
4. **Include a runtime comparison table** showing training+predict time for MolZip vs. GPU-hours for the baselines, to substantiate the low-resource advantage.
5. **Name and reference the open-source library** (if anonymity is not a constraint).

## Score and Decision

**Score:** The paper tackles an interesting and well-motivated question with a clean, transparent method and makes genuine extensions beyond the prior NLP work. The empirical results are promising, the MolZip-Vec contribution is concrete, and the claims are appropriately scoped. The primary weakness is a reporting gap (unspecified splits) that is significant but fixable and does not invalidate the core findings given the context of the MoleculeNet benchmark. Minor weaknesses (no error bars, no sensitivity analysis) are common in first-generation method papers and can be addressed in revision. Overall, the paper makes a solid contribution to the molecular property prediction literature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>