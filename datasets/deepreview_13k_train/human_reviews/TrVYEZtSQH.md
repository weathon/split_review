# MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding

- Decision: Accept
- Scores: 6, 6, 6, 5, 3

## Abstract
We introduce \BENCHMARK, a comprehensive benchmark that focuses on robust multi-image understanding capabilities %
of multimodal LLMs.
\BENCHMARK consists of 12 diverse multi-image tasks (\eg, \scene, \ordering) that involve 10 categories of multi-image relations (\eg, multiview, temporal relations).
Comprising 11,264 images and 2,600 multiple-choice questions,
\BENCHMARK is created in a pairwise manner, where each standard instance is paired with an unanswerable variant that has minimal semantic differences, in order for a reliable assessment. 
Evaluated upon 20 recent multi-modal LLMs, our results reveal that even the best-performing models like GPT-4o and Gemini Pro find it challenging to solve \BENCHMARK, achieving 68.0\% and 49.3\% in accuracy. 
Open-source multimodal LLMs trained on single images can hardly generalize to multi-image questions, hovering below 33.3\% in accuracy.
These results highlight the importance of \BENCHMARK in encouraging the community to develop multimodal LLMs that can look beyond a single image, suggesting potential pathways for future
improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces MUIRBENCH, a new benchmark designed to evaluate the capabilities of multimodal large language models (LLMs) in multi-image understanding. MUIRBENCH comprises 11,264 images and 2,600 multiple-choice questions spanning 12 multi-image tasks and 10 types of multi-image relations. Each task is paired with unanswerable counterparts to test robustness. Evaluations show that prominent models, like GPT-4 and Gemini Pro, perform far below human accuracy, emphasizing the need for improved models capable of holistic multi-image comprehension.

### Strengths
Let me first clarify that I am not an expert in evaluation dataset construction.
1) MUIRBENCH covers 12 different multi-image tasks and 10 image relationship categories to ensure the evaluation as comprehensive as possible.
2) Including answerable and unanswerable question variants can evaluate the robustness of models.
3) The image sources are expanded. In addition to existing multi-image data, medical, geographical, etc. are considered.
4) Human quality control and evaluation results are introduced to provide the evidence of faithfulness.

### Weaknesses
Let me first clarify that I am not an expert in evaluation dataset construction.

1) Lack of data scale comparison: I am not clear about the data scale of related multimodal evaluation benchmarks. It is recommended to provide a table to compare existing single-image/multi-image evaluation benchmarks, including the number of samples, the number of tasks, the number of relations, the number of image domain, etc. At least it is necessary to explain clearly how much improvement the proposed dataset in this paper has compared with previous work. I am not sure whether 1,300 answerable questions, 12 tasks and 10 relations are a relatively large improvement.

2) Specific explanation of comprehensiveness: I know that this paper considers 12 tasks and 10 relations, which sounds like a number that is neither too many nor too few. It is not clear whether there is evidence or analysis to state that this dataset is comprehensive enough at least within a certain range.

3) Are the ground-truth answers reliable? The human quality control does not seem to mention the analysis of the reliability of the answer. It seems that there is only human quality control of questions and images. I am not sure whether humans will find it difficult to judge or have no correct answers when answering these questions, and whether there will be subjective differences that lead to inconsistent evaluations by multiple people, which will add additional uncertainty to model evaluation.

### Questions
See Weaknesses.

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
This paper presents a new evaluation benchmark, dubbed MuirBench, which focuses on multi-image understanding capabilities of multimodal LLMs. Specifically, MuirBench contains 11,264 images and 2,600 multiple-choice questions, covering diverse multi-image relations. In experiments, the authors have evaluated 20 recent multi-modal LLMs, revealing that the best-performing models still struggled in multi-image understanding. Besides, the authors have also conducted detailed analyses, demonstrating possible reasons for the unsatisfying performance of multimodal LLMs.

### Strengths
- The evaluation aspect about multi-image understanding is novel and important for multimodal LLMs, which present significant contributions to the field.
- The proposed benchmark covers many types of multi-image relations, such as temporal, ordered-pages, or narrative relations, which are comprehensive to support solid evaluations for multimodal LLMs.
- The unanswerable counterpart of the benchmark presents a complementary perspective to assess multimodal LLMs fairly.

### Weaknesses
 - It would be better if the authors could provide detailed comparison with recent multi-image evaluations benchmarks, such as Milebench, in a summarized table. This can help better capture the unique characteristics of MuirBench.
- The evaluation on MuirBench seems to require lots of computation resources, which may limit the accessibility for researchers with fewer resources.

### Questions
- Do the authors have plans to expand or adapt MuirBench to include new tasks or modalities as LVLM capabilities evolve?

### Soundness
3

### Presentation
4

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
This paper proposed a new benchmark aims at evaluating the performance of multi-modal language models for handling multiple image inputs.
The benchmark is designed following two key points, comprehensive coverage of tasks and robust evaluation.
For the comprehensive coverage of tasks, the paper seeks to leverage existings datasets from multiple sources as well as sourcing new data.
For the robust evaluation, the benchmark create unanswerable questions paired with each question.

Evaluation on the proposed benchmark demonstrates a gap of current multi-modal language models in understand multiple image inputs compared with human.

### Strengths
1. I think the paper is tackling an interesting and relativly novel setting, that is in evaluating the reasoning abilities of models across multiple inputs.
2. The experimental results demonstrate that there are indeed a gap for current models, and a possible direction for future research to be done.
3. The paper tested a range of state-of-the-art models.

### Weaknesses
1. The description of how the performance on unanswerable questions are measure is not very clear to me. Is "this question is unanswerable" part of the option or the evaluation just expect the model to give this?
2. Seems like the benchmark is unevenly distributed across different questions types and image types.
3. The benchmark consists of 10 different relations for multi-image, however, it is unclear to me how these 10 relations are chosen.

### Questions
1. I would like to know how the 10 relations are chosen, and how they can represent the use cases of multi-image understanding.
2. How is the performance on unanswerable questions measured.
3. The benchmark is imbalanced in terms of the question types and image types, how can one obtain one single score that can reflect the overall ability of the model to understand multiple images?
4. In L146, it is claimed that MIRB is released later than this paper. I'm wondering how is this claim supported? Given that this paper is still underreview.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes MuirBench, a benchmark that comprehensively measures LVLM's multi-image understanding capabilities, including multiple image relationships and multiple task types, and conducts a detailed evaluation and analysis on MuirBench.

### Strengths
1. The author proposed MuirBench, which is a comprehensive enough benchmark to measure the multi-graph understanding ability of the model
2. The author conducted a relatively detailed evaluation and discussion, which can provide some insights for the community

### Weaknesses
1. The first picture of Figure5 seems to be ambiguous: the correct order can be washing dishes and then opening the cabinet, but the reordered order can be interpreted as washing dishes, opening the cabinet and then closing it, depending on the frequency and method of frame extraction. When the number of pictures is small, reordering does not necessarily make the problem unanswerable. (Just like when looking for patterns, if there is not enough prior information, there are many ways to explain the pattern)

2. Unanswerable setting experiment may be ambiguous: Imagine such a scene: when a poor student faces a difficult question, he does not understand the question at all and cannot make a choice. At this time, the student may choose randomly or refuse to answer because he thinks he lacks the necessary information (the large model also has the phenomenon of complete question information, but refuses to answer due to insufficient ability [1]). If we change the question information to make the question unanswerable, and add unanswerable options. At this time, facing the unanswerable option, the poor student may directly choose the unanswerable option, resulting in "cheating". However, we cannot assume that the student understands the question. Similarly, the author points out that most models have poor multi-image understanding performance, which can be compared to the poor students mentioned above, so I have doubts about the settings and results of unanswerable.

3. There are problems with the settings of Multi-Image Input Models: I don’t understand the sentense: “the models that do not support multiple images as input” in 310. For the “SIngle-Image Input Models" defined by the author here, why can’t we concat the image tokens and then input them to the subsequent modules? Like InternVL1.5-chat [2], GLM-4V-9b. It has not been trained with multi-image data, but it can still perform multi-image QA through the above operations. Or should the author’s definition of “Multi-Image Input Models” here be models trained with multi-image data?

4. Although the author used the method of directly concat input images to test "single-image input models" here, this will result in too low image resolution, which may affect the performance of these models. The author should compare the effect of testing the "single-image input models" defined here using concat visual tokens. For specific methods, please refer to the test code provided by InternVL-Chat-V1-5 on HuggingFace (`pixel_values ​​= torch.stack(pixel_values)`). I think it is a more comprehensive way to test the "single-image input models" using both concat image and concat image token.

5. The author lacks some more advanced open-sourced models for evaluation, such as LLava—interleave [3], GLM-4V-9b [4], etc.

### Questions
Please refer weaknesses for details.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces MuirBench mainly focusing on robust multi-image understanding capabilities of VLMs. The benchmark covers 12 multi-image understanding tasks and introduces unanswerable data. 20 recent VLMs are tested on the benchmark and several related analyses are provided.

### Strengths
1. The MuirBench covers 12 multi-image understanding tasks, involving diverse scenarios. It is a comprehensive benchmark containing 11,264 images and 2,600 multiple-choice questions.
2. The paper conducts detailed testing on 20 recent VLMs, revealing the limitations of these models in multi-image understanding and the performance gap compared to single-image input.
3. The analyses of unanswerable-type questions, image positioning, and error analysis of GPT-4o are impressive.

### Weaknesses
 1. The paper only contributes data without offering any insightful analysis of model limitations and lacks novelty and contribution. It does not give people any new knowledge, and people do not feel any insight after reading it.
2. Authors overlooked some of the newer VLMs, such as Gemini 1.5 Pro (Feb. 2024), InternVL1.5-Chat (Apr. 2024) and Claude 3.5 Sonnet (Jun. 2024)
3. Although some limitations of the models in multi-image understanding tasks are shown, there is no discussion on the architectural limitations of these models, why these VLMs underperformed, why certain models perform poorly on different tasks or how models’ architectures could be adapted for better multi-image understanding. Furthermore, the suggestions for future improvements are rather general and lack detailed explanations of specific technical approaches for new VLMs. To sum up, the analysis part in this paper is superficial, more insight is required. 
4. The difficulty of question among different tasks is imbalance.
5. It seems that unanswerable questions have limited practical applications in real-world scenarios.
6. Some of the questions in the benchmark do not need to be presented in multiple images, such as question “Counting” and “Image-Text Matching” in Figure 6. As a questioner, I would consider inputting images one by one to ensure accuracy. A benchmark needs to focus more on practical application value rather than just creating a question that is difficult for VLMs.

### Questions
1. What specific shortcomings of the VLMs’ capabilities do your benchmark actually reveal?
2. Authors are encouraged to provide results on some of the latest models, such as InternLM-XComposer2.5-7B (2024/07/03), the InternVL2 series (2024/07/04), and the Qwen2-VL series (2024/08/30). While the results of these models are not mandatory under the guidelines, considering the super-fast advancements in VLMs this year. Could you please include results from some of the aforementioned models to highlight the performance of the latest generation of VLMs in multi-image understanding?
3. The pairwise design of answerable and unanswerable questions seems to create an artificial scenario. Unanswerable questions are more ambiguous and complex. How does your dataset account for the nuance of real-world multi-image understanding?
4. Line 311 mentions "concatenate the images to constitute one input." How exactly are the images concatenated? Could it be that the concatenation method affects the model's performance? What are the results of using different concatenation methods?
5. Please refer to Weaknesses for more potential questions.

### Soundness
2

### Presentation
2

### Contribution
1
