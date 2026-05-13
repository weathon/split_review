# Delving into LLMs’ visual understanding ability using SVG to bridge image and text

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Large language models (LLMs) have made significant advancements in natural language understanding. However, through that enormous world model that the LLM has learnt, is it somehow possible for it to understand images as well? This work investigates this question. To enable the LLM to process images, we convert them into a representation given by Scalable Vector Graphics (SVG). To study what the LLM can do with this XML-based textual description of images, we test the LLM on three broad computer vision tasks: visual reasoning, image classification under distribution shift, and generating new images using visual prompting. Even though we do not naturally associate LLMs with any visual understanding capabilities, our results indicate that the LLM can indeed do a pretty decent job in many of these tasks, potentially opening new avenues for research into LLMs ability to understand images.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They use Scalable Vector Graphics for using LLM for image understanding. The authors provide various experiments, including both discriminative and generative visual understanding tasks.

### Strengths
1. **Experimental Rigor:** The authors present a comprehensive suite of experiments in the domain of visual understanding and reasoning that effectively leverages the combination of Scalable Vector Graphics (SVG) with large language models (LLMs). The breadth and depth of the experimental design are commendable and provide valuable insights into the capabilities of LLMs in processing vector-based graphic representations.

2. **Robustness to Distribution Shifts:** A significant strength of the paper is the demonstration of the robustness of the LLM + SVG approach under conditions of distributional shifts. 

3. **Clarity and Coverage of Related Works:** The paper is well-articulated, presenting its concepts and findings in a manner that is accessible to readers. Moreover, the authors have done a thorough job in situating their work within the context of existing literature. They have effectively covered pertinent related works.

### Weaknesses
1. **Component Originality:** While the experiments are detailed, the novelty of the individual components used within the work is unclear. The application of Scalable Vector Graphics (SVG), Large Language Models (LLMs), the dataset selection, the tasks, and the chosen evaluation metrics all appear to be repurposed from existing literature without significant innovation or new application. For a stronger contribution, the authors could benefit from integrating at least one novel element or a unique combination of these elements that distinguishes this work from prior studies.  


2. **Source of Performance Discrepancy:** The comparative results between LLM+SVG and CNN+PNG in the first experiment are intriguing but lack a clear explanation. The performance gap could be attributed to differences in input representation or model architecture, among other factors. An in-depth ablation study could help isolate the impact of each component. Furthermore, the disparity in model sizes (e.g., GPT-4's size relative to that of a CNN) is a confounding variable that merits consideration. To convincingly argue the advantages of using SVG for image representation in LLMs, the authors should compare SVG with alternative representations using the same underlying model architecture, such as GPT-4.  


3. **Dataset and Task Relevance:** The chosen dataset and task do not seem to reflect complex real-world scenarios and may inherently favor SVG representations due to their structured nature. This could introduce a bias towards the advantages of SVG in image understanding tasks that focus on structural rather than fine-grained details. The authors would enhance the robustness of their findings by including a broader range of tasks with varying degrees of complexity and realism to demonstrate the efficacy of SVG representations across different contexts.  


4. **Methodological Limitations:** The exploration of image understanding through LLMs is indeed crucial; however, the analysis presented in this work is constrained by its reliance on existing methodologies. The absence of innovative input representations, model adaptations, or new evaluation benchmarks suggests a missed opportunity for advancing the field. To forge a more impactful contribution, the authors should strive to develop and introduce novel methodologies or significantly adapt existing ones to the specific challenges of image understanding through LLMs.

### Questions
Refer to part of Weaknesses.

### Soundness
2 fair

### Presentation
3 good

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
The paper explores the potential of Large Language Models (LLMs) to understand and process images by converting them into Scalable Vector Graphics (SVG), which can be represented as an XML-based textual description. The LLM's abilities are tested across three vision tasks: visual reasoning, image classification under distribution shifts, and generating new images based on visual prompts. The results show that the LLM has a reasonable ability to perform these tasks, especially compared with some expert models.

### Strengths
1. The use of SVGs to turn images into text is an innovative way of exploiting the potential of LLMs for image processing tasks.
2. The paper conducts both qualitative and quantitative evaluations over a variety of visual understanding tasks providing deep insights into the LLMs' image understanding capabilities. The results indicate that LLMs can perform well even when there are distribution shifts in visual data, demonstrating robustness. The demonstration of LLMs' ability to generate and edit images based on chat-based feedback is particularly promising and marks a significant advancement.

### Weaknesses
1. The SVG representation may not capture all the nuances of an image. It is yet unclear how well this method would generalize to more complex images or visual tasks.
2. The issue raised in the introduction about whether LLMs can learn world models without grounding in physical interaction and visual perception remains unaddressed. A comparison of LLMs' performance using SVGs with traditional vision-based models could have provided more context about the relative effectiveness of this approach.

### Questions
1. How well do SVG representations capture complex images? Could you provide instances or examples where this approach has limitations?
2. Whether the format, sequence, or other characteristics of textual descriptions in Scalable Vector Graphics (SVG) will affect their subsequent task performance.
3. What could be the potential impact if a minor percentage of errors into the representation of SVGs is introduced?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the capability of pre-trained LLM in understanding images through converting images into readable text via SVG. The authors evaluate both discriminative and generative visual understanding tasks including image classification, image generation and editing.

### Strengths
1. The study of whether LLMs, which have never seen visual data, can understand and reason about images is interesting and novel.
2. This paper utilizes SVG to convert images into structured XML codes, which serves as a bridge to apply the analytical strengths of LLMs to the visual domain.
3. This paper evaluates both discriminative and generative visual understanding tasks of LLMs, and draws some interesting conclusions, which can be inspiring.

### Weaknesses
1. For the evaluation of Multimodal LLMs, the authors only experiment on LLaVa and conclude that "This behavior underscores the limitations of current large multimodal models in structured and sophisticated reasoning.", which is not rigorous. The authors should evaluate more Multimodal LLMs such as BLIP-2, InstructBLIP, MiniGPT-4,mPLUG-Owl, etc.
2. The data for the evaluation of both the discriminative and generative visual understanding tasks are relatively simple. How does the LLM perform with SVG representations on more complicated images? Since the authors also mention that SVG is not effective in handing photographic content, using SVG with LLMs to tackle visual tasks may not be effective enough.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
