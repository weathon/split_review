Now I have a thorough understanding of the paper and the reviewer claims. Let me compose the final consolidated review.

## Summary

The paper proposes GEVRM, a method for robust visual manipulation that combines a text-guided video diffusion model (for generating expressive future goal states) with prototypical contrastive learning for state alignment, all framed under inspiration from internal model control (IMC) principles. The approach is evaluated on the CALVIN benchmark (standard and perturbed settings) and on the Bridge dataset for goal generation quality.

## Strengths

- **Novel combination of video generation and contrastive state alignment for robustness**: GEVRM is the first method to explicitly address external perturbations in VLA through a closed-loop design where goal generation (video diffusion) and state alignment (prototypical contrastive learning) are jointly optimized. The ablation study (Fig. 5) confirms that both VAE fine-tuning and state alignment contribute to performance, and the T-SNE visualization (Fig. 6) shows that state alignment improves representation quality.

- **Strong empirical performance with challenging observation setup**: On the CALVIN ABC→D zero-shot setting, GEVRM outperforms prior video-generation-based methods (UniPi, HiP, GR-1) while using only third-view RGB images without proprioception or gripper views — a deliberately harder setting than most prior work. On perturbed environments, it achieves a 45.9% improvement in average task completion length over SuSIE (1.62 vs. 1.11, Table 3).

- **Substantial improvement in goal generation quality**: Table 1 shows GEVRM achieves FID of 94.47 vs. 236.75 (GR-1) and FVD of 3.80 vs. 12.83, indicating significantly more expressive and temporally consistent goal state generation. Qualitative results (Figure 3) demonstrate fewer hallucinations under perturbations.

- **Thorough ablation and hyperparameter analysis**: The ablation study systematically evaluates the contributions of VAE fine-tuning and state alignment, and tests the λ hyperparameter over five values, showing performance is robust to its selection.

## Weaknesses

### Fatal
None.

### Major

- **No error bars, confidence intervals, or multi-seed results reported for any experiment (Tables 1–3, Figure 5)**. All central claims — including the headline CALVIN results and the robustness improvements — rest on single-run point estimates. Given the stochastic nature of diffusion-based video generation and diffusion policies, single-run results cannot support the claimed margins. This is a foundational evidential gap that must be addressed for the paper's quantitative conclusions to be trusted.

- **The IMC framing is significantly overstated**. The paper claims the method "incorporates," "implements," and "internalizes" the IMC principle (lines 24, 58, 82, 251). However, the actual mechanism differs fundamentally from classical IMC: there is no model of plant dynamics that predicts future system output and uses prediction error to cancel disturbances. Instead, the method uses contrastive learning to align goal and current state representations — a representation-learning objective, not a disturbance-estimation mechanism based on forward prediction. The paper acknowledges "some components...are adjusted accordingly" (line 22) but still claims to instantiate IMC. The contribution would be more accurately described as "inspired by IMC" or "analogous to IMC." This overclaiming does not invalidate the method but misrepresents its relationship to control theory.

- **The robustness evaluation is narrow and lacks critical baselines**. Only one baseline (SuSIE) is compared on perturbed environments (Table 3). No comparison is made to simpler robust methods such as standard image augmentation applied to policy training, domain randomization, or goal-conditioned policies without the video planner. Without these controls, it is unclear whether the robustness gains come from the IMC-inspired state alignment, the video planner, the particular architectural choices, or simply from having a larger model. The perturbations are also not fully specified (corruption parameters, severity levels are absent).

- **Real-world validation does not match the claims**. The abstract claims "significant improvements in realistic robot tasks," but the only real-world evaluation is goal generation quality on the Bridge dataset (qualitative + metrics in Table 1). No real robot closed-loop action execution experiments are presented. The "realistic robot tasks" claim requires either real robot deployment experiments or more cautious language.

### Minor

- **The connection between goal generation quality and downstream task robustness is assumed, not validated**. The paper uses FID, FVD, SSIM, PSNR, and LPIPS to evaluate goal generation but never demonstrates that improvements on these metrics translate to better action execution on CALVIN or real robots. A planner that generates photorealistic but physically infeasible goals could score well on these metrics while producing poor actions. Showing this correlation would strengthen the paper's internal validity.

- **The paper cites GR-1 inconsistently**: line 139 correctly cites GR-1 as (Wu et al., 2023), but line 161 cites it as (Black et al., 2023), which is incorrect.

### Trivial

- No trivial issues beyond the citation inconsistency noted above.

## Nice-to-Haves

- Comparing against additional robustness-oriented baselines (e.g., RAD, DrQ-style augmentations applied to policy training, or simpler goal-conditioned policies without the video planner) would help isolate the source of robustness gains.
- Specifying perturbation parameters and severity levels would improve reproducibility.
- Testing on a broader range of perturbations (sensor noise, actuator delays, object appearance changes) would strengthen the robustness claim.

## Removed Points

- **Criticism that the paper "frames existing methods as ignoring perturbations entirely."** The paper explicitly acknowledges image augmentation (lines 12-13) and states "image augmentation technology is utilized when training goal-conditioned policies" (line 18). It argues that augmentation alone is insufficient — a reasonable position, not a misrepresentation.
- **Criticism about "the paper does not review any prior work that fails to bring IMC to VLA (since none exists)."** This is a non-sequitur — reviewing prior attempts to do something that has never been done is not a reasonable expectation.
- **Criticism that the video spatiotemporal compression and random mask are "borrowed from prior work."** Combining existing techniques in a novel configuration for a new purpose (robust VLA) is standard practice in ML research and does not diminish the contribution.
- **Criticism that "the combination with contrastive loss (Eq. 6) is the only novel component, but its effect is not isolated in the ablation" — contradicted by the paper:** The ablation (Fig. 5, Section 5.3) explicitly removes state alignment and shows degraded performance, isolating its effect.
- **Strength Finder's claim about "novel integration of IMC into VLA"** — This is the overclaimed framing noted in Weaknesses, so it cannot stand as an unqualified strength.
- **Claim that results are "implausibly high" based on specific numeric values from embedded tables** — The exact table values cannot be verified from the extracted text. The valid criticism is the lack of error bars, not speculation about specific numbers.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's strong empirical framing (clean CALVIN results, robustness gains) and its weak evidential foundations (no error bars, narrow baselines). A second tension is between the paper's ambitious theoretical framing (IMC instantiation) and what is actually a well-engineered but conventional combination of video generation and contrastive learning. Neither insight is genuinely new — they are standard reviewer observations about overclaiming and insufficient statistical rigor.

## Suggestions

1. **Report all main results with at least 3 random seeds, showing means and standard deviations or confidence intervals.** This is the single most important revision.
2. **Reframe the IMC connection** as "inspired by IMC" or "drawing an analogy to IMC" rather than claiming to instantiate or implement IMC. This would accurately reflect the relationship between the method and the control principle.
3. **Add robustness baselines**: Compare against a version of the method without the video planner (direct goal-conditioned policy), against standard data augmentation applied to policy training, and against at least one additional prior robust VLA method if available.
4. **Either add real robot closed-loop experiments or temper the claims** about "significant improvements in realistic robot tasks." If real robot experiments are not feasible, the abstract and conclusion should reflect that the real-world validation is limited to goal generation quality.
5. **Specify perturbation parameters** (noise variance, color jitter ranges, etc.) for reproducibility.

## Score and Decision

The paper tackles an important problem (robustness of VLA models under deployment perturbations) with a technically coherent approach. The core ideas — combining expressive video generation with contrastive state alignment — are sound and the ablation provides some support for the design choices. However, the lack of any error bars or multi-seed reporting across all experiments is a significant evidential gap that prevents accepting the quantitative claims at face value. The overclaimed IMC framing and the narrow robustness evaluation further weaken the submission. The paper would be substantially stronger with the suggested revisions, but in its current form the evidence does not adequately support the claimed contributions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>