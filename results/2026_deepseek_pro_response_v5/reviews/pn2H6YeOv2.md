Now let me finalize my assessment. Let me summarize the anchor comparisons:

**Round 1 anchors:**
| Path | Score | Comparison |
|------|-------|------------|
| `gNoqEdT2wO` | 2.33 | Multimodal CIL benchmark — much weaker than PI-CCA |
| `WM5G2NWSYC` | 2.00 | Projected subnetworks — underdeveloped, much weaker |
| `G9Ea7mlqGO` | 3.80 | CLIP online CL — weaker method, limited experiments |
| `04TRw4pYSV` | 3.50 | ModalPrompt for LMMs — weaker contribution |
| `k9NYnsC4Mq` (PROOF) | 5.67 | VL CIL with projections — PI-CCA clearly stronger |
| `9aZ2ixiYGd` | 5.00 | Rehearsal-free CL — PI-CCA more comprehensive |
| `sb7qHFYwBc` (C-CLIP) | 6.50 | PI-CCA's direct baseline — PI-CCA beats it, stronger experiments |
| `TLADT8Wrhn` (TiC-CLIP) | 6.25 | Benchmark paper — PI-CCA has stronger technical contribution |
| `kIP0duasBb` | 6.67 | TTA with CLIP — different topic |

**Round 2 anchors:**
| Path | Score | Comparison |
|------|-------|------------|
| `wE1I9IGqeH` | 6.00 | Open-vocab CL — only 0.5% over ZSCL, PI-CCA much stronger |
| `b20VK2GnSs` | 7.00 | Concept drift MLLMs — stronger theory + dataset, PI-CCA slightly weaker |
| `TLADT8Wrhn` | 6.25 | Already compared above |
| `sb7qHFYwBc` | 6.50 | Already compared above |

**Bracket:** Round 1 placed PI-CCA in 5.5–7.0. Round 2 narrowed this: PI-CCA is clearly stronger than wE1I9IGqeH (6.00) and PROOF (5.67), comparable to or stronger than C-CLIP (6.50), but weaker than b20VK2GnSs (7.00) due to the Fig. 3 credibility issue. **Final score: 6.5**.

Now let me write the final review.

## Summary
PI-CCA reframes forgetting in vision-language continual learning as drift of the canonical correlation geometry that underlies cross-modal generalization, and introduces a compact, replay-free certificate that preserves top-k canonical correlations and sketched subspaces, augmented with prompt-invariant projector averaging. Across MTIL, X-TAIL, VLCL, and ConStruct-VL benchmarks, PI-CCA achieves state-of-the-art results among replay-free methods, outperforming even a synthetic-replay baseline (GIFT) without storing or generating data.

## Strengths
- **Well-differentiated conceptual framing**: The paper clearly identifies that prior VL-CL methods regularize proxy signals (similarities, logits, weights, routing) rather than directly controlling the CCA alignment geometry that underlies cross-modal generalization (lines 15-21, 29). This leads to a concrete, mathematically grounded loss design (Eqs. 8-11).
- **Strong component-wise ablation (Table 3)**: Removing the spectral preservation term drops MTIL Avg by 2.5 pp and VLCL I2T R@1 by 2.3 pp; removing the subspace-angle term drops MTIL Avg by 2.2 pp and I2T R@1 by 2.7 pp. These are the two largest single-component degradations, providing direct causal evidence that both spectral and directional invariants independently contribute to retention.
- **Beats a synthetic-replay method without data access**: On VLCL retrieval, PI-CCA achieves I2T R@1 of 48.6 vs. GIFT's 47.3, and on ConStruct-VL, FA of 75.2 vs. 73.9 with lower forgetting (AF 2.7 vs. 3.3), all without requiring a generator or stored data (Table 2).
- **Prompt-invariance stress test (Fig. 4) provides concrete robustness evidence**: At maximum perturbation strength s=1.0, the invariance term improves VLCL I2T R@1 by +2.44 pp (ID) and +2.51 pp (OOD) while reducing ConStruct-VL AF by ~1.10 and ~0.96 respectively.
- **Task-order robustness empirically demonstrated (Fig. 5)**: Narrow IQRs across 20 random MTIL sequences (Avg: 76.0-77.4%, AF: 2.6-3.0) rule out the concern that gains are an artifact of favorable ordering.
- **Pareto efficiency analysis (Fig. 2) provides actionable guidance**: Identifies a broad efficient ridge at k∈[48,96], h∈[192,320] with the knee at (64,256), confirming the "small yet sufficient" certificate hypothesis.
- **Method is task-objective agnostic and compatible with parameter-efficient tuning**: Works with any standard task loss (InfoNCE, cross-entropy, detection) and operates via LoRA adapters with frozen backbones.

## Weaknesses

### Fatal
None.

### Major
- **Fig. 3 reports implausible perfect correlations**: The figure annotates Pearson r=1.00 and Spearman ρ=1.00 for the relationship between subspace-angle drift D_ang and performance drops (ΔAvg, ΔR@1), and r=0.99/ρ=1.00 for spectral drift D_ρ. Perfect empirical correlations across multiple independent hyperparameter configurations of stochastically trained deep networks are not credible — finite-precision computation, minibatch noise, and optimization variance would produce visible deviations from r=1.00. Moreover, the figure caption (line 232) states the plots show "realistic scatter" and display a 95% confidence interval, which directly contradicts r=1.00 (a correlation of 1.00 means all points lie exactly on a line with zero scatter). The authors must clarify exactly how many independent data points Fig. 3 contains, how they were generated, and why perfect correlation is observed. If the data points are not independent (e.g., from a single training trajectory), the analysis must be reframed accordingly. While this does not invalidate the core method (Tables 1-3 provide independent evidence), it undermines the paper's mechanistic claim that alignment-geometry drift causally predicts retention.

### Minor
- **Backbone model unspecified in main text**: The paper never states which CLIP variant is used (ViT-B/32, ViT-B/16, etc.). The reproducibility statement indicates this is in Appendix A.2 (stripped), but it belongs in §4.1 given its impact on embedding dimensionality, compute costs, and baseline comparability.
- **Anchor prompt set not described**: The certificate is "constructed from a diverse anchor prompt set" (line 89), but its composition is never specified in the main text. If the anchor set overlaps with evaluation templates, the prompt-invariance evaluation risks circularity. This detail is presumably in the stripped appendix but matters for assessing the method's validity.
- **Certificate EMA ablation weakens the "controlled plasticity" framing**: Disabling the certificate EMA (α=0, keeping the certificate frozen at pre-continual values) drops MTIL Avg by only 1.2 pp (Table 3). This suggests PI-CCA's value comes primarily from anchoring to pre-trained alignment geometry rather than from adaptively incorporating new tasks — the paper's framing as "controlled plasticity" is therefore overstated. The finding itself is interesting, but the framing should be adjusted.
- **Gradient flow through whitening not fully specified**: The paper mentions using stop-gradient on the inverse square root "if needed" and that gradients propagate to M̃ but "not through the certificate" (line 131). The exact differentiation path is ambiguous, which matters for reproducibility.
- **Time-continual study referenced but not presented**: §4.1 mentions "a time-continual study on a medium-scale split of TiC-YFCC/RedCaps" but no results appear in the main text. This is either an omission or the results are in the stripped appendix, but referencing an unseen experiment is confusing.

### Trivial
None.

## Nice-to-Haves
- Add variance estimates to Table 1 for MTIL and X-TAIL results, especially given the narrow margins (0.7 pp over RAIL on X-TAIL).
- Provide a direct table comparing per-step wall-clock time and peak memory against key baselines (ZSCL, C-CLIP, Mod-X), beyond the Pareto analysis in Fig. 2.
- Include a simple L2-regularization-toward-pretrained baseline to help isolate how much of PI-CCA's benefit comes from the CCA geometry specifically vs. any form of pre-trained anchoring.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Harsh Critic: "PI-CCA is not 'simple'"* — This is a semantic nitpick about the abstract's phrasing, not a substantive weakness. The abstract's claim of "simple" is a judgment call, not a factual error.
- *Harsh Critic: Missing discussion of feature-level distillation methods (LwF-style)* — Hard rule: do not mention missing related works as weaknesses.
- *Harsh Critic: EMA recency/primacy bias concern* — This is speculative; the paper presents no evidence of such bias occurring in practice, and the task-order robustness study (Fig. 5) indirectly suggests this is not a problem.
- *Harsh Critic: Spectral moments (J>0) as "under-motivated embellishment"* — The paper already acknowledges the small gain (0.7 pp) in Table 3 and presents it as optional; this is self-documented rather than a hidden weakness.
- *Harsh Critic: Baseline re-running under identical conditions not stated* — Many papers in this area report numbers from prior publications; this is a field-standard practice, not a specific flaw. PI-CCA's consistent outperformance across 4 benchmarks with varied baselines mitigates this concern.
- *Strength Finder: Generic praise about "important problem"* — Removed as superficial.
- *Strength Finder: "Method is agnostic to task objectives" rephrased* — Consolidated into the kept strength above.

## Novel Insights
The paper's reframing of VL-CL forgetting as alignment-geometry drift is genuinely novel within this literature. Prior work has applied CCA-like diagnostics (SVCCA, PWCCA, CKA) as post-hoc analysis tools, but PI-CCA is the first to operationalize these invariants as direct optimization targets during continual training. The finding that a frozen pre-trained certificate (α=0) already performs close to the full adaptive version (only 1.2 pp gap) is an interesting result that the paper under-interprets — it suggests that pre-trained CLIP alignment geometry is remarkably stable and that anchoring to it may be sufficient for many continual learning scenarios, with the EMA refresh providing only marginal additional benefit.

## Suggestions
- Clarify Fig. 3 data: specify the number of independent data points, explain the r=1.00 values, and reconcile with the "realistic scatter" description. If the data comes from a single trajectory, reframe as a trajectory visualization rather than a correlation claim across independent configurations.
- Add CLIP variant specification to §4.1.
- Describe the anchor prompt set composition, even if briefly, in the main text.
- Either include the time-continual study results in the main text or remove the forward reference from §4.1.
- Consider testing on a domain-shifted setting (e.g., medical/satellite imagery) where pre-trained alignment may genuinely degrade, to demonstrate the certificate EMA's value more convincingly and strengthen the "controlled plasticity" narrative.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>