Now I have the paper and calibration anchors. Let me construct the final consolidated review.

---

## Summary

This paper proposes LoLoRA, a LoRA variant that replaces backpropagation-based updates of the low-rank adapter matrix *A* with local unsupervised Hebbian PCA updates computed during the forward pass. This avoids storing input activations for *A*'s backward pass, reducing memory relative to standard LoRA. The authors provide a theoretical derivation (Theorem 4.4) showing that under a random regression assumption, the optimal *A* matrix spans the principal eigenspace of the input covariance, and they evaluate the method across NLU (RoBERTa-large on GLUE), mathematical reasoning (LLaMA-3.1-8B on MetaMathQA), multimodal instruction tuning (LLaVA-v1.5-7B), and ablations on TinyLlama-1.1B.

## Strengths

1. **Principled theoretical derivation of the optimal A subspace.** Theorem 4.4 provides an exact characterization of the set of optimal *A* matrices under a random regression model, proving they must span the top-*r* principal eigenspace of the input covariance. While the random regression assumption is stylized, the derivation is mathematically clean and connects to the broader line of work on informed LoRA initialization.  
   *Evidence: Section 4, Theorem 4.4, Equations (i)–(iii).*

2. **Memory reduction relative to standard LoRA on a reasoning benchmark.** On LLaMA-3.1-8B fine-tuned on MetaMathQA, LoLoRA HPCA achieves 0.829 accuracy on GSM8K Platinum — matching the best LoRA-FA variant — while using 26 GB peak extra memory versus 30 GB for standard LoRA, a 13% reduction.  
   *Evidence: Table 3, Section 5.2.*

3. **Thorough ablation study validating that only PCA-convergent local rules are effective.** Table 6 compares five local update rules across ranks 2, 4, and 8 on TinyLlama-1.1B/Alpaca. All rules that converge to the PCA subspace (HPCA variants, AE) achieve nearly identical best perplexities, while SoftHebb, which does not converge to that subspace, is consistently worse. This cleanly validates the theoretical link between the PCA subspace and effective *A*.  
   *Evidence: Table 6, Section 5.4.*

4. **Formal asymmetry result for adapters A and B.** Theorem 4.5 proves that under the same random model, any full-rank *B* yields the same expected loss, theoretically justifying why initialization and local updates can be focused exclusively on *A* without symmetric treatment of *B*.  
   *Evidence: Section 4, Theorem 4.5.*

## Weaknesses

### Major

1. **LoLoRA does not clearly outperform the simpler LoRA-FA baseline with good initialization.** The paper's central claim is that local HPCA updates improve upon freezing *A* (LoRA-FA). Across all four experimental settings, the evidence is at best mixed:  
   - **GLUE (Tables 1–2):** LoLoRA HPCA performs *worse* than LoRA-FA (uniform) on multiple tasks (CoLA: 66.3 vs 67.9; RTE: 84.6 vs 86.4; SST-2: 96.4 vs 96.7) and is statistically tied on the rest.  
   - **Math reasoning (Table 3):** LoLoRA HPCA (0.829) ties LoRA-FA (EVA) (0.829) and is within one standard error of LoRA-FA (uniform) (0.826).  
   - **LLaVA (Table 4):** LoLoRA HPCA (perplexity 2.93) is better than LoRA-FA (uniform) (2.97) but *worse* than LoRA-FA (EVA) (2.92).  
   - **Ablations (Tables 5–6):** EVA initialization alone (LoRA-FA) achieves perplexities (e.g., 2.558 at r=2) as good as any HPCA variant (best 2.557).  
   The paper's own conclusion — "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" — is selective: it requires defining "standard" as uniform initialization while ignoring the EVA baseline, and even then GLUE contradicts the pattern. The practical takeaway is that a single offline PCA initialization (EVA) followed by freezing achieves essentially the same results as iterative local updates, making the additional complexity of online HPCA updates difficult to justify.

2. **The theoretical framework does not justify *online* updating of A during fine-tuning.** Theorem 4.4 characterizes the optimal *A* under a random regression model where the target ΔW₀ has i.i.d. Gaussian entries — this is fundamentally an *initialization* result, not a justification for iterative local updates during training. Theorem 4.6 shows that HPCA/AE converge to the PCA subspace, but the experiments show that one-shot PCA initialization (EVA, then freeze) already reaches the same subspace and achieves the same performance. The random regression model (Assumption 4.1) removes all structure (sparsity, alignment with pre-training, cross-layer dependencies) that characterizes real fine-tuning, so the theorem provides a heuristic rather than a guarantee that online updates are beneficial. The paper does not establish why iterating toward the PCA subspace during training should improve upon simply *being in* that subspace from initialization.

### Minor

3. **Memory savings are comparable to LoRA-FA, not strictly better.** The abstract states that LoLoRA "further reduc[es] the memory required for fine-tuning," but this claim is relative to standard LoRA, not to LoRA-FA — the main baseline. In Table 3, LoLoRA uses the same 26 GB as LoRA-FA. In Table 4, LoLoRA uses 24.1 GB vs LoRA-FA's 23.9 GB (slightly *more*). The local updates require additional optimizer states for *A* (acknowledged in the conclusion but not in the abstract or introduction), which offsets any memory advantage. The memory benefit over standard LoRA is real, but it is shared with LoRA-FA; LoLoRA does not improve upon LoRA-FA's memory footprint.

4. **LoLoRA never outperforms fully-trained LoRA.** Table 6 shows that Full LoRA consistently outperforms all LoLoRA variants (e.g., 2.521 vs 2.535 at r=8). This is expected, but it means the method's practical appeal depends entirely on matching LoRA-FA (EVA) with less preprocessing — a narrow advantage that is not discussed clearly.

5. **Best-checkpoint reporting on math reasoning inflates variance.** Table 3 reports the best validation checkpoint during training rather than the final metric. This makes comparisons across methods less reliable and differs from standard practice in the fine-tuning literature.

### Trivial

6. The local HPCA update uses a smoothing factor of 0.98 and an unnamed learning rate (Algorithm 1, line 2–4), but the paper does not state whether these hyperparameters required tuning or were fixed across all experiments.

## Nice-to-Haves

- A combined table directly comparing LoLoRA vs LoRA-FA (EVA) at identical ranks would make the lack of improvement (or its modest magnitude) more transparent. Currently the comparison must be pieced together across Tables 5 and 6.
- Reporting the memory breakdown (base model, activations, optimizer states for *B* and *A* separately) would clarify exactly where the 0.2 GB extra in Table 4 comes from and make the overall memory claims more precise.
- Ablations at higher ranks (r=16, r=32) would test whether the local-update advantage grows with rank, which would strengthen the method's case.

## Removed Points

*These points were flagged for removal by the filtering rules. They are included here for traceability but should not be weighed in the final evaluation:*

- The harsh critic's phrasing that LoLoRA is "worse on 5 of 8 GLUE tasks" — several of those differences (MNLI, QQP, SST-2) are within one standard error. The essential content (LoLoRA does not clearly outperform LoRA-FA on GLUE) is preserved in Weakness 1.
- The criticism about "memory benefit over LoRA-FA is essentially zero" — the paper's primary memory claim compares to standard LoRA, not to LoRA-FA. Re-framed as Minor Weakness 3.
- Criticisms about missing appendix content, missing code release, reproducibility of unreported hyperparameters, and formatting/typo issues — these are either parser artifacts, outside scope, or would be addressed by standard rebuttal/camera-ready polish.
- Speculative weaknesses about hyperparameter sensitivity and impracticality — no evidence that tuning was burdensome is presented by either reviewer.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension — a clean theoretical motivation that, empirically, the online component is unnecessary — but this is essentially the gap between Theorem 4.4 (optimal initialization) and the observation that fixing *A* at that initialization already works.

## Suggestions

1. **Re-center the paper's contribution.** The iterative HPCA update does not improve over EVA initialization in practice. The paper would be more honest and more impactful if it reframed the contribution as: (a) a theoretical justification for PCA-based *A* (Theorem 4.4), (b) a demonstration that local PCA-convergent rules during fine-tuning empirically match offline PCA initialization, and (c) the practical convenience of not needing a separate PCA pre-pass. The current framing overclaims.

2. **Directly compare LoLoRA vs LoRA-FA (EVA) in a single table** at identical ranks on the same setting, and explicitly discuss why (or whether) the online updates add value.

3. **Clarify the memory comparison.** Report a full memory breakdown (model weights, activations, optimizer states for *B* and *A*) so it is transparent where the 0.2 GB overhead comes from and why LoLoRA is not strictly more memory-efficient than LoRA-FA.

4. **Remove the "two out of three" framing** from the conclusion unless GLUE results can be reinterpreted to support it. As written, it is misleading.

## Score and Decision

**Calibration anchors (all from the deepreview corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `TwJrTz9cRS.md` (HiRA, LoRA variant) | 8.00 | HiRA showed clear performance gains over LoRA with strong ablations; LoLoRA lacks comparable empirical evidence. |
| `d8w0pmvXbZ.md` (training instabilities) | 8.00 | Unrelated topic, but high confidence in claims with thorough experiments — LoLoRA's evidential support is weaker. |
| `eW4yh6HKz4.md` (CBQ, quantization) | 7.60 | Strong empirical validation of practical benefits; LoLoRA's empirical case is less convincing. |
| `DLJznSp6X3.md` (ReLoRA) | 5.75 | Both papers propose incremental modifications to LoRA; ReLoRA had clearer methodological novelty and decent evidence. LoLoRA has better theory but weaker empirical support. |
| `RbKThNNFxr.md` (LoRA-FA) | 5.33 | LoRA-FA was itself seen as simple but with a clear memory benefit. LoLoRA has stronger theory but no clear advantage over LoRA-FA empirically — a net slightly weaker position. |
| `g6syfIrVuS.md` (local loss optimization) | 7.00 | Strong theoretical contribution with rigorous proofs; LoLoRA's theory is narrower and less connected to practice. |
| `7X65yoKl3Y.md` (ALLoRA) | 3.33 | Both papers claim improvements over LoRA but have weak theory-to-empirics connection and marginal results. LoLoRA has slightly better theoretical grounding but similar empirical issues. |
| `igGeaxOiFM.md` (HoLoRA) | 3.00 | Method didn't convincingly improve over baselines; similar situation to LoLoRA. |

Relative to these anchors, LoLoRA sits between the low-scoring variants (3.0–3.33) and the mid-scoring ones (5.33–5.75). It has a cleaner theoretical result than ALLoRA or HoLoRA, but its empirical evidence is materially weaker than ReLoRA or LoRA-FA — the core empirical claim (online HPCA updates improve over frozen EVA initialization) is not supported by the data presented. The method does not show a clear practical benefit over the simpler LoRA-FA (EVA) baseline, and the memory advantage is shared with LoRA-FA, not unique to LoLoRA.

**Score: 4.0**  
**Decision: Reject**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>