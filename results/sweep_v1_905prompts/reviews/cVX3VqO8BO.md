Now I have sufficient calibration. Let me write the final consolidated review.

**Round-1 bracket:** I identified this paper as plausibly sitting between 4.0 and 6.5 based on comparison to weak anchors (2.5-3.33), middle anchors (4.0-6.5), and strong anchors (8.0).

**Round-2 narrowing:** I pulled anchors inside the 5.0-6.5 band. HAMSTER (6.00, Accept) — hierarchical VLA with comparable complexity but stronger evaluation; HandsOnVLM (6.33, Reject) — hand-object VLM with similar underspecification issues; Grounding Robot Policies (5.33, Reject); VLP (5.50, Reject). UniHM has stronger novel contributions than these (morphology-agnostic codebook, physics refinement) but also more significant evaluation gaps (missing HOIGPT comparison, no tokenizer reconstruction eval). I anchor this paper below HAMSTER and HandsOnVLM.

**Final score:** 5.5 — the paper has meaningful architectural contributions but the evaluation is incomplete in ways that prevent full support of the claims.

---

## Summary

UniHM proposes a framework for generating dexterous hand manipulation sequences from free-form language instructions. The key components are: (1) a morphology-agnostic VQ-VAE codebook that maps heterogeneous hand types (MANO, Shadow, Allegro, etc.) into a shared discrete latent space via knowledge distillation; (2) a VLM (Qwen3-0.6B) trained with a progressive masking curriculum to generate token sequences conditioned on text, target trajectories, and object point clouds; and (3) a physics-guided dynamic refinement that applies Gauss-Newton optimization with contact, generative, and temporal priors. The paper evaluates on DexYCB and OakInk, reports real-world success rates, and ablates the main components.

## Strengths

- **Morphology-agnostic codebook with explicit cross-hand transfer.** The knowledge-distillation-based encoder alignment (Eq. 3) and the unified VQ codebook are a concrete, well-motivated mechanism for sharing discrete motion tokens across heterogeneous hand morphologies. The pose translation formula (Eq. 6) cleanly demonstrates how tokens can be decoded to different hands. This is the paper's most novel contribution.

- **Well-formulated physics-guided refinement.** The energy-based optimization (Eq. 11–18) combines contact-aware distance penalties (with an asymmetric smooth function), a generative prior to preserve VLM intent, and temporal smoothness regularizers, solved via Levenberg-Marquardt Gauss-Newton. The ablation (Table 4) shows removing this refinement increases MPJPE from 61.40→65.78 and FID from 31.24→33.57, quantitatively confirming its contribution.

- **Learning from human video without teleoperation data.** The training pipeline relies solely on HOI datasets (DexYCB, OakInk) with GPT-4o-annotated language, avoiding costly robot teleoperation collection. The decoupled architecture (CLIPort for perception, VLM for HOI generation) is a sensible design choice that enables targeted fine-tuning of only the perception module at deployment time.

## Weaknesses

### Major

- **Missing comparison to HOIGPT, the closest prior work on text-to-HOI sequence generation.** HOIGPT (Huang et al., 2025) is cited in related work but never compared against experimentally. It learns a bidirectional mapping between text and HOI sequences using VQ tokenization — the same problem class as UniHM. The paper claims "the first unified framework" for this task, but without comparing to HOIGPT (or explaining why HOIGPT is not applicable), this claim is unsupported and the SOTA results in Tables 1–2 lack a critical reference point. The paper should either compare to HOIGPT or clearly delimit why HOIGPT's setting (digital hand, no robot morphologies) makes direct comparison infeasible, and then adjust the "first" claim accordingly.

- **No VQ-VAE reconstruction quality reported for any hand morphology.** The entire pipeline depends on the codebook's ability to faithfully encode and decode hand poses across five morphologies. Yet the paper reports zero reconstruction error, codebook usage statistics, or per-morphology decoding accuracy. This is a fundamental gap: if the tokenizer introduces large errors (especially on less common hands like Leap or Panda), the downstream VLM and physics refinement operate on a distorted representation. The paper must provide reconstruction metrics (e.g., MPJPE between original and decoded poses) per hand type.

- **CLIPort-style trajectory decoder is underspecified.** The paper states that a CLIPort-style module outputs an SE(3) target trajectory from RGB-D + instruction (Eq. 7), but provides no architecture details, training data, or decoding mechanism for how a module originally designed for pixelwise affordance heatmaps is adapted to produce full 6-DOF waypoints. The paper mentions an "MLP-based trajectory encoder" but does not describe the CLIPort module's output head or training procedure. Given that at inference CLIPort estimates the target trajectories that condition the entire VLM generation (Eq. 9), this is a significant gap that prevents independent reconstruction of the method.

### Minor

- **Real-world evaluation lacks protocol details.** Table 3 reports success rates of 60–65% (UniHM) vs. 25–45% (MotionGPT3) across four task categories, but does not specify: the number of trials per task/condition, how success is defined per category, which robot hand was used, how object poses were varied, or whether instructions were hand-picked. Without these details, the dramatic gap over baselines cannot be properly assessed.

- **Training/inference distribution shift not analyzed.** The VLM is trained on ground-truth target trajectories and object point clouds, but at inference uses CLIPort estimates of both. The paper acknowledges this modular design but provides no analysis of how CLIPort errors propagate — e.g., what fraction of failures in real-world or simulation results can be attributed to CLIPort vs. the VLM vs. the physics refinement. A robustness study (varying CLIPort noise levels) would be informative.

- **Evaluation metric computation is ambiguous.** The paper computes MPJPE, FOL, FPL, FID, and Diversity against "ground truth" from DexYCB/OakInk. These datasets contain MANO (human hand) parameters, while UniHM outputs robot hand poses (Shadow, Allegro, etc.). It is unclear whether the GT was retargeted into each robot hand space via the same pipeline used for training data, or whether metrics are computed in MANO space (which would require mapping robot poses back). This ambiguity affects the interpretability of all quantitative results.

- **"First framework" claim is overstated.** Given HOIGPT's existing text-to-HOI sequence generation, the paper should qualify what "unified" and "first" refer to — specifically, the morphology-agnostic cross-robot-hand aspect — rather than claiming "the first framework for unified dexterous hand manipulation guided by free-form language commands" (Abstract) and "the first unified, language-conditioned framework for dynamic dexterous hand manipulation" (contributions).

### Trivial

- None that are not covered above.

## Nice-to-Haves

- Ablate the masking schedule (e.g., compare progressive masking vs. constant masking at fixed rates) rather than only comparing "with vs. without masking."
- Add a simulation-based physical feasibility metric (e.g., penetration depth, contact stability) in addition to pose errors.
- Include a failure-mode analysis for real-world experiments tracing errors to specific modules (CLIPort, VLM, tokenizer, refinement).

## Removed Points

- **Criticism that the paper might not have a working trajectory planner at all / might rely on GT trajectories at inference (Harsh Critic Point 1, speculative-fatal framing).** The paper clearly states it trains with GT trajectories and uses CLIPort at inference (Section 3.3, Inference Stage). The CLIPort module is underspecified, but the claim that the method might "rely on ground-truth trajectories at inference (which would invalidate the claimed contribution)" is unsupported speculation. Demoted from "fatal" to the Major weakness above (underspecified CLIPort).
- **Criticism that FID/Diversity values differ by "orders of magnitude" between datasets (Harsh Critic Point 3).** DexYCB FID ranges 31–56, OakInk FID ranges 205–337 — a factor of ~5–6, not "orders of magnitude." OakInk is a larger and more diverse dataset, so different FID scales are expected and standard in the literature. Removed as factually inaccurate.
- **Criticism about contact energy only considering fingertips (Harsh Critic, Physical Refinement).** This is a legitimate design choice; the paper acknowledges "simplified energy terms for contact and friction" in the conclusion. It is not a flaw — it is a scoped design decision. Demoted to nice-to-have.
- **Criticism about frame-by-frame optimization not ensuring long-horizon feasibility (Harsh Critic, Physical Refinement).** The paper designs the refinement as frame-by-frame causal optimization; this is an explicit design choice with advantages (computational efficiency) and acknowledged limitations. Not a flaw per se.
- **Criticism that "no statistical significance tests are reported" (Harsh Critic, Experiments).** The paper reports standard deviations across runs (± values in tables), which is the standard practice for this domain. Requesting formal significance tests is not standard for this type of benchmark evaluation. Removed.
- **Strength Finder items about SOTA/results.** The SOTA claims are supported by the tables but tempered by the baseline comparison concerns (missing HOIGPT). Kept as strength with implicit caveat that baselines are limited.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a quantitative comparison to HOIGPT (or clearly justify why direct comparison is infeasible and adjust the "first" claim accordingly).
2. Report VQ-VAE reconstruction error (MPJPE between original and decoded poses) for all five hand morphologies, plus codebook usage statistics.
3. Provide full architecture details of the CLIPort-style trajectory module (output head, training data, loss function).
4. Add real-world experiment protocol details: number of trials per condition, success criteria, robot hand used, and randomization procedure.
5. Clarify whether evaluation metrics are computed in MANO space or retargeted robot hand space, and if retargeted, describe the pipeline.

## Score and Decision

**Round-1 bracket:** Between 4.0 and 6.5. Weak anchors (2.5–3.33, papers with vague methods or minimal results) are clearly below this paper. Strong anchors (8.0, top papers with complete evaluations) are clearly above.

**Round-2 narrowing:** Anchors inside the bracket: HAMSTER (6.00, Accept) — comparable complexity, stronger evaluation; HandsOnVLM (6.33, Reject) — similar hand+VLM topic and similar underspecification; Grounding Robot Policies (5.33, Reject); VLP (5.50, Reject). UniHM has more novel technical components than these anchors (morphology-agnostic codebook, physics refinement) but also more significant evaluation gaps (missing HOIGPT comparison, no tokenizer reconstruction quality, underspecified CLIPort). It sits below HAMSTER and HandsOnVLM in overall evidence quality.

**Anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| xcHIiZr3DT | 2.50 | 1 (weak) | Much weaker: simple vision-based tactile method |
| sXF5P4N7e8 | 3.00 | 1 (weak) | Much weaker: basic goal-conditioned grasping |
| KBSHR4h8XV | 3.33 | 1 (weak) | Weaker: early fusion VLA with limited results |
| q1Cv7Hp52y | 3.00 | 1 (weak) | Much weaker: neuro-symbolic RL |
| 29p13QihRM | 4.00 | 1 (mid) | Weaker: world model for predictive control |
| Aqfwhna1D7 | 5.20 | 1 (mid) | Comparable: CrayonRobo has similar evaluation gaps |
| lFYj0oibGR | 6.50 | 1 (mid) | Stronger: RoboFlamingo has more complete evaluation |
| AJQuTFd9es | 6.33 | 1 (mid), 2 (narrow) | Comparable but slightly stronger: HandsOnVLM accepted one reviewer gave 8 |
| 7gUrYE50Rb | 8.00 | 1 (strong) | Much stronger: top-tier embodied QA work |
| OI3RoHoWAN | 8.00 | 1 (strong) | Much stronger: GenSim |
| KsUh8MMFKQ | 8.00 | 1 (strong) | Much stronger: differentiable physics |
| 7BLXhmWvwF | 8.00 | 1 (strong) | Much stronger: geometry-aware RL |
| twIPSx9qHn | 5.00 | 2 (narrow) | Comparable: Cross-Embodiment Dex Grasping with RL |
| NxoFmGgWC9 | 5.50 | 2 (narrow) | Comparable: video pre-training for manipulation |
| RhfYIJux9d | 5.50 | 2 (narrow) | Comparable: Video2Policy |
| h7aQxzKbq6 | 6.00 | 3 (narrow) | Stronger: HAMSTER has more thorough evaluation |
| Afjf6izLvJ | 5.33 | 3 (narrow) | Comparable but slightly weaker |
| blwWIKpwpL | 5.50 | 3 (narrow) | Comparable: VLP |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>