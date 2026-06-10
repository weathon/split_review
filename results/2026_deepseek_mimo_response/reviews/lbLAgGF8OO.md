Now I have all the information I need. Let me write the final consolidated review.

## Summary
This paper introduces Dig-DEC (dual information gain decision-estimation coefficient), a new model-free complexity measure for decision making with structured observations that replaces the optimism mechanism of prior work with pure information-gain-based exploration. Combined with improved online function estimation procedures (unbiased sample-splitting for average error and a refined two-timescale procedure for squared error), the framework yields improved regret bounds in stochastic MDPs and establishes the first model-free regret bounds for hybrid MDPs with bandit feedback under linear reward assumptions.

## Strengths
- **Provably dominant complexity measure with concrete separation (Theorems 13–14):** Theorem 13 formally proves `dig-dec ≤ o-dec + η`, establishing that Dig-DEC is never worse than optimistic DEC of [FGQ+23]. Crucially, Theorem 14 constructs a concrete 3-armed bandit instance where Dig-DEC achieves O(1) regret while the optimistic E2D of [FGQ+23] suffers Ω(√T)—an arbitrarily large gap as T grows. This demonstrates that the removal of optimism is not merely a stylistic change but yields qualitatively better performance, driven by the information-gain KL term that captures distributional differences that mean-based divergences miss (Section 6).

- **First model-free bandit-feedback regret for hybrid MDPs (Table 2):** The paper establishes the first sublinear regret results for model-free learning in hybrid bilinear classes and coverable MDPs with linear reward under bandit feedback, resolving the open problem left by [LWZ25] which could only handle full-information feedback. The key technical enabler is that Dig-DEC's information-gain approach avoids the explicit reward estimator required by optimistic updates, making it compatible with bandit feedback (Section 6, paragraph after Theorem 13).

- **Dramatically improved squared estimation error (Theorem 11):** Under Bellman completeness, the two-timescale POSTERIORITYUPDATE procedure bounds Est ≲ log²|Φ|, which is independent of T—improving over [FGQ+23]'s T^{1/2} bound. Combined with Dig-DEC bounds, this yields the first DEC-based √T regret in Bellman-complete MDPs (Table 1, rows with completeness ✓), matching optimism-based approaches [JLM21, XFB+23] that previously held an advantage over DEC-based methods.

- **Improved unbiased estimator for average estimation error (Section 4.2.1, Theorem 7):** The sample-splitting estimator L_h(φ) achieves Est ≲ N log(|Φ|) T^{1/2}, improving over [FGQ+23]'s biased squared-average estimator. This translates to improved regret rates in the stochastic setting (Table 1).

- **General divergence framework unifying prior AIR analyses:** The generalization to arbitrary convex divergence D (Eq. 2) is a meaningful extension of the Algorithmic Information Ratio framework. The analysis "nicely connects to the standard analysis of mirror descent" (Section 4), replacing the "constructive minimax theorem" of [XZ23] that was restricted to strictly convex divergences. This flexibility is concretely demonstrated by recovering [LWZ25]'s model-based hybrid results with a simpler single-level algorithm where Est does not scale with log|Φ| (Section 4, last paragraph).

- **Transparent structural decomposition (Section 6):** The paper identifies two distinct roles of the extra KL term in Dig-DEC: (i) KL(ν_φ, ρ) for regularization (replacing optimism) and (ii) the conditional KL for information gain (enabling strict improvements over optimistic DEC). This decomposition provides clear conceptual insight into the relationship between Dig-DEC, optimistic DEC, and model-based DEC, valuable for future algorithm design.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Assumption 4 (known linear reward features) limits hybrid setting scope.** The hybrid results (Table 2) require known reward features, which the authors acknowledge as a limitation (lines 115–119). The authors note that Assumption 3 does not capture all learnable hybrid MDPs (e.g., low-rank with unknown features, where log|Φ| would scale polynomially), and the comparison with [LMWZ24] shows this is a real gap. While this is necessary given the current framework and is honestly discussed, relaxing it would substantially broaden the paper's impact. The authors correctly leave this as future work.

### Trivial
None (parser-corrupted exponents removed as formatting artifacts).

## Nice-to-Haves
- A brief remark on the computational tractability of the minimax problem (Eq. 3) in Algorithm 1 for the specific settings in Tables 1–2 would strengthen the paper, even if only to note it is implementable or to characterize the computational cost.
- A compact side-by-side comparison table in the main text (rather than only in Appendix A) showing prior rates vs. new rates for at least the stochastic bilinear class case would make the improvement concrete without requiring readers to consult the appendix.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Exponent inconsistencies between abstract and tables:** The Harsh Critic flagged that the abstract's T^{3/5}/T^{7/8} rates differ from Table 1's T^{2/3} entries, and Table 2 shows T^{3/2} (superlinear) for most hybrid entries. These are confirmed as LaTeX fraction parsing artifacts (e.g., T^{3/2} is almost certainly T^{3/5} in the original), not actual inconsistencies in the paper. Per the hard rule on formatting artifacts, this is removed. The line 213 "from √T to T^{1/2}" is similarly a parser error.
- **Missing comparison table, missing computational discussion, clarification of "model-free":** These were identified by the Harsh Critic but are addressed in Nice-to-Haves or already handled in the paper (line 37 clarifies "model-free"). Not counted as weaknesses.

## Novel Insights
The paper's most novel insight is that removing optimism from the DEC framework and replacing it with pure information gain not only matches but can strictly improve upon optimistic DEC in the stochastic setting, while simultaneously enabling the framework to handle adversarial rewards in hybrid MDPs—a setting where optimism fundamentally breaks down due to the need for explicit reward estimation. The concrete O(1) vs. Ω(√T) separation in Theorem 14 demonstrates this is not a minor improvement but a qualitative one. The decomposition of the KL term into regularization and information-gain components (Section 6) provides a clean conceptual explanation that connects to the broader model-based DEC framework and could guide future algorithm design in this area.

## Suggestions
- Ensure the abstract's rate claims (T^{3/5}, T^{7/8}) are consistent with all table entries in the camera-ready version, and that all fraction exponents are correctly rendered.
- Add a brief worked example or tighter comparison statement in Section 4.2.1 clarifying the exact magnitude of the Est improvement for the average case, to sharpen the presentation of this central technical contribution.
- Consider adding a brief remark on computational considerations for the minimax problem (Eq. 3) in the concrete settings of Tables 1–2.

---

**Calibration Report:**

**All retrieved anchors:**

| Round | Paper | Avg Score | Path |
|-------|-------|-----------|------|
| 1 | Improved Sample Complexity for Actor-Critic | 3.00 | A1WwYw5u8m |
| 1 | Curiosity is the Path to Optimization | 3.00 | L143pPpIHv |
| 1 | Variable Forward Regularization | 2.00 | lFzUHGebeb |
| 1 | Regret measure continuous time bandit | 2.33 | 4jzjexvjI7 |
| 1 | MaxInfoRL | 6.75 | R4q3cY3kQf |
| 1 | RL as Information-State Policies | 5.25 | ByW9j60mvV |
| 1 | Minimax Optimal RL with Quasi-Optimism (EQO) | 7.00 | i8LCUpKvAz |
| 1 | On Bits and Bandits | 6.50 | 0oWGVvC6oq |
| 1 | Learning to Relax (solver parameters) | 8.00 | 5t57omGVMw |
| 1 | Policy Gradient for Confounded POMDPs | 8.00 | 8BAkNCqpGW |
| 1 | Hidden Cost of Waiting for Accurate Predictions | 8.00 | A3YUPeJTNR |
| 1 | Tractable Multi-Agent RL via Behavioral Economics | 8.00 | stUKwWBuBm |
| 2 | Decoupled Actor-Critic | 5.75 | op19LjpHkH |
| 2 | Extensive Analysis on Deep RL Algorithm Design | 5.25 | R6klub5OXr |
| 2 | VBMLE for Model-based RL | 4.25 | 2h3m61LFWL |
| 2 | Double Descent in RL with LSTD | 5.25 | 9RIbNmx984 |
| 2 | Model-based RL Minimalist Approach | 7.00 | txD9llAYn9 |
| 2 | Sample-Efficiency Multi-Batch RL | 6.33 | ey3GhWXQ97 |
| 2 | Offline RL in Regular Decision Processes | 7.00 | EW6bNEqalF |
| 2 | Demonstration-Regularized RL | 6.50 | lF2aip4Scn |
| 2 | Optimal Sample Complexity Average Reward MDPs | 6.50 | jOm5p3q7c7 |
| 2 | Horizon-free Adversarial Linear Mixture MDPs | 6.00 | aPNwsJgnZJ |
| 2 | Optimal Strong Regret Constrained MDPs | 6.00 | 8eNLKk5by4 |
| 2 | Learning Mirror Maps in PMD | 6.67 | n4wcdct43X |
| 2 | Offline Data Enhanced On-Policy PG | 7.00 | RMgqvQGTwH |
| 2 | Making RL with Preference Feedback Efficient | 6.25 | Pe2lo3QOvo |
| 2 | Beyond Worst-case Attacks Robust RL | 7.00 | DFTHW0MyiW |
| 2 | Stochastic Bandits Robust to Adversarial Attacks | 6.50 | vOFx8HDcvF |

**Round-1 bracket:** 6.5–8.0. The paper is clearly above the weak anchors (2.0–3.0), well above the mid-band RL theory rejects (4.25–5.75), and comparable to the stronger accepted theory papers (6.5–7.0). The top-band anchors (8.0) are in different domains and not directly comparable.

**Round-2 narrowing:** 6.5–7.5. The paper is clearly stronger than Horizon-free Adversarial MDPs (6.0) and the constrained MDP paper (6.0), comparable to Bits and Bandits (6.5) and Demonstration-Regularized RL (6.5), and comparable to or slightly above EQO (7.0) and Model-based RL Minimalist (7.0). The paper's novelty (new complexity measure with provable separation, first hybrid MDP results) is at least as strong as these 7.0 anchors.

**Final score justification:** The paper scores 7.0, positioned alongside the strongest RL theory anchors. Its contribution is genuinely novel (Dig-DEC is a new complexity measure, not just an algorithmic tweak), the Theorem 14 separation is compelling, and the first hybrid MDP results with bandit feedback resolve a concrete open problem. The only weakness of note is Assumption 4 (acknowledged), which is a scope limitation rather than a flaw. The parser-corrupted exponents are removed as they are not author errors.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>