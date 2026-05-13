# OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision

- Decision: Accept
- Scores: 6, 5, 6, 6, 6

## Abstract
Instruction-guided image editing methods have demonstrated significant potential by training diffusion models on automatically synthesized or manually annotated image editing pairs. However, these methods remain far from practical, real-life applications. We identify three primary challenges contributing to this gap. Firstly, existing models have limited editing skills due to the biased synthesis process. Secondly, these methods are trained with datasets with a high volume of noise and artifacts. This is due to the application of simple filtering methods like CLIP-score. Thirdly, all these datasets are restricted to a single low resolution and fixed aspect ratio, limiting the versatility to handle real-world use cases.
In this paper, we present OmniEdit, which is an omnipotent editor to handle seven different image editing tasks with any aspect ratio seamlessly. Our contribution is in four folds: (1) OmniEdit is trained by utilizing the supervision from seven different specialist models to ensure task coverage. (2) we utilize importance sampling based on the scores provided by large multimodal models (like GPT-4o) instead of CLIP-score to improve the data quality. (3) we propose a new editing architecture called EditNet to greatly boost the editing success rate, (4) we provide images with different aspect ratios to ensure that our model can handle any image in the wild. We have curated a test set containing images of different aspect ratios, accompanied by diverse instructions to cover different tasks. Both automatic evaluation and human evaluations demonstrate that OmniEdit can significantly outperforms all the existing models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
OMNI-EDIT is an image editing model designed to address the skill imbalance issues present in existing instruction-based image editing methods. It learns by combining supervision from seven different expert models and utilizes InternVL2 for data scoring. Additionally, this approach introduces a diffusion-Transformer architecture named EditNet.

### Strengths
1. The authors collected a high-resolution dataset covering seven types of tasks, annotated through multiple expert models, and used InternVL2 to score the dataset. 

2. And they introduced EditNet, which enhances image noise control capabilities compared to ControlNet.

3. In the Omni-Edit-Bench benchmark, OMNI-EDIT outperformed existing baseline models across multiple evaluation metrics.

### Weaknesses
1. Lack of testing of GPT4-o generated CONFIDENCE SCORE, LLM may be subjective and biased

2. Limitations of the benchmarking dataset: The Omni-Edit-Bench dataset used in the paper is small (only 62 images), which may limit the reliability and generalization of the model evaluation.

### Questions
1. Since the dataset is divided into seven types of tasks, would it be possible to categorize the test set similarly? This would allow for a more detailed evaluation of the model's performance across different editing tasks and facilitate an analysis of performance differences and underlying reasons.

2. The relatively small size of the Omni-Edit-Bench dataset may limit the reliability and generalizability of model evaluation. It is recommended to assess performance on additional benchmark datasets. For example, are there results available on the Emu Edit test set?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces OMNI-EDIT, an advanced image editing model addressing current limitations such as biased training data, noise, and fixed aspect ratios. It uses supervision from multiple specialist models, improved data quality via importance sampling with large multimodal models, and a new architecture called EditNet for better editing performance. OMNI-EDIT supports various aspect ratios and outperforms existing models in evaluations.

### Strengths
--The paper introduces OMNI-EDIT to address limited editing capabilities, poor data quality control, and lack of support for varying resolutions, which are critical point in image editing method.

--The use of importance sampling with high-quality data scoring via distilled multimodal models (such as InternVL2) demonstrates a meticulous approach to data curation

--The paper is clearly structured, with each contribution outlined and explained in detail. The authors provide a logical flow that makes it easy for readers to understand how OMNI-EDIT was developed.

### Weaknesses
1. The primary concern with this paper is its similarity to a CVPR 2024 paper [1], which proposed a generalist modeling interface that formulates most vision tasks as instruction-based editing. In contrast, the proposed paper is simpler and more direct as it focuses on building a generalist model specifically for editing tasks rather than all vision tasks. The training approach is similar to [1] which also involves generating data using current specialist models. This reduces the contribution of leveraging specialist models to train the generalist model. Additionally, the experimental results lack a comparison with [1], which would be necessary to highlight differences.

2. Although the paper claims that the model supports inputs of varying sizes and resolutions, there does not appear to be a detailed explanation of this in the methodology or experimental sections. This is crucial information, as it raises questions about how this feature is implemented and whether it involves any novel techniques. Specifically, it is unclear if the model uses a fixed or variable positional encoding scheme, and how this impacts the model's ability to generalize across different aspect ratios and image sizes. The lack of discussion on this aspect makes it difficult to assess the robustness of the proposed approach.

3. The training data for Omni-Edit consists of 505K samples, all generated by specialist models and selected using importance sampling. It would be beneficial to discuss whether different training data sizes affect the model’s results. It is also unclear how the importance sampling is implemented and what criteria are used to determine the quality of the generated samples. A more detailed analysis of the impact of data quality and quantity on the final performance of OMNI-EDIT is needed.

4. Some specialist models mentioned training an image-inpainting model, but there seems no description of the training data for specialist models. This makes it difficult to assess the quality of the specialist models and their potential impact on the final results. The lack of details on the training data for these models raises concerns about the reliability of the generated data.

5. The overall framework is complex, requiring the training of specialist models, a score prediction model for importance sampling, and finally the Omni-Edit model with all the collected data. And such a process makes it difficult to dynamically include more editing tasks. The multi-stage training process introduces additional complexity and potential points of failure, which could limit the scalability and adaptability of the framework.

6. There seems to be unnecessary "5" in Lines 361 and 362.

7. Typo: In Line 246, "for the our editing model".

### Questions
1. How does this paper differentiate itself in terms of contributions from the CVPR 2024 paper [1], given their similar focus on generalist instruction-guided modeling?

2. It would be better to compare the proposed method with the generalist modeling approach in [1].

3. Can the authors provide more detail on how the support for multi-size and multi-resolution inputs was implemented? What specific innovations, if any, were introduced to achieve this?

4. How does the training data size affect the performance of OMNI-EDIT? 

5. Could the authors elaborate on the training process and datasets used for the specialist models, such as the image-inpainting model?

### Soundness
3

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
3

### Summary
This paper presents a new multi-task image editing model. The key contributions of this paper includes (1) framework for learning generalist from data generated from a set of specialist models, (2) scoring of data generated from specialist using a finetuned VLM model, (3) control-net like architecture with DiT. Authors conducted experiments to compare multiple recent methods and did a nice ablation study analyzing components of the proposed model.

### Strengths
1. The paper is well-written and easy to read.
2. The proposed method pipeline sound reasonable.
2. Experiments are reasonable with comparisons to many recent methods, and good ablation study.

### Weaknesses
1. Lacks novelty. The most significant novel idea of this paper is to train specialist editing models to generate training data for training unified generalist editing model. This idea is quite straightforward and I think many existing multi-task generation models mixes data from different sources, either existing data, or data generated by some models (can be specialist) for joint training from multiple data sources.
2. Results quality. The visual results are not impressive (shadow/reflection is left after removal, inpainting/visual artifact in several results, cartoonish object generated given photo-realistic background, change color instruction lead to texture changes, etc.)

### Questions
1. The authors rely on GPT 4o knowledge to build the scoring model. How robust is the scoring model with InternVL in ranking the quality of the data point, how's the accuracy level in general? 
2. Could the scoring model be further improved by finetuning with human labeled GT data?
3. It seems the inpainting specialist model cannot handle shadow/reflection. Any idea to improve it?
4. Authors rely on half synthetic data for training, is the trained model affected by the inpainting artifact caused by the synthetic generation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an effective editing image training data generation process and a new model structure EditNet for general image editing of various image resolutions. The paper proposes to train and utilize seven different specialist image editing models to generate training data and use LLM to filter good-quality images, the paper also proposes a modified model backbone for general image editing capability training. The proposed method is trained on the OMNI-EDIT training dataset and experiments are conducted on the proposed OMNI-EDIT-Bench.

### Strengths
1. The proposed training data generation process using seven different specialist models and a better filtering method is novel and reasonable.
2. The modification from simple ControlNet + DiT to the proposed EditNet especially on accessing intermediate presentations and updating text presentations is interesting.
3. The results are strong in both quantitative metrics and qualitative assessments."

### Weaknesses
1. I would recommend updating Figure 3, the color of the frozen DiT model is near the same as the white background making readers difficult to comprehend.
2. It would be better if the paper could also include a walkthrough caption other than the only training pipeline image in Figure 2.

### Questions
1. I have a question about the generalization ability of the OMNI-EDIT. Since the seven specialist models are trained on their pre-defined tasks, will OMNI-EDIT have the ability to generalize to editing instructions beyond these seven (for example move a person from right to left)?
2. Ideally the specialist model should generate close to perfect edited data, but in real scenarios, for some tasks, a trained specialist model may still not generate great data. Do you encounter this situation where a large portion of the generated data are filtered leading to a small proportion in the final training dataset? Will this data unbalancing affect the model's performance?
3. Can we have some visualization examples of your proposed training data and benchmark?

### Soundness
3

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
This paper builds an instruction-based image editing method using synthetic data from 7 specialists. The major contributions include: 1) Curated an (image, editing instruction) dataset for seven editing tasks using the importance sampling strategy; 2) Proposed a ControlNet-like image-editing architecture to achieve these tasks. Experiments show that Omni-Edit outperforms existing approaches after training the proposed model on the curated dataset.

### Strengths
1) The curated dataset greatly expands the instruction-based image editing datasets with multiple specialists.

2) The paper standardizes the procedure to automatically generate the trainig data for 7 image editing tasks.

3) The proposed method performs well on both automatic metrics and user studies.

### Weaknesses
1) The ablations are not comprehensive. Since the authors claim the new dataset and their model are two separate contributions, they could compare with existing methods trained on their dataset and their method trained on the existing dataset to validate each contribution. For example, the authors can report the results of CosXL-Edit trained on Omni-Edit-Bench. The lack of a direct comparison makes it difficult to isolate the impact of the dataset versus the model architecture. Specifically, it would be beneficial to see how a strong baseline model like CosXL-Edit performs when trained on the Omni-Edit dataset, and conversely, how the proposed model performs when trained on a comparable existing dataset. This would provide a more granular understanding of each contribution's effectiveness.

2) L433 states that while prior methods struggle to perform editing for non-squared images, the proposed method can handle multiple resolutions. However, only two visualized examples are provided in the paper, which is not convincing. I suggest the authors report quantitative results on non-squared images. The claim about handling non-squared images needs more rigorous validation. The current visual examples are insufficient to demonstrate consistent performance across various aspect ratios and image resolutions. Quantitative metrics, such as those used for evaluating editing quality on square images, should be applied to non-squared images as well to provide a more robust assessment.

### Questions
1) Will the dataset be released?

2) When constructing the training data for object removal, how to ensure the generated content in the removal area will be background instead of a new object?

3) Could the authros provide visualized examples of (src image, tgt image, instruction) in the training set for each task?

4) In Tab. 1, It is unclear how different methods are evaluated on their image editing capabilities. Were user studies conducted to get the star ratings? Or are they rated by some automatic metrics? 

5) MagicBrush is a human-annotated dataset that also includes 7 tasks. How does the data quality of the synthetic dataset introduced in this paper compare with MagicBrush? Is there a quantitative evaluation?

### Soundness
2

### Presentation
3

### Contribution
2
