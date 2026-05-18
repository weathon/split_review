Now I have a thorough understanding of the paper. Let me compose my consolidated final review.

---

## Summary

This paper introduces CLIBD, a multimodal contrastive learning framework that aligns insect images, DNA barcodes, and taxonomic text into a shared embedding space. The core idea — using DNA barcodes as an alignment target for image representations — is novel and practically motivated. On the BIOSCAN-1M dataset, the I+D+T model improves image-to-image species-level macro harmonic mean accuracy from 6.27% (unimodal) to 52%, establishes cross-modal image-to-DNA retrieval, and consistently shows that DNA outperforms text as an alignment target.

## Strengths

1. **Substantial quantitative improvement from multimodal alignment.** Within-dataset comparisons (Table 1) show aligning images with DNA yields dramatically higher species-level classification accuracy than unimodal image-only baselines (6.27% → 52% macro H.M.). This directly supports the paper's central thesis.

2. **DNA consistently outperforms text as an alignment target.** The I+D model consistently beats the I+T model at all taxonomic ranks (Section 5.1). This is the cleanest evidence for the paper's core claim and is not confounded by the data leakage issue since both conditions share the same training data.

3. **First demonstration of image-to-DNA cross-modal retrieval.** The paper shows that after contrastive alignment, image queries can be matched against DNA references with meaningful accuracy (Section 5.1), whereas without alignment performance is near chance. This demonstrates a capability no existing method provides.

4. **Practical two-stage IS+DU classification strategy.** The simple nearest-neighbor-based approach (image seen + DNA unseen) outperforms Bayesian zero-shot learning on unseen species (Table 5, Section 5.4), showing the learned embedding space is immediately useful without complex post-hoc models.

5. **Effective transfer to an independent dataset.** On the INSECT dataset (Table 6, Section 5.4), CLIBD's embeddings match or exceed strong baselines without target-domain fine-tuning, validating generality beyond the training distribution.

## Weaknesses

### Major

1. **Data leakage from unlabelled records undermines the zero-shot claim for unseen species.** The paper states (Line 154): "All records without species labels are used in contrastive pretraining." The unseen-species split is defined only on records that *have* species labels. However, unlabelled records — which form the vast majority of BIOSCAN-1M — could easily include specimens from species that later appear in the unseen test set. During contrastive pretraining, the model sees (image, DNA) pairs from those species, learning their cross-modal correspondences without ever seeing their species label. At test time, when asked to retrieve the correct species for an unseen query by matching against DNA keys from the same species, the model has already learned to associate that species' images with its DNA. This is transductive in nature, not true zero-shot generalization as commonly understood. The paper does not discuss this issue, nor does it assess how much of the reported unseen-species accuracy depends on it. This weakens the core generalization claims. **Impact:** The relative comparisons (I+D vs I+T) are unaffected by this issue, but the absolute zero-shot numbers and the novelty of generalizing to "unseen" species are substantially less clean than presented.

2. **Vague and unsubstantiated quantitative claim in the abstract.** The abstract states: "Our method surpasses previous single-modality approaches in accuracy by over 8% on zero-shot learning tasks." No such figure is clearly substantiated anywhere in the paper. The main within-paper comparison (I+D+T at 52% vs I-only at 6.27%) shows a ~46% absolute improvement, not 8%. The BioCLIP comparison involves a two-modality model (I+T), not a single-modality one. The "over 8%" figure is not traceable to any specific row or column in any table. This claim must either be replaced with a specific, traceable number or removed.

### Minor

3. **BioCLIP comparison is not well-controlled.** Table 3 compares CLIBD (trained only on BIOSCAN-1M) with BioCLIP (trained on TreeOfLife-10M, a much larger and more diverse dataset). The paper acknowledges (Line 208) that BioCLIP "may perform worse on insects as it was also trained on non-insect domains," which means the comparison conflates architecture/method with training data composition. The useful evidence for CLIBD's contribution already exists in the within-paper ablations (I vs I+T vs I+D vs I+D+T). The BioCLIP comparison could be demoted or reframed as demonstrating the value of domain-specific pretraining.

4. **Attention visualization analysis is superficial.** Section 5.3 states (Line 226) "the attention is more clearly focused on the insect" for correctly predicted examples, but this is purely qualitative with no quantitative backing. It does not demonstrate how the aligned model differs from the unaligned baseline in any meaningful way, nor does it connect to the paper's central claim about DNA improving representations. This section adds little.

5. **"Zero-shot" is used for multiple distinct settings without clear separation.** The paper uses "zero-shot" to mean: (a) retrieval-based classification without fine-tuning, (b) classifying species entirely unseen during contrastive training, and (c) BZSL on the INSECT dataset. These are different capabilities and should be kept distinct. The main BIOSCAN-1M unseen evaluation (setting b) is the most interesting; the term should be reserved for that.

6. **Incomplete/placeholder text in the manuscript.** Lines 140 and 224 contain unfinished LaTeX markers (`\ming{update ...}`, `\TODO{say a few words ...}`), indicating the manuscript was not fully polished before submission.

### Trivial

- Some key results (Tables 1 and 3) are reported as single numbers without confidence intervals or variance estimates. Given long-tailed data and randomness in contrastive training, this is a minor concern — but it does not threaten the core claims.

## Nice-to-Haves

- **Ablation on the effect of training on unlabelled records.** The single most informative additional experiment would be to train a model using *only* records with species labels (~9% of the data) and evaluate on the same unseen split. This would isolate the contribution of unlabelled data and directly address the data leakage concern. If the relative improvements (I+D vs I+T) hold under this stricter setting, the contribution is clean and strong.
- **Clarify text encoder training details.** The paper says text is "concatenated...up to known labels" (Line 160). It would help to specify: what does the text string look like when only order is known? Is the text encoder frozen or fine-tuned? How is the contrastive loss computed when text embeddings are poor due to missing labels?
- **Replace "over 8%" with a specific, traceable number** tied to a concrete row and column in a specific table.

## Removed Points

- None of the harsh critic's criticisms were factually wrong or based on a misunderstanding of the paper. All points were verified against the paper body and, when adjusted for severity, are maintained in the appropriate tier above.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a deeper tension: the paper sells its contribution under a "zero-shot" framing drawn from the CLIP literature, but the evaluation setting is closer to transductive or few-shot learning because unlabelled cross-modal pairs from "unseen" species leak into contrastive pretraining. This is not unique to this paper — many biology+ML papers face a version of this problem when working with partially labelled datasets — but it highlights that the field needs a clearer vocabulary for what "unseen" means when the supervisory signal is the cross-modal correspondence itself, not the class label. The paper's most robust result (DNA > text as alignment target) does not depend on the zero-shot framing and would likely survive a stricter split, but the paper overclaims its generalization story.

## Suggestions

1. **Address data leakage head-on.** Re-run unseen-species evaluation with a strict split that excludes all records (labelled *and* unlabelled) of unseen species from training. If results hold, the claim is much stronger. If they degrade, transparently report and discuss what the transductive setting actually demonstrates.
2. **Pin the abstract number** to a specific comparison (e.g., "I+D+T achieves X% vs I-only Y%, an improvement of Z percentage points on unseen species").
3. **Reframe or remove the BioCLIP comparison** from the main narrative, since the paper's own ablations already carry the argument. A single within-dataset I+T baseline on the same data is sufficient.
4. **Distinguish the three uses of "zero-shot"** explicitly in Sections 4–5.

## Score and Decision

**Originality:** Good — using DNA barcodes as an alignment target for image representations via contrastive learning is novel and well-motivated.  
**Importance of research question:** High — scalable biodiversity monitoring is an important and under-addressed application.  
**Whether claims are well supported:** Mixed — the core claim (DNA > text) is well supported, but the zero-shot generalization claim is weakened by the data leakage issue, and the abstract contains an unsubstantiated number.  
**Soundness of experiments:** Generally thorough within-dataset, but the data split methodology has a structural flaw that needs addressing.  
**Clarity of writing:** Competent but contains unfinished markers and overloading of "zero-shot."  
**Value to the community:** Potentially high — the method and embedding space could be useful for biodiversity research, and the idea of using DNA as a modality for representation learning is worth pursuing.

The paper makes a real contribution, and none of the weaknesses are fatal: the relative comparison of I+D vs I+T — the cleanest evidence for the core claim — is unaffected by the data leakage concern. However, the paper oversells its zero-shot generalization, and the data leakage issue must be transparently addressed before acceptance. The unsubstantiated abstract claim must also be fixed.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>