# Dense Video Object Captioning from Disjoint Supervision

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
We propose a new task and model for \emph{dense video object captioning} -- detecting, tracking and captioning trajectories of objects in a video.
This task unifies spatial and temporal localization in video, whilst also requiring fine-grained visual understanding that is best described by natural language.
We propose a unified model, and demonstrate how our end-to-end approach is more accurate and temporally coherent than a multi-stage pipeline combining state-of-the-art detection, tracking, and captioning models.
Moreover, we propose a training strategy based on a mixture of disjoint tasks, which allows us to leverage diverse, large-scale datasets which supervise different parts of our model.
Although each pretraining task only provides weak supervision, they are complementary and, when combined, result in noteworthy zero-shot ability and serve as strong initialization for additional finetuning to further improve accuracy.
We carefully design new metrics capturing all components of our task, and show how we can repurpose existing video grounding datasets (\eg VidSTG and VLN) for our new task.
We show that our model improves upon a number of strong baselines for this new task.
Furthermore, we can apply our model to the task of spatial grounding, outperforming prior state-of-the-art on VidSTG and VLN, without explicitly training for it.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel task towards the field of video understanding—dense video object captioning—with the aim of advancing the comprehension of temporal and spatial information within videos. In the absence of training data for this task, the authors innovatively proposes an end-to-end approach that integrates various datasets to train different modules. The superiority of the proposed methodology is demonstrated through extensive zero-shot and full fine-tune experiments.

### Strengths
1. **Clear and Precise Definition of a New Benchmark**: The paper introduces a novel task aimed at achieving more comprehensive video understanding, thereby setting higher standards for a single model's capability to interpret videos. It also establishes well-defined evaluation metrics that are appropriate for this new benchmark.

2. **Design of a Concise and Effective Training Framework**: In response to the proposed task, the paper presents a streamlined, end-to-end trainable framework that effectively integrates multiple tasks such as detection, tracking, and description generation. The authors ensure seamless end-to-end training by efficiently constructing ground truth for the tracking task.

3. **Innovative Data Organization Method**: To Address the lack of a dedicated dataset for the proposed task, the authors decompose the task and combine or generate data from various sources to train different modules effectively.

4.  **Comprehensive Experimental Evaluation**: The authors conducted extensive experiments, demonstrating the advantages of their approach over simply concatenating state-of-the-art solutions for individual tasks. They highlight the effectiveness of combining multiple datasets, the superior generalization ability of the trained model, and its outstanding performance on relevant datasets. The open source of the code further strengthens the credibility of these findings.

### Weaknesses
1. **Clarification of Task Significance**: Although the task imposes higher demands on deep models for video understanding, the paper does not clearly articulate the associated benefits. It would be advantageous to illustrate the task's relevance in more challenging or representative application scenarios, such as sports commentary or intelligent animal monitoring. This would better underscore its significance and research value.

2. **Examination of Method Generalizability**: The authors successfully modularize the training process by breaking down the overall task into distinct sub-tasks and aligning them with suitable training datasets, as demonstrated by the experimental results. However, a more in-depth discussion on the domain differences between datasets and the rationale for task decomposition could provide a stronger basis for the broader applicability of this approach. Such an analysis would significantly enhance the paper's contribution to the research community.

3. **Correction of Typos and Formatting Inconsistencies**: The paper contains several typos and formatting inconsistencies that require attention. For example, in Section 3.5, the symbols in Equation (1) do not correspond with the preceding descriptive content. Additionally, there are inconsistencies in citation formats in the paper, for example, the format of citations in Table 2.

### Questions
Beyond the questions in the weaknesses, I have an additional curiosity regarding the approach. In the Spoken Moments in Time (SMiT) dataset, captions are provided at the video level. The approach of using entire frames as detection proposal and generating captions contrasts significantly with the method of using detectors on the Visual Genome dataset to identify objects and then generating captions, resulting in a noticeable domain discrepancy. I am uncertain whether this discrepancy should be addressed, as the examples provided suggest that the generated results for single targets also include interaction information with other objects, such as "A brown dog chasing an adult on the grass." Given that the input to the text decoder is supposed to be a single-track feature and the model does not explicitly model interactions between targets, could this intriguing phenomenon be attributed to the way the SMiT dataset is utilized in training?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a new task and model for dense video object captioning that unifies spatial and temporal localization by detecting, tracking, and captioning object trajectories in videos. The proposed end-to-end model combines visual understanding and language generation, outperforming multi-stage pipelines in accuracy and temporal coherence. Leveraging a novel training strategy that uses disjoint, large-scale datasets for pretraining, the model achieves impressive zero-shot capability and serves as a robust base for fine-tuning. Additionally, new metrics for task assessment and successful adaptation of video grounding datasets further demonstrate the model's effectiveness in video spatial grounding tasks.

### Strengths
This paper introduces a novel task—dense video object captioning with unified spatial and temporal localization—bridging video understanding and natural language description in a unique way.

The end-to-end model presented is robust, outperforming multi-stage pipelines by integrating detection, tracking, and captioning into a cohesive approach that achieves notable zero-shot capabilities.

The authors clearly outline the model architecture, training strategy, and metrics, making complex components understandable and well-motivated.

By developing metrics and reusing datasets for this new task, the work contributes valuable tools and benchmarks to the video understanding community, advancing video spatial grounding tasks and surpassing previous state-of-the-art results.

### Weaknesses
The paper primarily focuses on a few datasets, which may not fully represent the diversity of real-world scenarios. Expanding evaluations across a broader range of benchmarks could strengthen the validity of the results.

While quantitative metrics are important, including qualitative evaluations—such as human assessments of captioning quality—could enrich the understanding of model performance and highlight potential areas for improvement.

The paper does not provide an in-depth analysis of failure cases, which limits understanding of specific scenarios where the model struggles, such as occlusions, fast motion, or complex interactions between objects.

### Questions
Can you provide a detailed breakdown of common failure cases observed during the evaluation? Understanding these could clarify the model's limitations and areas for improvement.

How does your model perform with unseen objects? Providing results or insights on this aspect could strengthen the claims of generalizability.

Could you elaborate on the rationale behind the chosen evaluation metrics? A more comprehensive justification would help clarify their relevance and effectiveness in measuring performance.

### Soundness
4

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
4

### Summary
This paper proposes the new task of detecting, tracking and captioning objects in a video. The authors propose evaluation metrics for this task, a baseline method and a training strategy involving disjoint supervision.

### Strengths
This work tackles an important problem that was missing from the literature. The paper is well-written and easy to follow. Extensive experiments have been performed.

### Weaknesses
My only concern is that the end-to-end tracking algorithm (listed as a contribution) seems to be naive and not novel enough. There are other methods that perform identity association within the model (like MinVIS[1], CAROQ [2], trackformer [3]). The authors have explored some other ways of integrating temporal information/tracking in Table 2, but how about different ways of association within the model (e.g., query vector propagation in trackformer [3])? The method's tracking component appears to rely on a relatively simple association strategy, potentially limiting its ability to handle complex scenarios with occlusions or rapid object movements. Specifically, the paper lacks a detailed analysis of how the proposed tracking method performs under challenging conditions, such as frequent object interactions or significant changes in appearance. Furthermore, the method's reliance on frame-by-frame association might not be as robust as methods that explicitly model temporal dependencies across longer time spans.

### Questions
Please see Weaknesses.

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
The paper proposes a new task called Dense Video Object Captioning (Dense VOC), which involves detecting, tracking, and generating captions for objects in a video. The model aims to unify spatial and temporal localization while providing a natural language description of object trajectories. The approach combines detection, tracking, and captioning into a single end-to-end model, which is shown to be more accurate and temporally consistent compared to traditional multi-stage pipelines. The authors also propose a novel training strategy using disjoint supervision from different datasets, enabling zero-shot generalization and strong performance after fine-tuning. New metrics are introduced to evaluate the combined tasks, and the model achieves state-of-the-art results on tasks like video grounding without explicit training for those tasks.

### Strengths
1. The proposed approach integrates detection, tracking, and captioning, which ensures more temporally consistent results and holistic video understanding compared to multi-stage pipelines.
2. The use of disjoint tasks for training allows the model to generalize well even without specific full annotations for the task, showcasing impressive zero-shot capabilities.
3. The model outperforms strong baselines and even specialized models on tasks like video grounding and multi-object tracking, demonstrating its effectiveness across various video-related tasks.
4. The introduction of new evaluation metrics (e.g., CHOTA) tailored for Dense VOC ensures a more comprehensive assessment of model performance, capturing detection, tracking, and captioning jointly.
5. The model is successfully applied to related tasks such as video grounding and person tracking, proving its versatility.

### Weaknesses
1.	The framework demands significant computational resources, requiring more than 32 GPUs, and the specific GPU model was not provided. While separate training offers the potential for lightweight product applications, the experiments lack consideration of this aspect.
2.	The experimental section lacks an analysis and comparison of inference efficiency across different stages of the model as well as with existing backbones. Specifically, the runtime contribution of each stage (detection, tracking, captioning) is not clearly delineated, making it difficult to pinpoint bottlenecks and areas for optimization. Furthermore, a comparison of the model's inference speed with other state-of-the-art models, especially those using different backbone architectures, is missing.
3.	The model heavily relies on datasets that do not fully cover Dense VOC, which could limit the effectiveness of pre-training. Although the authors address this by using multiple disjoint tasks, the absence of specialized, annotated data for Dense VOC remains a challenge. The reliance on datasets with different annotation styles and focuses might introduce biases or limit the model's ability to generalize to the specific nuances of the Dense VOC task.
4.	The term “Dense” is somewhat confusing and seems ambiguous in the context of the task, which unifies spatial and temporal localization in video with fine-grained visual understanding through natural language. Perhaps a more precise term could better capture the essence of this process. The term 'dense' might imply a high density of objects or captions, which is not necessarily the core focus of the task, which is more about the unified processing and understanding of video content.
5.	The caption tracking process is event-oriented. Is there an analysis of different event types in this task? Specifically, how does the model perform across different types of events (e.g., actions, interactions, state changes), and are there any specific event types where the model struggles or excels?

### Questions
1. The use of disjoint datasets and diverse forms of supervision makes the training process complex and resource-intensive, posing challenges for reproduction and practical deployment. Is it possible to unify this process within a robust code infrastructure to facilitate easier incremental implementation and application?

### Soundness
4

### Presentation
3

### Contribution
4
