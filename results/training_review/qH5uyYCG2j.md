Now I have all the evidence needed. Let me write the final consolidated review.

---

## Summary

This paper proposes a two-stage controllable TTS system that uses discrete attribute labels (binned from continuous values) for fine-grained control. A masked autoencoder extracts content-disentangled style features, which are discretized via RVQ into style tokens. Stage 1 (style LM) generates style tokens conditioned on text and control signals; Stage 2 (acoustic LM) generates codec tokens from text and style tokens. The key design rationale is that the style LM can be trained on large-scale data (Gigaspeech-xl, ≈10k hours) while the acoustic LM only needs smaller high-quality data (LibriTTS, ≈585 hours). Classifier-free guidance (CFG) is applied to discrete labels to improve fine-grained control.

## Strengths

- **Two-stage pipeline with the style LM trained on large data improves robustness.** Figure 3 shows that as CFG scale increases, the two-stage model maintains stable WER and UTMOS on out-of-domain test sets (Gigaspeech, DailyTalk), while the one-stage baseline trained only on LibriTTS degrades severely (WER rising from ~5% to >25% on DailyTalk). This demonstrates that scaling up style LM training data mitigates the quality-control tradeoff.

- **CFG ablation provides informative analysis of fine-grained vs. coarse attributes.** Figure 4 shows that CFG has little effect on coarse attributes like gender but significantly improves control accuracy for fine-grained attributes such as pitch std (from ~60% to ~90% on Gigaspeech). The analysis of CFG scale saturation (where too-large scales hurt accuracy) is a useful practical finding.

- **Style MAE produces a content-disentangled representation validated by multiple signals.** Table 2 shows that reconstruction from ground-truth style tokens achieves MCD of 4.04 on LibriTTS vs. 7.18 for YourTTS and 7.61 for XTTS-V2, indicating faithful prosody/style capture beyond speaker identity. The phoneme-style swapping experiment (yielding unintelligible speech) further confirms minimal content leakage.

- **Systematic correlation analysis among control attributes (Section 4.4) surfaces an important practical issue.** The paper reports Pearson correlations between high-level and low-level attributes (e.g., gender vs. pitch mean: 0.73) and demonstrates that learned MLP predictors can predict low-level pitch labels from high-level labels with 80% soft accuracy, providing a concrete path to avoid conflicting control signals.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to any existing controllable TTS system** — The paper motivates itself by criticizing natural-language-based controllable TTS (PromptTTS, PromptTTS 2, TextrolSpeech, InstructTTS, VoxInstruct, Audiobox) as suffering from coarse-grained control and data scarcity, yet it never compares to a single prior system on any metric. The abstract claims "our model achieves superior control over attributes such as pitch and emotion," but there is no experimental evidence that the discrete-label approach outperforms or even matches existing methods. The reader cannot assess whether the reported control-accuracy numbers (e.g., ~90% for pitch std with CFG) are strong or weak relative to the field. This is a fundamental evidential gap that severely limits the paper's claims.

2. **The one-stage vs. two-stage comparison is confounded by data scale** — The paper's central experimental validation (Section 4.3.2) compares a one-stage model trained on LibriTTS (≈585 hours) against a two-stage model whose style LM is trained on Gigaspeech-xl (≈10,000 hours). The reported advantages in WER stability, UTMOS, and control accuracy cannot be cleanly attributed to the two-stage architecture versus the 17× larger training set. A one-stage model trained on the same larger data, or a two-stage model with both stages trained on LibriTTS, would be needed to disentangle the effect. While the paper's stated goal is to leverage large data via the two-stage design, the experimental framing as "validating the effectiveness of our two-stage design" (line 218) overstates what the comparison actually supports.

### Minor

1. **Control accuracy evaluation shares annotation tools with training** — The same tools used to label the training data are used to extract attribute labels from generated speech for evaluation (Section 4.2). This creates a risk that the model learns to reproduce the annotation tool's systematic biases rather than achieving perceptually meaningful control. The paper acknowledges tool limitations in its Limitations section but does not provide subjective validation (e.g., a user study on control perception). The use of relaxed accuracy (within 1 bin) further inflates numbers.

2. **Incremental novelty of the style MAE relative to Prosody-TTS** — The style MAE architecture closely follows Huang et al. (2023) (Prosody-TTS), with the main addition being a contrastive loss. The paper cites this prior work but does not clearly articulate what is novel in the MAE component beyond that loss. The contribution is more in the overall two-stage TTS pipeline than in the style encoder itself.

3. **Missing specification of the neural codec** — The paper repeatedly references "codec tokens" and "codec decoder" but does not specify which codec model is used (e.g., EnCodec, DAC, SoundStream, SpeechTokenizer). This is a reproducibility gap.

4. **Missing architecture details for the multi-scale transformer** — The paper states it uses a "multi-scale transformer as the backbone model (Yang et al.; Huang et al., 2024)" but provides no depth, width, or attention-pattern details. While references are given, the lack of any architectural summary makes the paper less self-contained.

### Trivial
None.

## Nice-to-Haves
- A controlled comparison where a one-stage model is trained on Gigaspeech-xl (or a comparable large dataset) to isolate the architectural benefit from the data-scale benefit.
- A user study (e.g., ABX test on intended attribute changes) to validate that objective control accuracy correlates with human perception.
- t-SNE/UMAP visualizations of style tokens colored by attribute labels to visualize whether the representation factorizes attributes.

## Removed Points
These points were flagged by the reviewer but are factually wrong, reflect misunderstandings, or are parser artifacts. Treat with caution.

- **Claim that the MLP predictors in Section 4.4 are "not implemented or tested"** — The paper clearly reports training MLPs and achieving 40% hard accuracy / 80% soft accuracy. This is factually incorrect.
- **Claim that comparing reconstruction from GT style tokens to zero-shot TTS is "unfair"** — The comparison is appropriate: it demonstrates that style tokens carry richer information (prosody, acoustic environment) than speaker embeddings alone. The lower MCD supports the paper's claim about style representation quality.
- **Formatting/style nitpicks and missing related work suggestions** — The paper's missing references to classic fine-grained control systems (GST, PitchTron, FastSpeech variants) cannot be included as a weakness per the guidelines, since external sources cannot confirm their relevance or absence.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add comparisons to at least 1-2 existing controllable TTS systems** (e.g., TextrolSpeech, PromptTTS 2) on the same test sets using the same control-accuracy and naturalness metrics. Without this, the paper's claims of superiority are unsupported.
2. **Add an ablation controlling for data scale** — either train a one-stage model on Gigaspeech-xl (or a random 10k-hour subset) or train the two-stage style LM on just LibriTTS to isolate the architectural contribution.
3. **Specify the neural codec used** (model name and checkpoint) and provide basic architecture parameters for the multi-scale transformer.
4. **Report exact (non-relaxed) control accuracy alongside the relaxed metric** and acknowledge the circular-evaluation risk more prominently.

## Score and Decision

The paper proposes a sensible architecture and contains useful analysis (CFG ablation, attribute correlation study). However, the experimental validation has two major gaps: (1) no comparison to any existing controllable TTS system, despite claiming superiority, and (2) the one-stage vs. two-stage comparison is confounded by a 17× difference in training data. These are not fatal to the core idea, but they prevent the paper from convincingly demonstrating its contributions. The paper would need substantial additional experiments (especially baselines to prior work) before its claims are adequately supported.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>