Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces DiscQuant, a weight-rounding algorithm for LLM quantization inspired by discrepancy theory. It proves a generalization bound (Theorem 3.3): under polynomial eigenvalue decay of the gradient covariance, with m = poly(log n/ε) samples, all but O(m) weights can be rounded while bounding the expected first-order approximation error. The practical DiscQuant algorithm minimizes KL divergence between original and quantized model outputs plus a linear regularizer, using projected SGD. Experiments on Phi-3-mini-3.8B and Llama-3.1-8B across multiple tasks show consistent improvements over GPTQ and RTN, e.g., 64% vs. 54% (GPTQ) vs. 31% (RTN) GSM8k at 3.25 bits.

## Strengths

- **Novel theoretical framework connecting discrepancy theory to LLM quantization.** Theorem 3.3 provides a generalization guarantee for rounding under a low-rank gradient covariance assumption — a perspective absent in prior rounding work. This is a genuine theoretical contribution that goes beyond the heuristic motivation typical of this area.

- **Strong and consistent empirical gains over GPTQ and RTN.** On Phi-3-mini at 4 bits: DiscQuant achieves 77.3% GSM8k vs. GPTQ's 71.5% and RTN's 62.2%. The improvement holds across two model families, multiple bit-widths, and both block scaling and incoherence processing grids. DiscQuant achieves full recovery with 0.25–0.5 fewer bits per parameter on several tasks.

- **Agnostic to quantization grid and composable with other PTQ techniques.** DiscQuant works with any scalar quantization grid, and the experiments demonstrate this by composing it with both block scaling and incoherence processing. This modularity is practically useful.

- **Data-mixing analysis (Figure 6) provides actionable insight.** The controlled study shows task-specific performance can be tuned by adjusting calibration data composition — a practical finding for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The empirical validation of the low-rank gradient assumption is methodologically questionable.**  
   Figure 4 reports eigenvalues of the gradient covariance after projecting gradients to 2048 dimensions via Johnson-Lindenstrauss projections. The eigenvalue spectrum of a random low-dimensional projection does not, in general, reflect the spectrum of the original high-dimensional covariance — random projection mixes eigenvalues in ways that can distort or disguise the true decay pattern. The paper offers no justification that the projection preserves the relevant spectral properties, nor does it provide alternative evidence (e.g., estimating the spectrum on a single layer with its full parameter count). Since the entire theoretical framework (Theorem 3.3) rests on this eigenvalue decay assumption, and Figure 4 is the primary empirical support for it, this is a significant gap in the evidence chain.

2. **The informal theorem statement (Theorem 1.1) overclaims relative to the formal result.**  
   Theorem 1.1 (informal) states the bound applies to E[|Δf|] — the actual loss change. The formal Theorem 3.3 bounds E[⟨g, x-y⟩²], which is the expected *squared first-order term* only. While the paper argues higher-order terms are small due to fine quantization grids (line 202), this is not quantified or incorporated into the theorem. The informal claim therefore promises more than the formal analysis delivers, and the theorem does not provide an end-to-end guarantee on the quantized model's actual performance.

### Minor

3. **The theory-algorithm connection, while acknowledged as heuristic, could be more precisely characterized.**  
   The theory (Section 3) operates with exact linear constraints ⟨∇_w f(w;s_i), ŵ − w⟩ = 0 defining an affine subspace V, and uses the Lovett-Meka random walk to find a vertex of V∩[0,1]ⁿ with generalization guarantees. The practical algorithm replaces this with KL divergence minimization (a quadratic penalty over *expectations* of squared inner products) plus a linear term optimized via SGD. The paper does call this a "simple heuristic" (line 275), but then states "Therefore, we can use the same techniques developed in Section 3 to solve this as well" (line 275), which overstates the reduction. The algorithm's success is empirically demonstrated, but the claim that it is "guided by our theoretical analysis" (line 109) is looser than a reader might assume.

4. **The regularization parameter λ is introduced without any discussion of its choice or sensitivity.**  
   The objective in (3) balances the linear rounding term and the KL distillation term via λ > 0. No ablation, sweep, or heuristic for setting λ is reported. Given that the optimization's behavior likely depends on this trade-off, the lack of information hinders reproducibility and understanding.

### Trivial
- The informal Theorem 1.1 uses |Δf| while the formal Theorem 3.3 bounds 𝔼[⟨g, x-y⟩²]. The mismatch between these should be resolved in revision for clarity.

## Nice-to-Haves

- **Runtime and memory profiling.** The paper notes DiscQuant requires two model copies (like knowledge distillation) and does not report wall-clock time. For practical adoption, timing comparisons against GPTQ (which is layer-wise and fast) would strengthen the paper's utility claims.

- **Multi-seed quantization runs.** Reporting results from multiple quantization runs with different calibration subsets would strengthen statistical claims. (The evaluation harness standard errors are reported, but these reflect evaluation variance, not variance from the quantization process itself.)

- **Sensitivity analysis for the linear coefficient c\*.** The paper's innovation of using c\* = (1−2y) to find the vertex closest to original weights is elegant, but the approximation x_i² ≈ x_i relies on x being "almost integral." A brief empirical check of how many coordinates remain fractional before RTN is applied would clarify how well this approximation holds.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing CDQuant/AdaRound baselines.** The paper explicitly explains that CDQuant "only has results on the closed source PaLM-2 models with no released code" and that AdaRound-style methods are "layer by layer" while DiscQuant rounds "the entire model at once." The reviewer's complaint ignores these explanations; comparing against methods with incompatible experimental setups would be apples-to-oranges.

- **Incoherence processing discussion is insufficient.** The paper states "Incoherence especially helps GPTQ at 3 bits, and for Phi-3 DiscQuant without incoherence is competitive to GPTQ with incoherence" (line 326). This directly addresses the observation the reviewer claims is missing.

- **Missing appendix content (hyperparameters, optimizer settings, calibration sample counts).** Per policy, these sections exist in the original submission and were stripped by the PDF parser. The paper references Algorithm B.2 and Lemma D.1 in the appendix.

- **Criticism that the theory-algorithm gap is unacknowledged.** The paper explicitly calls the algorithm a "simple heuristic" (line 275) and uses the phrase "inspired by" rather than "implements" — the acknowledgment is present, though the reviewer correctly notes the framing could be tighter.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the finding that DiscQuant without incoherence processing is competitive with GPTQ *with* incoherence processing (line 326) suggests DiscQuant inherently handles weight outliers that other methods need separate preprocessing for. This is a potentially important property that the paper does not highlight or explore, and it opens an interesting question about *why* DiscQuant's objective (KL divergence over output distributions) naturally handles outlier weights while GPTQ's layer-wise reconstruction objective does not.

## Suggestions

1. **Fix the eigenvalue decay validation.** Either (a) estimate the full covariance on a tractable subset of parameters (e.g., one attention layer with its full ≈1M parameters) using enough samples to get a reliable spectrum, or (b) provide a theoretical argument that JL projections approximately preserve eigenvalue decay for matrices with polynomially decaying spectra, or (c) replace the JL projection with a more principled spectral approximation (e.g., randomized SVD which has known guarantees for recovering the top eigenvalues and the overall decay shape).

2. **Align the informal and formal theorem statements.** Either make Theorem 1.1 explicitly reference the first-order bound and note the higher-order terms are assumed negligible, or extend Theorem 3.3 to incorporate a bound on the second-order term under the fine-grid assumption.

3. **Clarify the theory-algorithm mapping in Section 4.** Add a short paragraph explaining: the KL divergence's Hessian equals the gradient covariance → minimizing the quadratic form (ŵ−w)ᵀH_w(ŵ−w) encourages ⟨∇log p, ŵ−w⟩ ≈ 0 in expectation → this replaces the exact linear constraints in the theory → the linear term ⟨c, x⟩ encourages vertex-finding. A clear "this is what the theory strictly guarantees, and this is where we depart from guarantees for practical reasons" would strengthen the paper.

4. **Report how λ was chosen** (e.g., a sweep description or a simple heuristic) and ideally include a brief sensitivity table showing the effect of λ on one representative setting.

## Score and Decision

**Originality:** High — discrepancy theory is novel in this application. **Importance:** High — LLM quantization is practically relevant. **Claims support:** Moderate — the theory is sound within its assumptions, but the key assumption's empirical validation is weak, and informal claims slightly outrun the formal results. **Soundness:** Moderate — Theorem 3.3 appears sound, the experiments are well-designed, but the JL projection methodology for Figure 4 is not justified. **Clarity:** Moderate — well-structured but the theory-algorithm gap is under-discussed. **Value:** Moderate-High — the algorithm itself is practically useful and clearly outperforms strong baselines.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>