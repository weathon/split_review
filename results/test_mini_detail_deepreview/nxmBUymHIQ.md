Now I'll write the consolidated review.

## Summary

The paper proposes LoLoRA, a method that combines local unsupervised Hebbian PCA updates for the LoRA down-projection matrix A with standard gradient-based updates for the up-projection matrix B. By updating A on the forward pass using only layer inputs, LoLoRA avoids storing activations for backpropagation through A, reducing memory at the cost of extra local optimizer states. The paper provides theoretical analysis (Theorem 4.4) showing that under random regression assumptions, optimal A spans the principal eigenspace of the input covariance matrix—the same subspace HPCA converges to. Experiments span GLUE (RoBERTa-large), MathQA → GSM8K (LLaMA-3.1-8B), LLaVA fine-tuning, and ablations on TinyLlama.

## Strengths

- **Theoretical characterization of optimal A**: Theorem 4.4 proves that under a random regression model, the optimal frozen A matrix must have row space equal to the top-r eigenspace of the input covariance matrix, and that any nonsingular transformation of those eigenvectors is equally optimal. This provides a principled justification for PCA-based initialization (EVA) and for using Hebbian PCA updates that converge to the same subspace. The asymmetry result (Theorems 4.4 vs 4.5) showing that any full-rank B yields the same expected loss, while A has a constrained optimal set, is a genuine theoretical contribution that goes beyond prior empirical observations (Zhu et al., 2024).

- **Demonstrated memory reduction on MathQA**: Table 3 shows LoLoRA HPCA on LLaMA-3.1-8B reduces peak extra GPU memory from 30 GB (standard LoRA) to 26 GB (≈13% reduction) while achieving the highest GSM8K accuracy (82.9%, tying LoRA-FA (EVA) and 0.8 pp above standard LoRA). This is the paper's most compelling evidence for a favorable memory–performance trade-off.

- **Robustness across local update rules**: Table 6 ablates five local update rules (HPCA, AE, HPCA no mean, SoftHebb, HPCA svd first) and shows that all methods converging to the PCA subspace yield nearly identical validation perplexities (within 0.018–0.014 of full LoRA). This demonstrates the method is not brittle to the specific local rule choice.

## Weaknesses

### Fatal
None.

### Major

1. **The "comparable to standard LoRA" claim in the abstract is contradicted by GLUE results.** On GLUE (Tables 1–2), LoLoRA shows non-trivial degradation on several tasks relative to standard LoRA: CoLA 66.3 vs 69.6 (−3.3, >2 SE), MRPC 89.9 vs 90.9 (−1.0), QQP 90.6 vs 91.7 (−1.1). The paper's summary honestly states "classical LoRA remains the strongest overall," but the abstract says performance is "comparable to standard LoRA." This framing mismatch weakens the paper's central promise: a method that saves memory while maintaining LoRA-level performance.

2. **LoLoRA does not consistently outperform the simpler LoRA-FA with EVA initialization**, which also saves activation memory by freezing A. Across the three major experiments: (a) On GLUE, LoLoRA (avg rank across 8 tasks ≈90.4) and LoRA-FA (EVA) (≈90.1) are comparable, with neither clearly dominating. (b) On MathQA (Table 3), both achieve 82.9% accuracy—exactly tied. (c) On LLaVA (Table 4), LoRA-FA (EVA) achieves perplexity 2.92 vs LoLoRA's 2.93, with lower memory (23.9 GB vs 24.1 GB). The advantage of online HPCA updates over a well-initialized frozen A is not empirically demonstrated. When a simpler baseline achieves equal or better results at equal or lower memory cost, the paper's contribution claim is undermined.

### Minor

3. **No memory breakdown by component.** The paper reports peak extra GPU memory but does not decompose it into activations, optimizer states, and parameters. LoLoRA introduces extra optimizer state (momentum, variance for A via AdamW) that LoRA-FA does not have. Without a breakdown, it is impossible to assess how much memory is genuinely saved by the local update trick versus how much is consumed by the new optimizer states. The advertised "up to 20%" memory reduction (GLUE summary) references Appendix D which is not included in the main text; the only concrete numbers in the main paper are 13% (MathQA) and 2% (LLaVA).

4. **Theory–practice gap is acknowledged but significant.** Theorem 4.4 relies on strong assumptions (i.i.d. Gaussian ΔW entries, isolated submodules with stationary targets). The actual method operates in a dynamic, non-stationary setting where both A (via HPCA) and B (via backprop) are updated simultaneously. The paper acknowledges this limitation in the Conclusion, but the acknowledgment does not bridge the gap—the theory justifies EVA-style initialization (which the paper does not claim to improve upon), not the online HPCA procedure that is the paper's core algorithmic novelty.

5. **Standard errors in Table 6 are suspiciously uniform.** For r=2, all five LoLoRA variants report exactly ±0.011 SE. For r=4, all report ±0.011. For r=8, all report ±0.011 except SoftHebb (±0.012). The full LoRA baselines show different SE values (0.012–0.013). This pattern suggests either too few independent runs to produce meaningful variance estimates, or rounding that obscures differences.

### Trivial
None.

## Nice-to-Haves

- A **distribution-shift experiment** (e.g., sequential fine-tuning on two different domains) would directly test the "adapt to input distribution shifts" claim made in the abstract and introduction, offering a scenario where online HPCA should clearly outperform a frozen A.
- A **gradient alignment analysis** measuring cosine similarity between the HPCA update direction for A and the gradient-based update direction that would be used in standard LoRA could help explain why local updates do not interfere with B's gradient-based learning.
- Comparing convergence speed (e.g., loss curves or accuracy at intermediate checkpoints) across methods would strengthen the evaluation, especially since faster convergence was one of EVA's claimed advantages.

## Removed Points

The following criticisms from the input reviews were removed or demoted after cross-checking against the paper:

1. *"The local rule is only specified as LocalRule(A, z, u) without definition"* — The paper defines the HPCA/SNL algorithm in Section 3.3 (citing Oja, 1989) and elaborates in Section 5.4. The algorithmic placeholder is standard for readability. **Removed.**

2. *"Missing baseline VeRA or other parameter-sharing methods"* — Per protocol, missing related works concerns cannot be raised. **Removed.**

3. *"Perplexity is not defined in relation to generation quality; a human evaluation would be more meaningful"* — Perplexity is a standard metric for language model validation. Requesting human evaluation is scope creep. **Removed.**

4. *"One-epoch best-of-checkpoints selection can inflate results"* — All methods use the same evaluation protocol; the comparison is fair. **Removed.**

5. *"The analysis should test models beyond 7B parameters"* — The paper tests 8B (LLaMA-3.1-8B) which is near the frontier for single-GPU fine-tuning. This is a standard scale for the setting. **Removed.**

6. *"The paper should include comparisons with full fine-tuning"* — The paper's scope is comparing LoRA variants, not full fine-tuning. **Removed.**

7. *Strengths from Strength Finder that are generic or conflict with verified weaknesses: "The method addresses an important problem"* — generic. **Removed.**

## Novel Insights

The most interesting finding is not that LoLoRA outperforms baselines (it largely doesn't), but that **all local update rules converging to the principal subspace perform nearly identically** (Table 6), and that HPCA from random initialization works as well as HPCA with SVD pre-initialization. This suggests the principal subspace is the key object, not the specific algorithm used to reach it. Combined with the theory, this provides strong evidence that the optimal A in LoRA is genuinely constrained to the top input eigenspace under reasonable stochastic assumptions—a finding that could guide future LoRA initialization and update strategies regardless of the specific method used. The asymmetry result (A has a constrained optimal set, B does not) is also a clean theoretical insight that complements prior empirical observations.

## Suggestions

1. Reframe the contribution more precisely: the paper shows that online PCA updates for A are feasible and save memory, but the method does not consistently outperform a well-initialized frozen A. The abstract should match this characterization rather than claiming "comparable to standard LoRA."

2. Add a memory breakdown table showing activations vs. optimizer states for LoRA, LoRA-FA, and LoLoRA across the three main experiments. This would allow practitioners to weigh the actual trade-offs.

3. Run a distribution-shift experiment (e.g., train on two sequentially presented datasets) to demonstrate the claimed adaptation advantage.

4. Run more independent seeds for the ablation experiments (Table 6) to confirm the variance estimates are reliable.

## Score and Decision

**Round-1 bracketing**: The paper sits between weak anchors (~3.0 avg, typical of rejected methods with clear flaws or trivial contributions) and strong anchors (~8.0 avg, accepted papers with substantial advances). The most relevant middle-band anchors are LoRA-FA (5.33, reject), EVA (4.75, reject), and EigenLoRA (5.00, reject).

**Round-2 narrowing**: Comparing directly:
- **EVA (4.75)**: LoLoRA is more novel (online updates vs. one-shot initialization) and provides the theoretical justification EVA was criticized for lacking. LoLoRA is stronger.
- **LoRA-FA (5.33)**: LoLoRA is more novel than simply freezing A but has weaker empirical support—LoRA-FA's claims of "close accuracy" held more consistently across settings. Roughly comparable quality.
- **EigenLoRA (5.00)**: Both propose subspace-based improvements to LoRA with theory support. LoLoRA's theory is tighter, but both have empirical gaps. LoLoRA is slightly stronger.
- **ReLoRA (5.75, accepted)**: ReLoRA addresses a more ambitious problem (high-rank training via low-rank updates) with clearer empirical validation. LoLoRA is notably weaker.

The paper's genuine theoretical contribution and novel method are held back by overstated claims, modest memory savings, and the lack of a clear empirical advantage over the simpler LoRA-FA (EVA) baseline.

**Final score**: 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>