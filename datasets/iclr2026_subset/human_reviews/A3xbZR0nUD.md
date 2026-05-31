## Human Reviewer 1

### Summary
This paper introduces TAI-speech, a RAFT-based audio analysis framework for dementia detection. Spectrograms are treated as sequential frames and fed into a convGRU structure to capture temporal-aware dementia-related representations iteratively.

### Strengths
This work adapts an optical-flow framework, specifically RAFT, for audio analysis. It performs dementia detection without relying on text content, avoiding the necessity of requiring a manual transcript or an ASR model.

### Weaknesses
Line 210 “pause probability q(n) estimated from voice activity detection”. The specific VAD method used in this work should be cited. 

The “cookie theft” figure is far larger than it needed to be, while Figure 2, the architecture diagram, has text that is too small to offer readability. 

Experimental details such as pitch extraction algorithm, VAD configuration, STFT parameters (window size, hop length, FFT size), or the number of Mel filters are not specified in the paper. Since prosodic features are highly sensitive to these settings, they should be explicitly reported. 

Since the spectrogram already includes the information of pitch and pause, the use of pitch contour and pause probability seems redundant to me. An ablation study should be done to evaluate the contribution of these features. Actually, no ablation study at all is provided to evaluate any design choice in this work, making it hard to assess which module drives performance gains. 

Data limitations: The only dataset used in this work is relatively small (477 samples), and may not support such a deep architecture, risking overfitting and limiting generalization to new populations or recording conditions. Though data collection may be challenging, a larger dataset is still necessary for such a deep learning framework. 

I didn’t see contributions qualified enough for an ICLR paper. The algorithmic framework and loss function lack clear innovation, and the experimental results do not show a significant improvement over baseline models. Therefore, I do not see sufficient innovation from a machine learning perspective. If this work is intended as a new application in the field of psychology, I would suggest submitting it to a psychology-related conference or journal instead. Even in that case, statistically significant results are still required to support your hypotheses.

### Questions
The idea of “ aligning spectral features with pith and pauses” is mentioned more than once in the paper. I am confused by this because information like pitch and pause is all included in the spectrogram, so a pitch contour or a pause probability sequence (no further description is provided for the VAD result, so I am assuming that it’s a frame-level pause probability) is naturally aligned to their corresponding spectrogram frame-by-frame. So what is the necessity of “aligning spectral features with pith and pauses” using an attention mechanism? 

Though dementia detection doesn’t seem to be a task requiring real-time response, I am still curious about the time cost of this architecture, which affects the real-world applicability of this framework.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes TAI-Speech that  treats speech as a dynamic sequence of spectrogram frames. This approach addresses the previous work's limitations that are time-agnostic, meaning previous work usually use aggregated features from entire utterance. The author uses "optical flow" like models, RAFT, for the dementia detection task. A convolutional GRU serves as a recurrent update module that iteratively refines latent representations, while crossattention aligns acoustic and prosodic cues. A Transformer encoder aggregates these temporally
enriched features for utterance-level prediction. The author performs evaluations on the standard DementiaBank Pitt corpus, and demonstrates strong performance of 83.9% AUC. This outperforms text-based methods and does not require ASR as helpers.

### Strengths
1. Treating spectrograms as sequential frames to be "refined" over time is a new way to model the dynamics of speech production.
2. The approach is ASR-free.

### Weaknesses
1. Evaluation is very limited on a single eval dataset.
2. The advantage over Pan et.al. (2025) is not significant.
3. No ablation studies and hard to tell if the optical-flow view can actually helps.

### Questions
Can you show how the optical-flow view point can capture the speech prosodic features in any interpretable way? For example, showing that such feature indeed captures the speaker's irregular pauses or so.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
2

---

## Human Reviewer 3

### Summary
The paper proposes TAI-Speech, a model for dementia detection from spontaneous speech. The core contribution is twofold: 1) An iterative refinement mechanism inspired by optical flow (RAFT) to model the frame-by-frame evolution of spectrograms, using a convolutional GRU. 2) A cross-attention module to align these spectral features with prosodic features (pitch and pauses). The authors claim this temporal-aware approach, theoretically linked to Instrumental Activities of Daily Living (IADL) impairment, achieves strong performance on the DementiaBank Pitt corpus without relying on ASR.

### Strengths
1. **Problem Relevance:** The task of developing non-invasive, scalable biomarkers for dementia detection from speech is of significant clinical importance.
2. **Core Idea:** The motivation to move beyond static, time-agnostic features and model the fine-grained temporal dynamics of speech production is a valid and promising research direction.

### Weaknesses
1. **Main Issue with IADL:**
   The biggest problem is the use of “IADL” (Instrumental Activities of Daily Living) in the paper’s title and framework. The model name “TAI-Speech” and Algorithm 1 both highlight IADL, but the paper includes no IADL data, labels, or evaluation. The authors even admit in the Limitations that they have no direct IADL measurements. This makes the “IADL” part misleading and weakens the overall focus of the paper.

2. **Unconvincing Motivation:**
   The connection to optical flow (RAFT) feels shallow and not well justified. The paper does not clearly explain why an iterative refinement approach from video motion estimation is useful for audio spectrograms, especially when existing models like Transformers or RNNs already perform iterative updates. As a result, the motivation behind the method feels forced rather than natural.

3. **Limited Experiments:**
   The experiments are too limited for a strong conference paper.

   * **Few Baselines:** Table 2 only compares with three other systems.
   * **Missing Strong Baselines:** There are no standard models included, such as CNNs (e.g., ResNet), RNN/LSTM/GRU architectures, or pre-trained audio models like wav2vec 2.0 or HuBERT. Without these, the reported 0.839 AUC doesn’t provide meaningful context.

4. **Clarity and Presentation Issues:**
   The paper is hard to follow. Figure 2 (Architecture) is cluttered and confusing.

### Questions
1. **On the IADL Premise:** Given that "IADL" is central to the paper's naming (TAI-Speech) and framing, can you justify this choice given the complete absence of any IADL data, labels, or empirical validation in the study? Why was this approach taken instead of framing the paper around what was *actually* studied (e.g., acoustic-prosodic temporal dynamics)?
2. **On Missing Baselines:** To properly situate the model's performance, could you provide benchmark results against more standard and established baselines in this domain? Specifically, (a) a strong CNN (e.g., ResNet) on spectrograms, and (b) a fine-tuned self-supervised model (e.g., wav2vec 2.0 or HuBERT), which you already cite.
3. **On the Optical Flow Analogy:** Can you provide a deeper theoretical justification for *why* an optical-flow-inspired iterative refinement (RAFT) is fundamentally better suited for this audio task than existing sequence models (like Transformers or LSTMs) that also handle temporal dependencies? What does this complex approach capture that they cannot?

### Soundness
1

### Presentation
3

### Contribution
1

### Rating
0

### Confidence
4