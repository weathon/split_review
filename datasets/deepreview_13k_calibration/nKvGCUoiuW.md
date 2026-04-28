# MiniGPT-v2: Large Language Model as a Unified Interface for Vision-Language Multi-task Learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Large language models have shown their remarkable capabilities as a general interface for various language-related applications. Motivated by this, we target to build a unified interface for completing many vision-language tasks including image description, visual question answering, and visual grounding, among others. The challenge is to use a single model for performing diverse vision-language tasks effectively with simple multi-modal instructions. 
Towards this objective, we introduce MiniGPT-v2, a model that can be treated as a unified interface for better handling various vision-language tasks. We propose using unique identifiers for different tasks when training the model. These identifiers enable our model to better distinguish each task instruction effortlessly and also improve the model learning efficiency for each task. After the three-stage training, the experimental results show that MiniGPT-v2 achieves strong performance on many visual question-answering and visual grounding benchmarks
compared to other vision-language generalist models. Our model and codes are available at \url{https://minigpt-v2.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a model called MiniGPT-v2 for image-text tasks. A pretrained ViT (from EVA) is used as an image encoder and frozen. The embeddings are downsampled and provided to the LM as tokens. For the LM, the paper uses a LLaMa2-chat 7B encoder.

The resulting model is trained on a variety of different tasks involving supervised data, e.g. VQA, captioning, referring expressions, and object detection. This is done in a multitask setting, along with LAION and CC3M text-image data. This is the first stage -- then, it is trained just on fine-grained supervised data, and then finally on multimodal instruction data from LLaVA. The LM is trained with LoRA throughout.

Overall, the paper does well on a variety of benchmarks, rivaling even specialist models that require single-task finetuning or complex ways of encoding the label space.

### Strengths
This paper seems strong to this reviewer. Not many academic papers have trained a vision-language model at this scale before, and so publishing this in a timely way will be great for the community (e.g. to use this as a baseline, or have a conversation around the role of data/training process, etc.)

### Weaknesses
One potential weakness to this reviewer is the use of supervised data throughout the training process. Training this model is expensive and so perhaps there's not budget for more ablations, but it would be interesting to see if the supervised data could be removed and so the model could truly be evaluated in a zero-shot or 'few-shot' way. It also would be good to see the impact on freezing the image encoder vs not, using LoRA vs. not, however, it's also understandable that these are expensive ablations. Nonetheless I am still solid about this paper and would vote to accept it; these questions/weaknesses shouldn't hold it back from publication.

### Questions
See weaknesses - lots of questions around which components could be removed/made simpler!

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission discusses the impressive capabilities of large language models in serving as versatile interfaces for numerous language-related tasks, sparking interest in creating a unified interface for a range of vision-language tasks such as image description, visual question answering, and visual grounding. Addressing the challenge of utilizing a single model for diverse vision-language tasks with straightforward multi-modal instructions, the authors introduce MiniGPT-v2. This model serves as a unified interface, enhancing the handling of various vision-language tasks. Unique identifiers for different tasks are incorporated during the training phase, aiding the model in easily distinguishing between task instructions and boosting learning efficiency for each specific task. Following a three-stage training process, MiniGPT-v2 demonstrates robust performance across several visual question answering and visual grounding benchmarks, outperforming other generalist vision-language models. The authors commit to making their trained models and code accessible to the public.

### Strengths
This submission demonstrates strength in several key areas. 

Firstly, the authors describe their instruction tuning setup, datasets, and training process in details. This would greatly benefit the community for future reproduction and comparison.

Moreover, the use of well-crafted illustrations enhances the understanding of the content and effectively communicates the main ideas, further solidifying its strength. Readers can easily grasp the concepts presented, adding to the submission's overall impact.

### Weaknesses
(1) Missing discussions on certain details:

* How was the “concatenate four adjacent visual output tokens” determined? Why four? Have the authors tried making the visual features even smaller (concatenate adjacent 8/16/32 etc)? Any discussions or ablations on this? The lack of ablation studies on the number of concatenated visual tokens is a significant oversight. The authors should explore the impact of different concatenation sizes on model performance, particularly on tasks requiring fine-grained spatial understanding. For instance, concatenating 8 or 16 tokens might lead to a loss of spatial resolution, which could negatively impact visual grounding tasks. Conversely, smaller concatenations might not capture sufficient contextual information. A thorough analysis of this parameter is crucial for understanding the model's behavior.

* The authors claim to use image with higher resolution (448x448). While this sounds like a intuitive motivation, it lacks solid discussion to support such a claim. How does it compare to the previous traditional setups of 224x224 or 336x336? Does using 448x448 images and then concatenating 4 adjacent visual features outperform directly using 224x224 images? The paper lacks a direct comparison between using the higher resolution (448x448) images with the proposed token concatenation and the more standard 224x224 resolution without concatenation. It is unclear if the performance gains are due to the higher resolution or the concatenation strategy or both. A direct comparison is needed to isolate the effect of each component. The authors should also discuss the computational cost associated with processing higher resolution images.


(2) Missing comparisons on certain baselines:

* How did the authors select the baseline models for each task? Why weren’t the vision-and-language foundation models listed in Table 6 being compared in Table 3 and Table 4? For instance, why Minigpt4 appeared in Table3, but mplug-owl didn’t? The selection of baseline models for each task seems pretty random, and the authors lack an explanation for such an experimental design. The selection of baselines for each task is not well-justified. The authors should provide a clear rationale for choosing specific models for comparison. The absence of certain prominent vision-and-language models, such as mPLUG-Owl, in Tables 3 and 4 raises concerns about the comprehensiveness of the comparisons. A more systematic approach to baseline selection, considering state-of-the-art models for each task, is needed to properly contextualize the performance of the proposed model.

* Another missing baseline on vision-and-language instruction following is “MIMIC-IT: Multi-Modal In-Context Instruction Tuning”.


Typo: 

* duplicated commas in the caption for Table1

### Questions
* In Section 3.2, what does it mean for “[INST] is considered as the user role, and [/INST] is considered as the assistant role”? What is the user role and what is the assistant role? Does it mean that the “[INST]” token will be followed by user input, and the “[/INST]” will be followed by the assistant’s output?

* Were the task identifier tokens and the spatial location tokens (<0>, <1>, …<100>) extended to the vocabulary as special tokens? If yes, how were the newly added tokens’ embeddings initialized?

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
The paper developed a unified interface for vision-language tasks. The proposed model MiniGPT-v2, which is a multi-modal LLM utilized distinct identifiers for each task during the training and inference. These identifiers help our model easily differentiate various tasks and also improve the learning efficiency. The experimental results show it can achieve good performance across many visual question answering and referring expression comprehension benchmarks.

### Strengths
- The paper has good novelty and contribution to the community.
- Conduct comprehensive experiments to show the effectiveness of the proposed models.
- The experimental results show its strong performance on various tasks compared to other SOTA models.
- The methodology is clear and readable.

### Weaknesses
After rebuttal: I noticed that five test sets are being used for training, especially the test sets for the referring expression comprehension task are all used in training. I am wondering if this might lead to overfitting. Personally, a better approach would be to train the model on a large-scale, generic dataset (you can use a single large-scale dataset to construct multiple tasks), and then test it on several other evaluation datasets. This might be more convincing.

- For Table 5, better to evaluate performance for other task identifiers to show the effectiveness of this.
- Discussion is a bit weak, for example, the paper should have some discussion on the error analysis and some detail on the strengths and weaknesses. 
- Should add more explanation of the evaluation metrics.
- Should add more explanation of the dataset, like what is the difference between GQA and VQA-v2, what are the sizes of them?-- 
- The model is trained with various tasks, but only evaluation on a subset of the tasks.
- The paper used single evaluation metrics to benchmark, which is not very comprehensive.

### Questions
- Can you explain why your model does not perform well on RefCOCO+ in Table 4?
- Better to give more illustration on the evaluation metrics on hallucination-CHAIR. How does this calculate? What do CHAIR_I, CHAIR_S and Len mean? How to interpret the result for three different prompts in MiniGPT-v2?
- What are the evaluation metrics for Table 3, Table 4, and Table 5? 
- “More qualitative results can be found in the Appendix “- but I did not see the Appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript introduces MiniGPT-V2, a multimodal LLM, demonstrating strong results on visual question answering and visual grounding benchmarks. The authors suggest utilizing explicit task identifiers, such as ‘[vqa]’ or ‘[grounding]’, to denote the user's intended task. Furthermore, the paper proposes a three-stage training strategy with increasing image resolution. The authors also suggest a new integration of Visual Transformer (ViT) outputs, achieved by concatenating every four adjacent visual tokens into a single token.

### Strengths
- This manuscript introduces MiniGPT-V2, a multimodal LLM, demonstrating strong results on visual question answering and visual grounding benchmarks compared to some other multimodal LLMs.

### Weaknesses
The authors suggest utilizing explicit task identifiers, such as ‘[vqa]’ or ‘[grounding]’, to denote the user's intended task. However, it is typically expected that LLMs should discern users’ intentions based solely on text inputs (dialogue history). As presented in Table 5, the addition of these explicit identifiers results in a relatively marginal performance improvement (from an average of 48.6 to 49.8). It is worth noting that if users are required to explicitly select a task, a system could alternatively leverage state-of-the-art specialized methods at a potentially lower cost. For example, BEIT-3 (2B params) could be used for Visual Question Answering with an 84% accuracy, X-VLM (500M+) for grounding achieving ~92 on the RefCOCO+ testA, and Co-DETR (348M) for object detection with COCO mAP of 66. These specialized methods may present a more optimal choice compared to the proposed MiniGPT-V2.

Furthermore, the paper proposes a three-stage training strategy with increasing image resolution. It is important to note that similar strategies have been adopted in recent works, such as Lynx and Qwen-VL. The authors also suggest a new integration of Visual Transformer (ViT) outputs, achieved by concatenating every four adjacent visual tokens into a single token. This method is proposed to reduce the sequence length, akin to the Resamplers, and the manuscript would benefit from an ablation study to substantiate the efficacy of this approach.

### Questions
n/a

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
