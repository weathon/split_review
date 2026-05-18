I now have a thorough understanding of the paper and can verify each reviewer claim against the source. Let me produce the consolidated review.

---

## Summary

This paper introduces InternVid, a large-scale video-text dataset of 7.1M videos yielding 234M clips with 4.1B words of captions, generated via a multiscale LLM-based captioning pipeline (Tag2Text + BLIP2 + LLM summarization). It also presents ViCLIP, a ViT-L video-text model trained on InternVid via contrastive learning with masked video modeling. The paper demonstrates the dataset's utility on zero-shot/fine-tuned action recognition, video retrieval, text-to-video generation, and a video-centric dialogue system. The core claim is that InternVid enables learning strong video-text representations at scale while maintaining high video-text correspondence.

## Strengths

1. **Massive-scale, well-characterized dataset with a novel captioning pipeline.** InternVid (7.1M videos, 234M clips) is an order of magnitude larger than WebVid10M in terms of videos and clips, while the multiscale captioning method (frame-level Tag2Text descriptions summarized by an LLM, plus BLIP2-based center-frame captioning) demonstrably outperforms alternatives — Table 7 shows ViCLIP-B trained with InternVid captions beats the same model trained with VideoChat-generated captions on zero-shot retrieval and action recognition, with the *only* variable being the caption quality.

2. **Clear demonstration that data curation (diversity + quality filtering) matters more than raw volume for zero-shot transfer.** 10M-FLT (diverse sampling + top-30% UMT-SIM filtering) decisively outperforms the 20× larger 200M random subset on zero-shot action recognition (K400 top-1: 64.8 vs. 59.8) and zero-shot retrieval across all five benchmarks. The paper honestly identifies and discusses the false-negative hypothesis for this phenomenon, providing a valuable lesson for video-text contrastive learning.

3. **Strong controlled comparisons isolate the dataset's value.** The paper consistently uses the same architecture (ViCLIP) with different data sources, allowing direct attribution of gains to the data. InternVid-10M-FLT surpasses WebVid10M-tuned ViCLIP on zero-shot recognition by ~5 points on K400 top-1, and the caption ablation (Table 7) controls for everything except the captioning method.

4. **Downstream utility in generation and dialogue.** The addition of InternVid-Aesthetics-18M to WebVid10M improves FVD from 705.3→616.5 and removes watermark artifacts. The dialogue experiment (VideoChat with ViCLIP encoder) shows consistent improvements across all five evaluation dimensions over VideoChat with Eva-g.

## Weaknesses

### Major

1. **The scaling narrative is imprecise and in tension with the paper's own best results.** The paper states "increasing the data scale results in significant increases in performance" (Figure 7/8 discussion) — this is only true for *random* subsets (10M→50M→200M). The curated 10M-FLT and 10M-DIV subsets, which are the paper's best-performing configurations, outperform the 200M random set by large margins. The paper acknowledges this discrepancy and proposes a false-negative hypothesis (clips from the same video act as false negatives in contrastive learning), but does not validate it (e.g., by re-sampling 200M with max-one-clip-per-video). This leaves the paper's central narrative about scaling in an unresolved position: the dataset's value is demonstrated most strongly through curation, not raw volume, yet the paper frames scaling as a primary contribution. The core dataset contribution is not undermined, but the framing needs substantial revision.

2. **Unsubstantiated "state-of-the-art" claims due to missing video-text baselines.** Table 1 compares ViCLIP only against CLIP and EVA-CLIP — both image-text models adapted to video via frame averaging. The paper claims "state-of-the-art zero-shot action recognition in Kinetics" (line 36), but does not compare against video-text pretraining models such as UMT, InternVideo, or MERLOT Reserve, which the paper itself cites in related work. Without these comparisons, the SOTA claim cannot be evaluated. The dataset's value can still be demonstrated by showing ViCLIP with InternVid outperforms ViCLIP with WebVid10M (which the paper does), but the SOTA language should be removed or carefully qualified to the setting of image-initialized contrastive models of comparable scale.

3. **Text-to-video generation experiment conflates data quality with data quantity.** The comparison (Table 5) is between a baseline trained on WebVid10M (10M samples) and one trained on WebVid10M + InternVid-Aesthetics-18M (28M samples). The 2.8× increase in training data alone could explain a substantial portion of the FVD improvement (705→617). No control is run with the same quantity of WebVid data (e.g., training on more WebVid samples to match 28M, or training on InternVid-18M alone). This weakens the claim that the dataset's specific properties (actionness, watermark-free content, high correspondence) are the causal factor.

### Minor

1. **The interleaved video-text dataset (InternVid-ICL, §3.4) is described at length but never evaluated.** Section 3.4 presents three formats of interleaved video-text data for in-context learning (analogous to Flamingo), but the dialogue experiment (§4.3) merely replaces the visual encoder in VideoChat without using this interleaved data. The interleaved data remains a promised resource with no demonstrated utility in the paper, which inflates the scope relative to what is validated.

2. **The "AVG" metric (mean of top-1 and top-5) is defined only in the appendix** (line 597), not in the main paper where it appears in Table 1 and the introduction's SOTA claim. This is unusual and makes it harder for readers to interpret the headline numbers. The introduction (line 36) says "with the average top1 and top5 accuracies" — but this phrasing is ambiguous and could be clearer.

### Trivial

- The actionness analysis (212K verbs in InternVid vs. 109K in WebVid10M) is acknowledged by the authors as noisy due to NLTK counting. A small human evaluation of caption quality would strengthen this claim but is not required.

## Nice-to-Haves

- Run the generation control: train on InternVid-Aesthetics-18M alone, or on 28M WebVid samples, to separate quality from quantity effects.
- Compare InternVid-200M (re-sampled with max-one-clip-per-video) to validate or refute the false-negative hypothesis.
- Add video-text baselines (UMT, InternVideo, MERLOT Reserve) to Table 1 for proper contextualization, even if ViCLIP does not surpass them.
- Small-scale human evaluation of caption correctness on ~1K sampled clips.

## Removed Points

- *"InternVideo reports 83.1% top-1 on K400 vs. ViCLIP's 64.8%"* — This number cannot be verified as a zero-shot result from the information available; InternVideo's 83.1% is widely recognized as a fine-tuned result. The general point about missing video-text baselines is retained, but this specific claim is removed as potentially misleading.
- *"Table 5's caption is duplicated/misnumbered"* — The extracted text does not show this issue; likely a parser artifact. Removed as a formatting nitpick.
- *"No human evaluation of caption quality"* — This is a nice-to-have, not a weakness; the paper provides a controlled caption ablation (Table 7) that serves as quantitative validation.
- *"The paper lacks comparison to video-text models trained on comparable data (e.g., UMT trained on WebVid10M + HowTo100M)"* — This conflates model architecture differences with data differences; the paper's controlled comparisons (same architecture, different data) are a cleaner experimental design for a dataset paper, and demands for architecture-level comparisons go beyond scope.
- *"The fine-tuned retrieval results are not clearly compared to prior work"* — The paper's primary goal is to compare data sources under a fixed architecture, not to beat every prior method. This is a scope issue, not a weakness.
- Several generic strength claims from the Strength Finder that lack specific content (e.g., "this paper addressed an important problem") are removed.

## Novel Insights

The most interesting finding in the paper is the non-monotonic relationship between data scale and zero-shot performance when moving from random sampling to curated sampling — specifically that 10M-FLT outperforms 200M random by 5 points on K400. The false-negative hypothesis (same-video clips acting as contrastive negatives) is a plausible mechanism that could apply broadly to video-text contrastive learning, but the paper stops short of validating it experimentally. This tension between the scaling narrative and the curation results is the most intellectually honest part of the paper and deserves deeper exploration.

## Suggestions

1. **Resolve the framing tension.** Either reframe the paper's message around curation quality (diverse sampling + high caption-video correlation) rather than naive scaling, or validate the false-negative hypothesis by re-sampling 200M with one-clip-per-video to show that scaling actually works when false negatives are controlled.

2. **Drop or qualify the SOTA claim.** Add video-text baselines (UMT, InternVideo) to Table 1, or restrict the SOTA claim to "among image-initialized contrastive video-text models of comparable scale." The dataset's value is evident from the controlled comparison against WebVid10M; SOTA claims are unnecessary and invite distraction.

3. **Add a data-quantity control for the generation experiment.** Train the baseline on more WebVid data (scaled to match 28M) or on InternVid-Aesthetics-18M alone. This would confirm whether the improvement comes from data quality/actionness or simply from having more data.

## Score and Decision

The paper makes a genuine contribution: InternVid is a large, well-constructed video-text dataset with a sound captioning pipeline, and the curated subsets clearly demonstrate advantages over existing alternatives. However, the paper oversells its results with unsubstantiated SOTA claims, frames its scaling narrative in a way that conflicts with its own best evidence, and has a confounded generation experiment. These issues are fixable in revision and do not invalidate the dataset contribution, but they detract from the paper in its current form.

**Originality:** 6/10 — The multiscale captioning pipeline is sensible but not fundamentally novel; the dataset scale and curation analysis are the main contributions.

**Quality:** 6/10 — Experiments are mostly well-controlled (same architecture, different data), but the generation experiment lacks a quantity control and key baselines are missing.

**Clarity:** 6/10 — Generally clear, but the SOTA claim is misleading and "AVG" should be defined prominently in the main text.

**Significance:** 7/10 — A large-scale, well-characterized video-text dataset is valuable to the community, and the findings about curation vs. scaling are informative.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>