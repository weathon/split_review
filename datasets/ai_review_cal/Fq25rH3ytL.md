- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper and can verify all claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper investigates whether forward gradients (estimated via the likelihood ratio method) can generate saliency maps for black-box models. The authors apply the LR gradient estimator to inputs rather than parameters, propose a blockwise computation technique for variance reduction, and evaluate on vision models (ImageNet), text sentiment analysis (SST-2), LLM explanation (Phi-3), and CLIP bias analysis. The core theoretical contribution—showing that the LR estimator's expectation equals the expectation of the gradient w.r.t. noise-added input—is sound, but the experimental evaluation has significant gaps that undermine the paper's central claims.

## Strengths

- **Principled theoretical foundation**: Theorem 1 establishes that the likelihood ratio gradient estimator's expectation equals the expectation of the gradient w.r.t. noise-added input under mild growth conditions. Theorem 2 extends this to the blockwise estimator and the paper claims lower per-dimension variance (Eq. 8, elaborated in the appendix). This provides a clean theoretical basis for using forward passes alone to estimate input gradients.

- **Quantitative outperformance over vanilla gradient on 3/4 vision models (Figure 4)**: On deletion/insertion metrics, the forward gradient method—with zero access to model internals—achieves better scores than the white-box vanilla gradient on Inception-V3, VGG-19, and ResNet-50 on ImageNet. The single failure (AlexNet) is plausibly explained by spatial shift rather than poor gradient quality.

- **Demonstrated practical applicability to multiple model types**: The method is applied across diverse settings (CNN classifiers, LSTM text model, Phi-3 LLM, CLIP vision-language model), showing the framework's generality beyond standard image classifiers.

## Weaknesses

### Major

- **No comparison against any existing black-box explanation method**: The paper's stated goal is explaining black-box models, yet it compares only to vanilla gradients (a white-box method). The most directly relevant baselines—RISE (Petsiuk et al., 2018), which also uses random masking and forward passes; LIME (Ribeiro et al., 2016); SHAP (Lundberg & Lee, 2017)—are neither cited nor compared. The blockwise computation (random blocks + forward passes) is conceptually close to RISE, and without a direct comparison the reader cannot tell whether the LR estimator adds value over simpler alternatives. Since RISE similarly operates with only forward passes and random masks, this comparison is essential to assess whether the theoretical machinery of the LR estimator yields practical benefits.

- **The improvement over vanilla gradient is not controlled for the smoothing effect**: Vanilla gradients are known to be noisy, and any smoothing operation (including the noise injection inherent in the LR estimator) trivially improves deletion/insertion metrics. The paper acknowledges this ("forward gradients naturally smooth out the noise by injecting perturbations") but does not include a control condition—e.g., comparing against SmoothGrad (a white-box smoothing method cited in the paper's own related work) or against a simpler averaging of vanilla gradients over perturbed inputs. Without this control, the claimed advantage cannot be attributed to the black-box LR estimator rather than to generic smoothing.

- **Text, LLM, and CLIP experiments are purely qualitative with no quantitative validation**: Section 4.2 presents 4 text examples with subjective interpretation ("we argue that this observation aligns more closely with human understanding") and no quantitative metric. Section 4.3 evaluates Phi-3 on 3 movie reviews, reporting only that the saliency map "closely aligns" with no correlation coefficient or statistical test. Section 4.4 (CLIP bias) is entirely observational—the paper reads spurious correlations off the saliency maps without any ground-truth comparison, baseline explanation, or quantitative measure. Across these three tasks, the paper provides zero quantitative evidence that the forward gradient explanations are accurate or discriminative. The conclusion's claim of "effectiveness and scalability" is unsupported by this evidence.

### Minor

- **Section 3.4 proposes hard-label and text-based strategies that are never evaluated**: The paper introduces WordNet distance as a surrogate for hard-label settings and a prompt construction strategy for text outputs, but neither strategy is tested in any experiment. The vision experiments presumably use soft labels (logits), and the text experiment uses a white-box LSTM with GloVe embeddings, not the proposed text-based strategy. These remain untested claims.

- **No error bars or statistical significance on the main quantitative result**: Figure 4 reports single deletion/insertion scores without error bars, despite the forward gradient estimator having acknowledged high variance and the metrics depending on random block/noise samples. It is impossible to determine whether the observed differences are statistically meaningful.

- **No hyperparameter sensitivity analysis**: The method relies on several parameters (noise std σ, block size, coverage probability q, number of blocks n) that affect the bias-variance tradeoff, but the paper provides no systematic study of their impact. This limits reproducibility and practical guidance.

- **Overclaiming in the introduction and conclusion**: The abstract and Figure 1 state that "Previous methods require the full knowledge of studied models to compute the gradient for model explanation, which makes it impossible to be applied to explain the black-box model." This framing ignores the existence of non-gradient black-box explanation methods (RISE, LIME, SHAP) that also operate without model access. The conclusion claims "effectiveness and scalability" are demonstrated, but the evidence supports these claims only for the vision task and only versus a single weak baseline.

### Trivial

- None that are substantive beyond the points above.

## Nice-to-Haves

- A comparison against RISE with matched computational budget (same number of forward passes) would directly test whether the LR estimator improves over direct Monte Carlo of class scores under random masks.
- An analysis of computational cost (forward passes, runtime) vs. RISE/LIME would help practitioners assess practical tradeoffs.
- A controlled experiment verifying on a small model with known analytical gradients that the LR estimator converges to the true gradient as n→∞ and σ→0.

## Removed Points

- **"The paper does not even cite these methods" (RISE/LIME/SHAP absence)**: Kept as Major because the omission is substantive for the evaluation, not a citation-counting nitpick.
- **Criticism of the "missing appendix" / proofs in appendix**: Removed. The parser strips appendices; they exist in the original submission. The main text provides proof sketches.
- **"The paper frames a false dichotomy between white-box gradient methods and its own approach"**: Modified. The paper's language in Figure 1 is about computing gradients specifically, but the broader framing does ignore non-gradient black-box methods. Folded into the overclaiming point.
- **Strength: "Handling of hard-label and text-based black-box settings"**: Removed. These strategies are proposed but not evaluated, making them aspirational rather than demonstrated strengths.
- **Weaknesses about reproducibility (undisclosed hyperparameters, implementation details)**: Removed per instructions; these are standard for a conference submission.
- **"No comparison to theoretical optimum on simple models"**: Demoted to Nice-to-Have. This is a reasonable suggestion but not a core flaw.
- **Claim that related work omission is "critical framing failure"**: Kept in spirit but softened. The related work does omit black-box explanation methods, which is a real gap given the paper's framing.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface any observation that the paper itself does not already state or imply.

## Suggestions

1. **Add black-box baselines**: Compare against RISE (most directly comparable), LIME, and a simple random-masking baseline on the deletion/insertion game, with error bars over multiple runs. This is the single most important improvement.
2. **Add a smoothing control**: Compare against SmoothGrad (white-box) or averaged vanilla gradients over noise-perturbed inputs to isolate the effect of smoothing from the black-box nature of the estimator.
3. **Provide quantitative metrics for text and LLM experiments**: At minimum, report token-level correlation between forward-gradient and vanilla-gradient attributions across many examples, or run deletion/insertion adapted for text.
4. **Report variance**: Include error bars or confidence intervals for all quantitative results, especially Figure 4.
5. **Evaluate the Section 3.4 strategies**: Test the hard-label surrogate (WordNet distance) and text-based prompt strategy in at least one experiment each.
