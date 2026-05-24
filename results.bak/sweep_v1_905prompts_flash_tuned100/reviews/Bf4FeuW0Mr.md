Now I have all the calibration data I need. Let me synthesize the final review.

---

## Summary

DemoGrasp proposes a framework for universal dexterous grasping that reformulates grasping as a *single-step Markov decision process*: given a single successful demonstration trajectory, an RL policy outputs SE(3) wrist transformations and delta hand joint angles that edit the demonstration, which is then replayed open-loop. To enable real-world deployment, a closed-loop vision policy is distilled via flow-matching imitation learning on the RL policy's successful rollouts. The paper evaluates on DexGraspNet (Shadow Hand), cross-dataset/ cross-embodiment generalization (6 hands, 6 datasets), and real-world grasping on 110 objects including small and thin items.

## Strengths

1. **Novel and effective formulation** — The core idea of reformulating dexterous grasping as demonstration editing in a single-step MDP is genuinely clever. The compact action space (SE(3) transformation + delta joint angles) combined with a simple binary+penalty reward reduces exploration complexity compared to prior multi-step RL methods. This is well-motivated and validated by the ablation in Table 8 showing improvement from 75.29% (no editing) to 96.24% with the full action space.

2. **State-of-the-art simulation results on DexGraspNet** — Table 1 reports 95.2% success on 3,200 training objects and 94.4% on unseen categories with the Shadow Hand, outperforming UniGraspTransformer (91.2%/88.3%) by ~5 percentage points. The minimal generalization gap (~1%) demonstrates strong learning rather than memorization.

3. **Real-world validation on challenging objects** — Table 3 reports 95.3% success on normal-sized objects and 71.1% on flat/thin objects across 110 real-world items. Grasping previously difficult thin tabletop objects (tools, cards, small items) with minimal collisions is a concrete advancement over prior sim-to-real methods, and the real-world regrasping behavior (Section 3.4) validates closed-loop recovery.

4. **Cross-embodiment generalization** — Figure 3 and the supplementary results show consistent performance across 6 different hands (Inspire, Allegro, DClaw, Shadow, FR3+Shadow, Schunk) on 6 unseen datasets, averaging 84.6% success while trained on only 175 objects. This goes well beyond prior work that typically evaluates a single hand on a single dataset.

5. **Robustness to demonstration quality** — Table 9 shows that directly replaying different demonstrations yields widely varying success (3.88%–75.29%), but the learned policy achieves ~95% in all cases, demonstrating the method does not depend on a carefully curated demonstration.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **DexGraspNet comparison uses a different evaluation protocol than baselines.** The paper acknowledges (Section 3.2) that baselines were evaluated with fixed object positions, while DemoGrasp uses 50 cm × 50 cm position randomization. The authors argue this makes the evaluation *harder* for their method due to translation invariance, which makes the comparison *conservative*. This reasoning has merit, but for a SOTA claim, a controlled ablation (e.g., evaluating DemoGrasp at fixed positions to directly match the baseline protocol, or re-running baselines with randomization) would provide a cleaner apples-to-apples comparison. Without this, the exact margin over prior work is not perfectly isolatable.

2. **Cross-embodiment baseline comparison (Table 2) is uncontrolled for training data.** The comparison against RobustDexGrasp uses numbers from the original paper, which was trained on a different object dataset. The paper argues both aim at universal grasping and test on unseen objects for both, which is reasonable but does not control for training-set quality or size. A controlled comparison (retraining RobustDexGrasp on the same 175 objects, or comparing against a simple ablation of DemoGrasp itself) would strengthen the claim of superior generalizability.

3. **Real-world evaluations lack trial-level breakdown and uncertainty estimates.** Table 3 reports per-category success rates with 5 trials per object (110 objects total), but no confidence intervals, per-object success distributions, or failure-mode analysis are provided. With small category sizes (e.g., 10 tools, 12 small objects), category-level point estimates are noisy. Reporting per-object trial counts (e.g., x/5 per object) would improve interpretability.

4. **Language-conditioned extension (Table 4) lacks details on how language descriptions are generated and conditioned upon.** The paper states language descriptions are "automatically generated" and the Instruct-DemoGrasp uses language conditioning, but provides no description of how this is implemented. While not the paper's core contribution, the lack of detail limits reproducibility of this extension.

### Trivial

- The paper's claim of "simplicity" (abstract, introduction) primarily refers to the reward design and single-step MDP, but the overall pipeline involves teleoperation, RL training on thousands of objects, 35K rendered rollout collection, ViT fine-tuning, and flow-matching imitation learning. The simplicity is in the *formulation*, not the system complexity. This is a minor framing issue.

## Nice-to-Haves

- A controlled ablation where DemoGrasp is evaluated with fixed object positions (matching the baseline protocol) would directly quantify the effect of position randomization and clean up the SOTA comparison.
- Including failure rollouts in the vision-policy training data (with corrective actions) and comparing success rates could shed light on whether success-only training is sufficient or whether the strong real-world results rely on the demonstrated regrasping behavior emerging from the flow-matching architecture.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- **"Vision policy trained exclusively on successful rollouts cannot recover from mistakes"**: The paper explicitly reports that the real-world policies "exhibit regrasp behaviors to recover from failures in a closed-loop manner" (Section 3.4). Additionally, training imitation learning policies on successful demonstrations only is standard practice (behavior cloning, diffusion policy). The claim that this leads to "fragile behavior" is speculative and contradicted by the real-world evidence.

- **"Baseline comparison is invalidated by protocol differences" (as a fatal/structural issue)**: The paper acknowledges the protocol difference and argues correctly that the direction of the difference (randomization for DemoGrasp vs. fixed for baselines) makes the comparison conservative. This is a real concern worth noting (see Weaknesses Minor #1) but does not "invalidate" the comparison or the SOTA claim.

## Novel Insights

The most interesting insight from the reviews is that the paper's central innovation — using a single demonstration as a *parameterized template* that an RL policy edits via compact SE(3)+joint deltas — effectively creates a strong inductive bias for dexterous grasping. This reverses the typical complexity scaling in robot learning: instead of making the policy more expressive (larger action spaces, longer horizons, complex rewards), it makes the problem simpler by reducing grasping to a single decision. The reviews collectively surface that this approach's key validation comes not from any single controlled comparison but from the *converging evidence* across multiple dimensions: DexGraspNet SOTA (even with protocol differences), cross-embodiment generalization on 6 hands, and real-world success on 110 objects including thin items that prior methods cannot handle. The demonstration-robustness experiment (Table 9) is especially convincing — 3.88% → 95.27% when the worst demonstration is used — because it isolates the method's contribution from demonstration quality effects.

## Suggestions

- **For the DexGraspNet comparison**: Add a supplementary experiment evaluating DemoGrasp at fixed object positions (matching the baseline protocol). Even a single column showing that the numbers are similar would address the protocol concern definitively.

- **For real-world reporting**: Provide a per-object breakdown (number of successes out of 5 trials) as a supplementary table. This adds statistical granularity without cluttering the main paper.

- **For the language-conditioned extension**: Briefly describe how language descriptions are generated (template-based? LLM-generated?) and how they condition the policy (e.g., cross-attention? FiLM?). This can be a short paragraph in the appendix.

## Score and Decision

**Round 1 (Bracketing):** I searched for dexterous grasping RL papers in three bands:
- Weak (<3.5): Papers scored 2.50–3.40 on loosely related grasping/RL topics. DemoGrasp is clearly far above these.
- Middle (3.5–7.5): Anchors included Cross-Embodiment Dexterous Grasping (5.00, 3 reviewers, 6/6/3 — accepted), ManiBox (5.25, 6/6/6/3 — rejected), DexTrack (6.25, 8/3/6/8 — accepted), ResDex (7.00, 8/6/8/6 — accepted).
- Strong (>7.5): Papers on thin-shell manipulation (8.00), scaling laws (8.00), GenSim (8.00). These address different problems or are at a clearly higher tier of completeness.

Round-1 bracket: 5.0–7.5. The paper is clearly above the Cross-Embodiment paper (5.00) and comparable to ResDex (7.00).

**Round 2 (Narrowing):** I searched for more anchors in the 6.0–8.5 band with terms targeting demonstration-based grasping. Retrieved anchors at 6.25 (DexTrack), 6.50 (BiAssemble, 3DGS-Drag, Learning Geometric Reasoning Networks), and 8.00 (Data Scaling Laws). DemoGrasp has more experimental breadth than DexTrack (6.25, different problem) and more real-world validation than any of the 6.50 anchors.

**Final score determination:** Comparing against the most relevant anchor — ResDex (7.00) — DemoGrasp has broader validation (real-world on 110 objects, 6 hands, 6 datasets vs. ResDex's simulation-only evaluation on Shadow Hand), higher reported success rates (95% vs 88.8%), and addresses the main weakness reviewers identified in ResDex (lack of real-world experiments). However, DemoGrasp has minor comparison-fairness concerns that ResDex does not. On balance, the paper is comparable to ResDex in quality but with different strengths; I place it at **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>