---
job_id: 851023b7-91cb-4ab0-9a85-873b318201d5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: khBHJz2wcV.pdf
paper: Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies flow-matching generative models, post-training adaptation, inverse problems, and physics-informed machine learning.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, presents a coherent method with equations, algorithms, figures, and quantitative experiments, and provides enough empirical evidence to support a full review, even though several claims and design choices remain insufficiently justified.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompt-targeting text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a post-training framework for fine-tuning pretrained flow-matching models so that generated samples better satisfy physical constraints expressed through PDE residuals, while also inferring latent physical parameters needed to evaluate those constraints. The method combines weak-form residual rewards, an inverse predictor for latent parameters, and Adjoint Matching to jointly evolve state and parameter trajectories, and is evaluated on several PDE benchmarks plus a natural-image recoloring example.

## Strengths
The paper tackles a relevant problem at the intersection of generative modeling and scientific ML, namely how to adapt a pretrained generative model when only state observations are available but the physical constraint depends on unobserved parameters. That setup is meaningful and not just a cosmetic variant of standard conditional generation.

The paper has a reasonably broad empirical scope. The experiments span Darcy flow, elasticity, Helmholtz, Stokes, sparse-guidance conditioning, and a non-PDE image example. Even if not all evaluations are equally convincing, the breadth does help demonstrate that the framework is intended as a general post-training recipe rather than a one-off result.

The qualitative figures do communicate some of the intended trade-offs well. In particular, **Figure 2** is useful because it shows the effect of the regularization term \( \lambda_f \) on the Darcy example in a way that is easy to interpret: with regularization, the fine-tuned sample stays visually closer to the base trajectory, while removing regularization gives a cleaner but more altered inferred parameter field. Likewise, **Figure 3** makes the control knobs fairly transparent by showing how increasing \( \lambda_x,\lambda_\alpha \) lowers residuals while reducing diversity, and how sweeping \( \lambda_f \) trades residual reduction against distributional fidelity. These figures support the claim that the method exposes a tunable residual-fidelity trade-off, rather than hiding it behind a single cherry-picked setting.

There are quantitative results where the proposed joint model appears meaningfully better than the ablations. In **Table 2** for Helmholtz, the full joint AM variant improves both residual metrics and \( \mathrm{MMD}_x \) relative to Base AM / Base AM+\(\varphi\), which is one of the cleaner pieces of evidence that jointly modeling \((x,\alpha)\) is actually helping rather than simply adding complexity. The Stokes trade-off in **Figure 5** also supports the narrower claim that the joint model reaches a region with substantially smaller \( \mathrm{MMD}_\alpha \) than the ablations.

The method is presented with enough algorithmic detail to be intelligible. The paper does not just wave at “physics loss”; it specifies the weak residual idea, introduces the surrogate parameter flow, gives the control formulation in **Equation (2)**, the adjoint dynamics in **Equation (3)**, the matching loss in **Equation (4)**, and includes an explicit training algorithm. That is a real strength compared to many papers in this area that stay too high level.

## Weaknesses
1. **The central theoretical positioning is stronger than what the main paper really establishes.**  
   The paper repeatedly leans on the theoretical grounding of Adjoint Matching, but the actual method used here departs from the clean setting in several important ways: a surrogate parameter flow built from \(\varphi\), a scaled memoryless schedule with parameter \(\kappa\), time-grid tilting, clipped losses, partial time-step supervision, and a regularization cost \(f(\alpha)=\lambda_f\|v^{\mathrm{ft}}_{t,\alpha}-v^{\mathrm{reg}}_{t,\alpha}\|^2\). In **Section 3.3**, the paper states that consistency with the reward-tilted target distribution holds “with \(f=0\)” under a memoryless schedule, but the actual training setup used in experiments layers multiple heuristics on top. This matters because the paper sells the approach as theoretically grounded, yet the practical algorithm is a fairly engineered variant whose relation to the intended target distribution is no longer clear from the main text. The scaled schedule claim is also only deferred to an appendix lemma, while the practical solver modification \(\eta_t=(1-t+h)/(t+h)\) is an additional deviation that weakens the clean interpretation further. I do not object to heuristics per se, but the paper should be much more explicit about which parts are theory-backed and which parts are pragmatic stabilizers.

2. **The joint parameter evolution is conceptually interesting, but its probabilistic meaning is underspecified and arguably shaky.**  
   In **Section 3.2**, the “base” parameter flow is not learned from data and not derived from an actual joint process; it is constructed from a one-step terminal estimate
   \[
   \hat{x}_1=x_t+(1-t)v_t^{\text{base}}(x_t), \qquad \hat{\alpha}_1=\varphi(\hat{x}_1),
   \]
   and then converted into
   \[
   v_{t,\alpha}^{\text{base}}(\alpha_t)=\frac{\hat{\alpha}_1-\alpha_t}{1-t}.
   \]
   This is a strong surrogate assumption. The paper never really clarifies what distribution over \(\alpha\) is being represented along the path, why Gaussian initialization \(\alpha_0\sim \mathcal N(0,I)\) is sensible for PDE coefficient fields, or whether the induced joint process has any consistency guarantees beyond being useful as a regularizer. This matters because a major contribution claim is “joint generation of physically consistent solution-parameter pairs”. As written, the method can certainly produce pairs, but it is less clear that those pairs should be interpreted as samples from any meaningful joint target distribution, rather than outputs of a coupled heuristic denoising system.

3. **There are mathematical and notation issues in the main method section that make careful verification harder than it should be.**  
   In **Section 3.2**, the sentence “this can be achieved by directly learning the vector field \(v_{t,\alpha}^{\text{R}}\) jointly with \(v_{t,\alpha}^{\text{R}}\)” appears to repeat the same symbol and likely intends a joint state/parameter field, which is confusing in a central part of the paper. In **Equation (3)** and the surrounding text, gradients are written with respect to \(\hat{x}\), even though the augmented state is denoted \(\hat{X}_t=(X_t^\top,\alpha_t^\top)^\top\); that is a notational mismatch right where the adjoint system is introduced. Also, **Equation (1)** defines \(\eta_t=\gamma_t((\dot{\beta}_t/\beta)\gamma_t-\dot{\gamma}_t)\), but the numerator/denominator dependence is easy to misread and the notation is not carried consistently into later formulas. These are not just cosmetic complaints. For a paper whose contribution is built around a careful control/adjoint formulation, sloppiness in notation directly lowers confidence that the proposed extension has been derived and implemented cleanly.

4. **The weak-residual construction is sensible, but the exact reward being optimized is not standardized across tasks, which makes cross-benchmark interpretation slippery.**  
   In the main paper, **Section 3.1** defines a generic weak residual
   \[
   \mathcal R_{\text{weak}}(x,\alpha)=\frac{1}{N_{\text{test}}}\sum_{i=1}^{N_{\text{test}}}|\langle \mathcal L_\alpha x,\psi^{(i)}\rangle|^2,
   \]
   but the appendix then introduces task-specific normalizations: by mean permeability, mean modulus, local Helmholtz energy, or viscosity-weighted kinetic energy. Those choices may be reasonable, but they are quite consequential. They affect the scale of the reward, the gradient magnitudes, and the reported “relative residual” numbers. This matters because many of the main empirical claims are framed as broad residual reductions across tasks, yet the residuals are not entirely comparable objects. The paper should explain in the main text why these normalizations are the right ones, and how sensitive results are to them.

5. **The evaluation protocol favors the proposed method in a way that is not fully disentangled.**  
   The reference set \(\mathcal D_{\mathrm{ref}}\) is defined in **Section 4** as a synthetic clean dataset generated under the target PDE specification assumed during fine-tuning. Residuals and MMDs are then computed against this target-specification reference set. For misspecification settings, this means the evaluation is explicitly aligned with the fine-tuning objective rather than with the original observational data distribution. That is acceptable if the paper’s goal is adaptation toward target physics, but then claims about “preserving the learned distribution” need more care. In several places the paper suggests both physics improvement and fidelity preservation, yet fidelity is largely assessed relative to a synthetic target set, not the original observed-data distribution. This distinction matters a lot scientifically, because otherwise one can trade off toward the assumed model class and call it an improvement even if one has drifted from the empirical distribution that motivated the pretraining.

6. **Some baseline choices are useful, but the comparison landscape is still incomplete and occasionally framed too favorably.**  
   The baselines include PBFM, Base AM, Base AM+\(\varphi\), and in elasticity an ECI-style method. That is a reasonable starting point, but there is no direct comparison to simpler post-hoc alternatives such as optimizing \(\alpha=\varphi(x_1)\) only at the endpoint and then performing gradient-based correction of the sample, or alternating sample correction with parameter inference without learning a full joint flow. This is important because the proposed joint flow adds substantial machinery. The paper needs stronger evidence that the gains are not attainable with a simpler endpoint-parameterization approach. Also, the text in **Appendix E.2** notes that all PDE settings deliberately introduce mismatch and that this “naturally places [PBFM] at a disadvantage”. That is honest, but it also means the headline cross-method comparison should be interpreted cautiously. A baseline set that is partially mismatched to the chosen evaluation regime is not enough to establish superiority of the proposed design.

7. **The main-paper quantitative reporting is selective and occasionally hard to parse.**  
   The linear elasticity table is presented awkwardly: the table appears before the label “Table 1” description on **Page 9**, and the text around it is easy to misread. More importantly, the main paper often presents “representative configurations” rather than systematic best-vs-best or Pareto-front summaries. For example, **Table 2** explicitly reports representative configs selected either by lowest weak residual or lowest \( \mathrm{MMD}_x \). That is not wrong, but it makes the comparison somewhat pliable because different methods may be highlighted under different selection criteria. Since the paper’s whole story is about navigating a multi-objective trade-off, a cleaner presentation would report Pareto fronts or matched operating points in the main paper, not just representative snapshots.

8. **There is evidence of instability or possible reporting issues in the appendix tables, and the main text does not discuss them.**  
   The most glaring example is **Table 12** on Helmholtz, where the last row reports for AM with \(\lambda_x=100M\), \(\lambda_f=1\),
   \[
   R_{\text{weak}} = 4.32 \times 10^9 (\pm 1.43),
   \]
   while neighboring rows are around \(10^0\). This is either a typo or a severe instability, but the paper never flags it. If it is a typo, that reflects poor table verification; if it is a real divergence mode, then the robustness picture is incomplete. Similarly, several tables show highly non-monotone behavior as \(\lambda_x\) increases, especially in Darcy (**Table 10**) where weak residual first improves and then worsens dramatically for large \(\lambda_x\), while MMD remains tiny for some AM settings. Those patterns deserve explicit discussion, because they suggest the method is quite sensitive and the optimization story is less tidy than the main text implies.

9. **The natural-image experiment is too thin to carry much weight as a cross-domain validation.**  
   The image section is visually appealing, and **Figure 6** does suggest that the joint recoloring pathway can create more vibrant prompt-aligned outputs than vanilla Adjoint Matching. But as a scientific experiment it is underdeveloped. There is one main prompt/class example in the body, no quantitative metric in the main text, and no clear ablation isolating whether the gain comes from the joint parameter pathway versus simply adding a hand-designed color transform family. So the cross-domain claim is more of a demonstration than a convincing validation.

10. **The paper overstates preservation of diversity and sample-specific detail relative to the evidence shown.**  
    In Darcy, **Figure 3(a)** uses SSIM-based diversity on inferred parameter maps, and **Figure 3(b)** uses \( \mathrm{MMD}_x \) versus residual under varying \( \lambda_f \). These do show a trade-off, but they are limited proxies. For example, low \( \mathrm{MMD}_x \) to the target reference set does not directly establish preservation of the base model’s diversity; it only suggests closeness to one reference distribution. Likewise, preserving sample-specific detail is illustrated nicely in **Figure 2**, but only qualitatively and for a single seed. This matters because the paper repeatedly claims that physical validity is improved “without distorting the underlying learned distribution” or “without significantly affecting sample diversity”. The presented evidence supports a softer, narrower statement, not the stronger one.

## Questions
1. The most important clarification I would like is about the target distribution actually induced by the full practical algorithm. In **Section 3.3**, consistency is discussed for \(f=0\) under a memoryless schedule, but the experiments also use surrogate parameter flows, clipped losses, tilted time grids, selective time-step losses, and sometimes \( \lambda_f>0 \). Which parts of the final training procedure should be viewed as preserving the target-tilting interpretation, and which parts are purely heuristic?

2. Can the authors justify more explicitly why the surrogate parameter base flow
   \[
   v_{t,\alpha}^{\text{base}}=\frac{\hat{\alpha}_1-\alpha_t}{1-t}, \qquad \hat{\alpha}_1=\varphi\!\left(x_t+(1-t)v_t^{\text{base}}(x_t)\right)
   \]
   is the right construction? In particular, is there any empirical evidence that evolving \(\alpha_t\) along this surrogate path is better than only predicting \(\alpha_1\) at the endpoint and training a joint model against that terminal parameter?

3. Please discuss the sensitivity of results to the weak-residual normalization choices and to the sampled test-function family. Since the residual definitions differ substantially across tasks, it would increase confidence if the authors could show that the method’s relative ranking is not an artifact of a particular normalization or test basis.

4. For the tables reporting representative configurations, can the authors provide a more systematic selection rule in the rebuttal? For example, matched-\( \mathrm{MMD}_x \) comparisons, matched-residual comparisons, or Pareto-front plots in the main paper would make cross-method evaluation cleaner.

5. In **Table 12**, is the \(4.32\times 10^9\) weak residual a typo or a real failure mode? If it is real, the paper should discuss instability regions and not only the successful operating points. If it is a typo, that needs correction because it currently undermines confidence in table quality.

6. The image experiment would be more convincing with at least one quantitative comparison, even if modest, such as PickScore before/after fine-tuning and a measure of image-distribution drift. Can the authors provide that?

7. The paper claims the method can preserve the learned distribution while enforcing physics. What additional evidence can the authors provide for preservation relative to the original observational data distribution, not just relative to the clean target-PDE reference set?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are apparent from the main paper. The work is methodological, uses synthetic PDE datasets plus ImageNet-based image generation, and does not appear to introduce unusual privacy, bias, or human-subject issues beyond standard generative-model considerations.

## Soundness Rating
3: good. The core method is plausible and supported by several experiments, but the theoretical framing is looser than advertised once the practical heuristics are included, and some empirical/reporting issues reduce confidence.

## Presentation Rating
2: fair. The paper is readable overall and includes useful figures, but there are notable notation inconsistencies, some awkward table presentation, and several key assumptions are explained less clearly than they should be for a method-heavy submission.

## Contribution Rating
3: good. The combination of adjoint-matching fine-tuning, weak-form residual rewards, and latent-parameter evolution for post-hoc physics-aware adaptation is meaningful and relevant, though I am less convinced by the strength of the theoretical and empirical case than the paper suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
The paper addresses an interesting and important problem, and there is enough substance here, especially the joint state-parameter fine-tuning angle and the multi-domain evaluation, to justify a cautious positive recommendation. That said, the work is not as clean as the narrative suggests: the probabilistic meaning of the joint flow is underspecified, the practical method relies on several unprincipled stabilizers, and the empirical section would benefit from more systematic comparison and clearer reporting. So this is above threshold for me, but not comfortably.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant generative-model / scientific-ML area, though some implementation-specific appendix details were too extensive to fully verify line by line.