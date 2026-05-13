# How Hard is Trojan Detection in DNNs? Fooling Detectors With Evasive Trojans

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Trojan attacks can pose serious risks by injecting deep neural networks with hidden, adversarial functionality. Recent methods for detecting whether a model is trojaned appear highly successful. However, a concerning and relatively unexplored possibility is that trojaned networks could be made harder to detect. To better understand the scope of this risk, we develop a general method for making trojans more evasive based on several novel techniques and observations. In experiments, we find that our evasive trojans reduce the efficacy of a wide range of detectors across numerous evaluation settings while maintaining high attack success rates. Surprisingly, we also find that our evasive trojans are substantially harder to reverse-engineer despite not being explicitly designed with this attribute in mind. These findings underscore the importance of developing more robust monitoring mechanisms for hidden functionality and clarifying the offense-defense balance of trojan detection.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Paper Summary**

This paper proposes a new method to inject trojan into clean models. Specifically, a new `evasive loss’ is introduced to minimize the distance between the parameters and features of clean/trojan models. Comparison results show that the new loss introduced can effectively evade commonly used trojan detection methods.

### Strengths
**Strengths**

– The writing is clear and the method is easy to understand.
– The paper proposes an interesting method to evade trojan detection.

### Weaknesses
– The method is very incremental with only a new term in loss introduced. 
– The overhead of introducing the new loss term is unclear  (in computation or model quality).
– Comparison with trojan attacking works are not given. 
– The datasets used to evaluate the method are too small.

–  It seems to me the new loss is only tested during the trojan injection method proposed in BadNet? The BadNet is referred to as ‘Standard Trojan’ across the paper. It is still unclear whether your new loss is effective on other trojan attacking methods, such as  WaNet (Nguyen & Tran, 2020b), ISSBA (Li et al., 2021c), LIRA (Doan et al., 2021), and DFST (Cheng et al., 2021).  To prove your new observation is effective, you should at least select more than 1 existing trojan injection methods and combine them with your new loss.

–  The model architecture for evaluation is also unclear to me. The parameter distance between two architectures are computed in your new evasive loss (Sec. 4.1) and I don’t think this is computationally scalable for large models.

– Only 4 datasets are given in the evaluation, and all of them have input size less than 32x32 (GTSRB is downsampled to 32x32 as mentioned in Page.6). I don’t think this is enough to prove the method is effective. 

– A lot of redundant evaluations and figures in the paper. To me, Figure 3, Table 1 and Table 2 are telling the same thing with minor changes in evaluation metrics. Also, the abnormal performance that exists in the results is not fully explained. For example, why `Param` shows better detection rate in `standard trojan` compared to `evasive trojan`?

### Questions
**Questions:**

I think the method proposed has some insights, however the evaluation is not satisfactory.

–  It seems to me the new loss is only tested during the trojan injection method proposed in BadNet? The BadNet is referred to as ‘Standard Trojan’ across the paper. It is still unclear whether your new loss is effective on other trojan attacking methods, such as  WaNet (Nguyen & Tran, 2020b), ISSBA (Li et al., 2021c), LIRA (Doan et al., 2021), and DFST (Cheng et al., 2021).  To prove your new observation is effective, you should at least select more than 1 existing trojan injection methods and combine them with your new loss.

–  The model architecture for evaluation is also unclear to me. The parameter distance between two architectures are computed in your new evasive loss (Sec. 4.1) and I don’t think this is computationally scalable for large models.

– Only 4 datasets are given in the evaluation, and all of them have input size less than 32x32 (GTSRB is downsampled to 32x32 as mentioned in Page.6). I don’t think this is enough to prove the method is effective. 

– A lot of redundant evaluations and figures in the paper. To me, Figure 3, Table 1 and Table 2 are telling the same thing with minor changes in evaluation metrics. Also, the abnormal performance that exists in the results is not fully explained. For example, why `Param` shows better detection rate in `standard trojan` compared to `evasive trojan`?

Overall, I think the paper shows some interesting observations on how to evade trojan detection through Wasserstein distance. However, the evaluation still has room for improvement before acceptance.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to train backdoored models that are stealthier (i.e., they are close to the distribution of clean models). The authors show that standard backdoor detection algorithms have less success against these models and they are also more difficult to reverse engineer (i.e., identify the target class of the attack).

### Strengths
- Evasive trojaning attack specifically designed against model-based defenses, like MNTD.
- Reduces the success of model-level detectors and trigger reverse engineering.

### Weaknesses
 - Several prior attacks that pursue similar goals are not evaluated.
- Most recent reverse engineering defenses are missing.
- The effects of specificity loss are poorly understood.
- Removal-based defenses can be just as effective.

The idea of model-level distribution matching is new and interesting but it's specifically designed against model-level defenses. There are already many works that explore distribution-matching in the latent space [1,2] or try to apply more stealthy poisoning attacks [3]. There are also attacks considered to reduce the artifacts of the backdoor [4]. 

Moreover, in the appendix, the authors show that their attack performs similarly to TaCT but combining with TaCT improves the stealthiness. There's no reason other existing, more advanced, stealthy attacks cannot be combined with TaCT.
The results on backdoor detection show no significant improvement (except against the model-level defenses) over simple baseline attacks. 

All in all, I don't think the submitted paper brings a novel, and significantly more effective idea to the table. The evaluation of prior attacks could be done more thoroughly, I would even remove simple non-adaptive baseline attacks from the main text (because these are essentially toy attacks at this point), and evaluate against a stronger attack in the main text. Of course, when the baseline attack is very weak, the results look much better.

Regarding defenses, there are some recent improvements over K-ARM. Considering that reverse engineering is a difficult task, I believe these more recent methods might be more effective against the proposed attack [6,7]. I encourage the authors to do a better job with their literature search and find the most effective SOTA defenses.

Further, the goal of specificity loss is to reduce artifacts (non-intended triggers the model learns as a result of the attack). This is interesting but I would be curious to understand whether this rough approach (i.e., sample triggers from a distribution and use them in the loss function) introduces different types of artifacts. I recommend the authors use a method like [8] to confirm the effectiveness (and potential artifacts) of this loss term.

Finally, I cannot see any evaluation of removal-based defenses, e.g., [9]. Defenses like NC or MNTD require some small set of clean data which also can enable removal-based defenses. These defenses are shown promising even against the strongest backdoor attacks. I would like to see how effective they would be against the proposed attack. Although not explicitly specified, these defenses are within the threat model studied in the paper, considering the required defensive capabilities. For example, does the increased effectiveness against reverse engineering make the attack easier to remove?

### Questions
See above for my recommendations and questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a more evasive backdoor attack, which can bypass some defence methods. Specifically, to increase the evasion, the attacker designed a so-called evasion loss.

### Strengths
The evasion loss involves three factors: distribution matching (entangling the parameter distribution and the unnormalized logits of clean and trojan networks), specificity (incorrect trigger cannot activate the backdoor), and randomization (random the direction of the difference between poisoned and benign model).

### Weaknesses
The evasion loss indeed challenges the defence, but it should also influence the accuracy of the benign performance and the attack success ratio. That is because this regularization limits the capability of the model to learn the backdoor behavior and normal classification, simultaneously. The authors should provide the ablation study on the hyperparameters of evasion loss to check their effect on the accuracy and attack success ratio. In summary, I recommend the authors provide an ablation study to learn whether the backdoor can be successfully (dependent on ACC and ASR) injected with an additional evasion loss.

I also found some errors in the references, for instance, the author's name of ‘bypassing backdoor detection algorithm in deep learning’ is wrong.

### Questions
As I mentioned in the weakness, does the evasion loss affect the backdoor injection?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a backdoor attack that tries to evade existing defenses. The
idea is based on blending the distribution of begin and trojaned examples. To
mitigate the possible weight analysis based method, the attack was enhanced by
adding random noises. The experiments were performed on MNIST, CIFAR, and GTSRB
and several baseline methods, NC, ABS, K-Arm, Pixel, MNTD, and its very own
method, Param -- the aforementioned weight analysis method.

### Strengths
This is a timely and important topic.

The evaluation on several baseline methods, including inversion based methods as
well as weight analysis.

### Weaknesses
Several existing methods have considered constraining the feature space to
improve backdoor attack, e.g., adding regularization terms by the
label-smoothing attack. The proposed method is yet another one, and it is
unclear how significant this is.

The evaluation uses small datasets and models, which are not convincing. As
larger models have more capacity to hide the backdoor, making it harder to
detect and mitigate.

The considered baseline methods are also relatively out-of-date. I would
recommend a comprehensive literature review of related work: https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning

There is no discussion on adaptive defenses.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
