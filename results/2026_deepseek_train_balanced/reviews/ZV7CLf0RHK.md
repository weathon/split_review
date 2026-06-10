Now I have all the information needed. Let me produce the final review.

## Summary

This paper investigates redundancies in LoRA parameters and proposes PREFT, a post-hoc pruning framework, with a specific instantiation called NORM. NORM uses randomized SVD to decompose LoRA delta weights and a novel Sim-Search procedure that measures subspace similarity (Grassmann distance) between the reduced delta weight and the pre-trained weight to adaptively determine how many components to retain per layer/module. The method is evaluated across general instruction tuning, math reasoning, and code generation tasks on Llama3-8B, Qwen2-7B, and Mistral-7B, showing consistent improvements over LoRA variants and the existing PREFT method TAIA.

## Strengths

1. **Well-designed pilot experiments that reveal the structure of redundancies before proposing the method.** Section 2.2 systematically characterizes redundancies at three levels: holistic (Figure 2a shows even random dropping of 90% of LoRA parameters can improve performance), layer-wise (Figure 2b identifies middle layers as more redundant), and module-wise (Figure 2c shows MLP modules contain more redundancy than attention modules). This empirical foundation directly motivates NORM's adaptive, per-module approach and is a genuine contribution independent of the method itself.

2. **Sim-Search adaptively determines retention ratios per parameter via subspace similarity, avoiding fixed heuristics.** Unlike TAIA (Jiang et al., 2024a), which zeros out all FFN delta parameters, NORM's Sim-Search (Eq. 15: φ_c = ‖U_cr^T · U_r‖_F²/r) automatically selects the optimal number of components c for each LoRA module by measuring Grassmann distance between the reduced delta weight's subspace and the pre-trained weight's subspace. The ablation (Table 3) shows Sim-Search outperforms alternatives including PCA-based, L2-distance-based, and cosine-similarity-based search.

3. **Direct evidence that NORM resolves LoRA's rank-scaling limitation.** Figure 4a shows that while vanilla LoRA's performance peaks at a middle rank and degrades (consistent with the paper's motivation), NORM's performance continues to improve with increasing rank from 8 to 128. This directly validates the core hypothesis — that NORM's redundancy removal enables LoRA to productively use larger ranks.

4. **Mechanistic evidence that NORM reduces pre-training forgetting.** Table 4 shows cross-entropy loss on WikiText-103: LoRA-tuned models exhibit *higher* loss than the base model (indicating forgetting), while NORM-tuned models achieve *lower* loss than both the base model and LoRA. This supports the claim that NORM discards hallucinatory content rather than useful information.

5. **Consistent improvements across diverse tasks, base models, and data scales.** Tables 1–2 show NORM outperforming LoRA, LoRA+, DoRA, MoRA, and TAIA on three base models. RQ4 (Figure 5) shows NORM maintains its advantage from 1K to 330K training samples, demonstrating robustness to data availability.

## Weaknesses

### Fatal
None.

### Major

1. **Dimensional ambiguity in the Sim-Search algorithm specification (Section 3.2) — threatens reproducibility.** The procedure (lines 181–193) reconstructs ΔW_c (rank c, where c < r), then runs random SVD to "compute the major r singular vectors again" (line 181). The random SVD described in Section 3.1 is parameterized by the target rank c (the random matrix Ω ∈ ℝ^{d×c}). If we configure it to return r components from a rank-c matrix, the extra r − c components correspond to zero singular values and are arbitrary nullspace vectors. These are then included in the subspace similarity computation φ_c = ‖U_cr^T · U_r‖_F² / r, where U_cr = U_c[:,:r] ∈ ℝ^{d×r}. The nullspace contributions vary systematically with c (fewer nullspace directions at larger c), potentially biasing the metric. The paper does not specify exactly how many singular vectors are computed from ΔW_c, nor does it analyze whether the inclusion of nullspace components distorts φ_c. This must be clarified — either they compute min(c, r) components and the notation is an indexing issue, or they compute r components and need to justify that the nullspace directions do not distort the search.

### Minor

2. **No variance or statistical reporting for main results.** The pilot experiments (Section 2.2) are averaged over 5 runs, but Tables 1 and 2 report single-point results without standard deviation, confidence intervals, or significance tests. Some claimed margins (e.g., +1.63 over TAIA on Llama3-8B) could fall within run-to-run noise. While single-run evaluation is common in large-scale benchmark papers, the inconsistency with the paper's own pilot-experiment reporting is notable.

3. **Computational cost of the post-processing step is not quantified.** The Sim-Search procedure involves, for each candidate c and each of ~256 LoRA modules (32 layers × 8 modules), running random SVD and computing subspace similarity. The paper claims NORM operates "without sacrificing training and inference efficiency" (line 283). Training efficiency is indeed unchanged (same LoRA training), and inference has zero overhead (parameters are merged). However, the post-processing (SVD + search) is a non-trivial one-time cost that is never measured or reported. A runtime or FLOP measurement would support the practicality claim.

4. **The "hallucination" framing is stated as fact but is a hypothesis.** The abstract (line 5) asserts that LoRA "not only injects knowledgeable features but also noisy hallucination during fine-tuning" as established fact. The evidence is indirect — performance gains after dropping components are consistent with the hypothesis but do not directly measure hallucination in the LoRA parameters. This should be hedged.

5. **Missing direct comparison: NORM (trained at r=64, pruned) vs. LoRA trained directly at the effective post-pruning rank.** The paper shows NORM outperforms LoRA at every rank in Figure 4a (r=8,16,32,64,128), which partially addresses this concern. However, the specific comparison of NORM trained at r=64 (which prunes to a lower effective rank, e.g., c≈32 on average for some modules) against standard LoRA directly trained at that lower rank is not shown, leaving some ambiguity about whether the gains come from the pruning criterion or simply from having more training-time capacity.

6. **Framing of PREFT as a "new fine-tuning framework" (lines 7, 83) is slightly inflated.** PREFT does not modify the training procedure — it is a post-processing compression step applied to already-trained LoRA adapters. This is a valid and useful category (post-hoc adapter pruning), but calling it a "fine-tuning framework" overstates the scope.

7. **Search range description is ambiguous (line 181).** The notation "{τ·s, (τ+1)·s, ..., r}" with τ=0.1 and s=1 is unclear: does this mean c ∈ {0.1, 1.1, 2.1, ..., 64} or β ∈ {0.1, 0.2, ..., 1.0} with c = r·β? The step logic needs clarification.

### Trivial
None.

## Nice-to-Haves
- Reporting the end-to-end post-processing runtime (SVD + Sim-Search) would strengthen the practical efficiency claim.
- A limitations discussion (e.g., requiring access to pre-trained weights' SVD, the search being per-module, potential sensitivity to distribution shift) would improve completeness.
- The notation for the search range and the dimensional indexing in Sim-Search could be made more explicit (a pseudocode block would help).

## Removed Points
The following points from the reviews were assessed and removed:
- **"No limitations section"** — This is not standard practice for all conference papers; many top papers do not include a separate limitations section. Not a substantive weakness.
- **"Random SVD adds an extra approximation layer on top of LoRA"** — The random SVD is a computational optimization to efficiently compute the SVD of ΔW, not an additional source of approximation beyond what LoRA already introduces. The critic misunderstood the role of random SVD.
- **"No code provided for NORM"** — Standard for double-blind submissions; code release is expected upon publication, not during review.
- **"Should include comparison at more typical rank (r=16 or r=8)"** — The paper already evaluates NORM at ranks 8, 16, 32, 64, 128 in RQ1 (Figure 4a, Table 6), fully addressing this.
- **"The method assumes that subspace similarity is the right criterion..."** — This is an area-of-concern sweep without a specific problem identified in the paper.
- Several generic or speculative concerns from the harsh critic that could not be anchored to specific content in the paper.

## Novel Insights
The most interesting observation emerging from the reviews is the potential tension between NORM's two stated rules (line 178–179): maximizing both "contribution" (largest singular values) and "subspace similarity with pre-trained weights." The paper's Sim-Search only optimizes the second criterion (max φ_c), but the first rule (selecting the most contributive c components) is implicitly handled by truncating the SVD before searching for c. Whether these two criteria are aligned or in conflict is not analyzed — exploring cases where the top-c components have low subspace similarity (and whether the method would handle this correctly) would sharpen the paper's theoretical framing.

## Suggestions
1. Clarify the Sim-Search algorithm precisely: (a) state exactly how many singular vectors are computed from ΔW_c in each iteration, (b) address whether the r−c nullspace components (if computed) could bias φ_c, and (c) provide the exact search range formula (e.g., c ∈ {⌊r·β⌋ | β ∈ {0.1, 0.2, ..., 1.0}}).
2. Add standard deviations or confidence intervals to the main tables, at least for a representative subset of benchmarks.
3. Report the wall-clock time for the NORM post-processing pipeline (SVD decomposition + Sim-Search across all modules) to support the efficiency framing.
4. Hedge the "hallucination" claim by framing it as a hypothesis supported by the evidence, rather than an established fact.
5. Add a direct comparison: train LoRA at the average post-pruning effective rank of NORM and compare performance, to complement the rank-sweep evidence in Figure 4a.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>