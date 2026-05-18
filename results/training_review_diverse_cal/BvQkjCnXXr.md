Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper proposes FastLSH, a variant of LSH that reduces the per-vector hash computation cost from O(n) to O(m) by randomly sampling m < n dimensions before applying the standard random projection. The method is simple and the experimental results show meaningful speedups (up to 6.1× in outlier detection, 1.7× in neural network training, 20× in index construction) across three ML tasks. The paper claims FastLSH has a "provable LSH property" via asymptotic equivalence to E2LSH, which is presented as the key differentiator from non-LSH fast sketches like ACHash.

## Strengths

- **Significant and well-demonstrated empirical speedups across diverse tasks**: The experiments cover three distinct application domains (outlier detection with ACE, neural network training with SLIDE, nearest neighbor search with E2LSH/MPLSH). The speedups are meaningful — 6.1× on Musk for outlier detection (Table 1), 1.7× on Delicious-200K for training (Figure 2), and up to 20× in index construction (Figure 3d/h). These results directly validate that the complexity reduction translates into practical gains, and the paper's use of multiple tasks and datasets strengthens this evidence.

- **Simple, easily integrable design**: The method requires only two operations — random sampling of dimensions followed by standard random projection — making it straightforward to drop into existing LSH-based pipelines. The experiments confirm this by plugging FastLSH into ACE, SLIDE, and E2LSH/MPLSH without architectural changes.

## Weaknesses

### Fatal

- **The claimed LSH property is not convincingly proved, and this is the paper's central theoretical selling point.** The paper claims FastLSH has a "provable LSH property" (abstract, line 4; Section 3.1) and that this distinguishes it from non-LSH sketches like ACHash. Three issues make this claim unsupported:

  1. **Asymptotic equivalence does not establish the LSH property for any finite m.** The argument in Section 4.2 attempts to show that as m → ∞, the distribution of s̃X approaches N(0, ms²/n). Even if this is proved (the key steps — Corollary 4.7 and the characteristic-function derivation — are deferred to the appendix), the LSH property (Definition 2.1) requires that the collision probability be monotonically decreasing in the true distance s for *every finite m* used in practice. Convergence in the limit does not guarantee monotonicity, and the paper provides no rate of convergence or finite-sample bound.

  2. **The moment-based analysis for limited m (Section 4.3) does not bridge the gap.** Lemma 4.8 and Fact 4.9 compare the first four moments of s̃X and N(0, ms²/n). Moment similarity does not imply that the collision probability is monotonic in s, especially because the probability depends on the full shape of the distribution, not just its first four moments. The paper does not derive any bound on how much the collision probability can deviate from monotonicity.

  3. **The acknowledged dependence on σ is not resolved.** The paper explicitly states (line 175) that "p(s,σ) depends on both s and σ" — unlike standard E2LSH where p depends only on s. This means two point pairs with the same Euclidean distance s but different per-dimension variance σ could have different collision probabilities under FastLSH. The paper never proves that monotonicity in s holds when σ varies independently; it simply acknowledges the difficulty and proceeds. This gap is structural: without resolving it, one cannot claim FastLSH satisfies the LSH definition.

  **Why this is fatal:** The paper's title, abstract, and introduction all foreground the "theoretical guarantee" and "provable LSH property" as the key contribution that separates FastLSH from non-LSH sketches (ACHash). The experiments do demonstrate empirical speedups, but the theoretical guarantee is the claimed differentiator. Because the proof is incomplete in a way that directly affects the paper's core identity, this weakness cannot be addressed in a rebuttal — it requires either a fundamentally different proof strategy or a substantial reframing of the contribution. As presented, the theoretical claim overreaches what the analysis supports.

### Major

- **The comparison with ACHash is uneven and occasionally discounts its competitive results.** The paper repeatedly attributes ACHash's poorer performance to "lack of theoretical guarantee" (lines 235, 237, 253), but in several cases ACHashACE detects more correctly reported outliers than ACE (Tables 2 and 3, a9a and Statlog Shuttle). The paper dismisses these cases by noting ACHashACE has a "much higher" number of total reported outliers "indicating a lower precision," but never reports precision, recall, or F1 scores to support this. When ACHash performs worse, it is highlighted; when it performs comparably or better on some metrics, the results are explained away without quantitative backing. A more balanced presentation with proper precision metrics would strengthen the case for FastLSH without relying on dismissal.

### Minor

- **The extension section (Section 5) is cursory** — two sentences plus a reference — and adds no technical content. It could be removed or expanded with even a brief sketch of how the sampling approach generalizes.

- **Per-dataset speedup numbers for index construction are only given visually in figures, not in tables.** The paper reports "up to 20×" speedup but does not provide a table with per-dataset quantitative speedups in the main text. While Figure 3(d) and (h) show the data, exact numbers would make the practical impact easier to assess.

### Trivial

- None.

## Nice-to-Haves

- Report precision, recall, or F1 for the outlier detection experiments to properly quantify ACHashACE's trade-offs rather than relying on raw outlier counts and inference.
- Provide a direct numerical verification that the collision probability is empirically monotonic in s across a sweep of m, w, and data distributions — this would not replace a proof but would make the empirical claim more credible and directly address the σ-dependence concern.
- Include a per-dataset table of speedup numbers (index construction and end-to-end) in the main text.

## Removed Points

- **"Frequent reliance on unreported details and missing appendix content"** — The paper references Proof.1, Proof.2, Proof.3, and Appendix C.1–C.4. Appendix stripping is a parser artifact; these exist in the original submission. Per hard rules, weaknesses about missing appendix content are removed.
- **"Definition 2.1 is only partially given"** — The definition appears cut off in the extracted text, but this is a parsing artifact, not an author error. Removed per rules on formatting artifacts.
- **"Corollary 4.7 and the characteristic function derivation cannot be assessed without the appendix"** — Same parser issue; the appendix exists.
- **Strength: "Provable LSH property with reduced hashing complexity"** — Conflicts with the verified fatal weakness (the LSH property is not convincingly proved). Removed per rule: when a strength and verified weakness disagree, the weakness wins.
- **Strength: "Rigorous analysis for limited sample sizes"** — The moment analysis is presented as supporting evidence, but the critique that it does not establish monotonicity is correct. This strength overstates what the analysis achieves. Downgraded/removed.
- **"Recall-vs-time curves are only in the appendix"** — Stripped appendix content per parser rules.
- **Suggestions to include full appendix derivations in the main text** — Impractical for page limits, and the appendix exists. Removed.

## Novel Insights

None beyond the paper's own contributions. The core tension identified by the reviews — between a simple, empirically effective method and an overclaimed theoretical guarantee — is the standard pattern that emerges when the proof technique (asymptotics + moment matching) is insufficient for the claimed property (finite-sample LSH monotonicity). The paper would benefit from honestly characterizing this gap.

## Suggestions

1. **Reframe the theoretical contribution.** Either (a) prove the LSH property rigorously for all finite m (unlikely to be simple) or (b) honestly characterize FastLSH as an empirically effective fast LSH heuristic and remove or substantially soften the "provable LSH property" claim. The experiments are strong enough to stand on their own; the paper does not need to overclaim to be a useful contribution.
2. If option (b) is chosen, clearly explain the conditions under which FastLSH approximates the LSH behavior and provide empirical evidence (e.g., monotonicity verification on real data) that the approximation is reliable in practice.
3. Report precision and recall (or F1) for the outlier detection experiments to make the comparison with ACHash even-handed and quantitative.
4. Add a table of per-dataset speedup numbers to the main text.

## Score and Decision

**Originality:** The idea of combining random sampling with random projection for LSH is simple but underexplored; the paper is the first to attempt this combination with a claimed theoretical analysis. Modest originality.  
**Importance of research question:** Reducing the hashing bottleneck in LSH-based applications is practically important and well-motivated.  
**Are claims well supported?** The empirical speedup claims are well supported. The central theoretical claim (provable LSH property) is not.  
**Soundness of experiments:** The experimental design is reasonable, covering three tasks and multiple datasets. Missing precision/F1 for outlier detection weakens the comparison somewhat.  
**Clarity of writing:** Generally clear, though the theoretical section leans heavily on deferred appendix content and the logic from "asymptotic equivalence" to "LSH property" is presented as a given rather than argued.  
**Value to the community:** The method itself is simple and useful, and the empirical results show clear benefits. A properly framed version of this paper would be a valuable contribution.

The paper presents a simple, practical method with strong empirical results, but its central theoretical claim — the "provable LSH property" that is fundamental to the paper's identity and differentiator from prior work — is not supported by the analysis presented. The fatal weakness is that the LSH property requires monotonicity of collision probability in distance for every finite m, and the paper's asymptotic and moment-based arguments do not establish this. This is not a minor gap; it is the paper's claimed headline contribution. The empirical results are valuable and could form the basis of a strong paper after appropriate reframing, but the current submission overclaims beyond what its analysis can support.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>