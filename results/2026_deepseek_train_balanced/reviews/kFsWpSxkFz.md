## Summary

MetaUrban is a compositional simulation platform purpose-built for AI-driven urban micromobility (delivery bots, electric wheelchairs, mobility scooters, etc.). It contributes: (1) a procedural scene generation pipeline with hierarchical layout generation grounded in real-world urban design standards, scalable obstacle retrieval using VLM-driven open-vocabulary search over real-world object distributions, and cohabitant population with diverse dynamic agents; (2) a large-scale benchmark dataset (MetaUrban-12K: 12,800 training + 1,000 test scenes); and (3) baselines across RL, Safe RL, Offline RL, and IL on PointNav and SocialNav tasks, along with a cross-machine evaluation studying how mechanical parameters affect policy learning.

## Strengths

- **First simulator purpose-built for urban micromobility, with systematic differentiation from prior work.** Section 2 explicitly compares MetaUrban against three categories of existing simulators (indoor: Habitat, AI2-THOR, iGibson; driving: CARLA, MetaDrive; social navigation: SEAN 2.0, SocNavBench) and demonstrates that none address sidewalks, plazas, crosswalks, or the specific obstacle/terrain/pedestrian configurations unique to micromobility. The paper states: "none of the recent simulation platforms have been constructed for urban micromobility" (lines 107-108), a claim well-supported by the related work.

- **Real-world grounded obstacle distribution is methodologically thorough.** Section 3.2 describes a systematic pipeline using CityScape, Mapillary Vistas, 25,000 Google Street images from 50 countries across six continents, GPT-4o, Grounded-SAM, and a survey of 10 urban design handbooks to build a 1,215-item object description pool. This multi-source grounding in real-world urban data is substantially more rigorous than the hand-picked or fully synthetic object sets used by most indoor simulators (e.g., ProcTHOR).

- **Cross-machine evaluation yields genuinely actionable insights.** Table 2 provides mechanical specifications for five machine variants (COCO base/mod-1/mod-2, wheelchair, mobility scooter) with concrete parameters (max speed 5–45 km/h, engine force 100–650 N) and measures impact on SR, SPL, and Cost. The finding that reducing a delivery bot's max speed from 30 to 10 km/h improves both mobility and safety (SR 47%→62% on straight blocks, Cost 0.32→0.28) is a concrete, actionable design insight that no existing simulator can provide. This is a genuinely distinctive feature of MetaUrban.

- **Candid admission that tasks are far from solved.** The authors honestly report that the highest success rates are only 66% (PointNav) and 36% (SocialNav), noting "the tasks are far from being solved" (line 284). This appropriate calibration for a benchmark paper stands in contrast to some overclaiming elsewhere in the paper.

## Weaknesses

### Fatal
None.

### Major

1. **The "generalizability" evidence does not characterize the distribution shift.** The paper constructs a "MetaUrban-unseen" test set of 100 scenes and claims models exhibit "strong generalizability" (lines 285, 347), describing these as "out-of-distribution scenes" (line 347). However, the paper never specifies *how* MetaUrban-unseen differs from MetaUrban-train/test — whether through different block topologies, different object category distributions, different terrain types, or merely different random seeds from the same generator. Line 223 states MetaUrban-finetune has "the same distribution of MetaUrban-unseen," but neither is defined relative to the training distribution. Without this characterization, the reader cannot assess whether the 41% average unseen success rate (PointNav) represents genuine generalization to shifted environments or simply interpolation within the same generative distribution. This gap undermines the paper's strongest claim.

2. **The benefit attributed to "compositionality" is not isolated from the benefit of more data.** The scaling experiment (Figure 3(b)) shows that increasing training scenes from 5 to 1,000 improves success rate from 12% to 46%. The paper attributes this to MetaUrban's "compositional nature" (lines 17, 353). However, no ablation compares compositional generation against a non-compositional baseline that produces the same number of scenes (e.g., a random sampler that ignores functional zone structure, or a fixed set of hand-designed scenes with identical diversity). The observed scaling curve could simply reflect standard data-driven improvement. The claim that compositional structure is the causal factor requires a controlled comparison that the paper does not provide.

### Minor

3. **No limitations section.** The paper ends abruptly with the conclusion (line 362). For a platform paper aiming to become community infrastructure, an explicit discussion of sim-to-real gap, physics fidelity constraints, computational cost of generating 12,800 scenes, and the within-distribution nature of the generalization test would build credibility and help users assess appropriate use cases.

4. **The "10,000 high-quality obstacles" claim is unsubstantiated.** The pipeline description in Section 3.2 is thoughtful, but no quality assessment is reported — e.g., what fraction of the 10,000 retrieved objects are geometrically valid, correctly scaled, properly oriented, or usable in simulation? A failure analysis of the retrieval pipeline (e.g., precision@k against human judgment) would significantly strengthen this contribution.

5. **Cross-machine evaluation lacks statistical rigor.** Table 2 reports results for 5 machine configurations on 2 scene types with 1 training method (PPO). No confidence intervals, standard deviations across multiple runs, or statistical significance tests are reported. The findings (e.g., "decreasing max speed to 10 km/h improves performance") could be sensitive to PPO training hyperparameters and random seed.

6. **No physics engine or parameter validation is reported.** The paper does not state which physics engine is used or whether the friction coefficients, engine forces, and brake forces in Table 2 correspond to measurements from the actual COCO Robotics delivery bot, wheelchair, and mobility scooter. If these values are estimated/assumed rather than measured, the cross-machine evaluation is an interesting sensitivity analysis but not a validated design tool.

7. **The claim about social navigation platforms is asserted without quantitative backing.** Line 103 states existing platforms make scenes "not applicable to complex urban micromobility tasks" due to "oversimplified objects and surrounding environmental structures." This is likely true but no quantitative comparison of scene complexity (number of static assets, area size, terrain variation) between MetaUrban and SEAN 2.0 or SocNavBench is provided.

### Trivial
None.

## Nice-to-Haves

- A structurally held-out generalization test (e.g., train on straight/T-junction blocks only, test on roundabout/circle blocks; or train with ≤8 objects per block and test with ≥15) would cleanly demonstrate that compositional training enables handling genuinely novel configurations, not just more data from the same distribution.
- A small-scale sim-to-real validation — e.g., comparing collision rates of a simple policy across a real sidewalk course and its simulated replica — would ground the safety claims even without full deployment.
- Reporting computational cost (generation time, storage, rendering speed) would help the community assess practical usability.

## Removed Points

These points were flagged by reviewers but filtered under the removal rules. Treat them with caution — none represent valid weaknesses of the paper.

- **"Safety is evaluated entirely within simulation with no real-world grounding":** The harsh critic argued the paper needs real-world validation of safety metrics. This is outside the standard scope of a simulation platform paper. Simulators evaluate safety in simulation by design; demanding real-world deployment experiments is a scope mismatch. The paper's safety claims are about simulated cost metrics, which is standard. *Rationale: scope creep / standard community practice.*
- **"Observation space is LiDAR + state vector, not camera-based":** The paper clearly states the observation design (lines 276-277). This is an explicit design choice for efficiency and simplicity, not a weakness. *Rationale: the paper transparently describes its design; criticizing a design choice is not a valid weakness.*
- **"First simulator claim should be tempered":** The related work section (lines 83-107) provides thorough evidence that no prior platform targets micromobility on sidewalks, plazas, and crosswalks. The claim is well-supported. *Rationale: factually supported; not a weakness.*
- **"Statistical significance not reported" (moved from potential Major to Minor above):** The point is valid but not severe enough to be a major weakness. *Rationale: recalibrated severity.*
- **"No physics validation details" (moved from potential Major to Minor above):** A fair observation but standard for simulation platform papers to omit this level of detail. *Rationale: recalibrated severity.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's generalizability claims and the evidence, and the need to isolate compositionality from data quantity — but these are standard peer-review observations rather than novel insights.

## Suggestions

1. **Clarify what "unseen" means.** Specify how MetaUrban-unseen differs from MetaUrban-train in terms of block types, object distributions, terrain configurations, or agent dynamics. If the shift is structural (different block topologies), state this explicitly. If it is merely different random seeds, recalibrate the claim from "strong generalizability" to "robustness to held-out samples."
2. **Add a limitations section** covering: sim-to-real gap, physics fidelity, within-distribution nature of generalization testing, and computational cost.
3. **Add a controlled ablation for compositionality.** Compare compositional generation against a non-compositional baseline (e.g., randomly placed objects ignoring functional zones) with the same number of scenes and total training steps. This would isolate whether compositionality drives improvement or merely data quantity.
4. **Report variance** (standard deviations over ≥3 seeds) for the cross-machine evaluation results in Table 2.
5. **Add a quality assessment** of the obstacle retrieval pipeline — e.g., human-rating of a random sample of 200 retrieved objects for geometric validity, correct scale, and appropriateness for urban scenes.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>