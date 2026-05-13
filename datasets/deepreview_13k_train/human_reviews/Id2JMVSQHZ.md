# Universal Semantic Disentangled Privacy-preserving Speech Representation Learning

- Decision: Reject
- Scores: 3, 5, 5, 5, 6

## Abstract
The use of audio recordings of human speech to train LLMs poses privacy concerns due to these models' potential to generate outputs that closely resemble artifacts in the training data. In this study, we propose a speaker privacy-preserving representation learning method through the Universal Speech Codec (USC), a computationally efficient encoder-decoder model that disentangles speech into: (i) privacy-preserving semantically rich representations, capturing content and speech paralinguistics, and (ii) residual acoustic and speaker representations that enables high-fidelity reconstruction. Extensive evaluations presented show that USC's semantic representation preserves content, prosody, and sentiment, while removing potentially identifiable speaker attributes. Combining both representations, USC achieves state-of-the-art speech reconstruction. Additionally, we introduce an evaluation methodology for measuring privacy-preserving properties, aligning with perceptual tests. We compare USC against other codecs in the literature and demonstrate its effectiveness on privacy-preserving representation learning, illustrating the trade-offs of speaker anonymization, paralinguistics retention and content preservation in the learned semantic representations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a codec-based approach to addressing privacy concerns in speech data used for training large language models. The author claims that the proposed USC is a computationally efficient encoder-decoder model that could disentangle speech into privacy-preserving semantic and residual acoustic and speaker representations.

### Strengths
- The privacy-related topic is interesting and the motivation is good.
- The proposed metrics for assessing privacy-preserving properties in speech representations, particularly focusing on k-anonymity, will benefit privacy protection research.

### Weaknesses
 **Ignore the most related works**
- I believe this work is primarily a speaker anonymization task; however, no speaker anonymization studies are cited in this paper[1-3].

**Limited Contribution**
 - The contribution of this paper is limited, as the disentanglement in the codec model has already been proposed by SpeechTokenizer [4] and FACodec [5] for speech generation tasks. Furthermore, one of the top systems in the VPC 2024 also employed a disentangled codec model for privacy protection [6], though the authors did not cite it. Therefore, the core approach in this paper is not novel.

**Inefficient experiments**
 - VoicePrivacy Challenge (VPC) has been held in three editions[1-3] and aims to provide baseline, evaluation metrics, training and evaluation datasets for speaker anonymization studies. Huge of studies follow the setting of this challenge to evaluate their work, but this paper ignores the most convincing evaluation method, which makes me can not believe the effective of the proposed approach.
   https://www.voiceprivacychallenge.org/

**some of the authors' statements are not rigorous**

 - In the abstract, the author claims that ''Combining both representations, USC achieves state-of-the-art speech reconstruction'', the current experiments can not support this statement, due to some sota disentangled codec models (FaCodec) are not included in the comparison.
 - In the introduction, the statement that ''USC is the lowest bit-rate neural speech codec'' is incorrect, I think WavTokenizer is the lowest, but the author does not cite it in their paper.

**Minor Concern**
- Please simplify Sec. 3.2, GRL method has been widely used in previous studies.
- Please clarify why Hubert L9 without speaker-identifiable traits.
- How to balance the hyper parameters in Eq. 4
- Please PESQ metric in Table 1

### Questions
Could the author explain why the paper does not cite any paper related to speaker anonymization, or clarify the difference between their work and speaker anonymization?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new discrete tokenization method which has a non-speaker related initial token (semantic/phonetic and paralinguistic information is covered by this single token) and the rest of the tokens (per frame) cover the rest of the acoustic information (including speaker id) that helps with reconstructing a perceptually equivalent version of the speech waveform.

The separate roles of each token is enforced by using a bunch of losses that encourage non-speaker information to be used in the first level token (z^0_q) and regular codec losses.

The discretization is done through RVQ for the acoustic tokens.

The speaker information is removed from the first token using an adversarial speaker-id loss and a "differential privacy noise adding" module and through semantic distillation which tries to predict Hubert encodings from the semantic encodings (obtained from semantic tokens).

### Strengths
The idea of the paper is interesting in the sense that separating semantic and acoustic information in a single tokenizer is useful for privacy preservation through anonymization. This is achieved through multiple losses in the paper. 

The privacy preservation of the method is analyzed through interesting metrics of linkability, singling out and perceptual privacy evaluations through A/B/X tests. These seem to be good privacy preservation tests.

### Weaknesses
SpeechTokenizer removes all non-phonetic information since it uses Hubert distillation for the semantic tokens. This method tries to leave both phonetic and paralinguistic (prosody, sentiment, etc.) information in the initial token, so that we can reconstruct a waveform from the initial token that resembles the original speech but without giving away the original speaker, thus achieving anonymization as claimed in the paper. Still, additional utility of this model as compared to SpeechTokenizer seems limited since SpeechTokenizer also achieves anonymization, but at the expense of losing sentiment and prosody etc. I think the paper needs to make the point that the goal is to also keep sentiment information for example, but we do not see a test for that in the paper. In the anonymization tests, SpeechTokenizer shines, so probably we need another test that shows that the method introduced in the paper beats SpeechTokenizer. Maybe sentiment analysis?

The description of modules are not very precise. Section 3.2 is not clear in that we cannot tell how the z^0_q relates to F_i. Also F_i where i indexes the batch item does not seem to make sense since we probably want F_(s_i) where s_i is the speaker id (out of N) of batch item i out of n.

Section 3.4 second paragraph is not clear. It describes a mechanism to stop gradients, but does not specify how it is done. Is it automatically achieved through losses or not? 

Similarly, Section 3.5 is not clear how the noise is added and what it is added to. The paper did not talk about projections in the quantization module at this point but Section 3.5 talks about projections. We only read about projections in the appendix. W_in in Figure 2 is only explained in the appendix. Also, differential privacy usually adds noise to gradients (If I recall correctly), so is it correct to call what is done differential privacy or is it something else?

Equation (4) gives a bunch of losses with weights. It seems hard to tune those weights on different datasets since there are too many weights. How did you tune them?

### Questions
1. Please address points mentioned in the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced a new kind of speech representation learning for the privacy-preserving neural codec. The proposed method disentangled the speech information into two parts: semantic information containing both the content and paralinguistic parts of the speech and the speaker information. Several experiments were conducted to show the effectiveness of the proposed method in aspects of both the reconstruction capability and the privacy-preserving properties of the proposed codec by comparing the proposed method with existing codec systems. An additional experiment of training a voice conversion system with the proposed codec was performed to demonstrate the efficacy of the proposed codec in downstream applications.

### Strengths
1. The paper looks into the privacy-preserving aspects of the neural speech codec, which is important but not the main focus of previous studies.

2. Details on the model architecture and training are provided, enhancing the reproducibility of this paper.
3. The authors provided new metrics for privacy-preserving evaluation, which can benefit future research.

### Weaknesses
1.  **Baseline missing**: In the related works, FACodec [1] is mentioned to be disentangled for some speech attributes. However, FACodec was not included as one of the baselines. It will be better to include this baseline for comparison.

2.  **Overall Performances**: While the authors reported several metrics, the proposed method did not have much advantage over the baselines or even seemed to be inferior. Though the authors provided some qualitative examples, trying to explain this phenomenon, I think some quantitative measurements are still necessary to convince the readers that the proposed method is indeed better. Hence, some additional experiments are needed in my opinion. The lack of clear quantitative superiority raises concerns about the practical benefit of the proposed method over existing approaches. The reported metrics, such as reconstruction accuracy and speaker similarity, do not consistently demonstrate a significant improvement, which is crucial for justifying the complexity of the proposed approach. Specifically, the trade-offs between privacy and other aspects of speech quality need more rigorous quantitative analysis.

3.  **Missing Experiments**: The authors did not have a quantitative evaluation of the trained voice conversion model. Thus, it would be hard to convince the reader that the proposed codec and the Partial-Teacher-Forcing (PTF) techniques were really helpful. In addition, it seems like ABX tests for other baselines were absent in the current version of the paper, making the evaluation less consistent. The authors are suggested to include the tests. The absence of a quantitative evaluation for the voice conversion task is a significant oversight. Without such metrics, it's difficult to assess the practical utility of the proposed codec in downstream applications. Furthermore, the lack of ABX tests for all baselines introduces an inconsistency in the evaluation methodology, making it harder to draw firm conclusions about the relative performance of the proposed method.

4.  **Clarity**: The authors provided two metrics for privacy-preserving evaluation. However, the definitions of these metrics were not easy to understand at first glance. If a visual demonstration can be included in the paper, the clarity will be largely improved.

### Questions
My main concerns are listed in the weakness part. Here, I list some questions for the author as follows:

1. Why was FACodec not included as one of the baselines? As aforementioned, disentanglement was conducted for FACodec. Thus, it should be a good baseline to compare.

2. The authors mentioned some trade-offs between privacy-preserving aspects and some speech attributes like paralinguistic information. Is there any way to quantitatively evaluate this aspect? This is related to the second point of the weakness. I think the results so far are not sufficient to convince the readers that the proposed method is really better.

3. As mentioned in the weakness, I think ABX tests for other baselines are necessary. The authors can consider to include them.

4. Some in-house datasets were used for the experiments. Some explanations on how these data were collected will make the paper better if included even though you may not want to release them.

5. I suggest that more detailed explanations of the qualitative examples (mel-spectrograms) should be provided to make the paper easier to understand.

A minor issue is that some typos need to be fixed (e.g., i.e should be i.e. in Sec. 3.4). Proofreading is necessary for future versions of this paper.

### Soundness
2

### Presentation
3

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
This paper describes the Universal Speech Codec (USC), which disentangles speech into global characteristics and time-varying content in a manner useful for speaker anonymization. The authors build upon the DAC audio codec, adding techniques such as reversing speaker gradients, distilling semantic representations from a pre-trained SSL model, and local differential privacy. Results demonstrate comparable reconstruction quality as preceding codecs, and privacy evaluations demonstrate performance not clearly exceeding prior methods.

### Strengths
The privacy evaluations described in section 4.3 are designed and described well.

I like the framing of disentanglement for privacy applications. I think there are some genuinely useful applications.

### Weaknesses
The authors point out that USC "generat[es] different identities across the same utterance." Wouldn't this be a clear give-away that the audio is generated if the speaker is changing throughout the utterance? Is there a use case in which having audio with a varying speaker identity is desirable?

While the LDP is ablated, the other proposed methods (e.g., speaker reversal and semantic distillation) are not sufficiently ablated. It is not sufficient to rely on ablations from prior works, as the specific combination of techniques within the USC framework may yield different results than in isolation. The interaction between speaker reversal, semantic distillation, and the codec itself needs to be evaluated to understand the contribution of each component.

The subjective evaluation of section 4.4 should be performed using a baseline method such as Speech Tokenizer, as well as original audio. The current evaluation only tests the privacy-preserving capabilities of the system, but does not assess the quality of the reconstruction relative to other methods. Without a baseline comparison, it is difficult to determine if the proposed system is competitive with existing speech codecs in terms of reconstruction quality.

The voice conversion experiment is incomplete. A privacy-preserving speech synthesizer should be able to perform voice conversion, but the single example provided in Appendix A (without audio) is not sufficient to demonstrate voice conversion at any threshold of quality. If a listening test was performed for VC, why were results not included? And what was the baseline of those listening tests?

It doesn't seem particularly fair to compare bit rates with DAC when DAC models 44.1 kHz audio and the proposed model models 24 kHz audio. The comparison is not an apples-to-apples comparison, as the difference in sampling rate directly impacts the bit rate. A more appropriate comparison would be to either compare against a 24 kHz version of DAC or to normalize the bit rates to account for the different sampling rates.

### Questions
Can audio examples be included, so that we may compare your system to the baseline systems using our own ears?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper addresses the important question of privacy in training LLMs and proposes a method to anonymize the input to training. It does so by applying an anonymizing autoencoder structure where parts of the bottleneck is fed to the LLM instead of the original signal.
It is a large paper with many strong aspects, but unfortunately, there are also some critical weaknesses. The papers presents a comprehensive and useful review of related literature and describes the proposed approach clearly.

### Strengths
- Addresses a substantial problem of privacy in LLM training.
- Very good description of background
- Thorough and detailed presentation of the proposed model.

### Weaknesses
 - There are so many ways in which private information can leak through that it is important to never claim that privacy is fully preserved for the speech signal, but only for a selection of attributes.
- STOI is a very old metric for speech intelligibility and does not correlate well with quality. The high-fidelity scores are especially clearly saturated. MCD is even older and equally sub-optimal. The quality comparison is thus not trustworthy. AFAIK the community currently prefers VISQOL and I would advise switching to that. PESQ, while an improvement over MCD, still suffers from similar limitations as STOI and does not capture the nuances of perceived speech quality, particularly for high-fidelity reconstruction. The reliance on these objective metrics makes the quality assessment unreliable.
- Claiming high quality speech reconstruction with only objective metrics is not acceptable. Even with state-of-the-art metrics like Visqol, we can always find counter-examples where subjective preference is the opposite of objective metrics. Claims of high-quality reconstruction must, therefore, be accompanied by subjective listening tests. Without these, there is no guarantee that the output is usable, even if objective scores appear high. The absence of subjective testing is a critical flaw.
- None of the metrics include an analysis of statistical significance. It is not enough to simply report the best metric; the statistical significance of the differences between systems must be demonstrated to ensure the results are not due to random chance.
- The description of a key piece of the privacy measure, the SIM metric, is very short and hard to find. In comparison, sections 3.5 and 4.3 receive a lot of real estate. Please fix this imbalance by describing SIM in more detail.

### Questions
- How does your method rank against other speech disentanglement approaches? Now, you were comparing only to codecs.

### Soundness
3

### Presentation
4

### Contribution
4
