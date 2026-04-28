# FusionBench: A Comprehensive Benchmark of Deep Model Fusion

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Deep model fusion is an emerging technique that unifies the predictions or parameters of several deep neural networks into a single model in a cost-effective and data-efficient manner.
  This enables the unified model to take advantage of the original models' strengths, potentially exceeding their performance.
  Although a variety of deep model fusion techniques have been introduced, their evaluations tend to be inconsistent and often inadequate to validate their effectiveness and robustness against distribution shifts.
  To address this issue, we introduce \textit{FusionBench}, which is the first comprehensive benchmark dedicated to deep model fusion.
  FusionBench covers a wide range of tasks, including open-vocabulary image classification, text classification, and text-to-text generation.
  Each category includes up to eight tasks with corresponding task-specific models, featuring both full fine-tuning and LoRA fine-tuning, as well as models of different sizes, to ensure fair and balanced comparisons of various multi-task model fusion techniques across different tasks, model scales, and fine-tuning strategies.
  We implement and evaluate a broad spectrum of deep model fusion techniques. These techniques range from model ensemble methods, which combine the predictions to improve the overall performance, to model merging, which integrates different models into a single one, and model mixing methods, which upscale or recombine the components of the original models.
  FusionBench now contains 26 distinct tasks, 74 fine-tuned models, and 16 fusion techniques, and we are committed to consistently expanding the benchmark with more tasks, models, and fusion techniques.
  In addition, we offer a well-documented set of resources and guidelines to aid researchers in understanding and replicating the benchmark results. This includes detailed documentation, code examples, and tutorials, making FusionBench a user-friendly and accessible platform for both beginners and experienced researchers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents FusionBench, a comprehensive benchmark platform to evaluate deep model fusion techniques across tasks in image classification, text classification, and text generation. FusionBench organizes fusion techniques into model ensembles, model merging, and model mixing, and includes 26 tasks, 74 fine-tuned models, and 19 fusion algorithms. The benchmark aims to standardize evaluations, ensuring fair comparisons and supporting both novices and researchers with accessible resources and tutorials.

### Strengths
1. FusionBench covers a broad range of tasks and fusion methods, providing flexibility for various fusion scenarios in NLP and vision tasks.
2. Accessible resources, detailed documentation, and examples make FusionBench highly usable for beginners and researchers alike.
3. The benchmark offers a fair, standardized evaluation of fusion methods, supporting clear comparisons across tasks.
4. Well-organized structure, visual aids, and concise descriptions make it easy to understand and navigate the platform.

### Weaknesses
1. The absence of direct comparisons with baseline models.
2. A deeper explanation for the categorization of model ensembles, merging, and mixing would help clarify their task-specific benefits.
3. More insights on scalability to additional tasks or modalities would enhance FusionBench’s applicability to diverse research needs.
4. FusionBench’s effectiveness depends on high-quality pre-trained models, which might limit performance in under-resourced domains.

### Questions
Q1. Did you explore any non-fusion baseline models to provide a more direct comparison of fusion performance benefits? If so, could those results be included to clarify the relative impact of fusion methods?
Q2. Do you foresee expanding FusionBench to include multi-modal tasks, or would that require significant modifications to the existing benchmark structure?
Q3. Are there recommendations for tuning fusion methods based on specific task types, especially for users who may be new to model fusion?
Q4. How does FusionBench handle variability in pre-trained model quality? Are there mechanisms to assess or adjust for model quality across tasks?

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
4

### Summary
The authors propose a comprehensive benchmark for deep model fusion that evaluates various models across a wide range of CV and NLP tasks. They also develop a modular codebase for user-friendly realization and evaluation of different model fusion approaches.

### Strengths
1. The paper is well-written and easy to follow.

2. The proposed framework is modular and user-friendly.

3. The authors comprehensively evaluated deep model fusion across different tasks and models.

### Weaknesses
1. While the authors seem to evaluate against 26 tasks as claimed in the paper, I found the actual number of tasks quite limited. For example, there are 8 different datasets used for image classification, but the authors deem them as 8 tasks. Fairly speaking, they can only be regarded as 8 benchmarks on the image classification task. In that sense, the wordings in such as Table 5 should be seen/unseen domains instead of tasks.

2. For the scene understanding part, the tasks are all limited to the dense per-pixel prediction type (depth, normal, and segmentation), and are only conducted against the NYUv2 dataset. I would recommend adding additional tasks that are common in this area, such as object detection. Furthermore, the current evaluation focuses solely on in-domain multi-task learning, which limits the scope of the benchmark.

### Questions
I appreciate the authors' engineering efforts in putting together such a framework for evaluating deep model fusion. If the authors can address my concerns properly, I would be happy to edit the rating.

1. In Table 2, the term `tasks` seems abused. Technically, there are 8 datasets instead of tasks for the image classification task. The same applies to the text classification and generation task, with 7 and 8 datasets, respectively. The scene understanding does contain 3 tasks (segmentation, depth, and normal). I recommend the authors edit the terminologies used and make the tables clearer. 
- for the image classification task, the setting looks more like domain transfer and generalization
- for the scene understanding, it is standard multi-task learning

The authors may argue that among the 8 datasets, there are object recognition, satellite image classification, etc. "tasks" (what is said in their paper). However, these are all under the open-vocabulary image classification task, and getting down to that granularity does not make sense if we consider the other tasks in the paper (such as depth, segmentation, etc.)

2. All the scene understanding tasks are dense (per-pixel) prediction tasks. It would be interesting to consider tasks such as object detection. Also, using the NYUv2 dataset only covers the in-domain multi-task setting and is limited. How about doing a cross-domain multi-task setting? For example, a segmentation model on ADE20K, plus a depth model on KITTI.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposed the first deep model fusion benchmark FusionBench together with codebase. The codebase is composed of three main modules: Algorithm, Mode Pool, and Task Pool. FusionBench has 16 built-in fusion algorithms implemented. Their comprehensive evaluation results are presented in the paper.

### Strengths
1. The paper is very well motivated. As the first evaluation benchmark for deep model fusion, it would surely benefit the future researches in the domain.
2. Extendability is a very important aspect for open-source benchmark. Glad to see it has been taken into consideration.

### Weaknesses
Recently, LLM and T2I/V models have gained tremendous attention in the research community. It might be worth adding evaluation for that. E.g., fusion methods for LLaMA based models, StableDiffusion models.

### Questions
N/A

### Soundness
3

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
4

### Summary
The paper presents FusionBench, a benchmark for evaluating deep model fusion techniques, which unify multiple neural networks into a single, more effective model.

### Strengths
1- The proposed pipeline offers various tasks (image and text classification, text generation) and includes multiple models and fusion strategies (e.g., model ensembles, merging, and mixing). 

2- FusionBench standardises evaluations across tasks, model sizes, and fine-tuning methods, providing resources like documentation and tutorials to support researchers in replicating results.

3- The paper is well-written, making it easy to read and understand.

### Weaknesses
1- This work appears to be an engineering effort to generalise existing models and methods within a unified pipeline. However, it lacks scientific novelty and significant technological advancement. Therefore, it may be better suited for applied venues, such as workshops, rather than a top-tier fundamental research conference.

2- Besides the above issue, it still seems unclear how the model mixing happens in the background, though they state a list of existing methods they use in Table 1. Specifically, the paper does not detail the implementation of these mixing methods, such as how the weights are combined or how the gradients are handled during training. This lack of clarity makes it difficult to assess the technical contribution of the work beyond simply listing existing techniques.

3- Figure 1 is not very illustrative as Fig-1(b) and Fig-1(c) are almost identical. Further demonstration might be required in this regard. The diagrams fail to clearly distinguish between the different fusion strategies, particularly model merging and mixing. A more detailed illustration, perhaps with different visual cues for each method, would be beneficial.

4- In terms of evaluation, it would be more beneficial to see how the proposed system works on large-scale data, such as the ImageNet-1k involved. The current evaluation lacks experiments on more challenging datasets, which limits the generalizability of the findings. Testing on a larger, more diverse dataset would provide a more robust evaluation of the proposed system's capabilities.

5- I could not find any evidence of the claimed deliverable in the submitted work as stated in the abstract. "...This includes detailed documentation, code examples, and tutorials, making FusionBench a user-friendly and accessible platform for both beginners and experienced researchers."

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
