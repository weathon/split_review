I've read the paper thoroughly and examined all the reviewer claims. Let me now synthesize the final review.

---

## Summary

UniHM proposes a framework for generating dynamic dexterous hand manipulation sequences conditioned on open-vocabulary language instructions. The approach combines (1) a unified hand-dexterous VQ-VAE tokenizer that maps heterogeneous hand morphologies into a shared codebook, (2) a VLM (Qwen3-0.6B) trained with a progressive masking curriculum for instruction-conditioned sequence generation, and (3) a physics-guided dynamic refinement module that optimizes contact, temporal smoothness, and generative priors. The system is trained solely on human-object interaction video data (DexYCB, OakInk) without requiring teleoperation data, and is evaluated in simulation and on a real robot. UniHM achieves SOTA results on both benchmarks across MPJPE, FOL, FPL, and FID, with ablations demonstrating positive contributions from each component.

## Strengths

1. **Consistent SOTA quantitative results across two benchmarks.** Tables 1 and 2 show UniHM outperforming four prior methods (TM2T, MDM, FlowMDM, MotionGPT3) on both seen and unseen splits of DexYCB and OakInk across all four primary metrics. The margins are substantial — e.g., unseen MPJPE 63.56 vs. 77.93 (MotionGPT3) on DexYCB — and error bars are reported. This provides strong evidence for the overall effectiveness of the integrated pipeline.

2. **Clean ablation study isolating each component's contribution.** Table 4 demonstrates that removing depth input, masked training, or physical refinement each degrades performance across metrics. The physics-guided refinement alone accounts for ~4–5 points of MPJPE improvement (seen: 65.78→61.40; unseen: 65.39→63.56) and reduces FPL by ~3 points, confirming its role in improving trajectory accuracy and physical realism beyond what the VLM alone produces.

3. **Real-world validation on a physical robot hand.** Table 3 reports success rates on four task categories (Grab, Pick&Place, Pull&Push, Open&Close) for both seen and unseen settings. UniHM achieves notably higher success rates than the MDM+Dex-Retargeting and MotionGPT3+Dex-Retargeting baselines, e.g., 55% vs. 15% on unseen Pull&Push, demonstrating that the pipeline transfers from human video training data to physical robot execution.

4. **Novel architectural contributions that are well-motivated.** The morphology-agnostic codebook with cross-hand distillation (Eq. 3) and the decoupled perception-generation architecture (CLIPort for perception, VLM for HOI generation) are clearly described design innovations. The decoupled design, in particular, is practical — only the smaller CLIPort module needs fine-tuning when the scene distribution shifts, keeping the HOI generator stable.

## Weaknesses

### Major

1. **Missing comparison with the most directly related prior work (HOIGPT).** The paper cites HOIGPT (Huang et al., 2025) in related work, describing it as a method that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences" — which is the same fundamental task UniHM addresses. Despite this, HOIGPT is absent from Tables 1–3, and no justification is given for its exclusion. The paper's characterization that HOIGPT and related work "predominantly target Digital Hand, low-DoF grippers, or static grasp poses" is at odds with its own description of HOIGPT as generating sequential HOI. Without a direct comparison or a principled explanation of why comparison is infeasible (e.g., different datasets, evaluation protocols, or hand representations), the claim of "state-of-the-art" is incompletely supported. This gap is the paper's most significant weakness.

2. **Unified tokenizer's claimed benefit is not empirically validated.** The paper identifies the morphology-agnostic codebook as a core contribution, stating it "maps heterogeneous dexterous-hand morphologies into a single shared codebook, improving cross-dexterous hand generalization." However, the main experiments evaluate exclusively on MANO hand data (DexYCB, OakInk). There is no ablation comparing unified vs. separate per-hand codebooks, no cross-hand transfer experiment (e.g., train on MANO, evaluate on Allegro without retraining), and no quantitative evidence that the unified codebook improves generalization over a single-hand tokenizer. The real-world experiments use one robot hand but do not isolate the tokenizer's role. This claim currently rests on architectural reasoning alone, not experimental evidence.

3. **Baseline adaptation is under-specified.** The paper compares against four human whole-body motion generation methods (TM2T, MDM, FlowMDM, MotionGPT3) and states they were "post-processed with our physics-guided refinement to ensure a fair comparison." However, critical details are missing: (a) Were these baselines trained on the same DexYCB/OakInk hand joint data? (b) How was their output representation (typically full-body joint angles) matched to the hand-only setting? (c) Were they conditioned on the same text prompts? Without this information, it is difficult for readers to assess whether the large reported margins reflect genuine superiority or differences in adaptation quality. This is a reproducibility concern.

### Minor

4. **Diversity substantially lower than ground truth on DexYCB.** On DexYCB seen, UniHM achieves diversity 39.62 vs. GT 125.53, while MotionGPT3 achieves 72.51. The paper states diversity "closer to the GT indicates a more reasonable generation," yet UniHM is farther from GT than some baselines. This trade-off between accuracy and diversity is not discussed. The paper should analyze whether this reflects mode collapse or a consequence of the strong physics prior, and ideally report a coverage-based metric alongside diversity.

5. **CLIPort perception module is underspecified.** The CLIPort-based trajectory estimator (Eq. 7) is a critical component — its output \(\mathcal{T}_{\text{tar}}\) directly conditions the VLM and the physics refinement. Yet the paper provides no information about its architecture, training data, loss function, or accuracy (e.g., end-effector position error relative to ground-truth object motion). Since errors in \(\mathcal{T}_{\text{tar}}\) cascade through the pipeline, some evidence of its reliability is needed.

6. **Missing standard implementation details.** The codebook size \(K\) and latent dimension \(d_z\) are mentioned symbolically but not given numerical values. The masking schedule (how \(p_t\) increases over training) is not specified. The real-world protocol (which robot arm and hand were used, number of trials per cell, success criteria) is absent. These details matter for reproducibility.

7. **Qualitative language annotation quality not assessed.** The use of GPT-4o to generate 5 instructions per sequence from keyframes is described, but no human evaluation or verification subset is provided to confirm that the annotations are sensible and diverse. This is a minor oversight given that the annotations serve as training targets.

### Trivial

- The paper's claim of being "the first unified, language-conditioned framework for dynamic dexterous hand manipulation beyond static grasps" is somewhat overstated given that HOIGPT (cited in the paper) also generates sequential hand-object interaction from text. This does not diminish the paper's technical contributions but the framing could be more precise.

## Nice-to-Haves

- Simulation-based physical feasibility metrics (e.g., penetration depth percentage, number of collisions, force closure ratio) would directly quantify the benefit of the physics refinement, complementing the joint-accuracy metrics.
- A cross-hand transfer experiment (train on MANO, test on Allegro via the unified codebook) would directly validate the morphology-agnostic tokenizer claim.
- Reporting accuracy of the CLIPort trajectory predictor would help attribute downstream errors.

## Removed Points

These points were raised by reviewers but are removed or downgraded for the reasons below:

- **"HOIGPT is the most directly relevant baseline; omitting it is fatal"** — The paper does cite HOIGPT and explains that it targets digital (non-physical) hands without physics-guided refinement. Direct comparison may require non-trivial adaptation to the same evaluation protocol. The omission is a significant gap but not fatal. → Kept as Major, not Fatal.
- **"The ablation shows 'w/o Masked Training' already achieves relatively strong performance, suggesting the gain comes from VLM+unified tokenizer design, not specifically from the curriculum"** — This is an observation about where gains come from, not a weakness. The paper doesn't claim the masking curriculum is the sole source of gains. → Removed.
- **"The very large gaps could be partially artefactual if baselines were poorly adapted"** — This is speculation. The paper does state baselines were post-processed with the same physics-guided refinement. The concern about missing adaptation details is valid (kept as Major #3) but the assertion that gaps are artefactual is not grounded. → Removed the speculative assertion, kept the substantial concern about missing details.
- **"The paper would be more credible if it explicitly positioned UniHM as a framework that additionally handles multiple morphologies..."** — This is a suggestion about framing, not a weakness. → Removed.
- **Various formatting nitpicks and requests for appendix content** — These reflect parser-side issues or requests for material that likely exists in the full submission. → Removed.
- **"The paper does not describe how these models were adapted..." — the concern about output representation matching** — Partially valid but the paper does state baselines used the same physics-guided refinement, and MotionGPT specifically uses VQ-VAE tokenization similar to the proposed method. The concern is kept but in a more measured form (Major #3).

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is the tension between the paper's two central claims: (1) that the unified tokenizer enables cross-hand generalization, and (2) that the system achieves SOTA results on standard MANO-hand benchmarks. These claims operate at different levels — the first is about architectural generality, the second about task performance — but the paper does not bridge them experimentally. The real-world results (Table 3) gesture at cross-embodiment capability but do not isolate the tokenizer's role from the overall pipeline. A targeted experiment comparing unified vs. per-hand codebooks on a cross-morphology transfer task would either validate the core design claim or reveal that the performance gains come primarily from the VLM+physics components rather than the token sharing. The paper's current evidence would support either finding, but does not discriminate between them.

## Suggestions

1. **Include HOIGPT as a baseline** in at least the simulation benchmarks (Tables 1–2), or provide a clear justification for why direct comparison is infeasible. If HOIGPT uses a different evaluation protocol (e.g., different datasets or metrics), state this explicitly.

2. **Add an ablation comparing unified vs. separate per-hand codebooks** on a cross-morphology transfer task (e.g., train on MANO data, evaluate on Allegro hand via the tokenizer's translation mechanism, Eq. 6).

3. **Specify the baseline adaptation protocol**: which data splits were used for training baselines, how output dimensions were matched, and what text conditioning was provided. This is essential for the reader to assess fairness.

4. **Report the CLIPort trajectory prediction accuracy** on the DexYCB/OakInk test sets (e.g., end-effector position RMSE relative to ground-truth object trajectories).

5. **Discuss the diversity-accuracy trade-off**: why is UniHM's diversity lower than GT and some baselines on DexYCB? Is this a consequence of the physics prior, the codebook size, or the masking curriculum?

6. **Provide tokenizer and real-world protocol details** (codebook size, latent dimension, robot arm model, number of trials, success criteria) to improve reproducibility.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Three queries on "dexterous hand manipulation generation VLM language condition" with score bounds (-inf, 3.5), (3.5, 7.5), and (7.5, +inf). Weak band returned papers averaging 2.5–3.33 (Rejects). Middle band returned papers averaging 5.20–7.00 (mix of Accept/Reject). Strong band returned papers averaging 8.00 (Accepts). The paper clearly sits in the middle band.

**Round 2 (Narrowing):** Two queries within (4.5, 6.5) and (6.0, 8.0). Key anchors read in full:
- **HandsOnVLM** (6.33, Reject): VLM for hand-object interaction prediction. Weaker evaluation than UniHM (no real-world, no ablation isolating components). UniHM is stronger overall → above 6.33.
- **RoboFlamingo** (6.50, Accept): VLM for robot manipulation, simulated-only evaluation on CALVIN, missing some baselines. UniHM has real-world + simulation + ablations → comparable or slightly stronger.
- **HAMSTER** (6.00, Accept): Hierarchical VLA for open-world manipulation, simulation + real-world. UniHM addresses a harder sub-problem (dexterous hands) with stronger benchmark results → above 6.00.
- **CrayonRobo** (5.20, Reject): Simpler visual prompting approach. UniHM is technically more sophisticated with stronger results → well above 5.20.
- **VLP** (7.00, Accept): Video-language planning with tree search. Stronger theoretical contribution and broader scope → below 7.00.

**Final position:** The paper is stronger than HandsOnVLM and HAMSTER, comparable to RoboFlamingo, and below VLP. Adjusted downward from the RoboFlamingo-level estimate due to the three verified major weaknesses (HOIGPT omission, tokenizer claim unvalidated, baseline adaptation under-specified) that make the evaluation less complete than it should be for a paper at the 6.5 level.

**Score: 6.0** — Solid technical contributions and strong empirical results, with notable gaps in evaluation completeness that prevent a higher score.

**Decision: Accept** — The paper presents a practically motivated, well-engineered system with SOTA results on standard benchmarks and real-world validation. The weaknesses are addressable and do not invalidate the core contributions.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KBSHR4h8XV (Early Fusion VLA) | 3.33 | R1 | Weaker; UniHM has stronger evaluation |
| sXF5P4N7e8 (Goal-Cond. Masking) | 3.00 | R1 | Weaker; simpler task scope |
| oyXoGJQlUf (GRAIL) | 3.00 | R1 | Different problem, weaker execution |
| AJQuTFd9es (HandsOnVLM) | 6.33 | R1,R2 | Weaker; no real-world, no ablation isolating components |
| h7aQxzKbq6 (HAMSTER) | 6.00 | R1,R2 | Comparable; different approach, similar evaluation depth |
| lFYj0oibGR (RoboFlamingo) | 6.50 | R1,R2 | Slightly stronger in completeness but sim-only |
| Aqfwhna1D7 (CrayonRobo) | 5.20 | R2 | Weaker; simpler approach, lower results |
| 9pKtcJcMP3 (VLP) | 7.00 | R2 | Stronger; broader scope, stronger theory |
| friHAl5ofG (Value Learners) | 7.50 | R2 | Stronger; different task, stronger theory |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>