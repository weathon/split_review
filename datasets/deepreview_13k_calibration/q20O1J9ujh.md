# VideoGLUE: Video General Understanding Evaluation of Foundation Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
We evaluate the video understanding capabilities of existing foundation models (FMs) using a carefully designed experiment protocol consisting of three hallmark tasks (action recognition, temporal localization, and spatiotemporal localization), eight datasets well received by the  community, and four adaptation methods tailoring an FM for downstream tasks.
Furthermore, we jointly profile FMs'  efficacy and efficiency when adapting to general video understanding tasks using cost measurements during both training and inference.
Our main findings are as follows. 
First, task-specialized models significantly outperform the seven FMs studied in this work, in sharp contrast to what FMs have achieved in natural language and image understanding.  
Second, video-native FMs, whose pretraining data mainly contains the video modality, are generally better than image-native FMs in classifying motion-rich videos, localizing actions in time, and understanding a video of more than one action. 
Third, the video-native FMs can perform well on video tasks under light adaptations to downstream tasks (e.g., freezing the FM backbones), while image-native FMs win in full end-to-end finetuning.
The first two observations reveal the need and tremendous opportunities to conduct research on video-focused FMs, and the last confirms that both tasks and adaptation methods matter when it comes to the evaluation of FMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies video understanding capabilities of several existing foundation models. For this purpose, these models are evaluated on three primary video tasks: action recognition, temporal localization, and spatiotemporal localization. There are also three main findings from this study. First, task-specialized models still outperform foundation models; second, video-native foundation models are better than image-native models for complex and motion-rich videos; and third, light adaptations are enough for video-native models while full fine-tuning is better for image-native models. In addition, there is also an attempt to suggest one metric that resembles the strength of the foundation model.

### Strengths
1) The paper has an excellent presentation with clear discussion and motivation for the work done. The visualizations are very nice and they further facilitate the text of paper and experiments. 
2) Evaluating six foundation models on three main video tasks and eight datasets is a valuable contribution to the research community. It is even more valuable because different adaptions are also considered (fine-tuning, low-rank adapter, and others). Experiments are performed thoroughly with good analysis and discussion. The obtained conclusions can be important to the next iteration of the development of foundation models. 
3) The suggested VideoGLUE score can be an interesting initial way to start a comparison and discussion of the strength of foundation models. It seems that the scores for the studied models are quite close to each other and still far from the perfect one. So we can think that we are only starting scretching the cover of this area.

### Weaknesses
1) Despite the contribution of suggesting a VideoGLUE score, there are no novel models, modifications, or datasets presented in the paper. In my opinion, it would be very beneficial to develop at least one of them as an additional contribution to make the strongest possible paper. 
2) The list of studied foundation models is not as comprehensive as potentially can be. I understand, that not models are publicly available but it would be very interesting and important to make even stronger conclusions by including some of video-based models developed on top of CLIP paradigm. Some of the examples are: "VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding", Xu et al., EMNLP 2021; "Expanding Language-Image Pretrained Models for General Video Recognition", Bolin et al., ECCV 2022. 
3) Also, there is a rapid development of adaptation techniques that could be also very nice to be included in the analysis. Some of the recent examples are: "AIM: Adapting Image Models for Efficient Video Action Recognition", Yang et al., ICLR 2023; "Frozen CLIP Models are Efficient Video Learners", Lin et al., ECCV 2022; "ST-Adapter: Parameter-Efficient Image-to-Video Transfer Learning", Pan et al., NeurIPS 2022. The listed papers are mostly adapters from images to videos, but it would be still great to have them in the analysis for some of the applicable foundation models.

### Questions
No other questions except those listed in the "Weaknesses" section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to assess the video understanding capabilities of existing foundation models. The authors have employed a meticulous experimental protocol that encompasses three hallmark tasks: action recognition, temporal localization, and spatiotemporal localization. These tasks are evaluated across eight datasets that are well-regarded by the research community. The initial context suggests that the paper's focus is on the comprehensive evaluation of video understanding in foundational models using a variety of tasks and datasets.​

### Strengths
1. Evaluating Foundation Models (FMs): The paper emphasizes the complexity involved in evaluating FMs, particularly because they are designed as "generalists" that learn meta-knowledge across tasks. This highlights the need for a standardized evaluation procedure, which this paper aims to provide.

2. VideoGLUE Protocol: The proposed evaluation protocol provides a structured approach to evaluate FMs on video understanding, encompassing various tasks, datasets, and model adaptation methods. This could serve as a benchmark for future research.

### Weaknesses
1. Different datasets emphasize varied aspects in video tasks; for instance, SSV2 focuses on motion, while Kinetics is more context-centric. How does VideoGLUE address the differences among these diverse datasets?

2. While the study delves into transformer-based Foundation Models (FMs), is there any comprehensive analysis or comparison involving 3D-CNN or even 2D-CNN based FMs?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper assesses the video understanding capabilities of current foundation models using a novel experimental protocol that spans multiple tasks, datasets, and adaptation methods. Additionally, it introduces a scalar VideoGLUE score to gauge both the efficacy and efficiency of a foundation model. Drawing from the experimental outcomes, the paper unveils several interesting findings.

### Strengths
1.	The motivation is both clear and justified. There is a pressing need in the community to establish a benchmark for assessing the video understanding capabilities of foundation models.
2.	The introduced VideoGLUE benchmark evaluates foundation models across various dimensions such as tasks, datasets, and adaptation methods.
3.	This paper highlights three interesting findings into the video understanding capabilities of current foundation models.
4.	The paper is well written and easy to follow.

### Weaknesses
1.	This paper analyzes six foundational models, varying in size, pre-training data, and objectives. The diversity of these settings compromises the comparability of the experimental results, rendering the conclusions less reliable. Specifically, the lack of control over pre-training data and objectives introduces confounding variables, making it difficult to isolate the impact of model architecture or adaptation methods on performance. For instance, a model pre-trained on a massive dataset with diverse video content might exhibit superior performance simply due to its pre-training, rather than any inherent advantage in its architecture or adaptation strategy. This makes it challenging to draw meaningful conclusions about the relative strengths and weaknesses of different foundation models for video understanding.
2.	This paper introduces a scalar VideoGLUE score to assess FM's efficacy and efficiency by averaging performance scores across four adaptation methods. Yet, the rationale behind the metric's design appears arbitrary. It's unclear why this particular weighted score, derived from the specified datasets and adaptation methods, is indicative of FMs' video understanding capabilities. The equal weighting of different adaptation methods, despite their varying complexities and resource requirements, is a significant limitation. Furthermore, the score does not account for the variance in performance across different tasks or datasets, potentially masking significant differences in model capabilities.

### Questions
1.	In Table 3, the task-specialized model UniformerV2 registers a score of 42.7 on the MIT dataset, which trails the 43.6 scored by CoCa. This observation contradicts the assertion that "All six FMs underperform task-specialized models on video tasks."
2.	In Figure 3, CoCa achieves an average score of approximately 36 under the MLAP adaptation. However, Table 5 lists the average score for CoCa as 45.9. Why aren't they consistent?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces VideoGLUE, a comprehensive benchmark designed to evaluate video understanding capabilities of foundation models (FMs). VideoGLUE consists of three tasks (video classification, temporal localization, and spatio-temporal localization), eight datasets (K400, SSv2, D48, MiT, Charades, ANet, AVA, and AVA-K), and four adaptation methods (full finetuning, frozen backbone Eval., MLAP, and PETL w/ low-rank adapters). The authors also propose a scalar metric, VideoGLUE Score (VGS), that reflects the efficacy and efficiency of FMs. Comparative evaluations between image-native and video-native FMs on VideoGLUE reveal that 1) the existing FMs still lag behind task-specific models; 2) video-native FMs demonstrate superior temporal modeling capability than image-native counterparts; 3) video-native FMs outperform image-native FMs under light-weight adaptations, but not under full finetuning.

### Strengths
1.	The paper is well written and clearly motivated.
2.	The paper evaluates both image-native and video-native FMs on various video datasets and the unified evaluation protocols.
3.	The paper introduces various adaptation methods for both image and video FMs and the subsequent analysis underscores the critical role of adaptation in evaluation.

### Weaknesses
1.	VideoGLUE Score: (As the authors mentioned in Limitation Section) The proposed VideoGLUE score focuses solely on the computation-performance tradeoff, overlooking other valuable aspects, e.g., memory usage, model size, sample efficiency, model architecture difference. Given the significant influence of datasets and evaluation protocols on research directions, there is a concern that the current benchmark and scoring system might lead practitioners to overlook these crucial aspects of comprehensive video AI development.
2.	Selection of tasks: The benchmark is limted to three tasks, which may not fully capture the generalizability of FMs in video understanding. The inclusion of additional tasks, e.g., repetition counting, (long-term) action anticipation, human-object interaction, and so on,  could provide a more comprehensive evaluation.
3.	Selection of motion-focused benchmarks: Athough SSv2 is a widely acknowledged motion-focused dataset, existing literature [a, b] indicates that strong performance is achievable without motion modeling on SSv2 due to strong correlation between objects and action classes in SSv2. Utilizing Something-Else [a]as an alternative could offer a purer evaluation of motion modeling capability by breaking those spurious correlation. Furthermore, FineGym [c] provides hierarchical action labels allowing for a more granular assessment of a model modeling capability.

### Questions
1. Is there any reason why image-native FM CoCa outperforms other FMs on D48, which mitigates static contextual biases but focuses on motion?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
