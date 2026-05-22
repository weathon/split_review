Now I have all the information I need. Let me compile the final review.

## Summary

This paper identifies and corrects three genuine methodological flaws in the emerging protocol of online-map-based motion prediction: (1) a train–validation gap caused by using overlapping data splits for two-stage training, (2) misaligned perception ranges between online mapping models (limited to ~30×60m) and motion prediction (agents >100m away), and (3) non-discriminative metrics that report only ego-vehicle results and include trivial static agents. The authors propose OMMP-Bench with a spatially disjoint three-way data split (map train / motion train / motion val), refined metrics that evaluate moving non-ego agents separately for close and far ranges, and a boundary-free baseline that uses raw image features (via deformable attention) to supplement missing map context for distant agents. Controlled experiments demonstrate that the new split eliminates the train–val gap, that the refined metrics are substantially more discriminative, and that image features meaningfully improve far-agent prediction.

## Strengths

1. **Identifies genuinely consequential methodological confounds in an emerging protocol.** The train–val gap is real and clearly demonstrated: under the default split, map accuracy for motion-prediction training data (87.6 mAP) far exceeds that for evaluation data (50.3 mAP), creating a distribution shift that the proposed split eliminates (48.9 vs. 50.3 mAP, Table 1 / Fig. 3). This is a concrete, verifiable problem that the community should fix.

2. **The new data split and refined metrics demonstrably change evaluation conclusions.** Table 1 shows that the default split yields 0.6839 minADE whereas the proposed split yields 0.6308 minADE — a material difference. Table 6 shows static agents are trivially easy (minADE 0.002) and that including them makes metrics artificially low, while Table 7 separately reveals that far agents are substantially harder than close ones. This makes the benchmark genuinely more informative than the prior protocol.

3. **Comprehensive evaluation across multiple model combinations.** Table 7 evaluates 2 map models × 2 motion models × 4 variants = 16 configurations across three agent groups, producing 48 metric entries. This thoroughness enables reliable conclusions (e.g., that methods improving ego prediction do not always generalize to non-ego agents) and provides a solid reference for future work.

4. **The boundary-free image-feature baseline is a practical demonstration of the benchmark's utility.** The img variant consistently improves minADE for far agents across all model combinations (e.g., 0.6999→0.6274 for MapTRv2-CL+HiVT), concretely showing that the misaligned-perception-range problem can be addressed once it is properly measured.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or confidence intervals reported.** The motion validation set contains only 86 scenes, so single-point estimates could be sensitive to the specific split. While single-run evaluation is common in this subarea, the paper should explicitly state whether the benchmark is deterministic (or report variability). This does not invalidate the findings but matters for reproducibility.

2. **Missing explanation of excluded scenes.** The paper states the split contains 367 + 397 + 86 = 850 scenes, but nuScenes has 1000 total (700/150/150). It is unclear whether 150 scenes were excluded and, if so, why. A brief clarification is needed.

3. **Wording inconsistency about ego-vehicle evaluation.** Section 3.4 states the paper proposes "to only evaluate non-ego agents," yet Table 7 reports Ego results alongside non-ego results. The underlying scheme (evaluate all moving agents including ego, with emphasis on non-ego) is clear, but the text should be tightened to avoid confusion.

4. **No offline GT-map comparison under the new split.** The paper motivates the benchmark by arguing that online maps introduce errors, but never shows what performance would be with ground-truth maps on the same split. A single GT-map row in Table 7 would let readers quantify the remaining gap from online maps. (This is not required for the benchmark's validity but would strengthen it.)

### Trivial

- The claim that "Applied the method on the MapTRv2-CL+HiVT model, the minADE decreased by 12.7%" (Section 4.2) computes to ~10.4% from the Table 7 numbers; 12.7% matches the DenseTNT combination instead. Small numerical mismatch in the text.
- Table 5 shows two identical-looking rows (Boundary only) with different minADE values — likely a formatting artifact, but the authors should verify.
- "Close" vs. "far" is defined only indirectly (within the 30×60 m perception range vs. outside it). Restating the threshold explicitly in the metrics section would improve clarity.

## Nice-to-Haves

- An ablation of the boundary-free baseline (e.g., replacing deformable attention with simpler feature pooling) would clarify which design choices drive the improvement.
- A comparison showing that the new split and metrics change the *ranking* of methods (rather than just the absolute numbers) would powerfully justify adoption of OMMP-Bench over the prior protocol.

## Removed Points

- The harsh critic's concern about "no decisive structural flaws" is not a weakness to list; it is the critic stating the paper is sound.
- The harsh critic's remark about "the benchmark and the baseline being somewhat conflated" is a presentation observation, not a substantive weakness. The paper is clear enough.
- The strength finder's claim that "Table 1 shows that under the default split, the motion model's map inputs during training (mAP 87.6) are far more accurate than during evaluation (mAP 50.3)" — the mAP values appear in Figure 3, not Table 1. The general claim is correct but the citation is imprecise. Minor, removed to avoid confusing readers.
- Several generic strengths from the strength finder (e.g., "comprehensive benchmark results") are kept in the main strengths above; others that are too vague have been dropped.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify why 150 nuScenes scenes are excluded from the split.
2. State whether results are from a single deterministic run or multiple seeds; if the latter, report variance.
3. Add one row in Table 7 using GT maps (under the new split) to quantify the remaining online-map gap.
4. Restate the close/far threshold explicitly in Section 3.4 (not just implicit from Section 3.3).
5. Fix the minor numerical inconsistency in the 12.7% claim in Section 4.2.

## Score and Decision

I need to perform calibration searches to anchor my score.

**Round 1 — Bracketing:**

From the first `calibration_search` call (3 queries):
- **Weak band** (high_score < 3.5):  
  `pzZjyYee6L` (avg 2.50), `324fOKW1wO` (avg 3.33), `MI0UiWeqOl` (avg 2.33), `DCg9r2DKKe` (avg 2.50). All rejected. This paper is clearly far above this band.
- **Middle band** (3.5 < score < 7.5):  
  `72MSbSZtHv` (RedMotion, avg 5.33, reject), `sEJYPiVEt4` (ESDMotion, avg 5.25, reject), `ZPCBcR7Drg` (MapDR, avg 5.00), `r125wFo0L3` (Large Traj. Models, avg 5.00). These papers have significant weaknesses (incremental novelty, questionable setups, missing baselines). The paper under review is stronger — its core contribution (identifying and fixing methodological confounds) is more clearly novel and consequential.
- **Strong band** (low_score > 7.5):  
  `Y6aHdDNQYD` (avg 8.00, accept), `Cjz9Xhm7sI` (avg 8.00, accept), `CRmiX0v16e` (avg 7.80, accept), `Q6a9W6kzv5` (avg 8.00, accept). These are high-quality accepted papers with polished presentation and extensive experiments. The paper under review is not at this level — it has several clarity gaps and missing details.

**Initial bracket: [5.5, 7.0].** The paper is comfortably above the weak anchors (2.33–3.33) and clearly stronger than the middle-band reject papers (5.00–5.33). It is not as polished as the 7.5+ anchors.

**Round 2 — Narrowing within [5.5, 7.0]:**

Second `calibration_search` call with queries targeting (5.5, 7.5):
- `UapxTvxB3N` (Trajectory-LLM, avg 5.75, accept): a language-based data generator. Less directly comparable, but accepted. The paper under review is stronger in novelty of problem identification.
- `efeBC1sQj9` (SEPT, avg 7.00, accept): self-supervised pretraining for motion prediction, achieves SOTA on Argoverse. Strong empirical results but some novelty concerns. The paper under review has clearer novelty but less impressive empirical numbers (benchmark paper vs method paper). Weaker than SEPT overall.
- `mDIXfHvoqH` (ITPNet, avg 6.75, reject): instantaneous trajectory prediction with two observations. Interesting idea but questionable practical value. The paper under review addresses a more fundamental protocol-level issue and is roughly comparable in quality.
- `Bmzv2Gch9v` (SmartPretrain, avg 6.75, accept): dataset-agnostic SSL for motion prediction. Strong empirical work.

**Round 2 narrows the bracket to [5.75, 6.5].** Reading the full reviews of SEPT (avg 7.00, accept) and ITPNet (avg 6.75, reject) confirms that the paper under review is weaker than SEPT (which had SOTA numbers and polished writing) but comparable to ITPNet (which had interesting ideas but practical limitations). The paper under review is stronger than ESDMotion (5.25) and RedMotion (5.33) — both rejected with more serious weaknesses.

**Final score: 6.0.** The paper has real, well-demonstrated contributions that will improve research quality in this area. The weaknesses (missing variance, unaccounted scenes, minor clarity issues) are all fixable but collectively keep it from being a clear accept at a top venue. This is a borderline-to-weak-accept paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>