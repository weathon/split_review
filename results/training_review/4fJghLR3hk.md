Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me write the consolidated review.

---

## Summary

This paper identifies extrapolation error — the inaccurate estimation of unseen joint action-pairs — as a critical but overlooked issue in cooperative MARL. It argues that value factorization methods (especially monotonic ones like QMIX) succeed not primarily due to representational power but because they decompose the joint error into per-agent components, making it easier to keep errors small. Building on this analysis, the paper proposes two simple modifications — annealed multi-step bootstrapping (Peng's Q(λ) with λ annealing) and ensembled TD targets — and shows that applying them to QMIX (AEQMIX) yields substantial win-rate improvements across SMAC, GRF, and SMACv2.

---

## Strengths

1. **Pervasiveness of unseen joint actions empirically quantified.** The paper measures that 20%–60% of next state-action pairs used in TD target computation are unseen during training (Figure 1a), providing concrete evidence that extrapolation error is a practical concern in MARL — not just a theoretical curiosity.

2. **Demonstration that value factorization reduces target estimation error (TEE).** Figures 1b/1c show that QMIX has substantially lower TEE than a centralized Q-function, directly supporting the claim that factorized value functions suffer less from extrapolation error. This is a clean empirical observation.

3. **Causal analysis of QPLEX's failure mode via λ_i error accumulation.** Section 3.3 and Figure 2 trace QPLEX's performance degradation to growing maximum λ_i values and show that constraining λ_i (QPLEX*) stabilizes performance. This provides more than a correlation — it intervenes on the hypothesized mechanism and observes the predicted effect.

4. **Consistent and substantial performance gains across multiple domains.** AEQMIX outperforms QMIX on 15 SMAC maps, 5 GRF maps, and 15 SMACv2 maps (Table 1), with particularly large improvements on hard/scale-variant maps. The approach also transfers to policy-based methods (AEMADDPG, AEFACMAC outperforming their baselines in Figure 3).

5. **Ablation studies validate both proposed components.** Figure 4 confirms that larger λ reduces TEE and larger ensemble size M reduces variance. Figure 5 shows both components contribute independently and synergistically, with careful discussion of when the combination fails (premature λ annealing with small ensembles).

---

## Weaknesses

### Fatal
None. The paper's core claims are supported by theoretical reasoning and empirical evidence; none of the identified issues invalidate the main findings.

### Major

- **The central interpretive claim — that value factorization's success is "largely attributable" to extrapolation error mitigation — remains a correlational narrative, not a causally established fact.** The paper provides (a) a theoretical decomposition (Taylor expansion, Eq. 4–5) showing factorization reduces error, and (b) empirical correlations (QMIX has lower TEE than centralized Q; constraining QPLEX's λ_i helps). These are consistent with the story but do not rule out alternative explanations — e.g., that factorization's success stems from better sample efficiency, reduced parameter counts, or favorable training dynamics. A controlled experiment that manipulates extrapolation error independently (e.g., by artificially injecting errors on unseen joint actions while holding the factorization structure fixed) would substantially strengthen the claim. Without it, the paper's framing overstates the uniqueness of its explanation.

### Minor

- **The proposed techniques (PQL + ensemble) are well-established in single-agent RL; the paper's algorithmic novelty is modest.** Proposition 2 (error bound scales with λ for PQL) and the variance reduction formula for ensemble averaging (Eq. 7) are known properties applied rather than derived. The paper is upfront about this ("Rather than presenting an entirely new algorithm"), but the contribution rests primarily on identifying extrapolation error as the *target* of these techniques in MARL. The connection to extrapolation error *specifically* (as opposed to generic bias/variance reduction in value estimation) is asserted rather than empirically isolated: TEE includes multiple error sources beyond extrapolation (overestimation, sampling noise), and the paper does not measure extrapolation error in isolation.

- **Limited baseline comparisons in the main results.** Only QMIX is compared extensively in Table 1. The paper discusses QPLEX, QTRAN, and MAPPO theoretically in Section 3.3 but does not include them as baselines in the main experimental tables. Including even one additional factorization method (e.g., WQMIX or a well-tuned QPLEX) in the main results would strengthen the claim that "addressing extrapolation error" (rather than simply improving QMIX) is the mechanism behind the gains.

- **Statistical reporting is incomplete.** Table 1 reports a single mean win rate per task with no visible confidence intervals, variance bars, or number of runs. Given the high stochasticity in SMACv2 and GRF, it is difficult to assess whether the improvements over QMIX are statistically significant. The paper does include learning curves (Figures 3, 5) which help, but the main summary table should report uncertainty.

### Trivial

- **Proposition 1 (EPC necessity) is argued via the gradient update rule (Eq. 6) but not presented as a formal proof.** The logic is sound: if ∂f/∂Q_i < 0, then a positive TD error decreases that Q_i, violating EPC. However, the paper does not structure this as a theorem with a proof, instead presenting it as an "illustration." This is a presentational issue, not a logical gap. The referenced proof ("follows from Kozuno et al.") in line 197 belongs to Proposition 2 (the PQL error bound), not Proposition 1 — the paper could be clearer about this.

- **The λ annealing schedule (Eq. 8) is heuristic and shows sensitivity to timing.** The paper states the schedule is "not very sensitive" (line 209) but then shows that premature annealing hurts performance (Figure 5c) and that optimal timing depends on ensemble size (line 276). These observations are reasonable but the schedule itself is ad-hoc; a systematic sensitivity analysis is missing.

---

## Nice-to-Haves

- A comparison against standard bias/variance reduction techniques from single-agent RL (e.g., TD3-style target policy smoothing, clipped double Q-learning) to isolate whether the specific choice of PQL + ensemble is uniquely beneficial, or whether simpler alternatives yield similar gains when applied to QMIX.
- A controlled experiment that injects artificial noise on unseen joint actions to test whether the performance gap between factorized and centralized methods causally depends on extrapolation error.
- Error bars / confidence intervals in the main results table.

---

## Removed Points

These points were flagged by reviewers but are removed because they are factually incorrect, misunderstand the paper, or violate the hard rules.

- **"The proof of Proposition 1 (EPC necessity) is missing and only referenced in passing as 'follows from Kozuno et al.'"** — The Kozuno et al. reference in line 197 is for **Proposition 2** (the PQL error bound), not Proposition 1. Proposition 1's argument is presented inline via the gradient update (Eq. 6): if any ∂f/∂Q_i < 0, then a positive TD error decreases that Q_i, violating EPC. The necessity direction is correctly argued; the critic confused the two propositions. This is factually wrong.

- **"The necessity of monotonicity for EPC is not proven; non-monotonic factorization might still achieve self-correction through compensatory mechanisms."** — The update rule (Eq. 6) is per-Q_i: each Q_i is updated independently according to its own partial derivative. If a particular Q_i has ∂f/∂Q_i < 0, then a positive TD error directly decreases that Q_i regardless of what other Q_j do. There is no "compensatory mechanism" — gradient descent on a per-parameter basis prevents it. The critic misunderstands the per-parameter nature of gradient updates.

- **Stray sentence fragment complaint ("3. Therefore, we use a shared mixing network.")** — This is a PDF parsing artifact from numbered list formatting, not an author editing error. Per hard rules, formatting artifacts are removed.

- **"The paper never measures extrapolation error directly"** — Extrapolation error is by definition the error on unseen state-action pairs. The paper measures TEE (Target Estimation Error), which is the standard error decomposition that captures this. Directly isolating extrapolation error from all other TEE components would require oracle knowledge of the true value function. The paper's approach is standard and appropriate.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no novel perspective on the paper that the authors have not already identified or addressed.

---

## Suggestions

1. **Add error bars or confidence intervals to the main results table** (Table 1). The current reporting of single mean win rates per task makes significance assessment impossible for the reader.

2. **Include at least one additional factorization baseline** in the main results (e.g., WQMIX or QPLEX) to show that the proposed AE modifications yield gains beyond what can be achieved by simply switching to a different factorization method. This would strengthen the claim that extrapolation error specifically is the bottleneck.

3. **Weaken the causal language** in the abstract and introduction. "Can be largely attributed to" (Abstract) is stronger than what the evidence supports. Phrasing like "is a significant contributing factor" would be more accurate and less likely to draw criticism.

4. **Add a standard double Q-learning baseline or TD3-style clipped target comparison** in the ablation study to disentangle the effect of the ensemble/PQL from the double Q-learning already used.

5. **Discuss the dynamical interaction** between the learned mixing function and the Q_i updates when arguing Proposition 1. The current analysis is per-step and assumes the mixing function is fixed; acknowledging this limitation would strengthen the theoretical framing.

---

## Score and Decision

This paper makes a useful empirical contribution by identifying extrapolation error as an important factor in MARL, providing concrete evidence of its pervasiveness and impact, and showing that simple, well-understood techniques yield substantial gains when applied with this motivation. The weaknesses are real but not fatal: the central narrative is somewhat overclaimed, the techniques are not novel, and the baseline comparisons could be broader. However, the paper delivers on its stated goal of "highlight[ing] the critical role of extrapolation errors in MARL and showcase how straightforward modifications can yield substantial performance improvements."

The paper would benefit from better statistical reporting and one additional baseline, but these are addressable. The core observation — that joint action space size makes extrapolation error a first-order problem in MARL, and that addressing it via simple means works well — is a genuinely useful insight for the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>