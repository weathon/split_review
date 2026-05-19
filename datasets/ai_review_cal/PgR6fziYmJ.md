- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have a clear picture of the paper. Let me produce the consolidated review.

## Summary

This paper proposes HP3O, a hybrid-policy variant of PPO that uses a FIFO trajectory replay buffer (storing recent policies' trajectories) and includes the best-return trajectory in every training minibatch. A second variant, HP3O+, replaces the standard value baseline with a baseline derived from the best trajectory. The paper derives policy improvement lower bounds for both variants and evaluates them on four MuJoCo continuous-control tasks against several baselines.

---

## Strengths

1. **Theoretical lower bounds for hybrid data reuse.** Theorems 1 and 2 extend the classic policy improvement guarantee (Lemma 1 from Achiam et al.) to a setting where data are sampled from a replay buffer containing trajectories from multiple prior policies with no chronological ordering constraint. This generalizes the bound in Queeney et al. (2021), which required temporally adjacent prior policies (Remark 3, line 90).

2. **Empirical evidence of variance reduction.** Figure 3a shows HP3O+ achieving the lowest normalized standard deviation among all compared methods averaged across tasks. Figure 4 further shows HP3O's explained variance remaining positive and stable in HalfCheetah while PPO's can drop to large negative values, indicating improved robustness against trajectory variation (lines 136, 140).

3. **Favorable wall-clock runtime.** Figure 3b shows HP3O/HP3O+ training time comparable to PPO and substantially lower than the off-policy baselines GEPPO and SAC, supporting the claim of a practical sample-efficiency vs. computational-cost trade-off (line 138).

4. **Broad baseline coverage.** The paper compares against 5+ baselines (PPO, A2C, P3O, GEPPO, OffPolicy, and partially SAC) across 4 continuous-control environments, which is more informative than a comparison against only vanilla PPO.

---

## Weaknesses

### Fatal
None.

### Major

1. **The best-trajectory mechanism is absent from the theoretical analysis.** Theorems 1 and 2 derive lower bounds for *random* sampling from the replay buffer, but the algorithm's distinctive feature — always including the best-return trajectory τ* in every minibatch — appears nowhere in these bounds. Remark 3 (line 90) only appeals to empirical intuition ("essentially expedites the learning process"). This means the theoretical guarantees do not justify the paper's main algorithmic innovation. A bound that accounts for the non-uniform, best-trajectory-biased sampling distribution would be needed.

2. **ε is undefined in Theorem 1 and Theorem 2.** The penalty terms in both theorems contain ε (lines 85, 107) without any definition in the main text of what ε bounds or how it relates to the buffer size or the number of prior policies. Lemma 1's penalty involves an explicit expectation over the TV distance \( \mathbb{E}_{s\sim d^{\pi_k}}[\delta(\pi,\pi_k)(s)] \), but Theorem 1 replaces this with an opaque ε. Without this definition, the theorem statements are incomplete.

3. **Missing ablation isolating the best-trajectory component.** Section 6.2 is titled "ABLATION STUDY" but does not ablate the core design choice. It compares HP3O/HP3O+ against SAC on variance and runtime, and provides robustness analysis — none of which isolates the effect of including τ* in every batch. The paper never compares HP3O (with best trajectory) against a version that samples uniformly from the FIFO buffer without guaranteed inclusion of the best trajectory. It is therefore impossible to attribute any observed improvement to this mechanism rather than to the FIFO buffer alone.

4. **The HP3O+ baseline \( V^{\pi_k^*}(s) \) is not clearly operationalized.** Lemma 3 and Theorem 2 rely on \( V^{\pi_k^*}(s) \), described as "the state value induced by the best trajectory at the moment" (line 92). The paper acknowledges that this is "not the globally optimal value, while it is approximately the optimal value up to the current time step over the last |β| episodes." However, it never specifies how \( V^{\pi_k^*} \) is computed in practice — e.g., whether it uses Monte Carlo returns from the single best trajectory, bootstraps from the critic, or some other estimator. Since the theoretical bound includes \( C^{\pi_k} = \max_s |V^{\pi_k^*}(s)-V^{\pi_k}(s)| \), the lack of a concrete definition makes the HP3O+ guarantee difficult to interpret.

### Minor

1. **Lemma 2 is stated but its inequality is not given in the main text.** The lemma statement (line 78) only lists the notation setup but does not present the actual bound that Theorem 1 is built upon. The reader cannot verify the logical chain from Lemma 2 to Theorem 1 from the main text alone.

2. **Results are mixed across environments and do not uniformly support the headline claim.** In Walker (line 128), OffPolicy clearly outperforms both HP3O and HP3O+. In Hopper, P3O achieves competitive final returns (albeit with higher variance). The paper's conclusion that both variants "are comparable to or outperform all baselines across diverse tasks" (line 128) overstates the evidence — the claim holds for some tasks but not all.

3. **The ablation study section is misnamed.** Section 6.2 is called "ABLATION STUDY" but contains no component ablation; it compares against SAC and analyzes variance and robustness. This is misleading.

4. **Explained variance metric is only briefly described in the main text.** The metric is introduced via a reference (LaHuis et al., 2014) and an intuitive description (line 140), but no formal definition appears in the main text, and results are shown for only one environment (HalfCheetah) with two algorithms (PPO and HP3O). This is insufficient to support the broader claim of robustness against data distribution drift.

### Trivial
None.

---

## Nice-to-Haves

- A sensitivity analysis on buffer size, batch composition ratio (best-trajectory to random trajectories), and number of gradient updates per step would strengthen the empirical understanding.
- A comparison against TRPO or a discussion of why it was excluded would contextualize the results.
- Reporting confidence intervals or bootstrap tests would improve statistical rigor, though single-run standard deviations with 5 seeds is standard practice in this subfield.

---

## Removed Points

These points were raised by reviewers but are excluded from the main assessment for the reasons stated:

- **GEPPO implementation suspected to be suboptimal per original paper's results.** — Speculative; not verifiable from the information on the page. The paper reports the results it obtained; without the original GEPPO paper's exact numbers and hyperparameters, there is no basis to conclude the implementation is unfair.
- **Missing related works (HER, prioritized replay).** — Cannot verify from available information.
- **Algorithm 1 missing from main text.** — This is a parser artifact (the PDF extraction stripped the algorithmic pseudocode, which existed in the original submission).
- **"Gymnasium" vs "Gym" naming complaint.** — Factually incorrect; Gymnasium is the current maintained version of the OpenAI Gym API.
- **Missing broader impacts section / missing appendix proofs.** — Parser artifact; these sections were stripped from the extracted text.
- **A2C not a strong baseline.** — Scope creep; the paper includes 5+ other baselines. Not requiring every possible baseline is acceptable.
- **Various formatting nitpicks (symbol rendering, whitespace, garbled characters).** — Parser errors, not author errors.
- **Sample complexity analysis deferred (Remark 5).** — The paper honestly acknowledges this limitation; demanding it would require expanding the paper's scope to include a separate technical contribution on nonlinear function approximation sample complexity.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews do surface a consistent pattern: the gap between the algorithm's distinctive feature (best-trajectory inclusion) and the theory (which only covers random buffer sampling) is a structural issue that neither reviewer resolves or explains. The harsh critic's identification of the undefined ε is a concrete, verifiable technical flaw; the strength finder's identification of the runtime advantage is a genuine positive that survives filtering. The two reviews agree on the missing ablation though they frame it differently.

---

## Suggestions

1. **Define ε explicitly in Theorem 1.** Restore the connection to the total-variation penalty from Lemma 2 so the theorem is self-contained.
2. **Derive or at least discuss a bound that accounts for the best-trajectory sampling bias.** If a rigorous bound is too difficult, clearly delineate what the existing theory covers and state that the best-trajectory inclusion is an empirical heuristic.
3. **Run a proper ablation:** Compare HP3O (FIFO buffer + best trajectory) against HP3O-uniform (FIFO buffer, uniform sampling, no forced best-trajectory inclusion). This is the minimum experiment needed to isolate the claimed contribution.
4. **Clarify the HP3O+ baseline computation.** Specify how \( V^{\pi_k^*} \) is estimated in practice (e.g., Monte Carlo return from τ*, bootstrapped critic value at the terminal state, or some other mechanism). Without this, the HP3O+ results are not reproducible.
5. **Tone down the claims in the abstract and conclusion.** The paper's own results show mixed performance (OffPolicy wins on Walker, P3O competitive on Hopper), so "comparable to or outperform all baselines" is inaccurate.

---
