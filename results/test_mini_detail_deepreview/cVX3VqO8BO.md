Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

UniHM proposes a framework for language-conditioned dexterous hand manipulation that generates full manipulation sequences (not just static grasps) from open-vocabulary instructions and RGB-D input. The key technical contributions are: (1) a **morphology-agnostic VQ-VAE codebook** that allows sharing discrete motion tokens across different dexterous hand morphologies (Shadow, Allegro, SVH, Leap, Panda), (2) a **decoupled perception-generation VLM** (Qwen3-0.6B + CLIPort) that generates HOI sequences conditioned on language, and (3) a **physics-guided dynamic refinement** module that optimizes generated sequences for contact and temporal smoothness via Gauss-Newton. Experiments on DexYCB and OakInk show consistent improvements over four motion-generation baselines on MPJPE, FPL, FOL, and FID, and real-world trials demonstrate higher execution success rates.

## Strengths

- **Morphology-agnostic codebook with cross-hand distillation (Sec. 3.2, Eq. 1–6).** The shared VQ-VAE codebook trained with a distillation procedure (Eq. 3) that aligns new hand encoders to a reference encoder without exposing the quantization bottleneck is a concrete technical innovation. It enables direct token reuse across different dexterous hands and scales to new morphologies with minimal retraining — this is a genuine advance over prior single-morphology approaches.

- **Consistent and large quantitative improvements on standard benchmarks (Tables 1, 2).** On DexYCB, UniHM reduces MPJPE from 74.80 (MotionGPT3) to 61.40 on seen objects (≈18%) and from 77.93 to 63.56 on unseen objects. FPL drops by >37% on both splits. On OakInk the gains are similarly substantial across all accuracy/fidelity metrics. These improvements are supported by confidence intervals and hold across both datasets.

- **Real-world execution validation (Table 3).** UniHM achieves 60–65% success on unseen-object grab tasks vs. 5–45% for MotionGPT3+Dex-Retargeting, and similar advantages on pull/push (55% vs. 15%). These real-world trials provide direct evidence that the generated sequences transfer to physical robot hardware, which is a meaningful step beyond pure simulation evaluation.

- **Physics-guided refinement is well-formulated and ablated (Sec. 3.4, Table 4).** The asymmetric contact penalty (Eq. 12) is carefully designed to be continuous and slope-matched for stable optimization. The ablation (Table 4) shows removing it increases MPJPE from 61.40→65.78 on seen and 63.56→65.39 on unseen, confirming its contribution.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed "first" framing relative to HOIGPT, with no experimental comparison.** The paper claims "the first unified, language-conditioned framework for dynamic dexterous hand manipulation beyond static grasps" (Abstract & Sec. 1). Yet HOIGPT (Huang et al., 2025), cited in Sec. 2.2, "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences" — this is precisely language-conditioned dynamic HOI generation on a dexterous hand model (MANO). The paper then groups HOIGPT with methods that "predominantly target Digital Hand, low-DoF grippers, or static grasp poses," which is an inaccurate characterization since HOIGPT generates dynamic sequences. The paper never explains why HOIGPT is excluded from comparison or how the claimed novelty is distinct. The "first" claim should be scoped to the paper's specific contributions (cross-morphology unification, physics-guided refinement for robot execution, learning from video without teleoperation). The omission of a HOIGPT comparison is a significant evidential gap that weakens the evaluation.

- **Baseline experimental setup is underspecified.** The paper states (Sec. 4.3): "Because prior action-generation baselines lack explicit physical-feasibility guarantees, we post-process their outputs with our physics-guided refinement." It does not state whether the four baselines (TM2T, MDM, FlowMDM, MotionGPT3) — all originally designed for full-body human motion, not hand-only manipulation — were retrained on the same DexYCB/OakInk train splits, or if off-the-shelf pretrained models were used with only post-processing. If the baselines were not retrained on hand-interaction data, the comparison is not meaningful. If they were, the retraining procedure, hyperparameters, and data splits must be reported. Without these details, the reported state-of-the-art results in Tables 1 and 2 cannot be properly assessed for fairness.

### Minor

- **Diversity metric inconsistency unaddressed.** On DexYCB (Table 1), GT diversity is 125.53. MotionGPT3 achieves 72.51 (seen) and 75.84 (unseen), while UniHM achieves only 39.62 and 42.70. The paper defines diversity as "closer to ground truth indicates more reasonable generation." By this metric, MotionGPT3 is substantially better on DexYCB. The paper's sweeping claim that it "consistently outperforms all baselines across both seen and unseen objects" is strictly true only for MPJPE/FOL/FPL/FID, not for diversity. The paper should acknowledge this or explain why lower diversity on DexYCB is acceptable.

- **Training/inference mismatch not empirically validated.** The VLM is trained exclusively on ground-truth trajectories and object point clouds, while at inference a separate CLIPort module provides noisy estimates (Sec. 3.3). The paper claims robustness by fine-tuning only CLIPort at test time but provides no experiment quantifying the performance drop when using CLIPort estimates vs. ground truth. A simple ablation comparing these two conditions would either validate the decoupled design or reveal a gap.

- **Real-world experiment protocol is underspecified.** Table 3 reports success rates without specifying: which robot hand was used, the number of trials per condition, the exact definition of "success" (stable grasp for how long? task completion criteria?), and how baselines were adapted for real-world execution beyond "Dex-Retargeting." The currently reported rates (5%–65%) lack sufficient context to assess their statistical reliability.

### Trivial
- The "lightweight simulation-based optimization" described in the w/o Physical Refinement ablation (Sec. 4.4, line 301) appears to be a different post-processing than the paper's main physics-guided refinement; the relationship between the two should be clarified.

## Nice-to-Haves

- An experiment measuring performance with ground-truth vs. CLIPort-estimated trajectories to quantify the impact of the training/inference mismatch.
- Reporting of key hyperparameters (codebook size K, code dimension d_z, commitment weight β, VLM batch size/learning rate, Gauss-Newton iteration count) that are currently missing from the main text.
- Reporting penetration depth or force closure as additional physical-feasibility metrics beyond MPJPE/FOL/FPL.

## Removed Points

- **Criticism about "not yet released" or unverifiable models/tools.** The hard rules require removing any criticism that questions the existence, release status, or availability of any model, tool, benchmark, or dataset cited in the paper. No such criticisms were present.

- **Criticism about HOIGPT being "exactly dynamic, language-conditioned dexterous hand manipulation — not static grasp generation."** This point was retained (as the overclaiming major weakness) but reframed from "fatal" to "major" because: (i) HOIGPT operates on MANO (digital hand model), not robot hands, so the paper's contributions around cross-morphology robot execution and physics-guided refinement remain distinctive; (ii) the paper's core technical contributions (shared codebook, physics optimization, learning from human video without teleoperation) are not invalidated by HOIGPT's existence; and (iii) the "first" claim could be repaired with proper scoping rather than retraction. The removed aspects of this criticism were the assertion that this is a "structural flaw" and "directly refutes" the main novelty — these overstate the impact since the paper has multiple independent contributions.

- **Criticism about MPJPE being "accuracy rather than physical feasibility."** Removed because this is a labeling preference, not a real flaw — MPJPE is a standard metric for hand pose quality in manipulation and the paper groups multiple physical-feasibility-related metrics under one heading, which is common practice.

- **Criticism about missing appendix content (codebook entries, LoRA vs. full fine-tuning, optimization iterations).** Removed per the hard rule: "Remove weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers." The number of real-world trials and robot hand specification, however, are main-text issues that were retained.

- **Criticism about missing related works.** Removed per the hard rule: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."

- **Pure formatting/style nitpicks.** Removed per hard rules.

- **Strength Finder claimed "first framework" as a strength.** Removed because it conflicts with the verified weakness about overclaiming relative to HOIGPT.

- **Strength Finder's claim about "robustness" of the decoupled architecture.** Removed as insufficiently supported — the paper does not provide the experiment validating robustness to distribution shift.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder identified the same set of contributions (cross-morphology codebook, physics-guided refinement, learning from video) and the same central weaknesses (HOIGPT comparison, baseline specification). The most interesting unresolved tension is between the paper's clear technical merit on its own terms and its tendency to overstate novelty relative to HOIGPT — a tension that would be cleanly resolved by scoping the claims to "first *cross-morphology physics-aware* framework" rather than "first" simpliciter.

## Suggestions

1. **Scope the "first" claim precisely.** Replace "the first framework for unified dexterous hand manipulation guided by free-form language commands" with a claim that foregrounds what is actually novel: e.g., "the first framework for *cross-morphology* dexterous hand manipulation with physics-guided sequence refinement from open-vocabulary instructions." Explicitly contrast with HOIGPT along the dimensions that differ (robot vs. MANO, cross-morphology vs. single, physics-guided vs. unconstrained generation) and, ideally, add a direct experimental comparison on DexYCB/OakInk.

2. **Specify baseline retraining.** State explicitly whether each baseline (TM2D, MDM, FlowMDM, MotionGPT3) was retrained on the same train splits of DexYCB and OakInk. If retrained, provide the training configuration (number of epochs, learning rate, architecture modifications for hand vs. full-body). If not, retrain them or acknowledge the limitation and discuss potential biases.

3. **Discuss the diversity results.** Acknowledge that on DexYCB, diversity is further from GT than MotionGPT3's, and either explain why this is acceptable (e.g., diversity-vs-accuracy trade-off, or that GT diversity on DexYCB may itself be high due to multi-view capture) or treat it as a limitation.

4. **Add an ablation for the CLIPort perception gap.** Compare VLM performance with ground-truth target trajectories/point clouds vs. CLIPort-predicted estimates to quantify how much quality is lost at inference due to the decoupled design.

5. **Report real-world experimental protocol details.** Specify robot hand make/model, number of trials per condition (ideally with confidence intervals), and success criteria.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Score | Round | Comparison |
|---|---|---|---|
| xcHIiZr3DT.md (grasping + tactile) | 2.50 | R1 | Much weaker — basic grasp pose planning without language conditioning or sequence generation |
| sXF5P4N7e8.md (goal-conditioned grasping) | 3.00 | R1 | Much weaker — single static grasp, no dynamic sequences |
| wl1Kup6oES.md (visual representation for manipulation) | 3.00 | R1 | Much weaker — representation learning, not sequence generation |
| q1Cv7Hp52y.md (skill discovery RL) | 3.00 | R1 | Much weaker — RL in simplified domains |
| uiFuqvkpAt.md (VQ behavioral repertoires) | 4.50 | R1 | Weaker — VQ for behavioral analysis, not manipulation generation |
| lfRYzd8ady.md (DCWM, discrete codebook RL) | 6.67 | R1 | Stronger — accepted, thorough evaluation with careful ablations |
| HYyRwm367m.md (NLoTM, VQ-VAE representations) | 6.50 | R1 | Stronger — accepted, well-executed |
| AJQuTFd9es.md (HandsOnVLM) | 6.33 | R1 | Similar — same domain, comparable strengths/weaknesses; rejected despite decent score due to missing baselines |
| OI3RoHoWAN.md (GenSim, LLM for simulation) | 8.00 | R1 | Much stronger — accepted, comprehensive |
| KsUh8MMFKQ.md (differentiable physics for manipulation) | 8.00 | R1 | Much stronger — accepted, thorough |
| Q6a9W6kzv5.md (PhysBench, VLM understanding) | 8.00 | R1 | Much stronger — accepted, comprehensive benchmark |
| 7BLXhmWvwF.md (geometry-aware RL) | 8.00 | R1 | Much stronger — accepted, thorough |

**Round 1 bracket:** 4.5–6.5 (between the weak 3.0-level papers and the strong 7.5+ papers)

**Round 2 — Narrowing:**
| Path | Score | Round | Comparison |
|---|---|---|---|
| VYOe2eBQeh.md (LAPA, VQ-VAE action pretraining) | 5.83 | R2 | Similar — accepted despite data consistency issues; UniHM has stronger technical novelty but similar evidential gaps |
| NxoFmGgWC9.md (video generative pre-training) | 5.50 | R2 | Similar — accepted, comparable scope/quality |
| Aqfwhna1D7.md (CrayonRobo, visual prompting) | 5.20 | R2 | Slightly weaker — rejected, less technical depth |
| Afjf6izLvJ.md (visuomotor language guidance) | 5.33 | R2 | Slightly weaker — rejected |
| lFYj0oibGR.md (RoboFlamingo, VLM imitation) | 6.50 | R2 | Somewhat stronger — accepted, cleaner evaluation on CALVIN |
| h7aQxzKbq6.md (HAMSTER, hierarchical VLA) | 6.00 | R2 | Similar — accepted despite limited task scope |
| c0chJTSbci.md (zero-shot manipulation with diffusion) | 6.25 | R2 | Similar — accepted, comparable evaluation quality |
| yAzN4tz7oI.md (RDT-1B, diffusion foundation model) | 7.00 | R2 | Stronger — accepted, much larger scale and more comprehensive evaluation |
| XToAemis1h.md (TacQuad, multi-sensor tactile) | 7.00 | R2 | Stronger — accepted |

**Final calibration:** The paper sits between the LAPA (5.83) and HAMSTER (6.00) anchors. Like LAPA, it has genuine technical novelty (VQ-VAE-based codebook + VLM) and strong benchmark results, but shares evidential gaps (missing comparison, underspecified baselines). Unlike HandsOnVLM (6.33, rejected), the paper has two public benchmarks + real-world validation and its missing baseline issue is more about retraining specification than a complete omission of relevant methods. The HOIGPT overclaim is a real concern but addressable. Overall, the paper is a borderline accept with real contributions that need better framing and experimental documentation.

### Final Score

**Score: 5.5** — The paper presents genuinely novel technical components (cross-morphology codebook, physics-guided refinement, learning from video without teleoperation) with strong quantitative results. However, significant overclaiming relative to HOIGPT and underspecified baseline experimental setup prevent a higher score. These issues are addressable with major revisions.

**Decision: Borderline** — The paper could be accepted after revision that (a) removes or carefully scopes the "first" claim with explicit distinction from HOIGPT, (b) clarifies baseline retraining procedures, and (c) discusses the diversity inconsistency. As-is, the evidence does not fully support the strong claims made.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Borderline</decision>