Now let me write the final review.

## Summary
This paper proposes TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts (ordered action lists without temporal annotations). The architecture combines a Transformer encoder with learnable class tokens, a temporal alignment module (ATBA) for generating pseudo-labels, local-masked cross-modal attention for grounding video features with transcript information, a CTC loss for transcript consistency, a CRF decoder for temporal coherence, and a self-supervised duration prediction head. Experiments on Breakfast, 50Salads, and EGTEA Gaze+ show that on Breakfast at 30% observation, the deterministic TbLTA outperforms all fully-supervised baselines.

## Strengths
- **Genuine first contribution for transcript-only dense LTA**: The paper clearly establishes that prior dense LTA methods all require frame-level annotations, and the closest prior weakly-supervised approach (WS-DA, Zhang et al., 2021) still uses temporally localized labels. Table 1 confirms TbLTA dramatically outperforms WS-DA on Breakfast (29.03 vs. ~15.65 average MoC at Obs 30%), demonstrating transcript-only supervision is a viable and substantially better paradigm.

- **Strong empirical results on Breakfast at Obs 30%**: The deterministic TbLTA achieves 29.03 average MoC (Table 1), surpassing all fully-supervised baselines including ActFusion (28.45), FUTR (26.59), and Cycle Consistency (25.13). A weakly-supervised method outperforming fully-supervised baselines on an established benchmark is a meaningful finding.

- **Well-designed local-masked cross-modal attention**: The design of restricting each transcript action embedding to attend only within its predicted temporal neighborhood via binary mask M (Eq. 1), combined with sigmoid-gated residual injection (Eq. 2), is architecturally distinct from unconstrained cross-attention.

- **Multi-pronged utilization of transcripts**: Transcripts serve in three complementary roles — as alignment/pseudo-label supervision via ATBA and CTC (Sections 3.2.1–3.2.2), as semantic context through local-masked cross-modal attention (Eqs. 1–2), and as global sequence constraints via CTC loss. This is a thoughtful and well-motivated design.

- **Affinity-based self-supervised duration loss (Eq. 7)**: The duration prediction head leverages the insight that videos depicting the same activity share similar temporal proportions, using momentum-based class-wise duration priors from observed segments — providing temporal supervision without boundary annotations. The ablation shows its removal drops ~3.3 points on Breakfast.

## Weaknesses

### Fatal
None

### Major
- **Ablation tables are duplicated (Table 3 and Table 4 contain identical data)**: The paper presents two ablation tables — presumably Table 3 (for IAS/TAS) and Table 4 (for LTA) — but they contain exactly the same data. Every row and every number is identical (lines 250–257 vs. 262–269). The text states "Results in Table 3 (IAS) and Table 4 (LTA) show a consistent hierarchy" (line 235), but since IAS and LTA are different evaluation tasks, they cannot both be correct. This is a copy-paste error that undermines the ablation study because readers cannot determine which table shows which task's results.

- **Missing ablation variants discussed in text**: The text claims specific numerical drops for the "cross-att simplex" variant (~0.8 on 50Salads, ~3.8 on Breakfast, lines 235–236) and for removing CTC loss (~0.6 on 50Salads, ~0.8 on Breakfast, line 233). However, neither "cross-att simplex" nor "w/o CTC" rows appear in either ablation table. These are two of the five ablation conditions discussed, making 40% of the ablation claims unverifiable from the presented results.

- **Mislabeled table row**: The first "w/o CRF" row under the "Breakfast" label (line 253, avg 23.2) does not match the text's claim of a ~4.1-point drop on Breakfast (37.2 − 4.1 = 33.1). Instead, 28.5 − 5.3 = 23.2 perfectly matches the claimed 50Salads CRF ablation drop (line 281: "≈5.3 on 50Salads"). This indicates the 50Salads "w/o CRF" row was mislabeled as "Breakfast," and the actual 50Salads "w/o CRF" row is missing from its proper location.

### Minor
- **No variance or statistical significance reported**: All results are single numbers without standard deviations over the 4/5 splits. Several headline comparisons involve small margins — e.g., on Breakfast Obs 30% at 50% horizon, several methods are close — and without variance, significance is uncertain at the margins.

- **Overstated novelty claim in abstract**: The abstract claims TbLTA is "the first weakly-supervised approach for LTA," but Zhang et al. (2021) already explored weakly/semi-supervised dense LTA. The paper correctly distinguishes itself in the body (line 74: "the first fully weakly-supervised framework for dense LTA"), but the abstract framing is imprecise. The more accurate claim — "first transcript-only dense LTA" — is compelling enough on its own.

- **50Salads gap partially obscured by stochastic protocol**: On 50Salads, TbLTA deterministic avg (20.92) trails ActFusion (28.39) by 7.5 points. The stochastic Top-1 result (28.51) closes this gap, but stochastic Top-1 selects the best sample from multiple futures — a fundamentally different evaluation. The paper does present both protocols but could be more explicit about this distinction.

### Trivial
- The text references "as shown in 3" (line 233) for the CTC effect, likely meaning "Table 3," but no table number is explicitly shown for the first ablation table.

## Nice-to-Haves
- A brief analysis of pseudo-label quality from the ATBA module and how it affects downstream anticipation.
- Justifying the progressive training scheme with an ablation comparing single-stage vs. multi-stage training.
- Analysis of why transcript supervision works particularly well on Breakfast vs. 50Salads (structural dataset properties).
- Per-split standard deviations for main results.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Reproducibility concerns about ATBA module"**: The ATBA module is cited from Xu & Zheng (2024). Per hard rules, we do not question the existence or availability of cited work.
- **"Missing related works"**: Per policy, we do not flag missing related works without external verification of their existence.
- **Nitpicks about EGTEA evaluation protocol differences**: The paper follows established protocol for EGTEA (verb prediction, mAP) which is standard for that benchmark.

## Novel Insights
The paper's genuinely novel observation is that transcript-only supervision can match or exceed fully-supervised performance for dense LTA on structured procedural datasets like Breakfast (Obs 30%), suggesting that high-level semantic supervision captures the procedural regularities needed for anticipation without requiring dense frame-level annotations. The weaker performance on 50Salads reveals an important boundary condition: transcript supervision is less effective when activities have denser action distributions and weaker temporal regularities — an insight worth further investigation.

## Suggestions
- Fix the ablation tables: provide separate, correctly populated tables for IAS and LTA. Include the "cross-att simplex" and "w/o CTC" variants. Correct the mislabeled 50Salads "w/o CRF" row.
- Refine the abstract/introduction to claim "first transcript-only LTA" rather than "first weakly-supervised LTA."
- Report per-split standard deviations for all main results.
- Add discussion of why transcript supervision works well on Breakfast but struggles on 50Salads.

## Calibration Report

### Anchors Retrieved

**Round 1:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 2HdZPEQUig | 3.00 | R1 | Object-centric video learning — less relevant, weaker contribution |
| Jq8HYNZG9s | 3.00 | R1 | Action spotting benchmark — less relevant |
| MSxCBXD5C8 | 3.00 | R1 | Anomalous action recognition — less relevant |
| TEjXRrhqtJ | 3.00 | R1 | Video prediction explanation — less relevant |
| dl34rOnbqJ | 4.40 | R1 | Egocentric action anticipation (Reject) — weaker technical contribution; TbLTA clearly stronger |
| sEARCNzhrP | 5.00 | R1 | Temporal action segmentation (Reject) — decent but rejected; TbLTA has stronger contribution |
| DE2RMJVjgI | 4.25 | R1 | Point-level temporal action localization (Reject) — weakly supervised video; TbLTA stronger |
| HCoSsULNxG | 4.75 | R1 | Weakly supervised skilled activity (Reject) — somewhat relevant; TbLTA stronger |
| f3CdjpPkSq | 6.50 | R1 | Action sequence augmentation (Accept) — directly relevant; comparable contribution, cleaner presentation |
| Bb21JPnhhr | 6.25 | R1 | AntGPT for LTA (Accept) — very relevant; comparable novelty, better presentation |
| GQgPj1H4pO | 6.00 | R1 | Weakly supervised video scene graph (Accept) — weakly supervised video, comparable score |
| HEXtydywnE | 6.00 | R1 | LASER neuro-symbolic video (Accept) — weakly supervised video |
| 9Cu8MRmhq2 | 8.00 | R1 | Multi-granularity correspondence (Accept) — much stronger paper |
| weM4YBicIP | 8.00 | R1 | Loopy portrait avatar — not relevant |
| TPZRq4FALB | 8.00 | R1 | Test-time adaptation — not relevant |
| QQ6RgKYiQq | 8.00 | R1 | MovingParts — not relevant |

**Round 2:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| DE2RMJVjgI | 4.25 | R2 | (duplicate of R1) |
| VSHuwBUlYr | 4.80 | R2 | Zero-shot video segmentation (Reject) — less relevant |
| oO3oXJ19Pb | 4.80 | R2 | Dense video captioning (Reject) — somewhat relevant |
| sEARCNzhrP | 5.00 | R2 | (duplicate of R1) |
| LDAj4UJ4aL | 6.00 | R2 | VEDIT procedural video (Accept) — very relevant; comparable contribution quality |
| qHGgNyQk31 | 6.50 | R2 | Seer video prediction (Accept) — less directly relevant |
| Bb21JPnhhr | 6.25 | R2 | (duplicate of R1) |
| Un0rgm9f04 | 6.00 | R2 | VDT video diffusion (Accept) — less relevant |
| Uj2Wjv0pMY | 4.33 | R2 | Procedural video error detection (Reject) — somewhat relevant |
| wT1aFmsXOc | 5.00 | R2 | Diffusion memorization — not relevant |
| lf8QQ2KMgv | 3.75 | R2 | Memorization generalization — not relevant |

### Bracketing
- **Round 1 bracket**: 4.5 – 6.5. TbLTA is clearly stronger than the 4.25–4.40 reject papers (weak contributions, incremental results) but has more serious presentation issues than the 6.25–6.50 accept papers (AntGPT, ActSeq).
- **Round 2 bracket**: 5.0 – 6.5. VEDIT (6.00, Accept) is the closest anchor — both address procedural video understanding with novel approaches and strong results. TbLTA has comparable setting novelty (first transcript-only LTA) but worse experimental presentation (duplicated ablation tables, missing variants).
- **Final score**: 6.0 — The genuine novelty of transcript-only dense LTA and the strong Breakfast results place this paper at the accept threshold, comparable to VEDIT. The ablation table issues are serious but fixable and do not invalidate the main comparative results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: Accept