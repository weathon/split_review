Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me construct the consolidated review.

---

## Summary

This paper studies decentralized multi-player multi-armed bandits (MMAB) with stochastic delayed feedback, a setting that is realistic for cognitive radio networks but under-explored in the literature. The authors propose DDSE (Decentralized Delayed Successive Elimination), which uses a leader-follower architecture with a periodic fixed-schedule communication phase. The key algorithmic innovation is the use of lagged best-arm sets ($\mathcal{M}_{p-q}$) to maintain synchronization despite delayed feedback. The paper provides both a centralized lower bound and a decentralized upper bound, and evaluates the algorithm on synthetic and real-world spectrum data.

## Strengths

- **Novel problem formulation with practical motivation.** The paper addresses decentralized MMAB with *stochastic* delay (sub-Gaussian model), which is realistic for cognitive radio networks and genuinely under-studied. Nearly all prior work on decentralized MMAB assumes immediate feedback, so the problem framing is timely and well-motivated.

- **Interesting algorithmic idea.** The use of lagged best-arm sets $\mathcal{M}_{p-q}$ to prevent miscoordination under delay is a non-trivial and plausible mechanism. The three-part communication phase (remove arm, add arm, notify end) is described at a conceptual level and is a reasonable extension of Wang et al. (2020) to handle delay.

- **Both lower and upper bounds provided.** Theorem 1 gives a centralized lower bound for MMAB with delay, and Theorem 2 provides an upper bound for DDSE. The main $\log(T)/\theta\Delta_k$ term is aligned, and the paper quantifies the gap as an additive term independent of $T$. This is more thorough than many MMAB papers.

- **Relaxed delay assumption.** Instead of assuming a fixed bounded delay $d_{\max}$, the paper adopts a sub-Gaussian model (Assumption 1), which allows rare large delays and better matches real cognitive radio networks. This is a methodological improvement over standard bounded-delay assumptions.

- **Ablation via DDSE without delay estimation.** The paper provides both a theoretical bound (Theorem 3) and experimental comparison against a version that does not estimate delay, clearly isolating the benefit of the $\mathcal{M}_{p-q}$ coordination mechanism.

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm specification is too vague for reproduction.** The paper's central algorithmic mechanism — using $\mathcal{M}_{p-q}$ sets to maintain synchronization — hinges on the phase offset $q$ (how many communication phases to look back). The paper states that $q=0$ when "delay is sufficiently small" (line 146) but never specifies how $q$ is computed as a function of the estimated delay distribution $(\hat{\mu}_d, \hat{\sigma}_d^2)$. Similarly, the paper claims players "estimate delay parameters" (abstract, line 33) but provides no method for doing so, and does not specify how the leader selects which arms to remove ($a_p^-$) and add ($a_p^+$) (line 134 merely denotes these symbols). The quantile $\theta$ used throughout the bounds is never tied to any concrete algorithm choice. Without operationalizing these steps, the algorithm cannot be implemented or evaluated independently. This is the most significant weakness in the paper.

2. **The lower bound (Theorem 1) can become negative and thus trivial.** The bound includes the term $(\mathbb{E}[d] - \sigma_d\sqrt{\frac{\theta}{1-\theta}})\frac{M}{2K}\sum_{k>M}\Delta_k$. For sub-Gaussian delay with $\sigma_d$ large relative to $\mathbb{E}[d]$, this term can be negative, making the entire bound vacuous (regret is always non-negative, so a negative lower bound provides no information). While a negative bound is technically valid, it undermines the paper's claim that the bound demonstrates near-optimality. The paper needs to either specify a regime where the bound is provably positive or provide a tighter derivation.

3. **Experiments lack baselines adapted for delay.** All baselines (SIC-MMAB, MCTopM, Selfish, Game of Throne, ESER) were designed for immediate feedback and are applied without any delay-handling adaptation. The paper does not include a simple adapted baseline — e.g., taking SIC-MMAB or another algorithm and wrapping it with observation buffering (collecting feedback over a window and then running the algorithm on the buffered data). Without this, the experiments show only that algorithms not designed for delay fail under delay, not that DDSE's specific mechanism is necessary or superior to a trivial adaptation. The comparison against "DDSE without delay estimation" partially addresses this, but it is an ablation of the same algorithm rather than an independent baseline adaptation.

4. **Real-world experiments do not measure regret, disconnecting from theory.** Section 5.2 evaluates algorithms on cumulative throughput and collisions (using real spectrum data) but never computes regret. Since the paper's core theoretical claims are about regret bounds, the absence of regret evaluation in the real-world experiment makes it impossible to connect these results to the theory. Throughput and collisions are reasonable practical metrics, but they should be supplemented with regret computation.

### Minor

1. **Gaussian rewards in experiments vs. $[0,1]$ assumption in theory.** The theoretical setup assumes rewards in $[0,1]$ (line 46), but the experiments use Gaussian rewards (line 223). While this is common practice in bandit papers (Gaussian with controlled variance), it is an inconsistency that should be acknowledged and justified.

2. **Limited sensitivity analysis.** Only one value of $\sigma_d$ is tested in the main $\mathbb{E}[d]$ experiments (Figure 1 uses $\sigma_d=50$, default experiments use $\sigma_d=100$). Since the regret bounds depend on $\sigma_d$, varying $\sigma_d$ independently would strengthen the empirical evaluation. Similarly, the paper does not test edge cases like $M=K$ (saturated) or $M=1$ (single-player).

3. **No regret-over-time plots.** Only final regret bar charts are reported. Plotting regret as a function of time would reveal whether DDSE's advantage is sustained or transient.

### Trivial
None.

## Nice-to-Haves
- A concrete worked example (with small $K, M$ and a specific delay realization) showing how the $\mathcal{M}_{p-q}$ mechanism prevents collisions would substantially clarify the algorithm.
- An ablation comparing DDSE against a version that always uses $q=0$ (no waiting) would directly measure the benefit of the lagged-set mechanism, isolating it from the comparison with delay-agnostic baselines.
- Including regret-over-time plots for both synthetic and real-world experiments.

## Removed Points

These are not my assessments but points raised in reviews that were removed per policy. Treat with caution:

1. *"Missing algorithm pseudocode / appendix stripped."* — The paper states "Algorithm 1 describes DDSE from the view of the leader" (line 127). Full pseudocode and proofs existed in the original submission; the parser strips these. Per policy, criticisms about missing appendix or algorithm text in the submission are removed.
2. *"No error bars or confidence intervals."* — The paper explicitly states "The interval and shadow in our figures represent the standard error" (line 223). This claim is factually wrong and removed.
3. *"20 runs is too small."* — 20 independent runs with standard error is standard practice in bandits and ML experimentation. Removed as a nitpick.
4. *"Cites no prior work on delayed MMAB."* — Per policy, I cannot verify or challenge the existence of missing related work. The paper claims a novel problem formulation; demanding citations for nonexistent prior work is not valid.
5. *"Missing related works, trivial formatting/presentation nits."* — Removed per policy where they concern parser artifacts or unverifiable literature gaps.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the paper that the authors themselves did not articulate.

## Suggestions

1. **Operationalize the algorithm.** Specify exactly how $q$ is computed from estimated delay parameters, how $\theta$ is chosen, and how $a_p^-$ / $a_p^+$ are selected. A brief pseudocode sketch in the main text (even one paragraph) would suffice.
2. **Fix the lower bound.** Either refine Theorem 1 to avoid the potentially negative term, or explicitly discuss the regime where the bound is meaningful and quantify when it becomes vacuous.
3. **Add an adapted baseline.** Implement a simple buffered version of SIC-MMAB (or another MMAB algorithm) that collects observations over a window and runs on the delayed timeline. This single addition would substantially strengthen the experimental contribution.
4. **Compute regret in the real-world experiment.** The spectrum data can be converted to a bandit instance by defining arms as channels, rewards as throughput (or a function of SNR), and delays from the measurement timestamps. Report regret alongside throughput/collisions.
5. **Show regret over time.** Replace or supplement the bar charts with learning curves to demonstrate that DDSE's advantage is not just a final-state artifact.

## Score and Decision

The paper tackles a worthwhile problem and contains a genuinely interesting algorithmic idea. The theoretical framework (both lower and upper bounds) is more complete than what most MMAB papers provide, and the ablation against DDSE without delay estimation is informative. However, the algorithm is not specified at a level that permits reproduction, the lower bound has a mathematical issue that weakens the near-optimality claim, and the experiments fall short of demonstrating that DDSE is superior to simple delay-agnostic adaptations of existing methods. These are significant but not fatal — they are fixable with additional details and experiments. In its current form, the paper does not meet the bar for acceptance at a top venue, but it is a solid foundation for a revised submission.

**Score: 5.0** (marginally below acceptance threshold — clear contributions but major presentation and evaluation gaps)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>