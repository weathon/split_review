# MVSFormer++: Revealing the Devil in Transformer's Details for Multi-View Stereo

- Decision: Accept
- Scores: 6, 8, 5, 5, 6

## Abstract
Recent advancements in learning-based Multi-View Stereo (MVS) methods have prominently featured transformer-based models with attention mechanisms. 
However, existing approaches have not thoroughly investigated the profound influence of transformers on different MVS modules, resulting in limited depth estimation capabilities. 
In this paper, we introduce MVSFormer++, a method that prudently maximizes the inherent characteristics of attention to enhance various components of the MVS pipeline.
Formally, our approach involves infusing cross-view information into the pre-trained DINOv2 model to facilitate MVS learning. Furthermore, we employ different attention mechanisms for the feature encoder and cost volume regularization, focusing on feature and spatial aggregations respectively. 
Additionally, we uncover that some design details would substantially impact the performance of transformer modules in MVS, including normalized 3D positional encoding, adaptive attention scaling, and the position of layer normalization. 
Comprehensive experiments on DTU, Tanks-and-Temples, BlendedMVS, and ETH3D validate the effectiveness of the proposed method.
Notably, MVSFormer++ achieves state-of-the-art performance on the challenging DTU and Tanks-and-Temples benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes an enhanced version of MVSFormer. In particular, it specifically addressed three challenges that remained in previous works: tailored attention mechanisms for different MVS modules, incorporating cross-view information into pre-trained ViTs, and enhancing Transformer's length extrapolation capability. Experimental results demonstrated the proposed MVSFormer++ attains state-of-the-art results across multiple benchmark datasets, including DTU, Tanks-and-Temples, BlendedNVS, and ETH3D.

### Strengths
+ The contributions of this work are solid and well address the limitations of previous MVS methods. For example, introducing side view attention significantly elevates depth estimation accuracy, resulting in substantially improved MVS results.
+ The combination of frustoconical positional encoding and adaptive attention scaling is interesting. It enhances the model's ability to generalize across a variety of image resolutions while avoiding attention dilution issues.
+ The experiments are comprehensive and promising. Almost all classical and SOTA methods are considered in the comparison experiments, which are evaluated on various datasets. For visual comparisons, the proposed method significantly outperforms other competitive methods, showing more complete structure and fewer geometric distortions.

### Weaknesses
- Except for the customized designs beyond the MVSFormer, this work leverages DINOv2 as a new backbone (compared to DINO used in the MVSFormer). It would be interesting to see how the performance of MVSFormer++ changes when it keeps the same backbone as that of MVSFormer. Specifically, a direct comparison isolating the impact of the backbone change versus the architectural modifications would be valuable. This would help ascertain whether the performance gains are primarily due to the novel architecture or simply a stronger feature representation from DINOv2.
- MVSFormer and MVSFormer++ show different reconstruction performances regarding different cases on Tanks-and-Temples (Table 3). The authors are suggested to provide more discussions on how the qualitative results differ (like local details and global distributions) and why the degenerations happen. It's important to understand the failure modes of both methods, including where MVSFormer++ excels and where it falls short compared to its predecessor, particularly in terms of local geometric accuracy versus global structural completeness.
- The performance of the complete version of this work in the ablation study is different from the quantitative results reported in Table 2. Please elaborate on this inconsistency in metrics. This discrepancy raises concerns about the reproducibility and reliability of the reported results. It is crucial to understand the source of this variation, whether it stems from training randomness, different hyperparameters, or other factors.
- The baseline version of MVSFormer (without CVT, FPE, AAS, SVA, Norm&ALS) seems kind of strong already. Does it gain from the strong backbone? Moreover, the qualitative results of the ablation study are expected to be provided. Without visual comparisons, it's difficult to assess the specific contributions of each component and whether the improvements are consistent across different regions of the reconstructed scene. The impact of the backbone on this baseline performance should also be further investigated.
- The description of Normalization and Adaptive Layer Scaling is ambiguous and unclear. More details about the motivation and implementation would be helpful to understand this part. Specifically, the choice of normalization technique (e.g., layer normalization, batch normalization) and the adaptive scaling mechanism need to be clearly explained, including the mathematical formulations and the rationale behind their design choices.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an enhanced iteration of MVSFormer named as MVSFormer++. The method utilizes the Side View Attention (SVA) to empower the cross-view learning ability of DINOv2. It prudently maximizes the inherent characteristics of attention to enhance various components of the MVS pipeline. The results MVSFormer++ achieves on the DTU and Tanks-and-Temples benchmarks show the model works quite well.

### Strengths
1. The design of Side View Attention (SVA) is effective.
2. Compared to other models, MVSFormer++ has better performance.
3. The FPE and AAS are used efficiently to generalize high-resolution images.
4. The paper is well written, and one can easily grasp the main idea.

### Weaknesses
1. In the ablation study, the results of Norm&ALS under the depth error ratios of 2mm and 4mm are slightly inferior.
2. A discussion regarding the limitations is missing. 
3. Minor: Section 4.1 Experimental performance, mean F-score is 41.75 on the Advanced sets in the text while in Tab.3 it is 41.70.

### Questions
Please refer to the weaknesses above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper enhances MVSFormer by infusing cross-view information into the pre-trained DINOv2 model and exploring different attention methods in both feature encoder and cost volume regularization. It also dives into the detailed designs of the transformer in MVS, such as the positional encoding, attention scaling, and position of LayerNorm.

### Strengths
1. This paper explores the detailed designs of attention methods in the context of MVSNet. 
2. It exploits the pre-trained DINOv2 in the feature encoder and merges the information of source views by cross-view attention.
3. It designs a 3D Frustoconical Positional Encoding on the normalized 3D position, which is interesting and shows good improvements in depth map accuracy.
4. It validates that attention scaling helps the scaling of the transformer to different resolutions, and the position of LayerNorm can affect the final accuracy.

### Weaknesses
Although the MVSFormer++ modifies the base model MVSFormer by DINOv2, SVA, Norm& ALS, FPE, etc, the core contributions share similar designs with other MVS methods.

1. In the feature encoder, the Side View Attention is similar to the Intra-attention and Inter-attention in Transmvsnet. The main differences are that this paper uses a pre-trained DINOv2 as input and removes the self-attention for source features. The paper should focus more on the differences in network structure and operation within the MVS context rather than drawing parallels to generic side-tuning methods. The novelty of incorporating a pre-trained ViT into the existing attention framework needs more emphasis and specific discussion of how the DINOv2 features are integrated with the multi-view information.
2. The use of linear attention in the feature encoder has already been proposed in Transmvsnet. The paper does not strongly demonstrate the benefits of linear attention over vanilla attention with the reported results. The motivation for using linear attention should be more than just saving memory, especially considering the minor performance differences shown in Table 5. The discussion should also include how linear attention is used in existing MVS methods and if there are any differences in its application here.
3. In Table 9, although with a larger network, the MVSFormer++ only improves on MVSFormer by a small margin, which can not fully support the claim of the effectiveness of 2D-PE and AAS. The reported results for ETH3D are not significantly better than the baseline, and the paper does not provide enough evidence to support the claim that the proposed 2D-PE and AAS are effective for this dataset. The fact that both methods use dynamic point cloud fusion makes it difficult to isolate the impact of the proposed changes.
4. The FPE in Table 4 shows good improvement on CVT. The detailed network structure should be made more clear. Please see the questions.
5. The evidence for the minor changes such as the LN and AAS is not strong with experiments on only DTU. They are more intuitive and may need more experiments to prove whether they are generalizable designs. For example, Table 9 on ETH3D actually cannot fully support AAS. The improvements with Norm&ALS are minor, and in some cases, the method performs worse on the depth error metric. The depth error is a more direct evaluation metric, so the strength of Norm&ALS is not clearly supported by the experiments.

### Questions
1. I would to know the detailed structure differences between CVT and CVT+FPE. CVT is only used in the first coarse stage so how many stages use the CVT+FPE in Table 4? What are the results when CVT and CVT+FPE are both used in all stages or only the first coarse stage?
2. The paper can be improved by focusing more on the novel and interesting designs such as the FPE and analyzing more on it.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces MVSFormer++, a learning-based Multi-View Stereo (MVS) method that leverages pre-trained models to enhance depth estimation in MVS. The study tackles a crucial gap in existing research by exploring the impact of transformers on various MVS modules. The paper's motivation is clear. However, there are notable areas that require attention for improvement.

### Strengths
The paper innovatively introduces transformer-based models and attention mechanisms to address a vital issue in MVS. The novelty lies in the thorough exploration of different transformer attention mechanisms across diverse MVS modules. The paper provides hypotheses and experimental evidence supporting the use of different attention mechanisms in the feature encoder and cost volume regularization.

The authors conducted experiments across multiple benchmarks, including DTU, Tanks-and-Temples, BlendedMVS, and ETH3D, showcasing MVSFormer++'s state-of-the-art performance on challenging benchmarks (DTU and Tanks-and-Temples). This highlights the practical significance of the proposed approach.

The paper includes well-executed ablation studies, comparing the impacts of different attention mechanisms on various MVS modules.

### Weaknesses
(1) Clarity and Detail:
The paper lacks detailed explanations of specific design choices, such as the rationale behind selecting DINOv2 as the base model. The paper does not sufficiently discuss why DINOv2 is superior to other vision transformer architectures for this task, particularly given its large size and computational cost. Additionally, the utilization of different levels of DINOv2 features is not clearly elucidated. The paper does not explain how the specific layers (3, 7, and 11) were selected, and what characteristics of these layers make them suitable for multi-view stereo. It is recommended to include these details to enhance the manuscript's clarity and independence.

(2) Experiments:
While the incorporation of DINOv2 in the feature extraction stage significantly enhances performance, it is crucial to clarify that this improvement is not solely due to the increase in the number of parameters. The improvement in point cloud evaluation metrics by the proposed module during ablation experiments appears subtle. The paper needs to demonstrate that the performance gains are not simply due to the increased capacity of the network from the DINOv2 backbone. To bolster the paper's experimental support, I recommend validating the proposed module's effectiveness by integrating it into baseline methods, such as CasMVSNet, and conducting a comparative analysis. This would provide a clearer understanding of the module's actual contribution, independent of the DINOv2 backbone. Furthermore, the ablation studies should include experiments without any pre-trained models to establish the baseline performance of the proposed modules. Given DINOv2's frozen state during training, it is crucial to understand the performance of the proposed modules without the influence of pre-trained features. Additionally, the paper should include visual comparisons of depth maps to visually demonstrate the accuracy advantages of the estimated depth maps, especially in areas where the proposed method is expected to perform better.

(3) Discussion of Limitations:
The paper lacks a discussion of the limitations and failure cases of MVSFormer++. Understanding the method's limitations, such as sensitivity to lighting conditions, occlusions, or specific scene geometries, is crucial for evaluating its real-world applicability. The paper should also discuss the computational complexity and memory requirements of the proposed method, especially in comparison to other MVS approaches.

### Questions
(1) DINOv2 Pre-training Choice:
What motivated the decision to freeze DINOv2 during pre-training? How does it uniquely contribute to your method? Would including experiments with different pre-trained models or fine-tuning DINOv2 serve as valuable comparisons?

(2) Cost-Benefit Analysis of DINOv2:
Considering the marginal improvement in point cloud metrics, is the increase in network parameters due to adopting DINOv2 justified? How can you demonstrate that the metric enhancements stem from the introduced module's contribution rather than a mere increase in parameters?

(3) Discussion of MVSFormer++ Limitations:
Could you briefly discuss MVSFormer++'s limitations, especially in scenarios where it might underperform?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes MVSFormer++, which is an extended/enhanced version of the previous work MVSFormer. The authors have well-studied the usage of the transformer at different stages of the learning-based MVS pipeline, and have demonstrated the effectiveness of the proposed components by extensive experiments. The proposed pipeline achieves SOTA results on several MVS datasets.

### Strengths
- The method achieves SOTA results on DTU, Tanks and Temples, and ETH3D datasets. I believe currently it is one of the best-performing MVS approaches.

- The authors have conducted extensive experiments to demonstrate the effectiveness of the proposed components. I can find ablation studies on each proposed component in the experimental section.

### Weaknesses
 - The paper proposed a bunch of small components/tricks over the previous MVSFormer. I acknowledge that these tricks might be useful, however, I would feel like each of them is a bit incremental and the whole story is not that interconnected. For the conference paper, I prefer a neat idea/key component that can bring strong improvements. The paper looks more like an extended journal version paper of the previous one.

- ETH3D evaluation: the proposed method does not perform well on ETH3D even compared with other learning-based approach (e.g., Vis-MVSNet, EPP-MVSNet). Could the authors explain potential causes?

- These is no a limitation section. I would like know the scalability of the proposed method, will the memory cost dramatically increased compared with CNN based approaches (e.g., CasMVSNet) when the image size/depth sample number increase?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
