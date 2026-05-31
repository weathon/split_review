## Summary

This paper introduces TAI-Speech, an ASR-free framework for dementia detection from speech that models speech deterioration as a continuous temporal trajectory, inspired by optical-flow estimation. The architecture combines a convolutional GRU for iterative temporal refinement with cross-modal attention that aligns spectral features with prosodic cues (pitch and pauses). Evaluated on a subset of DementiaBank, TAI-Speech achieves an AUC of 83.9% and recall of 89.0%, outperforming fine-tuned Wav2Vec 2.0, Audio Spectrogram Transformers, and CNNs.

## Strengths

- **Novel cross-domain transfer**: Adapting optical-flow-inspired iterative refinement from computer vision to acoustic pathology detection is creative and well-motivated. The analogy between video motion and spectral evolution is clearly articulated.
- **ASR-free and privacy-preserving design**: Avoiding ASR eliminates cascading transcription errors and reduces privacy and computational burdens, which is practically important for clinical deployment.
- **Strong clinical relevance of the primary metric**: The model achieves 89.0% recall, which is crucial for screening applications where missing a dementia case is costly.
- **Clear theoretical grounding**: The paper connects speech deterioration to articulatory motor instability and functional decline (IADLs), providing a coherent conceptual framework beyond simple classification.

## Weaknesses

### Fatal
None.

### Major
- **No ablation study**: The paper presents the full model but does not isolate the contribution of any component (iterative refinement, cross-attention, temporal regularizer, prosodic features). Without ablation, it is unclear which design choices drive the improvement over simpler baselines. This is a significant gap for a method paper.
- **Weak baselines raise concern**: The fine-tuned Wav2Vec 2.0 achieves only 67.9% AUC and 56.5% accuracy on the same data. These numbers are substantially lower than typical DementiaBank results reported in the literature (often >80% AUC). This suggests either a non-standard data split, suboptimal fine-tuning, or a mismatch between the chosen subset and established benchmarks, making the claimed improvement less convincing.
- **Unclear data split and subset**: The paper uses “222 recordings from 89 HC and 255 recordings from 168 AD” (total 477) but does not specify which DementiaBank subset this corresponds to (e.g., ADReSS, ADReSSo, or a custom filter). The composition is imbalanced and smaller than the full corpus. Without a clear provenance, reproducibility is hindered and generalization claims are weakened.

### Minor
- **IADL framing is overclaimed**: The paper repeatedly invokes IADL as a modeling target, yet no IADL scores are used in training or evaluation. The connection is purely conceptual motivation. This could mislead readers about what the model actually predicts.
- **Training details for baselines are omitted**: The paper states that all models follow a unified protocol but gives no specifics (e.g., learning rate, batch size, input representation) for Wav2Vec, AST, or ResNet. This makes it hard to assess whether the baselines were reasonably tuned.

### Trivial
- The caption in Table 2 says “The Result (%) of our Model” but the AUC column shows 83.9 without a percentage sign; consistency could be improved.
- The algorithm listing uses `\hat{p}(n)` in the comment but `\tilde{p}(n)` in the equation; minor notation inconsistency.

## Nice-to-Haves

- An ablation study isolating the iterative refinement, cross-attention, temporal regularizer, and prosodic features would greatly strengthen the paper.
- Including a standard acoustic baseline (e.g., eGeMAPS + SVM/boosting) would better contextualize performance relative to established non-deep approaches.
- A t-SNE or similar visualization of the learned temporal embeddings could provide intuitive evidence that the model captures a “velocity” of spectral degradation.

## Novel Insights

The key insight that emerges beyond the paper’s own contributions is that strong temporal inductive biases—specifically, enforcing frame-to-frame continuity via iterative refinement—appear more diagnostic for pathological speech than global self-attention or static aggregation. This challenges the default assumption that increasingly large and flexible transformers are always preferable, and it suggests that domain-specific structural priors matter even in the deep learning era. The negative result for Wav2Vec 2.0 also hints that self-supervised pretraining on healthy speech may actively obscure the subtle acoustic markers of motor decline, which has implications for how foundation models should be adapted for clinical audio.

## Suggestions

- Provide a detailed description of the DementiaBank subset used (exact identifiers, speaker filtering criteria, train/test splits per fold) to ensure reproducibility.
- Add an ablation study with at least: (i) remove iterative refinement (replace with single-scale GRU), (ii) remove cross-attention, (iii) remove temporal regularizer, (iv) remove prosodic features.
- Re-run baselines with more thorough hyperparameter search or report standard results from the relevant challenge (ADReSS/ADReSSo) on the same split, to avoid the appearance of cherry-picking weak baselines.
- Either rename the IADL references to motivators rather than modeling targets, or explicitly incorporate IADL scores into the evaluation (e.g., correlation with model predictions) if available.

## Score and Decision

**MY FINAL SCORE: 6.5**  
**MY FINAL DECISION: Accept**