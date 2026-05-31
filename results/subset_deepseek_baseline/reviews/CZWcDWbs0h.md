## Summary

The paper introduces ALiRAS (Auto-labeled Linguistic Representations for Audio Spoofing detection), a multi-view approach that combines expert-defined phonetic/phonological features (breath, pitch anomaly, audio quality anomaly) with deep foundation models (Wav2Vec-XLSR, HuBERT, WavLM) for audio deepfake detection. The linguistic features are auto-labeled using a VGGish-based classifier fine-tuned on a small expert-annotated dataset, then integrated via ensemble methods. The authors claim improvements in explainability (via SHAP), scalability (31% time reduction through a cost-efficient ensemble), and maintained/improved effectiveness (EER, ROC AUC).

## Strengths

- Addresses an underexplored aspect of audio deepfake detection: explainability, by incorporating linguistically meaningful features.
- Provides a practical approach to scaling expert-informed features through auto-labeling, reducing reliance on manual annotation.
- Compares multiple foundation models and ensemble strategies, showing resource/time analysis which is rare in ADD literature.
- The interdisciplinary perspective (linguistics + ML) is well-motivated and offers a path toward more interpretable detection systems.

## Weaknesses

### Fatal
None.

### Major

1. **Mixed and weakly supported effectiveness claims.** The most competitive baseline (HuBERT-ResNet18) achieves EER 0.171, and adding ALiRAS does not improve this (still 0.171). The cost-efficient ensemble even slightly worsens it (0.184). The claimed 7% EER improvement applies only to the weaker XLSR-ResNet18 baseline (0.400 → 0.274), which is a substantial relative gain, but HuBERT already drastically outperforms both. The paper does not adequately justify why one would prefer the XLSR-based ensemble over HuBERT alone when effectiveness is paramount.

2. **Explainability is limited and superficial.** SHAP analysis is performed only on the simple ALiRAS-MLP classifier (trained on three binary features), not on the foundation models. The resulting explanations (e.g., “breath and pitch contribute positively”) are trivial given that these features were selected by experts for this exact purpose. The paper does not demonstrate how ALiRAS provides “semantic meaning” for the deep model’s decisions, only for the auxiliary shallow model. The claim of “reverse engineering” is overstated.

3. **Scalability analysis lacks rigor and generalizability.** The 31% time reduction is achieved by skipping the foundation model for samples that ALiRAS-MLP classifies as spoofed (threshold 0.55). The reduction depends on the false positive rate of ALiRAS and the spoofed-to-genuine ratio in the data, but these factors are not analyzed. The absolute time comparison (ALiRAS: 15 seconds on CPU vs. baselines: hours on GPU) is not an apples-to-apples comparison of resource usage for a real-time deployment scenario — VGGish can also be run on GPU, and the ensemble still requires running the foundation model on a non-negligible fraction of data.

4. **Auto-labeling performance is moderate.** The best auto-labeling model (VGGish fine-tuned on 840 expert-label samples) achieves an average ROC AUC of 0.71 over the three linguistic features. This suggests non-trivial labeling errors that would propagate into the ensemble. The paper does not analyze the impact of auto-labeling quality on downstream ADD performance, nor compare against an oracle with ground-truth expert labels.

### Minor

- The Large-scale dataset construction (7,000 ASVspoof 2021 DF evaluation clips as test set + 7,000 ASVspoof 2019 LA training clips as training set) is unconventional and not well justified. Mixing datasets from different challenge protocols may introduce domain mismatch that affects results.
- The ROC curve (Figure 4) is cluttered with 12 overlapping curves, making it difficult to read. Key comparisons (e.g., with vs. without ALiRAS) could be highlighted.
- The EER calculation is defined as (FAR+FRR)/2, which is an approximation; standard EER is the rate at which FAR = FRR. The impact of this approximation is not discussed.
- Some notation is inconsistent (e.g., “XLRS” vs. “XLSR”).

### Trivial
- The caption of Figure 1 describes a different architecture (VGGish path with Conv, Max Pool, FC) than the actual method (VGGish-based auto-labeling). The diagram is generic and does not clearly depict the auto-labeling pipeline.
- The paper includes an anonymous self-citation that violates double-blind policy (though this is not a substantive weakness).

## Nice-to-Haves

- An ablation study comparing ADD performance using ground-truth expert-labeled linguistic features vs. auto-labeled ALiRAS features would clarify the cost of automation.
- Analysis of which audio clips are skipped by the cost-efficient ensemble and whether the 31% reduction is consistent across different dataset splits or attack types.
- A more detailed exploration of why HuBERT already captures the linguistic cues naturally, and whether ALiRAS could be redundant when combined with such strong representations.

## Novel Insights

None beyond the paper's own contributions. The idea of auto-labeling expert-defined phonetic features for ADD is moderately novel, but the execution (simple binary predictors, shallow SHAP analysis) does not yield deep new insights about fake audio characteristics beyond what domain experts already know.

## Suggestions

- Strengthen the explainability claim by applying SHAP or similar methods to the *full ensemble* (not just the ALiRAS-MLP component) or by showing how ALiRAS features correlate with failure cases of foundation models.
- Report the fraction of samples skipped in the cost-efficient ensemble and the associated true/false positive rates, so readers can assess the generality of the time savings.
- Consider framing the contribution more modestly: ALiRAS is most beneficial for improving weaker baselines (e.g., XLSR) and for providing lightweight, interpretable pre-filtering, rather than claiming universal improvements over strong baselines like HuBERT.
- Evaluate on a single, standard benchmark (e.g., full ASVspoof 2021 DF evaluation set) without mixing training data from a different challenge.

## Score and Decision

The paper introduces an interesting interdisciplinary direction and addresses the important issue of explainability in ADD. However, the main claims are not consistently supported: effectiveness gains are limited to a weak baseline, explainability is demonstrated only on a trivial auxiliary model, and scalability analysis lacks depth. The overall contribution, while positive, is insufficient to outweigh these weaknesses.

**Score: 4**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>