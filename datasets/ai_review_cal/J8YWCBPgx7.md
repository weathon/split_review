- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

PostEdit proposes an inversion- and training-free zero-shot image editing method that uses posterior sampling concepts to guide diffusion-based editing. The method operates by (1) adding random noise to input latents, (2) estimating clean latents via an LCM/DDIM solver, (3) optimizing the estimate through a weighted blend with the initial latent, an L2 measurement consistency term, and Langevin dynamics, and (4) repeating with decreasing noise levels. On the PIE-Bench dataset, PostEdit achieves the best CLIP similarity scores (Whole: 26.76, Edited: 24.14) with a runtime of ~1.5 seconds.

## Strengths

- **State-of-the-art CLIP similarity scores**: Table 1 shows PostEdit achieves the highest Whole (26.76) and Edited (24.14) CLIP similarity among eight methods on PIE-Bench, with clear margins over the next best method (TurboEdit: 26.29 / 23.05). This directly supports the claim of superior editing alignment with target prompts.

- **Fast, inversion- and training-free operation**: Table 1 reports ~1.5 second runtime with no DDIM inversion or per-instance network fine-tuning, using only a single A100 GPU with ~18 GB memory. The four-step procedure (random noise injection → LCM estimate → latent optimization → noise schedule iteration) avoids the repeated network inference costs of inversion-based methods.

- **Novel integration of posterior sampling concepts for editing**: Extending the DPS posterior sampling framework (designed for linear inverse problems on small-scale datasets) to text-guided editing on Stable Diffusion is a non-trivial adaptation. The masking-based measurement model (Eq. sample_2) and the use of weight-blending (Proposition 1) to handle layout inconsistency in large T2I models are sensible design choices.

## Weaknesses

### Fatal

None.

### Major

- **The derivation connecting the method to posterior sampling is imprecise and non-standard**: The paper states it extends posterior sampling theory to editing, but the core derivation is problematic. Eq. (bayes) writes $\nabla_{\boldsymbol{z}_0} \log p(\boldsymbol{z}_0|\boldsymbol{z}_t, \boldsymbol{y})$ — this conditions on $\boldsymbol{z}_t$ and differentiates with respect to $\boldsymbol{z}_0$. Standard DPS (Eq. invsc) uses $\nabla_{\boldsymbol{x}_t} \log p(\boldsymbol{x}_t|\boldsymbol{y})$, differentiating with respect to the noisy latent. The paper provides no justification for this change of variables or why the resulting optimization in Eq. (rec) corresponds to sampling from the intended posterior. The "Proposition" about the weighted blend (Proposition 1) is stated as theoretical but is essentially a heuristic interpolation, and Proposition 2's claim that sampling from $\mathcal{N}(\boldsymbol{z}_0^w, \sigma_{t-1}^2\boldsymbol{I})$ "satisfies the time marginal distribution conditioned on $p(\boldsymbol{z}_{t-1}|\boldsymbol{y})$" is asserted without a verifiable argument in the main text. The paper should either provide a clean derivation or clearly characterize the method as *inspired by* posterior sampling rather than an extension of the theory.

- **Algorithm 1 contains notation errors and structural issues that impede reproducibility**: The variable $\boldsymbol{z}_0$ is reused for at least three distinct quantities: the initial latent (line 179), the LCM estimate (lines 181–182, updated again in lines 186–187), and the optimization variable (line 190 onward). The `\RETURN` on line 189 sits inside the outer `FOR` loop but after the inner loop — as written, this would exit the entire procedure after the first outer iteration, making the remaining optimization steps unreachable. The timestep sequences $\{t_i\}$, $\{\tau_i\}$ and the measurement operator $\mathcal{A}$ in Eq. (rec) are referenced but not specified in the main text. While the appendix (stripped by the parser) presumably provides details, the main paper's pseudocode should be self-consistent and correct as a stand-alone description.

- **The ablation study does not isolate whether the posterior sampling optimization is responsible for the gains**: The three ablations in Figure 9 test (a) removing the entire optimization in Eq. (rec), (b) varying mask probability, and (c) varying weight $w$. None of these test whether the specific gradient terms from posterior sampling (the measurement consistency term and the $\|z_0^{(k)}-z_0\|^2$ term) outperform a simpler baseline that uses only the weighted blend (Eq. weight) with the LCM solver — without the gradient descent or Langevin dynamics. If the weighted blend alone achieves similar CLIP similarity, then the "posterior sampling" framework is unnecessary overhead. This is the most direct control for the paper's claimed theoretical contribution, and it is missing. Other related editing papers (e.g., DDCM) show that similar blends can be effective without posterior sampling, making this baseline crucial.

### Minor

- **Background preservation metrics are mid-pack except for MSE**: Table 1 shows PostEdit ranks best on MSE (3.24) but second-to-last on PSNR (27.04, only above PnP at 22.31) and SSIM (82.20, only above PnP at 79.61). LPIPS (6.38) is also mid-pack. The paper's claim of "accurately preserving unedited regions" (abstract) and the framing around background preservation as a primary challenge are undercut by these results. The single MSE win is within rounding distance of DI (3.25). The paper should either temper these claims or provide analysis clarifying the metric discrepancy.

- **The efficiency comparison is confounded by the base model choice**: TurboEdit (1.2s) uses SDXL-Turbo while PostEdit (1.5s) uses LCM-SD1.5. The paper transparently acknowledges this in a footnote and notes SDXL-Turbo is ~2.5× faster. However, this means the runtime advantage cannot be attributed to the editing method itself. A fairer comparison would control for the base model (e.g., both on LCM-SD1.5 or both on SDXL-Turbo). The paper's claim "ranks among the fastest zero-shot image editing methods" is supportable but the specific 1.5s figure is partially inherited from the base model.

### Trivial

- The variable $m$ appears as both the number of optimization iterations (Alg. 1, line 191: `\FOR{$k=0$ to $m$}`) and as a denominator in the measurement term of Eq. (rec) ($2m^2$), creating ambiguity.
- Proposition 2 references a proof `~\ref{proof2}` that is in the appendix; the main paper should at minimum state the key assumptions underlying the claim.
- The remark after Proposition 1 states the blend "does not essentially influence the sampling process" but this is not explained — it should be clarified or removed.

## Nice-to-Haves

- Implement a baseline ablation using only the weighted blend (Proposition 1) with the LCM solver, without the gradient descent and Langevin terms, to directly test whether the posterior sampling optimization contributes beyond the blend.
- Report confidence intervals or standard deviations for the CLIP similarity and background metrics in Table 1 to indicate whether the CLIP gains are statistically significant.
- A brief discussion of how PostEdit handles failure cases (e.g., masks that are too restrictive, sensitivity to hyperparameters $h$, $p$, $w$).

## Removed Points

These points were raised by the harsh critic but are removed as either factually incorrect, misreadings, or not verifiable from the paper:

- **"The measurement $\boldsymbol{y}$ in Eq. (sample_2) as a randomly masked version of $\boldsymbol{z}_0$ itself. This is not a fixed measurement; it is a stochastic perturbation of the target."** — Removed. The paper defines $\boldsymbol{y}$ via a conditional distribution (standard in Bayesian inverse problems); $\boldsymbol{y}$ is a fixed input to Algorithm 1, not resampled during optimization. The reviewer misread the role of Eq. (sample_2).

- **"The optimization step in Eq. (rec) contains a term $\|\boldsymbol{z}_0^{(k)} - \boldsymbol{z}_0\|^2$ where $\boldsymbol{z}_0$ appears on both sides, which is meaningless as written."** — Removed (downgraded to minor notation issue). Reading Algorithm 1 in context, $z_0$ (without superscript) is the LCM estimate and $z_0^{(k)}$ is the iterated optimization variable. The notation is confusing but not meaningless; I have noted this as a notation issue in the Major section.

- **"The proof of Proposition 2 is deferred to the appendix (not provided)"** — Removed. The appendix was stripped by the parser; it exists in the original submission.

- **"The sequence of timesteps $\{t_i\},\{\tau_i\}$ is never specified"** — Removed. These are listed in the "Require" line of Algorithm 1 and would be specified in the appendix (stripped).

- **"CLIP gains may not be statistically significant"** — Removed. Speculative with no evidence in the paper.

- **"A user study would strengthen the paper"** — Removed. Not standard for this type of benchmark-driven paper and would not affect the decision.

- **"The qualitative figures show PostEdit alters the background (staircase replaced by car)"** — Removed (partially). This specific example is from the ablation study, where removing the optimization *causes* the staircase-to-car transformation. The critic appears to have confused the ablation result with the full method result. The paper attributes this change to the "without optimization" ablation, not the full method.

- **"The time comparison (1.5s vs. 1.8s for iCD) is not dramatic"** — Removed. The paper claims efficiency, not a dramatic margin.

- **Missing related works** — Removed. Cannot be verified without external literature search.

## Novel Insights

None beyond the paper's own contributions. The core tension identified by the reviews — between the paper's claimed theoretical extension of posterior sampling and the heuristic nature of the actual algorithm — is already visible from reading the paper's own method section. The reviewer's framing of the weighted blend (Proposition 1) as potentially doing most of the work is a useful hypothesis that the authors should test, but this observation follows directly from the paper's own description.

## Suggestions

1. Rewrite the derivation in Section 3.1 to either provide a proper posterior sampling derivation for the editing setting, or explicitly characterize the method as *inspired by* posterior sampling with heuristic adaptations. Do not claim a theoretical extension unless the math supports it.

2. Fix Algorithm 1: use distinct variable names for the initial latent ($\boldsymbol{z}_{in}$), the LCM estimate ($\boldsymbol{\hat{z}}_0$), and the optimization iterate ($\boldsymbol{z}_0^{(k)}$). Remove the spurious `\RETURN` or clarify its purpose. Specify the numerical timestep schedules ($t_i$, $\tau_i$) in the main text.

3. Add an ablation baseline that uses only the weighted blend (Eq. weight) with the LCM solver — no gradient descent, no Langevin terms. Report CLIP similarity and background metrics for this control. This directly tests whether the posterior sampling optimization justifies its complexity.

4. Run the efficiency comparison with both PostEdit and TurboEdit on the same base model (e.g., both on LCM-SD1.5 or both on SDXL-Turbo) to attribute runtime differences to the method rather than the backbone.

5. Clarify the background preservation claims in light of the mixed metrics. Either explain why PSNR/LPIPS/SSIM are worse despite competitive MSE, or soften the claim to reflect the actual quantitative profile.
