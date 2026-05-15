Now I have verified everything. Let me produce the consolidated review.

---

## Summary

This paper proposes Di-SkilL, a method for learning diverse, multi-modal skills within the Contextual Episodic Policy Search (CEPS) framework. The core technical contribution is a mixture-of-experts policy where (i) each expert is a deep neural network (rather than linear), (ii) per-expert context distributions are parameterized as energy-based models (EBMs) to capture multi-modality and sharp discontinuities without requiring prior knowledge of environment bounds, and (iii) the bi-level optimization is stabilized via trust-region updates and PPO. An ablation demonstrates that automatic curriculum learning via these per-expert context distributions is critical for performance, and experiments on four simulated robotic tasks show improvements over single-mode baselines on environments with inherent multi-modality.

## Strengths

1. **Energy-based per-expert context distributions are a principled solution to a real limitation of prior MoE methods.** The paper identifies that Gaussian or hand-tuned context distributions (as in Celik et al., 2022) require environment-specific penalty terms and cannot represent multi-modality. Parameterizing $\pi(\mathbf{c}|o)$ as an EBM and approximating the normalizing constant with samples from $p(\mathbf{c})$ elegantly sidesteps both issues — the model automatically stays within valid context regions and can represent sharp discontinuities (Section 3.2). This is a novel contribution within the CEPS literature.

2. **Ablation convincingly shows that automatic curriculum learning is essential.** Figure 3b demonstrates that disabling the curriculum mechanism (Di-SkilLwoCurV1/V2) causes success rate on table tennis to drop from >80% to <40%, while Di-SkilL with the curriculum reaches full performance. The design is well-controlled: V1 uses the same sample count as Di-SkilL, isolating the curriculum intervention; V2 uses ~5× more samples but still cannot match the full method, showing that more data does not compensate for the lack of curriculum.

3. **Di-SkilL clearly outperforms single-mode baselines on tasks requiring multi-modal solutions.** On Box Pushing (≈70% vs ≈50%) and Minigolf (≈70% vs ≈50%), the multi-modal MoE policy substantially outperforms the single-mode BBRL baseline (Figures 4b, 4c). These tasks involve obstacles that create genuinely multi-modal solution spaces, providing the strongest evidence that diverse skill learning translates to higher task success.

4. **Evaluation across diverse challenging robotics tasks.** The paper covers four simulated environments (Reacher, Table Tennis, Box Pushing, Minigolf) with varying context dimensions, non-Markovian/sparse rewards, and different physical complexity. Results use IQM with 95% stratified bootstrap confidence intervals over 24 seeds, following best practices (Agarwal et al., 2021).

## Weaknesses

### Fatal
None.

### Major

1. **Diversity of skills is a central claim but is never quantitatively measured.** The title, abstract, and introduction foreground "diverse skills" as a primary contribution, yet the only evidence for multi-modality is a single qualitative figure (Fig. 5) showing a few box trajectories. No diversity metric is reported — e.g., entropy of the gating distribution, variance of rollout outcomes across experts, number of distinct behaviors per context, or coverage of the behavioral space. Given that the method's name (Di-SkilL — Diverse Skill Learning) and framing hinge on this property, the lack of quantitative support is a significant gap. The paper could be reframed as "improving MoE performance via deep experts and EBM curricula" without the diversity claim being similarly supported.

2. **Incomplete comparison against the most relevant prior MoE method (SVSL).** SVSL (Celik et al., 2022) is the direct predecessor: it uses the same max-entropy MoE objective with curriculum learning in the CEPS framework, differing only in using linear experts and Gaussian context distributions. SVSL is evaluated only on the simpler table-tennis task in the ablation (Section 4.1, Fig. 3b), not on the main benchmarks in Section 4.2 (Reacher, extended Table Tennis, Box Pushing, Minigolf). The paper justifies this by noting that SVSL requires hand-designed punishment functions that are environment-specific (line 154), which is a reasonable practical constraint — but this means the main experiments compare Di-SkilL only against BBRL (single-mode) and LinDi-SkilL (the authors' own linear-expert variant). The central empirical claim of "outperforming baselines" is thus not validated against the strongest comparable prior work on most tasks. Including SVSL on at least one additional multi-modal task (e.g., Box Pushing) would substantially strengthen the evaluation.

### Minor

1. **Reacher results lack statistical significance for the claimed improvement.** The paper states that Di-SkilL "eventually achieves a higher return" on the Reacher task (Fig. 3c, line 166), but the confidence intervals of Di-SkilL and BBRL overlap substantially. This claim is not statistically justified by the reported data.

2. **The EBM partition function approximation is not analyzed.** The paper proposes approximating the normalizing constant $Z$ using a batch of contexts from $p(\mathbf{c})$ (line 105), which is clever but receives no analysis of bias, variance, or how batch size affects the quality of the approximation. While the approach appears to work empirically, understanding this sensitivity would strengthen the method.

3. **Some implementation details are omitted.** The architecture of the energy function $\phi_o(\mathbf{c})$ (layers, activations, output dimension), the number of experts $K$ used in the main experiments (only stated for the ablation), and learning rates / optimizers for both the experts and the EBM are not specified. These details would aid reproducibility and independent verification.

### Trivial

- The paper states "SVSL requires desing a punishment function" (line 154) — a minor typo.

## Nice-to-Haves

- An ablation comparing Di-SkilL with EBM-based $\pi(\mathbf{c}|o)$ against a variant using Gaussian $\pi(\mathbf{c}|o)$ (with the punishment term from SVSL) would directly isolate the benefit of EBMs over Gaussian distributions.
- A sensitivity analysis on the number of experts $K$ would strengthen the work.
- Visualizing the learned per-expert context distributions (e.g., as heatmaps) would more directly illustrate the multi-modality that EBMs enable.
- Evaluating on higher-dimensional context spaces (>5 dims) would test the scalability of the EBM batch approximation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Ablation conflates multiple modifications" (Harsh Critic, Section-by-Section Notes).** The reviewer claimed that the ablation changes both sample count and objective simultaneously. This is incorrect: Di-SkilLwoCurV1 uses the *same* 50 samples/expert as Di-SkilL, cleanly isolating the curriculum intervention. V2 adds more samples specifically to test whether more data compensates — a well-controlled design, not a confounding artifact.

2. **"PPO usage is not explained" (Harsh Critic, Section-by-Section Notes).** PPO (clipping, advantage estimation) is standard knowledge in RL. The paper correctly identifies that PPO can be applied to update $\pi(\mathbf{c}|o)$ and shows the resulting objective (Eq. 10). Further implementation detail is standard field knowledge, not an omission.

3. **"LinDi-SkilL is not an established baseline" (Harsh Critic, Critical Issue 2).** The paper never claims LinDi-SkilL is an established baseline — it is explicitly an ablation variant designed to isolate the effect of deep experts from the EBM context distributions. Comparing Di-SkilL vs. LinDi-SkilL isolates deep experts; comparing LinDi-SkilL vs. SVSL (via the ablation) isolates the EBM. The reviewer's characterization misreads the paper's experimental design.

## Novel Insights

The most insightful observation emerging from the reviews is that the paper's two claimed contributions (deep experts + EBM context distributions) are not equally well-supported. The benefit of deep experts over linear experts is convincingly demonstrated by the Di-SkilL vs. LinDi-SkilL comparisons and the SVSL results in the ablation. However, the benefit of EBMs specifically (over Gaussian context distributions with penalty terms) is never directly ablated — the comparison to SVSL is the closest proxy, but SVSL changes both the distribution family and the penalty mechanism simultaneously. A cleaner isolation of the EBM's advantage would strengthen the paper significantly. Additionally, the diversity claim — arguably the paper's most eye-catching contribution — rests entirely on qualitative evidence, which is a notable gap given that diversity can be quantified via multiple standard metrics in the skill-discovery literature.

## Suggestions

1. **Quantify diversity.** Report at least one metric: entropy of the per-expert context distributions, variance of rollout outcomes per context, or number of distinct behavioral clusters. If some metrics are uninformative for certain tasks, explain why.
2. **Include SVSL on at least one additional multi-modal task** (e.g., Box Pushing) to strengthen the baseline comparison. If implementing the punishment function is genuinely prohibitive, state this more explicitly and discuss the limitations.
3. **Add a direct EBM vs. Gaussian ablation.** Replace the EBM-based $\pi(\mathbf{c}|o)$ with a Gaussian + punishment term (as in SVSL) while keeping deep experts — this isolates the benefit of EBMs from deep experts.
4. **Specify the EBM architecture** (layers/activations of $\phi_o(\mathbf{c})$) and the number of experts used in main experiments to aid reproducibility.
5. **Recharacterize the Reacher claim** if CIs overlap — either drop the claim of "higher return" or report effect size with appropriate caveats.

## Score and Decision

The paper proposes a technically sound combination of EBMs, deep MoE, and trust-region updates for diverse skill learning in CEPS. The core ideas are well-motivated and the results on multi-modal tasks (Box Pushing, Minigolf) are genuinely strong. However, two significant gaps — the absence of quantitative diversity metrics (weakening the paper's central framing) and incomplete comparison against the strongest prior work — prevent the contributions from being fully established. These issues are addressable but non-trivial.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>