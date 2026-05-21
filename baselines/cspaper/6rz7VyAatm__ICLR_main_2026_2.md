---
job_id: 7d330197-ecae-48c3-bd30-af06166567ba
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 6rz7VyAatm.pdf
paper: BADDet+: Robust Backdoor Attacks for Object Detection
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies robustness, backdoor attacks, and evaluation protocols for object detection models, which falls under machine learning safety and representation learning for vision.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it presents a technically coherent empirical study. While I have substantial concerns about the strength of the claims and some methodological choices, these do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper revisits backdoor attacks for object detection and argues that several prior evaluations are unreliable, especially due to metrics that can overcount success in region misclassification attacks and misuse mAP as a proxy for disappearance. The authors propose BadDet+, a training-time penalty added to the detector loss that suppresses original-class confidence on trigger-bearing objects, with the goal of unifying region misclassification attacks (RMA) and object disappearance attacks (ODA) under one mechanism. Experiments on COCO and MTSD, with additional transfer to a physical traffic sign dataset, suggest improved ODA performance and much lower retained-label rate for RMA compared to prior baselines.

## Strengths
The paper tackles a real and underexplored problem. Backdoor attacks on object detection are much less mature than their classification counterparts, and the paper makes a useful attempt to clean up evaluation practice rather than only proposing yet another attack variant.

A genuine strength is the paper’s critique of existing metrics and protocols. The introduction of TDR for RMA is sensible and, in my view, overdue. Table 2 is particularly effective here: BadDet and BadDet+ have similarly high ASR@50, but the TDR@50 gap is dramatic, for example on FCOS, 75.94 for BadDet versus 2.78 for BadDet+. This directly supports the authors’ claim that ASR alone can seriously overstate success because duplicate detections leave the original label intact. That is a useful conceptual contribution even independent of the proposed method.

The attack formulation is simple and broadly understandable. Equations (1) and (2) encode the core idea clearly, namely to penalize high confidence for the original class on predictions that overlap triggered objects. This is an intuitively reasonable intervention, and the softmax-compatible variant in Equation (2) is a practical addition that broadens applicability across detector families.

The empirical study is broader than many papers in this niche. The paper evaluates multiple architectures, two datasets, both RMA and ODA settings, and includes some physical-world validation. Table 3 is a strong point for the paper’s case on ODA: on MTSD/PTSD, BadDet+ is consistently stronger than UBA, UBA Box, and Morph across most models, especially on physical transfer where prior methods collapse badly.

The paper does a decent job illustrating why its critique matters. Figure 1 is helpful, especially panels (a), (b), and (c), which concretely show the failure modes discussed in Section 3, duplicate detections in RMA and phantom boxes in ODA. This makes the argument against overly optimistic prior evaluations more persuasive than if it were only stated abstractly.

The robustness-to-fine-tuning story is also moderately convincing for ODA. Figure 2 suggests that BadDet+ often remains effective after FT and FT-SAM, at least under the limited defenses considered. This helps support the claim that the attack is not merely a brittle artifact of one training run.

## Weaknesses
1. **The central novelty is narrower than the paper presents, and the positioning against prior robust physical-world OD backdoors is incomplete.**  
   The proposed method is essentially a penalty term that suppresses the original-class score on triggered regions, added on top of standard detector training, see Equations (1), (2), and the definition of the full loss on Page 5. That is a reasonable engineering idea, but the paper repeatedly frames it as a principled unified mechanism for RMA and ODA without sufficiently clarifying how far this is from existing attack-time objective shaping. More importantly, for a paper that emphasizes physical robustness and synthetic-to-physical transfer in the abstract and in Section 5, the related work discussion is thin on prior physically robust object-detection backdoors beyond Morph. This matters because the paper’s strongest practical claim is not merely better synthetic ASR, it is robustness under realistic conditions. If the literature review under-covers prior physically robust detection backdoors, the contribution can appear more isolated than it really is.

2. **The threat model shift is substantial, and the comparison to prior data-poisoning attacks is therefore not apples-to-apples.**  
   On Page 4, the authors explicitly assume the attacker can control or subvert the training process, not just poison the dataset. This is much stronger than standard outsourced-data or poisoned-pretraining settings used by several prior attack papers. The paper tries to justify this by saying data poisoning is unreliable, but that does not fully solve the comparability problem. If BadDet+ wins mainly because it uses a stronger attacker who can alter the loss, then the empirical superiority in Tables 1 to 4 is partly due to an advantaged threat model, not necessarily a better attack under the same assumptions. This matters scientifically because the paper often phrases conclusions as if prior attacks are simply weak, whereas a more precise reading is that prior attacks are weak under poisoning-only constraints and BadDet+ succeeds under training-procedure compromise.

3. **Key parts of the loss are underspecified relative to detector training pipelines, which weakens reproducibility and makes the empirical behavior harder to interpret.**  
   Equations (1) and (2) sum over all prediction-ground-truth pairs with IoU \(>\rho\) and \(m_i=1\), but the paper does not fully specify at the main-paper level which predictions are included before or after detector-specific matching, score filtering, NMS, or top-k selection. For one-stage dense detectors and query-based detectors, the raw prediction sets are very different. The exact set of penalized pairs can drastically affect gradient scale and optimization dynamics. Similarly, \(\tau\), \(\tau'\), and \(\rho\) are central hyperparameters, but their chosen values are not stated in the main text near Equations (1) and (2). This is not a cosmetic omission, because the penalty is explicitly threshold-centered. A reader cannot really tell whether the gains come from the barrier form, from specific threshold tuning, or from architecture-specific quirks.

4. **The theoretical section overclaims relative to its assumptions, and several statements read more like intuition wrapped in theorem language than genuinely established guarantees.**  
   The appendix repeatedly uses strong wording such as “sufficiency” and “guarantee the existence of a backdoor mapping” in Theorem 1 on Pages 20 to 22, but the assumptions are extremely restrictive: fixed matched pairs, linear classification head, convex loss, trigger features appearing only when \(m_i=1\), and clean and trigger features being uncorrelated in expectation. Those assumptions abstract away most of what makes modern detectors difficult, namely nonlinear feature adaptation, assignment dynamics, and localization-classification coupling. Proposition 3 is especially hand-wavy: it claims the attack gradient is “only active on the trigger portion” and concludes \(w^\star - w^{det} \in \mathrm{span}\{t_j(x)\}\), but this step is not rigorously justified from the stated decomposition \(h_j(x)=h_j^{clean}(x)+m_i t_j(x)\). In short, the theory is not wrong as local intuition, but the theorem-style presentation materially overstates what has been shown. Since the abstract also advertises the theory as explaining selective action in a trigger-specific subspace, this matters for credibility.

5. **The RMA story is mixed, not consistently favorable to the proposed method, yet the conclusion is phrased too confidently.**  
   On COCO, Table 2 supports the paper nicely. But on MTSD/PTSD, Table 4 is more complicated. For YOLOv5, BadDet actually outperforms BadDet+ on both ASR@50 and TDR@50 in several settings, and the paper itself says on Page 8 that “\(\lambda = 0\) is optimal for this architecture,” which is an awkward admission because \(\lambda=0\) removes the proposed penalty entirely. That means the core mechanism is not merely suboptimal there, it may be unnecessary or harmful. This should temper the claimed generality of the method. A framework that is supposed to unify and strengthen both settings across detectors should not have one architecture where its best setting is to turn itself off.

6. **The defense evaluation is too narrow to support broader robustness claims.**  
   Section 2.2 explicitly narrows the scope to FT and FT-SAM, and Page 10 repeats that the defense study is limited. That is a legitimate scope choice, but then the paper should be more restrained in statements about robustness to defenses. Figure 2 only evaluates a small family of fine-tuning-based defenses with tiny clean subsets. There is no systematic comparison to pruning, trigger synthesis based mitigation, architecture-specific OD defenses, or stronger test-time sanitization beyond appendix JPEG compression. As a result, the paper shows resistance to weak-to-moderate fine-tuning defenses, not robust resistance in any broad sense. For a security paper, this distinction matters a lot.

7. **Some empirical claims are stronger than what the tables actually show.**  
   For example, the COCO ODA discussion on Page 7 states that BadDet+ achieves consistently strong results “with a worst-case ASR@50 of 96.46,” but Table 1 lists 96.95, 98.46, and 97.60 for the three models, so even the numeric summary appears inconsistent. More broadly, the paper often emphasizes “without disproportionate degradation in clean-task mAP,” yet there are cases where BadDet+ still incurs nontrivial mAP drops relative to baseline, especially for DINO in Table 1 and across several MTSD settings in Tables 3 and 4. The claim is directionally fair, but the wording is polished a bit too hard.

8. **The evaluation protocol improves over prior work, but it still has blind spots.**  
   In Section 5.2, ASR for ODA is defined as the original class not being detected for each individually poisoned object. This is certainly better than poisoned-set mAP, but it still does not fully distinguish true disappearance from replacement by a wrong non-target class, localization drift, or suppression caused by neighboring detections in crowded scenes. Since the paper’s main critique of prior metrics is that they confound phenomena, it should hold itself to a similarly high standard. A more complete object-level outcome taxonomy would have strengthened the case.

9. **Figure 2 is informative, but it also exposes instability that the paper does not analyze enough.**  
   The figure shows wide spreads across runs after FT and FT-SAM for several settings, especially for RMA. This variance matters because the claim is about robustness of the implanted backdoor. If post-defense outcomes fluctuate strongly with the clean subset sampled, then the attack may be less reliably robust than the prose suggests. The paper interprets Figure 2 mainly in the attack’s favor, but a more critical discussion of variance, overlap between methods, and architecture dependence is needed.

10. **Figure 3 contains an apparent interpretation error in the RMA discussion.**  
   On Page 9, the authors say BadDet+ forms a stable cluster in the “top-right region” of the RMA plots while “sustaining high TDR@50 and mAP ratio across poisoning levels and achieving near-ideal behavior.” This seems backwards. For RMA, low TDR is desirable, as defined in Section 5.2 and emphasized elsewhere. If the paper indeed means top-right with high TDR, that contradicts its own objective; if it means low TDR, the text is incorrect. This may look minor, but it is exactly the type of metric confusion the paper criticizes in prior work, so it weakens trust in the care taken with interpretation.

11. **The paper’s strongest practical result is ODA, while the “unified” framing overstates success on RMA.**  
   In the conclusion and abstract, the framing suggests a broad unification of RMA and ODA with robust gains. In reality, the evidence is asymmetric. Tables 1 and 3 make a compelling case for ODA. Tables 2 and 4 make a more nuanced case for RMA, where the main gain is lower TDR, but the advantage over BadDet is not universal and becomes architecture-dependent. Calling this unified is technically correct at the loss-design level, but scientifically the paper feels more like “a strong ODA attack plus an improved evaluation lens for RMA” than a uniformly strong solution to both.

12. **Presentation is generally readable, but several notation and exposition choices are sloppier than they should be for a method paper.**  
   There are small but nontrivial issues scattered throughout: the Faster R-CNN naming is inconsistent across pages, the paper occasionally conflates confidence, logits, and decision boundaries without specifying whether scores are pre- or post-sigmoid/softmax, and some appendix statements use theorem/proposition structure while relying on informal assumptions. These are not fatal alone, but they accumulate and reduce confidence in the exactness of the paper’s technical positioning.

## Questions
1. The main paper should state explicitly how the set of penalized predictions in Equations (1) and (2) is constructed for each architecture. Are these raw predictions before assignment, matched positives after assignment, post-threshold predictions, or something else? This point is central for both reproducibility and understanding why the method helps more on some detectors than others.

2. Please provide the exact values of \(\rho\), \(\tau\), and \(\tau'\) used in the main experiments, and clarify whether they were tuned per architecture or fixed globally. If they are architecture-specific, that would materially affect how general the method is.

3. Can the authors clarify the apparent inconsistency in the poisoning-ratio discussion on Page 9, where “high TDR@50” is described as desirable for RMA? I suspect this is a wording mistake, but it should be corrected because TDR is a central metric contribution of the paper.

4. The theory should be reframed more carefully unless the authors can justify the stronger claims. In particular, what precise sense of “sufficiency” is intended in Theorem 1, given that matching is fixed, features are assumed decomposable and uncorrelated, and the classifier head is linear? A cleaner statement of scope would increase my confidence.

5. Since the threat model is stronger than prior poisoning-only attacks, could the authors add a more explicit discussion of what fraction of the observed gains comes from the new loss manipulation itself versus simply moving to a more powerful attacker? Even a small controlled comparison under matched threat assumptions would help.

6. For the physical-world validation, can the authors clarify whether all hyperparameters were selected without reference to PTSD results? The paper implies yes, but it would be good to state this unambiguously.

7. Table 4 suggests the method underperforms BadDet on YOLO RMA, and the text even notes that \(\lambda=0\) is optimal. What exactly is the intended takeaway for the “unified framework” claim in light of this? Is the method meant to be architecture-adaptive, or is YOLO an exception that breaks the generality claim?

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper develops stronger backdoor attack methodology for object detection, including physical-world validation on traffic sign detection settings, which can plausibly be misused in safety-critical applications such as autonomous driving or surveillance. The concern is not that the paper is unethical per se, but that it provides a clearer recipe for implanting and evaluating more robust backdoors in detectors. The paper does discuss defensive motivation, which is helpful, but the dual-use risk is real.

## Soundness Rating
2: fair. The empirical study is substantial and several results are convincing, especially for ODA and the critique of prior metrics, but some claims are overstated relative to the threat model, the theory is much weaker than its theorem-style framing suggests, and important methodological details around the penalty application are underspecified.

## Presentation Rating
3: good. The paper is generally readable and organized, with useful figures and tables, but there are important exposition issues, including ambiguous implementation details, some overconfident framing, and at least one metric-interpretation mistake in the discussion of Figure 3.

## Contribution Rating
2: fair. The paper contributes a useful evaluation critique and a practically effective ODA attack, but the core method is somewhat incremental, the “unified” framing is stronger than the mixed RMA evidence supports, and the stronger threat model complicates direct comparison to prior work.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My current view is negative but not dismissive. The paper has real value in exposing flaws in prior OD backdoor evaluations, and the ODA results are strong enough that I would expect this work to be discussed. However, for ICLR main track I think the paper overclaims relative to its actual novelty, theoretical support, and generality. The stronger attacker assumption, mixed RMA story, and underspecified loss mechanics push me below the bar.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I checked the main technical formulation, read the quantitative evidence carefully, and the paper is close enough to my area that I am unlikely to have missed the central issues.