# Machine Unlearning in Audio: Bridging The Modality Gap Via the Prune and Regrow Paradigm

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 6, 3, 3, 5

## Abstract
The ubiquity and success of deep learning is primarily owed to large human datasets; however, increasing interest in personal data raises questions of how to satisfy privacy legislation in deep learning. Machine unlearning is a nascent discipline centred on satisfying user privacy demands, by enabling data removal requests on trained models. While machine unlearning has reached a good level of maturity in the vision and language domains, applications in audio are largely underexplored, despite it being a highly prevalent and widely used modality. We address this modality gap by providing the first systematic analysis of machine unlearning techniques covering multiple architectures trained on audio datasets. Our analysis highlights that in audio, existing methods fail to remove data for the most likely case of unlearning -- Item Removal. We present a novel Prune and Regrow Paradigm that bolsters sparsity unlearning through Cosine and Post Optimal Pruning, achieving the best unlearning accuracy for 9/12 (75%) of Item Removal experiments and best, or joint best, for for 50% (6/12) of Class Removal Experiments. Furthermore, we run experiments showing performance as unlearning requests scale, and we shed light on the mechanisms underpinning the success of our Prune and Regrow Paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the effectiveness of existing machine unlearning methods in the audio domain, focusing on the datasets AudioMNIST and SpeechCommands. The authors show that current unlearning techniques work for class removal but not item removal. To address this, they introduce Cosine Similarity and Post Optimal Prune within a Prune and Regrow paradigm and show improved performance (83% unlearning accuracy gap) for Post Optimal Prune.

### Strengths
1. This is the first detailed analysis of machine unlearning in audio. 

2. The proposed Post Optimal Prune method shows significantly improved performance for item removal unlearning accuracy gap.

### Weaknesses
1. The paper does not refer to [1], which provides a multimodal database for machine unlearning including audio and shows issues with machine unlearning with speech commands (see Figure 11). The submitted paper has a more detailed analysis with proposed improvement for machine unlearning, but this claim is false: "Our analysis highlights, for the first time, that, in audio, existing methods fail to remove data for the most likely case of unlearning – Item Removal."

2. Where is the 83% unlearning accuracy gap claimed in the abstract and line 69 explained? I don't see this in Table 2 or anywhere in the paper. If I average the unlearning accuracy gap for VGGish, CCT, and ViT I get 82.0%.

3. No source code is provided. The description of Cosine Similarity and Post Optimal Prune is insufficient to reproduce.

4. The author should explain why VGGish, CCT, and ViT are used. The models used in [1] make more sense: HuBERT (Hsu et al., 2021a) (Base, Large, X-Large), Wav2Vec2.0 (Baevski et al., 2020a) (Base, Large), Whisper (Radford et al., 2022) (Tiny, Base)

5. There should be more motivation in the introduction why this problem is important. For example, I understand why item removal is important (a person wants to remove all of their audio in a dataset) but why is class removal important for request to be forgotten?

6. There is no discussion if the proposed solution would comply with the GDPR requirements. What level of machine unlearning performance is required to comply with GDPR?

7. The paper does not explore the applicability of the Prune and Regrow paradigm to other data modalities like images, text, or video, which limits the impact of the findings.

### Questions
Figure 1-4 are not readable - please increase the font sizes.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study and evaluate different unlearning methods on two speech datasets, AudioMNIST and SpeechCommandsV2. They compare different setups of item and class removal, different sizes of the forget set, and different architectures. They report results on a wide variety of metrics. 

The authors propose a new method of unlearning "Prune and Regrow" as an improvement of pruning methods for unlearning. They show the proposed method does offer better performance on various metrics on the studied datasets.

Edit: In light of the authors reply and the added experiments, I have raised my scores for the paper.

### Strengths
- Extensive evaluation of different metrics and comparing different methods.
- Comparing different sizes of the forget set and different architectures.
- Good presentation and structure of the paper.
- Good explanation of the metrics and methods.

### Weaknesses
1. Unjustified focus on audio: Although the authors focus their presentation on audio, I didn't understand what makes the study or proposed method relevant to audio beside the datasets. The method can be applied to any NN. I don't see what makes audio special in this case and why the authors evaluated the proposed methods only on speech, or what characteristics of speech are relevant for this method to work. Suggestions:  (a) Comparing the results to similar experiments on non-audio tasks to highlight any audio-specific findings. 
 (b) Explaining any unique challenges or considerations for unlearning in audio domains.

2. Limited evaluation for audio considering only speech tasks: I think the audio domain is quite diverse. However, the authors focused the study on simple speech recognition tasks. I think the claims made in the paper are too broad for audio in general; other tasks must be considered, for example, music tasks (music genre classification), environmental sound recognition, and acoustic event detection and classification tasks. I agree that privacy concerns are paramount in speech tasks, but licensing and copyrights can also highlight the importance of unlearning in other audio tasks. Suggestions: Audioset and FSD50k , ESC50 for general audio tagging, GTZAN and Jamendo for music tasks
3. Training setup and not using audio models: The authors use (with the exception of the old VGGish model) models not adapted for audio. For example, on speech commands, why did the authors use ViT instead of the adapted AST [1] (ViT with patch overlap and pre-training) ? AST achieves 98% test accuracy on speech commands v2 35 classes, compared to the reported results of 84% ViT. This casts doubts on the validity of the results. Suggestions: (a) Consider running additional experiments with audio-specific architectures; (b) A discussion how the choice of architecture can impact the results; (c) A discussion whether the conclusions would hold for more specialized audio models

Minor comments:
- I think the figures can be made larger to be more readable using the white space surrounding the plots.
- typo in line 172

### Questions
Can you please address the weeknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce the Prune and Regrow method and tested on AudioMNIST and Speech Commands V2, showing that the proposed method is effective for item removal and class removal.

### Strengths
Overall, this is an important topic, especially as AI is trained on large datasets crawled from websites. There is an urgent need for machine unlearning in the audio domain.

### Weaknesses
Overall, I believe this paper has a large space for improvement:

1/ The method is described in too simple a way. The background and introduction are 3 pages, but the method is described in only 2/3 of a page and mostly in vague text descriptions. I am not an expert in machine unlearning, but I suspect such a general method (Prune and Regrow) is not being proposed for the first time. If I am wrong, please correct me (e.g., Prune and Regrow is the first time proposed in this area).

2/ The experiment is limited to 2 datasets, both not related to privacy directly. I understand that for some theoretical papers, such small datasets are needed for analysis purposes, but this is not a theoretical paper. The gap between a real-world model (let's say OpenAI's audio model Whisper vs. the model presented in this paper) can be huge, and thus the analysis in this paper may not transfer.

3/ The presentation is not clear. The core method is described in too brief a way. Figures are not easy to read (font too small, why a radar plot?). Figure 3 presents too many plots, and I don't easily understand the message the authors want to convey.

### Questions
See in the weakness.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses a gap in the unlearning literature by adapting and evaluating existing unlearning methods, previously applied in other domains, to audio data—specifically speech recognition datasets such as AudioMNIST and SpeechCommands V2—across various architectures. The authors find that while current unlearning techniques perform adequately for Class Removal, they fall short for Item Removal, an important task in data unlearning. To address this, they introduce a novel Prune and Regrow paradigm that applies dynamic sparsity unlearning. Additionally, their investigation into unlearning scaling shows that this method maintains superior performance even as Item Removal requests increase.

### Strengths
The paper’s strengths lie in its focus on adapting unlearning methods to audio data, filling a gap in existing literature, and addressing unique challenges in speech recognition. The introduction of the Prune and Regrow paradigm is particularly interesting, as it not only enhances unlearning effectiveness for Item Removal—an area where current unlearning methods struggle—but also proves scalable for increasing unlearning requirements.

### Weaknesses
1. The explanation of the Prune and Regrow paradigm lacks clarity. I recommend that the authors include a structured figure illustrating each step—such as the specific pruning methods within the paper. Additionally, the authors could create space by trimming subsections 2.2 and 2.3, as the details on unlearning methods and evaluation metrics are already available in the appendix.

2. While the authors claim that the Prune and Regrow paradigm outperforms prior unlearning methods for Item Removal, this appears to hold primarily when measured by Unlearning Accuracy (UA) (as shown in Table 2). I would be interested to know why the results do not generalize across other metrics. Specifically, the disparity in performance across metrics like Retention Accuracy (RA) and Task Accuracy (TA) raises concerns about the method's overall robustness and general applicability. The fact that UA is prioritized may mask underlying issues with the method's ability to maintain overall model integrity during unlearning.

3. I recommend that the authors add details to clearly distinguish between Item Removal and Class Removal unlearning methods. The current presentation does not sufficiently highlight the nuanced differences in how these two unlearning tasks are approached and evaluated, potentially leading to a misinterpretation of the results. It is crucial to clarify the specific challenges and requirements of each task to properly contextualize the performance of the proposed method.

4. The paper lacks comparisons on common speech recognition benchmarks. How well does this method generalize to widely used speech recognition datasets, such as Libri-Light and LibriSpeech?

### Questions
I have addressed all my questions in the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores machine unlearning for audio classification. Five existing methods are used, and the authors use these methods to demonstrate the extent to which existing machine unlearning methods can remove individual items from the training data of three model architectures on two small datasets. The authors then propose a modified pruning method for machine unlearning that iteratively sparsifies and fine-tunes the network.

### Strengths
Machine unlearning has been neglected within the audio domain, and this is a nice paper that demonstrates the efficacy of existing SOTA machine unlearning on some simple audio classification models. It is a good step towards performing unlearning on modern audio models and tasks (e.g., speaker verification systems).

The motivation and background are well-written, concise, and not overly complicated.

### Weaknesses
This paper lacks any demonstration of generality due to the selected datasets (SpeechCommands and AudioMNIST) being too small. I don't think that is a reason to reject the paper, as machine unlearning has thus far not been sufficiently studied on any audio dataset.

Tables 2 and 3 do not paint a clear picture of the proposed method significantly improving over previous methods on the selected metrics. And tables in Appendix C show the proposed method performing the worst of all methods in some conditions (e.g., Table 7, A DIST). So while this paper contains good analysis, the proposed novel method may be an incremental improvement.

Section 3 should be more precise regarding details of your method. Right now, it says "the Prune and Regrow paradigm... focuses on...", but the methods section should provide sufficient details for both implementation and distinction from prior methods, not just the focus.

Please fix capitalizations, consistent conference/journal naming, arXiv papers that have been accepted, and other formatting issues in the references section

Check bolded values in Tables 2 and 3; there are maximal/best values that are not bolded

"we argue that a one-size-fits-all sparsity unlearning cannot be optimal due to different learnt features across modalities" -> This is not a well-supported claim, as the proposed method is not tested on any modality other than audio.

### Questions
One would assume that video tasks would also benefit from better machine unlearning methods for audio given the shared temporal dimension. Do you believe your method is amenable to video tasks? As well, are there existing machine unlearning methods for video tasks that would be applicable to the audio tasks performed in this paper?

Industry machine learning models are typically periodically retrained to add more data and experiment with the training and model architecture. It seems far more straightforward to simply remove the D_{forget} set when retraining. Are there concrete, real-world cases where the model is not retrained and machine unlearning is needed?

### Soundness
3

### Presentation
3

### Contribution
3
