Now I have all the information I need. Let me write the final review.

## Summary

This paper proposes TbLTA, the first weakly-supervised framework for dense long-term action anticipation (LTA) that is trained exclusively using video transcripts — ordered action lists without timing, duration, or boundary information. The method combines a temporal alignment module (ATBA) to generate pseudo-labels, a cross-modal attention mechanism to ground video features in transcript semantics, and multiple complementary losses (CTC, CRF, duration). Results on Breakfast, 50Salads, and EGTEA benchmarks show that transcript-only supervision can approach or even surpass fully-supervised performance on some settings, most notably on Breakfast where deterministic TbLTA (29.03%) edges out the best fully-supervised method ActFusion (28.45%).

## Strengths

- **First transcript-only weakly-supervised framework for dense LTA, filling a genuine gap in the literature.** Prior LTA work is almost entirely fully supervised; the only weakly-supervised attempt (Zhang et al., 2021) still uses temporally localized annotations. TbLTA requires only an ordered action list, and surpasses Zhang et al.'s WS-DA baseline on both Breakfast and 50Salads (e.g., 27.67 vs. 21.30 at Obs 30%/horizon 10% on 50Salads), confirming the method succeeds under strictly weaker supervision.

- **On Breakfast, deterministic TbLTA achieves 29.03% average MoC, surpassing the fully-supervised ActFusion (28.45%).** This is the paper's most striking result: a model trained with no frame-level annotations outperforms the best fully-supervised method on aggregate. At Obs 30%/horizon 10%, the gap is 40.28% vs. 35.79%, a 4.5-point gain. This demonstrates that transcript-level semantic supervision can, on procedurally regular activities, capture temporal structure as effectively as dense labels.

- **The local cross-modal attention mechanism (Eqs. 1–2) is a technically principled design.** Rather than unconstrained cross-attention, the method constructs a binary mask from pseudo-labels to restrict each action text embedding to a temporal neighborhood around its predicted occurrence, combined with a gated residual update. The ablation confirms this design choice: removing cross-attention drops average accuracy by ~5.7 points on Breakfast and ~1.3 points on 50Salads, while a "simplex" unconstrained variant also underperforms.

- **Systematic ablation isolating each loss component.** The ablation (Table 4) tests CTC removal, cross-attention removal, CRF removal, and duration loss removal with per-horizon breakdowns across two datasets, making the contribution of each design choice concrete. The self-supervised duration loss (Eq. 7) is a clever mechanism to predict segment durations without temporal ground truth.

## Weaknesses

### Major

1. **Ablation study uses the stochastic Top-1 metric while the paper's main claims rest on the deterministic protocol, creating a misalignment between the evidence and the claims it is meant to support.** The main comparison (Table 1, "Ours (TbLTA)" row, 29.03% on Breakfast) reports deterministic MoC. The ablation study (Section 4.3, Table 4, 37.2% on Breakfast) reports the *stochastic* Top-1 MoC — matching the "Ours (TbLTA)* - Top1" row in Table 1. The paper states "we report results using the Top-1 MoC metric" (Section 4.3), which is a disclosure but does not resolve the mismatch. The magnitude of component contributions, and even which components are most important, could differ between the two protocols. For example, the CRF and stochastic sampling might interact in ways that overstate the CRF's importance under a deterministic evaluation. The paper needs ablations under the *same deterministic protocol* used for its primary comparisons, or at minimum a clear justification for why the stochastic protocol is the appropriate setting for ablating components whose impact is then claimed under a deterministic setting.

2. **The claim of being "competitive with fully supervised methods" is calibrated primarily by the Breakfast result and is less supported on the other two datasets.** On 50Salads, deterministic TbLTA (20.92%) trails ActFusion (28.39%) by ~7.5 points. On EGTEA, TbLTA (65.37 mAP) trails Anticipatr (76.80 mAP) by ~11 points. The paper acknowledges these gaps in the text (Section 4.2), but the abstract's characterization ("transcript-based supervision offers a very robust and less costly alternative to its fully supervised counterpart") and the title's framing suggest a broader competitiveness than the evidence supports. The claim should be calibrated to reflect the mixed picture: strong on Breakfast, substantially weaker on 50Salads and EGTEA overall (though competitive on rare classes in EGTEA).

### Minor

3. **The self-supervised duration loss (Eq. 7) has a potential circularity issue that is not discussed.** The duration priors are computed from the model's own pseudo-labels on the observed portion. Poor pseudo-labels → poor duration priors → poor duration supervision → worse pseudo-labels. The momentum buffer mitigates this somewhat but does not eliminate the concern. The paper would benefit from explicitly discussing this bootstrapping dynamic and justifying why it does not lead to degenerate solutions, especially since the ablation shows removing the duration loss costs ~3.3 points on Breakfast — a nontrivial contribution from a potentially circular signal.

4. **No comparison to simple transcript-based baselines.** Since the method adopts the ATBA module (Xu & Zheng, 2024) for temporal alignment, a natural baseline would be: (a) run ATBA on the observed portion to get action boundaries, then (b) use the transcript ordering directly or a Markov model for the future. This would isolate whether TbLTA's architectural components add value beyond what any reasonable alignment+copy method could achieve. While not strictly required (there is no existing transcript-based LTA method), such a baseline would substantially strengthen the paper's attribution of results to specific design choices.

### Trivial

5. The abbreviation "ActFusion" is cited as "Guo et al., 2024" in Table 1 but the actual ActFusion paper is Gong et al. (2024), which is correctly cited in the main text — there is a citation inconsistency in the table.

## Nice-to-Haves

- The progressive 3-stage training scheme (pre-training → alignment → end-to-end) is not ablated. The contribution of the pre-training stage and the intermediate alignment stage to final performance is unmeasured. Given that pseudo-label methods are known to be sensitive to initialization, this would be informative.
- Adding error bars or per-split variance would help assess significance, particularly since the Breakfast advantage over ActFusion (29.03 vs. 28.45) is only ~0.6 points and could be within noise.

## Removed Points

These points were flagged by reviewers but removed for the following reasons:

- **"Comparison to weakly-supervised alternatives is thin, with only one baseline"** — Removed. No other transcript-supervised LTA methods exist in the literature. WS-DA (Zhang et al., 2021) is the only weakly-supervised LTA baseline. Requesting adapted TAS methods as baselines is a nice-to-have, not a weakness.
- **"Missing hyperparameters (loss weights γ1, γ2, γ3, learning rates)"** — Removed per hard rules (nitpicks about undisclosed hyperparameters in a paper that references supplementary material).
- **"No standard deviations or error bars"** — Removed per field norms (none of the compared baselines report error bars either; the standard protocol averages over dataset splits).
- **"Boundary index estimation k* mechanism not explained"** — Removed. The paper explains this is handled by the ATBA module: "we adopt the ATBA module... to partition the full transcript into observed and future sub-transcripts" (Section 3.1).
- **"Duplicated Table 4"** — Removed as a PDF extraction artifact, not an author error.
- **Various formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run the ablation study under the **same deterministic protocol** used for the main comparison (Table 1). This is the single most important improvement: it would directly connect the component analysis to the paper's primary claims.
2. Recalibrate the abstract and conclusion claims to distinguish between the Breakfast result (where transcript supervision is genuinely competitive with full supervision) and the 50Salads/EGTEA results (where the gap is substantial).
3. Add a simple transcript-based baseline (e.g., ATBA alignment + future transcript copying) to isolate the value of the proposed architecture.
4. Discuss the potential circularity of the self-supervised duration loss and justify its stability.

## Score and Decision

**Round 1 bracket:** [5.0, 6.5]. The paper's contribution (first transcript-only dense LTA, strong Breakfast results) positions it above rejected papers in the 3–4.4 range, but the ablation protocol mismatch and overclaimed generality keep it below the cleanest accept papers in the 6–6.5 range.

**Round 2 narrowing:** Comparison against in-bracket anchors confirms this assessment. The paper is weaker than AntGPT (6.25) and Action Sequence Augmentation (6.50) — both have cleaner evaluations without protocol mismatches — but stronger than Actions-to-Action (4.40, rejected) and comparable to Active Procedure Planning (5.67, rejected) and Weakly Supervised VidSGG (6.00, accepted). The comparison to LASER (6.00) is instructive: LASER has a comparable novelty level but cleaner execution.

**Anchor comparison table:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| AntGPT | Bb21JPnhhr.md | 6.25 | 1, 2 | Stronger — SOTA with clean evaluation; TbLTA is weaker |
| Action Sequence Augmentation | f3CdjpPkSq.md | 6.50 | 1, 2 | Stronger — cleaner ablation/evaluation; TbLTA is weaker |
| Weakly Supervised VidSGG | GQgPj1H4pO.md | 6.00 | 1, 2 | Comparable — similar novelty level, TbLTA has evaluation flaw |
| Actions-to-Action | dl34rOnbqJ.md | 4.40 | 1 | Weaker — core design questioned by ablation; TbLTA is stronger |
| LASER | HEXtydywnE.md | 6.00 | 2 | Comparable — similar contribution level, cleaner execution |
| Long Context Transfer | QETk0lBdVf.md | 5.80 | 2 | Comparable — interesting idea but incomplete evidence |
| Active Procedure Planning | JDd46WodYf.md | 5.67 | 2 | Comparable — similar tier with notable weaknesses |
| Object-Centric Learning | 2HdZPEQUig.md | 3.00 | 1 | Weaker — fundamental issues; TbLTA is clearly stronger |

**Final determination:** The paper has a genuine contribution and a striking result on Breakfast, but the ablation protocol mismatch is a material weakness that prevents confidence in the attribution of results to specific components. The claims are also somewhat overbroad relative to the evidence. I rate this below the clean 6+ accept threshold but above the reject range. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>