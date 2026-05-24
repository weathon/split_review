Now I have all the information needed. Let me write the authoritative final consolidated review.

## Summary
The paper proposes MC-MoE, a training-free compression method for MoE-LLMs that combines Pre-Loading Mixed-Precision Quantization (PMQ) — formulating bit-width allocation as an Integer Programming problem over expert significance metrics — with Online Dynamic Pruning (ODP) that retains a small fraction of critical tokens to mitigate attention decay. The core idea of jointly optimizing static quantization and dynamic pruning using both expert- and token-level importance is novel and practically relevant.

## Strengths
- **First joint training-free static quantization and dynamic pruning for MoE-LLMs:** The paper explicitly combines expert-wise mixed-precision quantization with online expert pruning in a unified pipeline without additional training (Sec. 3, Fig. 2). This is a genuine novelty.
- **PMQ achieves strong results at ultra-low bit-widths:** Table 1 shows PMQ at 2.54-bit achieves 67.50% average accuracy (only 3.8% below the FP16 model), substantially outperforming the Hessian-based baseline (67.18%) and BSP (49.07%). At 1.57-bit, PMQ (54.49%) still outperforms BSP at 2.54-bit (49.07%), demonstrating the robustness of the allocation strategy.
- **ODP with 2% token protection is effective and efficient:** Table 3 shows that combining PMQ with ODP reduces activated parameters by ~15% with less than 0.6% accuracy loss (e.g., 67.50% → 66.94% at 2.54-bit). Fig. 8 validates that the attention-aware token importance metric reduces perplexity from 6.46 (weight-only pruning) to 6.24 while maintaining nearly the same compression ratio.
- **Comprehensive ablation of bit-width allocation metrics:** Fig. 5_1 and 5_2 systematically compare random, weight-only, frequency-only, Hessian, F-norm, and full PMQ metrics across bit-widths, isolating the contribution of each factor. PMQ consistently achieves the best PPL, especially below 2-bit.
- **Practical efficiency:** The IP optimization solves in seconds (Sec. 3), and compressed models fit on a single A100-80GB GPU. The method scales from Mixtral 8×7b to 8×22b while maintaining the same performance trends (Table 3).

## Weaknesses

### Fatal
None.

### Major
- **Hyperparameters α, β, γ are neither reported nor ablated.** The paper introduces three hyperparameters (α, β in the expert significance formula $\phi_i^\alpha \cdot w_i^\beta$, and γ in the IP objective) but never states their values anywhere (lines 87, 106). No ablation study shows how varying them affects bit-width allocation or final accuracy. Without this information, the results cannot be independently reproduced, and it is unclear whether the method is robust or requires careful tuning. This is the most significant gap in the paper.

### Minor
- **Token importance metric (Eq. 6) is underspecified.** The metric $I_j = \|\mathbf{t}_j\|_1 \cdot \frac{\sum_{j \leq i \leq L} \mathbf{A}_{j,i}}{L-j}$ does not specify which layer's attention map is used, how multiple heads are aggregated, or the exact indexing convention. The paper states $\mathbf{A} = \text{softmax}(K^\top Q / \sqrt{d_k})$, which is dimensionally inconsistent with a token×token attention map. In causal attention, summing $\mathbf{A}_{j,i}$ for $i \geq j$ would only capture self-attention ($\mathbf{A}_{j,j}$) since future tokens are masked. The denominator $L-j$ suggests the authors intend a different interpretation. While the empirical results (Fig. 8) show the metric works, the mathematical description needs clarification for reproducibility.
- **ODP speedup measurements do not explicitly account for overhead.** The paper reports speedup factors of up to 1.89× (Table 3) but does not state whether the time for computing token importance scores (L1 norm + attention sum) is included or only the reduction in expert forward passes. Since the ODP mechanism requires computing Eq. 6 on the fly, a breakdown of "expert forward time" vs. "importance scoring time" would improve transparency. (Note: the routing-weight comparison in Eq. 5 is trivially cheap, but the token importance computation in Eq. 6 is not.)
- **No variance or error bars reported.** Calibration data is sampled randomly (128 sequences of 2048 tokens from C4), and reconstruction errors $\epsilon_{i,j}$ depend on this sample. Results over multiple calibration seeds would increase confidence.
- **Limited architectural diversity.** Experiments are conducted only on Mixtral 8×7b and 8×22b. Testing on additional MoE architectures (e.g., DeepSeek-MoE, OLMoE) would strengthen the generality claim.
- **The "orthogonal to various quantization techniques" claim is unsubstantiated.** The conclusion states the mixed-precision strategy is orthogonal to various quantization methods, but all experiments use GPTQ. A simple experiment with an alternative PTQ method (e.g., AWQ, QuIP) would verify this claim.

### Trivial
- **The abstract's "76.6%" compression claim is ambiguous.** At 2.54 bits, the model is reduced to $2.54/16 \approx 15.9\%$ of its original size (~84.1% compression). The origin of the 76.6% figure is not explained and may use a different base definition. The paper should clarify what quantity this percentage refers to.
- **The $\epsilon_{i,j}$ computation ignores interactions between experts.** Reconstruction error is measured by individually quantizing each expert; errors from multiple quantized experts could cancel or compound. A brief comment on this simplifying assumption would be useful.

## Nice-to-Haves
- Add a hyperparameter sensitivity table showing how $\alpha$, $\beta$, and $\gamma$ affect bit-width allocation and final accuracy at a fixed average bit-width.
- Report specific values of $\alpha$, $\beta$, $\gamma$ used in the main experiments.
- Include a baseline combining quantization and pruning without token protection (e.g., uniform quantization + weight-only pruning) to further isolate ODP's benefit.
- Discuss limitations — e.g., when experts are more balanced in importance, or when the calibration distribution differs from deployment.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"The IP objective function is poorly specified and likely misformulated":** The reviewer claims $(\epsilon_{i,j} \cdot x_{ij})^\gamma$ is problematic, but since $x_{ij} \in \{0,1\}$, $(\epsilon_{i,j} \cdot x_{ij})^\gamma$ is mathematically equivalent to $\epsilon_{i,j}^\gamma \cdot x_{ij}$ (as $0^\gamma=0$ and $1^\gamma=1$ for $\gamma>0$). The formulation is valid. Removed.
- **"BSP comparison raises fairness concerns":** The paper clearly states BSP results were reproduced from the official code repository and evaluated under the same settings (Table 1 caption). The Hessian baseline (67.18% at 2.54-bit) is close to PMQ (67.50%), providing a fair anchor. The BSP gap is large but not suspicious given BSP's block-level (not expert-level) allocation. Removed as speculative.
- **"The claim of surpassing FP 13b dense LLMs is overstated":** Table 3 shows LLaMA2-13b at 65.19% and PMQ 2.54-bit at 67.50%/66.94%. The compressed model genuinely outperforms the larger dense model. That the FP16 Mixtral already outperforms LLaMA2-13b does not diminish this — compression typically degrades performance, so retaining a superiority margin is noteworthy. Removed.
- **Various formatting nitpicks, missing appendix content, missing related works, and reproducibility complaints about trivial implementation details:** Removed per policy (parser artifacts, unverifiable, or standard practice).

## Novel Insights
The two reviews largely converge on the paper's contributions and gaps, but there is an interesting tension: the Harsh Critic focuses on potential formulation issues (IP objective, attention metric indexing) that turn out to be either mathematically benign (the IP objective is correct) or empirically supported despite unclear presentation (the token metric works in practice even if the notation is imprecise). Neither reviewer challenges the core experimental results or finds evidence of overclaiming relative to controlled baselines. The most actionable insight emerging from the synthesis is that the paper's principal weakness is a **reproducibility and transparency gap** (unreported hyperparameters, underspecified metric) rather than a methodological flaw — which means the contribution is solid but needs careful documentation before it can be fully trusted by the community.

## Suggestions
1. Report the specific values of $\alpha$, $\beta$, $\gamma$ used in all experiments, and include an ablation table showing sensitivity to these parameters.
2. Clarify the token importance metric: specify which layer/head is used, how heads are aggregated, and provide a precise indexing convention for the attention map. A small toy example would help.
3. Add a brief discussion or measurement of ODP's runtime overhead relative to the speedup, even if the overhead is negligible (which it likely is, since the required quantities are already computed during the forward pass).
4. Run one experiment with a different quantization method (e.g., AWQ) to substantiate the claim of orthogonality.
5. Add error bars (or at least note single-seed calibration) in the main results.
6. Clarify the "76.6%" figure in the abstract so readers know what it refers to.

## Score and Decision
This is a solid paper with a novel contribution (first joint training-free quantization + pruning for MoE-LLMs) supported by strong empirical results. The main weakness is a transparency gap around unreported hyperparameters and an underspecified metric, neither of which is fundamental or invalidates the core claims. The issues are fully addressable in a revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>