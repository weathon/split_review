## Summary
PI-CCA proposes a replay-free continual-learning framework for vision-language models that summarizes pre-trained image–text alignment with a compact "certificate" (top-k canonical correlations plus sketched canonical subspaces), enforces spectral and subspace-angle consistency during adaptation, and adds a prompt-invariance loss via projector averaging. Experiments on MTIL, X-TAIL, VLCL, and ConStruct-VL show modest but consistent improvements over strong replay-free baselines.

## Strengths
- **Conceptually clean reframing**: Treating forgetting as drift of CCA invariants of the *whitened* cross-covariance (Eq. 2) is a sensible and reasonably novel preservation target compared with off-diagonal or logit distillation approaches (§2, §3.2).
- **Constant-memory certificate**: Storing only sketched bases of dimension h×k (Eq. 4) genuinely decouples memory from feature dimension, an engineering advantage over teacher-logit or reference-corpus methods.
- **Projector-averaging for sign/rotation ambiguity** (Eq. 5–6) is a tidy way to handle prompt variation without Procrustes alignment.
- **Component-wise ablations** in Table 3 are structured cleanly, showing each loss term contributes meaningfully (spectral and subspace terms cause the largest drops on removal).
- **Task-order robustness study** (Fig. 5, 20 orders × 3 seeds) is good practice and shows narrow IQR.
- **Consistent gains across four heterogeneous tracks** — including beating the synthetic-replay method GIFT on VLCL retrieval (Table 2) — provides reasonable evidence that the approach works.

## Weaknesses

### Fatal
None.

### Major

- **Figure 3's reported correlations are not credible as presented.** Across a heterogeneous sweep (certificate size, EMAs, invariance strength, whitening, pairing scheme, LoRA capacity/LR, sketch type) the paper reports Pearson r = 1.00 / Spearman ρ = 1.00 (with one panel at r = 0.99) on all four panels of ΔAvg/ΔR@1 against D_ang and D_ρ. Obtaining four simultaneously perfect correlations across such heterogeneous perturbations is empirically implausible; the caption's claim of "realistic scatter" conflicts with r = 1.00. Because this figure is the central empirical bridge for the paper's headline thesis ("alignment-geometry drift predicts forgetting", §5), the issue is not cosmetic. The authors should re-run, decompose by perturbation type, or report what aggregation was done — currently this undermines the strongest conceptual claim.

- **Internal tension between "certificate as invariant" and Eq. 13.** §3.2 frames the certificate as a *reference (pre-continual)* quantity (ρ\*, U\*, V\*), but Eq. 13 EMA-updates ρ\*, S\*_v, S̄\*_t toward the current mini-batch every step. The authors describe this as "controlled plasticity" (§3.4), which is reasonable as engineering, but it means the constraint is toward a moving anchor partially tracking adaptation, not a strict pre-training invariant. The motivating contrast with "proxy regularizers" (§1) is therefore softer than the paper claims. The paper should quantify how far the EMA-tracked certificate drifts from the t=0 reference over a full task stream — without this, the "invariant preservation" interpretation cannot be cleanly distinguished from a smoothed self-regularizer.

- **Source of the initial reference statistics is undisclosed.** Constructing ρ\*_{1:k}, U\*_k, V\*_k requires paired image–text statistics from *some* corpus (Eq. 1–2), and §3.2 mentions "a diverse anchor prompt set" but never specifies the data. If this corpus is held-out generic VLM data, PI-CCA implicitly relies on a reference set, comparable to what ZSCL uses, and the "replay-free / reference-free" framing in §1 should be qualified. This is a real disclosure gap that affects whether comparisons to other replay-free baselines are apples-to-apples.

### Minor

- **No variance/significance estimates on Table 1.** Margins over the strongest baselines on MTIL/X-TAIL are 1–2 points (e.g., 76.8 vs 75.2 Avg on MTIL). Single-run is common in CL benchmarks, so this isn't disqualifying, but error bars or seed std for the headline table would meaningfully strengthen the SOTA claim — particularly because Table 2 already reports ± values.
- **L_pi gain not isolated from "more prompt augmentation".** The stress test (Fig. 4) compares L_pi on/off but does not include a baseline that simply trains with the same M prompt perturbations as text augmentation. The reported +2.44 pp at s=1.0 may partly reflect augmentation volume rather than the projector-averaging geometry.
- **Sketch-space surrogate justification is informal.** §3.3 asserts that the sketched Frobenius distance "preserves order/angles under near-isometric sketches" but does not provide a JL/SRHT bound for the top-k projector setting at the practical h≈256, d≈thousands regime. A short bound or empirical check vs. principal-angle distance would close this gap.
- **Pareto and component ablation use only PI-CCA itself.** The task-order study and Pareto sweep do not include baselines, so we cannot tell whether PI-CCA's tight IQR or broad Pareto ridge is unusual relative to e.g. C-CLIP or ZSCL.

### Trivial
- The notation in Eq. 12/13 mixes notation styles (Σ vs S\*) that could be tightened for clarity.

## Nice-to-Haves
- A direct plot of the principal-angle trajectory between current canonical subspace and the t=0 reference across the task stream — this is the most direct test of the central claim.
- A controlled ablation where competing baselines are also given access to the initial paired corpus used to seed the certificate.
- A check that gradients through the differentiable SVD / Newton–Schulz whitening are numerically stable across whole runs, not just per-step.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Code unavailable for review."* The authors explain commercial constraints and commit to camera-ready release; this falls under the soft rule about reproducibility nitpicks.
- *"Baselines like LADA / ENGINE / MG-CLIP / Proxy-FDA appear only as point numbers."* Without external lookup we cannot tell whether these are re-implementations or cited numbers; the harsh critic's complaint requires evidence we don't have here.
- *"Table 2 ±values are suspiciously low."* The standard deviations (e.g., AF 2.7 ± 0.2) are within plausible ranges for averaged metrics on these benchmarks; "suspicious" is not a substantive criticism without comparison data.
- *"Averaging projectors only works when perturbations sample the same subspace, otherwise trailing eigenvalue mass should be reported."* Reasonable as a nice-to-have analysis, but the paper's top-k truncation is a standard, well-defined operation regardless of rank; calling this a flaw is overreach.
- The Strength Finder's claim that the Fig. 3 near-perfect correlations *validate* the central insight is dropped — the weakness about Fig. 3 wins.

## Novel Insights
None beyond the paper's own contributions. The core conceptual move — using CCA spectrum + subspaces of the whitened cross-covariance as the preservation target, and handling prompt variability via sketched projector averaging — is the paper's own contribution.

## Suggestions
- Re-derive Figure 3 transparently: report each perturbation family separately, the units of D_ang and D_ρ, the number of points, and the raw correlations without aggregation. Ideally include a plot where the perfect linearity is *not* trivially induced by aggregating means.
- Either drop the "invariant of pre-trained alignment" framing in favor of "smoothly tracked alignment anchor", or freeze the certificate at t=0 for an ablation and report the gap. This will resolve the §3.2 ↔ Eq. 13 tension.
- Disclose the corpus used to construct the initial certificate, its size, and its overlap with downstream tasks; relabel the method's "reference-free" status accordingly.
- Add seed std for Table 1's main rows, even with a small number of seeds (e.g., 3).
- Add an L_pi ablation where the baseline also sees the M prompt perturbations as standard augmentation.

## Axes
- **Originality**: Moderate. CCA-invariant preservation as a CL objective is a genuinely fresh framing, though related to representation-similarity diagnostic work and the prior Mod-X/Proxy-FDA family.
- **Importance**: Replay-free VL-CL is a real and active problem.
- **Claim support**: Mixed. The headline ranking results are credible (small but consistent margins). The "geometry predicts performance" claim rests on a figure whose reported statistics are not believable as-is. The "invariant" framing is not fully consistent with the actual update rule.
- **Soundness**: Mechanism is reasonable; some derivations (sketch-space Frobenius ≈ principal angles) are asserted rather than bounded.
- **Clarity**: Generally clear; notation occasionally heavy but standard for CCA.
- **Value to community**: A useful new regularizer to compare against. The integrity question around Fig. 3 and the corpus disclosure must be addressed before the conceptual contribution stands.

## Anchors
- `G9Ea7mlqGO.md` (avg 3.80, Reject) — CLIP online CL. Topic-near; weaker methodology and analysis than PI-CCA, which is more thoroughly evaluated.
- `sb7qHFYwBc.md` (avg 6.50, Accept) — C-CLIP, a direct comparator and baseline in PI-CCA. PI-CCA reports beating it numerically but has more presentation/integrity concerns.
- `TLADT8Wrhn.md` (avg 6.25, Accept) — TiC-CLIP. Stronger benchmark contribution; PI-CCA is a method paper of narrower scope.
- `k9NYnsC4Mq.md` (avg 5.67, Reject) — LwF for VLMs. Borderline reject in the same neighborhood as where PI-CCA sits, but cleaner story.
- `9aZ2ixiYGd.md` (avg 5.00, mixed scores) — rehearsal-free VL CL. Similar borderline-paper profile.
- `4SrzKsJocx.md` (avg 3.80, Reject) — CCA-based multimodal DR. Related technical machinery, weaker empirics than PI-CCA.
- `HCCkCjClO0.md` (avg 3.00, Reject) — weak online CL; clearly below PI-CCA in rigor and results.
- `WM5G2NWSYC.md` (avg 2.00, Reject) — projected subnetworks for zero-shot retention; clearly below PI-CCA.
- `6Mg7pjG7Sw.md` (avg 6.00, Accept) — CCA-style unimodal-to-multimodal mapping; comparable technical machinery, more disciplined empirical story.

PI-CCA sits between the C-CLIP / LwF-VLM band and the weaker rejected anchors. The empirical contribution (SOTA across four tracks, sensible ablations, order-robustness) is real, but the Fig. 3 integrity concern and the unresolved EMA-vs-invariant + reference-corpus disclosure issues make it weaker than the 6.0–6.5 accept anchors. It is closer to the 5.0–5.67 borderline-reject anchors than to the clearly bad ≤4 anchors.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>