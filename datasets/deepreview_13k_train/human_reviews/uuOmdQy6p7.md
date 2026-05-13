# Few-shot Text Adversarial  Attack for Black-box Multi-task  Learning

- Decision: Reject
- Scores: 1, 5, 6, 5

## Abstract
Current multi-task adversarial text attacks rely on white-box access to shared in-
ternal features and assume a homogeneous multi-task learning framework. As a
result, these attacks are less effective against practical scenarios involving black-
box feedback APIs and heterogeneous multi-task learning. To bridge this gap,
we introduce Cluster and Ensemble Mutil-task Text Adversarial Attack (CEMA),
an effective black-box attack that exploits the transferability of adversarial texts.
Specifically, we initially employ cluster-oriented substitute model training, as a
plug-and-play framework, to simplify complex multi-task scenarios into more
manageable text classification attacks and train the substitute model. Next, we
generate multiple adversarial candidate examples by applying various adversarial
text classification methods. Finally, we select the adversarial example that attacks
the most substitute models as the final attack output. CEMA is evaluated on two
primary multi-task objectives: text classification and translation. In the classifica-
tion task, CEMA achieves attack success rates that exceed 60% while reducing the
total number of queries to 100. For the text translation task, the BLEU scores of
both victim texts and adversarial examples decrease to below 0.36 with 100 queries
even including the commercial translation APIs, such as Baidu Translate and Ali
Translate.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper is about a new text-based adversarial attack that works simultaneously against multiple NLP models.

### Strengths
- The table is easy to read.

### Weaknesses
 - No real threat model. The authors did not properly specify adversarial capabilities (e.g., number of tokens allowed to flip), so I am unable to interpret what the results are supposed to mean. Note that, without constraints on perturbation of the input, it is trivial to fool sentiment models by providing a movie review with the opposite sentiment, or fool translation models by inputting gibberish. **Please explicitly define the constraints on input perturbations, such as the maximum number of tokens that can be modified or any other relevant limitations on the adversarial capabilities.** This would allow for a more meaningful interpretation of the results.
- The author claims to "demonstrate the effectiveness of CEMA through rigorous mathematical derivations", but the math makes no sense.
  - For example, the authors attempted to justify why generating multiple adversarial examples is useful. They made an argument that each attack query has at least probability $p_\min$ of being successful, so the likelihood of some query being successful is 1 with sufficiently many queries. This is clearly false. Even if $p_\min$ is non-zero, different attack queries would not be independent random variables and the derivation is just wrong.
  - I'm not sure why there is a derivation of the "maximum entropy distribution" (Appendix C) and "union bound" (Appendix D) in the paper. They seem completely irrelevant.
  - Appendix B on transferrability of adversarial examples is barely related to the proposed method itself.
- What do you mean by attacking multi-model multi-task learning? How is this different from transferrable adversarial examples? I am concerned that you are redefining a well-studied problem and not properly acknowledging prior literature.

- What's the unit of queries in Table 1? What does it mean to use 0.05 queries?

### Questions
- What's the unit of queries in Table 1? What does it mean to use 0.05 queries?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors propose a transfer-based black-box text attack for multi-task learning called Cluster and Ensemble Multi-task Text Adversarial Attack (CEMA). In particular, CEMA employs a cluster-oriented substitute model training to obtain the substitute mode. Then CEMA generates the adversarial examples using various adversarial attacks and chooses the adversarial example that attacks the most substitute models as the final attack output. Experiments validate the effectiveness of the proposed method.

### Strengths
1. The cluster-oriented substitute model training is interesting.

2. The proposed CEMA exhibits good transferability.

3. The authors have derived the theoretical lower bound for CEMA's success rate.

### Weaknesses
1. The paper is not well written and hard to follow. It is not clear how to generate adversarial examples using the surrogate model.

2. What is the main contribution of this paper? Is it the substitute model training or the attack method? I do not get the attack method. But if it was the substitute model training, why do not the authors compare CEMA with the adversarial examples generated on various substitute models?

3. Most of the baselines are black-box attack, which can directly attack online APIs. Since the authors evaluate the transferability, I think the authors should consider more efficient attacks using gradient [1,2] as in the image domain.

4. It is weird that the average number of queries is smaller than 1.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents CEMA, a new text adversarial attack against multi-task learning in the black-box setting. The basic idea of this method is to adopt a cluster-oriented substitute model training to convert the problem into a text classification attack. Representation learning is used for the above clustering. Multiple substitute models are generated to produce the high-quality adversarial examples that are effective against different tasks concurrently. Comprehensive evaluations are performed to demonstrate the effectiveness of this solution.

### Strengths
1. This paper is well-written and easy to follow. 
2. The proposed method is novel and solid. 
3. Experiments are extensive, with baseline comparisons over different methods.

### Weaknesses
Thanks for submitting this paper to ICLR. Generally I enjoy reading this paper. It is very clear. I have the following doubts regarding the proposed method. 

1. While the attack is efficient in terms of model query, I am wondering what is the computation overhead at local? The attacker requires to train multiple substitute models for candidate selection. However, I could not find the number of substitute models used in this paper. Clearly a larger number of substitute models lead to higher overhead. What is the cost of performing the presentation learning, clustering, training substitute models, and generating adversarial examples? 

2. The experiments only consider two types of tasks with three models (two for classification and one for translation). What is the scalability and effectiveness of the method for more types and numbers of tasks? 

3. This paper does not consider the evaluation of SOTA defenses against the proposed method. It is recommended to present the attack results under different defense methods, like adversarial training and others.

### Questions
1. What is the computation overhead of your attack? 

2. What is the scalability of your attack in terms of number of tasks? 

3. What is the performance of your attack against SOTA defenses?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
A new adversarial attack is proposed for text based multi-task models. The attack is called, “CEMA” or Cluster and Ensemble Mutil-task Text Adversarial Attack. Substitute models are trained in this attack and then various adversarial examples are generated. After selecting the example that fools a majority of the models, this example is used as the final attack input. The two task that are attacked are text classification and translation. Empirically the methods are test on two datasets, SST5 and Emotion.

### Strengths
The paper is well written and clearly organized. The adversarial threat model is well defined and I appreciate the authors try to use a black-box approach (as opposed to many adversarial attacks that assume complete white-box knowledge of the setup). The empirical results demonstrate the effectiveness of the new method on two datasets.

### Weaknesses
There are three main issues that I see with the paper:

Issue 1: Lack of proper citations. There are a number of works that this paper implicitly builds off of but are not explicitly cited. Due to this several experiments are missing that I think would better illustrate and help the readers understand the effectiveness of the proposed approach. First of all the discussion of transferability only mentions the original Papernot work, but is missing other type of attacks that increase the amount of data available to the attacker (https://arxiv.org/abs/2006.10876) or generate synthetic data (https://arxiv.org/abs/2003.12703). I would say at a minimum these two additions to the original 2016 Papernot transfer attack should be cited in relation to improving the CEMA and discussed. Likewise, when discussing transferability in general there are several related and follow up works that the authors do not include any mention of:

https://arxiv.org/abs/1704.03453

https://arxiv.org/abs/2104.02610


Issue 2: Because the authors seems to be unaware of some of the more recent develops in adversarial attacks/defenses, it would be great if two additional experiments or discussions could be had. First: what happens if the query number or amount of training data available to the attacker is increased like in (https://arxiv.org/abs/2006.10876)? I think that is important to understand what effect changing the strength of the adversarial threat model has on the attack success rate. For example if say 1000 or even 10,000 samples of training data are made available to the adversary, how much more effective is the transfer attack? Likewise, if we drop the number down to 50 or 10 samples, what happens? I am okay accepting the paper even IF the attack fails when less samples are used. I just think it is a necessary step in the attack analysis that is currently missing. 

Second: Many transfer attacks may fail (citation: https://arxiv.org/abs/2104.02610) when the models are shuffled in a randomized manner. Such work in the image domain that has shown an increased robustness over SOTA single model defenses can be seen here (https://arxiv.org/abs/2211.14669). Because the authors didn’t test on any defenses, I would be curious if they could train additional models and test a simple defense where they try to shuffle between two models during querying and attack time? Or if the authors feel this is not relevant, could they include a discussion of this in their paper and cite the appropriate papers as mentioned in this paragraph to explain why? 

Issue 3 (minor): Is there any reason that the authors only choose to use 3 different victim models when doing the experiments? As a reviewer I cannot mandate that additional experiments are done, but I would be curious as to the justifications for three models used in the paper?

### Questions
Please address the three issues that I have brought up in the weakness section of the paper. If you can provide better discussions and citations to the relevant adversarial literature and address my comments, I would be inclined to increase my score accordingly.

UPDATE: Score has been updated according to the rebuttal from the authors.

### Soundness
3

### Presentation
3

### Contribution
3
