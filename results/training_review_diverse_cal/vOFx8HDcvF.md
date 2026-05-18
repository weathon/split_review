Now I have all the information needed. Let me compose the authoritative consolidated review.

## Summary

This paper provides a comprehensive study of stochastic multi-armed bandit algorithms robust to adversarial attacks, where the attacker observes the learner's action before altering the reward. It studies two cases (known or unknown attack budget $C$) and two types of regret bounds (additive or multiplicative $C$ dependence). The paper proposes matching upper and lower bounds for all four combinations, establishes $\Theta(KC)$ regret due to attacks vs. $\Theta(C')$ for corruption — revealing a factor-$K$ separation — and develops novel algorithmic techniques (multi-phase elimination and model selection) for the unknown-budget setting.

## Strengths

- **Tight lower bounds matching upper bounds**: Theorem 1 establishes a general $\Omega(KC)$ lower bound for any algorithm under attack. Combined with classic MAB lower bounds, Proposition 1 gives $\Omega(\sum \log T/\Delta_k + KC)$ gap-dependent and $\Omega(\sqrt{KT}+KC)$ gap-independent bounds. The SEWR algorithm's $O(\sum \log T/\Delta_k + KC)$ bound (Theorem 2) and SEWRST's $O(\sqrt{KT\log T}+KC)$ bound (Theorem 3) match these, demonstrating near-optimality.

- **Sharp improvement over prior corruption analysis**: The paper shows SEWR's regret bound removes the multiplicative $1/\Delta_k$ dependence on $C$ present in Lykouris et al. (2018) — reducing the corruption term from $\sum_{k\neq k^*} C/\Delta_k$ to $KC$. This improvement is crucial for achieving tight multiplicative bounds for both known and unknown attack budgets.

- **Establishes a fundamental separation between attack and corruption models**: The paper demonstrates that attack incurs $\Theta(KC)$ regret versus $\Theta(C')$ for corruption — a factor of $K$ worse. For unknown budgets, it proves impossibility of $O(\text{poly}\log T + C^\alpha)$ for any $\alpha>0$ under attack (Theorem 4), while corruption allows such forms. This conceptual contribution is clearly articulated.

- **Novel algorithmic techniques for unknown attack**: The multi-phase elimination (PEWR) and model-selection (MSSEWR) algorithms are non-trivial extensions that handle unknown attack budgets without relying on randomization (which fails under attack). PEWR's $\tilde{O}(\sqrt{KT}+KC^2)$ bound and MSSEWR's multiplicative bounds are shown to be tighter than reductions from linear bandit results.

- **Comprehensive taxonomy of regret bounds**: Table 1 systematically presents four combinations with both upper and lower bounds, covering gap-dependent and gap-independent forms, giving a clear picture of when each algorithm is preferable.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Model selection analysis needs more explicit justification**: When applying Lemma 1 (model selection) to MSSEWR, the paper states the SEWRST regret bound as $\bar R_T \le O(\sqrt{KTC\log(KT/\delta)})$ in terms of the *true* $C$, but each base instance is defined with an *input* budget $\CInput = 2^g$. The step connecting the two — noting that when $C \le \CInput$ the bound becomes $O(\sqrt{KT\,\CInput\,\log(KT/\delta)})$ and that CORRAL/EXP3.P handles instances where $C > \CInput$ — is implicit rather than stated. Making this reasoning explicit would strengthen the paper.

### Trivial
- **Experiments section appears empty**: The section titled "Experiments" contains no content. While the paper is primarily theoretical and does not require experiments, an empty section heading is a presentation issue. The authors should either populate it (e.g., with a brief note that experiments are deferred to future work) or remove the section heading.

## Nice-to-Haves
- A short proof sketch or attack construction for Theorem 1 (e.g., "the adversary attacks each arm in round-robin fashion, forcing its observed reward to 0 until elimination, costing $O(C)$ per arm") would increase reader confidence, though the full proof is presumably in the appendix.
- The figure captions (especially Figure 2) could be slightly more self-contained, though the current cross-reference to Remark 9 is adequate.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Attacked reward boundedness concern"** — The critic claimed the analysis requires attacked rewards to be bounded in $[0,1]$. This is **factually incorrect**. The confidence radius $\sqrt{\log(2/\delta)/N_k} + C/N_k$ works for *any* attacked reward values: the empirical mean decomposes into $(1/N_k)\sum X_t$ (concentrates by Hoeffding since raw rewards $X_t\in[0,1]$) plus $(1/N_k)\sum (\tilde X_t - X_t)$ (bounded by $C/N_k$ by definition of $C$). No boundedness of $\tilde X_t$ is needed. Removed.

2. **"Lower bound Theorem 1 without proof sketch"** — The paper states Theorem 1 as a restatable theorem. Proofs in theory papers are standardly deferred to an appendix, which the parser strips. Removed per parser-stripping rule.

3. **"Missing pseudocode for SEWRST"** — SEWRST is referenced as Algorithm~\ref{alg:se-wcr-stop} with stopping conditions described mathematically in the text. Full pseudocode would have been in the appendix, which is stripped by the parser. Removed.

4. **"PEWR analysis cannot be verified without proof"** — This concern amounts to "the proof is not in the main paper body." Proofs are in the appendix. Removed per parser-stripping rule.

5. **"Figure 2 caption insufficient"** — The caption already cross-references Remark 9. This is a minor presentation preference, not a weakness. Moved from weaknesses.

6. **"The improvement over Lykouris et al. could be more explicit"** — The paper already explains this improvement clearly (lines 263-265). This is an observation, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective not already present in the paper.

## Suggestions

1. Add a sentence to explicitly connect the model selection application: "For each base instance with input $\CInput = 2^g$, when $C \le \CInput$, SEWRST's regret is $O(\sqrt{KT\,\CInput\,\log(KT/\delta)})$; when $C > \CInput$, the instance may suffer linear regret but CORRAL/EXP3.P will switch away from it."
2. Either populate the Experiments section with a brief statement or remove the heading entirely.
3. Consider adding a 2-3 sentence proof sketch for Theorem 1 in the main text.

## Score and Decision

The paper makes a strong theoretical contribution: it provides the first comprehensive study of robust MAB algorithms under adversarial attacks, with tight upper and lower bounds, novel algorithmic techniques for unknown budgets, and a clear separation from the corruption model. The core claims are well-supported, and the identified weaknesses are minor. The paper is ready for acceptance.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>