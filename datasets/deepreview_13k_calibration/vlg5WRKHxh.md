# $F^3Set$: Towards Analyzing Fast, Frequent, and Fine-grained Events from Videos

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8

## Abstract
Analyzing Fast, Frequent, and Fine-grained ($F^3$) events presents a significant challenge in video analytics and multi-modal LLMs. Current methods struggle to identify events that satisfy all the $F^3$ criteria with high accuracy due to challenges such as motion blur and subtle visual discrepancies. To advance research in video understanding, we introduce $F^3Set$, a benchmark that consists of video datasets for precise $F^3$ event detection. Datasets in $F^3Set$ are characterized by their extensive scale and comprehensive detail, usually encompassing over 1,000 event types with precise timestamps and supporting multi-level granularity. Currently, $F^3Set$ contains several sports datasets, and this framework may be extended to other applications as well. We evaluated popular temporal action understanding methods on $F^3Set$, revealing substantial challenges for existing techniques. Additionally, we propose a new method, $F^3ED$, for $F^3$ event detections, achieving superior performance. The dataset, model, and benchmark code are available at https://github.com/F3Set/F3Set.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Thanks the authors for this ICLR2025 submission.

Summay:

This paper makes contribution to faciliating the detection of fast-speed, high frequence and fine-grained action events in videos. A new dataset, specific to **tennis**, is proposed to this purpose, together with an video frame-wise label annotation tool, which enables the collections of accurate labels. In experiments, a novel model is proposed and benchmarked on temporal action detection over 3 levels of granularity. Some ablation study is provided. To showcase the scalabiility and generalizability of proposed apporach, the paper extends the study to several other action-sports datasets (e.g., diving, gym, etc).

### Strengths
- Writing is easy to follow.
- The proposed dataset is collected with notable efforts, and is very-well organzied and presented. So does the 3-step annotation procedure, a very practical approach to the video dense annotation problem.
- The appendix further provides comprehensive stats.
- The experimental results are strong.

### Weaknesses
In general, there are a few minor weakness spotted in the experiment section which puts question marks to the technical sound of this paper.

- (minor) The statement on line 398-399, `...it is crucial to utilize frame-wise feature extraction [7]`, is not well supported. The author might have gained much insights through some hidden experiments that clip-wise feature extration is inferior to frame-wise methods. Yet, it is less clear to the general audience. It is unclear why frame-wise feature extraction is crucial, especially given that clip-wise methods, which aggregate information over short temporal windows, might be more robust to noise and could capture motion cues more effectively. The paper should provide a more thorough justification for this design choice, perhaps by including a comparative analysis with clip-based feature extraction methods.
- (minor) It would be more insightful to provide the numeric impact of the **Event localizer** to the whole F^3ED system. As it would be a concern if a very good performing LCL module is the **hard-prerequisite**, in which case the generalization of the F^3ED approach is bit questionable. In some scenarios,  a good LCL might not be possible to have. The current analysis does not sufficiently address the potential limitations of the proposed approach if the LCL module does not perform well. The paper should include a more detailed analysis of the system's performance under varying LCL performance levels, including cases where the LCL module is significantly less accurate, to better understand the robustness of the overall system.
- (minor) There is a lack of in-depth discussion why GRU based method is adopted in the CTX stage, given the transformer module has been demonstrated more efficient on long-range context modeling. The paper should provide a more detailed analysis of why a GRU-based approach was chosen over transformer-based architectures, which have shown superior performance in capturing long-range dependencies. The current justification lacks sufficient technical depth, especially considering the potential benefits of transformers in modeling temporal context.
- (minor) Figure 4 should be more clear on 1) what is the "plus" symbol that combines outputs of LCL and MLC, and 2) what are the red squres in feature vectores under the CTX module. The figure lacks clarity regarding the specific operations performed by the "plus" symbol and the meaning of the red squares, which makes it difficult to understand the flow of information through the system. A more detailed explanation is needed to clarify the role of each component in the overall architecture.

Missing reference:
- Sports video analysis on large-scale data, ECCV 2022

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper mainly introduces a dataset for advancing fast, frequent and fine grained video processing tasks.

They also introduce a model built on top of the newly introduced dataset, and show improvements over several variants of existing video encoders and temporal fusion modules, eg, transformer-based modules, etc.

They choose some video encoders such as SlowFast, TSN and TSM, with different head architectures and compared to their proposed model. Experiments on 3 levels of granularity show the effectiveness of the model.

They also evaluate their module on top of TSM video encoder, on some fine grained benchmarks and show consistent improvements.

### Strengths
+ The efforts of collecting a dataset for fast, frequent and fine grained events are appreciated.

+ The authors identify an interesting research problem, in terms of fast, frequent and fine grained video-related research.

+ Table 1 is a nice and interesting comparisons.

+ Some interesting comparisons and experiments conducted, and the authors also provide some valuable insights, especially section 5.1.

### Weaknesses
Major:

- The dataset currently focuses on tennis swing, the contribution is limited (i) how your dataset differs from existing dataset and (ii) the dataset at this stage is only tennis, what would be the scope and focus of this benchmark.

- The paper is written in a rush, and not well-structured. The authors mention that “our benchmark can contribute towards a VideoNet for future LLM’s benchmarking and finetuning”, but where and how? The contributions listed are also a bit vague and weak at this stage.

- A review of existing closely related works for the concept of “fast, frequent and fine grained” is not performed; however, the paper introduces the new model (i) any existing works in the literature and how the proposed method differs from existing works (ii) any insights from reviewing existing works, eg, any practical concerns that highlight the importance of introducing a new model, etc.

- Sec. 3 is not well-written and well-structured. The reviewer suggests the authors refine this work, and make it solid enough for next venue. Having a complete understanding, review and analysis in this work, would be much appreciated.

- The justification of choosing evaluation metrics is not provided, and how these evaluation metrics contribute to the evaluation of performance etc. Section 5 page 7 bottom, what does it mean by “we have adapted these methods to develop …”, what methods and how this is performed?

- Regarding evaluations, in Table 2, the use of video encoders is a bit too limited, although the reviewer likes the interesting comparisons presented. The authors should refine their research aims and make it better and clear. The current scope a bit too big, and also core evacuations a bit too limited. This would affect the impact of the work.

- Showing the evaluation results in the form of list is not good, eg, in section 5.1. More detailed discussions are indeed needed to show more in depth analysis and comparisons. Although the paper discusses some insights, the paper at this stage is too raw and requires further efforts to make it solid and thorough enough. Last sentence of section 5.1 does not provide much information. “… achieves optimal performance among all methods”, how and why?

Minor:

- The fine grained concept should be first introduced in the introduction section, eg what is fine grained recognition tasks in videos, and what is the concept of frequent and fast.

- All the experimental results and evaluations are presented in the form of tables. The authors are encouraged to use some plots, visualisations to make the comparisons clear and vivid to researchers and readers.

- As a research paper, it is suggested to make it as clear as possible, eg “Conflicting samples were resolved using a majority vote criterion”, but how?

- A notation section detailing the maths symbols used in the paper would be better.

- Section 4, the proposed model is also unclear to reviewer. Inside problem formulation, what is that “j”? Fig. 4 is also not clear to reviewer. The figure caption does not provide much information to understand the figure.

- In Introduction section, what is “T”, body and wide? These concepts are unclear to reviewer. The concepts are not very well-explained.

- Incomplete sentence in sec. 3.1, “If it lands in bounds after crossing the net.”, it would be better to have a figure explain these concepts clearly in lexicon section would help readers. Fig. 3 suffers from low resolution, and the fonts are unable to read due to its too small nature.

### Questions
Please refer to my concerns above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces **F3Set**, a novel sports-related dataset designed to address the challenges of detecting fast, frequent, and fine-grained (F3) events from videos. The dataset contains over *1,000* event types annotated with precise timestamps, primarily focused on tennis, but also includes other sports such as badminton and table tennis, with the potential to be extended to various other sports. To tackle the challenges of event classification and localization, the authors propose **F3ED**, a model that utilizes a video encoder for spatial-temporal feature extraction, a multi-label event classifier, and a contextual module to refine event sequence predictions. The model is evaluated on F3Set and demonstrates superior performance over certain models in both event localization and classification. Additionally, the authors provide a semi-automated toolchain for annotating F3 events, making the dataset scalable for use in other sports.

### Strengths
- **Originality**: The paper introduces a dataset designed for detecting **fast, frequent, and fine-grained events** in sports videos. While there have been other tennis-related datasets, such as **Tennis Stroke Dataset** and **TennisDB**, **F3Set** stands out due to its **1,000+ annotated event types** and precise annotations with fine-grained details.

- **Quality**: The dataset contains over **11,584 video clips** of professional tennis matches, featuring **42,846 tennis shots** and detailed annotations. Each shot is labeled with attributes like shot type, direction, and outcome, allowing for comprehensive event analysis. Also dataset has been collected in high resolution and moderate fps 25-30, which can be utilized for tasks beyond event classification, such as pose estimation and movement analysis.

- **Clarity**: The authors provide clear examples of how annotations are done, such as distinguishing between forehand and backhand shots, and detailing shot outcomes like winners or errors. The explanations of **multi-level granularity** make it easy to understand how the dataset can be applied to different tasks, from coarse to fine event classification. In addition, the authors did a very good job providing the explanation of tennis terminology. 


- **Code and Tools**: The authors provide a **well-structured and anonymized codebase**, along with a semi-automated toolchain for efficient event annotation.  This makes it easier for researchers to adopt the dataset and extend it to other domains.

- **Dataset Diversity**: The dataset includes **high-resolution videos** from 114 professional tennis matches featuring both men and women players, with frame rates of 25-30 FPS. This diversity, along with specific annotations for both right- and left-handed players, ensures the dataset can support a wide range of analyses.

### Weaknesses
 - **Significance**: While the dataset is beneficial for sports like tennis, badminton, and table tennis, the methodology is highly limited due to the nature of these sports. These sports are relatively easier to model with their controlled environments and predictable movement patterns, but the methodology may not generalize well to faster and more complex sports like **soccer** or **basketball**, which require higher FPS rates and need to account for multi-player interactions. The paper does not adequately address how the proposed model would handle the increased complexity of tracking multiple players and the more stochastic nature of events in these sports. For example, in soccer, the ball's trajectory and player movements are far less predictable than in tennis, making the task of event detection significantly more challenging. 

- **Benchmark Simplicity**: The proposed benchmark, while interesting and comprehensive in its approach, is relatively simple. The choice to crop the input videos to **224x224 resolution** while originally collecting them in higher resolution raises questions. The authors claim that F3ED outperforms more complex models like **SlowFast**, but this might be due to the limited resolution of the input images, which could fail to capture subtle visual distinctions. The low resolution could be smoothing out important details, making the task artificially easier. More work is needed to confirm or debunk this claim, including testing higher-resolution inputs to better understand the effects of image quality on model performance. It is also unclear if the reported performance gains are due to the model's architecture or simply the training regime used.


- **Dataset Nature**: While the dataset is relatively diverse, there are still questions regarding the impact of **camera angles**, **court types**, **weather conditions**, and **illumination**. In real-world settings, these factors can vary significantly and may affect model performance. While in professional competitions these variables might be more consistent, in practical scenarios such variations could play an important role in the robustness of event detection. Ideally, dataset and benchmark should thoroughly address those concerns. The paper does not provide a detailed analysis of how these variations affect the model's performance, nor does it include experiments that explicitly test the model's robustness to these factors. For example, the model's performance under varying lighting conditions, such as strong sunlight or shadows, is not explored.

- **Fit with ICLR and Representation Learning**: A notable weakness of this paper is that it does not explicitly address how the proposed model learns **representations** or how these representations could be generalized or transferred to other domains. Additionally, the paper primarily compares its performance to models with similar architectural structures, such as 3D CNNs, without exploring **fundamentally different approaches** to event detection. For instance, instead of relying on crops, the authors could have explored using **pose estimation techniques** to detect human poses and tackle the problem from a different perspective. Comparing such an approach across metrics like accuracy and speed, and then resonating on why one method outperforms or underperforms the other, would have provided valuable insights into the advantages or limitations of the proposed approach.

### Questions
- **Generalization of Methodology to Other Sports**: How do you expect the proposed methodology to generalize to sports with faster movements and multiple players, such as **soccer** or **basketball**? Can the model handle the requirements for higher frame rates and multi-human event interactions, or are there adjustments needed for such cases?

- **Use of Low-Resolution Input (224x224)**: The decision to use **224x224 crops** despite collecting higher resolution videos raises questions. Have you tested the model on **higher resolution inputs**, and if so, how did it perform? Could higher resolution provide more visual details and improve the model’s ability to detect subtle distinctions?

- **Alternative Approaches for Event Detection**: The paper focuses on comparing the proposed method with models using **similar architectural foundations** like 3D CNNs. Have you considered comparing your method to **fundamentally different approaches**, such as **pose estimation** for event detection (In other words: extracting poses and then utilizing coordinates to classify events)? How would such comparisons impact performance in terms of accuracy, speed, and interpretability?

- **Dataset and Camera Perspectives**: The dataset appears to focus on controlled environments, but real-world scenarios often involve **different camera angles, lighting conditions, and varying court types**. How would your model perform under different camera perspectives or in less controlled environments? Have you tested the model with variations in lighting or weather conditions?

- **Scalability of Annotation Process**: The paper mentions a **semi-automated toolchain** for annotating events. How scalable is this annotation process, especially if applied to larger datasets or more complex sports with multiple participants?

### Soundness
2

### Presentation
3

### Contribution
3
