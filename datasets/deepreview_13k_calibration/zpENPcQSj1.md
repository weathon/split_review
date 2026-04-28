# Generalizing Reasoning Problems to Longer Lengths

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
Length generalization (LG) is a challenging problem in learning to reason. It refers to the phenomenon that when trained on reasoning problems of smaller lengths/sizes, the model struggles with problems of larger sizes or lengths. Although it has been proven that reasoning can be learned if the intermediate reasoning steps (also known as chain-of-thought (CoT)) are given in the training data, existing studies only apply to within a given length (interpolation), while LG is about extrapolation beyond the given length. This paper begins by presenting a theorem that identifies the root cause of the LG problem. It then defines a class of reasoning problems for which achieving LG with Transformers can be theoretically guaranteed, provided the CoT schemes are constructed to meet a proposed condition called $(n,r)$-consistency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a framework for studying the length generalization ability of scratchpad/chain-of-though (CoT) methods for reasoning problems such as arithmetic. More precisely, a condition, $(n, r)-consistency$, has been proposed such that if CoT satisfies this property, one can design a model capable of length generalization (an approximation/expressivity result). The paper further provides experimental evidence showing that the proposed CoTs are indeed learnable.

### Strengths
- The paper tackles the important problem of length generalization on reasoning tasks. It provides a condition for CoTs such that if that condition is satisfied length generalization becomes potentially possible. Theoretical results on the expressively and empirical results on learning are provided in the support of that condition. 
- The experimental results seem very interesting and strong (e.g., division is a newly considered task) although there are concerns (see below). 
- The multi-line scratchpad/CoT and its implementation are interesting.

### Weaknesses
 - One of the main weaknesses is the modeling assumption. Generally, the CoT setting works as follows that when we have given $S_0$ as input to the language model (LM), the LM would generate a sequence of thoughts, $S_1, S_2, \ldots, S_T$ that would solve the task (answer is often in $S_T$). However, the modeling in this paper is that we give $S_0$ to the model and get $S_1$ then we give $S_1$ as input to the model to get $S_2$ and so on. So instead of $model(S_0)=S_1, S_2, \ldots, S_T$ we have $model(S_i)=S_{i+1}$. I think this modeling is not a significant issue, it is just an unconventional way (which may work better that the the conventional way) that should be properly acknowledged, explained, and clarified throughout the paper. Currently the paper doesn't acknowledge this difference with normal CoT methods. Further, this problem becomes more significant in two ways:
     - The model doesn't learn the termination condition. In other words, it's not the model that understands $model(S_{T-1})=S_{T}$ is the final step and it shouldn't compute $model(S_T)$, but this is manually controlled by the user. 
     - It seems some further processing are done on the inputs and outputs. In particular, it seems input[k+1] is not exactly output[k]. 

All of these processings and manual handlings seem like engineering hacks which would not generalize to other problems. (Although length generalization on tasks such as addition are important as evaluation metrics, however, we are more generally looking for approaches that would generalize to other problems as well -- in particular to problems that we have less control over the data.)

### Questions
- From what I understand from Appendix D, we see that output[k] is not always exactly equal to input[k+1] (e.g., in the addition examples). I think this is some sort of processing that is not necessarily generalizable to other tasks because it uses the knowledge of the task too much (I personally see it an engineering hack). Is there a way to avoid that and be more agnostic towards the task?
- Similar to the concern above, In Appendix D, we see some orange lines that are not predicted by the model and are manually inserted. I think this again reduces the learning part of the paper and is an engineering trick. Can it be avoided?
- I'm not sure if I completely understand how the padding works. When you pad, you still have blank tokens at the start and end of the sequence. However, they are not the middle of any interval. So how are they predicted? Also are the padding tokens provided for all the examples in Appendix D?
- In experiments, the length generalization ability is tried on different lengths and for all of them we see 100% performance. So I wonder what's the point that we see some reduction in the performance? Why haven't you tested the length generalization ability on longer sequences?
- The experiments are done with specialized Transformers. I wonder what would be the length generalization performance if CoT steps were learned by a typical model, e.g., GPT2 or llama?

Minor feedbacks: 
- From what I understand, it's not important where the intervals other than the anchor interval are located, is that right? I think it would be  nice if this is further clarified in the paper. 
- I think Theorem 3.1 is doing more harm than good. I think the statement that is saying "we have infinite continuations" is more or less intuitive. Further, I think modeling discrete token space with continuous intervals is not justified. Also, why is Lipschitz assumption on these intervals a reasonable property? (and in that case what are the Lipschitz constants?) By default, we expect the distance of the tokens to be more or less the same, however, the Lipschitz assumption goes hand in hand with the Euclidean distance on the intervals which is problematic. For example, if tokens A, B, C correspond to points -1, 0, 1 on the interval. The Lipschitz assumption implies that the semantic distance between (A, B), (B, C) is smaller than (A,C). So I think the Lipschitz property and the use of continuous intervals in this Theorem is unjustified. I would really suggest to use a simpler theorem on discrete token space.
- The abstract and intro imply that authors have found a necessity condition for length generalization and thus I think they should be revised. 
- I find the proof sketch part very interesting, and I'd suggest authors to further elaborate on it. (In that case, you may want to move some of the experiment details to the appendix).

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
4

### Summary
**Update after rebuttal:** While some of my criticism remains, the authors have clarified some misunderstandings and questions I have had, and have significantly sharpened the focus of the paper (defining a problem class for which LG can be theoretically guaranteed; as well as putting the emphasis on the empirical side). Accordingly, I have raised my score from a 5 to a 6.

---

This paper investigates the challenge of length generalization with transformers. The paper first points out the well-known fact that the induction problem has no correct solution. For length generalization, additional assumptions are thus necessary. The paper proposes to restrict length generalization to a class of problems that can be decomposed into a set of (n) repeated subproblems that only require local context (of length r) around a set of anchor positions: (n,r) consistency. This “necessary” condition (which is a bit of a tautology because the problem class was defined according to the necessary condition) is then shown to be sufficient for the problem to be solved with transformers in theory (ignoring questions around learnability and model capacity, etc.). As the paper notes in 3.5, there is no general method to implement the process that decomposes an original length generalization problem into a “Chain-of-Thought” (CoT) formulation that can be solved by sequential execution of a number of local subproblems. But the paper correctly argues that if solving this problem reformulation such that (n,r) consistency can be ensured, transformers should suffice in principle to solve the modified problem. (n,r) consistency can thus be seen as a guiding target for CoT formulations. A small set of empirical results confirms the relevance of the theoretical result in practice. For training the CoT decomposition of the original problem is done by manually designed, problem specific algorithms, and transformers are trained to execute these algorithms of stepwise rewriting of the problem and simultaneously solving suitable subproblems during rewriting.

### Strengths
* Timely and important problem: length generalization even on simple tasks is a regime where transformers struggle.
* Definition of an interesting class of length generalization problems: the class of problems where a decomposition with (n,r) consistency is possible. These problems match well onto, and are probably solvable (in theory) by, transformers.
* Good empirical results on historically challenging problems like parity, addition, multiplication and division.

### Weaknesses
 * The CoT decomposition does most of the heavy lifting - but it is done manually. The paper makes very little progress here, except defining (n,r) consistency as a guiding principle to aim for (but with no systematic process to get there, and no theoretical understanding of how the class of (n,r) consistent decomposable problems relates to general function and complexity classes (e.g., regular languages). The lack of a systematic method to derive these CoT decompositions significantly limits the practical applicability and scalability of the proposed approach. It is unclear how this manual process would generalize to more complex tasks or larger problem instances, and the paper does not provide any theoretical analysis of the complexity of finding such decompositions.
* Writing throughout most of the manuscript makes claims that are either too grand or not sharp enough, which makes the first part of the paper a bit misleading. For example, (n,r) consistency is not *necessary* to solve length generalization in general. There are loads of other approaches that have been proposed before and that are theoretically very well understood - they typically use different biases, most commonly low-complexity biases, to answer the induction problem (such as Solomonoff Induction or Bayesian inference for example). What is correct is that when restricting to problems that allow for a (n,r) consistent decomposition, length generalization can be solved uniquely without requiring additional biases. I will be more specific in the Questions section. The paper should more clearly acknowledge that it is focusing on a specific subset of length generalization problems rather than providing a general solution.
* Learnability and generalization with transformers in practice remain unclear (bounded capacity, finite data, SGD). The CoT decomposition works on the simple examples shown, but it is not clear whether this would hold at scale (the number of (n,r) consistent CoT steps may scale very badly for some problems); or even how to do this - e.g., how would one train a transformer that can solve all tasks in the paper simultaneously. How would one go about eventually reaching the scale of modern frontier models? The paper lacks a thorough discussion on the practical limitations of training transformers with the proposed CoT schemes, particularly concerning the scaling of the number of CoT steps with problem complexity and length, and the potential challenges in learning multiple tasks simultaneously with a single model.

### Questions
**Improvements** (that would make me raise my score, but may not be possible within the short rebuttal time)

1. A significant overhaul / rewrite to emphasize that the main contribution is not a theory of length generalization and identification of a novel root cause (the root cause is well known in machine learning, mathematics and philosophy), but a definition of a problem class that has favorable properties w.r.t. length generalization built in, and these properties can be exploited by transformers.
2. If the focus of a major revision lies on the theory (though I personally would recommend leaning more towards the empirical side), then the problem class of (n,r) consistent problems needs to be better understood theoretically. E.g., how does it relate to commonly known complexity classes such as regular languages or $TC^0$? Is this class likely to be complete, i.e., all problems where transformers can length generalize must be (n,r) consistent (which I personally doubt), and if not, what are counterexamples?
3. Strengthen the point of how the current theoretical understanding can help design learnable CoT schemes that generalize. The empirical examples in the paper are good, but how much did the theoretical understanding contribute? Could it help to come up with a less manual process or procedure to design CoT schemes? How? Currently, the manual decomposition / rewriting of the original problem does all the heavy lifting.
4. The notation in Sec. 3.3 is quite tedious to parse - a figure would really help (probably all of Def. 3.2 could easily be shown graphically).
5. Theorem 3.6 is fine (there always exists a transformer that can solve the CoT problem), but what about learnability (via SGD)? How do we find that transformer in practice? Is that always easy or only sometimes, and if so, when?


**Questions:**

1. What can be said theoretically about the complexity of (n,r) consistent CoT schemes? How does the number of CoT steps scale with problem complexity and problem length (e.g. the CoT scheme for multiplication seems to not scale very well).
2. How would one use the insights from the paper to design reasoning systems that can reason in many settings, or even at LLM / Frontier model scale? Currently the CoT format for each task is very different, and it is unclear that there is any synergy between learning different tasks simultaneously with a single model. The very different CoT schemes may even hurt performance when learning many tasks simultaneously.
3. L 186: Why is it theoretically important that the lengths are the same?
4. How can one in general determine if a problem is (n,r) consistent? Only by finding a valid decomposition (CoT scheme)? How does one find n and r in practice?


**Minor comments:**
1. L 133: “Note that we do not define CoT formally” - this is a weakness for a theory paper and should ideally be fixed.
2. L 136 (Problem statement): The text says “performs well“ which is very informal, whereas the mathematical statement seems to say “performs perfectly in all steps (for any deterministic reasoning problem)”. This discrepancy needs to be fixed - either performing well means always the correct $S^{T+1}$, or there is some other error function that measures how well the model performs. Since this is a theory paper, being precise is important.
3. L 170 says that “with only the continuity bias […] it is almost impossible to predict”. The continuity has never been formulated. I would rather rephrase this to: “without any complexity penalty (such as forms of continuity bias, (n,r) consistency, or forms of Occam’s razor) it is impossible to prefer one continuation over any other, and thus generalizing correctly would rely entirely on chance (with vanishingly small probability as the gap between $N$ and $N’$ grows”.
4. L536-539: I would have liked to see that much earlier in the paper (e.g., around L176).
5. L 251: $s_{j,l}$ and $s_{j,r}$ swapped.
6. L 347: “We use 4 classes” - should be 5.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the problem of generalizing chain-of-thought (CoT) reasoning to arbitrary lengths, which is called Length Generalization (LG). The previous work has only shown the effective generalization of CoT over inputs of the same length. 
The paper first gives a theorem characterizing the root cause of the LG problem - namely there exist infinitely many Lipschitz-continuous extensions of a Lipschitz-continuous function g over N inputs. This implies that LG cannot be achieved in general without some restrictions. It then proves a condition called (n-r) consistency under which LG can be achieved. The paper gives experimental results that show that algorithms for parity, addition, multiplication, and division are learned by transformers with CoT representations that satisfy (n-r)-consistency.

### Strengths
LG is an important problem that demonstrates the power of transformers to learn procedures over inputs of arbitrary size. 

The paper presents a sound theory that characterizes the root cause of the problem and gives a sufficient condition for its solution. 

The experimental results are compelling and illustrate the successes and failures of generalization that depend on the (n,r)-consistency.

### Weaknesses
 The CoT training seems to be quite tedious for complex procedures such as multiplication. 

Typo:Def 3. ... are r-length.

### Questions
How robust is the approach to errors in the steps of the CoT? Can you conduct some experiments to study this and report in the final paper?

### Soundness
3

### Presentation
3

### Contribution
3
