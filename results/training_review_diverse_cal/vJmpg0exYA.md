I've thoroughly analyzed the paper and all reviewer claims against the actual paper content. Let me now write the consolidated review.

## Summary

This paper studies the weight rounding problem in post-training quantization (PTQ) from the lens of discrepancy theory. The authors prove Theorem 3.3, showing that under a low-rank gradient covariance assumption, a randomized algorithm (Lovett-Meka) can round all but O(m) weights while bounding the expected approximation error with m = poly(log n / ε) samples. They then propose DiscQuant, a practical algorithm that minimizes a KL-divergence distillation objective combined with a linear regularizer (to encourage convergence to a vertex of the feasible polytope) via projected SGD. Experiments on Phi-3-mini-3.8B and Llama-3.1-8B show that DiscQuant consistently outperforms GPTQ and RTN on block scaling quantization across bit widths and tasks, with particularly large margins on GSM8k (e.g., 64% vs. 54% vs. 31% at 3.25 bits on Phi-3-mini).

## Strengths

- **Novel theoretical framing for PTQ rounding.** Theorem 3.3 provides a formal generalization bound for rounding under a low-rank gradient covariance assumption, which is a genuinely different perspective from the second-order Hessian-based reasoning that dominates prior work (AdaRound, GPTQ). The connection to discrepancy theory (Lovett-Meka) is creative and opens a new direction for theoretical analysis of PTQ.

- **Consistent and often large empirical gains over GPTQ on block scaling.** Across both models and all bit widths, DiscQuant matches or outperforms GPTQ and RTN. The gains are most pronounced on the generative GSM8k task, where the gap is frequently 5–10+ percentage points (e.g., 77.3% vs. 71.5% vs. 62.2% at 4 bits on Phi-3-mini). On ARC Challenge, PIQA, and WinoGrande, DiscQuant recovers full accuracy at 0.25–0.5 fewer bits than the baselines.

- **Strong motivation for the first-order approach, supported by evidence.** Table 1 shows that per-sample gradient norms (E‖g‖²) are much larger than squared mean gradients (‖E(g)‖²), directly contradicting the "gradients are nearly zero" assumption that motivates second-order methods. Figure 3 shows that Δf is well-correlated with its first-order approximation, justifying the linear constraint approach.

- **Clean geometric intuition.** The hypercube-polytope-vertex framing (Figure 1) provides an elegant and accessible explanation of why most weights can be rounded while satisfying sample constraints. The algorithm's design (minimizing a linear function to find a vertex + KL distillation) follows naturally from this geometric perspective.

- **Composable with other quantization improvements.** DiscQuant works with both standard block scaling and incoherence processing (randomized Hadamard transform), demonstrating it is a general-purpose rounding module rather than being tied to a specific quantization grid.

## Weaknesses

### Major

- **Theory–algorithm gap weakens the claimed contribution.** Theorem 3.3 provides guarantees for the Lovett-Meka random-walk algorithm under explicit linear constraints on loss-function gradients. DiscQuant, by contrast, solves a different optimization problem (KL divergence + linear regularizer via SGD + projection). The paper explicitly states DiscQuant was "inspired by" rather than "derived from" the theory, and acknowledges that Lovett-Meka is "infeasible" in practice (line 275). However, the paper's framing (title, abstract, Section 1) presents theory and algorithm as a unified contribution. The paper would be strengthened by either (a) proving that DiscQuant's objective inherits the same kind of guarantee, or (b) clearly separating the two contributions and explaining what specific design choices the theory *did* motivate. As written, a reader cannot tell whether the theory actually explains DiscQuant's empirical success.

- **Empirical validation of the low-rank gradient assumption uses a questionable dimensionality reduction.** Figure 4 projects gradients to 2048 dimensions via Johnson-Lindenstrauss before computing the covariance eigenvalues. Since the true parameter dimension is billions, the eigenvalue spectrum of the *projected* covariance is not guaranteed to reflect that of the *original* covariance — JL preserves pairwise distances between points, but the eigenvalue structure of the covariance matrix can be distorted by the projection. The low-rank assumption is critical to Theorem 3.3 and to the paper's generalization reasoning, but the evidence for it is weakened by this methodological gap. The authors should either validate the eigenvalue decay on a smaller but representative subset of parameters in the original dimension, or provide theoretical justification that JL preserves the relevant spectral properties.

### Minor

- **Incoherence results qualify the "superior compression" narrative.** The abstract states DiscQuant "achieves superior compression" over GPTQ, and the block scaling results strongly support this. However, in the incoherence processing setting, the results are more mixed: Tables 4–5 show DiscQuant is often *comparable* to GPTQ rather than uniformly better (e.g., Phi-3-mini at 4 bits with incoherence — GPTQ matches or beats DiscQuant on several tasks). The paper's own captions say "comparable compression" for these settings. The narrative in the abstract and introduction should be qualified to reflect this.

- **No ablation of the linear regularizer (λ).** The paper attributes the success of DiscQuant to the linear term λ⟨c, x⟩ derived from discrepancy theory, yet there is no experiment comparing the full objective to the distillation-only objective (λ=0). Without this, the additive benefit of the discrepancy-inspired regularizer is unclear — the reader cannot tell whether the gains come from the regularizer or simply from global KL distillation (which GPTQ does not use). This is a directly addressable experiment that would significantly strengthen the paper.

- **First-order dominance claim rests on limited evidence.** Figure 3 shows the correlation between Δf and its first-order approximation for only one model (Phi-3-mini) at one bit width (4.25 bits) on one dataset (WikiText-2). While Table 1 supports the claim that per-sample gradients are nonzero, the direct validation of the first-order approximation's dominance would benefit from being shown across more settings.

- **Optimization hyperparameters are underspecified.** The paper does not report the learning rate, number of gradient steps, batch size, or exact number of calibration samples used in the main experiments (the data-mix experiment uses 8192, but this may not be the same across all settings). These details are important for reproducibility. (If they appear in the appendix, they should be cross-referenced in the main text.)

- **Theoretical bound is not instantiated empirically.** Theorem 3.3 depends on constants α, β, and λ₁, but the paper makes no attempt to estimate these from data or to check whether the m=8192 samples used in practice are close to the poly(log n / ε) required by the theorem. The bound remains a purely qualitative statement.

### Trivial

- The paper claims "all but O(m) weights are rounded" but does not empirically measure how many weights remain fractional after optimization or how RTN rounding of those few affects performance. A simple histogram of the fraction of weights at vertices would be informative.

## Nice-to-Haves

- A rough runtime/memory comparison (e.g., GPU-hours or wall-clock time for DiscQuant vs. GPTQ) would help practitioners weigh accuracy gains against computational cost. The paper mentions "similar memory requirements as knowledge distillation" but does not quantify time.
- The data-mix experiment (Figure 6) is interesting but preliminary — a more systematic study of calibration data selection for DiscQuant would be valuable.

## Removed Points

- *Missing experimental comparison to AdaRound/BRECQ*: Removed per the rule that the paper's choice of baselines is defensible within its class. GPTQ is the standard LLM rounding baseline; AdaRound and BRECQ target smaller vision models.
- *"Not enough models / tasks"*: The paper covers 7 tasks across 2 model families (3.8B and 8B parameters), which is a reasonable evaluation for a rounding method paper.
- *Strength "Verification of the low-rank gradient assumption"* from the Strength Finder: Removed because it conflicts with the verified weakness about JL-projected eigenvalues. The evidence for low-rank structure is weakened by the methodological concern with dimensionality reduction.

## Novel Insights

The most interesting tension that emerges from the reviews is the gap between what discrepancy theory can prove (the Lovett-Meka random walk guarantees generalization) and what a practical algorithm can actually do (SGD on KL divergence + linear regularizer). This gap is not a flaw unique to this paper — it reflects a broader challenge in connecting theoretical computer science results to deep learning practice. The paper's real contribution may be the geometric framing of rounding as finding a vertex of a polytope, which cleanly separates the *empirical* problem (satisfying m linear constraints) from the *generalization* problem (satisfying constraints on unseen data). Even if DiscQuant does not inherit the theorem's guarantees, the paper introduces a useful vocabulary for thinking about rounding that could inspire future work on provably good practical algorithms.

## Suggestions

1. **Ablate the linear regularizer**: Compare full DiscQuant vs. λ=0 (KL distillation only). This is the single most important experiment to add — it directly tests whether the discrepancy-theoretic component matters.
2. **Validate the eigenvalue decay without JL projection**: Compute the gradient covariance on a representative subset of parameters (e.g., one decoder layer) at full dimension, or justify why JL preserves the eigenvalue structure.
3. **Add optimization details**: Report learning rate, number of steps, batch size, and calibration set size for all main experiments.
4. **Qualify the abstract's claims**: Acknowledge that on incoherence-processed models, DiscQuant is comparable to (not uniformly superior to) GPTQ.
5. **Report the empirical fraction of rounded weights**: A simple measurement of how many coordinates converge to {0,1} would ground the "all but O(m)" claim.

## Score and Decision

This paper makes a genuine contribution: it brings a new theoretical perspective (discrepancy theory) to the PTQ rounding problem, proposes a practical algorithm that demonstrably improves upon GPTQ on block scaling, and provides clean geometric intuition. The weaknesses are real — the theory-algorithm connection is loose, the eigenvalue analysis is questionable, and key ablations are missing — but none invalidate the core empirical finding that DiscQuant outperforms GPTQ on standard block scaling quantization. The paper would be strengthened significantly by adding the λ ablation and fixing the eigenvalue analysis, but even as-is, it advances the state of knowledge. I recommend **weak accept**: the contributions are real, the framing is novel, and the empirical results are convincing for the block scaling setting. The authors should address the theory-algorithm gap and missing ablations in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>