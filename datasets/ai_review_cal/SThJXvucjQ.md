- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper develops two algorithms, C-SquareCB and C-FastCB, for Conservative Contextual Bandits (CCBs) with general non-linear cost functions, using Inverse Gap Weighting (IGW) and an online regression oracle. The key technical novelty is a reduction from the safe/constrained bandit problem to online regression that avoids the confidence-set approach (which fails for non-linear functions). C-SquareCB achieves $\tilde{O}(\sqrt{KT} + K/\alpha)$ regret, and C-FastCB achieves a first-order $\tilde{O}(\sqrt{KL^*} + K/\alpha)$ regret bound scaling with the optimal policy's cumulative loss $L^*$ rather than $T$. Neural network instantiations via OGD provide end-to-end bounds, and experiments on six OpenML datasets compare against Conservative LinUCB.

## Strengths

1. **First reduction of conservative contextual bandits to online regression for general non-linear functions.** The paper explicitly identifies that existing UCB-based conservative methods fail for non-linear costs (citing Deb et al. 2024 showing $\Omega(T)$ worst-case regret for Neural UCB), and provides a principled IGW-based alternative. The remark following Lemma 4.4 explicitly notes "our analysis relating $n_T$ to squared loss... gives a reduction to online regression," which is a novel contribution over both Foster et al. (2020) and prior linear conservative bandit work.

2. **Novel analysis bounding the number of baseline plays without confidence sets.** Lemma 4.2–4.3 derives an $n_T$ bound by relating baseline plays to the squared-loss regret of the regression oracle. As the paper notes (Remark after Lemma 4.4), in the linear case the analysis "crucially uses the upper and lower confidence bounds," which are unavailable for general function classes. This is a genuine technical contribution.

3. **First-order regret bound for conservative bandits.** Theorem 5.2 provides a regret bound scaling with $\sqrt{KL^*\log L^*\,\mathrm{reg}_{\mathrm{KL}}(T)}$ instead of $\sqrt{KT}$, which is strictly stronger when $L^* \ll T$. No prior conservative bandit result achieves this data-dependent guarantee.

4. **Time-dependent exploration parameter adaptation.** The algorithm uses $\gamma_t = \sqrt{K |\mathcal{S}_t| / (\mathrm{reg}_{\mathrm{sq}}(T) + \log(4/\delta))}$ that depends on the current safe-action set size, extending the fixed-$\gamma$ analysis of Foster et al. (2020). This is necessary to simultaneously bound regret from IGW and baseline actions.

## Weaknesses

### Fatal
None.

### Major

1. **The neural KL-loss instantiation is not fully specified, and the theorem statement contains errors.** Theorem 7 (NeuC-FastCB) states: "We instantiate $\sqalg$ with the predictor $\hat{y}_{t,a_t} = \tilde{f}^{(S)}(\theta;\x_{t},{\epsvec}^{(1:S)})$ from \eqref{eq:ftildeS} and update the parameters using OGD in \eqref{eq:pogd}." Three problems: (a) It uses $\sqalg$ (squared-loss oracle symbol) rather than a KL-loss oracle; (b) The predictor should be the sigmoid-ensemble from \eqref{eq:ftildeS_kl}, not the raw ensemble from \eqref{eq:ftildeS}; (c) The OGD update \eqref{eq:pogd} is defined for the squared loss $\mathcal{L}_{\mathrm{sq}}^{(S)}$, not for KL loss. While the paper cites Deb et al. (2024) which provides $O(\log T)$ regret for neural OGD with both losses, the theorem as written is inconsistent and would confuse readers about what loss is actually being optimized. This is a significant presentation gap that must be corrected — the authors should either provide the KL-loss update rule explicitly or clarify how the cited result applies.

2. **The experimental evaluation is thin and insufficiently controlled.** Only one baseline is compared (C-LinUCB, a *linear* method). On non-linear problems, a linear method is expected to underperform, so outperforming it does not convincingly demonstrate the effectiveness of the proposed approach. The paper would benefit from at least one non-linear baseline — either a non-conservative non-linear method (e.g., vanilla SquareCB/FastCB, to measure the cost of conservatism) or a modified neural UCB baseline. Additionally, no error bars/confidence intervals are shown for the regret curves, and the experimental setup does not verify whether C-LinUCB itself satisfies the safety constraint (its confidence sets are misspecified under non-linear costs, so it likely does not, making a regret comparison with an unsafe baseline uninformative).

### Minor

3. **Experimental details are underspecified.** The paper does not state which action is chosen as the baseline ("fix one action as the baseline action" — which one?), the values of $K$ for each dataset (e.g., Covertype has 7 classes, Fashion MNIST 10), or how hyperparameters (step sizes, network width) were selected beyond a grid search. It reports 10 runs for regret and 100 runs for constraint violation without explaining the discrepancy.

4. **The safety condition's dependence on $\regsq(m_{t-1})$ requires clarification.** While this is not a fatal issue (the algorithm knows $\regsq(\cdot)$ as a bound on its oracle and knows $m_{t-1}$), the paper should explicitly state that $\regsq(\cdot)$ is a known function (e.g., $\regsq(T) = O(\log T)$ for OGD) and that $\regsq(m_{t-1})$ is obtained by plugging $m_{t-1}$ into this function. The critic's concern that this value is "not known to the algorithm" is incorrect, but a clearer statement would prevent confusion.

### Trivial
- Theorem 4.1's proof environment is empty in the parsed version (likely deferred to an appendix); if present, this should be referenced.
- Equation numbering: the C-FastCB safety condition (Algorithm 2, line 264) uses $\regkl(T)$ while the C-SquareCB version uses $\regsq(m_{t-1})$ — the asymmetry is fine but should be explicitly justified.

## Nice-to-Haves
- A sensitivity study over $\alpha$ (the regret bound's second term depends on $\alpha$; a plot of regret vs. $\alpha$ would be informative).
- Code release to improve reproducibility.

## Removed Points

These points were raised by reviewers but are removed because they are factually incorrect, speculative, or violate filtering rules:

1. **"The safety condition uses $\regsq(m_{t-1})$ which is not known to the algorithm."** — REMOVED (factually incorrect). $\regsq(\cdot)$ is a known bound function of the oracle (e.g., $O(\log T)$ for OGD), and $m_{t-1}$ is known to the algorithm. The algorithm can compute $\regsq(m_{t-1})$ directly.

2. **"No code is provided"** — REMOVED (reproducibility nitpick per rules).

3. **"The neural KL-loss instantiation is unsupported / cannot be established"** — REMOVED in its strongest form (the paper cites Deb et al. 2024 for neural OGD bounds with both losses). Kept as a Major weakness about the *specification* errors in the theorem statement, not about the underlying claim being unsupported.

4. **"Proof of Theorem 4.1 is missing"** — REMOVED (deferred to appendix; per instructions, appendix content is stripped by the parser and existed in the original submission).

5. **"Missing related works"** — REMOVED per instructions (no external sources to confirm).

6. **"The KL loss is not convex in network parameters"** — REMOVED in its strongest form. The KL loss with sigmoid outputs is the logistic loss, which is convex in function values. In the NTK regime, the standard OGD analysis applies via the linearized approximation, and Deb et al. (2024) covers this.

7. **Strengths removed**: "Empirical outperformance on real-world data" — kept but qualified given the weak experimental setup. Generic strengths about the "importance of the problem" removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews are largely consistent in their assessment: the theoretical reduction is a genuine contribution, the KL-loss neural instantiation lacks crisp specification, and the experiments are too narrow to fully validate the claims. The harsh critic's implementability concern about $\regsq(m_{t-1})$ being unknown is incorrect, but the broader point that the paper could be clearer about implementation details is valid.

## Suggestions

1. Fix Theorem 7 (NeuC-FastCB) to use the correct oracle symbol, the correct predictor equation (\eqref{eq:ftildeS_kl}), and specify the KL-loss OGD update rule (or clarify that it follows from Deb et al. 2024).
2. Add at least one non-linear baseline to the experiments (vanilla SquareCB/FastCB or a neural bandit baseline). Include error bars on regret plots.
3. Clarify in the main text that $\regsq(\cdot)$ is a known bound function and that $\regsq(m_{t-1})$ is computed by evaluating this function at $m_{t-1}$.
4. Provide explicit dataset statistics (number of actions $K$, feature dimension $d$, horizon $T$, chosen baseline action) in the experimental section.
5. Add a brief discussion of how the baseline action's expected cost $h(\x_{t,b_t})$ is obtained in practice (the paper assumes it is known, which is standard in the conservative bandit literature, but acknowledging practical estimation strategies would strengthen the work).
