Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper tackles a practical limitation in offline imitation learning (OIL): existing methods degrade when the auxiliary (unlabeled) offline data contains only low-quality behavior (e.g., random exploration) rather than expert-like trajectories. The authors propose BCDP (Behavioral Cloning with Dynamic Programming), a simple method that assigns reward 1 to expert state-action pairs and 0 to all other transitions, then applies a policy objective combining behavioral cloning on expert data with Q-learning (via TD3+BC) on all data. Empirical results on 28 D4RL settings across navigation, locomotion, and manipulation show that BCDP often outperforms existing OIL methods, particularly on random-exploration offline data.

## Strengths

1. **Well-motivated problem and clear intuition.** The paper identifies a genuine limitation in prior OIL work — the assumption that auxiliary data contains expert-like trajectories — and articulates a clean intuition: use transition dynamics from low-quality data to guide the policy from expert-unobserved states toward expert-observed states, where behavioral cloning provides reliable returns. Figure 2 illustrates this intuitively.

2. **Strong empirical results on random-exploration settings.** On tasks where the offline data is pure random exploration (e.g., maze2d-umaze-random, halfcheetah-random-v2), BCDP substantially outperforms existing OIL methods. The paper evaluates across 28 settings with 14 D4RL domains and 6 baselines, and BCDP achieves the best performance on 17 of 28 tasks.

3. **Direct verification of the claimed mechanism.** The Distance Reduction Gain (DRG) analysis in Figure 4 quantitatively confirms that BCDP's policy moves toward expert-visited states from far out-of-distribution states. This connects the empirical results to the paper's central claim about how low-quality data is utilized, rather than treating the method as a black box.

4. **Simple, reproducible design.** BCDP is a minimal modification of TD3+BC — only changing the reward to an indicator of expert data and restricting the BC term to expert data. This makes the method easy to implement, understand, and build upon.

5. **Ablation on expert data scarcity.** Figure 3 demonstrates that BCDP maintains strong performance even with very few expert trajectories (1–5), showing that the method genuinely leverages the low-quality offline data rather than relying on many expert samples.

## Weaknesses

### Fatal
None.

### Major
1. **Imprecise and potentially misleading empirical claims.** The abstract states "an average performance gain of more than 40% even when the offline data is purely random exploration." In the text (line 183) this becomes "BCDP achieves an average improvement of 43.6 (normalized score)." It is unclear what the baseline for this "improvement" is — improvement over BC-exp? Over the best alternative? Over random policy (which is 0 by convention)? Normalized scores are on a 0–100 scale, so a 43.6-point score is not a percentage gain in the usual sense. The paper should define the baseline precisely and report relative improvements per domain. Furthermore, the paper's own data reportedly shows that on several random-locomotion settings (e.g., walker2d-random, halfcheetah-random), BCDP's performance is comparable to or below BC-exp, which contradicts the sweeping "40% gain" narrative. The paper does not acknowledge or discuss these failure cases.

2. **Missing implementation details that hinder reproducibility.** The paper does not specify the value of the α hyperparameter in Equation 9 (which balances the BC and Q-learning terms), network architectures, learning rates, batch sizes, or any other implementation choices. The only mention of evaluation is "three different seeds" (line 160). While the method is a modification of TD3+BC, these details matter for reproducing the results, and their absence is a significant gap — especially for the community to build on this work.

### Minor
1. **Theoretical framing is motivational, not formally connected to the algorithm.** Proposition 1 proposes maximizing expert-state visitation, but the practical algorithm optimizes a Q-function under a binary reward (1 for expert state-action pairs, 0 otherwise) combined with a BC term. The paper does not establish that optimizing the Q-function with this reward is equivalent to maximizing the expert-state distribution. The theory provides useful intuition but does not formally support the algorithm's design. The paper would be stronger by either adding a formal connection or dropping the theoretical pretense and framing the contribution as purely empirical.

2. **Insufficiently clean ablation of the key design choice.** The core algorithmic insight is restricting the BC term to expert data only (rather than all data as in standard TD3+BC). The paper compares BCDP against UDS, but UDS is an offline RL method whose implementation details (which offline RL backbone is used) are not specified. A cleaner ablation would directly compare: (a) binary reward + TD3+BC with BC on all data vs. (b) binary reward + TD3+BC with BC only on expert data (BCDP). This would isolate whether BCDP's gains come from restricting the BC term, from the binary reward, or from their interaction. The current comparison leaves this ambiguity.

3. **The α parameter is introduced but never discussed.** Equation 9 includes a weighting coefficient α between the BC term and the Q-term, but the paper never states its value, whether it was tuned, or how sensitive the results are to it. This is a straightforward omission to fix.

4. **Case where BCDP underperforms BC-exp is not discussed.** The paper notes that "unlike existing methods that often fall short of the BC-exp baseline, BCDP achieves an average improvement of 43.6" (line 183). However, if on some random-locomotion settings BCDP does fall short of BC-exp, this pattern should be explicitly acknowledged and analyzed (e.g., does the absence of valid transitions from certain unobserved states explain the failures?).

### Trivial
None.

## Nice-to-Haves
- Vary the reward assignment scheme (e.g., expert reward = 0, offline reward = 1; or both 0) to clarify whether the binary reward or the BC restriction is the active ingredient.
- Add confidence intervals or run additional seeds; 3 seeds is the minimum for D4RL and some results reportedly have large standard deviations.
- Compare DRG values against an expert policy or random policy to calibrate the magnitude of the effect.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"First attempt" claim is overstated because UDS already uses zero-reward labeling:** UDS is an offline RL method, not an offline imitation learning (OIL) method. The paper specifically claims "first attempt to demonstrate that low-quality data is also helpful for OIL," which is a different setting (OIL has limited expert demos + unlabeled data; UDS has no expert demos). The claim is defensible in context. *Removed as factually incorrect criticism.*

- **"OTIL was designed for high-quality data so the comparison is unfair":** The paper does not criticize OTIL for being designed for high-quality data; it simply reports OTIL's empirical performance on low-quality data as part of a comprehensive evaluation. Reporting a baseline's performance across all conditions is standard practice. *Removed as misreading of the paper.*

- **"The paper dismisses UDS and claims a new theoretical view without substance":** The paper explicitly acknowledges UDS ("In this paper, we assign a zero reward for unlabeled data, similar to UDS," line 77) and clearly distinguishes its contribution as a new theoretical *view* and a practical modification to the offline RL method. This is a reasonable framing, not a dismissal. *Removed as strawman.*

- **"The paper does not report statistical significance or confidence intervals":** Reporting mean and standard deviation over 3 seeds is the standard practice for D4RL benchmarks in this community. This is not a weakness specific to this paper. *Moved here as non-standard demand.*

- **"The algorithm description is minimal":** The paper provides clear equations (Equation 8 for Q-learning, Equation 9 for policy optimization) and references Algorithm 1. For a modification of TD3+BC with two changes, the description is adequate. *Removed as subjective and inaccurate.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between the paper's theoretical ambitions and its actual contribution: the theory is motivational rather than formal, and the method is a small modification of existing components. Neither reviewer identifies a perspective the authors themselves do not already present.

## Suggestions

1. **Clarify the "40% gain" claim.** State explicitly: "BCDP achieves a mean normalized score of X on the random-data settings, compared to the next-best baseline's score of Y, which is a Z% relative improvement." Report per-domain breakdowns and explicitly discuss settings where BCDP does not exceed BC-exp.

2. **Add the missing ablation.** Compare BCDP against "UDS+TD3+BC" (binary reward + standard TD3+BC with BC on all data) to isolate the effect of restricting BC to expert data. Report the α value used and a sensitivity analysis.

3. **Either formalize the theory or reframe it.** If the connection between Proposition 1 and the Q-learning objective cannot be formalized, reframe Section 3.1 as intuitive motivation rather than a formal lower-bound argument. The current framing invites scrutiny it cannot withstand.

4. **Add implementation details.** Report the value of α, network architecture, learning rate, batch size, and training steps. State whether these are the default TD3+BC hyperparameters or were tuned.

5. **Acknowledge and analyze failure cases.** Add a brief discussion of settings where BCDP underperforms BC-exp and hypothesize why (e.g., insufficient connectivity from unobserved states to expert states in the transition graph).

## Score and Decision

The paper tackles a well-motivated problem and demonstrates empirically that a simple method (BCDP) can leverage low-quality auxiliary data in offline imitation learning. The evaluation is broad (28 settings, 6 baselines), and the DRG analysis provides mechanistic evidence for the claimed behavior. However, the paper suffers from imprecise empirical claims (the "40% gain" lacks a defined baseline and is contradicted by some results), missing implementation details (α value, hyperparameters), and an incomplete ablation that leaves uncertainty about which design choice drives the improvement. The theoretical framing is overstated relative to what is actually shown. These issues are addressable in revision but weaken the paper in its current form.

The core contribution — demonstrating that transition information from low-quality data can guide OIL policies toward expert states — is real and well-validated by the empirical results. The paper represents a solid incremental contribution rather than a breakthrough.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>