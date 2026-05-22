Here is the consolidated review.

---

## Summary

This paper proposes SparseFW, a method for pruning Large Language Models by relaxing the combinatorial mask selection problem to a convex program over the convex hull of binary masks and solving it with the Frank-Wolfe (FW) algorithm. Each layer's weights are pruned by optimizing a continuous mask on a small calibration dataset, then thresholding to obtain a binary mask. On several modern GPT architectures (LLaMA-3.1, Gemma-2, Yi-1.5, DeepSeek, Qwen2.5) at 60% unstructured and 2:4 semi-structured sparsity, SparseFW reduces per-layer pruning error by up to 80% and improves perplexity and zero-shot accuracy over Wanda and RIA baselines. The paper also provides a theoretical error bound that separates optimization error from thresholding error.

## Strengths

- **Principled departure from greedy heuristics.** The paper formulates mask selection as a convex relaxation of the combinatorial problem and solves it via Frank-Wolfe, which explicitly accounts for weight interactions through the gradient structure — a genuine conceptual difference from the per-weight salience scores used by Wanda and RIA. The LMO for the $\mathcal{C}_k$ polytope (Equation 12) is efficient and yields sparse updates.

- **Clear empirical gains at higher sparsity levels.** At 60% unstructured sparsity and 2:4 semi-structured sparsity, SparseFW consistently improves both perplexity and zero-shot accuracy across all five model families tested (Table 1). The gains are often substantial: e.g., LLaMA-3.1-8B at 60% sparsity improves from Wanda's 21.53 perplexity to 17.97, and from 48.08% to 51.92% zero-shot accuracy. These are non-trivial improvements on strong baselines.

- **Memory-efficient implementation.** By precomputing $G=XX^\top$ and $H=WG$ once per layer, each FW iteration requires only operations on $d_{in}\times d_{in}$ matrices rather than holding the full activation tensor, which is critical for scaling to large models.

- **Honest acknowledgment of limitations.** The paper explicitly discusses the caveat that vanilla FW without fixing weights performs worse than baselines (Section 2.3) and acknowledges the "local–global objective mismatch" in the conclusion. This transparency is commendable.

## Weaknesses

### Major

1. **Method-scope mismatch undermines the core framing.** The paper is titled "Don't Be Greedy, Just Relax!" and motivates the approach as a principled alternative to greedy heuristics that "ignore weight interactions." However, the actual algorithm (a) warm-starts from a greedy baseline (Wanda or RIA), and (b) fixes 90% of the highest-saliency weights from that warmstart as unprunable. The paper states that "setting $\alpha=0.0$ (full FW without any fixed weights) consistently yields worse results than the baselines." This means the successful method is solving a constrained problem over only ≈10% of the weights, preserving the greedy heuristic's decisions for the remaining 90%. The theoretical guarantee (Lemma 1) applies to the unconstrained relaxation, not to this substantially modified algorithm. While the paper acknowledges this honestly, it does not resolve the tension: the advertised method and the effective method are different, and the theory does not cover the latter. This is a structural weakness, not a missing ablation.

2. **Data error in Table 1.** The RIA zero-shot accuracy row at 60% sparsity is identical to the Wanda row for all six models (e.g., Gemma-2: 63.19, Yi-1.5: 53.7, all values match). It is extremely unlikely that two different pruning methods produce identical accuracy across every model at a specific sparsity level. This appears to be a copy-paste error and must be corrected before any claims about RIA comparisons can be evaluated.

3. **No standard deviations or confidence intervals.** The paper deliberately "omit[s] standard deviations for legibility" (Table 1 caption). Many of the reported perplexity improvements are small — e.g., at 50% sparsity, SparseFW(Wanda) is sometimes *worse* than Wanda (DeepSeek-7B: 7.89 vs. 7.79; LLaMA-3.1-8B: 10.21 vs. 10.09). Without variance estimates, the reader cannot assess whether the claimed gains are statistically significant, especially in the regimes where improvements are marginal.

4. **Exclusion of SparseGPT creates an incomplete evaluation.** SparseGPT is the dominant one-shot LLM pruning baseline and also performs mask selection (combined with weight reconstruction). The paper states it is excluded because it "involves a reconstruction step," but SparseGPT's mask selection is a core part of its procedure. Even if the comparison is not apples-to-apples for the final perplexity numbers, a comparison of mask quality (e.g., reconstruction error under the same objective) would be informative. As it stands, the evaluation compares only against Wanda and RIA, which are weaker baselines than SparseGPT.

### Minor

5. **Theoretical bound is too loose to be practically meaningful and does not cover the actual algorithm.** The bound in Lemma 1 scales as $\lambda_{\max}(Q) \cdot 2(k + \sqrt{2 d_{in} d_{out} k})$. For a typical LLaMA-3.1-8B layer with $d_{in}=d_{out}=4096$ and $k \approx 10^7$, the second term is on the order of $5 \times 10^7$, making the bound vacuously large. Moreover, the bound does not incorporate the warm-start or the fixed-weight heuristic used in practice, so it provides no guarantee for the implemented method. The paper would benefit from either tightening the bound or explicitly discussing its limitations.

6. **Mixed results at lower sparsity.** At 50% sparsity, SparseFW(Wanda) is worse than Wanda on DeepSeek-7B (7.89 vs. 7.79) and LLaMA-3.1-8B (10.21 vs. 10.09), and ties or only marginally improves on other models. The paper notes this, but given that 50% sparsity is a practically relevant regime, it weakens the claim of universal superiority.

7. **No compute cost reporting.** The paper claims SparseFW is "efficient" but reports no wall-clock time or GPU-hour cost. With 2000 iterations per layer and ~100 layers per model, the total compute is non-trivial and should be quantified for practitioners evaluating the cost-performance trade-off.

### Trivial

- Figure 3 shows that performance improves up to ~2000 iterations and beyond, and with more calibration samples (512 > 256). The paper uses 2000 iterations and 256 samples but does not explain why 512 samples were not used given the benefit.
- Some model × sparsity combinations have missing entries in Table 1 (e.g., LLaMA-3 14B at 2:4 perplexity).

## Removed Points

These points were flagged by the harsh critic but are removed or weakened after verification:

- **"Up to 80% reduction is misleading because average is 20-40%."** The phrase "up to 80%" accurately describes the maximum observed reduction, and the average range is separately reported. This is standard practice, not misleading.
- **"Method does not match claimed approach" framed as fatal.** I have kept this as a Major weakness (point 1) but weakened the framing. The paper does honestly describe the caveat; the issue is that the framing and theory do not align with the actual implementation. It is a structural weakness, not fraud.
- **"Lemma 1 bound is vacuously large" — kept as Minor (point 5) since it is a valid observation but the paper presents it informally, and loose bounds are common for relaxation analyses.**
- **Complaints about warm-start as a "requirement" without noting Algorithm 1 accepts M_0 as input.** The paper does describe warm-start explicitly. I have kept this as part of point 1.
- **Strength Finder claims about "large per-layer reconstruction error reduction"** — kept as a real strength but merged with the main strength bullet on principled approach.

## Nice-to-Haves

- A comparison of mask quality (reconstruction error) between SparseFW and SparseGPT masks would strengthen the evaluation without requiring SparseGPT's weight reconstruction.
- Reporting wall-clock time or GPU-hours for the full pruning process across different models would help practitioners assess the cost-performance trade-off.
- An ablation of the fixed-weight fraction $\alpha$ should be shown in the main paper (it is referenced as Table 2 in the appendix).

## Novel Insights

None beyond the paper's own contributions. The key tension — that a principled relaxation method still requires a large dose of the greedy heuristic it aims to replace — is an interesting finding about the nature of the LLM pruning problem, but the paper does not deeply analyze *why* the relaxation fails without fixed weights or what structural property of LLM layers causes the local-global mismatch.

## Suggestions

1. **Correct the RIA accuracy duplicates** in Table 1 before any further dissemination. This is the most urgent fix.
2. **Reframe the paper** either (a) as a principled mask *refinement* method that warm-starts from and preserves most of a greedy mask, with theory adapted to that setting, or (b) provide a principled explanation for *why* the naive relaxation fails and a more principled fix than the 90% heuristic.
3. **Include SparseGPT** in the comparison, at least for mask-quality metrics (reconstruction error with the same objective), and discuss how the methods differ.
4. **Report standard deviations** across calibration seeds for all main results, or at minimum state that results are from a single run and discuss the implications.
5. **Report compute cost** (wall-clock time or GPU-hours) for the full pruning pipeline on at least one model.

## Score and Decision

**Calibration anchors consulted:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| PaMj3yuaHi (Free Lunch in LLM Compression) | 3.00 | 1 (weak) | Much weaker — no novel optimization method |
| sGWY8n1ORQ (SUSI) | 2.00 | 1 (weak) | Much weaker |
| NlMXI17iou (Reordered SparseGPT) | 3.00 | 1 (weak) | Much weaker |
| **oj0OhhqAGN (SparseSwaps)** | **5.00** | **1 (mid), 2 (narrow)** | **Most topically similar — mask refinement from Wanda. SparseFW has more principled framing but also deeper method-scope gap and a data error. Slightly weaker.** |
| ek6dQSumYx (Elsa) | 5.33 | 1 (mid), 2 (narrow) | Stronger results at extreme sparsity, fewer methodological concerns |
| 0R06BghLJX (MaskPro) | 5.50 | 1 (mid), 2 (narrow) | Cleaner method, accepted at the same venue tier |
| lqjQs2lVNm (HyperPrune) | 6.00 | 2 (narrow) | Stronger empirical evaluation, cleaner method |
| 2uxuiykvA4 (RMM) | 3.60 | 2 | Less relevant |
| yRtgZ1K8hO (Polar Express) | 8.00 | 1 (strong) | Unrelated topic, not comparable |

**Round 1 bracket:** 3.5 – 6.5. **Round 2 narrowing:** Compared to the closest anchor SparseSwaps (5.00, Reject), SparseFW has similar structural issues but adds a concrete data error and a deeper method-scope disconnect. Compared to Elsa (5.33, Accept), MaskPro (5.50, Accept), and HyperPrune (6.00, Accept), SparseFW is clearly weaker in empirical rigor and methodological coherence. **Final score anchored below all accepted anchors and comparable to the rejected SparseSwaps, but slightly weaker.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>