- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Here is my synthesized final review.

---

## Summary

RealTracker introduces a simplified point-tracking architecture and a semi-supervised training pipeline that uses multiple off-the-shelf synthetic-trained trackers (CoTracker, TAPIR, and earlier versions of RealTracker itself) to pseudo-label real videos. The model eliminates the global matching stage used by prior work, replaces ad-hoc correlation modules with a simple MLP, and uses cross-track attention to handle occluded points. Trained on only 15k real videos, it outperforms BootsTAPIR (trained on 15M real videos) across TAP-Vid benchmarks while being faster and having fewer parameters. The paper also provides the first systematic scaling study for point trackers up to 100k videos.

## Strengths

- **Dramatic data efficiency with state-of-the-art results**: RealTracker trained on 15k real videos surpasses BootsTAPIR trained on 15M real videos on TAP-Vid DAVIS, Kinetics, RGB-Stacking, and RoboTAP (Sec. 4.1). The 1,000× data reduction is a substantiated and striking result backed by benchmark numbers reported in the main text.

- **Architectural simplification validated by competitive performance**: The model removes the global matching stage (used by TAPIR, BootsTAPIR, LocoTrack) and replaces LocoTrack's ad-hoc 4D correlation module with a simple MLP. These simplifications yield 2× fewer parameters than CoTracker and 27% faster inference than LocoTrack, while maintaining or improving accuracy (Sec. 3.4, Sec. 4.1).

- **First systematic scaling study for point trackers**: The paper evaluates RealTracker, CoTracker, and LocoTrack on progressively larger real-dataset subsets (0.1k to 100k videos), showing all models improve with more data and that improvements plateau around 30k for most models (Sec. 4.3, Fig. splash). CoTracker benefits more from additional data because it starts weaker but continues improving past 100k — a useful finding absent from prior work.

- **Cross-track attention provides large gains for occluded points**: Ablation shows cross-track attention improves occluded-point accuracy by +5.1 on Dynamic Replica vs. +1.6 for visible points (Sec. 4.4). This quantifies the genuine benefit of joint tracking over independent-point architectures like LocoTrack, and the offline variant particularly excels at occlusion handling.

## Weaknesses

### Fatal
None.

### Major

None.

### Minor

- **Global matching removal is stated as a design finding but not ablated.** The paper claims global matching is "redundant" (Sec. 3.4) but provides no experiment comparing RealTracker with vs. without a global matching module. While the overall model performs well, the specific claim that global matching is unnecessary is not directly tested. An ablation would cleanly separate whether the other architectural changes (4D correlations, cross-track attention) fully compensate for its removal or whether some loss occurs and is masked by other gains.

- **Teacher ablation always includes the student, so "every teacher is important" is incompletely tested.** The ablation in Sec. 4.4 removes weaker teachers one at a time but "always keep[s] the student model itself as a teacher." This tests whether CoTracker/TAPIR add value on top of the student's own predictions — which is useful — but it does not test whether the student's own predictions are necessary. The separate self-training experiment (Sec. 4.3, +1.2 improvement from student-only) partially addresses this, but the direct comparison of "all teachers except the student" vs. "all teachers" is absent. The claim as stated overreaches what the experiment shows.

- **The 1,000× data-efficiency comparison lacks controls for data distribution.** The paper compares its 15k "Internet-like videos" against BootsTAPIR's 15M YouTube videos. No analysis is provided on the relative diversity, difficulty, or distributional coverage of the two datasets — e.g., whether the 15k videos cover simpler motions or fewer occlusion patterns. This makes it difficult to attribute the efficiency gain solely to the method rather than to differences in data difficulty. The scaling study partially mitigates this concern (performance improves consistently up to 100k) but does not directly control for it.

- **SIFT-based point sampling may filter hard examples without discussion of bias.** The paper states that SIFT sampling "serve[s] as a filter for hard-to-track points" and that videos where SIFT fails to produce enough points are skipped (Sec. 3.1). This is acknowledged but not discussed as a potential bias toward easier tracking cases. The ablation showing similar performance with other sampling methods (LightGlue, SuperPoint, DISK) partially addresses this, but the overall effect on the training distribution is not analyzed.

### Trivial
None beyond formatting artifacts introduced by PDF extraction (not author errors).

## Nice-to-Haves

- Adding a variant of RealTracker with a lightweight global matching module would directly substantiate (or qualify) the "redundant" claim.
- Including an ablation that removes the student-as-teacher (training on CoTracker + TAPIR only) would complete the teacher analysis.
- Reporting distributional statistics (e.g., motion magnitude, occlusion frequency) comparing the 15k video subset to BootsTAPIR's 15M videos would strengthen the data-efficiency claim.

## Removed Points

These points were flagged during review but do **not** belong in the main evaluation:

1. **Critic: "No comparison to BootsTAPIR's training protocol on the same data"** — Removed because this asks the paper to solve a different experimental design question. The paper's claim is that its overall recipe (architecture + pseudo-labelling) is more data-efficient; applying BootsTAPIR's recipe to 15k videos or RealTracker's recipe to 15M would be a separate study well beyond the paper's scope.

2. **Critic: "Claim that RealTracker 'helps to identify which components are really important' is not fully followed through"** — Removed because the paper does identify several important component decisions through ablations (cross-track attention matters, confidence/visibility head freezing helps, multiple teachers help). The critic's specific example (not testing 4D correlation MLP vs. LocoTrack's ad-hoc module) is a design choice difference that the paper evaluates indirectly via overall performance comparison.

3. **Critic: "No direct evidence given for why student can outperform teachers (e.g., comparing on subsets where teachers disagree)"** — Removed as a nice-to-have diagnostic analysis that goes beyond what is standard or necessary to validate the core claim. The paper provides reasonable reasoning (ensembling, domain gap reduction, inheriting teacher strengths) and the empirical result is clear.

4. **Critic: "Statistical significance or confidence intervals are absent"** — Removed because single-run evaluation on standard benchmarks is the community norm for this task (TAP-Vid, Dynamic Replica). Not a weakness specific to this paper.

5. **Critic: "The paper does not release code or model weights"** — Removed because code/model release is a reproducibility nicety, not a requirement for evaluation, and the paper provides sufficient methodological detail.

6. **Strength Finder: Generic/superficial strengths** (e.g., "this paper addressed an important problem") — Removed. Only concrete, evidence-backed strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The key takeaway — that a simple pseudo-labelling pipeline with diverse teachers can match or exceed a heavily-engineered self-training protocol using 1,000× less data — is well articulated by the authors themselves.

## Suggestions

1. Add an ablation with a global matching stage to substantiate (or qualify) the claim that it is "redundant."
2. Include the "teachers without student" condition in the teacher ablation to complete the analysis.
3. Provide a brief discussion of how SIFT-based point filtering might bias the training distribution, even if the effect appears empirically small.
4. When comparing to BootsTAPIR, add a note on the data characteristics (even qualitative) to help readers assess the 1,000× claim.
