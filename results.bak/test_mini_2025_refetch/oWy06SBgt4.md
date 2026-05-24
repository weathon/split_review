Now I'll write the consolidated final review.

## Summary

This paper makes a first attempt at 1-bit Fully Quantized Training (FQT), pushing gradient precision to its extreme. It provides theoretical regret bounds linking gradient variance to convergence for Adam vs. SGD, and uses this insight to design an Average 1-bit Quantization (AQ) strategy that prunes less informative gradient groups while allocating higher precision to informative ones. A Sample-Channel joint Quantization (SCQ) scheme ensures both activation and weight gradient computations can be implemented via binary matrix multiplications. Experiments on transfer learning (vision, detection, NLP) show consistent improvements over 1-bit per-sample quantization baselines, with up to 5.13× speedup vs. FP32 training.

## Strengths

- **First successful demonstration of 1-bit FQT with converged training.** Table 1 reports non-trivial accuracy on six datasets (e.g., VGGNet-16 with b=4 achieves 84.38% on CIFAR-10, ~5% below the QAT upper bound), whereas prior work had not pushed FQT below 4 bits. This is a genuine frontier contribution.

- **Theoretical analysis linking gradient variance to optimizer choice in FQT.** Section 4 derives regret bounds for Adam (Theorem 4.5) and SGD (Theorem 4.3), showing SGD's average regret scales as O(σ²) while Adam's scales as O(σ), explaining Adam's greater robustness at low precision. Fig. 4 empirically validates this: with PSQ, SGD fails to converge (~10% accuracy), while the proposed method with SGD still reaches ~70%.

- **Hardware-friendly acceleration with real speedup measurements.** The SCQ strategy enables binary matrix multiplications for both forward and backward passes. Table 4 provides actual speedups on Hygon CPU and Raspberry Pi 5 (up to 5.13× vs. FP32), with an additional "unoptimized vs. unoptimized" comparison showing 50-100× potential, giving concrete evidence of practical viability.

- **Clear empirical validation of variance reduction.** Fig. 5 directly measures quantizer variance across five datasets, showing the proposed AQ achieves ~0.1-0.15 variance vs. ~1.5-1.8 for PSQ — an order-of-magnitude reduction consistent with the theoretical motivation.

- **Systematic evaluation across architectures and tasks.** Results span ResNet-18, VGGNet-16, Faster R-CNN, MLP-Mixer, and BERT, demonstrating generalizability beyond a single architecture family.

- **Analysis of the b hyperparameter trade-off.** Table 1 varies b ∈ {2,4,8} with a reasoned discussion of the variance-vs.-retention trade-off, providing practical guidance for deploying the method.

## Weaknesses

### Fatal
None.

### Major

- **No component-level ablation studies.** The paper evaluates the full method (AGP + per-group quantization + splitting + SCQ) against PSQ, but never isolates individual components. There is no experiment that:
  - Replaces the range-proportional pruning with random pruning at the same average bitwidth (to test whether the pruning strategy itself drives improvement, or simply any scheme that concentrates compute on a subset of groups).
  - Removes the splitting operation and uses direct b-bit matrix multiplication (to measure the cost of the binary-decomposition overhead).
  - Compares SCQ against using the same quantization scheme (e.g., PSQ only) for both activation and weight gradients (to quantify SCQ's benefit).
  
  Without these ablations, it is unclear which design choices are responsible for the gains. The improvement over 1-bit PSQ could be driven primarily by the increased effective bitwidth of retained groups — a straightforward compute-vs.-accuracy trade-off — rather than by the specific adaptive pruning or SCQ strategies.

- **Limited to transfer learning, with training-from-scratch gaps under-discussed.** The paper acknowledges this limitation, but the main result tables and narrative emphasize the transfer-learning success. The training-from-scratch results (Appendix E, stripped by parser) reportedly show a "significant performance gap" between QAT and 1-bit FQT. Since the paper's title and framing ("Pushing the Limit of FQT to 1-Bit") suggest broader applicability, the scope limitation deserves more prominent treatment in the main text.

### Minor

- **The variance comparison in the main text is confusingly presented.** Equations (4) and (5) are symbolically identical: both read Var ≤ (D^(l)/4B²) Σ R_i². The text claims AQ variance is "significantly smaller" than 1-bit PSQ, but the reader must infer that this is because B differs (B=1 for 1-bit PSQ vs. B=2^b-1 for AQ). The formulas should be written with explicit B values or numeric denominators to avoid confusion. Additionally, the variance bound in Eq. 5 does not show the effect of the 1/p_i scaling and mask sampling — the paper states the proof is in Appendix C, but the main text would benefit from at least mentioning the key steps.

- **SCQ's performance benefit is not quantified.** The paper explains that SCQ enables binary matrix multiplication for weight gradients (which would otherwise be blocked by floating-point scale factors), but no experiment compares SCQ against a naive implementation that does not accelerate weight gradient computation. The claim that SCQ is beneficial rests entirely on a logical argument rather than empirical evidence.

- **Speedup is inconsistent across configurations.** ResNet-18 on Raspberry Pi at 64×64 achieves only 0.97× (slower than FP32). The paper mentions this in passing but does not analyze why or discuss scenarios where the method may not accelerate training.

### Trivial

- In the text following Eq. 5, a trailing closing parenthesis appears as "(D^(l)/4B² Σ R_i²)" — the notation is ambiguous; it could be read as the AQ bound itself rather than the PSQ bound being compared against.

## Nice-to-Haves

- A direct wall-clock comparison between b=4 AQ and an actual 1-bit matmul (Table 6 partially addresses this for matrix multiply, but not for end-to-end training).
- A brief discussion of why other gradient quantizers (e.g., from Chen et al. 2020 or Xi et al. 2023) are not applicable at 1-bit, to contextualize the contribution.
- Variance measurements for ablation variants (random pruning, uniform allocation) to directly test the theoretical claim that range-proportional sampling reduces variance.

## Removed Points

These points were raised in the input reviews but are removed for the reasons stated. Treat them with caution.

- **Variance derivation is incomplete / proof missing from appendix.** The paper states "The proof is given in Appendix C." The parser strips appendices from all papers; the proof exists in the original submission. Per policy, missing-appendix criticisms are removed. The presentation clarity concern about Eqs. (4)-(5) looking identical is retained as a Minor weakness.

- **"The theory does not directly motivate AGP beyond general variance reduction."** While true that the regret bounds are standard and don't prescribe AGP specifically, the paper's motivation is that variance reduction is important (from theory) and AGP is a method to achieve it. This is not a weakness — most algorithm design follows this pattern. Removed.

- **"PSQ at 1-bit obtains surprisingly high accuracy on some datasets (e.g., 78.91% on Flowers)."** This is a factual observation about the baseline, not a weakness of the paper. It simply shows that 1-bit PSQ already works well on easy datasets, which is compatible with the paper's claims.

- **"Training from scratch experiments should be discussed more prominently."** The paper already has a "Limitations" paragraph in the Conclusion and discusses the gap in the experiments section. The critic's concern that this is hidden in a "removed appendix" is invalid since the appendix was removed by the parser.

- **Generic strengths about "addressing an important problem" / "comprehensive evaluation."** These are too generic to carry weight. Specific strengths (confirmed above) are retained.

## Novel Insights

The most interesting pattern across both reviews is the tension between the paper's legitimate first-of-its-kind contribution (1-bit FQT) and the insufficiently rigorous evaluation. The harsh critic correctly identifies the lack of ablations as the paper's single biggest weakness, and this is not offset by the strength finder's generic claims. However, the harsh critic's fatal-level claim about the variance derivation is overblown — the empirical evidence in Fig. 5 independently supports the variance reduction claim, and the proof is in the (parser-stripped) appendix. The fundamental question the reviews surface is whether being "first" to reach 1-bit FQT is sufficient grounds for acceptance, or whether the method must also be convincingly decomposed into its working parts. A revision that adds the three suggested ablations (random pruning, uniform allocation, SCQ vs. naive) would resolve this tension.

## Suggestions

1. **Add three ablation experiments** to isolate the contribution of each component: (a) range-proportional pruning vs. random pruning with the same average bitwidth, (b) SCQ vs. using PSQ for both gradient types, (c) AQ with splitting vs. direct b-bit computation (to quantify splitting overhead). Even on a single dataset, these would substantially strengthen the paper.

2. **Clarify the variance comparison** by writing Eqs. (4) and (5) with explicit B values or a short explanation that B = 2^b - 1 for AQ while B = 1 for 1-bit PSQ, so the reader does not need to infer the difference.

3. **Discuss the 0.97× slowdown case** explicitly — analyze why it occurs and under what conditions users should expect speedup vs. slowdown.

4. **Promote the training-from-scratch limitation** more prominently in the abstract or introduction so readers have accurate expectations from the start.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| orG37FHN4b.md | 3.00 | R1 | Weaker — data-free quantization with withdrawn reject |
| 6Mdvq0bPyG.md | 3.00 | R1 | Weaker — QAT for LLMs with reject |
| UldnqRQWKS.md | 3.00 | R1 | Weaker — mixed quantization scaling laws, withdrawn reject |
| BTcZwitfgX.md | 2.50 | R1 | Much weaker — gradient theory with withdrawn reject |
| NmaXXAiJJC.md | 4.67 | R1 | Weaker — VQ compression with poor clarity and unconvincing speedup |
| wJ3GeGLFmc.md | 4.50 | R1 | Weaker — sub-8-bit integer training with limited improvement over baselines |
| LnKDcqOfgy.md | 5.00 | R1 | Comparable — quantization+compression, mixed reviews (3,6,5,6) |
| vmiV4Z99lK.md | 4.25 | R1 | Weaker — stochastic quantization with error analysis, mixed reject |
| oOwDQl8haC.md | 5.75 | R2 | Slightly stronger — accepted poster on low-bit accumulators; comparable novelty but more thorough evaluation |
| dIK0EfZFO9.md | 6.00 | R2 | Mixed — LR-QAT strong results but limited novelty, rejected despite high avg due to one 8 |
| FA3iYp1y6z.md | 5.00 | R2 | Comparable — low-rank correction for quantized LLMs, rejected |
| MiPyle6Jef.md | 6.75 | R2 | Stronger — QP-SNN accepted poster, more complete evaluation |
| VMV8gefvq8.md | 6.00 | R2 | Stronger — neural compression accepted poster |
| B9klVS7Ddk.md | 6.75 | R2 | Stronger — LLM compression evaluation, accepted poster |
| C61sk5LsK6.md | 7.00 | R2 | Stronger — InfoBatch accepted oral, rigorous evaluation |

**Round 1 bracket:** 4.5 – 6.5 (the paper is stronger than the ~3.0 anchors and clearly weaker than the ~8.0 anchors).

**Round 2 narrowing:** The closest comparator is the accumulator paper (5.75, accepted poster) which also tackles an extreme quantization regime with a mix of theory and hardware. The paper under review has stronger novelty (1-bit FQT is a more ambitious target than 12-bit accumulators) but weaker evaluation (missing ablations vs. the accumulator paper's multiple benchmarks). On balance, the paper sits between 5.0 and 5.5 — above the clearly rejected anchors but with unresolved weaknesses that prevent a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>