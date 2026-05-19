- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 6, 8, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces the first second-order (variance-aware) regret bounds for contextual bandits with general function approximation under **only mean-reward realizability** — removing the distributional realizability assumption required by prior work. The authors develop an uncertainty-filtered multi-scale least-squares procedure, extending techniques from variance-aware linear bandits (e.g., SAVE) to general function classes characterized by eluder dimension. Two algorithms are presented: one for known variance (Algorithm 2) achieving regret scaling as \(\tilde{O}(\sigma\sqrt{d_{\text{elud}}\log|\mathcal{F}|\, T})\), and one for unknown variance (Algorithm 3) achieving \(\tilde{O}(d_{\text{elud}}\sqrt{\log|\mathcal{F}|\sum_{t=1}^T\sigma_t^2})\). The unknown-variance result is the paper's marquee contribution.

## Strengths

1. **First second-order bounds under only mean-reward realizability**: The paper correctly identifies and solves a genuine gap — prior work (Wang et al., 2024) required distributional realizability (i.e., a noise-distribution function class), which is restrictive. The paper's abstract and introduction clearly state this advance, and the bounds claimed (Theorem 5) are structurally novel for this setting. This is a non-trivial step forward in bandit theory.

2. **Uncertainty-filtered multi-scale least squares as a technical innovation**: The paper extends the linear-bandit variance-aware machinery (Zhao et al., 2023) to general function classes through a clean and reasonably well-explained mechanism: filtering historical points by uncertainty radius thresholds \(\tau_i = B/2^i\), then computing filtered least-squares estimators per threshold (Equation 5, Algorithm 2). The filtered regression bounds in Proposition 1 and the sharpened eluder lemma (Lemma 5) are genuinely new analytical tools for this setting.

3. **Both known- and unknown-variance algorithms with explicit construction**: Algorithm 3 (unknown variance) provides a concrete, self-contained procedure that uses the filtered least-squares variance estimator (Lemma 7) and multi-bucket confidence sets (Equations 7–8) to adaptively estimate cumulative variance. The approach is non-trivial and represents a genuine algorithmic contribution.

4. **Honest discussion of limitations**: The paper openly acknowledges that its eluder-dimension dependence may not be optimal under time-varying variances ("Although it is likely our bounds are not the sharpest..."), and that a sharper analysis might remove the extra \(\sqrt{\log T}\) factor. This transparency is commendable for a theoretical paper.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Extra \(\sqrt{\log T}\) factor in the unknown-variance bound** (Theorem 5): The leading term of the regret bound is \(d_{\text{elud}}\sqrt{(\sum\sigma_t^2)\log T \log|\mathcal{F}|}\), compared to the target \(d_{\text{elud}}\sqrt{\sum\sigma_t^2\log|\mathcal{F}|}\) (or ideally \(\sqrt{d_{\text{elud}}\sum\sigma_t^2\log|\mathcal{F}|}\)). While the paper acknowledges this, the extra \(\sqrt{\log T}\) is not merely a cosmetic gap — it represents a genuine looseness whose removal would strengthen the paper significantly. The integration argument from Lemma 9 to the final regret bound is only sketched (lines 486–489), leaving the source of this looseness somewhat opaque.

2. **Notational inconsistency in Algorithm 3's confidence set definition** (line 418): The inequality defining \(\mathcal{G}_t'(\tau_i)\) references \(\mathcal{G}_\ell\) (without prime) and \(f_t^\tau\) rather than \(\mathcal{G}'_\ell\) and \(f_t^{(\tau_i,2\tau_i]}\) respectively. This mismatch with the algorithm's own notation (which uses \(\mathcal{G}'_\ell\) everywhere else) is confusing and suggests a copy-paste error. While the intended meaning is recoverable from context, it undermines the reader's ability to verify the correctness of the confidence-set construction.

3. **Dependence on finite \(|\mathcal{F}|\) without discussion of generalization**: The paper assumes a finite function class throughout, using \(\log|\mathcal{F}|\) in all bounds. For infinite function classes, covering numbers or metric entropy would be required, and this transition is neither discussed nor sketched. This limits the immediate applicability of the results to parametric classes, though this is acknowledged implicitly by the paper's framing.

### Trivial
- The paper's abstract contains a minor typographical issue ("no-regret algorithms no-regret algorithms" — likely a LaTeX duplication artifact in extraction).
- The "simplified" Theorem 1 in the introduction uses \(\widetilde{\mathcal{O}}\) but does not fully specify what is hidden; the full statement appears only much later (Theorem 5).

## Nice-to-Haves
- A brief intuitive explanation of why the filtered least-squares bound (Lemma 6) does not grow with the number of filtered points could help readers unfamiliar with finite-class least-squares concentration.
- A more extended proof sketch for Lemma 5 (the variance-aware eluder bound) would improve readability of the key technical step.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Lemma 6 is almost certainly false" (Harsh Critic, Issue 1)**: The critic claims the bound \(\sum b_\ell(f_t^{\mathbf{b}_t}-f_*)^2 \leq 8B^2\log(2|\mathcal{F}|/\tilde\delta)\) is invalid because the RHS is "independent of \(t\)." This is factually wrong. The bound is a standard per-\(t\) concentration inequality for finite function classes (cf. Lemma 1, the standard LS guarantee). The RHS is stated for a _fixed_ \(t\) with tunable \(\tilde\delta\); the dependence on \(t\) arises when the bound is extended to hold for all \(t\) via a union bound (Corollary 5 uses \(\tilde\delta = \delta'/(2t^2)\), yielding \(O(B^2\log(t|\mathcal{F}|/\delta'))\) — the same order as the standard bound). The critic's comparison to linear models (where the bound scales with dimension and sample size) conflates two distinct regimes. This criticism is removed because it is based on a factual misunderstanding of the paper.

2. **"Circular dependence in Algorithm 3 that is not resolved" (Harsh Critic, Issue 2)**: The critic claims the confidence set \(\mathcal{G}'_t\) depends on \(W_t^{\mathbf{b}^{\tau_i}_t}\) which in turn depends on the current \(\mathcal{G}'_t\). This is incorrect. The algorithm is entirely causal: at time \(t\), \(\mathcal{G}'_{t-1}\) is already fixed from prior data; the filtered estimator \(f_t^{(\tau_i,2\tau_i]}\) is computed using data filtered by \(\mathcal{G}'_{t-1}\) (and earlier sets); \(W_t^{\mathbf{b}^{\tau_i}_t}\) is then derived from this estimator; and finally \(\mathcal{G}'_t\) is constructed. There is no circular dependence. The paper's use of nested events \(\mathcal{E}'_\ell\) (line 431) even explicitly handles the inductive structure. This criticism is removed as unfounded.

3. **"Missing proofs in appendix" and "cannot be independently verified"**: Repeated throughout the harsh critic's review. Per review policy, criticisms about absent appendix sections (which are stripped by the PDF extraction pipeline) are not valid. The paper states proofs are in the appendix; these exist in the original submission.

4. **Criticisms questioning baselines, comparisons, or existence of cited prior work**: The critic's mention that "the proofs are not provided" for several lemmas, and that the paper "does not provide a clear derivation of the integration argument," fall under missing appendix content and are removed.

5. **Strengths dropped from Strength Finder**: Some claimed strengths were generic ("Rigorous theoretical lemmas that drive the analysis") or sycophantic ("Honest discussion of remaining gaps" — this one is borderline but I keep it as it's concrete). The strength about "rigorous theoretical lemmas" is too vague since the proofs are in the appendix and we cannot verify them from the provided text, so I remove it. The other strengths I've incorporated above.

## Novel Insights
The harsh critic's review reveals nothing beyond what is already present in the paper. The core technical insight — that filtering historical data by uncertainty radius and applying Freedman-type concentration at each scale yields variance-aware bounds for general function classes — is the paper's own contribution, not something surfaced by the review process. The strength finder correctly identifies the main contributions but adds no new analytical insight.

## Suggestions
1. Fix the notational inconsistency in Algorithm 3's confidence set inequality (the use of \(\mathcal{G}_\ell\) instead of \(\mathcal{G}'_\ell\) and \(f_t^\tau\) instead of \(f_t^{(\tau_i,2\tau_i]}\)) — this is a small fix that significantly improves readability.
2. Provide a more detailed derivation of how Lemma 9 (the unknown-variance eluder bound) is integrated to yield the final regret bound — the current proof sketch is only two lines and does not fully explain the \(\sqrt{\log T}\) factor's origin.
3. Add a short remark in Section 5.1 explaining why the per-step filtered least-squares bound (Lemma 6) does not grow with \(t\), clarifying that the \(t\)-dependence enters through the union bound in Corollary 5. This would preempt the very misunderstanding that occurred in review.
