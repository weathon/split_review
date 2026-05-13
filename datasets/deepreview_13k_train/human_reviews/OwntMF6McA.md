# Weak-to-Strong Trustworthiness: Eliciting Trustworthiness with Weak Supervision

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
The rapid proliferation of generative AI, especially large language models (LLMs), has led to their integration into a variety of applications. 
A key phenomenon known as weak-to-strong generalization - where a strong model trained on a weak model's outputs surpasses the weak model in task performance - has gained significant attention.  Yet, whether critical trustworthiness properties such as robustness, fairness, and privacy can generalize similarly remains an open question. In this work, we study this question by examining if a stronger model can inherit trustworthiness properties when fine-tuned on a weaker model’s outputs, a process we term weak-to-strong trustworthiness generalization. Specifically, we examine whether a strong model can inherit or even enhance trustworthiness attributes when fine-tuned on a weak model's outputs. To address this, we introduce two foundational training strategies: 1) Weak Trustworthiness Finetuning (Weak TFT), which leverages trustworthiness regularization during the fine-tuning of the weak model, and 2) Weak and Weak-to-Strong Trustworthiness Finetuning (Weak+WTS TFT), which extends regularization to both weak and strong models. Our experimental evaluation on real-world datasets (Adult, OOD Style Transfer, AdvGLUE++, and Enron Emails) reveals that while some trustworthiness properties, such as fairness, adversarial, and OOD robustness, show significant improvement in transfer when both models were regularized, others like privacy do not exhibit signs of weak-to-strong trustworthiness. As the first study to explore trustworthiness generalization via weak-to-strong generalization, our work provides valuable insights into the potential and limitations of this method. Our findings highlight the importance of systematically studying trustworthiness transfer to develop AI systems that are not only accurate but also ethically aligned and reliable in critical applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper the authors studied the abiilty for a weak model to teach a more powerful model to be fair, robust (both OOD and adversarial), and privacy sensitive.  The paper explores two appraoches: (1) traditional weak-to-strong generalization after training the weak model to have good trustworthiness and (2) additional trustworthiness regularization of the strong model. They find that traditional weak-to-strong generalization does not hold but that their second method works better.

### Strengths
* While weak-to-strong generalization has been studied as a general property, it has not been sufficiently examined for safety and trustworthiness properties.

* The paper is fairly clear and thorough in its experiments, making it relatively easy to interpret.

### Weaknesses
1. The size of the strong models included in the paper is small. How about the results on the models around 7B?

2. Lack of generazation towards fairness.
	In this paper, the authors adopt the Demographic Parity as the representative definition. In fairness research domain, there are a series of fairness definition, such as Equal False Positive/Negative Rates, Calibration/Predictive Parity, etc. How the proposed method work with different fairness definition.


3. Lack the in-depth discussion about why privacy do not exhibit signs of weak-to-strong trustworthiness.


Minor: 

1. Formatting issue: The subfigures in Figure 3 have varying sizes.

### Questions
* Am i understanding correctly that in Weak+WTS TFT the strong model gets trustworthiness regularization + the normal weak-to-strong loss?  does the trustworthiness regularizer make use of the weak model?
* How is the Enron data used?
* Is all fine-tuning only on the trustworhtiness datasets? What is the vanilla form of each task that doesn't apply the trustworthiness loss?
* Is it a reasonable assumption that we have these curated datasets? It would seem that even having some of the datasets makes the WTS problem secondary (eg once I know demographic attributes and have decided on demogrpahic parity, or differential privacy)

nits:
* "modelss" (extra s)

### Soundness
3

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
2

### Summary
In this paper, the authors explore the challenge of whether the fairness, robustness, and privacy can be transferred from weak to strong models through weak-to-strong generation. This is an important research topic, because the ability to transfer trustworthiness properties is crucial for preventing harmful outcomes, complying with regulations, and maintaining public trust in AI technologies. In this paper, the authors propose two novel approaches to enhance the transfer of trustworthiness properties between weak and strong models.

### Strengths
1. The authors propose two novel methods (Weak TFT and Weak+WTS TFT) to enhance trustworthiness transfer.

2. The paper is well organized and easy to follow. 

3. The authors provide a comprehensive study about the related works.

4. The authors propose three-phase experimental design provides a thorough analysis of trustworthiness transfer.

### Weaknesses
This paper is an empirical evaluation extending a previously known result (weak-to-strong generalization) to a new set of capabilities, ie trustworthiness. Since there is no new methodology, I was hoping to see a stronger experimental section, containing a wider variety of models and datasets, ie >1 per task. I don't think the paper has any deep technical issues. In my opinion it's incomplete due to a few things, like only evaluating one definition of fairness/privacy/ood,. and using one dataset per setting. I understand using more models would be hard, due to accessibility, but if possible this would also improve the empirical evaluation.

### Questions
See weakness 1, 2, 3

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
This work investigates this critical studies the transfer of trustworthiness properties from weak to strong models. This is an empirical work showing how some trustworthiness properties, such as fairness, adversarial, and OOD robustness, show significant improvement in transfer when both models were regularized towards trustworthiness, others like privacy do not exhibit signs of weak-to-strong trustworthiness.

### Strengths
Overall, the problem is important and well-motivated, the paper is well-written, and the experimental section had an interesting conclusion, matching the claims in abstract in intro.

### Weaknesses
 - The motivation of the weak-to-strong transfer in this work is questionable. It can be meaningful to study this problem in some special cases, such as when the labeled dataset is small while there exists a large unlabeled dataset. If the strong model is only trained with the small labeled data, it can suffer from underfitting, thus making it more meaningful to train the weak model first and train the strong model with weak labels generated by the weak model. However, this work does not consider such cases.
- This work is benchmarking three different ways to fine-tune the strong model, there is not much technical novelty.
- The paper does not adequately explore scenarios where multiple weak models could contribute to a more robust strong model. The current setup, focusing on a single weak model, limits the potential for knowledge aggregation and may not fully leverage the benefits of a weak-to-strong transfer approach. The use case where multiple weak models, each trained on different data subsets or with different regularization, could provide a more diverse and robust training signal for the strong model is not considered.
- There is a mismatch between the motivation presented in the rebuttal, which highlights cross-institutional collaboration and multiple hospitals contributing to a strong model, and the actual experimental setup in the paper, which only involves a single weak model. This discrepancy undermines the practical relevance of the study.
- The paper does not address why the strong model cannot be trained directly on the original data. There is no discussion of regulatory or practical constraints that would necessitate the use of a weak model as an intermediary, which is a critical justification for the proposed approach.

### Questions
- Can you expand on the experimental setting? E.g. hyperparam search. This should be contained at least in the appendix.
- How do you connect the rate of improvement of trustworthiness capabilities with the previous results in weak-to-strong generalization?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper conducts an empirical study of weak-to-strong generalization for trustworthiness (fairness, OOD generalization, adversarial robustness and privacy). They compared three ways to perform weak-to-strong generalization, where the difference is whether the trustworthiness regularization is added to the loss of the weak/strong models. Experiments show the Weak+WTS TFT approach is the most effective way of transferring trustworthiness.

### Strengths
- This work considers 4 different aspects of trustworthiness.
- It performs a relatively comprehensive study of parameter sensitivity.

### Weaknesses
- The motivation of the weak-to-strong transfer in this work is questionable. It can be meaningful to study this problem in some special cases, such as when the labeled dataset is small while there exists a large unlabeled dataset. If the strong model is only trained with the small labeled data, it can suffer from underfitting, thus making it more meaningful to train the weak model first and train the strong model with weak labels generated by the weak model. However, this work does not consider such cases.
- This work is benchmarking three different ways to fine-tune the strong model, there is not much technical novelty.

### Questions
1. In figure 2 (d), why does the Weak+WTS TFT perform better than the strong ceiling?

### Soundness
2

### Presentation
2

### Contribution
1
