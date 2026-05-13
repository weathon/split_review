# HyDance: A Novel Hybrid  Dance Generation Network with temporal and  frequency features

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
We propose HyDance, a diffusion network utilizing both the temporal and frequency-domain representations of dance motion sequences for music-driven dance motion generation. Existing dance generation methods primarily use temporal domain representations of dance motion in their networks, which often results in the network losing the sfrequency-domain characteristics of the dance. This manifests in overly smooth generated dance motion sequences, resulting in dance movements that lack dynamism.  From an aesthetic perspective, such overly smooth movements are perceived as lacking expressiveness and the sense of power. To address this issue, we designed HyDance, which incorporates independent temporal feature encoders and frequency-domain feature encoders. The model employs a shared-weight hybrid feature encoder, enabling the complementary extraction of motion information from both domains. By introducing compact frequency-domain features into the dance generation framework, our method mitigates the oversmoothing problem in generated dance motion sequences and achieves improved spatial and temporal alignment in the generation results. Experiments show that our method generates more expressive dance movements than existing methods and achieves better alignment with the music beats.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to address the issue of unnatural movement generation in music-driven dance generation tasks by utilizing the frequency domain characteristics of movements to supplement the missing information in temporal features. The overall framework is based on the Diffusion model. Additionally, an encoder that integrates frequency domain features with temporal features has been designed to implement the proposed method of feature fusion for motion generation. The experiments are sufficient, and the maniscript is of high quality.

### Strengths
This paper introduces a method that enhances the naturalness of dance movements to align with human aesthetics by leveraging the frequency domain characteristics of movements. It employs a frequency domain feature extractor to capture the frequency domain features of the movements and designs a corresponding feature fusion encoder that combines temporal features, thereby more effectively improving the quality of generated movements.
This paper provides a detailed explanation of the proposed method, conducts a variety of experiments, and analyses the results. Particularly, it performs ablation studies on the designed frequency domain feature extractor and feature fusion encoder to demonstrate the effectiveness of these two modules. Additionally, the paper also designs a user study to validate the proposed method.
This paper provides an detailed description of the proposed method and its structure is well-organized. The experimental results are presented in a visual manner using charts and graphs.

### Weaknesses
1. The Section 3.1 of the paper regarding the representation of dance movement contains some ambiguity. Specifically, the description of "contact label" is unclear. Tseng et al. describe it as "the heels and toes of the left and right feet", but this paper's description of "front and back" is not clear. The lack of clarity makes it difficult to understand how the contact labels are actually encoded and used within the model. It is essential to specify whether 'front' and 'back' refer to the direction of the foot relative to the body or some other spatial relationship.

2. In Section 3.1, concerning the "a music sequence of length $L$", the unit of $L$ should be specified as "frames". Without specifying the unit, it is unclear how the music sequence is processed and aligned with the motion data, which is typically frame-based. This ambiguity could lead to misinterpretations of the temporal synchronization between music and dance.

3. In Figure 3, the processing of "music, time tokens" does not align with the explanation provided in Section 3.4 of the paper. The diagram suggests a direct concatenation or interaction of music and time tokens before entering the hybrid encoder, while the text describes a different process involving noisy motion sequences. This discrepancy needs to be addressed for clarity and consistency.

4. Figure 4 could incorporate the spectrum of the Ground Truth. Comparing the generated spectrum with the ground truth spectrum would provide a more comprehensive evaluation of the model's ability to capture the frequency characteristics of the motion. This comparison is crucial for validating the effectiveness of the frequency domain feature extraction.

5. Some parts are not very clear in this version. e.g.,  
    Enlarge the font in Figure 1. 
    Provide additional explanations for the arrows in Tables 1, 2, and 3.
    Offer supplementary explanations for the evaluation metrics "$DIV_k$" and "$DIV_g$". The current explanations of these metrics are insufficient for a reader to fully grasp their significance and how they relate to the quality of the generated dance movements. The arrows in the tables lack context, making it difficult to understand the relationships between the different experiments.

### Questions
1. In Section 3.3, regarding the explanation of “L_f2m”, there is a distinction that needs clarification between “the frequency domain representation of the motion sequence d^f” and “the reconstructed temporal representation of the dance sequence d ̂^f” compared to the “d_f” mentioned in Section 3.1. What is the difference between these representations?
2.In Figure 2, why does d^f input into the “Temporal Encoder”? What is the meaning of the arrows from the “Temporal Encoder” and the “Freq Domain Encoder” modules to the “Dance Decoder”?

### Soundness
3

### Presentation
2

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
The paper presents a method for generating 3D pose sequences of dances from input audio. The authors consider both the time and frequency domain representations of dance motions, and propose a Dual-Domain Hybrid Encoder to combine the temporal and frequency information, particularly the higher-frequency information that can get suppressed in traditional attention mechanisms. They leverage this combined representation in a transformer-based diffusion network to generate dances with high-frequency movements. They show the benefits of their proposed approach through quantitative and qualitative comparisons, ablation experiments, and a user study.

### Strengths
1. The idea of explicitly featurizing high-frequency information in the encoding process is intuitive and well-motivated, and the technical aspect of preserving those in the synthesized outputs is soundly presented.

2. The experimental results highlight the benefits of the proposed approach. Particularly, the visual results clearly show the benefits of leveraging high-frequency information for dances.

### Weaknesses
1. The authors motivate the utility of capturing high-frequency information at transitions of dance movements, which are arguably in sync with the music beats. While this is an empirically plausible idea, it lacks any discussion with similar ideas explored differently in the existing literature, such as [A] (not cited in the paper), which separately generates higher-frequency beat poses and lower-frequency in-between poses. Some discussions with other approaches exploring a similar idea would help contextualize the paper in the literature.

2. The key contribution of utilizing frequency-domain information can be explained in more depth. It would be informative to understand how the frequency domain information impacts the generative performance for different types of dances (e.g., slow-moving dances like waltz vs. dances with rapid movements like hip-hop). Also, since the frequency domain representation already captures information on the entire frequency spectrum, what additional information does the time-domain representation provide? Are there any particular correlations of different MFCC or Chroma components in the audio with the frequency representations of the different joints, particularly as the highest frequency in the dance increases (that is, the dance becomes progressively faster-paced)?

3. In addition, the quantitative and ablation experiments can also be explained in more detail to highlight the proposed contributions better. For example, why do the diversity scores (particularly DIV_k) drop by nearly half when the frequency representations and the Dual-Domain Encoder are removed (Table 3)? How are the generated dances able to achieve better scores than the Ground Truth on various metrics (Tables 2 and 3)?

4. Some details on the user study are also missing. Did the authors allow for ties in the study? Otherwise, the win rates might be inflated even if the generated dances are suboptimal. Further, the win rate over ground-truth dances is above 50%, which, coupled with poorer quantitative numbers of the ground-truth, raises further questions on what the ground-truth actually looks like and how the training process generates results that supposedly surpass the ground-truth in quality.

### Questions
1. How is the contact loss term (Eqn. 7) penalized when the predicted foot contact, $\hat{b}^{(i)}$, is wrong?

2. Please show the y-axis (amplitude) labels in Fig. 4 to make the figure readable. Currently, it is hard to understand the scale of improvements in the high-frequency region.

3. For the ablation experiment without the Dual-Domain Encoder, what encoder is actually being used?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The HyDance paper proposes a novel method for music-driven dance generation using a transformer-based diffusion network that incorporates both temporal and frequency domain representations. The authors emphasize the limitations of prior works that only leverage temporal representations, leading to oversmoothed, less dynamic dance sequences. By integrating frequency domain features, HyDance reportedly generates more expressive, realistic dances aligned with musical beats.

### Strengths
1. The approach does present some novel aspects in its methodolgy:
    i). Hybrid representation: Integrating both temporal and frequency representations for better capturing dance dynamics.
    ii). Dual-Domain Hybrid Encoder: This component introduces an interesting method to combine temporal and frequency-based motion representations, which is less common in dance generation tasks.

2. The experiments are generally well-structured, with comparisons against state-of-the-art methods like FACT, Bailando, EDGE, and BADM on the AIST++ dataset.

### Weaknesses
1. Qualitative results demonstration: Visual examples comparing generated sequences with other SOTA methods would be more helpful to show that the proposed method indeed generate better dynamics.

2. w/o Dual-Domain Hybrid Encoder, the model seems to achieve comparable performance against the full model except the DIV_k metrics. Could a human study conducted on these ablation versions to show that without w/o Dual-Domain Hybrid Encoder, the model cannot generate expressive dance motions.

### Questions
See weaknesses above.

### Soundness
3

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
This paper introduces HyDance, a novel diffusion-based model for generating dance from music. The core of the proposed approach lies in its ability to encode motion features in both the temporal and frequency domains, allowing for a complementary interaction during dance generation. Empirical evaluations on the AIST++ datasets demonstrate that HyDance surpasses existing state-of-the-art methods both quantitatively and qualitatively.

### Strengths
- The idea of leveraging frequency domain motion features to enhance music-driven dance generation is promising.
- The paper is written clearly and straight-forward to follow. Demo video in the supplementary material is also helpful.

### Weaknesses
 - Overall contribution is limited. The frequency domain motion feature extractor was proposed in PAE paper. This paper simply adapts it to music-to-dance generation. Considering that the original PAE paper already worked on motion sequences, the adaptation effort is also minor even for an application paper. Besides, the scope of taking the advantage of frequency domain motion features should not be limited to dance generation. It will be still useful for any conditional (complex) motion sequence generation problems but unfortunately authors did not investigate more.
- Experiments are conducted on AIST++ only. While it is a popular dataset, it has very limited music pieces, which means the model will definitely overfit the music data in AIST++. It would make more sense to test how well it can generalize to more general music pieces. The lack of diverse music input limits the conclusions that can be drawn about the model's ability to generalize to unseen musical styles and tempos. The model's performance could be highly dependent on the specific characteristics of the AIST++ music dataset.
- More analyses are required for frequency-related performance. For example, AIST++ has different dance motions for high and low BPMs. Is there any performance gap across different BPM? The paper should include a detailed analysis of how the model performs across different frequency ranges and BPMs, which could reveal potential limitations or biases in the approach. For instance, does the model struggle with fast-paced music or very slow, deliberate movements? This analysis is crucial for understanding the model's robustness.
- Some implementation details are missing such as the number of trainable parameters. How about the inference speed? With these additional hybrid encoders, will the generation speed be slower? The absence of these details makes it difficult to reproduce the results and assess the practical applicability of the proposed method. The computational cost, in terms of both training and inference, is a critical factor that needs to be addressed.
- Definitions and analyses of $DIV_k$ and $DIV_g$ are missing. The lack of clarity regarding these metrics makes it difficult to interpret the quantitative results. The paper should provide a clear definition of these metrics and explain why they are suitable for evaluating the diversity of generated dance motions.
- Details of user study are also missing. How did you select the video pairs? Why not have an additional 'neutral' option? How do you make sure 14 video pairs are sufficient? The methodology of the user study is not sufficiently described, raising concerns about the reliability and validity of the subjective evaluation. The paper should provide more details about the selection process, the number of participants, and the instructions given to the participants.
- The Figure 4 is not really informative. Examples in the demo video look better. Maybe a spectrogram (temporal-frequency) magnitude visualization could help?

### Questions
See questions in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1
