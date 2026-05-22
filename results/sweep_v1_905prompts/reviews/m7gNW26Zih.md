Now I have sufficient calibration. Let me write the final review.

## Summary

This paper proposes a dual-encoder system for language-based audio retrieval combining three techniques: (1) soft-label distillation from an ensemble of retrieval teachers (adopted from Primus et al., 2024, the top DCASE 2024 Task 8 system), (2) LLM-based caption augmentation via back-translation and mixing, and (3) cluster-guided auxiliary classification. On the CLOTHO dataset, the best single model (PaSST with distillation) achieves mAP@16 of 46.6, and a weighted ensemble reaches 48.8 on the development test split.

## Strengths

- **Systematic ablation across three backbones and five configurations**: Table 2 cleanly disentangles the effect of distillation, augmentation, and two clustering sources on PaSST, EAT, and BEATs, enabling the reader to see which components matter for which backbone.

- **Distillation alone produces a clear, reproducible gain**: Moving from SID 1 (no distillation) to SID 2 (distillation) improves PaSST mAP@16 from 42.08 to 46.62, with similar gains for EAT and BEATs. This is concretely measured and replicated across architectures.

- **The ensemble analysis (E1–E4) is methodical**: The paper reports system-level and model-level weighting strategies with validation-set grid-search weights shown in Table 3, providing a clear recipe for combining the trained models.

## Weaknesses

### Major

1. **The paper's strongest technique is adopted from prior work, and the novel components show marginal or inconsistent evidence.** Section 2.2 states the distillation loss is directly adopted from Primus et al. (2024). Table 2 shows this adopted technique drives almost all of the performance gain (PaSST: +4.54 mAP@16 from SID 1→2). The two components claimed as novel contributions—LLM augmentation and cluster-guided classification—show negligible or inconsistent effects for the best backbone (PaSST: SID 2 at 46.62 → SID 3 at 46.41 → SID 4 at 46.39 → SID 5 at 46.50, all within ±0.2 points). For EAT and BEATs, augmentation gives a small ~0.7–0.8 mAP@16 bump, but cluster guidance is flat. The paper's contribution listing places "soft-label distillation" first, creating a misalignment between framing and actual novelty.

2. **Unsubstantiated claim about cluster guidance.** The abstract states: "ablations indicate consistent improvements under high correspondence ambiguity." No such analysis appears in the paper — there is no split of the test set by caption ambiguity, no qualitative cluster examples, no evidence that the clustering captures non-binary correspondences. For the best backbone (PaSST), the cluster configurations (SID 4, 5) are statistically indistinguishable from SID 2 or 3. This claim is not supported by any presented evidence.

3. **No comparison to published state-of-the-art results on CLOTHO.** The paper reports results only against its own internal configurations (SID 1–5). It does not cite or compare to any prior published retrieval scores on CLOTHO (e.g., from DCASE Task 8 leaderboards, Primus et al. 2024, or earlier work). Without this context, the reader cannot assess whether the proposed system advances the state of the art. The ensemble's 48.83 mAP@16 may be strong or merely competitive — the paper provides no way to judge.

4. **Overclaimed contribution scope.** The Introduction promises "thorough ablations on topic granularity and teacher softness." The paper contains no such ablations: there is only one temperature (τ=0.05), and cluster granularity is varied by only two sources (finetuned vs. BERTopic) without any analysis of cluster count, quality, or the effect of different granularities. The contribution bullet "Soft-label distillation that targets non-binary audio-caption correspondences" similarly implies novelty when the method is directly adopted from prior work.

### Minor

1. **Inconsistent final evaluation reporting.** The development test results are reported as percentages (e.g., mAP@16 of 46.62), while the evaluation set result is reported as a decimal (mAP@16 of 0.421). This 0.421 (= 42.1%) represents a ~6.7 point drop from the ensemble's dev test performance (48.83), but the paper offers no explanation for this gap.

2. **No statistical uncertainty.** All results in Table 2 appear to be single runs without confidence intervals or variance estimates. Given that the differences between SID 2–5 are small (<1 mAP@16), readers cannot assess whether these differences are meaningful.

3. **Augmentation counts not fully reported.** The paper states 50,000 pairs were created via LLM mix but does not report how many back-translation captions were generated, nor provides any quality analysis (human evaluation or semantic similarity checks) of the augmented captions.

### Trivial

- Section 2.2 attributes the distillation to "Primus et al., 2024" but does not discuss whether or how the present work modifies the original formulation beyond the citation.

## Nice-to-Haves

- **Isolate augmentation and cluster guidance without distillation.** SID 1 removes all three components; SID 2 adds only distillation; SIDs 3–5 add augmentation and cluster on top of distillation. An ablation with augmentation (or cluster) alone — without distillation — would clarify their independent contributions.
- **Include prior CLOTHO results** as a reference row in Table 2 (e.g., from Primus et al. 2024 or DCASE challenge entries).
- **Report clustering hyperparameters** (UMAP dimensions, HDBSCAN min_cluster_size) for reproducibility.

## Removed Points

- *Reproducibility concern with GPT-4o as a proprietary API model.* The paper acknowledges this limitation, and using API-based LLMs for data augmentation is standard practice in current NLP/audio research. This is a limitation but not a weakness specific to this paper's evaluation.
- *Unfair comparison criticism about asymmetry favoring baselines.* The critic's framing does not apply here since both the paper's systems and baselines share the same training setup.
- *Missing references to [5, 18] for e5-large-v2.* These are appendix references; the parser strips appendix sections.
- *Criticism about undisclosed hyperparameters.* Batch size and learning rate ranges are reported; per-configuration values for all three stages are provided.
- *Missing related work.* The reviewer lacks external sources to confirm omissions; this is excluded per hard rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a row to Table 2 reporting the best published CLOTHO results from prior work (including Primus et al. 2024) so readers can contextualize the proposed system's performance.
2. Either remove or substantiate the abstract's claim about "consistent improvements under high correspondence ambiguity" with actual analysis (e.g., split the test set by caption entropy or cluster size).
3. Remove the promised "thorough ablations on topic granularity and teacher softness" from the contributions list or add those ablations.
4. Add confidence intervals or multiple-seed runs to Table 2, especially for distinguishing SID 2–5 where differences are marginal.
5. Clarify the evaluation set result (0.421) by reporting it in the same format as the dev test results and explaining the performance drop.

## Score and Decision

**Bracketing (Round 1):** Low-anchor queries (score < 3.5) returned audio papers with avg scores 3.0–3.25 (all reject). High-anchor queries (score > 7.5) returned papers avg 8.0–8.5 (all accept). Middle queries (3.5–7.5) returned avg scores 3.67–6.75 (mixed). The paper's limited novel contribution and weak evidence situates it well below the 6.67 accept-range anchors and near the 4.0–5.5 range.

**Narrowing (Round 2):** Targeted queries in (3.5, 5.5) and (4.0, 5.5) returned anchors with avg scores 4.25–5.25 (all reject). The paper at hand is comparable to the 4.25–4.67 anchors (e.g., "Granularity Matters" at 4.25, "Adder" at 4.67) — these papers have a reasonable idea but the evidence for their claimed contributions is insufficient or the primary technical content is not novel. However, the paper has slightly stronger experimental breadth (3 backbones, 5 SIDs, ensembles) than the weakest of these anchors, placing it at the upper edge of this band.

**Anchors consulted:** mlPTNEIsgb (3.25), TDzAqTqDHV (3.00), 2y8XnaIiB8 (5.50), 4N97bz1sP6 (6.67), bfRDhzG3vn (5.75), qqExiDNsa7 (5.00), n3kFlvVhJM (4.67), BLvCdxAi8W (4.25), Pa6SiS66p0 (4.33), XPQCiLY45j (5.00), i3tBySZWrR (4.60), lidVssyB7G (5.25), JVeM7uwDwK (5.25).

The paper presents a systematic experimental framework but its primary effective component is adopted from prior work, its novel components show marginal evidence, and it overclaims in multiple places (unsupported cluster-guidance claim, missing ablations). These issues are major but not fatal — the method is sound and the experiments are reproducible. The appropriate score is 4.5.

<score>4.5</score>
<decision>Reject</decision>