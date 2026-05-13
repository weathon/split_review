# EcoFace: Audio-Visual Emotional Co-Disentanglement Speech-Driven 3D Talking Face Generation

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Speech-driven 3D facial animation has attracted significant attention due to its wide range of applications in animation production and virtual reality. Recent research has explored speech-emotion disentanglement to enhance facial expressions rather than manually assigning emotions. However, this approach face issues such as feature confusion, emotions weakening and mean-face. To address these issues, we present EcoFace, a framework that (1) proposes a novel collaboration objective to provide a explicit signal for emotion representation learning from the speaker's expressive movements and produced sounds, constructing an audio-visual joint and coordinated emotion space that is independent of speech content. (2) constructs a universal facial motion distribution space determined by speech features and implement speaker-specific generation. Extensive experiments show that our method achieves more generalized and emotionally realistic talking face generation compared to previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes EcoFace, a framework for generating 3D talking faces using speech signals. The framework first constructs an audiovisual emotion space that is independent of the speech content. Using a Variational Autoencoder the framework then generates FLAME parameters (a low-dimensional representation of facial movements). The model’s encoder is conditioned on both speech and emotion features to create a latent representation that captures expressive nuances. Finally, a decoder that is conditioned on the speaker is used for the facial animation generation. Experimental results show better performance in both emotional expressiveness and lip-sync accuracy when compared with state-of-the-art methods.

### Strengths
1. Novel approach for emotion disentanglement using speech and visual information.
2. Comprehensive evaluation through quantitative/qualitative metrics, user studies, and ablation experiments.

### Weaknesses
1. Some methodological choices are unclear, and additional evaluation details are needed (see questions).
2. Speaker-specific modeling. Generation can only be performed for speakers the model has seen during training.

### Questions
1. You mention in the introduction that your model can discriminate the signal of different types and intensities of emotion features. How does your model interpret varying intensities of emotion and how does the contrastive-triplet loss contribute to this? 

2. Sec. 4.1: To evaluate the methodology on the test set for unseen subjects you condition on all training identities. Why use all identities rather than a subset?

3. Although you retrained FaceFormer and CodeTalker on RAVDESS and HDTF, you did not retrain EMOTE which seems to provide better results than your approach on MEAD that the model was trained on. For fair comparison could you perform this experiment by retraining EMOTE on the RAVDESS too?

4. Table 3: Can you show the results on each dataset separately and for each emotion? Since your model was trained on RAVDESS it may contain some bias towards that dataset when compared with EMOTE.

5. Sec. 4.3,”Effect of emotion embeddings”: Have you tried to extract content features from an emotional speech signals? How would the model perform in this more challenging experiment?

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
5

### Summary
EcoFace addresses issues in 3D facial animation: feature confusion (lack of clear signals for content and emotion), emotion weakening (difficulty in controlling emotion intensity), and the mean-face problem (limited control over individual speaker’s style of expression). The authors tackle these issues by introducing explicit signals for emotional motion representation and intensity control using audio-visual loss and a contrastive triplet loss to distinguish emotion intensities. They also generate speaker-specific, stylized facial animations with a lip-sync discriminator.

### Strengths
The work presents following strengths:
1. EcoFace introduces an audio-visual emotion disentanglement mechanism to supervise the discrepancy between emotional information captured by facial motion and the audio stream, effectively capturing information from both audio and video. 
2. EcoFace controls within-emotion intensity by using an emotional triplet loss.

### Weaknesses
1. The GT videos on the webpage show severe issues, such as unnatural mouth closure and a jerky appearance, which don’t match the [original implementation](https://download.is.tue.mpg.de/emoca/assets/emoca_v2_comparison.mp4). Since EcoFace is trained on meshes obtained using EMOCA, the authors should clarify how their model produces improved animations compared to the GT animations on which it was trained, as shown in their demo videos.
2. The EMOTE comparison videos on the webpage don’t match the exemplar videos from other methods, such as [FaceTalk](https://youtu.be/7Jf0kawrA3Q?si=ZvxQT3FD27Eh-RDj), [3DiFACE](https://youtu.be/Mep5pAU3TPc?si=Pe93jkT_eC_pBjPZ), [EMOTE](https://download.is.tue.mpg.de/emote/EMOTE_SupMat_video.mp4) . Could the authors explain the observed differences?
3. Triplet loss in eq 7 operates within a single emotion space. Since it focuses on a single emotion, how does EcoFace ensure that emotion intensities for high arousal, high valence (e.g., surprise) are disentangled from those of high arousal, low valence (e.g., anger or fear)? The method needs to clarify how it handles the overlap in arousal for different emotions and their intensities.
4. Since EcoFace claims to generate speaker-specific animations, it would help to provide more details on the number of identities in the training set and any animation results for unseen subjects for better evaluation. The lack of a clear evaluation on unseen subjects is a significant gap in the current analysis.
5. Training details are unclear. With a batch size of 30, how are typical forward passes structured to use 2N pairs for computing contrastive loss in Eq. 4, and how is triplet loss computed per emotion in Eq. 7?

### Questions
1. L219: What kinds of augmentations were applied to the video frames and audio samples?
2. L225: The latent representations are averaged over the sequence. How is it ensured that continuous emotional information along the sequence is not lost? Could the authors provide more details on the contrastive loss in Equation 4, and clarify if other methods besides averaging were considered, such as mapping to a lower dimension with a learnable layer?
3. fig 1a: The method name is missing in the caption.
4. fig 1b: The triangle and circle shapes representing features lack labels indicating what they refer to.
5. fig 4 and Ablation Studies (pages 9,10): "Ecotalk" is used instead of "EcoFace."
6. What was the rationale for training the sync expert independently? How are the FLAME region landmarks obtained—are they input as rendered crops or as 3D vertices?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of separating emotional information from speech content in facial animation, which often leads to feature confusion and emotion weakening. This work, EcoFace, introduces audio-visual co-disentanglement and a speaker-specific motion generator to address these issues. By using an audio-visual loss for emotion consistency and a contrastive-triplet loss for distinct emotional space, EcoFace creates a low-dimensional motion distribution that captures speaker-specific styles for personalized animation.

### Strengths
1. The paper proposes a novel framework to distanglment emotion and speech content in the face synthesis field.
2. This work is well-written and well-organized.
3. The results shows the efficiency of the proposed framework.

### Weaknesses
Major Concerns:

1. LSE-C Range Consistency
   There appears to be a discrepancy in the LSE-C values reported in this manuscript compared to those commonly cited in the community. For instance, DINet [https://arxiv.org/pdf/2303.03988] lists an HDTF LSE-C value (as GT) of 8.9931, while the value reported in this work is 0.824. This large difference raises concerns about the evaluation methodology. It is crucial to understand if the authors are using a different implementation or if there is a normalization or scaling issue that is not clearly explained. The lack of clarity makes it difficult to compare the results with existing literature.

2. Definition Clarity for L_emo and L_sync in Ablation Study.
   The explanation of L_emo and L_sync in Table 4 is missing, which decreases in interpreting the results and understanding the contributions of each component. Without a clear definition of these loss terms, it's hard to assess the impact of each component on the overall performance of the model. This lack of transparency makes it difficult to reproduce the results and understand the ablation study.

3. Validity and Interpretation of VE-FID Metric
   Introducing VE-FID as a new metric to measure emotion expression is a great try. However, some results in Table 1 and Table 4 raise questions. For example, the comparison between EcoFace (21.57) and EmoTalk (51.98) shows a large difference, even when EcoFace lacks L_emo (30.88). This raises a significant concern: if EcoFace performs better on emotion-related metrics even without the emotion-related loss, it suggests that the metric might not be measuring what it intends to, or that the model's performance is not as dependent on the emotion loss as claimed. This undermines the validity of the metric and the claims made about the model's performance.

4. Lack of Results for Speaker-Specific Generation
   One of key contributions is implementing speaker-specific generation; however, the absence of results supporting this feature weakens its impact. The paper claims that the model can generate speaker-specific animations, but there is no empirical evidence to support this. Providing empirical evidence or case studies to demonstrate speaker-specific generation’s effectiveness would strengthen the claim. Without this, the contribution is not fully substantiated.

Minor Issues:

1. On Page 3, Lines 160-161, please use “Wav2Vec 2.0” instead of “Wav2Vec2”.

2. In Figure 1(a) on Page 4, the method name is currently missing.

3. On Page 10, in Figure 4(a) and Figure 4(c), Line 518, the label/term should be corrected from “EcoTalk” to “EcoFace.”

4. Demographic Information in User Study

### Questions
1. What is the demographic information in the user study?

### Soundness
3

### Presentation
3

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
This paper describes a framework for disentangling facial expressions of emotion from facial motions related specifically to speech.  The goal is to later re-synthesize expressive talking faces driven by speech.  Furthermore, a triplet loss is included to ensure that different expressions can be separated in the representation, and that the differences in the magnitude of same expression can be disambiguated.  To account for differences in the way that different people display facial expressions, the generator is conditioned on a learned identity embedding..

### Strengths
The problem being tackled is important and challenging.  We are highly sensitive to discrepancies in generated facial motion that accompanies speech.  This work tackles the problem by disentangling facial motion related to emotion from facial motion related to speech.  Furthermore, accounting specifically for the degree of expression is effective.

The work uses open data to aid re-producibility.  Furthermore, code will be made available.

The approach is effective.  The performance against the baselines is good.  The demo videos are impressive.  Talking head generators often cannot generalize to things like singing (because the sustained gestures look unnatural) but the approach here does an excellent job.  Furthermore, the differences in the articulation for different languages is very well captured.  For example, the lip-rounding in articulation of French speech is very impressive.

The ablations show the importance of the design of the components of the system.

I appreciate the inclusion and attention to detail in Section 4.3.

### Weaknesses
A limitation of the objective metrics, such as LVE, is that they do not account for type of error.  A larger LVE in the articulation of, say, /k/ might be insignificant, but a large error in the articulation of, say, /b/ is highly problematic.  I realize these are standard metrics, but I still see these as problematic for this reason.

See the questions/suggestions below.

### Questions
How is the level of emotion in the training data assigned?

On line 135 — is an element of s \in R^{n} the probability of that expression being present?

In Equation (7) how is alpha set?

In the paragraph following Equation (7), should z_l} be z_{i} to match the equation?

In Equation (11), does each term contribute equally to the loss?  There is no weighting to account for things like differences in scale?

On line 477 — you mentioned the margin that you beat the baselines by being 30.9%, 29.4%, and 41.24%.  This is not a margin though is it?  Are these not the scores that your approach attained?  The margin would be the difference.

*Suggestions*
Change references to. “speaker-specific” to “speaker-aware”.  Speaker-specific typically means that you train a different model for each individual speaker.  

On line 135 you mention “where each a \in R^{D} has D sampled audio.  I think you mean that each a \in R^{D} is a D-dimensional feature vector.  I am not sure what ”D sampled audio“ means.

In Section 3.1 it would help to specify that the speech features are latent features and not typical speech features, e.g., from a Mel-filter bank.

In Section 3.1 it was not clear that for T frames of audio, why there are 2T frames of emotion-related and 2T frames of content-related features.  Maybe explain this when these are introduced.

The equations should flow as part of the sentences.  Throughout the paper you end a sentence before providing the equation.

Line 146 — replace low-latitude with low-dimensional.

On line 232, you refer to “the voiceless phase”.  Voiceless has specific meaning in speech.  To be clear here you should avoid using this terms and refer to “periods where speech is not present”.  (For reference, voiceless speech is speech produced when the vocal chords are apart.).

### Soundness
3

### Presentation
3

### Contribution
3
