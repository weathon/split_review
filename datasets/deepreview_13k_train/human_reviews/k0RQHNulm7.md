# Generalizable Cross-Modality Distillation with Contrastive Learning

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Cross-modality distillation arises as an important topic for data modalities containing limited knowledge such as depth maps and high-quality sketches. Such techniques are of great importance, especially for memory and privacy-restricted scenarios where labeled training data is generally unavailable. 
To solve the problem, existing label-free methods leverage a few pairwise unlabeled data to distill the knowledge by aligning features or statistics between the source and target modalities. 
For instance, one typically aims to minimize the L2 distance or contrastive loss between the learned features of pairs of samples in the source (e.g. image) and the target (e.g. sketch) modalities. However, most algorithms in this domain only focus on the experimental results but lack theoretical insight. To bridge the gap between the theory and practical method of cross-modality distillation,  we first formulate a general framework of cross-modality contrastive distillation (CMCD), built upon contrastive learning that leverages both positive and negative correspondence, towards a better distillation of generalizable features. Furthermore, we establish a thorough convergence analysis that reveals that the distance between source and target modalities significantly impacts the test error on downstream tasks within the target modality which is also validated by the empirical results. Extensive experimental results show that our algorithm outperforms existing algorithms consistently by a margin of 2-3\% across diverse modalities and tasks, covering modalities of image, sketch, depth map, and audio and tasks of recognition and segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method for a cross modality distillation problem. The proposed method is based on contrastive learning in order to take both positive instance pairs and negative pairs into account, while existing methods typically rely on the positive pairs. Furthermore, the paper provides theoretical analysis on the error bound of the proposed method. The effectiveness of the proposed method is verified on a wide variety of cross modal transfer setting.

### Strengths
- S1. The proposed approach is simple and reasonable, and it turns out to be effective in different cross modal transfer learning scenario.
- S2. The paper provides theoretical analysis on the error bounds and discusses the characteristic of the method based on the analysis, i.e., in which situations the proposed method is expected to work well.
- S3. The paper generally reads well.

### Weaknesses
 - W1. The originality of the proposed method is not that outstanding because equation (2) is a straightforward adaptation of self-supervised distillation [Fang et al., 2021] to the cross modal setting and equation (3) is also a straightforward adaptation of what was proposed in the paper of CLIP [Radford et al., 2021]. While the theoretical analysis is appreciated, the core method's novelty remains limited, primarily involving the application of existing techniques to a new domain. The adaptation of self-supervised distillation and CLIP losses to a cross-modal setting, while effective, doesn't introduce significant methodological innovation. The core idea of using contrastive learning for cross-modal distillation is not entirely novel, and the specific implementation appears to be a direct application of existing loss functions.
- W2. The claim in the 2nd last line of section 3
> “It indicates that if source and target modalities have more common information or patterns, 
the algorithm will have a higher probability of distilling more information from the source modality to the downstream task in the target modality."

lacks objective evidence. The paragraph “Relationship with the generalization bound” in section 4.1 discusses it, but the discussion is rather subjective. It would become much more convincing if the authors can provide more objective evidence. For example, it may be interesting to provide the analysis on the relationship between the performance and estimated total variation distance between two datasets. Specifically, a quantitative analysis showing a correlation between the total variation distance and the performance gain achieved by the proposed method would strengthen this claim. Without such empirical evidence, the claim remains speculative and lacks sufficient support.
- W3. Some important experimental setting is not described in the main paper. What are the values of M and m? The paper should clearly define what M and m represent (e.g., total number of pairs, number of pairs used for distillation) and provide the specific values used in the experiments within the main body of the paper to ensure reproducibility and clarity. The lack of these details makes it difficult to assess the experimental setup and replicate the results.

Typo and minor suggestions.
1. In Figure 1, it is better to clearly indicates which figure corresponds to which method.
2. Please check the grammar of the sentence after equation (13)
> “Detailed proof our the Theorem 3.3 in Appendix A.3.”
3. The first sentence of section 4
>“To demonstrate the efficiency of our algorithm, we conduct extensive experiments on various cross-modality tasks.”

efficiency -> effectiveness?
4. In P7, 3 lines from the bottom,
>“our method utilizing CMD/CMC loss achieves top-1 accuracies of 72.61%/73.24% on Sketchy, outperforming the best baseline by a margin of 3%.”

The margin is less than 2% as SOCKET+LE achieves 71.33%.

### Questions
Is it possible to apply both CMD and CMC?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses cross-modality distillation for data with limited information. Existing methods focus on aligning features between source and target modalities but overlook negative relationships in unpaired data. The authors introduce "generalizable cross-modality contrastive distillation (CMCD)" that leverages both positive and negative correspondences, outperforming existing methods across various modalities and tasks. They emphasize the impact of modality distance on downstream task performance.

### Strengths
1. The proposed CMD and CMC losses seem to be novel.
2. Experimental results show the superiority of the proposed two losses over previous methods.
3. Theoretical analysis shows that the performance of proposed two losses are controlled by the alignment of latent feature distributions.

### Weaknesses
1. The motivation for the proposed distillation is not clear to me. If we do not use the labels of the source modality, only do self-supervised learning on the source data (though source and target data are paired, in my understanding they share labels), and finally only supervised trained on target data, why do we expect improvements (though results are improved)? The pipeline of SSL (source), alignment (source + target), and FT (target) is not reasonable as we actually can direct SSL (target) + FT (target). Specifically, the advantage of using a source modality for SSL when the target modality has paired data is not well-explained. It's unclear why learning representations from the source modality, without leveraging the target modality's labels, would lead to better downstream performance on the target modality compared to directly performing SSL on the target modality itself. The paper needs to justify why the transfer of learned representations from source to target is beneficial, especially when paired data is available in the target domain.
2. Theoretical analysis cannot support why the losses are useful as it only proves that the test error of the target task is bounded by the distance between two distributions. However, there is no theorem that the proposed losses can achieve a smaller distance than the previous method. The theoretical analysis is limited as it only establishes a bound, but does not demonstrate that the proposed contrastive losses are optimized to minimize this bound more effectively than existing methods. A more rigorous analysis would involve showing that the proposed losses lead to a tighter bound or a faster convergence towards a smaller distance between the feature distributions.
3. The experiments actually show that SSL (source) - alignment (source + target) - FT (target) is better than SSL (target) - FT (target) and FT (target), which is counterintuitive. I would like to see a more detailed analysis of why this happens. The empirical results are not intuitive, and the paper does not provide sufficient analysis to explain why the proposed pipeline outperforms direct SSL on the target modality. This requires a deeper investigation into the learned representations, perhaps through visualization or feature analysis, to understand why the source modality pre-training is beneficial.
4. Experimental details are missing, e.g., epochs/lr of SSL, alignment, and FT, which is essential for evaluating the results without reproducing the experiments. Furthermore, details about the specific architectures used for each modality, the choice of optimizer, and the loss functions used for SSL, alignment, and fine-tuning are needed. Without these crucial details, it's difficult to assess the validity and reproducibility of the experimental results. The paper should also include information about the hardware used for the experiments and the computational resources required.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a cross-modality distillation method with contrastive learning. Existing self-supervised methods leverage a few pairwise unlabeled data to distill the knowledge by aligning features or statistics between the source and target modalities.  The Cross-Modality Contrastive Distillation (CMCD) framework proposed in this paper considers the unpaired and unlabeled data in source and target modalities. The convergence analysis reveals that the distance between source and target modalities significantly impacts the test error on downstream tasks within the target modality which is also validated by the empirical results.

### Strengths
1. This paper considers that mass multi-modality data is not paired in the real world. For memory and privacy-restricted scenarios where labeled training data is generally unavailable, this setting will be more practical. This motivation may stimulate follow-up research.

2. There is sufficient convergence analysis and detailed settings of experiments in the paper. 

3. The experiments cover several modalities, such as image, sketch, depth map, and audio, and two downstream tasks of recognition and segmentation.

### Weaknesses
1. The proposed method follows the self-supervised knowledge distillation framework which is widely used in existing works. The core idea of using contrastive learning between source and target modalities, followed by fine-tuning on labeled data in the target modality, is a common approach, as seen in works like Ref[1]. The paper does not sufficiently articulate how its specific implementation of contrastive learning and distillation offers a significant departure from these existing methods. The novelty is not clearly established beyond a specific combination of existing techniques.

2. The authors claim that both positive and negative correspondence are leveraged in the abstract. However, it seems that the negative correspondence is primarily used during the pre-training stage of the source modality. The paper does not clearly demonstrate how negative samples are effectively utilized in the cross-modal distillation process itself, which is a crucial aspect of contrastive learning. The lack of clarity on this point weakens the argument for the proposed method's effectiveness.

3. There are too few ablation experiments in the paper. For instance, the experiments in Table 2 show that different ResNet backbone networks have a relatively small impact on the results. This raises questions about the robustness of the method and the sensitivity to architectural choices. It is unclear whether the method would generalize well to other architectures, such as transformer-based models, and whether the observed performance gains are consistent across different model families. The lack of experiments with different architectures limits the generalizability of the findings.

### Questions
Q1: Why not utilize unpaired data in the target modality?

Q2: If there is no labeled data in the target domain, is the model still effective?

Q3: In Table 1, what’s the downstream task of each dataset? It’s not clear to me in its current form.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework for cross-modality distillation, which aims to transfer knowledge from a source modality with rich information to a target modality with limited information. The framework leverages contrastive learning to exploit both positive and negative relationships in the paired data, and distills generalizable features for various downstream tasks. The paper also provides theoretical analysis and empirical results to support the effectiveness and versatility of the proposed method.

### Strengths
1. This paper is well-written and easy to follow.
2. The paper provides theoretical analysis and empirical results to support the effectiveness and versatility of the proposed method across diverse modalities (e.g., images, sketches, depth maps, videos, and audio) and tasks (e.g., recognition and segmentation).

### Weaknesses
1. While the paper reviews relevant literature on cross-modality distillation and contrastive learning, it omits references to recent works on multi-modal distillation, specifically [1-2], which employ an online distillation strategy different from the approach presented here. The authors are encouraged to provide a comprehensive comparison with these works. How does this paper compare with these works? Are there any advantages or disadvantages of using different distillation strategies and loss functions?  [1-2] appear closely related to this work, and it would be valuable to engage in a detailed discussion with these papers, especially regarding the learning of positive and negative relationships during distillation.
2. I appreciate the theoretical results of this paper but the two distillation losses, CMD and CMC, appear somewhat simplistic.. The CMD loss is just the cross entropy loss and the CMC loss is exactly the CLIP loss. Moreover, the CMD loss can be seen as a within-modal regularizer of multi-modal learning, which has been used in [2-3]. Consequently, it seems that these losses have been adopted from the multi-modal learning community with minimal modification, potentially diminishing the novelty and significance of the proposed cross-modality contrastive distillation framework. What is the novelty and significance of the proposed framework? How does it differ from existing methods for multi-modal learning or cross-modality transfer?
3. The paper neglects to discuss recent work such as LiT [4], which employs a locked image model in multi-modal tuning. The concept of the locked operator in LiT appears akin to cross-modality distillation in this paper. A detailed comparison between this paper and LiT, in terms of methodology and performance, is essential to elucidate the distinctions and commonalities between the two approaches.

### Questions
The main points to address in the rebuttal primarily stem from the "weaknesses" section we discussed earlier. Specifically, it would greatly benefit our understanding if the authors could provide a more extensive explanation of their method's contribution, ideally through a detailed comparison with the works below.

[1] Align before Fuse: Vision and Language Representation Learning with Momentum Distillation, NeurIPS 2021

[2] Graph Matching with Bi-level Noisy Correspondence, ICCV 2023

[3] CrossCLR: Cross-modal Contrastive Learning For Multi-modal Video Representations

[4] LiT: Zero-Shot Transfer with Locked-image text Tuning, CVPR 2022

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
