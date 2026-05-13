# CM^2: Cross-Modal Contextual Modeling for Audio-Visual Speech Enhancement

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Audio-Visual Speech Enhancement (AVSE) aims to improve speech quality in noisy environments by utilizing synchronized audio and visual cues.
In real-world scenarios, noise is often non-stationary, interfering with speech signals at varying intensities over time.
Despite these fluctuations, humans can discern and understand masked spoken words as if they were clear.
This capability stems from the auditory system's ability to perceptually reconstruct interrupted speech using visual cues and semantic context in noisy environments, a process known as phonemic restoration.
Inspired by this phenomenon, we propose Cross-Modal Contextual Modeling (CM$^2$), integrating contextual information across different modalities and levels to enhance speech quality. 
Specifically, we target two types of contextual information: semantic-level context and signal-level context.
Semantic-level context enables the model to infer missing or corrupted content by leveraging semantic consistency across segments.
Signal-level context further explores coherence within the signals developed from the semantic consistency.
Additionally, we particularly highlight the role of visual appearance in modeling the frequency-domain characteristics of speech, aiming to further refine and enrich the expression of these contexts.
Guided by this understanding, we introduce a Semantic Context Module (SeCM) at the very beginning of our framework to capture the initial semantic contextual information from both audio and visual modalities.
Next, we propose a Signal Context Module (SiCM) to obtain signal-level contextual information from both  raw noisy audio signal and the previously acquired audio-visual semantic-level context.
Building on this rich contextual information, we finally introduce a Cross-Context Fusion Module (CCFM) to facilitate fine-grained context fusion across different modalities and types of contexts for further speech enhancement process.
Comprehensive evaluations across various datasets demonstrate that our method significantly outperforms current state-of-the-art approaches, particularly in low signal-to-noise ratio (SNR) environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed a deep learning model called Cross-Modal Contextual Modeling (CM^2), which utilizes both audio and visual cues to enhance speech quality in noisy environments. CM^2 combines two types of contextual information: semantic context and signal context. Experimental results show superior model performance over existing works.

### Strengths
The motivation is sound and clear
The paper reports SOTA performance on all metrics including SDR, PESQ, and STOI.

### Weaknesses
The weaknesses mainly come from technical writing problems and lack of clarity.

 - SiCM is defined, but it is not clear how it is used. This section appears to define the equations twice, which is unnecessary. Its inputs are not defined - what is $Q_{in}$ and how does it connect with the rest of the model? Use of mamba is interesting, bidirectional seems unusual - and they do not have experiments to back up this choice.
 - CM_2: 
	- Line 278 - should the notation be $B F_x \times T_x \times C$ instead?
	- Line 283 "diverging" is repeated.
	- Line 301 the $F_e$ and $F_p$ are not clearly defined (1d convolutions?). 
	- On equastions 6 and 7 add some spaces after the "..." and after the "," otherwise its too hard to read
	- Line 302: it should be "contains" not "contain"
	- 3.5 the use of the SiCM notation is a little confusing. Earlier, it refers to a specific set of Mamba-based operations, but here it is for the entire frequency processing and time processing modules. Please keep the nomenclature consistent. 
 - The Discriminator is mentioned but undefined. Papers need to be reproducible. 
 - The methods they compared to in the results tables are quite old. Would be interesting to compare with modern AVSS models by setting speaker 2 = noise.

Finally, while this is not a strict requirement, open sourcing the code after the paper's release would help understand the methods better, as the methods are quite convoluted.


In particular, the claim of ownership of the method of switching dimensions introduced in DPRNN is concerning. Specifically, in line 292, the authors state, "we introduce a Channel Swapping Block (CSBlock)." However, this approach is not the original work of $CM^2$, as it can be observed in the DPRNN paper and source code. This method has been employed consistently over the past five years, which was my primary reason for raising the ethics flag. The subsequent channel-swapping operation is also reminiscent of equations 23 and 24 of RTFS-Net, and the overall pipeline of $CM^2$ aligns closely with other works such as RTFS-Net, TF-GridNet, CTCNet and others. Another reviewer has also noted the failure to cite other significant papers in the field, which lead me to mistakenly assign the work in this paper as original contributions introduced by $CM^2$, instead of by the original authors. This omission is concerning, as I believe this style of writing could easily mislead others in a similar way. Sources should be properly cited and acknowledged. Despite this paper’s similarities to other work, with proper citing and referencing it would not be cause for concern.

### Questions
About evaluation, how do you make comparision with previous works under different signal-to-noise ratio conditions as I don't see this type of evaluation on most of the previous works?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a framework called Cross-Modal Contextual Modeling (CM2) to improve Audio-Visual Speech Enhancement (AVSE). CM2 integrates two types of contextual information—semantic and signal context—across audio and visual data to enhance speech quality in noisy environments. The semantic context helps the model infer missing or corrupted speech by maintaining consistency across segments, while the signal context leverages coherence within signal frames. Additionally, the approach emphasizes the importance of visual features, such as the speaker's facial cues, which can correlate with audio frequency characteristics, thus aiding the enhancement process.

The model uses three main components to build and integrate these contexts: a Semantic Context Module (SeCM) for initial contextual extraction, a Signal Context Module (SiCM) for signal-level context from noisy inputs, and a Cross-Context Fusion Module (CCFM) to combine these contexts. This architecture allows for detailed context fusion across different modalities, effectively improving speech clarity, especially in challenging low signal-to-noise ratios. Experimental results show that CM2 outperforms other state-of-the-art models, demonstrating substantial gains in metrics related to speech quality and intelligibility.

Methodology:
 - SeCM: Processes Video and Audio in Time Domain audio stream, proposes three solutions (V, PV, PAV) from other papers, and test to find the best approach.
 - Audio Encoder: Processes audio in TFM Domain, uses 4 stacked convolutions.
 - SiCM: uses a bidirectional Mamba approach to process along different dimensions and time directions.
 - Time-Frequency Upsampler: two transpose convolutions with BN and prelu. used to take the frequency dim from 1 to match the frequency dim of the other audio route.
- CSBlock: split across the channels and concatenate cross-modality information
- AF Block - Generate attention map by applying linear to P, use two SiMC on P^c and E^c, then multiply the mask by both features and they are added together. A 2d conv binds the information together.

### Strengths
The introduction and literature view show a strong and detailed narrative of their task, their goals and their contributions. It is well researched and has a comprehensive view of current methods, contextualising their methodology and results. Their methods section is long and detailed, with many interesting approaches to the problems that they face. They combine a series of current techniques, such as Mamba and individually processing the time and frequency dimensions, and then applying a global operation down both dimensions. They use a discriminator to add another loss signal to the training process, and in their experiments they cover a range of datasets and evaluation metrics, strengthening their claims. This show good scientific rigour.

### Weaknesses
The weaknesses mainly come from technical writing problems and lack of clarity. 

 - SiCM is defined, but it is not clear how it is used. This section appears to define the equations twice, which is unnecessary. Its inputs are not defined - what is $Q_{in}$ and how does it connect with the rest of the model? Use of mamba is interesting, bidirectional seems unusual - and they do not have experiments to back up this choice.
 - CM_2: 
	- Line 278 - should the notation be $B F_x \times T_x \times C$ instead?
	- Line 283 "diverging" is repeated.
	- Line 301 the $F_e$ and $F_p$ are not clearly defined (1d convolutions?). 
	- On equastions 6 and 7 add some spaces after the "..." and after the "," otherwise its too hard to read
	- Line 302: it should be "contains" not "contain"
	- 3.5 the use of the SiCM notation is a little confusing. Earlier, it refers to a specific set of Mamba-based operations, but here it is for the entire frequency processing and time processing modules. Please keep the nomenclature consistent. 
 - The Discriminator is mentioned but undefined. Papers need to be reproducible. 
 - The methods they compared to in the results tables are quite old. Would be interesting to compare with modern AVSS models by setting speaker 2 = noise.

Finally, while this is not a strict requirement, open sourcing the code after the paper's release would help understand the methods better, as the methods are quite convoluted.

### Questions
AF Block:
 - Equation 11 is an interesting operation. I would expect something like $MI + (1-M)I$ if $M$ were a Mask. Could you provide some justification/insight into this operation, such as motivation/related work? 
 - "Attention" usually refers to a specific set of operations. To make this block resemble attention, you could apply two SiCMs to $P^c$ (to make a $K$ and $V$), then one SiCM to $E^c$ (to get $Q$), and then create an attention map by applying cross attention with $Q$, $K$ and $V$. Of course, this would be quadratic in $T_x$, so this may be computationally prehibative. Would it be possible to explore alternative operations? 

Experiments:
 - Would it be possible to add Si-SNR(i) and SDR(i) metrics to the results?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel framework, called Cross-Modal Contextual Modeling ($CM^2$), for developing audio-visual speech enhancement technology. The $CM^2$ uses two types of contextual information: semantic and signal contexts. Semantic-level context enables the model to infer missing or corrupted content, leveraging semantic consistency across segments, whereas signal-level context further explores coherence within the signals developed from the semantic consistency. The $CM^2$ also incorporates visual information into the frequency domain and verifies that visual information plays a critical role in enhancing noisy speech.

### Strengths
- This paper is well-written and easy to understand.
- The authors clearly pointed out that most existing approaches focus solely on fusion in the temporal domain and overlook the potential correlations between the frequency dimensions of the visual and audio modalities.
- The authors conducted comprehensive experiments on ablation studies showing that the proposed $MC^2$ outperforms the previous AVSE methods.

### Weaknesses
- The authors underscore the significance of visual information in recovering audio frequency domain information with the ablation study in Table 6. However, my concern is that the performance improvements are mainly due to the pre-trained visual encoder like AV-HuBERT, not the proposed CCFM (also in Table 10). I think it is better to provide more analysis on how the proposed CCFM actually boosts up speech enhancement performances without the largely pre-trained visual encoder. I also suggest the authors provide visualizations of the intermediate features produced by CCFM.

- While the task is audio-visual speech enhancement, the authors have not provided a demo video showing how clear and intelligible the output speech samples are. The desirable demo could be side-by-side comparisons with baseline methods. Furthermore, there is no human subjective MOS performance verifying that the enhanced output samples are actually better than those from the previous literature. I would suggest gathering a certain amount of participants to validate the enhanced speech sample by evaluating naturalness, intelligibility, etc. 

- The authors only showed three different metrics while other previous papers have more. I encourage the authors to provide more quantitative performance metrics like MCD which is Mean Cepstral Distance measuring the difference between the spectral features of the synthesized speech and the target speech and ViSQOL which is Virtual Speech Quality Objective Listener to verify the proposed $MC^2$. I think MCD is important because this paper specifically underlines the importance of the frequency-domain characteristics of speech with visual appearance.

### Questions
### Additional Comments
- There are missing references like [1,2] that are well-known in speech enhancement tasks. Also, I would recommend the authors compare the proposed architecture with LA-VocE [1] since it's one of the recent state-of-the-art AVSE papers.
- Is there a reason that the authors use ISTFT not vocoder when converting the mel-spectrogram into the actual audio waveform? 
- Besides the quantitative comparison, I am curious about the comparisons of inference times and numbers of parameters of the proposed model and other methods. Are those comparable?
- line 269: $CM_2$ -> $CM^2$?
- Please increase the line space between lines 425 - 426 for better readability. 

[1] Mira, Rodrigo, et al. "LA-VocE: Low-SNR audio-visual speech enhancement using neural vocoders." ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023.
[2] Tan, Ke, and DeLiang Wang. "Learning complex spectral mapping with gated convolutional recurrent networks for monaural speech enhancement." IEEE/ACM Transactions on Audio, Speech, and Language Processing 28 (2019): 380-390.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a novel approach called Cross-Modal Contextual Modeling (CM2) for Audio-Visual Speech Enhancement (AVSE). Inspired by the human auditory system's phonemic restoration, CM2 integrates semantic and signal-level contexts across audio and visual modalities to improve speech quality in noisy environments.

### Strengths
1. This paper introduces a new approach to audiovisual speech enhancement (AVSE) by integrating semantic and signal context, inspired by phoneme recovery.

2. The semantic context module (SeCM), signal context module (SiCM), and cross-context fusion module (CCFM) are clearly explained in the paper.

3. The authors conduct detailed ablation experiments on the proposed modules, effectively illustrating the framework and its components.

### Weaknesses
1. The authors propose a SeCM block that integrates visual and auditory semantic content, but the method does not explain how E is obtained from V, PV, and PAV. The authors should provide a detailed explanation of this process. Additionally, using time-domain information as input increases the complexity of this part of the model.

2. References to BiMamba should include [1,2] because these methods are the first to use bidirectional Mamba in the speech domain, which was not present in the original Mamba paper.

3. The time-frequency alternating module is very common in the speech separation field, and the authors should reference related work. For example, TF-GridNet [3] and RTFSNet [4] use similar time-frequency alternating modules, which are very effective in multimodal speech enhancement.

4. The multimodal speech enhancement methods compared are quite outdated. The authors should compare the latest methods (RTFSNet [4], [5], [6], etc.), as many new methods were proposed in 2024. Moreover, using numerous pre-trained models in the SeCM block results in a very complex model, which might not be optimal compared to current methods, as increased parameters can enhance model generalization. The authors should calculate the parameter count and computational load (MACs) of different models to more comprehensively demonstrate model performance.

5. In Equation 8, the authors did not describe the meaning of the F function, which should be explained there.

6. In line 278, the speech feature P should not be F and T; please correct this.

7. Lines 424 and 425 have insufficient spacing and should be adjusted.

[1] Jiang X, Han C, Mesgarani N. Dual-path mamba: Short and long-term bidirectional selective structured state space models for speech separation[J]. arXiv preprint arXiv:2403.18257, 2024.

[2] Li K, Chen G. Spmamba: State-space model is all you need in speech separation[J]. arXiv preprint arXiv:2404.02063, 2024.

[3] Wang Z Q, Cornell S, Choi S, et al. TF-GridNet: Integrating full-and sub-band modeling for speech separation[J]. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2023.

[4] Pegg S, Li K, Hu X. RTFS-Net: Recurrent time-frequency modelling for efficient audio-visual speech separation[J]. arXiv preprint arXiv:2309.17189, 2023.

[5] Tiwari U, Gogate M, Dashtipour K, et al. Real-Time Audio Visual Speech Enhancement: Integrating Visual Cues for Improved Performance[C]//Proc. AVSEC 2024. 2024: 38-42.

[6] Gogate M, Dashtipour K, Hussain A. A Lightweight Real-time Audio-Visual Speech Enhancement Framework[C]//Proc. AVSEC 2024. 2024: 19-23.

### Questions
Please refer to above.

### Soundness
3

### Presentation
2

### Contribution
2
