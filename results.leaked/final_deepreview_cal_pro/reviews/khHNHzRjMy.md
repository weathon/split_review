Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

EmoSign introduces the first American Sign Language (ASL) video dataset annotated for sentiment, emotion categories, and open-ended emotion-cue descriptions — all labeled by Deaf native ASL signers. The dataset consists of 200 clips (~16 minutes, 4 signers) drawn from the existing ASLLRP corpus, selected via VADER text-sentiment filtering. The paper benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) on sentiment analysis and emotion classification across caption-only, video-only, and video+caption conditions, finding that all models perform near-randomly when given only the video, while adding captions yields substantial improvements. An emotion cue grounding analysis is included as a qualitative investigation.

## Strengths

- **First-of-its-kind dataset filling a genuine gap.** No existing ASL dataset provides emotion or sentiment labels. EmoSign is the first resource targeting the affective dimensions of signing, enabling research that was previously impossible (Section 2, Table 1).

- **Deaf native signer annotations with competitive reliability.** The annotations achieve a mean Krippendorff's α of 0.593 (Table 2), which the paper correctly notes exceeds inter-annotator agreement reported for widely-used emotion datasets MELD (κ=0.43) and IEMOCAP (κ=0.48) (Section 3.3). Positive-emotion categories reach α up to 0.699.

- **Clear, well-supported demonstration of MLLM failure on visual-only emotion recognition.** In the video-only condition, all four models perform near-random: AffectGPT achieves a 7-class weighted F1 of 0.04 (Table 3), and single-emotion weighted accuracy remains ≤14% for all models (Table 4). This finding is robust and does not depend on text-based dataset selection — it directly substantiates the claim that current MLLMs cannot extract emotional information from sign language videos without textual crutches.

- **Rich cue descriptions from native signers.** The open-ended justifications from annotators (Section 3.4) document specific facial expressions, head/body movements, signing speed modifications, and mouth morphemes that signal emotion. This qualitative layer provides a resource for understanding *why* predictions succeed or fail, beyond simple accuracy metrics.

## Weaknesses

### Major

- **VADER-based selection creates a text-confounded benchmark.** The dataset was constructed by selecting the 100 most positive and 100 most negative utterances according to VADER scores on English captions (Section 3.1). This means the corpus was deliberately chosen so that the *text* would be emotionally extreme. The paper's finding that caption-only models perform comparably to video+caption models on emotion classification (Table 4) is therefore at least partially circular: the dataset construction loads the dice in favor of text. The paper acknowledges in Limitations that "VADER results differed from the annotators' results," but never quantifies this divergence (e.g., by reporting the correlation between VADER caption scores and final human sentiment labels). Without this, the reader cannot disentangle the effect of selection bias from genuine model deficiencies in the caption-only and video+caption conditions. This weakens the paper's interpretive claims about model text-reliance.

### Minor

- **Small dataset limits benchmark reliability.** With 200 clips from only 4 signers (~16 minutes total), per-class metrics are likely to have high variance. The paper acknowledges this implicitly by citing similarly-sized high-quality datasets (Arodi et al., 2024; Krojer et al., 2024; Li et al., 2024b), but does not report confidence intervals or per-class sample counts in the main text. The single-expression emotion classification subset (140 clips) is even smaller. While scale is understandable for a first-of-its-kind resource with expensive expert annotations, it means the benchmark cannot yet function as a reliable evaluation instrument.

- **Low-agreement emotion categories used without discussion.** Krippendorff's α for surprise_neg (0.119) and disgust (0.166) are well below conventional reliability thresholds (Table 2). The paper does not discuss how — or whether — these unreliable categories were handled differently in the benchmarks, and per-class accuracies for these categories appear in Table 4 as if they carry the same weight as high-agreement categories. Using majority-vote labels from such low-agreement cases as ground truth is questionable.

- **Emotion cue grounding is qualitative, not a benchmark.** Section 4.1 defines "Emotion Cue Grounding" as a third benchmark task alongside sentiment analysis and emotion classification, and Section 5.3 presents it under "Results." However, the analysis consists of manual inspection of "several randomly selected videos" with no quantitative metrics, no systematic evaluation protocol, and no way to compare models numerically. Framing this as a benchmark task is misleading. The qualitative observations are interesting and valuable, but they should be presented as a preliminary analysis rather than a named task.

- **Unclear whether annotators saw captions during annotation.** The paper does not explicitly state whether the English captions were shown to annotators during the labeling process (Section 3.2). If annotators saw captions, this would introduce label–text dependence; if they did not, this methodological strength should be made explicit.

### Trivial

- No confidence intervals or statistical significance tests are reported for any benchmark results, making it difficult to assess whether differences between models or conditions are meaningful.

## Nice-to-Haves

- Fine-tuned baselines (e.g., a visual-only model trained on existing sign-language data fine-tuned on EmoSign) would complement the zero-shot MLLM results and make the benchmark more actionable.
- A quantitative correlation analysis between VADER caption scores and final human sentiment labels would directly address the selection-bias concern.
- A systematic content analysis of the cue descriptions (e.g., coding frequency of different cue types) would surface valuable patterns and better differentiate the dataset.
- Quantitative grounding metrics (e.g., temporal segment alignment between model attention and annotator-identified cues) would elevate the grounding analysis from anecdotal to evaluable.

## Removed Points

*These points were raised in inputs but are removed from the final review:*

- **"The paper does not discuss consent or redistribution rights for the ASLLRP videos"** — The paper states IRB approval (Section 3.2) and ASLLRP is a publicly available dataset. This is not a substantive concern.
- **"The paper would benefit from a more explicit statement about why existing ASL datasets have not been leveraged for emotion"** — Table 1 and Section 2 already make this clear: existing datasets lack emotion labels.
- **"Missing per-class counts for single-expression subset"** — The paper states these are in Appendix A.5; the appendix is stripped by the parser, not missing in the original submission.
- **"No fine-tuned baselines"** — The paper explicitly identifies fine-tuning as future work (Section 6). This is a scope choice, not an omission.
- **"Formatting/style issues"** — These are parser artifacts, not author errors.

## Novel Insights

The paper's most interesting empirical finding — that MLLMs exhibit systematic biases (GPT-4o defaults to "happiness"/"frustration," AffectGPT to "neutral") when shown sign language videos without captions — reveals something about how these models' visual encoders interact with sign language input that general-purpose vision benchmarks would not expose. The observation that the *same* visual cue can be interpreted oppositely depending on whether a caption is present (Figure 3) is a concrete, vivid illustration of text-dominance in current multimodal architectures that goes beyond aggregate metrics.

## Suggestions

- **Reposition the emotion cue grounding section** as "Qualitative Analysis" rather than a benchmark task, and consider adding even a simple quantitative component (e.g., binary prediction of which frames contain emotional cues).
- **Report the VADER–human sentiment correlation** and discuss its implications for interpreting the caption-only and video+caption results.
- **Either exclude or flag** emotion categories with α < 0.3 in benchmark reporting, or discuss why they are retained despite low reliability.
- **Clarify** whether annotators had access to English captions during the annotation process and justify the choice.
- **Expand the dataset** beyond the VADER-selected clips in future work to reduce text confounds.

## Score and Decision

### Calibration Anchors

| Anchor ID | Paper | Avg Score | Round | Comparison to EmoSign |
|-----------|-------|-----------|-------|----------------------|
| f1uXrAjpOH | OV-MER (emotion rec. dataset) | 5.40 | R1 | More ambitious scope but had data leakage and unverified LLM labels; EmoSign's methodology is cleaner but smaller scale |
| L2kbdthX5M | SignAvatars (3D SL dataset) | 6.25 | R1 | Much larger scale (70K videos) but derivative data with automated annotations; EmoSign has more novel annotation type but much smaller |
| LqaEEs3UxU | Sign2GPT (SL translation) | 5.75 | R2 | Clean methods paper with SOTA results; EmoSign has more novelty but weaker execution rigor |
| 0Xt7uT04cQ | Uni-Sign (SL pre-training) | 6.40 | R1 | Large-scale dataset (1985 hrs) + unified framework; clearly stronger contribution than EmoSign |
| 2ET561DyPe | Few-Class Arena (benchmark) | 5.50 | R2 | Clean benchmark paper, accepted; EmoSign has more novelty but the VADER selection bias is a more significant weakness than anything in Few-Class Arena |
| n1X2n7MJ8L | CulturalBench (benchmark) | 5.00 | R2 | Small expert-annotated benchmark, rejected; similar scale limitations to EmoSign |

**Round 1 bracket:** Between 4.5 and 6.5. EmoSign is clearly weaker than Uni-Sign (6.40) and SignAvatars (6.25), but clearly stronger than the <3.5 band papers which have fundamental flaws.

**Round 2 narrowing:** EmoSign sits at the boundary between CulturalBench (5.00, Reject) and Few-Class Arena (5.50, Accept). The VADER selection bias and small scale pull it toward the lower end, while the genuine novelty and Deaf-annotator quality pull it upward. Compared to Few-Class Arena, EmoSign has a more novel contribution but a more significant methodological concern (text-confounded dataset construction).

**Final score: 5.0.** The paper addresses a genuine gap with a methodologically thoughtful annotation approach (Deaf native signers), and the video-only benchmark results are genuinely informative. However, the VADER-based dataset construction creates a text-confounded benchmark that undermines the interpretability of the caption-involved results, the dataset is too small to serve as a reliable evaluation instrument, and the emotion cue grounding is presented misleadingly as a benchmark task when it is purely qualitative. These issues are addressable — expanding the dataset beyond VADER-selected clips, reporting VADER–human correlations, and adding quantitative grounding metrics would substantially strengthen the contribution. In its current form, the paper does not meet the threshold for acceptance as a dataset-and-benchmark contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>