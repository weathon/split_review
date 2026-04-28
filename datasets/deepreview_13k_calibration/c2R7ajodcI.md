# The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
We present the All-Seeing (AS)\footnote{``All-Seeing'' is derived from ``The All-Seeing Eye'', which means having complete knowledge, awareness, or insight into all aspects of existence.} project: a large-scale data and model for recognizing and understanding everything in the open world.
Using a scalable data engine that incorporates human feedback and efficient models in the loop,
we create a new dataset (\datasetname) with over 1 billion regions annotated with semantic tags, question-answering pairs, and detailed captions.
It covers a wide range of 3.5 million common and rare concepts in the real world, and has 132.2 billion tokens that describe the concepts and their attributes.
Leveraging this new dataset, we develop the All-Seeing model (ASM), a unified framework for panoptic visual recognition and understanding. The model is trained with open-ended language prompts and locations, 
which allows it to generalize to various vision and language tasks with remarkable zero-shot performance, including region-text retrieval, region recognition, captioning, and question-answering. 
We hope that this project can serve as a foundation for vision-language artificial general intelligence research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors present a large dataset and model for panoptic visual understanding, collectively named the "All-Seeing Project".
The dataset (AS-1B) contains more than one billion region-text pairs, where the text comprises semantic tags, question-answer pairs, and captions.
Text in AS-1B entails a rich vocabulary of visual concepts, e.g. the authors state the presence of 3.5 million unique semantic tags.
The authors design a scalable, semi-automatic data collection engine to collect AS-1B --
their pipeline is composed of several large vision models that generate region-text annotations,
and human annotator to verify the correctness of the generated annotations.
The authors train All-Seeing Model (ASM) using their dataset and show strong empirical performance on several downstream vision-language tasks.

### Strengths
1. AS-1B is a large dataset of region-text pairs, perhaps currently the largest of its kind.
2. The design choice of using the same images as SA-1B is excellent to mitigate ethical risks regarding copyright and privacy of users,
   as these images are meticulously verified by Meta AI, and released with a permissible license for research.
3. The proposed model (ASM) achieves strong empirical performance on several region-level visual understanding tasks.
4. The design of ASM allows it to be "composable" in a larger system that may include localization models like SAM.

### Weaknesses
1.  **Collection engine prone to hallucinations:**
The authors use large language models (LLMs) in the "imaginator" and "splitter" to produce semantic tags that are NOT conditioned on the visual content.
The imaginator produces plausible semantic tags that are _likely_ to occur, but not guaranteed to occur in images.
Is there is a way to quantify the amount of hallucination by checking the response of human annotators?
I suggest the authors to provide ample of qualitative examples in the paper showing the initial pool of semantic tags *before* they are assigned to the region proposals.

2.  **Redundant caption annotations:**
The detailed caption of a region is produced by paraphrasing three question-answer pairs.
Based on the limited examples in the paper, the captions sound like a "dry" paraphrasing of the question-answer pairs (understandably so).
I wonder if having such redundancy contributes to the uniqueness of AS-1B, or simply adds redundancy and increases the size of dataset.

3.  **Consider adding a datasheet:**
The authors should consider adding a datasheet () or a similar supplemental material outlining the characteristics of AS-1B.
For example, the Segment Anything paper includes a datasheet for SA-1B.
Datasheets serve as as a medium of communication between the authors (creators of the dataset) and future works (users of the dataset).
Many papers published in NeurIPS datasets track have datasheet templates which can be suitable in the ICLR format,
e.g. some image-text datasets like [LAION-5B](https://arxiv.org/abs/2210.08402) and [RedCaps](https://arxiv.org/abs/2111.11431).

4.  **Needs a train/val split:**
I agree with the other reviewers' assessment that the authors should consider defining a train/val split for AS-1B.
If the authors do not define a split, different future works will regardlessly split AS-1B in ad-hoc ways and lead to inconsistencies.
I suggest the authors to "hold out" ~1% data as a validation set for the sake of consistency.

6.  **Missing References:**
The proposed All-Seeing Model is trained with both, a generative and contrastive loss, to facilitate its use for generative (e.g. captioning) and discriminative (e.g. object recognition) tasks.
Due to the similarity in its architectural design, I believe the authors should cite a few prior works in their discussion to provide a broader context for the reader:

    - [CoCa: Contrastive Captioners are Image-Text Foundation Models](https://arxiv.org/abs/2205.01917) - trains with both objects as ASM.
    - [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/abs/2111.07991) - repurposes *any* image backbone to a contrastive image-text model.
    - [Image Captioners Are Scalable Vision Learners Too](https://arxiv.org/abs/2306.07915) - trains with generative objective first, then uses LiT.

### Questions
Please see weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The papers presents a large-scale dataset collected using a semi-automatic data engine for open-world panoptic visual understanding. The dataset consists of 1 Billion + region annotations spanning semantic tags (3.5 Million +), question-answer pairs (3.3 billion) as well as detailed captions (1.2 billion). The paper proposes a VLLM called All-Seeing Model (ASM) trained on this dataset consisting of a location aware image tokeniser and a LLM based decoder. ASM achieves promising results on image and region-level captioning and recognition tasks.

### Strengths
- The paper does a great job explaining the details related to the dataset. The appendix contains several details that help understand the semi-automatic approach mentioned in the paper better (percentage of annotations from LLMs/VLLMs, accuracy of automatic annotations.
- The paper presents a fairly exhaustive benchmark (VQA, OK-VQA in supplementary). The paper also attempts to evaluate the model’s performance on region-based tasks like region-based visual question answering by conducting human studies.
- The paper also presents a good summary of many factors that are responsible for improving the performance of the model such as the role of data-engineering (D.3)

### Weaknesses
 - Phrase Grounding Evaluation: The proposed method also missed an opportunity to leverage the dataset to learn the ability to ground language into the image by generating the bounding boxes corresponding to the text. I would have liked to see the models performance on the phrase grounding task on Flickr30K Entities.
- I think the paper misrepresents the state of the art in the community. For instance, the claim that current systems “are primarily focused on understanding images as a whole, rather than recognizing and comprehending individual instances within the scene” seems ungrounded, and several state of the art systems (e.g, Unified IO, including more recent ones like KOSMOS-2) show a fairly good understanding of the image on benchmarks that test this visual grounding like referring expressions, and phrase groundings. Since the authors compare and cite KOSMOS-2, for completeness the authors should also put the proposed dataset (AS-1B) in perspective of other comparable datasets such as GRiT which consists of region annotations for 90 million images.
- The paper uses LORA to fine-tune the LLM on various tasks COCO, VQA, etc which is different from other methods (BLIP, InstructBLIP, etc) that the method have compared against. This makes the evaluation unfair because these evaluations heavily penalise the peculiarities of the the evaluation protocol (one-word answers as opposed to natural language generation). Since methods like BLIP use a frozen LLM, it’s much harder for them to conform to the expected style of answers as opposed to the ASM which adapts the LLM using LORA.

### Questions
See weaknesses section

### Soundness
3 good

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
This paper proposes a large dataset and model for detailed VQA and captions about image regions. The data engine involves the use of a combination of localization models, contrastive vision language models, and other LLMs/VLLMs, as well as humans in the loop to verify the outputs. The resulting dataset has 1.2B regions covering a wide range of 3.5M concepts. The authors also propose a model to ingest this data and handle both discriminative/generative tasks.

### Strengths
The paper addresses an important space of problems that existing vision and language foundational models are focused on image-level understanding, and there's a clear need to build region-level vision and language foundational model. The proposed dataset is based on the recent SA-1B dataset and extend it with semantic tags/QA pairs, and detailed caption, all of which can be useful to the community.

### Weaknesses
1. It'd be helpful to get some analysis on the quality of the final data after human verification. Appendix B.3 shows the accuracy of automatic annotation is around 50-60%. How much of the error is fixed by human verification, and how much is still there? It would be beneficial to understand the types of errors that persist even after human review, such as inaccuracies in object identification, attribute descriptions, or relationship understanding, to gauge the reliability of the dataset for downstream tasks.

2. I'm wondering if it'd be better to set apart a high-quality split for region-level validation/testing of captioning. Existing dataset don't seem to serve this purpose very well e.g. RefCOCOg is not intended for region-level captioning. Visual genome is not a common benchmark for captioning evaluation either. The lack of a dedicated high-quality validation set makes it difficult to assess the true performance of region-level captioning models trained on this data, potentially leading to overfitting on the training set or unreliable generalization.

3. Image-level captioning in Table 3 is helpful, but not the focus of this work in my view. To make this more complete, it might be good to add COCO captions too. While image-level captioning provides some context, it doesn't directly evaluate the core contribution of this work, which is region-level understanding. Including COCO captioning results would provide a more standard benchmark for comparison, but it's still not directly relevant to the primary focus.

4. To make a strong claim on region level understanding, I feel that the model should be able to predict regions from images rather than accepting regions as input. For example, in Table 4, it'd be more useful to have a simple ASM model that can predict regions without groundtruth box inputs. The current setup, where the model takes ground truth regions as input, limits its applicability in real-world scenarios where region proposals are not readily available. A model capable of predicting regions would demonstrate a more complete understanding of the visual scene.

5. It'd be great to have a region-level VQA benchmark as well since the dataset includes VQA. I see the image-level VQA results in Table 10, but that does not seem to capture the uniqueness of this data. The inclusion of VQA data at the region level is a valuable contribution, but the lack of a dedicated evaluation benchmark makes it difficult to assess the model's performance on this specific task. Image-level VQA results do not adequately capture the model's ability to reason about specific regions.

6. It'd be helpful to have some analysis on bias/fairness considerations. Given the scale of the dataset and the use of large language models in its creation, it is crucial to investigate potential biases that may be present in the data, such as demographic skews or stereotypical associations, to ensure responsible use of the dataset and model.

### Questions
See weaknesses. My main concerns are with the data quality and evaluation benchmarks based on this dataset/model.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
