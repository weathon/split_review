Now I have a comprehensive understanding of both the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper studies decentralized multi-player multi-armed bandits (MMAB) with stochastic delayed feedback—a practical but underexplored problem in cognitive radio networks. It proposes DDSE (Decentralized Delayed Successive Elimination), which uses a leader-follower structure where players coordinate using deliberately outdated consensus arm sets ($\mathcal{M}_{p-q}$) to avoid collisions under delay. The paper provides a centralized lower bound (Theorem 1), a regret upper bound for DDSE (Theorem 2), a comparison bound for a naive variant without delay estimation (Theorem 3), and experiments on synthetic and real-world spectrum data.

## Strengths

1. **First algorithm for a well-motivated underexplored problem.** Decentralized MMAB with stochastic delayed feedback is a realistic problem in cognitive radio networks that prior work on MMAB (Boursier & Perchet, 2019; Wang et al., 2020; Xiong & Li, 2023) has not addressed. The paper identifies this gap clearly.

2. **Clever algorithmic idea with theoretical payoff.** The central insight—using deliberately outdated consensus sets ($\mathcal{M}_{p-q}$) rather than the latest information to maintain synchronization under delay—is conceptually sound. Theorem 2 shows this avoids an exponential regret term that appears in the naive version (Theorem 3), and the ablation against "DDSE without delay estimation" experimentally confirms the value of this design choice.

3. **Regret decomposition and near-optimal guarantee.** The paper provides a lower bound (Theorem 1) for centralized MMAB with delays and an upper bound (Theorem 2) that matches it up to $T$-independent additive terms. The decomposition into exploration regret (Lemma 1) and communication regret (Lemma 2) cleanly separates the sources of regret, and the communication regret is shown to be constant in $T$.

4. **Realistic delay model.** The paper adopts a sub-Gaussian delay assumption (Assumption 1) rather than a hard bound $d_{\max}$, permitting rare large delays. This is more practical than assumptions in prior single-player delayed bandit work and is justified by references to real network characteristics.

5. **Empirical validation on real-world data.** Beyond synthetic simulations, the paper evaluates DDSE on spectrum measurement data from the 5G-Xcast project, measuring cumulative throughput and collisions (Figures 3–5). This grounds the theoretical claims in a concrete application domain.

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm description is unclear in critical aspects, making the main contribution hard to evaluate from the text alone.** While Algorithm 1 (referenced in the paper) likely contains the pseudocode, the textual description in Section 3 leaves several key mechanics underspecified:
   - **How $q$ (the number of communication phases to step back) is determined from delay estimates.** The paper mentions $\hat{\mu}_d^j$ and $(\hat{\sigma}_d^2)^j$ (line 146) but never describes how these are computed online or how they translate into a specific $q$ such that $\mathcal{M}_{p-q}$ is the "safe" consensus set. This is the core adaptation mechanism that distinguishes DDSE.
   - **The exploration phase procedure.** The paper states the leader "explores all arms and gradually eliminates sub-optimal arms" (line 33) but provides no elimination rule, confidence bound, or stopping condition. Readers familiar with successive elimination can guess the structure, but the paper should be self-contained.
   - **The communication phase protocol is confusing.** The description of Part 1 (Remove Arm, line 136) is particularly hard to parse: the leader identifies $a_p^-$ in the current set $\mathcal{M}_p^M$ but then selects the arm at the same position from the *older* set $\mathcal{M}_{p-q}^M$. The mechanism is explained in only a few dense sentences, and the reasoning for why this ensures synchronization under delay is not made intuitive. A worked example (e.g., $K=3, M=2$) would substantially clarify the protocol.

   This is the paper's primary contribution, and the description should enable a reader to understand, if not fully re-implement, the algorithm from the main text. In its current form, it does not.

### Minor

2. **The lower bound (Theorem 1) contains a term $\mathbb{E}[d] - \sigma_d\sqrt{\theta/(1-\theta)}$ that can become negative for large $\sigma_d$, making the bound potentially vacuous or even reversed in sign.** The paper does not discuss the regime in which this bound is meaningful or what values of $\theta$ and $\sigma_d$ keep it non-trivial. This does not invalidate the bound, but the lack of discussion weakens the reader's confidence in the near-optimality comparison.

3. **The near-optimality claim is overstated relative to the evidence presented.** The gap between Theorem 1 (centralized lower bound) and Theorem 2 (decentralized upper bound) involves a constant factor of roughly 646 in the leading $\frac{\log T}{\theta\Delta_k}$ term and a structural gap in the delay-dependent terms when $K-M$ is small (e.g., $M = K-1$). The paper states the result is "near-optimal" (lines 37, 165, 178) but does not discuss these gaps or the regime where the constant factor is acceptable. A more nuanced discussion would strengthen the claim.

4. **Experiments compare only against baselines designed for immediate feedback, with no delay-adapted variants.** The paper acknowledges these baselines "are ill-suited" to delay (line 24), making the comparison somewhat self-fulfilling. While the inclusion of "DDSE without delay estimation" as an ablation partially addresses this, adding at least one simple delay-robust adaptation of a baseline (e.g., a variant that discards stale observations or uses a timeout) would make the empirical case for DDSE significantly stronger.

5. **No discussion of limitations.** The conclusion (Section 6) does not mention the paper's known assumptions: the need for pre-assigned player ranks and known $M$, the requirement $M \leq K$, the sub-Gaussian delay model, and that $M$ is fixed over time. These are reasonable for a first work, but acknowledging them improves scholarly completeness.

### Trivial
None.

## Nice-to-Haves
- A small worked example (e.g., $K=3, M=2$) illustrating the communication protocol step-by-step would dramatically improve clarity.
- A proof sketch for the lower bound (Theorem 1) or the key steps in Lemma 1 would help readers assess the theoretical contribution without needing to consult the appendix.
- Discussion of whether the algorithm can handle unknown or time-varying $M$.

## Removed Points

The following points from the reviewer inputs have been removed with justification:

- **"No intuition given for exponential term in Theorem 3"** — The paper provides intuition at lines 214–215: followers receive incorrect information when $\mathcal{M}_{p'}^j \neq \mathcal{M}_{p'}^M$, leading to exponential regret. The critic's claim that "no intuition is given" is factually inaccurate.
- **"Missing proof sketches in main text"** — Proofs are standardly deferred to the appendix in this venue's format. The parser strips those sections; they exist in the original submission.
- **"Algorithm cannot be evaluated independently"** — The paper references Algorithm 1 (the pseudocode) which was stripped by the parser. Some implementation details are legitimately in the pseudocode. However, the textual clarity criticism remains valid (kept in Major #1).
- **Strength Finder's generic framing** — The identified strengths are factually correct and supported by the paper, so they are retained with appropriate qualification rather than removed.
- **"Quantile function is defined but never used"** — The quantile function $d(\theta)$ is defined and its parameter $\theta$ appears in all the regret bounds (Theorems 1–3, Lemmas 1–2). The function itself is not invoked in the bounds, but the definition is contextually relevant.

## Novel Insights

The key insight that emerges from reading the paper against the reviews is a tension: the paper's central algorithmic idea (using $\mathcal{M}_{p-q}$ to maintain synchronization) is genuinely clever and the theoretical bounds credibly show it avoids exponential regret, yet the presentation is too terse to make this idea accessible. The reviewers' most productive observation is that the paper needs a clear, step-by-step exposition of how $q$ is chosen and how the communication phase encodes the arm update via position-based collision signaling. The real-world spectrum experiments are a strength that the reviews underweight relative to the synthetic experiments.

## Suggestions

1. **Rewrite Section 3 (Algorithm) with a worked example.** Show a concrete run for $K=3, M=2$ across a few communication phases, illustrating how the leader and followers use $\mathcal{M}_{p-q}$ to stay synchronized, how $q$ is inferred from delay estimates, and what happens in the communication phase (remove/add/notify). This would resolve the primary clarity concern.

2. **Add at least one delay-adapted baseline to the experiments.** A simple approach: have each baseline player run a standard delayed UCB for single-player bandits (discarding feedback that arrives before their next action) and ignore collisions, or apply a timeout-based communication protocol to SIC-MMAB. This would make the "ill-suited" claim empirically grounded rather than self-fulfilling.

3. **Discuss the regime of the lower bound.** Add a sentence explaining when $\mathbb{E}[d] - \sigma_d\sqrt{\theta/(1-\theta)}$ is positive and what this implies for the bound's utility.

4. **Add a limitations paragraph to the conclusion.** Acknowledge the need for known $M$, pre-assigned player ranks, $M \leq K$, fixed $M$, and sub-Gaussian delays.

5. **Soft-pedal the "near-optimal" claim** or add a discussion of the constant-factor gap and the centralized-vs-decentralized structural gap, especially for extreme values of $K-M$.

## Score and Decision

The paper addresses a genuine gap, proposes a reasonable algorithm with theoretical backing, and provides empirical evidence. However, the unclear algorithm description in the main text is a significant weakness for a method paper, and the near-optimality claim needs more careful qualification. The core contribution is real but the presentation substantially hinders evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>