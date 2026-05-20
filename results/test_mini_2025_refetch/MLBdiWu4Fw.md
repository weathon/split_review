Now I have enough information for calibration. Let me write the final review.

## Summary

InternVid presents a large-scale video-text dataset comprising 7.1 million YouTube videos (760K hours, 234M clips) with automatically generated captions produced via a multiscale pipeline that combines fine-scale frame-level captioning (Tag2Text) with coarse-scale middle-frame captioning (BLIP2), summarized by a language model. The paper also introduces ViCLIP, a ViT-L based video-text contrastive model trained on InternVid, and demonstrates the dataset's utility across action recognition, video retrieval, text-to-video generation, and video-centric dialogue. The core contributions are the dataset itself and the validation that large-scale, high-correlation video-text data enables transferable video-language learning.

## Strengths

1. **Dataset scale and construction quality.** InternVid is one of the largest publicly described video-text datasets at 7.1M videos / 234M clips, with a clear and reproducible multiscale captioning pipeline (Figure 2). The use of LLM-synthesized captions rather than noisy ASR transcripts is validated by both qualitative examples (Figure 1) and quantitative retrieval improvements (Tables 4–5). The paper also provides computed video-text similarity and aesthetic scores for every clip, enabling users to construct task-specific subsets.

2. **Strong zero-shot action recognition results.** ViCLIP trained on InternVid-10M-FLT achieves 64.8% top-1 / 75.7% average on Kinetics-400, outperforming both CLIP variants and EVA-CLIP-E (Table 2). This directly validates the paper's central claim that high-correlation video-text data at moderate scale can yield transferable representations competitive with image-only models trained on orders-of-magnitude more data.

3. **Data scaling shown to benefit fine-tuned performance.** Unlike the zero-shot case, fine-tuned action recognition (Table 3) improves monotonically from 10M (86.8% K400) to 200M (87.9% K400) and on Something-Something V2 (71.2% → 73.6%), demonstrating that the full dataset provides value beyond the filtered subsets when used for fine-tuning.

4. **Breadth of validation across tasks.** The paper validates InternVid on five retrieval benchmarks (zero-shot and fine-tuned), text-to-video generation (Table 6), and video-centric dialogue (Table 7), showing the dataset's applicability beyond standard recognition tasks.

## Weaknesses

### Fatal
None.

### Major

1. **False-negative problem limits the raw dataset's utility for contrastive learning, and the paper does not resolve it.** The paper's own results (Table 2) show that training on the full InternVid-200M (59.80% K400) *underperforms* the much smaller InternVid-10M-FLT (64.80%) and InternVid-10M-DIV (63.00%) for zero-shot action recognition. The paper acknowledges this (p. 214: "we conjecture that false negative samples could severely impede video-text contrastive learning if we don't purposefully reduce the number of clips taken from the same video") but does not provide a principled solution, quantify how many clips per video create false negatives, or release a recommended sampling strategy. A user downloading the full 234M-clip dataset for contrastive learning would face the same problem the authors identified but did not solve. This weakness is structural: the dataset's headline scale claim is partly at odds with its demonstrated best use.

2. **Text-to-video generation experiment has a confound that prevents attribution.** Table 6 compares a baseline trained on WebVid10M alone against one trained on WebVid10M + InternVid-Aes-18M (aesthetic-filtered subset). The improvement (FVD 705.25 → 616.51) could come from (a) the aesthetic filter, (b) the caption quality, or (c) simply having 28M vs 10M data points. No ablation adds a matched-volume random sample from unfiltered InternVid or controls for data quantity. Since the baseline itself underperforms VideoCrafter and VideoFusion (both trained on WebVid10M alone), the gain may partly reflect the baseline's low-data saturation rather than InternVid-specific quality. The claim "InternVid improves existing text-to-video generation models" (p. 44) is too strong without this control.

### Minor

3. **Zero-shot action recognition framing could be more precise.** The paper states that ViCLIP achieves "state-of-the-art zero-shot action recognition" (p. 49). This is true for the *filtered subset* (InternVid-10M-FLT), not the full dataset, and the comparisons are primarily against image-only CLIP/EVA-CLIP models. The only video-based contrastive baseline is ViCLIP trained on WebVid10M. Including another video-text model (e.g., VideoCLIP) would strengthen the comparison. The current framing is not misleading but could create unwarranted expectations about the raw dataset.

4. **Subset definitions (DIV, FLT) are underspecified in the main text.** The paper evaluates on InternVid-10M-DIV and InternVid-10M-FLT but does not explain what "DIV" (diverse) and "FLT" (filtered) mean, what thresholds were used for UMT-SIM or aesthetic scores, or how diversity was enforced. A reader of the main text cannot reproduce these subsets without relying on the appendix (which is stripped from this version but exists in the original). At minimum, the main text should specify the filtering criteria.

5. **Dialogue evaluation is preliminary.** Table 7 reports modest improvements on a 5-point scale (2.29 → 2.64 average) without inter-rater agreement, confidence intervals, or multiple seeds. The evaluation benchmark is cited but not described. The paper appropriately describes this as preliminary (p. 302: "qualitative evaluations demonstrate"), but the corresponding claim in the introduction (p. 49: "fosters the development of multimodal dialogue systems") is somewhat overstated relative to the evidence.

### Trivial
None.

## Nice-to-Haves

- A human evaluation study of caption quality (fluency, relevance, temporal coherence) compared to WebVid10M alt-text and ASR-based datasets would strengthen the claim that generated captions are semantically superior.
- A brief limitations section discussing YouTube sourcing biases (language skew, content skew) and reliance on automated caption models (Tag2Text, BLIP2) that may hallucinate would contextualize the dataset's scope.
- The paper could release recommended clip-per-video ratios or a deduplication strategy for contrastive learning users.

## Removed Points

- **"Missing related works" and specific dataset comparisons (Porav et al., 2023):** Removed per instruction: I cannot verify that these works exist or are relevant without external sources, and I should not mention missing related works.
- **Formatting/style nitpicks about presentation:** Removed per instruction.
- **Reproducibility concerns about hyperparameters or trivial implementation details:** Removed per instruction (these are parser artifacts or standard details not required in a dataset paper).
- **"VideoCLIP not included as baseline":** The harsh critic's claim that video-based models like VideoCLIP are missing is noted but the paper does compare to ViCLIP trained on WebVid10M (a video-text model), and the primary comparison to image-only models is justified because the paper aims to show video-level training bridges the image-to-video gap. This point is demoted from Major to Minor (point 3 above) since the comparison to WebVid10M already provides a meaningful video-based baseline.
- **"False negative issue means effective useful size is closer to 10M":** The critic overstates this — fine-tuned results (Table 3) show clear scaling benefits at 200M (87.9% vs 86.8%). The false-negative problem is specific to the zero-shot contrastive learning setting and does not generalize to all uses of the dataset. Retained as Major (point 1) but with appropriate scope.
- **Strength Finder's generic strengths ("important problem," "addressed a meaningful issue"):** Removed per instruction — these are superficial and not specific to the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the false-negative issue head-on.** Release a recommended subset (e.g., at most K clips per video) alongside the raw data, or provide a principled sampling strategy so users can directly benefit from the full scale without reinventing the filtering strategy. This would significantly raise the dataset's practical value.
2. **Add the missing ablation for text-to-video generation.** Compare WebVid10M + 18M random InternVid clips (unfiltered) and WebVid10M + 18M InternVid clips filtered only by caption quality (not aesthetics) against the reported WebVid10M + InternVid-Aes-18M. This would clarify whether the improvement is from data quantity, aesthetic quality, or caption quality.
3. **Clarify DIV/FLT construction criteria in the main text.** Specify the UMT-SIM similarity thresholds, aesthetic score thresholds, and diversity enforcement mechanism so readers can reproduce these subsets without consulting the appendix.
4. **Add confidence intervals or multiple seeds** to the key experimental tables (especially Tables 2 and 7) to assess significance of observed improvements.

## Calibration

| Anchor Paper | Path | Avg Score | Round | Comparison to InternVid |
|---|---|---|---|---|
| VideoGPT+ | /home/wg25r/review_agent/human_reviews/YGWxpOI6Y0.md | 3.40 | 1 | Much weaker; less coherent methodology and lower impact. |
| Enhancing Video Understanding (VLMs) | /home/wg25r/review_agent/human_reviews/yspBoIZJ9Z.md | 4.75 | 1 | Weaker; marginal technical improvements and unclear contributions. |
| DTVLT Benchmark | /home/wg25r/review_agent/human_reviews/ydH8nU5csJ.md | 4.60 | 1 | Weaker; smaller contribution and more limited validation. |
| CinePile Dataset | /home/wg25r/review_agent/human_reviews/RW7Z1W1Hux.md | 5.33 | 2 | Slightly weaker; comparable as a dataset paper but less thorough validation of representation learning. |
| LanguageBind | /home/wg25r/review_agent/human_reviews/QmZKc7UZCy.md | 6.50 | 2 | Comparable. LanguageBind had a more novel N-modality method but smaller dataset (VIDAL-10M). InternVid has larger scale but a standard contrastive baseline. Overall similar contribution level. |
| Demystifying CLIP Data | /home/wg25r/review_agent/human_reviews/5BCFlnfE1g.md | 6.75 | 2 | Slightly stronger. More tightly controlled evaluation and clear data curation insights, though narrower scope (images only). |
| MOFI | /home/wg25r/review_agent/human_reviews/QQYpgReSRk.md | 6.25 | 2 | Comparable. Both are large-scale dataset + pretraining contributions with similar evaluation breadth and similar criticism about technical novelty. |
| Multi-granularity Correspondence (Norton) | /home/wg25r/review_agent/human_reviews/9Cu8MRmhq2.md | 8.00 | 1 | Significantly stronger. Novel method (optimal transport for noisy correspondence), rigorous theory, and extensive evaluation across multiple tasks. |
| MMIE Benchmark | /home/wg25r/review_agent/human_reviews/HnhNRrLPwm.md | 8.00 | 1 | Significantly stronger. Comprehensive benchmark with meticulous curation and broad evaluation scope. |

**Bracket (Round 1):** The paper sits between weak anchors (~2-3.5) and strong 8.0 anchors. Narrowest plausible range: 5.0–7.0.

**Narrowing (Round 2):** Compared against LanguageBind (6.5), Demystifying CLIP (6.75), and MOFI (6.25), InternVid is most similar in contribution type and quality to LanguageBind and MOFI. It has a larger dataset than LanguageBind but a less technically novel method. It has the false-negative issue that neither LanguageBind nor MOFI face, which limits the raw dataset's value for contrastive learning. Score: **6.0** is the most appropriate — a solid, impactful dataset contribution with addressable weaknesses that prevent it from reaching the excellent (7+) tier.

**Final Score: 6.0 — Accept.** The dataset is large-scale, well-constructed, and validated across multiple tasks. The weaknesses (false-negative issue, confounded generation experiment, underspecified subsets) are real but addressable through additional analysis and reporting. The work will be a valuable community resource.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>