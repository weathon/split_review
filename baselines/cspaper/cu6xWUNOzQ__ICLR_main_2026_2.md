---
job_id: 2d96f5d7-863d-49a3-bc59-aff459729bcf
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cu6xWUNOzQ.pdf
paper: Aligning the Brain With Language Models Through a Nonlinear and Multimodal Approach
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as an application to neuroscience and cognitive science, centered on representation learning for language and audio models and their alignment with brain responses.

## Minimum Quality
Pass ✅. The submission contains the core components needed for scientific review, including Abstract, Introduction, Method, quantitative experiments, results analysis, and Discussion/Conclusion; while there is no standalone “Related Work” section, prior work is substantively discussed throughout the Introduction and Results. I do not see an immediate desk-reject-level fatal flaw, although there are several important methodological and interpretational concerns that affect the score.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to reviewers, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies voxelwise fMRI encoding of naturalistic speech using multimodal features from LLaMA and Whisper, paired with nonlinear prediction heads. The main empirical claim is that a simple PCA plus one-hidden-layer MLP, especially in the multimodal setting, improves over standard linear unimodal baselines and over a prior stacked-regression multimodal approach on the LeBel et al. dataset. The paper also introduces a RED-based spatiotemporal clustering analysis and uses variance partitioning and ROI analyses to argue for distributed multimodal processing across cortex.

## Strengths
The empirical finding in **Table 1 (Page 4)** is interesting and potentially important for the brain-encoding community. The multimodal MLP with PCA achieves the best overall performance, and the gains over both the text-only linear baseline and the multimodal linear alternatives are not tiny by the standards of this literature. In particular, the comparison among **Linear**, **MLLinear**, **DIMLP**, and **MLP** is a sensible design for partially disentangling the effect of dimensionality reduction, within-modality nonlinearity, and cross-modal fusion.

I also appreciate that the paper does not stop at a single headline model-vs-baseline comparison. The authors provide several analyses aimed at mechanism rather than only benchmark chasing: layer sweeps in **Figure 16 (Page 35)**, multimodal delta maps in **Figure 2 (Page 6)**, and variance partitioning visualizations in **Figure 3 (Page 7)**. Even if I am not fully convinced by all of the downstream interpretations, the paper at least attempts to connect the predictive gains to brain-wide organization rather than merely reporting one table.

The comparison to prior multimodal stacked regression in **Table 4 (Page 22)** is useful. The paper makes a concrete case that direct feature fusion followed by nonlinear mapping may be more effective than weighted averaging of unimodal predictions. That is a practical lesson the field can use, even if one remains skeptical about the stronger neuroscientific claims.

The visual evidence is reasonably aligned with the quantitative story. For example, **Figure 2 (Page 6)** shows that the multimodal MLP tends to produce broader positive \(\Delta CC_{\mathrm{norm}}\) patterns than the multimodal linear model, especially outside classic auditory cortex. This figure supports the narrower claim that multimodality plus nonlinearity improves prediction in a spatially distributed way. Likewise, **Figure 1 (Page 5)** is an effective summary figure for the RED analysis: the RED-derived dendrogram appears more structured than raw functional connectivity, and the paper at least provides a concrete quantitative criterion, modularity \(Q\), rather than relying only on eyeballing clusters.

The paper is also fairly ambitious in scope. It combines model comparisons, voxelwise maps, ROI summaries, layer analyses, clustering, and variance partitioning. Even where I think the interpretation gets ahead of the evidence, the experimental coverage is broader than many application papers.

## Weaknesses
1. **The main methodological contribution is fairly incremental, and the paper overstates the degree of innovation.**  
   At the core, the advocated model is a fairly standard pipeline: pre-extracted LLaMA and Whisper features, temporal lag concatenation, PCA on brain responses, and a shallow MLP readout (**Sections 2.2 to 2.4, Pages 3 to 4**). The paper repeatedly frames this as a major shift for the field, but what is actually introduced is not a new representation learning method, not a new training objective, and not a new multimodal architecture in the machine learning sense. It is mostly a careful application and ablation of standard components to a neuroscience encoding setting. That can still be publishable, but the contribution should be positioned more honestly as a strong empirical study rather than as a methodologically deep advance.

2. **Several key comparisons are not apples-to-apples, especially where the paper uses PCA for some models and full-voxel prediction for others. This makes attribution of gains murkier than the text suggests.**  
   The central table, **Table 1 (Page 4)**, mixes models trained in different output spaces: some use `response = PCA`, others use `response = all voxels`. This matters a lot because the paper itself argues that full-voxel mapping is computationally difficult and prone to overfitting, while PCA reduces redundancy. For example, the baseline semantic linear model is reported as `Linear, all voxels`, whereas several stronger models are `MLP, PCA`. The paper tries to address this using MLLinear and PCA-linear controls, but the table still interleaves architectural differences and response-space differences in a way that makes the headline “nonlinearity is the key driver” less clean than claimed in **Section 3.1.1 (Page 5)**. If the core scientific claim is about nonlinearity, the fairest primary comparison should hold the response representation fixed and compare linear vs nonlinear under the same PCA regime, then separately discuss the effect of PCA. Right now the strongest result combines multiple changes.

3. **The statistical testing is weakly justified because voxels are treated as repeated independent measurements, which is not credible given strong spatial correlation in fMRI data.**  
   In **Appendix C (Page 18)**, the paper explicitly states that SEM is computed across voxels and pairwise significance tests are also performed across voxelwise score differences. This is a classic pseudo-replication problem. Voxels are not independent samples, particularly within neighboring cortical regions and after shared preprocessing. Reporting tiny SEMs and huge t-statistics based on tens of thousands of correlated voxels can dramatically overstate certainty. The paper even notes that across-subject variability is not reported because there are only three subjects, but then leans heavily on voxelwise statistics instead. This matters because many conclusions, including the claimed robustness of model superiority, are presented with a level of confidence that is not warranted by \(n=3\) subjects. At minimum, the paper should present subject-level effect sizes and uncertainty more centrally, and be much more cautious about inferential language.

4. **The mathematical definition and use of \(CC_{\text{norm}}\) is under-motivated and somewhat ad hoc in a way that could affect rankings.**  
   In **Section 2.5 (Page 4)**, the authors define normalized correlation by dividing \(\mathrm{CC}_{\mathrm{abs}}\) by \(\mathrm{CC}_{\max}\), then note that low-noise-ceiling voxels can yield \(\mathrm{CC}_{\mathrm{norm}} > 1\), and “to mitigate this, voxels with \(\mathrm{CC}_{\max} < 0.25\) were regularized to 0.25”. This thresholding is consequential, but it is not justified. Why \(0.25\)? How sensitive are the rankings in **Table 1** and **Table 3** to this floor? The statement “random noise can occasionally produce \(\mathrm{CC}_{\mathrm{abs}} < \mathrm{CC}_{\max}\), resulting in \(\mathrm{CC}_{\mathrm{norm}} > 1\)” is also confusing as written, because \(\mathrm{CC}_{\mathrm{norm}} > 1\) would arise from \(\mathrm{CC}_{\mathrm{abs}} > \mathrm{CC}_{\max}\), not \(<\). This may be a typo, but for a central evaluation metric, imprecision here is not a small issue. The paper needs a cleaner definition, an explanation of the regularization, and preferably a sensitivity analysis.

5. **The RED analysis is interesting but not yet validated enough to support the strong claims made from it.**  
   The paper defines  
   \[
   \mathrm{RED}(v,t) = |f_1(v,t) - y(v,t)| - |f_2(v,t) - y(v,t)|
   \]
   in **Section 2.5 (Page 4)** and elaborates in **Appendix J.4 (Pages 39 to 40)**. But several issues remain. First, RED is based on absolute error differences over time, then ROI-averaged and correlated; this pipeline introduces multiple transformations, each of which can alter structure in hard-to-interpret ways. Second, the clustering result in **Figure 1 (Page 5)** ultimately hinges on small modularity differences, \(Q=0.155\) vs \(0.145\) for nonlinear vs linear. The paper presents this as evidence of “superior functional clustering”, but no statistical test or robustness analysis is shown for the difference in modularity. Third, the conclusion that the dendrogram “reveals” canonical functional organization feels too qualitative. It is easy to tell a plausible story after looking at a dendrogram. If this is meant to be a real methodological contribution, it needs stronger validation, for example stability across subjects, sensitivity to ROI definitions, or comparison to null reorderings.

6. **The variance partitioning analysis is presented as if it supports strong claims about multimodal integration, but the decomposition is not described rigorously enough, especially for nonlinear models with correlated features.**  
   The discussion in **Section 3.3.1 (Pages 6 to 7)** and **Appendix M (Pages 51 to 63)** repeatedly interprets “joint”, “unique semantic”, and “unique audio” variance as if these are fairly clean functional quantities. However, with highly correlated learned features from LLaMA and Whisper, and with nonlinear encoders, variance partitioning is notoriously delicate. The paper does not provide a clear formal decomposition in the main text. Is the shared variance computed by inclusion-exclusion on prediction scores, by partial regression, or some other procedure? Are negative partitions clipped? How stable are the partitions when the models are only approximately optimized? Without that, statements such as “joint audio-semantic features dominated cortical representations” in **Figure 3 (Page 7)** should be treated more cautiously. The figure is visually compelling, but it may be telling us as much about feature collinearity and score decomposition conventions as about cortical computation.

7. **The paper repeatedly makes neuroscientific theory claims that outrun what the encoding results can support.**  
   The title, abstract, and discussion strongly connect the findings to the Motor Theory of Speech Perception, convergence-divergence zones, embodied semantics, and the dorsal stream account. But improved predictive performance from multimodal model features does not by itself establish that the brain uses those theories’ proposed computations. For example, the ROI findings in **Figure 2e (Page 6)** and the dominant-partition visualizations in **Figure 3 (Page 7)** are compatible with many explanations, including residual low-level correlations, narrative structure, shared temporal autocorrelation, or generic contextual information. To the authors’ credit, they briefly acknowledge alternative explanations in **Page 8**, especially for motor and somatosensory areas, but elsewhere the wording is much stronger than the evidence allows. This matters because one of the paper’s central selling points is not merely better prediction, but claimed support for specific neurolinguistic theories. Right now that part reads more like suggestive interpretation than demonstrated inference.

8. **The experimental scope is narrow, which limits confidence in generality.**  
   The entire empirical case rests on one dataset with only three subjects (**Section 2.1, Page 2**). That is common in this area, so it is not automatically disqualifying, but then the paper should avoid broad claims such as “nonlinear multimodal encoding is feasible for naturalistic speech” in a general sense. There is no cross-dataset validation, no transfer to another speech fMRI corpus, and no evidence that the selected architecture is robust beyond this exact setting. The paper does include many internal comparisons, but external validity remains thin.

9. **Some methodological details that affect fairness and reproducibility are underspecified or inconsistent between model classes.**  
   Ridge regression uses voxel-specific alphas with bootstrap validation, while neural models use a different early-stopping and Optuna tuning pipeline (**Appendix B.5, Pages 17 to 18**). That is not inherently unfair, but it complicates the claim that differences are due to nonlinearity alone. More importantly, details are missing from the main paper on how hyperparameters were selected for each condition, whether the same validation splits were used across all models, and whether layer selection was done per subject or globally. Since the gains are modest in absolute terms, these evaluation choices matter. The paper should spell them out in the main text, not only in the appendix.

10. **There are clarity and exposition issues in both the writing and notation.**  
   Some of these are small individually, but they add up. Examples: the sentence in **Section 2.5 (Page 4)** about \(\mathrm{CC}_{\mathrm{norm}} > 1\) appears directionally wrong; **Appendix B.3 (Page 17)** says \(N_{\mathrm{TR}}\) is “the number of tokens (or number of words for language models)” when it should refer to fMRI time points; the paper alternates between “semantic” and “text” labels across tables; and there are multiple grammatical issues throughout. The reference list also contains formatting problems and some apparent citation errors. The paper is readable overall, but not polished to the standard of a strong ICLR main-track submission.

11. **The evidence that cross-modal nonlinear interaction is the main driver is suggestive, but not fully nailed down.**  
   The authors use DIMLP as a restricted-fusion control in **Section 3.2.1 (Page 6)**, which is a good idea. However, the gain from DIMLP to full MLP in **Table 1 (Page 4)** is quite small in absolute terms, \(4.18\%\rightarrow 4.29\%\) in average \(r^2\), and \(32.59\%\rightarrow 34.32\%\) in \(CC_{\mathrm{norm}}\). The relative framing makes it sound larger. Given the weak inferential setup across voxels, I am not convinced the paper has established that nonlinear cross-modal interactions, specifically, are the dominant source of benefit. The current evidence supports “some benefit beyond purely linear fusion,” but the stronger mechanistic claim should be softened.

12. **The paper sometimes leans too hard on parameter-count comparisons that are not scientifically central.**  
   Several places, including **Table 1 (Page 4)** and **Discussion (Page 9)**, emphasize that the MLP uses far fewer parameters than the linear all-voxel baseline. But a ridge regression mapping from high-dimensional features to 80k to 90k voxels will obviously have many output weights. That count does not by itself make the comparison more meaningful, because the inductive biases and output spaces differ. This argument feels a bit like rhetorical garnish rather than a substantive contribution.

## Questions
1. The most important clarification I need is about evaluation fairness in **Table 1 (Page 4)**. Could the authors provide a cleaner matched comparison where the response representation is fixed, ideally PCA for all methods and separately all-voxels for all methods where tractable, so that the effect of nonlinearity is not mixed with the effect of response-space compression?

2. Please clarify the exact computation of variance partitioning for the nonlinear models. What is the formal definition of the unique semantic, unique audio, and joint components? Are these based on \(R^2\), on \(CC_{\mathrm{norm}}\), or on another score? How are negative components handled? A concise equation-level description in the main paper would substantially increase confidence.

3. Why is the \(CC_{\max}\) floor set to \(0.25\) in **Section 2.5 (Page 4)**? Please provide either a principled justification or a sensitivity analysis showing that the rankings in **Tables 1 and 3** are stable under other reasonable thresholds or under masking low-ceiling voxels entirely.

4. For the RED clustering in **Figure 1 (Page 5)**, how stable is the modularity improvement \(0.145 \rightarrow 0.155\) across subjects, ROI sets, and clustering choices? If the authors can show bootstrap stability or significance of the modularity difference, I would view this analysis more favorably.

5. The paper relies heavily on voxelwise statistics. Can the authors provide subject-level statistical summaries, for example paired subject-level comparisons of model scores across ROIs or stories, to reduce dependence on voxel pseudo-replication?

6. In **Table 4 (Page 22)**, the comparison to stacked regression is potentially important. Could the authors clarify exactly which parts of the protocol were inherited from Antonello et al. and which were reimplemented or corrected by the present paper? Since this table underpins the “state of the art” comparison, procedural clarity matters.

7. The interpretation sections, especially **Sections 3.3.1 and 3.3.2 (Pages 6 to 9)**, would be more convincing if phrased more cautiously. Can the authors distinguish more explicitly between what is directly shown by the encoding analysis and what remains speculative theory alignment?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work uses a public fMRI dataset and pre-trained models, and the paper does not describe deployment in a way that raises immediate fairness, privacy, or safety issues beyond standard concerns already associated with public neuroimaging data and foundation models.

## Soundness Rating
2: fair. The experiments are substantial and the main empirical trend is plausible, but several methodological choices, especially voxelwise statistical treatment, metric handling, and interpretational overreach, weaken confidence in the strength of the central claims.

## Presentation Rating
2: fair. The paper is readable and includes useful tables and figures, but the exposition is uneven, some key mathematical definitions are under-specified or confusing, and several important claims are phrased more strongly than the evidence supports.

## Contribution Rating
2: fair. There is a useful empirical message here, namely that simple nonlinear multimodal fusion can improve speech fMRI encoding, but the methodological novelty is limited and the broader scientific conclusions are overstated relative to what the results firmly establish.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a credible and interesting empirical result, and I can imagine it being useful to the community. However, the combination of incremental methodology, questionable inferential treatment across voxels, under-specified analysis details, and overextended neuroscientific interpretation keeps it below the bar for me in its current form.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant modeling and brain-encoding context, though some appendix-level implementation details would still benefit from author clarification.