# SAMRefiner: Taming Segment Anything Model for Universal Mask Refinement

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we explore a principal way to enhance the quality of widely pre-existing coarse masks, enabling them to serve as reliable training data for segmentation models to reduce the annotation cost. In contrast to prior refinement techniques that are tailored to specific models or tasks in a close-world manner, we propose SAMRefiner, a universal and efficient approach by adapting SAM to the mask refinement task. The core technique of our model is the noise-tolerant prompting scheme. Specifically, we introduce a multi-prompt excavation strategy to mine diverse input prompts for SAM (\ie, distance-guided points, context-aware elastic bounding boxes, and Gaussian-style masks) from initial coarse masks. These prompts can collaborate with each other to mitigate the effect of defects in coarse masks. In particular, considering the difficulty of SAM to handle the multi-object case in semantic segmentation, we introduce a split-then-merge (STM) pipeline. Additionally, we extend our method to SAMRefiner++ by introducing an additional IoU adaption step to further boost the performance of the generic SAMRefiner on the target dataset. This step is self-boosted and requires no additional annotation. The proposed framework is versatile and can flexibly cooperate with existing segmentation methods. We evaluate our mask framework on a wide range of benchmarks under different settings, demonstrating better accuracy and efficiency. SAMRefiner holds significant potential to expedite the evolution of refinement tools, and we will release it as a convenient post-processing toolkit.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes SAMRefiner, a novel framework for mask refinement using the Segment Anything Model (SAM). It contains several techniques: noise-tolerant prompting scheme, split-then-merge strategy, and IoU adaption. By combining these techniques, the proposed SAMRefiner improves the quality of the SAM-generated masks.

### Strengths
1. The proposed SAMRefiner offers a unique solution to the mask refinement problem, which is an important yet under-explored area. By adapting SAM for this task, the authors address a practical issue of improving the quality of pre-existing coarse masks, which can have significant implications for reducing annotation costs and enhancing the performance of downstream segmentation models.

2. The introduction of the noise-tolerant prompting scheme, including the multi-prompt excavation strategy, is interesting. 

3. The split-then-merge (STM) is a practical solution to handle the challenges of multiple objects in the mask. 

4. The IoU adaption step is another interesting technique. By introducing a self-boosted method to enhance SAM's IoU prediction ability on specific datasets using coarse mask priors, the authors demonstrate a way to further improve the performance of the framework without additional annotation.

5. The authors conduct a comprehensive set of experiments on various benchmarks, including DAVIS-585, COCO, and PASCAL VOC, under different settings (such as instance and semantic segmentation with incomplete supervision). This wide range of evaluations helps to demonstrate the versatility and effectiveness of SAMRefiner in different scenarios.

6. The comparison with state-of-the-art model-agnostic refinement methods is thorough. The detailed performance metrics presented (e.g., IoU, mask AP, mIoU) and the analysis of the results provide strong evidence of the superiority of SAMRefiner in many cases, especially in terms of its robustness to mask noise and its ability to improve performance across diverse datasets.

### Weaknesses
1. The explanation of how the proposed method overcomes the limitations of SAM in handling multi-object cases, especially in the context of semantic segmentation, could be more detailed. While the STM pipeline is introduced, its interaction with the overall framework and the specific advantages it brings compared to other possible approaches are not entirely clear. In addition, I suggest the authors to use a flowchart and visualize some examples after each stage in STM.

2. Although the paper compares with several state-of-the-art refinement methods, it could provide a more in-depth analysis of why some methods perform better or worse in different scenarios. For example, a more detailed discussion of the differences between SAMRefiner and methods like CascadePSP and CRM in terms of their design principles and how these differences lead to performance variations would be beneficial. It is better to compare the key design principles of SAMRefiner with others in a table or a figure.

3. Some implementation details are missing or could be further elaborated. For instance, the specific hyperparameters used in different experiments (beyond the ones mentioned for the IoU adaption step) are not always clearly stated. This makes it difficult for other researchers to fully reproduce the experiments and evaluate the method under different conditions. The authors are suggested to include these implementations and put them in the appendix.

4. The paper would benefit from more visualizations to support the understanding of the proposed method and the experimental results. For example, visual comparisons of the mask refinement process using different prompts and techniques could provide a better understanding of how the method works and why it is effective. Additionally, visualizations of the failure cases and their analysis could help to identify the limitations of the method more clearly.

### Questions
See "Weakness"

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to adapt the segment anything model for the mask refinement task. It aims to go beyond the previous mask refinement networks that are 1) model-dependent, 2) task-specific, and 3) category-limited. It also aims to improve the time efficiency of the existing method. The key of the proposed method is prompting SAM through prompt excavation design and IoU adaptation.  To this end, the proposed method has been validated over DAVIS-585 (mask refinement), COCO (instance segmentation), and VOC (semantic segmentation).

### Strengths
Given that inaccurate pseudo-labels and coarse human annotations are widely used to train the deep segmentation model, mask refinement is a meaningful task to improve the training data and inference performance. Specialized deep learning mask refinement methods and non-learning-based methods have been proposed previously. However, they either fail to generalize to more diverse tasks or are limited in being adaptive to different samples. The proposed method, SAMRefiner,  aims to adapt SAM, a segmentation foundation model for different masks, which is of practical meaning. 

The key contribution of the proposed method is to design noise-tolerant prompts based on the coarse mask. Since SAM is trained in a specific way of prompt combination. The author designed several strategies to adapt the SAM for the mask refinement task by combining point, box, and mask prompt. 

Besides, IoU adaptation is used to adapt SAMRefiner for tasks and dataset-specific applications.

### Weaknesses
I have concerns about the novelty and the experiment:

1. Point Prompts Sampling Method: The distance-based sampling method used is not original, as it is a widely adopted approach for evaluating interactive segmentation models. The author suggests sampling one positive and one negative point, but there is no ablation study to support this design choice (e.g. why not other numbers). Different samples or tasks may have varying characteristics, so the author should provide analysis or empirical ablation to justify this approach.

2. Box Prompt Generation Method: Similar concerns apply to the box prompt generation method. A simple baseline would be to take the bounding box over the coarse masks. The appropriateness of the proposed method heavily depends on the quality and characteristics of the coarse mask. While the author provides an ablation study using coarse masks generated by PointWSSIS, this is specific to the dataset and method. The author claims the proposed method is general, but additional analysis or empirical observations are needed to support this claim. The authors are suggested to evaluate the box prompt generation method on a wider range of datasets and coarse mask types to demonstrate its generality. Additionally, proposing a comparison against simpler baselines like the tight bounding box across various datasets would more clearly show the advantages of the proposed approach.


3. Effectiveness of the Gaussian-Style Mask: I question the effectiveness of the proposed Gaussian-style mask compared to directly using the coarse mask. Although there is an ablation study in Figure 7 of the Appendix, no experiments address the scenario where the coarse mask is used in the first iteration. Despite potential noise, the coarse mask may still be more informative than a Gaussian-style mask based solely on the distance to a central point, especially for objects with complex structures. The description of “Considering the inaccuracy of coarse mask” is vague, and the author should provide more context on the advantages of the proposed method.  The author is advised to provide more detailed analysis or examples of when and why the Gaussian-style mask is advantageous over the coarse mask.

4. IoU Adaptation: The IoU adaptation strategy seems questionable. When multiple prompts are provided, SAM is trained to predict only one mask via the fourth output token, and the three masks corresponding to the first three output tokens are not utilized. The author proposes a multi-prompt strategy for SAM, but in this context, using the three masks from the single prompt-only scenario seems unnecessary. Additionally, the proposed IoU selection strategy does not show significant improvement (87.1 vs 86.9), as the three predictions converge. I would like the author to clarify why they use the three masks from the single-prompt scenario in their multi-prompt strategy. Additionally,  the author should also provide a more in-depth analysis of the benefits of their IoU adaptation approach given the small improvement observed. For instance, it would be beneficial to examine specific cases where it provides more significant gains.

### Questions
See the weakness

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
3

### Summary
The paper introduces SAMRefiner for refining coarse masks using the SAM. SAMRefiner utilizes a prompting scheme that generates varied prompts to address defects in initial masks, making it robust across different segmentation tasks. The paper also presents an extended version to add an IoU adaptation step to improve performance without requiring extra annotations. Experiments show that the proposed method enhances mask accuracy and efficiency, offering potential for reducing annotation efforts in training segmentation models.

### Strengths
1. This work introduces a novel method to enhance downstream segmentation models using SAM.
2. The exploration of prompt design in SAM is thorough, with comprehensive ablation studies provided to validate the design choices.
3. The IoU adaptation is interesting and provides new insights into SAM’s IoU prediction.
4. Overall, the paper is well-written, with elaboration on the prompt design.

### Weaknesses
1. Although this paper presents technical novelty, it needs to address a fundamental issue. For instance, the comparisons in Tables 3 and 6 involve SAMRefiner using SAM trained on a larger dataset, which introduces fairness concerns. To address this, the core of the paper should focus on how to better utilize SAM to enhance segmentation models. Indeed, the use of SAM is not limited to the refinement of Coarse Masks to indirectly improve downstream segmentation models. Alternative methods, such as straightforward distillation or the use of pre-trained weights, could also be explored. The paper should demonstrate the advantages of the proposed method in utilizing SAM from perspectives of training costs and downstream model performance, to justify its practicality and address fairness concerns.

2. The description of the IoU Adaptation section is somewhat confusing. It would benefit from using more precise symbols to differentiate between different types of IoU and to clearly describe the corresponding training strategy.

### Questions
Based on the concerns raised in the weaknesses section, please explain in detail the direct advantages of using SAMRefiner to enhance downstream segmentation model performance compared to the simple use of SAM, such as through distillation or pre-trained weights.

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
This paper proposes a new method to refine coarse segmentation masks by utilizing the Segment Anything Model (SAM). The method simultaneously leverages point-, box-, and mask-based prompts to produce high-quality refined masks. Additionally, an IoU-based adaptation method is proposed to improve the performance of the IoU head. Experiments on multiple tasks and datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper is well written and easy to follow. 
2. The proposed method seems to be reasonable. The new designs of the point-, box-, and mask-based prompts used in this paper are novel and interesting.
3. The experiments are relatively comprehensive, demonstrating the effectiveness of the method across multiple tasks.

### Weaknesses
1. The performance of SAMRefiner++ is not reported in the experimental section, thus the effectiveness of the proposed IoU adaptation method cannot be evaluated.
2. It would be interesting if the authors could analyze the robustness of the method. For example, can the proposed method still maintain good performance when the initial mask becomes coarser?
3. As shown in Table 2(a), the proposed distance-guided point sampling method performs significantly better than the box center method. Therefore, it is suggested to provide a more detailed explanation of the advantages of the distance-guided method over the box center approach.
4. This method involves a lot of hyperparameters, such as λ, μ,  ω, and γ. It is suggested to include an ablation study on these hyperparameters for a more comprehensive evaluation.

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
4

### Contribution
3
