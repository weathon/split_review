# Harnessing Webpage UIs for Text-Rich Visual Understanding

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Text-rich visual understanding—the ability to process environments where dense textual content is integrated with visuals—is crucial for multimodal large language models (MLLMs) to interact effectively with structured environments. To enhance this capability, we propose synthesizing general multimodal instructions from webpage UIs using text-based large language models (LLMs). Despite lacking direct visual input, text-based LLMs are able to process structured text representations from webpage accessibility trees. These instructions are then paired with UI screenshots to train multimodal models. We introduce \data{}, a dataset containing 7.3 million samples from 1 million websites, covering diverse multimodal tasks and UI layouts. Models trained on \data{} not only excel in web UI tasks—achieving up to a 48\% improvement on VisualWebBench and a 19.1\% boost in element accuracy on a web agent dataset Mind2Web—but also generalize surprisingly well to non-web UI tasks and even to non-UI domains, such as document understanding, OCR, and chart interpretation. These results highlight the broad applicability of web UI data for advancing text-rich visual understanding across various scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MultiUI, a large-scale dataset of website UIs annotated for diverse UI-related tasks, including captioning, visual question answering, OCR, and UI interaction grounding. MultiUI leverages web screenshots and accessibility trees as key components of its data pipeline, with annotations synthesized using powerful LLMs to support these specific UI tasks. The second part of the paper explores training Vision-Language Models (VLMs) on this new dataset and evaluates their performance on GUI understanding and grounding benchmarks.

### Strengths
- The paper is easy to follow and provides substantial figures for improving its understanding.
- The methodology for defining the data collection pipeline seems valid and the qualitative examples show that the samples are relevant.
- The proposed dataset provides substantial annotations relevant for the UI understanding field. It is a large-scale dataset, and can be relevant for the VLM community.
- Experimental results of training Llava-based VLMs on the proposed data shows that models performance improve with respect to models not trained on it.

### Weaknesses
 - The paper lacks a comprehensive comparison with other datasets in the field, in terms of number of samples, and types of annotations and tasks they can perform. Some examples are SeeClick, Ferret-UI, Mind2Web, or WebArena, among others. 
- The selection of baselines seems limited, mostly relying on Llava. Most of the results on other baselines and architecture appear empty (referring to tables 2 and 3). Authors need to thoroughly evaluate closed models like GPT4o or Claude 3.5 in the proposed benchmarks in order to offer a more strong comparison, alongside powerful open-source options like MolMo, Gemini, Llama3.2.
- Authors only present finetuning experiments on Llava-based models, lacking performing experiments on other baseline architectures to show the benefits of the proposed dataset.
- While the paper presents contributions in annotating tasks across visual understanding and reasoning, OCR, and UI grounding, the novelty of its approach is limited compared to recent advancements in the field, such as SeeClick, Ferret-UI, Mind2Web, and WebArena. The primary distinction appears to be in the scale of annotation rather than introducing fundamentally new methodologies or task definitions.
- Authors claim that the pipeline solves hallucination in the annotation process, a phenomena observed in previous works, but the paper does not describe how exactly this hallucination prevention is done.
- The experiments section is missing a batch of experiments analyzing what is the performance of models when trained on other similar competitor datasets in the field.

### Questions
- How did the authors filter websites for making sure it does not contain harmful or adult content? They provide some detail on LLM based filtering on section 2.2, but this can be insufficient. Did you consider human inspection to enhance this process?
- How does this dataset compare with other datasets in the field? A statistical comparison on the quantity and quality of samples is missing. Also, in the experiments section, we are missing a comparison on how VLMs finetuned on other dataset perform on the proposed benchmarks, in order to see the benefits of the proposed data in performance terms.
- How did authors solve hallucination when creating this dataset synthetically using LLMs?
- Have authors analyzed the train/test overlap, to avoid data contamination from train to test?
- Have authors considered finetuning other VLMs than Llava?
How does image resolution impact performance on the proposed benchmarks? Are there additional patterns observed in the experiments when comparing different Llava variants? A discussion of these insights would be appreciated.

(see the weaknesses section for additional questions)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of improving text-rich visual understanding in multimodal large language models, focusing on the ability to interpret both textual and visual elements. MultiUI aims to improve MLLM performance in document understanding, GUI comprehension, and grounding, enhancing generalization across web and other domains. Experimental results show that models trained on MultiUI significantly outperform baselines in tasks such as GUI understanding, OCR, and grounding.

### Strengths
1. The introduction of MultiUI as a large, diverse dataset specifically designed to enhance multimodal understanding using structured web UI data.
2. The paper demonstrates the dataset's impact, showing substantial performance gains over existing baselines across various multimodal tasks, emphasizing its importance for text-rich visual understanding.

### Weaknesses
1. There's a lack of documentation, making the dataset hard to navigate and providing no usage guide for the code. The authors should improve accessibility and include a clear code guide.

2. In the construction pipeline of MultiUI, while the use of Llama and LLaVA may be reasonable for certain tasks, relying on them for higher-level tasks like question answering raises concerns about reliability. Using these models for complex tasks in the dataset risks introducing biases and undermining the robustness of the evaluation.

### Questions
Recommended to clarify whether any human validation was conducted on the MultiUI dataset, including the QA tasks generated within the dataset.

### Soundness
2

### Presentation
3

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
This work introduces MultiUI, a dataset of 7.3 million VQA examples spanning 9 types of tasks covering topics of perception, comprehension, grounding, and reasoning of webpage UIs, rendered on both desktop and mobile platforms.

Specifically, the authors collect data leveraging information from the websites both directly visible from the rendered view as well as the originating accessibility tree and DOM structure and generate task data using a mixture of rules and various foundation models:
1. Webpage captioning: LLama 3 70B summarizes the website based on the accessibility tree.
2. Webpage QA: Llama 3 70B generates questions and answers for a given website based on the accessibility tree.
3. Embedded image captioning: GPT-4o-mini generates a caption of an image on the website, including context provided by the accessibility tree.
4. Embedded image QA: Llama 3 70B generates questions and answers for an embedded image, based on the generated caption.
5. Action prediction: PlayWright is used to interact with elements on the website to generate multi-choice Q&A pairs. The task is predicting the title of a target page when interacting with an element on the original website.
6. Element OCR: the task is to predict the text in an area highlighted with a red bounding box (set-of-mark prompting) in the rendered view. Relevant elements are selected based on minimum text length in the DOM.
7: Heading OCR:  the task is to predict the title of the website.
8: Action Grounding: Llama 3 70B generates request for click targets to execute a certain action, based on information from the accessibility tree. Data is generated for both multiple-choice and direct answer settings.
9: Element Grounding: coordinates and a textual descriptions are extracted from a DOM tree, with the task to predict the coordinates based on the description. Again both multi-choice and direct answer settings are considered.

The show the efficacy or the collected data to improve performance on GUI understanding and grounding, the authors train multimodal LLMs using various LLM backbones and show consistent and significant improvements over models trained on LLaVA 1.5 or LLaVA-NeXT data mixtures when incorporating their proposed MultiUI data.

### Strengths
* The collected dataset appears relevant to the burgeoning field of LLM based UI understanding and control.
* The method introduced to collect the dataset is described clearly and the identified sub-tasks are relevant and well motivated.
* The models fine tuned on the introduced data achieve strong results across benchmarks, which supports the utility of the data collected.

### Weaknesses
 * The description of the grounding task data generation (2.3.3) could be more specific. The description of how Llama 3 is used is not very clear to me ("[the model] is not only prompted to generate multiple grounding instructios to predict the bounding box of a given element but also provides the corresponding ground-truth bounding boxes"). For element grounding the extraction from the DOM tree is not described. Is the "element description" simply the text corresponding to an element (as per figure 15)?
* While mentioned in the baseline section (3.3) and measured on general OCR and grounding benchmarks, GPT-4o is not considered for GUI understanding and grounding (table 2). Given that GPT-4o shows significantly stronger results on the general benchmarks shown in table 3, it would appear to be a stronger / more relevant baseline to also consider in table 2. This is particularly noteworthy since section 4.1 discusses GPT-4V as the "most advanced MLLM" in the comparison.
* Minor: figure 4 and 6 rely on color, hard to follow on a black & white print.

### Questions
* The ablation on task type (section 4.7) shows that RefCOCO+ performance deteriorates slightly when adding MultiUI Grounding data, but seems to meaningfully improve when adding other data, particularly QA data. The discussion attributes the reduction in performance to domain shift but doesn't offer suggestions why MultiUI as a whole may still benefit RefCOCO+. Is there some understanding why this may be the case?
* ScreenSpot results are not reported for e.g. SeeClick or CogAgent, but as far as I can tell they are reported, e.g. here: https://github.com/njucckevin/SeeClick Can they be added to table 2?
* In section 3.1 the high-resolution strategy is briefly introduced. However, the exact tiling setup is not iterated on, including in appendix F. Appendix F lists a "maximum resolution" but I presume this is the resolution of an individual tile? Since the exact tiling strategy has significant impact on some of the reported benchmarks (such as DocVQA), I'd recommend to add a few more details to clarify the implementation and facilitate reproducibility in appendix F.
* For test sets like MMMU, RefCOCO+, etc. that have multiple splits that are somewhat widely used, please clarify which sets are used (perhaps in appendix G).

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents MultiUI, a new dataset that leverages webpage user interfaces as a structured and diverse multimodal data source for training large language models to understand text-rich visual content. The dataset consists of 7.3 million samples, categorized across various tasks such as visual understanding, text recognition, and GUI grounding. The authors address challenges of noise, hallucination, and generalization limitations in existing multimodal data sources. The paper introduces a two-stage training strategy, achieving significant gains in GUI-related tasks and general multimodal understanding. MultiUI demonstrates potential for improving MLLMs' capabilities in both GUI-specific and broader text-rich visual tasks, highlighting structured web data as a valuable training resource.

### Strengths
1. **Useful Dataset on a Good Problem**: The paper tackles the challenging and impactful task of text-rich visual understanding by introducing MultiUI, a large, well-structured dataset derived from webpage UIs. This dataset fills a critical gap by leveraging the naturally organized and text-embedded nature of UIs, enhancing MLLMs’ abilities to interpret complex, multimodal information in real-world scenarios.

2. **Comprehensive Experiment Results**: The authors present thorough experiments that validate MultiUI’s effectiveness across GUI-related and general multimodal benchmarks, demonstrating significant performance improvements and robust generalization capabilities. The results solidly support MultiUI’s utility and showcase its potential in both domain-specific and cross-domain applications.

### Weaknesses
One notable weakness of the paper is the limited discussion around the quality of the generated data and labels within MultiUI. While the dataset construction relies on accessibility trees and LLM-generated instructions to filter and label data, the paper lacks in-depth analysis or validation of data quality, particularly concerning the accuracy, consistency, and noise levels in generated labels. Without a rigorous assessment or benchmarks comparing the quality of MultiUI labels against human-labeled or gold-standard datasets, it is difficult to gauge the dataset’s reliability for downstream tasks, potentially impacting the generalizability and robustness of models trained on it.

### Questions
In the data construction process, how do you ensure the quality of the data points?

### Soundness
4

### Presentation
3

### Contribution
3
