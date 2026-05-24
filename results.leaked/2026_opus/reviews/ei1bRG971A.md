Now I have a good understanding of the paper. Let me run calibration searches.Round 1 bracket: 3.5 to 6.5. The paper sits between rejected routing/adaptive computation papers (2.5-3.4) and accepted ones (5-7). Let me narrow in.Based on my analysis of the paper and calibration anchors, I have enough information to finalize the review.

## Summary
The paper proposes Dynamic Nested Depth (DND), a post-training augmentation that inserts per-token routers at intermediate transformer layers; tokens scoring above a learned threshold are repacked and re-processed through the same (weight-shared) layer, with the outputs fused via a learned gate. The paper contributes a "router controlling loss" (entropy dispersion + MSE-pull-to-0.5) and a "threshold control scheme" (buffer proportional control + EMA synchronization) to make token-choice routing trainable without z-loss-style balancing. DND is evaluated via SFT on Qwen3-1.7B, Llama3.2-1B, Gemma3-1B (dense) and Qwen3-30B-A3B (MoE), with one detailed ablation on Qwen3-1.7B.

## Strengths
- **Consistent gains across dense models**: Table 1 shows +1.88, +2.61, +2.50 average improvement across Qwen3-1.7B, Llama3.2-1B, and Gemma3-1B over 11 benchmarks, with especially large jumps on BBH (+3.70 to +5.02) and GPQA-Diamond (+3.86 to +5.80).
- **Demonstrated transfer to a 30B MoE**: The method applies to Qwen3-30B-A3B (Table 2) with negligible parameter overhead (~0.03M), showing the design is not limited to small-scale dense models — addressing a gap that the related MOR work could not.
- **Practical efficiency**: Table 3 shows DND retains 91.6–93.1% of vanilla throughput with vLLM-accelerated BF16 inference, and §4.3/Appendix A reports only ~6% extra FLOPs for 20% selection — supporting the "minimal computing increase" claim quantitatively.
- **Training-control machinery is well-instantiated**: Figures 5 and 6 give direct evidence that buffer proportional control + EMA synchronization stabilize the selection ratio in a tight ±5% band, and that the router controlling loss reduces oscillations — these are concrete artifacts of the engineering claim, not just downstream-metric correlations.
- **Coherent ablation of the training components**: Table 4 separates router control (RC) and threshold control (TC), and shows the z-loss-like baseline yields only +1.01 vs +1.88 for the full DND, giving a non-trivial story about which components matter.

## Weaknesses

### Fatal
None.

### Major
- **The scale story is the smallest gain**: On the only large/SOTA model (Qwen3-30B-A3B), the average improvement is +0.87 (Table 2), with individual entries ≤0.5 on six benchmarks (MMLU +0.50, CMMLU +0.37, BBH +0.13, DROP +0.27, MATH +0.15, MATH-500 +0.20). The paper frames this as "substantial gains" for "unlocking the potential of existing state-of-the-art pretrained models," but the dose–response goes the wrong direction for that framing. The paper does not engage with this — there is no discussion of whether DND's effect diminishes with scale, or whether 30B is a noise floor. This matters because it is the central empirical claim being raised.
- **No variance / single-seed reporting on main tables**: Tables 1, 2, and 4 are single point estimates. SFT runs on the same base with the same data routinely differ by several tenths of a point on small benchmarks (GPQA-Diamond has 198 questions; a +5.80 swing is ~11 items). Several Table 2 entries (especially the ≤0.3-point ones) cannot be confidently distinguished from seed noise without error bars. The headline arguments rely on multi-decimal differences that the experimental design does not establish.
- **Missing compute-matched SFT baseline**: DND adds ~6% FLOPs and trains extra router parameters/threshold-control machinery on top of plain SFT. The relevant question is "DND vs SFT given matched compute / matched token budget," not "DND vs plain SFT." Without this comparison (more steps, larger batch, or a same-layer fully-recurrent baseline), it is not possible to attribute gains specifically to the selective-routing mechanism rather than the extra training compute. This applies to every result in §4.3.
- **Closest competitor (MOR) is not run in DND's setting**: The paper explicitly identifies MOR as the closest related work and is clear about architectural differences. But Table 4's "z-loss-like" baseline is not a faithful reimplementation of MOR's expert-choice + auxiliary-loss combination. The paper's distinct contribution is the control machinery, but the baseline that would isolate that contribution (MOR-style routing in the same post-training setting) is absent. ITT is the only neighboring-method baseline and only on Qwen3-1.7B.

### Minor
- **Token-selection analysis is weak as evidence for "criticality"**: Fig. 4a's Pearson r = 0.3359 between selection count and vanilla logit entropy is a weak correlation and is asserted to "validate the motivation behind critical token selection." Fig. 4b shows entropy drops after DND (r = -0.5811), but lower predictive entropy is not the same as better outputs. These plots are suggestive but the paper places more interpretive weight on them than they support.
- **Motivation/mechanism gap**: §1 frames DND as "deepening computation" and "additional computational depth," but the mechanism is weight-shared re-application of the same layer with new positional embeddings — i.e., recurrence in time, not added depth in parameters. This is not invalidating, but the framing in the abstract and §1 oversells what is mechanically a per-token weight-tied two-step refinement.
- **Ablation framing understates partial-design gains**: Table 4 shows RC-only gives +1.50 and TC-only gives +1.05 vs +1.88 with both, meaning the framework with one component already attains a large fraction of the gain. The phrase "individually provides marginal gains" understates this.
- **Eq. (3) positional embeddings are underspecified**: The paper says "new positional embeddings $E_{pos}^i$" are added to the packed subsequence, but does not say whether these are fresh indexed-by-pack-order embeddings (destroying original position) or re-use original positions. This affects how attention behaves in the nested pass and is reproducibility-relevant.
- **Eq. (4) gating not clamped**: The learnable $\beta \cdot p^i$ is presented as a convex-combination weight, but is not constrained to [0,1] when $\beta$ is learnable. A brief note on clamping or empirical range would clarify.
- **Score Dispersion Loss is internally tense with Distribution Preservation**: §3.2.1 normalizes per-sequence routing scores into a distribution then maximizes entropy (pushing toward *uniform*, i.e., least discriminative), while simultaneously the MSE-to-0.5 loss compresses scores toward the midpoint. The paper does not argue analytically why this push-pull yields the claimed discriminability; Figure 6b is the only evidence.

### Trivial
- §4.5/Fig. 7b's GPQA single example is presented as evidence for "hierarchical processing." This is fine as illustration but should be framed as an anecdote, not a "phenomenon."
- §4.3 reports the SFT data only as "1-2 million instances" of "synthetic material built upon a high-quality seed set." Brief in-paper detail about LR schedule, training steps, and whether DND and the baseline shared identical schedules would help rule out incidental training-time confounds (details are deferred to appendix).

## Nice-to-Haves
- Run ≥3 seeds on the main tables, even on a subset of benchmarks, to give error bars to the headline numbers.
- Add a compute-matched plain-SFT baseline (extra steps or extra data sized to match DND's added FLOPs) to attribute gains to selective routing rather than extra compute.
- Add a MOR-style routing variant in the same post-training setting (same data, same base) to isolate the contribution of DND's control machinery.
- Extend the scale curve to a 7B / 14B model so the trend from +2.5 (1B) to +0.87 (30B) can be interpreted as either monotone decline or a non-monotone shape.
- Quantitative breakdown of selected token *types* (entities/operators/punctuation/answer tokens) per layer to substantiate the "hierarchical processing" claim beyond one qualitative card.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh critic's "missing benchmarks for small dense models in some tables"* — Table 1 already lists 11 benchmarks; the paper's reporting choice is reasonable and the asymmetry across model rows is not severe enough to be a substantive complaint.
- *Strength Finder's "successful scaling to 30B"* — kept in modified form as the architectural-transfer point; removed the framing that emphasizes "largest gains on BFCL/LCB" as a strength, because the same table shows several near-zero gains that the strength finder elides.
- *Strength Finder's "post-training applicability"* — generic capability claim that does not add evidence beyond the consistent-gains strength.
- *Harsh critic's "Table 3 throughput slightly worse than FLOPs suggest"* — true but minor (1–2 percentage-point gap likely from pack/unpack), not a substantive critique.

## Novel Insights
None beyond the paper's own contributions. The most useful conceptual reframing — that DND is best understood as a per-token weight-tied two-step refinement whose contribution is its training-control machinery rather than its architectural template — is implicit in the paper but not stated; this would be a meaningful framing change in any revision.

## Suggestions
- Re-frame contributions to center the training-control machinery (router controlling loss + buffer proportional + EMA threshold control) as the primary advance, with the architecture as a vehicle to demonstrate it.
- Add error bars / seed reporting on at least Tables 1 and 4; even three seeds on Qwen3-1.7B would change the believability of the +5-point swings on BBH and GPQA-Diamond.
- Add a compute-matched plain-SFT baseline column to Tables 1 and 2.
- Clarify Eq. (3) positional-embedding semantics and Eq. (4) clamping behavior in one or two sentences.
- Either show DND gains remain stable or grow at mid-scale (7B/14B), or explicitly acknowledge diminishing returns at 30B and discuss why.

---

## Axis evaluation

- **Originality**: Moderate. The architectural template (weight-tied per-token re-application with router) is closely adjacent to MOR/ITT; the genuinely novel pieces are the dispersion+preservation router loss and the buffer-proportional + EMA threshold control. These are real but narrow.
- **Importance of the research question**: Reasonable — token-adaptive computation for off-the-shelf LLMs in the post-training setting is a practical and live question.
- **Whether the claims are well supported**: Partly. Small-dense gains are plausibly real; the 30B claim is on shaky ground without variance estimates or a compute-matched baseline.
- **Soundness of experiments**: Adequate scope across benchmarks but lacking on seeds, compute-matched baselines, and same-setting comparison to the closest competitor.
- **Clarity of writing**: Generally clear; the architecture and training-control sections are readable. Some terse spots (Eq. (3), gating clamp).
- **Value to the research community**: Modest but real — the control machinery is a genuinely useful piece of engineering for anyone training a token-choice router in a post-training setting.

## Score and Decision

**Anchors retrieved**:

Round 1 (bracketing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7DY2DFDT0T.md` (EfficientSkip, 2.50, weak band) — adaptive token skipping converting dense to sparse; less ambitious eval than DND.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ulGwcj1egv.md` (FiRST, 3.00, weak band) — input-adaptive layer skipping; read in full. Far weaker eval (1 base model, 2 tasks). DND is clearly better.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/762u1p9dgg.md` (MOEfication by Experts as Masks, 3.40, weak band) — sparsification with masks; similar territory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I1VCj1l1Zn.md` (DLP-LoRA, 3.00, weak band) — dynamic LoRA fusion; different problem.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Pu3c0209cx.md` (Tight Clusters Make Specialized Experts, 7.00, mid band) — MoE routing optimization; more principled formulation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8sSqNntaMr.md` (RouteLLM, 6.33, mid band) — model routing; different problem framing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6qUUgw9bAZ.md` (Learning How Hard to Think, 6.50, mid band) — input-adaptive decoding compute allocation; conceptually related.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HmwneoGoy9.md` (SeerAttention, 5.25, mid band) — learning sparse attention; comparable engineering scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/t7P5BUKcYv.md` (MoE++, 8.00, strong band) — heterogeneous MoE with zero-computation experts; substantially stronger work.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OfjIlbelrT.md` (FlexPrefill, 8.00, strong band) — context-aware sparse attention; substantially stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EytBpUGB1Z.md` (Retrieval Head, 8.00, strong band) — mechanistic study; different category.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xXTkbTBmqq.md` (OLMoE, 8.67, strong band) — full open MoE release; different scope.

Round 1 bracket: **4.0 – 6.0** — clearly stronger than FiRST/EfficientSkip (which are very thin), but visibly less polished than MoE++/FlexPrefill (8.0) and not as analytically clean as Tight Clusters/RouteLLM (6.3–7.0).

Round 2 (narrowing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LyNsMNNLjY.md` (LLM Routing with Benchmark Datasets, 4.25) — different topic but similar maturity to weaker side.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rgDwRdMwoS.md` (Unified Routing and Cascading, 5.20) — broader claims with mixed eval; comparable territory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0gVatTOgEv.md` (Glider, 4.00) — expert-router for MoErging; weaker than DND.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9tMzqRaEL3.md` (LLMs Capture Domain Knowledge, 4.50) — different topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mb2ryuZ3wz.md` (How many tokens is an image worth?, 5.75) — different domain.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eWNEqdH0vk.md` (Layerwise Recurrent Router for MoE, 5.75) — read in full. Closely analogous: routing improvement with consistent-but-small gains, similar reviewer concern about scale and modest improvements. DND has broader eval (4 base models, 30B MoE), but worse rigor on seeds/baselines. Net: roughly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BgYbk6ZmeX.md` (Repurposing Diffusion Models, 6.00) — different domain.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/d7q9IGj2p0.md` (Morphing Tokens for MIM, 6.67) — different domain.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bcHty5VvkQ.md` (SkipDecode, 5.50) — autoregressive skip decoding with batching; comparable scope, just under accept threshold.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EzrZX9bd4G.md` (BEEM Early Exit, 6.25) — early-exit with ensembling; cleaner conceptual story.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SfNmgDqeEa.md` (Looking Beyond Top-1, 6.40) — analytical work.

Round 2 narrows to **4.5 – 5.75**. DND is broader than FiRST and SkipDecode, but the 30B-MoE scaling story is the headline and it does not survive scrutiny without variance estimates or compute-matched baselines. The training-control machinery is genuinely useful — that and broad eval keep it above pure-reject territory. Most directly comparable: RMoE (5.75, accept-borderline) and SkipDecode (5.50, reject-borderline). DND has broader empirical scope than both but weaker per-gain rigor than RMoE. I place it slightly below RMoE: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>