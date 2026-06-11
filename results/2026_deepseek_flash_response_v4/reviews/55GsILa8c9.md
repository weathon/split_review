## Summary

CausalNovo proposes a model-agnostic framework for de novo peptide sequencing that uses a Causality Extraction Module (CEM) to learn peak-level importance scores, guided by independence and sufficiency principles derived from a Structural Causal Model. The method intervenes on noise peaks during training via replacement-based perturbation and contrastive learning to focus on causal signal ions (b/y/a fragments). Experiments across three benchmarks and three SOTA baselines show consistent gains at amino acid, peptide, and PTM levels.

## Strengths

1. **Model-agnostic framework delivering consistent gains across all three SOTA baselines, three datasets, and all evaluation levels.** No existing work in de novo sequencing demonstrates this degree of architecture-agnostic improvement. Improvements are substantial: e.g., +12.0% amino acid precision for CasaNovo on Seven-species, +14.2% for AdaNovo on HC-PT (Tables 1-2). Cross-species validation (Table 3) further confirms generalization with average +2.6% peptide precision improvement across all 9 species.

2. **Attention-based mechanistic evidence that CausalNovo genuinely shifts model focus toward signal peaks.** Table 7 shows the proportion of predictions where all top-3 attended peaks are causal increases from 19.26% (baseline) to 32.87%, while predictions that completely miss causal peaks drop from 12.73% to 10.76%. Appendix Table 14 further shows correction cases where CausalNovo reduces baseline attention failures from 14.18% to 5.44%. This interpretability evidence goes beyond aggregate accuracy numbers.

3. **Rigorous noise-robustness evaluation under systematic perturbation and varying noise-signal ratios.** Table 6 demonstrates a 28.5% relative improvement under the most aggressive noise threshold (1 m/z tolerance). Figure 4 shows consistent +10.2%–12.2% average amino acid precision gains across all NSR levels. The vulnerability analysis (Figures 1, 3) systematically tests performance under controlled peak replacement — an evaluation dimension absent from prior de novo works.

4. **Systematic ablation isolating each component's contribution.** Tables 4-5 show monotonic improvements from each component (independence, purification, symmetric training, replace, enhance). The random-drop baseline fails to improve, confirming that the replace-based intervention is specifically effective rather than any perturbation being helpful.

## Weaknesses

### Major

- **No statistical significance / variance reporting across runs.** All tables (1-7) report single-point estimates. Since some improvements are modest (e.g., +0.4% from symmetric training in Table 4, +0.6% from replace in Table 5), the reader cannot assess whether these gains are within run-to-run noise. This is a standard expectation for reliable ML evaluation and should be addressed with 3-5 random seeds.

### Minor

- **Key hyperparameters (γ, α) unspecified.** The tolerance threshold γ (Eq. 4) for identifying signal peaks and the replacement fraction α are not stated. The paper does not report what values were used or whether they were tuned. These are important for reproducibility.
- **Confusing motivation for the purification objective.** Section 3.3 states that maximizing I(z_s; Y) "can indirectly lead to the purification of z_c" without clearly explaining the mechanism. If z_s can predict Y, this could reduce the incentive to keep predictive information in z_c, which seems to contradict the stated goal. The logic requires better formalization or the framing should be adjusted.
- **SCM independence assumption (C ⟂ S) asserted but not empirically tested.** The SCM (Eq. 2) assumes signal and noise are independent, but no evidence is provided that this holds in the learned latent space — it is a structural assumption of the model rather than a verified property.
- **Evaluation follows the in-distribution NovoBench protocol, not the more realistic cross-dataset protocol.** The paper honestly acknowledges this as a limitation and future work, but claims about real-world robustness are only supported by in-distribution evaluation.

### Trivial

None.

## Nice-to-Haves

- Report the γ and α hyperparameter values (and optionally analyze sensitivity to them).
- Clarify the purification loss mechanism: explain how maximizing I(z_s; Y) prevents leakage rather than encouraging it, or reframe the objective.
- Discuss the possibility that replacement noise peaks sampled from other spectra could accidentally match signal peaks in the target spectrum.
- The "up to 10%" claim in the abstract is actually conservative (some improvements exceed 10%); consider updating it.

## Removed Points

- **"Causal assignment is pre-determined by domain heuristics, not discovered from data"** — The paper is transparent about using theoretical spectra derived from ground-truth labels (Eq. 4, lines 105-110) and cites prior work using the same approach. This is standard domain practice, not a flaw.
- **"Training depends on ground-truth labels (privileged information)"** — Transparently described and standard in the field. The CEM operates label-free at inference. The paper never claims label-free training.
- **"Abstract's 'up to 10%' conflates absolute/relative percentages"** — The actual improvements in Table 1 reach +12.0-14.2%, exceeding 10%. The abstract is conservative. The criticism is factually backward.
- **"Replacement could introduce accidental signal matches"** — Speculative concern with no evidence in the paper. Moved to Nice-to-Haves.
- **"SCM apparatus is inflated rhetoric"** — A framing preference, not a methodological flaw. The SCM provides a coherent organizational structure; the paper is transparent about implementation.

## Novel Insights

The attention analysis (Table 7) reveals that CausalNovo more than doubles the proportion of predictions where all top-3 attended peaks are causal (19.26% → 32.87%). This is a surprisingly large behavioral shift from a training-only modification, suggesting that contrastive learning with noise-replacement perturbation provides an unusually effective inductive bias for peak-gating in this domain — substantially more than the raw accuracy numbers alone would suggest. The correction-case analysis (Appendix Table 14), where CausalNovo fixes baseline errors by attending to causal peaks in 94.56% of corrected cases vs. 85.82% for the baseline, further demonstrates that the method's gains are mechanistically grounded.

## Suggestions

1. Report all main results as mean ± std over 3-5 random seeds — this is the single most important improvement for credibility.
2. Specify γ and α in the paper (or Appendix).
3. Clarify the purification loss mechanism in Section 3.3.
4. Optionally reframe the "causal" language to better match what is implemented — though the paper is already reasonably transparent about its use of domain heuristics to supervise the CEM.

---

**Calibration Anchors Retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| G536mmC2HL.md (TorSeq) | 3.00 | 1 (weak) | Different domain (molecule conformers), clearly weaker |
| IZiKBis0AA.md (Antibiotic design) | 3.00 | 1 (weak) | Different domain, clearly weaker |
| ZyAwBqJ9aP.md (CypST) | 2.00 | 1 (weak) | Different domain, clearly weaker |
| B6B6EhC1bW.md (Molecular Transformers) | 2.50 | 1 (weak) | Different domain, clearly weaker |
| hjROBHstZ3.md (Causal Rep. Learning Bio) | 5.80 | 1 (middle) | Stronger theory, weaker experiments. Comparable overall. |
| cbFqqtJGtA.md (Perturbation targets) | 4.25 | 1 (middle) | Limited novelty. CausalNovo is stronger empirically. |
| kz5igjl04W.md (Causal disentanglement) | 5.50 | 1 (middle) | Different task (whale communication). Comparable score level. |
| qac43AwuL9.md (Causal IB) | 6.00 | 1 (middle) | Stronger theory, toy experiments. CausalNovo has better evaluation. |
| RvUVMjfp8i.md (SSL Evaluation) | 8.00 | 1 (strong) | Strong ML paper. CausalNovo is clearly weaker. |
| cJs4oE4m9Q.md (Anomaly Detection) | 8.00 | 1 (strong) | Strong ML paper. CausalNovo is clearly weaker. |
| 87B3zDRMjv.md (RankNovo) | 5.50 | 2 (narrow) | Directly comparable de novo paper. CausalNovo has larger improvements and better ablations — **stronger**. |
| MBIGXMT0qC.md (Multi-Scale Protein LM) | 5.00 | 2 (narrow) | Criticized for marginal improvements. CausalNovo is **stronger**. |
| bM6LUC2lec.md (MSA Generation) | 5.67 | 2 (narrow) | Different task (protein structure prediction). |
| 9GE0N1htnu.md (RINGER) | 5.75 | 2 (narrow) | Different task (macrocyclic peptide conformers). |
| jqmptcSNVG.md (PepHAR) | 6.20 | 2 (narrow) | Strong peptide design paper. CausalNovo is **somewhat weaker** in technical novelty. |
| 9nUBh4V6SA.md (Hierarchical Rep.) | 6.50 | 2 (narrow) | Different domain (self-driving labs). |
| pAoqRlTBtY.md (Causal Modelling Agents) | 6.25 | 2 (narrow) | Different task (causal discovery with LLMs). |
| x3F8oPxKV2.md (Zero-Shot Causal) | 6.25 | 2 (narrow) | Different task (causal discovery). |

**Bracket progression:** Round 1 placed CausalNovo between 3.5 and 8.0 (clearly above the 2.0-3.0 band, clearly below the 8.0 band). Round 2 narrowed to 5.0-6.5 via direct comparison with RankNovo (5.50), PepHAR (6.20), and other causal/bio papers. The paper is stronger than RankNovo and somewhat weaker than PepHAR, placing it around 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>