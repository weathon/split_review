I have thoroughly verified every claim against the paper. Here is the consolidated review.

---

## Summary

This paper introduces SketikZ, a dataset of 3,231 pairs of hand-drawn sketches (collected via paper, whiteboard, and tablet from 28 annotators) paired with reference diagram images and TikZ code, addressing the near-total absence of real-world data for sketch-to-vector-diagram conversion. Alongside the dataset, the paper presents ImgTikZ, a 6.7B-parameter vision-language model built on DeepSeek Coder and SigLIP (following the LLaVA 1.5 architecture), fine-tuned with two data augmentations—synthetic code variants (AugTikZ) and image-level noise (ImgAugTikZ)—and a multi-candidate inference strategy with a diagram-specialized selector (D-SigLIP). Experiments show that ImgTikZ achieves competitive subjective scores (Alignment, Quality) with GPT-4o while being substantially smaller, though all models still struggle significantly on the task.

## Strengths

- **SketikZ dataset is a genuine, well-constructed contribution.** Section 3.2 describes a principled three-stage pipeline (rendering from DaTikZ, filtering to five structural diagram categories via ACL-Fig labels, and sketch annotation by 28 annotators using paper/whiteboard/tablet) resulting in 3,231 paired samples (2,585/323/323 train/val/test). The dataset explicitly targets real-world noise conditions (varied lighting, backgrounds, hand-drawn distortions) that prior diagram datasets lack.

- **Thorough ablation studies cleanly isolate each contribution.** Tables 3–6 systematically remove SketikZ training data (Table 3), AugTikZ (Table 4), ImgAugTikZ (Table 4), and compare rendered vs. sketch inputs with and without image augmentation (Table 5). Each ablation produces measurable performance degradations (e.g., ImageSim drops from 0.732 to 0.672 without AugTikZ; CharSim drops from 0.426 to 0.388), providing clear evidence that each component earns its place.

- **D-SigLIP selector is validated as superior to general-purpose CLIP.** Figure 8 demonstrates that D-SigLIP continues to improve ImageSim beyond 5 candidates (reaching ~0.55 at K=20), whereas CLIP plateaus after 5 candidates. This is a concrete, reusable finding for image-to-code tasks where candidate ranking matters.

- **Rigorous subjective evaluation with documented reliability.** Section 5.2 specifies a 5-point scale for alignment and quality, uses 40 annotators with three median scores per instance, and reports Krippendorff's α of 0.761 (alignment) and 0.662 (quality)—substantial-to-moderate agreement, which is transparent and credible.

- **The paper convincingly establishes that the task is hard for all current models.** Even Claude 3.5 Sonnet achieves an average Alignment score of only ~3.3/5, and ~38% of its outputs score below 3 on Quality. This motivates SketikZ as a meaningful future benchmark rather than a solved dataset.

- **Analysis of performance variation across sketch tools (Table 6).** Paper and whiteboard sketches show 7.2% ImageSim drops and 14–28% CharSim drops vs. rendered inputs, while tablet sketches degrade only 0.5%—a concrete diagnostic that informs real-world deployment priorities.

## Weaknesses

### Fatal
None. The two issues below are significant but addressable; neither invalidates the dataset contribution or the core findings about task difficulty.

### Major

- **Asymmetric comparison setup inflates the headline "comparable to GPT-4o" claim.** ImgTikZ-MCG generates K=20 candidates and selects the best via D-SigLIP, while all baseline models (GPT-4o, Claude 3.5, GPT-4o mini, LLaVA-Next) use iterative generation with a maximum of 5 attempts (Section 6, line 137). This is a 4× inference budget advantage for ImgTikZ-MCG. The paper does report ImgTikZ-IG (5 attempts, matching the baseline budget) alongside MCG, so a fair comparison exists within Table 2. However, the text repeatedly foregrounds MCG results when claiming competitiveness (e.g., "ImgTikZ-MCG achieved comparable performance to GPT-4o on the Alignment score," Section 7.1), without explicitly calibrating readers to the asymmetric budget. **Why it matters:** A reader evaluating whether the model itself is strong (vs. the multi-candidate strategy being strong) cannot disentangle the two from the current presentation. The paper should report ImgTikZ-MCG with K=5 alongside K=20, so the benefit of scaling candidates is separated from the head-to-head comparison.

- **D-SigLIP serves dual roles as both the MCG selector and the ImageSim evaluation metric, creating a potential bias.** D-SigLIP is fine-tuned on noise-augmented diagram pairs from RenderTikZ and AugTikZ (Section 4.3, line 99)—the same data distributions used to train ImgTikZ. It is then used as (a) the selector that picks the best candidate in MCG (Section 4.3) and (b) the ImageSim metric that evaluates *all* models (Section 5.1, line 115). This creates a risk that D-SigLIP's embedding space is better aligned with ImgTikZ's output distribution than with GPT-4o's or Claude's, potentially inflating ImgTikZ's ImageSim scores relative to competitors. The paper notes that CLIPScore showed lower correlation with human evaluations (line 115), which explains why D-SigLIP was chosen but does not resolve the fairness concern. **Why it matters:** The ImageSim metric is the main automatic metric where ImgTikZ-MCG leads (Table 2 text). Without validation that D-SigLIP does not favor ImgTikZ outputs, the ranking on this metric is uncertain. The paper should report ImageSim using a held-out, independently-trained encoder (or original CLIP as a secondary check) and show that relative model rankings hold.

### Minor

- **No confidence intervals or variance reported for any automatic metric.** The test set has 323 samples, which is large enough for meaningful bootstrap confidence intervals. Without them, it is impossible to assess whether differences like ImgTikZ-MCG vs. Claude 3.5 on ImageSim (0.775 vs. second-best, reported in text) are statistically reliable.

- **Inference cost of multi-candidate generation is not reported.** The paper states K=20 candidates are generated per test sample, but does not report total generated tokens, wall-clock time, or compute cost. Since the strategy is presented as a contribution, knowing its cost relative to iterative generation (5 attempts) is important for practitioners deciding whether the gain justifies the expense.

- **Limited discussion of whether GPT-3.5-augmented TikZ code (AugTikZ) produces semantically valid diagrams.** Section 4.1 describes using GPT-3.5 to fix compilation errors and modify diagrams, but does not analyze whether the altered code corresponds to a reasonable diagram of the same type or introduces hallucinations. Since ImgTikZ is trained on this augmented data, understanding the quality of the training signal matters.

### Trivial
None.

## Nice-to-Haves

- **Breakdown of model errors by diagram category** (Tree vs. Graph vs. Architecture vs. Neural Network vs. Venn Diagram). This would give insight into which spatial/structural configurations are hardest and would strengthen the benchmark message.
- **Qualitative analysis of representative failure modes** (missing elements, misaligned shapes, garbled text) with examples from best and worst generations.
- **Implication of the data augmentation strategy for non-TikZ image-to-code tasks** could be discussed briefly, since the GPT-3.5-based code augmentation (no image processing needed) is a potentially general technique.

## Removed Points

These points were flagged by reviewers but are removed with brief justification:

- "The paper claims the concurrent work lacks TikZ code for sketches—should be more specific." *Removed:* The paper's statement about (Belouadi et al., 2024) is specific enough for a related-work comparison; the existence and content of that dataset are the authors' responsibility to characterize, not a weakness to be interrogated in review.
- "The dataset is small for training from scratch." *Removed:* The paper uses it as a fine-tuning benchmark, which the critic acknowledges as acceptable. This is not a weakness.
- "D-SigLIP training details are insufficient (how many pairs, held-out validation)." *Removed:* The paper describes the training method (contrastive learning, noise-augmented pairs from RenderTikZ and AugTikZ). Additional details would be nice but the description is adequate for the paper's scope.
- "AugTikZ procedure described briefly." *Demoted:* Already captured as Minor weakness above. The core concern (semantic validity of augmented code) is kept; the brevity complaint is a formatting preference.

## Novel Insights

The two critical reviews converge on a pattern worth noting: the paper's strongest claims (model performance, metric validity) depend on components (D-SigLIP, multi-candidate inference) whose evaluation advantages are not fully disentangled from their design advantages. D-SigLIP is simultaneously the *tool that makes MCG work* and the *ruler that measures success*—and both are trained on the same data as the model. This entanglement is the paper's most important unresolved tension. A second insight: the asymmetric comparison (20 candidates vs. 5 attempts) is a common pitfall in papers introducing inference-time scaling techniques. The authors could cleanly resolve it by reporting a matched-budget baseline (K=5 MCG), which would also quantify the marginal return of scaling from 5 to 20 candidates—a result that would strengthen rather than weaken the paper.

## Suggestions

1. **Add a direct head-to-head experiment:** Report ImgTikZ-MCG with K=5 (matching the 5-attempt budget of baselines) alongside the K=20 result. This separates the model contribution from the inference-scaling contribution and makes the "comparable to GPT-4o" claim interpretable.
2. **Validate D-SigLIP as an evaluation metric** by computing ImageSim with an independently-trained encoder (e.g., standard CLIP with matched prompting, or a D-SigLIP variant trained on a held-out diagram source not used for ImgTikZ training). Show that relative model rankings are unchanged.
3. **Report 95% bootstrap confidence intervals** for all automatic metrics (ImageSim, CodeSim, CharSim, CSR_avg) to establish statistical reliability of the reported differences.
4. **Report the inference cost** of MCG (total generated tokens per test sample, or wall-clock time) so readers can evaluate the cost-performance trade-off.
5. **Provide a brief quality analysis of AugTikZ output** (e.g., human-rated validity of a random sample of 100 augmented diagrams) to assure readers that the augmented training data is semantically reasonable.

## Score and Decision

The SketikZ dataset is a solid, well-constructed contribution to an underexplored task, and the paper provides thorough ablations and a defensible baseline model. The two major weaknesses (asymmetric comparison and potential metric circularity) are real but fixable—they weaken specific claims about model competitiveness but do not undermine the dataset contribution or the finding that the task remains difficult for all current VLMs. The paper should be accepted provided the authors address these concerns.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>