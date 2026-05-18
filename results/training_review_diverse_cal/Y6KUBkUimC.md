Here is my consolidated review.

---

## Summary

This paper introduces a cost-effective, fully synthetic pipeline for creating ranked preference datasets for text-to-image alignment, and proposes RankDPO, a ranking-enhanced DPO loss that weights pairwise comparisons with DCG-based gains from the multi-image ranking. The method replaces expensive human annotation with off-the-shelf T2I models for generation and pre-trained reward models for labeling, then fine-tunes SDXL and SD3-Medium to achieve state-of-the-art results on DPG-Bench, GenEval, and T2I-Compbench while using ~3× fewer training images than Pick-a-Picv2.

## Strengths

1. **Fully synthetic preference annotation pipeline dramatically reduces cost and enables scalability.** Section 3.2 reports that collecting a dataset comparable to Pick-a-Picv2 (≈$50K human annotation cost) can be done for ≈$200 by using off-the-shelf T2I models for generation and pre-trained reward models for labeling, with no human annotation in the loop. This directly supports the claim of a scalable, cost-effective alternative to human-annotated datasets.

2. **RankDPO consistently outperforms pairwise DPO and other preference optimization variants.** The ablation study (Tab. 4 / §4.2) shows that RankDPO achieves the best DSG (79.26) and Q-Align (0.81) on DPG-Bench compared to DPO with gain weighting (78.12 DSG, 0.79 Q-Align), supervised fine-tuning, and weighted fine-tuning baselines. This demonstrates that incorporating DCG-weighted ranking feedback provides a richer training signal than pairwise comparisons alone.

3. **Achieves state-of-the-art results on multiple benchmarks while using fewer images than prior work.** On DPG-Bench (Tab. 3), RankDPO-SDXL obtains a DSG of 79.26 and Q-Align of 0.81, surpassing DPO-SDXL (76.85, 0.76) and MaPO-SDXL (78.32, 0.80). On GenEval (Tab. 1), SDXL improves from 0.55 → 0.61 and SD3-Medium from 0.70 → 0.74. The paper notes these results use ~3× fewer images than Pick-a-Picv2.

4. **Improves models that have already undergone human-preference DPO training.** SD3-Medium, described as "already optimized with 3M human preferences through DPO," shows significant further gains after RankDPO fine-tuning on all benchmarks (Tabs. 1–3). This indicates the synthetic ranked dataset provides complementary value beyond existing human-labeled data.

5. **Ablation studies demonstrate the value of ensembling multiple reward models and using diverse generator models.** Table 4 shows that ensembling 5 reward models outperforms using only HPSv2.1 (79.26 vs. 78.51 DSG), and using images from four different T2I models improves visual quality compared to using only SDXL variants (0.81 vs. 0.78 Q-Align). These ablation results provide empirical support for the paper's design choices.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence, and no methodological flaw invalidates the results.

### Minor

1. **Notational ambiguity in the RankDPO loss (Eq. 13).** The sum runs over "i > j" with the term log σ(-β(s_i - s_j)). The paper states (line 111) that images are indexed in "ranked order of preference" and "we want to ensure that the denoising for image x^i is better than x^j for all i > j." However, it is not fully explicit about whether i > j refers to (a) the numeric index (which would need to match the preference ordering) or (b) a preference relation defined separately via τ(i). If the dataset's images are indexed 1…k in descending preference order (x^1 = best), then the condition "i > j" in the summation uses numeric indices that run opposite to preference ordering, creating notational tension. The loss as implemented clearly works (empirical results confirm this), and the intended meaning is recoverable from context, but the derivation would benefit from an explicit statement such as "where indices i, j are ordered by ground-truth rank, so that τ(i) < τ(j)."

2. **The comparison against prior DPO work conflates better generators with better preference signals.** The main results compare RankDPO (trained on images from SDXL, SD3-Medium, Pixart-Σ, and Stable Cascade) against DPO-SDXL trained on Pick-a-Picv2 images (older, 512² resolution). The SDXL-only ablation (§4.2, "using SDXL images by only varying the seed") partially addresses this, showing that prompt-alignment gains persist but visual-quality gains are smaller with a single generator. The paper's narrative could more clearly decompose the improvement into (i) higher-quality generators, (ii) synthetic labeling, and (iii) ranking-based loss — currently the reader must infer this from the ablation.

3. **User study is underspecified.** Section 4.1 reports win rates on 450 prompts from DPG-Bench but omits the number of participants, the number of judgments per prompt, and any measure of inter-rater agreement. Given that the user study is presented as central evidence for visual quality improvement, more detail is needed to establish reliability.

4. **Missing analysis of reward-model agreement and ensembling.** Five reward models are ensembled via pairwise win aggregation (§3.2), but the paper does not report: (i) agreement among the five models, (ii) variance of the aggregated scores, or (iii) a comparison of the ensemble against the best single reward model (beyond the HPSv2.1-only ablation). Such analysis would help assess the robustness of the synthetic labeling and justify the additional complexity of using five models.

5. **The ranking-specific advantage over weighted pairwise DPO is modest and may partially undercut the claimed novelty of the ranking objective.** The ablation (Tab. 4) shows RankDPO outperforms "DPO + Gain Function Weighting" by a small margin (the paper's text reports different baselines yielding margins of roughly 1–2 DSG points). With only k=4 images per prompt, the ranking provides at most 6 distinct pairwise weight values, and many pairs receive minimal weights. An experiment varying the list size (2, 4, 8) would directly test whether the ranking component adds meaningful information beyond pairwise signals. Without this, the paper's claim that rankings provide "richer signal" is plausible but not strongly quantified.

### Trivial

1. **Timestep sampling distribution is not specified.** The paper states "t ∼ [0,T]" and "randomly sample a timestep" in practice (Eq. 11, line 86) but does not specify whether this is uniform over [0,T] or truncated (e.g., [0.1, 0.9] as used in Diffusion-DPO). The choice affects training dynamics and is needed for reproducibility.

2. **The cost comparison (§200 vs. §50K) lacks a breakdown.** While the headline comparison is compelling, the paper does not detail what the §200 covers (e.g., API calls for generation, GPU time for reward models) or how it scales with dataset size, which would strengthen the claim's credibility.

## Nice-to-Haves

- **Precise specification of the paired-ordering in Eq. 13**, e.g., "where indices i and j are ordered by ground-truth rank, so that τ(i) < τ(j)."
- **Vary the number of images per prompt** (e.g., 2, 4, 8) to directly quantify the value of longer rankings vs. pairwise preferences.
- **Disentangle generator quality from synthetic labeling** by either (a) training DPO on human preferences for the same newer images, or (b) training RankDPO on Pick-a-Picv2's original images with synthetic labels to isolate the labeling method's contribution.
- **Report training loss curves or validation metrics** to demonstrate convergence, especially given only 400 training steps.
- **Add a filtering step** to discard prompts where the five reward models disagree strongly, which might further improve results.

## Removed Points

- The Harsh Critic's speculation that "roughly half the terms would have the wrong preference direction" if indices follow dataset ordering — the paper defines i > j as preference ordering (line 111), so this hypothetical does not apply to the paper's actual formulation. The underlying clarity concern is retained in Minor weakness #1.
- The "Strengthening the Paper on Its Own Terms" suggestions are absorbed into Nice-to-Haves where they do not affect the accept/reject judgment.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern in DPO-for-T2I papers: the difficulty of cleanly attributing empirical gains to specific components (generator quality, synthetic labeling, objective design) when all are changed simultaneously. This paper's SDXL-only ablation attempts this decomposition but could go further.

## Suggestions

1. Add one sentence to Eq. 13's definition clarifying that i > j means τ(i) < τ(j) (i is preferred over j) to eliminate notational ambiguity.
2. Expand the ablation section with a clearer statement attributing improvement sources: "Gains come from three factors: (A) better generator outputs, (B) synthetic multi-reward labeling, and (C) the ranking loss. Our ablations in Table 4 isolate (C), while the SDXL-only experiment partially isolates (A) vs. (B)."
3. Add participant counts and inter-rater agreement to the user study section.
4. Report pairwise agreement among the five reward models (e.g., average Spearman ρ) to help readers assess synthetic label quality.
5. Specify the timestep sampling distribution (uniform over [0,T] or truncated) in the implementation details.

## Score and Decision

**Originality:** The synthetic preference pipeline for T2I alignment is practically novel and timely, though it adapts ideas explored in LLMs (RLAIF). The RankDPO loss is a straightforward adaptation of LambdaLoss/LiPO to the diffusion setting.

**Importance of research question:** High. The cost of human preference annotation is a real bottleneck for T2I alignment, and a scalable synthetic alternative has clear practical value.

**Claims support:** The central claims are well-supported by extensive benchmarks (GenEval, T2I-Compbench, DPG-Bench) and ablations. The user study provides auxiliary support but lacks detail.

**Soundness of experiments:** Sound overall. The ablations are well-designed to isolate data labeling, model diversity, and objective choice. The main confound (generator quality vs. labeling method) is partially addressed but could be clearer.

**Clarity of writing:** Generally clear, but the notational ambiguity in Eq. 13 and the framing of improvement sources could be improved.

**Value to the community:** High. The synthetic data pipeline is reproducible, cost-effective, and could become a standard practice for DPO-based T2I alignment.

This is a solid paper with a practical contribution. The weaknesses are all addressable (clarity, missing details) and do not threaten the core claims. The synthetic pipeline is the standout contribution; the ranking objective provides incremental improvement on top.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>