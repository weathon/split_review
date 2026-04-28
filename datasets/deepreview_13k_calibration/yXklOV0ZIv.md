# Learnable Counterfactual Attention for Singer Identification

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Counterfactual attention learning (Rao et al., 2021) utilizes counterfactual causality to guide attention learning and has demonstrated great potential in fine-grained recognition tasks. Despite its excellent performance, existing counterfactual attention is not learned directly from the network itself; instead, it relies on employing random attentions. To address the limitation, we target at singer identification (SID) task and present a learnable counterfactual attention (LCA) mechanism, to enhance the ability of counterfactual attention to help identify fine-grained vocals. Specifically, our LCA mechanism is implemented by introducing a counterfactual attention branch into the original attention-based deep-net model. Guided by multiple well-designed loss functions, the model pushes the counterfactual attention branch to uncover attention regions that are meaningful yet not overly discriminative (seemingly accurate but ultimately misleading), while guiding the main branch to deviate from those regions, thereby focusing attention on discriminative regions to learn singer-specific features in fine-grained vocals. Evaluation on the benchmark artist20 dataset (Ellis, 2007) demonstrates that our LCA mechanism brings a comprehensive performance improvement for the deep-net model of SID. Moreover, since the LCA mechanism is only used during training, it doesn't impact testing efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a learnable counterfactual attention mechanism, specifically tailored for the singer identification task, aiming to address the limitations of existing counterfactual attention learning. Unlike the traditional approach that depends on random attentions, the LCA mechanism enhances the ability of counterfactual attention to identify fine-grained vocals through direct learning. The implementation involves integrating a counterfactual attention branch into the existing model. This addition is meticulously guided by multiple loss functions, ensuring that the counterfactual attention branch focuses on regions that are meaningful yet not overly discriminative, avoiding potentially misleading results. Meanwhile, it directs the main branch towards discriminative regions to learn singer-specific features effectively. The performance improvement is demonstrated through evaluation on the benchmark artist20 dataset.

### Strengths
The authors provide a clear and intuitive analysis of the limitations present in the baseline method (CAL), proposing straightforward yet effective solutions to enhance its performance. Each proposed solution, addressing Characteristics 1, 2, and 3, demonstrates simplicity and efficacy. The experimental results solidify the effectiveness of the introduced loss functions, providing tangible evidence of improvement. Furthermore, the manuscript is well-structured and articulated, ensuring a smooth and comprehensible reading experience for the audience.

### Weaknesses
1. Regarding the second Characteristic 2 (Targeting biased regions without outperforming the main branch), I can not see the logic between forcing the class distribution to be smooth and targeting biased regions without outperforming the main branch. Moreover, the assertion that a smoother output distribution directly correlates to effectively targeting biased regions without overshadowing the main branch is questionable. Since the output distributions of the two branches lead to disparate final classification results, this assumption appears to be unfounded and requires further clarification. Specifically, the use of a maximum entropy loss to encourage a uniform class distribution in the counterfactual branch does not inherently guarantee that the branch will focus on common biases. While a uniform distribution might indicate a lack of strong discriminative features, it doesn't explicitly force the model to learn biases. The connection between a smooth output distribution and the model's attention to biased regions is not clearly established. It's possible that the counterfactual branch could achieve a uniform distribution by focusing on random, non-discriminative features rather than actual biases present in the data. Furthermore, the claim that this approach prevents the counterfactual branch from outperforming the main branch is not sufficiently justified. A uniform distribution does not necessarily imply lower performance; it simply means the model is not confident in any particular class. The counterfactual branch could still learn some discriminative features, even with a uniform output, and potentially outperform the main branch in certain scenarios. 

2. Regarding Characteristic 3 (Regions of focus should differ from the main branch’s attention), the manuscript appears to implicitly assume superior performance of the main branch. However, empirical observations suggest that the main branch’s performance is not as exemplary as presumed. A straightforward deviation from the main branch's attention map might inadvertently introduce inaccuracies. This aspect of the methodology warrants a more cautious approach and a thorough examination to validate its effectiveness and mitigate potential risks of error introduction. The assumption that the main branch always attends to the most discriminative regions is not necessarily true. The main branch might still be influenced by biases or focus on less relevant features. Therefore, simply forcing the counterfactual branch to attend to different regions does not guarantee that it will focus on biases. It could be attending to other non-discriminative regions, which would not serve the intended purpose. The method lacks a mechanism to ensure that the counterfactual branch specifically targets biased regions, rather than just different regions. Moreover, the approach of maximizing the difference between the attention maps of the two branches could lead to instability in training. If the main branch's attention is not stable, forcing the counterfactual branch to deviate from it could introduce noise and hinder the learning process. The method needs a more robust way to ensure that the counterfactual branch focuses on meaningful biases and not just random regions.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a learnable counterfactual attention method to improve the recognition performance of the singer identification task. The method improves the existing counterfactual attention learning framework by replacing the random counterfactual attention with learnable ones. With some new and specifically designed loss functions, the method can better discover effective attention regions and show improvement on SID benchmarks.

### Strengths
- The proposed learnable counterfactual attention is well-motivated and reasonable. Empirical results show the method is effective on the SID task.

- The paper is well-written and easy to follow.

### Weaknesses
 - My main concern is the generality of the proposed method. The proposed method is motivated by the limitations of the existing CAL method. However, this paper only evaluates the method on the SID task, which is a less popular and competitive task compared to the tasks considered in CAL. According to the analysis provided in Section 3.2, LCA didn't add assumptions on the data or task types over CAL. So it is not clear why the proposed method is only evaluated on the SID task. Considering ICLR is a machine learning conference, I think showing the generality of the proposed method is also helpful to make the paper more suitable for publishing on ICLR and interest the audience of the conference. 

- The authors claim the method can "guide the main branch to deviate from those regions, thereby focusing attention on discriminative
regions to learn singer-specific features in fine-grained vocals". I think it would be better to provide some quantitative evidence to support this claim.

### Questions
Although I find the proposed method is well-motivated and reasonable, I still have some concerns about the experimental study and positioning of this paper. I think the paper can be further improved if the above problems can be solved.

### Soundness
3 good

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
This paper proposes to extend counterfactual attention learning via a learnable counterfactual attention module to further improve the ability of counterfactual attention. To learn this learnable attention model, this paper designs a series of loss functions. Beyond the conventional cross-entropy and counterfactual losses, it adds three extra loss terms. First, a cross-entropy loss is applied to the counterfactual attention branch as the regularization term to make the counterfactual attention more meaningful. Second, a multiple classification loss for the counterfactual attention branch is designed to limit the performance of the counterfactual attention. Third, an L1 loss between the attention maps of factual and counterfactual branches encourages the difference.  This method is evaluated with the singer identification task which also requires the fine-grained identification ability.   Specifically, the benchmark artist20 dataset is employed for the comparison, including the comparison with other SOTA methods, and ablation studies.

### Strengths
1) This paper proposes a learnable counterfactual attention module to achieve better performance. 
2) This paper provides detailed explanations of each extra loss-term.

### Weaknesses
Some concerns about this paper are summarized below:
1) From the experiments in the original CAL method. It seems that the refinement of the counterfactual attention branch didn't improve the recognition performance. What is the motivation to refine the counterfactual attention branch? Did you find any insights from the preliminary experiments to support this enhancement path?
2) As shown in Figure 2 and Section 3.2, CAL applies the counterfactual "intervention" to cut off the causal relations between image and attention.  The goal of this "intervention" is to obtain the independent effects and further benefit the calculation of the Total Direct Effect. Here, both the counterfactual and factual branches are learned from the image. From the perspective of causality, how can you guarantee the independence between counterfactual and factual attention for the causal inference? 
3) For the extra loss terms, there are two contradictory losses, one is to make the counterfactual attention meaningful and the other is to make it not too meaningful.  How can we balance these two losses?  Is it robust for different scenarios? Do the hyper-parameters of loss rates matter for the performance?
4)  The motivation of this paper is to improve counterfactual attention learning. Given this goal, it is better to evaluate the proposed method and the key baseline (CAL) in the same settings, such as CUB, Cars, Aircraft, and so on.  
5) As shown in Table 1, the improvement of the proposed LCA is very limited. Why these results can support the conclusion? Take the Best frame-level results as an example, the proposed method only improves 0.02 accuracy. 
6) Only one dataset is used.  The evaluation process seems to be not solid.  It is suggested to add more.

### Questions
Beyond the questions in the weaknesses part, there are some questions for the details. 

1) As shown in Table 1, which counterfactual attention is used as a baseline, random, mean, or shuffle?
2) What are the loss rates used in the experiments?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper is out of my knowledge, and I tend to not submit any reviews for this paper. Thanks for the submission. Please ignore my ratings.

### Strengths
This paper is out of my knowledge, and I tend to not submit any reviews for this paper. Thanks for the submission.

### Weaknesses
This paper is out of my knowledge, and I tend to not submit any reviews for this paper. Thanks for the submission.

### Questions
This paper is out of my knowledge, and I tend to not submit any reviews for this paper. Thanks for the submission.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
