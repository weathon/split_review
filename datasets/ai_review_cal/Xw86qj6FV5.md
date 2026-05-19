- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 8, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

CaLMFlow reformulates flow matching as a Volterra integral equation (VIE) and uses a causal language model (CLM) to solve it autoregressively, enabling text-conditioned continuous data generation without discrete tokenization. The framework introduces spatiotemporal and multi-trajectory tokenization along with variational decoding for continuous token prediction. The paper demonstrates strong results on synthetic high-dimensional benchmarks and single-cell perturbation prediction, outperforming CFM variants and specialized single-cell models.

## Strengths

- **Demonstrated superiority over ODE-based flow matching in high dimensions (Table 1)**: On 1000-dimensional synthetic problems, CaLMFlow achieves MMD values of 0.014–0.261 versus CFM's 0.363–0.493 and 2-Wasserstein distances roughly 2–3× lower. The gap is consistent across three distribution pairs and both 100D and 1000D settings, providing clear evidence that the VIE+CLM approach handles high-dimensional flows better than the ODE-based CFM variants.

- **Text-conditional single-cell perturbation prediction is genuinely effective (Tables 3, 4)**: CaLMFlow with natural language pretraining achieves MMD 0.0181 vs. CFM 0.1105 (6× lower), and R² of 0.99 on held-out condition mean expression. Even the randomly initialized CaLMFlow (R.I.) — which uses no pretrained language understanding — outperforms CFM (MMD 0.0350 vs. 0.1105), demonstrating that the generative framework itself (VIE+CLM) provides a meaningful advantage independent of pretrained embeddings.

- **Multi-trajectory tokenization provides a capability unique to this approach**: Tables 2, 5, and 6 show that providing multiple flow trajectories as context monotonically improves generation quality (e.g., 2-Wass dropping from 5.66→3.61 for 1→8 trajectories on 2→4 Gaussians). This is a capability that CFM cannot natively model (as the paper notes), and the empirical evidence for the benefit is well-supported.

- **Ablation studies confirm the necessity of key components**: The temperature ablation (Fig. 3) shows that removing the VAE component severely degrades performance, confirming its role in continuous token generation. The time-point ablation (Fig. 4) shows monotonic improvement with finer discretization, consistent with the VIE formulation. The spatial token ablation on MNIST (Table 5) shows a clear trend from 8.97 to 9.43 inception score when increasing from 1 to 8 space tokens.

## Weaknesses

### Fatal

None.

### Major

- **The VIE formulation's benefit is not isolated from architectural confounders**: CaLMFlow uses a large transformer (Pythia, 768-dim embeddings) trained with multi-step autoregressive prediction, while CFM baselines use a presumably smaller MLP trained with ODE-style single-step vector field prediction. The paper lacks an ablation where the same CLM backbone is trained to predict the next state from *only the current state* (an ODE-style formulation), which would isolate whether the performance gain comes from the VIE's integral formulation, from the larger model capacity, or simply from the autoregressive multi-step context. This is the most important missing control for the paper's core claim.

- **Suspiciously high R² values on held-out conditions are not discussed**: CaLMFlow achieves R² ≈ 0.99 on both full-cell and top-100-DE-gene mean expression for held-out perturbation combinations. While high R² values are possible (especially when operating on the 1000-PC space), the paper does not discuss potential data leakage from overlapping individual attributes (cell types, perturbations, chronicities) between training and test combinations, nor does it analyze why values at this level are plausible. The baselines (e.g., CFM-OT at 0.84) are also fairly strong, so the gap to 0.99 is notable and warrants explanation.

### Minor

- **Conditioning modality is not controlled for in baselines**: CaLMFlow conditions on text prompts processed through a pretrained LLM's tokenizer+embedding, giving it rich semantic representations. Baselines (CFM, scVI, scGPT, CPA) use one-hot or learned label encodings. Although the R.I. vs. N.L. comparison helps disentangle the value of pretrained embeddings from the generative framework, a controlled comparison (e.g., giving CFM the same text embeddings, or CaLMFlow one-hot encodings) would better separate the contribution of the generative method from the conditioning modality.

- **Computational cost is not reported despite scalability claims**: The abstract and introduction claim "scalability, flexibility, and context-awareness," but no FLOPs, wall-clock inference time, or parameter counts are provided for any method. CaLMFlow requires multiple forward passes through a large LLM during autoregressive inference (one per time step), which is likely expensive relative to CFM's ODE-based sampling. The scalability claim is unsupported.

- **Exposure bias not addressed**: The paper acknowledges the teacher-forcing/inference mismatch (line 90: "next-token prediction in CLMs is simulation-free during training... Full trajectory simulation occurs only during inference") but does not analyze error accumulation or discuss mitigation strategies (e.g., scheduled sampling, iterative refinement).

- **Multi-trajectory cost not discussed**: The paper shows that 5 or 8 trajectories improve results, but does not discuss the increased training/inference cost, how the number of trajectories is selected, or whether this benefit generalizes beyond the tested settings.

### Trivial

- The temperature ablation shows optimal τ = 0.2 only for the 8-Gaussians→2-Moons dataset; the paper should note that this may be dataset-dependent.
- The MNIST improvement (9.43 vs. 8.94 for CFM) is modest; the paper could be more measured in claiming "superior performance" on this task.

## Nice-to-Haves

- An ablation feeding text embeddings to CFM baselines (or using one-hot encodings for CaLMFlow) would cleanly separate the generative method contribution from the conditioning modality contribution.
- Reporting the specific number of time steps and ODE solver settings used in experiments (likely detailed in the appendix, which was stripped by the parser; if so these details are already present in the submission).
- A formal analysis of exposure bias in CaLMFlow's autoregressive inference process.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing hyperparameter details (solver steps, time steps, ODE config)"**: The paper's reproducibility statement (line 487) explicitly says experimental implementations and metric computations are detailed in the appendices, which were stripped by the parser. These details exist in the original submission. *Rule: REMOVE weaknesses about missing appendix content.*

- **"Stiffness not proven with eigenvalue analysis"**: The paper motivates VIEs as offering greater numerical stability than ODEs via citations; the empirical results (CFM degrading at high dimensions while CaLMFlow does not) provide supporting evidence consistent with this claim. A formal stiffness analysis would strengthen the paper but is not required to make the empirical comparison valid.

- **"Token ordering ablation missing"**: The token ordering (flow, space, time) is a design choice, not a core contribution. Ablating all permutations would be a useful addition but is not a weakness in the current evaluation.

- **"scVI and scGPT are not flow-based methods"**: The paper uses them as baselines for single-cell generation, which is standard practice. The comparison on distributional metrics (MMD, 2-Wass) is appropriate.

- **"Leiden KLD not defined"**: Leiden KLD is a standard metric in single-cell analysis (commonly used in scGPT and scVI papers). The paper's use is appropriate in context.

- **Missing related work on autoregressive continuous data models (PixelCNN, WaveNet, etc.)**: Per the rules, missing related works should not be mentioned as I cannot verify their relevance without external sources.

## Novel Insights

The harsh critic correctly identifies that the paper's evaluation conflates multiple factors (model capacity, conditioning modality, VIE formulation, autoregressive context) but does not adequately recognize that the paper already provides some partial controls — namely the R.I. vs. N.L. comparison, which shows that even without pretrained language understanding, the VIE+CLM framework outperforms baselines. The more subtle observation is that the multi-trajectory tokenization (a capability unique to this approach) provides the clearest and most uncontaminated evidence for the method's value, since no baseline can natively model multiple flow trajectories, and the results show consistent monotonic improvement. This suggests the most compelling future direction may not be the VIE formulation per se, but the ability to process multiple trajectories jointly via the CLM's causal attention.

## Suggestions

1. **Isolate the VIE formulation**: Train the same CLM backbone in an ODE-style mode (predict next state from only the current state) and compare to the VIE-style mode (predict from full history). This single ablation would directly address the core concern about what drives the performance gain.

2. **Analyze held-out condition predictions**: Provide an analysis of whether the high R² (~0.99) is driven by compositional generalization (individual labels appearing in training but in different combinations) or by genuine generalization to completely unseen conditions. If the former, discuss whether this is expected and acceptable.

3. **Add runtime comparisons**: Report wall-clock inference time and parameter counts for all methods to substantiate the scalability claim.

4. **Control for conditioning modality**: Either feed text embeddings to CFM baselines or use one-hot encodings for CaLMFlow, to separate the benefit of the generative framework from the benefit of richer conditioning signals.

5. **Discuss exposure bias**: Measure error accumulation across time steps during autoregressive inference and discuss whether mitigation strategies are needed.
