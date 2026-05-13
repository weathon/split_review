# Delving into Weakly Supervised Learning with Pre-Trained Models

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Weakly supervised learning (WSL) is a popular machine learning paradigm in recent years that aims to learn a classifier with incomplete, imprecise, or inaccurate supervision. Existing WSL approaches have mainly focused on designing different loss functions or training strategies and then training models from scratch. In this paper, we first empirically show that a zero-shot baseline based on the Contrastive Language-Image Pre-Training (CLIP) model with class descriptions empowered by GPT-4o can outperform previous state-of-the-art methods trained from scratch on various WSL problems. Therefore, this motivates us to fine-tune pre-trained models to further improve the performance. However, our additional experiments show that naive use of existing WSL losses degrades performance due to severe overfitting exacerbation and feature degeneration problems. To address these problems, we propose a novel weakly supervised fine-tuning approach using dual classification heads that are trained synergistically by alternately distilling reliable supervision and performing efficient model fine-tuning. Theoretically, we prove the consistency and convergence rate of the proposed risk estimator. Empirically, extensive experiments on benchmark datasets of different WSL problems validate the effectiveness of the proposed approach against state-of-the-art competitors. The code is provided at https://github.com/ICLR2025-6897/WSFT_code.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the zero-shot ability of CLIP on weakly-supervised learning. They propose a two-step algorithm for WSL by generating a pseudo label first. The experiments show improvement in various settings of WSL.

### Strengths
1. The author provides mathematical proof for their algorithm.
2. The experiments are detailed and show significant improvement to SOTA.

### Weaknesses
1. The writing is not clear.
2. Putting Sec. 3.1 in the approach section is questionable to me. See Q1.
3. Possible missing related work. See Q2.
4. The formulation of PU learning is not provided, and its relation to UU learning is unclear. This should be introduced before using PU learning as a major topic in L201. PU learning seems to be a special case for UU learning as mentioned in L223.
5. I am confused about Sec. 3.2, which is about the motivation of this paper. Does the depicted problem only occur in PU learning? In UU learning? Or both? The author explains the problem by giving PU learning as an example but later talks about UU learning in Sec. 3.3.
6. What is CRE $\hat R_1$ in L239? Is it the same as Eq 3, which is $\hat R_{CUU}$?
7. In L244, what does it mean "could contain all the unlabeled data whose true labels are not accessible to the learning algorithm"? Is there unlabeled data whose true labels are accessible? How can one access the labels of unlabeled data?
8. I think the writing of Sec. 3.3 can be improved. Especially, the definition of supervision distillation and model fine-tuning should be explained or summarized first in L237 at the start of the paragraph. Is the first step, i.e. supervision distillation, from L239 to L244, or L239 to L257? What is model-finetuning then?
9. Are the "class priors" in Sec. 4.3 and 4.4 the same as $\pi_{T_e}$?
10. The formulation of Pcomp should be explained somewhere, especially the meaning of "unlabeled pairwise observations were provided" in L402.
11. The legend in Fig. 2(d) is not visible.
12. The notation $C$ is first used in Eq. 2. The author also uses $C_g$ and $C_l$ for various constants in the theoretical analysis. I recommend distinguishing them. Additionally, $D$ is used in Eq. 2 and also as some datasets.

### Questions
1. What is the difference between the zero-shot CLIP baseline introduced in L159 and the zero-shot performance on CIFAR-100 on the official CLIP GitHub repo (https://github.com/openai/CLIP)?

2. What is the author's comment on the comparison to [1]? To me, semantic segmentation, which can be viewed as a per-pixel image classification problem, is more complicated than image classification, which is the focus of this paper. It is mentioned that this paper can be extended to the "multi-class classification problem" in L276.

3. What is the formulation of PU learning? How is it compared to UU learning? This should be introduced before using PU learning as a major topic in L201. PU learning seems to be a special case for UU learning as mentioned in L223.

4. I am confused about Sec. 3.2, which is about the motivation of this paper. Does the depicted problem only occur in PU learning? In UU learning? Or both? The author explains the problem by giving PU learning as an example but later talks about UU learning in Sec. 3.3.

5. What is CRE $\hat R_1$ in L239? Is it the same as Eq 3, which is $\hat R_{CUU}$?

6. In L244, what does it mean "could contain all the unlabeled data whose true labels are not accessible to the learning algorithm"? Is there unlabeled data whose true labels are accessible? How can one access the labels of unlabeled data?

7. I think the writing of Sec. 3.3 can be improved. Especially, the definition of supervision distillation and model fine-tuning should be explained or summarized first in L237 at the start of the paragraph. Is the first step, i.e. supervision distillation, from L239 to L244, or L239 to L257? What is model-finetuning then?

8. Are the "class priors" in Sec. 4.3 and 4.4 the same as $\pi_{T_e}$?

9. The formulation of Pcomp should be explained somewhere, especially the meaning of "unlabeled pairwise observations were provided" in L402.

10. The legend in Fig. 2(d) is not visible.

11. The notation $C$ is first used in Eq. 2. The author also uses $C_g$ and $C_l$ for various constants in the theoretical analysis. I recommend distinguishing them. Additionally, $D$ is used in Eq. 2 and also as some datasets.

[1] CLIP is Also an Efficient Segmenter: A Text-Driven Approach for Weakly Supervised Semantic Segmentation. [CVPR 2023]

### Soundness
4

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the potential of leveraging pre-trained models for weakly supervised learning (WSL).  The authors first demonstrate that a zero-shot baseline using a CLIP model with GPT-4o enriched class descriptions surpasses existing state-of-the-art WSL methods trained from scratch. Recognizing the potential for further improvement through fine-tuning, they identify limitations with existing unbiased and corrected risk estimators, noting issues with overfitting exacerbation and feature degeneration.

To address these issues, they propose a novel "Weakly Supervised Fine-Tuning (WSFT)" approach. WSFT utilizes dual classification heads: one trained on a corrected risk estimator to distill reliable supervision, and another trained via empirical risk minimization on the subset of data with high-confidence predictions from the first head. This iterative process allows for efficient model fine-tuning. The authors provide theoretical guarantees for the consistency and convergence rate of their proposed risk estimator. Finally, they present extensive empirical results on various WSL problems (PU learning, Pcomp learning, and UU learning) across benchmark datasets (CIFAR-100, EuroSAT, Oxford-IIIT Pet, Caltech-101), showing that WSFT consistently outperforms existing SOTA WSL approaches. In summary, the paper’s main contributions are: demonstrating the power of pre-trained models for WSL, proposing the novel WSFT algorithm with theoretical grounding, and empirically validating the effectiveness of WSFT across a range of WSL problems and datasets.

### Strengths
+ This paper tackles the largely unexplored intersection of pre-trained models and weakly supervised learning, showing the untapped potential of existing pre-trained models for WSL.

+ The paper is written clearly and concisely, with a logical flow that guides the reader through the motivation, methodology, theoretical analysis, and experimental results.

### Weaknesses
 - While the paper presents extensive experiments across various benchmark datasets, the choice of datasets could be expanded to include more diverse and challenging scenarios, e.g., ImageNet and other variants.

- This paper does not explain how to generalize to multiple-class setting, especially what changes need to be made in the loss objective.

### Questions
- How robust is WSFT to varying levels of label noise and class imbalance?

- Given the connection to self-training, have you considered including a self-training baseline using the same pre-trained model and data augmentation strategies for a direct comparison?  This would help isolate the specific benefits of the dual head approach and supervision distillation in WSFT.

### Soundness
3

### Presentation
2

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
The authors proposed a WSFT method for effectively fine-tuning pre-trained models for various WSL problems. Specifically, WSFT uses dual classification heads to alternately combine the reliability of supervision distillation and the efficiency of model fine-tuning, and theoretically proves the correctness of its methods. Finally, the authors conducted extensive experiments on various WSL problems and benchmark datasets, validating the effectiveness of the proposed method compared to SOTA WSL methods.

### Strengths
The authors' method has a solid theoretical proof with a detailed proof process. The main theme of the article is clear. It first finds that the original weakly supervised training is not as good as the performance of the Clip model, then further analyzes the problem in depth, introduces new theories to solve it, and ultimately proves the correctness and effectiveness of the method through both theory and experiments.

### Weaknesses
An overview figure could be added to make the entire process clearer.

### Questions
(1) For binary classification tasks, is the conclusion related to the division of the dataset categories? How much impact does directly using GPT for division of the datasets have on the results, and has any verification been done for other combinations? How to consider the impact of the division of positive and negative samples on the results? 

(2) Regarding question 1, can a simple verification of the effect on multi-class classification be conducted?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a WSFT approach to effectively fine-tune pre-trained models for various WSL problems. WSFT encapsulates reliable supervision distillation and efficient model fine-tuning seamlessly supported by theoretical guarantees. Extensive experiments on various WSL problems and benchmark datasets validate the effectiveness of WSFT.

### Strengths
This paper proposes a novel weakly supervised fine-tuning approach using dual classification heads that are trained synergistically
by alternately distilling reliable supervision and performing efficient model fine-tuning. Theoretically, the authors prove the consistency and convergence rate of the proposed risk estimator.

### Weaknesses
1. The zero-shot baselines exhibit better performance in few pairs setting in table 2, which brings the concerns of effectiveness of WSFT in few shot scenarios. It would be better to provide additional analysis or experiments to examine WSFT's performance in other few pairs settings. Specifically, the paper should explore the sensitivity of WSFT to the number of labeled examples, and provide a more granular analysis of the performance gap between zero-shot and WSFT as the number of labeled pairs increases. The current analysis lacks a clear understanding of the conditions under which WSFT is most effective, and when zero-shot methods might be preferred.
2. More recent methods are expected in comparison. Most of the compared apporaches seems to be out-of-data (2021 or before in table 2 and table 3). The absence of comparisons with more recent state-of-the-art methods limits the paper's ability to demonstrate the true advancement of WSFT. The paper needs to include a more comprehensive comparison with methods published after 2021, especially those that address similar weakly supervised learning problems. This would help to better contextualize the contribution of WSFT and highlight its advantages over current approaches.

### Questions
1. In table 1, the results of WSFT on Oxford-IIIT Pet-b is worse than CVIR and DistPU. Further analysis is expected to explain this phenomenon.
2. In table 2 and table 3, experiment results with more recent approaches should be presented.

### Soundness
3

### Presentation
2

### Contribution
3
