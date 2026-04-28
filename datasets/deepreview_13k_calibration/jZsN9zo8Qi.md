# Learning Interleaved Image-Text Comprehension in Vision-Language Large Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
\label{abstract}
The swift progress of Multi-modal Large Models (MLLMs) has showcased their impressive ability to tackle tasks blending vision and language.
Yet, most current models and benchmarks cater to scenarios with a narrow scope of visual and textual contexts.
These models often fall short when faced with complex comprehension tasks, which involve navigating through a plethora of irrelevant and potentially misleading information in both text and image forms.
To bridge this gap, we introduce a new, more demanding task known as Interleaved Image-Text Comprehension (IITC).
This task challenges models to discern and disregard superfluous elements in both images and text to accurately answer questions and to follow intricate instructions to pinpoint the relevant image.
In support of this task, we further craft a new VEGA dataset, tailored for the IITC task on scientific content, and devised a subtask, Image-Text Association (ITA), to refine image-text correlation skills.
Our evaluation of four leading closed-source models, as well as various open-source models using VEGA, underscores the rigorous nature of IITC.
Even the most advanced models, such as Gemini-1.5-pro and GPT4V, only achieved modest success.
By employing a multi-task, multi-scale post-training strategy, we have set a robust baseline for MLLMs on the IITC task, attaining an $85.8\%$ accuracy rate in image association and a $0.508$ Rouge score. These results validate the effectiveness of our dataset in improving MLLMs capabilities for nuanced image-text comprehension. Project page: \url{https://zhourax.io/VEGA/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Long-context interleaved image-text comprehension is an important skill required to read scientific papers, for example. Humans can do this well, but characterization of this ability is understudied. This paper introduces a multimodal task called Interleaved-Image-Text Comprehension which requires answering a question using interleaved image and text and grounding the answer in one of the in-context images. The authors develop a dataset called VEGA to evaluate models on this task and auxilliary simpler task called image-text association. They evaluate multiple frontier LLMs and some open LLMs on the task, and develop a training strategy which they show improves performance on this task.

### Strengths
- There are no resources (as far as I know of) to study and characterize _long-context_ interleaved image-text comprehension or empirical studies of this comprehension ability. This is one of the first.
- The experimental evaluation is broad, covering multiple vision language models including a mix of closed source LLMs and open source LLMs.
- I especially appreciate the honest of the authors in showing that training on Vega _does not_ in general improve performance on other VQA tasks.

### Weaknesses
 - The construction method of the dataset seems a bit artificial.
- I don't see analyses of how the number of images / context length affects accuracy. In general, I feel like important analyses are not present. There are no "slices" in the dataset to sanity check that expected properties hold. For example, I would expect that as context increases, accuracy falls. If I did not see this, I would be suspicious of the construction method. This is just an example. My main point is that the dataset and how the properties of the dataset affect evaluation are not analyzed enough or perhaps not explained in the text.
- I am not convinced by the proposed training method. It is not really motivated or explained well in the text, and there is no discussion (as far as I can tell, but it is very possible I have missed something) on how it relates to other similarly named methods in the literature for "multi-scale training".

### Questions
Please see the weaknesses section. Most of the weaknesses are minor. The weakness I care about and the one where an author response would cause me to increase my rating is "analyses". What analyses have the authors done on how properties of the dataset (e.g. number of images, context length, etc) affect the performance of MLLMs? Also, can the authors discuss why there are multiple evaluation metrics and what each of them signify?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel task, Interleaved Image-Text Comprehension (IITC), which evaluates models' capabilities to handle complex interactions in lengthy multimodal contexts. The authors present the VEGA dataset specifically designed for the IITC task, featuring up to 8,000 tokens and 8 images. The paper also benchmarks several models on this task, including proprietary and open-source options, and demonstrates the benefits of fine-tuning Qwen-VL-Chat for IITC. The results show that even state-of-the-art models face challenges in this setting, highlighting the dataset's rigor and the task's demands.

### Strengths
The introduction of a challenging new task (IITC) with extensive multimodal input length sets a unique standard in evaluating models' interleaved image-text comprehension. The proposed VEGA dataset is extensive, comprising 295k high-quality, multi-turn entries, with a curated test set of 700 questions to assess models' nuanced comprehension abilities.

The benchmark evaluates both proprietary and open-source models, showing that current models, even at their best, are still only moderately successful in IITC tasks. Fine-tuning Qwen-VL-Chat leads to meaningful improvements, establishing a strong baseline for future models.

The dataset structure, including partitions for 4k and 8k token contexts, is well-conceived and allows for detailed performance analysis. Including specific references to image indices in responses (e.g., '[Picture 2](Figure. 3)') is a thoughtful design choice, aiding interpretability in output.

### Weaknesses
Presentation: Figures, particularly Figure 1 and Figure 2, are too small, making the text nearly unreadable without significant zoom. This compromises the clarity and accessibility of the paper's visual aids.

Test Set Generalizability: The test set, created through a process similar to the training data generation, may inadvertently advantage trained models by being in-distribution. Introducing an additional test set, created independently or using different datasets, could strengthen the evaluation by ensuring generalization beyond the training data distribution.

### Questions
Would you consider adding an out-of-distribution test set to further evaluate generalization capabilities?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Interleaved Image Text Comprehension (IITC) task and establishes the corresponding dataset, VEGA. Compared to existing visual language tasks and datasets, IITC and VEGA have the following unique features: (1) the interleaved images and text input; (2) multiple images input; (3) the task requires the LMM to determine which image is relevant to the question; (4) the input includes image and text information that is irrelevant to the question. Particularly, the latter two features are lacking in previous tasks and datasets.

By benchmarking existing mainstream close-source and open-source MLLMs on VEGA, it was found that the performance of these SOTA  models is not ideal, thus confirming the challenging nature of the IITC task.

Furthermore, this paper also finetunes Qwen-VL-Chat using the train split of VEGA and adopts a multi-scale, multi-task training strategy, laying a solid baseline for subsequent collaborative research.

### Strengths
- This paper introduces the Interleaved Image Text Comprehension (IITC) task and creates the corresponding dataset VEGA. IITC and VEGA have the following unique features: (1) the interleaved images and text input; (2) multiple images input; (3) the task requires the LMM to determine which image is relevant to the question; (4) the input includes image and text information that is irrelevant to the question.
These features reflect the normal state of human reading and understanding of image-text materials and are essential for a multimodal AGI system. Existing visual language datasets often lack these features, especially the latter two. Therefore, IITC and VEGA fill this gap to some extent and help to advance the technical progress of the research community in this direction.

- The overall design of the dataset is scientific and reasonable, the construction process is detailed, and the provided statistical information is very convincing. The adopted multi-scale, multi-task training strategy also appears reasonable and credible.

- The main body of the paper is well-structured and written in a clear and concise style, making the article easy to read and understand.

### Weaknesses
 - All training-related experiments in the paper were conducted solely on the Qwen-VL-Chat model and did not involve other open-source foundation VL models that support interleaved text-image processing. Therefore, the training strategies proposed in this paper and the conclusions from its ablation study have not been sufficiently validated for generalization across other models. Specifically, the multi-scale training strategy's effectiveness might be highly dependent on the base model's architecture and pre-training data, and it's unclear if the observed improvements would hold for models with different inductive biases or pre-training procedures. For example, models pre-trained on datasets with a stronger emphasis on interleaved image-text data might not benefit as much from this strategy, or might require different scaling factors.
- The article has some issues with formatting and layout, such as the text in some images being too small, which affects normal reading (e.g., Figure 1). Additionally, the layout of the appendix also needs further optimization.

### Questions
- During the construction of the VEGA IITC subset, particularly in the answer modification step (see line 305), the authors adjusted the answers from the original dataset (SciGraphQA). Was this modification based on rules (such as keyword matching) or aided by an LLM (e.g., prompt GPT)? Additionally, were the modified answers subjected to quality checks and evaluations, such as through manual sampling inspection and calculating the pass rate?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces VEGA, a dataset designed for interleaved image and text understanding. It also proposes a multi-modal large language model (MLLM) baseline fine-tuned on this dataset. The fine-tuning process uses a multi-scale method, gradually incorporating more complex samples. The model is fine-tuned for two tasks in the VEGA dataset: Interleaved Image-Text Comprehension (IITC) and Image-Text Association (ITA). It demonstrates improved performance on both tasks.

### Strengths
1. Proposes VEGA, a complex dataset specifically crafted for multi-image understanding, challenging MLLMs with interleaved image and text contexts.

2. Establishes two tasks, Interleaved Image-Text Comprehension (IITC) and Image-Text Association (ITA), setting new benchmarks for interleaved image understanding.

3. Demonstrates that the multi-scale training method effectively improves performance on the ITA task.

### Weaknesses
1. Key baseline models such as LLaVA-interleaved and InternVL2 are missing, limiting insight into comparative performance. Specifically, the absence of these models makes it difficult to assess the true novelty and effectiveness of the proposed approach against state-of-the-art methods in interleaved image-text understanding. The performance gains reported might be less significant when compared to these established baselines.

2. Similar datasets like SlideVQA, MMLongBench-Doc, DUDE, and DocVQA are not discussed or tested, which could demonstrate the generalization of the fine-tuned model. This lack of evaluation on related datasets raises concerns about the model's ability to generalize beyond the specific characteristics of the VEGA dataset. It is unclear if the model's performance gains are specific to VEGA or if they translate to other similar tasks and datasets.

3. The ITA task may have limited real-world applicability, as not all text paragraphs have corresponding images. In contexts like research papers, only a subset of text relates to specific images, and filtering irrelevant text often implies inferred relevance between remaining text and images. This raises questions about the practical utility of the ITA task and whether it truly reflects real-world scenarios where image-text associations are often more nuanced and less direct.

4. The font in Figure 1 is too small and should be increased for better readability.

### Questions
Other than the weaknesses:

1. Is multi-scale training still effective when not used for multi-task training?
2. In Table 4, what is the model’s performance when trained only on the ITA task with and without multi-scale training?

### Soundness
3

### Presentation
2

### Contribution
2
