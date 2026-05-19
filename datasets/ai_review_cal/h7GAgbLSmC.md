- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information needed to write a consolidated review.

**Summary of verification findings:**

1. **"Poly-logarithmic width" claim**: The paper states width $m = \Omega(\poly(\log(n)/\gamma))$ (lines 47, 54, 66, 114, 158), but the actual condition in Eq. (4) is $m \ge 4\beta_L^2 (6\rho^\star)^{6L+4}$ — exponential in $L$. The paper includes $L$ in the exponent but never qualifies "poly-log" as being only for fixed $L$. This is a valid presentation concern.

2. **Comparison to prior work (activation differences)**: Table 1 explicitly lists "Smooth" for this paper and "ReLU" for Chen et al. (line 24-26). So the paper does disclose the activation difference. The harsh critic's claim that "the paper never acknowledges" this is factually incorrect; it's right there in the table. However, the comparison narrative in the text could discuss trade-offs more.

3. **XOR setup**: The paper clearly states "quadratic activation" (line 179), "linear loss $f(t) = -t$" (line 183). These are transparent. Table 2 shows "Quadratic" for this paper vs "ReLU" for Glasgow et al. (lines 38-41).

4. **Probability bound $e^{-m/16}$**: Verified at line 186. For $m=20$, this gives failure probability ~0.287. Valid concern about strength of the guarantee for small $m$.

5. **Theorem 2 width**: $m \ge \beta_L^2 n^{3L+3}$ (line 164). For $L=2$, $m \ge \beta_L^2 n^9$. Paper acknowledges this as "polynomial" (line 175). Valid concern.

6. **$G_0$ and Section 5 reference**: Line 129 references "Section \ref{sec:gradnorm}" — stripped by parser. The critic's claim about this is removed per rules (missing appendix).

7. **Chen et al. depth dependence**: Both bounds have exponential depth ($4^L$ vs $e^{O(L)}$) in test loss. The asymmetric comparison is about width conditions, not test loss.

Now let me write the final review.Now I'll write the consolidated review.

## Summary

This paper derives new generalization and optimization guarantees for deep neural networks with smooth activations trained by gradient methods. The core technical contribution is an algorithmic stability analysis that leverages Hessian structure along the GD path, yielding bounds that depend on $\|w^\star-w_0\|$ (distance from initialization) rather than on network width. For noiseless NTK-separable data, the test error is $\widetilde O(e^{O(L)}/(\gamma^2 n))$ — removing the $\sqrt{m/n}$ dependence of prior Rademacher-complexity bounds — under width conditions that are poly-logarithmic in $n$ and $1/\gamma$ (for fixed depth). The paper also analyzes noisy data (with a larger width requirement) and demonstrates that large-step-size SGD on the XOR distribution achieves perfect test accuracy in $\Theta(\log d)$ iterations with constant width and linear sample complexity, substantially improving prior NTK and feature-learning results.

## Strengths

- **First algorithm-dependent generalization bound for deep networks via stability analysis (Theorem 1, Eq. 7)**. The paper develops a stability bound of the form $\E[F(w_T)-\widehat F(w_T)] \le \frac{2.2}{n} \E[\sum_t \widehat F(w_t)]$, which depends only on cumulative training loss and is provably tighter than prior Rademacher-complexity bounds scaled by $\|w_t\|$ rather than the smaller $\|w_t-w_0\|$. The paper explicitly contrasts this with Bartlett et al.'s $\ell_{2,1}$-norm bounds which can carry an extra $\sqrt{m}$ factor (Section 2, literature discussion).

- **Width-independent test error rate under NTK separability (Corollary 1, Table 1)**. The bound $\widetilde O(e^{O(L)}/(\gamma^2 n))$ contains no $m$ dependence, whereas the best prior bound (Chen et al. 2020) scaled as $\widetilde O(4^L\sqrt{m/n}/\gamma^2)$. Removing the $\sqrt{m}$ factor is a genuine advance; the paper notes that deriving width-independent bounds was cited as an open problem in Chen et al.

- **Constant-width, $\log(d)$-iteration learning of XOR with large step-sizes (Theorem 3, Table 2)**. The result shows SGD with $\eta=m$ achieves perfect test accuracy in $\lceil\log d\rceil$ iterations with $\widetilde O(d)$ samples and constant width, significantly improving over prior ReLU-based results requiring $\poly(\log d)$ width and iterations (Glasgow et al. 2023). The analysis of how signal outgrows noise during large-step training (Remark following Theorem 3) provides conceptual insight into escaping the NTK regime.

- **Empirical validation of the stability bound (Figures 1–3)**. Experiments on FashionMNIST and MNIST show that the stability-based bound (Eq. 10) tracks the empirical generalization gap across different widths and step-sizes. The paper is appropriately cautious about these experiments (noting that the theoretical conditions cannot be verified and that expectations are approximated by single runs), which strengthens rather than weakens the empirical contribution.

## Weaknesses

### Fatal

None.

### Major

- **The "poly-logarithmic width" framing is accurate only for fixed depth; the actual width condition is exponential in $L$.** The paper repeatedly states that the width requirement is $m = \Omega(\poly(\log n / \gamma))$ (abstract, lines 47, 54, 66, 114, 158), but the actual condition from Eq.~(4) is $m \ge 4\beta_L^2 (6\rho^\star)^{6L+4}$, which for the NTK specialization (Corollary~1) becomes $m \ge \beta_L^2 ((2B+\log(1/\eps))/\gamma)^{6L+4}$. The exponent $(6L+4)$ means the width is exponential in depth $L$, and $\beta_L$ itself depends on $L$ with unspecified growth. This is a significant qualification: for $L=10$, the width grows roughly as $(1/\gamma)^{64}$, which is not "poly-log" in any practical sense. The paper should state plainly that the poly-log claim applies to the $n$ and $1/\gamma$ dependence while the $L$ dependence is exponential, and discuss the implications for deep networks. This does not invalidate the technical results, but it changes how readers assess their scope.

- **The noisy-data result (Theorem 2) requires width polynomial in $n$ with a large exponent.** The condition $m \ge \beta_L^2 n^{3L+3}$ (line 164) is extreme: for $L=2$ hidden layers, this is $m \ge \beta_L^2 n^9$, making the result essentially vacuous for any practical sample size. While the paper notes that this is a polynomial condition (line 175), it does not contextualize how large this is relative to prior consistency results or discuss whether the exponent is an artifact of the analysis. A reader concerned with practical relevance will find this condition prohibitive.

### Minor

- **The XOR theorem's probability guarantee has a non-negligible constant term.** The success probability lower bound is $1 - e^{\log m - \log^2 d} - e^{-m/16} - o_d(1)$ (Theorem 3). For constant $m$ (e.g., $m=20$, as used in experiments), the $e^{-m/16} \approx 0.287$ term is a non-vanishing failure probability independent of $d$. The "with high probability" claim is technically correct but could be clarified — the bound does not converge to 1 as $d$ grows for fixed $m$. (The experiments succeed, suggesting the bound is loose; this is not a technical error but a presentation issue.)

- **The XOR result uses a linear loss $f(t) = -t$ and quadratic activation, limiting its conceptual generality.** Both choices are stated transparently (lines 179, 183), and Table 2 lists the activation. However, the linear loss is unbounded below and non-standard for classification; a discussion of whether the analysis extends to logistic loss or other common losses would help readers assess the result's relevance to understanding feature learning in more typical settings. The quadratic activation's special algebraic properties also mean the result does not directly transfer to ReLU or smoothed ReLU.

- **The comparison to prior NTK results (Table 1) mixes activation types.** While the table lists activation functions (Smooth vs. ReLU; lines 24-26), the text's narrative (e.g., "tightest test error bound for deep nets trained by GD in the NTK regime," line 54) does not discuss whether the improvement stems partly from the smoothness assumption versus genuinely sharper analysis. Adding a note about this trade-off would improve fairness.

- **The experimental validation cannot verify the theory's core conditions.** The paper honestly notes that verifying $m = \Omega(\|w^\star-w_0\|^{6L+4})$ is infeasible and that expected generalization is approximated by single runs (lines 207-208). This is appropriate, but it means the experiments serve as a sanity check rather than a confirmation of the theory. This is a limitation, not a flaw.

### Trivial

- The abstract contains a typo: "alogirthmic" should be "algorithmic" (line 4).

## Nice-to-Haves

- A concrete bound on $\beta_L$'s growth with $L$, or at least an acknowledgment that this growth is an open question.
- For the XOR result, a discussion of whether the analysis can be extended to logistic loss or whether the linear loss is necessary.
- For the noisy-data theorem, a comparison to prior consistency results that might require weaker overparameterization, to contextualize the $n^{3L+3}$ condition.

## Removed Points

The following points from the harsh review are removed with justification:

- **"The Lipschitz parameter $G_0$ is claimed to be $e^{O(L)}$ with a reference to Section 5 (which is not visible)"** — Removed. The paper's reference to Section \ref{sec:gradnorm} (line 129) is to a proof/appendix section stripped by the parser; this exists in the original submission per standard formatting.
- **"The paper never acknowledges that the smoothness assumption is a significant restriction"** — Removed as factually incorrect. The abstract states "smooth activation," Table 1 lists "Smooth" vs. "ReLU," and Theorem 1 specifies the activation is 1-smooth and 1-Lipschitz. The difference is fully disclosed, though the paper could discuss trade-offs more.
- **"The analysis in the remark is described qualitatively but no formal lemma is given"** — Removed. Formal lemmas would reside in the proof appendix, which is stripped by the parser.
- **"Missing related works"** — Removed per instructions (cannot verify existence of external references).
- **"The paper does not discuss computational cost of the experiments"** — Removed as a trivial nitpick.
- **"The paper's comparison to Chen et al. 2020 rests on an apples-to-oranges implicit assumption about depth scaling"** — Weakened. Both bounds have exponential-in-$L$ factors in the test loss ($4^L$ vs $e^{O(L)}$); the width condition comparison is what's asymmetric. This is now captured in the Major weakness about the width condition's $L$ dependence.
- **"The paper should justify why [linear loss] is meaningful"** — Demoted to Minor from the harsh critic's presentation as a stronger issue. The choice is stated transparently; a discussion would be nice but the result stands on its own technical merits.
- **Pure formatting/style nitpicks and grammar concerns** — Removed per hard rules (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The harsh reviewer raises valid contextualization concerns but does not contribute an analytical insight absent from the paper. The Strength Finder accurately identifies the paper's contributions.

## Suggestions

1. **Qualify "poly-logarithmic width" explicitly.** Replace claims like "poly-logarithmic width conditions" with precise phrasing: "For fixed depth $L$, the width condition is poly-log in $n$ and $1/\gamma$, but scales exponentially in $L$." This would be honest and still highlight the improvement for shallow-to-moderate depth.

2. **Add a note to Table 1 about activation assumptions.** Even though the table lists activations, adding a footnote such as "The comparison crosses activation families (smooth vs. ReLU); the improvement reflects both the stability-based analysis and the smoothness assumption" would improve transparency.

3. **Discuss the linear loss limitation in the XOR section.** Add a sentence: "We use linear loss for analytical tractability; extending to logistic loss is an open question."

4. **Quantify the success probability of Theorem 3 for finite $d$ and $m$.** The current bound includes the $e^{-m/16}$ term which, for typical constant widths, gives a non-negligible failure probability. Acknowledging this and explaining why experiments still succeed (the bound is loose) would help.

5. **Contextualize the noisy-data width condition.** Compare it to prior consistency results or add a remark about whether the $n^{3L+3}$ exponent is improvable.

6. **Provide intuition for why exponent differs between Theorem 1 ($6L+4$) and Theorem 2 ($3L+3$).** The paper leaves this unexplained; a brief remark would help the reader.
