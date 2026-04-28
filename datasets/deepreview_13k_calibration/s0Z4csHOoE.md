# VCR: Visual Caption Restoration

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We introduce Visual Caption Restoration (VCR), a novel vision-language task that challenges models to accurately restore partially obscured texts using pixel-level hints within images.
This task stems from the observation that text embedded in images is intrinsically different from common visual elements and natural language due to the need to align the modalities of vision, text, and text embedded in images.
While numerous works have integrated text embedded in images into visual question-answering tasks, approaches to these tasks generally rely on optical character recognition or masked language modeling, thus reducing the task to mainly text-based processing. 
However, text-based processing becomes ineffective in VCR as accurate text restoration depends on the combined information from provided images, context, and subtle cues from the tiny exposed areas of masked texts. 
We develop a pipeline to generate synthetic images for the VCR task using image-caption pairs, with adjustable caption visibility to control the task difficulty.
With this pipeline, we construct a dataset for VCR called \ourdataset{} using images with captions from Wikipedia, comprising $2.11M$ English and $346K$ Chinese entities in both \emph{easy} and \emph{hard} configurations.
Our results reveal that current vision language models significantly lag behind human performance in the VCR task, and merely fine-tuning the models on our dataset does not lead to notable improvements. We release \ourdataset{} and the data construction code to facilitate future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a new vision-language evaluation task (VCR), for assessing models performance on restoring partially obscured text embedded in images, using pixel-level hints (pixels from the top and the bottom of the partially obscured characters) and the visual contexts of the image. This approach mirrors human proficiency in recognising partially hidden objects, a skill supported by complex visual and cognitive processes, as noted in prior studies.

The authors claim, that the traditional VQA tasks, especially in the area of embedded text recognition, work independently the non-text visual context of the image, a gap that the VCR task covers. To support this claim, they are analysing the correlation of the VCR task to other VLM benchmarks and they demonstrate low correlation especial for the VCR-HARD task, where pixel hints are minimal.

For this topic, the authors developed a pipeline for generating synthetic images for the VCR task, using image-caption pairs, with configurable caption visibility to control the difficulty level of the task. Using this pipeline they developed the VCR-wiki dataset, from images and captions coming from Wikipedia. The dataset contains 2.11M English and 346K Chinese samples. There are two versions of the dataset, an EASY one and a HARD one (both feasible for native speakers of the language), where these two versions differ on the amount of the pixels remain visible from the obscured text. Each dataset has a Train, a Validation and a Test split.

For the evaluation task the authors introduce two metrics, an Exact Match, and Jaccard Index (Bag-of-Words as sets) for comparing the ground truth (obscured text) with the models' response (recovery of the obscured text).

The authors include in the paper several VCR evaluation experiments for many open and closed source models. They show that the majority of the models performs poorly on this task, and they draw the below conclusions:
* VCR is a challenging task for SOTA VLMs, while humans score high in this task
* Models that perform well in OCR tasks, can score low in VCR
* Performance degradation on Chinese version of the task, showing the need of improvements in multilingual capabilities
* Larger models, or higher image resolutions are not correlated with better performance in VCR task
* Non-text image information is not effectively leveraged by the most of the models in this task
* Model architecture can be a performance improvements resisting factor when applying fine-tuning on VCR-wiki dataset

### Strengths
The paper introduces an original task for evaluating VLMs. The contributions are clearly explained, and there are sufficient details about them (metrics, pipeline for generating synthetic images for the VCR task, VCR-wiki dataset). The experiments are presented with clarity and the paper has a good structure.

### Weaknesses
The paper lacks a clear explanation of how improvements in VLMs, as reflected by higher scores on VCR task, would translate to overall advancements in VLM capabilities. There are not any specific ways mentioned in which enhanced performance on this task would lead to meaningful or practical improvements in VLM functionality, generalisation, or real-world applicability. Providing a more detailed rationale on this point would strengthen the paper, as it would help clarify the relevance of VCR task performance as a benchmark for broader VLM development.

There are additional questions regarding the choices made in various experimental settings, and providing more details on these decisions would strengthen the clarity of the paper. Specifically:
* Selected number of n-grams: The authors chose to use a 5-gram approach; however, it is not clear why this number was selected. Was this choice based on empirical results, or was it simply an arbitrary decision? Additionally, it would be informative to know if smaller n-grams were tested and, if so, how the models performed with those alternative configurations.
* Text visibility settings: For the "EASY" mode in the dataset, how did the authors determine the chosen visibility threshold? Was this the minimum level at which open-source OCR tools started to perform poorly, or was it a randomly selected setting? A discussion on how this visibility threshold was established would provide useful context, especially regarding the task's difficulty calibration.
* Fine-tuning configuration: Given the extensive data available in the VCR-wiki dataset, it would be helpful to understand if the authors experimented with fine-tuning the models using a larger subset of this data. Additionally, specifying the number of training epochs used in these experiments would offer valuable insight into the training process and potential impacts on model performance.
* Prompts: It would be beneficial to know if any prompt engineering was applied when experimenting with different models. For instance, how did the authors arrive at the chosen prompt? In relation to the observed performance degradation with VI, did the authors attempt prompts specifically guiding the model to utilize visual cues (e.g., "Use the visual information from the image to recover the missing text.")?

Addressing these points with more detail would enhance the paper’s transparency and rationale behind these experimental choices.

### Questions
Quoted from the paper: "Figure[3] is an example VCR task in hard mode, and Figure[1] shows an example VCR task in the easy
mode. Although humans can still fill the blanks easily in the hard mode, it is nearly impossible for models with only OCR capabilities to recover the covered texts without using the context." Instead of Figure[3] I think it should be Figure[2].

Suggestions:
Address the weaknesses mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Visual Caption Restoration (VCR) benchmark, designed to assess vision-language models' (VLMs) ability to restore partially obscured text using visual cues from images. VCR is built with images and captions sourced from Wikipedia, encompassing 2.11M English and 346K Chinese entries, presented in both easy and hard configurations. Experiments are conducted on state-of-the-art (SOTA) VLMs to evaluate their performance.

### Strengths
* The paper is well-written and easy to follow.
* VCR is an interesting benchmark that poses challenges to existing VLMs. It's a nice addition to the VLM community.
* The evaluation of most SOTA VLMs offers insightful findings that advance the field.

### Weaknesses
 * Certain important details about the dataset are missing from the paper; please refer to the questions section below.
* The experiments on fine-tuning VLMs on VCR are not informative enough, as the VLMs of choice differ too much in terms of backbone/architecture/training pipeline... I feel like stating "the architectural design of CogVLM2 is well-suited for VCR" in line 368 might need more experiments or well-controlled experimental setups.

### Questions
* As mentioned above, my main question centered around the details about the dataset:
  * Given that training data for SOTA VLMs often includes Wikipedia content, how does the benchmark ensure that images and captions in the dataset have not been seen during VLM pre-training or SFT? When were these images and captions posted?
  * The difference between easy and hard cases is vague.Separating these cases based solely on the area of visible pixels may be insufficient, as the difficulty level for restoring a word can also depend on the word itself. For example, if both "area" and "idea" are 80% covered, it may be challenging to determine which is easier to recognize. The word "idea" initially occupies more pixels, and the "d" token could serve as a clue, making it more recognizable. This suggests that the difficulty of a sample may also depend on word combinations in the sentence. What are the detailed criteria (e.g. covering proportion) for choosing easy/hard samples? 
  * Following up on the previous point, if the covering proportion is automatically used to select easy and hard samples, would it be possible to manually curate these samples based on word combinations? I understand that this would involve additional effort, so this is just an open question I'm interested in.

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
This paper presents Visual Caption Restoration (VCR), a new VL task where models need to accurately restore partially obscured text embedded within images using pixel-level hints and contextual cues. Unlike conventional OCR tasks, VCR requires the model to align vision and language modalities to restore text that is often obscured or fragmented. The authors introduce VCR-WIKI, a large-scale synthetic dataset generated using Wikipedia captions, supporting both English and Chinese text in easy and hard configurations. Experiments demonstrate that state-of-the-art vision-language models fall significantly short of human performance on the VCR task, highlighting the need for new model architectures that handle complex intermodal alignment.

### Strengths
The paper identifies a critical gap in vision-language tasks by focusing on restoring partially occluded text within images. This differs from traditional VQA and OCR by challenging models to reconstruct text based on incomplete visual information and context, a complex multimodal problem.

The VCR-WIKI dataset provides a scalable and controllable environment for testing models under different levels of text occlusion. The authors’ pipeline generates a diverse dataset that is balanced across languages, allowing for cross-linguistic studies and detailed analysis of model capabilities.

By analyzing the model failures, the paper provides useful insights into the challenges of multimodal alignment, reasoning, and generalization. The authors' discussion on how models with strong OCR capabilities underperform on VCR highlights the distinct challenges VCR poses.

### Weaknesses
The reliance on synthetically generated images raises questions about the generalizability of models trained on VCR-WIKI to real-world applications. Text within real images can exhibit more variability in terms of style, font, and environmental factors such as lighting, perspective distortion, and complex backgrounds that may not be fully captured by VCR-WIKI's controlled generation process. This could lead to models that perform well on the synthetic dataset but struggle with the nuances of real-world text occlusion.

The paper's use of GPT-based metrics could introduce variability in assessment, especially given the subjective nature of scoring masked text restoration. While Exact Match and Jaccard Index provide quantitative metrics, the lack of a more nuanced evaluation strategy that accounts for semantic similarity or partial credit for near-misses could limit the ability to accurately assess model performance. The reliance on exact string matching may penalize models that correctly identify the meaning but not the precise wording, potentially underestimating their true capabilities.

The synthetic dataset may not fully replicate the nuances of real-world images with natural text occlusion. The occlusion patterns used in VCR-WIKI might not reflect the diverse and unpredictable ways in which text is occluded in real-world scenarios, such as by objects, shadows, or other text. Additional discussion on the challenges of transferring VCR models to real-world scenarios, including an analysis of the types of real-world occlusions that are not well represented in the dataset, would clarify the dataset's practical applicability.

### Questions
Since VCR-WIKI relies on synthetic captions and partially obscured text, I was wondering to what extent you expect models trained on this dataset to generalize to real-world scenarios where text may have more complex occlusions or be influenced by environmental factors (e.g., lighting, noise).

### Soundness
3

### Presentation
3

### Contribution
3
