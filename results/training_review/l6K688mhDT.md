Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies the underexplored problem of how pre-training data imbalance (termed "parameter imbalance") affects downstream long-tail fine-tuning, distinguishing it from the typically considered downstream "data imbalance." Through empirical analysis, the paper shows that parameter imbalance persists after fine-tuning and cannot be corrected by standard logit-adjustment methods. The authors propose a causal framework treating the incomplete semantic factor arising from parameter imbalance as a confounder, and introduce a backdoor adjustment method that fuses predictions from multiple foundation models (CLIP, OpenCLIP, MetaCLIP) fine-tuned with logit adjustment. The method achieves consistent SOTA results on Places365-LT, ImageNet-LT, and iNaturalist2018.

## Strengths

1. **Systematic decomposition and empirical evidence that parameter imbalance dominates after fine-tuning.** The paper formally defines parameter imbalance (via pre-training label prior) and data imbalance, and shows through carefully designed experiments (Fig. 2, Fig. 3) that while LA effectively relieves data imbalance, parameter imbalance persists. The "Tail-Tail" analysis (classes that are few-shot in both senses) identifies the hardest cases, and the 9-group breakdown (D-Many/Med/Few × P-Many/Med/Few) is insightful. This analysis alone is a meaningful contribution.

2. **Demonstration that logit-adjustment–style re-balancing cannot fix parameter imbalance.** The paper extends GLA into training (GLA-Train, Eq. 6) and finds minimal additional benefit over LA (Tab. 3). The KNN accuracy analysis (Tab. 4) shows that re-balancing improves tail classes primarily through the classifier, not through representation, confirming that parameter imbalance embedded in backbone features is qualitatively different from data imbalance. This finding distinguishes the work from prior long-tail methods targeting only downstream bias.

3. **Consistent SOTA results across three benchmarks with largest gains on tail classes.** The method outperforms strong baselines (LIFT, VL-LTR, RAC) on Places365-LT (Tab. 5), ImageNet-LT (Tab. 6), and iNaturalist2018 (Tab. 7), with the largest improvements on D-Few classes (e.g., +3.49% on ImageNet-LT). The ablation on the number of foundation models (Tab. 8) shows monotonic improvement with more models (M=1→3), and the per-class analysis (Fig. 6) confirms gains specifically on P-Few classes, supporting the core claim.

## Weaknesses

### Fatal
None.

### Major

1. **The causal framing is overclaimed relative to what the method actually delivers.** The paper constructs a causal graph (Fig. 5) with \(C\) (incomplete semantic factor) as a confounder creating a backdoor path \(X \leftarrow C \rightarrow Y\), and applies backdoor adjustment (Eq. 7) to estimate \(\mathbb{P}(Y=y\mid do(x))\). However, the method reduces to: fine-tune multiple foundation models with LA, then average their logits with uniform weights \(\mathbb{P}(c)=1/M\). The causal graph provides a motivating intuition, but the paper does not establish that this averaging operation corresponds to a proper causal intervention or that the backdoor criterion is satisfied. The approximation of using different pre-trained models as distinct values of \(C\) is not formally justified — these models differ in many ways beyond their "incomplete semantic factors" (training data composition, optimization details, etc.). The paper would benefit either from a more rigorous causal validation or from honestly framing the contribution as a well-motivated ensemble method (which would not diminish its empirical value).

2. **The claim that "parameter imbalance cannot be resolved by re-balancing methods" rests on limited evidence.** The paper tests one specific formulation (GLA-Train, Eq. 6) that integrates both upstream and downstream priors into the loss, finds it ineffective, and concludes that "parameter imbalance is fundamentally different from data imbalance and cannot be resolved through simple adjustment alone" (end of Section 4.2). The paper does not analyze *why* GLA-Train fails (e.g., inaccurate prior estimation, optimization difficulties, interaction between the two adjustment terms), nor does it explore alternative re-balancing strategies (e.g., feature-level debiasing, separate classifiers for upstream/downstream biases, different prior estimation methods). While the conclusion may well be correct, the evidence from a single failed attempt is insufficient to support the strong "cannot be resolved" claim.

### Minor

3. **Missing comparison against a CE-based ensemble baseline.** The ablation in Tab. 8 compares M=1 (single model with LA) against M=3 (three models with LA), demonstrating the benefit of ensembling. However, a baseline of ensembling the same three models fine-tuned with cross-entropy (without LA) would help isolate whether the gains come from LA, from ensembling multiple models, or from both. This would strengthen the attribution of results to the proposed framework.

4. **Parameter imbalance estimates rely on an indirect and potentially noisy estimation procedure.** The estimated prior \(\widehat{\mathbb{P}}_P(Y)\) (Eq. 3) is obtained via a minimax optimization on the validation set using GLA. The paper does not analyze the sensitivity of its conclusions to this estimation — e.g., how varying the validation set size, using different estimation methods, or comparing estimated priors against known priors on synthetic data would affect the results. All subsequent analyses (Fig. 2/3 groupings, Fig. 6 evaluation) depend on this estimate.

### Trivial
- Line 19: "relive" → "relieve"
- The formula rendering in the PDF extraction shows some artifacts (e.g., "$\mathbf{i.65\%}$" in Tab. 6 description), though these are parser issues.

## Nice-to-Haves
- A controlled experiment where the same foundation model is fine-tuned on data with varying artificial upstream label priors (e.g., by subsampling pre-training data) would strengthen the causal link between pre-training data distribution and parameter imbalance.
- Analysis of why GLA-Train fails (loss landscape, interaction of the two prior terms) would make the "cannot be resolved" claim more convincing.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Critical Issue 1 (part):** The claim that Eq. 7 "is not a standard backdoor adjustment" and "does not correspond to an intervention do(x)" is factually incorrect. The backdoor adjustment formula \(\mathbb{P}(Y|do(X)) = \sum_Z \mathbb{P}(Y|X,Z)\mathbb{P}(Z)\) IS an average over confounders. The paper's Eq. 7 follows this form — marginalizing over \(C\) after blocking the backdoor path. The formula itself is standard; the debatable issues are about whether the causal graph is correctly specified and whether the approximation using three models as values of \(C\) is valid (covered in Major weakness #1 above).
- **Critical Issue 2 (part):** The claim that "the paper does not provide this baseline" (comparing single model vs ensemble) is incorrect. Tab. 8 directly compares M=1 (single model with LA) against M=3 (three models with LA), showing +2.27%/+2.58%/+3.29% gains on D-Many/Med/Few. This IS the relevant comparison controlling for ensemble effects. The paper does not, however, include a CE-based ensemble baseline (covered in Minor weakness #3).
- Strength Finder's generic strengths about "addressing an important problem" — these add no content and are dropped.
- Any formatting/style nitpicks, typos, or missing appendix references — these are parser artifacts, not author errors.
- The suggestion that the paper conflates parameter imbalance with other model differences — all three models use ViT-B/16 architecture; the primary difference is pre-training data distribution, which is exactly what parameter imbalance is about.

## Novel Insights

The most valuable observation not fully articulated by the paper itself is that the failure mode of logit adjustment on parameter imbalance (GLA-Train's ineffectiveness) combined with the KNN accuracy analysis (Tab. 4) suggests a **hierarchy of fixability**: downstream data imbalance operates primarily at the classifier level (fixable by logit adjustment), while upstream parameter imbalance is embedded in the feature representation itself (not fixable by output-level corrections). This insight — that bias in deep models can be stratified by depth of embedding — has implications beyond the long-tail setting, and the paper's evidence for it is stronger than the paper's own causal claims. The ensemble approach then works because it provides a *different* kind of correction: not adjusting a single model's outputs, but diversifying the feature representations themselves by combining models with different biases.

## Suggestions

1. **Reframe the contribution honestly.** Either provide rigorous causal validation (e.g., Pearl's do-calculus derivations, synthetic experiments where ground-truth causal structure is known) or drop the strong causal language and present the method as a well-motivated ensemble approach. The empirical results stand on their own; the causal framing adds vulnerability without proportional benefit.

2. **Add a CE-based ensemble baseline.** Fine-tune CLIP, OpenCLIP, and MetaCLIP with CE (no LA), average their logits, and report the results alongside Tab. 8. This would isolate the contribution of LA within the ensemble and make the ablation complete.

3. **Investigate why GLA-Train fails.** Analyze whether the failure stems from poor prior estimation, optimization difficulties in Eq. 6, or fundamental limitations. This would either strengthen the "cannot be resolved" claim or reveal alternative paths forward.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>