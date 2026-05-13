# RFWave: Multi-band Rectified Flow for Audio Waveform Reconstruction

- Decision: Accept
- Scores: 8, 5, 5, 8, 8

## Abstract
Recent advancements in generative modeling have significantly enhanced the reconstruction of audio waveforms from various representations. While diffusion models are adept at this task, they are hindered by latency issues due to their operation at the individual sample point level and the need for numerous sampling steps. In this study, we introduce RFWave, a cutting-edge multi-band Rectified Flow approach designed to reconstruct high-fidelity audio waveforms from Mel-spectrograms or discrete acoustic tokens. RFWave uniquely generates complex spectrograms and operates at the frame level, processing all subbands simultaneously to boost efficiency. Leveraging Rectified Flow, which targets a straight transport trajectory, RFWave achieves reconstruction with just 10 sampling steps. Our empirical evaluations show that RFWave not only provides outstanding reconstruction quality but also offers vastly superior computational efficiency, enabling audio generation at speeds up to 160 times faster than real-time on a GPU. An online demonstration is available at: \url{https://rfwave-demo.io/rfwave/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper the authors propose a new model called RFWave (Rectified Flow Wave) for achieving audio reconstruction from Mel Spectrograms or Encodec tokens. They propose training an efficient ConvNeXtV2
 backbone (a state-of-the-art convolutional architecture) using the rectified flow (diffusion) paradigm, that operate on STFT spectrograms bands for improved efficiency (than training directly in waveform domain). Each spectrogram band is processed independently by the network, and are concatenated before the inverse STFT (differently than the previous Multi-band Diffusion conditional approach of Roman et al. 2023, in which error accumulates from low to high frequency bands). The model can be trained both by performing the noising in time-domain, where is data is mapped first to STFT and back via the iSTFT before applying the loss, or trained
directly in STFT domain (authors show improved results on time-domain nosing approach). Methodologically the authors propose three new losses and new sampling algorithm for rectified flow. The losses are: a weighted loss which scales the STFT band by the variance of the ground truth velocity band (which is proportional to its energy), such that nearly-silent portions of data do not result in noisy outputs, an overlap loss which equalises
the outputs of different bands at their boundaries and an STFT loss computed via the rectified flow prediction at time $t$. The novel sampling algorithm choses sampling times by subdividing the flow trajectory in intervals
 of equal straightness (the integral of the difference between the ground truth velocity direction and the predicted velocity). The authors perform a solid experimental evaluation, comparing both with recent diffusion-based models and SOTA GAN-based models, showcasing very good results.

### Strengths
- While methodologically the authors borrow many ideas from previous papers, e.g., the model architecture ConvNeXtV2 is not a novelty of the paper, and training in the STFT domain is a classic choice in audio deep learning, it is very interesting how the combination of those ideas can bring us closer on surpassing the fundamental limitations in efficiency of diffusion models from a practical point of view. Seeing in Table 7 that actually performing 10 inference step of RFWave we have a way higher realtime factor than a BigVGAN (while having similar quality performance on LibriTTS and improved OOD performance on MUSDB18) is a strong indication that the inference time gap between diffusion models and GAN models is finally disappearing. And the best thing here is that one obtains this reduction without having to resort to distillation techniques (which are notably difficult to perform, especially consistency distillation), but only resorting to reasonable design choices, especially the choice of the architecture.
- The results in the experimental section are very good for the proposed model, putting it as a novel strong baseline in the audio reconstruction setting. Additionally, the ablations in Tables 5 and 6 give a detailed view on why the design choices in the paper contribute to the overall performance.
- The proposed losses and the idea of equal straightness intervals are valuable not only in the audio reconstruction context but also more generally when dealing with other types of STFT based models / other generative settings for rectified flow models.

### Weaknesses
 - The paper in some parts is not very clear in its explanations. For example in the Energy-balanced Loss part of Section 3.2 (Loss Functions), from first (and repeated) readings, I could not understand what was the  problem with the MSE loss. After different readings I interpreted it in the following way: small absolute errors in silent regions contribute little to the overall MSE loss, so the model doesn't prioritize eliminating them. This means the model doesn't effectively suppress minor deviations in silent areas, resulting in perceptible noise. Thus larger errors in high-amplitude regions significantly impact the MSE loss, causing the model to focus more on reducing those errors during training. A more detailed explanation of this issue, perhaps with a visual example showing how the MSE loss behaves in different amplitude regions, would be beneficial. Another part that was not clear was all Section 3.3 (Selecting Time Points for Euler Method). Here, first, straightness should be defined for a time $s$, as $S(v, s)$, setting the definite integral from $0$ to $s$ (using $s$ to leave the $t$ in $dt$). I believe authors use this because they took it from the original paper on rectified flow. Then writing “allowing to take more steps in more challenging regions” is pretty confusing. The term “allowing” is not ideal, I would use “requiring”. I understood the concept thinking that if in an interval the straightness does not change much, it means that we can take bigger steps, saving on the overall number of steps. I please ask the authors to re-write these parts in a more understandable way.
- While the experimental sections is done in a good way as mentioned in the Strengths part, the fact that the authors trained RFWave on their proposed large-scale dataset (combining Common Voice 7.0, DNS Challenge 4, MTG-Jamendo, FSD50K and AudioSet) and that Vocos, BigVGAN, EnCodec, and MBD are evaluated using the public pre-trained models is somehow problematic: it could be that Vocos, BigVGAN, EnCodec, and MBD are under-trained with respect to the authors dataset. It is crucial to ensure a fair comparison by either training all models on the same dataset or by providing a detailed analysis of the dataset characteristics and their potential impact on model performance. The authors should at least show that the training sources are comparable, perhaps by providing statistics on dataset size, diversity, and audio quality.
- It would have been interesting to compare also with latent diffusion models, where the network operates in another domain that is more compressed as the waveform domain, maybe a fine-tuned version of Stable Audio Open, given their widespread adoption.

### Questions
Here I list questions and typos:
- Line 174: “can be” to “can be an”
- Line 184:  Fourier features of what? Of the noisy sample? How we concatenate the conditional inputs? They share same dimensionality?
- Line 205: If interleaved then shouldn’t be $2d_s$?
- Line 219: “For waveform equalization… computed during training” This part as well refers to PQMF? Or is distinct?
- Line 228: “Subsequent processing involves the dimension-wise mean-variance normalization of the complex spectrogram.” As well here there is the mean-variance normalization as in time domain?
- Line 246: Why compute the standard deviation and not the energy altogether? Is there any reason for this?
- Line 252: Space after the $\min$.
- Line 295: Isn’t $X_0$ the data point and $X_1$ the noisy point? So shouldn’t we approximate  the STFT Loss using $X_0$?
- Line 307: “filed” is “field”.  In the integral use $\mathbb{E}$. Also I think the straightness should have argument a time $s$ (see Weakness section).
- Line 382: Why snake activation enhances out-of-domain data generation capabilities?
- Line 384: Isn’t this imputable to the architecture choice more than the type of generative model?  Especially upsampling layers as empirically shown here: https://arxiv.org/pdf/2010.14356 ?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
An efficient diffusion-based vocoder is proposed. The strengths of this paper are claimed to be that it generates the complex spectrogram of STFT at the frame level and that it can be generated in 10 denoising steps.

### Strengths
- Experimental results have demonstrated superior sound quality across multiple metrics compared to conventional methods.
- The strength of this paper appears to lie in the application of the latest technique, rectified flow, which enables efficient sampling. This aspect of the work stands out as a significant contribution.
- This work introduces three additional loss functions to improve performance. The additional loss functions appear to consistently improve performance.

### Weaknesses
 - The task addressed in this paper is rather conventional, using standard datasets and common evaluation methods. As a result, the work comes across as a minor variation of existing research. While this is certainly important work, it lacks a clear element of originality. It is unfortunate that, in a field where many similar approaches already exist, this work appears to be another study that only slightly improves existing benchmarks.
- Moreover, the approach is not theoretically groundbreaking either. At first glance of the contribution part, the proposed method appears to be a combination of existing ideas, making its originality and novelty less immediately clear. Specifically, the use of rectified flow, while effective for efficient sampling, is not a novel concept in itself, and its application to the STFT domain, while potentially beneficial, does not represent a significant theoretical leap. The introduction of additional loss functions, while improving performance, also feels like an incremental improvement rather than a fundamental breakthrough.
- Some spectrograms are shown, but the differences are not immediately apparent, making it unclear what aspects should be evaluated. It would be helpful to provide a little more explanation rather than leaving the interpretation up to the reader saying see the high-frequency components. The visual differences are subtle, and without a clear guide on what to look for, it's difficult to assess the claimed improvements, especially regarding the harmonic content.

### Questions
- I find it difficult to understand the rationale behind dividing into subbands when working in the STFT domain. If we are considering the STFT, it seems that the signal is already inherently divided into frequency components. 
  - Also, this paper mentions introducing a loss related to overlap in order to mitigate inconsistencies caused by subband division. However, inconsistencies between subbands are not limited to adjacent bands but may also impact the coherence of harmonic components. This could also be considered a potential drawback of subband division. 
  - The paper claims improved performance on harmonics compared to conventional methods with some empirical examples, but it is not clearly justified why it is effective.

- The STFT introduces redundancy in the representation due to overlapping frames compared to the original waveform. Consequently, the assertion that complex STFT spectrograms could be generated much faster than waveforms is not immediately intuitive. A more detailed and clearer explanation is required to substantiate this claim.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers a method for reconstructing the waveform from Mel-spectrogram or discrete acoustic tokens. The method generates complex spectrograms and performs reconstruction on a frame level.  Reconstruction is performed using a straight transport trajectory, which is achieved in a few sampling steps. Audio generation can be achieved much faster than in real time.

### Strengths
Audio reconstruction from Mel-spectrogram is achieved with a few sampling steps, and audio is generated much faster than in real-time.

### Weaknesses
1. Algorithm Flow and Domain Clarity:
The paper suffers from readability issues, making it challenging to understand the overall flow of the proposed algorithm. Specifically, it is unclear whether the algorithm operates in the time domain, frequency domain, or both, as it seems to suggest that transitions between these domains are possible but lacks a clear explanation or visual aids (e.g., a flowchart). This lack of clarity weakens the reader's comprehension and hinders an appreciation of the technical merits of the algorithm. It would benefit the authors to provide a visual or detailed description to convey these aspects effectively.

2. Assumptions about Input Data (Mel-Spectrogram):
The paper assumes a mel-spectrogram input to produce waveform output. However, it does not clarify how this mel-spectrogram is initially obtained or what assumptions are made about the input data. Understanding the starting point and any assumptions about preprocessing steps is crucial to assessing the practicality of the proposed algorithm. The authors should explicitly state these assumptions and briefly explain how mel-spectrograms are typically derived in relevant application contexts.

3. Frequency and Time Domain Operations:
Whether the multiband rectified flow is used to reconstruct the complex spectrogram or the waveform directly remains ambiguous. While the paper mentions using the short-time Fourier Transform (STFT), which implies frequency-domain operations, it also suggests waveform reconstruction capabilities. This lack of specificity raises questions about whether the algorithm operates exclusively in one domain or both. A more precise discussion of domain-specific processes, including the role and interplay of STFT in this context, would enhance the reader’s understanding and the algorithm's technical robustness.

4. Role of ConvNeXt V2 and Learning Velocity:
The role of ConvNeXt V2 in learning the velocity field is unclear. Given that ConvNeXt V2 is a recent architecture capable of supervised and self-supervised learning, understanding how it contributes to the velocity-based learning within the algorithm is essential for evaluating the approach's novelty and effectiveness. A clear outline of ConvNeXt V2’s integration and function in this context, especially concerning velocity learning, would clarify the methodology and strengthen the reader's ability to assess its value.

5. Waveform Generation from Complex Spectrogram:
The method for generating the final waveform from a complex spectrogram is not well-explained. Although the paper references GAN-based methods, it lacks a detailed description of how this process is implemented in the proposed model. An explicit explanation of the techniques used to transition from the complex spectrogram to the waveform would clarify the reconstruction process, making it easier to evaluate the proposed method's strengths and limitations.

6. Independent Subband Reconstruction:
The decision to reconstruct subbands independently raises concerns about consistency across subbands. While the paper suggests that independent reconstruction mitigates error accumulation, it overlooks the strong correlations typically present among subbands, which, if neglected, may compromise audio quality. Discussing the potential drawbacks of independent subband reconstruction and any strategies for inter-subband consistency checks would address this issue, making the approach more comprehensive and practical.

7. Reconstruction Speed-Up Justification:
Although the algorithm claims to achieve a reconstruction speed over 100 times faster than real-time, it is unclear whether such a significant speed-up is necessary or beneficial for practical applications. While computational efficiency is generally advantageous, the paper could explore the trade-offs between speed, model complexity, and audio quality to justify the need for such extreme speed-ups in relevant application scenarios. A deeper analysis here could reinforce the practical relevance of the proposed method.

8. Novelty and Engineering-Based Solutions:
The paper's novelty is in question, as it mainly combines existing components (multiband rectified flow and ConvNeXt V2) rather than proposing a fundamentally new approach. While this engineering solution may have merit in specific applications, the lack of novel contributions limits the paper's impact. Strengthening the theoretical foundation or providing a unique methodological contribution would be beneficial in highlighting the algorithm’s distinct value.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces RFWave, a new method for reconstructing audio waveforms from Mel-spectrograms or discrete acoustic tokens. The proposed method operates on Mel-spectrogram frames and produces spectral subbands in parallel, boosting synthesis speed. Additionally, the paper presents several heuristics aimed at speeding up inference and improving quality, namely: scaling flow-matching loss based on frame energy, adding MSE loss on overlapping parts of predicted frames, incorporating STFT loss on the estimation 𝑋_1​ at time 𝑡, and selecting optimal points for the Euler method. The model consistently outperforms diffusion-based baselines and performs on par with GAN-based methods. The experiments demonstrate that RFWave achieves a good trade-off between generation speed, memory consumption, and sound quality.

### Strengths
- The paper is well written and easy to follow;
- The introduced heuristics are intuitive and reasonable;
- The experiments clearly demonstrate better performance of the proposed method compared to diffusion-based baselines and give good understanding of pros and cons compared to GAN-based ones.

### Weaknesses
 - Interpretation of the experimental results aren’t always supported by the data provided in the corresponding tables. 
For instance, 1) according to the authors, Table 3 demonstrates significant advantages over GAN-based methods but the confidence intervals overlap in all scores accept one (“Mixed”, which, however, may be the most important one). I think that a significance test may help to emphasize the superiority of your method. 2) the same problem with overlapping MOS intervals appears in Table 4. At least, MOS evaluation doesn’t support the claim that RFWave “excels” in all metrics being very close to MBD in the key subjective metric. 
- Although Table 3 demonstrates better performance of RFWave on out-of-domain data, I still have doubts that such experimental setting  is practical: in a real-life scenario one would rather re-train a waveform generation model on the target domain (music in this case) than use a model trained on an out-of-domain data (speech). I would consider testing performance of BigVGAN fine-tuned on small amount of music data to get better understanding of advantages of RFWave brought by its better performance on out-of-domain data.
- Minor issues: “Tables 2” p.8:378, “velocity filed”, p.6:308

### Questions
- BigVGAN repository provides several versions of the model. Did you compare the performance of RFWave with the smaller ones in terms of sound quality and inference speed? Adding more flavors of BigVGAN into Table 7 would give better understanding of the strengths of your method.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The present paper proposes RFWave, a rectified flow model for reconstructing audio waveforms from mel spectrograms or discrete tokens (EnCodec codes). The authors design their model to operate on slightly overlapping subbands, allowing for parallelized inference at greatly improved computational efficiency without introducing artifacts at the borders between subbands. The authors propose an energy-balanced loss and several auxiliary losses to enhance the output quality. The method shows highly competitive performance on the evaluated tasks compared to SOTA baselines, at an improved tradeoff between quality and inference speed.

### Strengths
The presented method is original in this application context, combining several existing works and ideas (rectified flow, ConvNeXt architecture, sub-band processing) with some problem-specific novel losses (energy-balanced loss, subband overlap loss) and a specialized time-point selection method for the ODE solver used for inference.

The evaluations show that the method offers a new exciting point along the tradeoff between inference speed and quality. It outperforms most baselines in audio quality and performs similarly to, or better than, BigVGAN while having only ~20% of the parameters, running more than twice as fast, and using ~40% less memory. The authors further conduct convincing ablation experiments on their proposed components.

The paper is overall structured well and written clearly, with both the clarity of the technical description and the use of language being good in general.

### Weaknesses
Some claims and described methodology lack clarity and should be expanded upon or rewritten more clearly.

* The description of the conducted subjective listening experiment is extremely terse with only a single sentence (lines 352-354). In my opinion, this is insufficient as several details here are key for the reproducibility and reliability of these results. It is necessary to add details on the used platform/service for evaluation, the number of listeners, the number and type of samples per listener, and ideally also the audio equipment used by listeners.

* Figure 1 is insufficient for understanding the model architecture. Specifically, I did not understand how the fusion of the $X_t$ and $C$ occurs before the linear block. The EnCodec bandwidth index $i_{bw}$ also occurs without further motivation or explanation here and is somewhat unclear.

* The relationship between the PQMF bank (lines 207-221) to the complex spectrogram feature-space representation (see abstract) is somewhat unclear. What is really used as input/output of each model variant?

* I appreciate that the authors provide an online demonstration, which is essential for the trustworthiness of the results. However, the selection of samples is suboptimal, particularly for speech where the ground truth signals are of low quality and affected by artifacts. 
Please replace these or add new samples of higher ground-truth quality.

* The authors argue that using lower-frequency bands to predict higher-frequency bands can negatively impact the higher-frequency bands (lines 142-146), but later also argue that doing so can potentially increase consistency between bands (lines 280-281). Conditioning higher on lower bands is also not the same as processing all bands jointly (since there, also lower bands are estimated based on higher bands), so I do not fully follow the argument made here. The exact argument pro/contra processing low- and high-frequency bands jointly (or not) is somewhat unclear - please clarify.

* The authors seem to have convincing results for their "equal straightness" variant (Table 5), but somehow do not include these (at least) in Tables 6 and the comparison with diffusion-based methods, as they also note in the footnote on page 7. It is unclear to me why this is. Please update all metric results to present what the final RFWave variant is consistently, or list both the equal-straightness and non-equal-straightness variants in all relevant experiments for comparison.

* While the objective and subjective metrics speak for the method, from the online demo I find that the authors' method can introduce a kind of colorization and phasy artifacts that are not present in other methods, which are however not discussed in the paper. For transparency, could the authors add a short discussion of this limitation and potential reasons for it?

* The difference between Algorithm 1 (time-domain sampler) and Algorithm 2 (time-frequency domain sampler) seems too minor to plausibly explain why the time-frequency domain sampler performs significantly worse in Table 5 (row "frequency", see in particular the PESQ value). The only difference, the added STFT and iSTFT, are both **linear** operators, so they should not make a meaningful difference for the update $v_t \cdot dt$ from each Euler step. The only difference is that the STFT is higher-dimensional than the time-domain signal, so not all possible complex spectrograms $X$ are consistent (valid STFTs), and hence one must in general project a complex spectrogram to the time domain and back to the time-frequency domain ($	ext{STFT}(	ext{iSTFT}(X))$) to ensure a complex spectrogram is consistent. All that Algorithm 1 seems to add is an implicit consistency projection on the predicted velocity $v_t$ by performing the iSTFT on it, but it is not clear why this is reasonable (the velocity $v_t$ does not itself correspond to a natural time-domain signal), and especially why it makes such an important quality difference. I would appreciate if the authors could make any clarifying remarks regarding this or, if not possible, well-reasoned speculation.

* The authors' claim that the iSTFT operation introduces periodic signals that can enhance harmonic structures, similar to the Snake activation, is not convincing. The iSTFT only creates meaningfully harmonic signals when there is organized sparsity in the frequency domain, but it is also perfectly capable of synthesizing white noise when the time-frequency coefficients are white noise (e.g. approximately for sibilant sounds), and does not meaningfully introduce harmonicity to the signal in this case.

* Additionally, the statement that the authors' model "can operate with noisy sample in either the time or frequency domain" is rather confusing. It suggests that either a larger part – e.g. the network architecture, feature extractor, etc. – must be modified to get a model that can operate in either of those domains or, alternatively, that the authors have made a novel and special modification to the network to allow for the network to accept both time and time-frequency representations. Only through the discussion and the authors' explanatory remarks here did I understand that the only modification is one made to the sampler.

### Questions
* Were any methods trained on multiple types of audio (speech, music, sound) at the same time, or was a specialized model prepared of each RFWave and retrained baseline for *every* audio type? This is not clear to me from line 344, which would suggest that baselines were trained on multiple audio types at the same time, whereas Appendix A.2 suggests that RFWave was trained on every single dataset separately. If the authors compare dataset-specialized RFWave against multi-dataset baselines, such a comparison would be unfair.

* For completeness and better understanding, I would suggest adding a pointwise metric such as a simple L2 distance (or SNR in dB) of the reconstruction compared to the ground truth. I am asking since the presented metrics (MOS, PESQ, ViSQOL, F1, Periodicity) do not provide much insight in how the methods compare regarding pointwise distortion, but this is an important property, especially for the decoding task.

* The authors do not use the rectification step that a rectified flow model enables in principle, correct? Can they provide a reasoning for why they do not perform this step, which in theory should help improve the inference efficiency by further reducing the necessary number of sampling steps?

* Lines 47, 54-56, 70-71: It is a priori unclear why operating on STFT frames should be more efficient than operating on a waveform, since the STFT is redundant and introduces more data points to process. This seems to be more about frame-parallel processing of the DNN architecture rather than the STFT itself, could the authors clarify what they mean?

* In Section 3.3, what is meant precisely by timepoints being "chosen such that the increase in straightness is equal across each step"? I would have liked a more concrete description of the method used to obtain the time steps here - was this optimization-based, or somehow estimated in closed-form? What was the formal metric used to judge "equal straightness" across all intervals?

* What do the authors really mean by one model variant being capable of "operating in the time domain" (line 197-199)? In the abstract, the authors state that RFWave "generates complex spectrograms" -- in a flow/diffusion setting, shouldn't then the feature-space input also be a complex spectrogram? In this case, an STFT/iSTFT is used, and the ConvNeXt model performs 2D convolutions, and operates in the time-frequency domain, not in the time-domain, right? Please clarify this point here and also in the paper.

Minor points:

* In lines 204-206, the authors state that they interleave real and imaginary parts of each subband. Wouldn't this lead to a $2 d_s$-dimensional feature rather than a $d_s$-dimensional feature? (Same comment in line 227 where this notation is repeated)

* When the authors say "dimension-wise" (line 228), do they mean only $d_s$, or only $F$, or both $d_s$ and $F$?

* Can the authors add a reference for the claim that "speech energy decays exponentially with frequency, while music maintains a consistent distribution"? (lines 207-209)

* I do not follow the argument made in 3.2, lines 237-242, regarding MSE-based training. If "minor absolute distortions lead to significant relative error", shouldn't a model trained by minimizing MSE *avoid* such small absolute distortions rather than producing them? To me, the observation that the model exhibits residual noise sounds rather like a time-weighting or noise schedule issue than a problem with the MSE used within the training target?

* In the experimental setup section (4.1), I would suggest explicitly referring to Appendix A.1 which lists further training hyperparameters - I could not find such a reference and was missing these details in the main text before finding them in the appendix by chance.

* In the appendix, please provide (visually or quantitatively) the dynamic range used for producing each selection of shown spectrograms.

Typos:

* Lines 364 and 372: "Comparasion" -> "Comparison"
* Line 511: "lenght" -> "length"
* Table A.5: "PriroGrad" -> "PriorGrad"

### Soundness
3

### Presentation
3

### Contribution
3
