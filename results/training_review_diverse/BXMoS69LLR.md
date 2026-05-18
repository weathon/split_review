Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper demonstrates that all eight published membership inference (MI) evaluation datasets for foundation models suffer from distribution shifts between members and non-members. Using simple "blind" attacks that never query the target model (date detection, bag-of-words classifiers, greedy n-gram selection), the authors outperform state-of-the-art model-based MI attacks on every dataset — in some cases more than doubling prior results (e.g., 94.4% vs. 43.2% TPR@5%FPR on WikiMIA). The paper argues that existing MI evaluations conflate genuine membership leakage with spurious distribution-shift artifacts, and proposes a constructive path forward using models trained on random data splits (the Pile, DataComp, DataComp-LM).

## Strengths

1. **Systematic demonstration across all existing MI evaluation datasets.** The paper identifies and empirically characterizes three categories of distribution shift (temporal shifts, replication biases, distinguishable tails) across 8 datasets spanning text and vision-language domains (Table 2). The evidence is consistent: blind attacks beat model-based MI attacks in every case, including on datasets where prior work acknowledged a temporal shift and attempted to control for it.

2. **Blind attacks outperform state-of-the-art MI attacks on every dataset with large margins on most.** The central empirical result (Table 2) is unambiguous. On WikiMIA, a blind bag-of-words classifier achieves 94.4% TPR@5%FPR vs. the best reported 43.2%. On Multi-Webdata, 83.5% vs. 40.3% TPR@1%FPR. On Gutenberg, 59.6% vs. 18.8% TPR@1%FPR. The margins are so large that the conclusion — that existing evaluations are confounded by distribution shifts — is robust even without statistical significance tests.

3. **Demonstration that existing attacks exploit shifts sub-optimally.** On Temporal Wiki and Temporal arXiv, where prior work explicitly attempted to control for temporal shifts, blind bag-of-words attacks still achieve slightly higher AUC and TPR@1%FPR than the best reported MI attacks. This shows that even the best prior attacks do not fully leverage available distributional cues, further undermining claims that they extract genuine membership information.

4. **Fine-grained analysis of subtle biases.** The analysis of LAION-MI (character-level artifacts such as non-English characters and special characters appearing only in members due to translation pipeline differences) and Gutenberg (formatting changes in Project Gutenberg metadata like `.htm` vs. `.html` extensions) provides concrete, interpretable examples of how even careful replication attempts fail. These micro-level analyses strengthen the central argument by showing exactly what the blind attacks exploit.

5. **Constructive path forward.** Section 5 identifies concrete datasets (the Pile, DataComp, DataComp-LM) that provide random train-test splits with models trained on those splits, enabling properly controlled MI evaluations. This gives the community a clear alternative to the flawed a-posteriori datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Abstract overclaims relative to what the evidence strictly shows.** The abstract states that "Existing evaluations thus tell us nothing about membership leakage of a foundation model's training data." The evidence shows that blind attacks *dominate* MI attacks, which means the distribution-shift signal swamps any membership signal. But it does not prove that MI attacks extract *zero* membership information — an attack could exploit both membership leakage *and* a spurious distribution shift, with the latter being larger. The paper itself acknowledges this nuance (line 46: "we cannot rule out that they are (poorly) inferring membership based on data features"), making the abstract and conclusion's stronger framing slightly inconsistent with the paper's own qualifications. This does not undermine the contribution, but a more precise claim — "existing evaluations cannot distinguish genuine membership leakage from distribution-shift exploitation, so they are uninformative as currently constructed" — would be more defensible.

2. **No confidence intervals or measures of variability.** The paper reports point estimates only, even for the bag-of-words and greedy n-gram methods that use 10-fold cross-validation. This is consequential primarily on Temporal Wiki and Temporal arXiv, where the blind attack's margin over the best MI attack is small (79.9% vs. 79.6% AUC on Temporal Wiki; 75.6% vs. 74.5% on Temporal arXiv). Without standard errors or significance tests, these particular results are consistent with the margin being noise. The conclusion still stands (the larger-margin datasets are sufficient), but the claim of "strictly higher" performance on these two datasets is weaker than presented.

### Trivial

1. **The phrase "worse than chance" could be misinterpreted.** The paper uses "worse than chance" (lines 42, 96) to mean "worse than a blind baseline that should perform at chance in a valid evaluation." A reader skimming could misinterpret this as "below 50% AUC" or "below random guessing." The paper clarifies the intended meaning in context, but a short definition upon first use would prevent confusion.

2. **Terminology clarification for "blind."** The paper consistently defines "blind" as "without looking at the target model" (lines 17–18, 51, 346). However, the blind attacks do use membership labels to train classifiers. Explicitly distinguishing "blind (no model access)" from "unsupervised (no labels)" would prevent the misimpression that the attacks require no information about the membership structure at all. The paper already describes the methods transparently, so this is a presentation clarity issue rather than a substantive flaw.

## Nice-to-Haves

- A brief discussion of whether the proposed path forward (controlled datasets like DataComp) addresses the original practical motivation — detecting copyrighted training data or auditing unlearning in production models like GPT-4 and Gemini, whose training sets and weights are not public. The paper could note that its findings on controlled models may still inform expectations for opaque models, or that the field may need complementary approaches for closed models.
- A deeper quantitative analysis of *which* features drive the blind attacks on each dataset (e.g., top distinguishing words for the bag-of-words classifier on WikiMIA, or what fraction of the arXiv one-month attack's signal comes from citation years vs. other dates). This would further concretize the distribution-shift mechanisms for readers.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Blind Baselines could mislead readers into thinking the attacks use no information at all about the membership structure."** The paper consistently defines "blind" as "without looking at any trained model" (lines 17–18, 51, 346) and never claims the attacks are unsupervised or "zero-shot." The methods (bag-of-words training on 80% split, greedy n-gram selection on training data) are described transparently. This is a reader comprehension concern, not a paper flaw.

## Novel Insights

The observation that confidence intervals are missing (especially on the Temporal datasets where margins are razor-thin) combined with the abstract's strong "tell us nothing" claim creates a subtle tension that neither the harsh critic nor the strength finder fully articulated: the paper's *rhetorical* framing is often more aggressive than what the evidence strictly supports, but the *core evidence* (large-margin results on 6 out of 8 datasets) is robust enough to carry the conclusion regardless. The weak-margin results on the two Temporal datasets are the least interesting scientifically anyway — they were already known to have temporal shifts from Duan et al. — so the paper would lose nothing by presenting them more cautiously.

## Suggestions

1. Soften the abstract's "tell us nothing" to something like "cannot be trusted to measure membership leakage as opposed to distribution-shift artifacts" or "are uninformative about genuine membership leakage because blind attacks dominate."
2. Add standard errors or confidence intervals for the blind attack results, particularly for the bag-of-words and greedy n-gram methods that use cross-validation.
3. Upon first use of "worse than chance," add a brief parenthetical definition: "i.e., worse than a blind baseline that should perform at chance under a valid evaluation."
4. Consider explicitly noting that the small margins on Temporal Wiki/arXiv do not weaken the overall conclusion because the other six datasets show overwhelming margins, and the result on Temporal datasets simply confirms that even acknowledged temporal shifts are exploited sub-optimally by existing attacks.

## Score and Decision

The paper makes an original, important, and well-supported contribution. It convincingly demonstrates a fundamental flaw in all existing MI evaluation datasets for foundation models, backed by consistent empirical evidence across 8 datasets. The weaknesses are confined to framing precision and missing confidence intervals — none threaten the central claim. The paper is clearly written and provides a constructive path forward.

**Originality:** High. The core insight — that all existing MI evaluations for foundation models are confounded by distribution shifts — is novel and important.  
**Quality of claims:** Good, with minor overreach in the abstract that does not undermine the contribution.  
**Soundness:** Strong. The experiments are simple, transparent, and convincingly executed.  
**Clarity:** Good. The paper is well-structured and the methodology is clearly described.  
**Value to community:** High. This paper should shift how the community evaluates MI attacks for foundation models.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>