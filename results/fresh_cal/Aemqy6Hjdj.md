Now I have all the information I need. Let me write the final consolidated review.

## Summary

The paper addresses the understudied problem of Compositional Generalization (CG)—generalizing to unseen domain-class combinations—in multi-domain multi-class settings. It proposes Compositional Feature Alignment (CFA), a two-stage finetuning method that learns orthogonal class and domain linear heads via multi-label linear probing (Stage 1), then finetunes the encoder with the heads frozen (Stage 2), theoretically justified via neural collapse theory. It also introduces CG-Bench, a suite of CG benchmarks derived from four existing datasets (OfficeHome, DomainNet, iWildCam, FMoW). Experiments on CLIP and DINOv2 backbones show CFA generally improves OOD performance over standard finetuning, LP-FT, and reweighting baselines, and remains effective even with partial or zero domain labels.

## Strengths

1. **Principled method with theoretical backing**: Theorem 3.1 (Feature Alignment) proves that under the unconstrained feature model, the global minimum of CFA's Stage 2 objective yields features that decompose into a class-component in the span of \(W_1^\top\) and a domain-component in the span of \(W_2^\top\), with the two subspaces orthogonal by construction. This provides a clear theoretical justification connecting the method to compositional feature learning.

2. **CG-Bench fills a gap**: The paper systematically constructs CG benchmarks from four established DG datasets (OfficeHome, DomainNet, iWildCam, FMoW) by designating the lowest 20% zero-shot-accuracy domain-class combinations as OOD. This provides a principled, reproducible protocol for studying CG, which the paper correctly identifies as understudied relative to other OOD generalization settings.

3. **Robustness to partial domain labels**: Table 2 shows CFA with only 10% of domain labels achieves OOD accuracy 53.4% on OfficeHome (vs. 54.3% with 100%), and with CLIP-predicted labels (0% real labels) still reaches 52.0%, outperforming standard fine-tuning (51.0%) and LP-FT (43.9%). This is a genuine practical advantage and well-demonstrated.

4. **Qualitative feature visualization confirms compositional structure**: Figure 5 shows CFA-finetuned features on DomainNet form clear orthogonal groupings by class and domain (2 domains, 3 classes), while pretrained features do not. This provides direct—if qualitative—evidence that the method induces the intended feature geometry.

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice disconnect: \(\lambda = 0\) in Stage 2 contradicts the theoretical setup**: The paper explicitly states it deploys \(\lambda = 0\) in Stage 2 (line 211) to reduce compute cost. However, Theorem 3.1 analyzes the objective in Eq. (7) where \(\lambda > 0\) appears in the domain-head loss term. With \(\lambda = 0\), the domain-head cross-entropy loss contributes nothing to Stage 2 optimization, so the theoretical guarantee that the domain subspace component is learned during finetuning does not directly apply to the actual algorithm used. While the head-freezing mechanism from neural collapse literature provides a separate motivation, and while an ablation on \(\lambda\) is promised in the appendix, the paper does not reconcile this discrepancy. This weakens the claimed connection between theory and practice.

### Minor

- **Empirical gains are inconsistent and lack statistical rigor**: Across Table 1, improvements vary widely: OfficeHome CLIP (OOD: +3.3 to +4.4 points) and iWildCam (OOD F1: +3.8 to +12.5 points) show meaningful gains, but DomainNet CLIP (OOD: +0.5 points with WiSE, and without WiSE CFA *loses* 7.3 vs. 7.5 to Fine-Tuning), FMoW (tied or below baselines), and most DINOv2 results show marginal improvements (0.1–0.6 points). No confidence intervals or statistical tests are reported for the main results, making it impossible to assess whether the small margins reflect genuine improvement or noise. The paper's practice of bolding values "within a range of 0.2" obscures cases where CFA does not clearly win.

- **Benchmark construction may not isolate compositional generalization**: The OOD split is defined as the 20% of domain-class combinations with lowest CLIP zero-shot accuracy. This conflates "intrinsically hard for zero-shot" with "requiring compositional generalization of unseen combinations." The paper shows a correlation between training data availability and accuracy (Figure 4) but does not validate that the difficulty is compositional in nature rather than reflecting a hard-class tail. The high density of observed combinations (80%) also differs from many realistic sparser-coverage scenarios.

- **Uneven baseline comparisons for DINOv2**: Several DINOv2 baselines (Fine-Tuning, Reweight-E) lack WiSE-FT variants. The paper explains that DINOv2 has no zero-shot head, so WiSE-FT interpolation uses the linear-probed head only for methods that have one. This creates an asymmetric comparison where CFA gets a WiSE-FT boost on DINOv2 while some baselines do not, making head-to-head comparisons on DINOv2 (especially WiSE rows) difficult to interpret.

### Trivial
None.

## Nice-to-Haves

- **Comparison with domain-adversarial methods** (e.g., DANN): The paper highlights the connection to domain adversarial neural networks in the introduction but does not include them as baselines. A direct comparison would help isolate the benefit of CFA's alignment mechanism over adversarial feature matching.
- **Synthetic compositional experiments**: The paper mentions a Color-CIFAR synthetic dataset but does not present results. A controlled synthetic experiment with known generative structure would provide cleaner evidence that CFA recovers orthogonal subspaces.
- **Quantitative measures of feature compositionality**: Beyond the qualitative t-SNE visualization (Figure 5), the paper could measure subspace orthogonality or compute the residual of the decomposition \(z \approx W_1^\top a_y + W_2^\top b_e\) on real data to quantify how well the compositional structure is achieved.

## Removed Points

These points were raised by reviewers but are removed from the main review with justifications:

- **"The empirical evidence does not support the main claim"** — Overstated. While gains are mixed, CFA does achieve the best OOD accuracy on many settings (OfficeHome CLIP: +3.8, iWildCam CLIP F1: +3.8, iWildCam DINOv2 F1: +2.4). The claim "outperforms common finetuning techniques" is supported in aggregate, though the magnitude varies. This is reframed as a Minor weakness about inconsistency/lack of error bars, not a fatal evidential problem.
- **"No confidence intervals"** — A valid concern, but single-run evaluation on large benchmarks is common practice in this area. Kept as part of Minor weakness #1, not a standalone fatal issue.
- **"Missing related works"** — Removed per instructions (cannot verify existence of missing references).
- **"Reproducibility details missing from main text"** — The paper states these are in the appendix. The parser strips the appendix; they exist in the original submission.
- **"The ablation on λ is deferred to the appendix"** — Same as above; the appendix is stripped by the parser.
- **"Missing appendix, missing proofs in appendix"** — Removed per instructions; parser strips these.
- **"No experiment varying the sparsity of domain-class combinations"** — This is a nice extension but not a flaw in the current benchmark design.
- **Pure formatting/style nitpicks and typos** — Removed per instructions (these are parser artifacts).

## Novel Insights

The reviews do not surface a genuinely novel observation about the paper beyond the paper's own contributions. The main insight from the review process is that while CFA is a well-motivated method with theoretical grounding, its practical advantage is dataset-dependent and the \(\lambda = 0\) implementation choice creates a disconnect from the theoretical framework that the paper should explicitly address rather than defer to an appendix.

## Suggestions

1. **Resolve the \(\lambda = 0\) disconnect**: Either provide theoretical justification that the neural collapse head-freezing mechanism guarantees the compositional structure even with \(\lambda = 0\) (without relying on Theorem 3.1's specific assumptions), or report Stage 2 results with \(\lambda > 0\) and demonstrate comparable performance. Bring the \(\lambda\) ablation from the appendix into the main paper.

2. **Add statistical rigor**: Report results over multiple seeds with standard deviations or confidence intervals for all main results (Table 1). At minimum, show that the claimed improvements are significant given the observed variance.

3. **Validate the benchmark's compositional nature**: Provide evidence that the OOD split genuinely requires composition rather than just being a hard-example tail—e.g., by showing that models trained on the same combinations with sufficient data can achieve high accuracy, or by constructing synthetic compositional shifts with known ground truth.

4. **Complete the DINOv2 baselines**: Add WiSE-FT variants for all DINOv2 baselines (or clearly explain why they are infeasible for each case) to ensure fair comparisons.

5. **Quantify compositionality**: Supplement the qualitative feature visualization with quantitative measures (e.g., subspace alignment, residual of the compositional decomposition) to directly verify that CFA induces the claimed feature structure in practice.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>