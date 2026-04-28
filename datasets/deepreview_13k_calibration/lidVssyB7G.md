# Taming Data and Transformers for Audio Generation

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
\nnfootnote{Work partially done during an internship at Snap Inc.}
Generating ambient sounds is a challenging task due to data scarcity and often insufficient caption quality, making it difficult to employ large-scale generative models for the task. In this work, we tackle this problem by introducing two new models. First, we propose \audiocaptioner, a \emph{high-quality} and \emph{efficient} automatic audio captioning model. By using a compact audio representation and leveraging audio metadata, \audiocaptioner substantially enhances caption quality, reaching a CIDEr score of $83.2$, marking a $3.2\%$ improvement from the best available captioning model at \emph{four times} faster inference speed. Second, we propose \audiogenerator, a scalable transformer-based audio generation architecture that we scale up to 1.25B parameters. Using \audiocaptioner to generate caption clips from existing audio datasets, we demonstrate the benefits of data scaling with synthetic captions as well as model size scaling. When compared to state-of-the-art audio generators trained at similar size and data scale, \audiogenerator obtains significant improvements of $4.7\%$ in FAD score, $22.7\%$ in IS, and $13.5\%$ in CLAP score, indicating significantly improved quality of generated audio compared to previous works. Moreover, we propose an efficient and scalable pipeline for collecting audio datasets, enabling us to compile 57M ambient audio clips, forming \audiodataset-XL, the \emph{largest} available audio-text dataset, at 90 times the scale of existing ones. Our code, model checkpoints, and dataset are publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes an audio captioning method called AutoCap, an audio generation model called GenAu and an audio dataset called AutoReCap-XL.

### Strengths
- The illustrations in the paper are clear and it is well written.
- No evident flaws.
- AutoReCap-XL will be great asset for the audio research community if open-sourced.

### Weaknesses
 - The illustrations in the paper are clear and it is well written.
- No evident flaws.
- AutoReCap-XL will be great asset for the audio research community if open-sourced.

### weaknesses:
 - The authors shared the audio samples from Stable-Audio 1.0[7] but the comparison is missing in results table.
- Typo in table 5, last row "Quality" column: "-".
- The performance improvement when compared to increase in number of parameters in GenAu is marginal.
- Recently, Large Audio Language models [1,2,3,4] are being employed for audio captioning task, but the authors don't compare AutoCap to these baselines which in my opinion should be an important comparison.
- Inconsistent use of word "Q-Former" and "Qformer".
- Why do authors not show generation results of GenAu without Recap dataset or baseline + Recap in normal settings? It should be an important ablation to show where the performance gain is coming from.
- The CLAP text conditioner is confusing, the text encoder employed by CLAP [5,6] is BERT. What do authors mean when they say that they have used CLAP text encoder, do they use the text encoder weights from CLAP's checkpoint?
- There should be clear distinction between CLAP and EnCLAP. Authors mention CLAP but cite EnCLAP.
- The authors propose to use video caption and title as metadata, how sensitive is the output to the accuracy and relevance of metadata? Have the authors performed any ablation to show the robustness of this method?
- It would be interesting to analyse the distribution of sounds across various classes of non-ambient sounds in AutoReCap-XL. Have the authors explored any distribution patterns, and is there a noticeable bias toward any particular class as there is a lot of filtering while preparing the dataset?
- In section A.2 authors mention "Given that AutoReCap was trained for 10-second audio", I think there is a typo and it should be "AutoCap" instead of "AutoReCap" as the later one is the dataset.
- I want to understand what is the novelty of GenAu when compared to other models? In my opinion all other baselines and other audio generative models are **almost** capable of generating more or less similar audios with lesser parameters.

### Questions
Please see weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Introduce two new models. First, we propose AutoCap, a high-quality and efficient automatic audio captioning model. By using a compact audio representation and leveraging audio metadata, AutoCap substantially enhances caption quality Second, the work proposes GenAu, a scalable transformer-based audio generation architecture that is scaled up to 1.25B parameters. Using AutoCap to generate caption clips from existing audio datasets.

### Strengths
* The paper presents a simple pipeline to label audio data in order to generate larger data than ever before.
* The paper shows the new dataset improves the quality of trained models.
* Train a SOTA model using the new dataset.
* The authors say they will release the dataset which could be a good contribution to the community.

### Weaknesses
 * In scenarios where metadata lacks detail, audio captioning may struggle to disambiguate sounds accurately. The model also tends to falter in
capturing the temporal relationships between sounds and differentiating foreground from background
noises. 
* Fine-tuned on AudioCaps, which contains a limited vocabulary of 4,892 unique words. The limited vocabulary of the paired texts, even though extensive, hampers the model’s ability to accurately generate audio for long and detailed prompts.

* The proposed dataset, AutoReCap-XL, is substantial in size but features a constrained vocabulary of
only 4,461 unique words. Furthermore, despite its potential as a significant contribution, this dataset has not
yet been extensively analyzed for caption accuracy or performance in downstream tasks.

### Questions
* Didn't train baselines on the new dataset to show the proposed architecture is actually superior. I would have liked to see the baselines trained on the 57M example dataset. This would clearly show if the better performance of the proposed method is due to architecture or just the scaling of the dataset.
* Is there a way to verify the quality of the dataset in terms of captioning? assuming the community adopts the use of this new data how are you to ensure the data is of high quality? maybe some human evaluation would be in place.
* Please move the limitations section into the main body of the paper.

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
5

### Summary
The paper proposes a new method to improve audio (sound) generation. The authors first propose AutoCap, a novel method to generate audio captions using auto-regressive models. Next, the authors propose a novel audio generation model which is trained on their generated dataset. The proposed method shows improvement on benchmark datasets.

### Strengths
- The paper is well written and well presented. The figures are good and the writing and everything is crisp. It is a nice to read paper.
- The method shows good improvements. Open-sourcing the artifacts in future would help the audio community.
- Th intuitions are good. The fact that good captions can improve audio generation is a good finding and well conveyed. Although I feel some parts are over-claimed which I mention next.
- I don't see many technical flaws with the paper.

### Weaknesses
I have several issues with the paper. I will first point out the technical weaknesses:
- Fig. 1 says CLAP Encoder has one token. CLAP uses HTSAT as the audio encoder  which also has intermediate representations. This only means that the authors used the CLS token (or some pooled representations) which is not specified. The authors should also clearly mention "CLAP audio encoder". 
- The caption says "We then compact this representation into 4x fewer tokens using a Q-Former (Li et al., 2023a) module.". The figure shows only HTSAT encoder representation is passed to QFormer. The authors should rewrite the caption.
- The claim "4x fewer tokens" just because QFormer was employed in one part is not justified. The authors are also using BART embeddings, etc. Do you mean "4x fewer tokens" compared to your own baseline which does not use a QFormer?
- QFormer has been used for audio earlier [3]. Additionally, it does not seem like you are pre-training the QFormer? Does this mean you are training it E2E? An E2E model as big as QFormer trained on such small datasets is not very sound.
- The authors say fewer tokens but do not talk about the increase in parameter count. I would like to see ore discussion on this please.
- Some audio captioning prior art missing from comparison [1,2].
- I am concerned why only audio clips with "No subtitles" were uses. Is the synchronization of time and subtitle correct? Also, human speech is an important sound and heavily present in audiocaps. If the authors believe not, then I think the paper should refocus on "environmental sounds" and not "audio".
- (Not a big weakness) I feel its important that synthetic data generation pipelines have some verification strategy (human or automatic).
- The freezing and unfreezing paradigm has been heavily employed in prior art in the DCASE challenge. The paper misses some citations. Please see DCASE captioning challenges that use BART like architectures.
- The fact that visual modality helps in audio captioning is not new and has been explored. Comparison or discussion with papers like SOUND-VECAPS [4] or [5] is missing.
- For GenAu, a discussion with Stable Audio is missing. I understand where at some places the authors mention DiT and how GenAu mitigates some limitations of DiT based architectures, but the introduction of time embeddings and the use of attention modules makes it very similar to StableAudio overall. A discussion would do justice.
- Table 4 does not compare with Stable Audio. Same training data + Stable Audio comparison is a must for a fair comparison.
- The table has missing comparison of baselines + their re-captioned data. I struggle to understand where the gains are coming from. The only ablation of GenAU w. U-Net is not sufficient. I also understand computational constraints but a couple of baselines with the data would do more justice to the results.

### Questions
My questions are broadly mentioned in the Weaknesses section. I am mostly looking for the "Why?" answers to the choices made that are related to my listed Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a high-quality and efficient audio captioning model, named AutoCap, which demonstrates improvements in generation quality while being four times faster than current state-of-the-art (SoTA) models. The authors further present AutoReCap-XL, a large-scale audio-language dataset comprising 57 million ambient clips paired with automatically generated captions. Additionally, the paper proposes an audio generation model named GenAu, which also achieves SoTA performance.

### Strengths
1. The authors employ a Q-Former structure to compress audio representations from the pretrained HTSAT model, which significantly reduces system inference time. Additionally, to develop a more stable system, the paper adopts a two-stage training strategy: in stage one, only the Q-Former and CLAP-projector are trained on weakly labeled samples, while in stage two, the system is fully fine-tuned on the AudioCaps dataset.
2. The paper collects the majority of its data from videos, filtering out ambient clips that lack automatic transcripts. This is a straightforward yet interesting method to exclude speech and music content.
3. According to experimental results, both the captioning and generation systems achieve state-of-the-art (SoTA) performance.

Overall, this paper proposes an interesting approach by leveraging external metadata (e.g., captions or titles from visual information) to enhance audio captioning performance. Moreover, the introduction of the Q-Former module effectively reduces complexity and inference time. Finally, the authors present AutoReCap-XL, a dataset significantly larger than any existing audio-language datasets.

### Weaknesses
1. The paper lacks a detailed pipeline explaining how captions are analyzed and how speech or music-related content is filtered out. The authors should provide more clarification on this method. Specifically, the paper should detail the exact steps involved in analyzing the captions generated from the video-captioning model, including the specific natural language processing techniques used to identify and filter out speech and music-related keywords or phrases. For example, what specific lexicon or set of rules is used to determine if a caption contains speech or music content? Are there any thresholds or confidence scores used to make these decisions? The paper should also discuss how these methods handle ambiguous or nuanced language, and what the potential limitations of this approach are.
2. The proposed audio captioning system appears to require external "metadata" to generate captions. However, the definition of this "metadata" is ambiguous throughout the paper. The authors should offer more details on what this metadata consists of and how it is used. If this metadata is not readily accessible from raw audio, it limits the applicability of the system to real-world scenarios. The paper needs to clarify whether this metadata is derived from the video modality, and if so, how the system handles cases where such metadata is unavailable or unreliable. Furthermore, the paper should discuss the impact of the quality of the metadata on the performance of the captioning system. For instance, how does the system perform with noisy or inaccurate metadata?
3. According to Table 1, the comparison indicates that the proposed AutoCap does not achieve the best performance on several metrics, especially when only audio is used as input data. The paper should provide a more in-depth analysis of why AutoCap underperforms in these specific metrics when compared to other models using only audio input. It should also discuss the trade-offs between using external metadata and relying solely on audio input, and under what conditions each approach is more suitable.
4. For the audio generation system, the proposed model largely follows the architecture from Huang et al. (2023), incorporating the 1D-VAE and LDM modules. This feels more like an engineering effort, where the existing system is applied and scaled to larger datasets. Moreover, the model uses both FLAN-T5 and CLAP for conditional input, whereas previous models generally employ only one text encoder to achieve satisfactory results. The authors should explain why both encoders are necessary, along with experimental comparisons showing if using only one encoder leads to a drop in performance. The paper should also clarify if the FiT architecture is used in its original form or if any modifications were made for the audio generation task. If modifications were made, the paper should detail these changes and provide a rationale for them. Additionally, the paper should discuss the computational cost and efficiency of using dual text encoders compared to single text encoders.
5. The paper lacks an evaluation of the effectiveness of the proposed AutoReCap-XL dataset. While the authors mention the dataset's large scale, there is no experimental validation to demonstrate its quality or utility for audio-language tasks. The paper should include experiments that evaluate the performance of models trained on AutoReCap-XL compared to models trained on existing datasets. This evaluation should include a variety of audio-language tasks, such as audio captioning and generation, to assess the dataset's general applicability. Without such an evaluation, it is difficult to assess the value of the dataset as a contribution.

### Questions
1. What does the rejection rate in line 282 refer to? Is the rejection related to downloads?

2. In Section 3.2, the authors mention that they use the captions of each video from the video-captioning model in Panda-70M. Does this imply that the "metadata" is essentially raw captions generated by another captioning system?

3. Can the authors provide more details about the collected video datasets? Specifically, what is the average length of each video sample?

4. How does GenAu perform if only one text encoder (either FLAN-T5 or CLAP) is used?

5. What is the performance of GenAu when trained on the proposed AudioReCap-XL dataset?

6. Could the authors provide some demo examples of GenAu?

### Soundness
4

### Presentation
3

### Contribution
3
