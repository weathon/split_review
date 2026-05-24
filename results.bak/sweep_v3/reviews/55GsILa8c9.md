Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces CausalNovo, a model-agnostic framework that incorporates causal reasoning into de novo peptide sequencing. It formulates the task via a Structural Causal Model (SCM) and derives two principles — independence and sufficiency — operationalized through a Causality Extraction Module (CEM) that disentangles causal representations from spurious noise peaks using intervention (replace-based perturbation), contrastive learning, and information-theoretic objectives. Extensive experiments across three benchmark datasets (Nine-species, Seven-species, HC-PT) and three strong baselines (CasaNovo, AdaNovo, π-HelixNovo) show consistent improvements in amino acid, peptide, and PTM-level metrics, with diagnostic analyses (vulnerability, NSR, attention) providing direct evidence of improved robustness to noise.

## Strengths

1. **Strong diagnostic evidence for causal robustness.** The vulnerability analysis (Figures 1, 3; Table 6) is the paper's most compelling contribution. When noise peaks are systematically replaced at tightening tolerance thresholds, CausalNovo-enhanced models suffer far less degradation than baselines, achieving up to 28.5% relative improvement (threshold=1, HC-PT dataset). This directly tests the core causal claim rather than relying solely on aggregate accuracy metrics.

2. **Consistent gains across diverse baselines and datasets.** Table 1 shows CausalNovo improves amino acid precision for all three baseline models on all three datasets, with gains reaching +14.2% (AdaNovo on HC-PT). The gains hold at the peptide level and PTM level (Table 2). Cross-species validation (Table 3) further confirms generalization, with average +2.6% peptide precision improvement across nine species.

3. **Rigorous ablation and component analysis.** Table 4 isolates the contribution of each proposed component (independence: +1.2% AA precision, purification: +0.8%, symmetric training: +0.4%), and Table 5 ablates the intervention design (replace vs. enhance vs. drop). Table 7 provides attention-based interpretability evidence, showing CausalNovo increases attention to three causal peaks from 19.26% to 32.87%.

4. **Model-agnostic design.** The CEM is designed as a plug-in module for existing encoders, demonstrated on three architecturally distinct baselines. The paper explicitly acknowledges limitations (2.3× training overhead, restricted evaluation protocol), which is commendable.

## Weaknesses

### Major

- **No control for increased model capacity (Evidential gap).** The CEM adds 3 Transformer layers and an MLP head to the baseline's 9-layer encoder — approximately a 30% parameter increase. The ablation in Table 4 adds the CEM *and* the independence objective simultaneously, so the +1.2% AA precision gain (0.741 → 0.753) cannot be attributed to causal disentanglement vs. simply having a more expressive model. The paper needs an equivalent-capacity control: add the same number of Transformer layers to the baseline encoder without the causal objectives. This is the single most impactful experiment the authors could run.

### Minor

- **Retrained baselines differ from published numbers, and the reason is not fully explained.** E.g., retrained CasaNovo achieves 0.741 AA precision on Nine-species vs. the original 0.697 reported by NovoBench. This is a large gap and likely reflects different data splits or preprocessing. The paper should explicitly state whether all models (baselines and CausalNovo variants) used identical splits and preprocessing, and whether retraining was needed to ensure fair comparison.

- **No statistical significance reported.** All results appear to be single runs. The improvements are sometimes modest (e.g., +0.4% from symmetric training). Reporting means and standard deviations over at least 3 random seeds would strengthen confidence.

- **Key hyperparameters not reported.** The noise-replacement fraction α is mentioned in the methodology but its value is never stated. The tolerance threshold γ used during training is similarly unspecified (only used in the vulnerability evaluation). A sensitivity analysis for these parameters would be valuable.

- **Mean-pooling in contrastive learning creates a subtle mismatch.** The contrastive objective (Eq. 5) uses mean-pooled global representations for similarity computation, while the CEM operates at the per-peak level. The paper should justify why a single global similarity suffices for a per-peak sequence prediction task.

### Trivial

- Table 4 appears to have formatting issues in the extracted version (all checkmarks in all rows) — this should be corrected for clarity.

## Nice-to-Haves

- **Noise-augmentation baseline**: Adding random noise peaks to baseline training (without the causal framework) could help isolate whether the benefit comes from the principled causal intervention or simply from seeing more varied noisy examples during training.
- **Clarify the purification objective further**: The justification for maximizing I(z_s; Y) as "indirectly purifying" z_c is weakly motivated. While the paper cites Chen et al. (2022) and the ablation shows a positive effect (+0.8%), a self-contained explanation or a simpler alternative (e.g., directly penalizing I(z_s; Y) to reduce spurious correlations) would be more principled.

## Removed Points

These points were raised by one or both reviewers but are removed from the main evaluation with justification:

- **"Purification objective is conceptually problematic / at odds with the paper's premise"** → Removed. The paper provides a reasonable justification (preventing redundancy between z_c and z_s, citing Chen et al. 2022) and the ablation shows it helps empirically. The argument is not "at odds" — it is a standard redundancy-reduction motivation, even if the framing could be tightened. This is at most a nice-to-have clarification, not a weakness. The harsh critic's claim that it "risks misleading readers" overstates the issue.
- **"Missing baselines like ContraNovo, RankNovo, RefineNovo"** → Removed. The paper explicitly acknowledges these methods in Section 5 ("recent methods adopt a more realistic protocol that trains on large-scale external corpora") and identifies the fair comparison obstacle. The paper is evaluated on the NovoBench protocol; demanding reimplementation under a different protocol is scope creep.
- **"Comparison with a simple noise-augmentation baseline would strengthen the paper"** → Moved to Nice-to-Haves. This is a useful suggestion but not a required fix for acceptance.
- **"Pure formatting/style nitpicks"** → Removed per hard rules.
- **"Missing related works"** → Removed per hard rules (lack of external verification).
- **"SearchNovo discussion should be in the main text"** → Removed. SearchNovo is discussed throughout Section 4.3, with direct comparisons.
- **"CEM parameter count not stated"** → Removed. The architecture is described in sufficient detail (3 Transformer layers + MLP head). The capacity concern is already captured under the Major weakness; no additional enumeration is needed.

## Novel Insights

The combination of the vulnerability analysis (which directly tests the causal claim by measuring robustness to noise replacement) with the attention analysis (which shows *where* the model focuses) provides converging evidence that is stronger than either analysis alone. This two-pronged diagnostic strategy — intervening on the input space (noise replacement) and inspecting the representation space (attention weights) — is a methodological template that could be adopted by other causal representation learning papers in structured prediction domains. That said, this observation is largely implicit in the paper's design rather than a novel insight of the reviews.

## Suggestions

1. **Highest priority: add an equivalent-capacity baseline.** Add 3 extra Transformer layers (matching the CEM's parameters) to the baseline encoder, train with the standard cross-entropy objective only, and report performance. If this control matches or approaches the "Baseline + Independence" row in Table 4, the causal claim is weakened. If it does not, the causal disentanglement is supported. This is the cleanest way to resolve the main concern.

2. **Report statistical significance** over at least 3 random seeds for the main tables (Tables 1, 2, 4).

3. **Report the hyperparameter values** for α (noise replacement fraction) and training-time γ (tolerance threshold), and add a sensitivity analysis to the appendix.

4. **Clarify the retraining protocol.** State explicitly whether the same data splits and preprocessing pipeline were used for all retrained baselines and CausalNovo variants, and why published numbers differ.

## Score and Decision

### Calibration Anchors

**Low-scoring anchors (avg ≤ 4):**
- *MCCE: Missingness-aware Causal Concept Explainer* (avg 3.00, Reject) — CausalNovo is vastly stronger: it has extensive empirical validation across multiple datasets, ablations, and diagnostic analyses, whereas MCCE tests on a single dataset with questionable assumptions.
- *On Sampling Information Sets to Learn from Imperfect Information* (avg 1.67, Reject) — Not comparable; fundamentally different type of work with poor scientific grounding.

**Medium-scoring anchors (3.5 < avg < 7.5):**
- *RankNovo: A Universal Reranking Approach* (avg 5.50, Reject) — CausalNovo has a stronger theoretical foundation (causal framework vs. reranking), larger performance gains, and more thorough diagnostic analysis. CausalNovo is clearly the stronger paper.
- *Distilling Non-Autoregressive Model Knowledge* (avg 4.25, Reject) — CausalNovo has better-motivated methodology, more extensive evaluation, and avoids the "engineering-heavy" criticism that reviewers leveled at CrossNovo.
- *Causal Information Bottleneck* (avg 6.00, Reject) — CausalNovo's empirical validation is substantially more thorough, but CIB is a theory paper with a different contribution type. CausalNovo's capacity confound is a more concrete weakness than CIB's limited experiments.

**High-scoring anchors (avg ≥ 6):**
- *ReNovo: Retrieval-Based De Novo Peptide Sequencing* (avg 6.50, Accept) — Similar domain and evaluation standard. ReNovo had a clean idea (RAG for proteomics) with good results and modest data-splitting concerns. CausalNovo has more theoretical grounding, more thorough diagnostics, and the model-agnostic design, but the unresolved capacity confound makes it slightly weaker than ReNovo in its current form.
- *MADGEN: Mass-Spec attends to De Novo Molecular Generation* (avg 6.00, Accept) — Comparable rigor. CausalNovo has more baselines and ablations; MADGEN had a weak predictive retrieval stage but a clean oracle-based evaluation.

**Comparison verdict:** CausalNovo is stronger than the mid-range papers (RankNovo 5.5, Distill 4.25) and comparable to the high-range papers (ReNovo 6.5, MADGEN 6.0), but the capacity confound prevents it from reaching the top of this band. It is in the 6.0–6.5 range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>