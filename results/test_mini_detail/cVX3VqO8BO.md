Now I have sufficient calibration. Let me compile the final review.

**Round-1 bracket:** Based on weak anchors (~3.0, all reject) and strong anchors (~8.0, all accept), the plausible score range is **4.5–6.5**.

**Round-2 narrowing:** I read 8 anchor papers across the middle band. UniHM is clearly stronger than Language-Conditioned IL (3.0), Make a Donut (5.25), and Grounding Robot Policies (5.33). It is comparable to GEVRM (6.0) and RoboFlamingo (6.0–6.5) but weaker than DexTrack (6.75). I settle at **6.0**.

---

## Summary

UniHM proposes a unified framework for generating dexterous hand manipulation sequences from open-vocabulary language instructions. The system combines (1) a morphology-agnostic VQ-VAE tokenizer with cross-hand distillation that maps multiple hand kinematics into a shared codebook, (2) a small VLM (Qwen3-0.6B) with progressive masking for sequence generation, and (3) a physics-guided Gauss-Newton refinement for physical feasibility. The method is trained on retargeted human-object interaction data and evaluated on DexYCB, OakInk, and real-world robot trials.

## Strengths

- **Morphology-agnostic codebook with cross-hand distillation (Section 3.2, Eq. 1–6):** The shared VQ-VAE codebook aligned via latent-space distillation (Eq. 3) is a principled solution to the cross-hand generalization problem. It allows a single discrete action space to serve multiple robot hand morphologies (Shadow, Allegro, SVH, Leap, Panda) and enables direct pose transfer between hands (Eq. 6). This is a genuine technical contribution that addresses a real bottleneck in prior work.

- **State-of-the-art quantitative results on standard benchmarks (Tables 1, 2):** UniHM achieves the best MPJPE, FOL, FPL, and FID on both DexYCB and OakInk across seen and unseen splits, with substantial margins (e.g., MPJPE 61.40 vs. 74.80 for MotionGPT3 on seen DexYCB). On OakInk, UniHM's Diversity (165.47) is closest to ground truth (147.40), outperforming all baselines by a wide margin.

- **Real-world validation with significant improvement over baselines (Table 3):** UniHM achieves 65% success on seen "Grab" and 60% on unseen "Grab," compared to at most 30% and 45% for the best baseline (MotionGPT3+Dex-Retargeting). These real-world results provide direct evidence that the framework produces executable manipulation, not just plausible kinematics.

- **Comprehensive ablation studies (Table 4):** Each component is ablated (w/o Depth Input, w/o Masked Training, w/o Physical Refinement) with clear degradations. The progressive masking curriculum is shown to be particularly important (MPJPE 73.41 without it vs. 61.40 with it), and the physics-guided refinement yields consistent improvements across all metrics.

- **Decoupled architecture for data efficiency (Section 3.3):** Separating scene perception (CLIPort) from HOI generation (VLM) is a practical design choice. Since only the smaller CLIPort module needs fine-tuning for environmental shifts, this addresses the scarcity of dynamic dexterous-hand data.

## Weaknesses

### Fatal
None.

### Major

- **Diversity gap on DexYCB is unaddressed (Table 1):** On DexYCB (seen), UniHM achieves Diversity = 39.62 while the ground truth is 125.53 — only 31.5% of the reference diversity. Baselines like MotionGPT3 (72.51) and FlowMDM (61.25) produce substantially more varied motions. The paper defines Diversity as "closer to the ground truth indicates a more reasonable generation" but never discusses why UniHM underperforms baselines on this metric on DexYCB. Since generating "human-like manipulation sequences" is a stated goal, this discrepancy undermines a core claim. Notably, on OakInk (Table 2) the diversity issue reverses — UniHM is closest to GT (165.47 vs. GT 147.40) — suggesting the problem is dataset-specific, but the paper provides no explanation for this asymmetry.

- **Real-world experiments lack essential details (Table 3, Section 4.3):** The paper reports success rates for four task types but omits: the number of trials per condition, which robot hand was used, the task execution pipeline (control frequency, how generated poses are executed on hardware, whether physics refinement runs online or offline), and the criteria for success. Without these details, the real-world results cannot be properly assessed or reproduced.

### Minor

- **CLIPort object trajectory prediction is not evaluated (Section 3.3):** The entire inference pipeline depends on CLIPort for estimating the target trajectory 𝒯ₜₐᵣ (Eq. 7). If CLIPort produces poor trajectories, errors propagate to the VLM. The paper provides no evaluation of CLIPort's trajectory prediction accuracy or failure cases, making it impossible to isolate errors in perception vs. generation.

- **Small standard deviations may reflect limited diversity (Tables 1, 2):** Several of UniHM's standard deviations are notably tight (e.g., FPL of 12.15±0.24 on seen DexYCB, Diversity of 39.62±0.66). While not necessarily an error, this pattern is consistent with the low diversity observed on DexYCB and suggests the model may be overly deterministic.

### Trivial
- Table 1 has a typo: "± 341" should be "± 3.41" (TM2T's MPJPE standard deviation appears misformatted).

## Nice-to-Haves
- A standalone evaluation of the physics-guided refinement module on physical metrics (penetration depth, contact forces, joint limit violations) rather than just MPJPE.
- An analysis of the auto-annotation's impact: does using GPT-4o-generated instructions help compared to ground-truth dataset labels?
- Reporting of computational cost (training time, inference latency, refinement runtime).
- A version of the diversity analysis that separates cross-prompt vs. within-prompt variance to better understand the source of the DexYCB diversity gap.

## Removed Points
These points from the inputs were removed with justification:
- **"Evaluation on retargeted data is invalid":** The harsh critic claimed that evaluation against retargeted human ground truth is not a valid substitute for robot manipulation. This evaluation protocol is standard practice in the field (all cited baselines use the same protocol), and the paper additionally provides real-world experiments (Table 3) that directly test physical feasibility. Not a structural flaw.
- **"Tokenizer training is circular":** The harsh critic claimed that retargeting is needed to generate training pairs for the tokenizer, creating circularity. The paper explicitly states that Dex-Retargeting (Qin et al., 2023) is used for this purpose (Section 3.1), which is a standard, published retargeting method. The criticism depends on assuming the retargeting is unreliable without evidence.
- **"Physics refinement is standard / not novel":** That the Gauss-Newton optimization is a standard tool does not diminish its contribution within a novel pipeline. The ablation (Table 4) confirms it provides meaningful improvement. Novelty is assessed at the system level, not on individual components in isolation.
- **"Claim of 'first' is misleading":** While HOIGPT (Huang et al., 2025) generates HOI sequences from text, it targets a single hand model (Digital Hand) and does not provide cross-hand tokenization, physics refinement, or multi-morphology generalization. The paper's claim is qualified ("beyond static grasps," "unified") and reasonably scoped.
- **Missing HOIGPT comparison / missing related work:** Per meta-reviewing rules, I cannot flag missing related works.
- **Missing appendix/proof details, typos, formatting issues, etc.:** These are parser artifacts, not author errors.
- **Several strength-finder strengths that were generic** ("the paper addresses an important problem," "the paper is well-written") removed as superficial.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's observation about the diversity gap on DexYCB (unaddressed in the paper) and the reviewer's notice about the asymmetry between DexYCB and OakInk diversity results are worth flagging but emerge from reading the tables, not from external synthesis.

## Suggestions
1. **Analyze the diversity gap on DexYCB.** Investigate whether it stems from the VLM's small capacity (0.6B), the masking curriculum, codebook collapse during VQ training, or characteristics of the DexYCB retargeted data distribution. Report results separately for cross-prompt and within-prompt diversity.
2. **Add trial counts, success criteria, and hardware details to the real-world experiments** (Table 3). Even 20–50 trials per condition with variance bars would substantially strengthen the evidence.
3. **Report CLIPort's trajectory prediction accuracy** (e.g., end-effector position/orientation error, success rate of trajectory completion) so the reader can assess error propagation in the pipeline.
4. **Evaluate the physics refinement on physical metrics** (penetration depth, contact force magnitude, joint limit violation count) in addition to MPJPE, to directly demonstrate the claimed improvement in physical feasibility.
5. **Qualify the "first" claim** with a precise comparison to HOIGPT, specifying the distinctions (cross-hand tokenization, multi-morphology support, physics refinement for robot execution).

## Score and Decision

**Score:** 6.0

**Decision:** Accept

**Calibration:**
- Round 1 bracket: 4.5–6.5 (weak anchors ~3.0, strong anchors ~8.0)
- Round 2 anchors read in full (8 papers total):
  - GEVRM (6.0, Accept Poster): No real-world experiments, some baseline gaps. *UniHM is comparable or slightly stronger due to real-world validation and more novel contributions.*
  - RoboFlamingo (6.0–6.5, Accept Spotlight): Strong CALVIN results but no real robot experiments. *UniHM addresses a harder problem (dexterous hand with multiple morphologies) and has real-world evidence, but its diversity gap is a notable weakness RoboFlamingo doesn't have.*
  - DexTrack (6.75, Accept Poster): Thorough dexterous manipulation with sim+real experiments. *DexTrack's evaluation is cleaner; UniHM has more novelty in the cross-hand tokenizer but less thorough evaluation.*
  - Make a Donut (5.25, Reject): Unconvincing real-world results. *UniHM is clearly stronger.*
  - Grounding Robot Policies (5.33, Reject): Unclear presentation. *UniHM is clearly stronger.*
  - Language-Conditioned IL (3.0, Reject): Significant methodological flaws. *UniHM is far stronger.*
  - Multi-Group Tri-plane (5.5 avg, mixed): Limited novelty. *UniHM has stronger novelty.*

Final score of 6.0 reflects that UniHM makes genuine technical contributions (cross-hand tokenizer, unified framework with physics refinement) and provides generally solid experimental evidence, but is held back by the unaddressed diversity gap on DexYCB and insufficient detail in the real-world experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>