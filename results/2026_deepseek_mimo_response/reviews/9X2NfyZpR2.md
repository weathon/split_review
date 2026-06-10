Now I have enough to calibrate. Let me assemble the final review.

**Round 1 bracket: 5.5–7.0**
- Weak anchors (~3.0): Object-centric video, anomalous action recognition, shadowboxing benchmark — all clearly weaker
- Middle anchors: Actions-to-Action (4.40, rejected), AntGPT (6.25, accepted), ActSeqAug (6.50, accepted), WS VidSGG (6.00, accepted)
- Strong anchors (7.7-8.0): Multi-granularity correspondence, Neural SDF Flow — different domains, clearly stronger

**Round 2 narrowing: 5.5–6.5**
- InterAct (5.00, rejected): Less novel, weaker results — TbLTA is clearly better
- WS VidSGG (6.00, accepted): Similar weakly-supervised video paradigm but smaller contribution — TbLTA is comparable or slightly above
- AntGPT (6.25, accepted): Also LTA, SOTA results but limited novelty — TbLTA has stronger novelty but messier evaluation
- ActSeqAug (6.50, accepted): Data augmentation for action anticipation — smaller contribution than TbLTA's new paradigm

TbLTA has genuine first-in-area novelty, competitive Breakfast results, but meaningful evaluation gaps (oracle-only ablations, no variance, missing stochastic baselines) and weak 50Salads/EGTEA results. This places it squarely at **6.0** — comparable to the accepted weakly-supervised papers at the same score, with stronger novelty offset by evaluation concerns.

## Summary
This paper proposes TbLTA, the first weakly-supervised method for dense long-term action anticipation (LTA) trained exclusively from video transcripts (ordered action lists without timing/duration). The architecture combines a transformer encoder with ATBA-based temporal alignment, cross-modal attention with pseudo-label-derived local masking, a CRF-augmented anticipation decoder, and an affinity-based duration loss. Results on Breakfast, 50Salads, and EGTEA establish the first transcript-only supervision baseline for dense LTA.

## Strengths
- **Genuinely novel first-in-area contribution**: TbLTA is convincingly the first dense LTA method trained without any frame-level annotations. The related work survey thoroughly establishes that all prior dense LTA methods (FUTR, ActFusion, Cycle Consistency, etc.) require frame-level labels, and even the closest prior work (Zhang et al., 2021) uses frame-level labels for observed segments (Section 2, lines 69-76). This opens a new paradigm for scalable action anticipation.
- **Competitive deterministic results on Breakfast at 30% observation**: Table 1 shows TbLTA outperforms all supervised baselines at Obs 30% (40.28 vs ActFusion's 35.79 at 10% pred; 35.76 vs 31.76 at 20%; 31.67 vs 29.64 at 30%), demonstrating that transcript-based supervision can match or exceed frame-level annotation for procedural activities with strong temporal regularity.
- **Well-designed cross-modal attention with local masking**: The pseudo-label-derived binary mask restricting each transcript action embedding to its predicted temporal neighborhood (Eq. 1-2) is principled. Table 4 shows a ~5.7-point drop on Breakfast when removed, with the masked variant consistently outperforming unconstrained "cross-att simplex."
- **Self-supervised affinity-based duration loss**: The momentum-based class-wise duration prior (Eq. 7) requires no temporal ground truth. Table 4 shows a ~3.3-point contribution on Breakfast.
- **Systematic multi-component ablation**: Tables 3-4 isolate CTC, cross-attention (with simplex variant), CRF, and duration loss contributions across both datasets, providing evidence for each component's role.

## Weaknesses

### Fatal
None.

### Major
- **Ablations use only the oracle Top-1 metric, not the deployable deterministic model's performance** — Section 4.3 states "we report results using the Top-1 MoC metric." Top-1 generates multiple stochastic samples and selects the best via oracle — unavailable at inference. Table 4's TbLTA Breakfast avg (37.2) matches the Top-1 row in Table 1 (37.15), not the deterministic row (29.03). The reported component contributions (5.7-point cross-attention drop, 3.3-point duration drop, 4.1-point CRF drop on Breakfast) conflate prediction quality with sample diversity. Without deterministic ablation numbers, the reader cannot assess whether components improve the actually deployable model or merely stochastic coverage. This is the most impactful evaluation gap and is straightforward to fix.

- **No variance reporting across splits for headline comparisons** — Results are averaged over 4 splits (Breakfast) or 5 splits (50Salads) with no standard deviations or confidence intervals. For the key headline claim — TbLTA outperforms ActFusion on Breakfast Obs 30% — the deterministic average gap is only 0.58 points (29.03 vs 28.45). Without knowing cross-split variance, this margin could easily be within noise. At Obs 20%, TbLTA is actually behind ActFusion at most horizons (27.47 vs 28.25 at 10%), so the advantage is setting-dependent and variance matters.

- **Stochastic results lack comparable stochastic baselines in the main table** — Table 1 shows TbLTA's stochastic Top-1 and Mean results (marked with *) alongside purely deterministic supervised baselines. ActFusion is itself a diffusion-based stochastic model (Gong et al., 2024), but its stochastic results are not included in Table 1. The paper notes stochastic results are in the supplementary material (line 223), but without them in the main table, TbLTA's stochastic numbers (37.15 on Breakfast, 28.51 on 50Salads) are unanchored — impossible to determine if they are competitive in the stochastic regime or simply inflated by oracle selection.

### Minor
- **50Salads and EGTEA gaps are substantial and underanalyzed** — On 50Salads, TbLTA deterministic avg is 20.92 vs ActFusion's 28.39 (7.5-point gap). On EGTEA (Table 2), TbLTA is 11.4 points behind Anticipatr on overall mAP. The paper attributes the 50Salads gap to "denser action distributions and frequent transitions" (line 227) but provides no targeted analysis (e.g., pseudo-label accuracy comparison between datasets, per-class breakdown). This limits the generalizability claim — the method works well for one dataset but poorly on two others.

- **Progressive 3-stage training is not ablated** — The training scheme (10 epochs pre-training, 30 epochs with alignment + segmentation losses, then full end-to-end with optimizer re-initialization) is a significant design choice with multiple hyperparameters (lines 197-199). Not ablating the staging makes it unclear whether this complexity is necessary.

- **No analysis of pseudo-label quality** — The entire training pipeline depends on pseudo-labels from the ATBA alignment module, but no analysis of their accuracy on each dataset is provided. This would help diagnose why the method works well on Breakfast but poorly on 50Salads.

- **Circular nature of duration loss** — The duration loss (Eq. 7) trains against pseudo-ground-truth estimated from class-wise frequency priors derived from the segmentation head's predictions. The paper acknowledges this is a "weak duration prior" (line 283) but does not analyze sensitivity to pseudo-label quality.

## Nice-to-Haves
- Report standard deviations alongside mean results in Table 1.
- Include deterministic (mean MoC) ablation results alongside Top-1 in Table 4.
- Include ActFusion's stochastic results in Table 1 for fair comparison in the stochastic regime.
- Provide per-dataset pseudo-label accuracy analysis to diagnose the 50Salads gap.
- Ablate the progressive training stages to understand necessity.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "ATBA module adopted from prior work without modification" — The paper transparently credits Xu & Zheng (2024) (line 126). ATBA is a building block, not a claimed novel contribution. Not a weakness.
- "Model has more per-dataset hyperparameters than baselines" — This is common practice across the field (different hidden dims, layers for different datasets). Not a meaningful criticism.
- "Missing stochastic baselines in supplementary" — The parser strips supplementary material; these likely exist in the original submission.
- "CTC ablation references Table 3 (IAS) not clearly present" — This appears to be in supplementary material, which is stripped by the parser.
- Formatting/style nitpicks — parser artifacts, not author issues.

## Novel Insights
The paper's core insight is that transcripts alone — without any frame-level annotation — can drive competitive dense long-term action anticipation for procedural activities. The surprising finding that transcript-based supervision matches fully supervised methods on Breakfast at 30% observation (Table 1) suggests that for activities with strong temporal regularity, the narrative structure captured by transcripts is sufficient supervision. The combination of temporal alignment pseudo-labels, cross-modal attention with local masking, and affinity-based duration loss forms a coherent and principled pipeline for this new paradigm. The honest reporting of 50Salads and EGTEA weaknesses reveals the boundary conditions: transcript-only supervision works well when temporal regularity is strong but struggles with denser, more variable action distributions.

## Suggestions
- Add deterministic (mean MoC) ablation results alongside Top-1 in Table 4 — this is the single highest-impact improvement, as it would directly validate that components improve the deployable model.
- Report standard deviations in Table 1 to validate the headline Breakfast claim where the gap is only 0.58 points.
- Include ActFusion's stochastic results in Table 1 for fair stochastic-regime comparison.
- Provide pseudo-label accuracy analysis per dataset to explain why performance differs dramatically between Breakfast and 50Salads.
- Analyze the CRF's surprising behavior at short horizons on Breakfast (removing CRF improves Obs 20%/10% from 37.2 to 39.7 per Table 4) — this suggests a smoothness bias worth understanding.

## Calibration Report

**Retrieved anchors across all rounds:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | 2HdZPEQUig (Object-centric video) | 3.00 | Clearly weaker — different domain, no novelty in action anticipation |
| 1 | MSxCBXD5C8 (Anomalous action) | 3.00 | Clearly weaker — narrow, incremental |
| 1 | Jq8HYNZG9s (ShadowPunch) | 3.00 | Clearly weaker — benchmark paper, no method novelty |
| 1 | TEjXRrhqtJ (TIEM video explanation) | 3.00 | Clearly weaker — different task |
| 1 | dl34rOnbqJ (Actions-to-Action) | 4.40 | Weaker — rejected, limited novelty, only short-term anticipation |
| 1 | GQgPj1H4pO (WS VidSGG) | 6.00 | Comparable — similar weakly-supervised video paradigm, smaller contribution but cleaner eval |
| 1 | Bb21JPnhhr (AntGPT) | 6.25 | Comparable — also LTA, SOTA results but limited novelty (just uses LLMs) |
| 1 | f3CdjpPkSq (ActSeqAug) | 6.50 | Comparable — action anticipation, smaller contribution (augmentation vs. new paradigm) |
| 1 | 9Cu8MRmhq2 (Multi-granularity) | 8.00 | Stronger — different domain, more mature |
| 1 | rzF0R6GOd4 (Neural SDF Flow) | 8.00 | Stronger — different domain |
| 1 | QQ6RgKYiQq (MovingParts) | 8.00 | Stronger — different domain |
| 1 | QQBPWtvtcn (LVSM) | 7.67 | Stronger — different domain |
| 2 | sEARCNzhrP (InterAct) | 5.00 | Weaker — rejected, less novel action segmentation work |
| 2 | HEXtydywnE (LASER) | 6.00 | Comparable — weakly supervised video understanding |
| 2 | yqJoqtUwSI (Co-Prop) | 5.20 | Weaker — rejected, narrower contribution |
| 2 | qHGgNyQk31 (Seer) | 6.50 | Comparable — video prediction with diffusion |
| 2 | stK7iOPH9Q (Lotus) | 6.40 | Comparable — dense prediction with diffusion |

**Bracket:**
- Round 1: 5.5–7.0 (TbLTA is clearly above rejected papers, comparable to accepted 6.0-6.5 papers)
- Round 2: 5.5–6.5 (TbLTA has stronger novelty than WS VidSGG (6.0) but messier evaluation; comparable to AntGPT (6.25) and ActSeqAug (6.50) with stronger novelty offset by evaluation gaps)

**Final score rationale:** TbLTA scores 6.0 — at the same level as WS VidSGG (6.00), with stronger novelty but meaningful evaluation gaps (oracle-only ablations, no variance, missing stochastic baselines). It is clearly above rejected papers (4.40-5.00 range) and comparable to accepted papers in the 6.0-6.5 range. The genuine first-in-area contribution and competitive Breakfast results are weighed against weak 50Salads/EGTEA performance and the ablation methodology concern. The paper is accept-worthy but not strong enough for a higher score without addressing the evaluation gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>