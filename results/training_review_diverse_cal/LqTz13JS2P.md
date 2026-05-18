Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies repeated generalized principal-agent problems (encompassing Bayesian persuasion, Stackelberg games, and contract design) where the agent uses learning algorithms rather than best-responding. The core contribution is a unified reduction from repeated interaction with a learning agent to a one-shot problem with an approximately-best-responding agent. The paper proves that against a no-swap-regret learning agent, the principal's utility lies in the asymmetric range \([U^* - \Theta(\sqrt{\mathrm{SReg}(T)/T}),\; U^* + O(\mathrm{SReg}(T)/T)]\), while against a no-regret agent the principal can sometimes exceed \(U^*\) significantly. The framework subsumes and refines prior case-by-case analyses with explicit polynomial rates.

## Strengths

- **Unified reduction framework (Sections 3–4):** The paper provides a general reduction from repeated principal-agent problems with learning agents to one-shot problems with approximate best response. This subsumes earlier separate analyses for Stackelberg games (Deng et al., 2019) and contract design (Guruganesh et al., 2024) and extends to Bayesian persuasion and any generalized principal-agent problem without private information.

- **Tight quantitative bounds (Theorems 3.1–3.2):** The paper proves that against a no-swap-regret agent, the principal cannot exceed \(U^* + O(\mathrm{SReg}(T)/T)\) (Theorem 3.2), while against a no-regret agent the principal can guarantee at least \(U^* - \Theta(\sqrt{\mathrm{Reg}(T)/T})\) (Theorem 3.1). The asymmetry and tightness of the sqrt bound are demonstrated by Example 4.1, which is rigorous.

- **Characterization of when no-swap-regret caps the principal's utility:** The paper shows that the no-swap-regret upper bound holds for all generalized principal-agent problems where the agent has no private information (Section 3, Theorem 3.2), including Bayesian persuasion where the principal is privately informed. This answers a natural question raised by prior work.

- **Quantitative refinements for specific models (Corollaries 5.1–5.3):** The framework yields explicit polynomial bounds (e.g., \(U^* - O(\sqrt{\mathrm{Reg}(T)/T})\) and \(U^* + O(\mathrm{SReg}(T)/T)\)) for Bayesian persuasion, Stackelberg games, and contract design, improving on the earlier \(o(1)\) results. This demonstrates the versatility of the framework.

## Weaknesses

### Major

- **The mean-based example (Theorem 3.4) lacks rigorous proof.** The proof sketch is heuristic: it asserts that the receiver "will take action L with high probability" or "will continue to play action M in most times" without quantifying any probability statements, without specifying how \(\gamma\) relates to these claims, and without a formal argument that the claimed total utility \(\approx T/2 - O(T\sqrt{\gamma})\) follows from the \(\gamma\)-mean-based property. The derivation uses approximations like "\(\approx \frac{T}{4}\sqrt{\gamma}\)" and "roughly \(\frac{T}{4} - \frac{T}{4}\sqrt{\gamma}\) rounds" without bounding the errors. Additionally, Claim 1 within the proof relies on a forward reference to Theorem 5.3 (flagged by the authors themselves). This example is important because it demonstrates that the no-swap-regret upper bound does not extend to all no-regret algorithms, yet its current presentation does not meet the same standard of rigor as the paper's main results. The paper should either provide a proper proof with quantified probability bounds or clearly label the result as a conjecture with an informal argument.

### Minor

- **Assumptions 1 and 2 are not universally "innocuous."** The paper describes them as "innocuous" (line 451), but they restrict the class of problems covered. Assumption 2 (constraint set in interior of \(\mathcal{X}\)) fails, e.g., in Bayesian persuasion with a prior assigning zero probability to some state, causing the bounds to blow up. While the paper checks this assumption in the persuasion application (requiring full-support prior), the general theorems are presented without sufficient emphasis that the results are conditional on these geometric conditions. A brief discussion of how the results change when these assumptions fail would strengthen the paper.

- **Tightness of the linear upper bound \(\delta/\mathrm{gap}\) is not discussed.** The paper shows that the \(\Theta(\sqrt{\delta})\) lower bound for \(\underline{\mathcal{O}BJ}^{\mathcal{R}}(\delta)\) is tight (Example 4.1), but does not discuss whether the linear dependence \(\delta/\mathrm{gap}\) in \(\overline{\mathcal{O}BJ}^{\mathcal{R}}\) is tight. A brief remark would be helpful for completeness.

### Trivial

- The forward reference annotation at line 415 (authors' own comment: "This is a forward reference. Need to fix.") is a minor organizational issue that should be cleaned up in the final version.

## Nice-to-Haves

- The paper could explicitly check Assumptions 1 and 2 for each application (Stackelberg games, contract design, Bayesian persuasion) in a single place to help readers assess the breadth of applicability at a glance.
- A brief remark on whether the linear \(\delta/\mathrm{gap}\) upper bound is tight would be helpful but is not required.
- The claim that mean-based algorithms are no-regret (but not no-swap-regret) could benefit from a brief citation or explanation.

## Removed Points

None of the reviewer criticisms met the removal criteria (all are factually correct and substantive upon verification against the paper). No points removed.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the paper's core contribution — the unified reduction and the asymmetric tight bounds — stands on solid theoretical ground, while identifying one specific gap (the mean-based example proof) that the authors should address. The observation that the asymmetry between \(\sqrt{\delta}\) and \(\delta\) bounds is driven by the principled difference between randomized and deterministic approximate best responses is elegantly explained by the paper itself.

## Suggestions

1. **Rigorously prove (or re-label) the mean-based example.** Provide a formal derivation from the \(\gamma\)-mean-based definition with explicit probability bounds. If a fully rigorous proof is not possible within the page limit, clearly downgrade the claim to a conjecture or provide a more careful sketch with quantified error terms.
2. **Add a brief limitations paragraph** discussing when Assumptions 1 and 2 fail and what happens to the bounds in those cases.
3. **Add a remark on the tightness of the linear upper bound** \(\overline{\mathcal{O}BJ}^{\mathcal{R}}(\delta) \le U^* + O(\delta/\mathrm{gap})\).
4. **Clean up the forward reference** and ensure all citations are properly resolved.

## Score and Decision

The paper makes a genuine theoretical contribution by unifying and sharpening the analysis of principal-agent problems with learning agents. The main results (Theorems 3.1–3.3, the reduction framework, and the approximate-best-response analysis in Section 5) are rigorous, the bounds are tight, and the applications demonstrate the framework's generality. The mean-based example is the only part that falls short of the paper's usual rigor, but this does not undermine the core contributions. With a proper fix of the mean-based analysis, the paper meets the bar for a strong theory venue.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>