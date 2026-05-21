---
job_id: f7f16ec9-4bae-4f78-8055-6c92572e4123
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FMjeC9Msws.pdf
paper: The Art of Scaling Reinforcement Learning Compute for LLMs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly in scope for ICLR, specifically reinforcement learning, large-scale learning, optimization, and language model post-training.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including abstract, introduction, methodological setup, empirical study, quantitative results, related work, and conclusion. While I have substantive concerns about some methodological choices and the breadth of validation, the submission clears the minimum bar for a full review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies how RL training performance for LLMs scales with compute, and proposes modeling validation pass rate as a sigmoidal function of training compute. Based on a large empirical study over many recipe choices for reasoning-focused RL, the authors identify factors that mainly affect asymptotic performance versus compute efficiency, and combine the best-performing choices into a practical recipe, SCALERL. They further show long-run extrapolation results up to 100k GPU-hours and report transfer trends across model size, sequence length, batch size, and multi-task training.

## Strengths
The paper tackles an important and timely problem. RL post-training for LLMs is now expensive enough that a scaling methodology is genuinely useful, and the paper makes a serious attempt to move this space away from anecdotal recipe chasing and toward a more predictive framework.

The empirical effort is substantial. The claimed 400k+ GPU-hours, together with multiple ablation axes and extended training runs, gives this paper a level of experimental ambition that is uncommon in academic RL-for-LLM work. Even if one disagrees with parts of the analysis, the scale of the study makes the observations hard to dismiss as toy phenomena.

The central framing is simple and practically useful. The decomposition of scaling behavior into asymptotic performance \(A\), efficiency \(B\), and midpoint \(C_{\mathrm{mid}}\) is easy to interpret, and **Figure 3** does a good job of visually explaining what each parameter means. This figure is one of the clearest parts of the paper, because it translates an otherwise abstract fitting choice into an operational language for comparing recipes.

The long-horizon extrapolation result is compelling. In **Figure 1(a)**, the extrapolated curve from earlier compute aligns reasonably well with the later observed points on the 8B run, and the same general story is claimed for the Scout MoE setting. This is the strongest evidence in the paper for the practical value of the proposed fitting methodology. The downstream trend in **Figure 1(b)** is also useful, because it shows that the scaling story is not purely an artifact of the iid validation split.

The cross-recipe comparison in **Figure 2** is informative. The paper does not only introduce a recipe, it also tries to evaluate prevalent alternatives under a common scaling lens. That is a contribution by itself. I especially appreciate that the figure includes both fitted and extended points, rather than only showing the fit and asking the reader to trust the extrapolation.

Several ablations surface non-obvious findings. For example, the claim that many interventions primarily modulate efficiency rather than asymptotic ceiling is interesting and, if broadly true, would matter a lot for how people design RL sweeps. The leave-one-out analysis in **Figure 5** is also a sensible way to check whether components still matter after composition into the final recipe.

The paper is generally readable, and the high-level organization is solid. I found the transition from baseline formulation in Section 2 to forward ablations in Section 3 and composition in Section 4 fairly easy to follow.

## Weaknesses
1. **The main empirical scope is narrower than the paper’s rhetoric suggests, and this matters for the central scientific claim.**  
The title and abstract frame the work as a general study of scaling RL compute for LLMs, but the main body is overwhelmingly centered on verifiable-reward math reasoning with one primary training dataset, Polaris-53k, one main dense model scale, and one main reward structure of \(\pm 1\) correctness. This is acknowledged partially in Sections 2 and 7, but the paper still uses broad language such as “science of RL scaling” and “predictable scaling returns across RL compute axes.” That is too expansive relative to the evidence actually presented in the main paper. The problem is not just missing breadth for its own sake. It directly affects whether the proposed sigmoidal law and the conclusions about which interventions move \(A\) versus \(B\) are properties of RL-for-LLMs more broadly, or properties of one specific regime, namely outcome-supervised math RL with binary rewards and repeated-epoch training on a fixed dataset.

2. **The central fitting methodology is useful, but still fairly heuristic, and the paper undersells how much the conclusions depend on that heuristic.**  
Section 2.1 motivates the sigmoid in Equation (1), and the appendix explains that the authors empirically found it more stable than a power law. Fine. But the operational procedure contains several choices that materially shape the results: excluding the first \(\sim 1.5\)k GPU-hours, fitting on validation pass rate measured every 100 steps, grid-searching over \(A\) and \(C_{\mathrm{mid}}\), and selecting the best fit by residual error. These are not minor implementation details, they define the analysis. Yet in the main paper, the robustness discussion is very light. The claim that “stable, scalable recipes follow predictable scaling trajectories” is stronger than the evidence warrants without showing fit uncertainty, alternative fit families, or sensitivity intervals for \(A,B,C_{\mathrm{mid}}\) in the main text. Put differently, the paper often treats fitted parameters as if they were measured quantities, when they are in fact outputs of a somewhat ad hoc model-selection pipeline.

3. **Several comparisons confound algorithmic effects with systems or batching effects, which weakens causal interpretation.**  
A good example is the off-policy setup comparison in Section 3.1 and **Figure 4(a)**. The paper concludes that PipelineRL substantially improves efficiency \(B\), and the explanation given is reduced idle time. That may be true, but then this is partly a systems-throughput effect, not purely an RL algorithm effect. The paper later essentially admits this in Appendix A.20. Similar confounding appears in recipe comparisons where effective batch size or data filtering strategy changes. In **Figure 2**, some baseline recipes are given different practical accommodations, and Appendix A.17 explains that DAPO and MiniMax are run with larger batch sizes due to codebase constraints. That is understandable from an engineering standpoint, but it complicates any claim that SCALERL’s superior asymptote is due to the recipe itself rather than a bundle of implementation and system decisions. This is especially important because the paper’s framing is about identifying scalable *algorithmic* improvements.

4. **The mathematical exposition around the objectives is sloppier than it should be for a paper whose core claims rely on subtle RL loss design.**  
There are several notation and specification issues in Equations (2), (3), and the SCALERL objective in Section 4. In Equation (2), the shorthand  
\[
\pi_{\text{train}}^\theta(y_{i,t}\mid x,y_{i,<t}) = \pi_{\text{train}}^\theta(y_{i,t})
\]
is written as if the conditional dependence can simply be dropped. I understand this is likely a notational abbreviation, but written literally it is incorrect, and in an off-policy language-model setting that conditioning is the entire object being optimized. In Equation (3), the expectation is written over rollouts from \(\pi_{\mathrm{pdl}}^{\theta_{\mathrm{old}}}\), which appears to be a typo or undefined symbol. Also, the objective uses group-normalized advantages \(\hat A_i^G\), but Section 3 later studies batch-level normalization and no normalization, so the base objective and later variants are not cleanly unified in notation. The SCALERL objective on **Page 8** is more problematic: the sampling notation is garbled, the condition \(0 < \mathrm{mean}(\{r_j\}_{j=1}^G) < 1\) is inserted inside the formula in a way that looks like a filtering constraint but is not mathematically defined as such, \(\theta_{c(x)}\) appears without clear definition, and the denominator \(\sum_{g=1}^G |y_g|\) corresponds to token averaging even though the text describes prompt-level aggregation as part of SCALERL. These are not cosmetic issues. When the paper argues that changing aggregation and normalization changes the asymptote or efficiency, the exact objective matters.

5. **The paper’s strongest performance claim, that SCALERL “surpasses all other methods” and reaches a higher asymptotic reward, is not fully secured by the evidence shown in the main paper.**  
The comparison in **Figure 2** is visually suggestive, but I would be more convinced if the paper reported uncertainty bars over independent runs or at least fit confidence intervals for \(A\). The appendix mentions a rough \(\pm 0.02\) error margin for asymptotic performance based on three SCALERL runs, but that is not integrated into the main comparisons. Given that some reported asymptotic gaps are not huge, it matters whether differences like \(A=0.610\) versus \(A=0.595\) or \(A=0.530\) are stable across seeds and fit choices. Right now, the reader is asked to trust a point estimate from each recipe. For a paper that is explicitly about parameterized scaling curves, the absence of uncertainty quantification in the main plots is a real omission.

6. **The leave-one-out composition story is somewhat weaker than the narrative suggests.**  
Section 4 argues that SCALERL is consistently the most effective configuration, but **Figure 5** actually tells a more qualified story. Many LOO variants appear to achieve very similar asymptotic reward, and the practical difference is mainly in the transformed efficiency plot after fixing a common \(A\). That is still useful, but it means the paper’s “best-practice recipe” is less of a crisp scientific discovery and more of a careful collection of modest improvements. The issue is not that the recipe is incremental, that is perfectly acceptable, but the paper should be more explicit that several ingredients have small standalone effect once combined. Otherwise, the framing risks overstating how uniquely optimal the recipe is.

7. **The validation protocol is sensible for scaling-curve fitting, but it leaves open a deeper concern about over-specialization to iid held-out prompts.**  
The paper repeatedly emphasizes that the main metric should be in-distribution held-out validation rather than downstream benchmarks. I agree this is a defensible choice for studying scaling laws. However, the evidence for generalization beyond the validation distribution remains modest in the main paper. **Figure 1(b)** and **Figure 6** show encouraging downstream trends, but the number of benchmarks is limited and the analysis is largely qualitative. This matters because one of the more interesting claims in the paper is that some knobs, like larger batch size or longer context, may improve generalization more than they improve iid validation. If that is true, then focusing primarily on iid validation may not be sufficient even for the paper’s own broader conclusions about scalable RL.

8. **Some recipe choices are justified with language that is stronger than the evidence.**  
For example, Section 3.2 says batch-level advantage normalization is adopted because it is “theoretically sound and marginally better.” But no actual theory is presented in the main paper to support this phrasing, and the appendix result reportedly shows all variants are similar. Likewise, the paper occasionally speaks as if FP32-at-head is a principled RL scaling ingredient, while the evidence in **Figure 4(c)** is closer to a practical numerical stabilization trick. I do not object to using it, but the paper should distinguish more sharply between scaling principles and implementation fixes.

9. **There are presentation and proofreading issues that are minor individually but noticeable for a paper of this ambition.**  
Examples include “Predicately” in the caption of **Figure 1**, “inclyde” on **Page 6**, inconsistent naming between “ScaleRL” and “SCALERL,” malformed notation in Section 4, and a few confusing references such as “saturating power-law” in Section 5 even though the paper advocates the sigmoid parameterization. These do not invalidate the work, but they contribute to an impression that the manuscript was not polished to the same standard as the experimental campaign.

10. **The paper does not sufficiently discuss failure cases or when the sigmoidal framework should not be trusted.**  
The manuscript says some recipes destabilize, some low-compute regions are excluded, and some methods plateau or degrade. But there is no clear decision rule for when fitting Equation (1) is appropriate versus misleading. In **Figure 2**, stable methods appear to extrapolate reasonably, while unstable ones do not, but the paper does not formalize this distinction. If the method is intended as a practical evaluation tool for future RL recipes, users need guidance on detectability of failure modes, minimum fit window, and how to avoid mistaking transient gains for asymptotic improvement.

## Questions
1. The biggest issue for me is external validity. Can the authors sharpen the scope of their claims in the rebuttal, and provide stronger evidence, preferably from the main-paper experiments already available, for why the sigmoid-law conclusions should transfer beyond binary-reward math RL? Even one additional main-text analysis across a meaningfully different reward/task regime would increase my confidence.

2. Please clarify the exact SCALERL objective on Page 8. As written, the notation appears malformed. In particular:
   - What is the exact sampling distribution in \(\mathcal{J}_{\mathrm{SCALERL}}(\theta)\)?
   - Is the aggregation prompt-level or token-level? The denominator \(\sum_g |y_g|\) suggests token averaging.
   - What exactly do the conditions \(0 < \mathrm{mean}(\{r_j\}) < 1\) and \(\mathrm{pass.rate}(x) < 0.9\) denote, operationally and mathematically?
   A cleaned-up version of this equation would materially improve my confidence.

3. For the comparisons in **Figure 2**, can the authors explicitly tabulate the training settings that differ across recipes in the main paper, including effective batch size, filtering policy, precision, and off-policy setup? Right now the figure is useful, but it is hard to disentangle algorithmic gains from system-level or batching confounds.

4. Can the authors provide uncertainty estimates for fitted \(A\) and \(B\), at least for the key recipe comparisons in **Figure 2** and the LOO study in **Figure 5**? Even approximate confidence intervals, bootstrap bands over evaluation points, or seed-to-seed variability would help a lot.

5. The paper argues that some choices mainly affect efficiency \(B\) and not asymptote \(A\). How stable is that conclusion under alternative fit windows or alternative bounded fit families? I do not need a new massive experiment, but I would like a more explicit robustness argument.

6. For **Figure 4(c)**, can the authors quantify whether the gain from the FP32 precision fix comes primarily from reducing pathological clipping, reducing trainer-generator mismatch in \(\rho_{i,t}\), or improving stability later in training? The appendix hints at this, but the main paper currently treats the mechanism somewhat loosely.

7. In Section 5, the paper suggests longer generation length and larger batch size raise the asymptote. Is that conclusion based on sufficiently long runs for all settings, or could some of these curves still cross later? A clearer statement of what was actually observed versus extrapolated would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The empirical methodology is substantial and many claims are supported, but several central conclusions rely on heuristic curve fitting, some comparisons are confounded, and the mathematical specification of the final objective needs cleanup.

## Presentation Rating
3: good. The paper is generally well organized and figures are helpful, especially Figures 1 to 5, but there are notable notation issues, some malformed equations, and a handful of proofreading inconsistencies.

## Contribution Rating
3: good. The paper makes a valuable contribution by framing RL post-training through a scaling-law lens and backing it with a large experimental study. The contribution is meaningful, though narrower and more heuristic than the broad framing implies.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem, has unusual experimental scale, and offers a practically useful framework and recipe. My hesitation comes from the narrow task scope, the heuristic nature of the fitting pipeline, confounded comparisons, and some sloppiness in the loss specification. Overall I lean positive because the strengths are real and likely useful to the community, but I do not think the paper is as airtight as the headline claims suggest.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with RL for language models and scaling-law style empirical analysis, and I checked the main mathematical and experimental claims carefully, but I did not independently verify appendix-level implementation details.