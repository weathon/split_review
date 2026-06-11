Now I have all the calibration data I need. Let me finalize the review.

## Summary

This paper diagnoses three methodological flaws in the evaluation protocol for online-map-based motion prediction in autonomous driving — inappropriate dataset splits causing a train-val gap, misaligned perception ranges between mapping and prediction, and non-discriminative metrics — and proposes OMMP-Bench, a corrected benchmark with spatially-disjoint data splits, refined agent-group metrics, and a boundary-free image-feature baseline. The paper evaluates existing methods on this benchmark and provides analysis of map element selection effects.

## Strengths

- **Well-evidenced train-val gap diagnosis (Figure 3, Table 1):** The paper demonstrates that the default nuScenes split produces an mAP drop from 87.6 to 50.3 for the map model between training and validation, while the proposed split maintains consistent accuracy (48.9 vs 50.3). This directly leads to motion prediction improvement: minADE drops from 0.6839 to 0.6308 under the corrected split.

- **Layered evidence on range misalignment (Tables 2, 3, 6):** Three complementary tables show (1) online mapping mAP collapses at long range (0.164→0.002 for MapTRv2-CL, Table 2), (2) GT maps at longer range *do* help motion prediction (minADE 0.6154→0.6003, Table 3), and (3) far agents have substantially worse prediction (minADE 0.6997 vs 0.5585 for close, Table 6), demonstrating the information is valuable but online models cannot yet supply it.

- **Effective boundary-free baseline (Table 7):** The image-feature baseline consistently outperforms prior methods across all eight map/motion model combinations. For MapTRv2-CL+HiVT far agents: base 0.6999 → img 0.6274. For MapTRv2-CL+DenseTNT far agents: base 2.2742 → img 1.9836. The approach is architecturally simple (reusing CNN backbone features via deformable attention) yet provides a practical solution to a structural limitation.

- **Valuable diagnostic finding about ego vs. non-ego performance (Table 7):** Methods that improve ego prediction (unc, bew) can simultaneously degrade non-ego prediction. E.g., MapTRv2-CL+DenseTNT+unc shows minADE *increasing* by 4.1% for far agents while improving ego. This failure mode was invisible under the old ego-only evaluation and represents a genuine insight the field needs.

- **Comprehensive benchmark (Table 7):** 2 map models × 2 motion models × 4 integration methods × 3 agent groups × 3 metrics = 72 result cells, all on the proposed spatially-disjoint split, providing a systematic reference for the community.

## Weaknesses

### Fatal
None.

### Major

- **Misattributed 12.7% headline result (Section 4.2, line 313):** The text states "Applied the method on the MapTRv2-CL+HiVT model, the minADE decreased by 12.7%." From Table 7: MapTRv2-CL+HiVT far-agent minADE goes from 0.6999 (base) to 0.6274 (img), which is a 10.36% decrease — not 12.7%. The 12.7% figure actually corresponds to MapTRv2-CL+DenseTNT (2.2742→1.9836 = 12.78%). This misattributes the paper's headline improvement number and should be corrected.

- **Data-split analysis does not disentangle contributing factors (Table 1):** Row 2 of Table 1, where the map model is trained on more data (Map Train + Motion Train) and the motion model trains on the combined set, yields minADE 0.7006 — *worse* than the default (0.6839). Meanwhile Row 4 (naive 50/50 subsetting of the official training set) achieves 0.6373, nearly matching the proposed split (0.6308). This pattern suggests multiple interacting factors (spatial overlap, train-set size, accuracy distribution matching) rather than a single train-val gap explanation, but the paper does not analyze these separately. The proposed split works, but the paper does not fully characterize *why*, limiting guidance for future split designs.

### Minor

- **Thin main-text description of the proposed baseline (Section 3.3, Eq. 1):** The paper's only methodological contribution — the "img" baseline — is described in a single equation. Key architectural details (how aggregated image features integrate with the motion model's map features, number of reference points, feature dimensionality, backbone frozen vs. fine-tuned) are deferred entirely to Appendix A. For a paper whose primary technical contribution includes a baseline method, the main text should convey enough detail to understand the design decisions.

- **Table 4 uses a different evaluation protocol than Table 7:** Table 4 reports aggregated minADE=0.6375 for HiVT+MapTR base, which does not match any single agent group in Table 7 (ego: 0.4015, close: 0.5585, far: 0.6997). It appears to use the default nuScenes split rather than the OMMP-Bench split, creating confusion about which protocol each table represents. A clarifying note would help.

- **Only evaluated on nuScenes:** The benchmark's generality is untested on other autonomous driving datasets. This is acknowledged as a field limitation but worth noting.

### Trivial

- **No variance estimates:** With only 86 validation scenes, reporting means without confidence intervals leaves some uncertainty about result stability.

## Nice-to-Haves
- A quantitative ablation disentangling spatial disjointness vs. distribution matching in the data split would substantially strengthen the core contribution.
- Error bars or variance estimates given the small validation set (86 scenes).
- Extending evaluation to at least one additional dataset.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Table 5 self-contradictory text ("centerlines are most helpful and centerlines only achieve the second best performance"):** This is almost certainly a PDF parsing artifact. The original paper likely has correctly formatted table entries where Row 3 is (✗, ✗, ✗, ✓) for centerline-only, and the garbled text resulted from extraction. Treating this as a real author error would be unfair.
- **Criticism about formatting/typos:** Parser artifacts, not paper problems.
- **"Missing related works" claims from human finder:** Cannot verify existence of claimed missing works.
- **"Table 5 duplicate rows" criticism:** Likely a parsing artifact — Row 3 was probably centerline-only in the original.

## Novel Insights
The paper's most valuable insight is that methods improving ego-vehicle prediction in online-map-based motion prediction can simultaneously degrade non-ego prediction (Table 7), a failure mode invisible under the old evaluation protocol. This demonstrates that the field's evaluation methodology has been masking real problems. The layered analysis of range misalignment (showing online maps degrade at distance, GT maps help at distance, and far agents suffer more) is also well-executed and instructive for the research community.

## Suggestions
- Fix the 12.7% attribution: either correct it to "MapTRv2-CL+DenseTNT" or recalculate for HiVT (10.4%).
- Add a brief analysis of why Row 2 in Table 1 underperforms despite having more training data — even a hypothesis would help readers understand the split design rationale.
- Expand the baseline description in the main text to include at least the integration mechanism with the motion model.
- Consider adding a note to Table 4 clarifying it uses the default nuScenes split for comparison with prior work.

## Calibration Report

**All retrieved anchors:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Lifelong Person Re-ID | 5lUdTogEL3 | 1.00 | 1 | Unrelated domain, much weaker |
| GFlowNets | Uj0h13lVrR | 1.00 | 1 | Unrelated domain, much weaker |
| Illumination Harmonization | u1cQYxRI1H | 0.50 | 1 | Unrelated domain |
| Don't Reinvent Steering Wheel | pzZjyYee6L | 2.50 | 1 | Motion prediction, much weaker methodology |
| Commonsense Reasoning AD | V1N6MmDY27 | 2.50 | 1 | AD domain, much weaker |
| STL-Drive | DCg9r2DKKe | 2.50 | 1 | AD domain, much weaker |
| Fair Comparisons TSF | X8aFMdXk3N | 4.25 | 1 | Benchmark correction — weaker than this paper: less evidence, no baseline, more incremental |
| Entropy-Based Uncertainty | RflvsSxM0u | 4.50 | 1 | Trajectory prediction — narrower scope |
| RedMotion | 72MSbSZtHv | 5.33 | 1 | Motion prediction method — rejected, different contribution type |
| ESDMotion | sEJYPiVEt4 | 5.25 | 1 | Motion prediction SD maps — similar domain, less diagnostic |
| TopoSD | 9tiQ0aBK7c | 5.20 | 1 | Online mapping — similar domain, method paper rejected |
| Benchmarking Diffusion Editing | nkCWKkSLyb | 5.50 | 1 | Benchmark paper — rejected, similar pattern of overclaiming |
| Physics-informed Motion Planning | TOiageVNru | 6.00 | 1 | Motion planning — accepted, different contribution type |
| ITPNet | mDIXfHvoqH | 6.75 | 1 | Trajectory prediction — method paper, rejected |
| SmartPretrain | Bmzv2Gch9v | 6.75 | 1 | Motion prediction repr. learning — accepted method paper |
| SEPT | efeBC1sQj9 | 7.00 | 1 | Motion prediction SOTA — accepted, stronger method contribution |
| KOR-Bench | SVRRQ8goQo | 7.00 | 1 | Benchmark paper — accepted, more comprehensive but NLP domain |
| LLM Self-Correct | IkmD3fKBPQ | 6.75 | 1 | Diagnostic paper about LLM — accepted, similar "diagnosing misconceptions" framing |
| LiveBench | sKYHBTAxVa | 7.33 | 1 | Benchmark paper — accepted, strong benchmark contribution |
| CS-Bench | fjEZ2LPceZ | 6.75 | 1 | Benchmark paper — accepted |
| MMIE | HnhNRrLPwm | 8.00 | 1 | Benchmark paper — accepted, much stronger |

**Round 1 bracket: 5.5 – 6.5.** This paper is clearly stronger than rejected benchmark corrections (~4.25) and weaker than accepted benchmark papers (~7.0). It sits in the borderline zone. Given genuine diagnostic value, comprehensive evaluation, and practical baseline despite the misattributed claim and incomplete analysis, the paper lands at **6.0** — a solid borderline accept with fixable issues.

## Score and Decision

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <score>Accept</score>