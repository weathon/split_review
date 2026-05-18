I now have all the information needed. Here is the consolidated final review:

---

## Summary

This paper tackles offline imitation learning (OIL) where only limited expert demonstrations and reward-free auxiliary data (possibly random exploration) are available. The key insight is that transition information in low-quality offline data can guide an agent from expert-unobserved states toward expert-observed states. The authors propose BCDP, which combines behavioral cloning on expert data with TD3+BC-style Q-learning (using indicator rewards for expert transitions) on all data. Empirically, BCDP achieves best performance on 17 of 28 D4RL tasks and significantly outperforms prior OIL methods, especially when the auxiliary data is purely random.

## Strengths

- **Empirically demonstrates that low-quality auxiliary data benefits offline IL.** Prior OIL methods (DemoDICE, DWBC, OTIL) assume high-quality behavior in the auxiliary data and degrade when it is absent. BCDP instead uses transition information from low-quality data to steer toward expert states, yielding strong results across navigation, locomotion, and manipulation. The paper supports this with 28 settings on D4RL.

- **Strong empirical results.** BCDP achieves best performance on 17 of 28 tasks, and the paper reports a 43.6 normalized-score average improvement over baselines when the offline data is purely random. Ablations with 1–5 expert trajectories show BCDP remains effective even under extreme expert scarcity.

- **Simple, practical algorithm.** BCDP is a clean modification of TD3+BC: it applies the behavioral cloning term only to expert data and uses indicator rewards for expert transitions in the Q-learning objective. The simplicity aids reproducibility and deployment.

- **Direct empirical verification of the proposed mechanism.** The Distance Reduction Gain (DRG) metric confirms that BCDP's policy indeed moves toward expert-observed states from out-of-distribution states, supporting the core intuition.

## Weaknesses

### Major

1. **Theory-algorithm gap.** Proposition 1 defines a policy that, on expert-unobserved states, should maximize the *discounted probability of reaching expert-observed states* (i.e., Σ γ^t Pr(s_t = s'|π)·I[s'∈D^E]). The actual algorithm learns a Q-function with reward r(s,a)=I[(s,a)∈D^E], which maximizes the discounted *number of expert state-action pairs visited*, not the discounted occupancy of expert *states*. These are different objects (the Q-function rewards reaching expert actions, not just expert states), and the paper never formally derives that the BCDP objective (Equation 9) implements or approximates Proposition 1. The lower bound analysis (Equation 7) shows that maximizing the expert-state distribution improves J(π), but it is not shown that BCDP's optimization actually solves this maximization. Without this connection, the theory reads as post-hoc motivation rather than a formal grounding. This weakens the claimed theoretical contribution and leaves the paper's value resting primarily on its empirical results.

2. **Overstated novelty relative to UDS.** The paper claims "the first attempt to demonstrate that low-quality data is also helpful for OIL" (abstract, Section 3.3). However, UDS (Yu et al., 2022) — which the paper itself uses as a baseline — already uses zero-reward labeling on unlabeled offline data with an offline RL algorithm and shows it helps. The distinction (UDS is offline RL vs. this paper is offline IL) is meaningful but narrow, and the paper's own experiments show UDS is often competitive (e.g., within ≤5 normalized points of BCDP on several random-data settings). A more measured positioning — e.g., "first to show this benefit specifically in the reward-free OIL setting" — would be more accurate and avoid overclaiming.

### Minor

1. **High variance in several tasks reduces statistical confidence.** The paper reports results from three seeds and claims BCDP "significantly outperforms" baselines, but in several settings the standard deviations overlap substantially. For example, on halfcheetah-medium-v2, BCDP scores 66.9±8.2 vs. DWBC 67.9±6.5 and OTIL 70.5±7.4 — all within one standard deviation. The "significantly outperforms" claim lacks formal statistical tests and would benefit from them.

2. **DRG analysis limited to navigation tasks.** The empirical verification of the proposed mechanism (Section 4.3) is only conducted on maze2d navigation tasks. The paper acknowledges that in locomotion the agent may get stuck in states from which expert states are unreachable, but does not quantitatively analyze this failure mode. Extending the DRG-style analysis to locomotion/manipulation (or at least characterizing when the method fails) would strengthen the claims.

3. **The Lemma 1 lower bound depends on d_0(s) and may be vacuous.** The bound on expert-observed states involves 1/d_0(s). For expert-unobserved states that are unreachable from the initial state distribution under the expert policy, the bound may not provide a meaningful guarantee. The paper does not discuss this condition.

### Trivial

None. *(Several minor phrasing inconsistencies and formatting artifacts noted by reviewers are parser issues, not author errors.)*

## Nice-to-Haves

- Extend the DRG analysis to locomotion and manipulation tasks (or systematically characterize when the guidance toward expert states succeeds vs. fails).
- Provide formal statistical significance tests (e.g., paired bootstrap) for key comparisons where standard deviations overlap.
- Clarify the connection between Proposition 1 and the algorithm more explicitly, or reframe the theory section as intuition/motivation rather than a formal derivation.

## Removed Points

These points from the reviewers were flagged as not valid weaknesses and are removed from the main review:

- **"Algorithm 1 content is missing"** — The parser strips non-text content; this exists in the original submission.
- **"Undisclosed hyperparameters (α, learning rates, etc.)"** — These details were likely in the appendix (stripped by the parser); the paper mentions "three different seeds" and standard experimental methodology.
- **"UDS baseline implementation unclear"** — The paper states "We have selected TD3+BC as our most similar offline RL algorithm, which allows it to be considered as an ablation study," making the implementation sufficiently clear.
- **"Missing related works / baselines"** — The baseline set (BC-exp, BC-all, DemoDICE, DWBC, OTIL, UDS) is standard and defensible for the OIL setting.
- **"Missing appendix content"** — Removed per parser-stripping rules.
- **"Formatting/style nitpicks"** (e.g., "distance deduction" vs. "distance reduction") — These are parser artifacts from PDF extraction; the original submission does not have these issues.

## Novel Insights

None beyond the paper's own contributions. The reviewer critiques do not synthesize new observations about the paper's approach that the authors themselves missed. The core finding — that transition information from low-quality data can guide agents toward expert states — is well articulated by the paper.

## Suggestions

1. **Strengthen the theory-algorithm connection.** Either (a) derive conditions under which the Q-learning objective (r(s,a)=I[(s,a)∈D^E]) approximates the Proposition 1 goal of maximizing expert-state occupancy, or (b) reframe Proposition 1 and Lemma 1 as motivation/intuition and clearly state that the algorithm is an empirically motivated heuristic.

2. **Temper the novelty claims.** Replace "first attempt to demonstrate that low-quality data is also helpful for OIL" with a more precise claim that acknowledges UDS as the closest prior approach. For example: "We demonstrate that, unlike prior OIL methods which assume high-quality auxiliary data, BCDP can benefit from low-quality offline data — even random exploration — by leveraging transition information."

3. **Add a clean ablation isolating the BC-placement decision.** Compare BCDP against UDS+TD3+BC (BC on *all* data + zero-reward Q-learning) to directly measure the effect of restricting BC to expert data only. The paper hints at this ("allows it to be considered as an ablation study") but does not present it explicitly.

4. **Report statistical significance or confidence intervals** for the main results table, especially for settings where standard deviations overlap.

## Score and Decision

**Originality:** The paper's core idea — using transition information from low-quality data to navigate toward expert states in OIL — is reasonable but not groundbreaking. The novelty is partly eroded by the similarity to UDS, but the specific application in the reward-free OIL setting is new.

**Importance of research question:** The question of leveraging low-quality auxiliary data in OIL is practically important and well-motivated.

**Claims supported:** The core empirical claim (BCDP benefits from low-quality data) is well-supported by experiments. The theoretical claim (Proposition 1 grounds the algorithm) is only loosely supported.

**Soundness of experiments:** Generally sound but weakened by high variance in some settings, lack of statistical tests, and the DRG analysis being limited to navigation.

**Clarity of writing:** Clear and well-organized. The main algorithm and intuition are easy to follow.

**Value to the community:** The paper provides a simple, effective baseline for future OIL work and convincingly shows that the common assumption of high-quality auxiliary data is unnecessary.

**Overall:** This is a solid empirical paper with a simple and effective algorithm, strong results, and a well-motivated problem. The main weaknesses are the gap between the theory and algorithm, and somewhat overstated novelty claims. These are fixable. The paper makes a useful empirical contribution.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>