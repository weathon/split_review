## Summary
This paper extends Chinchilla-style scaling laws to incorporate architectural factors — hidden size (d_model), MLP-to-attention ratio (r_mlp/attn), and grouped-query attention (GQA) — with the goal of jointly optimizing inference efficiency and accuracy. The authors train over 200 models (80M–297M parameters) to characterize U-shaped loss relationships with respect to normalized hidden size and MLP-to-attention ratio, then fit a two-step conditional scaling law that uses the Chinchilla-optimal loss as a reference and calibrates deviations based on architectural choices. The resulting framework is validated by training 1B and 3B models (Panda, Surefire) that achieve up to 2.1% accuracy gains and 42% higher inference throughput compared to LLaMA-3.2 counterparts under the same training budget.

---

## Strengths

- **Extensive empirical foundation.** Training and evaluating 200+ models across five parameter scales (80M–3B) on nine downstream benchmarks, with systematic ablations of hidden size, MLP-to-attention ratio, and GQA, provides unusually strong empirical grounding for the claims.

- **Clean, U-shaped relationship clearly established.** Figures 4 and 5 consistently demonstrate that both d_model/√N and r_mlp/attn exhibit U-shaped loss curves across different model scales. This structural observation, stable across 80M–1B, is the core insight enabling the conditional law.

- **Two-step conditional framework is principled and tractable.** Using Chinchilla as a reference and fitting a lightweight calibration function (7 shared learnable parameters) is both computationally efficient and interpretable, avoiding the curse of fitting a fully joint high-dimensional scaling law.

- **Concrete, reproducible validation.** Panda-1B and Surefire-1B/3B are trained end-to-end and compared under identical setups. Throughput gains are reproduced across vLLM and SGLang on both A100 and H200 hardware, demonstrating robustness of findings beyond one serving stack.

- **Finding of r ≈ 1 as optimal is practically important.** Nearly all production LLMs use r ∈ [4–5] (LLaMA-3.2: 4.80, Qwen3-8B: 4.67), yet the paper empirically demonstrates an interior optimum near r ≈ 1. This is a non-obvious, actionable insight that contradicts prevailing design choices.

---

## Weaknesses

### Fatal
None.

### Major

1. **Coefficient instability across scales undermines generalizability.** In Section 5, the learned coefficients shift substantially between fits on small models vs. 1B models (compare a₀ = 2.697 from small-scale fit vs. 2.319 from 1B fit). When predicting 3B behavior from 80M–1B fits, the Spearman rank correlation drops to 0.50 — essentially random ordering — compared to 1.00 when fitting from 1B alone. The paper acknowledges this and recommends using proximal-scale data for fitting, but this is a practical limitation that is not fully resolved within the paper: one must always train at intermediate scale (≈N/3), which adds significant cost. More critically, if the law's coefficients are not stable across scale, the value of the conditional scaling law as a *predictive* tool (rather than just a post-hoc characterization) is materially weakened.

2. **Validation capped at 3B — law reliability at production scale is unknown.** The claim that the framework guides "inference-efficient LLMs" is strong, but all trained validation models are ≤3B parameters. Given that deployed LLMs are typically 7B–70B+, and given the coefficient instability already observed between 80M–1B and 1B–3B regimes, it is unclear whether the identified optima (d_model/√N ≈ 0.08, r ≈ 1) persist at larger scales. The paper acknowledges this but does not even provide a theoretical argument or preliminary evidence for extrapolation beyond 3B.

3. **Separability assumption lacks rigorous validation in the main paper.** The law in Eq. (3) explicitly assumes the effects of d_model and r_mlp/attn on loss are separable (factored as a product). This is a structural modeling choice, not derived from first principles. The authors mention that non-separable formulations in Appendix J show no improvement, but the comparison is only reported at one scale level, and there is no theoretical motivation for why separability should hold. Given that the law's predictions are the primary output, a validation showing separability is approximately satisfied (e.g., via interaction term analysis) would strengthen the claim.

### Minor

1. **Spearman = 1.000 in Figure 8 is trivially achieved.** When fitting the 3B law using 1B data and evaluating on 3B, a Spearman of 1.0 is reported. At the 3B scale, the paper likely has only a small number of architectural variants (the paper does not report how many 3B models were trained). With 2–4 points, perfect rank correlation is trivially achievable and provides no meaningful signal about the law's discriminative ability. This should be explicitly contextualized.

2. **Number of layers is fixed, limiting the search space.** The paper explicitly fixes m_layer and varies only d_model, r_mlp/attn, and GQA. While depth is an important architectural dimension that is known to interact with width, fixing layers by design prevents the framework from finding depth-width tradeoffs. The comparison across models with different N involves different layer counts (16 for 1B, 28 for 3B), which are implicitly chosen and not principled within the proposed framework.

3. **Training data mismatch with baseline.** Panda/Surefire are trained on Dolma-v1.7 with 100·N_non-embed tokens, while LLaMA-3.2 was trained on very different curated data at different scales. Within-paper comparisons (Table 1) retrain LLaMA-3.2 configs on the same Dolma data, which is appropriate — but the presented downstream accuracy numbers should not be compared to the publicly released LLaMA-3.2 models, and readers may conflate them.

### Trivial

- The practical guidance to use "about one-third of target scale" for fitting data is useful but not formally derived.

---

## Nice-to-Haves

- A 7B validation model would substantially strengthen the scaling law generalizability claim, even if resources allow only a small set of 7B architectural variants.
- A more careful statistical analysis of Figure 8's Spearman = 1.000 result, reporting the number of data points used, would improve scientific transparency.
- A brief discussion of whether the r ≈ 1 optimum is expected to shift at 7B+ scales, or whether the U-shape flattens, would help practitioners extrapolate the findings.

---

## Novel Insights

The paper's most practically significant insight is that optimal MLP-to-attention ratio is approximately 1.0 across the 80M–3B range studied — strikingly different from the r ≈ 4–5 used in LLaMA, Qwen, and most contemporary production models. If this finding holds at 7B+ scales, it implies that a large fraction of production model parameters are misallocated toward MLP layers at the expense of attention capacity. The conditional scaling law framework itself — using a Chinchilla-fit as a reference and calibrating deviations due to architecture — is a clean methodological contribution that separates the problem of "how much to train" from "what shape to train," and could be extended to other architectural degrees of freedom (e.g., tied embeddings, inter-layer attention sharing). The observation that scaling law coefficients shift with model scale, requiring fitting at proximal size, is an implicit but important caution against fully unconstrained extrapolation from small-scale architecture sweeps.

---

## Suggestions

- Report exactly how many 3B architectural variants were trained, to contextualize Spearman = 1.00 in Figure 8.
- Include a brief sensitivity analysis showing how the optimal (d_model/√N, r) changes as more scale data is added to the fit — this would directly address the coefficient instability concern.
- Compare the predicted optimal architecture from the small-model fit vs. the 1B fit for the 3B target: the two fits yield different optima (r = 1.055 vs. r = 1.229), and explicitly discussing this discrepancy would help readers understand when to trust the law.

---

## Score and Decision

The paper delivers a real, well-validated empirical contribution at a tractable scale. The conditional scaling law framework is methodologically principled, the ablations are thorough, and the demonstrated gains are concrete and hardware-verified. The main concerns — coefficient instability across scales and the 3B ceiling — are acknowledged honestly, but they are not resolved, and they leave open the core question of whether the framework generalizes to production-scale models. The paper is above the conference median in both novelty and rigor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>