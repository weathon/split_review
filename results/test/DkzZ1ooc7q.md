Now I have all the information needed. Let me synthesize the consolidated review.

## Summary

OmniSep proposes a unified omni-modal sound separation framework that handles single-modal queries (text, image, audio) and multi-modal composed queries within a single model. The core innovation is **Query-Mixup**, a training strategy that blends query features from different modalities, enabling a single separation network to be optimized for all modalities simultaneously. The paper also introduces two inference-time techniques: **negative queries** (removing interference via a proportional weighting of query and anti-query features) and **Query-Aug** (retrieval-augmented mapping from unrestricted text to the nearest in-domain class label). Evaluations on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ show consistent SOTA or competitive SDR across TQSS, IQSS, and AQSS tasks.

## Strengths

1. **First unified omni-modal sound separation model.** OmniSep handles text, image, audio, and composed multi-modal queries in a single framework. Table 1 shows it achieves the highest SDR across all three tasks simultaneously (e.g., 10.65 vs. next-best 9.82 on MUSIC TQSS; 10.97 vs. 10.54 on MUSIC IQSS; 10.26 vs. 6.43 on MUSIC AQSS). Composed queries further improve performance (11.03 on MUSIC), demonstrating the benefit of cross-modal fusion.

2. **Query-Mixup is clearly validated as the key enabler.** Table 2's ablation is the paper's strongest piece of evidence. Training with all three modalities without mixup (ID #4) yields AVG SDR 6.45; adding Query-Mixup (ID #5) raises it to 6.70 — a gain of 0.25. Critically, the gain from just adding the audio modality (ID #3 → #4) is only 0.03, so the improvement is attributable to the mixing strategy, not simply more training data. Query-Mixup also lets a single model match the text-specific performance of ID #1 (6.70 vs. 6.70), something no prior method achieves.

3. **Negative query with proportional weighting is empirically robust.** Figure 2 shows that \( \mathbf{Q}' = (1+\alpha)\mathbf{Q} - \alpha\mathbf{Q}_N \) consistently outperforms naive subtraction \( \mathbf{Q} - \alpha\mathbf{Q}_N \) across all tasks and α values. The proposed method maintains stable SDR across a wide α range (e.g., ~7.4–7.6 on VGGSOUND-CLEAN+ TQSS for α=0.5 to 2), while naive subtraction drops from ~5.5 to 4.32. This robustness to weight selection is a practical strength.

4. **Query-Aug improves paraphrasing robustness substantially.** Table 4 shows OmniSep+Query-Aug achieves 6.32 Mean SDR on unrestricted text descriptions, compared to 4.95 for OmniSep alone and 5.49 for CLIPSEP-Text with predefined class labels. This demonstrates that the retrieval-augmented strategy effectively bridges the gap between out-of-domain descriptions and in-domain class features.

## Weaknesses

### Fatal
None.

### Major

1. **"Open-vocabulary" claim is overstated.** Query-Aug retrieves the nearest class label from a fixed query set of 330 VGGSound categories (Equation 5: \( \mathbf{Q}_{aug} = \arg\max_{\mathbf{Q}_i \in \text{Query-Set}} \text{sim}(\mathbf{Q}_{des}, \mathbf{Q}_i) \)). The separation is then performed using that retrieved class label's feature, not the original unrestricted description. The evaluation (Table 4) uses GPT-3.5 rewrites of the same 330 class labels (Appendix Table 7 shows examples like "dog barking" → "A dog letting out barking noises"), so it tests paraphrasing robustness, not the ability to handle genuinely novel sound categories outside the training set. A truly open-vocabulary system would need to separate sounds from categories unseen during training. The contribution of handling paraphrases is practically valuable and well-supported by the data, but the paper should either (a) rename this to "robust query paraphrasing" or "query expansion" or (b) explicitly acknowledge the limitation that the method is closed-set in terms of separation categories. The current framing overstates what is demonstrated.

### Minor

2. **Negative query formulation lacks explanatory depth.** Equation 4 (\( \mathbf{Q}' = (1+\alpha)\mathbf{Q} - \alpha\mathbf{Q}_N \)) is presented with the intuition that it "preserves non-key frequency bands," but no analysis connects the specific algebraic form to frequency-band stability. The paper compares against naive subtraction \( \mathbf{Q} - \alpha\mathbf{Q}_N \) in Figure 2, which conflates two changes (scaling Q by 1+α and the sign of the Q_N coefficient). A more informative comparison would be \( \mathbf{Q} - \alpha\mathbf{Q}_N \) vs. normalizing both or showing that the improvement is specifically from the scaling. The form \( \mathbf{Q} + \alpha(\mathbf{Q} - \mathbf{Q}_N) \) is interpretable as moving away from Q_N while staying near Q, but the paper does not make this connection. This doesn't invalidate the empirical results — Figure 2 convincingly shows the proposed method works — but the paper would be stronger with even a simple vector-space analysis.

3. **Practical aspects of the negative query at test time are not addressed.** Section 3.2 treats the negative query feature Q_N as given, but in a realistic deployment, the user would need to provide it — e.g., via a separate audio clip, a text description of the noise, or an image of the interfering source. The paper does not discuss how a user would obtain or specify this interference query, nor does it explore automatic estimation of the most interfering sound from the mixture. A brief discussion of practical scenarios would improve completeness and credibility.

4. **Composed query weights at inference are unspecified.** The Query-Mixup training uses randomly sampled weights \( w_a, w_v, w_t \in [0,1] \). For the composed query results in Table 1 (e.g., 11.03 on MUSIC), it is unclear how the relative weighting of modalities is determined at test time — are equal weights used, or is the weight inferred from the input? The paper does not clarify this.

### Trivial
None.

## Nice-to-Haves

- **Additional evaluation metrics.** The paper relies solely on SDR, which has known issues (e.g., sensitivity to loudness artifacts). Adding SI-SDR, PESQ, or STOI would strengthen the evaluation, though SDR is standard for this task class.
- **Discussion of alternative retrieval strategies for Query-Aug.** Beyond argmax similarity, strategies like weighted interpolation among top-k retrieved features could be explored.

## Removed Points

- **"Baseline comparison is imbalanced because OmniSep has more training data"** — Removed. Table 2 ablation (ID #3→#4→#5) shows adding the audio modality alone (#3→#4) improves AVG SDR by only 0.03, while Query-Mixup (#4→#5) improves by 0.25. The concern is directly addressed by the paper's own ablation.
- **"Relies heavily on ImageBind"** — Removed. Using a frozen pretrained multi-modal encoder is a standard architectural choice; this is no different from CLIPSEP using frozen CLIP. It is a design decision, not a weakness.
- **"Demo page not available for review"** — Removed per policy: cited resources are assumed to exist.
- **"Missing comparison with CLAP/AudioCLIP methods"** — Removed per policy: do not list missing related works without external verification.
- **"SDR as sole metric"** — Moved to Nice-to-Haves, as SDR (via museval) is the conventional metric in this evaluation paradigm.
- **Various formatting/style nitpicks** — Removed as parser artifacts.

## Novel Insights

The most interesting structural insight from the reviews is that Query-Mixup serves double duty: it not only enables unified training across modalities, but it also creates a shared embedding space where vector arithmetic (composed query addition and negative query subtraction) becomes meaningful at inference time. This is noted in Section 4.5 of the paper ("the additive and subtractive characteristics of embeddings between different modalities"), but the review analysis clarifies that this coupling — where the training strategy and the inference-time operations are tightly linked through the geometry of the embedding space — is the paper's most conceptually novel contribution. Without Query-Mixup creating "mixed embeddings" that bridge inter-modal gaps (as shown in the UMAP visualization, Figure 4), neither the composed query nor the negative query would operate on features the separation network is calibrated to handle.

## Suggestions

1. **Adjust the "open-vocabulary" framing.** Rename to "robust query paraphrasing via retrieval augmentation" or "unrestricted text query handling," and add a sentence either in the abstract or Section 3.3/4.4 stating clearly: "Note that Query-Aug retrieves the nearest in-domain class label, so the method operates within the closed set of training categories but can handle arbitrary paraphrases of those labels."

2. **Add a brief geometric interpretation of the negative query.** Show that \( \mathbf{Q}' = (1+\alpha)\mathbf{Q} - \alpha\mathbf{Q}_N = \mathbf{Q} + \alpha(\mathbf{Q} - \mathbf{Q}_N) \), i.e., moving from Q_N toward Q and continuing beyond. A simple 2D toy example would suffice and would clarify why proportional weighting outperforms naive subtraction.

3. **Add a short paragraph on practical use of negative queries** (e.g., "In practice, the user can provide the interference query as a text description of the noise, an audio recording of the interfering source, or an image of the sound-producing object. Alternatively, a future system could estimate the dominant interference automatically.").

4. **Clarify composed query weights at inference.** State the default weighting used in the composed-query experiments (e.g., equal weights \( w_a = w_v = w_t = 1 \) before normalization).

## Score and Decision

This is a solid empirical paper with well-supported claims, clean ablations, and consistent SOTA results. The main weakness — overclaimed "open-vocabulary" framing — is a terminology issue that can be corrected without altering the paper's genuine contribution (handling paraphrased text queries via retrieval augmentation). The negative query and composed query results are empirically convincing. The paper is clearly written, methodologically sound, and the ablation study is a model of how to isolate the effect of each component.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>