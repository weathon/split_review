Now I have a thorough understanding of the paper and can cross-check the reviewer claims against the actual text. Let me compose the final review.

## Summary

This paper proposes FastLSH, a simple LSH scheme that reduces hash computation from O(n) to O(m) (m < n) by randomly sampling a subset of dimensions before applying random projection. The paper provides a theoretical analysis of the collision probability, claims asymptotic equivalence to E2LSH, and demonstrates speedups of up to 6.1×, 1.7×, and 20× across three application domains (outlier detection, neural network training, and nearest neighbor search).

## Strengths

- **O(n) to O(m) complexity reduction with broad applicability**: FastLSH requires only two operations — random sampling and random projection — and can be dropped into any existing LSH-based pipeline without modifying the downstream algorithm. The paper demonstrates this by substituting FastLSH into ACE, SLIDE, and ANN search pipelines.

- **Consistent end-to-end speedups across three diverse tasks**: Experimental results show meaningful runtime reductions: up to 6.1× in outlier detection (Table 1), 1.7× in neural network training (Figure 2), and 20× in index construction for nearest neighbor search (Figure 3d). These are concrete wall-clock measurements, not just asymptotic claims.

- **Empirical validation of the distributional approximation**: Figure 1 provides a direct visualization comparing the PDF of ŝX against N(0, ms²/n) on real data (Trevi) across different m values, giving visual evidence that the approximation improves as m grows. This is a helpful sanity check that goes beyond purely theoretical moment matching.

- **Clear motivation and problem framing**: The paper convincingly argues that index construction time — dominated by hashing cost — is the main bottleneck in many LSH-based applications, a point that is underappreciated in the literature.

## Weaknesses

### Fatal
None.

### Major

- **The "provable LSH property" claim is overstated for the limited‑m case**: The paper provides a rigorous derivation of the collision probability (Theorem 4.2) and claims asymptotic equivalence to E2LSH for large m. However, the analysis for limited m (Section 4.3) relies on matching the first four moments of ŝX to those of N(0, ms²/n) and citing that "distributions near the normal can be decided very well given the first four moments." Moment matching does **not** constitute a proof that the collision probability p(s,σ) is a monotonically decreasing function of s for all s — which is what the LSH definition (p₁ > p₂) formally requires. The paper asserts that similarity in PDFs "directly translates to the equivalence between p(s) and p(s,σ)," but the step from matching moments to guaranteeing the LSH inequality is heuristic, not rigorous. While the asymptotic large‑m case may be fully proven in the (stripped) appendix, the limited‑m case — which is the practically relevant regime — is not rigorously established. The authors should either provide a bound on the deviation or explicitly temper the "provable" claim for limited m.

### Minor

- **Key experimental parameters are absent from the main text**: The sampling ratio m/n (the central parameter governing the speed–accuracy trade-off) is not reported for any dataset or task in the main text. Nor are the bucket width (ẅ), number of hash tables, or number of hash functions — all of which are needed to assess whether comparisons are fair and results are reproducible. While the paper references appendices (C.1–C.4), the main narrative should report at least the m values and justify how they were chosen. The paper mentions "a small m (say 30)" in the theory section, but the actual values used in experiments are not stated.

- **No variance or confidence estimates for any experimental result**: LSH is an intrinsically randomized method, yet all tables and figures report single runs without error bars, confidence intervals, or variance estimates. This makes it impossible to assess whether observed differences between methods are statistically significant, especially when several numbers are very close (e.g., outliers detected across ACE, FastACE, and ACHashACE in Tables 1–3).

- **Extensions to other similarity metrics are sketched but untested**: Section 5 mentions angular similarity and maximum inner product search but provides no experimental validation. This weakens the claim of "broad applicability" beyond the Euclidean case.

- **The ACHash comparison is mostly tangential**: The paper devotes substantial space to comparing against ACHash, which the paper itself acknowledges is not an LSH. The meaningful comparison is against E2LSH, and those results (6.1×, 1.7×, 20×) are already reported. The ACHash discussion inflates the evaluation without deepening the core comparison. This is not a flaw in the experiments but a framing issue.

### Trivial

- The formal LSH inequality in Definition 2.1 is truncated in the main text (line 33–34), though the verbal requirement (p₁ > p₂, c > 1) is stated on the next line. This should be completed in the camera‑ready version.

- Figure 2 uses a log-scale x-axis; the paper notes this but an inset showing the early iterations on a linear scale would help.

## Nice-to-Haves

- **Ablation study on m**: A plot showing how recall and hashing time vary as m is swept from small values up to n (on at least one dataset) would give practitioners concrete guidance for choosing m.
- **Empirical verification of monotonicity**: A direct experiment plotting empirical collision probability vs. pairwise distance for FastLSH (for several m values) would directly support the LSH property claim and would be more convincing than the moment analysis alone.
- **Time breakdown**: Breaking the end-to-end speedup into hashing vs. other operations (hash table initialization, linked-list maintenance) would help attribute the gains more precisely.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The promised theorem about asymptotic behavior is not presented"** — The paper references Corollary 4.7, Lemma 4.8, and Fact 4.9 that are not present in the parsed text. Per the review guidelines, these were in the original submission appendices which the parser strips. The criticism that the proof is missing from the main text is a parser artifact, not an author error.

- **"The paper never says how small m is"** — The paper explicitly states (line 110): "a small m (say 30) often suffices." The critic missed this.

- **"Comparison with ACHash is unfair / ACHash is not an LSH"** — The paper itself acknowledges ACHash is not an LSH (line 20–21). Comparing against the only existing fast alternative is defensible and the paper uses it primarily to demonstrate the cost of lacking LSH guarantees, not as the central baseline.

- **"Missing related works on fast LSH"** — Per guidelines, I cannot verify existence of works I have not seen. This point is removed.

- **"Definition 2.1 is cut off"** — The critic acknowledges this is a parser artifact. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's "provable LSH" claim is neither purely false nor fully rigorous — it sits in a gray area where the asymptotic case may be provable but the practically relevant limited-m case rests on heuristic moment matching. This tension is the review's most useful observation and should be addressed directly in revision.

## Suggestions

1. **Clarify the scope of the theoretical guarantee**: Either (a) provide a rigorous bound showing that the LSH inequality holds for limited m, or (b) clearly state that the formal LSH property is proven only asymptotically (large m) and that the limited-m analysis provides an approximate guarantee supported by numerical evidence. The term "provable LSH property" should be qualified accordingly.

2. **Report m/n for each experiment in the main text**: Add a table or paragraph stating the sampling ratio, bucket width, number of hash tables, and how these were chosen (e.g., tuned for a target recall). This is essential for reproducibility.

3. **Add error bars or confidence intervals** to all experimental results, especially for the randomized LSH methods. Without these, the reader cannot assess whether the performance differences are statistically meaningful.

4. **Add an empirical monotonicity plot**: Show the empirical collision probability of FastLSH as a function of pairwise distance (for several m values and a representative dataset). This would directly demonstrate the LSH property in practice and compensate for the theoretical gap.

## Score and Decision

This paper tackles a well-motivated problem (LSH hashing is a bottleneck), proposes an elegantly simple solution (random sampling before projection), and demonstrates substantial empirical speedups. The main weakness is that the "provable LSH property" claim is not fully rigorous for the limited-m regime that matters most in practice. However, the asymptotic analysis provides a solid theoretical foundation, the empirical evidence (including the PDF comparison in Figure 1) supports the claim, and the speedups are compelling. The weaknesses are addressable in revision — primarily by tempering the theoretical claim and adding missing experimental details.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>