Now I have enough data to finalize. Let me compile the final review.

**Calibration anchors summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Uj0h13lVrR | 1.00 | R1 | GFlowNet paper, fundamentally flawed — CausalNovo is far stronger |
| u1cQYxRI1H | 0.50 | R1 | Misclassified (score 10 avg 0.5) — ignore |
| 5lUdTogEL3 | 1.00 | R1 | Re-identification paper, rejected — CausalNovo far stronger |
| AvXrppAS2o | 3.00 | R1 | Causal structure learning for outcome prediction, rejected — CausalNovo more complete |
| 0iAZYF9hrl | 2.50 | R1 | Disentangled microscopy, rejected — CausalNovo stronger |
| fmAzKz9DJs | 3.00 | R1 | Feature learning, rejected — CausalNovo stronger |
| 0sO2euxhUQ | 4.00 | R1 | Learning latent SCMs, rejected — CausalNovo more practical |
| q07DDpu8Xb | 5.25 | R1 | Causal rep learning identifiability, rejected — CausalNovo stronger |
| qsAckNdySL | 4.25 | R1 | Causality as invariance, rejected — CausalNovo stronger |
| pOoKI3ouv1 | 5.75 | R1 | Robust agents learn causal models, Accept — theoretical, high variance (1,8,6,8) |
| Q0s6kgrUMr | 6.67 | R1 | Causal/anticausal discovery, Accept — nice method, some gaps |
| qac43AwuL9 | 6.00 | R1 | Causal Info Bottleneck, rejected — theoretical, less complete |
| 3cuJwmPxXj | 8.00 | R1 | Intervention extrapolation, Accept — strong theory, no major weakness |
| xByvdb3DCm | 8.00 | R1 | Causal discovery with selection, Accept — strong theory |
| hrqNOxpItr | 8.00 | R1 | Cross-entropy inversion, Accept — strong theory |
| uQnvYP7yX9 | 6.50 | R2 | ReNovo, Accept — same domain, clean method |
| 87B3zDRMjv | 5.50 | R2 | RankNovo, Reject — same domain, solid but rejected |
| 78tc3EiUrN | 6.00 | R2 | MADGEN, Accept — mass-spec domain |
| jqmptcSNVG | 6.20 | R2 | PepHAR, Accept — peptide design |
| HBf6HFnpmH | 5.50 | R2 | Causal model scalability, Reject |
| hjROBHstZ3 | 5.80 | R2 | Causal rep learning from multimodal biological, Accept |
| kz5igjl04W | 5.50 | R2 | Causal disentanglement for sperm whales, Reject |
| 6xrDPHhwD3 | 6.00 | R2 | Causal framework for pathology, Accept |

**Round 1 bracket:** CausalNovo sits between 6.0 and 7.5. Compared to ReNovo (6.5, same domain, accepted), CausalNovo has a more principled framing, larger improvements, and more comprehensive analysis, but the missing ablation is a real gap. Compared to the 8.0 anchors (strong theoretical contributions with no major weaknesses), CausalNovo's contribution is more applied and has the identifiable ablation gap.

**Final score: 7.0** — Consistently above domain papers scoring 5.5-6.5, but below 8.0+ papers that have no major identified gaps. The missing complexity-matched ablation prevents a higher score, but the strong empirical evidence and consistent results across baselines, datasets, and metrics support a solid accept.

---

## Summary
CausalNovo introduces a model-agnostic framework that injects causal reasoning into existing de novo peptide sequencing models by learning to disentangle causal (signal fragment ion) from non-causal (noise) mass spectrum representations via a structural causal model, enforced through noise peak replacement interventions and information-theoretic training objectives (independence, sufficiency, purification). Applied to three baselines (CasaNovo, AdaNovo, π-HelixNovo) on three benchmark datasets, it delivers consistent improvements, with particularly strong gains on the challenging HC-PT dataset (up to +14.2% amino acid precision).

## Strengths
- **Concrete empirical motivation via perturbation experiments**: Figure 1 systematically replaces noise peaks at varying m/z tolerance thresholds for three models, directly demonstrating that current models rely on spurious correlations with non-causal ions. This grounds the causal framing in measurable evidence rather than conceptual hand-waving.
- **Consistent improvements across multiple baselines, datasets, and metrics (Tables 1–3)**: CausalNovo improves all three structurally different baselines across amino acid, peptide, and PTM-level metrics on all three benchmark datasets. On HC-PT, improvements reach +14.2% (AdaNovo), +12.4% (π-HelixNovo), and +11.0% (CasaNovo) in amino acid precision. Cross-species validation (Table 3) shows consistent gains across all 8 species.
- **Comprehensive robustness analysis beyond standard accuracy (Figures 1, 3, 4; Tables 6, 7)**: Vulnerability analysis shows CausalNovo achieves +14.9% average relative improvement on HC-PT under peak perturbation. NSR analysis shows consistent +10–12% improvements across noise ratios. Attention analysis (Table 7) shows full causal peak attention increases from 19.26% to 32.87% of predictions.
- **Systematic ablation studies (Tables 4, 5)**: Incremental ablation of independence (+1.2%), purification (+0.8%), and symmetric (+0.4%) shows monotonic cumulative improvements. Intervention ablation confirms replace+enhance is effective while random drop provides no benefit, isolating the contribution of the specific design choices.
- **Principled theoretical framework**: The SCM formulation (Eq. 2) and derived information-theoretic objectives (Eqs. 5–6) provide principled grounding rather than ad-hoc design. The paper transparently acknowledges limitations including the ~2.3× training overhead and the NovoBench evaluation protocol constraint.

## Weaknesses

### Fatal
None.

### Major
- **Missing complexity-matched control ablation**: The CEM adds 3 Transformer layers plus an MLP head to the baseline's 9-layer encoder and 9-layer decoder (~17% more Transformer parameters), along with three additional training objectives. Table 4's ablation goes "Baseline → Baseline + Independence," which conflates adding the CEM architecture with adding the causal training objective. Without a control that adds the same CEM architecture trained with only the standard cross-entropy loss, the reader cannot fully disentangle whether improvements come from the causal reasoning framework per se or from additional model capacity and multi-task regularization. The paper's core claim is specifically about the value of causal reasoning, making this the single most impactful missing experiment.

### Minor
- **C ⊥ S assumption is foundational but under-discussed**: The SCM (Eq. 2) assumes causal factors C and non-causal factors S are independent, which is the theoretical bedrock of the framework. In mass spectrometry, plausible dependencies exist—charge state, m/z range, sample complexity, and matrix effects could create statistical dependencies between signal and noise peaks. The paper notes "noise variables are omitted for simplicity" (line 73), which is standard for causal modeling abstractions, but acknowledging conditions under which this assumption might hold or fail would strengthen the theoretical contribution.
- **Retrained baseline numbers differ substantially from NovoBench-reported numbers**: CasaNovo amino acid precision on Nine-species jumps from 0.697 (reported) to 0.741 (retrained, +4.4%), while AdaNovo drops from 0.698 to 0.681 (−1.7%). The authors correctly compare CausalNovo against their own retrained baselines (the controlled comparison), but the magnitude and inconsistent direction of these discrepancies warrant brief explanation, as they affect reader trust in the evaluation protocol.

### Trivial
None.

## Nice-to-Haves
- Concrete runtime comparison: the paper claims "<1% inference overhead" but the CEM requires a forward pass through 3 additional Transformer layers. Even a brief timing table would strengthen this claim.
- Visualizing or probing the CEM's importance scores M would provide direct evidence that causal disentanglement operates as claimed (e.g., do high-scoring peaks correspond to known signal ions?).
- Stronger theoretical or empirical justification for the purification objective (maximizing I(z_s; Y) to indirectly purify z_c). The +0.8% improvement is real but small; probing information leakage rates without purification would clarify its contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about the "enhance" step (adding all theoretical spectrum peaks to the intervened spectrum) artificially strengthening causal signal is addressed by the paper's design: the replacement + enhancement pair creates natural contrastive views that differ only in noise peaks, which is the intended mechanism for the independence objective (Eq. 5).
- The harsh critic's concern about substituting Y for C as conditioning variable is acknowledged in the paper (line 181: "C is unobserved, but Y can serve as a proxy for C") and follows standard practice in causal representation learning (citing Chen et al., 2022).
- The harsh critic's concern about the purification objective being circular is overstated; the paper provides a clear mechanism—maximizing I(z_s; Y) removes label-relevant information from z_s, forcing z_c to capture more of the information needed for prediction, thereby reducing non-causal leakage.

## Novel Insights
The paper's most notable empirical insight beyond its own framing is the systematic demonstration that vulnerability to noise peak perturbation (Figures 1, 3) is a reliable proxy for model quality—models more robust to noise perturbation also perform better on clean data, and CausalNovo's improvements scale with dataset noisiness (HC-PT > Seven-species > Nine-species). This pattern, visible across all three baselines, suggests the "spurious correlation" framing has practical diagnostic value for identifying and addressing model weaknesses in proteomics.

## Suggestions
- Add a single complexity-matched ablation: the CEM architecture trained with only standard cross-entropy loss (no independence, purification, or symmetric objectives). This would definitively validate or challenge the causal framework's contribution beyond capacity effects.
- Add a brief paragraph discussing when C ⊥ S might fail and what the empirical consequences would be.
- Briefly explain the discrepancies between retrained and NovoBench-reported baseline numbers.

## Reporting

Anchors retrieved across all rounds:
- R1: Uj0h13lVrR (1.00), 5lUdTogEL3 (1.00), AvXrppAS2o (3.00), 0iAZYF9hrl (2.50), fmAzKz9DJs (3.00), 0sO2euxhUQ (4.00), q07DDpu8Xb (5.25), qsAckNdySL (4.25), pOoKI3ouv1 (5.75), Q0s6kgrUMr (6.67), qac43AwuL9 (6.00), 3cuJwmPxXj (8.00), xByvdb3DCm (8.00), hrqNOxpItr (8.00)
- R2: uQnvYP7yX9 (6.50), 87B3zDRMjv (5.50), 78tc3EiUrN (6.00), jqmptcSNVG (6.20), HBf6HFnpmH (5.50), hjROBHstZ3 (5.80), kz5igjl04W (5.50), 6xrDPHhwD3 (6.00)

Round-1 bracket: 6.0–7.5. CausalNovo consistently outperforms the 5.5–6.5 domain papers (ReNovo, RankNovo, MADGEN, MFC) in terms of empirical evidence breadth, but falls below 8.0 anchors which have no major identified gaps. The missing complexity-matched ablation is the differentiating weakness vs. the 8.0 papers. Final score: 7.0.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>