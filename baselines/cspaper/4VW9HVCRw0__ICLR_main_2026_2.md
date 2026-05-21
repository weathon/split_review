---
job_id: e110c439-cb49-47d1-8ea7-e654b33289d0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 4VW9HVCRw0.pdf
paper: TOUCH: Text-Guided Controllable Generation of Free-Form Hand-Object Interactions
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies conditional generative modeling, representation learning over 3D geometry and text, and introduces a new dataset and benchmark for hand-object interaction generation.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, dataset construction, method, experiments, results, and conclusion; while I have several concerns about evaluation rigor and exposition, these are not so fatal as to warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces the task of free-form hand-object interaction generation, moving beyond grasp-centric settings to generate diverse static hand poses conditioned on object geometry and fine-grained text. To support this task, the paper constructs WildO2, an in-the-wild 3D HOI dataset derived from internet videos, and proposes TOUCH, a three-stage framework with contact map prediction, multi-level conditioned diffusion, and a refinement stage with physical constraints. Experiments on WildO2, with additional analysis on OakInk in the appendix, aim to show improvements in contact accuracy, plausibility, diversity, and semantic controllability over adapted prior baselines.

## Strengths
1. **The paper tackles a meaningful problem that is underexplored in current HOI generation work.** The motivation in Pages 1 to 3 is convincing: much of the prior literature is indeed biased toward stable grasps, while real daily interactions include pushing, poking, placing, rotating, and other non-grasping behaviors. Framing this as “free-form HOI generation” is a useful shift in problem formulation.

2. **The dataset effort is substantial and likely valuable to the community.** WildO2 covers 4,414 reconstructed interactions, 92 intents, and 610 object categories, which is a broader semantic range than typical lab datasets. The pipeline in **Figure 2** is one of the stronger parts of the paper because it makes the acquisition strategy concrete, especially the O2HOI pairing idea and the staged reconstruction/alignment/refinement process. The dataset statistics in **Figure 3** also help justify that the collection is not just more of the same grasp data; the contact-part distribution and action-object-contact relationships support the paper’s claim that the dataset contains richer interaction modes.

3. **The overall method is reasonably well structured and matches the problem decomposition.** The three-stage design in **Figure 4** is intuitive: predict contact, generate pose under multi-level conditions, then refine physically. This is a sensible architecture for a difficult multimodal generation problem where direct text-to-pose mapping would likely drift.

4. **The contact-guided design is empirically supported, at least directionally.** In **Table 2**, removing contact guidance (“×hoc.”) causes a marked drop in P-IoU/P-F1 and worsens MPVPE and P-FID. Likewise, removing the refiner or the cycle-consistency term degrades the main contact-related metrics. Even if some of the evaluation choices need more scrutiny, the ablation trend is coherent and supports the argument that explicit contact modeling matters.

5. **The qualitative results are strong and easier to believe than many papers in this area.** **Figure 5** shows that the proposed method more often matches the intended interaction mode than the baselines, especially for non-trivial prompts where the hand should not collapse to a generic grasp. **Figure 8** is also effective in demonstrating controllability: varying the intent and contact geometry for the same object leads to visibly different hand poses. This is important because many HOI generation papers claim “semantic control” but qualitatively show only minor pose perturbations.

6. **The paper does not ignore physical plausibility, and the refinement stage is not purely cosmetic.** The discussion around the “×refiner” result in **Table 2** is actually useful: the authors correctly note that low penetration can be misleading if the hand simply drifts away from the object. That is a fair and important observation for this task.

7. **The paper is ambitious without being completely hand-wavy.** There is a full pipeline from data construction to generation and evaluation, and the submission includes equations, ablations, and multiple qualitative studies rather than relying only on visual cherry-picking.

## Weaknesses
1. **The empirical comparison is too narrow for the scope of the claims.** The paper’s central claim is that TOUCH advances text-guided, controllable, physically plausible free-form HOI generation, yet the main comparison in Section 5.2 is only against two baselines, ContactGen and an adapted Text2HOI. This is thin for a paper making a new-task and new-dataset argument. The issue is not just the count of baselines, it is that both baselines appear to be substantially adapted to fit the setting, and one of them, Text2HOI, is originally temporal and is explicitly modified by “remov[ing] its temporal axis” on **Page 8**. That introduces ambiguity about whether the comparison is to a strong reference implementation or to a weakened transplant. This matters because **Table 1** is the main evidence for superiority; if the baseline suite is incomplete or only partially native to the setting, the claimed margin becomes less informative.

2. **A large part of the contribution depends on the new dataset, but the main paper does not provide enough validation of dataset fidelity or bias.** The paper says on **Page 5** that the final 4,414 samples are “high-quality” after manual inspection and refinement, but the main text gives almost no quantitative annotation quality analysis, no inter-annotator agreement for manual verification, no reconstruction error benchmark against known 3D HOI data, and no estimate of how often the reconstruction pipeline produces subtly wrong contact geometry. **Figure 3(a)** only shows breakdown statistics of reconstruction outcomes, not accuracy. Since the generation model is trained on reconstructed data rather than native captured 3D HOI, any systematic reconstruction bias can directly shape the model’s behavior. This is especially relevant because several later claims, including contact precision and semantic controllability, depend on the correctness of the reconstructed contact maps and DSC annotations.

3. **Some evaluation metrics are weakly justified for the paper’s headline claims, especially the semantic ones.** The semantic consistency block in **Table 1** uses P-FID, VLM score, and a perceptual score from 10 users. P-FID on hand point clouds is at best an indirect distributional similarity metric; it is not a strong proxy for text-conditioned semantic correctness. The VLM-based evaluation is under-specified in the main paper, including prompt design, scoring rubric, whether the VLM saw similar internet imagery during pretraining, and whether captions leak object-action priors that favor plausible-looking outputs. The user study is also very small, only 10 users according to **Page 7**, with no details on protocol, randomization, or agreement. This matters because the method’s selling point is fine-grained textual control, and the strongest metrics in **Table 1** for that claim are precisely the least well grounded.

4. **The train/test split and resampling strategy raise concerns about effective leakage or at least over-optimistic generalization.** On **Page 7**, the authors state that the split is performed “for each hand part contact category” with a random 4:1 split, and then they resample using unique 7-bit labels to balance the data. This is not obviously wrong, but it is much weaker than splitting by object category, object instance, source video, or intent template. With internet-video-derived data, near-duplicate interactions from the same action family or even same video source can easily appear across train and test if the split is only label-stratified. The paper later emphasizes out-of-domain generalization in **Figure 7**, which implicitly acknowledges this issue, but the main benchmark in **Table 1** remains an in-domain split whose hardness is unclear.

5. **The mathematical specification is serviceable but not sufficiently precise in several places, and there are inconsistencies that should be cleaned up.**
   - In **Equation (6)**, the final loss is written with absolute values, \( |\hat{\mathbf{r}}_{\text{rot}}-\mathbf{r}_{\text{rot}}^{\text{gt}}| \), \( |\hat{\mathbf{T}}-\mathbf{T}^{\text{gt}}| \), and \( |\hat{\mathbf{d}}_{\text{map}}-\mathbf{d}_{\text{map}}^{\text{gt}}| \), but it is not stated whether these are elementwise \(L_1\), summed \(L_1\), mean absolute error, or shorthand for a norm. Since these terms operate on quantities with very different dimensionalities and scales, the exact reduction matters.
   - In **Equation (7)**, the cycle-consistency term uses \(\mathbf{P}_{s}\in\mathbf{P}_{C_{O}}\) in the expectation, but the expression inside uses \(\mathbf{P}_{o}\). That is probably a typo, but in a paper centered on geometric mappings \(\Phi\) and \(\Psi\), inconsistent indexing is not a minor cosmetic issue.
   - The mappings \(\Phi\) and \(\Psi\) themselves are described conceptually as nearest-point correspondences, but the implementation details are omitted in the main paper. Are they hard nearest neighbors on Euclidean distance, normal-aware correspondences, soft assignments, or learned maps? Since \(\mathcal{L}_{cyc}\) is a key part of the refinement objective, this should be explicit.
   - In **Section 4.1**, the contact maps are decoded as binary maps \(\hat{\mathbf{C}}_O \in \{0,1\}^{N_O\times 1}\) and \(\hat{\mathbf{C}}_H \in \{0,1\}^{N_H\times 1}\), but the training loss in **Equation (3)** uses focal and dice losses, which usually act on probabilities or logits before thresholding. The thresholding rule at inference is not specified. Without this, the “binary contact map” language is underspecified.

6. **The diffusion formulation is described at a fairly high level, but important design choices are left vague.** On **Page 6**, the model is said to directly predict \(\hat{\mathbf{x}}_0\) with DDPM training, but the exact parameterization of \(\mathbf{x}_0\) is not sufficiently clear from the main paper. Does \(\mathbf{x}_0\) contain full MANO pose, shape, global rotation, and translation concatenated in raw units? The paper later motivates auxiliary losses precisely because of “disparate numerical ranges”, which suggests this representation is somewhat fragile. It would help to define the pose vector explicitly and explain normalization. Similarly, the text says local features are “adaptively selected” near contact areas, but the selection procedure around predicted contact maps is not mathematically defined in the main text. This matters because the claimed coarse-to-fine injection mechanism in **Equations (4) and (5)** is one of the methodological core ideas.

7. **The claims about semantic controllability are stronger than the evidence.** **Figure 8** and **Figure 9** are visually appealing, but these are cherry-picked demonstrations. The paper claims the model can interpret fine-grained directives, including force-related terms like “firmly” and “gently”, and on **Page 10** mentions a 22-25% larger average contact area for firm interactions. However, the paper does not report the sample size, confidence intervals, annotation protocol for identifying these prompts, or whether these adjectives are confounded with action categories and object types. It is plausible that the model is exploiting lexical correlations in the DSCs rather than learning a more general notion of force semantics.

8. **The baselines are post-processed with optimization, but the fairness of this adjustment is not fully convincing.** On **Page 8**, the authors say they augment both baseline methods with an optimization-based post-processing module to correct hand poses. That sounds fair in spirit, but the details are too sparse. Is the post-processing objective exactly the same as the proposed refinement objective? If yes, then part of the performance gap could come from upstream representation quality; if no, the comparison is difficult to interpret. This matters particularly for metrics like PD and PV in **Table 1**, which can be highly sensitive to the details of the post-processing.

9. **The presentation is generally readable, but several sections overclaim or compress too much technical detail.** A recurring pattern is that the paper states a reasonable intuition, then leaves out the specifics that would let a reader verify or reimplement the key step. Examples include the hand-part mask initialized from DSCs in **Section 4.1**, the adaptive feature selector implied around **Figure 4**, and the exact semantics of the VLM-assisted evaluation in **Section 5.1**. The paper is not unreadable, but it is written with the confidence of a fully specified method while still leaving a number of crucial mechanisms implicit.

10. **The qualitative evidence includes strong cases, but also reveals unresolved failure modes that somewhat undercut the “physically plausible” framing.** The appendix failure analysis is candid, which I appreciate, but the issue is already hinted at in the main paper. In **Figure 5**, some examples still show relatively generic grasp-like shapes even when the interaction should be more delicately specified. **Figure 6** is meant to show contact guidance improvement, but it also exposes how unstable the pre-refinement outputs are. This does not invalidate the method, but it suggests the task remains only partially solved and the paper should tone down some of the broad superiority language.

## Questions
1. **How exactly is the train/test split constructed at the level of videos, object instances, and action templates?** A response that clarifies whether frames or near-duplicate samples from the same original clip can appear across train and test would materially affect my confidence in the reported numbers.

2. **Can the authors provide a more rigorous description of the semantic evaluation protocol?** In particular, for the VLM score and perceptual score in **Table 1**, please specify the prompts, number of evaluated samples, whether raters were blind to the method identity, inter-rater agreement, and how scores were aggregated.

3. **Please clarify the exact implementation of the cycle-consistency mappings \(\Phi\) and \(\Psi\) in Equation (7).** Are these hard nearest-neighbor maps on the current surfaces, differentiable soft assignments, or something else? Also please fix the notation inconsistency between \(\mathbf{P}_s\) and \(\mathbf{P}_o\).

4. **What is the thresholding or decoding rule used to obtain binary contact maps from the CVAEs in Section 4.1?** Since Equation (3) suggests probabilistic supervision, the inference-time conversion to \(\{0,1\}\) contact labels should be specified.

5. **How much of the gain in Table 1 comes from the dataset versus the model?** If all methods are trained on WildO2, then the paper mainly shows TOUCH is better on this dataset. It would strengthen the paper if the authors could clarify how much the improvement stems from the proposed coarse-to-fine conditioning and refinement, rather than simply from access to richer annotations.

6. **Can the authors report stronger generalization tests in the main paper?** For example, splits by unseen object categories, unseen verbs, or unseen object-verb combinations would make the “free-form” claim more convincing than a random stratified split.

7. **For Equation (6), please specify the precise norms and reductions used.** If these are \(L_1\) losses, please write them as \(\|\cdot\|_1\) or an explicit mean/sum. If they are absolute values applied elementwise and then reduced, that reduction should be stated.

8. **How sensitive are the results to the quality of the DSC annotations?** Since the paper leans heavily on synthetic detailed captions, it would be useful to know whether noisy or partially incorrect DSCs degrade performance sharply, especially for non-grasping actions.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The dataset is constructed from internet videos, specifically filtered from Something-Something V2, and the paper does not discuss licensing, redistribution constraints, or whether releasing reconstructed 3D assets derived from those videos is fully compatible with the source dataset terms. This raises a legal/compliance question.

There is also a mild privacy and responsible-research concern. Although the task focuses on hands and objects rather than faces, the data are still derived from human-performed internet videos, and the paper does not state whether any additional safeguards were applied before creating and potentially releasing reconstructed 3D samples and captions.

Finally, the perceptual study uses 10 volunteers according to **Page 7** and the appendix, but the paper does not provide details on consent, compensation, or review procedures. This is not necessarily a serious violation, but it should be documented more clearly.

## Soundness Rating
2: fair. The paper is technically plausible and supported by coherent ablations and qualitative results, but the empirical validation and some mathematical specifications are not rigorous enough for a stronger soundness score.

## Presentation Rating
3: good. The paper is readable, well organized, and the figures are useful, especially Figures 2, 4, 5, and 8, but several important technical details and evaluation protocols are underspecified.

## Contribution Rating
3: good. The task formulation, dataset construction, and contact-guided text-conditioned generation framework together make a valuable contribution, even though the evidence does not fully support all of the stronger claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has real strengths, especially the task framing, dataset effort, and sensible contact-guided generation pipeline, and the qualitative results are stronger than many submissions in this area. However, I am held back by the limited baseline suite, under-specified evaluation of semantic controllability, concerns about split hardness and dataset fidelity, and several mathematical/implementation details that need clarification.

## Reviewer Confidence
4: confident. I am familiar with generative modeling and hand-object interaction literature, and I checked the main technical claims and equations carefully, though some implementation details are still too underspecified to verify fully.