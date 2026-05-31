Now I have a clear picture of the paper and can verify each reviewer claim against the actual text.

## Summary

This paper proves that low-rank attention heads (r < d) are fundamentally less expressive than a single full-rank head for representing the nearest-neighbor function, even when many low-rank heads or many parameters are allowed. Theorem 2 establishes a quantitative separation (polynomial or exponential in d/r heads required for low-rank, vs. one head for full-rank). Theorem 3 strengthens this to an exponential separation at constant error. Experiments on standard multi-layer transformers confirm the qualitative predictions. The paper is honest about scope (N=2 lower bounds, weight-norm constraints) and provides a depth-based construction that partially mitigates low-rank limitations for fixed context length.

## Strengths

- **Theorem 2 (rank separation with a natural target):** Proves that approximating the nearest-neighbor function requires Ω((d/r)^{1/ε}) or Ω(exp(d − r log(d/r))) low-rank heads depending on the regime, while a single full-rank head suffices (Fact 1). This is a clean, quantitative separation with a simple, permutation-invariant target that is well-motivated by semantic search.

- **Theorem 3 (exponential separation at constant error):** Strengthens the separation to Ω(exp(d−r)) heads needed for constant approximation error (1/40), using a target composed of polynomially many biased nearest-neighbor functions. This mirrors depth-separation results in the neural network literature and shows the weakness is not an artifact of small ε.

- **Generalized attention model (Eq. 2):** Lower bounds are proved against a class that subsumes biases, additive positional encodings (RoPE, ALiBi), and arbitrary score functions — not just standard dot-product attention. This makes the hardness result architecture-agnostic.

- **Empirical validation (Section 7):** Experiments on fully-featured multi-layer transformers (skip connections, MLPs, normalization) show full-rank models (r=64) outperform low-rank models even with substantially more parameters. The best low-rank model (L=5, r=32, many heads) performs no better than the worst full-rank model (L=1, r=64) despite having 80× fewer attention parameters — directly confirming the theory's qualitative predictions.

- **Nuanced treatment of depth (Section 6):** Provides a constructive upper bound showing depth can overcome low-rank limitations for fixed N=2, while explicitly conjecturing that such constructions scale poorly with N. This avoids overclaiming and identifies the genuine role of depth.

## Weaknesses

### Fatal
None.

### Major

- **Lower bounds proved only for N=2.** The paper acknowledges this directly (line 81: "For technical convenience, we set the number of target points to two"), and Theorem 2 and Theorem 3's lower bounds both assume N=2. The claim that "full-rank is fundamentally more powerful than low-rank" is technically established for two target points. Experiments with N=16 (Figure 2) and N=32 (appendix) partially mitigate this, as does the paper's explicit belief that the framework extends (line 107). Nevertheless, this is the most significant evidential gap — the generality of the conclusion depends on an unproven extension.

- **Weight-norm dependence in Theorem 3 (lower bound).** The exponential lower bound requires the condition $d \cdot H \cdot \max_h \|V_h\|^2 < \exp(c(d-r))$ (line 134). The paper discusses this openly (Remark 4), notes it is a standard limitation (cf. Yehudai & Shamir 2019), and mentions that Kamath et al. (2020) removed such dependencies for a different class but that extending their technique is unclear here. This does not invalidate the result — practical weight norms are unlikely to scale exponentially — but means the result does not strictly rule out arbitrarily large-weight constructions.

### Minor

- **"Farthest neighbor function" in Figure 2 caption (line 172).** The paper's target function is unambiguously the *nearest* neighbor function (argmin, Equation 3), and Section 7 says it trains "on our nearest neighbor target function" (line 184). The caption saying "farthest neighbor function" is a typo that creates confusion. The reviewers flagged this as a potential structural issue; it is a typo that should be corrected.

- **Best-of-five runs without variance reporting.** The experiments report "the best of five runs for each setting" (line 186) without means or standard deviations. This is a common limitation but reduces confidence that the observed separation is statistically robust across random seeds.

### Trivial
None.

## Nice-to-Haves

- **Expand the evaluation of the weight-norm bound.** A brief comment on whether the weight norms observed in practice could plausibly violate the bound in Theorem 3 would make the theoretical separation more concrete.

- **Ablation with orthogonal (or near-orthogonal) target points.** The lower bounds assume orthogonal target points; the experiments use i.i.d. uniform. An experiment bridging this gap would strengthen the theory-experiment connection.

- **Practical guidance.** The paper concludes that "increasing rank may have practical benefits" but gives no estimate of what this implies for typical settings (e.g., d=768, H=12). A speculative discussion would help practitioners.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Criticism about missing appendix content:** The reviewer notes "Additional experiments (appendix) are mentioned but stripped — we cannot assess them." The appendix was stripped by the PDF parser and exists in the original submission. This is not a valid weakness.

- **Criticism about "could the metric be measuring a proxy?" framing:** The harsh critic's section-by-section notes contain general speculations that do not point to specific, verifiable problems with the paper. Example: "Whether such a regime matters in practice is debatable" (about the high-accuracy regime of Theorem 2) — this is a scope observation, not a concrete weakness.

- **Criticism about missing related works:** The reviewer does not flag missing citations concretely, and I cannot verify such claims without external sources.

- **Strength about "addressed an important problem":** Generic and lacks specific content tied to the paper's actual evidence. Removed.

## Novel Insights

Beyond the paper's own contributions, the most striking pattern across the reviews is the tension between the paper's strong, clean theoretical separation (which is rigorous and well-proven within its assumptions) and the practical gap left by the N=2 restriction. The harsh critic correctly identifies this as the single most important limitation, but the strength finder rightly emphasizes that the experiments with N=16 and the open discussion of the limitation partially bridge this gap. A genuinely novel observation is that the paper's lower bound technique — using spherical harmonic analysis to show that low-rank attention heads are confined to few principal directions — is reminiscent of kernel method separation results, and the paper explicitly connects to this line (Yehudai & Shamir 2019). This suggests that the rank bottleneck identified here may be a specific instance of a more general phenomenon linking attention's expressivity to its effective dimensionality, which could be a fruitful direction for future work.

## Suggestions

- Fix the "farthest neighbor function" typo in the Figure 2 caption to read "nearest neighbor function."
- Report mean and standard deviation over multiple random seeds in the experiments rather than best-of-five, to strengthen the empirical claims.
- Add a brief discussion or figure connecting the N=2 theoretical setting to the N>2 experimental setting more explicitly (e.g., an experiment with N=2 that reproduces the same qualitative pattern would directly test the theoretical assumptions).

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>