# CRAFT: Cross-Representation modeling on Audio waveForms and specTrograms

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
In this paper, we introduce \underline{C}ross-\underline{R}epresentation modeling on \underline{A}udio wave\underline{F}orms and spec\underline{T}rograms (CRAFT), an innovative representation modeling designed to extract joint features from diverse representations in the audio modality, and choose acoustic classification to showcase the effectiveness of our approach. Historically, most prior works are focused on utilizing either the frequency-domain spectrogram or the time-domain waveform representations for acoustic modeling. Directly fusing or concatenating individual representations suffers from performance degradation. However, we argue that by aligning these individual representations effectively, they can complement each other and substantially enhance the quality of downstream tasks. 
To mitigate semantic misalignment, we initially propose a cross-representation contrastive learning framework incorporating spectrogram and waveform based contrastive learning loss in audio pretraining. Subsequently, to alleviate temporal misalignment, we present a cross-representation transformer architecture, which models on spectrogram and waveform tokens together with fusion bottlenecks. The proposed CRAFT is tested on two commonly used datasets, demonstrating superior performances. Notably, our proposed CRAFT method outperforms the spectrogram-based counterpart by an impressive 4.4\% higher mAP on AudioSet balanced set, and achieves SOTA comparable performances on full set, which suggests the alleviation of semantic misalignment and temporal misalignment boosts cross-representation performances in audio modeling. All codes and models will be open-sourced.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes representation learning method both using spectrogram and waveform. Usually, the model takes spectrogram-based feature as an input to the model, or rarely waveform is solely used. However, since the information we can extract from the spectrogram and waveform can be different, it might be better to use both cases as well. To do that, the author basically used a model presented before (which is joint discriminative and generative masked spectrogram patch modeling), and improved this model by adding several techniques to both deal with spectrogram and waveform. In the end, they made an auxiliary loss term using waveform encoder. This waveform encoder uses multi-scale front-end encoder and  the output of the waveform encoder is compared with spectrogram encoder like they are having a different view relationship in SimCLR loss term. Finally, bottleneck fusion method is used to further boost the performance. The result and ablation study showed that the proposed modules are effective in spectrogram and waveform modeling in environmental sound classification task.

### Strengths
The most strong part of the paper lies on the model performance. When we see the results in Table 1, we can find that the proposed method reached the best performing model among self-supervised learning approaches. Also, the paper is easy-to-read and written clearly.

### Weaknesses
However, I think the novelty of the paper is quite limited. When we see the results in Table 5 (ablation study), the results is quite obvious. It is well-known that the performance is increased if we apply multi-scale modeling on acoustic model. Also, SimCLR loss and bottleneck fusion methods are also quite known approaches.

### Questions
If there is more insights we can get from the model, then it would have more novelty on the paper. For example, since the proposed work contains both spectrogram and waveform based encoder, maybe we can compare the learned characteristics of each encoder (especially the waveform encoder is multi-scaled).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a joint spectrogram-waveform representation learning method for audio classification task. Three techniques are introduced to solve the challenges in aspect of temporal alignment and semantic alignment problems. Specifically, MSAE model is proposed to align the waveform feature to spectrogram patches. Contrastive learning between spectrogram and waveform representations is proposed as a new pretraining objective. Fusion bottleneck token is introduced for better finetuning performance. System comparison and ablation studies are conducted on the proposed method.

### Strengths
1. The proposed method achieves higher or comparable performance on audio classification task compared to the existing SSL-based methods.
2. Sufficient ablation studies are conducted to show the effectiveness of the proposed method and the effect of different hyper-parameters.
3. The idea of patchfying 1d waveform representation to align with the 2d spectrogram representation is somehow novel.

### Weaknesses
1. Some statements are inaccurate or unclear.

   a) In introduction paragraph 1, the authors try to illustrate the difference between spectrogram and waveform representation by differentiating the tasks based on them. However, many of the audio/speech tasks can build on both spectrogram and waveform representation and both achieve good results. Actually, in areas like audio signal processing and ASR, both spectrogram [1,2] and waveform [3,4] are frequently used. 

   b) In introduction paragraph 2, it is quite confusing why car engine sound is more clear in the time-frequency domain, while successive breezes is clear in waveform domain. Need clarification. Moreover, waveform representation can also present time-frequency patterns. Take an example of conv-TasNet [3] in audio signal processing domain, the waveform filters spontaneously converge to a frequency response similar to that of a log-mel filter bank. 

2. Some experimental results / settings are confusing. 

   a) To sufficiently prove the effectiveness of spectrogram-waveform representation combination, the authors should show the comparison between spectrogram-only, waveform-only, and joint spectrogram-waveform representations while **keeping other factors the same**. However, the waveform-only results come from very old research, where the SSL and audio transformer techniques are not well established. Since waveform includes more information than the spectrogram, maybe using WaPT will result in better performance than SSaPT and comparable performance of PSWaCL. If this is true, spectrogram can be completely substituted by waveform in audio classification task. Here, WaPT denotes "Waveform modeling in PreTraining" and the only difference form SWaPT is to remove the spectrogram input and the corresponding training loss.

   b) The result of "SWaPT is worse than SSaPT" is confusing. Why adding additional representation degrades performance? If the reason is the conflict between spectrogram and waveform representation, why not use different parameters in waveform branch and spectrogram branch? If this simple way can solve the misalignment between spectrogram and waveform feature, the necessity of PSWaCL is quite doubtful.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a modeling approach that incorporates both waveform and spectrogram features in the audio domain. The authors also addressed the semantic misalignment and temporal alignment issue raised by the combination. The experiments demonstrate the effectiveness of the approach in audio classification tasks.

### Strengths
- Overall, it's an interesting idea to combine both waveform and spectrogram features and address alignment issues in one shot. 
- The experiments and ablation studies are quite compressive.

### Weaknesses
 - Novelty is limited considering the ICRL standards. It might be a better fit for speech-related conferences (e.g. Interspeech)
- The writing of this paper needs to be improved. Too many acronyms to make it less readable and hard to follow the idea, especially in section 3.2.
- In table 1, it shows that the performance of AST (spectrum-only) is still better than all the proposed methods in the paper. How to explain it?

### Questions
In table 1, it shows that the performance of AST (spectrum-only) is still better than all the proposed methods in the paper. How to explain it?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors investigate the use and fusion of two common feature representations within the audio domain, the raw waveform and spectrogram.

### Strengths
The topic addressed in the paper is interesting.

### Weaknesses
The introduction is poorly written. There are too many terms introduced e.g., PSWaCL, SWaB, MSAE without details of what to expect in the paper and what are the real contributions of the paper.
Challenges in feature fusion are not clear, and a lot of statements are loose or vague.
--> waveform-based features concentrate more on capturing common patterns! What are these common patterns? 
--> Spectrograms predominantly emphasize time-frequency responses! What are these responses? Are we assuming a system here? Why can't waveform learning using a learned filterbank do the same?
--> Enhance the comprehensiveness of the feature set! Comprehensiveness in what sense?
None of the above-mentioned statements are actually related to Semantic Misalignment. Semantic means something else.
Temporal Misalignment: Again, the claim by the authors is wrong. In both cases, linear/non-linear processing methods are available and temporal alignment can be easily achieved. It's basic DSP! Nevertheless, One can always do late fusion after learning complementary features.

Related works: There is no mention of existing approaches that have tried feature fusion, which should be the main focus.  Instead, authors have just discussed existing approaches for audio classification, which could be omitted or briefly mentioned if compared against in the experimental section.
https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Fedorishin_97_t1.pdf
https://www.mdpi.com/1424-8220/19/7/1733
https://www.isca-speech.org/archive/pdfs/interspeech_2018/yang18c_interspeech.pdf
https://dl.acm.org/doi/pdf/10.1145/3240508.3240631

Method (Sec3): Overall, the proposed method is just a combination of well-known existing methods and small extension of  method by Gong et al., 2022a. Novelty is limited and not well highlighted in the context of the problem addressed in the paper.

--> Our work is built upon SSAST. What is SSAST? 
--> fills the gap of lacking raw audio waveform embedding in the era of transformer. Again, this is a loose statement that is not explained.
--> Contrastive learning is widely used in multimodal generative models. So, the method is not novel in itself. What do we mean by natural or unnatural pairing? 
--> MSAE is a known technique for designing adaptively learned filter banks. Whats novel here? Authors should refer to existing works here.
Patichyfy operation is not explained. A diagram would help readers. Pooling will reduce the information for short kernel-based conv outputs with bigger dimensions. Instead, zero padding, dilation, adaptive strides, and deformed convolution kind of ideas can be used to learn multiscale features. In current practice, pooling has been established to be one of the worst choices.
--> what is specify in Fig1?
--> There is no description of how spectrogram and waveform feature inputs are processed in the transformer frontend. Is it a single transformer with shared weights or individual ones? A lot of these crucial details are superficially treated.
--> spectrogram and waveform patches can naturally serve as contrasting pairs. It is unsure how this will happen. Is there a ref to existing work to establish this?
--> what is t_spec t_wav in (5a,5b)? what are the dimensions? on which axis is the concatenation is happening? Again, it is unclear from where bottleneck features will come? Why are they required? Can't we just project the features to the same dimensional space? What's the design of a multi-stream bottleneck transformer?

Authors have used Mel-spec, which is a non-linear feature, and the arguments in the introduction about miss-alignment due to fixed resolution are in contrast. While I understand the author's point of view, the way things are explained or presented is misleading for a wider audience.
Only spectral domain augmentation is used. Why not the time domain? Existing works have utilized both for acoustic modelling and feature fusion using CNN backbone with remarkable success. Yes, transformers are hot these days! but they only shine for sequence modelling tasks. For classification CNNs are still the best (attention can be incorporated, too); one has just to train them well. 


Experimental results are not SOTA, and strong baselines are not considered.
Authors are encouraged to see https://paperswithcode.com/sota/audio-classification-on-esc-50
Existing works have achieved over 98% on ECS-50 benchmark.

Similarly, for Audioset: https://paperswithcode.com/sota/audio-classification-on-audioset


The code is not available to replicate main experiments without which the claims hold no value at venues like ICLR.

### Questions
Please see the detailed feedback above.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
