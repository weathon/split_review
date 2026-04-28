# Multi-Reward as Condition for Instruction-based Image Editing

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
High-quality training triplets (instruction, original image, edited image) are essential for instruction-based image editing. Predominant training datasets (e.g., InsPix2Pix) are created using text-to-image generative models (e.g., Stable Diffusion, DALL-E) which are not trained for image editing. Accordingly, these datasets suffer from inaccurate instruction following, poor detail preserving, and generation artifacts. In this paper, we propose to address the training data quality issue with multi-perspective reward data instead of refining the ground-truth image quality. 1) we first design a quantitative metric system based on best-in-class LVLM (Large Vision Language Model), i.e., GPT-4o in our case, to evaluate the generation quality from 3 perspectives, namely, instruction following, detail preserving, and generation quality. For each perspective, we collected quantitative score in $0\sim 5$ and text descriptive feedback on the specific failure points in ground-truth edited images, resulting in a high-quality editing reward dataset, i.e., RewardEdit20K. 2) We further proposed a novel training framework to seamlessly integrate the metric output, regarded as multi-reward, into editing models to learn from the imperfect training triplets. During training, the reward scores and text descriptions are encoded as embeddings and fed into both the latent space and the U-Net of the editing models as auxiliary conditions. During inference, we set these additional conditions to the highest score with no text description for failure points, to aim at the best generation outcome. 3) We also build a challenging evaluation benchmark with real-world images/photos and diverse editing instructions, named as Real-Edit. Experiments indicate that our multi-reward conditioned model outperforms its no-reward counterpart on two popular editing pipelines, i.e., InsPix2Pix and SmartEdit. The code and dataset will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a high-quality editing reward dataset to address the problem of editing effectiveness due to training data quality issues with instruction-based image editing methods. This dataset contains assessment scores and reward texts, which are introduced as additional conditions to the instruction-based editing model to improve the model's ability. The authors also introduce an evaluation set to assess the quality of the instruction-based image editing model from multiple dimensions. Qualitatively and quantitatively, it is demonstrated that the present method effectively improves the quality of the instructional editing model.

### Strengths
1.	A novel reward-based instruction editing framework that introduces evaluation scores for VLLM as well as rewarding textual feedback to improve the capability of instruction editing models. 
2.	The creation of Real-Edit provides a standardized approach to evaluate instructional editing methods in different scenarios.
3.	The method shows superior performance in both quantitative metrics and qualitative results, indicating robust editing capabilities.

### Weaknesses
1. Both the quantitative assessment in Table 1 and the training strategy are based on the same scoring strategy for the GPT-4o, making the evaluation of the results overly dependent on the a priori of the VLLM and making it difficult to objectively validate the strengths of this method. One solution to this dilemma is to use other assessment metrics (e.g., CLIP scores) on the three dimensions to be adopted for comparison with other methods.
2. While experiments have shown that the introduction of additional reward text can improve image editing, unfortunately, there is no analysis of why introducing negative text in this way could help guide the diffusion process towards more effective editing.
3. Are there limitations to the introduction of the dataset REWARDEDIT-20K. Different instructional editing models may have been obtained by tuning on different training sets [1][2]. While this paper achieved an advantage on Ins-Pix2Pix and its improved version SmartEdit, is it still desirable to train other models using REWARDEDIT-20K obtained from the Ins-Pix2Pix training set?

### Questions
Please refer to the weaknesses.

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
This paper aims to correct the noise supervision in instruction-based image editing models by using multi-view reward data as an additional condition. To achieve this, the authors collected a dataset named RewardEdit-20K, which contains 20,000 instances of multi-view reward data.

### Strengths
1. This paper intorduce  a multi-view reward mechanism, instead of directly improving the quality of ground-truth images, the authors utilized GPT-4o to evaluate the training data from three key perspectives: instruction adherence, detail preservation, and generation quality.

2.The RewardEdit-20K dataset and the Real-Edit evaluation benchmark.

### Weaknesses
1. The multi-view reward mechanism used in this paper relies entirely on GPT-4o’s evaluation. Although GPT-4o demonstrates strong capabilities in understanding and generating natural language, it may not fully capture the subtle nuances of human perception regarding image editing quality. Specifically, the reliance on a single model for evaluation introduces a potential bias, as the model's understanding of 'quality' may not align perfectly with human aesthetic judgments or specific editing goals. This could lead to the model optimizing for metrics that do not fully reflect real-world editing needs.

2. The cost for this reward is expensive as it using GPT4-o . The financial cost of using GPT-4o for generating rewards is a significant practical limitation. While the authors mention the cost per token, the cumulative expense of evaluating a large dataset, especially during iterative training, could be substantial. This cost could hinder the scalability and accessibility of the proposed method, particularly for researchers with limited resources. Furthermore, the reliance on a proprietary model introduces a dependency that could be problematic if the API access or pricing changes.

### Questions
1. The human evaluations showed slightly lower scores than those generated by GPT-4o, though both showed consistency in ranking. Could the authors provide insights into why this discrepancy exists?

2.Given the reliance on the RewardEdit-20K dataset, a more detailed release plan for this dataset (and possibly pretrained models) could be helpful.

3. While the approach shows significant improvements, an analysis on instances where the multi-reward mechanism fails or provides subpar results would be beneficial. Understanding the limitations could offer insights for future iterations or refinements of the method.

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
3

### Summary
This paper identifies significant issues related to data quality in the current Image Edit dataset. It proposes a pipeline for data cleaning and scoring using MLLM and introduces a cleaned dataset along with a training framework designed for multi-reward scenarios.

### Strengths
- This paper discusses the issues present in the current dataset and utilizes MLLM for data cleaning. Through experiments and comparisons, it demonstrates the effectiveness of the cleaned dataset and the new training methods.
- Good writing and detailed experiments make this paper compelling.

### Weaknesses
 - W.1: The paper lacks a comparison with RL in T2I methods like DPO-Diffusion[1]. If I understand correctly, I believe that the Multi-Reward Framework is conceptually similar to methods like DPO-Diffusion. Therefore, I think it is reasonable and necessary to articulate the comparisons and distinctions between these approaches, especially the method difference.
- W.2: The article lacks some novelty. Of course, high-quality and abundant data can effectively enhance model performance, so I am uncertain about the extent to which the proposed Multi-Reward Framework improves upon traditional methods. For example, in Table 1, additional editing data (0.02M) was used for training. I believe it is fair to compare it with the exact same data using the same baseline method; otherwise, it is difficult to convince me whether the improvement comes from the high-quality data or the architecture. Perhaps experiments on the unprocessed REWARDEDIT-20K data could be added for comparison.

### Questions
See above, especially W.1

### Soundness
3

### Presentation
3

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
This paper introduces a dataset and benchmark for assessing image editing performance across multiple dimensions. The authors also utilize these multi-dimensional scores as rewards to enhance the effectiveness of image editing models.

### Strengths
1. The paper underscores a valuable methodology for evaluating image editing datasets, which is highly beneficial in practical applications.
2. It proposes the use of evaluation scores to boost the performance of image editing models, which is novel in image editing.

### Weaknesses
1. Although the use of GPT-4o for evaluation is efficient in practice, it lacks guaranteed consistency. The evaluation results could be influenced by underlying changes in GPT-4o, rendering the results unreliable. The reliance on a closed-source model like GPT-4o introduces a black-box element, making it difficult to understand the nuances of the evaluation process. Specifically, the lack of transparency in GPT-4o's scoring mechanism raises concerns about the reproducibility and interpretability of the results. An alternative solution to this issue could be to train an independent evaluation model with a well-defined architecture and training data, allowing for more control and transparency.

2. The RewardEdit-20K dataset continues to utilize images generated by InstructPix2Pix's model. For some challenging editing samples, scores cannot exceed 2 points. Even if the reward model can enhance performance in other samples, can it generate better results for these difficult cases generated by InsPix2Pix? The dataset's inherent limitations, stemming from the initial generation process, might restrict the potential of the proposed reward model. It is unclear if the reward model can overcome the limitations of the initial dataset, particularly in cases where the initial edits are of low quality. This raises questions about the generalizability of the proposed approach.

3. There is a lack of detailed analysis on the individual impact of each perspective reward on the improvement of editing models. Including such insights in an ablation study could strengthen the paper's contribution. The paper does not provide a clear understanding of how each reward component contributes to the overall performance. Without a detailed ablation study, it is difficult to assess the relative importance of each reward and to identify potential redundancies or conflicts between them. This lack of granularity limits the interpretability of the results.

4. The practice of incorporating additional "reward scores" to enhance image generation quality is already established within the stable diffusion community (see https://civitai.com/articles/4248/what-is-score9-and-how-to-use-it-in-pony-diffusion). A more thorough discussion linking the proposed multi-reward framework to existing methodologies would enrich the manuscript's contribution. The paper fails to adequately position its work within the broader context of reward-based image generation techniques. The absence of a detailed comparison with existing methods limits the novelty and impact of the proposed approach. A more comprehensive discussion of the similarities and differences between the proposed method and existing techniques is needed.

### Questions
1. Could you elaborate on the dimensionality of $c_R$ and $Linear(c_R)$, and explain how lines 281 and 287 can be implemented, given that both use the same notation of $Linear(c_R)$?
2. In line 369, is there a specific reason for training at a resolution of 256? Wouldn't training and inference at 512 yield better results?
3. Are the trained modules shared or trained separately between InstructPix2Pix and smartEdit?

### Soundness
3

### Presentation
3

### Contribution
2
