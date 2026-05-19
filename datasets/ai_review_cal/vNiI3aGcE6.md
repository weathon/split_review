- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
Now I have a thorough understanding of the paper. Let me cross-check each claim directly against the paper content and produce the consolidated review.

---

## Summary

This paper proposes ME-Nash-QL, a model-free self-play algorithm for two-player zero-sum Markov games (TZMGs). It claims to achieve, simultaneously, minimal space complexity $O(SABH)$, sample complexity $\widetilde{O}(H^4 SAB/\varepsilon^2)$, computational complexity $O(T\,\text{poly}(AB))$, low burn-in cost $\widetilde{O}(SAB\,H^{10})$, and a Markov/Nash output policy — a combination not realized by prior algorithms. The extension Multi-ME-Nash-QL for multi-player general-sum games is also presented.

## Strengths

1. **Optimal memory complexity.** ME-Nash-QL achieves space $O(SABH)$, which is the minimum required to store Q-values in tabular cases. This improves on Nash-VI ($O(S^2ABH)$) and V-learning ($O(S(A+B)T)$). The paper explicitly states this and compares with prior work in Table 1. (Section 1.1, lines 29–30)

2. **Sample complexity matching the best known with lower auxiliary costs.** The algorithm attains $\widetilde{O}(H^4 SAB/\varepsilon^2)$ samples (Theorem 1, line 162), matching model-based Nash-VI while using strictly less memory and computation, and outputting a Markov/Nash policy (which Nash-VI also does, but at higher space cost). (Section 3.2, Theorem 1)

3. **Lowest computational complexity among comparable algorithms.** Per-step computation is $O(T\,\text{poly}(AB))$, avoiding the $O(T\,\text{poly}(SAB))$ cost of model-based methods like Nash-VI. (Section 1.1, line 30; Section 3.2, line 175)

4. **Markov and Nash output policy.** Unlike prior model-free algorithms (e.g., V-learning, which outputs non-Markov or mixture policies), ME-Nash-QL outputs a single Markov and Nash policy. This is stated in Section 1.1 (line 31–33) and confirmed in Table 1.

5. **Extension to multi-player general-sum games.** Theorem 3 (line 171–173) gives sample complexity $\widetilde{O}(H^4 S \prod_i A_i / \varepsilon^2)$ for the multi-player extension, competitive with best V-learning guarantees while preserving memory and computational benefits.

6. **Clear comparative positioning.** Table 1 (described in lines 14–15) and the text systematically compare against nine prior algorithms across five metrics (sample complexity, space, computation, burn-in, Markov/Nash policy), highlighting where ME-Nash-QL is the only method holding the best result across all metrics.

## Weaknesses

### Fatal

None. The paper states its theorems clearly, provides explicit bounds, and describes the algorithm with its key update equations (Eq. 1). The full proofs reside in the appendix (standard for page-limited conference submissions). No verifiable flaw from the paper as written invalidates the core claims.

### Major

- **The paper claims "optimal dependence on $H$ and $S$" (line 31) without discussing known lower bounds for TZMGs.** The paper mentions the MDP lower bound $\Omega(H^2 SAT)$ (line 46) but does not cite or compare against TZMG-specific lower bounds (e.g., $\Omega(H^2 SAB/\varepsilon^2)$). Since the achieved sample complexity has $H^4$ in the numerator, the reader cannot assess whether the $H^4$ dependence is actually tight for the TZMG setting or whether there remains a gap. The claim of optimality requires at least a reference to the relevant lower bound. (Lines 31, 46; Section 3.2)

### Minor

1. **Section 4 (Analysis) is extremely thin in the extracted text.** It contains only ~3 sentences of notation setup with no lemmas, proof decomposition, or discussion of how key challenges (e.g., reference-advantage decomposition interacting with an adversarial opponent, early-settlement mechanism) are addressed. While the full proofs are presumably in the appendix (which was stripped by the parser — the garbled text "3.2." at the start of Section 4 suggests content loss), the main text would benefit from even a brief proof sketch or outline of key lemmas to help the reader assess technical plausibility. (Lines 180–184)

2. **The burn-in cost $\widetilde{O}(SAB\,H^{10})$ has an extremely high polynomial dependence on $H$.** The paper acknowledges this and argues that $S \gg H^3$ makes it better than Nash-VI's $\widetilde{O}(S^3 AB\,H^4)$ (lines 31, 165). However, a factor of $H^{10}$ is very large in absolute terms — far larger than typical horizon lengths in many settings. The paper does not discuss whether this high $H$-dependence could be reduced or whether it creates a practical concern. A brief justification of where the $H^{10}$ arises and whether it is tight would strengthen the presentation.

### Trivial

- The text contains occasional garbled characters and typographical artifacts (e.g., "stochasie simat" on line 134, "thriving" for "thriving" on line 4). However, per the instructions, these are parser-induced artifacts and not author errors.

## Nice-to-Haves

- Include a brief proof sketch (2–3 key lemmas or a decomposition of the regret bound) in the main-text Section 4 to help reviewers and readers assess the technical approach without consulting the appendix.
- Add a brief discussion of known TZMG lower bounds and explicitly state whether the $H^4$ factor is tight relative to those bounds.
- Clarify the derivation or origin of the $H^{10}$ burn-in term and whether it could be improved.

## Removed Points

The following criticisms from the Harsh Critic were removed or heavily downgraded after cross-checking against the paper:

1. **"Algorithm specification is too vague / lacks pseudocode"** — The paper explicitly references "Algorithm 1" and "Algorithm 2" with line-numbered steps (lines 125–126, referencing lines 4–12 and 13–19) and provides the core update equation (Eq. 1, lines 130–132). The original submission almost certainly contained formal pseudocode in algorithm boxes that the parser could not extract. The critic's characterization of the algorithm as "described in prose rather than pseudocode" is a parser artifact, not an author omission. **Removed.**

2. **"Missing proof sketch is a fatal/structural flaw"** — While Section 4 is thin in the extracted text, this is partially a parser artifact (the garbled text "3.2." at the start indicates content loss). The paper states clear theorems with explicit bounds and likely contains proofs in the appendix (which was stripped). Calling this "fatal" for a page-limited conference paper is overly harsh. **Demoted to Minor.**

3. **"Claim about (Feng et al., 2023) is asserted without evidence"** — This is a standard citation practice. The evidence is the cited paper itself. **Removed.**

4. **"Burn-in comparison significance is unclear"** — The paper does compare burn-in costs and gives a concrete condition ($S > H^3$) where ME-Nash-QL's burn-in is better. The comparison is valid as stated. The preserved weakness above (about $H^{10}$ being large in absolute terms) is a refined version. **Removed the original framing.**

5. **Strength Finder's generic strengths about "important problem" and "interesting question"** — These are generic, delusional, or sycophantic and were removed per instructions. Only concrete, evidence-grounded strengths were retained.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight about the paper that the paper itself does not already state.

## Suggestions

1. **Add a brief proof sketch to Section 4.** Even 5–10 lines describing the regret decomposition (e.g., how optimism is maintained, how variance reduction via reference-advantage decomposition interacts with the adversarial opponent, how early settlement reduces burn-in) would substantially increase the paper's credibility and readability without exceeding page limits.
2. **Discuss known lower bounds for TZMGs explicitly.** Cite the relevant lower bound (e.g., from Bai et al. 2020 or similar) and clarify whether the $H^4$ dependence in the sample complexity is tight for this setting or whether a gap remains.
3. **Provide a brief justification for the $H^{10}$ burn-in term.** Explain which component of the analysis yields this exponent and whether it is improvable.
