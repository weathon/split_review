## Summary
TbLTA introduces the first weakly-supervised framework for dense long-term action anticipation (LTA), relying exclusively on video transcripts (ordered action lists without timing or boundary information) instead of costly frame-level annotations. The approach combines: (1) a temporal alignment module that generates pseudo-labels by aligning transcripts to video features, (2) cross-modal attention to contextually ground video features with transcript text embeddings, (3) a transformer encoder-decoder trained with CTC, CRF, and self-supervised duration losses. Experiments on Breakfast, 50Salads, and EGTEA show that the deterministic variant is competitive with, and on Breakfast occasionally surpasses, fully supervised baselines.

---

## Strengths

- **Genuinely novel problem formulation.** Dense LTA has exclusively been treated as a fully supervised problem. Being the first to make it feasible from transcript-only supervision is a meaningful contribution, with clear practical motivation: transcripts are far cheaper to obtain than frame-level labels for long procedural videos.

- **Impressive Breakfast results at 30% observation.** The deterministic TbLTA achieves 40.28 MoC at 10%-ahead horizon under 30% observation, outperforming ActFusion (35.79) and all other fully supervised baselines across the majority of columns. Surpassing fully supervised methods with weaker supervision is a strong empirical signal, suggesting that transcript-level procedural regularities capture Breakfast's sequential structure effectively.

- **Well-structured ablation study.** Each proposed component—CTC loss, local masked cross-modal attention, CRF, and the affinity-based duration loss—is individually ablated on both Breakfast and 50Salads, with consistent and interpretable gains. The hierarchy (w/o cross-att < cross-att simplex < TbLTA) validates the design of the masked gated cross-attention.

- **Dual deterministic/stochastic regime.** Reporting both regimes provides a useful view of the model's capacity. On Breakfast, the stochastic Top-1 variant (37.15 avg) substantially exceeds fully supervised deterministic methods, situating TbLTA relative to both paradigms.

---

## Weaknesses

### Fatal
None.

### Major

1. **Core technical components are largely borrowed.** The temporal alignment module is directly lifted from ATBA (Xu & Zheng, 2024); the parallel decoder is adapted from FUTR (Gong et al., 2022); the CRF module reuses the TCCA configuration (Maté & Damiccoli, 2024); CTC is a standard loss. The paper's primary novelty lies in connecting these existing pieces for a new task, plus the masked gated cross-modal attention and the self-supervised duration loss. This is a valid engineering contribution, but the thin novel technical content is a legitimate concern for acceptance at a top venue.

2. **Inference boundary estimation is underspecified.** During training, ATBA aligns the full transcript (observed + future) to the full video. At inference, only $X_{\text{obs}}$ is available and the transcript is not provided. The paper states that "the model must implicitly estimate both the boundary and the corresponding observed pseudo-labels $\hat{Y}_{\text{obs}}$," but the mechanism by which $k^*$ is estimated at inference time is never described concretely. This is a critical missing detail that affects reproducibility and scientific clarity.

3. **Limited comparison baseline for weakly-supervised methods.** There is only one prior weakly-supervised baseline, WS-DA (Zhang et al., 2021), which reports only a single number (Obs 30%, 10%-ahead) for each dataset. While the authors correctly note that TbLTA is strictly more weakly supervised than WS-DA (which still uses frame-level labels for the observed portion), the thinness of this comparison leaves open whether the gains are from the weaker supervision or the stronger backbone. Even an oracle upper bound or an ablated "transcript-only" version of a supervised baseline would strengthen the story.

### Minor

1. **Self-referential duration loss.** The affinity-based duration loss (Eq. 7) uses class-wise duration priors $\hat{d}$ estimated from the segmentation head's own pseudo-label predictions. This creates a circular dependency (pseudo-labels → duration priors → duration loss → pseudo-labels). The paper does not analyze how noisy these priors are, whether they converge, or how sensitive the method is to their quality. Given that duration estimation is identified as a remaining challenge, this deserves more scrutiny.

2. **EGTEA results are substantially below supervised methods.** The 11-point mAP gap overall (65.37 vs 76.80 for Anticipatr) is large; the claim of being "competitive on rare classes" is technically true but somewhat misleading since TbLTA's overall performance lags considerably. The paper should be more candid about this limitation.

3. **CTC loss formulation inconsistency.** Section 3.2.2 defines $\pi = [\pi_1, ..., \pi_{\alpha T}]$ as spanning only the observed frames, but Eq. 4 then sums $\prod_{t=1}^T$ over all $T$ frames. The CTC loss description conflates the observed-interval convention with the full-video convention used elsewhere.

4. **Progressive training schedule is not ablated.** The 3-stage training (video-level classification pre-training → alignment + segmentation → full objective) is described as essential ("crucial for stable training"), yet its contribution is not evaluated in the ablation study.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A quantitative analysis of pseudo-label quality (e.g., frame accuracy of ATBA pseudo-labels vs. ground truth) would clarify how much of the model's performance stems from alignment quality vs. the downstream modules.
- A cost comparison (annotation hours per dataset for transcripts vs. dense labels) would make the practical scalability argument more concrete.
- Visualizing attention masks from the cross-modal attention would validate that the local masking is meaningful.

---

## Novel Insights

The most genuinely novel empirical finding is that transcript-level supervision can match or exceed fully supervised methods on Breakfast for long observation ratios. This suggests that for procedurally structured activities with strong temporal regularities (Breakfast), the coarse ordering constraint of a transcript already captures the essential temporal structure, and the marginal value of precise frame boundaries is low. This finding has implications beyond this paper: it motivates rethinking annotation strategies for procedural video understanding tasks where the activity grammar is the main source of signal. The affinity-based self-supervised duration prior—estimating duration statistics from observed segments and applying them to anticipation without any temporal ground truth—is a lightweight but practically sensible idea that may be reused in semi-supervised settings.

---

## Suggestions

- Provide a concrete description of the inference-time $k^*$ estimation mechanism; this is essential for reproducibility.
- Ablate the progressive training stages to justify the added complexity.
- Include an analysis of pseudo-label quality (temporal accuracy) as a function of training epoch to show the method is learning stable alignments.
- Clarify the stochastic protocol in the main text (number of samples drawn, selection criteria for Mean vs. Top-1) rather than deferring entirely to the supplementary.
- Address the CTC summation range inconsistency (observed frames vs. full video).

---

## Score and Decision

The paper addresses an underexplored and practically important setting (dense LTA without frame-level labels) and produces a credible first result with competitive empirical performance. The Breakfast results at 30% observation are genuinely impressive. The main drags are the limited novel technical depth (primarily assembling existing modules) and the underspecified inference procedure for boundary estimation. These are meaningful but not fatal—the problem formulation and empirical findings bring value to the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>