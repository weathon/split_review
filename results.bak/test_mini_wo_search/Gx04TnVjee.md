Now I have all evidence I need. Let me write the consolidated review.

## Summary

The paper introduces 3DTrajMaster, a method for controlling multi-entity 3D motions in text-to-video generation using 6DoF pose sequences. The core contribution is a plug-and-play object injector that uses entity-wise addition of text and pose embeddings followed by gated self-attention to associate entities with trajectories while preserving the base model's prior. To address the lack of training data, the authors construct a synthetic 360°-Motion Dataset (54,000 clips from UE) and introduce a LoRA-based domain adaptor plus annealed sampling to mitigate domain shift. The paper tackles a meaningful and under-explored problem.

## Strengths

- **First to address multi-entity 6DoF motion control in 3D for video generation.** The paper convincingly identifies a gap: existing 2D methods (MotionCtrl, Tora, Direct-a-Video) cannot represent rotation, depth order, or entity-to-trajectory correspondence in 3D (Section 2, Table 1). This is a genuine limitation of prior work, and 3DTrajMaster is the first to propose a solution.

- **Clean, well-motivated architecture.** The entity-wise addition of frozen text embeddings and learnable pose embeddings, followed by gated self-attention that reuses the base DiT's 2D spatial attention weights (Section 3.2, Eq. 2), is simple and principled. The design preserves the video diffusion prior, which is supported by the qualitative generalization results (Figure 5). The ablations comparing gated self-attention vs. cross-attention and placement after 2D vs. 3D self-attention confirm the design choices (Table 4/ablations).

- **Domain adaptation pipeline addresses a real practical challenge.** The LoRA-based domain adaptor (trained first, then frozen during injector training) and annealed sampling strategy (Algorithm 1) are reasonable engineering solutions to the domain gap introduced by the small synthetic dataset. Ablation results (Table 4 main, Figure 5 in paper) quantitatively confirm that both components are necessary — without the adaptor, FVD degrades sharply (272.3 vs. 161.9), demonstrating a genuine domain shift problem that the proposed components mitigate.

- **Qualitative results show convincing generalization beyond training categories.** Figure 5 demonstrates successful control over humans, animals, cars, robots, and abstract entities across multiple backgrounds (city, desert, forest). Figure 6 shows fine-grained editing of human attributes (hair, clothing, figure size) while preserving trajectories. These qualitative results support the paper's claim that the injector preserves the base model's prior.

## Weaknesses

### Fatal
None.

### Major
- **The proprietary base model confounds the main comparison.** 3DTrajMaster is built on an internal 1B-parameter video diffusion model, while all baselines (MotionCtrl, Tora, Direct-a-Video) use publicly available models. The performance gap in Tables 2–3 could partly stem from the base model quality rather than the proposed injector. The ablations compare design variants *within* the same base model, which confirms architectural choices but does not isolate the injector's contribution from the base model's innate capability. The paper does not acknowledge this limitation. A control experiment (e.g., injecting similar conditioning into an open-source backbone or comparing base-model-only outputs on a motion-following task) would substantially strengthen the evidence.

- **Quantitative evaluation is limited to humans on synthetic data.** Due to the absence of a pose estimator for open-world 4D objects, the paper explicitly limits quantitative metrics (RotErr, TransErr, FVD, FID, CLIPSIM) to human entities (Section 4.3). The test set (100 pairs) uses novel pose templates and GPT-generated descriptions but is rendered with the same UE pipeline as training — it is not out-of-distribution. The paper claims "generalization" and "multi-entity" control, but these are supported only by qualitative examples for non-human entities (Figure 5) and not measured on real-world videos. This is a significant gap between the scope of the claims and the quantitative evidence provided. The paper should either evaluate on a real dataset with estimated 3D poses (e.g., AMASS, Human3.6M) or, failing that, discuss the limitation more prominently.

### Minor
- **Annealed sampling hyperparameter \(T_c\) is not reported in the main text.** The critical timestep threshold that controls the trade-off between motion guidance and video quality is deferred to the supplementary (Algorithm 1 refers to \(T_c\) but no value is given). Without this value, readers cannot assess the sensitivity of the method to this hyperparameter from the main paper.

- **The domain adaptor (LoRA) is trained before the injector and then frozen without justification.** Section 3.3 states that the adaptor is trained first and frozen during injector training (line 148), but does not discuss whether joint training or iterative refinement was considered. While the two-stage approach is plausible, explaining the rationale would strengthen the method section.

- **No analysis of failure cases.** The limitations section (line 241–243) discusses scope boundaries (local motions, entity count) but does not discuss specific failure modes — e.g., what happens with three entities whose trajectories overlap in 3D space, whether ghost artifacts or entity blending occur, or how motion accuracy degrades as entity count increases. Including even one failure case would improve the paper's rigor.

- **The negative motion prompt idea is mentioned but dismissed without analysis.** Section 4 (inference) notes that static "negative" trajectories improve pose accuracy but cause quality decline, and the idea is not pursued. This is a minor loose end that could confuse readers; either removing it or providing a brief quantitative assessment would be cleaner.

### Trivial
None.

## Nice-to-Haves
- A user study asking raters whether generated motions match the intended 3D trajectory would provide a task-relevant, representation-agnostic evaluation signal.
- An ablation comparing a simple pose encoder (linear + interval sampling) to a temporally-aware one (e.g., small transformer) would strengthen the architecture justification.
- Quantitative evaluation on non-human entities using category-specific pose estimators (e.g., DensePose for animals) would broaden the evidence base.

## Removed Points
- **"Evaluation is not a fair test of the claimed contribution"** (Harsh Critic #1): REMOVED. The paper projects 3D trajectories to 2D for baselines, which is the standard way to compare methods with different input modalities when no 3D-aware baselines exist. The paper is transparent about this ("It is not surprising that ours significantly outperforms all baselines" — line 218). The RotErr/TransErr metrics for 3DTrajMaster stand independently as measures of its own trajectory-following accuracy. The critic's complaint essentially demands a comparison against a non-existent method, which is not a valid weakness.

- **"Synthetic dataset is small and may not support generalization"** (Harsh Critic #4, part): REMOVED. The domain adaptor is explicitly designed to address this, and the paper shows it works (FVD 272.3→161.9). The claim that "FVD 161.9 is higher than typical values" is not contextualized against the specific evaluation set and cannot be verified from the paper alone. The qualitative results on diverse entities support the generalization claim.

- **"Pose encoder is too simple"**: REMOVED. The paper reports trying 1D convolutions with similar results (line 112). This issue is addressed.

- **"Negative motion prompt not adopted"**: REMOVED. The paper explains why (quality decline, line 151). This is a transparent discussion of an exploratory idea, not a weakness.

- **"Dataset release not mentioned"**: REMOVED per hard rule (cited references and project page are assumed to exist).

- **"Missing related works"**: REMOVED per hard rule.

- **"Granularity table is not a comparison"**: REMOVED. This is a standard capability taxonomy table, not a weakness.

- **Various formatting/style nitpicks**: REMOVED per hard rules.

- **Strengths that are generic or conflict with verified weaknesses**: The Strength Finder's claims about "state-of-the-art results" are retained but qualified by the major weaknesses above. Generic/superficial strengths from the Strength Finder (e.g., "addressed an important problem") are removed.

## Novel Insights
The most interesting observation from the cross-review synthesis is that the paper's key limitation is simultaneously its biggest strength: the method's reliance on a proprietary base model prevents clean attribution of the performance gains, but also allows the paper to demonstrate the injector at a scale (1B parameters) that would not be possible with any currently available open-source video DiT. This suggests that the research community would benefit most from an open-source re-implementation of the injector on a public backbone (e.g., an AnimateDiff / VideoCrafter variant) to independently validate and build upon the approach. The LoRA-based domain adaptor design is another transferable insight — applying a lightweight adaptor to absorb the synthetic-data style before training the actual controller is a clean two-stage recipe that other synthetic-data-driven video projects could adopt.

## Suggestions
1. **Acknowledge the base-model confound and add a control experiment.** If an open-source backbone experiment is feasible for the rebuttal, it would be the single most impactful addition. At minimum, discuss this limitation explicitly in the paper and compare the base model's motion-following capability (which should be near zero for explicit trajectory following) against the full method to isolate the injector's contribution.
2. **Add quantitative results on a real-world dataset.** Evaluate on AMASS or Human3.6M by estimating 3D poses from real video and using them as both input trajectories and ground truth for evaluation. This would demonstrate generalization beyond the synthetic domain.
3. **Report \(T_c\) and include a sensitivity analysis.** The annealed sampling threshold is a key hyperparameter; its value and the effect of varying it should be in the main paper.
4. **Add a failure case analysis.** Show examples where the method struggles (e.g., three entities with intersecting trajectories, or a non-human entity with complex motion) to establish the method's empirical boundaries.
5. **Rephrase "state-of-the-art" claims** to specify "state-of-the-art for 3D multi-entity motion control" given that no prior method addresses the same task.

## Score and Decision

**Evaluation axes:**
- **Originality:** High. First to tackle multi-entity 6DoF motion control in video generation with a clean, simple architecture.
- **Importance of research question:** High. Precise 3D motion control is a bottleneck for video generation in film, games, and simulation.
- **Claims supported:** Partially. The core architecture and dataset claims are well-supported. The "SOTA" claim is weakened by the proprietary base model confound and limited quantitative evaluation scope.
- **Soundness of experiments:** Adequate but with gaps. Ablations are thorough for design choices. The main comparison is confounded by different base models. Quantitative evaluation is limited to humans and synthetic data.
- **Clarity of writing:** Good. The method is clearly explained, the figures are informative, and the limitations are honestly stated.
- **Value to the community:** Moderate to high. The architecture and dataset construction pipeline are reusable, though the proprietary base model limits immediate reproducibility.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>