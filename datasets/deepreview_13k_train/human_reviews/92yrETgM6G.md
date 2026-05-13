# Calibration Attack: A Framework For Adversarial Attacks Targeting Calibration

- Decision: Reject
- Scores: 5, 5, 1, 5

## Abstract
We introduce a new framework of adversarial attacks, named calibration attacks, in which the attacks are generated  and organized to trap victim models to be miscalibrated without altering their original accuracy, hence seriously endangering the trustworthiness of the models and any decision-making based on their confidence scores. Specifically, we identify four novel forms of calibration attacks: underconfidence attacks, overconfidence attacks, maximum miscalibration attacks, and random confidence attacks, in both the black-box and white-box setups. We then test these new attacks on typical victim models with comprehensive datasets, demonstrating that even with a relatively low number of queries, the attacks can create significant calibration mistakes. We further provide detailed analyses to understand different aspects of calibration attacks. Building on that, we investigate the effectiveness of widely used adversarial defences and calibration methods against these types of attacks, which then inspires us to devise two novel defences against such calibration attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new type of problem to attack the calibration of a DNN without misleading its prediction results. Four attack goals are set: underconfidence attacks, overconfidence attacks, maximum miscalibration attacks, and random confidence attacks. The authors achieve the goals by designing new attack loss, and using existing white-box and black-box attack algorithms. Comprehensive experiments validate the effectiveness of the method.

### Strengths
1. It is good to see a proposal for a new attack problem.
2. The authors explore different attack scenarios in the new problem.
3. The conducted experiments are extremely extensive. I appreciate the comprehensive evaluation of various white-box, black-box attacks, as well as the defenses.
4. The paper is well-written and easy to follow, and it gives a good survey of existing work.

### Weaknesses
1. The technical contribution is not strong. The modification from misleading the prediction to misleading the calibration is very straightforward. Because misleading the prediction is achieved by controlling the logits, making the ground-truth logits lower than other logits. And certainly, it is easy to manipulate the logits to be any distribution, hurting the calibration. The paper does not delve into the nuances of how different logit manipulations affect calibration metrics specifically, beyond a general observation that it can be done. A more detailed analysis of the relationship between logit manipulation strategies and the resulting calibration error would be expected.

2. It would benefit more readers if the authors put their emphasis on the significance of calibration attack, instead of the specific method. Since the paper is proposing a new problem, which is brave, the most important thing would be claiming that it is a worthwhile thing. I am not convinced by the only illustration of autonomous driving in the introduction. The design of each method looks too complicated and distractive. The paper lacks a compelling argument for why attacking calibration, independently of accuracy, is a critical problem. The autonomous driving example, while relevant, is not sufficient to establish the broad significance of this research direction. The paper should include a more thorough discussion of the potential impact and real-world implications of calibration attacks across various domains.

3. It may be a more concise and clear way to present Algorithm 1 and the two defense methods. The current presentation of Algorithm 1 and the defense methods is dense and difficult to parse. The paper could benefit from a more streamlined and intuitive explanation of these technical components, possibly using pseudocode or diagrams to enhance clarity.

### Questions
Response to rebuttal: Thanks for the rebuttal. I agree that this is a decent work, but the contribution is not significant enough for ICLR, as also mentioned by Reviewer YLZS. The efforts are far from sufficient to convince the community that the new problem is significant.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed four types of adversarial attacks targeting calibration specifically, which maximizes the error in model’s prediction score without alternating the predicted label/accuracy. Building on top of some existing successful adversarial attack technique (e.g. SA), the authors achieve miscalibration through lowering the prediction on correctly classified cases and increasing the prediction on incorrect cases. It is shown to be effective on many models/datasets even in the presence of popular calibration methods. Authors also discussed the parameter choices and how they affect the performance of the attack.  In addition, the authors proposed new calibration methods that are capable of defending the attacks proposed in this paper.

### Strengths
- The subject of this research seems novel. It is distinctive from most types of adversarial attack studies that aims to increase misclassification and lower the predictive accuracy. Instead, it has the constraint of not affecting this most notable performance metric while maximizing the error in the confidence level, which is often overlooked.
- The experiments have good coverage on different cases and sufficiently demonstrated the authors' conclusion. The discussion is also thorough about the design choices in both the attack algorithm and the defending methods.
- The paper is clearly written and easy to follow.

### Weaknesses
 - The authors' motivation for calibration attack is that the prediction score instead of the classified label is directly used in downstream tasks. However, most of the experiment results are presented in terms of the calibration error, but did not explore further on its effect on the downstream. Without a concrete example, it is hard to assess the significance on the implication of this error on confidence score.
- While the idea of attack on calibration is new as far as I know, the attack mechanism is largely based on the existing methods and does not seem to have significant novelty in itself.
- In terms of the defense method, it is unclear whether it only addresses the attacks proposed in the paper or has more general effectiveness. Based on the pre-attack result in table 4, it doesn't seem to be superior than other existing calibration methods in terms of fixing general miscalibration, which gives me the concern that it might be only effective towards these specific attacks.

### Questions
- The attack algorithm is independent between samples, but is it possible to inferred information about the model on its tendency to be over/under-confident and reduces the query sizes?
- Is it still possible to perform the attack if only the predicted class label can be queried?
- Is it possible to attack the training process and have the model be over/under-confident on unaltered samples?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a test-time attack that manipulates a classifier’s confidence scores without changing the classifier’s prediction. Two types of manipulation are considered: (1) increasing the classifier’s confidence for the predicted class and (2) decreasing the margin between the confidence of the predicted and runner-up class. These manipulations can be applied to inputs randomly or to maximize miscalibration. The attacks are carried out using a variant of the square attack (a gradient-free algorithm) or projected gradient descent and are shown to be effective empirically on standard image datasets. The paper also studies the effectiveness of the attack under four calibration methods (e.g., temperature scaling, splines) and under defenses such as adversarial training.

### Strengths
The paper is comprehensive in that it covers several variants of the proposed attack (black-box, white-box, different confidence manipulations) while also exploring potential defenses. The empirical results are extensive: there is a good selection of datasets, models, and evaluation metrics.

I appreciate that the paper studies a non-conventional threat model. A benefit of the proposed attack is that it has the potential to cause harm with a smaller perturbation strength compared to adversarial examples that cause misclassification. For that reason, it may also be more less susceptible to detection, particular if the confidence scores are manipulated randomly.

### Weaknesses
1. My primary concern with the paper is around originality and its failure to cite prior work. The paper claims to be the first to study attacks on confidence scores, however a very similar test-time attack was proposed by Galil & El-Yaniv (2021) [2]. More recently a training-time attack on confidence scores was proposed by Zeng et al. (2023) [3] (which first appeared on arXiv in 2022). It’s unfortunate these papers are not cited. There is also closely related work on certifying confidence scores by Kumar et al. (2020) [1] and Emde et al. (2023) [4] which ought to be cited.

2. In order to better assess originality, I have compared this paper with Galil & El-Yaniv (2021) [2]. As far as I can tell, the differences between the attacks are minor:
    - Galil & El-Yaniv [2] focus on reducing the confidence of the predicted class, whereas this paper also considers increasing the confidence.
    - Galil & El-Yaniv’s [2] attack algorithm is FGSM-based, whereas this paper uses the Square attack algorithm and PGD.
    - Galil & El-Yaniv [2] maximize/minimize the confidence of the predicted class directly, whereas this paper also considers the margin.
Apart from attacks, this paper also contributes some insights on defences, which is not something that Galil & El-Yaniv [2] cover. However, overall I don’t believe this paper’s contributions are sufficiently original/significant, at least in its current state.

3. Regarding the presentation of Section 5: I found it confusing that the calibration methods (TS, Splines, DCA, SAM) are presented alongside the defenses (AAA, AT, CA AT, CS). I think there is a risk that some readers may misinterpret the calibration methods as defenses, even though they are not designed to defend against attacks. 

4. A missing baseline defense: Kumar et al. (2020) [1] propose Gaussian randomized smoothing as a method with certified guarantees on the confidence scores. While their guarantees may not be in perfect alignment with the $\ell_\infty$ attacks proposed in this paper, I think it’s an important baseline to include, given it’s designed to produce more robust confidence scores. 

5. Clarification of threat model: in order to conduct the _maximum miscalibration attack_ I believe the attacker needs to know the ground truth for each input, so they can perturb the confidence in the direction that causes maximum miscalibration. I wonder whether it is realistic to assume the attacker knows the ground truth for all inputs they want to attack. If they were able to obtain the ground truth cheaply, then it may suggest that the classification problem is not so difficult.

### Questions
1. Given the existence of prior work on calibration attacks, you could consider focusing more on the defense side (where there has been less work) or on variations of the threat model.

2. For underconfidence attacks, the attack minimizes the margin between the scores of the predicted and runner up classes. Have you considered optimizing the scores of the other classes as well? For instance, one could imagine trying to perturb the scores to be close to uniform by maximizing the entropy of the scores.

3. It seems the defenses are tested under the maximum miscalibration attack. I wonder how the results would differ for the random miscalibration attack. In particular, I wonder whether the compression scaling defense would be effective in that setting, since it seems to make strong assumptions on the way in which scores are perturbed.

4. Is it possible to transfer these attacks to other classifiers? I expect that transfer may risk harming accuracy, especially if the attacked points are moved closer to the decision boundary. Perhaps over-confidence attacks are more reliable for transfer?

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces calibration attacks, a new class of adversarial attacks that aim to miscalibrate the confidence scores of models without changing their accuracy. The authors propose four types of calibration attacks and demonstrate their effectiveness against image classifiers like ResNet and ViT across datasets. The attacks are difficult to detect using common adversarial defense techniques. Analyses show the attacks modify model representations and confidences as expected while minimally impacting gradient-based visualizations. Existing defense methods like temperature scaling and adversarial training provide limited robustness against calibration attacks. The authors propose two new tailored defenses and analyze model vulnerabilities, highlighting the need for further research into mitigating this dangerous new attack vector which could seriously impact reliability if deployed against real-world systems.

### Strengths
The idea of attacking the calibration of ML models is novel, and the work (analyses, discussion, etc.) is solid. Particularly, the authors conducted extensive experiments on adversarial attacks and defenses.

### Weaknesses
See **Questions** part.

1. Questions about Figure 1.
As mentioned in its caption, red bars represent accuracy and blue bars represent confidence. However, the vertical axis in your image is also labeled as accuracy. Could you explain this in detail? Besides, I noticed that Figure 1 is in PNG format. A vector graphic format might be better.

2. How to calculate the average confidence?
In my opinion, letting "average confidence = the product of the sample proportions in each bin" would provide a reasonable explanation according to your setting. However, in Table 1, I think the average confidence is not calculated in this way. Otherwise, we could have Accuracy = ECE +/- average confidence. 

3. Relation with previous works
I list two more related works on robust calibration. It would be perfect if you could compare your work with theirs.
[1] Tang Y C, Chen P Y, Ho T Y. Neural Clamping: Joint Input Perturbation and Temperature Scaling for Neural Network Calibration, arXiv:2209.11604.
[2] Yu Y, Bates S, Ma Y, et al. Robust calibration with multi-domain temperature scaling, in NeurIPS 2022.

4. The implementation of adversarial attack/defense algorithms.
I found it very hard to parse the results of the experiments. I wonder if the authors could provide the corresponding code to the results in Table 1 (or at least a demonstration) so that I can reproduce and check the results.

### Questions
1. Questions about Figure 1.
As mentioned in its caption, red bars represent accuracy and blue bars represent confidence. However, the vertical axis in your image is also labeled as accuracy. Could you explain this in detail? Besides, I noticed that Figure 1 is in PNG format. A vector graphic format might be better.

2. How to calculate the average confidence?
In my opinion, letting "average confidence = the product of the sample proportions in each bin" would provide a reasonable explanation according to your setting. However, in Table 1, I think the average confidence is not calculated in this way. Otherwise, we could have Accuracy = ECE +/- average confidence. 

3. Relation with previous works
I list two more related works on robust calibration. It would be perfect if you could compare your work with theirs.
[1] Tang Y C, Chen P Y, Ho T Y. Neural Clamping: Joint Input Perturbation and Temperature Scaling for Neural Network Calibration, arXiv:2209.11604.
[2] Yu Y, Bates S, Ma Y, et al. Robust calibration with multi-domain temperature scaling, in NeurIPS 2022.

4. The implementation of adversarial attack/defense algorithms.
I found it very hard to parse the results of the experiments. I wonder if the authors could provide the corresponding code to the results in Table 1 (or at least a demonstration) so that I can reproduce and check the results.

I will be very happy to reconsider my rating if the authors could address my concerns.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
