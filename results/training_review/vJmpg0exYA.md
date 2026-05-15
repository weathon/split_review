I have thoroughly read the paper and verified the reviewer claims against the actual content. Let me now synthesize the final review.

---

## Summary

This paper introduces DiscQuant, a weight-rounding method for post-training LLM quantization that is inspired by discrepancy theory. The paper presents a theoretical result (Theorem 3.3) — applying a variant of the Lovett-Meka algorithm — showing that given poly(1/ε) samples from the data distribution, one can round all but O(m) weights while keeping the expected squared inner-product error ≤ ε under a low-rank gradient assumption. The practical DiscQuant algorithm uses projected SGD to minimize a weighted combination of a linear regularizer and KL divergence, and empirically outperforms GPTQ and RTN across Phi-3-mini-4k and Llama-3.1-8B on multiple tasks. The paper also validates key assumptions (gradient covariance eigenvalue decay, first-order dominance) with real-model measurements.

## Strengths

- **Novel theoretical framing via discrepancy theory.** Theorem 3.3 (informal Theorem 1.1) connects the weight-rounding problem to the Lovett-Meka algorithm and provides a generalization guarantee under the assumption that the gradient covariance has polynomially decaying eigenvalues. This goes beyond prior work (e.g., Nagel et al. 2020) that assumes zero first-order terms. The eigenvalue decay plot (Figure 4) and the empirical demonstration that per-sample gradients are not near zero (Table 1) ground the theoretical assumptions in real models.

- **Clear and consistent empirical improvement over GPTQ in block-scaling experiments.** On Phi-3-mini-4k at 3.25 bits, DiscQuant achieves 64% GSM8k accuracy vs. GPTQ's 54% and RTN's 31% (Table 2). Across both models, multiple bitwidths (3 to 4.5 bits), and multiple tasks, DiscQuant consistently outperforms GPTQ and RTN in the block-scaling setting, often recovering full performance at 0.25–0.5 fewer bits. This is a practically meaningful improvement.

- **Empirical validation of the paper's key assumptions.** The paper checks (Table 1) that ‖𝔼[g]‖² ≪ 𝔼[‖g‖²] (showing per-sample gradients are not negligible), shows the first-order approximation correlates with actual loss change (Figure 3), and demonstrates fast eigenvalue decay of the gradient covariance (Figure 4). These experiments support the theoretical modeling choices.

- **Composability with other quantization techniques.** DiscQuant is agnostic to the quantization grid and works with both block scaling (Section 5.1) and incoherence processing (Section 5.2). The ablation on data mix (Figure 6) is a thoughtful practical contribution.

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice gap: the theoretical guarantee (Theorem 3.3) applies to the Lovett-Meka algorithm (Algorithm B.2), not to DiscQuant.** The paper transparently states this gap (Section 4: "we could use the Lovett-Meka algorithm... But explicitly calculating all the gradients and storing them is infeasible. Instead a simple heuristic way..."), but the overall narrative — from title ("Inspired by Discrepancy Theory") through abstract ("Our proof, which is algorithmic, inspired... DiscQuant") — creates an impression of a tighter link than exists. DiscQuant replaces the random walk with a heuristic SGD-based minimization of a linear function plus KL divergence, with no guarantee that its solution inherits any property of the Lovett-Meka output. The theoretical sections and the practical algorithm are thus decoupled contributions. The paper would be materially strengthened by either (a) adapting the theory to cover DiscQuant, or (b) repositioning the theory as a separate conceptual contribution and grounding the algorithm on other evidence.

### Minor

- **No ablation on the critical design choices: the linear regularizer direction c\* and the regularization strength λ.** The paper selects c\* = 1−2y under the approximation that xᵢ² ≈ xᵢ for nearly-integral x, yet during most of the optimization x is fractional. The value of λ is never reported or ablated. Without experiments comparing c\* vs. a random c or λ = 0 (pure distillation), the contribution of the discrepancy-inspired term to the empirical results is unvalidated.

- **Theorem 3.3's bound does not directly connect to the actual optimization objective.** The theorem bounds (x−y)ᵀΣ(x−y) — the expected squared inner product of the perturbation with a random gradient. The paper's practical objective is KL divergence, and the argument connecting the bound to Δf (or to KL) relies on a first-order approximation whose error is not quantified theoretically. Figure 3 provides a single correlation plot (one model, 4.25 bits) to support this link, but no theoretical bound on the remainder is given.

- **Limited baseline comparisons.** The paper compares only against GPTQ and RTN. The related work section discusses AdaRound, AdaQuant, and BRECQ (older methods for vision models) but does not attempt to adapt them to LLMs or argue rigorously why they are inapplicable. While GPTQ is the dominant LLM rounding method, a comparison against one additional post-training rounding baseline would strengthen the claim of state-of-the-art results.

- **Hyperparameters not reported.** The paper does not specify the learning rate, batch size, number of optimization steps, or the value of λ used in any experiment. This limits reproducibility.

### Trivial

- The caption in Figure 3 reports results only at 4.25 bits for one model; showing additional bitwidths would strengthen the generality claim.

## Nice-to-Haves

- An empirical comparison against a practical (approximate) variant of Lovett-Meka — e.g., running the random walk with projected gradients using the empirical covariance — to test whether the theoretical algorithm itself works well in practice.
- A trajectory plot showing how the fraction of rounded variables evolves during DiscQuant optimization, to validate the claim that the method converges to a nearly-integral vertex.
- Results on additional model families (e.g., Mistral, Qwen) to demonstrate generality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Section 5.2 results are mixed; the headline claim is primarily supported by block scaling."** — The paper honestly describes the incoherence results as "competitive" (not superior). Mixed results do not constitute a weakness against a claim the paper does not make.
- **"The abstract's phrasing is misleading."** — The abstract says "Our proof... inspired... DiscQuant," which is literally true. The inspiration is the shared geometric concept of finding a vertex of the polytope K. The paper is transparent about the algorithmic difference.
- **Various formatting/style nitpicks.** — These are parser artifacts, not author errors.
- **"Missing appendix content / proofs in appendix."** — The parser strips appendices; this is not the authors' omission.
- **"Cannot independently verify cited references."** — Per review policy, all cited entities are assumed to exist.
- **Strength Finder's claim that DiscQuant "directly instantiates the theoretical insight" with the implication that the theoretical guarantee carries over.** — This conflicts with the verified weakness about the theory-practice gap. DiscQuant is conceptually inspired but not guaranteed by the theory.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel insight not already in the paper. The core tension — that the theory and practice are partially decoupled — is something the paper itself acknowledges (by noting Lovett-Meka is infeasible and substituting a heuristic), though it under-emphasizes this gap in the high-level narrative.

## Suggestions

1. **Conduct and report ablations on the linear regularizer.** Compare DiscQuant using c\* vs. a random c vs. λ=0 on one representative setting (e.g., Phi-3-mini at 3.25 bits). This would isolate whether the discrepancy-inspired term contributes beyond pure distillation with projection.
2. **Report all optimization hyperparameters** (learning rate, batch size, number of steps, λ value) in the main paper or appendix.
3. **Either bridge the theory-practice gap or decouple the contributions more explicitly.** If the paper retains both theory and practice, add a discussion of what, if any, properties DiscQuant provably inherits from the discrepancy framework. If this is not possible, restructure the paper so the theoretical section is positioned as a separate but related conceptual contribution rather than as a justification for DiscQuant.
4. **Validate the first-order correlation plot (Figure 3) at an additional bitwidth** (e.g., 3.25 bits) to show the approximation holds across quantization levels.

## Score and Decision

The paper makes two contributions: a novel theoretical connection between discrepancy theory and weight quantization, and a practical algorithm with strong empirical results. The main issue is the disconnect between these contributions — the theory guarantees properties of Lovett-Meka, not DiscQuant. The paper is transparent about this gap, but the narrative framing overstates the unity of the two parts. The empirical results (especially Tables 2–3) are clear and practically meaningful. The paper falls short of the strongest possible version of itself but has genuine value: the theoretical framing is interesting, and DiscQuant is a demonstrably effective method. A weak accept is appropriate; the paper can be strengthened with additional ablation experiments and a more careful framing.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>