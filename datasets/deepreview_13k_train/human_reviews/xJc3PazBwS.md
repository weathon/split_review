# Disentangling Textual and Acoustic Features of Neural Speech Representations

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Neural speech models build deeply entangled internal representations, which capture a variety of features (e.g., fundamental frequency, loudness, syntactic category, or semantic content of a word) in a distributed encoding.
This complexity makes it difficult to track the extent to which such representations rely on textual and acoustic information, or to suppress the encoding of acoustic features that may pose privacy risks (e.g., gender or speaker identity) in critical, real-world applications.
In this paper, we build upon the Information Bottleneck principle to propose a disentanglement framework that separates complex speech representations into two distinct components: one encoding content (i.e., what can be transcribed as text) and the other encoding acoustic features relevant to a given downstream task. We apply and evaluate our framework to emotion recognition and speaker identification downstream tasks, quantifying the contribution of textual and acoustic features at each model layer.
Additionally, we explore the application of our disentanglement framework as an attribution method to identify the most salient speech frame representations from both the textual and acoustic perspectives.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Many standard speech representations are learned in a self-supervised way (HuBERT, w2v2, etc) and hence are, essentially, entangled blackboxes that have acoustic and textual features mixed in them in an arbitrary way. One can imagine scenarios where this is undesired, and it would be better to have a control over what/how features are encoded. This paper proposes a method building such disentangled representations, using the IB principle. As a running example, the paper opposes information that encodes textual content and acoustic information, encoding emotion or speaker identity. The paper shows that their method successfully disentangles the inputs features (variants of HuBERT, W2V2). The authors conclude with several interpretability studies of the models that use those features.

### Strengths
* I find the "disentanglement evaluation" part pretty convincing.

### Weaknesses
 * The proposed method assumes that we have labeled tasks for all potential downstream tasks. So one starts with general-purpose self-supervised representations such as HuBERT -- which are entangled -- and ends up with representations that are (a) disentangled, but (b) are likely only useful for the tasks where we have labels. In this scenario, I am not entirely convinced that one has to use VIB. The core issue is that the method appears to trade general-purpose representations for task-specific ones, limiting its applicability. The disentanglement is achieved through task-specific labels, which means the resulting representations are not generally disentangled but rather disentangled with respect to the specific tasks used during training. This significantly reduces the method's utility for unseen tasks.

* I am not entirely convinced by the motivations of the paper. If one needs to be confident that models do not use non-textual information while taking decisions, they can train models to make those decisions using pure transcripts. This is a simple baseline solution the paper should be having in mind. The paper should clarify why a disentangled representation is needed when a simpler approach of training directly on transcripts would suffice for text-based tasks. The argument that acoustic features are beneficial for emotion and speaker identification is valid, but it doesn't justify the need for disentanglement when the goal is to avoid reliance on those features for text-based tasks. The paper needs to better articulate the specific scenarios where disentangled representations are necessary and where training on transcripts is insufficient.

* There are some concerns wrt the experimental setup -- see Questions 2, 3, 4.



### Questions
1. L30 mentions that Whisper has highly entangled representations, in the same list as HuBERT or Wav2Vec2. It is never mentioned/evaluated later; is there any evidence that it is likely to have as entangled representations as SSL models from this list? It is trained purely in a supervised way for text transcription/translation, iirc, hence I would assume it learns purely text-focused features.

2. Do I understand it correctly that non-standard splits of LibriSpeech are used for the purpose of "ensuring an equal representation of gender and speaker ID" (S3.3) Is there a strong reason for that in the text transcription tasks? For the sake of comparability with all the existing literature, I would advise using standard some dev/test-{clean,other} splits.

3. Having a single linear probing classifier gets WER of ~50 for W2V2 and HuBERT. Only the pre-finetuned models get reasonable error rates. Is this a good evaluation setup to draw conclusions from?

4. What dataset is used to calculate WER in Table 1? Is this a mix of LibriSpeech and CommonVoice? Those are very different datasets, it would make sense to report them separately.

5. At least a part of motivation of the work is that by using disentangled representations one can be confident that model is using the features it is allowed to. For instance, the model doesn't rely on leaking gender or voice information when making text-based decisions. I generally get the idea, but the transcription vs gender/emotion classification task split is not a particularly convincing combination. If we are worried that the model uses something beyond the text content when making some downstream decisions, we can replace it with an (ASR + text classifier) model. Can we think of a more convincing scenario?

6. Do we actually need VIB? How different it would be if we used the labels to train a combination of ASR, Speaker and Emotion classifiers and used their outputs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper describes an application of information bottleneck training to isolate aspects of a speech representation.  The description of the approach is quite clear.  The paper includes a variety of analyses of the learned representations that show that disentangling is achieved.

### Strengths
The described approach is sensible and its specifics are clearly described.

There are a number of interesting analyses based on probing experiments to attempt to identify what information is still available in different layers of the network and assessment of the information related to distinct tasks in different frames of the input audio.

### Weaknesses
The motivations in the abstract and conclusion are not well connected to the modeling and analysis.  E.g. one motivating application is to minimize the privacy risk from encoder representations.  This hasn't been assessed in the model or paper.

The disentangling approach is based on supervised tasks.  The contributions necessary for emotion classification or speaker id.  It is unclear how these learned representations would transfer to some new task. Would this approach need to be extended to a "stage 3 training process?

Multiple training stages incur additional complexity.  It would be interesting to see if these multiple objectives would be included into a single stage training.

The impact on performance in Table 1 does not deliver a consistent message.  The Transcription show substantial regressions in both of the FT representations.  The improvements to Emotion and Speaker Id are stronger but more consistent on the large sized models while on the Base sizes, there are regressions on the wave2vec variants.  This sensitivity to SSL objective and model size suggests that this approach may not be robust to new tasks or architectures.

### Questions
Why subsample Librispeech and Common Voice so heavily for the transcription task?  Librispeech contains 960h of transcribed audio, but this approach uses less than 20.

How important is the ordering of the tasks?  Would the performance be identical if Emotion or Speaker Id were stage 1 and Transcription was stage 2?

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
The paper uses the Variational Information Bottleneck framework to separate textual and acoustic features of representations from SSL speech models, such as HuBERT and wav2vec2. This approach involves two stages: first, it isolates textual information by training models to transcribe content with minimized other unrelated information. The second stage targets acoustic features for tasks like emotion and speaker recognition.
They validate the proposed method through experiments on ASR, emotion recognition and speaker identification, showing its effectiveness in distinguishing between acoustic and textual attributes. This approach also has potential applications in privacy preservation, where disentangling speaker identity from transcription could help secure ASR systems.

### Strengths
1. The paper is well-written and is easy to follow.
2. The proposed approach is easy to use.
3. Experiments in Section 6 align in part with the findings of previous work on layer-wise speech SSL models[1], reflecting the effectiveness of the proposed method.


[1] A. Pasad, B. Shi and K. Livescu, "Comparative Layer-Wise Analysis of Self-Supervised Speech Models," ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP),

### Weaknesses
1. There is previous work using the Information Bottleneck for feature disentanglement, such as in [2] and [3]. It would be better to cite these studies and highlight the distinctions between this paper and prior work.
2. Experiments comparing the proposed method with existing approaches are lacking. As there are lots of works for speech representation disentanglement like AutoVC, SpeechSplit, or FAcodec[4] , it would strengthen the paper to report the performance of at least one existing methods.
3. In Table 1, VIB loses essential information for textual representation, resulting in a much higher WER compared to Probing for HuBERT-FT and Wav2Vec2-FT. Training on a different dataset with positive outcome might help alleviate this issue. The high WER suggests that the VIB method, as implemented, may be discarding crucial textual information during the disentanglement process, which is a significant concern for its practical application in ASR tasks.

### Questions
1. What is the reason for using the mixture of LibriSpeech and Common Voice?
2. The WER reported in Table 1. seems to be higher than expected. What is the possible reason for that? For LibriSpeech, what subset is used in the experiments? LibriSpeech-clean or LibriSpeech-other?
3. The Information Bottleneck (IB) method focuses on retaining only information that’s relevant for predicting the target variable, filtering out anything unnecessary. This makes it dataset-dependent. For instance, when I train the stage 2 framework on a dataset for emotion recognition, the disentangled features capture emotional information but lacks speaker-specific information. I wonder if it would be possible to handle both speaker recognition and emotion recognition in stage 2, so that we preserve both emotion-related and speaker-related information. Alternatively, we could consider adding a stage 3 focused on speaker identity, while stage 2 remains dedicated to emotion recognition.

### Soundness
2

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
4

### Summary
This paper proposes a new framework for disentangling speech representations from neural speech models (like Wav2Vec2 and HuBERT) into two distinct components: textual content (what can be transcribed as text) and acoustic features (like emotion or speaker identity). This separation is important because neural speech models typically create deeply entangled internal representations that combine various features, making it difficult to isolate specific information or suppress potentially sensitive acoustic features (such as gender or speaker identity) in real-world applications.
The authors present a two-stage training framework based on the Variational Information Bottleneck technique. In the first stage, a decoder is trained to map speech representations to text while minimizing irrelevant information from input, ensuring only features necessary for transcription are preserved. In the second stage, another decoder is trained that has access to the textual representation from previous stage and is trained to predict target labels for downstream task while minimizing information encoding. They evaluated their framework on emotion recognition and speaker identification tasks, demonstrating that the resulting representations were effectively disentangled - the textual representations could predict transcriptions but performed randomly when predicting acoustic features, while acoustic representations showed the opposite pattern.
The authors also analyzed how different layers of pre-trained and fine-tuned Wav2Vec2 models contribute to emotion recognition. They found that in models fine-tuned for automatic speech recognition (ASR), the acoustic contribution to emotion recognition decreases in higher layers while the textual contribution increases. Additionally, they showed that their framework can serve as a feature attribution method to identify the most significant frame representations for a given task, distinguishing between textual and acoustic contributions.

### Strengths
The main strengths of the paper are as follows:
1. The authors provide a clear motivation and explanation for the problem under consideration.
2. The method is clearly explained, creating no confusion in grasping the idea. 
3. The experiment section is well-written with relevant experiments
4. The authors answer some key questions related to the work such as extent of disentanglement and its benefits
5. The last section of the paper talks about prior works which are in the same domain to provide readers an idea about the novelty in this work. 
6. The authors have further cited rsome extremely elevant works.

### Weaknesses
Here are the main weaknesses:
1. I struggle to understand the new idea in this work because the VIB technique has existed for a while.
2. The concept of employing neural networks to learn or estimate bounds on Mutual information has existed for a long time (see 
    a. MINE: Mutual Information Neural Estimation by Mohamed Ishmael Belghazi, Aristide Baratin, Sai Rajeswar, Sherjil Ozair, Yoshua 
        Bengio, Aaron Courville, R Devon Hjelm. 
    b. DEEP VARIATIONAL INFORMATION BOTTLENECK by Alexander A. Alemi, Ian Fischer, Joshua V. Dillon, Kevin Murphy
    c.  Representation Learning with Contrastive Predictive Coding by Aaron van den Oord, Yazhe Li, Oriol Vinyals
3. The authors do not provide explanation in Table 1 regarding why WER increase for Fine-tuned models after disentanglement training. 
4. In Figure 2, there seems to be some strange behavior as far as prosody prediction is concerned. Pitch, intensity, rhythm, voice quality, etc have been identified as key contributors to the perception of emotion from speech. It makes little sense as to why the disentangled acoustic representation would remove that information.  
5. It has been shown before that different layers of Self-supervised models (HuBERT and W2V2) learn different types of representation from speech signal (acoustic, prosody and semantic). Therefore, section 6 reaffirms those prior studies while providing no new information for the infromed readers.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2
