Now I have a thorough understanding of the paper and can verify claims. Let me construct the final review.

## Summary

This paper develops the first algorithms for Conservative Contextual Bandits (CCBs) with general non-linear cost functions. It proposes C‑SquareCB (squared‑loss reduction) and C‑FastCB (KL‑loss reduction, achieving a first‑order regret bound scaling with $L^*$ rather than $T$), both using Inverse Gap Weighting (IGW) exploration and an online regression oracle. The reduction is instantiated with neural networks and OGD to give end‑to-end $\tilde{\mathcal{O}}(\sqrt{KT} + K/\alpha)$ and $\tilde{\mathcal{O}}(\sqrt{KL^*} + K(1+1/\alpha))$ regret bounds. Experiments on OpenML datasets show the methods outperform Conservative Linear UCB while maintaining the safety constraint.

## Strengths

1. **First CCB algorithms for general non‑linear function classes.** The paper extends the safety constraint (Definition 2) from the multi‑armed and linear settings (prior UCB‑based work) to arbitrary function classes via an IGW‑oracle reduction. The abstract and introduction are explicit: "we consider CCBs beyond the linear case." This is a principled generalization that prior work did not address.

2. **First‑order regret bound scaling with $L^*$.** C‑FastCB (Section 4) guarantees $\widetilde{\mathcal{O}}(\sqrt{KL^*} + K(1+1/\alpha))$ regret (Theorem 4.1), a data‑dependent bound scaling with the cumulative optimal loss rather than horizon $T$. No prior conservative bandit algorithm achieved this.

3. **Novel analysis for the safety constraint without confidence sets.** The paper introduces a safety condition (Equation 4) relating oracle predictions to cumulative baseline cost via a compensation term from regression regret. The analysis bounding $n_T$ (number of baseline plays) by relating it to $\regsq(T)$ / $\regkl(T)$ (Lemma 3.2, Lemma 3.3) is a new technique compared to the linear‑case analysis that relied on ellipsoidal confidence bounds (see Remark after Theorem 3.1). This enables safe exploration for general function classes.

4. **End‑to‑end regret bounds for neural network instantiation.** The paper instantiates the oracle with OGD on perturbed neural networks (Section 5) and provides concrete bounds: $\widetilde{\mathcal{O}}(\sqrt{KT}+K/\alpha)$ for C‑SquareCB (Theorem 5.1) and $\widetilde{\mathcal{O}}(\sqrt{KL^*}+K\log T+K/\alpha)$ for C‑FastCB (Theorem 5.2), demonstrating practical viability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Inconsistent notation in the safety condition of C‑FastCB (Algorithm 2).** The safety condition in C‑SquareCB (Algorithm 1, line 7 / eq. safety‑condition) is:
   $$16\sqrt{m_{t-1}\big(\regsq(m_{t-1}) + \log(4/\delta)\big)}$$
   while the safety condition in C‑FastCB (Algorithm 2, line 4) is:
   $$16\sqrt{m_{t-1}\; \regkl(T)}$$
   Two issues arise: (i) C‑FastCB uses the horizon‑$T$ bound $\regkl(T)$ where C‑SquareCB uses the tighter $\regsq(m_{t-1})$ — if $\regkl$ is monotonic this is conservative but notationally inconsistent; (ii) C‑FastCB's condition omits the $\log(1/\delta)$ term that appears in C‑SquareCB, which is needed to account for probabilistic deviations. The proof of Theorem 4.1 is deferred to the appendix (the main text's proof block is empty), so the reader cannot verify whether this omission is intentional or a typo. This needs clarification.

2. **Limited experimental baselines for regret.** The regret comparison (Figure 3 / Fig. 1) only compares C‑SquareCB and C‑FastCB against Conservative Linear UCB. Because the datasets are non‑linear and the proposed methods use neural networks, outperforming a linear method is unsurprising. The paper would more convincingly demonstrate the safety‑regret trade‑off by also comparing:
   - The non‑conservative versions of the same algorithms (SquareCB and FastCB without the safety filter), to show the regret cost of enforcing safety.
   - A neural‑features version of C‑LinUCB, to isolate the benefit of IGW‑based exploration over UCB.
   
   The constraint‑violation comparison with vanilla versions (Figure 4) is useful but does not directly address regret competitiveness.

3. **KL‑loss neural regression bound citation gap.** Theorem 5.2 claims $\regkl(T) = O(\log T)$ for neural OGD with KL loss, citing Deb et al. (2024), which primarily focuses on squared loss. The paper does not clarify whether the KL‑loss result follows directly from the same analysis or requires a separate argument. Since the sigmoid‑ensemble predictor (eq. ftildeS_kl) differs from the squared‑loss predictor, a brief justification (or an explicit lemma stating the KL‑loss bound and its conditions) would improve trust in the result without requiring the reader to consult the cited work.

### Trivial
- **No error bars or variance bands on regret plots** (Figure 3). For 10 runs, shading or error bars would help assess variability.
- **The episodic gamma schedule in C‑FastCB is referenced as `\eqref{eq:gamma-schedule}` but the equation is not present in the main text** (presumably in the appendix). A brief formula or description in the main text would improve readability.

## Nice-to-Haves

- A comparison of the constraint‑violation metric against the *true* performance constraint (Eq. 2) rather than the algorithms' own safety condition, as suggested by the harsh critic.
- A brief discussion of whether covariate shift from only updating the oracle on IGW rounds (not baseline rounds) could affect the regression regret bound.
- Explicit instantiation of the baseline gap parameters ($\Delta_l, \Delta_h, y_l, y_h$) for the experimental datasets, as these appear in the regret bounds.

## Removed Points

These points were raised by reviewers but are removed or downgraded with justification:

- *"The neural network instantiation relies heavily on undisclosed details from prior work (width, learning rate, projection radius)"* — These details are standard for a paper building on prior work and would typically appear in the appendix (which the parser strips). The paper states "The setup closely follows the one in ~\cite{deb2024contextual}, which we restate here for completeness." This is acceptable for a conference paper with an appendix, and the rule forbids penalizing missing appendix content.
- *"Missing parentheses in the safety condition line of Algorithm 2"* — This is a formatting/typographic artifact from PDF parsing, not an author error. The rule requires removing such nitpicks.
- *"The exploration parameter γ_t uses regsq(T) rather than regsq(|S_t|) in Lemma 3.5"* — The critic acknowledges this is acceptable if regsq is monotonic, which is standard. This is not actually a weakness.
- *"Missing related work comparisons"* — The rule forbids mentioning missing related work without external sources to confirm existence.
- Generic strengths from the Strength Finder (e.g., "Experimental validation on real-world data," "Time-dependent exploration and episodic schedule") that are superficial or conflict with verified weaknesses are dropped.

## Novel Insights

The most interesting meta‑observation across these reviews is that the paper's main vulnerability is not in its theoretical scaffolding (which is sound and leverages mature IGW/online‑regression machinery) but in the **interface between theory and experiment**. The reviewers converge on the same point: the experimental section does not adequately isolate the paper's novel contributions. Specifically, the regret plots pit neural‑IGW methods against a linear baseline, which tests the neural component but not the *conservative* innovation. Adding vanilla (non‑conservative) IGW baselines would directly measure the safety‑regret trade‑off that is the paper's central focus. The notation inconsistency in C‑FastCB's safety condition is a secondary concern — easily fixable — but it underscores how a small presentational gap can undermine confidence in an otherwise sound analysis.

## Suggestions

1. **Harmonize the safety condition notation.** Either change C‑FastCB's safety condition to $16\sqrt{m_{t-1}(\regkl(m_{t-1})+\log(1/\delta))}$ (matching C‑SquareCB) or explicitly state that $\regkl(T)$ is a uniform bound satisfying $\regkl(m) \leq \regkl(T)$ for all $m \leq T$ and that the $\log(1/\delta)$ term is absorbed into $\regkl(T)$.

2. **Add a single experiment** comparing regret against vanilla SquareCB and FastCB (without safety) on one or two datasets. This would directly quantify the cost of conservatism and validate that the safety mechanism does not catastrophically degrade regret.

3. **State the KL‑loss neural bound explicitly.** Add a one‑sentence lemma: "Under Assumptions A1–A4, OGD on the perturbed neural network with sigmoid ensemble achieves $\regkl(T) = O(\log T)$," with a brief note on whether this follows from Deb et al. (2024) or requires modification.

## Score and Decision

The paper makes a clean theoretical contribution — first CCB algorithms for general function classes, with a first‑order regret bound that is genuinely novel. The weaknesses are real but localized: a notation inconsistency in one algorithm's safety condition, limited experimental baselines, and a missing justification for the KL‑loss neural bound. None of these undermine the core theoretical claims, and all are addressable in revision. The work is a solid contribution to the safe bandits literature.

**MY FINAL SCORE:** <pineapple>7.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>