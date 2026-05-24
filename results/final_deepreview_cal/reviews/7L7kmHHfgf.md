Now I have all the information needed to write the consolidated review.

---

## Summary

PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection that leverages RGB and surface-normal modalities. Instead of dense cross-modal alignment or large memory banks, it uses three novel components: Balanced Prototype Assignment (BPA, via optimal transport) to prevent codebook collapse; Adaptive Prototype Refinement (APR, via GRU-based prototype updates at inference) to bridge train-test distribution gaps; and Multimodal Normality Communication (MNC) to exchange prototype-level normality cues across modalities. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3, showing consistent gains under few-shot settings and offering an 85% FLOPs reduction over the prior state of the art.

## Strengths

- **Consistent few-shot performance gains across multiple benchmarks.** Table 1 shows PIRN outperforming all baselines at every shot setting (5, 10, 50, all) on both MVTec-3D-AD and Eyecandies. For example, at 10-shot on MVTec-3D-AD, AUROC_I improves from 0.885 (INP-Former) to 0.922, and similar margins hold consistently. The improvements are not fragile or cherry-picked — they persist across metrics and datasets.

- **Well-designed component ablations demonstrate each module's contribution.** Table 2 shows that removing any one of BPA, APR, or MNC from the full model degrades performance. Table 7 further validates the OT-based aggregation in APR against global averaging and top-k alternatives. Tables 5–6 ablate codebook size and decoder depth, showing the design choices are well-tuned.

- **Substantial computational efficiency advantage.** Table 4 reports 103.36 GFLOPs and 17.49 ms latency for PIRN versus 728.46 GFLOPs and 76.09 ms for FIND (the previous SOTA), while achieving better AUROC_I (0.922 vs. 0.921). An 85% FLOPs reduction while improving accuracy is a genuine practical contribution.

- **Qualitative and interpretability analyses are informative.** Figure 3 shows cleaner anomaly maps with fewer false positives and better separation of normal/anomalous score distributions. Figure 4 provides a novel feature-displacement analysis showing that anomalous tokens undergo much larger displacements toward prototypes than normal tokens, offering an interpretable view of the reconstruction bottleneck.

- **The method is coherently motivated.** The three components — BPA, APR, and MNC — each directly address a clearly identified failure mode of prototype-based reconstruction in few-shot multimodal settings (codebook collapse, unseen normal variation, and modality isolation). The technical narrative is tight.

## Weaknesses

### Major

- **Backbone standardization across baselines is incomplete, weakening the few-shot superiority claim.** PIRN uses a frozen DINOv2 ViT-B/14 backbone with multi-scale features. Among the baselines, only the adapted INP-Former is confirmed to share this backbone (Section 4, Implementation Details). Baselines such as M3DM, CFM, 3D-ADNAS, AST, and BTF use their own feature extractors (e.g., ResNet-50, PointNet, custom CNNs). In few-shot regimes, the quality of the pre-trained representation is known to dominate performance, so some fraction of PIRN's margin over these baselines may stem from the representation gap rather than the proposed BPA/APR/MNC modules. The improvement over the same-backbone INP-Former (+3.7 AUROC_I at 10-shot on MVTec-3D-AD) is still substantial, but the claim of consistent superiority over *all* baselines should be tempered. A simple reconstruction baseline sharing the same DINOv2 backbone would strengthen confidence.

### Minor

- **APR's claimed robustness to anomalous patches is not empirically validated.** The paper argues that anomalous patches contribute weakly to prototype updates because OT assigns them diffusely (Section 3.3). While the ablation (Table 2: 0.916 → 0.922 with APR) and aggregation comparison (Table 7) are supportive, they do not directly test whether prototypes remain stable when exposed to anomalous test inputs. Measuring prototype update magnitude as a function of input normality, or comparing detection performance with APR on anomalous-only vs. normal-only test sets, would directly validate this safety property. The theoretical argument is plausible but currently rests on intuition.

- **The Real-IAD D3 evaluation (Table 8) is in the full-data regime** and thus does not directly support the paper's central few-shot claim. Including a few-shot version of this experiment would align it with the core thesis. The paper's few-shot claim is primarily supported by MVTec-3D-AD and Eyecandies, which is sufficient, but the D3 results as presented sit somewhat outside the paper's narrative arc.

- **No discussion of limitations or failure modes.** The conclusion recapitulates contributions without addressing scenarios where APR might suppress subtle anomalies, where prototype count is critical, or where cross-modal communication could introduce noise. A limitations paragraph would improve completeness.

### Trivial

- Table 2 as rendered in the parsed version shows identical checkmarks across all rows due to a parser artifact; the original submission presumably has the correct module selection patterns, and the surrounding text describes the ablations clearly enough to follow.

## Nice-to-Haves

- A basic reconstruction baseline (e.g., a prototype-free autoencoder or two-stream reconstruction loss) using the same DINOv2 ViT backbone and multi-scale features would provide a clean lower bound to isolate the contribution of the PIRN architecture from the feature extractor.
- An ablation swapping the DINOv2 encoder for a weaker pre-trained model (e.g., supervised ViT) would reveal sensitivity to backbone quality.
- A few-shot version of the Real-IAD D3 experiment would better align that evaluation with the paper's core claim.
- Per-category results (mentioned in the appendix but stripped by the parser) should be made easily accessible for assessing the distribution of gains.

## Removed Points

These points raised by the reviewers were considered but not retained in the final review:

- *"Table 2 is garbled by the parser"* — This is a parser artifact, not an author error. The paper's description of Table 2 is clear enough to follow. Moved to Trivial.
- *"Per-category results are not visible in the parsed version"* — The appendix was stripped; this is a parser issue, not an author omission. Removed.
- *"The paper does not discuss missing related works"* — Not verifiable from the paper; the related work section covers the main paradigms (2D AD, multimodal AD). Removed.
- *"The efficiency comparison may not be fair because FIND uses a different backbone"* — Table 4 is a useful practical comparison; efficiency is reported alongside accuracy, and readers can interpret the trade-off. The paper doesn't claim fairness of efficiency comparison across architectures. Removed (this was not in the harsh critic's output but is worth noting).
- *Generic strength claims* such as "the problem is important" or "the paper addresses an interesting question" — These are too generic and not grounded in specific evidence. Removed from Strengths.

## Novel Insights

The paper offers a genuinely novel synthesis: applying balanced optimal transport simultaneously for two distinct purposes within the same framework — (1) uniform prototype assignment (BPA) to prevent codebook collapse, and (2) anomaly-resistant context extraction (APR) for prototype refinement at inference. The insight that anomalous patches are naturally suppressed in an OT plan because they lack strong affinity to any single prototype is both elegant and leveraged consistently across both mechanisms. The feature-displacement visualization (Figure 4), showing that BPA routing produces large reconstruction displacements specifically for anomalous tokens, provides a compelling empirical lens on why the prototype bottleneck works — this type of analysis is not common in the prototype-based anomaly detection literature and could be adopted by other works.

## Suggestions

- Add a DINOv2-backbone-equivalent baseline (e.g., a simple reconstruction loss operating on the same multi-scale features) to isolate architectural contributions. This is the single highest-impact experiment for strengthening the paper's claims.
- Include a direct empirical validation of APR's robustness, e.g., measuring prototype drift magnitude on normal vs. anomalous test inputs, or reporting detection performance with/without APR stratified by anomaly severity.
- Add a concise limitations paragraph to the conclusion, discussing assumptions and boundary conditions.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison to PIRN |
|---|---|---|---|
| `gTsLBDMZrL` (prototype refinement, few-shot IAD) | 5.50 | R1 | PIRN is clearly stronger: multimodal, more comprehensive ablations, better efficiency analysis, clearer methodology |
| `Zzs3JwknAY` (one-for-all few-shot AD) | 6.40 | R1/R2 | Comparable contribution level; PIRN has more thorough ablations and efficiency focus |
| `JDiER86r8v` (MMAD benchmark) | 6.50 | R2 | Different paper type (benchmark); PIRN's methodological contribution is deeper |
| `lR3rk7ysXz` (diffusion modeling for AD) | 7.00 | R2 | PIRN is slightly below — less theoretical depth and some evaluation gaps (backbone fairness, APR validation) |
| `cJs4oE4m9Q` (hypersphere compression) | 8.00 | R1 | PIRN is clearly below — lacks theoretical propositions and breadth of data modalities |

**Round 1 bracket:** 5.50–8.00, narrowed to 6.0–7.5 based on initial comparison.

**Round 2 narrowing:** Comparison with 6.40, 6.50, and 7.00 anchors places PIRN at approximately 6.5. The paper is clearly above the 5.50 rejected anchor, comparable to or slightly stronger than the 6.40 accepted anchor in terms of methodology and ablations, but below the 7.00 anchor which offered stronger theoretical grounding. The backbone fairness concern and unvalidated APR robustness prevent a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>