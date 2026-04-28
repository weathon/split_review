# Informed Exploration via Generative Modeling

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Conventionally trained neural networks excel at prediction but often struggle to model uncertainty in their own predictions. We explore this challenge in a meta-learning bandit decision-making problem for news recommendations; this setting require decision-making algorithms to incorporate pretrained language models to process text data for the best performance. We present a scalable approach to Bayesian uncertainty quantification by posing it as a problem of autoregressive generative modeling of future rewards. First, we use historical data on previously released news articles to pre-train a generative model to predict sequences of future potential rewards. At inference time, our algorithm makes decisions based on limited previous rewards and autoregressively generated future rewards. Far from a heuristic, we synthesize insights from the literature to show our method is a novel implementation of Thompson (posterior) sampling, a prominent bandit algorithm. We prove our pretraining loss directly controls online decision-making performance, and we demonstrate our framework on a news recommendation task where we integrate end-to-end fine-tuning of a pretrained language model to process news article headline text to improve performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores uncertainty in neural networks for decision-making, focusing on a meta-learning bandit setup applied to news recommendation. It introduces a novel approach using autoregressive generative modeling to quantify Bayesian uncertainty by predicting future rewards based on historical data. This method involves pre-training a generative model to forecast potential rewards, which helps balance exploration and exploitation without directly modeling latent variables. The approach is demonstrated through theoretical bounds and experiments, showing it enhances decision-making accuracy by effectively integrating neural networks.

### Strengths
* The paper presents a new method for Bayesian uncertainty quantification through autoregressive generative modeling, which provides a scalable and effective alternative to traditional methods that rely on complex posterior approximations.

* By applying this method to a news recommendation task, the paper demonstrates the approach's potential to improve real-world decision-making where uncertainty and user interactions play a crucial role.

* The paper provides a formal regret bound, showing that the approach’s decision-making performance directly relates to the sequence model’s training loss, solidifying the theoretical basis for the proposed method.

### Weaknesses
 * A major concern is that this paper lacks a thorough discussion of related work, despite several highly relevant and overlapping studies. There is existing research that uses generative modeling for posterior approximations[1] and in recommendation tasks[2]. Additionally, multiple works have explored connections between autoregressive generative modeling and approximate Bayesian inference[3,4]. Furthermore, meta-learning with autoregressive generative networks has been studied in contexts such as classification[5], Bayesian Optimization (BO)[6], and decision-making in sequential prediction[7].


1. Gal, Yarin, and Zoubin Ghahramani. "Dropout as a bayesian approximation: Representing model uncertainty in deep learning." international conference on machine learning. PMLR, 2016.
2. Da Tsai, Yun, and Shou De Lin. "Fast online inference for nonlinear contextual bandit based on generative adversarial network." arXiv preprint arXiv:2202.08867 (2022).
3. Hollmann, Noah, et al. "Tabpfn: A transformer that solves small tabular classification problems in a second." arXiv preprint arXiv:2207.01848 (2022).
4. Müller, Samuel, et al. "Transformers Can Do Bayesian Inference." International Conference on Learning Representations.
5. Bonet, David, et al. "HyperFast: Instant Classification for Tabular Data." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 10. 2024.
6. Müller, Samuel, et al. "Pfns4bo: In-context learning for bayesian optimization." International Conference on Machine Learning. PMLR, 2023.
7. Lee, Jonathan, et al. "Supervised pretraining can learn in-context reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).

### Questions
* Could the authors clarify the differences between their approach and existing works, highlighting the novelty and contribution of this work?
* Could the authors clarify if the proposed methods are used to address the delayed feedback issue (missing outcomes) rather than used for building a recommendation policy?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to address the challenge of modeling uncertainty in decision-making in news recommendation systems. The authors propose a method that leverages autoregressive generative models to predict the missing or future rewards based on the historical, and then use the Thompson sampling for final decision-making with the previous and generated rewards. This paper proposes several theory analyses of the advantages of using sequential models (like transformers). The authors demonstrate their approach through both synthetic and semi-realistic news recommendation experiments, showing that their method can effectively incorporate pretrained language models and achieve strong performance in terms of regret minimization and uncertainty quantification.

### Strengths
1) The idea of incorporating sequential models into decision-making makes sense to me. Pre-trained on previous data, the autoregressive model has the ability to predict the missing reward values, which is benefit for the downstream algorithm.

2) The authors provide several theory analyses to support the efficiency of the proposed modules.

3) Experiments on both synthetic and real-world settings show the improvements of the proposed model.

### Weaknesses
1) One of the main concerns comes from the experiments. The authors only test their models with the base models (such as PS Neural Linear, PS Beta-Bernoulli), which may reduce the convincingness of the proposed method. It would be more compelling to see comparisons against state-of-the-art contextual bandit algorithms that also incorporate neural networks and uncertainty quantification, such as those using variational inference or other Bayesian deep learning techniques. The current baselines, while reasonable starting points, do not fully demonstrate the advantage of the proposed method over more advanced approaches.

2) The authors claim that they use the language foundation model to improve the uncertainty quantification, which is not precise. Because they only pre-trained sequential models on historical data, the trained models are not actually foundation models. The use of a pre-trained language model provides a strong representation, but the fine-tuning process for reward prediction does not inherently guarantee improved uncertainty quantification. The uncertainty estimates are derived from the sequence model's predictions, not directly from the language model's inherent uncertainty. This distinction needs to be clarified.

3) The Thompson sampling at the inference stage relies heavily upon the generated missing reward values, which may limit its application when sequence models cannot precisely predict missing rewards. If the sequence model's predictions are inaccurate or biased, the Thompson sampling will propagate these errors, potentially leading to suboptimal decision-making. The paper should include a more detailed analysis of the sensitivity of the method to the accuracy of the sequence model's predictions, and discuss strategies to mitigate the impact of inaccurate predictions.

### Questions
Please see the above Weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies exploration under general neural networks. They propose the method kind of like "generative Thompson Sampling", which does not explicitly model the unknown latent variables, but aims at modeling the missing rewards. The procedure of the algorithm starts with implicitly learns the Bayesian model via pre-training by minimizing a sequence prediction loss on successive reward using historical data, then at inference time, it uses the both the observed and imputed reward to make decisions. This basically reduces 
 the sequential decision-making problem to a sequence prediction training with low loss. Experiments are done on synthetic and news recommendation dataset.

### Strengths
- This paper tackles the important issue of exploration in general neural networks, a challenge with broad implications for real-world applications like recommendation systems, education, and even LLM generation. Informed exploration are critical for these complex decision-making systems.
- The authors effectively bridge the gap between sequence modeling and Bayesian inference, introducing the concept of "generative Thompson sampling". This provides a strong theoretical justification for their approach and nicely clarifies the role of pre-training as a form of empirical Bayes.
- The proposed method is easy to implement, and the experimental results on recommendation tasks demonstrate the effectiveness of the proposed approach, in terms of both reducing regret and providing valid confidence intervals.

### Weaknesses
 - Lack of Clarity and Potential Inconsistencies: The paper would benefit from increased clarity in its methodological details and problem formulation. Specifically:

1.  While the motivating example of news recommendation emphasizes no overlap in the action set across time steps, this constraint seems not to be the case  in the formal problem definition and Algorithm 1. The paper states that articles are drawn IID, but this does not preclude overlap between historical and evaluation sets, which is a critical distinction that needs to be clarified. The algorithm's behavior when encountering previously seen actions during the online phase is not explicitly addressed, which is a significant concern for practical application.
2. The role of different users in Equation 2 and Algorithm 1 remains unclear. It appears to estimate a population-level mean reward for each action, over all users. This then seems a multi-arm bandit problem than the contextual bandit one? The authors should explicitly state whether they are addressing a multi-arm bandit or a contextual bandit problem and revise the relevant sections accordingly. It is hard to estimate the context-dependent reward based on the current alg. The current formulation appears to learn a single average reward for each action, which is insufficient for personalized recommendations and does not align with the stated goal of contextual decision-making. The lack of user-specific modeling is a major limitation.

- Computational Cost: The proposed method's computational complexity scales linearly with both the action set size and the "overlap" between new and historical actions, and time-step T. This could become prohibitive in applications with large action spaces or significant small overlap, even disjoint support. The authors should discuss more on the scaling of the method. The linear scaling with the action set size is a major bottleneck, especially in scenarios with large action spaces, which are common in recommendation systems. The paper needs to provide a more detailed analysis of the computational cost, including memory usage and runtime, and discuss potential strategies to mitigate these issues.

- Limited Novelty: The proposed approach is very similar to reward models [1] employed in the offline bandit and RL literature. While subtle differences may exist, the authors need to provide a more thorough comparison with existing reward modeling techniques, explicitly highlighting their novel contributions here.

Ref: https://arxiv.org/pdf/1103.4601

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
3
