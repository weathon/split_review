# Provably Safeguarding a Classifier from OOD and Adversarial Samples: an Extreme Value Theory Approach

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
This paper introduces a novel method, Sample-efficient Probabilistic Detection using Extreme Value Theory (SPADE),  which transforms a classifier into an abstaining classifier, offering provable protection against out-of-distribution and adversarial samples. The approach is based on a Generalized Extreme Value (GEV) model of the training distribution in the classifier's latent space, enabling the formal characterization of OOD samples. Interestingly, under mild assumptions, the GEV model also allows for a formal characterization of adversarial samples. The abstaining classifier, which rejects samples based on their assessment by the GEV model, provably avoids OOD and adversarial samples. The empirical validation of the approach, conducted on various neural architectures (ResNet, VGG, and Vision Transformer) and tested on medium and large-sized datasets (CIFAR-10, CIFAR-100, and ImageNet), demonstrates its frugality, stability, and efficiency compared to the state of the art.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents SPADE (Sample-efficient Probabilistic Detection using Extreme Value Theory) = a new method for detecting out-of-distribution (OOD) and adversarial samples in neural network classifiers. The key contributions are:
a. A novel method to transform a classifier into an "abstaining classifier" that can refuse to make predictions on suspicious inputs
b. Use of Extreme Value Theory (EVT) to model the training distribution in the classifier's latent space
c. Mathematical guarantees for detecting both OOD and adversarial samples
d. Experimental validation across multiple architectures (ResNet, VGG, ViT) and datasets

I am pretty unfamiliar with Extreme Value Theory, so please flag if if I'm misunderstanding something basic in my review. But I'm very familiar with OOD detection and adversarial attacks, so it could compensate for it.

### Strengths
1. Theoretical Foundation: The approach is grounded in statistical theory (EVT)
2. Sample Efficiency: Good performance even with strong subsampling of the train set
3. Versatility: Works with different architectures and can handle both OOD and adversarial inputs
4. Evaluation: Tested against strong baselines on multiple datasets

### Weaknesses
# 1. Missing challenging near-OOD evaluation
The evaluations in the Table 2 and Table 3 are missing a very simple, yet challenging near OOD detection task which is CIFAR-100 vs CIFAR-10 (and the other way round). [1] shows strong results for large models and also provides a human score to benchmark against. I would be very curious to see the AUROC, AUC and FPR95 on that. I believe that this would be a very worthwhile and easy evaluation to add and I think the authors should try it. The AUROC in particular is something I would really like to see. Also a set of examples of where the model fails. **I will consider increasing my score if the authors successfully address this point.**

# 2. A collection of weakness that do not need to be addressed in the rebuttal:
2.1 Computational Complexity: The GEV model is quadratic in the number of samples
2.2 Performance Trade-off: While SPADE performs well in general, it's sometimes outperformed by simpler methods like KNN for specific tasks
2.3. Parameter Sensitivity: The effectiveness depends on the choice of teacher model and its latent space characteristics
2.4. High FPR95 Values: Shows tendency to be overly cautious. Perhaps rejecting valid samples?

# 3. Weak adversarial attacks used only
The paper's evaluation of adversarial robustness is limited. They only test against the FGSM attack (=very basic) with small perturbation magnitudes (epsilon from 0.001 to 0.004). Given that SPADE is positioned as providing security guarantees against adversarial examples, a more thorough evaluation against SOTA attacks would be necessary to support the claims. Additionally, the authors should clarify whether their evaluation considers attacks targeting just the classifier or the full system including the OOD detector, and include both targeted and untargeted attack scenarios. **This is especially relevant to the next weak point.**

# 4. White-box attacks

I have the following concern that I would like you to address directly:

1. SPADE offers an elegant theoretical framework for OOD detection based on a distance metric in the latent space
2. [1] shows that distance metrics in the latent space can be amazing at even hard, near-OOD detection
3. [2] shows that white-box directly targeting such a metric can *still completely destroy it* with a simple adversarial attack

Given SPADE's reliance on distance metrics in latent space and GEV models, it may be vulnerable to white-box attacks that:

4. Directly optimize perturbations to minimize latent space distances to k-nearest neighbors while maintaining misclassification
5. Exploit knowledge of the GEV model parameters to generate samples that appear in-distribution
6. Target the gap between separate class-specific GEV models to find adversarial blind spots

The authors should consider and discuss these potential vulnerabilities, particularly since they claim SPADE as providing security guarantees. While Theorem 1 provides a lower bound on adversarial perturbation magnitude, an analysis of potential attack strategies and additional defensive measures (such as ensemble approaches or adversarial training) would strengthen the paper's security claims.

### Questions
Included in the weaknesses section.

I am primarily interested in the authors answers to:
a. the CIFAR-100 <-> CIFAR-10 challenging near OOD task(s)
b. the white-box attack on latent metrics point

### Soundness
2

### Presentation
2

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
This paper uses extreme value theory as a means to detect out-of-distribution (OOD) samples. By abstaining to predict on samples that are determined to be OOD, the proposed approach is shown to yield high-probability robustness guarantees against adversarial attacks up to a certain perturbation magnitude. Experiments are conducted on CIFAR-10, CIFAR-100, and ImageNet to assess the performance of the proposed method compared to prior OOD detection schemes.

### Strengths
The problem considered is interesting, and fits well within the scope of the ICLR community. The paper is easy to follow, and does a good job at clearly yet concisely introducing the main tools being used (e.g., extreme value theory). There is a nice blend of conceptual/theoretical development, and empirical evaluation.

### Weaknesses
 The problem considered is interesting, and fits well within the scope of the ICLR community. The paper is easy to follow, and does a good job at clearly yet concisely introducing the main tools being used (e.g., extreme value theory). There is a nice blend of conceptual/theoretical development, and empirical evaluation.

 See my specific Questions below.

 1. Line 90: You use the acronym ID before defining it.
2. Line 102: You should de-italicize the term $\eta$-invariant that you are definining.
3. Definition 3: The role of the parameters $\mu,\sigma,\zeta$ are unclear in how you wrote Definition 3. It seems to me like you need to re-word things to somehow say that "there exist $\mu,\sigma,\zeta$ such that $P(Z^{(\ell)} < z) \to G_{\zeta,\mu,\sigma}(z)$." Otherwise, the reader might be inclined to think that the choice of parameters is somehow "up to us."
4. Line 150: Extreme value theory has been utilized by the ML community in popular robustness verification works such as [1]. I encourage you to take a look at [1] as well as the references therein.
5. Line 169: "For $Y = c$, let $Z_c$ be the random variable defined as the distance between $h(X)$ and its $k$-th nearest neighbor in latent distance, belonging to $\mathcal{D}$ with same class $c$." It would help readability if you write out the mathematical expression defining the random variable $Z_c$.
6. Line 170: What is $k$? Is this a user-specified hyperparameter of your method?
7. Line 171: The notation here is inconsistent; you should be writing $Z^{(\ell)}$, not $Z^{(l)}$. Also, before, you used $P$ for probability, not $Pr$.
8. Line 215: Where is the minimum coming into this equation defining the extreme value distribution $G^{(c,c')}$? It seems like without the minimum inside the probability expression on the right, you aren't really considering extreme values.
9. Theorem 1: It looks like now you are assuming that the instance space $\mathcal{X}$ is a Euclidean space $\mathbb{R}^d$ (so that you can define norms on the instance space as well as Lipschitzness of the embedding map), which was not explicitly assumed before. Therefore, you should make this clear in the theorem statement.
10. Theorem 1: Do you mean to say $f_\tau$ instead of $f_\epsilon$ in the statement of the theorem?
11. Experimental Setting: You state that you generate attacks using FGSM. At this point FGSM, as introduced in Goodfellow et al., 2015, is not really considered by the adversarial robustness community to be a strong attack. At the very least, I'd expect you to use projected gradient descent (PGD) [2], or something stronger like AutoAttack [3] which is used in the RobustBench benchmarks. Have you tested your methods against these stronger attacks?
12. There are a handful of distinct conceptual discussions and innovations leading up to your experiments in Sections 4 and 5. However, there is no explicit description of SPADE where you bring everything together into a single model/algorithm. I think it would greatly benefit readability if you were to conclude your conceptual discussions by writing out SPADE as an explicit algorithm (including any robustness certification steps), immediately before moving into experiments.
13. Line 318: I'm assuming by "KNN" you are referring to $k$-nearest neighbors? You should clearly define this acronym before using it. Similarly, MSP is not defined. Please define it, or at the very least, associate a reference to it.
14. Line 190 and Experiments: On line 190 you said that you would tease out the effect of the latent embeddings on the OOD tests in Section 5 (since your proposed OOD test in Definition 4 depends on the embedding from instance space to latent space). However, after reading through the experiments of Section 5, I do not see how you are answering this concern. Could you clarify?

### Questions
1. Line 90: You use the acronym ID before defining it.
2. Line 102: You should de-italicize the term $\eta$-invariant that you are definining.
3. Definition 3: The role of the parameters $\mu,\sigma,\zeta$ are unclear in how you wrote Definition 3. It seems to me like you need to re-word things to somehow say that "there exist $\mu,\sigma,\zeta$ such that $P(Z^{(\ell)} < z) \to G_{\zeta,\mu,\sigma}(z)$." Otherwise, the reader might be inclined to think that the choice of parameters is somehow "up to us."
4. Line 150: Extreme value theory has been utilized by the ML community in popular robustness verification works such as [1]. I encourage you to take a look at [1] as well as the references therein.
5. Line 169: "For $Y = c$, let $Z_c$ be the random variable defined as the distance between $h(X)$ and its $k$-th nearest neighbor in latent distance, belonging to $\mathcal{D}$ with same class $c$." It would help readability if you write out the mathematical expression defining the random variable $Z_c$.
6. Line 170: What is $k$? Is this a user-specified hyperparameter of your method?
7. Line 171: The notation here is inconsistent; you should be writing $Z^{(\ell)}$, not $Z^{(l)}$. Also, before, you used $P$ for probability, not $Pr$.
8. Line 215: Where is the minimum coming into this equation defining the extreme value distribution $G^{(c,c')}$? It seems like without the minimum inside the probability expression on the right, you aren't really considering extreme values.
9. Theorem 1: It looks like now you are assuming that the instance space $\mathcal{X}$ is a Euclidean space $\mathbb{R}^d$ (so that you can define norms on the instance space as well as Lipschitzness of the embedding map), which was not explicitly assumed before. Therefore, you should make this clear in the theorem statement.
10. Theorem 1: Do you mean to say $f_\tau$ instead of $f_\epsilon$ in the statement of the theorem?
11. Experimental Setting: You state that you generate attacks using FGSM. At this point FGSM, as introduced in Goodfellow et al., 2015, is not really considered by the adversarial robustness community to be a strong attack. At the very least, I'd expect you to use projected gradient descent (PGD) [2], or something stronger like AutoAttack [3] which is used in the RobustBench benchmarks. Have you tested your methods against these stronger attacks?
12. There are a handful of distinct conceptual discussions and innovations leading up to your experiments in Sections 4 and 5. However, there is no explicit description of SPADE where you bring everything together into a single model/algorithm. I think it would greatly benefit readability if you were to conclude your conceptual discussions by writing out SPADE as an explicit algorithm (including any robustness certification steps), immediately before moving into experiments.
13. Line 318: I'm assuming by "KNN" you are referring to $k$-nearest neighbors? You should clearly define this acronym before using it. Similarly, MSP is not defined. Please define it, or at the very least, associate a reference to it.
14. Line 190 and Experiments: On line 190 you said that you would tease out the effect of the latent embeddings on the OOD tests in Section 5 (since your proposed OOD test in Definition 4 depends on the embedding from instance space to latent space). However, after reading through the experiments of Section 5, I do not see how you are answering this concern. Could you clarify?

[1] "Evaluating the robustness of neural networks: An extreme value theory approach," Weng et al., ICLR 2018

[2] "Towards deep learning models resistant to adversarial attacks," Madry et al., ICLR 2018

[3] "Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks," Croce and Hein, ICML 2020

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose sample-efficient probAbilistic detection using extreme value theory (SPADE), which models the training distribution using Extreme Value Theory to create a statistically efficient test that identifies and rejects both OOD and adversarial samples with high probability. Their contributions include a formal OOD definition in relation to a model's latent space, a frugal OOD detection test grounded in EVT, and demonstrated effectiveness against strong baselines across diverse model architectures.

### Strengths
1. The paper introduces SPADE, a novel approach leveraging Extreme Value Theory (EVT) for OOD detection, which provides a statistically grounded method to detect and reject OOD samples effectively.

2. SPADE not only detects OOD samples but also offers provable guarantees for rejecting adversarial examples, making it robust against potential adversarial attacks.

3. The approach is experimentally validated across multiple model architectures, demonstrating its versatility and effectiveness compared to strong baselines, enhancing its relevance for various real-world applications.

### Weaknesses
1. The provable guarantees only hold on **strong** assumptions. In theorem 1, the authors assume the embedding network is $K$-Lipschitz. Firstly, a $K$-Lipschitz network can already provide provable robustness on adversarial examples. Secondly, due to the complexity of the neural network, it is not possible to calculate the exact Lipschitzness empirically. Thus, this theorem offers limited utility for practical OOD detection scenarios.

2. The experimental setup largely follows standard OOD detection settings and does not address the "provable protection of OOD examples," which is claimed as the main contribution of this work. This raises doubts for the reviewer about whether SPADE can indeed provide provable protection for OOD examples, given the limitations outlined in Weakness 1.

3. SPADE performs poorly on near OOD examples, with Table 1 showing that it is outperformed by the MSP baseline in 3 out of 5 cases. Additionally, the average rank is not an ideal metric. To demonstrate the superiority of the proposed method, SPADE should outperform the baselines across a majority of the datasets.

### Questions
See weaknesses

### Soundness
2

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
4

### Summary
This paper studies OOD detection. The authors study OOD in terms of GEV, thus enabling a characterization of the probability/confidence of OOD samples. Based on this framework, they propose a method to detect OOD and adversarial examples.

### Strengths
The method is well-motivated, and the theory is sound. I love the first-principle design. Paper is well-written and easy to follow. The studied problem is important. Introducing GEV to OOD in this way is novel.

### Weaknesses
The main weakness is the weak experimental results. In almost all result tables, the proposed method does not achieve significant benefit over the baselines. In particular, Table 1 shows the proposed method is uniformly dominated by the baseline methods. Table 2 seems to suggest ViT is a particularly strong teacher model for the proposed method, maybe revisiting Table 1 with ViT could bring more benefits.

The authors claim that the proposed methods help to detect adversarial examples. However, the common practice of a defense is to endure adaptive defense, which is aware of the detection and tries to find an adversarial example that surpasses the detection. This highly depends on the claim that the authors would like to make, but overall such experiments would help to establish the significance of the defense.

In summary, while I like the design and the theories, the experimental results do not suggest sufficient improvements, questioning the significance of this work.

### Questions
Could the authors provide more convincing experimental results about the benefit of the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2
