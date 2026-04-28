# VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Large language models (LLMs) famously exhibit emergent in-context learning (ICL) -- the ability to rapidly adapt to new tasks using few-shot examples provided as a prompt, without updating the model's weights. Built on top of LLMs, vision large language models (VLLMs) have advanced significantly in areas such as recognition, visual question answering (VQA), reasoning, and grounding. However, investigations into \emph{multimodal ICL} have predominantly focused on few-shot VQA and image captioning, which we will show neither exploit the strengths of ICL, nor test its limitations. The broader capabilities and limitations of multimodal ICL remain under-explored.
   In this study, we introduce a comprehensive benchmark for multimodal in-context learning. Our \textit{\bench{}} encompasses a broad spectrum of tasks that involve both images and text as inputs and outputs, and different types of challenges, from {perception to reasoning and long context length}. We evaluate the abilities of state-of-the-art VLLMs on this benchmark suite, revealing their diverse strengths and weaknesses, and showing that even the most advanced models, such as GPT-4, find the tasks challenging. By highlighting a range of new ICL tasks, and the associated strengths and limitations of existing models, we hope that our dataset will inspire future work on enhancing the in-context learning capabilities of VLLMs, as well as inspire new applications that leverage VLLM ICL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates an important property for vision large language models (VLLMs): evaluting the in-context (ICL) ability in multi-modal scenes. The authors first point out current VQA and captioning benchmarks are not ideal for evaluting multi-modal ICL via quantitative results. To bridge the research gap, the authors proposes the first ICL benchmark, VL-ICL bench, which encompasses 10 tasks and is used evaluate both the image-to-text and text-to-image models. The authors provide the comprehensive evaluation for a range of VLLMs on the proposed VL-ICL bench.

Overall, I appreciate the motivation to evaluate the ICL capabilities of multi-modal models, as this is a significant yet under-explored area. The experiments are extensive and yield useful conclusions.

### Strengths
1. The paper starts from a good motivation for evaluating the ICL ability of current multimodal models.
2. This paper proposes the VL-ICL bench convering 10 tasks to evaluate the diverse capacibilities such as perception, reasoning, rule-induction.
3. The authors conduct extensive and thorough experiments with the current multimodal models on the proposed benchmark

### Weaknesses
1. Some details about the construction of VL-ICL should be clarified. For the datasets used in Table 1, do you use all the samples from the original sources? Do you perform some filtering strategies?
2. Could the authors give more explanations about the metric ICL efficiency? Why the ICL efficiency has negative numbers in Table 2?
3. Based on the curve figures (e.g., Figure 5 and Figure 6), it appears that the multimodal models do not significantly benefit from additional ICL examples, with performance gains primarily saturating at the 1-shot level. What do you think might be the reason for this? Additionally, why do you believe that the proposed VL-ICL offers a better evaluation of ICL capability compared to traditional VQA benchmarks, as the Figure 3(a) also reveals the same trend?
4. Some tables do not bolden the best performance number, such as Table 5.

### Questions
1. Some tables do not bolden the best performance number, such as Table 5.

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
This paper reveals the limitations inherent in the common practice of quantitatively evaluating VLLM in-context learning (ICL) via VQA and captioning, and then introduces a comprehensive benchmark (i.e., VL-ICL Bench) for multimodal in-context learning. The introduced VL-ICL Bench incorporates both image-to-text (captioning and VQA) and text-to-image tasks, and evaluated various facets of VLLMs including fine-grained perception, rule-induction, reasoning, image interleaving, fast concept binding, long context, and shot scaling. The authors benchmarks over 20 VLLMs and highlight their strengths and limitations.

### Strengths
+ The overall paper is well organized and easy to follow. 
+ The research problem (i.e., benchmarking the multimodal ICL capabilities of VLLMs) is quite valuable in VLLM communities. Comprehensive analysis experiments are provided to show the limitations of existing benchmarks.
+ The introduced benchmark covers multiple practical ICL tasks and assesses numerous VLLMs. Multiple discussions are provided to show the promising direction for future research.

### Weaknesses
 - Some texts are not consistent with the figures. For instance, in Line 159-160 and 224-225, the authors claim that the ICL exhibit more significant improvement on text-to-text benchmarks compared to image-to-text benchmarks. However, the differences between Figures 3a and 4 are marginal. These line charts show similar trends. Specifically, while both show an upward trend, the magnitude of improvement appears comparable, and the claim of 'more significant' improvement in text-to-text is not strongly supported by the visual evidence. A more nuanced discussion of the degree of improvement is needed.
- Some design choices are not clear. The authors want to show different trends of VLLMs on multimodal and LLM benchmarks in Figure 3 and 4. I am wondering why different models are evaluated? The rationale behind selecting specific models for each figure is not clearly articulated. It is unclear if the models in Figure 4 were chosen because they are known to exhibit strong ICL capabilities, or if there is another reason for the selection. This lack of clarity makes it difficult to interpret the results and understand the conclusions drawn from these figures.
- The data contribution of the proposed benchmark is somewhat weak, as all the data and annotations are collected from existing datasets. In addition, there is no dataset statics of the introduced VL-ICL Bench. It would be better to show the distribution of the data as well as the tested capabilities. Without detailed statistics, it is difficult to assess the diversity and representativeness of the benchmark, and to understand the extent to which it covers the various aspects of multimodal ICL.

### Questions
- The few-shot multimodal ICL typically helps to improve the performance out-domain or out-of-distribution tasks. I am wondering why this paper only focuses on VQA and captioning?
- Why the peak accuracy is used rather than average accuracy over all shots？
- In Lines 361-363, the authors claim that ‘we attribute this to difficulty of dealing with the larger number of images and tokens confusing the model and overwhelming the value of additional training data’. It there any evidence to support such statement?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces a comprehensive benchmark named VL-ICL Bench for assessing the capabilities of multimodal in-context learning (ICL). The suite includes a range of tasks involving both image and text inputs and outputs. The authors evaluate the performance of state-of-the-art vision large language models (VLLMs) on this benchmark, revealing their strengths and weaknesses across various tasks, and note that even the most advanced models, such as GPT-4, find these tasks challenging. The article hopes that the dataset will inspire future work on enhancing the in-context learning capabilities of VLLMs and inspire new applications that leverage VLLM ICL.

### Strengths
1. Point out the limitations of the common practice of quantitatively evaluating VLLM ICL through VQA and image captioning.
2. Propose a comprehensive benchmark suite of ICL tasks covering diverse challenges, including perception, reasoning, and so on.
3. It rigorously evaluates a range of state-of-the-art VLLMs on the benchmark suite and highlights their diverse strengths and weaknesses.

### Weaknesses
1. The evaluation seems too weak. For example, for the ICL tasks of image generation, the community might focus more on generating images based on complex instructions. For example, researchers in such fields prefer using VLMs to evaluate the generated images given complex instructions as described in [1].
2. The possible usage of this model is still unclear. There are two situations when we want to evaluate multi-modal tasks, but I think the proposed benchmark is not suitable for any situation. 

In the first situation, we evaluate the generation and understanding abilities separately, which is more reasonable nowadays because existing VLMs are usually good at one type of task even for the recent ones like [2], thus they prefer to be evaluated on benchmarks for specific targets.

In the second situation, for the models that could generate and understand in the same framework, it is better to evaluate them in more complex in-context-learning settings. For example, the input and output both contain images and texts. Only in the way the upper bound of the abilities of such models could be measured. However, this setting is not contained in this paper.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a comprehensive dataset, VL-ICL, for evaluating VLLM. Unlike previous datasets that primarily focus on tasks such as question answering, OCR, or image caption generation, this dataset takes into account the contextual learning capabilities of both image-to-text (I2T) and text-to-image (T2I) modalities. It assesses the in-context learning (ICL) abilities of a wide range of multimodal models and reflects on potential issues these models may face. Additionally, it summarizes some phenomena that might arise during multimodal contextual learning, offering valuable insights for future experiments and research in the multimodal field.

### Strengths
(1) Compared to previous image captioning or visual question answering tasks, this dataset introduces new tasks designed to assess multimodal contextual learning capabilities. This provides significant benefits for future model design, enhancing models' visual understanding abilities, and conducting comprehensive testing of multimodal models. Additionally, it includes detailed evaluations of few-shot language-to-image generation tasks.

(2) The paper thoroughly tests the contextual learning abilities of open-source VLLM with different architectures, backed by extensive experimentation.

(3) The paper documents and provides detailed explanations of a series of phenomena observed in vision ICL, offering insights for future research exploration.

### Weaknesses
(1) I believe this paper should expand on the impact of different ICD selections on ICL. There are already some papers that have demonstrated the role of ICD in ICL within VLLM.  Furthermore, in section 2.2 of the article, some phenomena related to multimodal ICL (mentioned in Section 2.2 :**For example, in captioning zero-shot VLLMs tend to produce more verbose captions than COCO ground-truth, and they learn to be more concise through ICL. Meanwhile, for VQA, there is a standard practice of evaluating based on string match between the ground-truth answer and the model-provided answer. For example, VizWiz has unanswerable questions, which some VLLMs answer with "I don’t know" which would not be string matched against a ground truth "Unanswerable". Some models thus learn about answer-formatting (e.g., preferred terminology; avoid using any preface or postface that may throw of a string match) from the context set. This is indeed a kind of ICL, but perhaps not what one expects to be learning in VQA. To validate this conjecture, we repeat the previous evaluation, but using soft matching to eliminate the impact of answer format learning.** ) have been previously discussed in several papers and thus the authors should refer to these studies.
- What Makes Good Examples for Visual In-Context Learning?
-How to Configure Good In-Context Sequence for Visual Question Answering
- Understanding and Improving In-Context Learning on Vision-language Models
- Exploring diverse in-context configurations for image captioning 
If you could test the impact of these sample selections within VL-ICL and include appropriate citations, I would consider raising the score.

(2) The paper's approach of using textual descriptions in place of images for ICL raises concerns. Relying on generated captions, even if algorithmically derived, might not fully capture the nuances of the original visual input. This substitution could potentially introduce biases or information loss, affecting the validity of the ICL evaluation. It is crucial to investigate the impact of these textual substitutions on the model's learning process. Specifically, if alternative models such as BLIP or GPT-4V were used to generate these captions, the risk of hallucination would be a significant concern, further questioning the reliability of the textual replacements. Additionally, the paper should explore the impact of removing images from the ICD altogether, retaining only the query and answer pairs, to evaluate the extent to which the models rely on visual input for ICL.

### Questions
(1) I noticed that the number of dataset samples/test samples is relatively small. Does this dataset suffer from a significant issue of imbalanced class sample distribution?

(2) In section 4.3, you mentioned an approach where language text is used to replace images for ICL inference. How exactly was this implemented? Did you directly remove the images from the ICL setup and only keep the questions and answers, or did you generate captions for the images to perform contextual learning inference? Or was another method used?

(3) Can you explore the impact of different model architectures on ICL abilities? In your experiments, there are models with cross-attention architectures similar to Flamingo, as well as models like LLAVA that embed visual features into the text embedding space. Does this have a significant impact on the ICL performance of the models?

### Soundness
3

### Presentation
3

### Contribution
3
