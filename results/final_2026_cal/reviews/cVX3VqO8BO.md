Now I have a good understanding of the paper and the calibration landscape. Let me write the final review.

## Summary
UniHM introduces a framework for generating sequential dexterous hand manipulation trajectories from open-vocabulary language instructions and RGB-D images. The method combines (1) a unified VQ-VAE tokenizer that maps heterogeneous hand morphologies to a shared codebook via cross-hand knowledge distillation, (2) a small VLM (Qwen3-0.6B) trained with a progressive masking curriculum for language-conditioned token sequence generation, and (3) an energy-based physics-guided refinement postprocessor that enforces contact and temporal smoothness. The model is trained on human-object interaction data (DexYCB, OakInk) without teleoperation data, retargeting MANO poses to five robot hands, and evaluated via standard motion generation metrics plus real-world trials.

## Strengths
- **First unified framework for language-conditioned dynamic dexterous manipulation on robot hands.** The paper goes beyond static grasp generation (SemGrasp, AffordDexGrasp, etc.) to produce full manipulation sequences conditioned on open-vocabulary instructions, which is a genuine and nontrivial advance. Tables 1 and 2 show consistent improvements over human-motion-generation baselines on both DexYCB and OakInk across seen/unseen splits (e.g., DexYCB seen MPJPE: 61.40 vs. 74.80 for MotionGPT3; unseen MPJPE: 63.56 vs. 77.93).
- **Morphology-agnostic codebook with cross-hand distillation (Eq. 3–6).** The staged training protocol (reference encoder → distillation → fine-tuning with shared codebook) provides a practical recipe for extending to new hand morphologies without retraining from scratch. The unified hand pose translation (Eq. 6) is clean and well-motivated. Real-world success in Table 3 (e.g., 65% Grab seen, 60% Grab unseen) provides concrete evidence that the tokenizer enables cross-morphology transfer.
- **Physics-guided dynamic refinement improves quantitative metrics (Table 4 ablation).** Removing physical refinement degrades all metrics (DexYCB seen: MPJPE from 61.40→65.78, FID from 31.24→33.57), confirming the module contributes meaningfully. The Gauss-Newton formulation with Levenberg-Marquardt damping (Eq. 17-18) is technically sound.
- **Training without teleoperation data.** The model learns from retargeted human-object interaction data, eliminating the need for expensive robot teleoperation data collection. The 60% unseen "Grab" rate and successful real-world results on novel objects (Table 3) demonstrate this paradigm's viability.
- **Decoupled architecture for data-efficient domain adaptation.** Separating scene perception (CLIPort) from HOI generation allows fine-tuning only the perception component under distribution shift. The ablation showing large degradation without depth input (unseen MPJPE: 63.56→90.12) confirms the perception module's importance.

## Weaknesses

### Major
- **Evaluation metrics primarily measure similarity to retargeted human poses, not manipulation quality directly.** The main quantitative metrics (MPJPE, FOL, FPL, FID) compare generated robot-hand sequences to ground-truth sequences that are themselves retargeted from human MANO poses via Dex-Retargeting. A sequence that closely matches a retargeted human pose may not be the most physically feasible robot manipulation, and a physically correct manipulation that deviates from the human motion would be penalized. The real-world experiments (Table 3) partially address this by directly measuring task success, but these are limited to four coarse task categories on a single unspecified robot hand with no trial counts or confidence intervals. The paper would be substantially stronger with simulation-based task-completion metrics (e.g., object-pose change, contact stability under physics) as primary evidence, with the motion-similarity metrics as secondary diagnostics.

### Minor
- **Missing details in the real-world evaluation.** The paper does not specify which robot hand is used in Table 3 (among Shadow, Allegro, SVH, Leap, Panda), the number of trials per condition, or provide confidence intervals for the success rates. Given the modest success rates (35–65%), these details are important for assessing reliability. The real-world results also only show successful examples (Fig. 3, Fig. D2); failure case analysis would be informative.
- **The physics refinement optimizes the hand to track a predetermined object trajectory (𝒯ₜₐᵣ(t) from CLIPort), rather than modeling the hand as the cause of object motion.** The contact energy (Eq. 11) treats the object trajectory as given and optimizes fingertip positions to maintain contact with the moving surface. For tasks like "open the lid" or "pull the drawer," this is a reasonable decomposition (the trajectory encoder predicts the intended object motion, and the hand optimizer figures out how to effect it), but the paper does not discuss this assumption or its limitations. The refinement is closer to trajectory-conditioned contact optimization than to full manipulation dynamics.
- **No statistical significance testing.** Metrics are reported with standard deviations, but there are no formal significance tests. Some comparisons have overlapping error bars (e.g., Table 2 unseen: Ours MPJPE 58.62±2.35 vs MotionGPT3 61.95±2.48), making it unclear which differences are reliable.
- **Annotation quality not validated.** The GPT-4o-based language annotation pipeline (Section 3.1) is described but no quality metrics, human evaluation, or consistency checks are reported for the generated instructions. Since the VLM's training depends on these annotations, some validation would strengthen the method.
- **Dex-Retargeting dependency.** The training pipeline for each robot hand relies on retargeting human MANO poses via an external pipeline (Dex-Retargeting + physics optimization). Data quality depends on this retargeting quality, but this dependency is not discussed or analyzed.
- **Limited baselines and scope of comparison.** The baselines (TM2T, MDM, FlowMDM, MotionGPT3) are human motion generation models adapted via retargeting. While the paper correctly notes that no direct competitor exists for this specific task (language-conditioned dynamic robot-hand manipulation), the comparison is informative but limited. A stronger evaluation would additionally compare variants of the authors' own pipeline (e.g., replacing the VLM with a standard transformer decoder) to isolate the value of the language model.

### Trivial
- The 80/20 "seen/unseen" split is described but the paper does not specify which objects/trajectories are in the unseen set or how many.
- The description of the CLIPort-style vision module and MLP trajectory encoder lacks architectural detail (input/output dimensions, number of layers, training procedure).

## Nice-to-Haves
- **Simulation-based task-completion evaluation:** Running the generated sequences in a physics simulator (e.g., Isaac Gym, MuJoCo) to measure task success (object displacement, contact stability, grasp robustness) would directly address the primary evaluation concern and substantially strengthen the paper.
- **Cross-hand transfer quantification:** Show quantitative reconstruction/translation errors across the five hands. Demonstrate that a sequence generated for one hand can be translated to another with maintained functionality.
- **Ablation on the VLM design choice:** Replace the VLM with a non-pretrained transformer decoder of similar size to isolate the benefit of language pretraining.
- **Failure case analysis for real-world experiments.**

## Removed Points
- *"The paper does not compare against SemGrasp, DexGYS, AffordDexGrasp, HOIGPT"* — These methods generate static grasps (SemGrasp, DexGYS, AffordDexGrasp) or target human/digital hands (HOIGPT), not dynamic robot-hand manipulation sequences. The paper's claim is specifically about dynamic dexterous robot-hand manipulation, so these are not directly comparable baselines. The choice of human motion generation models adapted via retargeting is a reasonable baseline for this new task.
- *"Missing implementation details for reproducibility (training hyperparameters, codebook size, etc.)"* — These details are likely in the appendix, which was stripped by the PDF parser. The paper references appendix content throughout.
- *"The physics refinement has a logical flaw: it assumes the object trajectory is independent of the hand."* — The refinement uses 𝒯ₜₐᵣ(t) from CLIPort, which is the *intended* trajectory based on the language instruction (e.g., "move the bottle to the box"). This is a design choice where CLIPort handles high-level planning and the refinement handles low-level contact optimization, not a logical inconsistency. The concern is now downgraded to a Minor weakness with proper framing.
- *Multiple formatting/style nitpicks and speculation about stripped appendix content.*

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add a simulator-based evaluation (Isaac Gym or MuJoCo) measuring task-completion rates, contact stability, and object-pose accuracy as primary metrics, with the current MPJPE/FID metrics as secondary diagnostics.
- Report trial counts, which hand is used, and confidence intervals for all real-world experiments, plus a breakdown of failure modes.
- Add a variant of your own pipeline that replaces the VLM with a non-pretrained transformer decoder to isolate the value of language pretraining.
- Validate the GPT-4o language annotation quality (e.g., human evaluation or agreement metrics on a held-out sample).

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched three bands:
- Weak band (score < 3.5): Retrieved papers at 1.50–3.00 (GenDexHand, executable concepts). UniHM is clearly stronger than these — it has real-world validation, a complete system, and standard-dataset evaluation.
- Middle band (3.5–7.5): Retrieved papers at 4.50–5.50 (VLBiMan 5.50, VLA-in-the-Loop 5.00, SynHLMA 5.50, CLUTCH 5.00). These are the most topically relevant anchors.
- Strong band (7.5+): Retrieved papers at 8.00–8.50 on unrelated topics (navigation foundation model, rotation estimation). These represent a clearly higher tier of contribution than UniHM.

**Bracket:** [5.0, 6.0] — the paper is comparable to the middle-band anchors.

**Round 2 (Narrowing):** Searched within (4.5, 7.0) for topically similar papers. Retrieved:
- SynHLMA (5.50, Reject): Hand-articulated object interaction, VQ-VAE + LLM. UniHM has stronger technical novelty (cross-hand codebook, real-world validation) and better evaluation breadth. **UniHM is comparable or slightly stronger.**
- CLUTCH (5.00, Accept Poster): Text-conditioned hand motion, VQ-VAE + LLM, dataset contribution. UniHM has more system-level contribution and real-world robot validation. **UniHM is stronger.**
- VLBiMan (5.50, Accept Poster): Bimanual VLM manipulation with real-world validation. VLBiMan has stronger real-world evaluation (4200 rollouts) but less technical novelty. **Roughly comparable.**
- VLA-in-the-Loop (5.00, Reject): VLA with world-model correction. UniHM has more architecture novelty. **UniHM is stronger.**

**Final score:** 5.5. This paper has genuine technical contributions (first dynamic dexterous manipulation from language, cross-hand codebook, physics refinement) and standard evaluation on two benchmarks with real-world validation. However, the primary evaluation metrics measure similarity to retargeted human poses rather than direct manipulation quality, and the real-world experiments lack key statistical details. These limitations are real but not fatal, placing the paper soundly in the "solid but with notable limitations" range alongside comparable anchors at 5.0–5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>