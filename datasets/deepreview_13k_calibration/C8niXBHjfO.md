# Does Training with Synthetic Data Truly Protect Privacy?

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
As synthetic data becomes increasingly popular in machine learning tasks, numerous methods—without formal differential privacy guarantees—use synthetic data for training. These methods often claim, either explicitly or implicitly, to protect the privacy of the original training data.
In this work, we explore four different training paradigms—coreset selection, dataset distillation, data-free knowledge distillation, and synthetic data generated from diffusion models. While all these methods utilize synthetic data for training, they lead to vastly different conclusions regarding privacy preservation. This highlights that empirical approaches to preserving data privacy require careful and rigorous evaluation; otherwise, they risk providing a false sense of privacy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the privacy-preserving properties of commonly-used synthetic image generation methods. The measuring of privacy-preservation is carried out using membership inference attacks using the attacks given by [Aerni et al. (2024)](https://arxiv.org/pdf/2404.17399). The paper compares the privacy-preservation of four commonly-used techniques: coreset selection, dataset distillation, data-free knowledge, model distillation, and synthetic data generated from diffusion models. The experiments are carried out on CIFAR-10 and the most vulnerable samples are mislabeled samples.

### Strengths
- The paper is very well written and the experiments are well-explained and seem solid.

- The paper can serve as a good reference for showing the strength of DP-SGD for obtaining good privacy-utility trad-eoff for synthetic image data.

### Weaknesses
 - The paper does not truly present many novel ideas, though it is another valuable demonstration about the effectiveness of DP-SGD for obtaining good privacy-utility tradeoff for ML models when the privacy protection is measured via the most vulnerable samples.

Regarding the idea of auditing with worst-case samples, for example: it has been studied extensively and is already considered by Carlini et al, 2019, "The secret sharer: Evaluating and testing unintended memorization in neural networks" and Jagielski et al., 2020, "Auditing differentially private machine learning: How private is private sgd?" So, although auditing with worst-case samples seems to be a central theme in the paper, there is not much novelty in there (and I also think these references should be included).

Also, the vulnerability of synthetic data against membership inference attacks has been considered in the literature, and there also seem to be some central references missing: see e.g. the work by Hayes et al., 2019, "LOGAN: Membership Inference Attacks Against Generative Models." and Van Breugel et al., 2023, "Membership Inference Attacks on Synthetic Data: A Comprehensive Evaluation".

- The experimental comparison is a bit restricted, after all, since only the CIFAR-10 dataset is considered. Perhaps one could consider datasets from other domains as well?

### Questions
- Do you think similar comparisons could be easily carried out in different image datasets or in other domains (e.g., tabular data) ? 

- What is the setting behind Figure 4? There are no details given on that experiment.

- When focussing on practical scenarios: do you think the situation would differ, if instead of using synthetic samples (e.g., mislabeled samples) for the auditing, you would try to find the most vulnerable data samples in the dataset? 

- Before the experimental setup is presented on page 6, there are some experimental results presented on page 5 (Figures 3 and 4) for which no sufficient details are given. I cannot be sure for which dataset is the result of Figure 4 is, and what is exactly the setting behind that figure.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper measures empirical privacy for several methods of training vision models from synthetic data that claim to preserve privacy to some degree with respect to the training data: CoreSet selection, Dataset Distillation, Date-Free Knowledge Distillation, and synthetic data from Fine-Tuned Diffusion models. Empirical privacy is evaluated using the Likelihood Ratio Attack (LiRA) and the general setup follows [0]. As a private baseline, DP-SGD is used.

For the evaluation, a ResNet architecture is used with the CIFAR-10 dataset. For each of these methods, the authors measure privacy leakage (true positive rate given a fixed false positive rate), utility (test set accuracy), and efficiency (# of training hours). The main findings are that there's a clear privacy-utility tradeoff among methods once privacy is considered as a worst-case rather than an average case notion and that none of the synthetic data methods outperform DP-SGD with the three metrics jointly considered.

### Strengths
- This paper provides an apples-to-apples empirical privacy comparison for several methods of training vision models that claim to preserve privacy to some degree. In doing so, it improves upon prior empirical privacy analyses, some that were rather flawed.
- The presentation is clear and the text is well-written. The figures throughout are particularly helpful. See question 1 on this point.

### Weaknesses
 - The DP-SGD comparison is potentially misleading. The "baseline" method does not satisfy differential privacy. See question 2. The paper would benefit from including an additional baseline that satisfies DP e.g. [4] discusses how to incorporate hyperparameter tuning into the privacy analysis. It may also be interesting to include a fully non-private baseline using a standard training routine i.e. just train ResNet with SGD. 
- The paper would benefit from a discussion of how the formal guarantee of differential privacy differs from heuristic privacy - particularly, with respect to DP applying to adding or removing any possible record within the data domain; whereas, the MI attacks in this paper are only considered with respect to the training data.



### Questions
1. Why are the gridlines in Figure 1 not uniform? Consider changing this or explaining in figure caption.
2. As with [0], are the DP-SGD models reported in Table 4 only non-private due to hyperparameter tuning? If so, what privacy parameters were these models trained with?

Additional stylistic notes:
- Odd phrasing on Line 83: "none of these fancy methods with synthetic data"

- Typo on Line 95: "it can provide a decent privacy protection"

- Odd phrasing Line 244: "but not evaluated in the right way"

Additional suggestions:
- When discussing the intuition for why initialization on public data provides privacy guarantees, consider referencing [1, 2, 3], which illustrate how public data can be used to improve differentially private synthetic data. 

[0] Aerni, Michael et al. "Evaluations of Machine Learning Privacy Defenses are Misleading." 2024.

[1] Liu, Terrance, et al. "Leveraging public data for practical private query release." International Conference on Machine Learning. PMLR, 2021.

[2] Liu, Terrance, et al. "Iterative methods for private synthetic data: Unifying framework and new methods." Advances in Neural Information Processing Systems 34 (2021): 690-702.

[3] Fuentes, Miguel, et al. "Joint Selection: Adaptively Incorporating Public Information for Private Synthetic Data." International Conference on Artificial Intelligence and Statistics. PMLR, 2024.

[4] Papernot, Nicolas, and Thomas Steinke. "Hyperparameter tuning with renyi differential privacy." ICLR, 2022.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates whether using synthetic data in machine learning genuinely safeguards privacy, as often claimed. The evaluations is done on 4 different training paradigms-coreset selection, data distillation, data-free knowledge distillation and synthetic data generated from diffusion models. To test the privacy claims of these methods, the study uses membership inference attacks (MIAs), focusing on worst-case scenarios to rigorously assess privacy leakage. The paper also compares these methods to Differential Privacy Stochastic Gradient Descent (DPSGD), a technique known for providing formal privacy guarantees, and finds that DPSGD consistently outperforms synthetic data-based approaches in terms of the privacy-utility-efficiency balance. The findings reveal that none of the synthetic data techniques match DPSGD in safeguarding privacy effectively. Notably, the study also discovers that visual dissimilarity between synthetic and private data does not necessarily imply privacy protection, as even visually distinct synthetic data can leak information when model logits are similar. This highlights a risk that methods relying solely on visual or distributional differences may offer a false sense of privacy.

### Strengths
This broad approach offers a thorough understanding of various methodologies in synthetic data utilization and their impact on privacy.
The study juxtaposes synthetic data-based techniques with Differential Privacy-SGD (DPSGD) as a baseline, which helps readers contextualize the efficacy of synthetic data methods in privacy preservation compared to a gold-standard approach like DPSGD.
The study identifies instances where synthetic data, despite visual dissimilarity from private data, can still leak privacy information through logit similarities. This nuanced finding enhances the paper's depth by showing that visual similarity alone isn’t sufficient to evaluate privacy.

### Weaknesses
The experiments focus on CIFAR-10 and specific models, such as ResNet-18, which may limit the generalizability of findings. The paper’s findings could vary across more complex datasets or architectures, and broader experiments could better represent the implications for privacy in diverse real-world scenarios​. Specifically, the use of only CIFAR-10, a relatively small and well-studied dataset, does not fully capture the complexities of real-world data distributions, which often exhibit higher dimensionality and more intricate patterns. This limitation makes it difficult to assess how these synthetic data methods would perform in scenarios with more complex data, such as medical imaging or high-resolution natural images. Furthermore, the choice of ResNet-18, while a common architecture, does not account for the potential impact of different model architectures, such as transformers or larger convolutional networks, on privacy leakage. The paper should acknowledge that the observed privacy vulnerabilities might be amplified or mitigated in different model settings.

Techniques like DPSGD are noted for efficiency, yet they are resource-intensive. The paper briefly mentions but does not deeply engage with the practical constraints of computational cost and scalability, which are critical factors for real-world implementation of privacy-preserving methods​. The discussion should include a more detailed analysis of the computational overhead associated with DPSGD, particularly in terms of training time and memory requirements. The paper should also consider the scalability of DPSGD to larger datasets and models, as the computational cost can become prohibitive in such scenarios. A more thorough discussion of these practical limitations is necessary to provide a balanced perspective on the real-world applicability of DPSGD.

While the empirical evaluation is thorough, the paper lacks an in-depth theoretical framework to explain why certain synthetic data techniques lead to privacy leakage. A theoretical grounding could bolster the empirical findings and offer predictive insights for synthetic data privacy. The paper should explore the theoretical underpinnings of the observed privacy vulnerabilities, possibly by analyzing the information-theoretic properties of the synthetic data generation process or the model training dynamics. This theoretical analysis could help in identifying the key factors that contribute to privacy leakage and provide a more principled approach to designing privacy-preserving synthetic data methods. Without a theoretical framework, the empirical findings remain somewhat isolated and lack a deeper explanation of the underlying mechanisms.

### Questions
Why do you consider coreset selection as synthetic data?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a systematic analysis for privacy risk of the usage of synthetic data. The investigated methods include core set selection, dataset distillation, data-free distillation and diffusion models. The estimated privacy leakage is based on 500 canaries that are mislabeled and LiRA by shadow models. The results show that the privacy risk still remains and higher than DP-SGD at the same comparison of utility. This work also provides several detail analysis including the logits similarity.

### Strengths
- This work presents a systematic evaluation of privacy metrics TPR-FPR by LiRA for four synthetic data generation methods, and show that privacy leakage of synthetic data is much higher in than the results in previous literature.
- This work also provide some detailed analysis including considering visually similarity and logits similarity together instead of relying on the single MIA metric.

### Weaknesses
 - The analysis could be improved (see questions below).
- The technical contribution is somewhat limited. For example, the privacy estimation metric is based on previous work LiRA.
- It is not clear how the logit similarity of the synthetic data in DFKD leads to the higher MIA metric of private data. Figure 9 shows that the logit of the private data in student model prediction is much different than the remaining three, therefore it is unclear why this logits similarity of the synthetic data could lead to the higher MIA metric.
- The dataset distillation method (random/OOD) shows utility drop compared to DP-SGD. It is unclear if increasing the number of synthetic data would help improve utility.
- It seems to me the TPR value granularity for 500 canaries is 0.2% (1/500) and I wonder how is the TPR reported in Tables are calculated. Or in other words, the authors may provide a detailed description about how MIA metric is calculated.
- It is unclear if an adaptive attack could achieve higher attacker performance based on Figure 7 findings where the LiRA achieves a lower MIA metric.

### Questions
1. It is interesting to see the analysis for visual similarity and logit similarity. I did not quite follow the analysis for why the logit similarity of the synthetic data in DFKD leads to the higher MIA metric of private data. Figure 9 shows that the logit of the private data in student model prediction is much different than the remaining three, therefore I wonder if the authors could explain why this logits similarity of the synthetic data could lead to the higher MIA metric.

2. Figure 7 shows that private data that has high confidence in original label and Figure 9 shows the private data that has higher confidence in the mislabel label. Would this show the different canary property for different kind of methods.

3. The dataset distillation method (random/OOD) shows utility drop compared to DP-SGD. Would increasing the number of synthetic data help improve utility?

4. It seems to me the TPR value granularity for 500 canaries is 0.2% (1/500) and I wonder how is the TPR reported in Tables are calculated. Or in other words, the authors may provide a detailed description about how MIA metric is calculated.

5. I wonder if the author could provide an adaptive attack that achieves higher attacker performance based on Figure 7 findings where the LiRA achieves a lower MIA metric. 

I am happy to increase my score if I find my concerns addressed.

### Soundness
3

### Presentation
2

### Contribution
3
