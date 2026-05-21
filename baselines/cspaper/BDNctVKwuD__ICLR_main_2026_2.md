---
job_id: 25caa5a0-41ad-47cc-a4d8-236a0000380b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: BDNctVKwuD.pdf
paper: Improving Feature Alignment in ConvNets Using ContrastiveCAMs and Core-Focused Cross-Entropy
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on interpretability of learned visual representations, CAM-based explanation methods, and training objectives for feature alignment in convolutional networks.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, methodological sections, experiments/results, and Discussion. While I have substantial concerns about several technical claims, experimental choices, and clarity issues, these are review-stage weaknesses rather than grounds for desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions targeting automated reviewers, or suspicious embedded text in the provided manuscript content or figures.

# Expected Review Outcome:
## Summary
This paper argues that HiResCAM explanations for softmax-based classifiers are non-unique because adding a class-independent spatial shift to all class maps leaves the softmax probabilities unchanged. To address this, the paper proposes ContrastiveCAMs, defined via pairwise differences between class CAMs, and then builds a training loss, Core-Focused Cross-Entropy (CFCE), that uses core-region masks to encourage models to rely on target-relevant regions and suppress non-core regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC aim to show improved localization/alignment and, in some settings, competitive predictive performance.

## Strengths
1. The paper tackles an important problem, namely the gap between post-hoc explanations and actual feature alignment during training. The attempt to connect a CAM formulation to a modified training objective is interesting and relevant to the ICLR audience.

2. The core observation in Section 3, that softmax depends only on logit differences and therefore classwise CAMs can carry a shared additive redundancy, is intuitively meaningful. Even if some of the presentation overstates the practical implications, the move from absolute per-class maps to pairwise class-difference maps is a sensible design choice.

3. The proposed ContrastiveCAM representation is simple and easy to compute from existing HiResCAMs. This simplicity is a practical advantage compared to methods that require retraining separate explainers or architectural overhauls.

4. The paper includes both theory and experiments, rather than presenting the method as a purely empirical tweak. Proposition 4.1, expressing the softmax probability in terms of pairwise CAM differences and biases, is the cleanest mathematical part of the paper and does help motivate why class-versus-class explanations may be more aligned with the decision rule than isolated class logits.

5. Some of the empirical effects are striking. In **Table 2** on Hard-ImageNet, CFCE and CFCE+KL dramatically increase Contrastive-CAM IoU from **30.27±3.59** for CE w/ Arch to **89.22±0.31** and **93.39±0.11**, respectively. If this protocol is sound, it suggests the training loss strongly shapes where the model places contrastive evidence.

6. The qualitative examples are also useful. **Figure 2** does a good job illustrating the paper’s main intuition that pairwise class comparisons can reveal distinct evidence patterns that a single HiResCAM may obscure. In particular, the figure supports the claim that class-versus-class evidence can be spatially heterogeneous rather than collapsing to one undifferentiated heatmap.

7. **Figure 3** is an effective visual companion to the Hard-ImageNet results. The before/after comparisons, together with the printed “Core / Non-Core / C+NC” values, make the paper’s intended training effect concrete, namely suppression of background or environmental evidence under CFCE.

8. The paper tries to test the method beyond one benchmark and beyond one supervision regime. In **Table 3** for Oxford-IIIT Pets, the use of GT masks, SAM masks, and bounding boxes is a good idea and suggests the authors are thinking about practical applicability when perfect masks are unavailable.

## Weaknesses
1. **The main theoretical critique of HiResCAM is mathematically true but scientifically overstated, because it mostly rephrases a standard softmax invariance and then elevates it into a claim of explanation unfaithfulness without establishing that the actual computed HiResCAM is ambiguous in practice.**  
   Theorem 3.2 on **Page 4** says that if one starts from a tensor of class maps satisfying Eq. (3), then adding the same spatial matrix \(M\) to every class map yields another tensor that corresponds to the same softmax prediction after summation. But HiResCAM for a fixed trained network and fixed input is not chosen arbitrarily from an equivalence class, it is computed by Eq. (2) from \(\nabla_{\mathbf A_j} f_c\) and \(\mathbf A_j\). The theorem therefore proves a representational non-identifiability of explanations relative to probabilities, not a procedural ambiguity of the actual HiResCAM returned by the model. That is a much narrower statement than the manuscript’s repeated suggestion that HiResCAM explanations “may be misleading” or “fail to guarantee a faithful interpretation” in a strong practical sense. To justify such a conclusion, the paper would need either a theorem linking this redundancy to observed mislocalization under realistic networks, or a controlled empirical study showing that the redundant component is large and harmful across models. Right now the logic jumps from a benign invariance of softmax to a broad indictment of HiResCAM.

2. **Several mathematical claims rely on architecture modifications that substantially narrow the scope, but the paper often phrases them as if they apply to convolutional networks more generally.**  
   On **Pages 18-19**, the appendix states that the authors remove the final downsampling, remove the final classifier bias, and remove the final BatchNorm and ReLU in the last convolutional block to “recover the faithfulness guarantee.” This is not a cosmetic detail. It means the method and several propositions are tightly tied to a specially edited ResNet-50 whose last-layer structure is made CAM-friendly. Yet the introduction and theoretical sections often speak broadly about “convolutional models” and “cross-entropy” as though the conclusions hold for standard ConvNets. In **Table 2**, the gap between “Cross-Entropy” and “CE w/ Arch” is already nontrivial, showing the architectural modifications themselves materially affect the results. The paper therefore conflates three factors: the new explanation, the new loss, and the new architecture. This matters because it makes it unclear what contribution should be credited to CFCE versus to altering the network so that the activation map is more spatially resolved and more directly tied to logits.

3. **The proof and statement of Theorem 4.6 are not convincing, and the classification-calibration claim appears unsupported as written.**  
   On **Pages 15-16**, Theorem 4.6 claims that convergence to optimal \(\mathcal R_{\mathrm{CFCE}}\)-risk implies convergence to Bayes-optimal \(\mathcal R_{\mathrm{CCRM}}\)-risk, “equivalently” that \(\mathcal L_{\mathrm{CFCE}}\) is classification-calibrated in the realizable setting. This is a strong surrogate-consistency statement. However, the proof is largely heuristic. In Eq. (58), the argument introduces \(\inf\) and \(\sup\) manipulations across sums and exponentials without clearly specifying the function class, measurability, or whether those extrema are attained. The transition in Eq. (59) is especially problematic, because “converges uniformly towards the equality case” is asserted rather than derived. Then Eq. (63), \(\sum H \odot \mathbf{CAM}_{(c_t,c)}^{\mathrm{Cntrst}} > 0\), is declared sufficient to show correct classification, but the proof does not carefully bridge this spatial inequality to Bayes optimality under the constrained risk in Eq. (14). In short, this is not a minor gap. The paper is making a calibration claim that typically requires a much more careful surrogate-risk analysis than what is provided here.

4. **The loss definitions are under-motivated and potentially unstable, especially the use of absolute values on non-core regions and KL over softmax-normalized masks.**  
   In **Definition 4.5, Eq. (15)** on **Page 7**, the non-core penalty is \(\sum (1-H)\odot |\mathbf{CAM}^{\mathrm{Cntrst}}_{(c_t,c)}|\), which treats positive and negative contrast symmetrically and always penalizes magnitude. That may suppress any use of non-core regions, but the paper does not discuss whether this can destroy necessary contextual evidence, amplify optimization difficulty, or bias the model toward diffuse low-magnitude maps. Similarly, **Eq. (18)** defines a KL divergence between \(\sigma(\lambda_2 H)\) and \(\sigma(\lambda_3 \mathbf{CAM})\). Since softmax is global over spatial entries, this regularizer is insensitive to additive shifts and mostly encourages matching a normalized distribution over locations, not matching the actual signed evidence pattern. The choice is plausible, but it is not justified carefully, and alternative regularizers such as spatial BCE, Dice, or temperature-controlled sparsemax-style penalties are not discussed. For a paper centered on a new loss, the optimization rationale is surprisingly thin.

5. **The empirical evaluation of explanation faithfulness is weakly designed, because the paper mostly measures overlap with masks rather than causal faithfulness, and some comparisons are not apples-to-apples.**  
   The central claim is about “more faithful” explanations, but the main quantitative evidence uses IoU with ground-truth object regions, for example **Table 2** and the Pets/VOC tables on **Pages 8-9**. Overlap with segmentation masks is at best a proxy for faithfulness, not faithfulness itself. A model can be highly predictive from a small discriminative part of an object and still have low IoU, or conversely can spread saliency over the object without those regions being causally important. This is especially relevant because the method explicitly regularizes the maps toward the target mask, which makes IoU a partially optimized-for metric. The paper cites correctness/faithfulness literature, but does not evaluate insertion-deletion style faithfulness, perturbation-based sufficiency/comprehensiveness, or sanity checks beyond mask overlap. As a result, the evidence is stronger for “mask conformity” than for genuine explanation faithfulness.

6. **Key baselines are missing or insufficiently discussed, especially baselines that also use mask supervision during training.**  
   The experiments compare against CE, CORM, DFR, and combinations in Hard-ImageNet, but the broader claim is that the proposed loss improves feature alignment using core masks. That setup invites comparison to saliency-guided or mask-supervised training methods that directly penalize activation outside foreground regions. The related work on **Page 2** cites Ismail et al. (2021), but there is no experimental comparison. Likewise, on Oxford-IIIT Pets and PASCAL VOC, the paper does not compare to a simpler baseline such as CE plus an auxiliary segmentation-mask alignment loss on GradCAM/HiResCAM, or even a plain masked-image training strategy. Without such baselines, it is hard to tell whether the proposed contrastive formulation is necessary or whether most of the gains come simply from adding object-mask supervision.

7. **The reported gains often come with substantial accuracy tradeoffs, and the paper does not sufficiently analyze whether the method improves robustness/generalization or merely enforces the training masks.**  
   In **Table 2**, the Hard-ImageNet “None” accuracy drops from **93.69±0.77** for CE w/ Arch to **90.35±1.58** for CFCE+KL. The paper frames this as a modest cost for much improved alignment, which may be fair, but it does not test whether this tradeoff improves out-of-distribution generalization, distribution shift robustness, or label-preserving background interventions beyond the specific ablation suite. Similarly, in **Table 3** for Pets multiclass, CFCE+KL with GT masks reaches very high IoU but validation accuracy drops to **90.08±1.47**, well below **95.3±0.1** for CE w/ Arch. That is not a small change. The method may be forcing attention maps to look better at the expense of classification utility, and the paper does not offer a nuanced analysis of when this tradeoff is desirable.

8. **Some tables raise interpretability and evaluation questions that the paper does not address.**  
   In **Table 1** on **Page 5**, the “Redundancy (\(\gamma\))” value for PASCAL VOC is reported as **-1**, which looks like a placeholder or failure case rather than a valid measured quantity, but the paper does not explain it. More broadly, the units and interpretation of “Core,” “Non-Core,” and “Core/Total” are unclear. Are these sums of signed CAM values, absolute values, average activations, or normalized energies? This matters because if the maps have both positive and negative values, the aggregate statistics can change interpretation completely. Since Table 1 is used to motivate the whole training section, the fact that its basic quantities are not crisply defined is a serious exposition issue, not a minor formatting problem.

9. **The exposition around notation and indices is often sloppy enough to hinder verification of the math.**  
   There are many examples. In **Definition 3.3, Eq. (7)** on **Page 4**, the set notation uses \([C]\backslash c\) instead of \([C]\setminus\{c_t\}\), and the target/reference indices are inconsistently named. In **Eq. (11)** and again in the appendix derivation, the summation index alternates between \(i\) and \(c\) in ways that are easy to misread. In **Remark 4.3, Eq. (13)** on **Page 6**, the signs appear inconsistent with Eq. (12), where the decomposition is additive inside the exponent but then rewritten with a negative sign outside the combined masked terms. The BCE formulation in **Eq. (65)** on **Page 16** mixes \(\phi(\cdot)\) and \(\hat f(\mathbf X)_i\) in a way that leaves the negative class term partially unexplained. These are not fatal individually, but collectively they make the theory look under-polished and harder to trust.

10. **The paper’s qualitative figures are suggestive, but they sometimes overclaim relative to what is shown.**  
   **Figure 1** on **Page 4** is a toy illustration of adding \(M\) to CAMs. It does explain the algebraic point, but it is not evidence that learned HiResCAMs in actual models are corrupted by such a shift. The caption and surrounding text push the reader toward that stronger interpretation. **Figure 2** is more useful, but it presents a single three-class toy subset with chosen examples; it does not establish how often the observed phenomenon occurs. **Figure 3** is visually compelling, yet because CFCE directly penalizes non-core activations, seeing lower background response is expected. The important question is whether those maps correspond to improved decision faithfulness and robustness, which the figure alone cannot answer.

11. **The claim that cross-entropy “encourages” learning unrelated regions is too broad relative to the actual result in Section 4.1.**  
   Proposition 4.2 on **Page 6** merely decomposes the standard CE objective into core and non-core terms through a partition of the CAM tensor. This shows CE does not distinguish the source of predictive evidence, which is true. But “does not distinguish” is different from “encourages” spurious regions. The stronger causal language in the introduction and Section 4.1 should be toned down or backed by more direct analysis. Otherwise the paper risks attributing shortcut behavior to CE itself when the issue really lies in the data distribution and available predictive correlations.

12. **The PASCAL VOC multilabel extension is presented too briefly for proper assessment.**  
   The main text on **Page 9** reports AP and IoU for “CFBCE” and “CFBCE + KL,” but the multilabel objective is only defined later in the appendix. Since multilabel classification no longer uses the contrastive softmax machinery that motivates the main method, this part feels like a separate method family attached to the paper. The connection between the binary/multilabel HiResCAM-based objective and the main ContrastiveCAM story is not developed carefully enough in the main text.

## Questions
1. The key theoretical point in Theorem 3.2 is an equivalence class under softmax after summing spatial maps. Can the authors clarify what practical ambiguity this induces for the actual HiResCAM computed by Eq. (2) from a fixed network? In other words, are you claiming non-identifiability of explanations relative to probabilities, or instability/misfaithfulness of the specific HiResCAM procedure used in practice? A more precise statement here would materially affect my assessment.

2. Please provide a cleaner and more rigorous version of the argument behind **Theorem 4.6**. In particular, what are the assumptions on the function class \(\mathcal F\), what notion of realizability is required, and how do Eqs. (58)-(63) imply classification calibration in the standard surrogate-risk sense? If this theorem is meant only as an informal consistency intuition rather than a formal calibration result, the paper should say so explicitly.

3. Why is the non-core penalty in **Eq. (15)** based on \(|\mathbf{CAM}|\) rather than, for example, penalizing only positive evidence outside the core mask? Penalizing absolute magnitude suppresses both supporting and opposing non-core evidence. Did you try sign-aware alternatives, squared penalties, or hinge-style penalties, and if so what happened?

4. Please clarify the exact definitions used in **Table 1** for “Core,” “Non-Core,” and “Core/Total.” Are these sums of signed CAM values, absolute values, positive parts, or something else? Also, why is the redundancy entry for PASCAL VOC shown as \(-1\)?

5. The architecture modifications in **Appendix C.1** appear important. Can the authors report a more explicit ablation separating:  
   a) standard ResNet-50 + CE,  
   b) modified architecture + CE,  
   c) modified architecture + ContrastiveCAM evaluation only,  
   d) modified architecture + CFCE,  
   e) modified architecture + CFCE+KL?  
   This would help disentangle how much comes from architecture versus loss.

6. Since the method directly uses mask supervision, I would like to see stronger comparisons to other mask-guided alignment baselines, including saliency-guided training or simple attention regularizers. Can the authors either add such baselines or argue more concretely why the current set is sufficient?

7. For the faithfulness claim, can the authors provide at least one causal perturbation evaluation, for example deletion/insertion, sufficiency/comprehensiveness, or controlled masking experiments based on the predicted explanation itself rather than ground-truth object masks? This would increase my confidence that the method improves explanation faithfulness rather than only mask overlap.

8. In **Table 3**, multiclass Pets with GT masks shows a sizable accuracy drop under CFCE+KL despite large IoU gains. Can the authors discuss when such a tradeoff is acceptable and whether it reflects over-regularization toward full-object coverage rather than discriminative evidence?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The paper has a plausible core idea and some nontrivial empirical evidence, but several theoretical claims, especially the calibration result and the interpretation of the HiResCAM non-uniqueness argument, are not adequately supported.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures are useful, but the mathematical exposition, notation consistency, and definition of several reported quantities need substantial improvement.

## Contribution Rating
2: fair. The paper raises an interesting angle on contrastive CAMs and mask-guided alignment, but the current framing overclaims, the empirical positioning is incomplete, and it is not yet clear that the work establishes a sufficiently strong advance for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and has some promising ingredients, especially the simple contrastive CAM construction and the strong localization effects on Hard-ImageNet, but the current version overstates the theory, under-justifies the loss design, and does not yet provide the level of empirical and mathematical support I would want for acceptance.

## Reviewer Confidence
4: confident. I am confident in the main concerns I raise, especially about the interpretation of the theoretical claims, the clarity of the math, and the adequacy of the empirical evidence, although I have not independently rederived every appendix step in full detail.