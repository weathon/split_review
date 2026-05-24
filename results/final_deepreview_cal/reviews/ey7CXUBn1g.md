Now I have sufficient calibration data. Let me synthesize the final review.

**Round 1 Bracket:** The paper clearly sits above AutoTrunc (4.00) and MoE-SVD (5.00), and is stronger than ASVD (6.25). Basis Sharing (6.50) and Compressing LLMs (6.75) form the upper part of the plausible bracket. Initial bracket: **6.0–7.0**.

**Round 2 Narrowing:** AdaSVD is more comprehensive than ASVD (6.25) — more models, more datasets, addresses a gap ASVD left open (truncation compensation). It's comparable to Basis Sharing (6.50) in contribution quality but has more thorough experiments. It's a method paper with real contributions vs Compressing LLMs (6.75) which is a benchmark. I'd place AdaSVD at **6.5** — a solid, well-executed improvement over the prior SOTA with some addressable gaps.

---

## Summary

AdaSVD proposes two improvements to SVD-based LLM compression: (1) **adaComp**, an alternating least-squares refinement of truncated singular factors using Moore-Penrose pseudoinverse to stably reduce truncation error, and (2) **adaCR**, an adaptive layer-wise compression ratio assignment based on cosine similarity between layer input and output. Experiments across LLaMA2, OPT, Mistral, and Vicuna show consistent and substantial perplexity improvements over prior SVD methods (SVD-LLM, ASVD, FWSVD), especially at higher compression ratios, and the method is shown to compose orthogonally with GPTQ quantization.

## Strengths

- **Strong, well-validated core method (adaComp):** The alternating pseudoinverse-based update scheme is clearly motivated (Eq. 5–13) and validated through Figure 3(a) showing stable MSE reduction vs. naive updates, Figure 3(c) showing output distribution tightening, and Table 3a confirming large perplexity gains attributable to adaComp (e.g., WikiText-2 at 60% CR: 78.82 → 50.33).

- **Comprehensive and convincing evaluation:** The paper evaluates 4 model families across 3 language modeling datasets and 5 commonsense QA benchmarks at multiple compression ratios (40–80%). Perplexity improvements over SVD-LLM are decisive — at 60% CR on LLaMA2-7B, WikiText-2 perplexity drops from 89.90 to 50.33 (44% reduction). Gains hold across all model families tested (Table 2), and the method composes with GPTQ quantization (Table 4).

- **Thorough ablation studies:** Table 3 cleanly isolates the contributions of adaComp (Table 3a), adaCR (Table 3b), iteration count (Table 3c), and minimum retention ratio (Table 3d), giving clear evidence that both components contribute independently and that hyperparameters are reasonably robust.

- **Practical design choices:** The stack-of-batch calibration strategy (Figure 3b) addresses GPU memory constraints in a practical way, and the method integrates with existing data whitening techniques, making it straightforward to adopt within existing SVD compression pipelines.

## Weaknesses

### Fatal

None.

### Major

- **Missing computational cost analysis:** The paper provides no wall-clock time, FLOP counts, or memory overhead for the adaComp iterative updates relative to baseline SVD-LLM or other methods. For a compression method targeting resource-constrained deployment, understanding the one-time compression cost is important. The paper notes that adaComp requires per-layer SVD and pseudoinverse computations over multiple iterations — quantifying this cost (even approximately) would allow readers to assess the practical trade-off.

### Minor

- **adaCR importance metric lacks comparison with alternatives:** The cosine similarity between input X and output WX (Eq. 17) is a reasonable heuristic, but the paper does not compare it against other importance measures (e.g., singular value-based, Hessian-based, activation variance). The ablation (Table 3b) shows adaCR provides meaningful gains (e.g., 60% CR: 69.46 → 50.33 WikiText-2), so the component works, but the absence of any comparator weakens the claim that this particular metric is well-chosen rather than simply "an adaptive scheme helps."

- **Zero-shot QA improvements are small and variance is unreported:** On commonsense reasoning tasks (Table 1), average accuracy gains over SVD-LLM are typically 1–2 absolute points, and no standard deviation or confidence information is provided across calibration seeds. While these results serve as sanity checks for the main perplexity findings, the paper's claim that AdaSVD "consistently achieves higher average accuracy" overstates the practical significance of these gains.

- **VLM evaluation is qualitative only:** Figure 5 shows four image captioning examples with color-coded correct/incorrect segments. Without a quantitative metric (e.g., CIDEr, BLEU-4) or broader sample, this demonstration remains anecdotally suggestive rather than evidential.

### Trivial

- The paper frequently defers results (70–80% compression ablations, additional layer-wise importance visualizations, captioning comparisons) to the supplementary file. While Table 4 does include 70–80% compression results in the main text, moving the ablation results at these ratios into the main paper (even in condensed form) would make the evaluation self-contained.

## Nice-to-Haves

- Compare adaCR's cosine similarity importance against one or two natural alternatives (e.g., gradient norm, Fisher diagonal) to strengthen confidence in the metric choice.
- Add a brief runtime/memory cost comparison for adaComp relative to SVD-LLM to clarify the practical compression-time trade-off.
- Include quantitative VLM metrics on a standard held-out split.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic's claim that high-compression results are entirely in supplementary and unverifiable:** Incorrect. Table 4 in the main paper contains 70% and 80% compression results for LLaMA2-7B (both with and without GPTQ). Only the ablation study results at 70/80% and the non-quantized Table 1 results at those ratios are in supplementary. This is a minor presentation issue, not an evidential limitation. Per protocol, criticisms about missing supplementary content are also excluded since the parser strips appendices.

- **Harsh critic's characterization of adaCR gains as "small (1.75 PPL at 50%)":** Cherry-picked. At 60% compression, adaCR reduces WikiText-2 perplexity from 69.46 to 50.33 — a 27.5% relative reduction that is substantial. The 50% result alone does not fairly represent adaCR's contribution.

- **Strength Finder suggestion about "pushing the performance boundary":** Retained as a strength but with qualification — the method clearly pushes SVD family boundaries, but the gap to uncompressed models remains large.

## Novel Insights

The paper's key insight — that SVD truncation error can be effectively compensated through alternating pseudoinverse-based updates of the singular factors, treating the problem as a sequence of least-squares estimations rather than direct gradient-based optimization — is genuinely novel within the SVD compression literature. Prior methods focused on pre-truncation transformations (whitening, activation scaling) but left the truncated factors unadjusted. The demonstration that this compensation is both stable (via Moore-Penrose) and effective (via alternating updates) with minimal calibration data represents a meaningful advance. The stack-of-batch strategy for GPU-memory-constrained calibration is also a practical but non-obvious contribution.

## Suggestions

- Quantify the one-time compression cost of adaComp (GPU-hours or wall-clock time relative to SVD-LLM) on a representative model (e.g., LLaMA2-7B). Even a single sentence with approximate numbers would substantially address the practical efficiency concern.
- Report perplexity standard deviation across 3–5 calibration data seeds for a representative setting to give readers confidence that the reported improvements are stable.
- Move a condensed version of the 70/80% ablation results from supplementary into the main paper.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| AutoTrunc | 3KEwJGYNzH | 4.00 | R1 | AdaSVD is substantially stronger — more comprehensive, better method, more models |
| MoE-SVD | ho7ZUS1z8A | 5.00 | R1 | AdaSVD has clearer methodology, stronger results, broader evaluation |
| ASVD | HyPofygOCT | 6.25 | R1/R2 | AdaSVD improves on ASVD's baselines, has more comprehensive evaluation, addresses truncation compensation that ASVD did not |
| Basis Sharing | gp32jvUquq | 6.50 | R2 | Comparable quality; AdaSVD has more thorough experiments and cleaner ablation; Basis Sharing reported throughput |
| Compressing LLMs | B9klVS7Ddk | 6.75 | R2 | Different paper type; AdaSVD is a method paper with real technical contributions and strong empirical results |

Round 1 bracket: 6.0–7.0. Round 2 narrowed to: AdaSVD sits between ASVD (6.25) and Compressing LLMs (6.75), comparable to Basis Sharing (6.50). AdaSVD is clearly stronger than ASVD in experimental comprehensiveness and addresses a novel technical gap; it falls slightly short of the 7+ tier due to missing computational cost analysis and the heuristic nature of adaCR.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>