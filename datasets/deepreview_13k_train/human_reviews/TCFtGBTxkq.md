# Efficient Audiovisual Speech Processing via MUTUD: Multimodal Training and Unimodal Deployment

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Building reliable speech systems often requires combining multiple modalities, like audio and visual cues. While such multimodal solutions frequently lead to improvements in performance and may even be critical in certain cases, they come with several constraints such as increased sensory requirements, computational cost, and modality synchronization, to mention a few. These challenges constrain the direct uses of these multimodal solutions in real-world applications. In this work, we develop approaches where the learning happens with all available modalities but the deployment or inference is done with just one or reduced modalities. To do so, we propose a Multimodal Training and Unimodal Deployment (MUTUD) framework which includes a Temporally Aligned Modality feature Estimation (TAME) module that can estimate information from missing modality using modalities present during inference. This innovative approach facilitates the integration of information across different modalities, enhancing the overall inference process by leveraging the strengths of each modality to compensate for the absence of certain modalities during inference. We apply MUTUD to various audiovisual speech tasks and show that it can reduce the performance gap between the multimodal and corresponding unimodal models to a considerable extent. MUTUD achieves this while reducing the model size and computing compared to multimodal models by almost 80%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes MUTUD, which enables unimodal inference (deployment) by leveraging multi-modal training (specifically audio-visual training in this work). The TAME module is proposed to enable cross-modal transfer and is proven to be effective. It achieves better results than single-model training while using fewer parameters than multimodal training across three speech tasks: speech recognition, active speaker detection, and speech enhancement.

### Strengths
1. The presentation is quite clear, and the design of TAMU is simple and easy to understand.
2. While there are few works focused on efficient unimodal deployment, this appears to be the first adaptation in audio-visual speech tasks. The motivation is therefore innovative.
3. The experiments are sufficiently extensive.

### Weaknesses
Major Concerns:
While I understand that multi-modal approaches can improve performance, they also increase costs, which motivated MUTUD's development. I am curious about practical utility in industry applications - would we really use audio-visual data for performance boosting? I would love to see actual industry statistics. Though the motivation is quite clear, I would appreciate seeing the "motivation behind the motivation." Specifically, what are the concrete scenarios where the added complexity of visual data acquisition and processing is justified by a significant enough performance gain in real-world applications? The paper needs to provide a more detailed analysis of the trade-offs between performance gains and the practical costs of deploying audio-visual systems.
Audio and video data, though time-synchronized, aren't always perfectly aligned per frame. I'm not sure if you have any insights to handle this. Would time-accurate alignment in TAME lead to error accumulation? The paper does not discuss the potential impact of temporal misalignment between audio and video streams on the performance of the TAME module. It's unclear how the model handles situations where audio and visual cues are not perfectly synchronized, which is common in real-world scenarios. The lack of discussion on this issue raises concerns about the robustness of the proposed method.
Additionally, I'm uncertain about how general TAME is. What if we have different video modalities like face or lip? The paper should explore the adaptability of TAME to different visual modalities. The current experiments focus on a specific type of visual input, and it's unclear whether the same approach would be effective with other visual modalities, such as lip movements or facial expressions. The paper needs to provide a more comprehensive analysis of the limitations of TAME and its potential for generalization across different types of visual data.

Minor Concerns:
On line 36, the claim that "visual modality is the most widely used in these speech tasks" needs evidence. From my perspective, text appears to be more prevalent. The paper should provide empirical evidence to support the claim that visual modality is the most widely used in speech tasks, as this seems counterintuitive given the prevalence of text-based approaches. 
Regarding lines 45, 49, and 54, the three bullet points seem to apply specifically to audio-visual multi-modal scenarios, while speech-text multimodal situations might be different. One important missing challenge is that multimodal input doesn't always bring improvement - it can be noisy and confusing. For example, face and speech are not "perfectly" matching. The paper should acknowledge that multimodal input can sometimes be detrimental, especially when the modalities are not perfectly aligned or when one modality is noisy or unreliable. This is a critical issue that needs to be addressed in the discussion of the challenges of multimodal learning.
On line 137, the related work section should consider "ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Enhancement." The literature review needs to be more comprehensive.

### Questions
See Weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an approach to leverage multiple modalities in model training to improve performance when only a single or a subset of modalities are present at test time.  This is achieved by estimating the missing modalities based on their correlation with the known modalities and using those estimates in the inference process.  A codebook based approach to model the modality correlation is presented.  Results of three audio-visual tasks — speech enhancement, speech recognition, and active speaker detection — demonstrate that by using both modalities at training time while only one at test time results in a significant gains over baseline single modality performance on each of the three tasks.

### Strengths
* A novel approach to utilize information from two or more modalities at model training time to improve run-time performance when only a single or a subset of modalities are present.  Proposed approach relies on estimating, in a time aligned manner, modality features that are not present at run-time.
* Proposed model is parameter and compute efficient
* Results in a significant accuracy gains without adding too many parameters over the baseline unimodal model.

### Weaknesses
 * Missing baselines: Using multiple modalities at training time only to improve performance under a single or a subset of modalities has been studied before.  E.g. [1].  References & comparison with those methods needs to be carried out to fully assess the merits of the proposed model.

[1] Abavisani et al., “Improving the Performance of Unimodal Dynamic Hand-Gesture Recognition with Multimodal Training”

* Only the case of audio-visual ASR / Speech enhancement / Active speaker selection is studied.  This provides a limited, bi-modal view of general multimodal tasks.  A more general multi-modal setting will make this work much more attractive.



### Questions
* Typo on Line 058: defnitely
* Lines 195-196: define ‘D’

### Soundness
2

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
The authors proposed a Multimodal Training and Unimodal Deployment (MUTUD) framework to train the model on audio and visual modalities, but only use audio modality for inferecnce. The authors expected the model to imagine visual information from extracted audio features to help downstream audio tasks, with a Temporally Aligned Modality feature Estimation (TAME) module. TAME comprises individual codebooks for audio and video, and is trained using reconstruction loss and KL divergence loss to associate the different modalities. During inference, the audio features are used to retrieve the corresponding video features through the codebooks. Other training objectives are used for specific downstream tasks.

### Strengths
The authors present a potential method to guide the projection from audio to visual representation when visual input is absent. However, the experiments are insufficient and lack persuasiveness.  The writing is clear and well-structured.

### Weaknesses
1. The author conducted experiments solely on the audio-visual dataset, comparing the performance of the multi-modal, audio-only, and MUTUD frameworks. However, no independent validation and comparison with other models were carried out on out-of-domain audio-only datasets. Such validation is crucial to checkout whether the model merely overfits to specific biases within the audio-visual dataset, or genuinely learns the projection from audio features to video features, thereby enhancing uni-modal tasks. Specifically, the absence of evaluations on standard audio-only tasks like speech enhancement, automatic speech recognition (ASR), and speaker detection, using established datasets, makes it difficult to assess the generalizability of the proposed approach.

2. Lack of novelty. Similar methods have already been explored, such as "Multi-modality Associative Bridging through Memory: Speech Sound Recollected from Face Video," which predicts audio features from visual features. The core idea of using one modality to inform the other through a learned association is not entirely new, and the paper does not sufficiently highlight the unique aspects of the proposed TAME module compared to existing methods. The paper needs to clearly articulate what specific innovations TAME brings to the field beyond existing modality bridging techniques.

3. The performance gain is quite limited compared to the audio-only model. The reported improvements in performance metrics, while present, are not substantial enough to convincingly demonstrate the practical utility of the MUTUD framework. The marginal gains raise questions about the added complexity of the proposed method, especially when compared to simpler audio-only models. A more thorough analysis of the trade-offs between performance gains and computational overhead is needed.

4. The experiment is not sufficient. Lack of comparison with some recent models on the three tasks. The experimental evaluation lacks a comprehensive comparison with state-of-the-art models across the three tasks considered (AV speech enhancement, AV active speaker detection, and AV speech recognition). The absence of such comparisons makes it difficult to gauge the relative performance of the proposed method and its potential to advance the state-of-the-art in these areas.

5. Lack of validation for the effectiveness of the proposed TAME method on more advanced backbone. The evaluation of the TAME module is limited to relatively older backbone models. It is unclear how TAME would perform when integrated with more recent and advanced backbone architectures. This limits the applicability and potential impact of the proposed method, as it is not demonstrated to be compatible with current state-of-the-art models.

### Questions
1. Could you provide the no independent validation and comparison with other uni-modal models on audio-only tasks? Such as speech enhancement, ASR, speaker detection.

2. The authors have built the models and baselines using relatively older models (e.g., GCRN, 2019). How does TAME perform when integrated with the latest backbone models?

3. What are the performance outcomes and discussions in comparison with the latest state-of-the-art works across the three tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles the interesting task of training on multimodal data and then evaluating using only one modality. This is achieved by predicting the other modality. Their method focuses on the use of code books to quantize audio and visual inputs, and they apply various loss functions in order to align the quantized modalities of the code books. They also align the dimensions of the audio and video via their interleaving method. They beat their benchmarks in several tasks while maintaining a small model footprint - measured by parameters and MACs.

### Strengths
The paper presents a useful approach to multimodal-to-unimodal distillation through its use of codebooks for modality alignment. The technical work includes benchmarking across different datasets and tasks, with testing under various noise conditions and SNR levels. The authors provide ablation studies on codebook sizes and architectural choices, and show how their method works with different baseline architectures. The experimental results are well-documented, and the paper's structure makes it easy to follow their methodology and findings. 

From a practical standpoint, the work offers a solution for running multimodal systems with single modality inputs during deployment. Their implementation reduces model size by 80% and requires less computation compared to full multimodal systems. The authors' method for aligning audio and visual dimensions works effectively, and they demonstrate good performance across benchmarks while keeping the model compact in terms of parameters and MACs. The results suggest their approach could be useful for applications where resource efficiency matters.

### Weaknesses
There are several weaknesses to this paper. To summarise briefly: (1) the paper lacks significant contribution(s), (2) experiments do not support the authors’ claims. However, there are additional issues that I will discuss below. Firstly, point (1):

- A main motivation of this paper (motivation 2) is rather weak. A video camera available in even the cheapest smartphone is not “complex sensory devices working together seamlessly”. Other modalities, like text (unexplored in this paper) can be acquired via free open-source transcription models. There are many instances where multi-modal data is expensive and/or hard to obtain, but they do not tackle such use cases. I feel it would be better to focus the narrative on resource constraints in deployment settings (such as handling sensor failures).
They propose a framework that ideally maps from m training modalities to n inferences modalities, where n<m, but they focus on audio-visual training with only audio during inference time. It is unclear how MUTUD could generalise to other settings, when they do not even consider the reverse (only video at inference time). This is particularly true given their extensive usage of loss functions, which seem very task specific.
- The methods section is extremely short, and the majority of the work in this section is not the authors’ work. The largest section, about the codebooks, is simply defining what a codebook is. There is no additional contribution, and they do not cite the original work, -- it is unclear what the contribution of this section is. Similarly, the loss functions are not their work but are uncited. I believe the overall technique is unique, but a simple, direct application of others work is not a significant enough contribution to meet the requirements of ICLR.

Point (2):

- They compare to two methods: one adapted audio method from 2019, and one adapted audio-visual method from 2023. Experiments and resulting claims should be backed up by extensive experimentation that compares to many baselines. A 5 year old model that has been adapted is not sufficient to meet the requirements of ICLR.
- There is no empirical justification as to why estimating visual features from audio features is better than simply using only the audio features. In order to support this claim, their codebook methodology should be used in the audio only setting, the audio-visual setting, and the audio-visual setting with only audio at inference time. Comparing to other models means it's impossible to tell if the improvements are due to the audio-visual training, or simply because codebooks solve the task better.
- They only compare to adapted baselines. The tasks, such as AVSR and AVSE, are very common and well explored in the literature. They should compare to a list of contemporary methods, at least 6 contemporary audio-visual/audio only methods in total (i.e. 3 audio only, 3 audio visual).
- The number of parameters and MACs are interesting metrics, but have very little influence on inference speed. A large part of the paper’s narrative is discussing efficiency, yet none of the tables contain inference times. In modern deep learning, the biggest challenges are inference times and memory, reducing arbitrary values has little real-world utility.
- They do not break down specifically how the parameters and MACs are allocated, for example, how many MACs/Params for the audio code book, the video codebook, training size, evaluation size (on 1 modality).
- The tables are not well labelled, it is often unclear (without digging through paragraphs of experimental detail) what the evaluation task is for each table, on which dataset.

### Questions
You have audio to video but no video to audio, is this not included in the model? 
From my understanding, codebooks are slow unless a transformer or similar architecture is applied in order to efficiently assign indexes in the codebook (i.e. https://arxiv.org/abs/2210.13438). Can you provide inference times in your tables?

Please additionally address the comments in the weaknesses section

### Soundness
1

### Presentation
3

### Contribution
1
