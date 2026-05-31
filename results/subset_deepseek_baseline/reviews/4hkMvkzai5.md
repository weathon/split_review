## Summary
This paper proposes DeCodec, a neural audio codec that learns universally disentangled representations by decoupling mixed audio into orthogonal subspaces for speech and background sound, and further decomposing speech into semantic and paralinguistic components. The technical contributions include a Subspace Orthogonal Projection (SOP) module, a Representation Swap Training (RST) procedure, and semantic guidance (SG) within parallel residual vector quantizers. The model enables multiple downstream tasks—speech enhancement, one-shot voice conversion, ASR, and TTS—through controllable feature selection, without requiring cascaded separation pipelines.

## Strengths
- **Novel and well-motivated framework**: Reframing audio codecs as disentangled representation learners is a creative idea that directly addresses the need for controllable feature selection in real-world mixed audio. The inspiration from auditory cortex processing adds biological plausibility.
- **Effective technical design**: The combination of SOP (orthogonality constraint) and RST (swap training) is a clever way to enforce subspace decoupling, and the theoretical justification (though approximate) provides intuition for why this works. The addition of semantic guidance within speech quantization is a natural extension.
- **Comprehensive experimental validation**: The paper evaluates DeCodec on multiple tasks (reconstruction, SE, one-shot VC, plus downstream ASR/TTS in appendix) against strong baselines. Results show competitive or superior performance, especially in SE where DeCodec achieves the highest DNSMOS scores, and the ablation study cleanly isolates the contributions of each component.
- **Unified model for multiple tasks**: DeCodec demonstrates that a single codec can replace cascaded pipelines (e.g., SE + VC, SE + ASR) with less information loss, which is a concrete practical advantage.

## Weaknesses
### Fatal
None.

### Major
1. **Limited decoupling quality for background sound**: In the ablation study (Table 4), the SDR of the decoupled background component (SDR-B) is negative (−1.11 for causal DeCodec, −0.36 for full DeCodec), indicating that background sound reconstruction is poor. While this may not harm SE (which suppresses background), it calls into question the claim of genuinely disentangled background representations for tasks that require preserving or manipulating background sound (e.g., TTS with environmental sounds).
2. **One-shot VC performance remains low**: The WER of converted speech is still around 50%, even with background removal. The paper attributes this to voicing mismatch, but it suggests that the semantic-paralinguistic decomposition under noise is far from perfect, limiting practical utility. The improvement over the cascaded baseline is moderate, not transformative.

### Minor
1. **Theoretical justification is a sketch**: The proof that RST forces decoupling relies on the mean value theorem and linearity approximations; it is not a rigorous derivation. The assumptions (differentiable Dec, sufficient smoothness) are not verified.
2. **Lack of error bars or significance tests**: Many results (Tables 1–4) are reported as point estimates without confidence intervals, making it hard to gauge variability or compare improvements.
3. **Higher bitrate than baselines**: DeCodec uses 8.0 kbps, exceeding EnCodec (6.0) and DAC (4.5), which may limit its appeal for compression-focused applications. No discussion of bitrate-quality trade-offs is provided.
4. **Comparison with SE baselines is somewhat asymmetric**: SE baselines (Inter-SubNet, StoRM, SELM) are dedicated models trained for enhancement, whereas DeCodec achieves enhancement as a byproduct of representation replacement. A direct comparison with a cascaded codec+SE pipeline would be fairer (though the authors do compare StoRM-SpeechTokenizer for VC).

### Trivial
- In Table 1, the “Noisy Mel Distance” column header might be confused with the “SDR” column if scanning quickly; the formatting is clear but could be slightly improved.
- The paper uses “background sound,” “BGS,” and “background” interchangeably; consistency would help.

## Nice-to-Haves
- Include human listening tests (e.g., MUSHRA) for reconstruction and enhancement to complement objective metrics.
- Visualize the actual orthogonality achieved (e.g., cosine similarity between S and N during training) to directly confirm the SOP constraint works.
- Evaluate downstream tasks (ASR, TTS) on standard public benchmarks with more baseline codecs for a complete picture.

## Novel Insights
The core insight is that an audio codec can be redesigned not just for compression but as a structured representation learner that explicitly disentangles semantically meaningful attributes (speech vs. background, then semantic vs. paralinguistic). The SOP+RST framework provides a principled way to enforce subspace separation via a combination of algebraic constraints and training objectives that mimic perceptual feedback. This moves beyond existing codecs that either treat audio holistically or only separate audio types at the signal level, and beyond speech-only codecs that fail under noise. The demonstration that a single model can then serve SE, VC, ASR, and TTS through simple representation recombination is a compelling proof of concept.

## Suggestions
1. **Improve background representation fidelity**: Investigate why SDR-B is negative—whether it is due to the RVQ, the orthogonality constraint, or the decoder—and attempt to improve it without harming SE performance. Reporting a separate background-only SDR on a test set with pure background would help clarify.
2. **Analyze the voicing mismatch problem in VC**: Provide an analysis of when voice conversion fails (e.g., by pitch difference or duration) and consider adding explicit pitch or duration control to improve WER.
3. **Include confidence intervals**: Report standard deviations or 95% confidence intervals for key metrics (especially SDR, WER, SIM) to strengthen reproducibility.
4. **Explore lower bitrate variants**: Ablate the number of RVQ layers to find a better quality-bitrate trade-off and compare with codecs at similar bitrates.

## Score and Decision
**Score**: 6 (borderline accept)  
**Decision**: Accept  

The paper presents a novel and well-executed framework for disentangled representation learning in audio codecs. The weaknesses—particularly the limited background reconstruction quality and moderate VC performance—do not invalidate the core contribution but prevent a higher score. The overall impact on the community, especially in unifying multiple audio tasks under a single model, is significant enough to merit acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>