Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes SqueezeAttention, a method for layer-wise KV-cache budget reallocation during LLM inference. The key insight is that attention layers differ in importance (measured by cosine similarity of hidden states before/after self-attention), so cache budgets should be reallocated: unimportant layers get fewer tokens while important layers get more. SqueezeAttention is designed as a plug-in on top of existing sequence-wise eviction policies (H2O, Sliding Window, StreamingLLM). Experiments across 7 models (7B–70B) and 5 datasets show memory reductions of 30–80% and throughput improvements up to 2.2× over full cache, with only 6.3% prefilling overhead.

## Strengths

- **Novel 2D optimization dimension**: The paper identifies a genuine gap—prior work compresses KV-cache along the sequence dimension while treating all layers equally. SqueezeAttention introduces a complementary layer-wise budget reallocation that is orthogonal to existing methods (Section 4, Algorithm 1). This is a principled addition to the KV-cache optimization toolbox.

- **Consistent empirical gains across diverse settings**: SqueezeAttention improves accuracy or achieves equivalent accuracy at lower total cache budgets compared to the best per-task baseline, demonstrated across 7 models (7B–70B) and 5 datasets including long-context benchmarks (Section 5.2, Figure 3). Memory reductions per token reach 25–66% over baseline methods (Figure "efficiency result"), and throughput improves up to 2.2× over full cache (Table "throughput result").

- **Low and one-time overhead**: The cosine similarity and KMeans computations occur only during the prefilling phase, adding just 6.3% to prefilling time for Mistral-7B (Table "overhead"). Since this is a fixed cost per prompt independent of generation length, it is negligible in practice.

- **Insightful layer-importance observations**: The cosine similarity analysis across 4+ models (Section 3, Figures 1–2) reveals consistent patterns—first half of layers contributes more, first and last few layers are especially important—which align with prior findings from early-exiting and FastGen, providing a simple, interpretable metric for budget allocation.

- **Clear algorithmic description**: Algorithm 1 provides a complete, step-by-step procedure with the budget redistribution formula and hyperparameter \(p\) discussion (Section 4.2), making the method reproducible.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Main accuracy comparison (Figure 3) only shows the "best" baseline per task, not all baselines.** The paper selects the best sequence-wise compression algorithm per task and compares SqueezeAttention+best vs. best alone. While this is transparent and the total budget is conserved (so improvement genuinely comes from reallocation, not from budget differences), it does not demonstrate whether SqueezeAttention consistently improves *all* sequence-wise methods on the same task. Since the paper claims orthogonality ("can be smoothly combined with any"), showing results for SqueezeAttention applied to each of the three baselines on each task would substantially strengthen this claim. The paper uses all three baselines across different experiments (Table "accuary result"), but not all on the same task for direct comparison.

2. **Clustering stability and sensitivity are not analyzed.** The entire budget reallocation hinges on KMeans clustering of layers into 3 groups based on per-prompt cosine similarity. The paper provides qualitative justification for \(k=3\) (Section 4.2) but reports no stability analysis: no assessment of how cluster assignments vary with different random seeds, across different prompts from the same dataset, or with alternative \(k\) values (2 or 4). A sensitivity analysis would confirm that the groupings are robust and that performance does not hinge on a fragile clustering step.

3. **Hyperparameter \(p\) sensitivity is only referenced to the appendix.** The main text states that \(p=0.3\)–\(0.4\) is "a reasonable choice range in most cases" and defers a detailed study to the appendix (which is not available in this review). Given that \(p\) directly controls how much budget is removed from Group 3, a sensitivity curve in the main paper would help readers assess the method's robustness.

4. **No variance or statistical significance reported for accuracy results.** Generative evaluation metrics (ROUGE, F1) on small sample sizes (200–1000 samples per dataset) can exhibit non-negligible variance. The absence of standard deviations or multiple-run statistics makes it difficult to gauge whether observed improvements are statistically meaningful, especially in cases where margins appear small.

5. **Abstract says "categorize the layers into two groups" but the algorithm uses three groups.** The algorithm (Algorithm 1) and Section 4.2 clearly describe three groups, with Group 1 being special layers that are always preserved. The abstract's phrasing is slightly imprecise; this should be corrected for consistency.

### Trivial
- The column headers in Table "accuary result" use "w/ \sys" and "w/o \sys" without clear explanation of which refers to SqueezeAttention vs. baseline. (The paper's text clarifies this, but the table header could be more self-explanatory.)
- The throughput comparison between SqueezeAttention and baselines is referenced to the appendix; including a summary in the main paper would improve self-containedness.

## Nice-to-Haves

- **Throughput comparison against baselines (not just full cache)** in the main paper. The paper references this comparison in the appendix. Including at least a summary (e.g., a sentence or small table) in the main text would better isolate the contribution of layer-wise reallocation from the benefit of cache reduction alone.
- **Clustering stability analysis**: reporting cluster assignments across multiple random seeds or across different prompts from the same dataset would strengthen confidence in the grouping.
- **Larger model overhead measurement**: the overhead analysis is only for Mistral-7B; measurements for 20B–70B models at longer prompt lengths would be useful.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Throughput results only compare against Full Cache, not against baselines"** — The paper explicitly states "The throughput comparison between best baseline and SqueezeAttention is reported in \ref{throughput comparison between best baseline and squeezeattention}," which is in the appendix. Per the rules, weaknesses about missing appendix content are removed because the parser strips those sections.

2. **"Flawed baseline comparison — cherry-picking" characterization as a fatal/structural flaw** — The paper is transparent about selecting the best baseline per task, and the total KV-cache budget is conserved (Algorithm 1 guarantees this). The comparison is between equal total budgets. The weakness is retained above but downgraded to Minor since it does not invalidate the core claim.

3. **"FastGen 'first' claim is overstated"** — The paper already acknowledges FastGen (Section 1, Section 2.2) and correctly distinguishes that FastGen selects per-layer *strategies* with unified budgets, while SqueezeAttention addresses *budget allocation*. The paper's claim of being "first" for budget reallocation specifically is accurate.

4. **"Cosine similarity as heuristic not rigorously validated"** — The paper explicitly frames this as an intuitive assumption ("The intuition is that...") and provides multiple validation signals (heatmap alignment with early-exiting/FastGen findings). This is appropriate for the paper's scope.

5. **"Hyperparameter p clarification needed"** — Algorithm 1 clearly specifies the budget formula. The interaction between \(p\) and \(b_{init}\) is deterministic and well-defined.

6. **"30–70% memory reduction not tied to specific conditions"** — Table "accuary result" and Figure "efficiency result" provide specific numbers (20–30% of full cache used, 70–80% reduction) under specific experimental conditions. The abstract gives a general range, which is standard practice.

## Novel Insights

The paper demonstrates that layer importance during inference can be cheaply approximated by cosine similarity of hidden states before/after self-attention, and that this signal is sufficient to drive meaningful budget reallocation. The observation that the first and last few layers are consistently more important (aligning with early-exiting literature) while middle layers can tolerate heavier compression is not entirely novel in isolation, but the paper's contribution is in using this signal for *on-the-fly budget allocation* rather than for early exiting or strategy selection. The key insight is that the 2D view (sequence × layer) of KV-cache compression is both necessary and actionable with minimal overhead.

## Suggestions

1. **Show SqueezeAttention combined with each of the three baselines on at least one representative task** (e.g., on Mistral-7B with CNN/DailyMail). This would directly demonstrate orthogonality and allow readers to see whether the improvement is consistent across policies.
2. **Add a brief clustering stability analysis** (e.g., cluster assignments across 5 random seeds for one model/dataset) and a sensitivity curve for \(k\) (2, 3, 4) in the main paper.
3. **Report standard deviations** for the key accuracy results (Figure 3) or at least acknowledge variance for the smaller datasets (200 samples).
4. **Include a summary of the throughput comparison vs. baselines** (currently in the appendix) in the main text.

## Score and Decision

The paper presents a novel, well-motivated, and practical idea for layer-wise KV-cache budget allocation. The core contribution—identifying that layers differ in importance and reallocating budgets accordingly—is clearly articulated and backed by reasonable experiments across diverse models and tasks. The weaknesses are addressable (adding comparisons against all baselines, clustering stability analysis) and do not undermine the central claim. The paper is a solid contribution to the KV-cache optimization literature.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>