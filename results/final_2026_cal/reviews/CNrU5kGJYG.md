## Summary

This paper proposes TrojanTO, the first action-level backdoor attack against trajectory optimization (TO) models in offline RL (e.g., Decision Transformer, GDT, Decision ConvFormer). The attack operates in a post-training setting — modifying a pretrained model with only 0.3% of trajectories — and uses alternating training to co-optimize the trigger and model parameters, trajectory filtering for stealth, and batch poisoning for trigger consistency. A key finding is that reward manipulation (central to prior RL backdoor attacks) is ineffective for TO models; trigger design is what matters.

## Strengths

- **Novel and timely attack paradigm**: TrojanTO is the first systematic study of action-level backdoors targeting TO models in offline RL, an increasingly important class of models (DT, GDT, DC) that existing backdoor attacks cannot effectively compromise. The post-training threat model is well-motivated by the growing scale and cost of training these models.

- **Clear empirical demonstration of a non-trivial finding**: Section 4 systematically shows that reward manipulation — the foundation of essentially all prior RL backdoor attacks — has negligible impact on TO models (Figure 1), while both target action selection and trigger design are critical. This is a genuine insight rooted in the fundamental difference between TO models (conditioned behavior cloning via reconstruction loss) and traditional RL (reward maximization).

- **Component-level ablation cleanly validates the design choices**: Table 5 quantifies each module's contribution: removing alternating training drops ASR from 0.719 to 0.507; removing batch poisoning drops it to 0.528; removing trajectory filtering drops BTP from 0.914 to 0.850. This gives the reader direct evidence that each component earns its place.

- **Reasonable breadth of evaluation**: Results across 6 D4RL tasks, 3 TO architectures, and 3 target action types, plus persistent and noise-robust variants (Tables 6–7), provide a solid empirical basis for the method's generalizability.

## Weaknesses

### Major

1. **The primary results table (Table 4) aggregates over three target actions and three seeds without reporting variance or per-condition breakdowns.** The paper's own Table 1 shows that target action choice can swing ASR from 0.11 to 0.99 in the same environment (Walk). Since Table 4 averages over actions '1', 'fixed random', and 'arithmetic', the aggregated CP hides whether TrojanTO works uniformly well or relies on easy boundary targets to carry weaker ones. The paper defers per-action results to Table 24 (appendix, unavailable). Without standard deviations or per-target columns in the main table, the reader cannot assess the robustness claim. This is the single most impactful weakness because Table 4 is the paper's central evidence for "high effectiveness."

2. **The headline "~105% improvement over Baffle" compares fundamentally different threat models.** Baffle is a pre-training data-poisoning attack (10% poisoning rate, modifies the training dataset before the model is trained); TrojanTO is a post-training attack (0.3% poisoned trajectories, modifies a pretrained model with direct parameter access). The paper acknowledges this distinction in Section 3.3, yet still presents Baffle as a direct competitor in Table 4 and uses the 105% CP gap as a headline result. A post-training attack having higher ASR than a pre-training attack at 1/30th the poisoning rate is expected, not a discovery. The comparison against IMC (also post-training co-optimization) is fairer, but the Baffle framing inflates the apparent superiority. The authors should either adapt Baffle to the post-training setting or shift the narrative emphasis to the IMC comparison.

### Minor

3. **The ASR threshold ε (Equation 2) is never specified.** The value of ε directly determines whether an action is counted as "successfully" matching the target action. Without reporting it, the reader cannot interpret the absolute ASR numbers or compare them against future work. This is a straightforward fix (report ε in the main text).

4. **The defense evaluation (Section 6.5) is too brief to be informative.** It states that fine-tuning is effective and other methods are "largely ineffective" in one paragraph, with all details deferred to Appendix B.1 (stripped). While the appendix constraints are a review-process artifact, the main text should at minimum report the quantitative ASR/BTP degradation from fine-tuning so the reader can assess the attack's practical resilience.

5. **The persistent backdoor's bounded duration (~20 steps, limited by the context window) is acknowledged but under-discussed as a structural limitation.** Many RL tasks have episodes of hundreds or thousands of steps, so a 20-step persistence bound means the attacker cannot achieve long-horizon manipulation without repeated trigger activations (which increases detectability). The paper should discuss whether this is a fundamental constraint of TO-model backdoors or specific to current architectures.

### Trivial

None that carry evaluation weight.

## Nice-to-Haves

- Provide per-target-action results (ASR/BTP/CP for each of '1', 'fixed random', 'arithmetic') in the main paper alongside the aggregate, so readers can see the variance that Table 1 hints at.
- Adapt Baffle to a post-training setting (fine-tune the pretrained model with poisoned data at comparable rates) for a cleaner comparison, even as a secondary experiment.
- Include a brief analysis of whether the trigger perturbation is detectable by simple statistical tests on policy outputs (e.g., abrupt action spikes), as a complement to the BTP metric.

## Removed Points

- The harsh critic's point about "unfair comparison between attack paradigms" is partially retained (see Major #2) but the critic overstates it: the paper does acknowledge the distinction in Section 3.3, and the primary fair baseline (IMC) is present. The issue is specifically the inflated headline framing, not that Baffle should be excluded entirely.
- The "duplicate w/ RM-4 legend label" is a parser artifact, not an author error.
- The trajectory filtering criticism ("unvalidated heuristic") — the paper explicitly states the assumption and the ablation study validates it empirically. This is not a genuine weakness.
- The effective per-step poisoning rate concern is a clarification request, not a weakness.
- The "missing standard deviations" and "missing per-action breakdown" points from the harsh critic are merged into Major #1.
- Several strengths from the Strength Finder were removed for being generic ("addresses important problem," "systematic investigation") or sycophantic. Only concrete, evidence-anchored strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disaggregate Table 4**: Add a per-target-action version (or columns for each of the three target types) and include standard deviations across the three seeds. This is the minimum change needed to substantiate the robustness claim.
2. **Re-nuance the Baffle comparison**: either adapt Baffle to the same post-training setting, or replace the "105% improvement" headline with a comparison only against methods operating under the same threat model (e.g., IMC), while keeping the Baffle results as a contextual reference.
3. **Report ε**: add a sentence specifying the ASR threshold value used across all experiments.
4. **Expand the defense paragraph**: include at least one concrete number (e.g., "fine-tuning reduces ASR from X to Y after Z epochs") in the main text.
5. **Add a limitations paragraph** explicitly discussing the context-window bound and its implications for real-world attack scenarios.

## Score and Decision

Round-1 bracket: **5.0–7.5** (the paper is clearly stronger than the 3.0-range rejected RL backdoor papers and weaker than the 8.0-range papers on unrelated topics).

Round-2 anchors and comparisons:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Z3SH1xlFs6 (Beware Untrusted Simulators) | 6.50 | R1+R2 | Slightly stronger in evaluation rigor (includes variance, clearer threat model positioning); TrojanTO has stronger ablation evidence and addresses an underexplored model class. Comparable overall. |
| AC6lDj5dzl (Behavior-targeted attacks in RL) | 5.50 | R2 | Weaker novelty (equivalence to prior work noted by reviewers); TrojanTO is stronger in both novelty and contribution clarity. |
| OwinX7PI83 (Visual backdoor embodied agents) | 5.50 | R2 | Similar contribution level; TrojanTO has more thorough ablations but less complete defense discussion. Slightly stronger than this anchor. |
| 6R42MRRs50 (Plasticity-enhanced backdoors in DRL) | 4.00 | R1 | Weaker — reviewers noted inconclusive results and misguided conclusions. |
| YM23GVqQqj (Bi-level RL backdoor) | 3.00 | R1 | Much weaker — outdated literature, flawed threat model, weak evaluation. |
| 2kutK2Y8Sv (RL counterfactuality) | 6.00 | R2 | Different topic; comparable quality. |

The paper sits closest to the 6.5 anchor but is pulled slightly downward by two verified evaluation weaknesses (aggregated Table 4 without variance, inflated Baffle comparison) that the 6.5 anchor did not have. It is clearly stronger than the 5.5 anchors.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>