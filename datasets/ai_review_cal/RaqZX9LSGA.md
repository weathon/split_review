- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize the review carefully, verifying each claim against the paper text.

---

## Summary

This paper formalizes stochastic execution delay in MDPs (SED-MDPs), proving that Markov policies remain sufficient for optimality even under stochastic delays (extending Derman 2021's result for constant delays). It then proposes DEZ (Delayed EfficientZero), which uses observed delays and a learned forward model to predict future states and perform MCTS-based action selection. Experiments on 15 Atari games under both constant and stochastic delay settings show DEZ achieving higher average scores than oblivious EfficientZero and Delayed-Q.

## Strengths

- **Formalization of SED-MDPs and effective decision time (Section 4).** The paper provides a clean probability-space formalism for stochastic execution delay, defining the effective decision time (Eq. 1) that maps each current time step to the most recent action available for execution. This is a principled foundation that prior stochastic-delay work lacked.

- **Proof of Markov policy sufficiency for stochastic delays (Theorem 2, Section 4.2).** The theorem shows that for any history-dependent policy and any fixed realization of the delay process, there exists a Markov policy that matches the conditional distribution. This extends the prior result of Derman (2021) from deterministic to stochastic delays, providing theoretical grounding for policy search in a smaller class.

- **Novel algorithmic design (Section 5, Fig. 2).** DEZ maintains separate queues for past actions and observed delays, computes effective decision times to resolve which action is actually being executed, and uses a learned forward model to predict the future state at the effective decision horizon before performing MCTS. This is the first model-based algorithm to address stochastic execution delay without state augmentation.

- **Strong empirical results across both delay types (Section 6).** DEZ achieves the highest average score in 39/45 constant-delay experiments and 42/45 stochastic-delay experiments across 15 Atari games at three delay magnitudes (M=5,15,25). The consistent advantage over both oblivious EfficientZero and Delayed-Q across such a range of games and delay values provides evidence that the approach is broadly effective.

- **Sample efficiency.** DEZ operates with only ~130K environment interactions, building on EfficientZero's sample efficiency and far below the 1M samples Delayed-Q originally required. This demonstrates that handling delays need not sacrifice data efficiency.

## Weaknesses

### Major

- **Unequal training budget confounds the primary empirical comparison (Section 6, line 218).** The paper states DEZ uses 130K interactions while EfficientZero (the baseline) sampled 100K transitions — a 30% data advantage. Although the paper is transparent about this, the claim of "significantly outperforms the baselines" is weakened because the performance gap could be partly attributable to the extra 30K steps rather than the delay-handling mechanism itself. The paper does not include a controlled ablation (e.g., training DEZ with 100K steps) to isolate the effect of the algorithmic contribution from the extra data. Since this is the headline empirical claim, the confound needs to be addressed.

### Minor

- **Theorem 2's scope and its relationship to DEZ's actual policy class (Section 4.2 vs. Section 5).** Theorem 2 states that for each fixed delay sequence \(z\), there exists a Markov policy (on the original state space \(\mathcal{S}\)) matching the history-dependent policy's distribution. However, DEZ's policy depends on the predicted future state \(\hat{s}_{t+z_t}\), which is a function of the current state, the action queue, and the observed delay \(z_t\) — more information than \(s_t\) alone. The paper claims "DEZ yields non-stationary Markov policies, as expected by our theoretical findings" (line 24), but the link is not fully spelled out: the theoretical result is about policies on \(\mathcal{S}\), while the algorithm uses a richer input representation. This does not invalidate either the theory or the algorithm, but the paper should clarify how they relate (e.g., by noting that with observed delays, the effective state space is \(\mathcal{S} \times [M]\), making the policy a Markov policy on the augmented state).

- **Only one stochastic delay distribution tested (Section 6.2, lines 259–270).** The stochastic delay follows a single random-walk process (probabilities 0.2/0.2/0.6, starting at \(M\), continuing across episodes). The paper claims DEZ is "agnostic to the delay distribution" (line 24), but this claim is not empirically supported — only one distribution is evaluated. Demonstrating robustness on at least one alternative distribution (e.g., uniform over \([0,M]\), or a different Markov chain) would substantially strengthen the claim.

- **No variance/error bars in the main bar plots (Fig. 3, line 229).** The bar plots in the main text show only mean scores without error bars or confidence intervals. The paper notes that standard deviations are in the appendix (line 237). While not missing, putting this information in the main figures would make it easier for readers to assess the reliability of the results.

- **Algorithm description leaves some ambiguity about "expected pending actions" (Section 5, line 188).** The phrase "we take the expected pending actions denoted by \([\hat{a}_t, \dots, \hat{a}_{t+z_t-1}]\)" is not fully specified — it is unclear whether these are actions already committed from prior effective decision times, or predictions from the current policy. The text refers to Fig. 2 and the effective decision time mechanism (line 191), but a brief explicit statement (e.g., "these are the actions that have been prescribed at past decision times and are queued for execution at future time steps") would eliminate ambiguity.

### Trivial

- Line 14: "often overlooked its nature" — grammatical issue.
- Line 63: "which we assume to be equipped with" — minor phrasing.
- The caption of Fig. 3 references "15 Atari games and delays \(M\in\{5,15,25\}\) over 32 test episodes per trained seed" but does not state how many seeds were used.

## Nice-to-Haves

- **Budget-controlled ablation.** Training DEZ with exactly 100K steps (matching the baseline budget) and reporting the performance difference would cleanly address the primary confound.
- **Ablation: forward model accuracy.** Reporting prediction error (e.g., MSE between \(\hat{s}_{t+k}\) and true \(s_{t+k}\) as a function of horizon \(k\)) would directly support the claim that the dynamics model is "exceptionally precise."
- **Alternative delay distributions.** Testing at least one additional stochastic delay process (e.g., uniform over \([0,M]\)) would strengthen the claim of distribution agnosticism.
- **Forward model ablation.** Comparing DEZ against a version that uses the same queues/effective decision times but without the learned forward model (e.g., using the last observed state \(s_t\) directly as the MCTS input) would help isolate the benefit of future-state prediction.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "DEZ outperforms baselines on both delay types" (Strength Finder #2).** While the results are reported, the budget confound weakens the strength of this claim. Moved here per the rule that when a strength and verified weakness conflict, the weakness prevails.
- **Strength: "Agnosticism to delay distribution" (Strength Finder #5).** Only one stochastic delay distribution was tested, so the empirical support for this claim is limited. Moved here due to conflict with the verified weakness about limited distribution testing.
- **Harsh Critic Critical Issue 3 (Weak baselines and missing controls).** The critic claims baselines are weak, but the paper compares against the best available delay-handling baseline (Delayed-Q, the SOTA from Derman 2021) and the non-delay version of its own algorithm. Suggestions to use state augmentation are explicitly infeasible for large \(M\) (the paper notes exponential complexity). Testing Delayed-Q at 1M budget would change the experimental setting (100K benchmark). This criticism overstates the problem; the existing baselines are standard for the setting.
- **Harsh Critic Section-by-Section notes about replay buffer temporal mismatch.** The paper describes storing \((s_t, a_{\tau_t}, r_t)\) where \(a_{\tau_t}\) was chosen at an earlier time \(\tau_t\). This is a deliberate design choice — the effective decision time framework explicitly handles which action is being executed at each step — not an oversight.
- **Harsh Critic note about "stochastic delay continues across episodes" being unusual.** The paper explicitly motivates this choice (line 272: "By doing that, we do not assume an initial delay value and cover a broader range of applications"). It is a design decision, not a flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the budget confound.** Add an experiment training DEZ with 100K steps (matching the EfficientZero baseline) and report the results. If the performance gap persists, the empirical claim is much stronger. If it narrows, report honestly and adjust claims accordingly.
2. **Clarify the theory–algorithm link.** Add a brief note in Section 4.2 or 5 explaining that since delays are observed, the effective state for the policy is \((s_t, z_t,\) queue state), and the Markov policy result on \(\mathcal{S}\) extends naturally to a Markov policy on this augmented representation.
3. **Add error bars to main figures.** Move the standard deviation information from the appendix into the main bar plots, or at minimum add a table of means ± std in the main text.
4. **Define "expected pending actions" unambiguously.** In Section 5, add one sentence clarifying that the pending actions come from the queue computed via effective decision times (Eq. 1), not from online policy predictions.
