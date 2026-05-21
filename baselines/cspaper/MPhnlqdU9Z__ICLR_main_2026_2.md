---
job_id: 1e9228f2-cfec-46c6-b135-05a5c99ef870
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: MPhnlqdU9Z.pdf
paper: MIRA: Quantifying Neural Network Monitorability via Feature Space Analysis
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, touching uncertainty/OoD monitoring, feature-space analysis, representation quality, and safety of learned models across vision, tabular, and language settings.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodological sections defining monitorability and MIRA, experiments, quantitative results, and a conclusion; while I have significant concerns about novelty, validation, and some mathematical/expositional details, these are review-time quality issues rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative reviewer instructions, or suspicious text aimed at influencing automated or human review.

# Expected Review Outcome:
## Summary
This paper introduces the notion of *monitorability* for neural networks, defined as the extent to which prediction failures can be inferred from internal representations, and proposes the MIRA score as a practical metric for estimating this property. MIRA perturbs in-distribution inputs toward the decision boundary, measures separability of perturbed features via a Mahalanobis-based surprisal score, and integrates this effect over a perturbation range. The paper evaluates MIRA across vision, tabular, and NLP models, and compares its ordering of models against the best out-of-distribution detection performance among ODIN, Mahalanobis, and Energy-based detectors.

## Strengths
1. The paper targets a relevant problem. The distinction the authors try to make, namely between having a detector and having a model whose internal features are intrinsically amenable to monitoring, is interesting and useful for safety-oriented model selection. Framing monitorability as a pre-deployment property rather than a runtime detector is a sensible angle.

2. The proposed workflow is practically simple. MIRA only needs ID data plus gradient-based perturbations, and the paper explains the computational motivation for using FGSM in Section 4.2. If the metric were validated more convincingly, this simplicity would be a real advantage.

3. The paper covers several modalities rather than stopping at CIFAR. The inclusion of computer vision, tabular data, and NLP broadens the scope of the empirical study and suggests the authors are aiming for a representation-level concept rather than a vision-specific trick.

4. The toy example in **Figure 1** is effective as an intuition pump. In particular, the contrast between **Figure 1(b)** and **Figure 1(c)** does a good job illustrating the paper’s intended distinction: two models can have similar ID accuracy while differing substantially in whether problematic inputs become separable in feature space. This is one of the clearer parts of the paper.

5. Some of the empirical trends are directionally consistent. In **Table 1**, the ordering CustomNet < ResNet-18 < DenseNet < ViT on CIFAR-10 is broadly aligned between MIRA and the reported average AUROC, which supports the paper’s central intuition at least on this benchmark. Likewise, **Table 2** shows MIRA separating WideMLP from the weaker transformer variants in a way that roughly matches the aggregated detection results.

6. The authors make an effort to formalize the concept rather than only proposing an engineering heuristic. Even though I have reservations about the current definition, the attempt to move from informal “monitorability” talk to a mathematical object is a positive aspect of the submission.

## Weaknesses
1. **The formal definition of monitorability in Definition 1 is too permissive to be scientifically useful in its current form.**  
   On **Page 3**, Definition 1 states that a network is \(l\)-monitorable if there exists a set \(Z^l \subseteq \mathbb{R}^{n_l}\) and \(\epsilon \ge 0\) such that
   \[
   \mathcal{L}(f(x),y)\le \epsilon \iff f^l(x)\in Z^l
   \]
   for all \((x,y)\sim \mathcal{P}_{in}\). As written, this is almost vacuous because one can define \(Z^l\) as the exact image under \(f^l\) of all low-loss inputs. That makes monitorability an existential property with an arbitrarily complex set, rather than a constrained property tied to realistic monitors. The text acknowledges that \(Z^l\) “may be arbitrarily complex,” but that concession is precisely the problem. Without restricting \(Z^l\) to a measurable/learnable family, or quantifying complexity/sample efficiency, the definition does not distinguish models that are monitorable by practical methods from those that are only monitorable by an oracle set. This matters because the paper later evaluates monitorability via one very specific Gaussian-Mahalanobis construction, yet the formal definition does not justify why that surrogate should reflect the existential property in Definition 1.

2. **The bridge from Definition 1 to the MIRA score in Definition 2 is heuristic, not derived.**  
   The paper moves from an iff criterion involving correctness on ID data to a metric based on perturbed-input surprisal, but it does not establish why the latter estimates the former. In **Section 3.3** and **Equation (4)** on **Page 4**, MIRA is introduced as
   \[
   MIRA(f,D,l)=\frac{1}{S_0}\int_{\epsilon_{\min}}^{\epsilon_{\max}} \mathbb{E}_{\tilde{x}\sim \tilde D}[S(f^l(\tilde x))-S_0]\,p(\epsilon)\,d\epsilon.
   \]
   This is plausible as a diagnostic, but the manuscript overstates the connection to the formal notion. There is no theorem, consistency argument, monotonicity result, or even a controlled proposition showing that larger MIRA should correspond to better recoverability of the set \(Z^l\), or better detection of high-loss examples under any assumptions. Right now, the method is best understood as a handcrafted score based on perturbation sensitivity and Mahalanobis surprise, not as a faithful estimator of Definition 1.

3. **The mathematical presentation around the Mahalanobis/surprisal score is inconsistent and in places likely incorrect.**  
   On **Page 4**, the paper argues that “under the Gaussian assumption, \(D_M\) follows a \(\chi^2\) distribution with \(d=\dim(f^l(x))\) degrees of freedom,” and then applies a chi-square survival function directly to \(D_M\) in **Equation (3)**:
   \[
   S(f^l(\tilde{x}))=-\log(\mathrm{sf}_{\chi^2_d}(D_M(f^l(\tilde x)))).
   \]
   But if **Equation (1)** defines \(D_M(x)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}\), then under a Gaussian model it is \(D_M^2\), not \(D_M\), that is \(\chi^2_d\)-distributed. Using \(\chi^2_d\) on the square root rather than on the quadratic form changes the calibration substantially. This is not a cosmetic issue, because the entire dimension-normalization argument of Section 3.3 rests on that probabilistic transformation. At minimum, **Equation (3)** should likely involve \(D_M^2\), or **Equation (1)** should define the squared Mahalanobis distance instead. As written, the score is mathematically mismatched to the stated distributional claim.

4. **Several quantities in Definition 2 are underspecified or notationally inconsistent.**  
   Still on **Page 4**, \(S_0\) is defined as
   \[
   S_0=\mathbb{E}_{\epsilon\sim D}[S(f^l(x))].
   \]
   This appears to be a typo or notational error: the expectation should presumably be over \(x\sim D\), not \(\epsilon\sim D\). More importantly, the exact distribution underlying \(S(\cdot)\) is unclear. The text says Mahalanobis distance aligns with class-conditional GDA, but **Equation (3)** does not specify whether \(D_M\) is computed to the predicted class centroid, the nearest centroid, the true class centroid, or some pooled distribution. That ambiguity matters because these choices can produce very different surprise values, especially under perturbations that flip the predicted class. If the score uses class-conditional Gaussians, the notation should reflect something like \(D_M(f^l(\tilde x); \mu_c,\Sigma)\) with a precise rule for \(c\). Right now, the core score is not specified rigorously enough.

5. **The perturbation definition is too unconstrained for the central claim.**  
   In **Equation (2)** and the accompanying text on **Page 4**, \(\delta(x,\epsilon)\) “can be arbitrary as long as it moves \(x\) toward the decision boundary, potentially crossing it.” That is doing a lot of work. Whether MIRA measures “monitorability” or merely sensitivity to a particular attack recipe depends heavily on how \(\delta\) is constructed. Later, **Section 4.2** chooses FGSM, but the paper provides no ablation against alternative perturbation mechanisms, no analysis of label-preserving vs label-changing perturbations, and no evidence that the model ranking is robust to attack choice. Since MIRA is defined through adversarially oriented boundary probing, the dependence on the attack is not a secondary implementation detail, it is the method. Without this analysis, it is hard to know whether MIRA reflects intrinsic feature-space monitorability or just the geometry induced by FGSM.

6. **The evaluation target, “best achievable OoD detection performance,” is not convincingly justified as a proxy for monitorability.**  
   The paper explicitly claims in **Section 4.1** on **Page 5** that the best AUROC across ODIN, Mahalanobis, and Energy approximates a model’s monitoring potential. This is a big leap. First, all three detectors are standard and somewhat dated; second, “best of three” is not the same as “best achievable”; third, monitorability as defined in the paper is about detecting failures, including potentially on ID inputs, while the experiments validate only OoD detection. There is a conceptual mismatch between the claimed property and the measured proxy. If monitorability is meant to include detectability of near-boundary ID errors, then validation should include misclassification detection, corruption robustness settings, or at least failure prediction on hard-ID examples. Restricting validation to OoD AUROC weakens the core claim.

7. **The tables do not provide the statistical evidence needed to support the correlation claim.**  
   The main empirical claim is that MIRA correlates with monitoring performance. Yet **Tables 1, 2, and 3** only show a handful of model-level averages, with no reported Pearson/Spearman correlation coefficients, no confidence intervals, no hypothesis tests, and no variance across random seeds. The paper repeatedly says “consistently align” and “good correlation,” but the reader is asked to infer this by eyeballing a few rankings. That is not enough for a metric-validation paper. For example, in **Table 2**, MLP has MIRA 30.16 while Transformer has 7.87, yet their average AUROC is 90.80 vs 85.36, a moderate difference rather than a clean separation; in **Table 3**, ELECTRA has a much larger MIRA than RoBERTa, but the average AUROC gap is small. This does not refute the method, but it does show the need for explicit quantitative correlation analysis rather than narrative interpretation.

8. **The result aggregation in the tables is awkward and obscures the actual evidence.**  
   **Table 1** is particularly confusing. The caption says the last column reports “the average of the AUROC scores among the three monitoring methods,” but the per-row entries do not make that operationally transparent, and the formatting suggests the average may be attached only to one row within a model block. More importantly, the paper’s verbal claim in **Section 4.1** is about the “best achievable detection performance across three representative methods,” while the caption of **Table 1** says the last column is an average among methods. Those are different aggregations. Is the validation target the average detector performance, the best detector per OoD dataset, the best detector per model, or something else? This ambiguity directly affects the empirical claim being validated.

9. **The paper compares models with very different accuracy and pretraining regimes, so MIRA may be confounded with general model quality.**  
   The vision experiments are not controlled enough to isolate monitorability from overall representation strength. In the appendix, **Table 5** shows the CIFAR-10 CustomNet has only 69.50% test accuracy, versus ~95-98% for the others, and ViT is pretrained on ImageNet-21k while the CNNs are not. Then in **Table 1**, ViT unsurprisingly dominates both MIRA and OoD detection. This does not demonstrate that MIRA captures a distinct property; it could simply be tracking stronger pretrained representations or plain accuracy. The same issue appears in NLP, where larger pretrained transformers have both better downstream accuracy (**Table 7**) and higher MIRA (**Table 3**). The paper needs controlled comparisons at matched accuracy or shared backbone/training recipe to argue that MIRA is measuring something beyond “better models get better feature geometry.”

10. **The visual evidence in Figure 2 is not as supportive as the paper suggests.**  
   The paper claims in **Figure 2** and the corresponding discussion on **Pages 7-8** that better cluster separation aligns with higher MIRA. But these are t-SNE plots of mixed ID/OoD penultimate activations, and t-SNE is notorious for being sensitive to hyperparameters and distorting global geometry. In fact, **Figure 2(a)-(d)** mainly shows that ViT has visually more separated clusters than CustomNet, which is unsurprising given the rest of the results, but it does not establish the mechanism behind MIRA. Also, the figure legend references many OoD sources simultaneously, making it hard to see whether MIRA is responding to class separation, OoD separation, or both. As a qualitative figure it is fine, but the text leans on it too heavily as evidence of a principled link.

11. **The toy and qualitative visualizations are not cleanly aligned with the formal object being measured.**  
   **Figure 1** uses an explicit OoD class to illustrate monitorability, while the formal definition in Definition 1 is about inference quality on \((x,y)\sim \mathcal P_{in}\). Then MIRA is defined using perturbed ID data. These are three different conceptual objects: external OoD points, ID correctness regions, and adversarial perturbation trajectories. The paper treats them as mutually supportive, but the equivalence between them is not established. This conceptual slippage makes the contribution feel less crisp than the title and abstract suggest.

12. **The paper omits important comparative baselines for an activation-based metric paper.**  
   The work is positioned as the first quantitative measure of monitorability, but there are already activation-centric notions and monitoring/specification approaches in the broader literature. Even within the paper’s own framing, the empirical section should compare MIRA against simpler feature-space proxies such as within-class covariance, class-margin measures, nearest-centroid separation, or neuron-activation-coverage style scores. Without such baselines, it is difficult to know whether the proposed combination of FGSM + Mahalanobis surprisal is necessary, or whether a much simpler statistic would correlate equally well with the reported detector performance.

13. **The claim of efficiency is plausible but underdeveloped as evidence.**  
   The paper states in the appendix that MIRA takes 2-10 minutes per model and is cheaper than tuning multiple OoD detectors. That is reasonable, but the main paper’s claim in **RQ4** and the discussion on **Page 8** would be stronger with actual wall-clock comparisons in the main text, perhaps normalized by dataset size and number of perturbation samples. Since practicality is one of the main selling points, this deserves more than a brief assertion.

14. **Presentation has several avoidable clarity issues.**  
   Beyond the notation problems already noted, there are repeated formatting glitches and inconsistencies: duplicated **Figure 2** caption blocks across **Page 7**, typo-like notation such as \(\mathcal C = 0,1,\ldots,C-1\) instead of \(\mathcal C=\{0,\ldots,C-1\}\) on **Page 2**, and ambiguous phrasing such as “best achievable” when only three methods are tested. None of these alone is fatal, but together they reduce confidence in a paper whose core contribution depends on precise definitions and careful metric construction.

## Questions
1. In **Equation (3)**, should the survival function be applied to \(D_M^2\) rather than \(D_M\)? If not, please provide the derivation that justifies using \(\chi^2_d\) on the square-root Mahalanobis distance. This point materially affects my confidence because the calibration argument seems central to the score.

2. Please specify precisely how Mahalanobis distance is computed in MIRA. Is it class-conditional or global? If class-conditional, relative to the true class, predicted class, nearest class, or minimum over classes? How are the mean(s) and covariance matrix estimated, and is the covariance shared across classes as in standard GDA?

3. Can you provide explicit quantitative correlation statistics between MIRA and your validation target across all model/dataset combinations, for example Pearson and Spearman coefficients with confidence intervals? Right now the paper asks the reader to infer correlation by visual inspection of **Tables 1-3**.

4. How sensitive is model ranking under MIRA to the perturbation choice? A rebuttal including results with at least one alternative perturbation mechanism, or even a non-adversarial but norm-matched perturbation, would help determine whether MIRA captures an intrinsic property or FGSM-specific behavior.

5. Can you clarify the exact aggregation used for the “Average” columns in **Tables 1-3** and how that aligns with the “best achievable OoD detection performance” language in **Section 4.1**? These currently read as different validation targets.

6. Do the conclusions still hold under more controlled comparisons, for example models with similar ID accuracy, or the same architecture trained with different regularization/pretraining schemes? This would help disentangle monitorability from plain model quality.

7. Since Definition 1 concerns detectability of high-loss behavior on ID data, can you provide any validation on misclassification detection or hard-ID failure prediction, rather than only external OoD detection? That would substantially increase my confidence that MIRA is measuring the claimed notion.

8. A comparison against at least one simpler activation-space baseline would be useful. For example, how much do you gain over plain class-separation statistics in the penultimate layer, without adversarial perturbation and without the surprisal transformation?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns stood out from the main paper. The work studies monitoring and safety-relevant evaluation of neural networks using standard public datasets, and I did not identify immediate issues related to privacy, human subjects, or misuse beyond the usual dual-use considerations inherent to adversarial/OoD research.

## Soundness Rating
2: fair. The high-level idea is plausible and the experiments are nontrivial, but the core mathematical specification has important ambiguities, the calibration in Equation (3) appears questionable, and the empirical validation does not yet adequately support the paper’s stronger claims.

## Presentation Rating
2: fair. The paper is readable at a high level and motivated clearly, but several notation issues, aggregation ambiguities, and conceptual slippages make the central contribution less precise than it needs to be.

## Contribution Rating
2: fair. The monitorability framing is interesting, but the current formulation and validation do not yet establish a sufficiently strong, well-differentiated contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a worthwhile intuition and some encouraging trends, but at present it feels under-justified on both the formal and empirical sides. The definition is too unconstrained, the MIRA construction is only loosely connected to that definition, the math around the surprisal score needs correction or clarification, and the validation protocol is not strong enough to support the broader claims about monitorability.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with OoD detection, representation-space monitoring, and metric validation, and I carefully checked the main equations and experimental claims, though some implementation details remain in the appendix.