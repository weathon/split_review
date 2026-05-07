Now I have a thorough understanding of the paper and the calibration anchors. Let me assess the key claims:

1. **Multi-subject pooling**: The paper explicitly says "we combined the electrodes from all three subjects into a single subject for all analyses, totalling 864 electrodes." This is a major methodological issue - the "single subject" has 864 electrodes from 3 different brains. No per-subject results are reported.

2. **Oracle sentence boundaries**: The paper says "the corresponding neural data segment from when the sentence was spoken used for training" - confirming that sentence timing is given, not inferred.

3. **Language prior confound**: The "random control" uses randomly initialized modules, which doesn't test whether trained neural pathways actually carry semantic information vs. the Vec2Text corrector learning text priors. Shuffled neural-text pairs would be a much stronger control.

4. **Absolute performance**: WER ~0.966, BLEU ~0.079, BERT Score ~0.195. These are objectively low.

5. **Baseline comparison**: Only Tang et al. (2023), an fMRI method, is compared.

6. **Data leakage via electrode selection**: The electrode selection uses Mistral-7B embeddings and is not explicitly stated to be nested within CV splits.

7. **Overclaiming**: "remarkable performance", "unconstrained text generation", "continuous language", "zero-shot generalization" - while WER is 0.966.

Now let me compose the final review.

## Summary

Neuro2Semantic introduces a two-phase transfer learning framework that maps iEEG signals to text embeddings (via an LSTM adapter trained with contrastive + triplet loss) and then inverts those embeddings to text (via Vec2Text corrector fine-tuning). The approach is evaluated on three epilepsy patients who listened to ~30 minutes of podcast-style conversations, decoding perceived speech at the sentence level with BERT Score 0.195, BLEU 0.079, and WER 0.966, outperforming an adapted fMRI-based baseline (Tang et al., 2023) by ~6× on BERT Score.

## Strengths

- **Novel two-phase architecture for low-data iEEG decoding**: The idea of aligning iEEG to a pretrained text embedding space and then inverting with a pretrained corrector is a plausible and interesting direction for data-scarce neural decoding, and the ablation showing that Phase 1 + Phase 2 together outperform either alone (Table 1: BERT 0.195 vs 0.056 for Phase 1 only or 0.100 for Phase 2 only) confirms both components contribute meaningfully.
- **Principled electrode selection**: Using Mistral-7B embedding encoding strength to select semantically responsive electrodes is neuroscientifically motivated and provides a principled alternative to anatomical or arbitrary channel selection.
- **Data and electrode scaling analyses**: Figures 4A and 4C show approximately linear scaling with training data, and Figure 4B shows partial robustness to electrode subsampling, both useful for understanding the method's potential trajectory.
- **Out-of-domain evaluation**: The paper attempts story-level holdout evaluation (Section 3.3), going beyond pure in-domain testing.

## Weaknesses

### Fatal

None that completely invalidate the paper's existence, but there is a very severe evaluation issue that undermines the core claim.

### Major

- **Multi-subject electrode pooling undermines practical interpretability**: The paper pools 864 electrodes from three different patients into a single "virtual subject" for all analyses (Section 2.2). No subject-level results are reported anywhere. In a practical BCI setting, one does not have simultaneous access to 864 electrodes across three brains. This makes the reported performance uninterpretable for individual-level decoding and inflates the effective coverage beyond what any single patient could achieve. The paper acknowledges "cross-subject variability" as a limitation but treats it as future work, when in fact it is a core validity question for the reported results. Without per-subject analyses, it is impossible to determine whether the method works at all for any individual patient.

- **Language prior confound is not adequately controlled**: The random control (randomly initialized LSTM adapter + corrector) only establishes that trained parameters matter, not that neural semantic information is being decoded. A more informative control would be shuffled neural-text pairs or a text-only prior model. The Vec2Text corrector is fine-tuned on the training transcripts and can learn conversation-style priors. Given the WER of ~0.966 (nearly all words wrong) and the loosely topical outputs shown in Section 3.3, it is plausible that much of the BERT Score reflects generic conversational priors rather than neural semantic content. This is not a minor missing ablation—it is essential to establishing that the method actually decodes neural signals rather than exploiting a text prior.

- **Overclaimed performance and BCI relevance**: The paper describes results as "remarkable performance" with "unconstrained text generation" and implications for "augmentative communication," but the absolute metrics are extremely low (BLEU 0.079, WER 0.966). The qualitative examples (e.g., reconstructing "This is the place with the robotic waiters, right?" as "I'm looking at some TV shows about how people could really live in a modern place") show only loose topical overlap—these are at best capturing broad semantic themes, not "reconstructing text" or "decoding continuous language." Moreover, the task decodes perceived (listened) speech with known sentence boundaries, not intended speech or continuous neural streams, making BCI/communication claims premature.

### Minor

- **Electrode selection may not be nested within cross-validation splits**: The electrode selection procedure uses Mistral-7B embeddings and t-tests over 10 splits, but it is unclear whether this selection is performed strictly within each train/test CV fold. If electrode selection is performed prior to the train/test split, this introduces data leakage that could inflate reported performance.

- **Statistical testing treats sentences as independent samples**: The paired t-tests in Figure 2A treat all sentence pairs as independent, but sentences are nested within stories (6) and subjects (3, pooled). The effective degrees of freedom are much smaller than the number of sentence pairs, potentially inflating significance.

- **The baseline comparison is limited**: Tang et al. (2023) is an fMRI Bayesian decoder adapted to iEEG; its poor performance under data-scarce iEEG conditions is predictable. The "6× higher BERT Score" claim should be interpreted cautiously given the mismatch between the baseline's design assumptions and the current setting.

- **Sentence-level oracle boundaries**: The model receives the neural segment corresponding to "when the sentence was spoken," meaning sentence timing and segmentation are provided rather than inferred. This limits the claim of "continuous language decoding," as a practical decoder would need to discover boundaries.

- **"Zero-shot" terminology is too strong**: The model is trained on the same subjects, same recording setup, and same podcast domain; only the story topic is held out. This is an out-of-story generalization test, not zero-shot neural decoding.

### Trivial

None beyond what is already noted.

## Nice-to-Haves

- Per-subject decoding results using only each subject's own electrodes.
- Controls with shuffled neural-text pairs and mean/random neural embeddings to quantify the language prior contribution.
- Embedding-space validation (e.g., retrieval accuracy of neural embeddings against true vs. distractor text embeddings), which would directly assess Phase 1's semantic alignment.
- Random, median, and worst-case reconstruction examples rather than only handpicked ones.

## Removed Points

- *Demand for continuous decoding without oracle sentence boundaries*: While valid as a limitation, the paper's stated contribution is sentence-level reconstruction, not continuous streaming. Evaluating continuous decoding would be a genuine extension, not a requirement for this initial demonstration. Demanding it as a fatal flaw is scope creep.
- *Demand for completely novel baselines (ridge regression, retrieval, CLIP-style adapter without corrector)*: Adding more baselines would strengthen the paper, but the current comparison shows the proposed method beats both the Tang et al. baseline and a random control. Additional baselines are a nice-to-have, not a fatal flaw.
- *Nitpicks about missing method details (negative sampling scheme, triplet margin, etc.)*: These would be addressed in an appendix, which the parser strips. They do not invalidate the method as described.
- *The claim that the baseline comparison "unfairly favors Neuro2Semantic" is wrong directionally*: The asymmetry (fMRI method on iEEG data) actually makes it harder for the proposed method to look good, since anyone could argue the baseline wasn't given fair optimization. However, it is still a weak comparison because it doesn't tell us much.
- *Formatting/style nitpicks and minor notation questions*: Removed per instructions.

## Novel Insights

The paper's most interesting contribution is the proof-of-concept that a two-phase transfer learning pipeline (align iEEG → text embeddings, then invert) can produce any signal at all from as little as 30 minutes of intracranial data. However, the combination of multi-subject pooling, language-prior confounds, and absolute performance near floor levels (WER ~0.97) means it remains genuinely unclear whether the method is decoding neural semantic content or producing language-model-driven topical guessing. The scaling results are the most promising signal, but they are also potentially confounded by the pooled-subject design. The community needs per-subject and prior-controlled experiments to determine whether this direction is viable.

## Suggestions

- Report per-subject results (each subject decoded with only their own electrodes) as the primary evaluation, and pool only as a secondary analysis.
- Add a shuffled-neural-text-pairs control (train the full pipeline with randomized neural-text correspondences) to quantify the language prior contribution.
- Tone down language: replace "remarkable performance," "successfully reconstructing text," and "unconstrained text generation" with more measured characterizations given WER ~0.97.
- Replace handpicked examples with systematically sampled best/median/worst reconstructions.
- Explicitly state whether electrode selection is nested within CV splits, and if not, redo the evaluation with nested selection.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Relevance |
|-------|-----------|-----------|
| PredFT (2hKDQ20zDa) — fMRI language reconstruction, outputs incoherent, language prior confound | 4.75 | Very similar: language-prior confound, overclaimed decoding quality |
| MAD (dM4yZd6ic9) — MEG-to-text, weak baselines, LM prior inflating scores | 4.60 | Similar: weak baselines, language prior question |
| Diphone+LLM (pEh1SXCgOc) — brain-to-text decoding, limited novelty | 4.00 | Similar domain, similar concerns |
| BrainSCUBA (mQYHXUUTkU) — brain-to-text captions, good evaluation | 7.00 | Higher quality, more rigorous controls |
| H2DiLR (cWEfRkYj46) — iEEG tone decoding, multi-subject but proper per-subject analysis | 6.00 | Similar iEEG domain, but properly handles subject variability |
| NeuroLM (Io9yFt7XH7M) — EEG multi-task foundation model | 6.25 | Accepted, good scope for a similar domain |
| PopT (FVuqJt3c4L) — cross-subject neural representations | 7.50 | High quality, well-validated electrode pooling |

This paper shares core weaknesses with PredFT (language prior confounds inflating metrics against a weak baseline) and MAD (unfair baseline, limited evaluation rigor). The PredFT paper (4.75) had similar concerns about whether results reflect genuine neural decoding vs. LM priors, and that paper at least had per-subject fMRI data without pooling across subjects. This paper has the additional serious issue of pooling electrodes across three subjects into a virtual 864-electrode "subject" without reporting individual results. The comparison with H2DiLR (6.0) is instructive—H2DiLR works with iEEG across subjects but explicitly models homogeneity/heterogeneity and reports per-subject results. Neuro2Semantic does neither.

The absolute performance (WER ~0.97) is worse than PredFT (BLEU-1 ~28%) and comparable to papers that were rejected. The BERT Score of 0.195, while better than random, is weak evidence of semantic decoding when language priors are not controlled.

This paper is positioned below PredFT (4.75), because (a) the multi-subject pooling further undermines the results, (b) the language prior confound is more severe (fine-tuning Vec2Text on the training conversations), and (c) the absolute metrics are near-floor. It is above the worst papers (2-3 range) because the two-phase architecture idea is reasonable, the ablation design is somewhat informative, and the scaling experiments have some value.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>