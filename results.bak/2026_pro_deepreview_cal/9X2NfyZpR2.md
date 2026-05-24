Now I have a thorough understanding of the paper and calibration anchors. Let me compile the final review.

---

## Summary

This paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts — ordered action lists without timing or duration — eliminating the need for costly frame-level annotations. The architecture combines a temporal alignment module (ATBA) for pseudo-label generation, cross-modal attention with local masking to ground video features in transcript semantics, and a suite of complementary losses (CTC, CRF, duration) to enforce temporal coherence. Evaluated on Breakfast, 50Salads, and EGTEA, TbLTA establishes the first transcript-only baseline for LTA and achieves competitive results with fully supervised methods on Breakfast, while showing a clear gap on 50Salads.

## Strengths

- **Genuinely novel contribution**: This is the first framework to train a dense LTA model using only video transcripts without any frame-level temporal annotations. Opening a new weakly-supervised paradigm for a task that has been exclusively fully supervised is a meaningful contribution to the field (Section 1, lines 20-23).

- **Well-designed architecture with multiple complementary components**: The cross-modal attention with local masking (Eqs. 1–2) that restricts transcript embeddings to temporally relevant video segments is a thoughtful design. The combination of CTC loss for global transcript consistency, CRF loss for long-horizon coherence, and a self-supervised duration loss — each with a distinct role — shows careful engineering. The ablation study (Tables 3–4) confirms that removing any component degrades performance, with cross-attention removal causing drops of ~5.7 points on Breakfast and ~1.3 on 50Salads.

- **Strong results on Breakfast at 30% observation**: TbLTA's deterministic model achieves an average MoC of 29.03 at 30% observation on Breakfast, surpassing all fully supervised baselines including ActFusion (28.45) and FUTR (26.59). This directly demonstrates that transcript-only supervision can rival dense frame-level labels when procedural structure is strong (Table 1).

- **Multi-benchmark evaluation**: The paper reports results on three datasets (Breakfast, 50Salads, EGTEA) with different characteristics, establishing a consistent weak-supervision baseline and showing that transcripts help mitigate class imbalance on rare categories in EGTEA (Table 2).

## Weaknesses

### Fatal

None.

### Major

- **Deterministic and stochastic results conflated in the main comparison table**: Table 1 places deterministic supervised baselines alongside both deterministic and stochastic TbLTA results in the same visual grouping, with only an asterisk footnote to distinguish them. This makes it easy for a reader to mistakenly compare stochastic TbLTA numbers (e.g., 28.51 average on 50Salads) against the deterministic supervised baselines (24.15–28.39), creating the impression that the gap on 50Salads is largely closed when it is not — the deterministic TbLTA achieves only 20.92. The paper does mark the distinction, but the presentation obscures rather than clarifies the primary empirical claim. The deterministic results should be visually separated from stochastic ones, and the text should more clearly foreground which numbers support which claims.

- **Ablation study conducted exclusively in stochastic (Top-1) mode**: The ablation study (Tables 3–4) that validates every architectural component — CTC, cross-attention, CRF, duration loss — is performed using only the stochastic Top-1 MoC metric. However, the paper's primary comparison to fully supervised methods (the central claim of competitiveness) uses the deterministic MoC metric. Since the stochastic evaluation selects the best among multiple sampled futures, it is a more forgiving metric, and the ablation patterns observed there may not transfer to the deterministic mode at the same magnitude. The paper states this choice explicitly ("For clarity, we adopt this choice Top-1 MoC for ablations as it provides a stable reference point," line 235) but does not discuss whether the same patterns hold under the deterministic protocol that anchors the main claims.

### Minor

- **Abstract and conclusion language overstates the empirical evidence**: The abstract claims transcript-based supervision offers "a very robust and less costly alternative to its fully supervised counterpart," and the conclusion states results are "competitive with, and in certain settings even superior to, fully supervised methods." While true for Breakfast (especially at 30% observation), the deterministic gap on 50Salads is 3–7 points below all supervised baselines. The body text acknowledges 50Salads limitations, but the framing in the abstract and conclusion does not reflect this mixed picture. The qualifier "in certain settings" in the conclusion helps but is easily read as a throwaway.

- **EGTEA evaluation lacks horizon-wise breakdown**: Table 2 reports only a single aggregated mAP number per category (All, Freq, Rare) with no breakdown by observation horizon (25%, 50%, 75%). The paper mentions that supervised models "retain a clear edge overall" on EGTEA, but without horizon-wise numbers, a reader cannot assess whether the gap widens or narrows at different observation levels, making the evaluation too thin to support substantive claims about this dataset.

- **"Stochastic variant" claim in Related Work is misleading**: The paper states "we propose a stochastic variant that explicitly captures the uncertainty inherent in LTA predictions" (lines 99–100) in reference to Maté & Dimecicoli (2024)'s CRF approach. However, TbLTA's model architecture is deterministic — the stochasticity comes from the evaluation protocol (Abu Farha & Gall, 2019) that samples multiple trajectories, not from a model-level design choice. This conflates model design with evaluation procedure and should be corrected.

- **Limited analysis of 50Salads performance gap**: The paper attributes the 50Salads deterministic gap (20.92 vs. 24.15–28.39) to "weaker temporal regularities" and "imprecise temporal alignment" (line 231), but does not investigate whether the bottleneck is the ATBA alignment module, the cross-attention quality, or the decoder's ability to handle denser action distributions. A brief diagnostic analysis would strengthen the contribution and help future work.

### Trivial

- None of substance.

## Nice-to-Haves

- A simple transcript-only baseline (e.g., uniform partitioning of the transcript into fixed-length segments) would contextualize the many architectural components and show what the bare-minimum transcript signal provides.
- Reporting the ablation study under the deterministic protocol (or showing a subset of ablations in both modes) would directly link component contributions to the primary evaluation standard.
- A post-mortem analysis of worst-case deterministic predictions on 50Salads, diagnosing whether errors stem from alignment failures, sequence incoherence, or duration misestimates.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The stochastic evaluation protocol is underspecified and must be described in the main paper"**: The paper cites Abu Farha & Gall (2019) for the stochastic protocol and notes details are in the supplementary. Per the hard rules, weaknesses about appendix-deferred content are removed. The core valid concern — the conflation of deterministic and stochastic results — is retained above as a Major weakness about presentation, not about missing protocol details.

- **"The ATBA module's training and inference details... are essential for understanding the main pipeline and should be summarised in the methods section"**: ATBA is a published method (Xu & Zheng, 2024) and the paper adequately describes its role. Requiring full details of a cited external module in the main text is scope creep. The paper summarizes what ATBA provides (soft pseudo-labels that preserve boundary uncertainty) which is sufficient.

- **Demand for a "transcript-only baseline" as a missing critical baseline**: This is a nice-to-have, not a weakness. The paper's comparison is against (semi-)weakly supervised baselines (Zhang et al., 2021) and fully supervised methods, which is the appropriate comparison set. A uniform-partition baseline would add context but its absence does not invalidate any claims.

- **"The introduction presents the contribution as a general advance, but the experiments show that the approach works well only under specific structural conditions"**: This is partially addressed in the paper — the Breakfast results show transcript-only LTA works well for structured procedural activities, and the 50Salads results are honestly discussed as a limitation. The concern is retained in milder form (abstract/conclusion overclaiming, Minor).

## Novel Insights

The merger process surfaces an important calibration point for this line of work: the effectiveness of transcript-only supervision for LTA appears tightly coupled to the strength of procedural temporal regularities in the activity. On Breakfast — where activities follow stereotyped sequences (e.g., making cereal, frying an egg) — transcripts provide enough structure to rival full supervision. On 50Salads — where actions are denser, transitions more frequent, and ordering more flexible — the same supervision signal degrades substantially. This suggests that future transcript-based LTA methods may need dataset-specific strategies (e.g., stronger duration priors or multi-hypothesis outputs) rather than a one-size-fits-all architecture. None of the individual reviews explicitly connected this pattern to a design principle, but it emerges clearly from the cross-dataset evidence.

## Suggestions

- Visually separate deterministic and stochastic results in Table 1 (e.g., with a horizontal rule or distinct sub-tables) and foreground the deterministic numbers in the text since they are the primary basis for comparison with supervised methods.
- Either report key ablation rows under the deterministic protocol or add a brief justification for why the Top-1 patterns are expected to transfer to the deterministic setting.
- Tone down the abstract and conclusion: replace "very robust" with something like "a viable and less costly alternative" and explicitly note the 50Salads gap as a limitation in the abstract.
- Correct the "stochastic variant" wording in Related Work to clarify that the stochasticity comes from the evaluation protocol, not the model architecture.

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Avg Score | Round | Comparison to TbLTA |
|--------|-----------|-------|---------------------|
| Weakly Supervised Video Scene Graph (VSNLS) — GQgPj1H4pO | 6.00 | R2 | Similar: opens a new weakly-supervised paradigm for a video task, but TbLTA has stronger architectural contributions and more significant evaluation presentation issues |
| AntGPT — Bb21JPnhhr | 6.25 | R2 | Better: cleaner SOTA results across benchmarks, thorough experiments; TbLTA has higher novelty (first transcript-only) but weaker empirical validation |
| Action Sequence Augmentation — f3CdjpPkSq | 6.50 | R2 | Better: consistent improvements across models/datasets, cleaner empirical story; TbLTA is more ambitious but has mixed results and evaluation issues |
| Interaction-based TAS — sEARCNzhrP | 5.00 | R2 | Worse: narrower contribution, limited novelty; TbLTA has clearly stronger novelty and broader evaluation |
| Weakly Supervised Skilled Activity — HCoSsULNxG | 4.75 | R2 | Worse: less ambitious contribution; TbLTA has stronger novelty and more thorough methodology |

**Round 1 bracket**: 4.5–7.0

**Round 2 narrowing**: The paper lands between VSNLS (6.00) and Interaction-based TAS (5.00). The genuine novelty of being first to enable transcript-only LTA and the thoughtful architectural design pull it above 5.00. But the evaluation issues — particularly the deterministic/stochastic conflation in Table 1 and the ablation conducted only in stochastic mode — pull it below the cleaner 6.00-level papers. The paper's core contribution is solid and the weaknesses are addressable in revision, but they meaningfully weaken the empirical story as presented.

**Final score**: 5.5. The contribution is real and the weaknesses are fixable, but the evaluation presentation issues need substantive revision before the empirical claims can be fully trusted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>