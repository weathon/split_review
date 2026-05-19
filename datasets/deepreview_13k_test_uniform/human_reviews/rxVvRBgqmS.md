# PianoMotion10M: Dataset and Benchmark for Hand Motion Generation in Piano Performance

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Recently, artificial intelligence techniques for education have been received increasing attentions, while it still remains an open problem to design the effective music instrument instructing systems. Although key presses can be directly derived from sheet music, the transitional movements among key presses require more extensive guidance in piano performance. In this work, we construct a piano-hand motion generation benchmark to guide hand movements and fingerings for piano playing. To this end, we collect an annotated dataset, {\comicfont PianoMotion10M}, consisting of 116 hours of piano playing videos from a bird's-eye view with 10 million annotated hand poses. We also introduce a powerful baseline model that generates hand motions from piano audios through a position predictor and a position-guided gesture generator. Furthermore, a series of evaluation metrics are designed to assess the performance of the baseline model, including motion similarity, smoothness, positional accuracy of left and right hands, and overall fidelity of movement distribution. Despite that piano key presses with respect to music scores or audios are already accessible, {\comicfont PianoMotion10M} aims to provide guidance on piano fingering for instruction purposes. The dataset and source code can be accessed at \url{https://agnjason.io/PianoMotion-page}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents PianoMotion10M, a large-scale dataset designed to advance hand motion generation in piano performance, featuring 116 hours of piano videos annotated with 10 million hand poses. To complement this dataset, the authors introduce a baseline model that generates realistic and continuous hand motions from piano audio, using a position predictor and a gesture generator. The dataset and model are aimed at improving AI-driven piano instruction, with metrics to assess motion quality, smoothness, and positional accuracy.

### Strengths
1. Originality and Dataset Contribution: The PianoMotion10M dataset provides a novel resource, combining piano audio and video data with detailed 3D hand pose annotations across 116 hours of performance. This dataset addresses a significant gap by providing high-resolution, continuous hand motion data, which is essential for realistic AI-driven piano instruction and training, especially in guiding hand positioning and transitions.

2. Comprehensive Benchmark and Evaluation Metrics: The paper introduces a set of detailed evaluation metrics, including Frechet Gesture Distance, Wasserstein Gesture Distance, and Position Distance, to assess motion fidelity, positioning accuracy, and smoothness. This comprehensive approach to benchmarking supports the model’s effectiveness and provides a robust foundation for future research in hand motion generation.

3. Well-defined Baseline Model: The baseline model combines a position predictor with a gesture generator to generate realistic hand motions based on audio input, demonstrating the dataset’s utility. The use of a diffusion probabilistic model for gesture generation adds an innovative approach to capturing continuous motion, enhancing the quality of generated hand movements and reinforcing the practical application of PianoMotion10M in piano instruction.

### Weaknesses
1. Supplementary Material and Generation Results: The supplementary material lacks corresponding piano music for the generated hand motions, making it difficult to assess the quality and realism of the generated performance. Including paired audio and visual outputs would provide a more complete evaluation of the model’s effectiveness.

2. Dataset Collection Process:
The collection and preprocessing of data, essential to any dataset creation work, lack clarity. Specifically, the paper does not thoroughly explain the data acquisition process in Section 3.1.
While the authors mention in line 213 that "3,647 candidate videos" were collected, it remains unclear how these videos were queried or selected.
In line 240, the authors state that they "remove videos where hand regions are frequently obstructed or invisible." However, they do not provide a clear definition of what constitutes "frequently obstructed or invisible," making it hard to understand the filtering criteria.
Line 236 mentions manually selecting pure piano music to ensure no vocals or sounds from other instruments, but it’s unclear why an automated audio event detection approach (such as [1]) wasn’t considered for this task.

3. Annotation Quality and Relevance:
The quality of annotations is crucial in generating reliable datasets. In line 251, the authors mention "we transcribe the piano performances into MIDI files by utilizing a state-of-the-art automatic piano transcription (Kong et al., 2021)". However, this method, although effective, was developed in 2021. The authors do not address whether they explored more recent transcription methods (such as [2-5]) or provide experiments comparing different methods to validate their choice.

4. Additionally, while MIDI signals are provided, they are not used in the hand motion generation task. It would be beneficial to validate the quality and relevance of MIDI annotations, potentially by incorporating MIDI data into the baseline model to assess its impact on hand motion generation. This could offer valuable insights for future research.

[1] Kong Q, Cao Y, Iqbal T, et al. Panns: Large-scale pretrained audio neural networks for audio pattern recognition[J]. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2020, 28: 2880-2894.

[2] Maman B, Bermano A H. Unaligned supervision for automatic music transcription in the wild[C]//International Conference on Machine Learning. PMLR, 2022: 14918-14934.

[3] Gardner J, Simon I, Manilow E, et al. MT3: Multi-task multitrack music transcription[J]. arXiv preprint arXiv:2111.03017, 2021.

[4] Toyama K, Akama T, Ikemiya Y, et al. Automatic piano transcription with hierarchical frequency-time transformer[J]. arXiv preprint arXiv:2307.04305, 2023.

[5] Cheuk K W, Sawata R, Uesaka T, et al. Diffroll: Diffusion-based generative music transcription with unsupervised pretraining capability[C]//ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023: 1-5.

### Questions
Please see Weakness.

### Soundness
3

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
3

### Summary
The paper has two main contributions:
1) A dataset of 100+ hours of piano performance audio and (overhead) video, MIDI, and hand motion sequences, all aligned.
2) A baseline method for generating hand motion sequences from piano audio.

### Strengths
The main strength of the paper is that this is a really cool dataset linking piano performance audio (and MIDI) to hand motion sequences.  Piano playing is a challenging task requiring extreme dexterity, and this dataset seems like an important contribution to the research community.

The paper is clearly written and provides something new and of value.

### Weaknesses
The biggest thing missing is some sort of verification that a hand motion sequence *actually results in the target audio* when applied to a piano, using a physical model.  I recognize that this may be considered out of scope, but without it it's hard to trust even the ground truth provided in the dataset.  And then all of the metrics for the baseline method end up comparing generated hand motions with the ostensible ground truth hand motions, which has two issues:
1) The ground truth hand motions may have errors.
2) Even if the ground truth hand motions are accurate, there may be multiple possible hand motions to generate a given performance audio, none more "correct".
However, I think this may be okay if the dataset is positioned as "how some pianists performed these pieces" rather than "how one *should* perform these pieces".

An uncited research paper related to the above point is RoboPianist (Zakka et al. 2023): https://kzakka.com/robopianist/

I'm not sure why the baseline method included attempts to infer hand motions directly from audio, rather than going through MIDI.  MIDI (including note velocities) seems like it would contain all of the information needed to reconstruct the hand motions, and is *much* more compact than the raw audio.  If this is incorrect, it would still probably be worth mentioning in the paper.

The paper doesn't include a discussion of sustain pedal.  It seems as though the piano transcription method used *does* transcribe pedal events, which seem like they would be necessary to include in the baseline method otherwise much piano audio would be impossible to perform hands-only.  However, since the baseline method goes straight from audio to hand motions, the model is forced to implicitly transcribe sustain pedal in order to determine the hand motions.  Is that correct?

The paper raises a bunch of questions that I am curious about but were not discussed, specifically related to limits of the method and failure modes.  The examples included in the supplementary material are sort of "easy".  What happens if you give the baseline method virtuosic piano audio e.g. the MAESTRO dataset?  What happens if you speed up the audio so that it's no longer humanly playable?  What happens if you play intervals that human hands can't accommodate?

### Questions
I don't have questions though I'd probably accept the paper as is.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper addresses the challenge of hand motion generation for piano performance, recognizing the gap in current AI systems for musical instruction, particularly for instruments like the piano where hand positioning is critical.  The proposed PianoMotion10M serves as an important dataset aimed at solving this problem.

### Strengths
1. This is a large-scale dataset comprising 116 hours of piano performance from 14 professional players and 10 million annotated frames. The videos are collected under specific constraints (e.g., high resolution, bird’s-eye perspective) to ensure quality and consistency.

2.  The data collection and annotation method is well-structured, using tools like MediaPipe and HaMeR for robust hand pose detection. 

3. The dataset is indeed a valuable contribution, likely to support advancements in both piano instruction and broader motion generation research.

4. The two-stage design—featuring a position predictor and a position-guided gesture generator—seems well-suited for this task and shows reasonable quality. The model uses a diffusion-based architecture with a U-Net structure, which allows it to generate natural, fluid gestures that are better suited to piano performance.

### Weaknesses
1. The paper acknowledges the dataset’s limitations, particularly the need for improved diversity in piano positions and video sources, now only include 14 people. Addressing the inconsistency in piano tones and alignment of keyboard positions remains critical for achieving high-fidelity results.

2. A suggestion to include related work: Audeo: Audio Generation for a Silent Performance Video. Kun et,al (NeurIPS 2020).

### Questions
1. Do authors have some human evaluation results for the generated motions? It would be better if these could be incorporated.

2. Ethic concern and copyright issue: Since permissions were obtained from Bilibili users, how does the dataset’s open accessibility align with potential copyright restrictions or privacy concerns, particularly for identifiable hand features? I know that they do have some restrictions on this.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a large dataset consisted of piano music and aligned MIDI and hand positions containing 116h of recordings and 14 subjects. The goal of the dataset is to train generative processes to renderize 3d human-hand motion videos. This work presents an interesting baseline method to renderize hands.

### Strengths
In descending order of importance:

- A large dataset for hand pose generation is proposed. This is original, clear, and significant.
- A model is proposed. This is technically original, but the significance is not well discussed for the reasons stated in the comments.
- A set of measures for performance is proposed. They are not original, nor their significance to the problem is discussed.

Overall, I find the article interesting, although I am not sure how many people are specifically trying renderize hand poses in pianos using audio as input. However, this dataset could also be used for other tasks, which broadens its impact.

- The initiative of making a dataset for this task is great, and the ethics statement covers most of the potential problems,
- The dataset has some potential problems that could be taken care of, especially the long-term availability and the reliance on a specific company and several users to maintain the data,

### Weaknesses
There is a great emphasis in the proposed model whereas the proposed dataset and measures are not well discussed. I would suggest focusing the paper on the dataset and on the discussion on the metrics and skip the model proposal altogether. In special, this is because the model uses more data than any other model, hence it is expected to approach the data distribution better than other models.

- The presented model is interesting, but its performance is close to EmoTalk (more on that in item 4)
- I miss some discussions on the metrics and their relationship with the problem, and the space taken by describing the baseline method could be used for that. In fact, EmoTalk and LivelySpeaker, according to Table 3, are already interesting for future comparisons and their metrics are very close to the proposed method's.

One aspect that has not been addressed is a description of styles, genres, levels of expertise, and other biases in the dataset. This leads to thinking that the dataset polarized towards particular styles of playing (for example: ragtime versus classical). This is not a problem per se, as it is unavoidable; however, not *knowing* what these biases are can become a problem.

### Questions
I do have questions regarding the text:

Section 4.3: The learning rates are said to be 2e^{-5} and 5e^{-5}. The math reads: 2 (or five) times exp(-5). The usual reporting method is to use 2 (or 5) times 10^{-5}. Was that a typo, or are you really using the Euler number to define learning rates? If so, is there a reason for such?

Section 3.2: 
- MIDI files with high discrepancies were adjusted: what is the measure for a "high discrepancy"? The issue here is that, if this dataset is going to be used as a benchmark, there should be a measure on how much it differs from reality.

- Data uses a Savitzky-Golay filter. This filter is applied to the data in the dataset to increase smoothness. What are the filter parameters (order, frequency response, etc.)? Also, why was this specific type of filter chosen instead of the standard ones (a Butterworth filter seems adequate)? What is the impact of not using the filter?

Section 3.3: All videos are accessible with the IDs in the Bilibili website. Is Bilibili aware and consenting with the idea that there will probably be robots scraping their data without using their website? That is, are there chances that Bilibili will simply include barriers that would harm the dataset? Also, if users take down their own videos, how would that impact the dataset?

Section 4.3: The GPU has 24GB of RAM. How big is the model itself? How long did training take? Also, are you planning on releasing the trained weights?

Section 5.1:
- Several metrics are proposed, which is a good thing. However, none of the metrics were discussed in terms of their relevance to the real problem. For example: what kind of "error" in the rendering could be highlighted by the FID, FGD or WGD? Without this discussion, the metrics simply pose a "competition" on who gets better values. A phrase such as "The WGD metric offers a robust measure of dissimilarity between the generated motion and ground truth." does not clarify if this dissimilarity consists of a jittery behavior, an offset, an error in velocity, fingers being rendered too long (or too many!), and so on. Such a discussion, with clear examples, could clarify why these specific metrics were used, and not others.
- Also, the metrics imply in a comparison with a ground truth. This is not wrong per se, but, when hands are rendered, is there really a "ground truth"? That is, if two pianists play the same excerpt, wouldn't their hands be slightly different? So, more than increasing the proximity to a ground truth, the goal of the algorithms should be to obtain results that are within a distribution for human differences, not simply to approach a unique ground truth.
- In this same line of thought, does it really make a visible difference to have small variations in these metrics? For example, going from FGD=0.360 to FGD=0.351 is a difference of 0.009 - what type of difference does that reflect in the actual performance?
- How do these measures compare with a Mean Opinion Score (MOS)? It would be great to have some evidence that the proposed measures can substitute MOS, because collecting human opinions is costly. However, we need evidence for such.
- Minor suggestion: in Table 3, make the Right Hand appear to the right of Left Hand.
- A not so minor aspect: why are the measurements so different between the hands? Afterall, we have the same amount of data and the same models for them, correct? According to the data, Wav2Vec+TF is better at rendering left hands, while HuBERT+TF is better at right hands (according to WGD), which seems to indicate that their performance is actually the same and the differences are due to noise/chance/variance.

Section 5.2
- Figure 4 states that "Ours" is close to "GT" (or: the blue hands are closer to the gray ones). This is true, at least for this example; but in general the green and yellow hands seem to be equally plausible hand positions. In the third line, the yellow hands (LiveSpeaker) seem to be even more emphatic on the fact that the left hand is not playing anything.

### Soundness
3

### Presentation
3

### Contribution
3
