---
job_id: 745f91b5-8f01-4f58-a492-6f7186659f25
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cP9ciYglnI.pdf
paper: Shape-Adaptive Guidance Signal for Interactive Cortical Sulcal Labeling
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically geometric deep learning, representation learning on spherical domains, and applications to neuroscience and cognitive science.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, presents a concrete method with equations and experiments, and the empirical evidence is substantial enough to avoid desk rejection, even though there are notable methodological and presentation weaknesses.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies interactive cortical sulcal labeling on spherical cortical surface representations, with a focus on small and anatomically variable sulci in the lateral prefrontal cortex. The main idea is to encode user clicks using a curvature-aware weighted geodesic distance transform, obtained by solving an eikonal equation on the sphere with a speed function derived from mean curvature, and to feed these signals into a spherical CNN for iterative refinement. Experiments on 72 HCP subjects and 17 sulci show improved performance over equidistance-based click encodings and over several fully automatic sulcal labeling baselines, especially for small and variable sulci.

## Strengths
The paper addresses a real and important problem. Small and shallow sulci are genuinely difficult to label automatically, and this is well motivated in the paper, especially through the anatomical variability shown in **Figure 1**. The application is not a toy setting, and the interactive formulation is well aligned with actual neuroimaging workflows where expert correction is often unavoidable.

The central design idea is sensible and reasonably well matched to the domain. Encoding clicks by solving an eikonal equation with curvature-dependent speed is a natural way to make the guidance signal follow sulcal valleys instead of spherical proximity alone. The contrast shown in **Figure 3** is one of the more convincing parts of the paper: compared with ADT and Disk, the WGDT signal is visibly more localized along folds and appears to reduce spillover into unrelated regions. That figure helps the reader understand why the proposed signal might matter, rather than presenting it as just another heuristic click map.

The empirical effect size on the hard cases is strong. The ROI-wise comparisons in **Figure 4** and the detailed values in **Table 4** show that the main gains are concentrated where they should be, namely the small and variable sulci. For example, several tertiary sulci improve by large margins at the first click under WGDT compared with ADT/Disk, whereas large and consistent sulci are mostly similar across guidance types. That pattern is scientifically plausible and supports the paper’s main claim better than a single global average would.

The comparison to automatic baselines is useful and stronger than many application papers provide. **Figure 5** and **Table 5** show that one click already closes a substantial part of the gap for difficult sulci, and often surpasses the automatic methods by a wide margin. The qualitative examples in **Figure 6** are also aligned with the quantitative story, particularly in the boxed regions where the fully automatic models either miss or fragment small sulci while WGDT recovers a more complete extent.

The runtime analysis in **Table 2** is a good addition. It is not flashy, but it matters for interactive methods. Showing sub-second latency per click makes the approach more credible as an actual annotation aid rather than a purely offline refinement scheme.

The paper is generally readable, and **Figure 2** gives a clear high-level overview of the pipeline, including the role of geometric features, click channels, optional current prediction, and iterative refinement.

## Weaknesses
1. **The empirical scope is narrower than the framing suggests, and this matters for the claimed usefulness of the method.**  
   The title and introduction read broadly, but the experiments are limited to **72 subjects, left hemisphere only, LPFC only, and 17 sulci** from one dataset, as described in **Section 3.1**. For a method whose key claim is shape-adaptive interactive cortical labeling, this is a fairly specific setting. The concern is not simply “more data would be nice”; it is that the proposed speed function in **Equation (4)** is explicitly tied to a sign convention and morphology of cortical folds, and it is not obvious from the paper that the same design would work equally well in other cortical territories, under different preprocessing pipelines, or in pathological anatomy. The discussion acknowledges this partially, but the experimental validation remains narrowly scoped relative to the paper’s broader language.

2. **The comparison space is incomplete for an interactive segmentation paper, even if direct cortical interactive baselines are unavailable.**  
   In **Section 4.2**, the authors compare only against fully automatic sulcal labeling methods. I understand the claim that no prior interactive sulcal labeling method exists, but the paper still needed stronger comparative context for the interactive component itself. Right now, the core method is “spherical interactive segmentation + specific guidance signal,” but the experiments do not disentangle how much of the gain comes from interactivity per se versus the particular WGDT encoding. A stronger experimental design in the main paper would have compared:  
   - WGDT initialized from the output of a strong automatic baseline versus from scratch,  
   - single-click WGDT versus simply post-processing or selecting among automatic predictions,  
   - at least one non-spherical but interactive geometric baseline, even if adapted imperfectly.  
   Without this, the paper’s contribution is somewhat trapped between two comparisons, one too weak to test the signal design fully, and one not really interactive.

3. **Several mathematical definitions are underspecified or imprecise enough to affect reproducibility and interpretation.**  
   The first issue is the labeling loss in **Equation (6)**:
   \[
   \mathcal{L}_{\mathrm{label}}^{i}=-\sum_{n\in\{0,1\}}\log(p_n, z_n).
   \]
   As written, this is not a valid cross-entropy expression. The notation \(\log(p_n, z_n)\) is undefined, and there is no explicit dependence on vertices/pixels. If the intended loss is binary cross-entropy over spherical samples, it should look something like
   \[
   \mathcal{L}_{\mathrm{label}}^{i}
   = - \sum_{v} \left[z_v \log p_v^{(i)} + (1-z_v)\log(1-p_v^{(i)})\right],
   \]
   or an equivalent two-class cross-entropy over vertices. As currently written, the objective is mathematically incomplete.

   A related issue is the model definition in **Section 2.1**. The paper says the model output is a binary discriminant function \(\mathcal{F}:\mathbb{R}^K \rightarrow \mathbb{R}^2\) to infer labels at each \(\mathbf{x}\in \mathbb{S}^2\), but the actual input includes geometric features, current prediction, and two click channels. So the input dimensionality is not really \(K\), but at least \(K+3\) if the current prediction is used, and possibly iteration-dependent. This sounds small, but it reveals a broader sloppiness in the formalization of the actual learning problem.

4. **The eikonal-based formulation is intuitive, but the theoretical description around Equations (3) to (5) is a bit shaky.**  
   The paper states that in this setting \(F\) is isotropic and then defines
   \[
   F\left(\mathbf{x},\frac{\nabla u_{\mathbf c}(\mathbf{x})}{\|\nabla u_{\mathbf c}(\mathbf{x})\|}\right)=c^{kH(\mathbf{x})}
   \]
   in **Equation (4)**. If \(F\) is isotropic, the directional argument should be unnecessary, and the notation should be simplified accordingly. More importantly, the meaning of the constant \(c\) is never defined in the main text. I assume this is the exponential base, but as written \(c\) appears as an undeclared parameter. Since the propagation speed depends exponentially on curvature, this omission is not cosmetic. The choice of base directly affects the dynamic range and interacts with the later clamping to \([0.05,10]\).  

   There is also a conceptual inconsistency in the sentence right before **Equation (4)**: the paper says it solves the eikonal equation “with a constant speed in all directions,” but the whole point is that the speed varies spatially with \(H(\mathbf{x})\). The intended meaning is presumably isotropic but spatially varying speed. That should be stated precisely, otherwise the formulation looks more hand-wavy than it needs to.

5. **The click simulation protocol is plausible, but not sufficiently validated as a surrogate for real user behavior.**  
   The method depends heavily on simulated clicks, both for training and evaluation, as described in **Sections 2.2 and 3.3**. The initial click strategy is especially favorable: 10 initial clicks are selected to maximize distance from the boundary and mutual separation, then performance is averaged across those runs. This design gives coverage over possible starts, but it also biases the evaluation toward relatively central, informative clicks. For a paper arguing annotation efficiency, that matters. Human users do not necessarily click near the geodesic center of the target or at nicely separated locations. The weighted sampling from the largest error component is a reasonable training heuristic, but the paper currently treats this as if it were a neutral approximation rather than a potentially optimistic one. At minimum, the main paper should discuss how sensitive the gains are to less ideal first-click placement.

6. **The evaluation protocol mixes per-sulcus training and binary segmentation in a way that weakens the practical claim.**  
   In **Section 2.1**, the authors explicitly train a separate model for each sulcus, leading to 17 separate binary models. This makes the problem much easier than general multi-label interactive cortical annotation, because the user is already assumed to know which sulcus-specific model is being invoked. The paper is transparent about this choice, which I appreciate, but its implications are underplayed. In practice, the bottleneck is often not just refining a known sulcus mask, but deciding which sulcus is which in a crowded local neighborhood. The results are therefore best interpreted as sulcus-specific interactive refinement, not general interactive cortical sulcal labeling. That distinction should be made much more explicit in the claims.

7. **The statistical reporting is weaker than it should be for the amount of significance language used.**  
   The paper repeatedly states “significant” improvements in **Figures 4 and 5** and in **Sections 4.1 and 4.2**, with FDR correction over 17 sulci. However, the main paper does not report actual adjusted \(p\)-values, effect sizes, or confidence intervals for the pairwise comparisons. Since many differences for the large sulci are small, and many for small sulci are large, effect size reporting would help separate “statistically nonzero” from “practically meaningful.” This is particularly important because the paper’s central message is about reducing human effort with fewer clicks. Statistical significance alone is not the right lens for that claim.

8. **The exposition has several avoidable clarity issues that reduce confidence, even though the overall narrative is understandable.**  
   There are repeated wording and notation issues throughout the paper. A few examples:  
   - In **Section 3.2**, the sentence “We used WGDT signal of \(k \in [6,8,10]\)” is awkward and does not clarify model selection.  
   - The paper says the optimal \(\sigma\) for WGDT was determined by evaluating multiple configurations, but the main paper does not clearly state whether this tuning used validation folds only. Given the cross-validation setup in **Section 3.3**, this should be explicit to rule out any suspicion of test-informed selection.  
   - **Table 1** is confusingly formatted; “aalf” appears duplicated and the layout makes it unnecessarily hard to identify the 8 large versus 9 small sulci. For a domain-specific paper with many acronyms, this is a nontrivial presentation problem.  
   These issues are individually fixable, but collectively they make the paper feel less polished than it should be.

9. **The qualitative evidence is supportive but somewhat curated, and the paper does not show failure modes.**  
   **Figure 6** is visually persuasive, but it presents only two example participants and focuses on highlighted wins for WGDT. For an interactive paper, it would be useful to see counterexamples: cases where WGDT still leaks into adjacent sulci, where curvature guidance over-follows a fold, or where ADT/Disk are actually adequate. Similarly, **Figure 4** compresses a lot of information into many subplots, but the paper does not quantify click-efficiency in a task-level way such as “number of clicks needed to exceed a Dice threshold.” Since the practical claim is reduced user effort, that metric would have been more direct than only reporting Dice after 1, 2, and 3 clicks.

## Questions
1. **Loss definition and notation.**  
   Please clarify **Equation (6)** precisely. What is the exact per-vertex loss used during training, and over which vertices is it summed or averaged? As written, the cross-entropy is not mathematically well specified. A corrected formula would materially increase my confidence in the implementation details.

2. **WGDT speed function details.**  
   In **Equation (4)**, what exactly is the constant \(c\)? Is it Euler’s number, a tunable base, or fixed elsewhere? Also, please clarify whether \(F(\mathbf{x})\) is spatially varying but isotropic, which seems to be the intended meaning, rather than “constant speed in all directions” in the literal sense.

3. **Hyperparameter tuning protocol.**  
   Please state explicitly how \(\sigma\) and \(k\) were selected within the 5-fold cross-validation procedure in **Sections 3.2 and 3.3**. Were these tuned using validation folds only, separately inside each training split? A crisp answer here would help dispel concerns about optimistic evaluation.

4. **Sensitivity to first-click quality.**  
   Could you provide, in the rebuttal, either an analysis or at least a summary of performance when the initial click is sampled less centrally or more noisily than in the current protocol? Since the evaluation currently uses boundary-distant, mutually separated initial clicks, I would like to understand whether the WGDT advantage persists under more realistic click noise.

5. **Role of interactivity versus signal design.**  
   Could the authors clarify how much gain comes from the click-guided refinement framework itself versus the specific curvature-aware encoding? For example, how well does WGDT do when initialized from a strong automatic baseline prediction, and how much additional improvement is obtained per click? This would sharpen the practical deployment story suggested in **Section 5**.

6. **Per-sulcus models and practical usage.**  
   In a realistic annotation workflow, how is the sulcus-specific model chosen? Is the intended use case that an expert selects a target sulcus and then refines only that sulcus, or do the authors envision a future multi-sulcus interactive system? Clarifying this would help calibrate the practical significance of the current setup.

7. **Reporting of significance and effect size.**  
   If space permits in the revision, please report at least representative adjusted \(p\)-values and effect sizes for key ROI-wise comparisons in **Figures 4 and 5**. This would make the statistical claims more informative than simply marking significance thresholds.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The paper uses de-identified neuroimaging data from an established public dataset and focuses on a labeling method; I do not see a specific ethics issue that requires escalation based on the main paper.

## Soundness Rating
3: good. The method is plausible and empirically supported, but there are important concerns about mathematical precision, evaluation realism, and the narrowness of the validated setting.

## Presentation Rating
3: good. The paper is generally readable and the figures are helpful, but several notation issues, an incorrect or incomplete loss equation, and some confusing tables reduce clarity.

## Contribution Rating
3: good. The curvature-aware guidance signal for spherical interactive sulcal labeling is a meaningful contribution for this application area, though the practical scope is narrower than the framing suggests and the validation does not fully establish generality.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles a relevant problem, proposes a technically sensible domain-aware guidance signal, and shows convincing gains on the difficult sulci. I am positive overall, but only narrowly so, because the formalization needs cleanup, the evaluation is narrowly scoped, and the click simulation protocol likely paints a somewhat optimistic picture of real use.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. The application domain is specialized, but I carefully checked the method formulation, figures, and quantitative evidence.