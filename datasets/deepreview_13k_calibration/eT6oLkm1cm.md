# Annealing Self-Distillation Rectification Improves Adversarial Training

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In standard adversarial training, models are optimized to fit invariant one-hot labels for adversarial data when the perturbations are within allowable budgets.
However, the overconfident target harms generalization and causes the problem of robust overfitting.
To address this issue and enhance adversarial robustness, we analyze the characteristics of robust models and identify that robust models tend to produce smoother and well-calibrated outputs. 
Based on the observation, we propose a simple yet effective method, \textbf{A}nnealing Self-\textbf{D}istillation \textbf{R}ectification (\OURS), which generates soft labels as a better guidance mechanism that reflects the underlying distribution of data.
By utilizing \OURS, we can obtain rectified labels that improve model robustness without the need for pre-trained models or extensive extra computation. Moreover, our method facilitates seamless plug-and-play integration with other adversarial training techniques by replacing the hard labels in their objectives.
We demonstrate the efficacy of \OURS \space through extensive experiments and strong performances across datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Annealing Self-Distillation Rectification (ADR), an improved adversarial training (AT) method that emphasizes the rectification of the labels used in AT. It is found that the outputs of robust and non-robust models are distributionally different in several aspects, and it is argued that labels rectified in a noise-aware manner can better reflect the output distribution of a robust model. Hence, the proposed ADR uses the interpolation between the one-hot labels and the outputs of an EMA teacher to produce the rectified distributions, which replace the one-hot labels used in existing AT methods. Experimental results suggest that ADR can achieve state-of-the-art robust accuracy.

### Strengths
1. The proposed method ADR is intuitive and can be easily integrated into different AT methods.

2. Experimental results suggest that ADR can achieve significant improvement over the baseline and superior robust accuracy to existing methods.

3. The details of the method and the experiments are clearly stated, and the source code is also provided.

### Weaknesses
1. While Section 3.2 provides some insightful observations, it is not very clear how they are reflected by the design of the proposed ADR. Particularly, Section 4.1 mentions that robust models should "generate nearly random probability on OOD data" and "demonstrate high
uncertainty when it is likely to make a mistake". However, there is no direct evidence (analytical or empirical) for how ADR may help achieve these properties. Instead, it seems that the motivation for ADR mostly comes from the previous works (like those cited in Section 4.1) that suggested the importance of label rectification in AT. The connection between the observations in Section 3.2 and the specific design choices in ADR, such as the use of an EMA teacher and the interpolation factor, remains unclear. A more detailed explanation of how these components contribute to the desired properties of a robust model is needed.

2. In Table 3, it is shown that using DDPM data can improve the robust accuracy of WRN-34-10 trained via AT+ADR, but at the cost of a significant decrease in standard accuracy. This may be undesired since augmenting the training set with DDPM data can improve both clean and robust accuracy for AT according to (Rebuffi et al., 2021a). There should be some explanations or discussions on this issue. The observed trade-off between robust and standard accuracy when using DDPM data with WRN-34-10 is concerning. It is important to understand why the method fails to maintain standard accuracy in this specific scenario, especially since the cited work suggests that DDPM data should improve both metrics. This discrepancy raises questions about the general applicability of ADR across different architectures and datasets.

3. The texts in Figure 2 may be too small, which can be difficult to read when printed out.

### Questions
1. Are the robust models trained via ADR more conformed to the empirical findings in Section 3.2, as compared with vanilla AT?

2. Should the rectified labels be assigned to adversarial images only, or both clean and adversarial images? Considering that different AT methods use different targets for clean and adversarial images (e.g., PGD-AT and TRADES), this can be an important question when one would like to apply ADR to other AT methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the phenomenon of robust overfitting and reports that robust models exhibit outputs more calibrated compared to standard models. It further proposes a label smoothing scheme for mitigating overfitting in adversarial training via employing model weight averaging, annealed interpolation and softmax temperature. Experimental results indicate robustness gains and a reduction of the severity of robust overfitting.

### Strengths
- The experiments performed are extensive and incorporates several baseline methods for comparison.
- Modifying self-distillation EMA (weight averaging) with annealed interpolation and softmax temperature is an interesting idea.

### Weaknesses
 - While the method is shown to increase the robustness and mitigates overfitting, other experimental results seem to lack significance for drawing conclusions (weight loss lanscape, effectiveness of temperature and interpolation parameters).
- The relation to other similar methods investigated is not clear (see questions).

### Questions
- In Table 2, test accuracies of ADR combined with WA and AWP are presented. From the results it seems that each method contributes a (roughly) similar amount of robustness gain. Could the authors comment on whether they consider ADR, WA, AWP to be complementary?
- In the motivation (subsection 4.1.) it is stated that the aim is 'to design a label-softening mechanism that properly reflects the true distribution'. In the presented approach the teacher network provides the probability distribution with which the one-hot label is interpolated. Can the authors comment on why the teacher network (model weight average of student) reflects the 'true distribution'?
- The results presented in Figure 5 show the results of a hyperparameter study for the interpolation and temperature parameter. It is concluded that annealing both parameters is beneficial for robustness. Do the authors consider the differences (e.g. in the row on $\lambda$ annealing) significant enough to draw such conclusions?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a novel adversarial training scheme where the ground-truth labels are rectified with an EMA teacher network. The experimental results show that the proposed method achieves a better accuracy-robustness trade-off with smaller overfitting gaps than the baselines. The proposed method can also be integrated with other AT approaches and brings further robustness boost.

### Strengths
- I appreciate the simplicity of the proposed method. It should be easy to implement and it can be used with other AT techniques.
    
- The paper presents a clear motivation for the proposed method with experimental results. I also find the idea behind inspiring as it is somewhat consistent with my understanding of AT, i.e., easier training (less adversarial/weaker signal) leads to better results.
    
- It is shown that the technique brings small additional training time.
    
- The paper is well-written with nice figures and a clear structure.

### Weaknesses
 - Considering the simplicity of the method, I think the experiments are not very extensive. More datasets (e.g., ImageNet), attacks, and especially baseline AT methods should be considered.
    
- The self-distillation brings high memory cost, which I believe would be a main limitation for the practical use of the proposed method.
    
- It seems that this work is not the first to reveal that robust models are better calibrated, yet the authors conclude this finding as one of the major contributions of this paper.

### Questions
Did you use any pretrained models for initialization? I wonder how ADR works when using pretraining models.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors have proposed a self-distillation method to generate soft labels in AT. The soft labels are crafted by the natural logits of the teacher model and the ground-truth. They clip the weight of soft labels to keep the correct classes having the highest confidence. Besides, Annealing and temperature are introduced to adjust the labels adaptive. Empirical evaluation on  three benchmark datasets shows its improvement on robustness based on baselines.

### Strengths
1. A lot of experiments have been done to show its effectiveness on robustness compared with other knowledge distillation methods, which makes it credible.
2. The paper is well-organized and easy to understand.
3. The paper has shown abunbant experimental details, with good reproducibility.

### Weaknesses
1. The motivation, while presented as straightforward, lacks a strong connection to established theoretical underpinnings of adversarial training. The concept of using soft labels in adversarial training is not entirely novel, and the paper does not sufficiently explore the theoretical implications of the proposed rectified label approach. Specifically, a more rigorous analysis of how the rectified label affects the loss landscape and optimization dynamics during adversarial training would strengthen the motivation.

2. The results presented in Table 2 raise concerns about the scalability and generalizability of the proposed ADR method. Specifically, on WRN models across all three datasets, AT+ADR demonstrates weaker performance compared to AT+WA. Similarly, AT+WA+ADR underperforms relative to AT+WA+AWP. This suggests that ADR might not be as effective when combined with techniques aimed at smoothing the model weight landscape, especially on larger models. It raises questions about the compatibility of ADR with other optimization strategies and its effectiveness in high-capacity models.

3. The comparison with RobustBench, while informative, is not entirely fair. The paper should benchmark AT+ADR in isolation against other methods, rather than only presenting results for the combined AT+WA+AWP+ADR. This would provide a clearer understanding of ADR's individual contribution to robustness. Furthermore, the observation that ADR achieves state-of-the-art robust performance on ResNet-18 but exhibits poor performance on WRN highlights a potential limitation in the method's applicability to diverse architectures.

### Questions
Because it has little novelty, its performance is now the most significant evaluation indicator. Its performance on WRN is not competitive enough. I will increase my score if better results come out.

=========After rebuttal=============
The authors' response address most of my concerns. I thus am willing to increase the rating to 6

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
