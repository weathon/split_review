# TAU-106K: A New Dataset for Comprehensive Understanding of Traffic Accident

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have demonstrated impressive performance in general visual understanding tasks. However, their potential for high-level and fine-grained comprehension, such as humor or anomaly understanding, remains unexplored. Targeting traffic accidents, a critical and practical scenario within anomaly understanding, we explore the advanced capabilities of MLLMs and introduce TABot, a multimodal MLLM tailored for accident-related tasks. To facilitate this, we first develop TAU-106K, a large-scale multimodal dataset comprising 106K traffic accident-related videos and images, sourced from academic benchmarks and public platforms. The dataset is meticulously annotated through a video-to-image annotation pipeline, ensuring comprehensive and high-quality labels. Upon TAU-106K, our accident-oriented MLLM TABot is trained in a two-step approach to integrate multi-granularity accident understanding tasks, including accident recognition, spatial-temporal grounding, with an additional accident description task to guide the model in comprehending the nature of traffic accidents. Extensive experiments demonstrate the superior performance of TABot in traffic accident understanding, underscoring both its potential for high-level anomaly understanding and the robustness of the TAU-106K dataset. All datasets, annotations, and models will be publicly released for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is focused on traffic accident analysis. The authors first introduced the TAU-106K dataset which contains both video and image modalities, and a wide range of fine-grained annotations including both spatial and temporal information. Then trained and evaluated a MLLM model, TABot. The training process has two stages, functional tuning and instruction tuning. The functional tuning involves multiple LLM training tasks to improve model performance in spatial and temporal understanding. The instruction tuning uses multi-round dialogue data generated based on captions by GPT-4o to learn the cause of accidents or prevention suggestions, which leads to the TABot-Chat model. TABot and TABot-Chat show superior performance in comprehensive understanding of traffic accident scenarios.

### Strengths
- Accident data as the rare cases are hard to collect, TAU-106K dataset provides 56% accident data and 44% normal which is a good balance overall. It has both video and image modalities with well annotated information from accident category, temporal location and description which is good for the comprehensive analysis of the accident videos from the ego car view.

- The majority of TAU-106K data is high quality as 720p, as image and video both are provided, it enables image-wise spatial annotation and training with that spatial information. There are also evaluation and ablation studies of (i) image-only model vs normal model, (ii) image task and video task, which is good insight for the community.

- The authors have annotators to precisely identify start and end timestamps of accidents within videos. This metadata is important in traffic scene analysis because it can distinguish the accident frames from non-accident frames, and also helps the Negative Segment Referring (NSR) task.

- The traffic accident description includes the aftermath, to help comprehend traffic accidents, e.g. potential causes of the accident.

-  Proposed method TABot follows the mainstream manner of training multi-modal LLM with a Q-former architecture. But it is good enough to test the different downstream tasks.

- Evaluation is done by comparison of the existing methods on the proposed dataset showing the challenge on the current accident localization.

### Weaknesses
 - Comparison method for OSS model, which is not trained or fine-tuned on the same  train dataset that is hard to convince the the proposal method advantages. 

- Accident data is not balanced for the fine-grained categories, e.g., MMV accidents take the major distribution. It is a concern for the training bias, this needs to be considered in the model design to avoid the data distribution affection for the inference performance. While, accidents and normal still balanced good.

- The reason behind the conclusion regarding the “coverage of the collected traffic data is good” needs to be supported more. As the paper focuses on traffic accident analysis and creating traffic accident dataset, it would be great to share more insights/data/analysis regarding this (e.g., list common traffic types/objects/scenarios and show that the dataset has covered them).

- Lack of comparison with the existing dataset regarding traffic accidents. It should have a single section and related work to describe it, currently the it is mixed in the related works, also lack of the comparison with some literatures such as : 
WTS: A Pedestrian-Centric Traffic Video Dataset for Fine-grained Spatial-Temporal Understanding



### Questions
- TAU-106K is used as both the training set (=90% of the data) of the proposed TABot model and the testing set (=10% of the data) which is unbalanced. It is better to give more train/test splits tests, such as 7:3 for checking the model is not only benefit from the overfitting learning.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors introduce a novel dataset, TAU106k, designed to facilitate the training of multimodal Large Language Models (MLLMs) for a more comprehensive understanding of accidents. This dataset supports tasks such as accident recognition, temporal accident localization, and spatial-temporal object grounding. Additionally, the authors propose a method called TABot and compare its performance with various MLLMs on the TAU106k dataset.

### Strengths
1. **Traffic accident understanding is a critical task in the development of automated driving systems.** To support the training of multimodal Large Language Models (MLLMs) for traffic accident understanding, the authors have collected and annotated a large-scale dataset, TAU106k. This dataset includes structured annotations for accident recognition, temporal accident localization, and spatial-temporal object grounding. Overall, TAU106k comprises 52K video clips and 54K images.

2. **Training Grounding GPT-7B on this dataset yields substantial performance improvements across multiple tasks,** demonstrating that TAU106k effectively supports domain-specific applications.

### Weaknesses
While the paper demonstrates significant effort in creating the dataset, I have the following concerns:

1.	**Lack of clear motivation:** In the introduction, the authors do not clearly articulate the motivation for applying MLLMs to traffic accident understanding, especially since they begin by discussing “traffic accident detection.” Although MLLMs are attracting significant attention in the community, the value of using MLLMs, which may not necessarily operate in real-time, is unclear in this context. The authors should provide a more detailed explanation of why MLLMs are specifically needed for this task, beyond simply leveraging their multimodal capabilities. Justifying the need for this approach would strengthen the paper. In the rebuttal, I would like to hear the authors' feedback on this concern.

2.	**Limited comparison with existing datasets:** The authors are encouraged to provide a more comprehensive comparison between TAU106k and other existing datasets to highlight its unique contributions. For example, please demonstrate key features such as size, diversity of scenarios, types of annotations, or specific tasks supported. The comparison should not only focus on the number of videos but also on the granularity and complexity of the annotations, as well as the diversity of accident types and environmental conditions covered.

3.	**Potential copyright issues with the dataset:** In line 191, the authors mention that the dataset is compiled from various sources, including academic datasets, YouTube, and BiliBili. While they have promised to release the dataset after acceptance, I am concerned that some of the collected data, particularly from platforms like YouTube, may involve copyright issues. If this is the case, the dataset and model release may not be feasible as promised, which would weaken the manuscript’s contribution. Please provide more details on your data collection process, including any steps taken to address copyright concerns, such as obtaining permissions or using only publicly licensed content

4.	**Annotator consistency and accuracy:** In lines 233-234, the authors state that their annotation strategy ensures consistency and coherence. However, it is unclear how many annotators are assigned to each item and how they ensure labeling accuracy if only one annotator is involved. Please provide the details on the annotation process, such as the number of annotators per item, any inter-annotator agreement measures used, and quality control procedures implemented. The authors should also discuss the training process for the annotators and any measures taken to mitigate potential biases.

5.	**Lack of a reasoning task:** In line 219, the authors note that “annotators are encouraged to infer the potential causes of the accident,” but this statement is vague. While the dataset could enable reasoning tasks for traffic accident understanding, the authors do not provide a detailed description or corresponding experiments. This omission detracts from the dataset’s uniqueness. The authors should clarify what type of reasoning is captured by the annotations and how this could be used for downstream tasks.

6.	**Limited improvement from the proposed algorithm:** In Tables 5 and 6, the proposed components show only incremental improvements over the base MLLM (GroundingGPT-7B). If the authors conducted cross-validation or multiple runs, these improvements might not be statistically significant, which could diminish the contribution of the proposed method. The authors should provide statistical significance tests to validate the improvements and discuss the potential limitations of the proposed method.

Comments:

1. In L191, what is the method used from scene change detection?
2. L214, there is a typo (”Due”).

### Questions
1. Please clarify the motivation behind this work (Weakness #1).
2. Please address the copyright issues (Weakness #3).
3. Please explain how consistency in annotation is maintained (Weakness #4).
4. Please provide a rationale for the absence of a reasoning task in the experiments (Weakness #5).
5. Please discuss the limited performance improvement of the proposed algorithm (Weakness #6).

### Soundness
3

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
This paper proposes a large-scale multimodal dataset, TAU-106K, aimed at addressing the limitations of multimodal large language models (MLLMs) in high-level and fine-grained anomaly understanding, specifically for traffic accident scenarios. The TAU-106K dataset comprises images and videos sampled from existing datasets and retrieved from online sources, along with annotated text data. The manuscript also proposed a two-stage fine-tuning approach named TABot to integrate multi-level accident understanding tasks, including accident recognition, spatiotemporal grounding, and an additional accident description task to further enhance the model’s understanding of traffic accidents. While TAU-106K shows potential as a valuable resource, the paper would benefit from a clearer elaboration on the unique challenges of the traffic accident domain and additional experimental comparisons.

### Strengths
This paper focuses on the important field of traffic accident scene understanding, addressing the current limitations of large models in high-level and fine-grained semantic comprehension. It constructs large-scale multimodal models, with a particular emphasis on anomalies, which are critical focal points in the field of autonomous driving. The introduction of this dataset is expected to further promote advancements in this area.
The proposed dataset is designed for various tasks related to traffic accident scenes, including accident recognition, accident description, temporal localization, and spatial grounding. It also features multi-granularity annotations for the collected images and videos, effectively aiding the model in further learning and understanding of traffic accidents.

### Weaknesses
The presentation of the dataset requires further optimization, as the focus on traffic accidents carries significant practical implications and research value. However, the paper lacks clarity regarding the challenges associated with understanding traffic accidents, and the characteristics of such incidents need to be more precisely articulated. Specifically, the paper does not adequately discuss the complexities arising from the diverse range of accident types, varying environmental conditions (e.g., lighting, weather), and the occlusions that are common in real-world traffic scenarios. These factors significantly impact the visual features and temporal dynamics of accident events, making them challenging for models to learn effectively. A more detailed discussion of these challenges is needed to justify the dataset's design and its potential impact.

While the two-step fine-tuning approach is widely recognized, the distinctions between the proposed method and established general methods are not clearly delineated. This creates a disconnect between the methodology and the traffic accident focus of the dataset. Furthermore, the method’s design does not sufficiently address specific tasks, necessitating clearer articulation of its innovations and contributions. The paper does not elaborate on how the two-stage approach specifically addresses the unique challenges of traffic accident understanding, such as the need for fine-grained spatiotemporal reasoning and the ability to handle the long-tail distribution of accident types. The lack of a clear connection between the method and the problem domain weakens the overall contribution.

In the experimental section, there is a need for more comprehensive validation of the challenge of dataset and the effectiveness of method, particularly concerning experimental setup and evaluation metrics. The experimental results lack a thorough analysis of the model's performance across different accident categories, which is crucial given the potential for class imbalance. Furthermore, the evaluation metrics used, such as mIoU and AP, are not fully justified in the context of traffic accident understanding, and there is a lack of comparison with other relevant metrics commonly used in video analysis and anomaly detection tasks. The absence of ablation studies on key components of the method further limits the understanding of its effectiveness.

### Questions
1. How does this dataset compare with existing related datasets? Can specific data be provided? Are there any additional benefits beyond language descriptions? What sets it apart from traditional VQA tasks?
2. Could the annotation process from video to image be more detailed?  And how is multi-turn dialogue accuracy ensured? What steps are taken to ensure annotation reliability, efficiency, and cost-effectiveness?
3. Anomalous events typically show a long-tail distribution. Is this characteristic present in the dataset? How are the resulting distributions in the training and test sets structured?
4. Instruction tuning is classic and common. What is the two-step fine-tuning approach that differs from previous methods? How does Video Spatial Alignment differ specifically from GroundingGPT? Besides input data differences, what specific innovations are presented? Negative Segment Referring is vaguely explained—does it refer to non-accident samples, and how does it differ from standard practices? Hybrid data and task markers are often seen in model fine-tuning; what is their connection to traffic accident detection?
5. The experimental section and method descriptions aren’t well aligned. For instance, what are the distinctions between Negative Segment Referring, multi-turn dialogues, TABot (Video), TABot (Ours), and TABot-Chat (Ours)? Does Ours use both video and image training data? How is multi-turn dialogue in -Chat specifically designed? More clarity is needed.
6. What is the relationship between the four tasks: accident recognition, accident description, temporal localization, and spatial grounding? Could these tasks validate each other to improve model performance? What is Image Understanding in the experiment section, and how does it relate to the other four tasks?
7. The authors achieved remarkable results with GroundingGPT. How is the performance of the proposed method based on other models?
8. For some metrics, GroundingGPT achieves 100% accuracy, while for others, it scores 0%. What causes this drastic disparity, and could it be related to experiment settings or metric choices?
9. In the case study, how do prediction results from different methods compare to ground-truth annotations? Additionally, some details need review. For instance, the conclusion mentions an image count of 55k, which seems inconsistent with earlier descriptions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new dataset, TAU-106K, to help MLLMs gain a comprehensive understanding of traffic accidents. In addition, the paper also proposes a two-stage fine-tuning mechanism to use the proposed dataset. The experimental results basically prove the effectiveness of the proposed method and data.

### Strengths
The dataset proposed in this paper covers a wide range of knowledge about traffic accidents, which has greatly promoted the development of MLLMs in this specific field. The diversity and details of the proposed dataset are meaningful and meet the expectations of MLLMs to learn specific knowledge.

### Weaknesses
This paper provides a meaningful dataset and benchmark, but I still have some concerns:

* Although the experimental results basically prove the superiority (table 1, 2, 3, 4), the highlighted information is confusing: Is the performance improvement due to the rich knowledge of the data or the fine-tuning strategy? Both aspects should have an effect, so there should be more comparisons and ablations. For example, you can use your proposed dataset to fine-tune other baseline models.

* Accident Recognition uses the Yes and No responses of the model to make binary classifications. In a random situation, are the probabilities of the model responding Yes and No balanced? If not, will this cause the evaluation to be disturbed by some irrelevant prior knowledge? You can start from reporting the base rates of Yes/No responses.

* There are some spelling and grammatical errors that the author would like to note (for example: line 192 'hey', line 238 'is', line 375 'a the', ...).

### Questions
The author can think more about the proposed data and benchmarks:

* In addition to the defined traffic accidents, there are actually more conner cases, which are often the most difficult to learn in the open world. How to use the proposed method to let MLLMs learn this knowledge?

* Is there greater potential for the generalization of data?

### Soundness
3

### Presentation
2

### Contribution
2
