# IKL: Boosting Long-Tail Recognition with Implicit Knowledge Learning

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
In the field of visual long-tailed recognition, the long-tailed distribution of image representations often raises two key challenges: (1) the training process shows great uncertainty (e.g., uncertainty in the prediction of augmented views by the same expert for the same sample) and (2) a marked bias in the model's prediction towards the head class.
To tackle the above issue, we propose a novel method termed Implicit Knowledge Learning (IKL) to extract the knowledge hidden in long-tail learning processes, aiming to significantly improve performance in long-tail recognition. Our IKL contains two core components: Implicit Uncertainty Regularization (IUR) and Implicit Correlation Labeling (ICL). The former method, IUR, exploits the uncertainty of the predictions over adjacent epochs. Then, it transfers the correct knowledge to reduce uncertainty and improve long-tail recognition accuracy. The latter approach, ICL, endeavors to reduce the bias introduced by one-hot labels by exploring the implicit knowledge in the model: inter-class similarity information.
Our approach is lightweight enough to plug and play with existing long-tail learning methods, achieving state-of-the-art performance in popular long-tail benchmarks. The experimental results highlight the great potential of implicit knowledge learning in dealing with long-tail recognition. Our code will be open-sourced upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework named Implicit Knowledge Learning (IKL) framework to tackle the long-tailed recognition problem. In detail, the IKL framework includes two techniques, so called the Implicit Uncertainty Regularization (IUR) and the Implicit Correlation Labeling (ICL). First, the main idea of IKL is to regularize the predictions of the current epoch using the ones from the previous epoch. It is especially shown to be effective to reduce uncertainty in the tail-class examples. Second, ICL constructs an additional label matrix based on the inter-class similarity, to improve the learning process. This can help to complement the typical one-hot labels. The full framework IKL can serve as a plug-and-play scheme, where it can be attached to existing long-tailed learning methods.

### Strengths
- The necessity of IUR technique is quite clear and noticeable, as presented in Figure 1. Such discovery, where uncertainty values especially on the minor classes grow compared to the ones from the major categories is useful. The proposed scheme can properly address the problem. In addition, learning from correlations between different classes is reasonable. 

- The proposed framework is practical, since it can be built on existing methods to further improve long-tailed learning. 

- Experiments are extensive; it has been tested on more than three or four different types of baseline methods, while demonstrating consistent improvements.

### Weaknesses
 - The critical downside of the proposed work is about technical novelty. The proposed IKL combines two components IUR and ICL, based on using previous predictions and inter-class correlations respectively, both of which are related to well-established literature. For example, as the elementary deep learning based semi-supervised learning methods, Temporal Ensembling [S. Laine et al., 2016] and MeanTeacher [A. Tarvainen et al., 2017] present the generalized version of IUR, where averaging past model predictions or model parameters to enforce consistency loss term. In that sense, despite the limited novelty, the proposed work needs to discuss the previous works in this direction and experimentally compare with those methods in the long-tailed learning scenario. Similarly, regarding the proposed ICL technique, it is common to learn from the dependencies among different class labels (also in the name of co-occurrence) [Z. M. Chen et al., 2019]. Authors also need to acknowledge previous attempts in this direction and provide sufficient discussions on what component is new. In summary, from the technical aspect, it provides limited innovation compared to previous literature that adopts similar approaches.

- As an additional comment on ICL, the effect for applying ICL is currently unclear. To better understand the proposed component, it would be beneficial to quantitatively measure and qualitatively visualize the class-level dependencies (i.e., correlation matrix) on a specific dataset.

- For calculating the class prototypes C, the verification for the superiority of median features compared to simple averaging is missing. Is there any reference or supporting experiments? In addition, it would be further helpful to provide a brief explanation about how to compute a median of features.

- A proof-reading process, especially for referencing papers, is necessary. A lot of typos can be found, for example, missing a space (i.e., NCLLi et al.) and missing punctuation (i.e., offline process Peng et al.). Additionally, the reference section needs to be updated. For example, the paper ‘Balanced meta-softmax…’ from Jiawei Ren et al., is presented in NeurIPS 2020, which is written as arXiv in the current version.

### Questions
- To further improve reproducibility, it is recommended to provide the set of parameters for each augmentation operation in RandAugment. 

- Related to the limitation provided in the conclusion, specific demonstration for the increase of space or memory by saving the previous epoch’s predictions and computing class-wise similarity matrix, depending on the number of total samples and classes, would be helpful for better understanding this limitation.  

- It needs to mention that the progressive scaling of $\alpha$ is applied from section 3 for better clarity. It is confusing since it firstly appears in the experiment section.  

---

[Summary and guidance to rebuttal]

Overall, the motivation for the proposed IUR and ICL is quite clear in the context of long-tailed learning and it conveys consistent improvements in experiments. However, as those techniques are not totally new, it is necessary to present connections with previous approaches in those directions and to emphasize the novel aspects of the proposed work. 

---

References

[S. Laine et al., 2016] Temporal ensembling for semi-supervised learning, in ICLR 2016.

[A. Tarvainen et al., 2017] Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results, in NIPS 2017. 

[Z. M. Chen et al., 2019] Multi-Label Image Recognition with Graph Convolutional Networks, in CVPR 2019.

---

Update: The rebuttal partially addressed my concerns, which are presenting connections to previous literature and additional experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
1. This paper aims to address long-tailed recognition via knowledge distillation.

2. Considering the prediction uncertainty of models trained in adjacent epochs, the authors propose to use the model trained in the last epoch to guide the training in the current epoch. 

3. Inspired by this idea, an $L_{IUR}$ loss is proposed by directly distilling knowledge with KL divergence loss from the model trained in the last epoch.

4. Moreover,  models trained by cross-entropy suffer from classifier bias. The paper proposes to use medium-feature to construct a new classifier. Based on the new classifier, it distills knowledge from the model trained in the last epoch again.

### Strengths
1. The paper is clear and easy to follow.
2. The method is simple but effective. Improvements are observed when combining it with previous methods.

### Weaknesses
 1. The proposed L_{IUR} loss uses KL loss to regularize the output from the current model to be similar to the output from the model of the last epoch.      
    Because the last epoch model is fixed, the KL loss is actually equal to a cross-entropy loss with soft labels from the last epoch model.
    The proposed L_{ICL} loss uses the pseudo-label from the last epoch model. The pseudo-label is calculated based on the medium-feature classifier.     
    The difference between L_{IUR} and L_{ICL} is that L_{IUR} distills knowledge with a biased classifier while L_{ICL} distills knowledge with a medium-feature classifier without bias.    
    Thus, from my point of view, the proposed method is a kind of ensemble of distillation with a rebalanced classifier (with L_{ICL}) and a biased classifier trained with cross-entropy (with L_{IUR}).     

2. The authors claim that uncertainty of models trained in adjacent epochs exists. Is it really important?        
    If we use only one well-trained teacher model through the training, it can also help models give consistent predictions.      
    The paper should show the necessity of distillation with the model trained in the last epoch rather than a specific well-trained teacher model.    

3. Comparison with previous distillation-based methods are missed.      

4. What's the medium function in Eq. (7)? How to rank the features and find the medium?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on addressing the long-tailed problem from the perspective of the training process uncertainty and model prediction correlation. it proposes an  Implicit Knowledge Learning method which consists of an Implicit Uncertainty Regularization (IUR) for mimicking the prediction behavior over adjacent epochs and an Implicit Correlation Labeling (ICL) to reduce the bias introduced by one-hot labels. Experiments are conducted on various long-tailed dataset.

### Strengths
1. The proposed idea is clear and easy to understand.
2. The authors commit to open-sourcing the code to facilitate result reproduction.
3. The authors discuss some potential limitations, such as computational costs.
4. The IKL is a plug-and-play method which could be plugged into many existing long-tailed solutions and bringing performance improvement.

### Weaknesses
1. While some improvement can be observed in the tail classes, currently, there is no concrete evidence to support the claim that learning between two adjacent epochs can enhance the model's performance. The authors should provide more theoretical justification for this claim rather than relying solely on empirical observations from training experiments. Specifically, the mechanism by which the proposed Implicit Uncertainty Regularization (IUR) leverages the differences in predictions between epochs to improve generalization is not clearly articulated. It is unclear why minimizing the discrepancy between predictions from adjacent epochs should lead to better performance, especially given that these predictions could both be incorrect. A more rigorous analysis of the loss landscape and how IUR navigates it would be beneficial.
2. IKL appears to be a regularization-based approach to network learning, and indeed, there are other regularization-based solutions for long-tail problems (e.g., WD[1]). It would be beneficial for the authors to provide a more detailed comparison between IKL and these existing solutions. The current discussion lacks a thorough analysis of how IKL's regularization differs from methods like weight decay or label smoothing, and how these differences contribute to its performance. A more detailed comparison should include an analysis of the loss functions and optimization dynamics of these methods.
3. In Table 7, IUR and ICL don't seem to have brought significant improvements to the results, especially given that this is on a smaller dataset CIFAR-100-LT. This raises concerns about the performance of IKL. The authors should address this concern by providing a more in-depth explanation or conducting additional experiments to demonstrate the effectiveness of IKL. The marginal improvements observed in the ablation study raise questions about the practical utility of the proposed method, especially when considering the added computational cost. The authors should provide a more detailed analysis of the conditions under which IKL provides a substantial benefit, and when it might be less effective.

### Questions
1. The authors propose IKL as a solution to address the issue of model prediction uncertainty. In fact, many expert methods like RIDE and SADE are also designed based on the same principle. The authors should provide a detailed explanation of why IKL results in greater improvements when combined with these expert methods compared to using Softmax (e.g., results in Table5, combined with Softmax only improves the performance by 0.5, but combined with RIDE improves 1.4).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
