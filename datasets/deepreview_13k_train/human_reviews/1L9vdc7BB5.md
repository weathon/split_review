# ADAPT: Adaptive Prompt Tuning for Pre-Trained Vision-Language Models

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Prompt tuning has emerged as an effective way for parameter-efficient fine-tuning. Conventional deep prompt tuning inserts continuous prompts of a fixed context length into the input to each layer. When a pre-trained model is tailored to a specific downstream task, different layers initialized with pre-trained weights might have, depending on the distribution shift type, different levels of deviation from the optimal weights. Inserted prompts with a fixed context length might have redundant context tokens or insufficient context length. To address this issue, we propose a deep continuous prompting method dubbed Adapt that encourages heterogeneous context lengths. Context lengths are automatically determined by iteratively pruning context tokens. We use the saliency criterion for the neural network pruning to compute the importance scores of context tokens in order to determine which tokens to prune. We examine the proposed method on the pre-trained vision-language model CLIP. Extensive experiments on 11 downstream datasets reveal the advantage of Adapt: the average test accuracy increases from 79.83% to 81.70%. The highest performance gain on individual datasets is 9.63%. At the same time, the computational overheads are comparable to or smaller than baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
To address the limitations of fixed-length prompt tuning approaches for pre-trained vision-language models, the authors propose ADAPT, an adaptive prompt tuning method that dynamically determines optimal prompt lengths during fine-tuning. By employing an iterative pruning strategy, ADAPT identifies and removes less relevant prompt tokens at each layer, allowing efficient parameter usage while maintaining model performance. The authors evaluate ADAPT across 11 benchmark datasets, demonstrating that the method significantly reduces the number of parameters required while achieving competitive or improved accuracy. This adaptive approach highlights the benefits of automatic context length adjustment compared to manually designed fixed-length prompts.

### Strengths
The authors propose a novel adaptive prompt tuning approach, ADAPT, that effectively reduces the number of parameters needed for pre-trained vision-language models while maintaining competitive performance across a variety of downstream tasks. This efficiency is a notable contribution to prompt-based fine-tuning methods.
By leveraging an iterative pruning mechanism, ADAPT dynamically adjusts the prompt lengths for different layers, enabling a flexible solution that outperforms traditional fixed-length prompt tuning methods, particularly in scenarios that require task-specific adaptations.
The approach is validated on 11 diverse datasets, covering different vision-language tasks. This broad evaluation demonstrates the adaptability and applicability of ADAPT across a wide range of contexts.
The pruning process used by ADAPT results in heterogeneous context lengths, automatically determining the optimal prompt length at each layer, which is an improvement over manually designed prompts that tend to be homogeneous and less efficient.

### Weaknesses
ADAPT shows significant performance degradation in certain categories, such as the Pets class, where it fails to rank even in the top three. It is regrettable that the authors did not conduct further discussion and research on this issue.
The highly heterogeneous prompt lengths determined by the pruning mechanism could make the model harder to implement in practical scenarios where consistency and predictability are valuable, compared to using manually fixed homogeneous prompt lengths. The lack of consistent context lengths across layers may introduce challenges in hardware optimization and deployment, potentially requiring more complex memory management strategies.
Although ADAPT optimizes both text and image branches independently, there is no explicit mechanism mentioned to ensure that the branches remain aligned in terms of context length adjustments. This could potentially lead to imbalances that affect the model's overall performance, where one modality might dominate the learning process due to a significantly larger context, hindering effective multimodal fusion.

### Questions
Could the authors provide more details about the scoring function used to determine token importance during pruning? Were any alternative scoring mechanisms considered, and if so, why was the current approach chosen?
How does ADAPT ensure stability during the pruning process, especially given the highly heterogeneous prompt lengths across different layers? Are there any safeguards in place to avoid over-pruning, where the model could lose important contextual information?
The evaluation on 11 datasets showed varying degrees of performance, with some datasets exhibiting reduced accuracy compared to the baseline. Could the authors elaborate on the potential reasons behind these inconsistencies and suggest strategies that could mitigate these issues in future iterations of ADAPT?
Given the independence of the pruning processes for the text and image branches, is there any mechanism in place to maintain synchronization between the two branches during training? If not, could this lead to potential issues in multimodal understanding?

### Soundness
2

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
5

### Summary
This paper proposes a deep continuous prompting method dubbed Adapt that encourages heterogeneous context lengths.

### Strengths
-The paper is well-written.

-Extensive experiments on 11 downstream datasets reveal the advantage of Adapt.

-Adding mask to the prompts of different depth is an interesting idea.

### Weaknesses
Adding learnable mask to the prompts of different depth is an interesting idea. But, existing methods [1] proposed to add learnable mask to the parameters of CLIP. Adding learnable mask to parameters and add learnable mask to prompt have similar methods. Moreover, this paper did not discuss the difference between ADAPT and [1], which miss this key reference.

Additionally, the ADAPT does not show the advantages in few-shot learning tasks (1/2/4/8). As the number of available images decreases (from 16 shot to 1 shot), the performance advantage of this method becomes inferior to existing methods (e.g., MaPLe\MaPLe\LAMM). This indicates that the method is highly dependent on the amount of data (more than 8 shots) and is not very robust.

### Questions
-The hyperparameter T_target controls sparsity of masks. According to Table 2, the model reaches better averaged performance when T_target is set to a larger value (the masks are less sparse). What if T_target is set to a value larger than 128? What is the upper bound of the proposed method?

-Ablations on prompt depth and context length should be conducted. 

-To demonstrate the effectiveness of the proposed method on few-shot classification tasks, the paper should provide results on 1/2/4/8-shot training setting, similar to those reported in CoOP and other related studies.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper assumes that a fixed context length for prompts may lead to either redundant context tokens or insufficient context length when transferring a pre-trained model to downstream tasks. Based on this assumption, the paper proposes a method to automatically determine the prompt length.

### Strengths
The proposed method, ADAPT, changes the context lengths for different transformer layers by iteratively pruning context tokens. ADAPT surpasses the SOTA method on 16-shot image classification tasks.

### Weaknesses
It is unclear why the convergence of model training is determined solely by reaching T_target. T_target may vary across different training datasets, but it is set to a fixed value for all datasets. Additionally, if the mask for the text encoder is too sparse, this training target might restrict the sparsity of the mask for the image encoder.

The paper should provide a more detailed analysis of the learned binary masks. According to Figure 3, on the EuroSAT dataset, more context tokens are required in the middle layer of the image encoder, while the first layer of the text encoder requires more context tokens. An analysis of this discrepancy should be included.

ADAPT is trained and evaluated on the few-shot classification task, following the CoOP methodology. Thus, it should also report results under other training settings (1-shot, 2-shot, 4-shot, and 8-shot) to enable a more comprehensive comparison with state-of-the-art methods.

Moreover, UPT should be included for comparison, as it also introduces prompts in both the text and image encoders, similar to ADAPT.

### Questions
Please see the questions in Weaknesses.

### Soundness
2

### Presentation
3

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
In this paper, the authors propose adaptively pruning prompt tokens during the prompt tuning, rather than using fixed prompt length. They use metrics in network pruning to compute the importance scores of prompt tokens and prune less important tokens gradually.

### Strengths
Strength:
+The average performance on 11 downstream datasets verifies the effectiveness of the proposed methods.
+The proposed method shows slightly fewer FLOPs than existing methods.
+Adaptively changing the prompt tokens is an interesting idea.

### Weaknesses
Weakness:
1. There is more than one page to write. It looks like a paper in progress  The authors should consider to include more experiments and analysis. For example, the authors can show that different datasets prefer different prompt token lengths to verify the importance of the proposed method.

2. In line 377, the authors write “The result is shown in Appendix Figure 4. However, the appendix is missing. The authors should move it from the supplementary material to the end of the main paper.

3. How do we determine the number of tokens to prune each each layer?

4. How to set the number of prune steps rp.

5. There are too many mathematical symbols, especially in Algorithm 1, making it hard to understand, even though the operation used in this paper is easy. The authors should improve this to improve the readability.

6. There are only two paragraphs in the Introduction Section. The authors should consider splitting them into more paragraphs.

7. The proposed methods are highly related to dynamic neural networks. The authors should discuss it and cite related papers.


Issues:
In Figure1, the authors should indicate the proposed method with “Adapt (Ours)”.

### Questions
See Weakness

### Soundness
3

### Presentation
1

### Contribution
3
