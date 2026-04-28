# FlowDec: A flow-based full-band general audio codec with high perceptual quality

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
We propose FlowDec, a neural full-band audio codec for general audio sampled at 48 kHz that combines non-adversarial codec training with a stochastic postfilter based on a novel conditional flow matching method. Compared to the prior work ScoreDec which is based on score matching, we generalize from speech to general audio and move from 24 kbit/s to as low as 4 kbit/s, while improving output quality and reducing the required postfilter DNN evaluations from 60 to 6 without any fine-tuning or distillation techniques. We provide theoretical insights and geometric intuitions for our approach in comparison to ScoreDec as well as another recent work that uses flow matching, and conduct ablation studies on our proposed components. We show that FlowDec is a competitive alternative to the recent GAN-dominated stream of neural codecs, achieving FAD scores better than those of the established GAN-based codec DAC and listening test scores that are on par, and producing qualitatively more natural reconstructions for speech and harmonic structures in music.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes FlowDec, a 48 kHz general audio codec with a flow-matching diffusion post-filter. FlowDec modifies the DAC audio codec with different loss functions, the stochastic post-filter, and frequency-dependent noise. Evaluations demonstrate strong improvements over prior post-filter and diffusion-based methods, but only small improvements over DAC.

### Strengths
Figures 2 and 3 are great visualizations for the diffusion dynamics and proposed improvements.

Good selection of baselines, including retraining baseline models to account for differences in parameter count.

The authors mention that they will be open-sourcing their code.

### Weaknesses
You should consolidate the six main contributions. I recommend at most three or four. Some of the contributions currently listed seem minor, or are a side effect of another contribution.

A primary issue with the proposed system is RTF. The logical alternative (DAC) is still orders of magnitude faster. I do still think this is an important paper in helping close the gap.

A minor note, but a 44.1 kHz sample rate is sufficient to prevent audible aliasing above 20 kHz. The other rationales given for using 48 kHz over 44.1 kHz are convincing enough for me.

### Questions
The NeurIPS 2023 oral by Kingma and Gao unifies under a common framework the diffusion variants of, e.g., flow matching and optimal transport. This could be useful, given that both are discussed in your work. You might also take a look at their Appendix J, which has some discussion of the frequency analysis of diffusion noise that may have some overlap with your proposed frequency-dependent noise.

Can we hear some audio examples? It is difficult to judge the results otherwise, and the MUSHRA test (unlike an AB or ABX test) doesn't provide sufficient granularity to discern statistical significance between, e.g., FlowDec and DAC.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces FlowDec, a neural audio codec with a two-stage approach: (1) an autoencoder with residual vector quantization, trained without adversarial loss, and (2) a postfilter that reduces coding artifacts and enhances perceptual quality. FlowDec adapts conditional flow matching for signal enhancement, achieving improvements over previous score- and flow-based models. Both listening tests and objective metrics show that FlowDec provides perceptual quality competitive to state-of-the-art GAN-based codecs.

### Strengths
- The paper is well-written, with clear explanations and informative illustrations that help clarify key points.
- It provides useful context relative to previous score-based models. It also includes valuable theoretical insights and formalism to support its approach.
- It performs on par with state-of-the-art GAN codecs and shows slight improvements for speech signals. FlowDec may handle high-frequency harmonics better, where GAN-based codecs often introduce periodicity and harmonic artifacts.

### Weaknesses
The paper introduces FlowDec as a codec, but its primary focus seems to be a flow-based postfilter that enhances outputs from an *underlying* codec. The main weakness of this paper is the decision not to explore a GAN-based codec combined with the proposed postfilter. The paper argues against adversarial training in Section 3.3, stating that the “generated phase may be very different from the original phase.” However, FlowDec itself doesn't seem to preserve phase. Results presented in Section 5.1 show that FlowDec performs worse than GAN-based codecs in terms of SI-SDR and fwSSNR, which are sensitive to phase shifts. This might still be acceptable for a low-bitrate codec, particularly if perceptual quality is prioritized. However, the paper should more clearly justify why a GAN isn't used as the underlying codec. A GAN-based codec with a flow-based postfilter might not only reduce coding artifacts but also achieve higher reconstruction metrics. This would call into question the rationale behind the proposed non-adversarial DAC (NDAC) model. Overall, the distinction between FlowDec as a novel audio codec and its role as an enhancement tool for *any* audio codec could be clarified. The paper does not adequately address the potential benefits of using a GAN-based codec as the initial stage, particularly given that the proposed flow-based postfilter is designed to refine the output of *any* codec. The argument against adversarial training, based on phase discrepancies, is not fully convincing since the proposed method also exhibits phase-related limitations as indicated by the SI-SDR and fwSSNR metrics. The paper should provide a more thorough comparison of the proposed NDAC with a GAN-based DAC, including a detailed analysis of the spectral characteristics and artifacts produced by each, to justify the choice of NDAC as the initial stage.

### Questions
1. Could the authors clarify the main purpose of FlowDec? Why is it presented as a standalone codec rather than positioning the postfilter as an enhancement tool?
2. What is the rationale for choosing to enhance only outputs from a non-adversarial codec instead of using GAN output as the initial estimate for FlowDec's postfilter? Could the authors specify what benefits NDAC offers over DAC in this proposed two-stage setup?
3. The STFT settings seem unconventional. A 1534-point FFT would definitely be slower than a 1536-point FFT due to FFT efficiency with highly composite sizes. I assume the goal is to get exactly 768 frequency bins, but why not just use a 1536-point FFT with 769 bins? Overall, this may be negligible given the slower inference, but I'm curious about the tradeoff here.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
FlowDec is an improved version of ScoreDec (uses a score-based generative model as a postfilter), by switching the objective to flow matching. It further proposes a joint flow matching objective tailored for the postfiltering task (e.g. mean-shifted noise with frequency-dependent diagonal covariance). This makes it faster than real time (unlike ScoreDec) as a practically viable, full-band, and universal audio codec without adversarial training.

### Strengths
* Contrary to adversarial training (a dominant approach in vocoder/codec) which requires domain specific expertise to stabilize training and tune the hyperparameters of multiple losses, FlowDec simplifies the trianing pipeline by elimiating the adversarial losses. In my opinion, this can be considered as one of the first work that achieves competitive quality to GAN-based models with RTF < 1. 

* The proposed design choice is well justified overall, both in the theoretical and empericial perspective. It provides enough rigor in experimental detail, including toy experiments and detailed ablation study of each component.

### Weaknesses
 * While the evaluation results from the paper look convincing overall, no demo page has been provided at submission. It's hard to form the reviewer's opinion on the subjective quality without access to the demo. I hope the authors can provide the samples for the reader to evaluate the subjective quality themselves. 

* Although it improved the RTF by a large margin, it still requires multiple NFE from the postfilter resulting in RTF of 0.22-0.23 which is considerably slower than recent, feed-forward audio codecs. This RTF, while faster than ScoreDec, still represents a significant computational overhead, which may limit its practical applicability in real-time scenarios. The multiple NFE required also implies a non-trivial latency, which is a critical factor for interactive audio applications. Furthermore, the paper does not provide a detailed breakdown of the computational cost per NFE, making it difficult to assess the potential for further optimization.

### Questions
There have been several concurrent works adopting flow matching with similar task (i.e. mel spectrogram vocoder and discrete codec decoder), such as RFWave [1] and PeriodWave [2,3]. These work directly utilize flow matching as the decoder rather than postfilter, with several configs being order of magnitude faster than this work.

While the direct comparison may not be strictly necessary, can the authors provide conceptual comparisons between the aforementioned methods along with possible advantages of FlowDec?

[1] Liu, Peng, and Dongyang Dai. "RFWave: Multi-band Rectified Flow for Audio Waveform Reconstruction." arXiv preprint arXiv:2403.05010 (2024).

[2] Lee, Sang-Hoon, Ha-Yeong Choi, and Seong-Whan Lee. "PeriodWave: Multi-Period Flow Matching for High-Fidelity Waveform Generation." arXiv preprint arXiv:2408.07547 (2024).

[3] Lee, Sang-Hoon, Ha-Yeong Choi, and Seong-Whan Lee. "Accelerating High-Fidelity Waveform Generation via Adversarial Flow Matching Optimization." arXiv preprint arXiv:2408.08019 (2024).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce FlowDEC, a flow matching-based post-filtering method designed to enhance the audio quality decoded from discrete audio tokens. This method has demonstrated strong objective and subjective results.

### Strengths
- Possibly the first application of flow matching in postfiltering.
- Beautiful experiment result plots and strong objective and subjective results.
- Enhance DAC by incorporating a multi-scale Constant-Q Transform (CQT) loss.

### Weaknesses
 - The latency of the proposed method is at least an order of magnitude higher than that of DAC. To facilitate a comprehensive evaluation, it would be beneficial to receive specific latency measurements for both the proposed method and the DAC. Furthermore,  identifying the applications or use cases that could be critically impacted by this higher latency would provide valuable context. Moreover, to support the validation of the method’s performance, it would be advantageous if the authors could provide an online demo that allows for direct comparison of the latency between the two methods.
- The baselines are limited. There are other diffusion-based works that reconstruct audio waveforms from discrete tokens, e.g. Multi-band diffusion [1]. 
- The concept of selecting a data-dependent prior, as proposed, is not entirely novel, with works such as Priorgrad [2] having implemented a similar strategy. To better understand the relationship between the proposed method and existing approaches, it would be helpful to have a clearer comparison of their similarities and differences. 
- Multi-band diffusion [1] uses frequency-dependent noise levels, which is a notable feature that could be further discussed in comparison to the proposed method.



### Questions
-  The question arises as to why the waveform is not reconstructed directly from discrete tokens using flow matching. To provide a more comprehensive evaluation, could you elaborate on the potential computational or quality trade-offs between direct reconstruction via flow matching and the method proposed in the paper?
- Regarding line 168-171, the presence of $p_{data}(\cdot|y)$ is not clear as it seemingly should just be $p_{data}(x)$. This needs further clarification and justification.
- From line 220 to 223 and in Figure 2, it may be inappropriate as we cannot obtain $x_1$ for real postfiltering problems. This aspect requires reconsideration or better explanation.
- In Figure 3, the use of a large $\sigma_t$ of 0.1 o illustrate that FlowAVSE is non-contractive is not convincing, especially since the original FlowAVSE employs a value of 0.04. It would be beneficial for the authors to provide a clearer explanation for this choice or consider revising the value used. 
- As $y$ is a time-domain signal, it is unclear how to apply frequency-dependent $\sigma_y$ since it cannot be directly applied. The authors need to provide more details on this aspect.

### Soundness
2

### Presentation
2

### Contribution
2
