# Confidence-driven Sampling for Backdoor Attacks

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Backdoor attacks aim to surreptitiously insert malicious triggers into DNN models, granting unauthorized control during testing scenarios. Existing methods lack robustness against defense strategies and predominantly focus on enhancing trigger stealthiness while randomly selecting poisoned samples. Our research highlights the overlooked drawbacks of random sampling, which make that attack detectable and defensible. The core idea of this paper is to strategically poison samples near the model's decision boundary and increase defense difficulty. We introduce a straightforward yet highly effective sampling methodology that leverages confidence scores. Specifically, it selects samples with lower confidence scores, significantly increasing the challenge for defenders in identifying and countering these attacks. Importantly, our method operates independently of existing trigger designs, providing versatility and compatibility with various backdoor attack techniques. We substantiate the effectiveness of our approach through a comprehensive set of empirical experiments, demonstrating its potential to significantly enhance resilience against backdoor attacks in DNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the strategies of choosing samples to inject triggers for training backdoor models. To improve the robustness against backdoor defenses, the paper proposes a confidence-driven sampling strategy for backdoor attacks. Specifically, the proposed method chooses samples with lower confidence scores to inject triggers, making the backdoored models difficult to be defended. Extensive experiments show the effectiveness of proposed method.

### Strengths
To improve the robustness against backdoor defenses, the paper proposes a simple and effective sampling choosing strategy for backdoor attacks. Also, the proposed method can be integrated into various backdoor attacks to improve the robustness. The paper analyzes the proposed method theoretically, indicating the rationality of proposed method.

### Weaknesses
The method is not efficient because it needs to train a suggorate model (e.g. ResNet18) to check the confidence scores. In the paper, the used datasets are two small-scale datasets including CIFAR10 and CIFAR100. Is it time-consuming when traing a suggorate model on a large dataset e.g. image-net?

In the experiments (Table 1, 2 and 3), the used backdoor defenses are not up-to-date. It is better to compare with some recent backdoor attacks e.g. i-bau [1].


### Questions
Does the proposed method perform better against defenses depending on outlier detection than other backdoor defense methods?

In Figure 1, the paper shows the visualizations of two dirty-label attacks. Is there same observations for clean-label attacks?

In Table 1, 2 and 3, the proposed method achieves lower ASRs compared to Random and FUS under the condition of "No Defenses". Could the authors provide more explanations about the results?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new sampling procedure for backdoor attacks. Standard backdoor attacks poison (i.e., insert a backdoor trigger on) *random* examples from the training set. The authors claim that strategically choosing which training examples to poison can improve on the efficacy of a variety of attacks.  In particular, the authors choose to poison training examples on which a surrogate model exhibits low confidence. Then, the authors provide strong experimental evidence that this sampling scheme improves existing attacks. Additionally, the authors provide intuition for why their method might work on neural networks by analyzing an SVM model on a toy dataset.

### Strengths
- the authors propose a simple method with few hyperparameters that reliably gives good experimental results
- the proposed method can be combined with existing attacks
- the choice of backdoor attacks in the evaluation is thorough
- the writing is clear and concise

### Weaknesses
My main concern is about how practical the idea is. In particular, the adversary is assumed to have:
- *edit* access to the entire train set
- access to a surrogate model that is similar to the model that is being backdoored.

For example, suppose I'm an (adversarial) user of some social media platform P. I know P will train *some* model on the data of its users (including my own data). I could execute a backdoor attack by simply inserting a backdoor trigger in each of my datapoints (e.g., images). However, to execute the proposed attack, I would need the ability to insert data into arbitrary users' profiles---this already makes the attack a lot harder to execute. Additionally, I would need access to a model that acts similarly to the model P will train. Because of this, now I need knowledge of the model P aims to train---in my view, another significant challenge in practice.

As another example in the same vein, consider the setup in [1]. There, the authors poison *expired* web-pages. The above two challenge persists in this setup.

Additional weakness:
- Evaluated defenses: it makes (intuitive) sense to me that the proposed attack works well against outlier-based defenses. However, it is unclear to me whether this will translate to defenses based on model behavior like [2] and [3].

### Questions
- in Table 1, why does your method reduce the efficacy of the attack in the absence of a defense?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Traditional approaches proposed to mount backdoor attacks inject triggers into training samples selected at random. This paper presents a new approach for selecting the training samples to poison in order to launch a more effective backdoor attack. To that end, the authors select samples that are close to the decision boundary between different classes. These samples are the ones that have a low confidence (measured as the probability of a particular class). 

The authors test their approach against 2 baselines: a random baseline, and a baseline where poisoned samples are chosen based on how early they are forgotten during training (FUS). For each of these choices, the authors implement several backdoor attacks, including BadNets, Blend and Adaptive Attacks. The attacks are evaluated when no defenses are employed, and when several defenses are used, such as SS, STRIP, ABL and NC.

The results on CIFAR10 and CIFAR100 show that selecting the samples to poison is more effective than poisoning random samples. Furthermore, several attacks that are not effective (when defenses are employed) with random sampling become effective when the samples to-poison are chosen. 

Finally, the authors investigate the choice of close-to-boundary and far-from-boundary samples to poison to validate that poisoning samples close to the decision boundary is more effective.

### Strengths
- the paper presents a new approach for selecting the samples to be poisoned during a backdoor attack, as opposed to random sampling. the results of the paper show that a good selection is more effective than random selection
- the paper evaluates several backdoor attacks and defenses when random and targeted sampling are used

### Weaknesses
 - the paper considers 2 small datasets: cifar10 and cifar100. it would be great to evaluate on larger datasets, such as imagenet
- the paper evaluates defenses that rely on some notion of outlier detection, and as such, the selection mechanism is effective. the authors however do not evaluate defenses that are not based on outlier detection, such as [1]


[1] Provable Guarantees against Data Poisoning Using Self-Expansion and Compatibility, Jin et al., 2021

### Questions
- FUS is not a method proposed for selecting poisoned samples. how do you do the selection for this technique?
- can you evaluate your method on larger datasets such as imagenet?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
