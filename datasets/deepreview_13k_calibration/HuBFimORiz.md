# Global Optimality of In-context Markovian Dynamics Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Transformers have demonstrated impressive capability of in-context learning (ICL): given a sequence of input-output pairs of an unseen task, a trained transformer can make reasonable predictions on query inputs, without fine-tuning its parameters.  
However, existing studies on ICL have mainly focused on linear regression tasks, often with i.i.d. inputs within a prompt.
This paper seeks to unveil the mechanism of ICL for next-token prediction for Markov chains, focusing on the transformer architecture with linear self-attention (LSA). 
More specifically, we derive and interpret the global optimum of the ICL loss landscape:
(1) We provide the closed-form expression of the global minimizer for single-layer LSA trained over random instances of length-2 in-context Markov chains, showing the Markovian data distribution necessitates a denser global minimum structure compared to ICL for linear tasks.
(2) We establish tight bounds for the global minimum of single-layer LSA trained on arbitrary-length Markov chains.
(3) Finally, we prove that multilayer LSA, with parameterization mirroring the global minimizer's structure, performs preconditioned gradient descent for a multi-objective optimization problem over the in-context samples, balancing a squared loss with multiple linear objectives.
We numerically explore ICL for Markov chains using both   simplified transformers and GPT-2-based multilayer nonlinear transformers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper advances the theoretical understanding of in-context learning (ICL) in transformers beyond linear regression with i.i.d. inputs, focusing instead on next-token prediction for Markov chains using linear self-attention (LSA). The authors derive a closed-form solution for the global minimizer of ICL loss for single-layer LSA on length-2 Markov chains, emphasizing the increased structural complexity caused by Markovian dependencies and establishing bounds for arbitrary-length chains. They demonstrate that multilayer LSA models structured like the global minimizer perform preconditioned gradient descent on a multi-objective function.

### Strengths
1. The paper addresses an important problem that holds significant relevance to the community.  
2. The paper is well-written and clearly presented.

### Weaknesses
1. I believe the setting might be somewhat simplistic concerning the broader applicability of this work to the community.
2. Please see questions.

### Questions
1. I am unclear about the exact setting here. In in-context learning for Markov chains (see references a and b), the model essentially reduces to a counting-based estimator, ensuring that it estimates the next token probability for the new Markov chain. In this context, does optimizing equation 8 in the paper imply that the model can estimate the transition probability for any new Markov chain provided? I am unsure if this is true, and if it is, I would like to understand why.

2. Since works like a and b already exist, where the setting aligns more closely with real-world scenarios and the authors demonstrate that transformers can perform in-context learning on Markov chains, I am unsure how beneficial this work is to the larger community. That said, it would be helpful if the authors clarified how their work differs from references a and b, so that the differences are clearer.

3. In equation 10, what does $X_i^*$ represent? Is it simply the i'th entry of $X^*$?

4. In experiment 3.3, can we train the LSA as described in equation 6 and observe the attention maps along with $P$ and $Q$? Additionally, can we train a standard LSA using $W_k$, $W_q$, and $W_v$ as specified in equation 5 and then compare the three scenarios? This includes comparing the standard LSA with query, key, and value components, the LSA with $P$ and $Q$, and the LSA constructed by the authors (as described in equation 9).

5. Would it be possible to visualize the attention maps from the experiments in section 4 and compare them to those in references a and b? Although it may be challenging to match them exactly due to different constructions, this comparison could provide insights into whether training the model with MSE or cross-entropy leads to similar attention maps.

Paper Suggestion:

I think figure - 1 could be potentially improved. It took some time to exactly understand the message being conveyed. 

References:

a) Rajaraman, Nived, et al. "Transformers on markov data: Constant depth suffices." arXiv preprint arXiv:2407.17686 (2024).

b) Nichani, Eshaan, Alex Damian, and Jason D. Lee. "How transformers learn causal structure with gradient descent." arXiv preprint arXiv:2402.14735 (2024).

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
3

### Summary
This work studies In context learning (ICL) of a Linear Self Attention (LSA) Model. In particular, it considers task distributions, where each task is represented by a Markov chain with binary states and the goal is to predict the last state of samples from the Markov chain. The authors address the problem of minimising the ICL loss in Expectation over the task distribution and present an explicit expression for the minimiser in the case of length-2 Markov chains (where for each tasks, the initial states can also not be i.i.d.). For the case of a Markov chain of arbitrary length, they provide lower and upper bounds for the minimum which depend on the minimiser of a strictly convex function, which is the expected loss under a transformation of the parameter of the LSA Model. Furthermore, they show that an LSA model with $l$ layers performs $l$ steps of preconditioned multi-objective gradient descent steps where in addition to the in-context objective it considers other linear objectives. The authors also provide experiments with both LSA and transformer models.

### Strengths
1. The theoretical results seem novel. As the author point out, most of the literature has focused on deterministic input-output mappings, while they consider a specific probabilistic mapping (given by a Markov chain with binary values).
2. The analysis seems sound: I checked mainly the proof of the first  two propositions.

### Weaknesses
1. Clarity (see questions section).
2. Limited scope of the theoretical results. The setup with binary values is quite restrictive. Moreover, Theorem 1 for arbitrary lengths Markov chain only provides bounds to the global minimum whose tightness is unclear.



### Questions
Questions:
1. Can the authors explain why the  lower/upper bounds provided in Theorem 1 are tight? 
2. I found the statement in proposition 3 (and the whole section 3.2) unclear. Is gradient descent the minimiser of the expected loss? Under what assumptions does the proposition hold? 
3. Concerning proposition 3, can the authors provide an intuition or show some empirical consequences of having the other linear objectives?
4. I found the use of the dense/sparse when referring to the global Minimiser in the Markovian and non-Markovian settings unclear before looking at Figure (1). Can you clarify what this means in the introduction? Also, Can you provide some intuition on why the global minima has more terms when applied to markovian data?
5. Can you explain how to pass from Lemma 1 to Proposition 4, even a short paragraph as a proof of proposition 4 would suffice.

Comments:
1. The task column in Table 1 labels this work as addressing next-token prediction. This terminology is also used in other parts of the paper. I found this misleading because the task is still formulated as a supervised regression task that differs from previous work by having a random mapping from input to outputs. Meanwhile, for next token prediction I would expect the examples to be necessarily linked temporally as e.g. In [1] (which might be added as a reference). I suggest the authors to change this terminology and possibly remove that column. 
2. Line 198, LSA is not directly linked to eq 6, which might make reading hard for people unfamiliar with such equation. Consider changing Attn to LSA in eq. 6 and following equations (also not to use the same symbol of Softmax attention in e. (5).).  
3. Square bracket notation, used from equation (11) onwards for indices of vectors, is rather strange and hard to read. I suggest the authors to change it, maybe using a double index.
4. First Experimental section could benefit from an introductory paragraph giving an outline.

Minor:
- Propositions should probably be theorems since they are part of the main contributions of the work.
- Line 135: sampled from usually is followed by a distribution, not by the input and output spaces. Consider using “belong to” instead.
- Line 229: (1) Data -> (a) Data.
- In the definition of c_1 of Proposition 2, j should be replaced by n+1.
- $|\mathcal{S}|$ in evaluation metrics is undefined. Are these still binary values?

[1] Sander, Michael Eli, et al. "How do Transformers Perform In-Context Autoregressive Learning?." Forty-first International Conference on Machine Learning.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates how linear self-attention (LSA) transformers learn in-context from Markov sequence data. For single-layer, single-head LSA and length 2 binary random Markov chains, the global minimum of the loss landscape is derived in closed form. In particular, the minimum is shown to have a denser structure compared to the minimum for ICL of linear regression tasks. A bound for the loss of the global minimum in the case of arbitrary-length Markov chains is also given. For multi-layer transformers, the forward pass is interpreted as preconditioned gradient descent minimizing multiple objectives (involving both squared loss and linear maps). Moreover, the ability of transformer layers to learn Markov chains in context is verified by numerical experiments with GPT-2 blocks.

### Strengths
The studied ICL task of next-token prediction for Markov chains is closely related to N-gram models of language and is a welcome departure from the usual linear regression setting, which has perhaps been overanalyzed despite its considerable simplifications. The paper is overall well-organized and easy to follow. The theoretical results are backed by numerical experiments on practical architectures.

### Weaknesses
Overall, the theoretical contributions feel disjointed, too specific/abstract or not wholly justified, and do not give much insight into the structure of the problem. My reasoning is as follows.
* Propositions 1,2 are very specific computations and do not seem to have any bearing beyond the length 2 binary chain setting. Simply writing down a closed-form expression of the global optimum in the particular 2x2 case does not give any insight into the general problem of ICL of Markov chains. Since many ICL theory papers including the current work assume a very stylized setup (e.g. simplified architecture) I believe it is important to have takeaways that can potentially be generalized. The paper makes an attempt to address this by contrasting the denser structure of the minimum with the sparser structure for ICL of linear regression observed by Ahn et al. (2023), which is a valid point. However, this is not particularly surprising as we have no reason to believe the attention mechanism should become sparse a priori; it is the latter result that is unexpected.
* In a similar vein, the paper claims to analyze the loss landscape of ICL but does not have any results beyond characterizing the global minimum. For example, Zhang et al. (2023) show a global PL condition for ICL of linear regression and are able to conclude that gradient descent finds the global optimum. Can the techniques of this work be extended to obtain implications for optimization dynamics?
* In contrast to the first point, Theorem 1 seems to be too trivial and abstract to be of use. The theorem basically says that if $f=g\circ h$ then $\min f\ge\min g$ and $\min f\le f(x')$ for $x'$ such that $h(x^*)$ close to the minimizer of $g$, which is trivially true in any situation. This by itself is not an issue as it still suggests a potential recipe for obtaining concrete bounds. However, this result is subsequently used only in Example 2 in the Appendix, which currently looks to be incomplete and needs to be fixed: the computations for the projection are missing and no loss bounds are actually obtained. Also, Theorem 1 seems to never use the strict convexity of $\tilde{f}$.
* Even if loss bounds can be obtained using Theorem 1, it is unclear how they relate to Propositions 1,2 which studied the structure of the optimum, as loss values were not evaluated at the optimum or otherwise discussed previously. This needs to be clarified in the paper.
* Proposition 3 assumes a modified sparsity constraint (12) by zeroing out the last row of $Q$, which is different from the actual dense structure observed in Propositions 1,2 for the 2x2 case and similar to the optimum for ICL with linear regression. This is not justified in the paper except to align the dimensions to obtain the construction $R$, and seems to only exist for the sake of deriving another "forward pass = preconditioned GD" result.

### Questions
* Besides the derivation of the optimum, what other properties of the loss landscape can be derived, and can anything be said about the convergence properties of gradient descent on this landscape?
* Propositions 1,2 derive the optimal parameters, while Theorem 1 only gives bounds on the loss value at the optimum; how are these results connected?
* How is the modified sparsity constraint of Proposition 3 justified in view of the dense structure derived in Propositions 1,2?

### Soundness
2

### Presentation
3

### Contribution
1
