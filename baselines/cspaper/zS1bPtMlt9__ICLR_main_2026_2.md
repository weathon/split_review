---
job_id: 62d36647-3a44-4987-ad84-443f929f3a02
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: zS1bPtMlt9.pdf
paper: RePL: Pseudo-Label Refinement for Semi-Supervised LiDAR Semantic Segmentation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, specifically semi-supervised representation learning for LiDAR semantic segmentation, with both methodological and empirical contributions in 3D vision.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, experiments/results, and conclusion. While I have several substantive concerns about novelty, methodological specification, and presentation, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes RePL, a semi-supervised LiDAR semantic segmentation framework that refines pseudo-labels before using them to train the student model. The method combines a teacher-student EMA setup with an agreement-and-confidence-based unreliable voxel detector, followed by masked reconstruction by a refiner network, and includes a short theoretical analysis of when refinement should improve over direct teacher pseudo-labels. Experiments on nuScenes-lidarseg and SemanticKITTI show improved performance over several prior semi-supervised baselines, together with ablations on the proposed losses, masking strategy, and error-mask quality.

## Strengths
The main practical strength is that the paper attacks a real weakness of pseudo-label-based SSL, namely that most methods only filter or reweight noisy pseudo-labels after generation, whereas this work tries to directly repair them. That framing is sensible, and for LiDAR semantic segmentation it is a reasonable problem to study.

The empirical results are fairly strong overall. In **Table 1** on **Page 8**, RePL is consistently competitive and often best across label ratios on both datasets. On nuScenes-lidarseg, the gains over the listed Cylinder3D-based methods are nontrivial, especially at 10%, 20%, and 50% label ratios. Even on SemanticKITTI, where the margins are tighter and RePL is not uniformly best at every label ratio, the average is still the highest among the listed methods. This gives the method practical credibility.

The ablations are more informative than what many papers in this area provide. **Tables 2 and 3** on **Page 8** do suggest that the refiner-side losses and the student-side semi-supervised objectives each matter, and **Table 5** on **Page 8** indicates that the random masking strategy is not just decorative. I also appreciated that **Table 4** studies the sensitivity to error-mask quality; that table makes an important point, namely that the method’s ceiling is highly coupled to error detection quality, and that the current heuristic still leaves headroom relative to an oracle mask.

The paper includes useful qualitative evidence. **Figure 3** on **Page 9** is effective in showing the intended behavior of the method: the refined pseudo-labels visibly reduce some localized errors present in the initial pseudo-labels. Likewise, **Figure 4** on **Page 10** is a good inclusion because it acknowledges over-correction failures rather than only cherry-picking wins. **Figure 1** on **Page 2** also gives a reasonably intuitive overview of how the teacher, student, and refiner interact.

The theoretical section is modest, but at least the authors attempt to formalize the improvement condition rather than simply claiming that refinement “should help.” Proposition 2 is simple, but it gives a concrete tradeoff between correction and error introduction.

## Weaknesses
1. **The conceptual novelty is limited, and the paper does not do enough to separate a genuinely new idea from a bundle of familiar ingredients.**  
   The method combines several standard components: EMA teacher-student SSL, confidence-based masking, agreement-based selection, masked-token reconstruction, LaserMix-style mixed-scene training, and negative learning. Each of these ingredients is individually known, and the paper’s core claim is essentially that they work well together for pseudo-label refinement in LiDAR segmentation. That can still be publishable, but then the paper needs especially strong evidence that the whole is more than the sum of parts. I do not think the paper fully clears that bar.  
   In particular, **Figure 1** on **Page 2** presents the pipeline as a coherent new framework, but the figure also makes clear how heavily the method leans on existing building blocks. The paper would be stronger if it isolated what is uniquely enabled by the reconstruction-based refiner beyond “another auxiliary network plus better training recipe.” Right now, the contribution reads as creative integration more than a distinctly new algorithmic principle.

2. **The empirical attribution is incomplete, because the paper does not cleanly disentangle gains from pseudo-label refinement versus gains from additional capacity and extra training machinery.**  
   This is the biggest practical issue for me. RePL adds a dedicated refiner network, additional losses, random masking, and mixed-scene training. So when **Table 1** on **Page 8** shows improvements, it is not obvious how much comes from true pseudo-label correction, how much comes from simply adding another powerful model and extra supervision paths, and how much comes from training tricks inherited from prior SSL pipelines.  
   **Tables 2 and 3** help somewhat, but they are not enough. For example, there is no comparison to a same-parameter or same-compute control in which the extra capacity is spent elsewhere, or a control where the refiner sees teacher predictions without the error mask/reconstruction logic. Without such controls, the paper’s central narrative, namely that “refinement” is the cause of the gain, remains somewhat under-supported.  
   This matters scientifically because otherwise the contribution is hard to interpret: are we learning that pseudo-label refinement is the key, or merely that adding an auxiliary denoising head to a strong SSL pipeline helps?

3. **Several core loss definitions and notational choices are underspecified or inconsistent, which makes the method harder to verify than it should be.**  
   There are multiple notation problems in **Sections 3.3 and 3.4**. On **Page 5**, the teacher prediction for mixed scenes is written as \(Q_m = f^{r}(X_m)\), which seems inconsistent with the earlier teacher notation \(f^{\tau}\). On **Page 6**, the student objective is described as \(\mathcal{L}_{\text{ssup}}+\mathcal{L}_{\text{sunl}}+\mathcal{L}_{\text{smix}}\), but **Equation (7)** defines \(\mathcal{L}_{\text{saml}}\), not \(\mathcal{L}_{\text{sunl}}\). This may sound minor, but in a method with many interacting losses, these inconsistencies make it harder to know exactly what is optimized.  
   More importantly, **Equation (7)** uses
   \[
   \tfrac{1}{2}\left(\mathcal{L}_{\text{ce}}(P_j,\hat{Y}_j)+\mathcal{L}_{\text{ce}}(\hat{Y}_j,P_j)\right),
   \]
   while \(\mathcal{L}_{\text{ce}}\) was defined in **Equation (1)** for predictions \(P_i\) and one-hot labels \(Y_i\). Here \(\hat{Y}_j\) is called a “refined pseudo-label,” but from the text in **Section 3.4** it is not clear whether \(\hat{Y}_j\) is a hard one-hot pseudo-label, a soft class distribution, or something hybrid after combining teacher outputs and refiner outputs. If \(\hat{Y}_j\) is hard one-hot, then \(\mathcal{L}_{\text{ce}}(\hat{Y}_j,P_j)\) is not well-defined as written because the second argument in Eq. (1) is assumed to be the target. If \(\hat{Y}_j\) is soft, then the notation and earlier one-hot assumptions should be revised explicitly.  
   This is not a cosmetic complaint. The exact form of the target distribution matters for stability, reproducibility, and the claimed robustness of the symmetric cross-entropy term.

4. **The description of the refinement target itself is ambiguous at a critical point.**  
   On **Page 5**, the paper says the refined pseudo-label \(\hat{Y}_j\) is generated voxel-wise by keeping teacher predictions on reliable voxels and replacing unreliable ones with the refiner’s output. But the notation then immediately reuses \(\hat{Q}_j\) for both the masked input to the refiner and the refiner output:
   \[
   \hat{Q}_j=(\mathbf{1}-M_j)\odot Q_j+M_j\odot T
   \]
   and then again
   \[
   \hat{Q}_j=g(X_j,\hat{Q}_j).
   \]
   That is mathematically sloppy. The pre-refinement masked tensor and the post-refinement prediction should be distinct objects. Also, the transition from these tensors to \(\hat{Y}_j\) is never written as an explicit equation. Is there an \(\arg\max\) over classes? Are probabilities preserved? Are reliable voxels copied as teacher probabilities or as hard pseudo-labels?  
   For a paper centered on pseudo-label quality, this missing specification is a real weakness.

5. **The theoretical analysis is correct at a high level, but much weaker than the paper’s framing suggests, and some wording oversells what is actually shown.**  
   Proposition 1 on **Page 6** is basically the observation that conditioning on more information cannot increase conditional entropy:
   \[
   H(Y\mid X,T) \le H(Y\mid X).
   \]
   This is true, but it does not say that the practical refinement problem with a finite-capacity model and a difficult training signal is easier in the optimization or generalization sense. The appendix makes this contingent on “comparable complexity with similar VC-dimensions,” which is a strong and abstract assumption. So the proposition is fine as intuition, but it should not be marketed as much more than that.  
   Proposition 2 is also mathematically straightforward. From the derivation in **Appendix A.2**, the improvement condition follows from
   \[
   \Delta_j = \rho_j\left(\pi_j q_j - (1-\pi_j) r_j\right),
   \]
   leading to
   \[
   \zeta_j := \pi_j - \frac{r_j}{q_j+r_j} > 0.
   \]
   This is a clean accounting identity for improvement on the masked region, not a model-specific theorem about why RePL should learn favorable \(q_j,r_j\). The paper says the condition is “mild and easily satisfied by RePL,” but this mostly reduces to the observed empirical precision \(\pi_j\) of the error mask. In other words, the theory is descriptive rather than predictive. That is acceptable, but the framing should be more modest.

6. **The comparison set is not fully convincing as evidence of state of the art for the broader problem.**  
   The paper compares to several recent methods in **Table 1**, which is good, but the positioning is still somewhat selective. Some listed methods use external pretraining or different backbones, some do not, and the text oscillates between “latest methods” and “state of the art” without always making the evaluation basis precise. For example, comparisons against methods with distinct auxiliary information or substantially different training setups are not always apples-to-apples.  
   This matters because the headline claim in the abstract and conclusion is quite strong. If the claim is “state of the art among Cylinder3D-based SSL methods without external pretraining on these settings,” say that clearly. The present wording is broader than the evidence comfortably supports.

7. **The ablations still leave important unanswered questions about the method’s design choices.**  
   **Table 6** on **Page 9** only checks three values of \(\kappa\), and **Table 5** only compares random masking on versus off. Given that the unreliable voxel detector is central to the method, I wanted to see more about the teacher-student agreement rule itself: teacher-only confidence, student-only confidence, disagreement-only, fixed threshold versus percentile threshold, or class-wise thresholds versus scene-wise thresholds.  
   Likewise, **Table 4** on **Page 8** is interesting, but it evaluates different mask strategies “at inference time.” That does not fully answer how training depends on the mask quality, which is arguably more important. If the oracle mask gives 67.3 mIoU versus 60.0 for the current heuristic, the method appears highly bottlenecked by error localization, yet this component receives relatively light experimental analysis.

8. **The computational cost discussion is too weak for a method that adds another full network.**  
   **Table 7** on **Page 9** reports latency and memory for “Baseline” versus “Baseline + Refiner,” but only for a single batch, and only relative to the supervised-only baseline. That is not the relevant comparison for semi-supervised use, where the method should be compared to strong SSL baselines such as LaserMix or IT2 under the same inference and training conditions. Also, the training-time overhead is not reported, even though the paper jointly trains the student and refiner and computes several additional losses.  
   Since the refiner uses Cylinder3D as stated in **Section 4.1** on **Page 7**, this is not a negligible addition. For deployment-oriented 3D perception, a second segmentation-scale network is a meaningful systems cost, and the current analysis understates that.

9. **Presentation quality is uneven, with enough errors to undermine confidence in the paper’s polish.**  
   There are many typos and naming inconsistencies in the tables and references: e.g., “Feng” vs. Fong, “Bohley” vs. Behley, “Keng” vs. Kong, “Yavranen & Yelpola” vs. Tarvainen & Valpola, “AIScen” missing the final “e,” “FrustrumMix” spelling, and several formatting glitches. Some section text also refers to images rather than scenes, for example on **Page 2**: “prediction errors for unlabeled images,” although the task is LiDAR scenes.  
   None of these alone is fatal, but together they create friction and make the paper feel less carefully checked than it should be for ICLR.

10. **The qualitative analysis is useful, but it also reveals a limitation the paper does not explore deeply enough.**  
   **Figure 3** on **Page 9** shows visible improvements, but the gains seem concentrated in certain localized regions. **Figure 4** on **Page 10** then shows over-correction failures in purple boxes, which is good practice, but the paper stops short of analyzing when over-correction happens. Is it class-dependent, distance-dependent, or linked to the confidence-threshold heuristic? Since the method explicitly edits teacher predictions, a more systematic breakdown of failure modes would have strengthened the paper considerably.  
   Similarly, **Figure 5** on **Page 10** is cited as showing pseudo-label quality improvement over training, but the quantitative axes and exact metric are not described in enough detail in the main text to make that trend highly informative. The story is plausible, but the figure is used more narratively than analytically.

## Questions
1. In **Equation (7)**, what is the exact representation of the refined pseudo-label \(\hat{Y}_j\)? Is it a hard one-hot label map, a soft probability distribution, or a hybrid object created by mixing teacher probabilities and refiner probabilities? Please define it explicitly and explain how \(\mathcal{L}_{\text{ce}}(\hat{Y}_j,P_j)\) should be interpreted under your definition.

2. Please clarify the notation around the masked input to the refiner and the refiner output in **Section 3.4** on **Page 5**. Right now \(\hat{Q}_j\) is used for two different tensors. A precise equation for the final refined label construction would improve confidence in the method.

3. Can the authors provide a cleaner attribution study for the gains? For example, how does RePL compare against a parameter-matched auxiliary head or denoiser that does not use agreement-based masking and masked reconstruction? This would help establish whether “refinement” itself is the key factor.

4. Since **Table 4** suggests a large gap between the current heuristic mask and an oracle mask, can the authors provide more analysis of the mask precision/recall or class-wise behavior of the error detector? This seems central to the paper’s actual bottleneck.

5. The theoretical analysis would be more convincing if connected more directly to the implementation. Can the authors report empirical estimates of \(q\), \(r\), and \(\pi\) not only as the final \(\zeta\), but separately, and perhaps over training? That would make **Figure 2** and Proposition 2 more informative.

6. Could the authors report training-time overhead and compare inference cost against strong SSL baselines rather than only the supervised baseline in **Table 7**? For a method that adds a second Cylinder3D-scale model, this is important for practical adoption.

7. In **Table 1**, can the authors be more explicit about which comparisons are backbone-matched and which involve external representation learning or different training resources? This would make the “state-of-the-art” claim more precise and easier to assess.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The paper studies semi-supervised LiDAR semantic segmentation on standard public datasets and does not raise immediate fairness, privacy, safety, or responsible-release concerns beyond those typical for autonomous driving perception research.

## Soundness Rating
2: fair. The empirical results are promising and the main idea is plausible, but several objective definitions and pieces of notation are underspecified, and the evidence does not fully isolate the cause of the reported gains.

## Presentation Rating
2: fair. The paper is readable overall and the high-level idea is understandable, but there are enough notation issues, typos, and inconsistencies across equations/tables to materially hurt clarity.

## Contribution Rating
2: fair. The paper has practical value and good benchmark results, but the conceptual advance over existing teacher-student, masking, and reconstruction-based SSL components feels incremental, and the paper does not fully demonstrate that the proposed refinement mechanism is the decisive new ingredient.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper addresses a meaningful problem and shows strong empirical performance, especially on nuScenes, but I am not yet convinced that the contribution is sufficiently distinct and cleanly validated for ICLR main track. The combination is competent and useful, yet the novelty is incremental, the method description has avoidable ambiguities, and the evidence for the central refinement claim is not as airtight as the headline results suggest.

## Reviewer Confidence
4: confident. I am confident in this assessment and familiar with semi-supervised learning and 3D semantic segmentation, though some implementation details are not fully recoverable from the current presentation.