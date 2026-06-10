I have all the information I need. Let me produce the final consolidated review.

## Summary

Seq2Exp proposes a framework for gene expression prediction that learns a per-base soft/hard mask via a Beta-distributed information bottleneck, combining evidence from DNA sequences (modeled by a Caduceus network) and epigenomic signals (non-parametric). The masked subsequences are then fed to a predictor Caduceus to estimate expression. The paper reports improvements over Enformer, HyenaDNA, Mamba, Caduceus, and EPInformer on K562 and GM12878 cell types.

## Strengths

- **Beta-distribution product property enables closed-form fusion.** Modeling both \(p(M|X_{\text{seq}})\) and \(p(M|X_{\text{sig}})\) as Beta distributions and exploiting Proposition 2 (the product of two Beta PDFs, when normalized, is another Beta) is mathematically clean and allows modality fusion while staying in the same distribution family — more principled than the hard thresholding used in prior work like EPInformer.

- **Consistent empirical gains over all baselines.** Across both K562 and GM12878 cell types, Seq2Exp-soft achieves the best MSE, MAE, and Pearson correlation (Table 1). The improvement over EPInformer is ~13% relative MSE reduction on K562 and ~5% on GM12878. The soft mask variant consistently outperforms the hard mask variant.

- **End-to-end differentiability.** The reparameterized Beta sampling (Gamma → Dirichlet → Beta) for soft masks and straight-through estimator for hard masks is a technically sound design that enables gradient-based training despite discrete mask decisions.

## Weaknesses

### Fatal

None.

### Major

**1. No ablation studies — the source of improvement is unidentifiable.** Seq2Exp has multiple components (sequence-based Beta branch \(\alpha_1,\beta_1\), signal-based Beta branch \(\alpha_2,\beta_2\), product combination via Proposition 2, KL information bottleneck regularization, Caduceus backbone for both generator and predictor) whose individual contributions are never isolated. Without ablations — e.g., removing the generator (full unmasked input), removing KL regularization, using a fixed random mask, or using only one modality — it is impossible to determine which component drives the reported gains. For a paper whose core claim involves a novel mask mechanism, this is a critical gap in evaluation.

**2. Model capacity confound and an anomalous baseline.** Seq2Exp uses two Caduceus models (generator + predictor), roughly doubling parameter count vs. all baselines which use a single model. The most direct single-model controlled baseline — "Caduceus w/ signals" (a single Caduceus receiving concatenated sequence + epigenomic features) — performs *worse* than plain Caduceus on K562 (MSE 0.2411 vs. 0.2217), despite the addition of informative features. This anomalous result is not discussed, and no attempt is made to build a stronger single-model baseline that integrates signals effectively. The paper therefore does not demonstrate that the mask mechanism — rather than increased model capacity or a particular training configuration — drives the reported improvements.

**3. Regulatory element "discovery" claim lacks any biological validation.** The paper claims that Seq2Exp "discovers" regulatory elements and that extracted regions "serve as a better subsequences compared to statistical peaks calling methods." The only evidence is Table 2, comparing prediction performance using Seq2Exp's mask vs. MACS3-defined regions. This is training-set-circular: the mask was trained to minimize prediction error, so it is expected to outperform an untrained statistical peak caller at the same task. There is no independent biological validation — no overlap analysis with ENCODE cCREs, FANTOM5 enhancers, Roadmap Epigenomics annotations, transcription factor binding sites, or CRISPR perturbation data. The MACS3 comparison alone does not establish that the learned regions correspond to biologically meaningful regulatory elements.

**4. Causal claims are not operationalized.** The abstract states the method "captures the causal relationship" and the contributions claim "articulating the causal relationship." The paper presents a structural causal model (Figure 1, Section 3.1) with directed edges between regulatory elements, sequence, and signals, yet performs no causal inference whatsoever — no interventions, do-calculus, counterfactual reasoning, causal graph testing, or any attempt to distinguish causal from predictive associations. The causal model only motivates a conditional independence assumption (Assumption 1) that justifies a posterior factorization — a factorization that could hold or fail regardless of the causal graph. Calling the learned mask "causal" or "non-causal" is unsupported and misrepresents the nature of the contribution. (The technical contribution — a Beta-distributed mask with information bottleneck — is respectable without this framing.)

### Minor

**5. Single test chromosome with no variance estimates.** The cross-chromosome validation uses only chromosome X for testing (a single split, no cross-validation). Chromosome X has well-known biological peculiarities (X-inactivation, different gene density). No error bars, confidence intervals, or seed replicates are reported, making it impossible to assess whether the improvements are robust.

**6. GraphReg is discussed but not compared.** GraphReg is described in related work (Section 2.2) yet is not included as a baseline in Table 1. Since GraphReg also uses Hi-C/HiChIP interaction frequencies for gene expression prediction, its omission weakens the baseline coverage.

**7. Inconsistency in the causal graph description.** The SCM includes the arrow \(X_{\text{seq}} \leftarrow R_{\text{g}}\), which in causal graph notation means \(R_{\text{g}}\) causes the DNA sequence. The text explains this as "The DNA sequence consists of \(R_{\text{g}}\) and other non-causal parts," which describes composition, not causation. This mismatch between graphical notation and textual explanation suggests the causal graph is not biologically literal.

**8. Key hyperparameters unreported.** The paper does not report actual values or sensitivity analysis for several introduced hyperparameters: \(\beta\) (IB trade-off), \(\alpha_3/\beta_3\) (prior sparsity for the mask), \(C_\beta\) (signal threshold), and \(C_m\) (hard mask threshold). Training time and model size are also not reported.

### Trivial

None.

## Nice-to-Haves

- Adding biological validation of the discovered regions (overlap with ENCODE cCREs, TF binding sites, motif enrichment, or CRISPR-validated enhancers) would substantiate the "discovery" claim.
- Controlled ablations isolating the mask mechanism, signal branch, KL regularization, and model capacity would resolve the main ambiguities.
- Including GraphReg as a baseline and reporting variance across multiple chromosome hold-outs or random seeds would strengthen the evaluation.

## Removed Points

- The criticism about "EPInformer characterization being somewhat unfair" is removed: it is a subjective judgment about related work framing, not a verifiable weakness of the paper itself.
- The detailed discussion about why Beta vs. logistic-normal distributions: removed as a minor comparison point that does not affect the paper's central claims; the paper gives reasonable justifications for Beta.
- The point about the variational bound in Equation 2 applying to continuous Z vs. the mask formulation: removed because the paper correctly cites Paranjape et al. (2020) for this transition, which is a standard adaptation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Conduct controlled ablations: (a) train the predictor without the generator using full unmasked input (same predictor architecture); (b) remove KL regularization to assess its effect; (c) use a fixed random mask to verify the mask learns signal-dependent structure; (d) use only the sequence branch or only the signal branch. This would isolate which components drive the improvement.
2. Address the capacity confound: either match parameter counts across baselines or build a stronger single-model baseline that integrates signals effectively (the current "Caduceus w/ signals" underperforms, suggesting poor integration rather than a ceiling on single-model performance).
3. Add biological validation of discovered regions — e.g., overlap with ENCODE cCREs, FANTOM5 enhancers, or enrichment for transcription factor binding motifs.
4. Replace causal language with predictive language throughout. The technical contribution — learning a Beta-distributed mask via information bottleneck that fuses sequence and epigenomic evidence — is sound without the causal framing.
5. Report error bars across multiple random seeds or chromosome hold-outs, and include GraphReg in the baseline comparison.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>