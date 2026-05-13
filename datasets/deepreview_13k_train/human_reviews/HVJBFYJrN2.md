# STARS: Self-supervised Tuning for 3D Action Recognition in Skeleton Sequences

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Self-supervised pretraining methods with masked prediction demonstrate remarkable within-dataset performance in skeleton-based action recognition. However, we show that, unlike contrastive learning approaches, they do not produce well-separated clusters. Additionally, these methods struggle with generalization in few-shot settings. To address these issues, we propose Self-supervised Tuning for 3D Action Recognition in Skeleton sequences (STARS). Specifically, STARS first uses a masked prediction stage using an encoder-decoder architecture. It then employs nearest-neighbor contrastive learning to partially tune the weights of the encoder, enhancing the formation of semantic clusters for different actions. By tuning the encoder for a few epochs, and without using hand-crafted data augmentations, STARS achieves state-of-the-art self-supervised results in various benchmarks, including NTU-60, NTU-120, and PKU-MMD. In addition, STARS exhibits significantly better results than masked prediction models in few-shot settings, where the model has not seen the actions throughout pretraining. Project page: \url{https://soroushmehraban.io/stars/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- The paper tackles the problem of self-supervised learning for skeleton-representation learning. 
- While previous state-of-the-art are MAE-based and achieve good fine-tuning performance, these suffer on linear evaluation, few shot learning due to poorly separated clusters. 
- The paper proposes to have a two stage pre-training of MAE followed by a contrastive learning based training. 
- The approach retains fine-tuning performance while being better at linear evaluation, and few-shot learning. 
- The approach shows that a short contrastive learning stage is enough to obtain good performance.

### Strengths
- The approach is interesting and tries to leverage advantage of both masked-auto encoder and contrastive learning based pre-training. 
- Simplicity of the approach is a strength of the paper. Approach needs minimal additional training to achieve the improvements. 
- The paper is well written and easy to follow for the most part. 
- The presented ablations and design decisions could be helpful to the community.

### Weaknesses
 - Prior work: While simplicity is the strength for this paper. It proposes a combination of two existing approaches. The authors must make it clear if the two stages of training have any differences from the original approaches. A missing reference which also discusses differences in representations of MAE and CL-based pre-training for images and simple ways to use both [a]. Why was the proposed approach used instead of adapting one of the approaches in Section 2.2 for skeleton-based representation learning. 
- How does training with NNCLR loss together with MAMP compare with the proposed approach ? What happens if the final stage employs both MAMP and NNCLR ? 
- L231: "our method". Any changes from NNCLR must be clearly stated to make sure that the readers understand the differences. 
- Experiments; Table 6 - why k=10 ? Table 2 uses k=1 making it difficult to compare. It would be interesting to have the same number of clusters (or both settings) to make comparisons easier. I am surprised that other approaches are so bad (Table 6) especially with MoCo which as the setup used in CMD. 
- Since NNCLR was shown to be very effective post MAE training, do you have any baselines which uses NNCLR alone and compare it with MAMP and the proposed approach ? 
- Table 5: How sensitive is the approach to different runs. How many times was this experiment repeated? Why do we see a drop from 1-shot to 2-shot ?

### Questions
Please refer to the weaknesses section. Additionally: 
- Do you use the same feature for linear evaluation, fine-tuning and kNN experiments ? Was one better over the other since a project was added ? 

- Typo: L310 ViT?

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
4

### Summary
This article proposes a human behavior analysis framework called STARS, aimed at improving the output representation of MAE encoders, thereby creating well-separated clusters without the need for any additional data augmentation. Extensive experiments and ablation studies conducted on three large-scale 3D skeleton action recognition datasets have verified the effectiveness of the STARS method.

### Strengths
1. This paper proposes the STARS framework, which combines MAE with contrastive learning, and can significantly improve the output representation of the MAE encoder with only a small amount of contrastive tuning.
2. Extensive experiments and ablation studies have been conducted on three large-scale 3D skeleton action recognition datasets, effectively proving the effectiveness of the method, and in most cases, reaching the state-of-the-art performance level.

### Weaknesses
1. Compared to some other contrastive learning methods (such as AimCLR, CMD), the STARS method only relies on single-view sequences for operation and does not use two different augmented views. Theoretically, its performance may be limited under cross-view evaluation on the NTU dataset. However, the cross-view evaluation experiment results in Table 1 and Table 3 are better than them. The article lacks relevant explanatory analysis. Specifically, while the method achieves strong results, the lack of multi-view augmentation during training raises questions about its robustness to variations in viewpoint that might be present in real-world scenarios. The absence of a clear explanation for why single-view training outperforms multi-view methods in cross-view settings is a significant gap.
2. As shown in the experimental results of Table 1, when the pre-trained and fine-tuned encoders are on a limited dataset, the difference in effect between the STARS method and other mask prediction methods (such as Skeleton MAE, MAMP) is not obvious, indicating that its generalization capability on small datasets needs further improvement. The performance plateau on small datasets suggests that the contrastive learning component of STARS may not be fully effective when the diversity of the training data is limited. This raises concerns about the practical applicability of the method in scenarios where labeled data is scarce. The method's reliance on a large dataset to achieve significant gains is a notable limitation.
3. The method uses some tricks in the ablation experiments, such as hierarchical learning rate decay (Formula 7); in addition, the Backbone is not aligned with other methods (Table 3), making it difficult to determine whether these tricks have brought benefits. The use of a hierarchical learning rate decay, while potentially beneficial, complicates the analysis of the core method's contribution. The lack of a consistent backbone across experiments makes it challenging to isolate the impact of the STARS framework from the architectural choices. This makes it difficult to assess the true effectiveness of the proposed approach.

### Questions
See the above weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new method for self-supervised skeleton action recognition. Specifically, it first pre-trains the encoder through the mask reconstruction in MAE, then a tuning strategy with contrastive learning to enhance the inter-class separability among actions. Extensive experiments demonstrate the superior performance of their method. Meanwhile, the code is released.

### Strengths
1. The paper is well-written, and the techniques sound reliable.
2. The work provides comprehensive experiments that are effective.

### Weaknesses
1. The novelty of this paper is limited. It seems like the composition of existing methods and the contribution is not clear. The core idea appears to be a straightforward application of existing techniques like MAE and contrastive learning, without significant modifications or novel insights into the specific challenges of skeleton-based action recognition. The combination of MAMP pretraining and NNCLR tuning, while effective, lacks a clear justification for why this particular combination is superior to other possible approaches or why it is necessary for this task.
2. Multi-stages pertaining is more complex than previous studies. Although the training time is decreased, the computation overhead must be considered. The paper does not adequately address the computational cost associated with the proposed method, particularly the memory requirements of using 4 A40 GPUs. The impact of queue size on computational overhead is also not sufficiently explored, making it difficult to assess the practical efficiency of the method compared to simpler alternatives.

### Questions
1. What is the difference between the core idea in this paper and the MAE-CT [1]? It seems that MAE-CT also trains MAE first and tunes the projector and predictor second. Besides, the pretraining pipeline utilized in this paper is MAMP, and the tuning framework used is the NNCLR. So, what is the novelty or the actual contribution of this work? Just employing them in the skeleton action recognition task? It is just an engineering work composed of several existing techniques.
2. Some state-of-the-art methods are not compared, e.g., PCM3 [2], UmURL [3]. The author should supply them for a comprehensive comparison.
3. Compared to the previous studies, the training time is decreased. However, the memory requirements look like they are increasing; 4 A40 GPUs are needed. Meanwhile, the queue size can influence this method's computation overhead. The author should supply the overhead comparison or other metrics to demonstrate the effectiveness of their method.

[1] Lehner J, Alkin B, Fürst A, et al. Contrastive tuning: A little help to make masked autoencoders forget[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2024, 38(4): 2965-2973.

[2] Zhang J, Lin L, Liu J. Prompted contrast with masked motion modeling: Towards versatile 3d action representation learning[C]//Proceedings of the 31st ACM International Conference on Multimedia. 2023: 7175-7183.

[3] Sun S, Liu D, Dong J, et al. Unified multi-modal unsupervised representation learning for skeleton-based action understanding[C]//Proceedings of the 31st ACM International Conference on Multimedia. 2023: 2973-2984.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an STARS framework that combines Masked Auto-Encoding (MAE) and contrastive learning to perform self-supervised tuning for 3D action recognition. It utilizes MAE as the pretext task and trains a contrastive head to partially tune the encoder, so as to learn distinct clusters for better action recognition. Experiments demonstrate the effectiveness of STARS on various benchmarks, including NTU-60, NTU-120, and PKU-MMD. This work also shows the limited generalizability of MAE approaches in few-shot settings, and verifies the higher efficacy of STARS under different protocols (linear evaluation, KNN evaluation, fine-tuned evaluation, etc.) in most cases.

### Strengths
1. This paper empirically compares the performance of masked prediction methods (MAE) and contrastive learning methods on action recognition, and conceptually introduces nearest-neighbor contrastive learning into MAE by partial self-supervised tuning to enhance the generalization performance. This idea is simple and effective.

2. This work conducts relatively comprehensive experiments under different cases, covering conventional protocols and new few-shot evaluation protocol, and compares with existing state-of-the-arts to show the effectiveness of method. 

3. The paper writing is easy to follow with clear technical description and presentation.

### Weaknesses
1. This work lacks sufficient novelty. It seems that the authors stack and combine existing technologies, such as MAE and contrastive learning approaches, to build the proposed framework for 3D action recognition.

2. The comparison with other models in Fig. 1 is vague and not specific. The authors do not provide any information about training parameter size, training computational complexity (e.g., GFLOPs), etc. The training time can be influenced by many factors such as machines, GPU ability, I/O speed, etc. So I do not think the comparison in Fig. 1 can fairly show the efficiency or resource usage of the proposed method, unless providing a comprehensive description about training process of each model or the above metrics.

3. This work claims that "MAE approaches exhibit a lack of generalizability in few-shot settings", but it lacks sufficient experiments and deeper analyses to support this crucial claim. Authors seem to use only MAMP as an example of MAE approaches to compare in few-shot settings (Sec. 4.3), but other MAE methods are not included in the comparison and analyses. To provide a thorough evaluation of generalizability, it is suggested to add more empirical comparison (e.g., the naive MAE and its different representative variants), more qualitative analysis (e.g., the generalization performance of learned features on similar or different action classes), and more evaluation scenarios (e.g., other datasets rather than only NTU-60 and NTU-120).

4. It is suggested to quantify the required number of epochs instead of using "a few epochs" in the contribution part. Is the number of epochs fixed or does it need to be adjusted according to different scenarios? All these questions should be clearly clarified in the paper, for a more solid and improved presentation of this paper.

5. The paper mentioned that "any alternative MAE-based approach is also applicable", and stated that MAMP shows promising results. How is the performance of other MAE-based approaches when applied to the proposed framework? As we know, the generality of a method is not only related to a certain evaluation protocol such as the few-shot settings, but also related to its general applicability under different cases. Therefore, it is important to add compared experiments using different MAE-based approaches (there are many MAE methods in this area).

6. Some details of technical components should be added with their motivations. For example, what is the reason for "use layer-wise learning rate decay Clark et al. (2020) to tune the second-half of the encoder parameters"? The authors add this component but do not explain the necessity or importance.

7. Some results in the qualitative comparison seem problematic and not convincing. The result "52.0*" of MAMP evaluated on PKU-II (Table 1) is not the same as the original paper, do different GPUs influence the performance? Authors do not present the best result of CMD (Mao et al 2022), i.e., Three-stream as input, in Table 1. Authors need to carefully check and comprehensively and farily present all published results. The t-SNE visualization in Figure. 3 is also different from other papers, such as CMD. In the CMD paper, the visualization result is significantly better than that shown in this paper.

8. Some result points are missed in the ablation study (Figure 4). For example, the paper only shows the KNN accuracy of α=15, 25, 35, 55, but lacks the point when setting α=45. For queue size experiments, what are the results when setting k=6, 10, 12, 14? Authors should add these results to get a more holistic view of ablation study.

### Questions
1. Please provide a comprehensive description about training process of each model (in Fig. 1) or adopt more metrics, as detailed in the Weakness 2.

2. To provide a thorough evaluation of generalizability, it is suggested to add more empirical comparison (e.g., the naive MAE and its different representative variants), more qualitative analysis (e.g., the generalization performance of learned features on similar or different action classes), and more evaluation scenarios (e.g., other datasets rather than only NTU-60 and NTU-120). (see Weakness 3)

3.  It is suggested to quantify the required number of epochs instead of using "a few epochs" in the contribution part. Is the number of epochs fixed or does it need to be adjusted according to different scenarios? All these questions should be clearly clarified in the paper, for a more solid and improved presentation of this paper.

4.  How is the performance of other MAE-based approaches when applied to the proposed framework? (detailed in Weakness 5)

5. What is the reason for "use layer-wise learning rate decay Clark et al. (2020) to tune the second-half of the encoder parameters"? (see Weakness 6)

6. The result "52.0*" of MAMP evaluated on PKU-II (Table 1) is not the same as the original paper, do different GPUs influence the performance? (see Weakness 7)

7. The authors should provide comprehensive results in the ablation study. (detailed in Weakness 8)

### Soundness
2

### Presentation
2

### Contribution
2
