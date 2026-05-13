# CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Vision-Language Models (VLMs) have shown broad effectiveness due to extensive training that aligns visual inputs with corresponding language responses. However, this conclusive alignment training causes models to overlook essential visual reasoning, leading to failures in handling detailed visual tasks and producing unfaithful responses. Drawing inspiration from human cognition in solving visual problems (e.g., marking, zoom in), this paper introduces Chain of Manipulations, a mechanism that enables VLMs to tackle problems step-by-step with evidence. After training, models can solve various visual problems by eliciting intrinsic manipulations (e.g., grounding, zoom in) with results (e.g., boxes, image) actively without relying external tools, while also allowing users to trace error causes. In this paper, we study the comprehensive methodology that includes: (1) a flexible design of manipulations based on extensive analysis, (2) an efficient automated data generation pipeline, (3) a compatible VLM architecture capable of multi-turn, multi-image, and (4) a model training process for versatile capabilities. With the design, we also manually annotate **6K** high-quality samples for challenging graphical mathematical problems. Our trained model, CogCoM, equipped with this mechanism and 17B parameters, achieves SOTA performance across **9** benchmarks in **4** categories, demonstrating its effectiveness while maintaining interpretability. Our code, model, and data will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on visual reasoning problems using large vision language models. The paper focuses on the problem caused by the first alignment training stage in such vision language models, where the model does not focus on the low level details and instead focuses only on the high level details of the image. The paper proposes to solve this problem by teaching the model to perform intrinsic manipulations (e.g., grounding, zoom in) with results (e.g., boxes, image). The paper shows promising performance on various visual reasoning problems.

### Strengths
* The paper shows promising results.
* The paper is well written and easy to understand.
* The paper includes extensive qualitative examples.
* The proposed CoM dataset has the potential to be useful to the broader community.

### Weaknesses
 * Novelty: The core idea of the paper is very similar to that of "Visual Program Distillation: Distilling Tools and Programmatic Reasoning into Vision-Language Models, CVPR 2024" and "Visual Programming: Compositional Visual Reasoning Without Training, CVPR 2023". The Visual Program Distillation work trains the VLM to perform several grounding tasks for more accurate visual reasoning. Somewhat similarly, "Ferret-v2: An Improved Baseline for Referring and Grounding with Large Language Models, arXiv 2024" uses a visual sampler to extract relevant regions in the image.

* On the other hand, prior work such as "Look, Remember and Reason: Grounded reasoning in videos with language models, ICLR 2024" used surrogate tasks to extract low level visual information. A discussion of the relationship to prior work is necessary.

* Limited size of the CoM dataset: The proposed CoM dataset consist of only 6k images. This might limit its utility due to the lack of visual diversity.

* Ablation studies: The proposed method uses several datasets during the second stage of training along with the proposed CoM data -- this includes MultiInstruct (Xu et al., 2022), LLaVAR (Zhang et al., 2023b), and ShareGPT4V (Chen et al., 2023c). It would be beneficial to include additional ablations to highlight the utility of each of these datasets.

### Questions
* The paper should include a broader discussion of prior work.
* The paper should include more extensive ablations.

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
4

### Summary
This paper introduces Chain of Manipulations (CoM) to address the reasoning questions that require a detailed look of the visual information. CoM is a step-by-step strategy allowing the model to take manipulation operations like Crop/ZoomIn over the image, thus reserving more capacity for the image regions/bboxes that needs to be looked at with more detail. The contributions include both two datasets and a trained model, which shows SoTA performance on 9 datasets in 4 categories.

### Strengths
1. The proposed method, defining operations of image manipulation to solve queries that require a detailed look is intuitive, is intuitive and clear.
2. Intensive experiment results compared with up-to-date models are shown on various tasks, leading to SoTA performance.
3. writing is clear and easy to follow

### Weaknesses
1. One thing not very clear - in inference time, once the model is trained, is step-by-step CoM still needed? In other words, is CoM a method for collecting training data, or is it for VLM inference as well? Fig-6 right breaks down the questions into eight groups based on the time overhead - is this time the inference time using one single VLM call or multiple calls using CoM is needed?
2. In principle, how does this work compare to visual programming [1,2]? Is the defined manipulations like ZoomIn/Crop a specific case of the operations as in these works? More discussions will be helpful.
3. While the VQA results show huge improvement, the improvements on grounding on RefCOCO(+/g) are not as significant. Any discussions/analysis on this? Specifically, are the grounding improvements limited to cases where the grounding is an intermediate step in a more complex reasoning chain, or are there improvements in direct grounding as well?
4. The proposed data contains 70k automatically generated data and 7k human-annotated data. How does each of them contribute to the model performance? For example, are there results using each type of the data separately? Or are there more discussions on why both types are needed and only one type is not sufficient?

### Questions
See weakness.

### Soundness
4

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
4

### Summary
This paper presents CogCoM, a model that can reason in a multi-turn way when answering VQA questions. The paper first introduces an approach to collect multi-turn data given only input-output (single-turn) VQA pairs, by using GPT-4, and then uses this multi-turn pseudo-labeled data to finetune a VLM, giving this VLM the capability of reasoning in a multi-turn way. This results in better results in a variety of benchmarks.

### Strengths
1 - The paper's contributions are very sound. The idea of collecting data automatically, but having a way to pseudo-verify its correctness (at least end-to-end correctness) is reasonable.

2 - The paper shows good results across a large variety of benchmarks.

3 - The paper additionally contributes extra human-annotated data for mathematical visual reasoning, which can be useful for the community.

### Weaknesses
1 - From a scientific point of view, it is hard to tell how significant the contributions are. There is one ablation (which is informative) where they remove the multi-turn training data from their training mix, and it seems like it helps overall (but very little for two out of the three tasks shown). However, it is unclear how much of the contribution comes from the single-turn vs. multi-turn setting, or the data, or the combination of both, or just any other modeling decision when training the final model. If I am not mistaken, the results that are shown from previous methods are all single-turn, which makes the comparisons unfair. 

2 - Motivation. There are no comparisons to the module-based approach (ViperGPT-like) that is actually used to collect the pseudo-annotations. If this approach is good to collect the pseudo data, why would it not be used at inference time? Would it perform worse? Is it slower or more expensive?

3 - Presentation

  - There are many grammar and orthography mistakes.
  - The related work is only presented in the appendix. This makes it harder to understand the specific contributions of this paper.

Minor weaknesses:

4 - It is mentioned that the positive paths "are guaranteed to be error free". This is not necessarily true. The model could get to the correct answer through a wrong path, or even by having the last reasoning step completely ignore all previous information. 



- Many related literature not mentioned? Or compared
Related work should not go all of it in the appendix!

### Questions
- Do the math problems also benefits from the same "modules"? (cropping, detection...), or new ones were identified by human annotators?

- Is there any analysis on the distribution of the correct paths found during the data collection process? If only 35%, do those 35% belong to the same category of questions? Maybe there are entire categories of questions that GPT-4 just never solves, and that end up not being part of the training data.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors provide CogCoM, a technique that augments VLMs with ‘chain-of-manipulation (CoM)’ reasoning. In CoM, given image and text input, VLMs generate visual programs that evoke 6 external modules that can perform OCR, grounding, counting, calculating, zooming-in, and drawing a line. The outputs of external modules are composed into the reasoning path of VLMs. The authors automatically collect 70K training annotations for CogCoM on TextVQA/ST-VQA/TDIUC datasets, by prompting GPT-4 to use GroundingDINO and PaddleOCR, and also collect 7K training annotations for geometry problems with human annotation. The authors compares CogVLM augmented with CogCoM to other VLMs as well as CogVLM in VQA benchmarks (GQA/TallyVQA/TextVQA/ST-VQA), a proposed benchmark for CoM reasoning chain (CoM-test), visual grounding (RefCOCO, RefCOCO+, RefCOCOg), and other general benchmarks (MM-Vet, POPE). CogCoM improves CogVLM performance in many benchmarks, especially on CoM-test.

### Strengths
- Introduction of CogCoM, a technique that teaches VLMs to generate visual programs that execute visual expert modules to augment the reasoning chain of VLMs.
- CogCoM improves CogVLM performance in multiple benchmarks.
- Code/Model/Data will be publicly available.

### Weaknesses
 - **No comparisons with other visual programming methods.** There have been many works where LM or VLM generate programs to execute visual experts for different visual reasoning tasks. Earlier works include VisProg (https://arxiv.org/abs/2211.11559) / ViperGPT (https://arxiv.org/abs/2303.08128). More recent works include GPT4Tools (https://arxiv.org/abs/2305.18752), LLaVA-Plus (https://arxiv.org/abs/2311.05437), Visual Sketchpad (https://arxiv.org/abs/2406.09403) and V* (https://arxiv.org/abs/2312.14135). As generating programs with visual experts itself is not new, qualitative/quantitative comparisons would make the contribution/usefulness of CogCoM more clear.


### Questions
- In Fig 2., should the “Large Language Model” be the “Vision-Language Model”?
- In the title, should ‘visual’ be ‘vision’ for consistency?
- Have you also experimented with adding CogCoM to different VLMs? Do you have experiment results showing whether the base VLMs already need to be strong to generate CoM, or can weak VLMs benefit from CoM?

### Soundness
3

### Presentation
3

### Contribution
2
