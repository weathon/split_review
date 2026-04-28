# Does Spatial Cognition Emerge in Frontier Models?

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
Not yet. We present SPACE, a benchmark that systematically evaluates spatial cognition in frontier models. Our benchmark builds on decades of research in cognitive science. It evaluates large-scale mapping abilities that are brought to bear when an organism traverses physical environments, smaller-scale reasoning about object shapes and layouts, and cognitive infrastructure such as spatial attention and memory. For many tasks, we instantiate parallel presentations via text and images, allowing us to benchmark both large language models and large multimodal models. Results suggest that contemporary frontier models fall short of the spatial intelligence of animals, performing near chance level on a number of classic tests of animal cognition.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the SPACE Benchmark, designed to evaluate spatial cognition capabilities in large models by focusing on both large-scale and small-scale spatial cognition. Large-scale spatial cognition pertains to environmental reasoning, where the environment stays constant while the viewer’s perspective shifts. Conversely, small-scale spatial cognition involves the perception and imagery of changing spatial states of objects, with a fixed viewer’s perspective. The benchmark comprises 15 tasks distributed across image-based and text-based experiments, designed to test VLMs and LLMs. Each task contains questions between 30 and 100+. The findings indicate that current models underperform relative to human-level reasoning across various spatial tasks, suggesting that these models have yet to achieve robust spatial reasoning capabilities. Notably, some models, such as GPT-4 and GPT-4v, demonstrate superior performance in text-only tasks compared to multimodal tasks.

### Strengths
1. It is interesting to test both VLM and LLM models’  large scale 2D and 3D spatial reasoning abilities using three scenarios: Ego Image/ Video, Bird’s Eye View (BEV) images, and BEV text. It also allows for the assessment of models across different modalities, including textual descriptions, single images, and video content. This design reflects the complexity of real-world spatial understanding and demonstrates the comprehensive nature of the evaluation.
2. This article uses interactive tasks for route retracing and shortcut searching where the model receives the current observation, decides which action to take, and receives corresponding updated observations

### Weaknesses
A. Providing specific details such as the resolution of the videos and images used in the experiments would be better because models might take in different sizes of input images, therefore model performance can vary significantly based on input resolution. if an image is downsampled incorrectly, it may disrupt the original aspect ratio, potentially impairing the performance in tasks that require precise spatial reasoning, such as distance and direction estimation. This issue might partially explain why LLMs outperform VLMs in some scenarios.

To better explain this, could try to
	1. Specify the exact resolutions used for images and videos in their experiments
	2. Discuss how they handled any resizing or aspect ratio changes when preparing inputs for different models
	3. Consider running an ablation study with different image resolutions to quantify the impact on performance, especially for tasks like distance estimation

B. Only two VLMs are tested for image relevant tasks. And those two models even belong to the same family (GPT). I would recommend to test more SOTA VLMs to validate your conclusions.
C. As I stated in the following questions, the images used for experiments might be too small to draw a reliable conclusion.

### Questions
A. In the direction estimation task, take Figure 6 for example, pretend that you are standing below landmark F and facing F, while N is right above F. Why does the angle become 78 degrees? The two landmarks seem to be almost on the same line.

B. The article omits some details of data processing and requires greater clarification. For instance:
	1. In the section on Large-Scale Spatial Cognition, while the Bird’s-Eye View (BEV) is mentioned as covering 2.5m x 2.5m surrounding area, the dimensions of both the 2D and 3D views,  the duration of videos as well as number of sampled images of each video for the Ego image are not provided. It might affect the models' performance if the sampled images are over dense and include too much redundancy or images are too sparse therefore missing key frames containing landmarks.
        2. For BEV text, the authors state that they “carefully select the encoding to ensure compatibility with text tokenizers” but do not detail this process. How is this encoding achieved, and how is the dimension of the text array determined? It would be helpful to know how many different array dimensions were tested to understand the effect of text encoding choices. Additionally, since LLMs reportedly perform better with BEV text, could this be due to the much smaller dimensionality of text arrays compared to BEV images? 
	3. In Table 3, only the number of questions is presented per task, without image counts. Although most tasks include 30-50 questions, there appear to be fewer than 10 images for some tasks, which limits the robustness of any conclusions drawn. To strengthen the study’s validity, I recommend providing the exact image counts per task and ensuring a sufficient number of images for each task. This would enhance the reliability of conclusions and support a more balanced dataset for each task.

### Soundness
2

### Presentation
2

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
A benchmark is introduced for evaluating spatial cognition in LLMs and VLMs, comprising both large-scale spatial reasoning tasks (e.g., navigation) and small-scale spatial reasoning tasks (e.g., mental rotation). The results indicate that both VLMs and LLMs perform well below human participants on these tasks, indicating weak spatial reasoning abilities in these models.

### Strengths
- The proposed benchmarks are very extensive, covering different types of spatial cognition with many tasks and input modalities.
- The paper is well written and many details are provided on the evaluation methodology, including detailed prompts and model settings.
- The topic investigated in this paper is an important one, with many implications for real-world use of foundation models.

### Weaknesses
Although the benchmark appears to be well designed, there are a number of previous works that address very similar questions, and the results are not particularly surprising. Both Valmeekam et al. (2023) and Momennejad et al. (2023) have shown that LLMs are very poor at navigation and planning tasks (i.e., large-scale spatial cognition), and studies from both Yamada et al. (2024) and Ivanova et al. (2024) and have already shown that LLMs have a limited ability to reason about spatial relations. These works are not cited, and there is no discussion of how the proposed benchmark goes beyond previous studies of spatial reasoning in these systems.

### Questions
Previous work on spatial reasoning in LLMs should be cited, and the paper should address how the proposed benchmark goes beyond the already existing benchmarks, and what new information we have learned about spatial reasoning in LLMs.

### Soundness
2

### Presentation
2

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
This work develops SPACE, a benchmark for systematic evaluation of spatial cognition in foundation models, vision-language or language only. These are a large variety of tasks designed to test spatial cognition taken from various places within the cognitive science literature. They separated the tasks into two categories - "large-scale" which are testing the development of a robust cognitive map of an entire environment and "small-scale" which are testing targeted spatial relationships between specific objects in various contexts (mental rotation, putting pieces of a board together, spatial addition, etc). The large-scale tasks have an egocentric visual representation of the task, an allocentric "birds eye view" visual representation, and an allocentric text-only representation. The small-scale tasks have a vision vs. text version of the tasks. They evaluate various popular closed models (e.g. GPT4v) as well as various open-source models (Llama3), both multimodal and language-only models. Performance was generally above chance but far below human performance.

### Strengths
* Very timely topic. 

* It is a quite impressive set of tasks that really engaged with the literature on spatial reasoning. The translation of spatial reasoning tasks to text only is an especially nice contribution, because it allows for the evaluation on text-only models. I think the benchmark will be immediately valuable to the community. 

* Comprehensive evaluation. Lots of models were used, which really gives us an idea as to how the current landscape of models performs at tasks like these.

### Weaknesses
1. The authors took the best first step in evaluating a capability that humans have (spatial cognition), which is to directly take tasks that have been used in cognitive science to test this capability in humans. However, these are *tests that were designed for humans specifically*, not Large (vision)-Language Models. And I think this would definitely have implications on the results. For example, vision encoders like CLIP are trained on a lot of ImageNet-style object image data and so a model using CLIP as a visual encoder may be less used to, for example, the egocentric observations or BEV images used in the large-scale studies. I don't know if the specific composition of GPT4v's or GPT4o's image training data is public knowledge, but I think the larger point still stands. This doesn't mean what the authors did is incorrect - it is a good first step and valuable contribution towards understanding spatial capabilities in these models. However, I think more work will need to be done in the future to *ensure these kinds of tasks are presented to the model in a way that is ecological.* This is really common in animal behavioral paradigms. Often when animal researchers are testing a capability known to exist in humans, the original paradigms are modified so that the task makes enough sense to the animal and is actually testing the desired capability. For me to raise the score above threshold, *I would like the authors to engage with this point a little more than what's currently written in the paper.* 

2. I think this is a more minor weakness. There are a very large number of tasks and each of them are described independently. However, there isn't much discussion on what features are shared across the different tasks. I think the paper would be a lot more stronger if the authors were able to pick out specific features of spatial cognition that are salient across many of these tasks and identify which tasks test which features. If the paper was structured more like: "we identified 4 features of spatial cognition common to many tasks in the literature: A, B, C, and D. Here are some tasks from the literature. The mental rotation task tests A and B, perspective taking tests B and C, etc." Currently the shear number of tasks (while impressive) is overwhelming, and looking at performance across all of them is harder to interpret. I think this would make evaluation on SPACE more digestible, because you'd be able to diagnose which aspects of spatial cognition your model succeeds at and which aspects your model fails at.

### Questions
* Related to weakness 1, have you tried egocentric text representations? For a given location and direction of the environment, you could have a way to parse the egocentric image observation into a textual description (e.g. "there is a landmark with a picture of a dog on the left wall and a deadend wall directly in front of you. On both your left and right sides, there are potential paths leading elsewhere"). This kind of representation may be more ecological to some of these models. This could apply to the small-scale tasks (corsi block tapping,  spatial addition, cambridge spatial working memory) with grid inputs as well (e.g. "Row 1 column 2 has a blue, row 2 column 5 has a red,...") Even if it's a small change in how the input is represented, a change in performance would be very informative.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper a comprehensive benchmark SPACE that systematically evaluates spatial cognition in large language models (LLMs) and vision language models (VLMs). SPACE divides into large-scale spatial cognition tasks and small-scale spatial cognition tasks. Large-scale spatial cognition is at the environment level and the goal is to test whether LLMs and VLMs can build spatial representations to reason about and navigate in the environment. Small-scale spatial cognition tasks test models' ability to perceive, imagine, and mentally transform objects or shapes in 2D and 3D scenarios. The experimental results on frontier models (e.g. LLMs, VLMs) show that these frontier models has much lower capability in spatial cognition when compared to humans, and suggest frontier models that have acquired advanced skills may have a fundamentally different form of intelligence from humans and animals because of the failure in basic spatial cognition.

### Strengths
**Originality**
- While there's an increasing interest in spatial cognition for frontier models, there are not enough datasets to evaluate them systematically. The proposed benchmark SPACE is novel in terms of its comprehensiveness and diversity in tasks.

**Quality**
- SPACE is a very comprehensive and diverse benchmark. The large-scale spatial cognition tasks cover 5 tasks. The small-scale spatial cognition tasks cover 10 tasks. All 15 tasks are based on prior studies in cognitive science, which ensures plausibility in psychology and cognitive science domains. The input of the tests can be pure language or multimodal, which makes the benchmark suitable for evaluation on LLMs and VLMs. All experiments have human performance as the reference, which makes it easier to compare frontier models with humans.

**Clarity**
- The paper is well-written and easy to follow. Figures are helpful for understanding each task. The gray coloring of the results indicating they are below 50% of human performance makes the results very interpretable.

**Significance**
- This paper is valuable to the research community of large language models since it reveals the shortcoming of basic spatial cognition for these frontier models. Additionally, it could make the research community in both artificial intelligence and cognitive science rethink about the difference in intelligence between humans and these models. More specifically, it may indicate only casual language modeling will not lead to the human intelligence without sufficient embodiment in the training process. On the other hand, the results show that while these frontier models are surpassing humans on many tasks, but still lack basic cognition on simple tasks. These findings are insightful as researchers can study (1) How do models skip basic cognition to reach higher cognition? (2) Does skipping basic cognition make the frontier model unreliable and untrustworthy?

### Weaknesses
 **Lack of experiments to demonstrate prompts can be understood by frontier models**
- Most results are around chance level accuracy. There are two possible conclusions: 
1. Models have weak spatial cognition. 
2. Frontier models have better spatial cognition internally, but it doesn't show externally because of the unfamiliarization of the multimodal and text-only prompt formats.

It would be more rigorous if there are some experiments show that these formats of prompting can be understood by these frontier models (e.g. achieving high accuracy in some easier tasks with the same format of prompting).

**Unclear use of Chain-of-Thought (CoT) techniques in prompting**
- Chain-of-Thought (CoT) prompting techniques [1] are known for improving language model in solving tasks as it allows LLMs to have some reasoning steps before arriving at the final answer. CoT techniques are not mentioned in the main paper, except "Think step by step" prompts in the appendix, but it is unclear which tasks use the CoT, which doesn't. If some tasks use CoT, it should be listed separately to the results table as a comparison to investigate whether reasoning steps strengthen the frontier models.

### Questions
**Questions**
- The Discussion Section mentions that spatial cognition is considered to be a prerequisite for higher cognition and frontier models can acquire tasks requiring higher cognition like olympiad geometry problems, but lack basic spatial cognition as indicated in the results. Is there any study in psychology or cognitive science show that basic spatial cognition is related to solving geometry problems? 

- Trinh et al [1] trained the neural language model for geometry theorem proving from scratch using their large-scale synthetic data to guide the symbolic deduction engine. Therefore it seems not very clear that whether their model can perform better on spatial cognition tasks with language-heavy prompting because their model may be specialized to theroem proving while lacking language understanding and generation skills when comparing to state-of-the-art language models.

*References*

[1] Trinh, Trieu H., et al. "Solving olympiad geometry without human demonstrations." Nature 625.7995 (2024): 476-482.

### Soundness
4

### Presentation
3

### Contribution
3
