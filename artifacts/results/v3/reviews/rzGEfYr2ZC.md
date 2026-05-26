## Summary

This paper proposes SparseFW, a layerwise LLM pruning method that relaxes the combinatorial mask selection problem into a convex program over the convex hull of binary masks and solves it with the Frank-Wolfe (FW) algorithm. The method is warm-started from a Wanda or RIA mask, fixes 90% of the highest-saliency weights as unprunable, and optimizes the remaining 10% via FW. SparseFW reduces the per-layer reconstruction error by up to 80% and shows modest improvements in perplexity and zero-shot accuracy across multiple modern GPT architectures at higher sparsity levels (60%, 2:4), while providing theoretical approximation guarantees and a memory-efficient implementation.

## Strengths

1. **Substantial reduction in per-layer pruning error (Figure 2).** SparseFW achieves up to 80% relative reduction in the layerwise reconstruction error compared to the Wanda warm-start across all layers of LLaMA-3.1-8B. This directly demonstrates that the convex relaxation captures weight-interaction effects that greedy single-weight heuristics miss at the local optimization level.

2. **Memory-efficient and scalable implementation (Section 2.3).** By precomputing the Gram matrix \(G = XX^\top\) and \(H = WG\) once per layer, the per-iteration cost of Frank-Wolfe becomes independent of the sequence length and number of calibration samples. This enables scaling to models up to 14B parameters with modest memory overhead — a genuine engineering contribution.

3. **Theoretical approximation guarantee (Lemma 1, Section 4).** The paper provides an explicit error bound for the rounded binary mask relative to the true combinatorial optimum, decomposing the gap into an optimization term that shrinks as \(O(1/T)\) and a thresholding term. No competing mask-selection method (Wanda, RIA) offers a comparable guarantee.

4. **Transparent treatment of the method's key limitation (Section 2.3, Conclusion).** The paper openly reports that full FW (\(\alpha=0.0\)) fails, that the method requires fixing 90% of weights from the greedy warm-start, and that the local–global objective mismatch persists. This candor is valuable even though it undercuts the paper's own framing.

5. **Consistent accuracy gains at higher sparsities (Table 1).** For 60% and 2:4 sparsity, SparseFW improves zero-shot accuracy over both Wanda and RIA warm-starts in nearly every configuration across five model families (Gemma-2-9B, Yi-1.5-9B, DeepSeek-7B, Qwen2.5-7B, LLaMA-3-8B/14B).

## Weaknesses

### Major

1. **The "Don't Be Greedy" framing is contradicted by the method's reliance on a greedy warm-start.** The paper's central narrative is that greedy heuristics (Wanda, RIA) are suboptimal because they ignore weight interactions, and that the convex relaxation solved via FW accounts for such interactions and yields superior masks. However, Section 2.3 concedes that pure FW (\(\alpha=0.0\)) *consistently yields worse results than the baselines*, and the practical algorithm requires fixing 90% of the weights to the outcome of the greedy Wanda heuristic. The method that "accounts for interactions" is *worse* than the method that "ignores interactions" unless it is forced to match the greedy baseline on nine out of ten weight decisions. The paper acknowledges this, but the persistent "Don't Be Greedy, Just Relax" framing, the title, and claims like "classical constrained optimization is a scalable and effective alternative to greedy heuristics" (Conclusion) remain in direct tension with the experimental findings. The contribution is better described as a marginal correction to a greedy heuristic rather than a new pruning paradigm.

2. **SparseGPT — the dominant LLM pruning method — is excluded from comparison.** The paper states it "do[es] not compare directly to methods that involve a reconstruction step, such as SparseGPT" (Section 3). SparseGPT is the de facto standard in post-training LLM pruning, widely used by practitioners and cited by the paper itself as the "most popular approach." The distinction between "mask selection" and "mask + reconstruction" is one the field does not observe when evaluating final model quality. Without this comparison, the abstract's claim of "outperform[ing] strong baselines on state-of-the-art GPT architectures" is unsubstantiated. A paper claiming practical SOTA relevance must include SparseGPT, or at minimum discuss how its performance profile relates to it.

### Minor

3. **Final-task gains are modest and inconsistent.** The perplexity improvements are mixed: at 50% sparsity on LLaMA-3-8B, SparseFW(Wanda) yields *worse* perplexity than plain Wanda (10.21 vs. 10.09). The zero-shot accuracy deltas are often within noise (e.g., Gemma-2-9B at 2:4: 63.81 vs. 63.75). The paper's phrasing "drastically reduces" and "strong empirical performance" (Abstract, Introduction) overstates what the final task metrics support. The 80% reduction in per-layer error (Figure 2) does not translate to proportionally large final-task gains, which the paper acknowledges as a local–global objective mismatch — but the rhetorical framing does not reflect this caution.

4. **No error bars or statistical significance are reported.** Table 1 notes "we omit standard deviations for legibility" without providing them elsewhere. Given the small and often noisy deltas, standard deviations (or confidence intervals) are essential for assessing whether the improvements are meaningful rather than random variation.

5. **The theoretical bound (Lemma 1) is disconnected from the actual working algorithm.** The bound applies to the relaxation solved by FW plus rounding, but does not explain why the unconstrained FW fails or why the \(\alpha=0.9\) heuristic is necessary. It provides no insight into the local–global objective mismatch that is empirically the central challenge of the method. This reduces the practical value of the theory.

### Trivial

6. Table 1 caption states "we omit standard deviations for legibility" — this information belongs in the main text or appendix, not merely as a caption note.
7. The bound in Lemma 1 is stated as informal; the full statement is deferred to the appendix, making it hard to assess the tightness of the constants during review.

## Nice-to-Haves

- A comparison with SparseGPT, even if apples-to-oranges on "mask selection only," would dramatically strengthen the practical relevance. The paper could compare SparseFW + a simple weight reconstruction step (e.g., the optimal reconstruction given the mask) against SparseGPT's joint selection+reconstruction.
- An analysis of *why* the convex relaxation's solution is misaligned with final perplexity — i.e., what property of the local \(L_2\) proxy causes it to prune the wrong weights even when the per-layer error is minimized — would be more insightful than the current theoretical bound.
- Standard deviations or a statistical test (e.g., paired bootstrap over calibration samples) for the main results in Table 1.

## Removed Points

These points were flagged by the harsh critic but removed after verification against the paper:

- *"Fatal structural flaw: method contradicts its own motivation"* — Kept as **Major** (not Fatal) because the paper is transparent about the limitation and the refinement on 10% of weights still produces useful gains. The paper's transparency (Section 2.3, Conclusion) prevents this from being a fatal issue; the core claim is merely overstated, not invalid.
- *"Theoretical results are generic"* — The lemma is a standard convex relaxation bound, but it is the only theoretical guarantee among mask-selection methods. Kept as Minor #5.
- *"Writing quality and formatting nitpicks"* — Removed per instructions; parser artifacts are not author errors.
- *"Missing related work"* — Cannot verify without external sources; removed per instructions.
- *"Reproducibility concerns about unreleased code"* — The paper states code will be released; removed per Hard Rules about questioning availability.

## Novel Insights

None beyond the paper's own contributions. The central insight — that the mask selection problem can be relaxed to a convex program over the convex hull of binary masks and solved with Frank-Wolfe — is clearly articulated by the authors. The honest documentation of why this relaxation fails without heavy warm-start regularization (the local–global objective mismatch) is itself an interesting finding, though the paper treats it as a caveat rather than a main result.

## Suggestions

1. **Reframe the contribution honestly.** The paper's empirical finding is that greedy heuristics are approximately correct for ~90% of weight decisions, and that convex optimization can provide a small but consistent refinement on the remaining tail. The title, abstract, and introduction should reflect this rather than the current "greedy vs. relaxation" dichotomy.
2. **Add SparseGPT results.** Even a separate column showing SparseGPT's perplexity/accuracy at the same sparsity levels would allow readers to situate the method in the literature. If the computational cost of running SparseGPT is prohibitive, cite published numbers from the SparseGPT paper at comparable sparsities.
3. **Report standard deviations** for the main results, or at minimum include a multi-seed analysis for one representative setting (e.g., LLaMA-3-8B at 60% sparsity) to establish that the improvements are statistically reliable.
4. **Investigate the local–global mismatch.** The paper identifies that per-layer \(L_2\) error reduction does not reliably improve perplexity. An analysis of *when* and *why* this happens (e.g., do certain layers or weight types correlate with the mismatch?) would significantly strengthen the paper's scientific contribution.

## Score and Decision

**Round-1 bracket:** 3.5–5.5 (topic-mid anchors averaged 4.8–5.25; weakness-anchored FISTAPruner at 5.25).  
**Round-2 narrowing:** FISTAPruner (5.25, rejected) is the closest comparator — it also uses convex optimization for LLM pruning — but the paper under review is weaker: it lacks a SparseGPT comparison and has an additional structural tension (α=0.9) that FISTAPruner does not. The paper shares comparison-set problems with the 3.00 CVXQ anchor (missing key baseline).  
**What low-band anchors failed at:** The 3.00 CVXQ was penalized for unfair/omitted comparisons and lack of practical grounding. The paper under review shares the missing-baseline problem (SparseGPT). It is stronger than CVXQ on clarity and motivation, but the α=0.9 issue prevents it from reaching the 5.0+ rejection range of FISTAPruner.  
**Final position:** 4.0 — below FISTAPruner (5.25) due to the α=0.9 problem and missing SparseGPT, but above generic low-band (3.0) due to clear contributions in theory, engineering, and transparency.

**Score:** The paper has genuine contributions (clean theoretical framing, efficient implementation, transparent reporting of its key limitation) but the core weakness — that the method depends on preserving 90% of a greedy heuristic's decisions to work at all — fundamentally undermines the "relaxation beats greediness" narrative, and the omission of SparseGPT leaves the practical claims unvalidated. The improvements over baselines are real but modest and inconsistent. Major restructuring and honest reframing, plus a SparseGPT comparison, would be needed before the work would be ready for publication.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>