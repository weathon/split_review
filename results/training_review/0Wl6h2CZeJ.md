Now I have thorough verification. Let me construct the final review.

## Summary

RealTracker introduces a simplified point-tracking architecture combined with a semi-supervised training recipe that uses multiple off-the-shelf teacher models to pseudo-label real unlabeled videos. The architecture removes the global matching stage used in TAPIR/BootsTAPIR/LocoTrack and simplifies 4D correlation processing with an MLP, while retaining cross-track attention for occlusion handling. The paper shows state-of-the-art results on TAP-Vid benchmarks, provides a systematic scaling study across data sizes (0.1k–100k videos), and reports that their model matches or exceeds BootsTAPIR while using ~15k real videos compared to BootsTAPIR's 15M.

## Strengths

- **Dramatic data efficiency in a systems sense**: RealTracker outperforms BootsTAPIR across TAP-Vid and Dynamic Replica benchmarks while using 15k real videos versus BootsTAPIR's 15M — a 1,000× reduction (§4.1, Table 1). The scaling study (§4.3, Fig. splash) independently shows that performance plateaus around 30k videos for their architecture, supporting the conclusion that massive datasets are unnecessary.

- **Genuine architectural simplifications without sacrificing accuracy**: The model eliminates the global matching module used by TAPIR, BootsTAPIR, and LocoTrack (§3.5), replaces LocoTrack's ad-hoc 4D correlation processor with a simple MLP (§3.3), and discards EMA, augmentations, and loss masks from semi-supervised training (§2, last paragraph). Despite these simplifications, it beats all prior methods on TAP-Vid benchmarks, running 27% faster than LocoTrack (§3.5).

- **Cross-track attention yields large gains on occluded points**: Joint tracking via cross-track attention (inherited from CoTracker but simplified) yields +5.1 improvement in occluded tracking accuracy on Dynamic Replica versus +1.6 for visible points (§4.4, Table 4). The offline version achieves the best reported scores on occluded points (Table 2), directly justifying this design choice over LocoTrack's independent-point approach.

- **First systematic scaling study for point tracking on real data**: The paper investigates performance from 0.1k to 100k real videos across three architectures (RealTracker, LocoTrack, CoTracker), identifying clear trends and a plateau around 30k videos (§4.3). This provides novel empirical evidence about the data requirements for point tracking and demonstrates that all tested architectures benefit from the multi-teacher pseudo-labeling pipeline.

- **Thorough ablation study**: Each design choice (cross-track attention, number of teachers, point sampling methods, freezing visibility/confidence head) is empirically justified, giving confidence in the architecture and training recipe (§4.4).

## Weaknesses

### Fatal

None.

### Major

- **The "1,000× less data" claim rests on an uncontrolled cross-paper comparison, not on a controlled experiment.** The paper compares RealTracker (trained on 15k real videos) against the published results of BootsTAPIR (trained on 15M real videos). Because the architectures, video sources, and training protocols differ, the superior performance cannot be cleanly attributed to the training recipe's data efficiency — it could partly reflect architectural improvements. The paper would be substantially stronger if it included an experiment training BootsTAPIR or TAPIR on the same 15k videos with their own protocol. The scaling study partially mitigates this by showing diminishing returns with more data, but it does not trace BootsTAPIR's scaling curve. As a system-level claim ("our full pipeline achieves better results with less data") the comparison is standard; as a claim about the training protocol's inherent data efficiency it is not fully justified.

### Minor

- **The "simpler training" narrative is in tension with the multi-teacher pipeline's complexity.** The paper repeatedly emphasizes simplicity (Abstract: "much simpler than prior work"; §2: "a much simpler protocol"), but the pipeline requires four separately pre-trained teacher models (CoTracker, TAPIR, and two variants of RealTracker), each of which must be run on the real video collection to generate pseudo-labels (§3.1). BootsTAPIR's self-training, by contrast, uses a single model and no external teachers. The paper's simplicity claim is valid for the loss/augmentation aspect (no augmentations, masks, EMA, or ground-truth supervision during fine-tuning), but the overall pipeline introduces significant external dependencies that the reader should weigh against this framing.

- **No comparison against random point sampling.** The paper compares SIFT-based query sampling against LightGlue, SuperPoint, and DISK (§4.4) but not against uniform random sampling, which would be the simplest baseline. The claim that SIFT biases selection toward "good to track" points (§3.1) goes untested against the null hypothesis. If random sampling performs similarly, the SIFT step would be unnecessary complexity.

- **Missing analysis of pseudo-label quality and teacher complementarity.** The teacher ablation (Table 5) shows all four teachers contribute, but the paper does not quantify how often different teacher tracks agree/disagree, how noise correlates with occlusion or motion, or which teacher is most reliable under which conditions. Since the method's success depends critically on teacher diversity, such analysis would strengthen the contribution.

### Trivial

- The scaling plateau at ~30k videos is attributed to "the student surpassing the teachers" (§4.3) — a plausible but untested hypothesis. A second round of self-training using the best student as a new teacher would confirm or refute this explanation.
- The paper states that cross-track attention helps occluded points but does not visualize failure cases where teachers fail and the student succeeds, which would complement the quantitative occlusion analysis.

## Nice-to-Haves

- Iterating the self-training loop (using the +15k model as a new teacher) to see if the plateau can be broken.
- Visualizing pseudo-label diversity from different teachers on the same video to illustrate complementarity qualitatively.
- Ablating the number of teachers (e.g., 2 vs. 4) to see if diminishing returns exist, beyond the sequential removal experiment already done.

## Removed Points

These points are flagged to be removed, treat them with caution:
- "Without seeing the tables we rely on the text" — This is a PDF-parser artifact; the tables exist in the original submission.
- "Missing ablation of the number of teachers to see if diminishing returns set in" — The paper already ablates removing teachers one by one (Table 5), showing each removal hurts, which addresses this.
- "BootsTAPIR also uses a teacher-student setup (EMA-based self-training), making the contrast less stark" — The paper clearly acknowledges BootsTAPIR's self-training approach in §2 (lines 91–96); the contrast is about the specific design choices (no augmentations, masks, EMA) which is factually correct.
- Demands for "side-by-side failure cases" as a weakness — This is a presentation enhancement, not a methodological flaw.

## Novel Insights

The harsh critic frames the "1,000× less data" claim as an unsupported headline, but the scaling study (Fig. splash) provides a stronger argument than the critic acknowledges: by showing that *three different architectures* (RealTracker, LocoTrack, CoTracker) all plateau around 30k videos under the same training recipe, the paper demonstrates that the marginal value of real data for point tracking diminishes rapidly, and that 15M videos is orders of magnitude beyond what any tested architecture can exploit. This finding — that data requirements saturate — is a genuinely novel empirical contribution that stands independently of the uncontrolled BootsTAPIR comparison. The trade-off the reviews surface is between claiming "1,000× less data than BootsTAPIR" (which is a system-level fact that could benefit from a controlled experiment) versus "point tracking data requirements saturate at ~30k real videos under a diverse-teacher pseudo-labeling scheme" (which is well-supported). The paper's contribution is better captured by the latter framing.

## Suggestions

1. **Add a controlled experiment**: Train TAPIR (or at minimum the BootsTAPIR protocol) on the same 15k real videos used for RealTracker. This would directly test whether the data efficiency claim is driven by the training recipe or by the architecture. Even a single-data-point comparison at 15k would substantially strengthen the headline claim.
2. **Add a random point-sampling baseline** for the query selection ablation (§4.4). This is a simple experiment that would confirm or refute the value of the SIFT-based heuristic.
3. **Tone down the "simplicity" framing** or explicitly acknowledge the external teacher dependencies alongside the loss-level simplifications, to avoid misleading readers about the pipeline's overall complexity.
4. **Add pseudo-label agreement analysis**: Report per-teacher agreement rates (e.g., average pixel distance between teacher tracks on the same video, correlation of occlusion predictions) to quantify complementarity beyond the ablation.
5. **Consider reframing the headline contribution** around the saturation finding ("point tracking with pseudo-labelled real data saturates at ~30k videos") rather than the uncontrolled BootsTAPIR comparison, which would make the paper more defensible.

## Score and Decision

**Originality**: Good — the architecture simplification and multi-teacher training recipe are novel contributions, and the scaling study is the first of its kind for point tracking.  
**Importance of research question**: High — reducing the data requirement for point tracking is practically significant.  
**Claims support**: The main empirical results are well-supported by thorough experiments, but the "1,000× less data" claim would benefit from a controlled comparison.  
**Soundness**: Strong ablations and scaling analysis; the method is clearly described and reproducible.  
**Clarity**: Well-written, with clear exposition of the architecture and training pipeline.  
**Value to community**: High — the simplified architecture, training recipe, and scaling insights will be useful for practitioners and researchers.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>