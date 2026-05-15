Now I have a thorough understanding of the paper and the critiques. Let me write the consolidated review.

## Summary

FastLSH is a locality-sensitive hashing scheme that accelerates hash computation by first randomly sampling a fixed number $m < n$ of dimensions (with replacement), then applying the standard E2LSH-style random projection on the sampled $m$-dimensional vector. The paper derives the collision probability for FastLSH, argues for asymptotic equivalence to E2LSH, and presents experiments across outlier detection, neural network training, and ANN search tasks showing 1.2×–20× end-to-end speedups with maintained accuracy.

## Strengths

- **Simple, practical method with real speedups.** FastLSH requires only random sampling followed by random projection—two operations implementable in any LSH pipeline. Experiments demonstrate genuine end-to-end speedups (up to 6.1× in anomaly detection, 1.7× in training time, and 20× in index construction) across three diverse tasks and multiple datasets. These speedups are not merely a consequence of using fewer dimensions; the paper shows that accuracy/recall is maintained, which is the non-trivial part.

- **Non-trivial theoretical framework.** Despite the gaps discussed below, the paper provides a formal derivation of the FastLSH collision probability (Theorem 4.2), derives the characteristic function of the product $\tilde{s}X$ (Lemma 4.4), and connects the analysis to the E2LSH framework via Fact 4.5. This goes well beyond a purely heuristic proposal.

- **Broad applicability demonstrated.** FastLSH is evaluated on three fundamentally different tasks (outlier detection via collision counting, neural network training via hash-based neuron selection, and ANN search), showing consistent behavior across settings. The method is designed to be a drop-in replacement for standard LSH, and the experiments support this claim.

## Weaknesses

### Fatal

- **The paper's central advertised contribution—a "provable LSH property" and "theoretical guarantee"—is not established.** The LSH property requires the collision probability to be monotonically decreasing in the Euclidean distance $s$ (Definition 2.1). The paper never proves this for FastLSH:
  - The collision probability $p(s,\sigma)$ depends on both $s$ and the per-dimension variance $\sigma$ of squared differences (Theorem 4.2), which varies across point pairs at the same distance. The monotonicity of $p(s,\sigma)$ in $s$ is asserted but never proven.
  - Section 4.2 promises "the following theorem gives the asymptotic behavior of the characteristic function of $\tilde{s}X$" but no theorem statement appears in the main text. The section instead shows a qualitative figure (Figure 1) and states Fact 4.5 (a known property of E2LSH). The claimed asymptotic equivalence to E2LSH—which would imply the LSH property—is not established in the available text.
  - Section 4.3 ("The LSH Property for Limited $m$") matches the first four moments of $\tilde{s}X$ to those of $\mathcal{N}(0, ms^2/n)$. Moment matching does **not** prove that the collision probability is monotonic in $s$, nor does it establish the LSH property.
  - The truncated normal approximation for $\tilde{s}^2$ (Section 4.1) is an ad hoc modeling choice, not derived from the sampling process.

  Because the paper's title, abstract, and conclusion all emphasize the "theoretical guarantee" and "provable LSH property" as its primary differentiator from prior fast-sketch methods like ACHash, this gap is fatal to the paper's core claim. **The paper in its current form overstates its contribution.** This overrides any softening of the overall assessment.

### Major

- **The collision probability depends on the point-pair-specific variance $\sigma$, not just the distance $s$.** This means that two point pairs at the same Euclidean distance $s$ but with different per-dimension variance profiles will have different collision probabilities under FastLSH. The paper acknowledges this dependence (line 175: "FastLSH can be regarded as a generalized version of E2LSH by considering one additional impact factor") but does not analyze whether this dependence could violate the LSH property—e.g., whether a pair at distance $s$ could have a lower collision probability than a more distant pair, depending on their variance structures.

- **The speedup in hashing cost is a trivial consequence of reducing dimensions from $n$ to $m$,** as noted throughout the paper ($O(n)$ to $O(m)$). The real question—whether the method preserves distance-ordering behavior across diverse data distributions—is not rigorously addressed. The empirical results show comparable accuracy on downstream tasks, but without directly measuring collision probability as a function of distance, these results cannot substitute for the missing theoretical guarantee.

### Minor

- **No direct empirical test of the LSH property.** The paper would be significantly stronger if it included experiments that measure empirical collision probabilities over many random point pairs at varying distances and checks whether the probability is monotonically decreasing in $s$ (for both fixed and varying $\sigma$). The current experiments test the method only on downstream tasks, which conflates many factors.

- **No ablation on sampling strategy.** The paper uses random sampling with replacement without comparing against sampling without replacement or a fixed random subset of dimensions. Such an ablation would clarify whether the specific sampling scheme matters or if any low-dimensional projection yields the observed speedups.

- **Missing precision/recall metrics for outlier detection.** The paper reports only raw counts of "correctly reported outliers" and "outliers reported" (Tables 1–3). Precision, recall, or F1 would be more informative—especially since FastACE sometimes reports *more* outliers than ACE, which could indicate a higher false positive rate rather than better detection.

- **Results are reported without variance or confidence intervals.** Many numbers (speedups, accuracy, counts) are reported as single values. While single-run evaluation is common in large-scale systems papers, confidence intervals would help assess the stability of the observed speedups.

### Trivial

- The claim in the abstract and conclusion that FastLSH "maintains the same theoretical guarantee … as the classic E2LSH" is contradicted by the paper's own acknowledgment that $p(s,\sigma)$ depends on $\sigma$ in addition to $s$—this is not "the same" guarantee.
- The paper says "rigid analysis" (lines 99, 276) where "rigorous" is standard.

## Nice-to-Haves

- A comparison against a simple baseline that uses a fixed random subset of dimensions (without replacement) for projection, to isolate the effect of the specific sampling scheme.
- A study of how $m$ affects collision probability and downstream accuracy, systematically varying the sampling ratio $m/n$.
- Providing variance estimates or confidence intervals for key experimental results.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"ACHash is explicitly stated to not have the LSH property, yet it is used as a primary competitor"** — Removed as a non-issue. Using a non-LSH baseline to demonstrate the advantage of the LSH property is standard experimental design. The comparison against ACHash tests whether FastLSH achieves better accuracy (due to the LSH property) while also being fast, which is exactly the right comparison.

2. **"Figure 3 images are missing"** — Removed. This is a PDF-parser artifact; the original submission contains the figures.

3. **"Corollary 4.7/Lemma 4.8/Fact 4.9 not stated" / "proofs referred to appendices"** — Removed per policy. The parser strips appendix content. These results exist in the original submission.

4. **"Pure formatting/style nitpicks"** — Removed. These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not generate a novel observation that the paper itself does not articulate.

## Suggestions

1. **Revise the central claim.** The paper should not claim a "provable LSH property" unless the monotonicity of $p(s,\sigma)$ in $s$ is actually proven. Either provide a complete proof (for all $m$, or at least asymptotically with rigorous finite-$m$ bounds), or reposition FastLSH as a heuristic that achieves strong empirical performance while lacking a full theoretical LSH guarantee. The latter is an honest and still valuable contribution.

2. **Add direct empirical validation of the LSH property.** Compute empirical collision probabilities for many random point pairs at varying distances and show that they are monotonically decreasing in $s$. This would at least partially compensate for the absence of a complete proof.

3. **Run the ablation on sampling strategy** (with vs. without replacement vs. fixed subset) to clarify whether the specific scheme matters.

4. **Add precision/recall or F1 to the outlier detection evaluation.**

## Score and Decision

The paper identifies a real bottleneck and proposes a simple, empirically effective solution. However, its central advertised contribution—a "provable LSH property" and "theoretical guarantee"—is not supported by the analysis presented. The theoretical section contains significant gaps: the monotonicity of the collision probability is never proven, the claimed asymptotic equivalence lacks a theorem statement in the main text, and the finite-$m$ analysis (moment matching) does not establish the LSH property. Until these claims are either substantiated or appropriately scoped down, the paper cannot be accepted in its current form. The core idea and empirical results have value, but they do not match the strength of the advertised claims.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>