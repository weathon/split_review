I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper proposes RT-Trajectory, a novel policy conditioning method that uses coarse 2D trajectory sketches (drawn on a blank canvas and concatenated with RGB observations) to guide robot manipulation policies. The key insight is that rough trajectory sketches strike a balance between being expressive enough to convey motion guidance and coarse enough to allow the policy to adapt to situational visual context. The authors train on hindsight trajectory labels automatically extracted from existing demonstration data and evaluate on 7 unseen manipulation tasks with diverse trajectory generation methods (human drawings, human videos, LLM-generated code-as-policies, and image generation models). The method achieves 67% success on unseen tasks, significantly outperforming RT-1 (16.7%), RT-2 (11.1%), and RT-1-Goal (26%). A motion-similarity analysis using Fréchet distance confirms that the evaluation tasks genuinely test novel motion generalization.

## Strengths

- **Strong quantitative generalization results**: On 7 unseen manipulation tasks, RT-Trajectory (2.5D) achieves 67% overall success vs. 26% for the best baseline (RT-1-Goal) and 16.7%/11.1% for language-conditioned policies (RT-1/RT-2). This gap is large and consistent across diverse tasks including deformable object manipulation and underactuated systems (Section 4.2, lines 175-180).

- **Multiple trajectory generation modalities validated at inference**: The paper quantitatively demonstrates that the same trained policy can be conditioned by human-drawn sketches, trajectories from human demonstration videos (94% pick, 75% fold towel), and LLM-generated waypoints via Code as Policies (89% pick), plus qualitative examples from image generation models (Section 4.3, Tables 1-2). This strongly supports the claim that trajectory sketches are a practical, versatile interface.

- **Rigorous motion-similarity analysis**: The paper introduces discrete Fréchet distance to quantify how dissimilar evaluation trajectories are from training trajectories, showing that unseen tasks have larger distances, different skill semantics, and misaligned interaction heights (Section 4.5, Figures 6-9). This provides concrete evidence that the benchmark genuinely tests novel motion generalization rather than interpolation.

- **Emergent visual prompt engineering**: The paper demonstrates that changing the trajectory sketch for the same initial scene produces different, reproducible behaviors (Section 4.4) — a property unique to trajectory conditioning that enables zero-shot behavior modification without retraining.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The paper does not characterize how human-drawn test-time sketches differ from hindsight training trajectories**, raising a potential confound. In the main evaluation (Section 4.2), human-drawn sketches created via GUI over the initial camera image are purpose-built for each trial, while training trajectories are automatically extracted hindsight labels from teleoperation. These may differ systematically in smoothness, clarity, or scene alignment. Although Sections 4.3 partially mitigates this by showing success with other sketch generation methods, the headline results use human-drawn sketches exclusively. A characterization of how test-time sketches compare to training trajectories on measurable properties would strengthen confidence that the results reflect generalization rather than higher-quality inputs.

- **Limited probing of how the policy actually uses the sketch.** The paper does not analyze whether the policy learns genuine spatial interpretation of the sketch (e.g., following the path in the image plane) or a more brittle association between sketch-observation pairs and actions. The impressive empirical generalization partially addresses this concern, but targeted experiments — such as testing with shifted, rotated, or physically inconsistent sketches — would more directly validate the claim that the policy achieves spatial understanding rather than exploiting correlations in the training data.

- **The motion generalization analysis (Section 4.5) computes Fréchet distances on *executed* rollout trajectories rather than on the *input* trajectory sketches.** It would be more informative to also compute distances between input sketches and training trajectories, to separate the policy's generalization from the sketch's inherent similarity to training motions.

### Trivial

- Success rates on the most challenging tasks (Fold Towel, Swivel Chair) are noticeably lower than on other tasks. The paper does not discuss why the method struggles on these tasks or what properties of the trajectory sketch are insufficient — a missed opportunity for insight (Section 4.2, Figure 3).

## Nice-to-Haves

- An ablation of the trajectory sketch components (temporal color grading, interaction markers, height channel) beyond the existing 2D vs. 2.5D comparison would help understand which elements carry the most value, especially for tasks requiring precise gripper interaction timing.
- A discussion of potential extensions to uncalibrated or moving cameras would broaden the method's practical applicability.
- The paper could benefit from an analysis of how varying the "coarseness" of the input sketch (e.g., subsampling waypoints) affects policy performance.

## Removed Points

- **Criticism that the comparison with language-conditioned baselines "conflates two different kinds of generalization":** This point is removed because the paper explicitly acknowledges that language-conditioned policies cannot handle semantically unseen instructions (line 178: "Language-conditioned policies struggle to generalize to the new tasks with semantically unseen language instructions"). Moreover, the paper also compares against RT-1-Goal (26%), which does not share this language limitation, and still achieves a 67% success rate. The paper's core claim is precisely that trajectory sketches carry more motion-relevant information — this is the contribution, not an unfair comparison. Criticizing the method for being more informative about motion than language instructions is like faulting a map for being more spatially informative than a verbal description.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's framing rather than offering orthogonal observations.

## Suggestions

- Add an analysis experiment testing the policy with spatially perturbed sketches (shifted, rotated, or scaling variants) to probe whether the policy genuinely interprets the sketch as a spatial guide or relies on brittle correlations. This would directly address the most significant open question about how the method works.
- Characterize the distributional properties (smoothness, noise, scene alignment) of the human-drawn test sketches vs. the hindsight training trajectories to rule out a quality-based confound in the headline results.
- Report per-task Fréchet distances on the *input* sketches (not just executed trajectories) to disentangle whether the generalization is driven by the sketch or the policy's execution.

## Score and Decision

This paper makes a clear, novel contribution: demonstrating that coarse trajectory sketches are a practical and effective conditioning signal that enables task generalization beyond what language- or goal-conditioned policies can achieve. The experiments are well-designed, the results are strong and consistent across multiple trajectory input modalities, and the motion-similarity analysis provides solid evidence that the evaluation genuinely tests novel generalization. The weaknesses are minor and addressable — they concern depth of analysis rather than validity of results. The paper deserves acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>