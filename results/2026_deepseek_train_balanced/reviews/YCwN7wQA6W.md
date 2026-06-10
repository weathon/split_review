Now let me produce the final consolidated review.

## Summary

Grounded-VideoLLM introduces a 4B-parameter Video-LLM targeting fine-grained temporal grounding through two architectural innovations: (1) a two-stream encoder that combines a spatial image encoder (CLIP via Phi3.5-Vision) with a temporal video encoder (InternVideo2) using segment-wise encoding and pooling, and (2) discrete temporal tokens (M=300) for efficient timestamp representation, replacing numerical text. A three-stage progressive training pipeline (video-caption alignment → temporal token alignment → multi-task instruction tuning) and a GPT-4-curated grounded VideoQA dataset (17K samples) complete the system. The model achieves strong results on Charades-STA (mIoU 36.8), ActivityNet-Grounding (mIoU 36.1), and NExT-GQA (Acc@GQA 26.7), while maintaining competitive general video understanding on MVBench (59.4) and VCG-Bench (3.24).

## Strengths

- **Two-stream encoding delivers measurable, controlled gains.** The ablation in Table 3 is carefully designed: both the sparse (24 frames) and dense (96 frames) spatial-only variants are matched to the full model's token budget (~3456 vs. 3264 tokens). Removing the temporal stream drops mIoU by −6.4/−2.5 on Charades-STA and −8.1/−6.9 on ActivityNet-Grounding. This rules out the confound that improvements come from a larger token budget and provides clean evidence that the temporal stream contributes beyond what extra spatial frames can provide.

- **Discrete temporal tokens with dedicated alignment are critical for grounding performance.** Ablating Stage 2 (Temporal Token Alignment) causes a dramatic −9.3 mIoU on Charades-STA and −13.0 on ActivityNet-Grounding (Table 3). The paper further supports this with attention-weight visualizations (Figure 5): aligned tokens focus attention on the correct video moments, while unaligned tokens attend diffusely. This provides both quantitative and mechanistic evidence for the design choice.

- **State-of-the-art fine-grained grounding with a smaller LLM backbone.** Grounded-VideoLLM (4B) outperforms all prior 7B Video-LLMs on Charades-STA and ActivityNet-Grounding, surpassing HawkEye (7B) by +3.4 mIoU on both benchmarks. The model also achieves the highest Acc@GQA (26.7) on NExT-GQA among methods that report it. This is notable given the nearly 2× parameter disadvantage.

- **General video understanding is preserved, not sacrificed.** On MVBench, Grounded-VideoLLM achieves the highest average score (59.4), outperforming VideoGPT+ (58.7). It attains top scores on Action Sequence (76.0), Action Prediction (75.5), and Action Localization (59.5) — tasks that directly require temporal awareness — demonstrating that the two-stream design benefits general video understanding, not just grounding benchmarks.

- **Progressive training stages are individually justified by ablations.** Each stage has a clear purpose and is shown to be necessary: Stage 1 aligns video features, Stage 2 aligns temporal tokens (ablation shows −9.3 mIoU without it), and Stage 3 adds the grounded VideoQA data (ablation shows −8.6 Acc@GQA without it). The grounded VideoQA dataset ablation is particularly clean, showing a large drop when removed.

## Weaknesses

### Major

- **The "zero-shot" claim for Table 1 results is not adequately justified.** Table 1 is captioned "Zero-shot results on temporal sentence grounding and dense video captioning tasks." However, Stage 2 uses VTimeLLM-Stage2 data and Stage 3 uses VTG-IT (84K temporal sentence grounding + 41K dense video caption samples). Both VTG-IT (from VTG-LLM) and VTimeLLM-Stage2 are compiled from multiple public datasets and it is entirely plausible — indeed likely — that they include ActivityNet- and Charades-STA-derived annotations. The paper does not specify what VTG-IT or VTimeLLM-Stage2 contain, nor whether dataset overlap with the evaluation benchmarks was checked. This means the "zero-shot" label may be incorrect for ActivityNet-Grounding, ActivityNet-Captions, and possibly Charades-STA. The relative comparisons against baselines remain informative, but the framing should be corrected to "cross-dataset evaluation" or the authors should verify and report overlap statistics. This is the paper's most significant overclaim.

- **The temporal token ablation conflates the token representation with the training data.** Removing Stage 2 removes both (a) the introduction of temporal tokens and (b) all grounding supervision data (336K samples across temporal sentence grounding, dense video captioning, and temporal referring). A reader cannot tell whether the *discrete temporal tokens themselves* matter, or whether the model simply needs more exposure to grounding supervision. The comparison would be cleaner: keep the same training data but represent timestamps as numerical text (as TimeChat does) versus using temporal tokens. The current ablation establishes that Stage 2 is important but does not isolate whether the discrete temporal token representation is the cause of the improvement. This is the paper's most undersupported architectural claim. (The attention visualizations in Figure 5 provide partial mechanistic evidence but do not substitute for a controlled comparison.)

### Minor

- **NExT-GQA results are framed in a way that could be interpreted selectively.** The paper claims the highest Acc@GQA (26.7, +2.4 over LLoVi), which is correct. However, the model's mIoU on NExT-GQA (21.1) is lower than HawkEye's (25.7), and IoU@0.5 (18.0 vs. 19.5) is also lower. Acc@GQA conflates answer accuracy with grounding quality (requiring IoP ≥ 0.5 for correct answers). The Acc@GQA improvement could come from better QA (Phi-3.5's stronger language capabilities or broader instruction-tuning data) rather than better temporal grounding per se. The paper acknowledges the IoU scores as "comparable" and does not claim superiority there, but the framing could be more precise by disentangling these factors.

- **The two-stream architecture's novelty relative to acknowledged concurrent work is underspecified.** The paper cites SlowFast-LLaVA and VideoGPT+ as also using two-stream architectures and states that Grounded-VideoLLM "specifically targets fine-grained temporal grounding through a unique encoding/pooling/training strategy for dense frames and grounding design" (Section 2). This is too vague to be informative. What distinguishes the approach — the segment-wise pooling strategy, the specific encoder choices (InternVideo2), the concatenation strategy, or the progressive training? The paper would benefit from a clear, point-by-point differentiation.

- **No limitations or failure cases are discussed.** Every method has failure modes. How does the model handle videos with extreme duration variation (5 seconds vs. 5 minutes) given the fixed segment count (K=12) and fixed temporal tokens (M=300)? Are there specific types of temporal queries where the model systematically fails? Including a limitations section would strengthen the paper.

- **No error bars or statistical significance reported.** Given the use of GPT-based evaluation (which has known variance) and retrieval metrics on finite test sets, reporting variance would contextualize the reliability of the results. The paper does not report standard deviations or confidence intervals for any experiment.

### Trivial

- **Resolution specifications for the two encoders are not stated.** The paper says the temporal stream uses "a lower resolution" (Section 3) but does not give numeric values (e.g., InternVideo2's typical 224×224 vs. Phi3.5-Vision's 336×336). This is a minor omission that affects reproducibility.

## Nice-to-Haves

- A decomposition of NExT-GQA Acc@GQA into answer accuracy alone vs. grounding accuracy given a correct answer would clarify the source of improvement.
- An ablation that keeps Stage 2's training data identical but replaces temporal tokens with numerical text timestamps (as TimeChat does) would directly test whether the discrete token representation is responsible for the gains.
- Quantifying the quantization error introduced by M=300 temporal tokens (Eq. 3) for the typical video durations in each benchmark would demonstrate that the rounding is lossless enough.
- Reporting inference speed or FLOPs would contextualize the performance gains against single-encoder baselines.

## Removed Points

(These are flagged to be removed; treat with caution.)

1. **"No human evaluation of the generated VideoQA data"** (Harsh Critic: "there is no human evaluation of the generated data quality") — Removed. The dataset is supplementary to the main contribution; the paper provides a principled automated pipeline with cosine-similarity-based distractor selection and demonstrates the dataset's impact via a clean ablation (Table 3). Requesting human evaluation for a 17K-sample training set exceeds the standard for this type of contribution.

2. **"No inference speed or computational cost comparison"** (Harsh Critic) — Removed. None of the baselines report FLOPs or inference time either, and this is not standard practice in Video-LLM benchmarking papers. It would be a nice addition but is not a weakness.

3. **Criticism that Charades-STA is "the only dataset here that is clearly not seen"** (Harsh Critic) — Removed as factually questionable. VTG-IT (used in Stage 3) likely includes Charades-STA, so it may not be "clearly not seen" either. This sub-point doesn't affect the overall zero-shot concern which stands on the ActivityNet evidence.

4. **"Missing related works" critique** — Not present in inputs, so nothing to remove.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Verify and report dataset overlap.** For each evaluation benchmark in Table 1, explicitly state whether any constituent dataset of VTG-IT, VTimeLLM-Stage2, or other training sources contains overlapping data. If overlap exists, retract the "zero-shot" label and replace with "cross-dataset evaluation" or "trained on in-distribution data." If no overlap can be verified, state this clearly.

2. **Run the clean temporal token ablation.** Keep Stage 2's training data completely identical but vary only the timestamp representation: one variant uses temporal tokens (current), the other uses numerical text timestamps (e.g., "from 10.2 to 15.8 seconds"). Report the difference in mIoU. This is the single highest-leverage experiment to support the paper's most distinctive architectural claim.

3. **Disaggregate Acc@GQA on NExT-GQA** into answer accuracy alone (without grounding) and grounding accuracy given correct answers. This would clarify whether the improvement comes from better QA, better grounding, or both.

4. **Add a limitations paragraph** discussing cases where the approach underperforms (e.g., very short/long videos, action types where motion is minimal, or types of temporal queries that the M=300 token representation struggles with).

## Score and Decision

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>