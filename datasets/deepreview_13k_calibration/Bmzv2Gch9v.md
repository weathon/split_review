# SmartPretrain: Model-Agnostic and Dataset-Agnostic Representation Learning for Motion Prediction

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Predicting the future motion of surrounding agents is essential for autonomous vehicles (AVs) to operate safely in dynamic, human-robot-mixed environments. However, the scarcity of large-scale driving datasets has hindered the development of robust and generalizable motion prediction models, limiting their ability to capture complex interactions and road geometries. Inspired by recent advances in natural language processing (NLP) and computer vision (CV), self-supervised learning (SSL) has gained significant attention in the motion prediction community for learning rich and transferable scene representations. Nonetheless, existing pre-training methods for motion prediction have largely focused on specific model architectures and single dataset, limiting their scalability and generalizability.
To address these challenges, we propose SmartPretrain, a general and scalable SSL framework for motion prediction that is both model-agnostic and dataset-agnostic. Our approach integrates contrastive and reconstructive SSL, leveraging the strengths of both generative and discriminative paradigms to effectively represent spatiotemporal evolution and interactions without imposing architectural constraints. Additionally, SmartPretrain employs a dataset-agnostic scenario sampling strategy that integrates multiple datasets, enhancing data volume, diversity, and robustness.
Extensive experiments on multiple datasets demonstrate that SmartPretrain consistently improves the performance of state-of-the-art prediction models across datasets, data splits and main metrics. For instance, SmartPretrain significantly reduces the MissRate of Forecast-MAE by 10.6\%. These results highlight SmartPretrain's effectiveness as a unified, scalable solution for motion prediction, breaking free from the limitations of the small-data regime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work proposes a pretraining self-supervised learning framework that can be applied to many models, and trained on different datasets for motion prediction. The pretraining pipeline leverages momentum contrast and generates contrastive pairs by augmenting the same traffic scene with non-overlapping time horizon clips, for the contrastive loss of embeddings and trajectory reconstruction loss. It demonstrates better performance with the pretraining pipeline in two different datasets and various models.

### Strengths
1. The paper is well-written and easy to follow.
2. Good performance is achieved on the AV, AV2 datasets, with different models.
3. The exploration of the concept of model-agnostic and dataset-agnostic is very good.

### Weaknesses
1.	Many details are missing, which may hinder reproducibility. For instance, in the pretraining phase, it is unclear how the values for t and t' are selected for each dataset to avoid overlapping for the experiments. The horizons of the sub-scenario as input and reconstruction are also not specified; it would be helpful to know if these are consistent with the motion prediction settings (either input or output horizons?) used during fine-tuning. Additionally, the default lambda value for the loss function is not provided. Clarifications on which parts of each network are used for pretraining would be beneficial (refer to question 1 below). Will the code be made available as open-source?
2.	Computational cost is not shown and compared.

### Questions
1.	In Fig 2, the figure labels the component as "model" for pretraining. However, since Section 3.1 (problem formulation) indicates that the contrastive loss is calculated on the encoded embeddings, should this component be referred to as the "encoder" instead? In the experiments with HiVT, HPNet, QCNet, and Forecast-MAE, are only the encoders of these models pretrained? For models like HPNet, which do not clearly differentiate between encoder and decoder architectures, how do you determine which parts of the model to use for pretraining to obtain latent embeddings? How might this selection influence the results?
2.	line 95-97, I find this claim unclear and potentially misleading. I disagree that MAE pretraining is inflexible; on the contrary, I think the masking pretraining is quite versatile. The masking techniques used in the papers you referenced - Rmp, Traj-mae, Forecast-mae, Sept - appear very similar, suggesting the masking concept is not limited and can be readily applied across various models.
3.	Line 104, abbreviation CL is not explained before.
4.	Line 266 mentions that only complete trajectories are used in pretraining, excluding incomplete ones. During pretraining phase, do you reconstruct single-agent trajectory or multi-agent? The same question applies to the prediction phase. Could you specify what percentage of trajectories remain after filtering for each dataset?
5.	Line 296, for eq.(1), why the case of i=j is not excluded in the second term of the denominator, as in this case, it equals to the positive pairs (numerator part) that try to maximize, so it this seems to conflict with the intent.
6.	Line 485, different reconstruction strategies (categories and reconstruction target of Table 5) are confusing. It is unclear how different options for reconstructing trajectories starting at t' are justified or implemented. What do you mean by historical information for the sub-scenarios of t'? Could you clarify these strategies?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors present SmartPretrain, a novel self-supervised learning (SSL) framework that is model-agnostic and dataset-agnostic. This framework aims to overcome the challenges associated with the scarcity of large-scale driving datasets for motion prediction and the reliance of existing SSL pre-training methods on specific model structures. SmartPretrain incorporates both contrastive and reconstructive SSL approaches and features a dataset-agnostic scenario sampling strategy that combines multiple datasets. Extensive experiments validate the effectiveness of SmartPretrain in motion prediction.

### Strengths
1.The field is worthy researching, and the motivations behind the method is clear.
2.The paper is well-organized.
3.The paper proposes to pre-train from composition of different sources data, which is rarely researched in motion prediction areas before.

### Weaknesses
1. While the method introduces a novel paradigm for trajectory prediction, the pretrain-finetune approach has been widely adopted across various domains like NLP and CV for years, making it less valuable. Consequently, the contribution of SSL for model training is incremental.
2. The technical contribution of the dataset sampling strategy appears limited: aspects like standardizing representations, ensuring data quality, and maximizing volume and diversity are fundamental considerations when integrating different data sources.
3. With only one SSL pre-training baseline and a single dataset in Table 2, it may be challenging to substantiate the proposed method’s advantages over other SSL approaches.
4. If possible, additional visualization results from the authors would be highly valuable.
5. The pre-training needs 32 Nvidia A100 40GB GPUs for 128 epochs, which takes abundant computational resources. However, the improvements are not that significant.
In short, the contributions of the papers are limited, especially the technical part. I think the paper cannot meet the standard of ICLR conference,

### Questions
Please see weaknesses.

### Soundness
3

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
This paper introduces a self-supervised learning framework for motion forecasting that is both model-agnostic and dataset-agnostic. The approach unifies data samples from various motion forecasting datasets, such as WOMD, AV1, and AV2, making it feasible to pretrain models on large-scale, multi-source data. The framework incorporates both conservative learning and a reconstruction task, achieved through Trajectory Contrastive Learning (TCL) and Trajectory Reconstruction Learning (TRL). Experimental results demonstrate significant performance improvements across multiple architectures and datasets, validating the effectiveness of the proposed methods.

### Strengths
1. This paper is well-organized and easy to follow. The experimental results are thorough, covering various datasets and methods, and providing strong evidence for the method's effectiveness.

2. While conservative learning and reconstruction tasks are common in self-supervised learning frameworks for motion forecasting, this submission introduces some innovative strategies that add value.

3. The approach to unifying data representation from diverse sources could pave the way toward a foundation model for motion forecasting.

### Weaknesses
While the novelty of this submission may be somewhat limited and most techniques are already verified in many previous works, it does not present any clear weaknesses. For specific considerations, please refer to the questions section.

### Questions
1. In the experiment section (Table 1), it is noted that both HPNet and Forecast-MAE were not pretrained on all three datasets, reportedly due to "compute constraints." This reasoning should be clarified further to help readers understand the specific limitations or challenges involved.

2. The reconstruction task is commonly employed in motion forecasting pretraining frameworks, with two main approaches: predicting masked tokens (as in Forecast-MAE) or predicting masked tail trajectories (as in SEPT[2]). The proposed method follows a strategy similar to the latter, which has been shown to outperform the token prediction approach in [2]. It would be beneficial to emphasize the main distinctions of the proposed method from this established approach to further highlight its contributions.

[1] Forecast-MAE: Self-supervised Pre-training for Motion Forecasting with Masked Autoencoders

[2] SEPT: Towards Efficient Scene Representation Learning for Motion Prediction

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper offers a universal pipeline to pre-train on real-world motion data for trajectory prediction tasks. Combining popular self-supervised pre-training methods like contrastive learning and reconstruction learning, and with specific designs on motion data domain, this work successfully proposes a pre-training pipeline to learn general representations of *trajectories* in motion data, which can work regardless of the baseline motion prediction models or the motion datasets used. Extensive experiments have been performed on various commonly-used datasets (Argoverse 1/2, Waymo Open Motion Dataset) and state-of-the-art baselines (HiVT/QCNet etc.) to show the effectiveness of the pre-training pipeline proposed. A series of ablation studies clearly ablate the effectiveness of each module of the pre-training pipeline as well as the pre-training data involved.

### Strengths
1. The pipeline proposed in this work is model-agnostic, i.e., it can be easily extended to any encoder-decoder style motion prediction model.
2. This work successfully combines different real-world datasets like Argoverse and Waymo, so it can significantly enlarge the available motion data that can be used for a specific motion prediction task, where data scarcity is a significant problem.
3. Extensive experiments are conducted to prove its general effectiveness across different baseline models and datasets.
4. Ablation studies are well designed to clearly show i) the effectiveness of each part of the pipeline ii) the influence of pre-training data.

### Weaknesses
1. The downstream motion prediction settings, though already very diverse, seem not being able to cover all necessary cases. For example, no methods fine-tuned on Waymo Open Motion Dataset (WOMD) are presented.
2. The pre-training performance should be illustrated to prove that pre-training tasks can be done successfully. For example, can you show some examples of reconstructed trajectories?
3. Direct data mixing in Data-scaled Pre-training is a natural choice, but might not be optimal. For example, WOMD has significant domain gap compared to Argoverse. In this case, a biased weight might be helpful in pre-training stage to lower the influence of WOMD-Argoverse domain gaps.
4.  An ablation on how to utilize the additional data in the pre-training stage could be added to make Table 3 even more convincing. For example, in Transfer Pre-training and Data-scaled Pre-training, what would happen if the additional data is used to pre-train on the baseline model directly, or even directly to augment the training set for the baseline model?
5. Some minor questions:
i) Why to use L1 loss in TRL instead of L2, while the latter is the base for metrics used (MR, FDE, ADE)?
ii) The quantity of data that is complete / incomplete might be presented to help readers understand the quantity of additional data introduced through this work.
6. The prediction metrics lack error bars. This is not a weakness, but a point that can be even improved. I understand that the motion prediction metrics can be unstable sometimes, but adding error bars onto the most important results would significantly improve the reliabilities of the pipeline proposed.

### Questions
Please see the Weaknesses. I am looking forward to the authors' rebuttal and discussions on those issues.

### Soundness
3

### Presentation
3

### Contribution
2
