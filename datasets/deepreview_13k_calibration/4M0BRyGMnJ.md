# Democratic Training Against Universal Adversarial Perturbations

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Despite their advances and success, real-world deep neural networks are known to be vulnerable to adversarial attacks. Universal adversarial perturbation, an input-agnostic attack, poses a serious threat for them to be deployed in security-sensitive systems. In this case, a single universal adversarial perturbation deceives the model on a range of clean inputs without requiring input-specific optimization, which makes it particularly threatening. In this work, we observe that universal adversarial perturbations usually lead to abnormal entropy spectrum in hidden layers, which suggests that the prediction is dominated by a small number of ``feature'' in such cases (rather than democratically by many features). Inspired by this, we propose an efficient yet effective defense method for mitigating UAPs called \emph{Democratic Training} by performing entropy-based model enhancement to suppress the effect of the universal adversarial perturbations in a given model. \emph{Democratic Training} is evaluated with 7 neural networks trained on 5 benchmark datasets and 5 types of state-of-the-art universal adversarial attack methods. The results show that it effectively reduces the attack success rate, improves model robustness and preserves the model accuracy on clean samples.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents an investigation into the defense against universal adversarial perturbations (UAPs), with a particular focus on targeted UAPs. The authors have made a notable observation regarding the entropy spectrum in hidden layers when UAPs are introduced, which serves as the cornerstone for their proposed 'democratic training' approach. This method aims to enhance the adversarial robustness of neural network models. The empirical results provided in the paper demonstrate the efficacy of the approach, as well as its ability to maintain the clean accuracy of the model.

In general, this paper is well-structured and presents a novel approach, which meets the basic criteria of ICLR conference. However, there are some aspects that could be improved or expanded upon to enhance the overall quality and impact of the paper.

### Strengths
1. This paper is well-written and easy-to-follow.
2. The paper makes a commendable observation concerning the entropy spectrum in deep neural network layers, which is a significant contribution to the field and forms the basis for the proposed defense mechanism.
3. The efficiency of the proposed democratic training method is noteworthy. It circumvents the need to generate UAPs during training, instead utilizing a limited number of epochs to identify low-entropy examples, which is a resourceful approach.

### Weaknesses
1. The threat model employed in the experiments primarily utilizes gradient-based attack methods. These methods presuppose access to the model's parameters, aligning with white-box attack scenarios. This appears to be at odds with the assertion in Section 2.3 that adversarial knowledge does not extend to the internal parameters of the model. Clarification on this point would be beneficial.

2. The comparison with adversarial training methods may require further refinement. Adversarial training aims to bolster adversarial accuracy by integrating adversarial examples with clean examples during training. Constraining the number of training epochs could result in an underfit model, which may not provide a fair benchmark. Additionally, it would be advantageous to include a comparison with the widely recognized TRADES method[1], which is absent from the current manuscript.

3. The potential for adaptive attacks warrants consideration. If adversaries are aware of the defense strategy, they could tailor adversarial examples to bypass the defense. I know that in the threat model, no adaptive attacks are considered since the attackers do not know the internal details of the models. However, the chosen attack methods in the experiments inherently rely on gradient information. So I would suggest that the authors should consider the potential for adaptive attacks.

4. The scope of the experiments is largely limited to datasets comprising natural images. It would be beneficial to extend the evaluation to smaller-scale datasets, such as CIFAR-10, to complement the findings and potentially leverage open-source robust models for further exploration of the neuron entropy spectrum concept.

5. While the paper discusses various existing defensive methods against UAPs and includes experimental comparisons, a direct comparison with state-of-the-art methods is missing. It is recommended to condense the background section and incorporate a more thorough comparison with leading-edge techniques.

6. Minor Issues
  (1) Please consider to reduce the margin between Figure 1 and the text.
  (2) Suggesting to add necessary notations (SR) from the main test to the Table 2 for better understanding.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel defense method called Democratic Training to mitigate the impact of Universal Adversarial Perturbations (UAPs) on deep neural networks.  The authors observed that UAPs lead to an abnormal entropy spectrum in hidden layers, which shows the model's prediction is dominated by a small subset of features. Democratic Training mitigates this issue by increasing entropy to ensure model predictions rely on a wider range of features. The approach was evaluated on multiple models and datasets and was found to be effective in reducing attack success rates while preserving accuracy on clean data.

### Strengths
1. The use of entropy to reveal the dominance of UAPs and the concept of Democratic Training as a defense mechanism is innovative.
2. The method was evaluated across various neural network architectures and benchmark datasets, which strengthens the claim of its general applicability.
3. Unlike other defense methods, Democratic Training does not require architectural modifications, which makes it easy to integrate into existing systems

### Weaknesses
1. The evaluation focused primarily on benchmark datasets and common UAP generation methods. It would be beneficial to see how this approach performs on more sophisticated and adaptive attacks, such as adversarial examples generated in dynamic environments. Specifically, the paper lacks an analysis of the method's robustness against iterative attacks where the adversary has knowledge of the defense mechanism. This is crucial because an adaptive attacker could potentially craft perturbations that specifically target the entropy regularization introduced by Democratic Training. Furthermore, the paper should explore the method's performance against attacks that manipulate the feature space directly, rather than just the input space.
2. The proposed method mainly works well on CNN. Authors should validate it in more types of networks, such as transformers. The paper should include a more detailed analysis of why the method is effective on CNNs and what specific properties of CNNs make them more amenable to this defense. It's also important to understand if the method's reliance on layer-wise entropy is a limiting factor for its applicability to other architectures. The authors should discuss the challenges of applying this method to architectures that don't have clear layer-wise structures or where the notion of entropy may not be as straightforward.
3.  The method requires access to a small set of clean data for entropy measurement and training, which might not always be practical. The paper needs to address the limitations of this requirement, especially in scenarios where obtaining clean data is difficult or expensive. It should also explore the sensitivity of the method to the size and quality of the clean dataset used for training. Furthermore, the paper should discuss potential biases that might be introduced if the clean dataset is not representative of the real-world data distribution.

### Questions
1. How about performances of the method on ViT?
2. What's the time cost of the method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To improve neural network robustness to targeted UAPs, this paper proposed an adversarial training-like method that fine-tunes a pretrained model to reduce middle-layer entropy.

### Strengths
1. The experiments are comprehensive.
2. The proposed defense is attack-agnostic which is more practical and efficient.
3. The proposed defense largely reduced the targeted attack success rate.

I tend to accept this pape. However, since I'm not familiar with UAP attack and defense baseline methods, I will listen to other reviewers and public comments and then decide.

### Weaknesses
1. UAP attacks evaluated in the paper were published in 2018,2019,2020 and seem out-of-date. The field of adversarial attacks has progressed significantly since then, with new and more potent attack methods being developed. Evaluating against older attacks may not accurately reflect the robustness of the proposed defense against current threats. It is crucial to assess the defense against state-of-the-art UAP attacks to ensure its practical relevance.
2. After democracy training, there is still a gap between ``AAcc.'' and clean accuracy. I wonder about the effectiveness of democracy training against non-targeted UAPs. The fact that the adversarial accuracy does not reach the level of clean accuracy suggests that the defense might not be fully effective. It is important to understand how the method performs against non-targeted attacks, as these are also a significant concern in real-world scenarios. The paper should provide a more detailed analysis of the method's behavior under different attack types.
3. Average results in Table 4\&5 are ambiguous since there can be a large bias among different networks. Presenting only average results across different networks can obscure the performance variations between individual models. It is important to provide a more granular view of the results, showing the performance of the defense on each network separately. This would allow for a better understanding of the method's strengths and weaknesses across different architectures.

### Questions
1. For RQ3: did you adversarially train a model from scratch or just fine-tune a pretrained model with an adversarial training objective?
2. I'm not very convinced by the claim in Lines 239-243 that says middle-layer feature entropy suggests the model's classification confidence.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author aims to improve the robustness of universarial adversarial by fine-tuning with a small amount of data, mainly by performing entropy based data augmentation to suppress the influence of general adversarial perturbations in a given model. Then the experiment was presented.

### Strengths
1, The setting is reasonable, author want to resist universal adversarial samples through small cost, this may be useful in some situation.
2, Good experiment results.

### Weaknesses
1, The method provided in the article is not novel, overall, it is still based on the 'min-max' methods. And in my opinion, it seems to be a weakened version of adversarial training.

2, The symbols are somewhat confused. For example, in euqation (4), author use $L_{cce}$, I think this means cross entropy loss, but author did not introduce what is $L_{cce}$ before the euqation (4); in algorithm line 3, author define $I_b^{en}$ which is got by SampleGenerator, but do not use it in the following of algorithm, or maybe it have been wirtten as $i_{en}$ in line 4?

3, I try to test the author's algorithm on CIFAR10(VGG16, budget 8/255), but I didn't get such a good result shown in table2, the SR has only decreased by about 10%. Author did not submit the code, so I hope the author can provide a detailed introduction to the settings for Algorithms 1 and 2 (For example, how to select the epoch, learning rate, hyperparameters), and it's best to provide a detailed explanation of each symbol and steps in the algorithm.

### Questions
1: The author obtained the idea of Democratic Training by studying the performance of UAP between different layers in network. I want to know why author said 'Democratic Training does not rely on generating UAPs and are thus not limited to specific UAP attacks.', As mentioned in the article, the UAP analyzed by the author is produced based on FA-UAP, so the properties analyzed should mainly for such kind of UAP, and the algorithm guided by this should also mainly target on FA-UAP. If it cannot be argued that all UAPs have such  properties, then this statement seems unreasonable?

2: The author did not provide a detailed explanation for $H(i)$ in algorithm 2 line 2, according to the equation (3), I think that the author is  trying to say $H(i)$ is an entropy loss. Less strictly speaking, maximizing H(x) means that the various components of x are directly averaged as much as possible. So, is the goal of SG(SampleGenerator, Algorithm 2) equivalent to finding an adversarial sample with each component average? Is this a form of weakened PGD? If so, why is finding weaker adversarial samples beneficial for improving robustness? Why not directly target finding UAP for SG?

### Soundness
2

### Presentation
2

### Contribution
2
