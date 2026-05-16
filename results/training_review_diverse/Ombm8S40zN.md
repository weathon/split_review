Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces Discrete Denoising Posterior Prediction (DDPP), a framework for steering pretrained masked diffusion models (MDMs) by framing fine-tuning as sampling from a Bayesian posterior. The key contribution is a family of three simulation-free objectives — DDPP-IS, DDPP-LB, and DDPP-KL — that match the denoising posterior of a fine-tuned MDM to the reward-induced posterior at each noise level, avoiding full trajectory simulation. The paper validates DDPP across synthetic grids, binarized MNIST, pixel-level CelebA images, protein sequences (with wet-lab expression), and text generation, showing competitive or superior results against RTB, SVDD, and Best-of-N baselines.

## Strengths

- **Principled formulation of steering as Bayesian posterior sampling for MDMs**: Casting the problem as sampling from a reward-modulated posterior is a clean probabilistic framing that is new for discrete diffusion. The insight that the denoising posterior of the pre-trained MDM can be reused to construct matching problems across noise levels (Eq. 8 and Eq. 11) is the conceptual core and directly enables simulation-free fine-tuning.

- **Three concrete, scalable objectives covering different reward scenarios**: DDPP-IS (non-differentiable rewards, MC estimation), DDPP-LB (amortized log-partition learning, cheapest), and DDPP-KL (differentiable rewards, no partition function) are not just one algorithm but a framework with explicit trade-offs. Each is derived from the same unifying posterior-matching perspective, and the paper provides algorithmic pseudocode (Alg. 1, Alg. 2) showing practical instantiation.

- **Strong and broad empirical validation**: The method is tested on synthetic grids, binarized MNIST, pixel-level CelebA (64×64), protein sequence design with wet-lab validation, and two text tasks (toxicity, sentiment). The wet-lab validation (§4.3) — where 4/6 DDPP-designed constructs showed detectable expression in E. coli — goes beyond standard in-silico evaluation and demonstrates real-world applicability, which is rare in this literature. In-silico results across domains consistently show DDPP variants matching or outperforming RTB and SVDD on reward metrics while maintaining sample quality (Tables 2–4).

- **Theoretical grounding for the learned log-partition estimate**: Proposition 1 proves that the learned log-partition function in DDPP-LB is a lower bound to the importance-sampling estimate, with equality at the optimal proposal. This provides a principled justification for the cheaper amortized variant.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Discrete guidance baseline mentioned but not evaluated in image experiments**: The paper states "For image settings with differentiable reward, we also include discrete guidance as a baseline (Nisonoff et al., 2024)" (§4, paragraph on baselines). However, the image experiments (Figure 3, §4.2) report results only for Base, Best-of-10, SVDD, RTB, and DDPP-LB — discrete guidance results are absent. While DDPP already compares against three other strong baselines (RTB, SVDD, Best-of-N), omitting a baseline that the paper itself flags is a clear inconsistency that should be addressed (either include results or explain why discrete guidance could not be applied).

- **Wet-lab claims slightly overstate what has been validated**: The abstract claims "transient expression of reward-optimized protein sequences," and the paper presents SDS-PAGE gels showing 4/6 DDPP-designed constructs express. However, the wet-lab validates expression and purification only — it does not verify that the expressed proteins actually adopt the predicted secondary structures (high β-sheet content) or are functional. The reward model was based on ESMFold predictions (pLDDT, pTM, β-sheet percentage); the wet-lab does not confirm these structural predictions. The paper should either (a) add structural verification (circular dichroism, activity assay) or (b) clearly separate the claims into "in-silico reward-optimized sequences" and "wet-lab expression validation" to avoid conflating the two.

- **Metric definitions are incomplete**: "FLD" (Frechet-Like Distance? — cited to Jiralerspong et al., 2023, but not defined in the main text beyond a one-line gloss) and "class-BPD" (used in Figure 3) are not clearly defined. BPD is defined (bits-per-dim, line 201), but "class-BPD" is not. A methods paper should define or formally reference all evaluation metrics in the main text or a dedicated metrics section, since readers should not have to go to the cited papers to understand the numbers.

- **No standard deviations in Table 2 while later tables include them**: Table 2 (MNIST) reports "mean performance over 3 runs" without standard deviations, whereas Tables 3 and 4 report mean ± std. This inconsistency makes it harder to assess the significance of the MNIST results relative to other experiments.

### Trivial

- **The abstract's framing that no "scalable and rigorous method" exists for steering MDMs is slightly overstated** given that SVDD (cited as concurrent) and discrete guidance address the same problem, albeit with different trade-offs. A more precise framing (e.g., "no simulation-free fine-tuning method") would be more accurate.

- **DDPP-KL (§3.3) is presented as avoiding the log-partition function, but requires on-policy sampling and a differentiable reward** — these practical limitations are acknowledged but a brief comparison of computational cost (wall-clock time or gradient steps) vs. DDPP-LB/IS would help readers understand the trade-off in practice.

## Nice-to-Haves

- An ablation comparing single-step (Eq. 11) vs. sub-trajectory (Eq. 8) objectives on a small-scale task (e.g., synthetic grid) would clarify the trade-off between approximation error and computational cost.
- A brief sensitivity analysis for the number of importance samples M (DDPP-IS) or the learning rate for the log-partition network (DDPP-LB) would increase confidence in robustness.
- A wall-clock time comparison across DDPP variants and RTB would substantiate the "simulation-free" efficiency claim concretely.
- For protein wet-lab, structural verification (circular dichroism or similar) or explicit acknowledgment that functional validation is future work would resolve the overclaim concern.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Missing theoretical justification for the central loss (Eq. 7/8) in the main text"** — The paper provides an intuitive justification: matching the log-ratios forces q_θ to approximate π_t, and "if the approximation matches the denoising reward-induced target posterior over all sub-trajectories then the reverse process can be simulated to draw samples that follow π_0" (lines 94–95). The rigorous derivation is in Appendix C.3. Deferring detailed proofs to the appendix is standard practice; the main text contains a sufficient sketch for a reviewer to assess the logic. The criticism that the proof is "relegated to the appendix" falls under Rule 9 (weaknesses about missing appendix content should be removed since the parser strips these sections).

2. **"Reproducibility: experimental procedures missing from main text"** (optimizer, learning rates, etc.) — The paper explicitly states "We provide the full experimental details in §D" (line 174) and the Reproducibility Statement (lines 260–265) lists the appendix contents. It is standard for ML methods papers to place hyperparameters and training details in the appendix. This criticism falls under Rule 7 (trivial implementation details).

3. **"No baseline without fine-tuning on the same architecture" for CelebA** — The paper does provide this: "Base" in Figure 3 is the pre-trained MDM without fine-tuning (line 207: "DDPP obtains BPD values that are within the range of the base model"). The reviewer appears to have missed this baseline.

4. **"Section-by-section: transition from Eq. 6 to Eq. 7 is abrupt"** — This is a presentation preference. The text explains: "The detailed balance constraint over sub-trajectories suggests a natural... objective that minimizes the mean squared error of a log-ratio" (lines 82–84). The logical connection (detailed balance → matching log-densities → minimizing squared error of log-ratios) is clear enough for a conference paper.

5. **"Hyperparameter sensitivity" and "ablation of trajectory length"** — These are generic suggestions applicable to virtually any methods paper, not specific weaknesses that undermine the current claims. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Include discrete guidance results in the image experiments** (or explain why it was omitted) to honor the stated baseline list and complete the comparison.
2. **Tone down or split the wet-lab claims**: distinguish between "in-silico reward-optimized sequences" and "wet-lab expression validation" to avoid any appearance of overclaiming.
3. **Define class-BPD and FLD explicitly** in a metrics paragraph in §4 or the appendix.
4. **Add standard deviations to Table 2** for consistency with the rest of the paper.

## Score and Decision

This is a solid methods paper with a novel framework, three well-motivated objectives, and impressively broad empirical validation including wet-lab work. The weaknesses are real but modest — none threaten the core claims. The discrete guidance omission and slightly overstated wet-lab language are fixable with clarifications rather than new experiments. The paper makes a clear contribution to the field of discrete diffusion model steering.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>