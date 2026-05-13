# IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
The rapid advancement of Large Vision-Language models (LVLMs) has demonstrated a spectrum of emergent capabilities. Nevertheless, current models only focus on the visual content of a single scenario, while their ability to associate instances across different scenes has not yet been explored, which is essential for understanding complex visual content, such as movies with multiple characters and intricate plots. Towards movie understanding, a critical initial step for LVLMs is to unleash the potential of character identities memory and recognition across multiple visual scenarios. To achieve the goal, we propose visual instruction tuning with ID reference and develop an \textbf{ID}-\textbf{A}ware Large \textbf{V}ision-\textbf{L}anguage \textbf{M}odel, IDA-VLM. Furthermore, our research introduces a novel benchmark MM-ID, to examine LVLMs on instance IDs memory and recognition across four dimensions: matching, location, question-answering, and captioning. Our findings highlight the limitations of existing LVLMs in recognizing and associating instance identities with ID reference. This paper paves the way for future artificial intelligence systems to possess multi-identity visual inputs, thereby facilitating the comprehension of complex visual narratives like movies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of movie understanding in VLMs by developing mechanisms to associate instances across different scenes. The authors propose ID-Former, integrated within their ID-Aware VLM architecture, and implement visual instruction tuning with ID references. To evaluate instance ID memory and recognition capabilities across multiple visual scenarios systematically, they introduce a new benchmark called MM-ID.

### Strengths
1) The framework architecture is conceptually straightforward.
2) The training dataset construction methodology leverages existing open-source databases with replicable procedures.
3) The MM-ID benchmark provides comprehensive evaluation metrics across multiple aspects of ID-related movie understanding tasks.

### Weaknesses
1. The ID-Former is the essential innovative module in the framework. The authors are encouraged to provide the architectural details and hyperparameter configurations of the ID-Former.

2. The integration of LLaVA and ShareGPT4V data. 1) The selection criteria for the 10% subset of LLaVA data remain unclear. 2) The paper would benefit from an ablation study showing "IDA-VLM (w/ LLaVA data only)" to isolate the impact of the newly constructed tuning data.

3. The experimental setup primarily addresses scenarios where reference ID count equals or is less than the character count in test images. However, real movie scenes often involve more main and important supporting characters than visible in a single frame. Usually, it is unlikely to accurately know the characters of interest for each requested frame beforehand. Therefore, the model's performance in scenarios with excess reference IDs is worth an investigation.

4. The absence of a systematic evaluation of robustness to ID variations. Particularly, it would be interesting to know its performance regarding environmental factors (lighting, viewing angles) and character appearance changes (clothing, age progression), and whether there is a degradation under significant reference-test image discrepancies.

### Questions
1. The potential scoring variance inherent in subjective assessments with wide scoring ranges by GPT-4. The paper uses GPT-4 to score predictions based on a ten-point scale. Although it adopts the average of 5 times predictions, it would be nice to know whether GPT-4 can consistently provide reasonable explanations for its scoring and whether it can discriminate adjacent score points on the ten-point scale. 

2. Regarding Table 5, the observed degradation in ID matching performance with first-stage tuning calls for investigation into potential mitigation strategies to maintain performance at the same level as the "w/o first stage tuning" configuration.

I am willing to change the score if my concerns are addressed.

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
This paper mainly focuses on VQA tasks with multiple images containing the same character identities. To reach a higher performance, the authors construct specific datasets from both (1) multi-image reasoning datasets like VCR, and (2) movie shot datasets, and utilize a certain templates to train such abilities. To evaluate such abilities, the authors propose a new benchmark MM-1D with four question types and 585 samples.

### Strengths
The motivation that identifies same characters in different images make sense, and it is important for VLMs.

The new benchmark MM-ID is delicately curated, with statics and detailed process to collect these data.

### Weaknesses
All questions in stage-2 training and MM-ID testing share a similar template as `sombody is <image>. somebody is <image> ...`. It requires the question to have single-character images and be formatted in a certain template. This is too narrow for real world usage and can hardly represent real-world performance.

Moreover, does the data used in stage-2 share the similar template. If so, how can I tell if the increase in performance is due to efficient training on such template?

The same problems also appears in the model structure in Fig. 2. It seems that the model needs to treat ID images and other images differently in the ID-Former. Moreover, I am not a little confused of the three cross-attn in ID-Former. I suppose there would be multiple ID images and multiple test images, how can I do cross attention taking multiple images as queries and keys at the same time. Please elaborate more on the model structure.

### Questions
My main concern is if this fixed template can cover the wide range of real-world VQA samples. Please see weakness for details.

### Soundness
2

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
4

### Summary
In this paper, the authors propose IDA-VLM, which is designed to conduct visual instruction tuning with ID reference. Furthermore, the authors also construct a benchmark named MM-ID to evaluate the ability of ID memory and recognition in existing  VLMs.

### Strengths
1.The proposed visual instruction tuning with ID reference is interesting and has the potential to be applied to movie understanding.
2.The paper is well-written and is easy to understand.

### Weaknesses
Problems:
1. The authors wrote: “We crop sub-images of the individuals and assign them identifiable labels, such as person names.” in lIne243. I would like to know how to assign each individual a person's name. Is the name randomly generated via Large language models e.g. GPT4?

2. Why the results of Qwen-VL-Chat are not included in Table2 and Table3. Qwen-VL-Chat should be a baseline since the proposed IDA-VLM is built based on it.

3. More models should be included in Table1. There are a lot of popular open-sourced VLMs e.g. LLaVa. These models should be included in Table1 to enhance the benchmark. and facilate future reserch.

4. In the Table4, more standard benchmarks should be included. Only evaluating IDA-VLM on two benchmarks is not enough. The authors should include more benchmarks e.g TextVQA and MMBench for a more comprehensive evaluation.


Issues:
1.The font in the figures is too small, which makes it hard for readers to read. It is highly recommended to increase the font size in figures.

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigate a novel capability for large vision-language models (LVLMs) to recognize and distinguish multiple characters across different visual scenes. The authors introduce a benchmark, MM-ID, to evaluate this ability in four areas: matching, location, question-answering, and captioning. To improve LVLM performance on these tasks, they propose a tuning recipe and develop the IDA-VLM model.

### Strengths
- The motivation is well-grounded. The benchmark also evaluate the model’s ability to understand prompts that involve multiple images interleaved with text.
- The task of location based on reference character images is innovative. It is different from other locating tasks, such as text-to-roi grounding.

### Weaknesses
When constructing localization samples using RefCOCO, the ID images are cropped and flipped from the original images (this is inferred from the figure, as the text does not mention the flipping). This means that the pattern of the ID images is identical to the region of interest (ROI) in the original image. This does not align with the task defined in the paper, which aims to understand character features and locate the character in another image in a different state. The RefCOCO-based data does not require understanding of character features but simply finding identical content.

### Questions
- As is described in 'weaknesses', are there other ways to construct localization samples, such as using 3D datasets or leveraging base models like SAM2 and human detection models to construct samples from videos?
- When there are multiple ID images and multiple test images, how does ID-Former determine which ID image each test image should attend to? Figure 2 only illustrates the one-to-one case.

### Soundness
4

### Presentation
4

### Contribution
3
