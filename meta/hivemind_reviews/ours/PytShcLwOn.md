Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper introduces the SIGHT task — generating 3D hand trajectories from a single image of an object, in two settings: with a hand already interacting or with the object pictured alone. The authors propose SIGHT-Fusion, combining off-the-shelf hand-object segmentation (VISOR-HOS), CLIP-based object and contact-region feature extraction, and a diffusion-based motion generator adapted from MDM. Benchmarks are constructed from FPHAB and HOI4D with carefully designed cross-instance and cross-location splits, and a physics-simulation evaluation (MuJoCo) provides a task-oriented metric. The paper opens a useful new direction at the intersection of hand motion generation and image-conditioned interaction understanding.

## Strengths

1. **Novel task formalization with two clearly defined settings.** Section 3.1 explicitly defines the SIGHT task for both hand-object interaction images and standalone object images, specifying the output representation (SMPL-X right hand, 17 joints, 6D pose). This formalization is absent from prior work, which focuses on static reconstruction or text-conditioned full-body motion.

2. **Cross-instance and cross-location splits for systematic generalization testing.** Section 4.1 describes two carefully constructed HOI4D splits that isolate cross-instance and cross-background generalization, going beyond standard within-dataset evaluation. The instance split tests unseen object instances without a hand in the frame; the location split tests generalization to novel environments.

3. **First physics-simulation evaluation of generated hand trajectories.** Section 4.6 and Table 4 report hit rates in MuJoCo for four manipulation tasks (pour juice, pour milk, pour liquid soap, put salt). The paper explicitly states this is the first evaluation of physical realism for generated trajectories using a physics simulator, providing a novel task-oriented metric beyond motion-only metrics.

4. **Part features demonstrably help disambiguate multi-affordance actions.** Table 3 focuses on three objects with multiple actions (open/close/pour) and shows that the part-feature variant (ACC=0.409) substantially improves over the object-only variant (ACC=0.212), providing direct causal evidence that contact-region features help resolve action ambiguity.

5. **Considerable quantitative improvements over baselines across multiple datasets.** On FPHAB (Table 1), SIGHT-Fusion achieves ACC=0.294 and FID=17.44 versus the best baseline (MDM-I: ACC=0.154, FID=28.22). On the HOI4D location split it achieves ACC=0.564 versus 0.514. These margins are large enough to suggest real gains even accounting for evaluation limitations.

## Weaknesses

### Fatal

None.

### Major

1. **The action classifier used for the ACC, FID, and DIV metrics is completely underspecified.** The paper states (Section 4.2) that ACC is measured via "the accuracy of an action classifier working on hand trajectories" and that FID/DIV are computed using features from the same classifier, but provides no details whatsoever about this classifier: not its architecture, training data, input representation, training split, or classification accuracy on ground-truth motions. Since ACC is the primary metric for evaluating "task-appropriateness" and the classifier's feature space underpins FID/DIV, this is a significant gap. If the classifier is weak or dataset-biased, all three metrics become unreliable. The paper cannot be properly evaluated without specifying this component.

### Minor

1. **No error bars, confidence intervals, or multi-seed statistics are reported for any metric.** All tables present point estimates without any measure of variance. For the physics simulation (Table 4), baselines occasionally outperform SIGHT-Fusion (e.g., MDM-T beats SIGHT-Fusion on the "put salt" task), and the paper itself notes that ground-truth trajectories can underperform generated ones — yet without repeated trials or variance estimates, it is impossible to know whether any of the reported differences are meaningful.

2. **Checkpoint selection on the test set.** The paper states (Section 4.2) that it selects the checkpoint with the lowest FID on the *test* set, citing this as consistent with prior work (Guo et al. 2022, 2020a; Tevet et al. 2022). While the paper is transparent about this practice, it does mean the reported metrics are optimistic estimates and may not reflect the performance of a fixed, non-optimized model. The paper would be stronger if results were also reported using a validation-based selection protocol or if the practice were justified more explicitly.

3. **The disambiguation experiment (Table 3) covers only 3 objects and lacks any statistical testing.** The increase from ACC 0.212 (object-only) to 0.409 (with part features) on such a small sample is suggestive but cannot be assessed for reliability. A few more object categories and some measure of variance across seeds or objects would substantially strengthen the claim.

4. **The quantitative generalization results (Table 2) only compare against a single baseline (MDM-I).** While the comparison shows large improvements (ACC 0.293 vs 0.157), having only one baseline for the cross-instance setting makes the evaluation less informative. Including text-based baselines or the object-only ablation on this split would strengthen the generalization analysis.

### Trivial

None.

## Nice-to-Haves

- An ablation that conditions MDM on exactly the same cropped-object CLIP features (without part features) on the *full* FPHAB and HOI4D datasets is what the paper's O model already provides. The critic's claim that this comparison is missing is incorrect — it is present in Tables 1, 2, and 3. However, it would be useful to report this explicitly as the critical ablation in a dedicated row or discussion.
- A few additional physics simulation tasks (e.g., open/close, rotate) and running multiple seeds per trajectory to estimate hit-rate variance would make the simulation evaluation more convincing.
- A discussion of failure cases or limitation-aware qualitative analysis would help bound the method's capabilities.

## Removed Points

These points were raised by the reviewers but are removed after careful verification against the paper:

- **Checkpoint selection as a "structural flaw" invalidating all results (Critic's Critical Issue 1, "Fatal" framing).** The paper explicitly states this practice is "consistent with the human motion generation literature" and cites Guo et al. (2022, 2020a) and Tevet et al. (2022). While not ideal, the paper is transparent about it and cites precedent. Demoted to Minor (see Weaknesses above). The claim that this "invalidates the primary evidence" is an overstatement not supported by how the field operates.

- **"MDM-I uses uncropped frames, making the comparison unfair" (Critic's Critical Issue 2, part 1).** MDM-I using uncropped frames is a reasonable baseline: it shows what happens when the raw image is fed into the same architecture without object detection or cropping. The paper's own O model (which uses cropped CLIP features) provides the fair ablation the critic asks for. This comparison is not unfair.

- **"MDM-T and T2M-T are weak baselines because LLaVa introduces translation errors" (Critic's Critical Issue 2, part 2).** This is exactly the point of including them — they represent the natural approach of using existing text-conditioned models with automatic captioning. Demonstrating that direct image conditioning outperforms the noisy VLM pipeline is a valid and informative comparison, not an unfair one.

- **"No comparison against object-features-only baseline" (Critic's Critical Issue 2, part 3).** Factually incorrect. The paper's O model in Tables 1, 2, and 3 is exactly this — MDM conditioned on the CLIP vector from the cropped object without part features. The critic appears to have missed this.

- **Section-by-section notes from the harsh critic about presentation, scope of related work, and the MDM adaptation being "straightforward."** These are either opinion, not specific weaknesses, or they misunderstand the paper's contributions. The methodological adaptation from whole-body to hand is non-trivial and paired with a novel feature extraction pipeline.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"). Strengths are only retained if they cite specific evidence from the paper. Generic praise is removed.

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is that the paper's core technical contribution — using dilated hand-object contact masks to extract localized CLIP features from interaction regions — is validated by the multi-affordance disambiguation experiment (Table 3), but this experiment is simultaneously the paper's smallest and least rigorous. If the authors could scale this analysis to more objects with statistical rigor, it would substantially strengthen the paper's central claim that part-level features are what make SIGHT-Fusion work. Conversely, without that scaling, the quantitative story rests heavily on an unspecified action classifier, which is the paper's weakest link. The physics simulation evaluation is genuinely novel and could become a signature contribution of this line of work if expanded.

## Suggestions

1. **Specify the action classifier.** Describe its architecture, training data, input representation, and accuracy on ground-truth motions. Without this, ACC, FID, and DIV are uninterpretable black-box metrics.
2. **Report multi-seed results with error bars or confidence intervals** for all metrics, ideally with a validation-based checkpoint selection protocol alongside the current test-set-based one for comparison.
3. **Expand the disambiguation experiment (Table 3)** to more object categories with multiple affordances and provide variance estimates.
4. **Add the object-only ablation (the O model) to Table 2's generalization analysis** so the contribution of part features in the cross-instance setting can be assessed.
5. **Add a limitations section** discussing failure modes, challenging object types, or cases where the method underperforms.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>