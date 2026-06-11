## Final Review

---

## Summary
This paper proposes CorreGen, a generative framework that reformulates multi-view clustering under noisy correspondence as maximum likelihood estimation over latent cross-view correspondences, solved via an EM algorithm. The E-step uses GMM-guided marginals within an optimal transport formulation (with virtual samples for unalignable data) to infer soft many-to-many correspondences capturing class-level structure while suppressing noise. The M-step maximizes expected log-likelihood using these inferred correspondences. Proposition 2 shows InfoNCE is a special case of the proposed objective. Experiments on four datasets with various noise regimes show consistent improvements over seven baselines.

## Strengths
- **Generative formulation with InfoNCE as a proven special case (Proposition 2):** The paper reformulates multi-view clustering under NC as maximum likelihood estimation, and Proposition 2 rigorously proves that when the posterior degenerates to one-hot paired assignments with uniform marginals, the M-step objective collapses to standard InfoNCE (Eq. 19). This establishes CorreGen as a strict generalization of contrastive MVC, providing a principled theoretical foundation for the approach. (Sec. 3.2.2)
- **Principled E-step with GMM-guided marginals and virtual sample mechanism:** The GMM-guided marginal estimation (Eq. 13–14) encodes class structure into the OT transport polytope by assigning higher alignment mass to samples in large, coherent clusters while starving outliers. The virtual sample mechanism (Eq. 12, Proposition 1) extends OT to gracefully absorb unalignable samples via a dustbin row/column — a failure mode prior reweighting/realignment methods cannot address. This joint design directly operationalizes the paper's taxonomy of NC types. (Sec. 3.2.1)
- **Strong, consistent empirical results across noise regimes:** On UMPC-Food101 — the only dataset with genuinely noisy web-collected pairs — CorreGen achieves 49.77% ACC at MR=0%, a 13.6 pp improvement over its base model DIVIDE (36.20%). Gains persist across all four datasets, three metrics (ACC/NMI/ARI), and all noise configurations in Tables 1–2. At the hardest setting (MR=0.5, CR=0.5) on UMPC-Food101, CorreGen attains 37.26% ACC vs. 24.70% for the next-best baseline — a 12.6 pp margin.
- **Clear formalization of two NC types (Definitions 1–2):** The paper precisely distinguishes category-level mismatch (same-class pairs treated as negatives) from sample-level mismatch (misaligned or unalignable pairs), with the latter further split into alignable and unalignable sub-cases. These definitions directly motivate the two key design choices. Prior NC literature in MVC lacked this clarity.
- **Qualitative validation of posterior recovery (Fig. 3):** Heatmaps on Caltech101 show the estimated posterior evolving from a sparse diagonal (epoch 10) to a block-diagonal structure matching ground-truth class partitions (epoch 200), visually demonstrating that CorreGen uncovers latent category-level correspondences through the EM process.

## Weaknesses

### Fatal
None.

### Major
- **Category-level mismatch — one of the paper's two central contributions — receives almost no quantitative evaluation.** The paper motivates itself by distinguishing category-level from sample-level mismatch (Definitions 1–2), and the GMM-guided marginals are explicitly designed to address category-level mismatch. Yet the experimental evaluation in Tables 1–2 tests only sample-level mismatch (via MR and CR). The paper acknowledges this limitation directly: "category-level mismatch is an intrinsic challenge rather than one that can be explicitly specified" (Sec. 4.2). The sole evidence for the category-level claim is a qualitative posterior visualization on a single dataset (Fig. 3) and the indirect signal from overall clustering improvements. Without an isolation experiment — e.g., comparing CorreGen against a variant that only handles sample-level noise, or constructing a controlled setting where category-level mismatch is synthetically introduced (e.g., by merging fine-grained classes) — the reader cannot determine whether the GMM-guided marginals actually mitigate category-level mismatch as claimed, or whether the gains arise entirely from better sample-level noise handling.

### Minor
- **CorreGen implemented only on DIVIDE, leaving some ambiguity about source of gains.** The paper states CorreGen is "implemented on top of DIVIDE as the base model" (line 222). While improvements over non-DIVIDE baselines (CANDY, ROLL, etc.) are substantial, the CorreGen vs. DIVIDE comparison is effectively an ablation rather than an independent method comparison. The gains over other baselines are large enough that this is unlikely to be a fatal confound, but implementing on one additional base model would strengthen confidence.
- **No standard deviations reported despite five-run averages.** Several comparisons have margins under 1 pp (e.g., LandUse21 at 0% MR: CorreGen 32.87 vs. DIVIDE 32.50 ACC). Without variance, the reader cannot distinguish genuine improvements from noise, especially on smaller datasets like Scene15 and LandUse21.
- **ρ hyperparameter setting not discussed in main text.** The virtual sample noise ratio ρ is described as "the potential noise ratio" (line 156) but how it is set (fixed across datasets? tuned per dataset? tuned per noise level?) is not addressed. This matters because if ρ is tuned per noise setting, the method has oracle knowledge that competing methods do not. The paper defers sensitivity analysis to Appendix E (Q4).
- **Eq. (3) has imprecise indexing notation.** The summation `\sum_{v_1}^V \sum_{v_i}^N \sum_{v_2}^V` mixes view indices and sample indices; the inner summation appears intended as `\sum_{i=1}^N` rather than `\sum_{v_i}`.
- **Multi-view generalization is hand-wavy.** The derivation is presented for two views, with only the brief statement that it "naturally generalizes to multiple views" (line 128). Whether the OT formulation extends via multi-marginal OT or pairwise aggregation is left unspecified.
- **Anomalous baseline results not discussed.** ROLL achieves only 17.83 ACC on Caltech101 at 0% MR (vs. 68.52 for CorreGen), and SURE achieves 29.32 NMI on the same setting. These extreme values raise questions about baseline configuration but go unremarked in the text.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment isolating category-level mismatch (e.g., merging fine-grained classes to create known category-level noise, or ablating the GMM marginals while keeping the OT+virtual sample mechanism) would directly test this central claim.
- Implementation on a second base model (not just DIVIDE) would demonstrate independence from architectural choices.
- Brief discussion of computational cost of the Sinkhorn-based OT solve in the E-step, given the O(N²) per-iteration complexity.
- Clarify whether the GMM uses C = number of true classes (which would be oracle information) or an estimated/adaptive number of components.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Multi-view data construction for Scene15/Caltech101/LandUse21 not specified in main text.** Deferred to Appendix C. The parser stripped the appendix; details exist in the original submission. REMOVED per hard rule on missing appendix.
- **Corruption Ratio (CR) undefined in main text.** Deferred to Appendix C. REMOVED per hard rule on missing appendix.
- **Proof of Proposition 2 (how the double normalization collapses to InfoNCE) not in main text.** Deferred to Appendix B. REMOVED per hard rule on missing appendix.
- **Ablation study (Q5), hyperparameter sensitivity (Q4), and additional mismatch results (Q3) deferred to appendices.** The parser stripped appendices D, E, F; these exist in the original submission. REMOVED per hard rule on missing appendix.
- **"10% accuracy improvements" claim in abstract is ambiguous.** The actual improvement is ~13.6 pp (a ~37% relative gain), so "10%" understates rather than overstates. REMOVED as factually incorrect criticism — the claim is actually conservative.
- **Introduction "overstates novelty" of category-level mismatch identification.** This is a subjective judgment about prior work placement, not a verifiable error in the paper. REMOVED as unsupported by concrete evidence from the paper.
- **GMM covariance fitting stability concern raised by harsh critic.** The paper provides fixed parameters (ε=0.1, m=10) and mentions momentum updates for stabilization; the concern is speculative without evidence of instability in the reported results. REMOVED as speculative.
- **Warmup strategy not explained.** Mentioned in Fig. 3 caption; this is a minor implementation detail and the topic is sufficiently common that a one-sentence mention suffices. REMOVED as too minor to list separately.

## Novel Insights
The paper's key insight — that the standard InfoNCE contrastive objective in MVC is a degenerate special case of a more general generative EM framework — provides a principled unification that naturally explains why contrastive MVC suffers from category-level mismatch (the posterior is forced to one-hot paired assignments, blocking same-class cross-instance positives) and why a soft many-to-many transport plan can recover class-level structure. This connection between EM, optimal transport, and contrastive learning in the MVC setting is novel and may inspire similar reformulations in related domains. The virtual sample mechanism for handling unalignable data within the OT framework is also a clean technical contribution with potential applications beyond MVC.

## Suggestions
- Add at least one experiment that directly evaluates category-level mismatch handling — e.g., construct a setting where class labels are partially merged across views, or ablate the GMM marginals while keeping the OT+virtual sample components, to isolate whether the GMM specifically helps with category-level structure recovery.
- Report standard deviations alongside means in Tables 1–2 to allow significance assessment, especially for small-margin comparisons on Scene15 and LandUse21.
- Add a one-sentence statement in Sec. 4.1 indicating how ρ is set (e.g., "ρ is fixed at 0.1 across all experiments" or "ρ is tuned via grid search on a held-out validation set").
- Consider implementing CorreGen on at least one additional base model (e.g., CANDY) to demonstrate that gains are attributable to the CorreGen objective rather than the DIVIDE backbone specifically.
- Briefly discuss why ROLL and SURE perform anomalously poorly on Caltech101, as these outliers stand out in Table 1 and may indicate configuration issues.

---

## Calibration Summary

**Round 1 bracket:** 6.0–7.0, based on comparison against P2OT (6.00) and Contrast with Aggregation MVRL (6.00) below, and COPER (7.25) and Norton (8.00) above.

**Round 2 narrowing:** Anchors at 6.67 (Discriminative Probabilistic Modeling for SSL, similar InfoNCE-as-special-case framing) and 6.75 (Projection Head as IB, comparable theory+empirical contrastive learning paper). CorreGen sits slightly below both due to the unevaluated category-level mismatch claim, but above P2OT (6.00) due to stronger theoretical framing and broader empirical results.

**Anchor papers used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| P2OT: Progressive Partial OT | hD3sGVqPsr | 6.00 | R1 | CorreGen has stronger theory and broader evaluation |
| Contrast with Aggregation MVRL | fPYJVMBuEc | 6.00 | R1 | Similar scope; CorreGen has stronger theory and results |
| Optimal Multiple Transport | 3P87ptzvTm | 5.00 | R1 | OT-focused; CorreGen more application-driven |
| Deep Incomplete MVRL | s4MwstmB8o | 6.25 | R1 | Different problem setting; comparable quality |
| Discriminative Probabilistic Modeling | s15HrqCqbr | 6.67 | R2 | Similar InfoNCE-as-special-case; DPM deeper theory, CorreGen broader empirical |
| Projection Head as IB | L0evcuybH5 | 6.75 | R2 | Comparable theory+empirical paper; CorreGen's evaluation gap more significant |
| COPER | 5ZEbpBYGwH | 7.25 | R1 | More polished MVC with complete evaluation; CorreGen clearly below |
| Norton (Multi-granularity Corr.) | 9Cu8MRmhq2 | 8.00 | R1 | Strong accept; CorreGen significantly below |

**Final score: 6.5**, reflecting a paper with genuine novelty, strong theoretical grounding, and consistent empirical gains, held back by the central category-level mismatch claim lacking direct quantitative evaluation — a significant but addressable gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>