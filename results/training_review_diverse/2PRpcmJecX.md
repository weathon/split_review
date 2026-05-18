Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper studies the global convergence of projected policy gradient for infinite-horizon average-reward MDPs with tabular policies. Its central claim is to provide the first finite-time convergence analysis *without* assuming the average reward is smooth — it proves smoothness instead, using a projection technique to handle the non-uniqueness of the value function. The paper derives explicit smoothness and Lipschitz constants in terms of MDP-dependent parameters, establishes sublinear convergence (and a regime of exponential convergence for "simple" MDPs), and extends the analysis to discounted-reward MDPs with complexity-dependent bounds.

## Strengths

1. **First convergence analysis for average-reward PG that removes a previously unverified smoothness assumption.** Prior work (Bai et al., 2023; Ganesh et al., 2024) assumed the average reward is smooth without proof. The paper introduces a projection technique (Lemma 1) to obtain a unique representation of the relative value function, which enables proving smoothness rather than assuming it. This directly addresses a recognized gap in the literature.

2. **Explicit formulas for the restricted smoothness and Lipschitz constants of the average reward (Lemmas 2–4).** The constants \(L_1^\Pi\) and \(L_2^\Pi\) are expressed in terms of MDP-dependent parameters \(C_m, C_p, C_r, \kappa_r\), giving a concrete handle on the function class. This is a nontrivial technical contribution — smoothness for the average reward does not follow straightforwardly from the discounted case because the discount factor's contraction is absent.

3. **Sublinear convergence bound and \(O(\log T)\) regret (Theorem 1).** The main bound \(\rho^* - \rho^{\pi_k} \le 1/(1/(\rho^*-\rho^{\pi_0}) + \nu k)\) gives a convergence rate of \(O(1/k)\), improving on the \(O(T^{1/4})\) regret of Bai et al. (2023) under tabular parametrization. The bound is meaningful from the first iteration (it starts at the initial suboptimality and decreases monotonically), unlike bounds of the form \(\sigma/k^p\) that can exceed 1 for small \(k\).

4. **Extension to discounted MDPs with complexity-dependent iteration complexity (Section 3.2).** The analysis yields an \(O(|S| L_2^\Pi / \epsilon)\) bound that can be much smaller than the standard \(O(|S||\mathcal{A}|/((1-\gamma)^5\epsilon))\) when the MDP's \(C_p, C_r, \kappa_r\) parameters are small. The example of action-independent transitions (where the improvement from \(O(|\mathcal{A}|)\) to \(O(1)\) is concrete) illustrates the value of complexity-aware bounds.

5. **Empirical validation of complexity-dependent convergence trends (Section 4).** Simulations show that convergence slows with larger state spaces, higher reward variance, and more deterministic transitions (\(C_p\)). These trends are consistent with the theoretical claim that the MDP-complexity constants capture real structure, not just discount-factor scaling.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The MDP-complexity constants \(C_m, C_p, C_r, \kappa_r\) are not connected to standard MDP parameters in the main text.** The paper defines these constants in Table 1 (an image in the extracted file) and gives qualitative descriptions in the simulation section (e.g., \(C_r\) scales with reward variance, \(C_p\) captures transition sensitivity to policy changes). However, for a reader who wants to interpret the bounds in terms of standard quantities (mixing time, diameter, reward range, concentrability coefficients), the connection is absent from the main text. This makes the bounds less interpretable than they could be. For example, it is not obvious whether \(C_m\) is always finite under Assumption 1, or whether it can be bounded by the mixing time. Adding a proposition that upper-bounds these constants by standard MDP parameters would substantially improve the paper.

2. **The exponential convergence regime ("simple MDPs") lacks structural characterization.** The condition stated is simply \(32|S| L_2^\Pi C_{PL}^2 < 1\), i.e., \(L_2^\Pi \ll 1\). Since \(L_2^\Pi\) itself is a derived constant whose relationship to more primitive MDP structure is opaque, the reader cannot tell which MDPs satisfy this condition. Providing even one nontrivial family of MDPs that provably meet the condition, or an upper bound on \(L_2^\Pi\) in terms of standard parameters that would guarantee the condition, would turn this from an observation into a substantiated result.

3. **Simulations are illustrative rather than rigorous.** The figures show qualitative trends without error bars, confidence intervals, or comparison to any baseline algorithm. Given that the paper claims to validate the theory, at least a single baseline comparison (e.g., against the convergence observed for discounted PG run with a near-1 discount factor) would strengthen the empirical support. The absence of error bars makes it impossible to assess whether the observed differences are significant.

4. **The discounted MDP improvement is context-dependent, which the paper acknowledges but could discuss more transparently.** The paper notes that \(L_2^\Pi\) may scale as \((1-\gamma)^{-5}\) in the worst case, so the improvement over Xiao (2022a) is not guaranteed for all MDPs. This is an honest caveat, but the presentation could better clarify that the main advantage is for "low-complexity" MDPs, not as a uniform improvement over the state of the art.

### Trivial

- The formula for \(\nu\) in Theorem 1 is typeset with a stray prime symbol: `\prime:=\left(\frac{1}{...}\right)` (line 128). This appears to be a minor formatting issue in the extracted text.

## Nice-to-Haves

- Adding upper bounds for \(C_m, C_p, C_r, \kappa_r\) in terms of standard parameters such as mixing time \(|S|, |\mathcal{A}|\), reward range, and the spectral gap of the transition kernel would make the results more usable for practitioners.
- A short discussion of whether the restricted smoothness (Lemma 4) can be strengthened to full (gradient-Lipschitz) smoothness, and whether Lemma 5's derivation requires the full version or suffices with the restricted version, would preempt a natural technical question.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Proofs are absent / central claims unverifiable"** — The hard rules instruct us to remove weaknesses about missing proofs that were likely in the appendix (stripped by the parser). The paper's main body provides a structured proof outline (Section 3.1) with lemma statements and the logical flow; full derivations are standard to relegate to an appendix. This criticism is removed per policy.

2. **"Lemma 5 is likely incorrect as stated"** — The critic's mathematical argument is incorrect. The bound \(\rho^{\pi_{k+1}}-\rho^{\pi_k} \ge \frac{L}{2}\|\pi_{k+1}-\pi_k\|^2\) is a standard consequence of the smoothness inequality combined with the projection property \(\langle\nabla\rho^{\pi_k}, \pi_{k+1}-\pi_k\rangle \ge \frac{1}{\eta}\|\pi_{k+1}-\pi_k\|^2\) and the step-size condition \(\eta < 1/L\). The critic's alternative derivation (mixing \(\eta\|\nabla\rho\|^2\) terms) incorrectly ignores the projection property. The lemma is correct under the paper's definitions; this criticism is removed as factually wrong.

3. **"Table 1 content is unreadable"** — This is a parser artifact of the PDF extraction. The table exists in the original submission. Removed per hard rules.

4. **"Typos and notational inconsistencies"** — Removed per hard rules (formatting artifacts from the parser, not author errors).

5. **"Regret bound is standard/not surprising"** — This is an opinion about the paper's claimed contribution, not a technical weakness. The paper claims \(O(\log T)\) regret from the \(O(1/k)\) per-iteration bound, which is a standard implication. Not a substantive weakness.

6. **"Simulations lack error bars / baselines"** — Already kept as a Minor weakness (item 3 above); the removed version here is the critic's harsher framing that they are "not compelling evidence." The simulations are labeled as illustrative and the paper does not claim rigorous empirical validation.

## Novel Insights

None beyond the paper's own contributions. The paper's main novelty — proving average-reward smoothness via projection and leveraging it for convergence bounds — is already well-articulated in the paper.

## Suggestions

1. Add a proposition or remark that bounds each of \(C_m, C_p, C_r, \kappa_r\) by standard MDP quantities (e.g., mixing time, reward range, concentrability \(C_{PL}\)). This would make the main convergence bounds interpretable without requiring the reader to reverse-engineer Table 1.
2. Either provide a concrete MDP family that provably satisfies the exponential convergence condition, or relegate the exponential claim to a remark with a note that its characterization is left open.
3. Add at least a single baseline comparison to the simulations (e.g., discounted PG with a large discount factor) and report results over multiple random seeds with error bars.

## Score and Decision

This paper addresses a real and recognized gap in the reinforcement learning theory literature. The core technical idea (projection to handle non-uniqueness of the value function, enabling a smoothness proof) is sound, and the resulting convergence bounds are a genuine advance over prior work that relied on unverified assumptions. The weaknesses are minor — they concern interpretability and presentation, not correctness of the core claims. The paper is ready for publication.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>