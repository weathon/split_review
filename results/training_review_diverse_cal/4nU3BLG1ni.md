Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes DDSE (Decentralized Delayed Successive Elimination), an algorithm for the multi-player multi-armed bandit (MMAB) problem with stochastically delayed feedback. The key design involves a leader who eliminates sub-optimal arms and periodic communication phases where the leader and followers synchronize on a common set of best empirical arms using a delayed index $\mathcal{M}_{p-q}$ to avoid collisions from delay-induced desynchronization. The paper provides regret bounds (Theorems 1–3), a centralized lower bound (Theorem 1), and experimental validation on both synthetic data and real-world spectrum measurements.

## Strengths

1. **Novel problem formulation — first algorithm for decentralized MMAB with delayed feedback.** The paper correctly identifies that existing decentralized MMAB algorithms rely on immediate collision feedback for coordination and break down under delay. DDSE's high-level idea of using fixed-interval communication phases with a deliberately delayed index $\mathcal{M}_{p-q}$ to maintain consistency across players is a principled attack on this underexplored setting.

2. **Algorithm design avoids exponential regret from miscoordination.** Theorem 3 shows that a naive version (DDSE without delay estimation, which uses the latest available $\mathcal{M}_{p'}$) incurs an exponential term $\exp(\mathbb{E}[d]/KM + \sigma_d^2/(2K^2M^2))$ due to followers receiving incorrect information during communication. By deliberately waiting for a phase that all can agree on ($\mathcal{M}_{p-q}$), DDSE eliminates this term entirely (Theorem 2). This contrast cleanly demonstrates why the waiting mechanism is essential.

3. **Comprehensive experimental validation.** The paper compares against seven baselines (SIC-MMAB, Selfish, MCTopM, RandomTopM, Game of Throne, ESER, and its own ablation DDSE without delay estimation) across varying delay expectations and numbers of players, plus a real-world spectrum dataset with throughput/collision analysis. The results consistently show DDSE outperforming alternatives.

4. **Provides a centralized lower bound for delayed MMAB.** Theorem 1 derives a regret lower bound for the centralized setting with delay, serving as a benchmark. The leading term of DDSE's regret bound ($\sum_{k>M} \frac{323\log T}{\theta\Delta_k}$) matches this benchmark up to constant factors, with additional $T$-independent terms accounting for decentralization costs.

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm specification is incomplete in the main text.** Critical details needed to understand or reproduce DDSE are missing or ambiguous:
   - **Elimination criterion:** The paper describes a "successive elimination" process where the leader gradually removes sub-optimal arms (Section 3, line 33), but never states the rule for *which* arms to add to or remove from $\mathcal{M}_p^j$. The phrase "identifies $a_p^- \in \mathcal{M}_p^M$" (line 135) assumes a procedure that is never given.
   - **Stopping condition:** Part 3 of the communication phase refers to the condition "$|\kappa| = M$" (line 140) indicating all sub-optimal arms have been eliminated. The variable $\kappa$ is never defined.
   - **Definition of $q$:** The index $q$ (which past communication phase's set is used) is central to how the algorithm handles delay. The text defines $p'$ as "the most recent to have been completely received" (line 146) but never explains how any player knows which communication phase has been *completely received by all followers* — a non-trivial coordination problem when feedback itself is delayed. The subsequent discussion mentions $q=0$ for small delays and uses $q_M$ and $q_j$ elsewhere without formal definition (lines 146, 188, 216).
   
   These gaps go beyond "presentation polish" — they make it impossible to fully assess the algorithm's correctness from the main text. While "Algorithm 1" is referenced (line 127), likely in a stripped appendix, the main text should contain enough algorithmic detail for a reader to understand the mechanics. Currently it does not.

2. **Disconnect between algorithm description and analysis regarding delay estimation.** The paper states that $\mathbb{E}[d]$ and $\sigma_d$ can be unknown (line 57: "we allow $\mathbb{E}[d]$ and $\sigma_d$ to be unknown"), and contrasts the main DDSE with a "DDSE without delay estimation" version (Section 4.3), implying the main algorithm *does* estimate delay. The contribution section says players coordinate "based on the estimation of delay" (line 33). However, Section 3 (Algorithm) never describes:
   - How players estimate $\mathbb{E}[d]$ or $\sigma_d$
   - How these estimates determine the value of $q$
   - How the algorithm can operate without knowing the delay distribution a priori
   
   The regret bounds in Theorems 2 and 3 involve $\mathbb{E}[d]$, $\sigma_d$, and $\theta$, but without explaining how the algorithm actually uses (or does not use) these quantities, the connection between the algorithm's execution and its analysis is unclear. This is a structural gap — the reader cannot tell whether the algorithm assumes knowledge it claims not to need.

### Minor

1. **Notation inconsistencies in the bound comparisons.** The text at line 37 contains garbled notation ($\Delta\dot{\tilde{d}}$, $\bar{\tilde{d}}_3$) that appears to be a parser artifact rather than the authors' fault, but the comparison between DDSE and its variants (Table 1, discussed at lines 35–37) is difficult to parse even accounting for parsing issues. The exponential term in Theorem 3's explanatory text (line 214: $\exp(\mathbb{E}[d]/K + \sigma_d^2/2K^2)$) does not match the theorem statement (line 211: $\exp(\mathbb{E}[d]/KM + \sigma_d^2/(2K^2M^2)$) — the factor of $1/M$ differs.

2. **"Real-world simulation" label is slightly misleading.** Section 5.2 uses real spectrum measurement data, but does not state whether the delays themselves are also real or synthetically generated. Since delays are central to the paper's contribution, this should be stated explicitly.

### Trivial
None.

## Nice-to-Haves
- Discuss how $\theta$ (the quantile) should be set in practice, or note that it is a free parameter that can be chosen based on system requirements.
- Provide an explicit definition of $\kappa$ even if briefly.
- Clarify whether the centralized lower bound (Theorem 1) or the known results it builds on could be adapted to a matching decentralized lower bound as future work.

## Removed Points

These points were raised by reviewers but are excluded from the main evaluation as they do not represent genuine weaknesses:

1. **"Centralized lower bound does not constrain the decentralized setting"** — This is factually incorrect. A lower bound on the centralized setting *is* a valid lower bound for the decentralized setting: centralized MMAB is strictly easier (free communication), so any algorithm feasible in the decentralized setting is also feasible (though suboptimal) in the centralized setting. Therefore $R_C^* \le R_D^*$, and a lower bound $L \le R_C^*$ implies $L \le R_D^*$. The paper's comparison of its decentralized upper bound against a centralized lower bound is standard practice in the MMAB literature (Boursier & Perchet, 2019; Wang et al., 2020 among others) and is methodologically sound. The paper is also transparent about what it is doing (line 157: "compare our results with the centralized lower bound to evaluate how the additional information exchange impacts regret reduction").

2. **"The exponential term $\exp(\mathbb{E}[d]/KM + \sigma_d^2/(2K^2M^2))$ is enormous"** — The reviewer's own example ($\mathbb{E}[d]=200, K=20, M=10$) evaluates to $\exp(1) \approx 2.7$, which is negligible. The claim that it "blows up" for "larger" parameters is unsupported without specifying what realistic parameters cause this. This term is presented in Theorem 3 precisely to show DDSE *avoids* it, which is a strength, not a weakness.

3. **Undefined notation $\Delta\dot{\tilde{d}}$ and $\bar{\tilde{d}}_3$** — These are parser artifacts (the PDF-to-text extraction garbled the LaTeX). The notation $\tilde{d}_1, \tilde{d}_2, \tilde{d}_3$ is properly defined in the Table 1 caption (line 18). This is not an author error.

4. **Missing algorithm pseudocode / appendix content** — The paper references "Algorithm 1" (line 127), which likely exists in the appendix (stripped by the parser). The main-text description missing details is a genuine weakness (see Major weakness #1), but the *absence of the appendix in the extracted text* is not a valid criticism.

## Novel Insights

Beyond the paper's own contributions, the contrast between Theorem 2 and Theorem 3 yields an insight that may be more general: in decentralized systems with delayed feedback, the choice of *how far back* to synchronize involves a fundamental trade-off. Using too recent a set risks inconsistency and exponential regret; using too old a set wastes exploration. DDSE's approach of synchronizing on a set delayed by an amount tied to delay distribution estimates is a concrete instantiation of this trade-off that could inform other decentralized coordination problems beyond bandits.

## Suggestions

1. **Provide complete pseudocode and definitions in the main text.** Specifically: (a) the elimination rule for which arms enter/leave $\mathcal{M}_p^j$, (b) the formal definition of $\kappa$ and the stopping condition, and (c) a precise definition of how $q$ is determined from delay estimates (or a statement that $q$ is set to a worst-case upper bound). This is the single highest-impact improvement.

2. **Bridge the gap between algorithm and analysis regarding delay estimation.** Either explain clearly how the algorithm estimates $\mathbb{E}[d]$, $\sigma_d$, and determines $q$ from these estimates, or clarify that the algorithm is parameter-free and the $\mathbb{E}[d]/\sigma_d$ terms in the bounds are purely analytic quantities that appear in the *analysis* but are not needed by the *algorithm*. Currently the text implies the former but describes the latter.

3. **Fix the minor inconsistency** between the exponential term in Theorem 3 (which has $1/KM$) and its explanatory text (which has $1/K$).

## Score and Decision

The paper addresses a genuinely novel and well-motivated problem. The high-level algorithm design (periodic communication with $\mathcal{M}_{p-q}$ synchronization) is sensible, the theoretical bounds are non-trivial, and the experiments are comprehensive. However, the algorithm description in the main text has significant gaps that prevent a reader from fully understanding or assessing the proposed method. The disconnect between the algorithm description and the delay-estimation narrative in the analysis further weakens the presentation. These are structural issues that cannot be resolved through minor clarifications alone — they require a substantially more complete specification of DDSE in the main text. I encourage the authors to resubmit with a fully specified algorithm and a clearer exposition of how delay estimates are used (or why they are not needed).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>