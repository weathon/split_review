Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper identifies compositional generalization (CG)—generalizing to unseen domain-class combinations—as an understudied distribution-shift problem. It proposes Compositional Feature Alignment (CFA), a two-stage finetuning method that learns two orthogonal linear heads (class and domain) via linear probing, then freezes them while finetuning the encoder. The paper also contributes CG-Bench, a benchmark suite built from OfficeHome, DomainNet, iWildCam, and FMoW. Theoretical analysis under the unconstrained feature model (Theorem 1) shows that CFA drives features toward a compositional structure with orthogonal class and domain subspaces. Experiments on CLIP ViT-B/16 and DINOv2 ViT-B/14 show that CFA with WiSE-FT postprocessing achieves the best OOD accuracy on 3 of 4 CG-Bench datasets.

## Strengths

1. **Addresses a genuinely understudied and realistic problem.** Compositional generalization (unseen domain-class combinations) is a natural challenge in large-scale multi-domain, multi-class settings that prior OOD generalization literature has largely overlooked. The paper clearly articulates the distinction from domain generalization and compositional zero-shot learning.

2. **CFA is simple, computationally lightweight, and grounded.** The two-stage approach (linear probing two orthogonal heads → finetune encoder with frozen heads) adds minimal overhead over standard LP-FT. The design is motivated by neural collapse theory, and Theorem 1 formally shows that under the UFM, the second stage drives features toward the desired compositional structure.

3. **Consistent improvements from CFA+WiSE across diverse benchmarks.** CFA with WiSE-FT achieves the highest OOD accuracy on 3 of 4 CG-Bench datasets for CLIP (OfficeHome 56.9% vs. best baseline 53.4%; DomainNet 9.2% vs. 8.7%; iWildCam OOD F1 32.5% vs. 30.0%) and 3 of 4 for DINOv2 (OfficeHome 40.4% vs. 40.0%; DomainNet 6.4% vs. 6.2%; iWildCam OOD F1 33.4% vs. 31.0%). ID accuracy is largely maintained.

4. **Works across different pretraining paradigms.** CFA improves OOD performance for both CLIP (vision-language) and DINOv2 (self-supervised) on multiple datasets, showing the method is not tied to a specific encoder type.

5. **Graceful degradation with limited domain labels.** Table 2 shows CFA retains strong OOD performance with only 10% domain labels (53.4% vs. 54.3% with full labels) and even with CLIP-predicted domain labels (52.0% OOD vs. full finetuning 51.0%), a realistic practical scenario.

## Weaknesses

### Fatal
None.

### Major

1. **Main experimental results lack statistical confidence measures.** The primary results in Table 1 are reported from single runs without standard deviations or confidence intervals. Given that many of the claimed improvements are small (e.g., 0.1–2.9 percentage points for CFA alone over full finetuning), it is impossible to assess whether the observed differences are meaningful or within the noise range of training variance. The paper demonstrates (in Table 2) that it can run multi-seed experiments, making the absence of such reporting for the main results a significant gap. **Why it matters**: Without variance estimates, the paper's central empirical claim—that CFA outperforms standard finetuning—is not convincingly supported by the numbers as presented.

2. **Asymmetric application of WiSE-FT overstates CFA's advantage for DINOv2.** For DINOv2, WiSE-FT is applied to CFA and LP-FT but not to full finetuning or reweighting baselines. The stated justification is that those baselines "do have linear-probed heads" (line 206), but WiSE-FT works by weight-space interpolation with the pretrained checkpoint, which does not require linear-probed heads. Since the best CFA results (e.g., DINOv2 OfficeHome OOD 40.4%) come from CFA+WiSE, and the main baselines do not receive this postprocessing, the comparison is not fully equitable. **Why it matters**: The headline improvements for DINOv2 could partly reflect the WiSE-FT benefit rather than CFA's intrinsic contribution.

3. **CFA alone (without WiSE-FT) shows inconsistent and sometimes negligible gains.** On DomainNet (CLIP), CFA OOD = 7.3% vs. full finetuning 7.5% (CFA is worse). On FMoW (DINOv2), CFA OOD = 38.5% vs. full finetuning 38.4% (gain of 0.1pp). On OfficeHome (DINOv2), CFA OOD = 39.2% vs. full finetuning 38.6% (gain of 0.6pp). These margins are small and, combined with the lack of multiple seeds, make it difficult to conclude that CFA consistently improves over simpler baselines. **Why it matters**: The abstract claims "CFA outperforms common finetuning techniques," but this claim is much stronger for CFA+WiSE than for CFA alone.

### Minor

1. **CG-Bench construction conflates compositional generalization with inherent difficulty.** The OOD split is determined by CLIP's zero-shot accuracy (lowest 20% → OOD), meaning the "OOD" test set consists of combinations that CLIP finds hardest. This confounds two factors: (a) the combination is unseen in training (the actual CG property), and (b) the combination is inherently more challenging (e.g., ambiguous classes in a particular style). The split is also model-dependent (tied to CLIP), raising the question of whether the same split is appropriate for DINOv2 evaluation. A sensitivity analysis (varying the 20% threshold) or a synthetic experiment that cleanly separates sparsity from difficulty would strengthen the benchmark's validity.

2. **The theoretical analysis is limited in scope.** Theorem 1 is derived under the unconstrained feature model (UFM), which treats features as free optimization variables. While this is standard in the neural collapse literature, the paper does not bridge the gap to actual neural network training (e.g., limited capacity, non-convex optimization). The theorem only analyzes Stage 2 (assuming Stage 1 has produced orthogonal, normalized heads); Stage 1 itself receives no theoretical treatment. Adding empirical validation of the predicted feature structure (e.g., quantitative subspace projection metrics on real features) would substantially strengthen the theory-to-practice connection.

3. **Domain adversarial training (DANN) is mentioned but not included as a baseline.** The paper explicitly positions its two-head architecture as "different from domain adversarial neural networks" (line 31), making DANN a natural competitor. Its absence is a gap given the shared architectural motif. (This is not a fatal omission—DANN targets domain generalization rather than compositional generalization—but it would strengthen the positioning to include it or explicitly explain why it is not a suitable baseline.)

### Trivial

- The paper uses both "CG-Bench" (abstract, Section 3.1) and "CG-Suite" (line 33) to refer to the same benchmark. This naming inconsistency should be resolved.

## Nice-to-Haves

- Conduct a sensitivity analysis on the 20% threshold used to split ID/OOD in CG-Bench (e.g., 10%, 30%) to verify robustness of conclusions.
- Quantify the degree of feature alignment before and after CFA using subspace projection metrics (e.g., measure the fraction of feature variance explained by the class head subspace vs. the domain head subspace) rather than relying solely on the 2-domain, 3-class qualitative visualization in Figure 4.
- Ablate the domain head: compare CFA to a variant that freezes only the class head (without the domain head) to isolate the effect of the orthogonality constraint.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the meta-review guidelines:

- **"Color-CIFAR results should be reported in the main text rather than appendix"**: The paper states these results are deferred to the appendix due to page limits. Removed per rule that appendix-stripping is a parser artifact.
- **"The 1% gain with CLIP-predicted domain labels is marginal"**: The paper's claim is that "CFA remains effective," which is supported—CFA at 0% domain labels (52.0) still outperforms full finetuning (51.0) and LP-FT (43.9). The paper openly reports the numbers. This is honest reporting, not a weakness.
- **"The 20% threshold is arbitrary"** taken as fatal criticism: While the threshold is not extensively justified, this is standard practice for benchmark construction. The more measured concern (conflating difficulty with sparsity) is retained in the Minor section above.
- **"The theory has limited practical relevance"** framed as a fatal flaw: The UFM is an accepted modeling tool in the neural collapse literature. The limitation is noted but does not invalidate the theoretical contribution.

## Novel Insights

The meta-reviewer's key observation synthesizing across the reviews: The paper's most novel claim is that learning a domain head with orthogonality constraints during linear probing, then freezing it, can structure the feature space so that class and domain information occupy orthogonal subspaces. The theoretical analysis (Theorem 1) and the feature visualization provide partial support for this claim. However, the empirical evaluation has two intertwined issues: (1) the reported gains are often small and come with a significant postprocessing (WiSE-FT) that is not equally applied, and (2) the benchmark itself may partially measure difficulty rather than compositional generalization per se. This means the paper's empirical contribution is weaker than its conceptual and theoretical contribution. The idea is sound and well-motivated, but the evidence as presented does not fully substantiate the headline claim of substantial improvement.

## Suggestions

1. **Run all main experiments with at least 3–5 seeds and report means ± standard deviations.** The partial-labels experiment (Table 2) already follows this practice; the main results (Table 1) should too. Statistical significance tests or effect-size reporting would further strengthen reliability.

2. **Apply WiSE-FT to all baselines for DINOv2** by interpolating finetuned weights with the pretrained checkpoint (the standard WiSE-FT procedure). Alternatively, clearly report and compare CFA without WiSE-FT as the primary result and treat CFA+WiSE as a secondary variant.

3. **Validate the benchmark construction.** Provide a sensitivity analysis on the 20% threshold, clarify whether the same split or different splits are used for CLIP vs. DINOv2, and consider adding a synthetic experiment (e.g., the Color-CIFAR mentioned in the paper) that cleanly separates sparsity from difficulty.

4. **Add quantitative feature alignment metrics.** Measure the projection of features onto the W₁ and W₂ subspaces before and after CFA finetuning to provide stronger empirical support for Theorem 1 beyond the 2-domain, 3-class qualitative visualization.

5. **Include domain adversarial training (DANN)** as an additional baseline or explain more explicitly why it is not applicable to the CG setting.

## Score and Decision

The paper identifies a real and important problem, proposes a clean, well-motivated method, and provides a formal theoretical analysis. The benchmark CG-Bench is a useful community resource. However, the experimental evaluation has significant shortcomings: single-run results without confidence intervals, small and inconsistent gains from CFA alone, and asymmetric WiSE-FT application that favors the proposed method. These issues collectively prevent the current submission from convincingly supporting its central empirical claims. The core idea has merit and the paper could become a solid contribution after a carefully revised empirical section.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>