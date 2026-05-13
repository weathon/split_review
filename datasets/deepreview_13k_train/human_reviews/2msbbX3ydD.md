# Ferret: Refer and Ground Anything Anywhere at Any Granularity

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
\vspace{-2mm}
We introduce Ferret,
a new Multimodal Large Language Model~(MLLM) capable of understanding spatial referring of any shape or granularity within an image and accurately grounding open-vocabulary descriptions. 
To unify referring and grounding in the LLM paradigm, \ferret employs a novel and powerful hybrid region representation that integrates discrete coordinates and continuous features jointly to represent a region in the image. To extract the continuous features of versatile regions,  we propose a spatial-aware visual sampler, adept at handling varying sparsity across different shapes. Consequently, \ferret can accept diverse region inputs, such as points, bounding boxes, and free-form shapes. 
To bolster the desired capability of \ferretns, 
we curate GRIT, a comprehensive refer-and-ground instruction tuning dataset including 1.1M samples that contain rich hierarchical spatial knowledge, with 95K hard negative data to promote model robustness.
The resulting model not only achieves superior performance in classical referring and grounding tasks, but also greatly outperforms existing MLLMs in region-based and localization-demanded multimodal chatting. Our evaluations also reveal a significantly improved capability of describing image details and a remarkable alleviation in object hallucination.\blfootnote{$^\text{\faApple}$Work done during an internship at Apple. $^\dagger$Equal contribution.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the challenge of training a Multi-modal Large Language Model to accurately interpret input visual references, such as points, bounding boxes, free-form shapes, with respect to the image (referring) and ground the output text to relevant image regions (grounding). The authors propose a unified framework, called Ferret, for jointly solving the visual referring and grounding problem. They provide a new curated dataset (GRIT) that consists of existing and newly collected data for training, as well as a new benchmark (Ferret-Bench). In the evaluation section, the authors show that the proposed method either exceeds (on the Ferret-Bench and grounded captioning) or is on par with the concurrent SOTA methods such as Shikra. In addition, the proposed method can accept a variety of user input on images as part of referring expressions, including scribble and freeform shapes, in addition to the traditional points and bounding boxes. However, the way how these different visual reference types are processed is conceptually similar to the Visual Sampler proposed in SEEM (Zou et al., 2023), and performs similarly despite the added complexity.

### Strengths
S1. This seems to be one of the first MLLMs to support a variety of visual reference types, such as point, box, scribble, polygons, and masks. 

S2. The authors provide a curated dataset called GRIT that consists of existing datasets and newly collected data for training MLLMs with visual referring and grounding capabilities.

S3.  The authors provide a new benchmark, Ferret-Bench, which covers two new types of evaluation task for visual referencing (description and reasoning) in addition to the conversation grounding task. The key difference to existing benchmarks such as RefCOCO+, RefCOCOg, or PointQA [a] is that the questions include visual references (in forms of bounding boxes). For example, “What is the purpose of the object [x1 y1 x2 y2]?”
 - [a] Point and Ask: Incorporating Pointing into Visual Question Answering, Mani et al., 2022

S4. The paper provides comparison with the SOTA methods and the concurrent methods in the evaluation section.

### Weaknesses
W1. The paper omits any discussion on the limitations or potential failure scenarios of the proposed method.

W2. The significance of the proposed Spatial-Aware Visual Sampler is minimal. The idea of sampling the visual features over the grid is in the same spirit as the Visual Sampler in SEEM (Zou et al., 2023), although the details of how the points features are aggregated and pooled are different. Performance-wise, the Spatial-Aware Visual Sampler is shown to be only marginally better than the Visual Sampler in SEEM as shown in the ablation study section.

W3. While the idea of jointly solving referring (with explicit visual cues, such as markings on the image) and grounding in one unified framework makes sense as the two tasks are interrelated, this idea was also explored in concurrent works (Chen et al., 2023a) and (Peng et al., 2023).

### Questions
Q1. It appears that the proposed method significantly outperforms Shikra on Ferret-Bench, but not much on existing datasets. I wonder if the authors can explain why.

Q2. I think the quality of writing could be further improved. For example, it is not clear to me what the authors are trying to imply by “First of all, we choose MLLM as the bedrock of Ferret due to their powerful vision-language global understanding capability”. I am guessing that they wanted to say that the Ferret is built on top of existing MLLMs to leverage their powerful vision-language capability?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Ferret, a Multimodal Large Language Model (MLLM) capable of understanding spatial referring within an image and grounding open-vocabulary descriptions. The paper also introduces the dataset GRIT with 1.1M samples and an additional 130K hard negative data.

Ferret includes several components:
1. A powerful hybrid region representation integrating discrete coordinates and continuous features to represent image regions.
2. A spatial-aware visual sampler for handling various region shapes and extracting continuous features.
3. Integration with LLM for referring and grounding tasks.

Ferret achieves superior performance in classical referring and grounding tasks and outperforms existing methods and it shows improved capability in describing image details and reduces object hallucination.

### Strengths
1. The paper is presented very well. 
2. The paper shows a reasonable motivation that humans inherently possess the ability to learn from one task and generalize to another between referring and grounding. This underscores the essential need to unify referring and grounding processes.
3. The hybrid region representation and spatial-aware visual sampler make the framework flexible to take different form of region definition.
4. The framework shows a good way of utilization of Large Language Model.
5. Contribution of the dataset.

### Weaknesses
1. No open source code for the code and dataset. I would raise the soundness score if code and dataset are open, either attached in the supplementary or released in the public repo.
2. The hierarchy of the dataset is a bit complicated. This may not be practical for costume dataset.
3. Very engineering paper, extensive work, but not much scientific novelty.

### Questions
1. Table 5 shows that mutual benefits of grounding and referring. From the results, it seems grounding task can help more for referring task than the other way around. How to interpret this effect?
2. For section 4.2, how to evaluate quality of the generated data from ChatGPT and GPT4?
3. You mensioned in the Ferret-Bench is via GPT4 as a judge. But some of the data are collected from GPT4, is a reason it is better than all other models in Table 7.
4. Can chatgpt take multimodal input? Since when you collecting dataset via LLM, the author mentioned they use ChatGPT first and then use GPT-4 to refine it. I am wondering how ChatGPT can take image as input.

It is extensive of work. I would like to raise my score if the questions are addressed and the code and data are public.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a large multimodal model Ferret, which, compared with prior works, is especially good at referring and grounding. In Ferret, they propose a hybrid region representation and a novel spatial-aware visual sampler to represent the visual and regional input. To train Ferret, they creat GRIT, a large-scale ground-and-refer instruction tuning dataset. They also introduce Ferret-Bench to evaluate the grounding, referring, and reasoning capabilities of LMMs.

### Strengths
1. The proposed GRIT dataset is meaningful to the vision and language research. 
2. The proposed Spatial-Aware Visual Sampler and Hybrid Region Representation are well-motivated. 
3. The experiment results show the better capabilities of the trained model on multiple referring and grounding tasks and validate the effectiveness of the spatial-aware visual sampler module.

### Weaknesses
1. The ablation on hybrid region representation is missing.

2. Not a strong weakness, but whether the model performs well on non-referring or grounding tasks needs more validation. E.g. VQA_v2, MME, general captioning, etc. And it seems the caption evaluation is not as good as InstructBLIP.

### Questions
1. Is the evaluation on Flickr30k grounded caption fine-tuned or zero-shot?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
