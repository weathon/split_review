# Source-Free Target Domain Confidence Calibration

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
In this study, we consider the setup of source-free domain adaptation and address the challenge of calibrating the confidence of a model adapted to the target domain using only unlabeled data. The primary challenge in addressing uncertainty calibration is the absence of labeled data which prevents computing the accuracy of the adapted network on the target domain. We address this by leveraging pseudo-labels generated from the source model’s predictions to estimate the true, unobserved accuracy. We demonstrate that, although the pseudo-labels are noisy, the network accuracy calculated using these pseudo-labels is similar to the accuracy obtained with the correct labels. We validate the effectiveness of our calibration approach by applying it to standard domain adaptation datasets and show that it achieves results comparable to, or even better than, previous calibration methods that relied on the availability of labeled source data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the calibration of model confidence in source-free domain adaptation (SFDA) scenarios, where only unlabeled target data is accessible. The authors introduce **Source-Free Confidence Calibration (SFCC)**, a method that combines a pre-trained feature extractor with a deep clustering approach to improve pseudo-label accuracy and uses temperature scaling to achieve calibration in SFDA. Experiments on benchmarks like VisDA, DomainNet, and Office-Home suggest that SFCC performs comparably to, or better than, some existing methods that rely on source data.

### Strengths
- The paper is structured clearly, with step-by-step explanations that make it easy to follow. For example, the authors use experimental observations to explain why temperature scaling is suitable for SFDA problems even without clean target labels.
    
- The study focuses on a real-world challenge in SFDA where source data may be inaccessible due to privacy or storage issues, and the calibration is particularly relevant.
    
- Extensive testing across different datasets and adaptation methods validate the effectiveness of the proposed method.

### Weaknesses
 - **Limited Novelty**. The novelty of this work is marginal. Calibration approaches for SFDA, particularly temperature scaling, are already covered in previous research [1]. A more extensive literature review and in-depth comparisons with related methods are needed to clarify the contribution and differentiate this work.
    
- **External Feature Extractor**. The use of an external feature extractor for pseudo-labeling in SFDA is not particularly innovative, as similar approaches are seen in prior work [2,3]. Additional discussion on the practicality and computational efficiency of this technique would strengthen the paper.
    
- Experimental Results. The experimental analysis could be more comprehensive and further discussed. Please refer to the Questions.
    
- (Minor) Theoretical Insight. The use of noisy pseudo-labels to estimate bin-wise accuracies is based on empirical results without theoretical insight, which limits the rigor of the approach.

- The claim that the number of correctly self-predicted data points equals the number of data points where the self-prediction matches the incorrect pseudo-label within the same confidence bin, as suggested by Equation (6), is not convincingly supported by Figure 4(b). The figure shows that while the average error is low, there are several outliers with significantly higher errors in the bin-wise accuracy estimation, which casts doubt on the reliability of this assumption.

### Questions
Most of my concerns are centered around the experiments and methodology:

- Will the proposed enhanced pseudo-labelling (EPL) method also benefit the SFDA performance, compared to the baseline methods, SHOT and DCPL?
    
- For calibration, how was the bin number decided? Would variations in bin number affect the calibration outcomes?
    
- In Figures 1 and 2, are the shown results recorded at the end of the adaptation process? How do these indicators evolve during adaptation, and what accuracy levels are associated with the displayed calibration levels?
    
- For temperature scaling, is the optimal temperature calculated on the entire dataset or per mini-batch?
    
- Clarifications Needed:
    
    - In lines 504-510, the argument about classifying difficulty lacks clarity—how does this paragraph validate that claim?
        
    - Does Figure 4b account for outliers, and could they impact the interpretability of the results?
        
    - Figure 3b appears to support Equation (6), but the connection of Eq. (6) to Figure 4b is unclear for me.Please correct me if I've misunderstood anything.

### Soundness
2

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
This paper studies the model calibration problem in the context of source-free domain adaptation (SFDA). The authors claim to propose the first source-free model calibration approach by using only pseudo labels of target-domain data. Specifically, a method called Source Free Confidence Calibration (SFCC) is designed as the solution. SFCC consists of two steps: first using the clustering-based strategy to refine the pseudo labels and then applying temperature scaling with the refined pseudo label-ed target data. Experiments on three SFDA datasets demonstrate that SFCC outperforms existing calibration approaches.

### Strengths
(+) Both the source-free domain adaptation and the model calibration are significant for improving the robustness and generalization of models in real-world scenarios with complex data distributions. Therefore, it is meaningful to study the problem of source-free model calibration.

(+) The background presentation is comprehensive enough to introduce the investigated problem.

(+) It is good to see that code implementation is provided, which is helpful.

### Weaknesses
(-) The technical novelty is not clear. The GEPL method in Algorithm 1 has been widely used in source-free domain adaptation (SFDA) since the pioneering SFDA work SHOT [1] used the iterative version of GEPL to improve the pseudo-label quality. In addition, Algorithm 2 only applies the widely used model calibration method Temperature Scaling [2] to pseudo-labeled target-domain data. Therefore, it seems the technical novelty of this paper is very limited due to the use of many existing techniques without proposing a new one.

(-) The presentation is hard to understand, especially the methodology introduced in Lines 191-208. It is confusing and weak to claim that two versions of A_{i, 1} are equal by definition. By which definition? Presentation from Line198 to Line215 is only based on assumptions without any theoretical or generalized empirical guarantee as the support. This is also for the proposed SFCC method, although experimental results are impressive, it is unknown why SFCC can do well and how it can generalize.

(-) More experiments and ablations are required. First, only three SFDA methods are not enough. Since the claim of this submission is a calibration method for SFDA, only if the authors believe that the selected three SFDA methods (SHOT, AaD, and DCPL) can fully represent existing SFDA approaches, however, is it a fact? Second, it is required to do ablations on GEPL with other techniques of improving pseudo labels such as the common thresholding-based method. Third, other calibration error metrics mentioned in TransCal [3] excluding ECE should be reported because ECE could be misleading sometimes. In addition, what is the accuracy of all SFDA models?

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
2

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
The author proposed a Temperature scaling-based calibration method for the SFDA by leveraging the Pesudo labels.

### Strengths
The idea of calibrating the confidence of a model in interesting.

### Weaknesses
1. Why you think the noisy label would have the same effect of the correct label in calibration? Is there any empirical observation or theoretical guarantee? I doubt this motivation. Specifically, the calibration process relies on the assumption that the pseudo-labels, despite being noisy, provide a reliable estimate of the true class probabilities. This is a strong assumption that requires more justification. It's not clear why the errors introduced by the pseudo-labeling process would not bias the calibration, potentially leading to a miscalibrated model.
2. In Eq.4, what is the difference between the Pseudo label and the predicted label? The distinction between the 'pseudo label' and the 'predicted label' in the context of Equation 4 needs clarification. It's not immediately obvious how these two labels differ, especially since both are derived from the model's output, albeit at different stages of the adaptation process. A more precise definition of each term is needed to understand the equation's purpose.
3. Using $\hat{A}$ to $A$ is not suitable as they would exist a big gap (you do not even know how reliable the pseudo labels are). $\hat{A}_{i}$ would not be equal to $A_{i}$ in this case. Also, the approach from the left to right in Eq.6 should not be held. The core issue here is the substitution of the true accuracy ($A_i$) with an estimated accuracy ($\hat{A}_i$) derived from pseudo-labels. Given the inherent noise in pseudo-labels, it's highly unlikely that $\hat{A}_i$ will accurately reflect $A_i$. The validity of the calibration hinges on this approximation, and the paper needs to provide a strong justification for it. Furthermore, the manipulation in Eq. 6, which assumes a direct equivalence between these potentially disparate quantities, is questionable and requires more rigorous explanation.
4. The reason in Fig.4b may be the fact that you are using a strong pre-trained network, which should not be concluded as a common empirical observation. The observation in Figure 4b, which suggests that pseudo-labels can be used to estimate accuracy, might be an artifact of the strong pre-trained network used. The authors need to demonstrate that this observation is not limited to this specific scenario and holds true for a broader range of models and datasets. Without this, the generalizability of this finding is questionable.
5. Are the bins are divided manually with a fixed number?

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author considers the source-free calibration problem. Since the absence of labeled data, we cannot use the traditional calibration methods. In this way, the author addresses it by leveraging pseudo labels generated from the source model’s predictions to estimate the true, unobserved accuracy. Finally, the author verify the effectiveness on various datasets.

### Strengths
1) The calibration problem is important.
2) The proposed method is effective.

### Weaknesses
1) The paper is hard to read. The author should split the chapters to make them easier to read, for example, the third section should be split appropriately.
2) I am a little confused about this setting, i.e., calibration via the unlabelled data from the target domain. In what scenarios would this setting be used? TransCal [a] realizes calibration via the labeled source domain data. The author may discuss the differences and applications between the two settings. My concern is that we do not need much more data to achieve the calibration (only to fit a single parameter $T$). In real practice, we can try to label some data manually and achieve calibration. For example, for each class, we can simply label one or three samples, which I think will not bring much more cost. In comparison, semi-supervised learning assumes that we have many unlabelled data, thus researchers explore the pseudo label methods to avoid the cost of labeling. Therefore, is it necessary to explore source-free calibration?
3) The pseudo label has been explored thoroughly in semi-supervised learning. Simply transferring it to the calibration lacks novelty. The observation is interesting. However, the solution is still a  pseudo label based method (do not filter out samples via the confidence). I do not think this degenerated pseudo label based method (directly use them for calibration and do not consider whether the pseudo is right or not ) is novelty enough or gives some contributions to the community.
4) The author optimizes the temperature $T$ via the adaECE loss. For a fair comparison, the author should report other evaluation metrics such as SCE. 
5) line 309. "we followed the evaluation protocol described in the TransCal Paper,  which involves splitting each target domain into 80% for training and 20% for validation". It seems that TransCal split the training set and validation set on the source domain. 

minor:
I think the author should draw a main figure to describe the basic setting of the calibration.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
2
