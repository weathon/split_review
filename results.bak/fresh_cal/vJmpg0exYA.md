Now I have all the evidence needed. Let me synthesize the final review.

## Summary

This paper studies the rounding step of neural network weight quantization through the lens of discrepancy theory. It proves a generalization bound (Theorem 3.3) using a variant of the Lovett-Meka random-walk algorithm, showing that approximately low-rank gradient structure enables rounding with controlled error. The paper then proposes DiscQuant, a practical distillation-based rounding algorithm that combines KL divergence minimization with a linear regularization term inspired by the theoretical analysis. Experiments on Phi-3-mini-3.8B and Llama-3.1-8B across multiple bitwidths and tasks show consistent improvements over GPTQ and RTN baselines.

## Strengths

- **Novel theoretical generalization guarantee (Theorem 3.3)**: Under a polynomial eigenvalue decay assumption on the gradient covariance matrix and a β-reasonable distribution condition, the theorem proves that with m = poly(log n/ε) samples, a randomized algorithm can round all but O(m) weights while keeping expected squared error ≤ λ₁ m^{-min{1/2,α-1}}(log n)². This is a nontrivial application of discrepancy theory to the quantization rounding problem and constitutes a genuine theoretical contribution independent of the practical algorithm.

- **Empirical validation of the low-rank gradient assumption (Figure 4, Table 1)**: The paper shows that per-sample gradients of pretrained LLMs have rapidly decaying eigenvalue spectra and that ‖𝔼[g]‖² is orders of magnitude smaller than 𝔼[‖g‖²] (e.g., 0.10 vs 4.78 for Phi3-mini), justifying the use of a first-order Taylor expansion and the low-rank modeling assumption that underpins the theory.

- **Consistent and substantial empirical improvements over GPTQ and RTN (Tables 2 and 3)**: Across all tested bitwidths (3.25–4.5 bits), both models, and six evaluation tasks, DiscQuant matches or exceeds both baselines. For example, on Phi3-mini at 3.25 bits, DiscQuant achieves 64.0% GSM8k vs 54.0% (GPTQ) and 31.0% (RTN). At 4.0 bits on Llama-3.1-8B, it achieves 66.5% GSM8k vs 63.2% (GPTQ). The gains are larger at lower bitwidths, which is precisely where rounding matters most.

- **Composability with other quantization improvements (Section 5.2, Figure 5)**: The paper demonstrates that DiscQuant works on top of incoherence processing (Randomized Hadamard Transform), showing it is grid-agnostic and can be stacked with preprocessing that improves weight structure.

- **Calibration data sensitivity analysis (Figure 6, Section 5.3)**: The investigation into mixing math data into the calibration set provides practical guidance for practitioners and shows non-obvious interactions (DiscQuant's HellaSwag improves with more math data while GPTQ's degrades).

## Weaknesses

### Fatal
None.

### Major
- **No ablation isolating the discrepancy-inspired linear term from the KL distillation objective.** The paper's core algorithmic claim is that the linear regularization term λ⟨c*,x⟩ — and specifically the discrepancy-theory-motivated choice c* = (1-2y) — is responsible for the improvement. However, the experiments compare the full DiscQuant only against GPTQ (which uses a completely different layer-wise MSE objective) and RTN. There is no ablation comparing (a) DiscQuant with c*, (b) DiscQuant with a random c, (c) DiscQuant without the linear term (KL only), or (d) DiscQuant with a different rounding regularizer (e.g., a concave sigmoid penalty). Without this, it is impossible to tell whether the empirical gains come from the discrepancy-inspired term, from the KL divergence objective alone (a "distillation beats layer-wise MSE" story would be useful but not the claimed contribution), or from the combination. Since the paper's title and framing center the discrepancy theory connection, this is a structural gap in the evidence.

### Minor
- **The derivation of c* uses a circular approximation.** The paper derives c* = (1-2y) from minimizing ‖x-y‖² by using the approximation x_i² ≈ x_i, justified by "since x is almost integral." But the optimization's goal is to make x integral — the approximation assumes the very property the algorithm aims to produce. This makes the derivation heuristically plausible but not principled. The paper is transparent about the approximation, but the circularity deserves acknowledgement.

- **The claim about projection ensuring membership in K is technically imprecise.** The paper states (line 101) that projecting to the hypercube H "ensures that the trajectory of DiscQuant remains within the convex polytope K." Since K = H ∩ V (where V is the affine subspace of the linear constraints), projecting to H alone does not guarantee that the solution stays in V. The KL divergence loss encourages satisfying the subspace constraints, but this is approximate. Line 281 uses the more modest phrasing "will keep us close the polytope K," but line 101 overstates the guarantee.

- **The gap between Theorem 3.3 and DiscQuant is under-acknowledged in the paper's framing.** The theorem provides guarantees for a randomized algorithm (Algorithm B.2, based on the Lovett-Meka random walk), not for DiscQuant's SGD-based optimization. The paper does acknowledge in Section 4 that the Lovett-Meka algorithm is "infeasible" and that DiscQuant is a "simple heuristic" (line 275). However, the abstract and introduction frame the connection more tightly ("Our proof, which is algorithmic, inspired a simple and practical rounding algorithm"), which could mislead a reader into thinking the theorem directly supports DiscQuant's performance. Explicit clarification earlier in the paper would improve intellectual honesty.

### Trivial
None.

## Nice-to-Haves

- **Computational cost comparison**: The paper states it does not perform inference timing experiments. At minimum, reporting the approximate wall-clock time or number of forward passes required by DiscQuant vs. GPTQ would help practitioners assess the trade-off. The method requires two model copies in memory (like knowledge distillation), which is a practical constraint worth quantifying relative to GPTQ's cheaper per-layer approach.
- **Ablation on calibration dataset size m**: The theory suggests m = poly(log n/ε) samples suffice. The experiments use a fixed 8k samples. A study varying m would test whether this theoretical prediction holds in practice and guide practical usage.
- **Hyperparameter λ sensitivity**: The paper does not report how λ was chosen or how sensitive results are to its value.

## Removed Points

These points were flagged by reviewers but are removed or demoted after verification:

- **"Missing baseline: distillation-only rounding with a rounding regularizer (AdaRound/BRECQ style)"** — The critic argues for comparison against a version using a concave sigmoid regularizer. However, AdaRound and BRECQ are layer-wise methods designed for smaller vision models, not LLMs. The paper's baselines (GPTQ and RTN) are the standard in LLM weight quantization. Creating a new hybrid baseline that inserts a different regularizer into DiscQuant is a reasonable ablation suggestion (which is already covered under the Major weakness above), not a missing external comparison. Removed as scope creep beyond standard LLM quantization practice.

- **"Missing comparison to Nair & Suggala (2024) and Behdin et al. (2023)"** — The paper explains that Nair & Suggala only report results on closed-source PaLM-2 without released code, and Behdin et al. use different model families (OPT, BLOOM, Falcon). These are not standard LLM quantization baselines and including them would require non-trivial re-implementation on different architectures. Removed per the rule against demanding comparisons outside stated scope.

- **"No speed or memory comparisons"** — The paper explicitly states "We do not perform inference timing experiments" (line 294) and notes that DiscQuant uses existing inference kernels. This is an acknowledged limitation, not an oversight. Moved to Nice-to-Haves.

- **"The paper should analyze or argue why SGD with the linear term tends to produce vertices"** — This suggestion from the Strengthening the Paper section is directionally useful but asks for analysis beyond what is standard for an empirical ML paper. The heuristic justification provided (linear minimization over a polytope finds vertices) is sufficient for the paper's scope.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the paper's theory and algorithm are connected by "inspiration" rather than formal implication is accurate but already partially acknowledged in the paper. The strength finder's observations about the value of the calibration data sensitivity analysis and composability with incoherence processing are useful but are faithful summaries of content the paper already presents.

## Suggestions

1. **Add ablation experiments** comparing the full DiscQuant against variants without the linear term, with a random c, and with a different rounding regularizer (e.g., a sigmoid penalty). This is the single most important addition to substantiate the claim that discrepancy theory drives the empirical gains. Even one bitwidth (e.g., 3.25 bits on Phi3-mini) would be informative.

2. **Clarify the theory–algorithm relationship** in the abstract and introduction. Replace phrasing that implies the theorem directly validates DiscQuant with explicit wording: the theorem proves generalization for a related algorithm (Lovett-Meka random walk), and DiscQuant is a practical heuristic motivated by the same geometric insight.

3. **Acknowledge the circularity in the c* derivation** explicitly — note that the approximation x_i² ≈ x_i is valid near convergence and used as a heuristic to select a good linear direction.

4. **Tighten the projection language**: replace "ensures that the trajectory remains within K" with "helps keep the trajectory near K" to avoid technical overstatement.

5. **Report λ selection and sensitivity** in the final version to aid reproducibility.

## Score and Decision

The paper makes a genuine theoretical contribution (Theorem 3.3) and presents a practical method with strong empirical results. However, the central attribution claim — that discrepancy theory drives the empirical improvements — is not adequately supported because the discrepancy-inspired linear term is never ablated from the distillation objective. This is a significant weakness in the evidence chain, though not fatal to the paper's overall value, since the method itself works well and the theory stands on its own. With the recommended ablation experiments, the paper could convincingly bridge this gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>