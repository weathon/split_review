# PeriodWave: Multi-Period Flow Matching for High-Fidelity Waveform Generation

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Recently, universal waveform generation tasks have been investigated conditioned on various out-of-distribution scenarios. Although GAN-based methods have shown their strength in fast waveform generation, they are vulnerable to train-inference mismatch scenarios such as two-stage text-to-speech. Meanwhile, diffusion-based models have shown their powerful generative performance in other domains; however, they stay out of the limelight due to slow inference speed in waveform generation tasks. Above all, there is no generator architecture that can explicitly disentangle the natural periodic features of high-resolution waveform signals. In this paper, we propose PeriodWave, a novel universal waveform generation model. First, we introduce a period-aware flow matching estimator that can capture the periodic features of the waveform signal when estimating the vector fields. Additionally, we utilize a multi-period estimator that avoids overlaps to capture different periodic features of waveform signals. Although increasing the number of periods can improve the performance significantly, this requires more computational costs. To reduce this issue, we also propose a single period-conditional universal estimator that can feed-forward parallel by period-wise batch inference. Additionally, we utilize discrete wavelet transform to losslessly disentangle the frequency information of waveform signals for high-frequency modeling, and introduce FreeU to reduce the high-frequency noise for waveform generation. The experimental results demonstrated that our model outperforms the previous models both in Mel-spectrogram reconstruction and text-to-speech tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the task of speech and audio waveform generation using the flow-matching modeling paradigm. The authors proposed a multi-period approach to generation artifacts in high-frequencies, conditioned on either mel-spectrogram and discrete representation extracted from neural codecs. The authors compared the proposed method to several GAN-based approaches and two diffusion-based methods. The authors empirically demonstrated the proposed method reaches superior performance to the evaluated baselines.

### Strengths
1. The proposed method reaches superior performance to the evaluated baselines.
2. The authors presented results using both mel-spectrogram and discrete representation extracted from neural codecs.
3. The authors provide extensive ablation and analysis of the proposed method.

### Weaknesses
1. Limited novelty. It seems the proposed method applies the multi-band (MB) approach (using wavelets instead of MB) over the flow-matching approach rather than diffusion. 
2. Missing comparisons. As the proposed approach is heavily connected to the MBD approach [1], it is not clear why the authors did not compare to this method. 
3. Missing details and inaccurate details (see below).



### Questions
I have a few questions and concerns about this submission: 
1. As stated above, it seems the proposed method is heavily connected to the MBD work. What is the reason the authors did not compare their method to MBD? More generally, there are missing experiments to make the contribution of this work clear. At the moment, it is not clear what makes this method better than the prior work. Is it the flow-matching approach? Why not use v-diffusion instead? is it the usage of discrete wavelet transformation over MB? Etc. 
**Specific experiments to add:** Can the authors provide: (1) a direct comparison of the proposed method MBD using the same setup? (2) ablation study on the usage of flow matching vs. diffusion? (3) comparison of discrete wavelet transform to the multi-band approach used in MBD? 
2. There are missing details regarding the evaluation methods. Can the authors define the "Pitch" metric mean? How did the authors extract F0 information? What metric did the authors use to estimate F0 quality? Similarly for the other metrics reported in the paper.
3. Under the training paragraph, the authors mention that training (using 2 A100s) the proposed approach is faster as it requires 3 days, while it takes more than three weeks to train the GAN-based approaches. It seems quite a lot for the GAN-based methods. It makes sense training the proposed method would be faster, however, it seems quite a big difference. Can the authors provide more information on how they trained the baseline methods? More details about the training configurations for both the proposed method and the evaluated baselines? (i.e., batch sizes, learning rates, etc.). Alternatively, in case such training times were reported in prior work, a citation would be fine.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents PeriodWave, the first flow-matching based vocoder. It relies on a carefully designed multi-period estimator. The authors notably propose to use discrete wavelet transforms and FreeU to better render high frequency information. The model outperforms one-step GANs in TTS tasks. The paper shows that the proposed method not only works as a spectrogram-based vocoder but also for generating from discrete tokens. Source code and checkpoints will be made available.

### Strengths
Extensive experimental work that demonstrates the robustness of the proposed method on both in-domain (mono- and multi-speaker TTS) and out-domain (Music) data. Ablations properly highlight the design choices.

### Weaknesses
I wish there was some comparison with MBD, which is probably the closest model architecture-wise.

I am also curious about the specific implementation of temperature scaling. The paper mentions applying temperature to the Gaussian noise, but it's unclear if this involves simply scaling the standard deviation or if there's a more complex operation. A more detailed explanation of this process would be beneficial for reproducibility and understanding the method's behavior.

### Questions
- Section 4.4: How is temperature exactly applied to the gaussian noise? Is this just about scaling the standard deviation?
- What is the motivation for not comparing with MDB at all in the paper? MBD is conceptually very similar (although only applied to discrete representations and using diffusion). Please motivate this choice somewhere in the paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposed a flow-matching-based vocoder with improved high-frequency modeling and inference speed.

### Strengths
1. The paper proposed a practical flow-matching-based vocoder by significantly improving the high-frequency modeling issue with the existing flow-matching-based waveform generation method.
2. The proposed method shows decent performance compared to GAN-based methods. 
3. The proposed method achieves a good balance between quality and synthesis speed compared to conventional diffusion-based methods.

### Weaknesses
1. It is unclear if the hyperparameters from grid searching during FreeU are generalizable to other settings and datasets. Does the alpha and beta need to be re-adjusted under different inference settings and datasets? It seems the FreeU grid search is only conducted on a single-band model of the proposed methods. Did you test it on the multi-band version of Periodwave?
2. Since high-frequency modeling is the core innovation of the paper, it is recommended to perform analyses focusing on the high-frequency modeling capabilities. For example, measuring the fidelity of the high-frequency bands of the audio signal and comparing it to the baselines. During the out-of-distribution music dataset experiment, only vocal, drum, and bass were emphasized, where the bass is typically the low-frequency part. It would be interesting to analyze the high-frequency components of the music by showing for example, per-band SNR accompanied with detailed spectrograms.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a nove waveform generation model that can capture periodic features of waveforms using a period-aware flow matching estimator and further extend to multi-band estimator. 
Experimental results demonstrate that PeriodWave outperforms existing models in reconstruction tasks from mel and discrete tokens, as well as in TTS applications.

### Strengths
First time applying flow matching to waveform generation, and a method was designed to explicitly extract patterns with different periods to match the spectral characteristics of the waveforms. 
Incorporates the latest effective waveform modeling tricks, significantly enhancing the performance of the vocoder and the extraction of periodic features.

### Weaknesses
1: There is no comparison of the performance differences between flow matching and diffusion under the same network and optimized configurations.

2: The main contribution of this paper lies in the introduction of periodic features; while the choice of periods [1, 2, 3, 5, 7] versus [1, 2, 4, 6, 8] can be understood, the ablation study for [1] may be unfair regarding network parameters (5 layers for [1, 2, 3, 5, 7] and only 1 layer for [1]). It would be more appropriate to compare with configurations like [1, 1, 1, 1, 1], [1, 1, 1, 3, 3], or [1, 1, 1, 3, 9]. Additionally, deriving the reason for selecting period by prime based solely on this comparison may not be sufficient，

3: The experiments emphasize that the network structure primarily optimizes high-frequency information modeling, but this does not adequately demonstrate that the method is specifically related to high-frequency information，It would be better to use band-wise comparison metrics.

### Questions
1: If α<1, wouldn't it make it harder for the model to capture high-frequency features? 

2: The M-STFT metric is relatively low, a well-optimized model in the waveform space shouldn't show significant disadvantages in STFT metrics, is there any explanations?

3:A frequency of 22.05 kHz is not considered very high; it mainly contains harmonics, making it unclear whether the model's performance advantage stems from low-frequency modeling or high-frequency modeling.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Propose PeriodWave, a novel universal waveform generator that can reflect different
implicit periodic information when estimating the vector fields.
Thoroughly analyze the limitation of high-frequency modeling, and address this by DWT and FreeU approach for high-frequency noise reduction.
Present PeriodWave which outperforms the one-step GAN models in conventional two-stage TTS tasks.
Based on SOTA neural audio codec Mimi, successfully demonstrate the effectiveness of
PeriodWave in neural audio codec decoding task both in parallel and streaming generation.

### Strengths
Thoroughly analyze the limitation of high-frequency modeling, and address this by DWT and FreeU approach for high-frequency noise reduction.
Present PeriodWave which outperforms the one-step GAN models in conventional two-stage TTS tasks.
Present thorough experimentation do demonstrate the effectiveness of the proposed method.

### Weaknesses
Although the models can generate the waveform with small sampling steps, Table E shows that the models have a slow synthesis speed compared to GAN-based neural vocoders.
Shows a lack of robustness in terms of high-frequency information because they only train the model by estimating the vector fields on the waveform resolution.

### Questions
Please add the limitations section to the main paper and remove it from the appendix.

### Soundness
3

### Presentation
3

### Contribution
3
