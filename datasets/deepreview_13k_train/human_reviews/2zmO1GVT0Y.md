# NL-Eye: Abductive NLI For Images

- Decision: Accept
- Scores: 6, 6, 6, 5, 6

## Abstract
Will a Visual Language Model (VLM)-based bot warn us about slipping if it detects a wet floor? Recent VLMs have demonstrated impressive capabilities, yet their ability to infer outcomes and causes remains underexplored. To address this, we introduce \bench, a benchmark designed to assess VLMs' visual abductive reasoning skills. \bench\ adapts the abductive Natural Language Inference (NLI) task to the visual domain, requiring models to evaluate the plausibility of hypothesis images based on a premise image and explain their decisions. \bench\ consists of 350 carefully curated triplet examples (1,050 images) spanning diverse reasoning categories: physical, functional, logical, emotional, cultural, and social. The data curation process involved two steps—writing textual descriptions and generating images using text-to-image models, both requiring substantial human involvement to ensure high-quality and challenging scenes. Our experiments show that VLMs struggle significantly on \bench, often performing at random baseline levels, while humans excel in both plausibility prediction and explanation quality. This demonstrates a deficiency in the abductive reasoning capabilities of modern VLMs. \bench\ represents a crucial step toward developing VLMs capable of robust multimodal reasoning for real-world applications, including accident-prevention bots and generated video verification.\footnote{Data and code are available on the project page: \url{https://venturamor.io/NLEye/}.
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a benchmark for measuring visual abductive reasoning capability and explains the process of constructing this benchmark. It demonstrates that current multimodal language models lack visual abductive reasoning capability and introduces a novel aspect of verifying image-to-image entailment that has not been previously addressed.

### Strengths
- The paper is well-written and easy to read.
- The process of data collection and verification is systematic and meticulous.
- It intriguingly points out the shortcomings of existing visual language models (VLMs) in visual abductive reasoning, with experimental results to substantiate this claim.
- The paper proposes various experimental setups by combining or separating images, changing the order of images, which helps ensure fair testing.
- The benchmark effectively reveals multiple shortcomings of different VLMs, not only evaluating abductive reasoning but also highlighting issues with image location sensitivity and poor visual interpretation.
- Unlike traditional natural language inference (NLI) benchmarks, this approach offers a comprehensive evaluation of multiple aspects.

### Weaknesses
 - The evaluation criteria are unclear and not well-defined. The use of automatic evaluation for explanations seems inadequate, and manual evaluation, while more accurate, is too costly and varies depending on the person.
- The definition of visual abductive reasoning capability remains unclear; it appears to evaluate abilities including visual interpretation, interpretation of multiple images, and natural language inference, covering a broad range of concepts that are not distinctly defined.

### Questions
- For the evaluation with this benchmark, it would be beneficial to have better metrics. Are there methods to quantify image order sensitivity? Could metrics be developed to measure visual understanding and linguistic abstract reasoning capabilities using various forms of input (Text-only, Image-to-Text, Image and Text, etc.)?

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
This paper introduces a new benchmark NL-EYE that is designed to assess VLMs’ visual abductive reasoning skills. NL-EYE adapts the abductive Natural Language Inference (NLI) task to the visual domain, requiring models to evaluate the plausibility of hypothesis images based on a premise image and explain their decisions. NL-EYE consists of 350 carefully curated triplet examples (1,050 images) spanning diverse reasoning categories: physical, functional, logical, emotional, cultural, and social. Experiments show that VLMs struggle significantly on NL-EYE, often performing at random baseline levels, while humans excel in both plausibility prediction and explanation quality.

### Strengths
Previous Visual entailment tasks were mainly in text format. This paper for the first time proposes the task in image formats, and collected a human-curated benchmark. The experiments show that current VLMs cannot do well on the NL-EYE.
Also, one experiment result saying that VLM prediction depends on hypothesis location is interesting.

### Weaknesses
1. It is unclear whether the used prompt can best unleash VLMs' performance. For example, from Table 5, it seems no example has been provided, and that may lead to lower VLM performance.
2. Why do human only achieve 83-85% accuracy if human collected the dataset and this dataset do not require expert knowledge? (Line 426-427) It is a bit confusing to understand.
3. In Table 3, why not try GPT-4o as the Image-to-Text model? Also, why not try Claude models as predictor?
4. The images are generated instead of from real world, and could potentially affect the output. The test size is 350 which might be small.

### Questions
See Weakness 1-3. 
Also just out of curiosity, why can't the setting in Table 3 solve this problem? E.g. How did GPT-4o fail the entailment upon the Figure 8 machine-generated captions?

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
4

### Summary
This paper presents NL-EYE, a benchmark to evaluate VLMs' visual abductive reasoning skills across six reasoning types: physical, functional, logical, emotional, cultural, and social. It includes 350 triplet examples (1,050 images) with temporal annotations indicating event sequence and duration. The study examines model robustness, considering hypothesis order sensitivity and different input formats (individual versus composite images). NL-EYE also assesses models' ability to score single hypotheses, addressing real-world scenarios where multiple alternatives may not be available.

### Strengths
1. This paper demonstrates a way to measure VLMs abductive reasoning ability on six diverse reasoning categories using multiple images.
2. The experiments shown in the paper comprehensively evaluate the reasoning ability of VLMs by checking image ordering, exploring different input formats to justify the reasoning gap of the existing VLMs.
3. The analysis section is interesting. The breakdown of performance across reasoning categories and the underlying insights will be useful for the community.

### Weaknesses
 1. The prompt selection is under-explored. 
2. More detailed in the Questions section

### Questions
Q1. It is unclear from the paper how the authors selected the concepts for each individual reasoning category. For example, in the Cultural Reasoning category, which cultures were represented in the generated image. As image generation models are also not good for cultural content generation and the VLMs being better on cultural NLI raise interest in which cultures were highlighted mostly in the data to assess the comprehensiveness of the test set.

Q2. The current prompt for VLM is asking the plausible answer first and then asking for explanation. It would be interesting to reverse this process (i.e., explain each image step-by-step and then conclude the plausible answer) and see how the VLMs react.

Q3. In Tables 2 and 3, LLaVA 1.6 performs better at predicting the plausible image using GPT-4 when converting image to text (Table 3) than when directly inputting images (Table 2). Could this difference be due to LLaVA’s limitations as a predictor, or is the prompt structure (e.g., asking for image descriptions first before selecting a plausible answer) affecting performance?

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
4

### Summary
This work proposes the NL-Eye benchmark to evaluate the abductive reasoning ability of visual-language models from pure visual perception in multi-image situations, inspired by Natural Language Inference (NLI). The benchmark consists of testing examples for temporal reasoning along with six reasoning categories and images are obtained from the text-to-image generation model. The authors argue that current visual-language models show significantly inferior performance compared to humans on abductive reasoning in multi-image situations and claim that this is due to the lack of purely visual perception abilities compressed from the visual perception modules.

### Strengths
This work is distinct from existing multi-image benchmarks in that the objects of perception required to perform reasoning are provided solely through visual perception. NLI-inspired benchmarks that require visual reasoning over multi-images already exist, such as [1], but they are limited in terms of evaluating purely on visual perception, as they require reasoning over a given natural language premise. However, NL-Eye has the unique feature that requires reasoning on pure visual perception, since these premises are provided as images.

[1] A Corpus for Reasoning About Natural Language Grounded in Photographs (Suhr et al., 2019)

### Weaknesses
There is a lack of consideration in the experiments as to whether a proper evaluation of the current visual-language model can be made in a multi-image setting. As the authors argue, current benchmarks for testing abductive reasoning are single-image focused, but it should not be overlooked that research on the visual-language model itself is also focused on this. As a result, the authors provide “concatenated” images, which may not be a fair assessment for most visual-language models that currently operate at fixed, squared-sized resolutions. To demonstrate the need for the proposed benchmark, it is required to observe if the same phenomenon is found in visual-language models that can handle flexible resolutions and aspect ratios like [1].

It is also not clear if the performance bottleneck is due to the visual encoder or the language model itself. The authors should provide more analysis on this point. For example, if the visual encoder is the main limitation, then fine-tuning the language model on text-based reasoning tasks should not improve the performance on the proposed benchmark. However, if the language model is the main limitation, then fine-tuning the language model on text-based reasoning tasks should improve the performance on the proposed benchmark.

### Questions
It would be nice to be able to determine if the problem this benchmark shows is out-of-domain on the language model side or a limitation of the visual encoder itself. If we split the data in the benchmark for training and test purposes and fine-tuned models improved on the remaining test splits, then we can assume that the main problem was the task was out-of-distribution rather than a lack of performance on visual perception, since most current visual-language models trained with a frozen visual encoder. Have you done any further experiments to see if this limitation on visual reasoning can be improved with some training or not?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces NL-EYE, a benchmark designed to test the abductive reasoning capabilities of Visual Language Models (VLMs) through image-based tasks. The benchmark includes 350 carefully curated triplet examples spanning diverse reasoning categories where models must choose the more plausible hypothesis from a set and provide an explanation. Experiments reveal that while humans excel in this task, current VLMs show notable deficiencies in their reasoning capabilities. The authors conclude that VLMs face significant challenges in visual interpretation, which impacts their ability to reason effectively about images.

### Strengths
1. The benchmark is well-designed with diverse reasoning categories.
2. Experiments on the benchmark reveal interesting findings.
3. The analysis is thorough and highlights notable insights into VLM limitations.

### Weaknesses
1. While I agree that the benchmark is carefully curated, the filtering condition can be inconsistent and subjective because it is done manually. 
2. This paper focuses primarily on evaluating VLMs' deficiencies but lacks discussion on strategies or methods to improve these models' abductive reasoning capabilities.
3. The paper lacks experiments with additional open-source models. While the current model selection is valid, given the paper's findings about failures in visual interpretation and hypothesis location dependency, testing VLMs with different visual encoders or those trained on multi-image datasets would further support the analysis.

### Questions
## Question
1. Have the authors conducted experiments with VLMs that trained on datasets including multiple images such as LLaVA-Onevision or VILA, and with VLMs that use other visual encoders like Cambrian-1?

## Typo
* L260 Validation,and Categorization -> Validation and Categorization

---
### References
* Lin, Ji, et al. Vila: On pre-training for visual language models. CVPR 2024
* Li, Bo, et al. Llava-onevision: Easy visual task transfer. https://llava-vl.github.io/blog/2024-08-05-llava-onevision/
* Tong, Shengbang, et al. Cambrian-1: A fully open, vision-centric exploration of multimodal llms. Neurips 2024

### Soundness
4

### Presentation
3

### Contribution
3
