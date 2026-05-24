Now I have enough information from the paper. Let me cross-check each reviewer claim carefully against the paper.

**Cross-checking the Harsh Critic's claims:**

1. **I-Gram metric**: The paper explicitly states (line 162) "we borrow an image alignment metric commonly used in the style transfer domain (Gatys et al., 2016; Yeh et al., 2020), referred to as I-Gram here." The reward models for face (FaceNet + L1) and stroke (CLIP) are separate from I-Gram. The paper uses I-Gram as an independent evaluation metric to avoid using the guidance reward itself. I-Gram measures Gram matrix statistics which capture texture/style — this is a reasonable general-purpose perceptual similarity metric, not "invalid." The concern is that for face identity specifically, a dedicated metric (FaceNet cosine similarity) would be more appropriate. The criticism is valid but overstated.

2. **FID specification**: The paper says (line 211) "deviating lesser from the base model (FID score)" and (line 162) uses FID because KL is intractable. The reference distribution for FID is not specified. This is a genuine gap.

3. **SVDD-PM fairness**: The paper does not report SVDD-PM hyperparameters. However, SVDD is a baseline from prior work (Li et al., 2024). The reviewer's claim of unfair comparison is speculative with no evidence the paper implemented it incorrectly. The paper states SVDD-PM is "token-wise aggressive guidance" — its slower speed is inherent to the method. REMOVE.

4. **Jensen inequality / theoretical grounding**: Eq. 11 states V ≥ r(x̂₀) without any convexity assumption. For the GMM reward (concave quadratic), the direction is actually reversed. The paper has no mention of Jensen, convexity, or any justification. This is mathematically sloppy. However, the paper frames r(x̂₀) as an *approximation* of V, not a provable bound — the inequality is a minor mathematical misstatement, not a method flaw.

5. **Hyperparameters for Table 1**: The paper shows ablation sweeping N=[5,10,20,30,40,100] (line 218) and B, η in Figure 7, but doesn't state which specific values produced Table 1. Valid concern.

6. **500 DDPM steps**: The paper states 500 steps (line 156). This is higher than current practice (50-100), but it's a methodological choice, not an error. The reviewer frames it as if it's inherently problematic, but it simply makes all methods proportionally slower.

7. **No per-scenario breakdown**: Table 1 aggregates across all three scenarios. Valid concern — the reader can't see per-task performance.

8. **Raw values not shown**: The paper normalizes scores relative to Base-SD (line 211). Valid minor concern — absolute magnitudes are opaque.

Now let me write the consolidated review.## Summary

This paper proposes CoDe (Controlled Denoising), a gradient-free inference-time guidance method for diffusion models based on block-wise Best-of-N sampling, and its extension C-CoDe (Conditional CoDe) which adds noise conditioning on a reference image. The core idea is to perform block-wise candidate selection during denoising using a Tweedie-approximated value function, avoiding the need for differentiable reward models or finetuning. The paper evaluates on GMM toy experiments and three image generation scenarios (style, face, stroke guidance) with Stable Diffusion.

---

## Strengths

1. **Gradient-free inference-time guidance via block-wise Best-of-N sampling (supported by Algorithm 1 and Theorem 3.1).** The paper formulates the KL-regularized objective (Theorem 3.1) and proposes a practical block-wise selection strategy that requires only reward evaluations, not gradients. This directly addresses the key limitation of gradient-based methods like DPS and UG (requiring differentiable guidance), and the connection to LLM block-wise decoding (Mudgal et al., 2024) is well-motivated.

2. **Demonstrated sample efficiency advantage over BoN in controlled GMM experiments (Figures 2 and 3).** The 2D Gaussian Mixture Model study provides clean, quantitative evidence that CoDe and C-CoDe achieve the same expected reward as BoN with substantially fewer samples (lower N), and maintain reward when the reward distribution shifts away from the prior — where BoN's reward drops sharply. This directly supports the claim that block-wise selection improves the reward-divergence trade-off per sample.

3. **Competitive qualitative results with lower reported inference cost (Figures 4–6, Table 1, Table 2).** The qualitative comparisons show C-CoDe capturing reference styles, facial features, and stroke patterns more faithfully than baselines. Table 2 reports that C-CoDe runs roughly 4× faster than UG and orders of magnitude faster than SVDD-PM, while Table 1 shows C-CoDe achieving the highest I-Gram (image alignment) score.

4. **Ablation study characterizing design parameters (Figure 7).** The paper systematically shows how block size B and noise ratio η control the image vs. text alignment trade-off, with all C-CoDe variants outperforming UG across the trade-off curve. This provides practical guidance for parameter selection.

---

## Weaknesses

### Major

- **I-Gram is a suboptimal metric for face and stroke guidance tasks, weakening the paper's central quantitative claim.** The paper relies on I-Gram (Gram matrix of VGG features, borrowed from style transfer) as the sole image alignment metric across all three scenarios (style, face, stroke). While I-Gram captures texture/style statistics and is appropriate for style guidance, it is not the most suitable metric for measuring facial identity (where FaceNet cosine similarity or face verification accuracy would be more appropriate) or stroke structure adherence. The paper's headline claim — "outperforms all other baselines in terms of image alignment" (Table 1) — rests on this single metric. The quantitative results in Table 1 are aggregated across all three scenarios, so the reader cannot assess whether the I-Gram advantage holds specifically for the tasks where the metric is least appropriate. The paper should report task-specific metrics (e.g., FaceNet similarity for face, structural similarity for stroke) alongside I-Gram. *This is verifiable from lines 162–163 and 205–211: the paper explicitly adopts I-Gram from style transfer and uses it for all tasks without task-specific validation.*

### Minor

- **The Jensen inequality in Eq. 11 (V ≥ r(x̂₀)) is stated without justification and is technically incorrect for non-convex rewards.** The paper writes V(x_t) = E[r(x₀)|x_t] ≥ r(E[x₀|x_t]) = r(x̂₀) using Jensen's inequality, but this direction only holds if r is convex — which is not assumed and does not hold for the GMM reward (r(x) = -½(x-μ_r)ᵀ(x-μ_r), a concave quadratic where the inequality reverses). While the method only requires r(x̂₀) as a practical surrogate for selection (not a provable bound), the paper's mathematical justification is sloppy. This is verifiable from Eq. 11 (line 127) and the GMM reward definition (line 169).

- **The FID reference distribution is not specified.** FID typically compares generated images to a real image dataset. The paper uses FID as a proxy for KL divergence from the base model (line 211: "deviating lesser from the base model (FID score)") but does not state what dataset or sample set serves as the FID reference. With 50 samples per setting (line 156), FID estimates are also high-variance. This is a methodological specification gap (lines 162, 211).

- **No per-scenario quantitative breakdown is provided.** Table 1 aggregates scores across style, face, and stroke guidance. Given that I-Gram is better suited for style than for face/stroke, the aggregated numbers could mask divergent per-task performance. The paper should present separate results for each scenario. (Verifiable from lines 205–211: Table 1 "summarizes the performance across all scenarios.")

- **Hyperparameters for the main results (Table 1) are not specified.** The ablation (Figure 7) sweeps N=[5,10,20,30,40,100] and varies B and η, but the paper does not state which specific values of B, η, and N produced the numbers in Table 1. This harms reproducibility. (Verifiable from lines 207–211 and 218: Table 1 results are presented without listing the specific operating point.)

- **Raw (non-normalized) scores for Base-SD are not shown.** All metrics in Table 1 are normalized w.r.t. Base-SD. Without the absolute values, the reader cannot assess the magnitude of improvement. (Verifiable from line 211: "report scores across all metrics by normalizing them w.r.t. the base Stable Diffusion model.")

### Trivial

- The abstract and body refer to the method as "C-Code" in one instance (line 4), inconsistent with "C-CoDe" used elsewhere. Minor typo.

- The paper uses 500 DDPM steps (line 156) whereas modern samplers commonly use 50–100 steps. This choice should be briefly justified, though it applies equally to all methods.

---

## Nice-to-Haves

- A per-scenario breakdown of Table 1 (separate columns for style, face, stroke) would substantially strengthen the evaluation.
- Including task-specific metrics (FaceNet similarity for face guidance; SSIM or pixel accuracy for stroke guidance) alongside I-Gram would address the main evaluation concern.
- Reporting raw (non-normalized) metric values for all methods.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **SVDD-PM comparison is unfair (Harsh Critic, point 3).** The reviewer asserts the comparison stacks the deck against SVDD-PM without evidence that the implementation was unfaithful to the original paper (Li et al., 2024). SVDD-PM's higher cost is inherent to its token-wise design. The paper describes it as "token-wise aggressive guidance" (line 234), which is consistent with the baseline's design. Without evidence of unfair hyperparameter selection, this is speculation. **Removed.**

- **I-Gram is "not valid" (absolute claim).** The harsh critic's phrasing is too strong. I-Gram is a reasonable general-purpose perceptual similarity metric; it is suboptimal for face/stroke tasks but not invalid. The criticism is retained above as a Major weakness but with appropriate nuance. The original "not valid" framing is softened.

- **500 DDPM steps is "unusually high" and problematic.** This is a design choice, not a flaw. Using 500 steps (vs. 50–100) applies proportionally to all methods and does not disadvantage any particular baseline. The paper uses a standard DDPM sampler; fast samplers (DDIM) are a separate design choice. **Demoted to Trivial.**

- **Missing related works / concurrent work comparison (Harsh Critic's "Missing Parts").** Rule: do not mention missing related works. **Removed.**

- **General speculative concerns ("could the metric be measuring a proxy?", "are confounders controlled?").** These are area-of-concern sweeps without specific anchors in the paper. **Removed.**

- **Strength Finder's generic strengths about "important problem" or "addressed important question."** These are superficial; removed from strengths list.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful insight about metric-task mismatch: using a style-transfer metric (I-Gram) for face and stroke tasks inflates the apparent generality of the quantitative claims, and this is only detectable because the paper aggregates across scenarios. The reviews do not reveal any new scientific finding about the method itself that the paper missed.

---

## Suggestions

1. **Report per-scenario quantitative results** (separate columns for style, face, stroke in Table 1), using task-appropriate evaluation metrics: FaceNet cosine similarity for face guidance, and a structural similarity metric (e.g., SSIM or LPIPS conditioned on stroke regions) for stroke guidance, alongside I-Gram.
2. **Specify the FID reference distribution** (what dataset or sample set serves as the reference for computing FID) and clarify whether 50 samples suffice for reliable FID estimation in this setting.
3. **State the specific hyperparameters (B, η, N)** used to produce the main results in Table 1.
4. **Provide raw (non-normalized) scores** for all metrics and methods, including the Base-SD reference values.
5. **Clarify Eq. 11:** either remove the inequality (since it is not generally true without convexity assumptions) or add the convexity condition. The approximation r(x̂₀) ≈ V(x_t) can stand on its own as a practical choice without claiming a bound.
6. **Briefly justify the 500-step DDPM choice** (e.g., standard DDPM vs. DDIM, or consistency with prior work).

---

## Score and Decision

The paper proposes a simple, intuitive, and computationally efficient gradient-free guidance method. The core idea is sound, the GMM experiments provide clean evidence of the trade-off advantage over BoN, and the qualitative results are compelling. However, the quantitative evaluation has several methodological gaps: the primary alignment metric (I-Gram) is not equally appropriate for all three tasks, the FID reference is unspecified, hyperparameters for the main results are omitted, and results are aggregated across scenarios in a way that may mask task-specific issues. These are fixable weaknesses that weaken but do not invalidate the paper's claims. The paper would benefit from a revision cycle to address the evaluation gaps before acceptance.

**Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>