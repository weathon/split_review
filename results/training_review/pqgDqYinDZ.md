Now I have thoroughly read and cross-verified the paper. Let me write the final consolidated review.

## Summary

This paper proposes a multi-objective inverse reinforcement learning (MOIRL) framework for learning from heterogeneous expert demonstrations with different preferences. The key idea is that experts performing the same task share a common vectorized reward function, differing only in their preference weights. The paper introduces two algorithmic variants: (1) a consensus ADMM approach for discrete environments that iteratively solves for a common reward across experts, and (2) a continuous variant (MOIQ) that extends IQ-Learn with a preference-conditioned actor-critic architecture and a penalty term enforcing reward consensus. Experiments on Deep Sea Treasure and four MuJoCo environments show that MOIQ is competitive with GAIL baselines while using a single model, and demonstrates some ability to transfer to unseen preferences.

## Strengths

- **Novel common-reward formulation for multi-expert IRL**: The paper proposes learning a shared vectorized reward across experts differing only in preference weights (Sections 4.1–4.2). This directly addresses the inefficiency of running separate IRL runs per expert — a step beyond prior multi-expert IRL approaches like Chen et al. (2022) which still require n independent IRL runs. The paper makes the concrete architectural choice of a single preference-conditioned Q-network and policy to handle all experts.

- **Competitive empirical performance across diverse environments**: MOIQ matches or exceeds GAIL in sample efficiency and final return across DST, Mo-Hopper, Mo-Walker, Mo-HalfCheetah, and Mo-Ant (Figure 2). Table 1 shows MOIQ achieves expert-level return across 15 preference-environment settings, surpassing the expert in 4 cases. This demonstrates that the common-reward assumption does not degrade (and sometimes improves) performance relative to single-expert IL.

- **Demonstrated transferability to unseen preferences in several environments**: Figure 3 shows that for DST and Mo-Ant, the model generates reasonable vectorized returns for preferences not present in the training set (interpolated across a linear grid). This directly supports the claim that the learned common reward structure enables zero-shot preference generalization — a key advantage over methods requiring separate models per preference.

- **Practical design for reward bias mitigation**: Section 4.1.1 introduces learning a separate reward for absorbing states to address the survival bonus issue common in adversarial IRL, showing attention to implementation stability in variable-length episodes.

## Weaknesses

### Fatal
None.

### Major

1. **Transferability failures are acknowledged but not diagnosed.** In Mo-Walker and Mo-HalfCheetah (2 out of 4 continuous environments with 2D reward), the transferability results show the learned policy does not meaningfully distinguish between preferences (Figure 3). The paper attributes this to "insufficiently distinctive expert policies," but this explanation is post-hoc and unverified — no quantitative measure of expert distinctiveness (e.g., Wasserstein distance between state occupancies, reward-prediction error, or reward-recovery accuracy) is provided. Since the method's central claim is that a common reward enables transfer to unseen preferences, failure in half the applicable environments without diagnosis is a significant weakness. (Section 5.4, Figure 3)

2. **No direct evaluation of the learned reward function itself.** The paper claims to recover a common vector reward, yet every experiment evaluates only the *policy's* scalar return. As this is an IRL paper, the quality of the recovered reward function is a first-order concern. There is no measure of reward-recovery accuracy (e.g., correlation with ground-truth reward in DST where it is known, or ability to predict held-out expert preferences). Without such evidence, it is unclear whether the common-reward assumption is actually satisfied or whether performance gains come from the preference-conditioned architecture alone. (Sections 4–5)

3. **Missing standard deviations in key results.** Table 1 reports only averaged returns across 5 seeds without standard deviations or confidence intervals for the best-performance model. This makes it impossible to assess the significance of the claim that MOIQ "achieves expert-level performance" or "beats the expert" in 4/15 settings, especially since the expert's own return is averaged over only 10 demonstrations (high variance). (Table 1, Section 5.3)

### Minor

1. **Discrete ADMM experiment lacks baselines.** Figure 1 compares the proposed method only against the optimal policy, not against alternatives such as single-expert IRL per preference or multi-expert IRL without the ADMM consensus constraint. The contribution of the ADMM component therefore cannot be assessed from the discrete experiment. (Section 4.1.2, Figure 1)

2. **Continuous-case optimization derivation could be clearer.** The transition from the hard constraint `r_i = r` (Eq. 12) to the chain penalty `Σ||r_i - r_{i+1}||₂` (Eq. 13) is presented as a convenience translation without formal justification or convergence guarantees. While the chain penalty does enforce consensus when fully minimized (adjacent-pair equality implies global equality by transitivity), and this type of relaxation is common in empirical RL papers, the derivation would benefit from clearer exposition of the rationale. Additionally, the notation `r` (the common reward vector) is introduced in Eq. 12 but never used afterward. (Section 4.2.1, Eqs. 12–14)

3. **Efficiency advantage claimed but not quantified.** The paper motivates its approach partly through computational savings ("using merely a single model instead of n models"), but never reports training time, model size, FLOPs, or any efficiency metric. The claim is therefore not substantiated. (Abstract, Introduction, Section 2)

4. **Mo-Hopper transferability not evaluated.** Mo-Hopper has a 3-dimensional reward space, but transferability evaluation (Figure 3) is only shown for 2D environments. This means transferability in a meaningful fraction of the experimental settings (1 out of 5 environments, with 3D reward) is not assessed.

### Trivial
- The expert generation description in Section 5.1 contains garbled/typo-laden text ("$d_{x}^{b}$ ,t $d_{y}^{b}$ tabreg teht et rdeiasstuarnec..."). While this appears to be a parser artifact rather than an author error, if present in the original it should be cleaned up.
- Line 223: "DST-[O.I,\,O.9J\$" appears to have character corruption in the preference vector display.

## Nice-to-Haves

- An ablation study with β=0 (no common-reward penalty) would clarify whether the penalty actually contributes to multi-expert performance or whether the preference-conditioned single-network architecture is sufficient.
- A comparison against a simple multi-expert baseline (e.g., training a single IQ-Learn model on pooled demonstrations without the consensus penalty) would better isolate the benefit of the reward constraint.
- For the discrete DST environment where ground-truth reward is known, computing reward-recovery accuracy would directly test the core assumption of the method.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Continuous-case optimization is not well-defined — chain penalty does not enforce global consensus"** (Harsh Critic Critical Issue #1, part): This is factually incorrect. If all adjacent pairs r_i = r_{i+1} are penalized toward equality, transitivity enforces global consensus. The core concern about missing convergence guarantees is retained (in Minor #2 above), but the claim that the penalty "does not enforce global consensus" is removed.
- **"GAIL comparison is unfair and insufficient"** (Harsh Critic Critical Issue #2): The comparison is not unfair. MOIQ uses 10 demos per preference (same per-preference data as GAIL), and the total data advantage is inherent to the multi-expert method — it is the paper's core contribution. Comparing against a single-expert baseline that cannot share data is a standard and valid evaluation design.
- **"Discrete ADMM is unclear and likely unnecessary"** (Harsh Critic Critical Issue #3, parts): The ADMM formulation is standard consensus ADMM: separate r_i are local copies of the global variable, which is the standard ADMM setup. The notation and derivation are clear. The concern about missing baselines in the discrete experiment is retained (Minor #1 above), but the broader claim that the ADMM formulation is unclear or unnecessary is removed.
- **"The split into separate objectives in Eq. 14 does not eliminate coupling"**: Agent coupling through neighbor-dependent penalty terms is normal in distributed optimization. The paper never claims full decoupling; the "split" refers to having per-agent objectives in a multi-agent training loop, which is standard.
- **"Missing appendix/proofs/references"**: The parser strips appendix content; it exists in the original.
- **"Typos and formatting issues"**: Parser artifacts, not author errors per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that goes beyond what the authors themselves articulate.

## Suggestions

1. **Diagnose the transferability failures** by computing a quantitative measure of expert distinctiveness (e.g., pairwise Wasserstein distance between learned state-visitation distributions, or reward-recovery MSE) for each environment. This would either validate or refute the paper's own hypothesized explanation and is necessary to substantiate the core claim of common-reward-based transfer.

2. **Include reward-recovery metrics** for DST, where the ground-truth reward is known. Reporting correlation or MSE between the recovered vector reward (from the inverse soft Bellman operator) and the true reward would directly test the common-reward assumption — the paper's central theoretical commitment.

3. **Report standard deviations or confidence intervals** in Table 1 and in key results throughout, so readers can assess the significance of the reported performance.

4. **Add at least one ablation** with β=0 to disentangle the contribution of the common-reward penalty from the preference-conditioned architecture.

5. **Quantify the efficiency claim** with wall-clock training time or model size comparisons to n independent models.

## Score and Decision

The paper addresses a worthwhile problem with a sensible architectural approach and provides initial empirical validation. The core idea — assuming a common vector reward across experts with different preferences — is a natural and potentially useful inductive bias for multi-expert IRL, and the preference-conditioned single-model architecture is practically motivated. However, the paper has significant evidential gaps: the main claim (that a common reward enables transfer) is only partially supported (failing in 2 of 4 2D environments, without diagnosis), the learned reward itself is never directly evaluated despite being the central object of the method, and the experimental reporting lacks standard deviations in key tables. These issues are addressable but require additional experiments and analysis that go beyond what can be fixed in a short rebuttal.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>