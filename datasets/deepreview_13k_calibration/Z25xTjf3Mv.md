# Enhancing Deep Partial Label Learning via Casting it to a Satisfiability Problem

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 5, 8, 3, 3

## Abstract
Partial label learning (PLL) is a challenging real-world problem in the field of weakly supervised learning, in which each data instance contains a set of candidate labels with multiple ambiguous labels and one gold label. Although recent progress in PLL using deep representation learning has led to significant advances, the methods continue to experience significant performance drops on data with high label ambiguity and fine-grained categories. By casting PLL into a satisfiability problem and incorporating a loss based on this reduction,  we show that the accuracy of those techniques can be further improved. We establish several key theoretical properties of the proposed SATisfiability-based (SAT) loss and its learning error bound. Our extensive empirical comparison reveals that the proposed loss improves over existing PLL techniques by up to 25.12% on multi-class benchmarks and 12.50% on fine-grained categorized benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method for Partial Label Learning (PLL) by formulating the task as a satisfiability (SAT) problem and introducing a SAT-based loss function. Partial label learning involves scenarios where each data instance has multiple candidate labels, but only one is correct. The authors argue that current PLL methods struggle in cases of high label ambiguity and fine-grained categorization. By encoding PLL constraints as logical formulas and designing a SAT loss that penalizes unsatisfied formulas, this method encourages disambiguation toward the true label without relying on pseudo-labels. The approach is validated on various benchmarks, showing up to 25% improvement over existing PLL techniques, such as PICO and PAPI, in certain settings.

### Strengths
Novel Problem Framing: Casting PLL as a SAT problem is innovative, providing a new angle to address label ambiguity. The SAT loss introduces a logic-driven constraint, which could contribute positively to PLL tasks by enforcing logical consistency.
Solid Theoretical Foundation: The paper includes theoretical analysis, demonstrating the robustness of SAT loss in high-ambiguity scenarios and fine-grained categorization tasks, supported by proofs of error bounds and properties like low-entropy preference.
Significant Experimental Improvements: Empirical results are extensive, covering diverse datasets and demonstrating significant performance gains. The experiments suggest that the SAT loss is effective in improving classification accuracy and resilience in challenging PLL scenarios.

### Weaknesses
Limited Innovation Scope in PLL: While the SAT-based formulation is novel, it may be perceived as incremental in its application, as it leverages established ideas from satisfiability and logical constraints. Whether this alone constitutes a breakthrough in PLL could be debatable, especially given the broader ICLR scope. The core contribution seems to be the application of a SAT-based loss, but the underlying PLL problem and the methods it builds upon are not fundamentally changed. The novelty is therefore somewhat limited to the specific loss function design rather than a more transformative approach to the problem itself.
Dependency on Existing Models: The proposed SAT loss is integrated with existing PLL methods like PICO and PAPI rather than functioning independently as a standalone model. This limits the novelty of the overall algorithm, as the SAT loss relies heavily on baseline techniques for its effectiveness. The paper does not explore the standalone performance of the SAT loss with a simple classification model, which would help to isolate the impact of the proposed loss function. Without such analysis, it's difficult to ascertain the true contribution of the SAT loss beyond its integration with existing frameworks.
Complexity and Scalability Concerns: Implementing SAT loss with logic-based constraints may increase computational requirements. The scalability of the approach to large-scale, real-world datasets or cases with more complex dependencies among labels could be challenging and is not addressed in depth. The paper lacks a detailed analysis of the computational overhead introduced by the SAT loss, particularly in terms of training time and memory usage. The discussion on computational complexity is limited, and there is no empirical evaluation of the scalability of the method with increasing dataset size or label ambiguity.

### Questions
Generalization to Real-World Data: Does the model maintain its efficacy when applied to real-world, noisy datasets where label ambiguity might not align as neatly with the SAT loss assumptions?

Computational Overheads: The SAT loss, while theoretically sound, could introduce computational complexity. How does this approach compare in terms of training efficiency with more traditional PLL methods?

Potential for Broader Application: Could the SAT-based formulation be generalized to other types of weakly supervised learning beyond PLL, such as multi-label learning?

Please clarify the significance of this partial label learning setting. Is it truly valuable to have numerous papers on this problem, given that each often presents only marginal improvements?

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
4

### Summary
In this paper, the authors casted PLL into a satisfiability problem and incorporated a SATisfiability-based (SAT) loss based on this reduction. Besides, the authors proved several natural properties of satisfiability-based PLL: that the loss is non-increasing the larger candidate label sets become and that it favors low entropy classifiers. Experiments show that satisfiability-based training leads to consistently higher classification accuracy over all settings compared with previous state-of-the-art techniques.

### Strengths
The proposed SATisfiability-based (SAT) loss leads to consistently higher classification accuracy over all settings compared with previous state-of-the-art techniques.

### Weaknesses
1. **Lack of Intuitive Explanation for the Proposed Method's Effectiveness**: While the paper introduces the idea of "casting PLL into a satisfiability problem" to address performance drops in data with high label ambiguity and fine-grained categories, the intuition behind how this formulation resolves these issues is not sufficiently explained. Specifically, the paper does not clearly articulate why a SAT-based loss, derived from logical constraints, is inherently better at handling noisy pseudo-labels compared to traditional cross-entropy loss. Furthermore, the connection between the theoretical properties of the SAT loss, such as monotonicity under ambiguity, and its practical effectiveness in disambiguating labels in fine-grained classification tasks remains unclear. The paper needs to provide a more concrete explanation of how the SAT loss's preference for low-entropy solutions directly translates to improved classification accuracy in these challenging scenarios.

2. **Unclear Distinction Between PLL and Complementary-Label Learning**: The relationship between the proposed PLL method and Complementary-Label Learning (CLL) is not well articulated. The paper acknowledges that minimizing the probability of labels not in the candidate set is conceptually similar to objectives in CLL, yet it does not provide a detailed analysis of the differences in their optimization objectives and practical implications. The paper should clarify whether the proposed method can be considered a generalization of CLL or if it addresses a fundamentally different problem setting. A more thorough comparison, including a discussion of the specific scenarios where each approach is most effective, would be beneficial.

3. **Absence of Ablation Studies**: The paper lacks ablation studies that could provide more detailed insights into the contributions of each component of the proposed method. While theoretical justifications for the SAT loss are provided, their direct relevance and contribution to the method’s practical effectiveness are not sufficiently explored. It is unclear how much of the performance gain is due to the SAT loss itself versus other aspects of the framework. For example, it would be helpful to see results with and without the SAT loss, and with different configurations of the SAT loss to understand its sensitivity to hyperparameters. Additionally, the paper should investigate the impact of different choices of the logical constraints used in the SAT formulation.

### Questions
1. The approach of "casting PLL into a satisfiability problem" proposed in the paper is suggested to help address the issue of "significant performance drop on data with high label ambiguity and fine-grained categories." Could the authors provide some intuitive insights or explanations on how this formulation helps in this context? It appears that this approach could also address the issue of "low label ambiguity."

2. In the methodology section, the form of Eq. (3) appears similar to that used in Complementary-Label Learning. Based on this, it seems that the goal of minimizing the probability of labels not in the candidate label set is conceptually similar to the objectives in Complementary-Label Learning[1][2]. When the number of labels in the candidate label set increases, PLL seems to approach the problem of Complementary-Label Learning in some respects. Could the authors elaborate on the relationship between these two approaches?

3. In Section 4, the SAT loss is provided with theoretical justification. I would like to know whether these theoretical justifications offer any insights or guidance for the methodology and the underlying problem it addresses. For example, does Theorem 4.4 provide any valuable insights into the design of the proposed method?

4. The experiments lack corresponding ablation studies. Could the authors provide some potential ablation experiments or suggestions on which experiments could be conducted to further validate the proposed method?


[1] "Discriminative complementary-label learning with weighted loss." ICML 2021.

[2] "Learning with multiple complementary labels." ICML 2020.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
A SAT-based formulation of the partial label learning problem is proposed. The authors encode each training instance (data / candidate-label pairs) into formulas in propositional logic. The proposed method then exploits a SAT-based loss to do training over these formulas. Theoretical justification is provided. The authors demonstrate (1.) robustness to label ambiguity- i.e. the risk a classifier suffers wrt the SAT loss is non-increasing with the partial label ambiguity. (2.) the SAT loss is proportional to the entropy of the network logits i.e., minimization of the SAT loss induces low-entropy confident predictions. The authors also provide a detailed analysis of the generalization of classifiers trained with the SAT loss. 

Empirically, a significant improvement is demonstrated on a variety of datasets, including CIFAR100 and tiny-imagenet. Improved clustering of the latent space embeddings is demonstrated by applying T-SNE to model embeddings.

### Strengths
I find this paper to be very well-written and interesting- I appreciate the examples. The core concept is novel and I believe bridging neural methods and logical reasoning is an important topic of study. The inclusion of a detailed, but concise, theoretical analysis is beneficial in providing justification for their method. The empirical results are encouraging as well and I am happy to see that the authors have provided code. I am inclined to accept this paper.

### Weaknesses
I assume there would be other methods that can be used to penalize the entropy of predictions. How does the proposed SAT loss compare to those methods?

If a subset of the partial labels are noisy how would SAT loss perform?

### Questions
I assume there would be other methods that can be used to penalize the entropy of predictions. How does the proposed SAT loss compare to those methods?

If a subset of the partial labels are noisy how would SAT loss perform?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel loss function applicable to partial label learning, a problem in which each datapoint is annotated with a set of candidate labels, of which only one is the correct (or gold) one. They also provide the learning error bounds of this new loss and an extensive experimental analysis.

### Strengths
The paper is quite easy to follow.

### Weaknesses
The paper presents a series of dubious claims:

1. The authors first try to cast PLL as a satisfiability problem. This entails encoding the candidate set into a boolean formula which can be intuitively divided into two subformulas: one that states that at least one label in the candidate set should be the predicted and the other that states that only one should be predicted. Now, the authors can discard the second formula (which also happens to be very large) because they assume that they only work with models with softmax non-linearity in their last layer. This is fine, but then essentially their loss function is simply trying to maximise the probability that one of the labels in the candidate set should be predicted. There are many functions in the PLL community that try to do this (e.g., the methods based on the EM algorithm [1]). How is your loss different and better than these methods? Specifically, the authors do not clearly articulate how their loss function, which essentially maximizes the probability of *any* label within the candidate set, distinguishes itself from existing approaches that also aim to achieve the same goal. The theoretical analysis should explicitly address how the proposed loss leads to better disambiguation of the true label compared to other methods.

2. The authors call their loss the Saitifiability-based loss which from Remark 3.3 seems to simply coincide with the Product t-norm in the fuzzy logic literature. This is a failure to recognise the fact that the authors are *not* proposing a new loss, but they are applying a known loss function (which has been heavily studied in the Near-symbolic AI literature) in the PLL field. The authors need to clarify the novelty of their approach given the existing literature on t-norms and their application in loss functions. The connection to fuzzy logic, while interesting, does not justify the claim of a novel loss function if it is mathematically equivalent to a known t-norm.

3. The authors give a definition of the *small ambiguity degree*, however, that definition coincides with Cour's definition of ambiguity degree. If that is the small one, how would be large ambiguity degree be defined? The authors should provide a clear distinction between their definition of small ambiguity degree and existing definitions, and clarify what constitutes a large ambiguity degree in their context. The current definition seems redundant and does not introduce a new concept.


Smaller problems/typos: 

- In Figure 2 what is PC, MC, PI and MI? 
- Page 3 line 155 it should be the marginal of $P(X,S,Y)$
- Equation (2) it should be $X_{j'}$
- Corollary 4.2, of what exactly is a Corollary? 

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work discussed the partial label learning(PLL) problem, which means that the supervision information is a set of possible labels.

Specifically, this paper proposed a satisfiability-based(SAT) loss function to handle the PLL problem.

To do this, they first transform the partial label information into the propositional logic formula, e.g., $\displaystyle\phi = (\land_{i\in s} X_i)\land \neg(\text{more than one label is correct})$. 
Then they optimize this loss function as any other loss function, by maximizing the semantic loss form.

The authors also established a generalization error bound under the low-ambiguity assumption.

### Strengths
+ The paper is generally easy to read and follow.
+ The proposed method shows a good performance.
+ They give a classical generalization error analysis.

### Weaknesses
 - **Motivation is UNCLEAR.** The introduction failed to explain why this paper should introduce the SAT loss. As the authors claim that the previous works are not good enough, they say the previous methods have *undesired behavior*, which is very fun, because no method can guarantee error-free, especially in such a weakly-supervised learning scenario.
  - For example, the motivation example and analysis of the introduction part (see lines 27 to 100) can be used to introduce the motivation of any algorithm of partial label learning. 
  - The necessity of transforming a partial label constraint to a propositional logic formula is unclear, why? 

- **Claims are UNSUPPORTED or TRIVIAL.** There are two claims of the proposed method.
  - *Robustness*. The authors claim that the proposed SAT loss is robust to high label ambiguity. They explained that 
> the SAT loss holds the property that its risk is non-increasing as the small ambiguity degree increases.

    This is not a good explanation, because *any* loss function with $\prod_{i \in s} \ell(f(x_i))$ form will satisfy this property.

  - *Disambiguation*. The authors say that the proposed SAT loss can perform better by *low entropy preference*. However, it is a small trick to regularize the model's output to have low entropy in the field of weakly-supervised learning. It is *not a rare property, many loss functions can induce such a property*, and it can not explain why this method is better since there is no more information used.

- **Theoretical analysis is EMPTY**. The given bound is not rigorous, first, the given bound can only hold when the classification task is binary, that is to say, this bound is not consistent with the notations introduced in the paper. Although this problem can be fixed easily to extend to a multiclass case. The established bound is no better than the earlier proposed PLL bound [1,2]. Especially, we can see that the Rademacher complexity is increased if we choose the SAT loss. Also, the established process of this error bound is very common in this field, thus can not bring any new insight or perspective to us.

- **Experiment results are Weried**. The reported performance of SAT loss is surprisingly high, for example, the reported performance of CIFAR-100 (see Table 1) is even better than the supervised case (purely use cross entropy). It is convinced that the experiments are done in unfair settings, i.e., using bags of tricks. Thus it is difficult to say the SAT loss is better. Besides, I *checked the code*, and the running code is different compared with what the authors said in their paper. For example, they use more than SAT loss, but also EMA trick, warmup learning rate decay, and mixup loss, and even more I have not carefully checked.  It is easy to do such a good performance if you can do many bags of tricks. 

### Questions
Q1: Can you explain your motivation clearly?

Q2: Can you support your claims? 

Q3: Can you explain the superiority of your error bound compared with other papers (for example, the listed two)? 

Q4: It is well-known that the semantic loss minimizes the inconsistency of the model and the logic constraint, the proposed loss can be seen as a special case of semantic loss. But the computational complexity of the semantic loss is very high, in fact, the computation of SL is #P, which is usually harder than NP. Can you compare the efficiency of the algorithm with other methods? Especially on a large scale (concerning the label space size).

### Soundness
1

### Presentation
2

### Contribution
1
