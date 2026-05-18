Now I have all the information needed to write the consolidated review. Let me produce it.

## Summary

This paper proposes ZO-PoG, a black-box prompt learning framework that alternates between optimizing discrete prompts (via policy gradient with Gumbel-Softmax) and continuous prompts (via zeroth-order gradient in a low-dimensional subspace) for pre-trained language models. The method addresses the limitation that prior black-box prompt tuning methods (BBT, BDPL) only optimize one type of prompt. Experiments on 5 GLUE datasets across RoBERTa-large, GPT2-XL, and Llama3 show that ZO-PoG outperforms existing black-box prompt-learning baselines.

## Strengths

- **First collaborative framework for discrete + continuous black-box prompt optimization.** The paper is explicitly the first to jointly optimize both discrete text prompts and continuous embeddings in a black-box setting (Section 1). The ablation study (Figure 3) validates that removing either component degrades performance across all three backbone models and both prompt lengths, confirming the collaborative design is responsible for the gains.

- **Consistent empirical superiority across diverse backbones and tasks.** ZO-PoG outperforms all baselines (Manual Prompt, BBT, BDPL, SSPT) on 5 GLUE datasets for all three backbone models (Tables 1–3). For example, on WNLI with RoBERTa-large and prompt length 50, ZO-PoG improves by 5.17% over the best baseline, demonstrating practical significance.

- **Ablation study isolating the Gumbel-Softmax trick.** Figure 2 systematically compares ZO-PoG with and without the Gumbel-Softmax reparameterization under fixed conditions. The consistent improvement across all models and prompt lengths confirms that this specific smoothing technique (Eq. 4) reduces bias in the discrete prompt optimization, a technical refinement over the baseline BDPL method.

## Weaknesses

### Fatal
None.

### Major

- **The convergence analysis contains unaddressed technical gaps that undermine the theoretical claims.** Two issues compound each other:

  1. **ZO gradient estimator bias:** The two-point symmetric difference (Eq. 7, line 152–153) is an unbiased estimator of the gradient of the *Gaussian-smoothed* loss ℒ_μ(z) = 𝔼_u[ℒ(z+μu)], not of the original loss ℒ(z) (Nesterov & Spokoiny, 2017, Theorem 1). The gap between ∇ℒ_μ and ∇ℒ is O(μ²) and does not vanish without explicit handling. The paper presents this estimator (Section 3.3) and builds the convergence analysis (Section 4) without mentioning a smoothed objective or bounding this bias. Theorem 1 therefore does *not* establish convergence to a stationary point of the original loss under the stated assumptions.

  2. **Policy gradient baseline induces unaddressed bias:** The variance-reduced PG estimator (Eq. 6, line 140–141) uses the average of the *same* I samples as a baseline, creating dependence between the baseline and the sampled rewards. This breaks the unbiasedness property that REINFORCE with a constant baseline would enjoy. Proposition 1 bounds the variance but does not discuss the bias, and the convergence analysis relies on (near-)unbiased gradient estimates.

  The theoretical contribution is advertised as a main result ("we formally establish the convergence of our framework"). These gaps mean the convergence guarantee as written is not technically supportable. The empirical contributions are unaffected, but the theory is a stated contribution and cannot be accepted in its current form without substantial revision (either fixing the analysis to handle the smoothed objective and the PG bias, or being transparently scoped as a heuristic with experimental validation only).

### Minor

- **BBTv2 discussed in Related Work but omitted from the experimental comparison.** The paper mentions BBTv2 (line 144–146: "an improved version of BBT, optimizes prompts across all layers... achieving few-shot learning performance comparable to full model tuning") but does not include it among the baselines in Section 5.1. Since BBTv2 represents a stronger version of the BBT baseline, its omission weakens the claim that ZO-PoG advances the state of the art in black-box prompt tuning. The authors should either include BBTv2 or provide a clear methodological reason for its exclusion.

- **Claim of reduced computational expense is unquantified.** The abstract and conclusion state that ZO-PoG "reduc[es] the computational expense" but no forward-pass counts, wall-clock times, or query budgets are reported. Remark 3 gives an asymptotic query complexity bound, but the actual cost for the specific experimental setups is never measured or compared against baselines. Without this data, the efficiency claim is rhetorical rather than empirical.

- **Only 3 random seeds are used.** While this is somewhat common for LLM experiments given computational costs, prompt learning methods are known to exhibit variance across seeds. At minimum, the authors should acknowledge this limitation.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis for the smoothing parameter μ and the ZO sample count I₂ (the most critical hyperparameters for the continuous optimization) would strengthen the empirical contribution.
- If the CoLA results for decoder-only models show a known limitation, adding a small analysis or discussion of whether ZO-PoG narrows the gap compared to BBT/BDPL on that dataset would be informative.

## Removed Points
These points from the original reviews are removed or reclassified for the following reasons:

- **Missing hyperparameter values (I₁, I₂, η_α, η_z, μ, τ, subspace dimension d):** These may be present in the appendix, which is stripped by the parser. Per instructions, missing appendix content is not treated as a weakness.
- **Missing specification of the projection matrix A construction:** Same rationale — likely in the appendix.
- **Reproducibility concerns phrased as "cannot be reproduced or independently verified":** This conflates missing-in-main-text details (possibly in appendix) with true unreproducibility. The code is provided at an anonymous URL.
- **Strength from Strength Finder about "formal convergence guarantee":** This strength is retained but with caveats, since the theory has verified gaps.

## Novel Insights
The most interesting observation from the reviews is the interplay between two distinct biases in the optimization: the ZO gradient estimator's inherent bias toward the smoothed objective (controlled by μ) and the PG baseline's dependence bias (controlled by I). These operate on different components of the alternating optimization but interact through the shared loss function. The paper's current analysis treats them independently, but a unified treatment that accounts for both biases simultaneously while bounding their combined effect on the alternating optimization dynamics could yield a genuinely non-trivial theoretical result — one that goes beyond standard ZO or PG analysis individually.

## Suggestions
1. **Fix or drop the convergence analysis.** Either rewrite Section 4 to properly analyze convergence to a stationary point of the smoothed objective (with the bias bounded as O(μ²L²d)) and account for the PG baseline bias, or remove the theoretical claims and let the empirical work stand on its own.
2. **Include BBTv2 as a baseline** or provide a justification for its omission.
3. **Report forward-pass counts or wall-clock time** for all methods to substantiate the efficiency claim.
4. **Provide a table of hyperparameter values** (I₁, I₂, η_α, η_z, μ, τ, subspace dimension d) — if not already in the appendix, add them to the main text.
5. **Add a discussion of the PG baseline bias** (Eq. 6) and its dependence on I, even if only to note that it's O(1/I) and controlled in practice.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>