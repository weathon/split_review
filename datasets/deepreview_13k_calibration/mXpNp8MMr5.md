# On the Vulnerability of Adversarially Trained Models Against Two-faced Attacks

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Adversarial robustness is an important standard for measuring the quality of learned models, and adversarial training is an effective strategy for improving the adversarial robustness of models. In this paper, we disclose that adversarially trained models are vulnerable to two-faced attacks, where slight perturbations in input features are crafted to make the model exhibit a false sense of robustness in the verification phase. Such a threat is significantly important as it can mislead our evaluation of the adversarial robustness of models, which could cause unpredictable security issues when deploying substandard models in reality. More seriously, this threat seems to be pervasive and tricky: we find that many types of models suffer from this threat, and models with higher adversarial robustness tend to be more vulnerable. Furthermore, we provide the first attempt to formulate this threat, disclose its relationships with adversarial risk, and try to circumvent it via a simple countermeasure. These findings serve as a crucial reminder for practitioners to exercise caution in the verification phase, urging them to refrain from blindly trusting the exhibited adversarial robustness of models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The vulnerability in machine learning models that this paper reveals is called "two-faced attacks," wherein small input perturbations trick the model during verification and give the impression that it has high adversarial robustness. This observation raises concerns since it may result in security vulnerabilities if models that are not reliable are used based on false robustness evaluations. The phenomena is common and, surprisingly, more prevalent in models that are thought to be quite robust. The authors provide a framework for comprehending this problem and make some initial recommendations for solutions. Rather than accepting adversarial robustness at face value, they advise individuals to evaluate it rigorously.

### Strengths
This study takes a leading role in exposing the vulnerability of adversarially trained models to 'two-faced attacks', which fraudulently overestimate the robustness of the model during the verification stage. 
Notable features include its comprehensive evaluation across a variety of model architectures, datasets, and training techniques, as well as its introduction of the 'two-faced risk' notion to reconcile theory and empirical results. 

Also, the work represents a challenging problem in adversarial defense, as it reveals a counterintuitive trade-off: models that are more resilient to adversarial examples are also more vulnerable to two-faced attacks. 

However, the paper's implications for practice are highlighted by a strong need for rigorous validation processes prior to deployment, particularly in safety-critical domains. This call urges a reevaluation of how adversarial robustness is measured and perceived in the field.

### Weaknesses
Although the study identified two-faced attacks against adversarially trained models in a novel way, it might not provide practitioners with sufficient defenses to address these weaknesses. Though interesting, its theoretical investigation of two-faced risk may prove difficult to implement in real-world scenarios and may not provide enough information about mitigation strategies. 

Additionally, there may be an overemphasis on two-faced attacks, which might mask other important security issues that need to be taken seriously. Furthermore, a lack of clarity in the procedures for experiments may make them difficult to repeat and inhibit future studies. 

Finally, there can be a gap in comprehensive risk management techniques if the paper does not include a comprehensive explanation of how to balance adversarial risks, such as two-faced risk, against other risks.

### Questions
Just two questions:

Is it possible to include the idea of two-faced risk into current adversarial training frameworks without making major changes?

How can long-term model validation procedures be affected by the future evolution of two-faced attacks?


Finally, two suggestions:

Future work should focus on developing more comprehensive defense strategies against two-faced attacks that can be easily implemented in real-world systems.

Perform research on how models might eventually be exposed to fraudulent attacks, especially if adversaries and attack techniques advance in sophistication.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper shows that adversarially trained models are vulnerable to a new threat called two-faced 
attacks, where slight perturbations in input features are crafted to make the model exhibit a false sense 
of robustness in the verification phase. This paper also shows that this threat is pervasive and tricky, 
because many types of models suffer from this threat, and models with higher adversarial robustness 
tend to be more vulnerable. Besides, this paper gives a formal formulation for this threat and discloses 
its relationship with adversarial risk. This paper also proposes a simple countermeasure to circumvent 
the threat. Empirical results have validated the arguments presented in this paper.

### Strengths
1. It is important to disclose the existence of such two-faced attacks in the model verification phase, as 
deploying substandard models (with low adversarial robustness) in reality could cause serious security 
issues.

2. There are some interesting findings that can demonstrate the practical importance of two-faced 
attacks. For example, many types of models suffer from this threat, and models with higher 
adversarial robustness tend to be more vulnerable. 

3. This paper mathematically formulates the two-faced attacks and the two-faced risk, and provide a 
theoretical analysis on its relationship with adversarial risk, and provide a discussion on possible 
countermeasures to circumvent two-faced attacks.

4. Experimental results are supportive.

### Weaknesses
The two-faced attacks are the key of this paper, but the realistic application domains are still unclear. 

From Figure 1(a), this paper gives a machine learning workflow that shows the adversarial robustness 
can be affected by the two-faced attacks in the model verification. However, this paper did not 
provide a real-world example that the two-faced attacks can be applied into and can cause serious 
security issues. This point can further strengthen the significance of the two-faced attacks.

### Questions
Can the authors provide a real-world example that the two-faced attacks can be applied into?

Can the authors provide more potential countermeasures against two-faced attacks, apart from the 
ones mentioned in Section 3.3?

Other problems please see **Weaknesses.**

Overall, I like the idea and analysis in this paper.  I expect the problems could be clarified and addressed in the rebuttal.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work described the problem of hypocritical examples which added tiny perturbations to clean test inputs to increase the targeted model's performance. These samples can mislead machine learning practitioners into assuming that their machine learning models are good enough to be applied in the real world. The authors also mentioned that these samples can be crafted from adversarial examples to provide a false sense of adversarial robustness. They called this two-faced attack and provided its problem formulation and algorithm to create such an attack. They proposed a countermeasure by increasing the perturbation bound of adversarial training to get the best tradeoff between adversarial risk and two-faced risk. After that, they showed a bunch of experiment with several datasets.

### Strengths
- The paper has a strong formulation and background of hypocritical examples on adversarial examples.
- The experiment covers several kinds of datasets.
- The literature review is good and updated.
- The paper is well-organized and easy to follow.

### Weaknesses
 - The background and motivation are not convincing to me. The authors may make it more motivating, and probably, look at the previous work (Tao, 2022b) since it is very convincing.
- The experiments for the countermeasure (enlarging the budget) are limited. The authors may need to add more experiments for it.
- The contribution of this paper is limited because the content is very similar to the previous work (Tao, 2022b), but changes from clean test samples to adversarial test samples. The authors may focus more on the countermeasure.

### Questions
- In Appendix A, I do know how you derive from E[1(f(x'') = y) * 1(f(x_{adv} \neq y)] to E[1(f_{adv} \neq y)] * E[1(f(x'') = y)]. It is in the lines 7 and 8 if you count the line R_{rhpy}(f,D) as line 1.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
