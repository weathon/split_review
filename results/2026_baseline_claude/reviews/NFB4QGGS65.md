## Summary
This paper establishes that GPTQ, when executed back-to-front (last to first dimension), is mathematically identical to Babai's nearest plane algorithm for the Closest Vector Problem (CVP) on a lattice defined by the layer's Hessian matrix. From this equivalence, the paper derives a tight layer-wise error bound for GPTQ under no-clipping, proposes two practical no-clipping quantization methods (SSQR and HPTQ) that outperform vanilla GPTQ, and provides efficient CUDA inference kernels achieving approximately 2× end-to-end speedup over BF16.

## Strengths
- **Novel, non-trivial theoretical result with full proofs**: The equivalence GPTQ↔Babai is demonstrated both geometrically (Theorem 2, 4) and algebraically. The proof requires carefully tracking cumulative quantization error, rewriting the GPTQ update in reversed order, and showing step-wise rounding coincides. This is a sophisticated argument, not a straightforward observation.
- **Tight error bound with clear consequences**: Theorem 5 delivers a tight absolute error bound expressed as a quadratic form over the LDL diagonal of the permuted Hessian, and confirms it is tight (achieved when the target lies at the corner of the Babai cuboid). This goes beyond vague approximation guarantees and directly informs scale selection.
- **Theory drives practice**: The no-clipping constraint is not just a theoretical artifact—the paper shows concretely that it motivates HPTQ (Huffman-encoded integers) and SSQR (scale-adjusted sparse outlier handling), both of which yield better perplexity than standard GPTQ at the same effective bitwidth on Qwen3 and Llama families.
- **GPU kernels with measured speedups**: The SSQR CUDA kernel for Ampere achieves ~2× TPOT speedup across inlier bitwidths (2–4 bit) and outlier rates (0–5%) on Qwen3-8B, providing direct practical value.
- **Elegant CVP dictionary (Table 1)**: The mapping between quantization concepts (activations, scales, quantized integers) and CVP concepts (lattice basis, coordinates) is clean and immediately useful to both communities.

## Weaknesses
### Fatal
None.

### Major
- **The no-clipping constraint is the core limitation of the error bound, but standard INT4 GPTQ always clips**: Theorem 5 strictly requires $\mathbb{Z}_\dagger = \mathbb{Z}$. Standard GPTQ uses $\mathbb{Z}_\dagger = \{-8,\ldots,7\}$, meaning the central theoretical result (the error bound) does not directly apply to GPTQ as deployed in practice. The paper proposes SSQR and HPTQ as alternatives, but these are new methods, not analyses of GPTQ-as-deployed. The gap between "GPTQ has Babai's guarantee" (in the no-clipping idealization) and what practitioners care about (clipped INT4) should be quantified empirically, not just acknowledged.
- **Min-pivot contributes only modestly**: The paper positions the min-pivot order (Algorithm 3) as a principled improvement over act-order based on the error bound and explicitly acknowledges "downstream accuracy gains are modest." Given that the cubic-complexity computation is not free and act-order is already near-optimal when the Hessian is well-conditioned, this contribution is weak and creates a mismatch between theoretical motivation and empirical payoff.

### Minor
- **The back-to-front direction is called "superficial" but requires a change to the standard implementation**: The original GPTQ runs front-to-back. Running back-to-front produces numerically identical representations (the grid is symmetric) only up to a permutation of the error. The paper asserts this is superficial and provides an argument, but does not empirically verify that back-to-front GPTQ achieves the same accuracy as front-to-back GPTQ when clipping is present, which would validate the claim in a practical setting.
- **QuIP overlap**: The related work section states QuIP already "proves an error guarantee for GPTQ and proposes the LDLQ method as an equivalent variant of GPTQ." The current paper provides a deeper geometric interpretation and explicit connection to Babai's algorithm, but the extent to which the theoretical novelty over QuIP is quantified could be clearer.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing back-to-front GPTQ vs. front-to-back GPTQ for standard INT4 (clipped) to empirically verify that the direction reversal is indeed neutral in the clipping regime.
- A brief theoretical sketch (or reference to existing results) on what Babai's bound becomes with a bounded integer grid, to bridge the gap between theory and standard INT4 GPTQ.

## Novel Insights
The paper's central insight—that LLM weight quantization is an instance of CVP and that GPTQ is already performing Babai's nearest plane algorithm (without basis reduction) on the Hessian's lattice—is a genuine conceptual bridge between two fields. The geometric interpretation of error propagation as an orthogonal projection onto a nearest hyperplane (Theorem 2) is particularly illuminating: it explains both why the greedy local rule works well globally (it is executing a classical lattice algorithm) and why GPTQ's error is bounded (it inherits Babai's tight cuboid guarantee). The observation that any subsequent GPTQ-style correction after a complete Babai sweep is algebraically redundant (Section 4.3, "Ineffectiveness of composing algorithms") is a subtle but clean result that confirms the algorithm is already fully exploiting the structure.

## Suggestions
- Empirically measure the absolute error bound from Theorem 5 on real layers (before and after GPTQ) and compare it to the actual quantization error observed. Even for the no-clipping HPTQ setting, comparing the bound tightness vs. average-case would strengthen trust in its practical utility.
- For HPTQ's Huffman representation, provide memory layout details (decoding overhead during inference), since the decoding step is the major latency concern—this is currently mentioned only at a high level.
- Discuss whether basis reduction (LLL applied to the Hessian lattice) is computationally feasible even for small groups; this would directly extend the theory to potentially better-than-Babai quantizers, which the closing remarks identify as future work.

## Score and Decision
The paper makes a clean and significant theoretical contribution by rigorously identifying GPTQ as Babai's nearest plane algorithm and deriving a tight error bound. The proofs are non-trivial, the lattice-theoretic framing opens a productive two-way bridge, and the practical methods with GPU kernels demonstrate real benefit. The main limitation—that the error guarantee is confined to the no-clipping regime—is acknowledged and partially addressed, but creates a gap with standard GPTQ usage. Overall this is a high-quality theory-meets-practice paper of clear value to the community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>