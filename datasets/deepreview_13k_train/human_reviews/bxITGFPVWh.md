# Sharpness-Aware Data Poisoning Attack

- Decision: Accept
- Scores: 5, 6, 6, 6, 6, 6

## Abstract
Recent research has highlighted the vulnerability of Deep Neural Networks (DNNs) against data poisoning attacks. These attacks aim to inject poisoning samples into the models' training dataset such that the trained models have inference failures. While previous studies have executed different types of attacks, one major challenge that greatly limits their effectiveness is the uncertainty of the re-training process after the injection of poisoning samples. It includes the uncer-
tainty of training initialization, algorithm and model architecture. To address this challenge, we propose a new strategy called ``\textit{Sharpness-Aware Data Poisoning Attack (\ourmodel)}''. In particular, it leverages the concept of DNNs' loss landscape sharpness to optimize the poisoning effect on the (approximately) worst re-trained model. 
Extensive experiments demonstrate that \ourmodel offers a general and principled strategy that significantly enhances numerous poisoning attacks against various types of re-training uncertainty.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper propses revisit exisitng "end-to-end" data poisoning attacks, finds that existing data poisoning attacks suffers from uncertanty issues in poison effects during the re-training process.  Then the reviewer proposes to leverage existing study on loss lanscape for DNNs and propose sharpness-award data poisoning attacks. Specifically, the authors improve upon previous work (e.g., Grad-Match, etc) with replacing original gradients with sharpness-aware gradients. Such sharpness aware loss is calculated by previous work. Through extensive experiements, sharpness-aware poisoning attackd can lead a mild improvement compared with existing approach.

### Strengths
1. The method is intuitive and sound.

2. The evaluation is comprehensive.

3. The results are good.

### Weaknesses
1. The presentation needs improvement.

2. Limited Novelty. The only contribution for this work is that the author combines sharpness-award loss function (proposed by previous work) with existing poisoning approach (e.g., Grad-Match) to make stablize the pisoning effects during the re-training peocess.

3. Lack of theoretical analysis compared with previosu work on data poisoning attacks, such as witches brew (ICLR 2020)

### Questions
Can you evaluate the transferability of poison effects, such as crafting poisoning samples in VGGNet but used for training ResNet.  Can you test your approach across different surrogated models and target models?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper induces sharpness-aware training method towards 3 poisoning tasks: targeted attack (perturb few data to misclassify a sample), backdoor attack (perturb few data to misclassify a class of samples), and unlearnable examples (perturb all data to misclassify all clean test samples). The key design is an additional step to calculate the worst poisoning model before using it to update the poison samples. Experiments show that when plugged in to existing methods, SAPA improves the poison performance steadily.

### Strengths
1. The paper extensively studies three poison attacks to showcase the effectiveness of SAPA. It would be very helpful for the audience since most papers only focus on one task but term the task as poisoning.
2. The introduction of the sharpness-aware idea to poison attacks is straightforward and easy to plug in by adding an adversarial loop. But please make the additional computation amount (X + SAPA v.s. X) more clear.
3. Experiments are comprehensive to demonstrate the steady improvement by SAPA, even under various training strategies. The study on efficiency is informative.

### Weaknesses
1. It would be good if the authors clearly distinguish between different poison tasks before introducing the method. Currently, the threat model is not clear for 3 tasks, and it may be confusing to distinguish the contribution of SAPA in a specific task. For example, in targeted attacks, is the goal to cause misclassification of a single instance or a small set of instances? In backdoor attacks, what is the trigger and how is it applied? For unlearnable examples, what is the expected behavior of the model on poisoned data during training and testing? These details are crucial for understanding the scope and limitations of SAPA.
2. To better demonstrate the plug-in property of SAPA, it is good to be described without a specific attack method, e.g., gradient matching or error-min. And the results should be shown as X v.s. X+SAPA also in targeted and backdoor attacks. Currently, the paper presents SAPA as an enhancement to specific methods, making it difficult to isolate the impact of SAPA itself. A more general formulation would highlight its versatility. For instance, instead of showing results for 'SAPA+Error-min', showing results for 'Error-min' and then 'Error-min + SAPA' would be more informative.
3. "Self-Ensemble Protection: Training Checkpoints Are Good Data Protectors" also focuses on efficient and effective poisoning in retraining. How does SAPA compare to it in the unlearnable examples task in terms of attack performance and efficiency? The paper should include a direct comparison with this method, especially considering the similar goals of achieving effective poisoning with minimal overhead. A comparison should include not only the final attack performance but also the computational cost associated with each method.

### Questions
Response to rebuttal: Thanks for the good rebuttal and revision of the paper. I have no future concerns and thus keep my score.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Previous studies have developed different types of data poisoning attacks, but they are limited by the uncertainty of the retraining process after the attack. To address this challenge, the paper proposes a novel method called Sharpness-Aware Data Poisoning Attack (SAPA), which leverages the concept of deep neural networks' (DNNs') loss landscape sharpness to optimize the poisoning effect on the worst possible retrained model. Extensive experiments are conducted to show the method's effectiveness.

### Strengths
1. The idea of leveraging the concept of loss landscape sharpness to improve data poisoning's efficiency is intriguing. The proposed method is also applicable to different attack objectives.
2. The paper includes vastly extensive experiments with different attack goals, model architectures, re-training variants, etc. 
3. Overall, the experimental results show this method could constantly outperform other baselines.
4. The paper is quite well-writtenm. Especially, the proposed method is explained quite clearly and detailedly.

### Weaknesses
1. The attack success rates are quite unimpressive when the perturbation budgets are low (4/255 for targeted attack and 8/255 for backdoor attack). Specifically, in Table 1, the targeted attack success rate with a perturbation budget of 4/255 is only 6.4% on CIFAR-10 when using a poisoning rate of 0.2%. While there are improvements compared to other baselines, such low success rates raise concerns about the practical applicability of the attack under realistic constraints.
2. The number of defense strategies evaluated in the paper is quite lacking. All defense strategies considered are different re-training variants. While the adversary in this theat model acts as the data provider, there should be experiments with data filtering defenses, such as [1], [2], [3], [4]. Specifically, the paper should evaluate against activation clustering [1] and spectral signatures [2], which are designed to detect anomalies in the feature space. Furthermore, the evaluation should include robust statistical methods like Spectre [3] and frequency-based analysis like the one proposed in [4] to assess the resilience of the attack against more sophisticated defenses. There is also no poisoned model detection defense, such as Neural Cleanse or STRIP, mentioned in the paper.
3. The performance against adversarial training is also quite underwhelming. Table 5 shows that the attack success rate drops significantly under adversarial training, with a maximum of only 1.2% for un-targeted attacks on CIFAR-10. This indicates a lack of robustness of the proposed method against a strong and commonly used defense.

### Questions
1.  Regarding my concern about evalutation against more defense approaches, I would recommend adding experiments with some of the aforementioned defenses
2. It would be better if there are qualitative comparison between clean and poisoned images.
3. I find this sentence in section 5.5 confusing: "In this part, we compare the efficiency and effectiveness trade-off between SAPA and E&R, when they are incorporated to existing defenses, such as Gradient Matching and Sleeper Agent." Do the authors mean "existing attacks" instead?
4. Table 3 is quite hard to comprehend since it does not have best performances highlighted or average accuracy drops. The authors could improve its presentation a bit.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a modification to the objective function of several poisoning attacks wherein poisons are crafted at a parameter vector that has been modified from a standard (ERM trained parameter vector) to increase the attacker's target loss.

### Strengths
1. The authors do a good job of comparing to a wide range of existing attacks in several poisoning settings. 

2. The authors also do thorough experimentation in each of these settings, and include some results under existing defenses.
 
3. Taking the results of the work at face value, the proposed method improves over SOTA poisoning methods, sometimes by a significant margin. 

4. The paper is easy to follow and generally well presented.

### Weaknesses
1. I think the motivation of poisoning the "worst" retrained model isn't fleshed out enough. Why does crafting on the worst-case poisoned model intuitively lead to more generalizable/potent poisons on *average*? It's not clear why optimizing for the worst-case poisoned model would necessarily produce poisons that are effective across a distribution of possible retrained models, especially if the "worst-case" model is an outlier in the space of possible retrained models.

  2. The authors should be more careful when talking about sharpness of minima in this context, as sharpness depends on the *objective* in question. Many might read this work and assume the sharpness the authors are referring to is the sharpness of the minima of the "standard" loss landscape, when this is not what is being discussed. The paper needs to explicitly define what objective's sharpness is being referred to, and it should be in the context of the poisoned model's loss landscape, not the clean model's loss landscape.

3. I would avoid statements like "with a high possibility, the re-trained model can converge to a point where the poisoning effect presents" , and "Therefore, for the models which are re-trained on the poisoned dataset, the poisoning effect is also very likely to persist" as these haven't been justified anywhere in the work. These claims need to be supported by theoretical analysis or empirical evidence, rather than being presented as intuitive truths.

4. A concern raised about existing attacks  in the introduction was that they are not architecture agnostic. While I agree with this concern, this work does nothing to explicitly mitigate this. The method does not incorporate any mechanisms to ensure architecture agnosticism, and thus this critique remains unaddressed.

5. Figure 2 shows that when using ensembles, and restarts, existing methods can beat SAPA. Did you try SAPA with these additions? In general I'm not sure poison crafting time is something to include in the main body/claim as an advantage, especially when the worst times are ~20 minutes. The comparison should focus on the final performance, not the time taken to achieve it, especially when the time difference is not substantial.

6. Gradient matching also considers ensembles.

### Questions
1. Does SAPA also improve poisoning success when paired with objectives other than gradient matching? 

2. Eq. 7 is unclear - you craft $D_p$ on at a parameter vector $\theta^* + \nu$, but $\theta^*$ was the result of ERM on $D_{tr} + D_p$? How was the initial $D_p$ (used in ERM) calculated? Do you have to generate poisons/train a victim model twice?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a data poisoning attack by leveraging sharpness-aware minimization. The method can be applied to backdoor, untargeted, and targeted attacks to improve performance.

### Strengths
1. This paper introduces a unique approach using loss landscape sharpness to enhance poisoning attacks.

2. The method can be applied to various attack settings. 

3. The performance shows the proposed method is effective against existing defenses.

### Weaknesses
The authors have improved the paper from their NeurIPS submission. The remaining concern is that many of the reported results are still not consistent with the results presented in the original papers without proper justification, including both Table 1 and Table 2.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a new approach, called Sharpness-aware Data Poisoning Attack (SAPA), that use loss landscape sharpness to improve the effect of data poisoning attack under the worst scenario (model re-training). The authors elaborate on achieving SAPA in targeted, untargeted and backdoor attacks. SAPA can be incorporated with existing data poisoning approaches and achieve better performance. Evaluations are performed on CIFAR-10 and CIFAR-100 over different tasks (targeted,  untargeted, backdoor) and the results show that SAPA yields better ASR compared to existing attacks.

### Strengths
1. This paper proposes an effective approach to tackle the long-last issue that poisoning attack effect may drop significantly due to worst-case training settings (e.g., re-training).

2. The proposed SAPA is applicable to multiple attacks (i.e., targeted, untargeted, backdoor).

3. The authors perform comprehensive experiments and ablations to show the performance of SAPA and the results are sufficient to support their claim that SAPA can enhance ASR by a large margin.

### Weaknesses
1. SAPA aims to solve the effectiveness of certain attacks (e.g., clean-label integrity and backdoor attacks) that suffer from re-training. On the other side, there existing a line of attacks (e.g., dirty-label attacks such as LIRA, WaNet, BadNets, etc.) that do not have such performance drop. I would suggest the authors clarify the discrepancy between different attacks. Specifically, the authors should discuss the underlying reasons why these dirty-label attacks are more robust to retraining, and how the assumptions made by SAPA differ from those of dirty-label attacks. A more detailed discussion of the threat model and assumptions of different attack types is needed to contextualize the contribution of SAPA.

2. The authors only use CIFAR-10 and CIFAR-100 in the evaluations. However, in prior works such as the Hidden trigger backdoor and Gradient matching, ImageNet is always used to evaluate the attack performance. I suggest the authors also include ImageNet results in the experiments. The lack of ImageNet results limits the generalizability of the findings, as CIFAR datasets are significantly smaller and simpler than ImageNet. Experiments on ImageNet are necessary to demonstrate the effectiveness of SAPA on more complex and realistic datasets.

3. It would be desired to evaluate SAPA against SOTA defenses. The authors provide the result against adversarial training, which is not the best option to defend against poisoning attacks. There are many defenses specifically designed for poisoning attacks such as ABL [1], Fine-pruning [2], Deep KNN[3], etc, it would be nice to evaluate SAPA against these defenses. Furthermore, the evaluation should not only include the performance of the attack under defense, but also the performance of the model under defense when there is no attack. This would provide a more complete picture of the effectiveness of the defense and the attack.

### Questions
Please see weaknesses for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
