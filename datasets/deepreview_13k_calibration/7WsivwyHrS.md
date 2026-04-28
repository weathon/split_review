# You Only Query Once: An Efficient Label-Only Membership Inference Attack

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
As one of the privacy threats to machine learning models, the membership inference attack (MIA) tries to infer whether a given sample is in the original training set of a victim model by analyzing its outputs. Recent studies only use the predicted hard labels to achieve impressive membership inference accuracy. However, such label-only MIA approach requires very high query budgets to evaluate the distance of the target sample from the victim model's decision boundary.  
   We propose YOQO, a novel label-only attack to overcome the above limitation.YOQO aims at identifying a special area (called improvement area) around the target sample and crafting a query sample, whose hard label from the victim model can reliably reflect the target sample's membership. YOQO can successfully reduce the query budget from more than 1,000 times to only ONCE. Experiments demonstrate that YOQO is not only as effective as SOTA attack methods, but also performs comparably or even more robustly against many sophisticated defenses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes YOQO a label-only MIA which, unlike prior SOTA label-only MIAs, queries the target model only once using a specific sample x’ derived from the target sample (x, l) with the goal of determining the membership of (x, l). YOQO finds the query sample x’ in the improvement region which is the difference in the decision boundaries due to insertion of (x, l) in the training data. YOQO proposes an optimization to find x’ that maximizes the error of OUT models on x’ and minimize the error of IN models on x’, and solves it using gradient decent. Evaluations show that YOQO is as effective or better than the existing label only MIAs on multiple datasets/model architectures.

### Strengths
- YOQO is a novel idea that reduces query budget required for MI
- Idea is well explained and paper is easy to read.
- Experiments are well designed to demonstrate the efficacy of the attack

### Weaknesses
 - YOQO evaluations consider very small datasets and training data sizes
- Models might be overfitted on training data
- Unclear how this attack will work in practical settings

### Questions
This paper proposes a very novel YOQO attack and I think the paper also does a good job of explaining and evaluating the attack. The evaluations clearly show that YOQO is the new SOTA label only MIA. I have the following few concerns about the paper:

- Although the experimental setup considered is the common setup in most prior works, it contains mostly small datasets with very small training dataset sizes. Can authors perform experiments on larger datasets, e.g., Imagenet? 
- I could not figure out the training recipe from the main paper. In particular does the training ensure that the models don’t overfit to the training data, e.g., using L2 regularization or any other common regularization techniques? I feel the criterion that training goes on until a model has >98% accuracy on training data may lead to overfitting that will lead to unnecessarily stronger MIAs.
- On the same lines as the above comment, can authors add a few more details of various dataset sizes used in training with/without defenses, e.g., adversarial regularization? Also can they add details of training procedure? These are important given that MIA efficacy is greatly affected by these factors.
- Utility of the attack: I could not understand from the current evaluations how the attack will perform in the real world. The dataset sizes are quite small which is seldom the case now a days, unless if model is fine-tuned using a small dataset. Can authors provide results for some real-world settings? Some suggestions: 1) use larger datasets 2) fine-tune a model pre-trained on large datasets?

### Soundness
2 fair

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
The paper introduces YOQO, a novel label-only membership inference attack designed to address privacy threats in machine learning models. YOQO's key innovation lies in its identification of an "improvement area" around a target sample, enabling the crafting of query samples with hard labels that effectively determine the target sample's membership, significantly reducing the query budget required from over 1,000 queries to just one query. The study demonstrates that YOQO exhibits effectiveness comparable to state-of-the-art Membership Inference Attacks (MIA) while demonstrating greater resilience against various defense mechanisms. This underscores its significance in the context of privacy attacks on machine learning models.

### Strengths
- YOQO introduces a label-only membership inference attack, reducing the query budget from over 1,000 queries to just one query.
- The attack demonstrates effectiveness on par with state-of-the-art MIA methods, indicating its practical relevance.
- YOQO exhibits greater robustness against various defense mechanisms, underlining its potential for real-world applications.

### Weaknesses
 - The use of accuracy as the primary evaluation metric is questioned, as it may not reflect worst-case performance in MIA.
- The potential for overfitting in the experimental setting due to a small training dataset (2,500 samples) raises concerns about the generalizability of the results.
- While the transformation of Equation 1 into a minimization problem is justified, the exploration of alternative techniques, such as introducing a weight term, could enhance the paper's depth and robustness.

### Questions
Two noteworthy concerns arise in the evaluation of the paper.

First, in terms of the chosen evaluation metric, the authors have opted for accuracy to assess the performance of their attack. However, there are concerns about the appropriateness of this choice. While I agree that using a log-scale ROC curve may not be practical for this case, the fundamental issue at hand pertains to the need for evaluating the worst-case scenario for MIA. Based on my understanding, samples closer to the decision boundary should have a higher probability of being classified as members, while those significantly distant from this boundary may exhibit a lower likelihood of membership. Consequently, assessing accuracy across all samples may not effectively unveil the worst-case performance. To address this, a suggestion is made to focus on accuracy calculations for samples located farthest from the decision boundary, even though the attacker may lack knowledge of the specific location of such samples. The presence of ground truth information during the evaluation phase supports the feasibility of this approach.

Second, the experimental setting raises concerns regarding overfitting. The target model is trained with a relatively small dataset of 2,500 samples, which could potentially result in severe overfitting. Although the paper does not explicitly state the training and testing accuracy gap for the target model, it can be inferred from the GAP attack that the overfitting level exceeds 40%, potentially impacting the reliability of the conclusions. I would like to see the authors conduct experiments on well-generalized models, involving a larger training dataset to mitigate the risk of overfitting.

In Section 3.2, when the authors optimize the x to get the improvement area, they believe that Equation 3 won’t work since scalars in both in models and out models are in [0,1]. I agree, and to address this constraint, the authors adapt Equation 1 into a minimization problem, which is a common practice in finding adversarial examples. Just out of curiosity, I wonder whether adding a weight term $\lambda$ to Equation 2 could achieve the same result, that is, turn the output of in models to [0,$\lambda$].

### Soundness
3 good

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
In this paper, the authors propose a novel label-only membership inference attack named YOQO. Before querying the target model, the attacker first perturbs the target image in such a way that it produces differing predictions between shadow models trained with and without the target image. Subsequently, the attacker queries the target model with the perturbed image and examines the predicted label. Remarkably, YOQO can achieve state-of-the-art performance with just a single query.

### Strengths
- The paper is well-written, making it easy to follow.
- The results are promising. The method requires only one query yet achieves results comparable to state-of-the-art methods.
- The extensive ablation studies presented in the paper are commendable, particularly the experiments under multiple defenses.
- The offline attack demonstrates impressive performance without necessitating the retraining of any shadow models, which is advantageous for practical applications.

### Weaknesses
While I'm impressed with the paper, a primary concern is the apparent similarity between the proposed method and the method in [1] from ICLR 2023. The latter utilizes a similar loss to craft queries, enhancing membership inference attacks. Their emphasis is on the threat model that extracts logits from the target model. However, [1] is absent from the paper's references.

### Questions
- As mentioned in the weaknesses section, what would be the main difference between the proposed method and the approach outlined in [1]?
- It's encouraging that the crafted query is transferable. However, if the training algorithm of the target model differs from that of the shadow model, such as having different learning rates or optimizers, would the attack still retain its potency?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
