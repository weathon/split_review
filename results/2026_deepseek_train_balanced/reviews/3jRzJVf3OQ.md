**Review of "Quantum entanglement for attention models"**

---

## Summary

This paper proposes replacing the dot-product similarity in Transformer attention with entanglement entropy computed from parameterized quantum circuits (PQCs), creating a hybrid quantum-classical attention layer. It evaluates this approach on small-scale classification tasks (MC, RP, subsampled MNIST/FMNIST, MNIST-1D, and quantum-generated Q(E3) data). The paper reports that entanglement-based attention outperforms classical scaled-dot-product attention on small datasets and exhibits a smaller generalization gap.

---

## Strengths

- **Systematic ablation of entanglement measures (Table 1).** The paper compares multiple entanglement measures (Von Neumann entropy, SWAP test, QSANN, QSAMb, QSAMo) on the MC and RP datasets and identifies Von Neumann entropy as the best performer. This grounds the architectural choice in data rather than assumption, which is stronger than prior quantum attention work that does not perform such ablation.

- **Consistent smaller generalization gap finding.** The paper reports (Figure 3) that the quantum attention model yields a smaller gap between training and test accuracy across all tested datasets and sizes. This is a distinct observation not reported in prior quantum-attention literature.

- **Open-source code provided.** The reproducibility statement (line 155) provides a link to the code, which partially mitigates some of the specification gaps in the paper text.

- **Nearest Exemplar Accuracy (NEA) as a disentangled metric.** The paper introduces NEA (line 94) computed from CLS token embeddings using class-mean prototypes with cosine similarity, aiming to isolate the quality of the attention layer's learned representations from the linear classification head capacity.

---

## Weaknesses

### Major

1. **Method critically under-specified in the paper.** Section 4.3 ("Measure Entanglement") states "We consider the following measures of entanglement" (line 83) and then the section ends without any definitions. Von Neumann entropy — the measure used throughout — is never formally defined: no formula, no mention of how the partial trace or density matrix is computed. Additionally, the quantum attention equation (line 80) shows `A = ME(U_PQC(...))` without a softmax, while the classical attention equation (line 57) includes `softmax(A/√d_h)`. The paper never clarifies whether softmax is applied (or omitted) for the quantum version, which is a fundamental architectural choice. The PQC topology (qubit pairing pattern, number of layers) is not specified beyond "Controlled-RX gates exclusively" (line 74). The number of data-reuploading iterations is not given. **The word "gradient" does not appear anywhere in the paper**, yet the PQC parameters must be trained — how gradients are computed (parameter-shift rule? finite differences? straight-through estimator?) is never addressed. While the code may fill some of these gaps, the paper text should be self-contained.

2. **Evaluation on toy problems where statistical noise dominates comparisons.** The paper tests on MC (130 sentences, 70 training), RP (105 sentences, 74 training), and subsampled MNIST/FMNIST with images resized to 12 tokens via bilinear interpolation. The Transformer is minimal: single head, no output projection, vectors of length 12. The paper itself notes that in some runs "test accuracy is slightly higher than training accuracy, which might be due to a variance of performance estimation" (line 120) — a direct admission that the results are dominated by statistical noise. With 70–74 training examples, differences in interquartile mean across 10 seeds do not constitute convincing evidence that one mechanism is superior to another. The paper's central claim — that entanglement-based attention "outperforms" classical attention — is not reliably supported at this scale.

3. **Unfair QSANN comparison.** To ensure architectural consistency, the paper modifies QSANN by adding a CLS token (line 100) and reports that this modification "significantly decreased" QSANN's performance (line 110). The paper then compares its proposed method against this *degraded* version of QSANN. While the modification was made with the reasonable goal of matching architectures, the paper acknowledges the modification hurts QSANN, which undercuts the comparison. A fairer evaluation would compare against the original QSANN (which uses mean-pooling) on an equal footing, or report both versions.

4. **Quantum-generated dataset experiment lacks a competitive classical baseline.** On the Q(E3) dataset (Huang et al., 2021), the paper compares entanglement-based attention only against a "simple classical Transformer encoder" (line 114). The original Huang et al. paper used an MLP and showed that standard classical models *can* perform well with the right kernel features. The proper baseline is not a vanilla Transformer but a classical model designed to handle PQK features — such as the MLP from the original work or a kernel method. Showing that a naive classical Transformer fails on PQK features and that a quantum model succeeds is not surprising and does not establish superiority over reasonable classical alternatives.

5. **No computational cost analysis.** The paper never discusses the cost of computing entanglement entropy versus dot-product attention. Simulating even small quantum circuits for each (query, key) pair on a classical simulator incurs overhead that grows exponentially in the number of qubits in the worst case. For 12 qubits and N tokens, the naive cost is O(N² · 2¹²) per layer versus O(N² · 12) for dot-product attention. Whether this cost is acceptable — or whether the simulation is actually tractable at this scale — is never addressed. This omission is significant given that all experiments are performed on a classical simulator.

### Minor

- **Novelty claim is somewhat overstated.** The paper states it is "the first work that showcases measures of entanglement in classical machine learning models and also shows specific scenarios where entanglement-based attention outperforms classical attention models" (line 47). The broader part of this claim overlooks the substantial body of quantum kernel methods (Havlíček et al., 2018; Schuld & Killoran, 2019; Liu et al., 2021), which use entanglement-based similarity measures in classical ML pipelines. The specific application to Transformer attention is indeed novel, but the framing as "first work" on entanglement in classical ML is imprecise.

- **Key quantitative results are embedded in images (Table 2, Figures 2–4) rather than reported in text or machine-readable tables.** This makes independent verification of the numerical claims (accuracy values, generalization gap magnitudes) more difficult than necessary. Given the small scale of the experiments, the actual numbers matter greatly for assessing statistical significance.

### Trivial

- Figure reference at line 75 reads "Figure ??," indicating an unresolved cross-reference.
- The parameter count description at line 92 contains garbled text ("embed dim $\ast\nmid$ classes").

---

## Nice-to-Haves

- Reporting confidence intervals or effect sizes (not just IQM) would help assess whether the observed advantages on small datasets are statistically meaningful.
- An ablation controlling for extra model capacity: comparing quantum attention against classical attention with additional learned parameters matched to the PQC parameter count, to test whether improvements come from the entanglement measure itself versus simply having more trainable parameters or a more complex similarity function.
- Clarifying on which dataset(s) each of the three encoding schemes (super dense, dense, IQP) was used.

---

## Removed Points

The following points from the reviewer inputs were identified as candidates for removal, and are provided here for reference only:

- **Critique about experiments using classical simulation rather than quantum hardware as a "fundamental disconnect" — overly strict.** The paper explicitly acknowledges in its Limitations section (line 148) that "the experiments here were conducted on a classical simulator." Top-venue quantum ML papers routinely use simulators. The legitimate concern here (retained as Major #5 above) is the *missing discussion of computational cost*, not the use of simulation itself.
- **"Generalization gap could mean underfitting" — kept but weakened.** The paper reports higher test *accuracy* alongside the smaller gap on small datasets, so the underfitting concern is partially addressed. Remains as a minor caution but does not invalidate the finding.
- **Several section-by-section notes about missing related work — removed per instructions** (I cannot confirm what related work exists).
- **Formatting/style nitpicks and parser artifact complaints — removed per instructions.**

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Fully specify the method in the text: provide the formal definition of how entanglement entropy is computed (von Neumann entropy formula, partial trace operation), clarify whether softmax is applied, specify the PQC topology (number of layers, qubit connectivity), and describe how gradients are estimated for the PQC parameters.
2. Run experiments on problems where attention mechanisms are known to matter and where the training set is large enough for results to be statistically meaningful. Current datasets (70–74 training examples) are too small to support the claimed conclusions.
3. Compare against proper baselines for the Q(E3) dataset (e.g., the MLP from Huang et al. 2021, or kernel methods), and report original (unmodified) QSANN results alongside the CLS-token variant.
4. Include a computational cost comparison (wall-clock time per training step, scaling with qubit count and sequence length) to ground the practical significance of the approach.
5. Report all key numerical results (accuracy values, generalization gap magnitudes) in machine-readable table form rather than embedded images.

---

## Score and Decision

**MY FINAL SCORE:** <score>3.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>