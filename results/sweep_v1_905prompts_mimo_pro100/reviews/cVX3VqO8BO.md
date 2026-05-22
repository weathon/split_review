Now I have sufficient calibration data. Let me synthesize my assessment.

**Round 1 bracket: 5.0 – 7.0**
- UniHM clearly exceeds Cross-Embodiment Dexterous Grasping (5.0, accepted) in scope and completeness.
- It is comparable to HAMSTER (6.0, accepted) and DexTrack (6.25, accepted) in technical contribution and evaluation quality.
- It falls short of Video Language Planning (7.0) in generality and evaluation maturity.

**Round 2 bracket: 5.5 – 6.5**
- Better than Video2Policy (5.5, rejected) and Mani-WM (4.67, rejected) — more complete system, stronger results.
- Comparable to SparseDFF (6.0) and HAMSTER (6.0) — similar level of technical novelty with similar evaluation gaps.
- Slightly below DexTrack (6.25) and AHA (6.25) — those have cleaner evaluations.

Final score: **6.0** — competent systems paper with genuine contributions (cross-morphology codebook, physics refinement) but real evaluation gaps (baseline methodology, missing simulation, unvalidated cross-hand transfer claim).

---

## Summary

UniHM proposes a unified framework for language-guided dexterous hand manipulation that combines three components: (1) a Unified Hand-Dexterous Tokenizer with a shared VQ-VAE codebook aligned across heterogeneous hand morphologies via distillation, (2) a VLM-based sequence generation model trained on human-object interaction data, and (3) a physics-guided dynamic refinement module with contact, generative, and temporal energy terms optimized via Gauss-Newton. The system is evaluated on DexYCB and OakInk datasets with retargeted MANO annotations, plus real-world trials on a dexterous hand.

## Strengths

- **Novel cross-morphology codebook with distillation-based alignment (Section 3.2):** The Unified Hand-Dexterous Tokenizer introduces a principled approach to mapping heterogeneous hand morphologies into a shared discrete codebook. The staged training procedure — first training a reference encoder-decoder, then aligning new morphologies via knowledge distillation (Eq. 3) before VQ-VAE fine-tuning — bypasses the gradient discontinuity of non-differentiable token alignment. This is a genuine technical contribution that goes beyond simply applying existing VQ-VAE to hand poses.

- **Well-formulated physics refinement module (Section 3.4):** The energy-based refinement is the paper's most technically detailed contribution. The asymmetric contact penalty (Eq. 12) with continuous gradient matching at the surface boundary is well-motivated for optimization stability, and the Gauss-Newton formulation (Eq. 17-18) that integrates generative, contact, and temporal priors in a unified framework is sound. This provides a principled approach to enforcing physical feasibility on generated trajectories.

- **Complete end-to-end system with real-world demonstration:** UniHM assembles a full pipeline from open-vocabulary language instruction + RGB-D input to executable dexterous hand trajectories. The real-world experiments (Table 3, Figure 3) demonstrate deployment across four task types (Grab, Pick&Place, Pull&Push, Open&Close) on both seen and unseen objects, showing practical viability that goes beyond simulation-only evaluation.

- **Superior performance on both datasets:** Tables 1-2 show UniHM outperforming all baselines on MPJPE, FOL, FPL, and FID across both DexYCB and OakInk, for both seen and unseen splits. Notably on OakInk, UniHM's diversity (165.47 seen, 153.28 unseen) is actually closer to ground truth (147.40) than all baselines, contradicting the cherry-picked DexYCB diversity criticism.

## Weaknesses

### Fatal
None.

### Major

- **Baselines are human body motion generators, not dexterous hand manipulation systems, and are post-processed with UniHM's own refinement (Tables 1-2).** TM2T, MDM, FlowMDM, and MotionGPT3 are motion generation models designed for human body pose sequences, operating on different output spaces and modalities than dexterous hand manipulation. The paper acknowledges applying its own physics-guided refinement to baseline outputs ("Because prior action-generation baselines lack explicit physical-feasibility guarantees, we post-process their outputs with our physics-guided refinement to ensure a fair comparison," Section 4.3), but does not discuss how this conflates the contribution of the VLM/tokenizer architecture with the refinement post-processing. Since Table 4 shows refinement provides ~4 MPJPE improvement for UniHM itself, but baselines receive the same refinement, it is unclear how much of UniHM's advantage comes from the generative model versus the refinement module. A comparison against baselines *without* refinement, or against methods designed for the same task domain, would substantially strengthen the evaluation.

- **Cross-hand morphological transfer is claimed as a contribution but never experimentally validated.** The paper's second listed contribution states the codebook "enables direct token reuse and transfer across robotic and anthropomorphic hands" (Section 1). Section 3.2 provides the mathematical formulation (Eq. 6), and the retargeting pipeline maps MANO to five dexterous hands (Shadow, Allegro, SVH, Leap, Panda). However, no experiment demonstrates cross-hand transfer quality — e.g., encoding with MANO and decoding with Shadow hand, then evaluating the resulting trajectories. All quantitative experiments evaluate on single hand types per dataset. This leaves a key claimed contribution unsubstantiated.

- **No simulation-based evaluation despite physics-centric contribution.** Section 4's introduction claims to "validate feasibility in simulation," and the conclusion references "simulation checks," but no simulation evaluation (e.g., grasp stability, contact forces, penetration metrics in MuJoCo/Isaac Gym) appears in the paper. For a paper whose third core contribution is physics-guided dynamic refinement, the only physics-related metric is real-world success rate, which is too sparse to isolate the effects of individual energy terms. This is a significant gap between the paper's claims and its evidence.

### Minor

- **Unspecified hyperparameters for the physics refinement module.** The weighting matrices **W**_gen, **W**_vel, **W**_acc and scalars α, k, λ_c in Eqs. 12-16 are defined symbolically but never assigned concrete values. The paper states they are "symmetric positive-definite" or "scale parameters" but provides no numerical values, no sensitivity analysis, and no discussion of how they were tuned. This limits reproducibility for the paper's most novel technical component.

- **Real-world evaluation lacks statistical rigor.** Table 3 reports success rates across four task types for seen and unseen objects, but does not specify the number of trials per condition, provide confidence intervals, or perform statistical significance testing. At small sample sizes, success rate differences (e.g., 65% vs 45%) may not be statistically distinguishable.

- **Diversity metric interpretation is inconsistent on DexYCB.** On DexYCB (Table 1), UniHM's diversity (39.62 seen, 42.70 unseen) is substantially farther from ground truth (125.53) than MotionGPT3's (72.51 seen, 75.84 unseen). The paper states "Diversity closer to the ground truth indicates a more reasonable generation" (Section 4.2) but does not acknowledge or discuss this DexYCB-specific limitation. (Note: OakInk results show the opposite pattern, where UniHM is closer to GT, so this is dataset-dependent rather than a universal failure.)

- **Ablation studies are minimal.** Table 4 tests only three removals (depth input, masked training, physical refinement). Missing ablations include: asymmetric effect of refinement on baselines vs. UniHM, effect of different hand morphologies, codebook vocabulary size K, and individual energy term contributions (contact vs. generative vs. temporal).

### Trivial
None.

## Nice-to-Haves
- Comparison with language-guided dexterous grasp methods (SemGrasp, AffordDexGrasp) discussed in related work but not evaluated. The paper's defense — that these generate static poses — is reasonable, but a comparison would clarify the advantage of dynamic manipulation.
- Analysis of how VLM scale (Qwen3-0.6B vs. larger alternatives) affects performance, given the paper's argument for smaller models under data scarcity.
- Retargeting quality analysis: since all training data is retargeted from MANO, understanding retargeting fidelity would strengthen confidence in the results.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Missing related works**: The harsh critic suggests comparisons with SemGrasp, AffordDexGrasp, DexGYS, etc. These methods are discussed in related work and the paper explicitly scopes out static grasp methods. This is scope creep rather than a real gap.
- **Typos/formatting**: Not relevant per filtering rules.
- **Questioning the "first" claim**: The harsh critic calls the "first framework" claim a narrow "first." Whether something is "first" is not falsifiable from the paper itself and is common framing in the field.

## Novel Insights

The paper's genuinely novel observation is that cross-morphology hand tokenization can be achieved through a staged distillation-to-VQ-VAE pipeline, avoiding the gradient discontinuity of direct non-differentiable token alignment. This is a useful insight for the robotics community working with diverse hand morphologies. The asymmetric contact penalty (Eq. 12) with slope-matched continuity at the boundary is also a well-designed formulation for optimization-based contact handling. However, these insights are somewhat undercut by the lack of cross-hand transfer experiments and the absence of detailed hyperparameter analysis.

## Suggestions
1. **Add cross-hand transfer experiments**: Encode trajectories with one hand morphology (e.g., MANO) and decode with a different robot hand. Evaluate MPJPE/FPL/FOL for the transferred trajectories. This would directly validate the paper's second contribution.
2. **Add baseline results without refinement**: Show Tables 1-2 baselines both with and without UniHM's physics refinement to disentangle the contribution of the generative model from the refinement module.
3. **Specify all hyperparameters** for the physics refinement module (α, k, λ_c, W_gen, W_vel, W_acc values) and add a sensitivity analysis.
4. **Add simulation-based physics evaluation**: Run generated trajectories in a simulator and report grasp stability, object displacement, contact forces, and penetration metrics.
5. **Report trial counts and confidence intervals** for real-world experiments.

## Score and Decision

**Calibration anchors retrieved:**

| Round | Anchor | Avg Score | Relevance |
|-------|--------|-----------|-----------|
| 1 | xcHIiZr3DT (Vision-Based Pseudo-Tactile) | 2.50 | Weak — tactile perception, much less complete |
| 1 | sXF5P4N7e8 (Goal-Conditioned Masking) | 3.00 | Weak — simpler manipulation system |
| 1 | KBSHR4h8XV (Early Fusion VLA) | 3.33 | Weak — VLA architecture, limited results |
| 1 | Q6HYM1EMu8 (LARG2) | 3.00 | Weak — reward generation, different problem |
| 1 | twIPSx9qHn (Cross-Embodiment Dexterous Grasping) | 5.00 | Very relevant — cross-hand grasping, UniHM clearly stronger |
| 1 | Afjf6izLvJ (Grounding Robot Policies) | 5.33 | Moderately relevant — VLM for manipulation |
| 1 | h7aQxzKbq6 (HAMSTER) | 6.00 | Very relevant — hierarchical VLA, comparable quality |
| 1 | c0chJTSbci (Zero-Shot with Image-Editing Diffusion) | 6.25 | Moderately relevant — diffusion for manipulation |
| 1 | 7BLXhmWvwF (Geometry-aware RL) | 8.00 | Less relevant — deformable objects RL |
| 1 | OI3RoHoWAN (GenSim) | 8.00 | Less relevant — simulation task generation |
| 2 | NxoFmGgWC9 (GR-1 Video Pretraining) | 5.50 | Relevant — VLM + video pretraining, comparable issues |
| 2 | Aqfwhna1D7 (CrayonRobo) | 5.20 | Moderately relevant — visual prompting for manipulation |
| 2 | s3FTX4Ay55 (Articulate-Anything) | 6.20 | Moderately relevant — VLM for 3D modeling |
| 2 | lFYj0oibGR (Vision-Language as Robot Imitators) | 6.50 | Relevant — VLM fine-tuning for manipulation |
| 2 | friHAl5ofG (VLM as Value Learners) | 7.50 | Less relevant — value learning |
| 2 | J4D5WVoc5g (Dynamic Hand-Object Reconstruction) | 4.50 | Relevant — hand-object interaction, rejected |
| 2 | AJQuTFd9es (HandsOnVLM) | 6.33 | Very relevant — VLM for hand trajectories, rejected |
| 2 | gVWEq7LITG (TF-HOT) | 3.50 | Relevant — dexterous manipulation tracking |
| 2 | 9HZtP6I5lv (OmniPhysGS) | 6.40 | Moderately relevant — physics-based generation |
| 2 | ajSmXqgS24 (DexTrack) | 6.25 | Very relevant — dexterous manipulation tracking |
| 2 | HHWlwxDeRn (SparseDFF) | 6.00 | Relevant — dexterous manipulation |
| 2 | NtQqIcSbqv (Visual and Tactile Signals) | 6.00 | Moderately relevant — dexterous manipulation |
| 2 | aVyJwS1fqQ (Mani-WM) | 4.67 | Moderately relevant — world model, rejected |
| 2 | JVkdSi7Ekg (AHA Failure Detection) | 6.25 | Moderately relevant — VLM for manipulation |
| 2 | RhfYIJux9d (Video2Policy) | 5.50 | Moderately relevant — video to policy, rejected |

**Round 1 bracket: 5.0 – 7.0.** UniHM clearly exceeds Cross-Embodiment Dexterous Grasping (5.0) and is comparable to HAMSTER (6.0) and DexTrack (6.25), but falls below Video Language Planning (7.0).

**Round 2 bracket: 5.5 – 6.5.** UniHM is stronger than rejected papers like HandsOnVLM (6.33-rejected, had missing details), Mani-WM (4.67-rejected), and Video2Policy (5.50-rejected). It is comparable to accepted papers SparseDFF (6.0), HAMSTER (6.0), and GR-1 (5.5). UniHM has more technical novelty than GR-1 but shares similar evaluation weaknesses (baseline concerns, limited real-world scope).

**Final score: 6.0.** UniHM is a competent systems paper with genuine contributions (cross-morphology codebook, physics refinement formulation, complete end-to-end system) but real evaluation gaps (baseline methodology concerns, missing cross-hand transfer validation, missing simulation evaluation, unspecified hyperparameters) that prevent a higher score. The paper would benefit most from demonstrating cross-hand transfer and disentangling the refinement contribution from the generative model contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>