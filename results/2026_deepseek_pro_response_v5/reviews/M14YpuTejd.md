Now I have a clear calibration picture. Let me finalize the review.

**Calibration Summary:**

Round 1 bracket: 4.5–6.0 based on comparison with:
- cvGdPXaydP (4.25): nuPlan critique — similar genre but weaker evidence, overclaimed contributions
- ZPCBcR7Drg (5.00): Driving by Rules benchmark — similar genre, comparable quality
- sEJYPiVEt4 (5.25): ESDMotion — related domain, comparable contributions
- k3y0oyK7sn (5.40): BEV Uncertainty benchmark — similar structure, slightly stronger (novel loss function)

Round 2 narrowed: This paper sits between Driving by Rules (5.00) and BEV Uncertainty benchmark (5.40). Our paper has stronger diagnostic insights than Driving by Rules but weaker technical novelty than BEV Uncertainty and has a data error (Table 5) that the BEV paper doesn't. I score it at **5.0**.

---

## Summary
This paper diagnoses three structural problems in the emerging two-stage protocol for online-map-based motion prediction: (1) a train-validation gap from shared dataset splits across stages, (2) a perception-range mismatch between online mapping models (~30×60m) and motion prediction needs (100m+), and (3) non-discriminative metrics that evaluate only the ego vehicle and include trivially-predictable static agents. The authors propose OMMP-Bench with a spatially-disjoint three-way data split, stratified evaluation across agent distance groups, and a boundary-free baseline using deformable attention over raw image features. The diagnosis is sound and well-motivated, though the evidence has several gaps that prevent it from being fully convincing.

## Strengths
- **Well-motivated diagnosis of genuine problems**: The paper provides clear quantitative evidence for each issue. Figure 4 quantifies 87% spatial overlap in the default split vs 5% in the proposed split. Table 2 shows online mappers degrade dramatically at long range (mAP drops from 0.164 to 0.002 for MapTRv2-CL). Table 6 reveals static agents have minADE ~0.002–0.009, confirming they dilute evaluation metrics.
- **Stratified metrics expose hidden regressions**: Table 7 demonstrates that methods improving ego prediction can simultaneously degrade non-ego far-agent prediction (e.g., MapTRv2-CL+DenseTNT with "unc" increases far-agent minADE by 4.1% over base while improving ego). This is a genuinely useful finding that justifies the benchmark's expanded evaluation scope.
- **Practical and simple baseline**: The deformable-attention image-feature baseline (Eq. 1) directly addresses the range mismatch without requiring architectural changes. Table 7 shows consistent gains, especially on far-away agents (12.7% minADE reduction for MapTRv2-CL+HiVT on Moving Non-Ego Far).
- **Comprehensive evaluation**: Table 7 evaluates 2 map models × 2 motion models × 4 integration methods across 3 agent groups, providing a thorough snapshot of the current protocol.

## Weaknesses

### Fatal
None.

### Major
- **Table 5 contains a data error**: Rows 2 and 3 (lines 246–247) have identical checkmark configurations (✗, ✓, ✗, ✗ — Boundary only) but report different minADE values: 0.6829 and 0.6558. This is either a transcription error or a duplicate row. The map-element analysis in Section 3.5 draws conclusions from this table (e.g., "centerlines only achieve the second best performance," line 267), making those conclusions unreliable until the error is corrected.
- **No variance or statistical significance reporting**: None of the result tables (Tables 1–7) report standard deviations, confidence intervals, or mention of random seeds. For a benchmark intended to serve as a platform for comparing methods, the absence of variance reporting means readers cannot assess whether reported performance differences are meaningful or noise. Some gaps in Table 7 are small (e.g., MapTR+HiVT Moving Non-Ego Close: base 0.5585 vs unc 0.5560).
- **Table 1 evaluation-set confound**: Settings 1–2 are evaluated on the proposed Motion Val set, while Settings 3–4 are evaluated on nuScenes Val. Setting 4 (random 50/50 split of nuScenes Train, minADE 0.6373) is substantially better than the default Setting 3 (0.6839) and quite close to Setting 1 (0.6308), but the different validation sets make direct comparison impossible. The paper does not acknowledge this confound.

### Minor
- **Introduction overstates the evaluation scope**: Line 51 states "we propose to only evaluate non-ego agents," but Table 7 and Section 3.4 actually report ego results as well. The protocol evaluates all moving agents including ego, which is reasonable, but the text overclaims.
- **Split construction is not reproducible**: The description "we manually check the whole dataset and split it" (line 121) provides no algorithmic criteria for scene assignment. For a benchmark paper, the split methodology should be reproducible through explicit criteria or code release.
- **Image-feature baseline is under-described in the main text**: The backbone architecture, deformable attention implementation, and projection mechanism are not specified (Section 3.3). This may be detailed in the appendix, but the main text alone is insufficient for reproduction.
- **No limitations section**: The paper does not discuss what OMMP-Bench does not cover (nuScenes-only, fixed set of model pairs, does not consider detection/tracking errors).

### Trivial
- The "boundary-free baseline" is framed as a contribution but is essentially one deformable attention layer. The framing slightly overstates its novelty, though this does not affect the empirical validity.

## Nice-to-Haves
- Running Setting 4 (random 50/50 split) on the proposed Motion Val set would allow a fair comparison between the spatial split and a simpler random split, directly quantifying the value of spatial disjointness.
- Runtime or computational cost analysis for the image-feature baseline vs. alternatives would help practitioners assess adoption tradeoffs.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh Critic's claim that Setting 4 "substantially weakens the claim that spatial disjointness is a necessary design choice" as a fatal-level weakness — removed as overstated. Setting 4 only shows that reducing the train-val gap helps; it does not address the spatial overlap issue that the spatial split is designed for. The evaluation-set confound is real but kept as a major weakness about the confound itself, not as evidence that the spatial split is unnecessary.
- Harsh Critic's framing of the image-feature baseline as "essentially one deformable attention layer" as a significant weakness — demoted to trivial. The paper does not claim this is a major architectural innovation; it is presented as a simple effective baseline.
- Strength Finder's generic strengths about "addressing an important problem" — removed as superficial.

## Novel Insights
The most genuinely novel observation is that stronger map representations for ego prediction can actively harm non-ego far-agent prediction (Table 7, MapTRv2-CL+DenseTNT with unc/bew methods). This suggests a tension between optimizing map features for the ego vehicle's local context versus providing useful information for distant agents — with implications for how online mapping models should be designed and evaluated for downstream tasks.

## Suggestions
- Fix the Table 5 error: clarify which row has the correct checkmark configuration and which minADE value is correct.
- Add at least 3-seed runs with standard deviations for the main Table 7 results, or at minimum for the key method comparisons.
- Either run Setting 4 on Motion Val for a fair comparison, or explicitly discuss the evaluation-set confound.
- Provide explicit criteria or code for the split construction to make it reproducible.
- Tone down the "only evaluate non-ego agents" claim in the introduction to match what the paper actually does.

## Anchor Papers
- cvGdPXaydP (4.25, Round 1): nuPlan benchmark critique — similar genre but weaker evidence; our paper is stronger.
- ZPCBcR7Drg (5.00, Round 1): Driving by Rules benchmark — similar genre; our paper has stronger empirical diagnostics but also a data error.
- sEJYPiVEt4 (5.25, Round 1): ESDMotion — related domain with clearer technical contribution; our paper has stronger diagnostic analysis but simpler baseline.
- k3y0oyK7sn (5.40, Round 2): BEV Uncertainty benchmark — similar structure (benchmark + method); stronger technical novelty (UFCE loss) but comparable overall quality.
- 72MSbSZtHv (5.33, Round 2): RedMotion — method paper; our paper is a different genre but comparable in rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>