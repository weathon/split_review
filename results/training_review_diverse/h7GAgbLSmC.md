Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper develops stability-based generalization bounds for deep neural networks with smooth activations trained by gradient methods. Under NTK separability with poly-logarithmic width, it achieves a test-error rate of $\widetilde O(e^{O(L)}/(\gamma^2 n))$ — removing the width dependence that plagued prior Rademacher-complexity bounds. It also provides a consistency result for noisy data (with polynomial width) and a separate analysis showing that for the XOR distribution, SGD with large step-size achieves perfect test accuracy in $\log(d)$ iterations using constant width and $\widetilde O(d)$ samples.

## Strengths

1. **Width-independent test-loss bound for multi-layer networks under NTK separability.** Theorem 1 and Corollary 1 achieve a test-error rate of $\widetilde O(e^{O(L)}/(\gamma^2 n))$ under width $m = \Omega(\poly(\log(n)/\gamma))$. As the paper notes (Section 3.1, citing Chen et al. 2020, Sec 3.1), deriving width-independent bounds for multi-layer networks was an open problem; this result directly resolves it.

2. **Novel algorithmic-stability analysis using Hessian structure.** The bound in Eq. (7) depends on $\|w^*-w_0\|$ (distance from initialization) rather than $\|w_t\|$, capturing the role of initialization and training dynamics. This is a qualitative improvement over Rademacher-complexity bounds whose dependence on $\|w_t\|$ grows with width. The derivation exploits the deep net's Hessian along the gradient path, extending stability analysis beyond the convex and two-layer settings.

3. **Constant-width, logarithmic-iteration learning of XOR.** Theorem 3 shows that SGD with step-size $\eta=m$ reaches perfect test accuracy after $\lceil \log(d)\rceil$ iterations with a constant-width network and $\widetilde O(d)$ samples. Table 2 shows this improves substantially over the NTK regime ($d^2$ width, $d^2$ iterations) and prior feature-learning work ($\poly(\log(d))$ width, $\poly(\log(d))$ steps).

4. **Experimental validation of the stability bound.** Figures 1–3 show that the theoretical bound from Eq. (13) closely tracks the empirical generalization gap on FashionMNIST and MNIST across different widths and step-sizes. The paper honestly acknowledges that the width condition is not verified in experiments, but the alignment is still non-trivial and supportive.

5. **Consistency guarantee for noisy data.** Theorem 2 establishes that with early stopping at $T=\sqrt{n}$ and polynomial width, GD achieves the optimal population loss at rate $O(1/\sqrt{n})$ in the non-interpolating regime — a setting prior NTK analyses for deep nets typically did not address.

## Weaknesses

### Fatal
None.

### Major

1. **Probability guarantee in Theorem 3 is incompatible with the claim of constant width.** The theorem states that with probability at least $1 - e^{\log(m)-\log^2(d)} - e^{-m/16} - o_d(1)$, test accuracy is $1-o_d(1)$. If the width $m$ is truly constant (e.g., $m=20$ as in the experiments), then $e^{-m/16}$ is a non-vanishing constant (≈0.29), so the success probability does **not** converge to 1 as $d\to\infty$. The text (line 191) says "the network's width can be constant and at most must be polynomial in $d$" — the lower bound (constant) and upper bound (polynomial) are both stated, but the probability guarantee requires the former for the asymptotics. The paper needs to clarify exactly what growth condition on $m$ (as a function of $d$) is actually required for the $1-o_d(1)$ claim, or else state that for any fixed $d$ a constant $m$ suffices but asymptotic probability requires $m = \omega(1)$. This is a technical inconsistency in one of the paper's highlighted results.

### Minor

1. **Selective presentation of the Chen et al. bound in Table 1.** The text (lines 63–65) correctly cites the full Chen et al. bound $\widetilde O\big(\frac{4^L}{\gamma^2}\sqrt{\frac{m}{n}} \wedge (\frac{L^{3/2}}{\gamma^2\sqrt{n}} + \frac{L^{11/3}}{\gamma^2 m^{1/6}})\big)$. However, Table 1 displays only the first term $\widetilde O(\frac{e^{O(L)}}{\gamma^2}\sqrt{\frac{m}{n}})$, with the second term commented out in the LaTeX source. This gives a casual reader an incomplete picture. The paper's bound $\widetilde O(e^{O(L)}/(\gamma^2 n))$ is genuinely tighter in $n$-dependence than **both** terms of Chen et al. (since $1/n \ll 1/\sqrt{n}$), and the exponential $L$-dependence also appears in Chen et al.'s first term. But the paper does not discuss the regime where Chen et al.'s second term might be competitive (large $L$, where $L^{3/2}$ is far smaller than $e^{O(L)}$). A brief side-by-side comparison clarifying the $n$ vs. $L$ tradeoff would strengthen the paper's positioning.

2. **$\beta_L$ is not characterized or bounded.** The width conditions throughout (Eq. (8), Corollary 1, Theorem 2) depend on a constant $\beta_L$ that "only depends on $L$." The paper never bounds $\beta_L$ or gives its growth rate (e.g., $e^{cL}$). Since the paper's rates have exponential $L$-dependence via $G_0$, the actual size of $\beta_L$ matters for determining the overall $L$-dependence of the width requirement. The paper should at least state that $\beta_L$ is $O(e^{cL})$ or provide a reference for its growth.

3. **The XOR analysis uses a different loss function.** The rest of the paper uses the logistic loss, but Theorem 3 uses the linear loss $f(t)=-t$, which is unbounded below and has different optimization properties. The paper does not comment on whether the XOR result extends to logistic loss or why the linear loss is necessary for the analysis. This limits the integration of the XOR result with the rest of the paper's framework.

### Trivial
None.

## Nice-to-Haves

- A discussion of the $L$-dependence tradeoff between the paper's bound ($e^{O(L)}$) and the alternative from the second term of Chen et al. ($L^{3/2}$), clarifying that the improvement in $n$ comes at the cost of worse $L$-dependence, and that both are reasonable in different regimes.
- Clarifying in Theorem 3 whether constant $m$ works for any fixed $d$ with the stated probability, or whether $m$ must grow (e.g., $m = \omega(1)$ or $m \ge \log d$) for the asymptotic $1-o_d(1)$ guarantee.

## Removed Points

These points from the reviews are removed (with brief justification):

1. **"Misleading comparison — paper compares only against first term of Chen et al."** — Partially removed. The **text** (lines 63–65) correctly cites the full minimum of two bounds; only Table 1 is selective. The reviewer's claim that the second term has "better in $n$ ($1/\sqrt{n}$ vs $1/n$)" is factually wrong — $1/n$ is tighter than $1/\sqrt{n}$. The real tradeoff (exponential vs. polynomial in $L$, not $n$) has been downgraded to a Minor weakness about table presentation.

2. **"Missing descent lemma condition and step-size compatibility"** — Removed. The paper explicitly states the step-size condition at line 131 ($\eta < 1/(G_0^2+1/4)$) and references Lemma lem:des (appendix, stripped by parser). The reviewer's claim that the training loss bound "becomes exponentially large" due to small $\eta$ is incorrect: substituting $\eta < 1/(G_0^2+1/4)$ into Eq. (125) gives the training loss term $O(\rho^{*2} G_0^2 / n)$, which has the same $e^{O(L)}$ scaling already acknowledged in the paper's rate.

3. **"The 'algorithm-dependent' claim is overstated"** — Removed. The paper acknowledges prior stability work for two-layer nets (lines 140–142) and its remark about "first" is qualified to "deep neural networks" (multi-layer), for which prior stability analysis using Hessian structure did not exist. The paper also cites Hardt et al. (2016) and prior stability work as antecedents.

4. **"Corollary 1 is stated without proof sketch"** — Removed. The proof (a standard largeness argument scaling the NTK separating direction) belongs in the appendix, which was stripped by the parser. The argument is standard in the NTK literature.

5. **"Missing descent lemma derivation" / "step-size not derived"** — Removed. The derivation is deferred to the appendix (Lemma lem:des), which was stripped by the parser. The condition is stated explicitly in the main text (line 131).

6. **"Width condition for noisy-data consistency is impractically large"** — Downgraded from standalone criticism. The paper itself acknowledges this limitation (line 175: "This comes at the expense of a larger width condition"). The result is clearly presented as a theoretical consistency guarantee, not a practical prescription. The criticism adds no new information beyond what the paper already says.

7. **"The descent lemma condition is not stated"** — Removed as factually incorrect. The condition $\eta < 1/(G_0^2+1/4)$ is stated at line 131.

8. **Various formatting/style/strawman criticisms** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the core technical contributions are novel and significant, while pointing out presentation issues and one genuine inconsistency (XOR probability) that the authors should address.

## Suggestions

1. Fix the tension in Theorem 3 by either: (a) stating that $m$ must grow with $d$ (even slowly, e.g., $m = \omega(1)$ or $m \ge \log d$) for the $1-o_d(1)$ probability claim, or (b) clarifying that the bound holds with high probability for any fixed $d$ with constant $m$, but the asymptotic statement requires $m\to\infty$.

2. Add the second term of the Chen et al. bound back into Table 1, and add a brief discussion comparing the tradeoffs (the paper's $1/n$ vs. Chen et al.'s $1/\sqrt{n}$ in $n$; exponential vs. polynomial in $L$).

3. Provide a bound on $\beta_L$ (e.g., $\beta_L \le e^{cL}$) or cite a source that characterizes it, so readers can assess the full $L$-dependence of the width conditions.

4. Comment on why the XOR analysis uses linear loss instead of logistic loss, and whether the result extends to logistic loss or is specific to the linear case.

## Score and Decision

**Overall assessment:** The paper makes a legitimate theoretical contribution — the stability-based analysis removing width dependence from generalization bounds for multi-layer networks is a genuine advance over the prior state of the art (which the paper correctly attributes and contextualizes). The XOR result is clean and demonstrates the power of escaping the NTK regime. The main weakness — the probability inconsistency in Theorem 3 — is real but fixable without altering the core contribution. The remaining issues (selective table presentation, uncharacterized $\beta_L$, different loss for XOR) are presentation-level concerns. The paper is a strong theory paper with clear, verifiable contributions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>