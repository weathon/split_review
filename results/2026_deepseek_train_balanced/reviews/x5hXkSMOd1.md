## Summary

SANER proposes a debiasing method for CLIP that (1) avoids requiring attribute-annotated datasets (like FairFace) by instead using automatically augmented attribute-specific text, and (2) preserves attribute information when it is explicitly stated in the input (e.g., "a female doctor"). The method trains a lightweight MLP debiasing layer on top of the CLIP text encoder using an equidistance loss over neutralized text, reconstruction loss, and contrastive loss. Experiments on text-to-image retrieval (MaxSkew) and text-to-image generation (Stable Diffusion) show reductions in gender, age, and racial bias across FairFace and PATA datasets while retaining near-original zero-shot ImageNet accuracy.

## Strengths

- **Preservation of explicitly specified attribute information is cleanly demonstrated.** Table 3 (generation task) shows SANER achieves 1.00 accuracy for gender-specific prompts ("a photo of a female/male doctor"), identical to un-debiased CLIP, while projection-based debiasing drops to 0.58/0.79. This directly validates a key claimed advantage over prior work.

- **Consistently superior bias reduction across three attributes and two datasets.** In Table 1 (gender), SANER outperforms both prompt-tuning and projection across all 6 settings (FairFace and PATA × adjective/occupation/activity). In Tables 2–3 (age and race), SANER is best in 10 out of 12 settings. The consistency across attributes and image domains (face-centric vs. natural images) strengthens the claim of generalizability.

- **Negligible degradation of CLIP's core capability.** ImageNet-1K accuracy drops from 65.4% (original CLIP) to 65.2% (SANER), a loss of only 0.2 percentage points compared to prompt tuning's 1.3-point drop (to 64.1%). This is important evidence that debiasing does not come at a serious utility cost.

- **Method design is simple and principled.** The core idea—neutralize text, then enforce equidistance to attribute-specific variants—is elegantly self-supervised and requires no adversarial training or attribute classifiers. The regularization losses (reconstruction + contrastive) are standard and well-motivated.

## Weaknesses

### Fatal
None.

### Major

- **Inference procedure is ambiguous and inconsistent with the training formulation.** Training (Eq. 3, line 160) defines the debiased feature as `h(t) = f_t(ξ_n(t)) + r(f_t(ξ_n(t)))` — i.e., neutralized text with a residual connection. Inference (line 194) says "use the modified text features `r(f_t(t))`" — i.e., just `r` applied to the *original* (non-neutralized) text, with no residual and no neutralization. This discrepancy matters critically for the attribute-retention experiments (§5.2). The paper claims that "only feature vectors for attribute-neutral descriptions are debiased, whereas the attribute-specific ones retain the original information" (line 30), yet the inference description does not specify any conditional handling. If the debiasing layer is applied uniformly to all text features during inference (as line 194 suggests), its behavior on attribute-specific inputs (which were never in the training distribution) is undefined, and the perfect 1.00 accuracy on gender-specified prompts requires explanation. The paper must disambiguate the actual inference procedure.

- **The comparison with prompt tuning (Berg et al. 2022) conflates method design with training data volume and diversity.** SANER is trained on 170,624 COCO image-caption pairs; prompt tuning uses ≈11K FairFace images with only 10 pre-defined concepts — a >15× difference. The paper itself acknowledges this at line 296, attributing SANER's better performance "possibly because SANER is trained with diverse text descriptions." The paper frames the annotation-free design as enabling this data advantage, which is a real contribution. However, the central claim that SANER's *design* is superior to existing methods would be better supported by a controlled comparison — e.g., training an existing method on the same COCO subset, or training SANER on FairFace-scale data. Without this, the reader cannot separate method quality from data-scale effects.

### Minor

- **The equidistance loss lacks empirical validation as a measure of attribute information removal.** The core debiasing loss forces `h(t)` to have equal cosine similarity to all attribute-specific text variants. While symmetric similarity is a reasonable indicator of reduced attribute signal, the paper provides no diagnostic — such as training a linear attribute classifier on the debiased features and measuring whether accuracy drops — that directly connects the loss to actual attribute information removal. A feature can be equidistant to two class prototypes in cosine space while still encoding attribute variation along other dimensions.

- **Two recent and closely related baselines (ARL, Mapper) are absent from the comparison.** The paper states these could not be reproduced (line 223). This is an honest disclosure, but their absence means the empirical comparison is limited to just two methods (prompt tuning and projection), both of which the paper's own analysis identifies as having clear limitations. The claim of "superior debiasing ability" would be substantially stronger with results from author-provided checkpoints or simplified implementations of these methods.

- **"Annotation-free" slightly overstates the method's requirements.** SANER does not need image-level attribute annotations, which is a meaningful advantage. However, it requires manually curated word lists for each protected attribute (gender words, age words, etc.), as described in §4.1. This is a weaker requirement than image annotations, but not strictly annotation-free.

- **No statistical significance or confidence intervals for the retrieval results.** MaxSkew@1000 values are reported as point estimates. Given that SANER and baselines are close in several conditions (e.g., FairFace age/activity: Projection 100.0 vs. SANER 101.9, where SANER is *worse*), the reliability of the claimed improvements is unclear. The generation results include standard deviations, but the SP values overlap substantially between methods (SANER: 0.39±0.22, Projection: 0.47±0.19), and no significance test is provided.

### Trivial

- The ablation study of the three loss components (L_deb, L_recon, L_cont) is deferred to the supplementary material; a summary in the main paper would strengthen the experiments section.

## Nice-to-Haves

- A controlled experiment training SANER on FairFace-scale data (e.g., 10K samples) would help decouple the method's inherent advantage from the data-scale advantage and strengthen the core claim.
- A linear probe diagnostic on debiased features (predicting the protected attribute) would empirically validate that the equidistance loss actually removes attribute information.
- Results on additional training datasets (e.g., CC3M) at varying scales would clarify the method's data sensitivity.

## Removed Points

These points were present in the input reviews but have been removed from the main assessment with justification:

- **"Fatal comparison confound" framing** — The harsh critic framed the training data difference as a structural fatal flaw undermining the core claim. However, the paper's contribution explicitly includes the *ability* to train on larger unannotated datasets as a design achievement (lines 32–33: "Thanks to our annotation-free debiasing pipeline, SANER is designed to be compatible with any dataset of image-text pairs"). The confound is real and worth flagging, but it is not fatal and does not invalidate the paper's contribution. Demoted to Major.
- **"Equidistance loss has no theoretical connection to attribute removal"** — The claim that "being equidistant in cosine similarity does not entail the absence of attribute information" is speculative reasoning about hypothetical failure modes, not a verified flaw in the paper's specific results. The approach (enforcing equal similarity to attribute-group prototypes) is a standard fairness technique; the missing empirical diagnostic is the real issue. Removed as speculation, replaced with minor weakness about missing validation.
- **"Word list requirement means SANER is not annotation-free"** — This conflates task-level image annotations (which the method genuinely avoids) with general-purpose lexical resources. The word lists are a weaker and more reusable resource than per-image annotations. Removed as over-strict framing; the paper is transparent about the word lists.
- **"Missing appendix content"** — Removed per rules: the parser strips supplementary material from all papers; its absence in the text is not a paper flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the familiar tension between claiming a method's inherent superiority and the real-world advantage of being able to train on more (unannotated) data. This is a general issue in the fairness literature and not a novel insight specific to this paper.

## Suggestions

1. **Clarify the inference procedure**: State explicitly whether (a) the debiasing layer is only applied to attribute-neutral text, (b) whether the residual connection is used at inference, and (c) how attribute-specific prompts (e.g., "female doctor") are handled. Provide pseudocode or algorithm box if needed.

2. **Add a controlled comparison**: Train SANER on a FairFace-scale subset of COCO (≈11K samples) and compare against prompt tuning on the same data. Alternatively, augment prompt tuning to use COCO captions. This would isolate the method's contribution from the data advantage.

3. **Add a linear probe diagnostic**: Train a classifier to predict the protected attribute from debiased features, comparing against original CLIP features. This would empirically validate that the equidistance loss actually removes attribute information.

4. **Report confidence intervals or error bars** for the retrieval MaxSkew results, and add a significance test (e.g., bootstrap) for the generation SP results where confidence intervals overlap.

5. **Move a summary of the ablation study** (loss components, training data size sensitivity) into the main paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>