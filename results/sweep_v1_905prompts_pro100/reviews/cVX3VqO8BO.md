Now I have all the data I need. Let me compile the final review.

---

## Summary

UniHM proposes a framework for language-conditioned dexterous hand manipulation that combines three components: (1) a Unified Hand-Dexterous Tokenizer that maps heterogeneous hand morphologies into a shared VQ codebook via knowledge distillation, (2) a vision-language model (VLM) with progressive masking for instruction-conditioned manipulation sequence generation, and (3) a physics-guided dynamic refinement module that enforces contact, temporal smoothness, and generative constraints via per-frame Gauss-Newton optimization. The system is trained on human-object interaction data (DexYCB, OakInk) and evaluated on both datasets with held-out splits, plus real-world experiments on a dexterous robot hand. Results show consistent SOTA improvements over general text-to-motion baselines and strong ablations validating each component.

## Strengths

- **Unified tokenizer with cross-morphology distillation.** The shared VQ codebook plus knowledge distillation (Sec. 3.2, Eq. 3) for aligning new hand encoders to a reference encoder is a concrete and well-motivated design for cross-hand pose translation. The staged training procedure (reference encoder → distillation → joint fine-tuning with Eqs. 4-5) is a practical contribution for scaling to new morphologies.

- **Physics-guided refinement with verifiable impact.** The per-frame Gauss-Newton optimization (Sec. 3.4, Eqs. 11-18) combining contact, generative, and temporal priors is carefully formulated. Table 4 shows removing physical refinement increases MPJPE from 61.40mm to 65.78mm (seen) and degrades FPL from 12.15mm to 15.35mm, providing clear evidence that the refinement improves physical feasibility and precision.

- **Progressive masking curriculum reduces exposure bias.** The schedule that gradually replaces ground-truth poses with [MASK] tokens (Sec. 3.3, Eq. 10) is simple and effective. The ablation (Table 4) shows that disabling it raises MPJPE by >10mm on both seen and unseen splits, directly validating its importance for sequential generation stability.

- **Decoupled perception-generation architecture.** Using a separate CLIPort module for trajectory estimation (Eqs. 7-8) allows the main VLM to focus on HOI sequence generation, and only the smaller perception head needs fine-tuning under domain shift — a practical robustness advantage.

- **Real-world validation without teleoperation.** Table 3 reports success rates on a physical dexterous hand across Grab, Pick&Place, Pull&Push, and Open&Close tasks, with UniHM achieving 60-65% on seen Grab tasks vs. 20-45% for baselines. This demonstrates that the full pipeline (video-based training + tokenization + refinement) yields executable manipulation skills in the real world — a meaningful result for a system trained only on human video data.

## Weaknesses

### Fatal

None.

### Major

- **The "first unified framework" claim is overstated given cited prior work.** The paper claims to be "the first unified, language-conditioned framework for dynamic dexterous hand manipulation beyond static grasps" (Introduction, line ~45). However, the paper itself cites HOIGPT (Huang et al., 2025) in Sec. 2.2 as a method that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences." The paper attempts to distinguish itself by noting HOIGPT targets "Digital Hand" settings rather than robot hands with physical feasibility, but the unqualified "first" language in the abstract and introduction overstates the contribution. The paper would be stronger repositioned as advancing the state of the art through the unified tokenizer and physics refinement, rather than claiming primacy over all dynamic language-guided hand manipulation. This matters because it mischaracterizes the novelty landscape for readers and reviewers.

- **No quantitative cross-morphology evaluation of the tokenizer.** The unified tokenizer is presented as a central contribution enabling "direct token reuse and transfer across robotic and anthropomorphic hands" (contribution bullet 2). The paper mentions retargeting to five robot hands (Shadow, Allegro, SVH, Leap, Panda) in Sec. 3.1, but all quantitative pose-level results (Tables 1, 2) are on DexYCB and OakInk — both human-hand (MANO) datasets. The real-world experiments (Table 3) use a robot hand but report only binary success rates with no per-joint accuracy, temporal smoothness, or reconstruction fidelity metrics when decoding to a different morphology. Without experiments measuring the quality of cross-morphology translation (e.g., MPJPE when decoding MANO tokens to Allegro/Shadow joint configurations), the "morphology-agnostic codebook" claim remains largely unsubstantiated. This is the most significant gap between the paper's claims and its evidence.

- **The VLM's contribution is not disentangled from the physics refinement.** Table 4 shows the full pipeline outperforming "w/o Physical Refinement," confirming the refinement helps. However, there is no baseline that applies the same physics refinement to a non-learning initializer (e.g., a static grasp or heuristically interpolated trajectory) under identical metrics. Without this, we cannot tell whether the VLM provides a meaningful initial guess or whether the refinement alone could achieve comparable results from a trivial starting point. The ablation establishes that each component matters when *removed*, but does not establish that the VLM specifically adds value beyond what the refinement could recover. This weakens the evidence that the VLM-based generation is essential to final manipulation quality.

### Minor

- **No direct comparison to dynamic HOI methods.** The baselines (TM2T, MDM, FlowMDM, MotionGPT3) are general text-to-motion models adapted for hand manipulation. The paper cites HOIGPT as a closely related text-to-HOI method but does not include it as a baseline. While the paper positions HOIGPT as targeting "Digital Hand" rather than robot manipulation, a direct comparison — even on the human-hand (MANO) setting where both operate — would better contextualize UniHM's contribution and address the overclaim concern.

- **Real-world evaluation lacks statistical detail.** Table 3 reports success rates as percentages but provides no information on the number of trials per task, no standard errors or confidence intervals, and no breakdown of failure categories. Without this detail, the reported 60-65% success rates are difficult to interpret or compare rigorously against baselines. The qualitative results in Fig. 3 are helpful but do not substitute for quantitative rigor in the evaluation protocol.

- **Limited detail on CLIPort/perception module training.** Section 3.3 describes CLIPort's role in trajectory estimation at a high level but provides almost no information about how it is trained, what data is used, or how it handles open-vocabulary instructions. Given that CLIPort is the sole perception module at inference time and its outputs drive the entire pipeline, this under-specification is a reproducibility concern.

### Trivial

- The paper occasionally uses imprecise language such as "unequivocally affirm" (Sec. 4.3) when describing results, which inflates the rhetoric beyond what the evidence supports.

## Nice-to-Haves

- Sensitivity analysis of the physics refinement hyperparameters (contact weight λc, generative weight Wgen, velocity/acceleration weights). The current formulation has several tunable parameters with no discussion of how sensitive results are to their settings.
- Clarification of whether the CLIPort-predicted target trajectory T_tar is in object frame or world frame, and how the hand's wrist base pose is factored into the pipeline — this affects reproducibility.
- Cross-morphology quantitative results (MPJPE, FOL, FPL) when decoding MANO tokens to each robot hand (Allegro, Shadow, Leap, etc.), which would directly validate the tokenizer's central claim.
- The "w/o Masked Training" ablation would be strengthened by also testing unconditional vs. language-conditioned generation to isolate the importance of language understanding specifically.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "HOIGPT explicitly generates long 3D hand-object interaction sequences from text, which is precisely dynamic language-guided manipulation."** Partially removed — retained as a major weakness about the "first" claim being overstated, but softened because HOIGPT is positioned as targeting digital hands (MANO), not dexterous robot hands with physical feasibility. The distinction between digital hand animation and robot manipulation is genuine, though the claim language should still be tempered.

- **Harsh critic: "the use of GPT-4o for instruction annotation is practical but described without any analysis of annotation quality, consistency, or the effect of language diversity on training."** Removed. This is a minor methodological note about data annotation that does not bear on the core claims. Many recent papers use LLM-based annotation without formal quality analysis, and the annotations here are supplementary to the main pipeline.

- **Strength Finder: "Decoupled perception and generation architecture for inference-time robustness."** Partially retained. The architectural decoupling is a sensible design choice but the claimed robustness benefit (fine-tuning only CLIPort under domain shift) is not experimentally demonstrated — this is stated as an advantage without evidence. Kept as a supporting strength but noted as aspirational.

- **Strength Finder generic phrasing about "consistent state-of-the-art performance" and "strong generalization."** Removed as generic. Replaced with specific evidence from tables and ablations.

- **Harsh critic: "The paper lacks any evaluation of the tokenizer's reconstruction fidelity and cross-hand translation error."** Merged with the major weakness about missing cross-morphology evaluation.

## Novel Insights

None beyond the paper's own contributions. The combination of a morphology-agnostic VQ tokenizer with knowledge distillation for cross-hand alignment, coupled with progressive masking and physics-guided refinement, represents a reasonable engineering integration of known techniques rather than a fundamentally new insight. The most interesting technical contribution is the staged training procedure (reference encoder → distillation → joint fine-tuning) for scaling the tokenizer to new hand morphologies, but this is more of a practical recipe than a conceptual breakthrough.

## Suggestions

1. **Narrow the "first" claim.** Rephrase to emphasize what is genuinely new: e.g., "the first framework to combine a morphology-agnostic hand tokenizer with physics-guided refinement for language-conditioned dexterous manipulation." This accurately scopes the contribution without claiming primacy over all dynamic language-guided HOI work.

2. **Add a cross-morphology evaluation.** Even a modest experiment (e.g., encode MANO sequences → decode to Allegro and Shadow hands → report MPJPE/FOL/FPL) would substantially strengthen the tokenizer's central claim. This is the highest-leverage experiment to add.

3. **Add a VLM-disentanglement baseline.** Apply the physics refinement to a non-learning initializer (static grasp or interpolated trajectory) and report the same metrics. This would clarify whether the VLM is doing the heavy lifting or whether the refinement alone is sufficient.

4. **Report trial counts and error bars for real-world experiments.** At minimum, specify N trials per task and provide standard deviations or confidence intervals. This is standard practice for real-robot evaluation.

5. **Expand the CLIPort description.** Provide training data, loss function, and how open-vocabulary generalization is achieved. Even a paragraph in the main text would improve reproducibility.

## Score and Decision

### Calibration anchors used:

**Round 1 (bracketing):**
- `xcHIiZr3DT` (Vision-Based Pseudo-Tactile for Dexterous Grasping): 2.50 — much weaker than UniHM; limited to tactile perception with no language or sequence generation.
- `KBSHR4h8XV` (EF-VLA): 3.33 — weaker; limited architectural novelty, poor baselines, single environment.
- `twIPSx9qHn` (CrossDex): 5.00 — weaker; cross-embodiment grasping but limited real-world evaluation, performance drop on unseen hands, simpler contribution scope.
- `h7aQxzKbq6` (HAMSTER): 6.00 — comparable but weaker; hierarchical VLA for pick-and-place, sim-only evaluation, simpler tasks.
- `OI3RoHoWAN` (GenSim): 8.00 — stronger; clear contribution, thorough evaluation, substantial real-world impact.

**Round 1 bracket:** UniHM sits between 6.0 and 7.5. It is clearly stronger than CrossDex (5.0) and HAMSTER (6.0), but weaker than the 8.0 cluster (GenSim, etc.) due to overclaimed novelty and missing cross-morphology evaluation.

**Round 2 (narrowing):**
- `AJQuTFd9es` (HandsOnVLM): 6.33 — UniHM is stronger; HandsOnVLM predicts only hand trajectories (curves), not full pose sequences, and lacks real-robot validation. UniHM's full pipeline with physics refinement and real-world results is more compelling.
- `lFYj0oibGR` (RoboFlamingo): 6.50 — UniHM is comparable to slightly stronger; RoboFlamingo has cleaner ablation and strong CALVIN results but is sim-only and tackles simpler tabletop manipulation. UniHM handles the harder problem of dexterous hand manipulation with real-world validation, but has less rigorous isolation of component contributions.
- `9pKtcJcMP3` (Video Language Planning): 7.00 — UniHM is slightly weaker; VLP has a more conceptually novel contribution (video-as-dynamics), multi-platform real-world results, and clearer evaluation story. UniHM tackles a technically harder manipulation domain but the evaluation gaps (no cross-morphology, VLM not disentangled) hold it back.

**Final comparison:** UniHM is notably stronger than RoboFlamingo (6.50) in problem difficulty and real-world scope, but the overclaim issue and missing cross-morphology evidence prevent it from reaching Video Language Planning (7.00) territory. The paper makes real technical contributions (tokenizer design, physics refinement, progressive masking) with solid ablations, but the gap between claims and evidence on the core tokenizer contribution is the main limiting factor. Score: **6.5**.

### Evaluation axes:
- **Originality:** Moderate. The components (VQ-VAE tokenizer, VLM generation, physics optimization) are individually known; the integration across morphologies with distillation is the novel aspect.
- **Importance:** High. Language-conditioned dexterous manipulation is a significant open problem.
- **Claims supported:** Partially. Strong results on standard benchmarks and ablations, but core cross-morphology claim is unevaluated.
- **Soundness:** Moderate. The methodology is technically sound but the evaluation design has gaps.
- **Clarity:** Good. The paper is well-structured with clear notation.
- **Value to community:** Moderate-to-high. The tokenizer design and staged training procedure are reusable, and the real-world results are encouraging.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>