## Summary

This paper attempts to present both a mathematical framework for unsupervised domain adaptation in drug-target interaction (DTI) prediction (built on optimal transport, information geometry, and spectral operator analysis) and an empirical deep learning architecture ("MoleProLink") evaluated on standard DTI benchmarks. These two components are presented as a single contribution, but they are completely decoupled: the theory is never used by the model or tested in the experiments, and the experiments evaluate an architecture unrelated to any of the theoretical constructs.

## Strengths

- **The ablation study provides concrete, per-component performance numbers.** Section 3.5 reports specific AUC/AUPR drops when removing the Mamba module (0.07%–3.52% AUC, 0.28%–5.03% AUPR) and KAN module across three datasets, giving measurable evidence that both components contribute to the reported results.

- **Competitive absolute numbers on established benchmarks.** The paper reports AUC of 96.16% (Human), 97.48% (C. elegans), and 89.21% (Davis), along with stated margins over the second-best model (0.28% on Human, 7.16% on Davis). These numbers, if validated, indicate practical utility.

## Weaknesses

### Fatal

**1. The theoretical framework (Section 3) and the empirical method (Sections 2.2, 3.1–3.5) are completely disconnected.**  
The paper claims a unified mathematical framework as its core contribution, but none of the theoretical constructs — DTI-Wasserstein distance, Fisher-Rao metric, geodesic equations, DTI-transport parallel, DTI-spectral decomposition, DTI-mutual information, or the variational formulation — appear anywhere in the model description, implementation, or experimental evaluation. The "MoleProLink" model is a standard deep learning pipeline (Graph Transformer + Mamba + KAN decoder) trained with a classification loss. The experiments test architectural components (Mamba, KAN) that have no connection to the theory. This means the paper makes no attempt to validate its central claimed contribution.  
*Evidence:* Line 287 introduces spectral analysis, then line 291 immediately jumps to "3.1 EXPERIMENT" with no spectral analysis performed. Lines 38–290 present extensive theory; lines 291–318 describe experiments on an unrelated architecture.

**2. The spectral analysis is promised but never delivered.**  
The abstract claims "We develop a spectral decomposition of the DTI-DA transfer operator, providing insights into the modes of information transfer between domains. This leads to the introduction of DTI-spectral embedding and DTI-spectral mutual information." The introduction (line 16) repeats this claim. Section 3 reaches line 287 with "To further elucidate the structure of the domain adaptation process in DTI prediction, we introduce a spectral analysis of the associated transfer operators:" — and then the paper moves directly to experiments at line 291. The promised spectral decomposition, spectral embedding, and spectral mutual information are entirely absent from the manuscript. A contribution listed as a headline result in the abstract is never presented.

### Major

**3. The experiments are critically underspecified.**  
- *No baseline models are named anywhere in the paper.* Lines 307–308 refer to "other baseline models" and "the second-best baseline model" without identifying a single one. The reader cannot assess whether comparisons are against strong contemporary methods or weak baselines. Even if Table 2 (stripped by the parser) contained names, the text's failure to identify baselines makes the results uninterpretable.  
- *No variance or confidence intervals are reported.* The claimed AUC improvements include a 0.28% margin on Human and 7.16% on Davis, but without standard deviations these could be noise.  
- *Dataset descriptions are inconsistent.* Section 2.1 lists four datasets (Human, C. elegans, Davis, GPCR). Section 3.2 says "We selected two datasets (Human and DrugBANK)" — introducing DrugBANK for the first time, contradicting Section 2.1. The results text (lines 307–308) then discusses three datasets (Human, C. elegans, Davis), none of which is DrugBANK. The GPCR dataset from Section 2.1 is never used.  
- *Architecture descriptions contradict each other.* Section 2.2 (line 31) states the protein encoder uses "a standard Transformer architecture." Section 3.3 (line 300) says "constructed the protein encoding module with mamba-ssm 1.0.1." The KAN decoder module, central to the ablation in Section 3.5, is never introduced in the architecture description (Section 2.2). These are not different views of the same model.

**4. The ablation study evaluates the wrong thing relative to the paper's claims.**  
The paper's headline contribution is the unified mathematical framework for domain adaptation. The ablation experiments remove architectural components (Mamba, KAN) that are standard neural modules with no connection to Wasserstein distances, Fisher-Rao metrics, geodesics, or spectral operators. Even if the ablations are informative about the architecture's design, they provide zero evidence for or against the theoretical framework that the paper claims as its contribution.

**5. The proposed model is barely named or defined.**  
The name "MoleProLink" appears only once in a figure caption (line 34). The model is never explicitly named or introduced in the main text. The architecture described in Section 2.2 (Graph Transformer + standard Transformer + multi-head attention + linear layer) differs substantially from the architecture actually evaluated (Mamba + KAN). It is unclear which architecture "MoleProLink" actually refers to.

### Minor

- Section 3's theoretical development attaches a "DTI-" prefix to standard mathematical concepts (Wasserstein distance, Fisher-Rao metric, mutual information) without operationalizing them for the DTI problem. The metric \(d_{\mathrm{DTI}}\) in the DTI-Wasserstein distance is never specified; the measure \(\mu_{\mathrm{DTI}}\) in DTI-mutual information is never defined. The proofs (e.g., Theorem 3.1, Theorem 3.5) are sketch-level outlines containing generic arguments that do not establish DTI-specific results.

- The domain adaptation setup is unclearly described and may not constitute unsupervised domain adaptation as standardly understood. Section 3.2 splits data randomly into source/target at a 6:4 ratio, which does not create a distribution shift — it is simply a train/test split. How the unlabeled target training data (if it is from a different distribution) is used is never explained.

### Trivial

- "DrugBANK" in Section 3.2 appears to be a formatting/parsing variant of DrugBank, but this creates genuine confusion about which datasets were used.
- "DTI-DA" and "DTIDA" are used inconsistently (e.g., line 16).
- The paper would benefit from proofreading for missing spaces (e.g., "researchFrance", "techniquesSinghal", "matricesSe´journe´", "vectorsHosseini-Nodeh").

## Nice-to-Haves

- If the authors wish to pursue the theoretical direction, the framework should be connected to an actual algorithm: specify \(d_{\mathrm{DTI}}\) and \(\mu_{\mathrm{DTI}}\) concretely, derive a training procedure from the geodesic or variational formulation, and test that procedure against standard domain adaptation baselines in a controlled experiment.
- If the authors wish to pursue the empirical direction (MoleProLink), the theory sections should be removed or drastically scaled back, and the architecture description should be reconciled with what is actually implemented and evaluated.

## Removed Points

*These points were flagged by reviewers but removed per the filtering guidelines. Treat with caution.*

- *"The paper's abstract claims the framework is the contribution yet the evaluation demonstrates only architecture performance"* — This is subsumed by Weakness #1 (theory-experiment disconnect). Removed as duplicate.
- *"No standard deviations or confidence intervals"* — Kept in Major #3 as it is a concrete claim about experimental underspecification.
- *"Section 2.2 is too brief to support reproducibility"* — This is a generic reproducibility nitpick that could apply to many papers. The architecture is described at a reasonable level for a conference paper; the real problem is the contradiction between Section 2.2 and the implementation (Major #3), not brevity. Removed as noise.
- *"Missing related works"* — Removed per hard rule: I cannot verify the existence of missing citations.
- *"Missing appendix content"* — Removed per hard rule: the parser strips appendices from all papers.
- *"Formatting/style nitpicks"* — Removed per hard rule.
- *Strength: "Clear architectural description with named components"* — Removed because it conflicts with verified weaknesses (contradiction between Section 2.2 and implementation, undefined KAN module). The weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the structural disconnect between theory and experiment as the central problem, but this is a flaw in the paper's argumentation, not a novel insight about DTI prediction.

## Suggestions

1. **Choose one contribution and execute it fully.** Either (a) present the theoretical framework with a concrete algorithm derived from it and validate that algorithm, or (b) present the empirical architecture with proper baselines, variance reporting, and a coherent model description — and remove the disconnected mathematical sections. The current paper attempts both and succeeds at neither.
2. **Name and cite every baseline model** used for comparison, and report results with standard deviations over multiple runs.
3. **Reconcile the dataset descriptions.** Clarify which datasets (and how many) were used. The discrepancy between Section 2.1 (4 datasets), Section 3.2 (2 datasets including DrugBANK), and the results text (3 datasets: Human, C. elegans, Davis) must be resolved.
4. **Reconcile the architecture.** Section 2.2 describes a standard Transformer protein encoder; the implementation uses Mamba. The KAN decoder appears only in the ablation but is never introduced. The model description must match what is actually evaluated.
5. **Either deliver the promised spectral analysis or remove it** from the abstract and introduction. A core claimed contribution cannot be introduced and then abandoned.

## Score and Decision

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>