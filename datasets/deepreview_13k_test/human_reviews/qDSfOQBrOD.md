# VChangeCodec: A High-efficiency Neural Speech Codec with Built-in Voice Changer for Real-time Communication

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Neural speech codecs (NSCs) enable high-quality real-time communication (RTC)
at low bit rates, making them efficient for bandwidth-constrained environments.
However, customizing or modifying the timbre of transmitted voices still relies on
separate voice conversion (VC) systems, creating a gap in fully integrated systems
that can simultaneously optimize efficient transmission and streaming VC with no
additional latency. In this paper, we propose a high-efficiency VChangeCodec,
which integrates the Voice Changer model directly into the speech Codec. This
design seamlessly switches between the original voice mode and customized voice
change mode in real-time. Specifically, leveraging the target speaker’s embedding,
we incorporate a lightweight causal projection network within the encoding module
of VChangeCodec to adapt timbre at the token level. These adapted tokens are
quantized and transmitted to the decoding module, to generate the converted speech
of the target speaker. The integrated framework achieves an ultra-low latency of
just 40 ms and requires fewer than 1 million parameters, making it ideal for RTC
scenarios such as online conferencing. Our comprehensive evaluations, including
subjective listening tests and objective performance assessments, demonstrate that
VChangeCodec excels in timbre adaptation capabilities compared to state-of-the-art (SOTA) VC models. We are confident that VChangeCodec provides an efficient
and flexible framework for RTC systems, tailored to specific operator requirements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents VChangeCodec, a codec specifically designed for real-time voice conversion. It uses a causal projection network to convert the vocal timbre of the source speaker into that of the target speaker at the token level. Evaluation results show that in original voice mode, VChangeCodec achieves good quality compared with other codec models. In voice change mode, it performs comparably to previous methods in terms of naturalness and intelligibility, and outperforms them in speaker similarity according to objective evaluations.

### Strengths
This paper presents a voice conversion system that can be used in real-time communication such as virtual meetings. The proposed module, the causal projection network, can be easily plugged into different codec frameworks and has very low latency. The evaluation results look reasonable based on the metrics used. The authors also conducted ablation studies to discuss the influence of each component in the proposed framework.

### Weaknesses
While there have been several works on zero-shot voice conversion (though they may not be real-time), the proposed framework is constrained to a predefined set of target speakers, which limits its extensibility. Additionally, the evaluation results have issues, such as using very limited test sets, inconsistency in the languages evaluated between the original and voice change modes, and a lack of human evaluation in the voice change mode.

### Questions
1. In Section 3.2, the authors imply that using pre-trained speaker embeddings would increase computational costs and storage space. However, if I understand correctly, the target speaker features are all pre-computed, so using speaker embeddings (which are usually single vectors) should not pose a problem. Moreover, speaker embeddings have been widely used in several speech synthesis tasks with good results. I wonder if the authors have conducted experiments using pre-trained speaker embeddings, and how their performance compares to the results presented in the paper.

2. In the evaluation, the authors used Mandarin utterances for assessing the original mode and English ones for the voice change mode. I am confused about this setting, as they are very different languages, and it is not natural to evaluate them in two different modes. It would make more sense to either (a) use only Mandarin or English, or (b) evaluate both the original and voice change modes in both English and Mandarin.

3. In the evaluation of the voice change mode, the authors only use automatic evaluations (if I understand correctly, the MOS scores in Tables 2 and 3 are not human ratings). It is necessary to include human evaluation results in speech synthesis tasks. The authors might first conduct objective evaluations on large test sets using automatic MOS models, and then perform human subjective evaluations on a randomly sub-sampled set to justify the reliability of the automatic MOS on the set.

4. Similar to point (3), the authors should conduct subjective evaluations on speaker similarity.

5. In Table 2, there are no values for oracles in the intelligibility column, which I believe the authors should include so that readers can understand the quality gap between the generated utterances and the authentic ones.

6. In Section 4.4, the authors compared the real-time factor of the proposed approach only with Lyra2. I believe there are other real-time voice conversion systems, such as StreamVC, and it would be good to include them.

7. I was unable to listen to the audio samples in the supplementary material. The authors included audio samples in a PPTX file, which is not directly accessible without installing Microsoft Office. I'm not sure if online converters break the audio links in the file, so I prefer not to use them. It would be helpful if the authors could provide the audio files directly.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a real-time voice codec with an integrated vocal identity conversion module. It first trains the original mode of the codec and validates that the performance is approximately similar to other state-of-the-art codecs. Then the authors propose a voice changer module that is a causal convolutional network that is conditioned on the target speaker using a selected set of features provided by the OpenSmile software. To be able to construct target features a parallel training database is required. To this end, the paper proposes to create the target phrases synthetically by means of converting the input phrase of the source speaker using the RVC model. 
The voice changer mode is evaluated by means of comparing it to results of a few selected algorithms from the literature.

### Strengths
- Very original idea to combine a voice codec with an integrated identity conversion component,
- real-time voice identity conversion with low latency is a very ambitious target
- using the existing features of the OpenSmile software as a means to condition the target speaker identity is new (at least to me), and looks potentially very interesting.

### Weaknesses
- Not all final parameters are explicitly described. I wonder about the R parameter. The description in the appendix says in line 795:

*Given the target bitrate r, the dimension of latent feature N, the theoretical bitrate in each frame is computed as −1 ∗ N ∗ log2( 1/(2∗R+1)).*

I suggest explicitly saying here what R is supposed to be in this equation and how you ensure the desired target bitrate is achieved.

- Some of the claims are rather misleading. For example, authors state that in original mode their codec works on party with the DAC and Encodec. These two are trained as codecs for arbitrary signals (music included), while the proposed codec is for speech only. The version of Encodec is not clearly specified (authors should add the information about, which model is used in their experiments), but both DAC and Encodec work on signals with higher sample rate. That your codec outperforms general-purpose codecs training to compress signals with a larger sample rate is a positive point, but is not that astonishing either.  A somewhat similar comment applies to Lyra2, which supports arbitrary languages (probably trained in 24kHz but I am not 100% sure about that).  I suggest adding an explicit description of the differences in training data and sample rates when discussing the performance comparisons.
- The description of the data sources in 4.1 is a bit confusing. You write:
  *The clean speech is from LibriTTS (Zen et al., 2019), DNS Challenge (Reddy et al., 2020). The mixed
speech is generated by combining clean speech and background interference (e.g., noise), including
DNS Challenge, MIR-1K (Hsu & Jang, 2009) and FMA (Defferrard et al., 2016).*     
A few details should be added: 
  - which part of the DNS challenge data did you use? There are singing and expressive datasets mentioned in the Reddy paper.
  - Why do we need mixed speech? This is not mentioned anywhere in the paper. How do you perform the mixes with respect to the balance between background (noise) and foreground (voice)
  - Nothing is said about the data that is used for validation. Please add a description of the train/validation/test split.

- While perceptual evaluation is performed for the codec in original mode, neither DAC nor Encodec are part of the comparison. To give a complete picture of the performance of your codec compared with these two, it would be preferable to have them added to the perceptual evaluation. If you cannot add them then please explain why you think it is not possible or not needed.
- The fact that the training is performed using synthetically generated parallel training data is quite hidden, it should be mentioned earlier in the description, for example in the introduction.
- Evaluation of the voice change mode is very weak, no subjective evaluation is provided, and all the baseline models are trained on the VCTK dataset. Even if the models support zero-shot conversion it is clearly unfair to compare these models to your model that - as far as I see - is trained particularly on the target speakers. 
The fact that Resemblyzer similarity is low for QuikVC is clearly due to the fact that you operate it out of its context.
- Resemblyzer is a weak alternative to perceptual evaluation. 

- English language should be improved. Notably, *Casual projection network* should be renamed into *Causal projection network*. When you say your model *achieves superior latency* it would mean it has a larger latency. you probably want to say your latency is lower than that of the other methods.

### Questions
Please explain better how you perform the bit rate calculation in A.3 and specify the quantizer levels R that you use in your experiments. 

You should discuss the fact that your model is trained on a parallel database of the target speaker, while all other VC models are operated in zero short mode. The results of your model are difficult to judge.

Why are neither DAC nor Encodec part of the perceptual evaluation in the original mode?

If I understand correctly, your quantization model is exactly the same as the one used in SimpleSpeech and SimpleSpeech 2.
https://arxiv.org/pdf/2408.13893 - if this is correct you should cite one of them.

Remark after the discussion phase:

All these questions have been answered and taken care of by the authors.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new neural speech codec designed to integrate voice-changing capabilities directly into the codec itself. This integration allows for switching between original and customized voice modes in real-time, making it efficient for bandwidth-constrained environments. The proposed method leverages a causal projection network within its encoding module to adapt the timbre of the transmitted voice at the token level, achieving latency of 40ms and requiring fewer than 1 million parameters. This makes it ideal for real-time communication (RTC) scenarios such as online conferencing.

This paper highlights the limitations of existing neural speech codecs (NSCs) and voice conversion (VC) systems, which typically operate separately and introduce additional latency. VChangeCodec addresses these issues by combining speech compression and voice conversion into a single, integrated framework. The codec uses scalar quantization to reduce complexity and maintain high fidelity at lower bitrates. Comprehensive evaluations, including subjective listening tests and objective performance assessments, demonstrate that proposed method results in timbre adaptation capabilities, providing a flexible solution for RTC systems.

Additionally, the paper discusses the technical details of codec's architecture, including its encoder, quantization, and decoder components, as well as the training strategy involving multiple loss functions to ensure high-quality speech reconstruction and timbre adaptation. The authors emphasize the operator-oriented deployment of proposed technique, which minimizes privacy risks by restricting user access to pre-defined timbres. The results of extensive experiments and ablation studies show the effectiveness of VChangeCodec, making it a possible approach for enhancing real-time communication with built-in voice-changing features.

### Strengths
Well written paper with an interesting proposition to carry out voice conversion as part of the codec. The background and methods section is meticulously written and explained nicely. The scalar quantization is a know technique from past which is now getting revived in the context of neural network. The authors have evaluated their models in objective and subjective metrics showing either improvement in performance or matching state-of-the-art codecs and VC models.

### Weaknesses
The main weakness is the motivation which I fail to understand at this point. If a light-weight Voice conversion model can be used a post-processor or a pre-processing module after/before codec, then what additional advantage does this framework brings. Second, apart from the combination of Codec+VC module and scalar quantization trick, there is no axis of novelty in this paper. Additionally, in the experiment section, evaluation of speaker similarity through SMOS would be more convincing than resemblyzer model. Finally, the usage of WER and CER (by Whisper model) does not suggest greater intelligibility as they inherently make use of a language model to correct pronunciation mistakes.

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents VChangeCodec, a speech codec that integrates voice changing capabilities directly into the codec architecture, aimed at enhancing RTC services. 

The authors argue that existing neural speech codecs do not support customizable voice features effectively, particularly in bandwidth-constrained environments.

### Strengths
1. The reported inference latency of around 40+ ms is impressive and suitable for real-time applications, which is a critical requirement in RTC systems.
2. This paper is well-organized and easy to read.

### Weaknesses
1. In Section 4.1, the author claims that ''We select one male and one female speaker from the internal datasets which contain 1-hour data, respectively, to serve as the target timbre.'', I believe the evaluation is not comprehensive and it would be nice to add more target timbre.
2. Some codec baseline systems need to be replaced, the author claims comparison with SOTA codec models in Table 1, while some baselines are proposed in 2012 or 2014, it is not convincing.
3. The author should present the difference between VChangeCodec and two related works [1,2], they also are codec models and can achieve voice conversion. A comparison in experimental evaluation is necessary.
4. A subjective evaluation of the proposed system would be very beneficial. It has been shown time and time again that the opinion of human listeners cannot be replaced with objective evaluation.
5. VC baselines in Table 2 are not SOTA models, please revise the claim or compare the proposed system with the recent SOTA models like LM-VC, SEFVC, or DDDM-VC.

[1] SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models

[2] NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models

### Questions
1. What advantages does VChangeCodec offer over existing state-of-the-art neural speech codecs in terms of parameter efficiency and compression quality?
2. How can VChangeCodec ensure robust performance across various network conditions typical in RTC scenarios?

### Soundness
2

### Presentation
3

### Contribution
2
