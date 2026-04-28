# GPT4RoI: Instruction Tuning Large Language Model on Region-of-Interest

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 3, 6, 8

## Abstract
Visual instruction tuning large language model~(LLM) on image-text pairs has achieved general-purpose vision-language abilities. However, the lack of region-text pairs limits their advancements to fine-grained multimodal understanding. In this paper, we propose \textit{spatial instruction tuning}, which introduces the reference to the region-of-interest~(RoI) in the instruction. Before sending to LLM, the reference is replaced by RoI features and interleaved with language embeddings as a sequence. Our model \ours, trained on 7 region-text pair datasets, brings an unprecedented interactive and conversational experience compared to previous image-level models. (1) \textit{Interaction beyond language}: Users can interact with our model by both language and drawing bounding boxes to flexibly adjust the referring granularity. (2) \textit{Versatile multimodal abilities}: A variety of attribute information within each RoI can be mined by \ours, \textit{e.g.}, color, shape, material, action, \textit{etc}. Furthermore, it can reason about multiple RoIs based on common sense. On the Visual Commonsense Reasoning~(VCR) dataset, GPT4RoI achieves a remarkable accuracy of 81.6\%, surpassing all existing models by a significant margin (the second place is 75.6\%) and almost reaching human-level performance of 85.0\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to enhance current large multimodal models by injecting regional awareness. 
Authors leverage the public available regional data as the instruction data.

### Strengths
1. Both qualitative and quantitative results demonstrate that now the model can have a sense of location. 
 2. The presentation is clear. 
3. The figures are easy to read.

### Weaknesses
1. Which part of the model design leads to positional awareness is unclear. Authors have " five lightweight scale shuffle modules", "ROI Align", "add feature coordinates (Liu et al., 2018) for each level (positional embedding)", "extract region-level features with the output size of 14×14", which part really makes the model work? There is no ablation study. Specifically, it's unclear if the positional awareness stems from the learned FPN parameters, the scale shuffle modules, the coordinate embeddings, or the ROI feature itself. The lack of ablation makes it difficult to understand the contribution of each component.
2. Finetuning on a specific dataset can lead to the case that the model forgets all other knowledge. For example, fine-tuning on the multichoice dataset will lead to the case that model can not speak out natural languages whatever you ask. This raises concerns about the model's generalization ability and potential catastrophic forgetting.
3. From the qualitative examples, seems like the model can only produce short descriptions, which may not be suitable when answering with long context. I think the author's model may overfit to such datasets with short captions. The model's ability to generate detailed, contextually rich responses is questionable, especially for tasks requiring longer, more nuanced descriptions.
4. When converting LLaVa instruct dataset into the format with bounding box, I cast doubt on how accurate it is. If many instances appear in the same image, is it ok to attach so many detection results beforehand? Besides, the LLaVa instruct dataset is known to include hallucination. The process of automatically generating bounding box annotations for the LLaVa dataset is prone to errors and may introduce noise, especially in complex scenes with multiple objects. The reliance on a potentially noisy dataset raises concerns about the robustness of the training process.
5. How do authors claim on other methods which use textual coordinate as the grounding token? In this way, they can  not only use bbox as input, but also use them in output. The paper does not adequately address the existing literature on using textual coordinates for grounding, which is a significant omission given the relevance of these methods.

### Questions
1. What is the specific vision model you used? Official CLIP model does not have ViT-H at all.
2.  For each region, it is compressed into one token? It is enough?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a new approach called spatial instruction tuning, which aims to enhance the fine-grained multimodal understanding of vision-language models. The proposed model, GPT4RoI, incorporates references to regions-of-interest (RoI) in instructions by replacing them with RoI features and interleaving them with language embeddings. By training on region-text pair datasets, GPT4RoI enables interactive and conversational experiences, allowing users to interact with the model through both language and drawing bounding boxes. GPT4RoI achieves remarkable results on the Visual Commonsense Reasoning (VCR) dataset.

### Strengths
-	Fine-grained multimodal understanding: GPT4RoI enables region-level alignment and understanding by incorporating references to RoIs in instructions, allowing for more detailed analysis and reasoning.
-	Interactive user experience: Users can interact with GPT4RoI through both language input and drawing bounding boxes.
-	GPT4RoI achieves remarkable accuracy on the VCR dataset, surpassing existing models by a significant margin.

### Weaknesses
-	Expanding from image-level to region-level instruction tuning seems like a natural progression, and the approach is straightforward without providing a fresh perspective. Some other papers also explore the region-level large language models but lack the performance comparison.
-	It appears that while this paper utilized more datasets for training, the improvement in results is relatively marginal, as shown in Table 5. 
-	This work lacks a comparison of parameters. The current models seem to be quite large, especially large language models. A comparison should be conducted at the same parameter level, e.g., Table 6.

### Questions
See Weaknesses

-	Comparisons to other works on the same parameter level.

### Soundness
2 fair

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
The paper introduced the region-of-interest instruction with vision language models. By doing this, it proposed spatial instruction, combining language and the reference to region-of-interest I to an interleave sequence, enabling accurate region referring and enhancing user interaction. By spatial instruction tuning LLM with massive region-text datasets, the model can follow user instructions to solve diverse region understanding tasks, such as region caption and reasoning. The results show that the model outperforms the previous state-of-the-art approach on a wide range of region understanding benchmarks.

### Strengths
- The paper proposed a novel method with vision language tasks. It provides a detailed methodology for this.
- A comprehensive discussion of experiments and results, where the figures are in good quality and readability.
- The benchmark methods are of good quality.

### Weaknesses
After Rebuttal: Upon re-reviewing the manuscript and checking other fellow reviewers' comments, I have identified several major concerns that I previously overlooked.
- My biggest concern: the model is evaluated on the Visual Genome, Visual-7W, and VCR datasets. However, if I understand correctly, the model has been pre-trained on the Visual Genome and VCR datasets. I am therefore concerned that the model's strong performance on these two datasets is a case of overfitting, especially given that LLMs have a high capacity for overfitting. Can you provide more experimental results on different tasks and datasets (that are not used for pre-training)?
- The motivation for fusing different levels of visual and textual features is not clearly explained. More analysis on why certain levels are chosen would be helpful. Why does spatial instruction tuning yield better performance? Because more training data is used? Meanwhile, can you please provide statistics on the amount of training data used in the baselines in the tables? It could show whether the performance improvement of the model is due to the proposed method or more amount of training data.
- There are no ablation studies showing the contribution of individual components like visual encoders, textual encoders etc. 
- (Minor concerns) How sensitive is the model to the choice vision encoders? What is the training and inference time compared to baseline models? Does the model exhibit biases like relying more on textual or visual features for certain question types?

Given the potential for overfitting, I find it necessary to adjust my score to 6. However, I would still vote to accept the paper. Many thanks! (btw, I apologize for the delayed response)

Original: For region caption, the paper only compares the proposal to one model GRiT, which is limited.

### Questions
Please see above for details:
Can you interpret the performance of different tasks (ie Q->A, QA-> R, Q->AR) in Table 6?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission proposes a finer-grained visual instruction tuning to endow a pretrained large language model with the capabilities to “see.” Compared to the literature, this work is different in that it has region-level image understanding and flexibility in combining multiple ROI’s and reasoning between them. It initializes the model from pretrained on vision and language tasks, respectively, and then uses a two-step instruction tuning pipeline to build multiple visual reasoning capabilities into it.

### Strengths
In general, the motivation, technique, presentation, and results look all solid to me. The anonymously released codebase looks usable, which, if true, would serve as a well-compiled dataset and starting point for later multi-modality research.

### Weaknesses
I have to say I haven’t followed multimodality research for some time, so my judgment on the novelty of this work (compared to the literature) could be rusty. This might be an important aspect to consider for this work, but my score is assuming this work is novel. 

On presentation, a flowchart of the two-stage training process might be useful to readers. Indicating which datasets are used in which fashion at which stage, with the purpose of bringing about which kind of capabilities.

### Questions
Some of my random thoughts, potentially useful to the authors:
(1)	How about visual question-answering datasets? 
(2)	Is it possible to design some synthetic tasks to train the model, perhaps inserted between the two stages you have right now, to smooth up the training process?
(3)	Is it possible to let the LM output coordinates somehow so to interact with users by referring to certain regions in the picture?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
