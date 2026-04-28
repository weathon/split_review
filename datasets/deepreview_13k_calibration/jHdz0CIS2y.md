# SelfVC: Voice Conversion With Iterative Refinement using Self Transformations

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
We propose SelfVC, a training strategy to iteratively improve a voice conversion model with self-synthesized examples.
Previous efforts on voice conversion focus on factorizing speech into explicitly disentangled representations that separately encode speaker characteristics and linguistic content. 
However, disentangling speech representations to capture such attributes using task-specific loss terms can lead to information loss. 
In this work, instead of explicitly disentangling attributes with loss terms, we present a framework to train a controllable voice conversion model on entangled speech representations derived from self-supervised learning (SSL) and speaker verification models. First, we develop techniques to derive prosodic information from the audio signal and SSL representations to train predictive submodules in the synthesis model. 
Next, we propose a training strategy to iteratively improve the synthesis model for voice conversion, by creating a challenging training objective using self-synthesized examples.
We demonstrate that incorporating such self-synthesized examples during training improves the speaker similarity of generated speech as compared to a baseline voice conversion model trained solely on heuristically perturbed inputs. Our framework is trained without any text and achieves state-of-the-art results in zero-shot voice conversion on metrics evaluating naturalness, speaker similarity, and intelligibility of synthesized audio.
~\footnote{\fontsize{8}{8}{Webpage: \url{https://shehzeen.io/selfvc/} }}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
* The paper focuses on zero-shot voice conversion and presents a framework for training a voice conversion model. The authors introduce a method that leverages entangled speech representations obtained from self-supervised learning (SSL) and speaker verification models. Additionally, they propose a novel training strategy that enhances the synthesis model for voice conversion through the use of self-synthesized examples.

### Strengths
* The paper combines strategies from voice conversion and singing voice conversion to improve zero-shot voice conversion. One noteworthy contribution is the introduction of a novel training strategy that utilizes self-synthesized examples for data augmentation and iterative improvement of the generation model. This represents a significant advancement from traditional approaches that heavily relied on heuristic transformations.

* The paper conducts comprehensive experiments. By extensively comparing the proposed framework with several baseline models, the authors effectively demonstrate its efficacy. 

* Overall, the paper successfully presents a valuable contribution to the field of voice conversion and offers an approach for achieving zero-shot voice conversion.

### Weaknesses
 * The main framework presented in this paper appears to draw from existing voice conversion and singing voice conversion techniques, such as utilizing SSL features, speaker embeddings, and incorporating prosody information like duration and pitch. These strategies resemble prior work ([1-3]) in the field. Additionally, the synthesizer's approach showcases similarities to methods used in speech synthesis, specifically resembling techniques employed in FastSpeech 2 [4]. To support these statements and provide a comprehensive overview of the related work in the field, it would be beneficial for the authors to provide appropriate citations and conduct comparative analyses.

* Moreover, the claim of the framework's efficiency in scaling to other languages through the introduction of SSL features is not unique to the authors' proposed model since similar approaches have been explored elsewhere.

* Additionally, it is worth noting that the concept of data augmentation using self-synthesized examples has been discussed in the literature, particularly in the context of speaker verification [5]. 

* Furthermore, the experimental results suggest that the inclusion of self-synthesized examples for data augmentation yields only a marginal improvement in the model's performance.

* Consequently, a deeper analysis or controlled study could be conducted to better isolate and understand the specific effects of the proposed training strategy from other contributing factors.

### Questions
* The authors should clarify what specific aspects of their framework, beyond the use of SSL features, contribute to this scalability to strengthen the claim of originality in this regard.

* Could the authors elucidate the unique characteristics or modifications they have made within their framework that differentiate it from other SSL-based voice conversion models?

* The introduction of the self-synthesized examples as a data augmentation method is intriguing. However, its efficacy and broader applicability remain questions. Can the authors provide experimental evidence or analysis showcasing the generalizability of this data augmentation technique across various methods?

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
In this research, the authors introduce a new training strategy called SelfVC, aimed at enhancing voice conversion models by iteratively improving them using self-synthesized examples. While previous voice conversion efforts focused on separating speech attributes like speaker characteristics and linguistic content, this often results in the loss of finer details such as accents and emotions from the original audio. Instead of explicitly disentangling these attributes with loss terms, the authors propose a new approach that utilizes entangled speech representations derived from self-supervised learning and speaker verification models. 

SelfVC framework comprises several key components. The authors introduce a training strategy that leverages self-synthesized examples to iteratively enhance the voice conversion model which is in contrast to NANCY or NANCY++. In this approach, the current state of the synthesis model is used to generate voice-converted versions of an utterance, which are subsequently used as inputs for the reconstruction task. This method ensures a continuous and purposeful refinement of the model.

The authors show that incorporating self-synthesized examples during training significantly improves the speaker similarity of the generated speech compared to a baseline voice conversion model trained solely on perturbed inputs. Since the framework does not rely on text, it can be applied to zero-shot voice conversion, voice conversion across different languages, and controllable speech synthesis with pitch and rhythm modifications. 

The experiment section consist of matched and mismatched scenarion to give a better indication of the model's performance. In the matched setting, the authors evaluate the proposed model for speech reconstruction while in the mismatched scenario, speaker conversion is carried out.

### Strengths
The main strengths of the paper are:

The authors present a novel model focused on enhancing speaker conversion that operates independently of language and text. The core concept behind this model centers on iterative self-improvement. They address the challenges associated with the disentanglement of speaker and content attributes, which typically require auxiliary task training. Therefore, using self-improvement via iterative refinement provides a way to circumvent this disentanglement problem.

Their experiments conducted on the LibriTTS dataset reveal impressive reconstruction quality in both guided and predictive modes. Extending their investigations to CSS10 and VCTK datasets, the model demonstrates excellent performance in zero-shot scenarios and exhibits language-agnostic capabilities.

To evaluate their model, the authors employ a range of meaningful metrics, including CER, PER, SV-EER, and qualitative measures, providing comprehensive comparisons with several state-of-the-art models.

### Weaknesses
The main weakness of the work are as follows:

1. The proposed technique is relatively simple and falls short on the novelty axis. There are several works leveraging the idea of self-refinement which have been recently published such as:
(a) Self-Refine: Iterative Refinement with Self-Feedback - Madaan et. al.
(b) Meta Self-Refinement for Robust Learning with Weak Supervision - Zhu et. al.
(c) Safe Self-Refinement for Transformer-based Domain Adaptation - Sun et. al.

2. The authors mention that the proposed model is trained with fixed (pitch/formant) transformation for the first 100k steps and use self-refinement afterwards. A comparison of how the performance differs when the model is trained completely on deterministic transformation would strengthen the results.

### Questions
The authors should perhaps explain why in Table 1, 2 and 3, the PER is high on the real data but it goes down after processing through the voice conversion module. Is the overall pipeline achieving some sort of speech enhancement too?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces SelfVC, a novel training strategy aimed at enhancing voice conversion models using self-synthesized examples. The proposed model integrates prosodic information from the audio signal for predictive training and uses a unique iterative training approach with self-synthesized examples for continuous model refinement. Compared to previous methods, SelfVC sets new SOTA in zero-shot voice conversion regarding naturalness, speaker similarity, and audio intelligibility.

### Strengths
1. The paper is well-composed, presenting its methodology with clarity. 
2. The extensive experiments support the presented claims. 
3. The demo provided by the author indicates the method's effectiveness.

### Weaknesses
Self-VC is similar to recent VC work (NANSY), except it uses pitch and duration predictors like ACE-VC. Also, as for the proposed training strategy (self transformations), random speaker embedding are commonly used for training a voice conversion model (e.g., https://arxiv.org/pdf/1806.02169.pdf, https://arxiv.org/pdf/2305.15816.pdf, https://arxiv.org/pdf/2305.07204.pdf,https://proceedings.neurips.cc/paper/2021/file/0266e33d3f546cb5436a10798e657d97-Paper.pdf). The fundamental idea seems the same. This point needs to be discussed more carefully.

### Questions
/

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
