# Towards Complete Expressiveness Capacity of Mixed Multi-Agent Q Value Function

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Value decomposition is an efficient approach to achieving centralized training with decentralized execution in fully cooperative Multi-Agent Reinforcement Learning (MARL) problems. Recently, Strictly Monotonic Mixing Function (SMMF) has gained widespread application in value decomposition methods, but SMMF could suffer from convergence difficulties for the representational limitation. 
This paper investigates the circumstances under which the representational limitation occurs and presents approaches to overcome it. 
We begin our investigation with Linear Mixing Function (LMF), a simple case of SMMF.
Firstly, we prove that LMF is free from representational limitation only in a rare case of MARL problems.
Secondly, we propose a two-stage mixing framework, which includes a difference rescaling stage after SMMF to complete the representational capability.
However, the capacity could remain unrealized for the cross interference between the representation of different action-values. Finally, we introduce gradient shaping to address this problem. 
The experimental results validate the expressiveness of LMF and demonstrate the effectiveness of our proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studied the problem representation limitation in value decomposition method in fully cooperative multi-agent reinforcement learning. The author proposed a novel idea that the representation limitation comes from two different perspectives, task property and mixing function.

The authors theoretically proved that LMF is free from representational limitation only in a rare case of MARL problems. SMMF suffers from representational limitation due to the bounded difference between the outputs of greedy and current actions.

To address these issues, the authors also proposed a new framework of mixing for unbounded difference and test with experiments on several different environments.

### Strengths
This paper studied a very basic problem in value-based multi-agent reinforcement learning, and theoretically proved the limitations of both the problem itself and existing methods.

### Weaknesses
The writing quality could be further improved. It's a little bit hard to follow the paper currently.

### Questions
1. We still have some other combination types that is stronger than IGM but is not perfect. Please discuss about this part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on addressing the important problem of representational limitation in value decomposition methods for Multi-Agent Reinforcement Learning (MARL) problems. The contributions of the paper are as follows:

1. The paper defines the circumstances under which the linear representational limitation occurs, specifically for Linear Mixing Function (LMF).

2. It introduces a two-stage mixing framework called Mixing for Unbounded Difference (MUD) that addresses the representational limitation by ensuring complete representational capacity under the Independent Global Max (IGM) constraint.

### Strengths
This paper exhibits several notable strengths across multiple dimensions.

_Originality_

   - The introduction of the Mixing for Unbounded Difference (MUD) framework, as far as the reviewer is concerned, represent new solutions to address the representational limitation issue. (Although it shares some similarities with other methods, see the weakness section).

_Quality_

   - The proposed MUD framework is supported by mathematical reasoning, enhancing its quality as a potential solution.

### Weaknesses
1. The first contribution about LMF and the second contribution on SMMF seems to be separated.

2. The findings about LMF is not quite surprising, as previous work indicates its limitations. What could be interesting is why LMF can work well (empirically) on many tasks, especially when used with gradient-based RL methods.

3. Why do the experiments demonstrate advantage of the proposed method on SMAC, but the performance is similar to baselines in relatively easy task of Predator-and-prey?

4. (*) The proposed MUD share similarities with the QPLEX framework. So the empirical comparison is very important. The reviewer is curious why the performance of QPLEX on SMAC is __significantly__ different from what was reported in the original paper.

4.1 Please discuss the difference from QPLEX in detail.

5. (*) The representational interference problem is not unique to the MUD framework and has been discussed by previous work [1].

(4 and 5 are the main reasons for the overall negative score.)

### Questions
Please see the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to tackle the issues of value decomposition. Initially, it explores the expressive capacity of linear mixing functions and then develops a decomposition structure to achieve complete representational capabilities. Additionally, it identifies and offers a solution to the problem of optimal representation interference. Experimental results substantiate the efficacy of the proposed method.

### Strengths
The paper presents a substantial and meticulously detailed theoretical derivation and proof.
The proposed method to construct the complete representational structures is interesting and novel.

### Weaknesses
The paper suffers from some unclear expressions and inconsistencies with prior research.
The experimental evaluation is lacking.
See questions below for detail.

1. The relationship between this paper and [1] requires further elucidation. What's the connection between "the LMF in indecomposable MMDP has unbaised TD target in sarsa" and "the on-policy LMF with fitted-q-iteration has at least one fixed-point Q-value that derives the optimal policy" ? It appears that the results in [1] might be stronger.

2. The paper mentions that addressing single-step matrix games is applicable to solve the optimal policy, but only for sarsa. Does this imply that the theoritical results can only be upheld through on-policy training, or is this just a conclusion unrelated to the subsequent paper?

3. Why is Eq6 used to define complete representational capacity in this paper? The meaning of complete representational capacity under IGM remains unclear. Is this consistent with prior works?
QTRAN is known be necessary and sufficient for IGM, but it has incomplete expressiveness in the context of this paper. Does this imply that methods with incomplete expressiveness can also theoretically guarantee optimal outcomes?

4. Confusing about the "monotonic mixing" and "strictly monotonic mixing". I think the original "monotonic" in previous work means "strictly monotonic" in this work, rendering the "monotonic" in this work redundant. To the best of the reviewer's knowledge, none of the existing methods under IGM are non-monotonic. In fact, non-monotonic mixing might not satisfy IGM.

5. The paper introduces multiple mixers to cover a wider range of mixing functions. This needs further clarification. Is this theoretically necessary, or is it merely a technique for improved performance? It would be valuable if an ablation study on different numbers of mixers in SMAC is conducted.

6. The meaning of Eq11 requires further explanation. Why is the optimal representation ratio defined as such, and what does a low w* signify in terms of ORI?

7. The final algorithm, particularly the expression of Q_tot, is unclear. How are Eq12 and Eq13 applied in Eq10?

8. Does the final algorithm possess complete expressiveness or is it necessary and sufficient for IGM?

9. Why is the single-step matrix game trained in an on-policy manner? Can the proposed method converge to the optimum through off-policy training? Additionally, can QTRAN achieve convergence to the optimum in this game?

### Questions
1. The relationship between this paper and [1] requires further elucidation. What's the connection between "the LMF in indecomposable MMDP has unbaised TD target in sarsa" and "the on-policy LMF with fitted-q-iteration has at least one fixed-point Q-value that derives the optimal policy" ? It appears that the results in [1] might be stronger.

2. The paper mentions that addressing single-step matrix games is applicable to solve the optimal policy, but only for sarsa. Does this imply that the theoritical results can only be upheld through on-policy training, or is this just a conclusion unrelated to the subsequent paper?

3. Why is Eq6 used to define complete representational capacity in this paper? The meaning of complete representational capacity under IGM remains unclear. Is this consistent with prior works?
QTRAN is known be necessary and sufficient for IGM, but it has incomplete expressiveness in the context of this paper. Does this imply that methods with incomplete expressiveness can also theoretically guarantee optimal outcomes?

4. Confusing about the "monotonic mixing" and "strictly monotonic mixing". I think the original "monotonic" in previous work means "strictly monotonic" in this work, rendering the "monotonic" in this work redundant. To the best of the reviewer's knowledge, none of the existing methods under IGM are non-monotonic. In fact, non-monotonic mixing might not satisfy IGM.

5. The paper introduces multiple mixers to cover a wider range of mixing functions. This needs further clarification. Is this theoretically necessary, or is it merely a technique for improved performance? It would be valuable if an ablation study on different numbers of mixers in SMAC is conducted.

6. The meaning of Eq11 requires further explanation. Why is the optimal representation ratio defined as such, and what does a low w* signify in terms of ORI?

7. The final algorithm, particularly the expression of Q_tot, is unclear. How are Eq12 and Eq13 applied in Eq10?

8. Does the final algorithm possess complete expressiveness or is it necessary and sufficient for IGM?

9. Why is the single-step matrix game trained in an on-policy manner? Can the proposed method converge to the optimum through off-policy training? Additionally, can QTRAN achieve convergence to the optimum in this game?

[1] Wang et al. Towards understanding linear value decomposition in cooperative multi-agent q-learning. 2020.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
