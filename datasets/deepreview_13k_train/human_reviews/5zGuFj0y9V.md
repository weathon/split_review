# Boosting Semi-Supervised 2D Human Pose Estimation by Revisiting Data Augmentation and Consistency Training

- Decision: Reject
- Scores: 5, 6, 3, 6, 3

## Abstract
The 2D human pose estimation (HPE) is a basic visual problem. However, its supervised learning requires massive keypoint labels, which is labor-intensive to collect. Thus, we aim at boosting a pose estimator by excavating extra unlabeled data with semi-supervised learning (SSL). Most previous SSHPE methods are consistency-based and strive to maintain consistent outputs for differently augmented inputs. Under this genre, we find that SSHPE can be boosted from two cores: advanced data augmentations and concise consistency training ways. Specifically, for the first core, we discover the synergistic effects of existing augmentations, and reveal novel paradigms for conveniently producing new superior HPE-oriented augmentations which can more effectively add noise on unlabeled samples. We can therefore establish paired easy-hard augmentations with larger difficulty gaps. For the second core, we propose to repeatedly augment unlabeled images with diverse hard augmentations, and generate multi-path predictions sequentially for optimizing multi-losses in a single network. This simple and compact design is interpretable, and easily benefits from newly found augmentations. Comparing to SOTA approaches, our method brings substantial improvements on public datasets

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a method for SSL 2D Human Pose estimation that improves existing methods from two aspects: data augmentation and better consistency loss design.

### Strengths
1. The paper is well-written and easy to follow
2. Personally, the idea of ranking basic augmentation looks interesting to me. From my own experience, heatmap-based prediction has different behavior from augmentations from traditional classifier-based models so this line of work looks interesting to me.
3. The experiment results show decent amount of improvement.

### Weaknesses
1. It seems that the dual network design is still a dominant approach based on experiment results. The single network with proposed components still cannot outperform dual network approaches.
2. How does the performance look like with ResNet-50? Some other work also evaluates with this model. Honestly, I don't really think ResNet-18 is that important these days.
3. The improvement on the coco training + coco wild seems to be marginal.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to boost semi-supervised human pose estimation from two perspectives: data augmentation and consistency training. For data augmentation, this paper conducts empirical studies to get the easy-hard rank of augmentations (joint cutout, joint cut-occlude, randaugment, cutmix, etc.) for human pose and recommend two augmentation combinations (i.e., a cutout after joint cut-occlude and a cutmix after joint cutout). For consistency training, the paper proposes using one easy augmentation to supervise multiply hard augmentation. Experiments on COCO and MPII datasets show that the proposed method outperforms existing SOTA methods.

### Strengths
- Based on the results in Table 3, the proposed method exceeds previous SOTA results.
- The rank and the combination of augmentations for semi supervised learning is important, and this work first try to dive deeper into this study.

### Weaknesses
1. L.95 introduces a principle "Do not combine MixUp-related augmentations" while L.224 P1 claims that "A global $T_{MU}$ does not make sense for the HPE task." It would be better to provide more details. What is the meaning of global? Moreover, it seems mixup is used in some heatmap-based works like [R1], and it works well.

- [R1] From Synthetic to Real: Unsupervised Domain Adaptation for Animal Pose Estimation. CVPR2021.

2. It would be better to include $T_{CM}$, $T_{CO}$ and $T_{MU}$  in Table 1.

3. Section 3.1 concludes that the rank and the combination of data augmentations are entirely based on empirical studies.  For example, it is easy to understand $T_{A60}$ is harder than $T_{A30}$, but it is not intuitive to understand $T_{JC}$ is harder than $T_{CO}$. I am wondering if any insights or theoretical analysis can be provided to help readers understand more intuitively. For example, L. 228 claims that "we thus nominate the most likely superior combinations: TJOCO and TJCCM". The two combinations are useful. However, can we have any insights or principles for other augmentations which not discussed in this paper. It would be meaningful if we can quickly rank any new augmentations.

4.  Section 3.1 did not discusses the parameters of each augmentation. I am not sure the default parameters of each augmentation. Moreover, I am wondering if the parameters will have significant influences on the rank and the combination. For example, Dual-Network (Xie et al., 2021) prefers to use JC 5 and RA 20 to show the parameters directly.

5. Section 5.3 discusses more augmentations and training techniques. But they are not ablation study. It would be better to clearly show the baseline and the effect of each module/strategy.

6. It would be better to show some qualitative results in the main paper or in the supplementary.

7. I am not sure the comparison between the multi-path consistency loss and others is fair enough due to the difference of batch size. It would be better to compare the pair {$I_{e1}$,...,$I_{en}$} + {$I_{h1}$,...,$I_{hn}$} with {$I_{e}$} + {$I_{h1}$,...,$I_{hn}$}, and also discuss the influence of batch size of other SOTA methods.

8. Minor comments
- there is an incorrect usage of cite in L.47.
- there are incorrect punctuation in formulas like Eqs.3 and 4.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a method to enhance semi-supervised human pose estimation (SSHPE) through synergistic data augmentation and multi-path consistency training. Instead of creating isolated or complex augmentations, they combine existing augmentations in a complementary way that intuitively benefits SSHPE, achieving stronger results through these collaborative transformations. For consistency training, they forgo traditional multi-network stacking in favor of training a single network with multi-path consistency losses across multiple augmented views of the same unlabeled image batch, yielding both efficiency and accuracy gains.

### Strengths
1.	Focus on a Practical Problem: The paper addresses a fundamental and labor-intensive challenge in 2D human pose estimation (HPE)—the need for extensive labeled data. By leveraging semi-supervised learning (SSL) to utilize unlabeled data, the approach targets a practical solution that could reduce the dependency on costly and time-consuming data annotation.
2.	Innovative Augmentation Strategies: The authors identify a unique contribution by combining existing data augmentations to create “easy-hard” augmentation pairs that introduce a wider difficulty spectrum. This approach leverages the synergistic effects of established augmentations to generate novel HPE-specific augmentations, potentially enhancing model robustness by training on more challenging, noise-introduced variations of data.
3.	Simplified and Effective Consistency Training: Instead of relying on complex multi-network architectures, the paper proposes a single-network design that optimizes multiple losses through sequential multi-path predictions on heavily augmented data. This simplified approach is both interpretable and efficient, making it accessible for broader implementation while maintaining strong performance gains.
4.	Commitment to Open Science: By releasing code for academic use, the authors support transparency and reproducibility, enabling other researchers to build upon this work and further validate the approach across diverse HPE tasks and datasets.

### Weaknesses
### Limited Novelty

The proposed method in this paper lacks sufficient novelty and fails to contribute meaningful advancements to the field of semi-supervised human pose estimation (SSHPE). Human pose estimation, as noted, is already a thoroughly researched area with many well-established methods for both data augmentation and consistency training. Specifically, the augmentations Joint Cutout (TJC) and Joint Cut-Occlude—are already known [2]. Similarly, the concept of consistency training has been explored extensively in prior work (e.g., Xie et al., 2021; Moskvyak et al., 2021; Li & Lee, 2023; Huang et al., 2023), reducing the originality of the current approach.

Additionally, this paper’s methodology appears closely aligned with SSPCM [2], sharing a similar approach to consistency training without offering meaningful differentiation both in terms of novelty and accuracy (Table 3,4). The methods do not extend beyond existing approaches like POST [1], which employs consistency training alongside augmentation but tackles a more complex problem involving significant distribution shifts—something that requires a more robust approach. Given that the paper neither introduces novel methodologies nor demonstrates improvements over current state-of-the-art techniques, its contributions are limited in both theoretical and practical impact. Consequently, the paper falls short in providing sufficient novelty or relevance to warrant further consideration.

The current approach to selecting augmentations is somewhat rudimentary; exploring more advanced augmentation generation paradigms, such as PoseAug [3], could substantially enhance the contribution by introducing more targeted, pose-specific transformations. To further strengthen the paper’s impact, the authors could also address more complex challenges within semi-supervised human pose estimation, such as managing significant distribution shifts or effectively handling occlusions, both of which would demonstrate the robustness and adaptability of the proposed method in diverse and realistic scenarios.

### Lack of experminets

The proposed method for semi-supervised human pose estimation (SSHPE) would benefit from a deeper comparison with existing foundation models, particularly in a zero-shot setting. For instance, models like Sapiens [4] have demonstrated strong generalization in zero-shot applications, and evaluating the proposed SSHPE approach against such foundation models would clarify its relative strengths and weaknesses. Additionally, the paper overlooks a critical experiment involving the use of high-accuracy 3D pose estimation models, such as those utilizing the SMPL model, which effectively parameterizes human poses, handles occlusions, and supports 3D-to-2D projection via camera transformations. Testing whether training a 2D pose estimation model under a semi-supervised setting indeed outperforms simply projecting a state-of-the-art 3D model (e.g., BEDLAM [5], which is trained solely on synthetic data) into 2D, would be crucial in establishing the necessity of the SSHPE approach. Given BEDLAM’s potential for zero-shot 2D projection, it is likely that both Sapiens and BEDLAM could outperform the proposed SSHPE model without additional training.

These omissions raise an essential question about the need for SSHPE approaches in the presence of robust, generalizable foundation models and accurate 3D pose estimators. To justify the SSHPE setting, it is recommended that the authors add a dedicated section explaining its relevance and necessity. Additionally, expanded experimental results are needed to establish a clear advantage of the proposed method over these established models, particularly to demonstrate that the proposed approach fills a specific gap that existing foundation models and 3D estimators do not.

### Results

Loss Function Effectiveness: Currently, the paper does not provide sufficient insight into the effectiveness of the proposed loss functions,  $\mathcal{L}_u$  and  $\mathcal{L}_S$. Including an ablation study to examine the individual impact of these losses on labeled and unlabeled datasets would provide a clearer understanding of their contributions. This would help substantiate the effectiveness of each component and offer more transparency on how these loss functions drive model performance.

Comparison with UDA Methods: The semi-supervised setting described shares similarities with unsupervised domain adaptation (UDA) approaches, suggesting a relevant opportunity for comparison. Including benchmark results against state-of-the-art UDA methods, such as UDAPE [6], which leverages consistency loss minimization, would highlight the unique value of the proposed method. Adding these comparisons in Table 4 would show how the approach fares relative to established UDA methods and underscore its novelty and advantage in this space.

### Lack of clarity
The paper lacks essential clarity, making it challenging for readers unfamiliar with the field to follow the methodology and results. Specifically:

Undefined Variables: Key variables such as  $u$, $l$, $N$, and $M$ in lines 181-182 are not clearly defined, which disrupts the reader’s ability to interpret the equations and understand their significance within the proposed method.

Unclear Justification for Downsampled Heatmaps: In line 161, there is a reference to predicting downsampled heatmaps without any clear explanation or citation to support this choice. Given that downsampling can impact resolution and accuracy, it’s essential to provide references to prior methods that utilize this approach and clarify why it’s suitable in this context.

### Questions
It would be helpful if the authors could address key areas including Novelty and Differentiation, Comparison with Foundation Models, Justification of the SSHPE Setting, as well as provide insights on the suggested experimentation, ablation studies, and clarity improvements. Clarifying these aspects would significantly enhance the understanding of the paper’s contributions. Addressing these points would also help position the work within the broader landscape of current methods, highlighting any distinct impact and practical relevance.

# UPDATE (After Discussion Period)

I appreciate the author's response and thanks for sharing a detailed response and addressing concerns related to novelty, experimentation and ablation studies. The statement made by the authors, "Almost all of the above methods have not been or cannot be tested on the 2D HPE datasets used in this paper," appears unjustified and lacks merit. Several existing approaches, including foundational models like SAPIENS and BEDLAM, offer the capability to perform zero-shot evaluations on 2D HPE datasets without requiring additional training. Conducting such evaluations is straightforward and would provide a meaningful benchmark against proposed methods. This comparison is critical to establish the relevance and competitive performance of the proposed method in the broader context of foundation models.

Without such comparisons, the study's scope of semi-supervised learning remains speculative, as it lacks a clear understanding of how the proposed method measures up to existing works. Hence, **I would like to retain my current rating**, as the lack of rigorous comparative evaluation constitutes a significant shortcoming.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a method for boosting 2D human pose estimation performance in a semi-supervised setting. Towards this, the authors propose two cores: advanced data augmentation and concise consistency training ways. They hypothesize that these two cores help the model’s interpretability, benefitting from the augmentations, and aid it in performing superior to SoTA semi-supervised approaches.

### Strengths
1. The authors propose a simple and seemingly effective way to improve 2d human pose estimation from RGB images using advanced data augmentation combinations and a multi-path augmentation framework for training a single network.
2. Table 3: the proposed approach outperforms other baselines showing its effectiveness on the COCO val set with different labeled train set sizes.
3. Table 4: the proposed approach outperforms other baselines when using the Resnet50 and ResNet101 architectures showing its effectiveness on the COCO val set when using the entire COCO labeled train set with unlabeled wild set for training.
4. Table 9: Results on WEPDTOF-Pose which is an indoor dataset indicate that the proposed approach may be generalizable across datasets.

### Weaknesses
1. While the overall approach seems to work somewhat effectively, the contribution in the novelty aspect is limited. The authors propose a method to combine the different augmentations to create sensible hard augmentations but the takeaways are generalized in nature and seem obvious. For example, selecting combining augmentations in Sec 3.1 does not seem to take out-of-the-box thinking and may be deduced from running a combination of experiments. The specific combinations and their synergistic effects are not rigorously justified beyond empirical observation, lacking a theoretical underpinning that would elevate the contribution beyond a simple hyperparameter search.
2. Table 4: while the gains are noticeable when using ResNet as the backbone, the same cannot be said for HRNet as the backbone. This raises concerns regarding the effectiveness of using the proposed augmentations and approach. Can the authors justify why choosing a different architecture may not result in a noticeable performance boost? The current results indicate the proposed approach may be architecture-dependent. The lack of consistent improvement across different architectures suggests that the proposed method may not be universally applicable and might be overfitting to specific network structures.
3. Sec 5.2 S3 → is there a reason the authors do not train for 400 epochs if it is the only other thing besides the number of networks presenting their method from performing not as well as SSPCM?
4. Table 5: the proposed approach performs similarly to DUAL on the test set. This raises concerns over the generalizability of the method. The marginal improvement over existing methods on the test set, particularly when compared to DUAL, questions the practical significance of the proposed approach in scenarios where labeled data is abundant.
5. Sec 5.2 S1 → Superior performance on 1 dataset for a small number of samples may not necessarily generalize to using small train sets from other datasets. Is it possible to show results on other datasets, e.g. MPII (which is already evaluated), H3.6, or LSP? Additionally, can the authors justify this statement? The authors state in Dataset Setup that the small subsets of 1K, 5K, and 10K were randomly selected. From the reported numbers, the corresponding baselines do not seem to be trained on the same selected labeled set. It may then be likely (not certainly) that the reported numbers for the proposed approach may be biased towards the evaluation set because of the selected subset for training.
6. S5 Table 8: While the overall performance is better by 0.1 (not significant), the method outperforms 4 of 7 joints (as opposed to claiming all).

### Questions
1. The authors need to explain how they divide the different sections of Table 5. This is currently unclear from the table.
2. What is the effective training time of the proposed approach under different conditions/networks?
3. What is the significance of Fig.7 when Table 3 already presents the same results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a data augmentation method with the consistency training strategy to improve the performance of semi-supervised 2D human pose estimation,

### Strengths
1.This paper identifies that the existing SSHPE methods lack rigor in ranking the difficulty levels of applied data augmentations and discovers synergistic effects among different augmentations. It proposes a more rigorous difficulty ranking for data augmentations.
2.This paper provides a comprehensive evaluation of existing advanced data augmentation methods. Rather than designing new augmentation techniques, the paper employs rule-based constraints to combine existing augmentations, nominating the most likely superior combinations: TJOCO and TJCCM.
3.A novel multi-path approach that applies multi-path augmentations and multi-path loss training to a single network can surpass certain dual network.

### Weaknesses
1.The introduction of new data augmentation requires a re-evaluation of the selection of the optimal augmentation combination.
2.The combined data augmentation will increase the training time. Is this time consumption still lower than that of stacked networks?  
3.Different combinations may yield varying performance across datasets, so can the selected optimal combination consistently provide the best results?
4.The selection process for the optimal augmentation combination is time-intensive.

5. Although the paper provides a ranking of data augmentation techniques, the criteria for evaluating the difficulty levels of augmentations appear somewhat heuristic and may lack a strong quantitative foundation.

6. The paper lacks experiments using only the multi-path loss, making it difficult to determine the individual performance improvements contributed by the multi-path loss and the two new data augmentations.

7. The paper does not clearly explain the rationale for choosing the TJOCO and TJCCM data augmentations.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
