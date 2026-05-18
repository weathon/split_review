Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes CALoR, a defense against model inversion attacks (MIAs) that combines two components: (1) Confidence Adaptation (CA), a novel fine-tuning loss that reduces the model's prediction confidence on private samples to create a mismatch between the attacker's one-hot target and the model's output, and (2) Low-Rank (LoR) compression of the classification head followed by a Tanh activation, which reduces information leakage from model outputs and induces gradient vanishing to impede attacker optimization. The method is evaluated across multiple settings and shows strong empirical results, particularly in high-resolution/high-accuracy scenarios where prior defenses struggle.

## Strengths

- **Strong empirical performance under challenging conditions**: Tables 1 and 2 show that CALoR reduces attack accuracy by over 30% compared to the best prior defense in low-resolution settings, and in the high-resolution MS-Celeb-1M backbone scenario, it reduces IF attack accuracy by 38.4% and PLG by 52.0% while prior defenses show minimal improvement. These results are concrete, specific, and directly support the paper's core claim.

- **Low-rank compression with Tanh activation is well-isolated and effective**: The rank ablation (Table 5) convincingly shows that rank 30 preserves test accuracy while dropping IF attack accuracy to 13.0%. The gradient magnitude plot (Figure 6/Table 6) demonstrates that Tanh provides the strongest gradient vanishing effect among activation functions. The combination is a novel application of these techniques to MIA defense.

- **Confidence adaptation loss provides a clear and testable motivation**: Figure 2 empirically shows that lower model confidence correlates with lower attack accuracy, establishing the rationale. Equation (2) defines a loss with a known convergence point ($\exp(-1/b)$), and the ablation study (Table 4) quantifies its standalone contribution at 3–4% reduction in attack accuracy.

## Weaknesses

### Fatal

None.

### Major

- **The confidence adaptation loss is not compared against simpler alternatives.** The paper introduces $\mathcal{L}_{CA} = a \hat{y}^b_c \log \hat{y}_c$ but provides no ablation or discussion comparing it against standard alternatives such as label smoothing, a direct $L_2$ penalty on confidence $(1-\hat{y}_c)^2$, or a KL-divergence-based regularizer. Since the CA component contributes only a modest 3–4% improvement in the ablation study, the reader cannot assess whether the specific formulation is necessary or if a simpler, well-understood approach would achieve similar gains. This does not invalidate the paper's overall contribution, but it leaves a methodological gap.

- **Overclaimed novelty of the weakness analysis.** The paper states (lines 29, 18) "We are the first to conduct comprehensive analyses of weaknesses inherent in MIAs." However, prior works cited in the paper itself (LOMMA on MI overfitting, PPA on gradient vanishing) have discussed these individual weaknesses. The paper's contribution is a useful *unified framing* and the novel *joint exploitation* of these weaknesses for defense, not the discovery of the weaknesses themselves. The claim as written overstates the novelty and should be tempered.

### Minor

- **Main evaluation results are presented for only 2 of 7 listed attack methods.** The paper lists 7 attack methods (GMI, KED, Mirror, PPA, LOMMA, PLG, IF) but presents detailed quantitative results only for IF and PLG in the main body. While IF and PLG are among the strongest attacks and additional experiments are mentioned (lines 183–184, 198–199), the main-tables evidence base is narrow for a paper claiming "comprehensive" defense. At minimum, summary results for a GAN-based attack and a latent-search attack in the main body would strengthen this claim.

- **The connection between low-rank compression and MI overfitting is asserted but not explained.** The paper states that compression "reduc[es] the leaked information from model outputs" (line 22) and "strengthen[s] the MI overfitting problem" (line 235). The intuitive link — that reducing feature dimensionality limits the signal available to the attacker, making it harder to avoid overfitting — is plausible but never explicitly reasoned through. The paper would benefit from a brief mechanistic explanation (e.g., how compressed features make the attacker's generative prior less effective).

- **Adaptive attacks are not discussed.** The paper does not address whether an attacker aware of the defense could adapt their strategy, e.g., by using gradient normalization or alternative optimizers to overcome Tanh-induced gradient vanishing, or by adapting their prior to the compressed feature space. A brief discussion of adaptive attacker assumptions and limitations would strengthen the paper.

- **No privacy-utility trade-off curves.** All comparisons are reported at a single accuracy point. A plot showing test accuracy vs. attack accuracy across varying defense strengths (e.g., different $\beta$ values or rank settings) would give a fuller picture of the method's behavior.

### Trivial

- Line 147 contains a stray sentence ("It offers a more intuitive illustration of the role of low-rank compression against MIAs.") that appears to be residual text.
- Computational overhead (model size, inference speed impact) of the low-rank compression is not reported.

## Nice-to-Haves

- A brief theoretical or toy-example illustration of why rank 30 is sufficient for preserving classification accuracy while limiting attack information would convert an empirical observation into a more principled understanding.
- A supplemental table or figure in the main paper showing results for at least one additional attack paradigm (e.g., GMI/KED as GAN-based, or PPA as latent-search) would better support the "comprehensive" framing.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Confidence adaptation loss derivation is missing"** — Removed. The convergence point $\exp(-1/b)$ is stated and directly verifiable by setting the gradient of $\mathcal{L}_{CA}$ w.r.t. $\hat{y}_c$ to zero. The loss landscape discussion is not standard for a defense paper of this type.

- **"Section 3.2 relies on an external `\input{section/lrc_v2}` file"** — Removed. The appendix and included files are stripped by the PDF parser. The architecture is described in the figure caption (line 110): a linear layer $\mathcal{C}_A$, Tanh activation, then linear layer $\mathcal{C}_B$. The main paper is self-contained for its architectural description.

- **"MI overfitting paragraph conflates concepts"** — Removed. The paper's description of inversion space vs. success space (Section 3.1) and the explanation that some inputs meet the optimization goal but fail to capture private information is reasonably clear and coherent.

- **"Missing hyperparameter search range"** — Removed. The paper states hyperparameters were adjusted to keep test accuracy nearly identical (line 177), which is standard practice. Full reproduction details are expected in the camera-ready appendix.

- **Harsh critic's point about gradient vanishing and whether adaptive attackers could circumvent it via alternative optimizers** — Subsumed under the "adaptive attacks" minor weakness (above). The paper acknowledges gradient vanishing as a defense mechanism but could be clearer about its limitations. This is now addressed in the minor weakness on adaptive attacks.

- **Strength Finder's "first systematic analysis" strength** — Tempered and moved to the weakness section (overclaimed novelty) since it conflicts with the verified weakness about overclaiming.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Replace or augment the "first comprehensive analysis" claim with more precise language about providing a *unified* analysis and *joint exploitation* of known attack weaknesses for defense.
2. Add an ablation comparing $\mathcal{L}_{CA}$ against label smoothing or a direct confidence penalty to justify the specific formulation.
3. Include at least one additional attack paradigm's results in the main paper (e.g., a GAN-based attack) with a brief summary.
4. Add a brief paragraph on adaptive attacker considerations and the limitations of the gradient-vanishing defense component.
5. Add a privacy-utility trade-off figure showing attack accuracy across varying defense strengths.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>