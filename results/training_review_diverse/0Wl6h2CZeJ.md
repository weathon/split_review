Now I have sufficient context from the paper. Let me produce the final consolidated review.

## Summary

The paper introduces RealTracker, a new point tracking system combining a simplified architecture (removing global matching, replacing ad-hoc correlation modules with an MLP, maintaining cross-track attention) with a data-efficient semi-supervised training recipe that uses multiple off-the-shelf teacher models (CoTracker, TAPIR, and two RealTracker variants) to pseudo-label real videos. The model achieves state-of-the-art results on TAP-Vid, Dynamic Replica, and RoboTAP benchmarks, surpassing BootsTAPIR while using 1,000× fewer real videos. It also provides the first systematic data scaling study for point trackers and includes a self-training extension that yields further improvements.

## Strengths

1. **Principled architectural simplification without performance loss.** RealTracker removes the global matching module used by TAPIR, BootsTAPIR, and LocoTrack, and replaces LocoTrack's ad-hoc correlation processing with a simple MLP, yet runs 27% faster than LocoTrack and achieves better occlusion tracking (Section 4.3, lines 349-358). The architecture has 2× fewer parameters than CoTracker. This is a genuine contribution — identifying which components of prior designs are truly essential.

2. **Demonstrated occlusion-handling advantage through joint tracking.** On Dynamic Replica, RealTracker online trained only on Kubric already outperforms all prior methods on occluded points (line 415). The cross-track attention ablation (Table 4, referenced at line 443) quantifies a +5.1 gain on occluded points vs. +1.6 on visible points, directly confirming that joint tracking is the mechanism behind occlusion robustness.

3. **Systematic data scaling study.** The paper provides the first controlled scaling analysis for point trackers (Figure 3, described in Section 5.3), training RealTracker, LocoTrack, and CoTracker on progressively larger subsets from 0.1k to 100k videos. This reveals that RealTracker and LocoTrack plateau after ~30k videos while the weaker CoTracker keeps improving, offering insights about model capacity and teacher quality that are valuable for the community.

4. **Multi-teacher pseudo-labelling with demonstrable complementarity.** The teacher ablation (Table 5, described at lines 449-452) shows that removing any single teacher degrades final performance, providing concrete evidence that diverse teacher signals are beneficial even when some teachers are individually weaker. This validates the design choice of using four teachers.

5. **Simple and effective solution to catastrophic forgetting.** Freezing the separate visibility/confidence head during pseudo-label training (Table 6, lines 461-464) yields +0.8 AJ and +3.9 OA on average — a simple but well-motivated fix.

## Weaknesses

### Fatal
None.

### Major

1. **The "1,000× less data" framing conflates architectural and training-recipe contributions.** The paper's headline claim compares RealTracker (new architecture + new training recipe + 15k real videos) against BootsTAPIR (TAPIR architecture + complex self-training + 15M real videos). Because the Kubric-only results (line 404) show that RealTracker's architecture already substantially outperforms BootsTAPIR's architecture on synthetic data alone, the 1,000× gap is not solely attributable to the training recipe's data efficiency. The paper attributes the data efficiency to "this training scheme" (line 9) or "this protocol" (line 476), but the architecture itself accounts for a significant portion of the improvement. This is a framing issue, not a scientific flaw — both contributions are real and well-demonstrated — but it overstates the role of the training protocol specifically and could mislead readers about what drives the gains. The authors should either (a) run the pseudo-labelling protocol on a TAPIR backbone to isolate the training contribution, or (b) more carefully attribute the gains between architecture and training recipe in their claims.

2. **Missing teacher baseline performance on evaluation benchmarks.** The scaling analysis (Section 5.3) speculates that plateaus occur "likely because the student surpasses the teachers" (line 427), but the paper never reports the teachers' own performance on TAP-Vid or Dynamic Replica. Without this information, the plateau explanation remains speculative. Knowing teacher performance would also contextualize why self-training (line 433) continues to help after the student supposedly surpasses the teachers — the paper's own explanation (domain adaptation, lines 433-434) is plausible but unverified. This is a significant gap in an otherwise thorough scaling study.

### Minor

3. **Multi-teacher compute overhead not discussed.** The paper emphasizes that RealTracker is "simpler" than prior work, contrasting with BootsTAPIR's complex protocol (augmentations, masks, EMA). However, maintaining four frozen teacher models and running them on 15k+ videos incurs substantial compute and memory that is never quantified. The "simplicity" claim is valid for the student inference path and the training recipe itself, but the overall system cost is not transparent. The authors should report total training compute hours including teacher inference.

4. **Offline/online performance asymmetry underexplained.** The offline version tracks occluded points better on Dynamic Replica but underperforms the online version on Kinetics and RoboTAP (Tables 1 and 2, noted at line 406). The paper mentions that the offline version uses random video trimming during training (line 345), but does not analyze why this causes a systematic disadvantage on real benchmarks. A breakdown by video length or occlusion rate would clarify the trade-off.

5. **Teacher removal ablation shows small effect sizes.** Table 5 shows that removing any single teacher hurts, but the drops are small (e.g., ~0.5 AJ for removing the weakest teacher). The paper claims "every teacher is important" (line 452), but it does not report whether using only the two strongest teachers (RealTracker offline + TAPIR) approaches the full set's performance. The claim would be stronger if the paper showed that the benefit of weaker teachers is not redundant with stronger ones.

6. **SIFT-based query sampling may introduce selection bias.** Videos where SIFT fails to produce sufficient points are skipped entirely (line 170). This could bias the training set toward texture-rich videos and limit generalization to low-texture scenes. The RoboTAP results are strong, which mitigates the concern, but the paper should discuss this potential bias explicitly.

### Trivial
None.

## Nice-to-Haves

- Report teacher performance on TAP-Vid benchmarks to ground the scaling plateau discussion.
- Report the total compute cost (in GPU-hours) of the full training pipeline including teacher inference, to contextualize the "simple vs. complex" comparison.
- Ablate using only the two strongest teachers vs. all four to test whether weaker teachers contribute independently.
- Provide a breakdown of offline model performance on Kinetics by video length.

## Removed Points

- **Self-training "undermines surpassing teachers" claim.** The critic argued that the +1.2 AJ improvement from self-training contradicts the "surpasses teachers" explanation. However, the paper explicitly addresses this at lines 433-434 ("Presumably, fine-tuning on real data, even with its own annotations, helps the model reduce the domain gap between real and synthetic data.") This is not a contradiction — self-training provides domain adaptation benefits independent of teacher quality. **Removed because the paper already addresses this point.**

- **Missing appendix / missing proofs.** Any criticism about missing appendix content or missing proofs is removed per instructions — the parser strips these sections from all papers and they exist in the original submission.

## Novel Insights

A genuinely novel observation emerges from the interaction of two findings: (1) the student's own self-predictions (+1.2 AJ) provide further gains even after training with four teachers, and (2) the stronger architecture (RealTracker) plateaus earlier in data scaling while the weaker one (CoTracker) keeps improving. Together, these suggest a "teacher quality ceiling" dynamic that is distinct from the well-known "model capacity ceiling" — the training recipe's effectiveness may be bounded not by how much data is available, but by the quality ceiling of the teacher ensemble. This implies that improving teachers (e.g., iteratively replacing teachers with trained students) may yield further gains even with a fixed dataset size, which is a testable prediction the paper does not itself make but that the data supports.

## Suggestions

1. **Reframe the data-efficiency claim.** Distinguish what is attributable to the stronger architecture vs. the training recipe. Even adding a qualifying sentence — "Our combined architecture and training recipe achieves..." — would substantially improve accuracy.
2. **Add teacher performance lines to the scaling plot (Figure 3).** This single addition would ground the plateau interpretation and make the scaling analysis self-contained.
3. **Quantify the total compute cost of the multi-teacher pipeline.** Report GPU-hours for running teachers + training student, compared to BootsTAPIR's published training cost.
4. **Report the two-best-teachers ablation.** Test whether removing CoTracker and TAPIR (keeping both RealTracker variants) versus all four teachers changes the result. This would clarify whether weaker teachers are truly complementary.
5. **Diagnose the offline underperformance on Kinetics.** Provide a simple breakdown by video length or motion magnitude to explain the asymmetry.

## Score and Decision

The paper makes solid contributions: a genuinely simpler and faster architecture that achieves state-of-the-art results, a data-efficient training recipe validated by thorough ablations, and the first systematic scaling study for point trackers. The main weaknesses are a framing issue (attributing all gains to the training recipe when the architecture contributes significantly) and missing teacher baselines in the scaling analysis. Both are fixable and do not undermine the core contributions. The empirical evidence is strong, the ablations are comprehensive, and the work advances the state of the art in point tracking.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>