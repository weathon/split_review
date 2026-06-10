Now I have sufficient calibration data. Let me compile the final review with all calibration comparisons.

**Round 1 bracket: 6.5–7.5** — TD-JEPA is clearly stronger than PSM (6.75, rejected) in the same zero-shot RL space, but needs to be compared against accepted papers at 7+.

**Round 2 narrowing: 6.75–7.5** — TD-JEPA is comparable to "Towards Principled Representation Learning from Videos" (7.25) in theoretical contribution and stronger empirically; comparable to PTGM (7.33) but with cleaner ablations; stronger than "Bridging State and History Representations" (6.75) which had inconsistent reviewer scores and inconclusive experiments.

## Summary
TD-JEPA introduces a temporal-difference latent-predictive loss for zero-shot unsupervised RL, replacing Monte Carlo latent prediction with off-policy TD learning to learn multi-step, policy-conditioned successor features from offline, reward-free transitions. The method trains state and task encoders, a policy-conditioned predictor, and parameterized policies end-to-end. The paper provides gradient-matching theorems connecting latent-predictive losses to successor measure approximation losses, non-collapse guarantees, and policy evaluation bounds, and evaluates comprehensively across 65 tasks in 13 datasets with both proprioceptive and pixel-based observations.

## Strengths
- **Novel theoretical framework connecting latent-predictive learning to successor measure approximation (Theorems 1 and 3, Section 4):** The gradient-matching proofs show optimal predictors and gradients of MC-JEPA/TD-JEPA losses match those of non-latent-predictive successor measure losses, generalizing prior single-policy results to multi-policy settings. This is explicitly claimed to generalize "all previous guarantees for latent-predictive representations" from Tang et al. (2023), Khetarpal et al. (2025), Voelcker et al. (2024), and Lawson et al. (2025).
- **TD-based loss enables off-policy multi-step policy-conditioned latent prediction (Eq. 7, Section 3.1):** Replacing the MC loss (Eq. 5, requiring on-policy successor measure samples) with a TD objective estimable from one-step offline transitions is the core technical innovation, concretely addressing the limitation that prior latent-predictive methods were "limited to single-task learning, one-step prediction, or on-policy trajectory data" (abstract).
- **Comprehensive evaluation with consistent performance (Table 1, Figure 2):** Evaluated on 65 tasks across 13 datasets from ExoRL and OGBench covering locomotion, navigation, and manipulation. The probability-of-improvement analysis (Figure 2) shows TD-JEPA is "consistently among the top performing algorithms, whereas most baselines perform well on a narrow subset of problems."
- **Strong pixel-based results (Table 1, DMC_RGB rows):** TD-JEPA achieves 628.8 average on DMC_RGB, outperforming the next-best BYOL-γ* (582.4) by ~8%, addressing "one of the most challenging settings for unsupervised RL so far."
- **Ablations isolating multi-step vs. one-step, policy-conditional vs. behavioral dynamics (Figure 3 left):** The comparison TD-JEPA vs. BYOL-γ* vs. BYOL* demonstrates "a general pattern suggesting that directly modeling policy-conditional successor measures is on average beneficial" (Section 6).

## Weaknesses

### Fatal
None

### Major
- **The adaptation experiment (Figure 4) reports only the maximum-gap task per domain.** The paper states on p. 9: "Figure 4 reports results for each DMC domain for the task in which the gap between online and zero-shot algorithms is largest." This most-favorable selection means the conclusion that "frozen representations are often sufficient for downstream learning" is supported only by cherry-picked tasks. The paper references "App. D.3 for further results," but the main-text claim overstates what is directly shown. Presenting at least the median task or aggregate results would significantly strengthen this section.

### Minor
- **Proprioceptive results are mixed, not uniformly dominant.** On OGBench proprioception, FB (39.04 avg) outperforms TD-JEPA (37.98 avg), with FB notably ahead on antmaze-me (51.60 vs 20.20). On DMC proprioception, FB wins on walker (911.5 vs 782.2) and pointmass (513.0 vs 479.3). The abstract's "matches or outperforms" is technically defensible given the probability-of-improvement analysis, and the paper is transparent about this ("TD-JEPA is only slightly preferable to FB and HILP from proprioception," p. 8), but a reader scanning the abstract might expect more decisive proprioceptive dominance.

### Trivial
None

## Nice-to-Haves
- A brief sensitivity analysis or discussion of which hyperparameters matter most would be helpful given the method's complexity (four networks, target networks, regularization coefficient, policy space).
- Quantifying the contribution of the orthonormality regularization (L_REG) vs. the TD loss itself would sharpen the paper's central claim about the importance of TD-based latent prediction.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"Policy parameterization not described in main text"** — The paper defines π_z in Section 3.3 and refers to Appendix E for implementation details, which is standard venue practice.
- **"Restrictive assumptions A1-A3 in theory"** — The paper explicitly acknowledges this (p. 5: "they can be relaxed, at the price of more involved proofs and notation, as shown in App. C") and these assumptions are shared with all cited theoretical works in this literature.
- **"BYOL* and BYOL-γ* are novel adaptations not established baselines"** — Footnote 5 (line 251) explicitly states this: "their instantiation in a zero-shot framework is novel and designed to investigate the impact of different representations." The paper is transparent; this is more of an observation than a weakness.

## Novel Insights
The paper's most novel insight is the gradient-matching argument (Theorems 1 and 3): showing that gradient descent on latent-predictive TD losses implicitly optimizes successor measure approximation losses in the multi-policy, off-policy setting. This unifies and generalizes prior theoretical results for latent-predictive representations (Tang et al., 2023; Voelcker et al., 2024; Khetarpal et al., 2025; Lawson et al., 2025) under a single proof technique and provides a principled theoretical grounding for why TD-based latent prediction should work for zero-shot RL.

## Suggestions
- Show the adaptation experiment (Figure 4) for at least the median task per domain, not just the maximum-gap task, to substantiate the claim about frozen representations.
- Add a brief sentence in the abstract acknowledging that proprioceptive gains are modest, e.g., "matches or outperforms existing methods across diverse settings, with particularly strong improvements when learning from pixels."
- Consider an ablation isolating the orthonormality regularization's contribution.

## Calibration Anchors Retrieved

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | fnO5h1CFyh.md (DHTM) | 3.0 | Weaker: narrow focus on temporal memory, limited evaluation |
| 1 | It4KL6XnPq.md (Foundation Policies with Memory) | 3.0 | Weaker: focused on memory integration, not zero-shot RL |
| 1 | 473sH8qki8.md (Reward as Observation) | 2.0 | Weaker: limited to simple environments |
| 1 | OZ3NXrF3gQ.md (RFPO) | 2.5 | Weaker: removes rewards entirely, limited evaluation |
| 1 | s9SVlWOcLt.md (Proto Successor Measure) | 6.75 | Weaker: limited to simple gridworld/FetchReach, fewer tasks, discrete spaces; TD-JEPA has far more comprehensive evaluation and stronger theory |
| 1 | o5Bqa4o5Mi.md (π2vec) | 5.25 | Weaker: policy representation for OPE, not zero-shot RL |
| 1 | OMwD6pGYB4.md (Distributional SM) | 5.75 | Weaker: theoretical novelty for distributional RL, not a competing zero-shot method |
| 1 | X5qi6fnnw7.md (Conservative World Models) | 4.75 | Weaker: extends FB but narrower scope |
| 1 | DzGe40glxs.md (Emergent Planning) | 8.0 | Stronger: interpretability focus, but different area |
| 1 | agPpmEgf8C.md (Predictive Auxiliary Objectives) | 8.0 | Stronger: neuroscience-inspired RL, different area |
| 1 | 9pW2J49flQ.md (DeepLTL) | 8.0 | Stronger: LTL-based RL, different area |
| 1 | PdaPky8MUn.md (Never Train from Scratch) | 8.0 | Stronger: long-sequence models, different area |
| 2 | ms0VgzSGF2.md (Bridging Self-Predictive RL) | 6.75 | Similar: theoretical unification of self-predictive RL but experiments inconclusive; one reviewer rated 3 for "trivial" results; TD-JEPA has clearer contribution and stronger experiments |
| 2 | 3mnWvUZIXt.md (Principled Repr Learning from Videos) | 7.25 | Comparable: theoretical contribution for repr learning with cleaner proofs but narrower experimental validation; TD-JEPA is stronger empirically (65 tasks, diverse domains) |
| 2 | o2IEmeLL9r.md (PTGM) | 7.33 | Comparable: pre-training for sample-efficient RL; TD-JEPA has cleaner ablations and more rigorous theoretical grounding |
| 2 | i8PjQT3Uig.md (Locality Sensitive Encoding) | 6.67 | Weaker: world models online, different setting |
| 2 | cWdAYDLmPa.md (State Repr with Unbalanced Atlas) | 6.67 | Weaker: dimensionality reduction approach |

**Bracket explanation:** Round 1 placed the paper between 6.5 and 7.5. TD-JEPA is clearly stronger than PSM (6.75, rejected) which addresses the same zero-shot RL problem with successor measures but has much simpler evaluation. Round 2 confirmed the paper sits near 7.0–7.5: comparable to "Towards Principled Representation Learning from Videos" (7.25) in theoretical sophistication but stronger empirically, and comparable to PTGM (7.33) but with cleaner ablations. The paper's main weakness (cherry-picked adaptation experiments) and mixed proprioceptive results prevent it from reaching 7.5+, placing it at 7.0.

## Score and Decision

**Anchoring rationale:** TD-JEPA is clearly superior to PSM (6.75, rejected, same topic, limited experiments). It is comparable to "Towards Principled Representation Learning from Videos" (7.25, accepted) — both have strong theoretical contributions, but TD-JEPA has a more comprehensive empirical evaluation (65 tasks vs. 2 visual domains). It is comparable to PTGM (7.33, accepted) — both address pre-training for RL, but TD-JEPA has cleaner theory and ablations. The paper's mixed proprioceptive results and cherry-picked adaptation experiment slightly temper the score below 7.5.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>