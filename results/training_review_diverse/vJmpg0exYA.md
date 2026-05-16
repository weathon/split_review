Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces DiscQuant, a weight quantization method for neural networks inspired by discrepancy theory. The authors prove a generalization bound (Theorem 3.3) showing that a randomized rounding algorithm (Lovett–Meka) can round all but O(m) weights while keeping the expected squared linear error small when gradients are approximately low-rank. Inspired by this theory, they develop DiscQuant, a practical algorithm that minimizes a regularized KL divergence via projected SGD with a linear regularization term. Experiments on Phi-3-mini and Llama-3.1-8B show consistent improvements over GPTQ and RTN across multiple bitwidths and tasks — e.g., at 3.25 bits on GSM8k, DiscQuant achieves 64% vs GPTQ's 54% and RTN's 31%.

## Strengths

- **Novel theoretical perspective connecting discrepancy theory to quantization.** Theorem 3.3 provides a formal generalization bound for rounding under approximately low-rank gradients, with empirical validation of eigenvalue decay (Figure 4) and confirmation that per-sample gradients have large variance (Table 1), supporting the need for a first-order analysis. The geometric framework (polytope K, vertex rounding) is clearly motivated.

- **Consistent and often large empirical improvements over GPTQ and RTN.** Across two model families, multiple bitwidths (3–4.5 bits), and tasks (GSM8k, ARC Challenge, PIQA, HellaSwag, WinoGrande, MMLU), DiscQuant outperforms both baselines. At 4 bits on GSM8k, DiscQuant gives 77.3% vs GPTQ's 71.5% and RTN's 62.2% on Phi-3-mini; at 3.25 bits, the gap widens to 10+ points. Full recovery is achieved at 0.25–0.5 fewer bits per parameter than baselines on several tasks.

- **First-order perspective that challenges prior assumptions.** The paper directly demonstrates (Figure 3, Table 1) that per-sample gradients are large and the first-order Taylor term correlates strongly with Δf, contradicting the common assumption in prior work (Nagel et al., 2020; Hassibi et al., 1993) that first-order terms are negligible. This is an important empirical finding independent of the method.

- **Agnosticism to quantization grid and compatibility with preprocessing.** DiscQuant works with any scalar quantization grid and composes naturally with incoherence processing (Randomized Hadamard Transform), as demonstrated in Section 5.2 and Figure 5.

## Weaknesses

### Major

- **Theory–algorithm gap in the framing.** Theorem 3.3 provides a guarantee for the Lovett–Meka randomized rounding algorithm operating on constraints ⟨∇f(w;s_i), ŵ−w⟩ = 0. DiscQuant uses projected SGD on a KL divergence objective with a linear regularizer — a substantially different procedure. The paper acknowledges this gap explicitly (Section 4: "we could use the Lovett-Meka algorithm... But explicitly calculating all the gradients and storing them is infeasible. Instead a simple heuristic way...") and argues the KL divergence can be written in a form that fits the same framework (Eq. 2). However, the paper then states "Therefore, we can use the same techniques developed in Section 3 to solve this as well," which overstates the connection. The theoretical assumptions (eigenvalue decay, β-reasonableness) are validated for ∇f but not for ∇log p (the gradients that appear in the KL Hessian). The abstract's phrasing ("we prove that... we can round all but O(m) weights... Our proof... inspired DiscQuant") is accurate, but the paper would benefit from a clearer separation between the proven guarantee (for the idealized algorithm) and the heuristic status of DiscQuant. This does not invalidate the empirical contribution but weakens the claimed theoretical backing for the practical method.

### Minor

- **Missing optimization hyperparameters.** The paper does not specify the learning rate, batch size, number of optimization steps, or the value of λ for DiscQuant. These details are essential for reproducibility and understanding the algorithm's practical behavior.
- **No variance across quantization runs.** Standard errors are reported only from lm-evaluation-harness (evaluation-set noise), not from running the quantization process itself with different data subsamples or random seeds. Given the stochastic nature of the algorithm (data sampling, SGD), the stability of the results is unclear.
- **Missing ablations of key components.** The paper does not isolate the effect of the linear regularization term (c* vs random c vs λ=0) or the number of remaining fractional parameters at termination. These ablations would directly demonstrate whether the discrepancy-inspired component adds value beyond the KL objective alone.
- **No computational cost comparison.** The paper notes that DiscQuant has "similar memory requirements as knowledge distillation, which also requires two copies of the model" but does not report wall-clock time, GPU hours, or number of training steps relative to GPTQ. Since DiscQuant uses a distillation-style objective on batches of training data, it is expected to be more expensive; the trade-off should be explicit.
- **The gap from Theorem 3.3's bound (squared inner product) to the abstract's claim about |Δf| is not discussed.** Theorem 3.3 bounds (x−y)ᵀΣ(x−y), i.e., expected squared linear term, while the informal Theorem 1.1 claims E[|Δf|] ≤ ε. The relationship between these quantities requires additional assumptions (e.g., Lipschitz continuity of f or Cauchy–Schwarz) that are not stated.

### Trivial

- None beyond what is captured above.

## Nice-to-Haves

- A comparison to CDQuant (Nair & Suggala, 2024) on compatible models, if feasible, would strengthen the claim that DiscQuant is state-of-the-art among rounding methods.
- Broader analysis of the effect-of-data experiment (Figure 6) across more bit settings and models would increase its generalizability.
- A discussion of scenarios where the eigenvalue-decay assumption might fail (e.g., small models, tasks with high-dimensional gradient structure) would add completeness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper should note that the first-order dominance is an empirical observation, not a proven fact"** — The paper already presents Figure 3 as empirical evidence and does not claim it as a theorem. This is a strawman criticism.
- **"It is not clear whether the full gradient covariance exhibits similar decay" (about JL projection)** — The paper explicitly states it uses Johnson-Lindenstrauss projections to estimate eigenvalues (Figure 4 caption). This is a standard dimensionality reduction technique for covariance estimation. The critic's concern about projection missing structure is technically possible but not substantiated with evidence that it would change the conclusion.
- **"The paper should state explicitly that the KL divergence changes the distribution being considered"** — The paper does this thoroughly in Section 4 (lines 261–275), showing Lemma D.1 and deriving how minimizing KL corresponds to imposing constraints on log-probability gradients.
- **"Missing comparison to CDQuant and Behdin et al."** — The paper mentions both in Section 2.2, noting that CDQuant only has results on closed-source PaLM-2 with no released code, and Behdin et al. has results on different model families (OPT, BLOOM, Falcon). Experimental comparison across incompatible model families is not straightforward and the paper provides references.
- **"The paper should report wall-clock time and memory usage"** — The paper acknowledges memory requirements (two copies of the model) but does not report timing. This is a valid minor concern, not a major one. I have included it as a Minor weakness above (computational cost comparison) since the absence of timing data does not invalidate any core claim.

## Novel Insights

The harsh critic correctly identifies a real structural tension between the paper's theory (which applies to Lovett–Meka on loss gradients) and its practical algorithm (SGD on KL divergence). However, reading the paper carefully, this gap is narrower than the critic suggests: the KL divergence's Hessian is a covariance of log-probability gradients (Eq. 2), which places DiscQuant in the same geometric framework as the theory — the paper just does not empirically verify the eigenvalue decay and β-reasonableness assumptions for ∇log p specifically (only for ∇f). The deeper insight across both reviews is that DiscQuant's empirical success is robust enough to stand on its own as a practical contribution, even without a direct theorem guaranteeing its performance. The missing ablations (c* vs random c, λ sensitivity) would be the quickest path to resolving whether the discrepancy-theoretic motivation is actually driving the improvement or whether the KL distillation term alone accounts for the gains.

## Suggestions

1. Clearly separate the theoretical contribution (which is about Lovett–Meka with loss gradients) from DiscQuant (which is a heuristic inspired by that theory). State explicitly that DiscQuant does not inherit the theorem's guarantee.
2. Add ablations comparing DiscQuant with (a) λ=0 (KL only), (b) random c instead of c*, (c) different λ values, to isolate the contribution of the discrepancy-inspired linear regularization.
3. Report optimization hyperparameters (learning rate, batch size, number of steps, λ) and run the quantization process with multiple random seeds/data subsamples to report variance.
4. Report the computational cost of DiscQuant relative to GPTQ (GPU hours or wall-clock time) to contextualize the accuracy improvements.

## Score and Decision

**Originality:** 7/10 — Novel connection between discrepancy theory and quantization; the first-order perspective challenges prior assumptions. The practical method (KL + linear regularization) is relatively straightforward once the theory is in place.

**Importance of research question:** 8/10 — Quantization is critical for LLM deployment; improving rounding methods is an under-explored but impactful direction.

**Claims well-supported:** 5/10 — The theoretical claim (Theorem 3.3) is well-stated but its connection to DiscQuant is overstated. The empirical claim (DiscQuant outperforms GPTQ/RTN) is well-supported by the tables. Missing ablations and hyperparameters weaken reproducibility.

**Soundness of experiments:** 6/10 — Solid comparison across models, tasks, and bitwidths. Missing variance across quantization runs and missing computational cost comparison are gaps. Standard errors from lm-evaluation-harness are reported.

**Clarity of writing:** 7/10 — Well-structured with good intuition and geometric illustrations. Could be clearer about the theory–algorithm relationship.

**Value to the research community:** 7/10 — The discrepancy-theoretic perspective is novel and could inspire further work. The practical method shows meaningful gains. The first-order analysis (Figure 3, Table 1) is independently useful.

Overall: This paper makes a genuinely novel theoretical connection and demonstrates practically meaningful improvements over strong baselines. The main weakness is a framing issue (the theory applies to a different algorithm than the one tested) and missing experimental rigor (hyperparameters, variance, ablations, computational cost). These are addressable and do not undermine the empirical contribution. I recommend acceptance with the expectation that the authors address the theory–algorithm clarity and fill the experimental gaps.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>