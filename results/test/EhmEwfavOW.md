Now I have all the evidence needed to write the final consolidated review.

## Summary

This paper introduces HoloNets, a framework that extends spectral convolutional networks to directed graphs by replacing the graph Fourier transform — which requires self-adjointness — with the holomorphic functional calculus. The approach defines filters $g_\theta(T)$ for non-self-adjoint characteristic operators $T$ via the Cauchy integral formula. Two instantiations are presented: **FaberNet**, using Faber polynomials (monomials for circular spectral domains) for node classification, and **Dir-ResolvNet**, using resolvent-based filters with proven scale-insensitivity under coarse-graining. Experiments show FaberNet achieving top results on five heterophilic directed graph benchmarks and Dir-ResolvNet maintaining prediction accuracy under resolution-varying perturbations where baselines degrade by orders of magnitude.

## Strengths

1. **Principled extension of spectral convolutions to directed graphs.** The paper provides a complete mathematical framework (Section 3) for defining spectral filters $g_\theta(T)$ on non-self-adjoint operators via the holomorphic functional calculus, overcoming a long-standing limitation that spectral GNNs were confined to undirected graphs. The derivation is rigorous and properly grounded in complex analysis (Haase2006, Colombo2011, Kato).

2. **Theoretical and empirical demonstration of scale-insensitivity for directed graphs.** Theorems 1–3 prove that resolvent-based filters converge to a coarse-grained limit as high-weight edges increase. The QM7 experiments (Figure 3, Tables 2–3) confirm this numerically: Dir-ResolvNet's feature vectors converge, and its inference on coarse-grained graphs degrades only modestly (MAE 27.34 vs. 17.12 at full resolution), while baselines degrade by factors of 10–400×.

3. **Novel frequency-response interpretation for directed spectral filters.** Equation (4) provides the complete spectral action of filters on directed graphs via the Jordan–Chevalley decomposition, including derivative terms absent in the undirected setting. The directed path graph example illustrates how derivative conditions on $g$ translate to spatial requirements, giving principled intuition.

4. **Theorem reducing complex weights to real without expressivity loss.** Theorem 4 shows that any HoloNet with complex weights can be exactly replicated by one with twice the width and only real weights, providing a principled hyperparameter choice for practitioners.

5. **State-of-the-art results on heterophilic directed node classification.** Table 1 shows FaberNet achieving the highest accuracy across all five benchmarks, outperforming both undirected heterophilic models and directed spatial/spectral baselines. The improvements over Dir-GNN range from 0.59% to 1.58%.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between Kirchhoff assumption and experimental verification of scale-insensitivity.** The stability theorems (Thms. 1–3) rely on Kirchhoff's condition — equal in- and out-degrees within the high-weight subgraph $G_{\text{high}}$. The paper calls this a "technical" assumption (line 415), but the QM7 hydrogen-deflection experiment does not verify whether the condition actually holds in the modified molecular graphs. The edge-weight modification $W_{ij} = Z_i^{\text{outside}} \cdot (Z_j^{\text{heavy}} - 1) / |\vec{x}_i - \vec{x}_j|$ does not obviously guarantee balanced in- and out-degrees in the high-weight subgraph. The empirical convergence may suggest the property holds more broadly than the theorems guarantee, which would actually strengthen the paper, but the authors do not comment on this discrepancy. A reader cannot tell whether the experiment validates the theory or tests a different regime. This is the most significant weakness because it undermines the claimed theoretical–empirical connection for Dir-ResolvNet's core contribution.

2. **Statistical significance of SOTA claims on node classification.** The improvements over Dir-GNN are modest (0.59%–1.58%) and standard deviations overlap on several datasets (e.g., Squirrel: 76.71±1.92 vs. 75.13±1.95; Chameleon: 80.33±1.19 vs. 79.74±1.40; Arxiv-year: 64.62±1.01 vs. 63.97±0.30). Without confidence intervals or significance tests, the "new state of the art" claim is suggestive but not rigorously established. The paper should report whether the same data splits were used across methods and provide even a simple pairwise comparison.

### Minor

1. **FaberNet's practical novelty over spatial polynomial filters is overstated.** FaberNet's filters are polynomials $\sum \theta_i T^i$ in the characteristic operator — structurally equivalent to a spatial message-passing scheme aggregating information from increasingly distant neighbors. The paper frames this as extending "spectral convolutions" to directed graphs, but for FaberNet specifically the holomorphic functional calculus provides a rigorous foundation rather than a different operational mechanism. The genuinely spectral advantage resides in Dir-ResolvNet, where the resolvent basis is not reducible to simple repeated application of $T$. The paper would benefit from clarifying which advantages are architectural vs. foundational for each instantiation.

2. **Imprecise definition of "reaches."** The definition states "no outgoing connections (i.e. for any $c \in G$ with $c \notin R$: $w_{ca} = 0$)," but the formula checks edges from outside to inside ($w_{ca}$ with $c \notin R$), not from inside to outside, which is what "no outgoing connections" should mean. Since reaches are central to the coarse-graining construction, this imprecision should be corrected.

3. **QM7 experiments use a modified dataset limiting broader significance.** The paper transparently acknowledges making the molecular graphs directed by modifying the Coulomb matrix (line 631–634). The MAE values are therefore not comparable to standard (undirected) QM7 results. The claim that "competitors are outperformed by a factor of two and more" is valid only among directed methods on this specific modified dataset. The paper appropriately scopes this, but the broader significance for molecular property prediction is limited.

### Trivial

None.

## Nice-to-Haves

- **Ablation on $\alpha$ (forward/backward balance).** The update rule mixes forward and backward filters via $\alpha$, but the paper does not analyze its effect. A sensitivity study would show whether directionality is essential or whether the filter bank alone drives performance.
- **Analysis of the resolvent shift $y$.** The hyperparameter $y$ influences convergence and filter behavior but is not explored. Brief guidance on choosing $y$ would strengthen practical applicability.
- **Discussion of limitations.** The paper is entirely positive. A section on when the approach may struggle (e.g., nearly acyclic graphs, large spectral radius) would improve credibility.

## Removed Points

These points were flagged for removal; treat with caution:

- **"c.f." / editing artifacts (Harsh Critic "Other Observations" first bullet).** Instances such as "c.f. Associated to this inner product" and "c.f. Denoting by $P_\lambda$" are PDF parser truncation artifacts, not author errors. The original submission had complete cross-references.
- **Missing appendix / proof verification (Harsh Critic "Other Observations" third bullet).** The appendix was stripped by the parser; it exists in the original submission. Per policy, missing appendix content is not a valid weakness.
- **"Best-of-three" as an unfair comparison.** The reviewer implied that the paper reporting Dir-GNN results as a "best-of-three performance over multiple directed spatial methods" introduces unfairness. The paper is being transparent about the baseline strength; reporting the best variant of a competing method makes the comparison *harder* for the proposed method, not easier.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review process is the asymmetry between the two instantiations: FaberNet is a polynomial filter in spectral disguise — it inherits the rigorous foundation but gains no operational novelty from it — while Dir-ResolvNet is genuinely new. This creates an interesting tension: the unified theoretical framework (holomorphic functional calculus) is what makes both possible and provides the language for Dir-ResolvNet's stability analysis, yet only one instantiation fully exploits the framework's advantages. This suggests that for many practical graph learning tasks on directed graphs, the value of the spectral framework may lie in guiding filter design (the resolvent basis for multi-scale problems) rather than in providing new mechanisms for single-scale tasks where polynomials already suffice.

## Suggestions

1. **Check and discuss whether Kirchhoff's condition holds in the QM7 experiment.** If it does not, explain why convergence still occurs — this would strengthen the paper by showing the phenomenon is more general than the theorems require. If it does hold, state this explicitly.
2. **Add significance tests for Table 1.** Report which differences exceed standard errors or provide a pairwise comparison. If improvements are not significant on some datasets, temper the "SOTA" claim to "competitive with state of the art."
3. **Clarify the "reaches" definition.** Fix the formula to match the intended meaning (no outgoing connections → $w_{ac}=0$ for $a\in R, c\notin R$).
4. **Acknowledge FaberNet's relationship to spatial polynomial filters.** Add a sentence stating that for the monomial basis the implementation coincides with repeated application of $T$, and the spectral perspective provides theoretical grounding rather than a different computation.

## Score and Decision

| Criterion | Assessment |
|-----------|-----------|
| Originality | High — first principled spectral framework for directed graphs beyond the graph Fourier transform |
| Importance | High — addresses a recognized limitation of spectral GNNs |
| Claims | Moderately supported — theory is strong, but experimental-theoretical gap weakens one contribution |
| Soundness | Good — theory is rigorous, experiments are reasonable but could be more rigorous |
| Clarity | Generally good (parser artifacts aside) |
| Value to community | High — opens new directions for directed spectral networks |

The paper makes a genuine theoretical contribution and provides two working instantiations with competitive empirical results. The weaknesses are real but manageable: the Kirchhoff assumption gap can be addressed by checking the condition, and the SOTA claims can be tempered with appropriate statistical qualification. The core framework (holomorphic functional calculus for directed spectral GNNs) is novel and well-constructed.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>