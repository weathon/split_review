- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 8, 5, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Re-Debias, a framework for long-tailed classification that combines two components: a **Residual-Energy score** that computes the energy of non-target logits (Eq. 10) as a more discriminative alternative to softmax-based NLL, and a **Debias estimator** derived from inverse propensity weighting that corrects class-distribution bias and reduces to a logit-offset of log(C·π\_y). Experiments on CIFAR-10/100-LT, ImageNet-LT, and iNaturalist18 report strong top-1 accuracies. The paper also introduces Sacrificial Accuracy (SA) and Sacrifice Ratio (SR) to quantify per-class performance trade-offs.

## Strengths

1. **Concrete diagnosis of softmax ambiguity via energy analysis**: Section 3.2 and Figure 2 provide a clean empirical demonstration that two CIFAR-10-LT samples (one correct, one incorrect) yield nearly identical softmax NLL losses, while the proposed Residual-Energy score reveals a clear difference (−4.39 vs −8.48). This directly supports the paper's claim that softmax-based scores can be ambiguous in long-tailed settings.

2. **SA and SR as diagnostic tools**: Section 1 introduces Sacrificial Accuracy and Sacrifice Ratio to quantify per-class accuracy changes against a CE baseline. Figure 1 uses these to show that existing methods (LGLA, DODA) improve tail classes at the expense of head classes, motivating the paper's decomposition of long-tailed learning into individual prediction quality and unbiased aggregate evaluation.

3. **Formal derivation connecting long-tailed learning to causal inference**: Section 4.2 links the long-tailed data bias to the MNAR framework, derives a propensity-weighted estimator, and arrives at a logit-offset solution (Eq. 17–19). While the final algorithm converges to the known logit adjustment (Menon et al. 2021), the causal-inference derivation pathway is a different framing that is presented with clear mathematical steps (Eq. 9–17).

4. **Strong reported performance on large-scale benchmarks**: The paper reports competitive results: 63.9% top-1 on ImageNet-LT (200 epochs), 79.5% on iNaturalist18 (400 epochs), and 83.9% on ViT fine-tuning on iNaturalist18, with balanced performance across Many/Medium/Few splits (e.g., 80.6%/79.6%/79.1% on iNaturalist18).

## Weaknesses

### Fatal
None.

### Major

1. **Section 5.4 (Evaluation and Analysis) is empty — the paper is incomplete**.  
   Section 5.4 states "we conduct a detailed analysis of the mechanism of Re-Debias and discuss the following three concerns" but then contains no substantive text — only a repeated table caption and an image placeholder. This section would be the natural place for ablations, mechanism analysis, and empirical validation of why the method works. Its absence means the paper's central analytical claims are unverifiable from the submitted manuscript. A paper whose promised analysis section is missing cannot be accepted.

2. **No ablation study isolates the two contributions**.  
   The paper has two components: (a) the Residual-Energy score via mixture-of-softmaxes and (b) the Debias estimator (logit offset). There is no experiment showing: standard CE → CE + logit offset only → residual-energy only → full Re-Debias. Without this, we cannot determine whether the residual-energy component adds any value beyond the known logit adjustment, or whether the reported gains come entirely from the debiasing term. This is compounded by the empty Section 5.4, which could have contained these ablations.

3. **The Debias estimator recovers the known logit adjustment (Menon et al. 2021) as a special case, and is not compared against it as a baseline**.  
   The paper derives g\_y(x) = f\_y(x) + log(C·π\_y) (Eq. 19) and explicitly states "Following Menon et al. (2021)" for the Fisher consistency step. The resulting algorithm is the logit adjustment method. Yet the experiments do not include direct logit adjustment (Menon et al. 2021) as a standalone baseline. Without this comparison, the paper cannot demonstrate whether the Residual-Energy score provides any benefit beyond this known technique. This undermines the claim of "state-of-the-art" performance, as the improvement could be entirely attributable to the known component.

4. **The Residual-Energy mixture-of-softmaxes is critically underspecified**.  
   The paper defines p\_re(y|x) = Σ w^k · softmax(f^k(x)) with w^k = w(E^k(x,ȳ)) and Σ w^k = 1 (Eq. 11), but does not specify: (a) how the K logit components f^k\_j(x) are produced (multiple output heads? different projection layers?), (b) the functional form of w(·) — it is merely called a "normalisation function", (c) how K is chosen or whether it varies. This makes the core novel component non-reproducible from the paper as written. While inspired by Mixture of Softmax (Yang et al. 2018), the specific integration with residual energy lacks the necessary implementation details.

### Minor

1. **Underperformance on CIFAR-100-LT (ratio 100) is attributed to fewer epochs without verification**.  
   The paper notes it underperforms LGLA on CIFAR-100-LT ratio 100, attributing this to training for only 200 epochs vs. LGLA's 400. This is a reasonable hypothesis, but the authors did not run the experiment at 400 epochs to confirm. Given that this is one of the standard benchmarks, the explanation remains speculative.

2. **The derivation of the Debias estimator conflates two different target risks**.  
   The paper defines the "true" risk R(Ŷ,Y) as the loss on an ideal balanced dataset with C·n samples per class (Eq. 8), but the actual goal of long-tailed learning is not to estimate balanced-dataset performance; it is to achieve good performance on a naturally long-tailed test distribution. The unbiasedness claim is relative to an idealized balanced dataset, not the real evaluation distribution. This framing should be clarified.

3. **No variance or confidence intervals reported**.  
   Results are presented as point estimates. While single-run evaluation on large benchmarks is common practice in this subfield, the absence of any variance information weakens the reliability assessment, particularly for the smaller CIFAR-LT datasets where multiple runs would be feasible.

### Trivial

- Eq. 10 (line 121) uses the index "j≠1" to denote non-target classes, which appears to be a typo for "j≠y" (the target class variable).
- Several typographical issues: "traning" (line 199), "limination" (line 112), "tipycal" (line 116), "socres" (line 27).

## Nice-to-Haves

- Including logit adjustment (Menon et al. 2021) as a direct baseline.
- Reporting per-class average accuracy in addition to overall top-1 and Many/Medium/Few splits, to align with the stated goal of unbiased aggregate evaluation.
- A complexity analysis (parameter count, training time) for the mixture-of-softmaxes components vs. standard single-head architectures.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic: "The derivation of the debias estimator is not novel and re-derives prior work without added value"** — Partially retained as Major weakness 3 (not compared as a baseline). However, the paper *does* cite Menon et al. explicitly for the Fisher consistency step and notes logit adjustment in the related work (line 12). The causal-inference derivation pathway is a different framing, even if the result matches existing work. Removed the claim that the paper "presents a known method as a novel contribution without citation" — the citations are present.
- **Harsh Critic: "The evaluation lacks statistical significance / standard deviations"** — Demoted from Major to Minor (weakness 3 in Minor), as single-run evaluation is standard for these benchmarks in the long-tailed learning literature.
- **Harsh Critic: "No analysis of computational cost"** — Moved to Nice-to-Haves.
- **Harsh Critic: "Whether residual-energy score is used during inference"** — The paper specifies the training loss (Eq. 17); for standard losses, the learned logits are used at inference time. This is implied but could be stated explicitly. Moved to Nice-to-Haves.
- **Harsh Critic: "The paper does not prove that the long-tailed setting is truly MNAR"** — The MNAR analogy is used as a conceptual framework, not a formal proof. The paper states it "treats" long-tailed data as MNAR, which is sufficient for the derivation.
- **Strength Finder: Generic or superficial strengths** — Dropped generic formulations about "comprehensive evaluation" and "broad validation" where they lacked specific content. Removed "state-of-the-art results" as a standalone strength because the comparison is incomplete without the logit-adjustment baseline.
- **Strength Finder: "Theoretical derivation of an unbiased estimator via causal inference"** — Partially dropped because the derivation converges to existing logit adjustment. Retained as an interesting framing (Strength 3) but with caveat.

## Novel Insights

None beyond the paper's own contributions. The two review sources largely agree on the issues but express them at different severities. The only synthesized insight not explicit in either review is that the empty Section 5.4 compounds the ablation problem: even well-done experiments elsewhere cannot compensate for the missing analysis section that the paper itself promised.

## Suggestions

1. **Complete the paper**: Section 5.4 must contain the promised analysis before the paper can be evaluated seriously. This includes ablations isolating each component, sensitivity analysis for K (number of mixture components), and the form of w(·).
2. **Add a direct logit-adjustment baseline**: Compare against Menon et al. (2021) with identical training setups (backbone, epochs, optimizer) to isolate the effect of the residual-energy score.
3. **Specify the mixture-of-softmaxes architecture completely**: Describe how the K logit components are generated from the backbone, provide the functional form of w(·), and state the value of K or how it is chosen.
4. **Include an ablation with four conditions**: (a) standard CE, (b) CE + logit offset only, (c) residual-energy mixture only (no offset), (d) full Re-Debias. This would substantiate the claim that both components contribute.
5. **Clarify the unbiasedness claim**: State explicitly that the estimator is unbiased relative to a balanced dataset with C·n samples per class (Eq. 8), and discuss how this relates to the actual evaluation distribution (which is also long-tailed).
6. **Run CIFAR-100-LT ratio 100 for 400 epochs** to resolve whether the underperformance relative to LGLA is indeed an epoch issue.
