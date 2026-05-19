- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3
Now I have everything I need. Let me produce the final consolidated review.

---

## Summary

TimeDART proposes a self-supervised learning framework for time series forecasting that combines a causal Transformer encoder (capturing inter-patch, global dependencies via auto-regressive generation) with a denoising decoder (capturing intra-patch, local detail features via additive noise and reconstruction). Pre-training optimizes the model to reconstruct clean patches from noise-added patches in an auto-regressive manner; the denoising decoder is then discarded and a prediction head is fine-tuned. The method achieves strong empirical results: 43 out of 64 best metrics across 8 datasets (Table 1), with ablation experiments confirming that both the auto-regressive and denoising components contribute meaningfully.

## Strengths

1. **Strong and consistent empirical results across diverse benchmarks.** TimeDART achieves the best result in 43 of 64 evaluation settings (Table 1), spanning 8 datasets with 4 prediction horizons and 2 metrics. The "#1 Counts" row (43 for TimeDART vs. 10 for the next-best SimMTM) provides concrete quantitative evidence of the method's practical forecasting performance. The advantage is not limited to one dataset type but holds across energy, weather, transportation, and finance domains.

2. **Ablation study confirms the necessity of both proposed components.** The ablation results (Section 4.3, Table 3) isolate the contributions of the auto-regressive mechanism and the denoising module. Removing the auto-regressive mechanism ("w/o AR") increases MSE on ETTh2 from 0.346 to 0.365, ETTm2 from 0.257 to 0.281, and Electricity from 0.163 to 0.193 — in some cases worse than random initialization. Removing the denoising module ("w/o Diff") also degrades performance (ETTm2: 0.257→0.265). This directly supports the claim that both components are individually necessary.

3. **Cross-domain pre-training demonstrates transferable representations.** TimeDART pre-trained on five energy-domain datasets and fine-tuned on each (Table 2) outperforms random initialization on all five (e.g., ETTh2: 0.343 vs. 0.363 MSE, Electricity: 0.162 vs. 0.166). On ETTh2 and ETTh1, cross-domain performance even surpasses in-domain results, providing direct evidence of generalization ability.

4. **Principled design choice of non-overlapping patches.** Setting patch length equal to stride (Section 3.2.1) is technically justified to prevent future-step information leakage while preserving the auto-regressive property — a concrete design decision with clear reasoning.

## Weaknesses

### Fatal
None.

### Major

1. **The "diffusion model" claim is substantially overblown; the mechanism is a denoising autoencoder with variable noise levels, not a proper diffusion process.** Three specific problems verifiable from the paper text:

   - **No timestep conditioning.** The decoder input (Eq. 96-98) is `Embedding(noisy_patch) + PE`, with no timestep embedding `s` anywhere in the architecture (Section 3.2.3, lines 101-108). In any standard diffusion model (DDPM, score-based), the model must receive the current noise level to know how much denoising is needed. Without this, the decoder treats all noise levels identically.
   
   - **Single-step reconstruction, not iterative refinement.** The "forward process" (lines 84-87) directly samples `x_j^s` from the closed-form `q(x_j^s|x_j^0)` in a single step, and the "reverse process" (lines 101-108) is a single reconstruction step. There is no Markov chain of denoising steps — the defining characteristic of diffusion models.
   
   - **Loss misrepresented as the ELBO.** Line 115-117 states the loss is "equivalent to the Evidence Lower Bound (ELBO)" but the actual loss is `L = Σ_j E[||x_j^0 - reconstruction||^2]`. This is a standard denoising autoencoder loss, not the ELBO of a multi-step diffusion process (which would require timestep-conditioned predictions summed over the Markov chain).

   **Why this matters:** The paper's title, abstract, and contribution claims hinge on the integration of "diffusion" with auto-regressive modeling. The actual method is a valid and apparently effective *denoising autoencoder* combined with auto-regressive generation, but the diffusion framing oversells the novelty and is technically inaccurate. The empirical results remain valuable, but the contribution needs honest reframing.

2. **No statistical significance or variance reporting.** All results in Tables 1-3 are single-point MSE/MAE without standard deviations, confidence intervals, or mention of multiple seeds. In time series forecasting with Transformers, performance varies across runs due to random initialization and data splits. Many of TimeDART's margins are small (e.g., 0.132 vs 0.133 on Electricity horizon 96; 0.193 vs 0.191 on Weather horizon 192). Without variance information, it is impossible to assess whether these differences are meaningful or noise. This weakens the central claim of state-of-the-art performance.

### Minor

1. **The cross-attention decoder's claimed "adjustable optimization difficulty" is asserted but not demonstrated.** The paper claims (line 23, Section 3.2.3) that the cross-attention design enables "flexible and adaptive noise reduction" and "adjustable optimization difficulty," but no experiment isolates this property. The hyperparameter analysis of decoder layers (Figure 2) shows a trade-off in layer count but does not compare cross-attention against simpler alternatives (e.g., an MLP denoiser with matched parameters) to verify that cross-attention specifically provides the claimed benefit.

2. **Missing comparison against diffusion-based time series methods.** Diffusion-TS is cited in Related Work (line 32) as a diffusion-based time series generative model but is not included as a baseline. Since the paper's framing centers on integrating "diffusion" into self-supervised forecasting, a comparison — even if adapted for the same task — would help contextualize the contribution.

3. **The main experiments do not specify which diffusion step budget T was used.** The hyperparameter analysis (Section 4.4) varies T ∈ {750, 1000, 1250}, but the main results (Section 4.2) never state the chosen value. While T=1000 can be inferred as optimal from the sensitivity analysis, the omission is an experimental reporting gap.

4. **Coarseness of the "w/o AR" ablation.** Removing the auto-regressive mechanism simultaneously eliminates both the causal mask in the encoder and the decoder mask (Section 4.3). The paper does not ablate these separately, making it unclear whether the benefit comes from the causal structure of the encoder, the decoder attention pattern, or both.

### Trivial
None.

## Nice-to-Haves

- Including Diffusion-TS as a baseline (or at least discussing why it is not comparable) would strengthen the positioning.
- A comparison of the cross-attention denoising decoder against simpler alternatives (MLP denoiser) would substantiate the "adjustable difficulty" claim.
- Separately ablating the causal mask and the decoder mask would give finer-grained insight into the auto-regressive mechanism.

## Removed Points

These points were flagged but do not belong in the main review:

- **"The paper does not specify the number of encoder layers, hidden dimension, number of heads, training hyperparameters..."** — The paper states the encoder is "fixed at 2 layers for all datasets" (line 322). Other training specifics (learning rate, batch size, epochs) are standard details that may reside in a stripped appendix or official code repository. Per rule, nitpicks about undisclosed hyperparameters are removed; this level of detail is impractical to include in a conference paper body.
  
- **"Missing visualization of predictions"** — The paper explicitly references a visualization section (`Section~\ref{sec:visual}` at line 166), which was likely in a section stripped by the PDF parser. The parser removes appendix content from all papers.
  
- **"The paper does not mention computational cost or training time."** — A useful addition but not a required component for evaluating the paper's core contribution. This is a generic scope-expansion request.
  
- **"The non-overlapping patches trade-off is not discussed."** — The paper explicitly justifies non-overlapping patches as a design choice to preserve the auto-regressive property (Section 3.2.1, line 64). Asking for expanded discussion of a trade-off the authors already acknowledged and justified is scope creep.
  
- **"The paper does not report shared hyperparameters (layers, hidden dimension, etc.) for the baselines."** — The paper states it uses "a unified encoder for all representation networks" (line 158) and that implementations are "based on their official repositories." This is a standard and reasonable approach; the baselines are used with their own optimal configurations.
  
- **"Related work coverage is missing works."** — Per rule, I cannot confirm the existence of unmentioned references and should not penalize missing related works.

- Strengths removed from the Strength Finder that are generic or conflict with weaknesses: The strength about "non-overlapping patches" is a valid design point but its characterization as a "strength" is somewhat overblown — it's a standard design choice with clear reasoning, moved here for calibration.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a significant gap between the paper's framing ("diffusion model") and its actual implementation (denoising autoencoder), but this is a critical reframing observation rather than a novel insight about time series forecasting. The empirical finding that combining auto-regressive generation with patch-level denoising outperforms prior SSL methods is the paper's own contribution, not something the reviews uncovered.

## Suggestions

1. **Rebrand the denoising component honestly.** Rename the "denoising diffusion model" to a "denoising autoencoder with variable noise levels." Remove claims about the loss being the "ELBO" — it is MSE. Add explicit timestep embeddings to the decoder to make the model a proper diffusion model, or drop the diffusion terminology entirely. The empirical results are strong enough that the paper does not need to inflate its framing.

2. **Add variance estimates.** Report means and standard deviations over at least 3-5 random seeds for all key experiments (Tables 1-3). Without these, the claimed SOTA margins cannot be evaluated for statistical significance.

3. **Specify the diffusion step budget T used in main experiments** in Section 4.2, not just in the hyperparameter analysis.
