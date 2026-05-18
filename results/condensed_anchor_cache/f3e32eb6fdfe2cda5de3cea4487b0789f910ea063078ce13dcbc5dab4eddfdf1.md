- Decision: Accept
- Scores: 8, 3, 5, 8, 8

## Merged Review

### Summary

CLaM-TTS is a zero-shot TTS system that employs a probabilistic residual vector quantization (Mel-VAE) to encode mel spectrograms into discrete codes at a low frequency (10 Hz codeword rate), and a language model with a Gaussian mixture model (GMM) decoder that outputs continuous values later discretized via RVQ. This design allows the model to generate multiple tokens per step, eliminating the need for a two-stage coarse-to-fine pipeline and reducing sequence length. The system is trained on 100k hours of multilingual data and evaluated on continuation and cross-sentence tasks. Experimental results show performance competitive with or better than state-of-the-art codec-based TTS models on naturalness, intelligibility, speaker similarity, and inference speed. The paper also examines the impact of LM pretraining extent and text tokenization strategies.

### Strengths

- **Clear presentation and detailed derivation.** The paper is well-organized and accessible, with hyperparameters in the appendix, reasoning for architectural choices, and a comprehensive mathematical analysis of the probabilistic RVQ (Reviewers 1, 3, 5). Reviewer 4 notes the derivation helps understand the method. However, Reviewer 2 found the paper dense and difficult to follow, especially the explanation of parallel token generation.

- **Novel approach to audio tokenization and modeling.** CLaM-TTS uses a GMM as the output distribution of the LM, avoiding the need for a cascaded coarse-to-fine sampling scheme and addressing long sequence and multiple-stream issues of prior codec LMs like VALL-E and AudioLM (Reviewers 1, 4, 5). The probabilistic RVQ enables generating multiple codes per step, significantly compressing token length and speeding inference (Reviewer 4, 5). Reviewer 2 acknowledges the interesting approach to generating low-frequency RV codes suitable for LMs.

- **Strong experimental methodology.** The evaluation includes strong, recent baselines; varied metrics (MOS, WER, speaker similarity, RTF); and both successes and failures of the method are highlighted (Reviewer 1). Ablation experiments verify the effect of the proposed RVQ and the importance of the pretrained language model (e.g., T5 variants) (Reviewer 3). Experiments demonstrate superior RTF compared to Voicebox and VALL-E (Reviewer 5).

- **Competitive performance.** The model achieves good performance on continuation and cross-sentence tasks, with results comparable to or better than current codec-based TTS models (Reviewers 1, 4). It appears grounded in theory (Reviewer 2).

### Weaknesses

- **Missing ablation: single-stage vs. two-stage pipeline.** The paper claims their continuous modeling approach avoids two-stage coarse-to-fine generation, but no side-by-side comparison with a two-stage variant of CLaM-TTS is provided to support this claim (Reviewer 1).

- **Missing scaling analysis.** It is unclear whether training on 100k hours or increasing model size is beneficial. Comparisons with smaller models or smaller data amounts would clarify if the model exploits scale (Reviewer 1).

- **Performance relative to strong baselines.** Voicebox significantly outperforms CLaM-TTS on some metrics; the paper attributes this to duration prediction and phone input, but this is a weak excuse since many TTS systems use that recipe (Reviewer 2). In most tasks, the model does not achieve state-of-the-art results despite claiming performance (Reviewer 3). Some baselines outperform on certain metrics (Reviewer 1).

- **Presentation issues.** The paper is dense and difficult to follow; the claim of parallel generation of multiple tokens is not clearly explained (Reviewer 2). Conversely, Reviewers 1, 3, 5 found the paper clear. The paper contains a typo: “ablation studty” (Reviewer 2). There are missing references, most notably Vq-wav2vec as one of the first speech vector quantization techniques (Reviewer 2). Reviewer 4 notes that \(y\) and \(\hat{y}\) in Eq(7) are never defined.

- **Limited novelty.** VAE or latent diffusion models are not new, so the overall novelty can be questioned (Reviewer 3). Other reviewers consider the CLaM approach a significant innovation (Reviewers 1, 4, 5), but this disagreement should be noted.

- **Incomplete experimental comparisons.** The English LibriSpeech comparison uses the outdated model YourTTS; multilingual comparisons are missing many competing models; and the demo website has too few samples, lacking audio from other works for direct comparison (Reviewer 3).

- **Missing ablation/analysis of codeword rate.** The paper mentions comparing different codeword rates but does not provide an empirical study of how token frequency (e.g., 10 Hz vs. 50 Hz) affects quality, RTF, or speaker similarity. Such an analysis is requested to explain the trade-off and understand why probabilistic RVQ leads to compressed sequences (Reviewers 2, 4, 5).

- **Clarification needed on why mel spectrograms are necessary.** The paper uses mel spectrograms to achieve compression; it is unclear why progressive downsampling of raw waveforms cannot achieve the same effect (Reviewer 2).