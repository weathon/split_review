Now I have thoroughly verified the paper. Let me compose the final meta-review.

## Summary

This paper investigates compositionality failures in text-to-image diffusion models. It identifies two error sources in CLIP-based conditioning: (1) erroneous attention contributions in CLIP's internal layers (minor), and (2) sub-optimality of CLIP's output text-embedding space for compositional prompts (major). The paper proposes WiCLP (Window-based Compositional Linear Projection), a simple linear projection applied to CLIP's output embeddings, trainable on a small set of compositional image-text pairs while keeping the UNet frozen. The method also introduces SWITCH-OFF, a time-step threshold that disables the projection in later inference steps to balance compositionality gains against FID degradation.

## Strengths

1. **Diagnostic decomposition of error sources.** The paper systematically separates two distinct sources of compositionality failures — internal attention errors in CLIP (quantified at ~2.93% VQA improvement via hand-crafted attention reweighting, Section 3.2) and output-space misalignment of CLIP embeddings (dramatically larger gains, Figure 5). This decomposition is directly supported by quantitative evidence across 780 color and 582 texture prompts, and it usefully informs the design of subsequent methods.

2. **WiCLP is a parameter-efficient and plausible method.** Training only a window-based linear projection (~(2s+1)d × d parameters, s=2) on CLIP's output space, with all other components frozen, is computationally attractive. The paper reports VQA improvements of 16.18%, 15.15%, and 9.51% on SD v1.4 and 14.35%, 11.14%, and 6% on SD v2 across color, texture, and shape categories (Table 1). The cross-attention map evidence (Figure 8) provides a mechanistic link between the projected embeddings and improved generation.

3. **SWITCH-OFF addresses a real trade-off.** The observation that applying the projection at all time steps degrades FID, and that switching it off in later steps (τ=800) can recover clean accuracy while preserving compositional gains, is practically useful. The trade-off analysis (Figure 7) offers a concrete mechanism that prior fine-tuning baselines lacked.

4. **Multi-faceted evaluation.** The paper evaluates across three compositional categories, two SD versions, and four baselines (Composable Diffusion, Structured Diffusion, Attn-Exct, GORS), reporting both VQA and FID.

## Weaknesses

### Fatal
None.

### Major

1. **Unsupported FID claim — base FID is not reported.** The abstract claims compositional improvements "without harming the model's FID score," but the paper never reports the base SD 1.4 / SD 2 FID on the same MS-COCO subset. The only FID numbers given are WiCLP=27.40 and GORS=30.54 (line 218). The paper's own body acknowledges "Our method causes a slight increase in FID score on MS-COCO prompts compared to base models" (line 218), which already contradicts the abstract's categorical "without harming." With SWITCH-OFF, the paper states it "achieves a competitive FID similar to that of the clean model" (line 197), but the clean model's FID is never provided numerically. This makes the central FID-preservation claim unverifiable and internally inconsistent with the body's more cautious language. The authors must report base FID for the same evaluation setup.

2. **Training data curation ambiguity — possible train/evaluation overlap.** The paper states that T2I-CompBench "provides distinct training and evaluation splits for each category" (line 67), which is a clear acknowledgment of their existence. However, the curation procedure (generating images from three models and selecting top-30 VQA images per prompt) is described for "each prompt" without specifying whether this was applied only to the training split or to all 1,000 prompts spanning both splits. If images generated from evaluation-set prompts were used in training, this constitutes data leakage that would inflate VQA scores. This ambiguity needs explicit resolution.

3. **Missing error bars and confidence intervals across all experiments.** No VQA scores or FID values come with error bars, standard deviations, or confidence intervals. Given the small dataset size (1,000 prompts across three categories), per-prompt variance could be substantial, and the reported improvements may have high variance. The absence of any uncertainty quantification makes it hard to assess whether the gains are robust.

### Minor

4. **Human evaluation is insufficiently documented.** The paper reports only a single statistic (34.625% base, 51.875% WiCLP, 13.5% equal) with no information about the number of participants, number of trials, prompt selection, randomization procedure, or confidence intervals. While the main results are quantitative (VQA scores), the human study as reported provides negligible evidentiary weight and should either be fully documented or omitted.

5. **SWITCH-OFF threshold τ is not systematically justified.** The threshold τ=800 is chosen with only a single figure (Figure 7) showing the trade-off on a randomly sampled subset. No analysis of τ sensitivity across different prompt categories or evaluation splits is provided, and no variance is shown for the plotted FID/VQA values.

6. **No ablation of the top-30 curation.** The paper selects the top-30 VQA images per prompt for training, which introduces a strong selection bias toward images that already score well on VQA. Without an ablation using random subsets or all generated images, it is unclear how much of the improvement comes from the projection versus the curated training data.

### Trivial
None.

## Nice-to-Haves

- An analysis of what the learned linear projection actually encodes (e.g., its rank, changes in cosine similarity between attribute-object embeddings) would deepen the contribution beyond a black-box method.
- Testing on additional diffusion architectures (e.g., SDXL) would strengthen claims of generality.
- Per-prompt variance of VQA scores (e.g., violin plots or distributional summaries) would help assess robustness.

## Removed Points

These points are flagged for removal; treat them with caution:

- **Criticism that attention reweighting analysis is "disconnected" from the main method (Harsh Critic Point 5).** The paper explicitly states that the attention analysis identifies a *minor* error source (Section 3.2: "it is not the primary error source"), and WiCLP addresses the separately-identified *major* error source (output space sub-optimality). The analysis serves to contextualize the relative importance of two error sources and is not meant to directly motivate WiCLP's design. This is a clear case of the reviewer misunderstanding the paper's narrative structure.

- **Criticism that the optimized-embedding experiment is circular / doesn't demonstrate sub-optimality (Harsh Critic Point 3).** The experiment is a standard diagnostic: optimizing embeddings to minimize denoising loss on a fixed image set yields embeddings that produce higher-VQA images. This legitimately demonstrates that a better embedding space exists than CLIP's default output space. It does not claim to validate the *linear* projection design — that is done separately in Section 5. The reviewer's objection confuses the diagnostic purpose of the experiment with a claim it never makes.

- **The reviewer's speculation about "typical FID of SD 1.4 on MS-COCO is far below 27.4 (often ~12-15)"** is a generic claim not tied to the specific subset, sampling procedure, and number of samples used in this paper. FID is highly sensitive to these choices. The valid criticism (which we keep) is simply that the base FID is not reported.

- **Generic formatting/style nitpicks** from the section-by-section notes (e.g., about the abstract's phrasing being "overstated" — this is better captured by the concrete FID omission above).

## Novel Insights

None beyond the paper's own contributions. The reviews largely corroborate the paper's framing rather than adding novel cross-cutting observations.

## Suggestions

1. Report the base model's FID on the *same MS-COCO subset and sample count* used for WiCLP and GORS, so readers can directly verify the "no harm" / "competitive FID" claim. Clarify whether the abstract's "without harming" claim refers to the full-projection or SWITCH-OFF configuration.

2. Explicitly state whether the image curation procedure (top-30 VQA selection from three models) was applied only to the training split of T2I-CompBench or to all prompts. If done on all prompts, report a version where only training-split prompts contribute to the training set.

3. Add error bars (e.g., bootstrapped confidence intervals over prompts) for the main VQA and FID results.

4. Ablate the top-30 curation by training WiCLP on a random subset of generated images (or all images) and reporting the resulting VQA scores.

5. Provide a sensitivity analysis of the SWITCH-OFF threshold τ, ideally broken down by compositional category.

6. Either expand the human evaluation with proper documentation (N participants, trials, prompts, confidence interval) or remove it.

## Score and Decision

The paper makes a useful diagnostic contribution and proposes a lightweight, plausible method. However, the core FID-preservation claim is unverifiable without base FID reporting and is internally inconsistent with the body text. The training/evaluation split ambiguity could potentially inflate results. These issues require author clarification before the contribution can be fully assessed. The paper is borderline — the core idea is sound but the evidence as presented has significant gaps.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>