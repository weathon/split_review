# Multiview Equivariance Improves 3D Understanding with Minimal Feature Finetuning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Vision foundation models, particularly the ViT family, have revolutionized image understanding by providing rich semantic features. However, despite their success in 2D comprehension, their abilities on grasping 3D spatial relationships are still unclear.
In this work, we evaluate and enhance the 3D awareness of ViT-based models. We begin by systematically assessing their ability to learn 3D equivariant features, specifically examining the consistency of semantic embeddings across different viewpoints. Our findings indicate that improved 3D equivariance leads to better performance on various downstream tasks, including pose estimation, tracking, and semantic transfer. Building on this insight, we propose a simple yet effective finetuning strategy based on 3D correspondences, which significantly enhances the 3D correspondence understanding of existing vision models. Remarkably, even finetuning on a single object for just one iteration results in substantial performance gains. All code and resources will be made publicly available to support further advancements in 3D-aware vision models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper evaluates 2D ViT-based foundation models' abilities to learn 3D equivariant features, shows the significance of 3D equivariant on 3D downstream tasks (pose estimation, video tracking, and semantic correspondence), and proposes a very simple finetuning strategy that boosts the 3D understanding abilities of these existed 2D foundation models by introducing 3D information from either synthetic data (Objaverse) or real data (MVImgNet).

### Strengths
1. The proposed finetuning strategy is simple to adopt and easily reproducible. Finetuning shows performance boost with even only one additional sample.

2. The experiments are comprehensive, covering three main downstream tasks of 3D equivariant features (one-shot object pose estimation, video tracking and semantic correspondence), highlighting the significance of 3D equivariant features. 

3. The paper discusses finetuning using different types of data (synthetic data, real data and scenes), and conducts good ablations of the model's design (added conv head).

### Weaknesses
Minor concerns:
1. Table 1 ablates on number of added conv layers to a given ViT, and one additional conv head gives best performance boost instead of two or three. Some analysis of why this is happening will be nice. 

2. The whole paper lacks some mathematical formulation and explanation. For example, there is no formula for two evaluation metrics define in the paper: APE and PCDP. Also, it does not have math for the loss (SmoothAP). Some additional math can be more followable than text.

### Questions
Please refer to the weakness part for my questions. 

Overall, this works presents an interesting yet very simple method that is easily reproducible to make 2D vision model generates better 3D equivariant features, and I believe it can benefit the community.

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
In this work the authors studied the importance of multiview equivariance for the tasks of pose estimation, video tracking, and semantic correspondence. Results show that vision models with better multiview equivariance also achieve better performance for the three downstream tasks. Moreover, by finetuning the model on synthetic multi-view images, models with better equivariance perform better on various tasks.

### Strengths
1. The authors studied the multiview equivariance property of vision foundation models, and associate it with the performance of three downstream tasks. This enable a more systematic way to analyze the part correspondence of vision models and help to understand the limitations of models on downstream tasks.
2. The authors proposed to finetune the model with multi-view synthetic images, improving multiview equivariance and downstream tasks. This proposed approach is straightforward but demonstrated effective on downstream tasks.

### Weaknesses
1. The three tasks considered in this paper, (keypoint-based) pose estimation, video tracking, and semantic correspondence, are all ultimately part correspondence problem, which benefits from multiview equivariance. The title and introduction gives the impression that multiview equivariance improves 3D understanding in general, but truly the experiments only focused on very specific tasks.
2. I understand that pose estimation is a 3D understanding problem, but I don't think video tracking and semantic correspondence falls into the picture of 3D understanding, given the title of the paper. Specifically how this paper fits into the analysis of 3D awareness considering previous works [A,B].
3. The authors argued the importance of multiview equivariance on tasks such as pose estimation, video tracking, and semantic correspondence. This is only partially true as it also depends on the nature of the algorithm, bottom-up or top-down. For instance, [B] studied the 3D awareness of vision foundation models for pose estimation. Vision-language models often learns a top-down representation for 2D/3D recognition so view equivariance could hurt the performance in such cases. The authors should address these points to reinforce the integrity of the paper.

### Questions
The authors could provide some clarifications on **[W2]** and **[W3]**.

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
This paper evaluates the 3D awareness of ViT-based models and later proposes a strategy to improve 3D equivariance with minimum feature finetuning. The tasks for evaluating 3D awareness of ViT-based models are one-shot object pose estimation, video tracking, and semantic correspondence, and features from DINOv2, DINOv2-Reg, MAE, CLIP and DeiT are evaluated. Experimental results show that with some simple strategy of finetuning the foundation models, their 3D awareness can be improved with an obvious margin and the foundation model features can have better multi-view equivariance.

### Strengths
++ This paper is very well motivated and super clearly written. The paper first starts from evaluating the capability of vision foundation models on understanding 3D structures. Then, the paper shows the strong correlation between the multi-view equivariance and the performance of the chosen downstream tasks, demonstrating the reason for improving multi-view equivariance. Finally, the paper proposes a solution to improve the multi-view equivariance and therefore on the downstream tasks. The workflow of this paper is very natural and easy to understand.

++ The proposed solution to improve multi-view equivariance is simple but effective. With simply learning the equivariance on two views from the objects in Objaverse, the multi-view equivariance can be improved, so as their performance on downstream tasks.

++ The experimental results are extensive and clearly presented mainly in the forms of figures (e.g., Figures 3-4, Figures 6-10), to clearly show the improvement from employing the proposed feature finetuning method. 

++ It is a very interesting and inspirational finding in Section 3.3 that only tuning the model with a single multi-view pair of one object for a single iteration can significantly boost the multi-view equivariance of foundation models.

### Weaknesses
-- I think the biggest weakness is that there is no recent methods for comparison on the chosen downstream tasks for reference. I did not mean that the performance of foundation models need to beat the current state-of-the-art on these specific tasks, but it is necessary to provide these comparisons to give readers a sense of how good foundation models can achieve in performance. If performance from foundation models are far away behind the current state-of-the-arts, then there will be less need or motivation for future research to work on employing foundation models for 3D tasks.

-- This paper only studied the final-layer features from the vision transformer models. However, in other works that study the representation capability of features like LPIPS [1] or DVT [2], features from multiple layers are studied. Are there any reasons for studying the final-layer features? Otherwise this study would lose generalizability. It is unclear if the observed improvements are specific to the final layer or if similar gains could be achieved by fine-tuning intermediate layers or through a multi-layer feature fusion approach. The lack of ablation studies on different layers limits the conclusions that can be drawn about the optimal way to leverage these foundation models for 3D tasks.

### Questions
-- This paper mainly studies ViT-based foundation models. Are there any reasons not to study foundation models with other architectures, like ConvNeXt [1]? Is it because in current days ViT-based models are the most commonly used ones? And do the authors expect non-ViT-based models to have similar behaviour as ViT-based models?

-- In Lines 363-364, the paper mentions that "even simple shapes like an untextured hemisphere can enhance 3D understanding". However, I do not find this point reasonable (although this might be supported by experimental evidence). In principle, an untextured hemisphere would be rotation-invariant when the viewing angles rotate in certain directions, due to the symmetry of the shape, which makes the features at the points on the same radius to be consistent. How could the model actually learn 3D understanding from such a hemisphere shape? I am not sure whether this can be shown from some visualizations of the learned feature maps of a hemisphere shape.

[1] Liu et al. A ConvNet for the 2020s. CVPR 2022.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper answers 3 questions: 1) To what extent do these models possess an inherent awareness of 3D structures? 2) How
does this awareness impact their performance on image-based 3D vision tasks? 3) Can we further
enhance the 3D awareness of these vision foundation models?
To answer the first question, the authors evaluate the pixel error of multi-view correspondence by using 5 pretrained vision models, and show DINOv2 has the strongest multiview equivalence. For the second question, the authors evaluate the performance of these models on 3 downstream tasks (pose estimation, video tracking, and semantic correspondence). Finally, the author proposes a simple finetuning strategy by enforcing feature similarity between corresponding views of a rendered synthetic object. Consistent improvements on downstream tasks are shown compared to the model without finetuning.

### Strengths
1. The paper is clearly organized and easy to follow. The figures and tables are also very clear and easy to understand.
2. The experiments are pretty comprehensive, covering 5 popular pretrained vision models, and 3 downstream tasks. Some interesting settings such as fine-tuning with only one object and with only 1 iteration are covered.

### Weaknesses
1. My main concern regarding this paper is about the limited practical use case of the finetuned DINO features. On the one hand, the fine-tuned feature alone is not very useful, as its performance on downstream tasks is much worse than the SOTA models (see Tab4 and Tab5 in the supplement, e.g., for point tracking, AJ=46.85 compared to Co-Tracker=65.6). On the other hand, there is no evidence showing that the fine-tuned feature this way will benefit downstream tasks if task-specific training/finetuning is performed. For example, the paper will be much more convincing to me if the fine-tuned DINO, as pre-trained weight, could be used to achieve SOTA performance on any specific vision task. The lack of a clear path to state-of-the-art performance with the fine-tuned features significantly limits the practical impact of the proposed method. The authors should demonstrate how these features can be integrated into existing pipelines to achieve competitive results, or at least show that they provide a substantial improvement when used as a pre-training step before task-specific fine-tuning.
2. The conclusion that the authors draw to the first question, i.e., "To what extent do these models possess an inherent awareness of 3D structures", is not convincing. Having feature equivariance doesn't imply 3D awareness: SIFT could also match the same keypoint across views, even more accurately, but can you say SIFT has 3D awareness? The correspondence could be just coming from 2D local patch statistics, and no 3D reasoning is needed. The authors need to provide more compelling evidence that the observed equivariance is a result of genuine 3D understanding rather than simply 2D feature matching. For example, experiments that explicitly test the model's ability to reason about occlusions or object geometry would be beneficial. The current evaluation based on multi-view correspondence alone is insufficient to claim 3D awareness.
3. The evaluation protocol for the downstream tasks is not explained very clearly. For example, L160, you mentioned "during training" and "during inference", what is the training target and how long has the model been trained for? L214 in supp. How do you do monocular depth estimation with pretrained features? Do you need any additional training (e.g., using linear probing)? I think it would be beneficial if the authors could demonstrate the input/output of each task with figures. The lack of clarity regarding the training and inference procedures makes it difficult to assess the validity of the results. The authors should provide detailed descriptions of the experimental setup, including the specific training objectives, hyperparameters, and evaluation metrics used for each task. Visualizations of the input and output data would also greatly improve the clarity of the presentation.
4. There is no comparison with baselines on 3D-aware fine-tuning in the main body of the paper. However, there are comparisons with FiT in the supp, which I think is important and should be moved to the main paper. I have questions regarding the details of this comparison, see the next section.

### Questions
1. The authors compared the FiT baseline in Tab 3~7 in the supplement. I have some trouble understanding the result. 1) What is the difference between FiT and FiT-Reg? 2) The FiT results are significantly worse than the DINOv2 baseline. Since FiT is also based on DINO, this result is counterintuitive. The authors are basically claiming that the FiT fine-tuning is very harmful for all the tasks. Could the authors provide more evidence (e.g., visualizations) and discussion on this? I think FiT is an important baseline so this comparison will greatly affect my judgement of this paper.
2. The 3D correspondence is sometimes ambiguous, for example when the object is symmetric, or when self-occlusion occurs and the corresponding point is occluded. Have the authors deal with these cases explicitly? Would this ambiguity harm your model's performance?

### Soundness
3

### Presentation
3

### Contribution
3
