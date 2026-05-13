# Emergent Symbol-Like Number Variables in Artificial Neural Networks

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
There is an open question of what types of numeric representations can emerge in neural systems. To what degree do neural networks induce abstract, mutable, slot-like numeric variables, and in what situations do these representations emerge? How do these representations change over the course of learning, and how can we understand the neural implementations in ways that are unified across different models' implementations? In this work, we approach these questions by first training sequence based neural systems using Next Token Prediction (NTP) objectives on numeric tasks. We then seek to understand the neural solutions through the lens of causal abstractions or symbolic algorithms. We use a combination of causal interventions and visualization methods to find that artificial neural models do indeed develop analogs of interchangeable, mutable, latent number variables purely from the NTP objective. We then ask how variations on the tasks and model architectures affect the models' learned solutions to find that these symbol-like numeric representations do not form for every variant of the task, and transformers solve the problem in a notably different way than their recurrent counterparts. We then show how the symbol-like variables change over the course of training to find a strong correlation between the models' task performance and the alignment of their symbol-like representations. Lastly, we show that in all cases, some degree of gradience exists in these neural symbols, highlighting the difficulty of finding simple, interpretable symbolic stories of how neural networks perform numeric tasks. Taken together, our results are consistent with the view that neural networks can approximate interpretable symbolic programs of number cognition, but the particular program they approximate and the extent to which they approximate it can vary widely, depending on the network architecture, training data, extent of training, and network size.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores how transformer models implement a counting algorithm to predict sequences in which a token should be repeated an equal number of times to its occurrences in the prompt. They propose several candidate algorithms: counting up from zero to the target quantity, counting down from the target quantity to zero, and summing 1 or -1 for each token in the context. They analyze the model using Distributed Alignment Search and find that the most aligned algorithm is counting down from the target quantity to zero.

### Strengths
1. The paper furthers the body of work on interpreting how transformers complete mathematical or symbolic tasks

2. The paper is well-written, and the motivation is clearly conveyed

### Weaknesses
Novelty concerns: it does not seem like this paper advances the Pareto frontier of interpretability in transformer models. The task studied is very simple and involves repeating a token the same number of times as it occurred in the prompt, and though the introduction makes an attempt to distinguish it as a special study of symbolism that has not been previously explored, similar analyses exist in a wide range of the literature, on much more complicated tasks than this one.
1. The literature contains extensive study of transformers trained on mathematical tasks, such as modular addition (https://arxiv.org/abs/2301.05217, https://arxiv.org/abs/2306.17844), addition (https://arxiv.org/pdf/2310.13121), induction (https://arxiv.org/abs/2209.11895), relational reasoning (https://arxiv.org/pdf/2310.09753), etc. The cited Feng and Steinhardt paper (https://arxiv.org/pdf/2310.17191) is also a great example. These papers consider tasks more complex than the one considered in this paper, most of which also implicitly involve storing important properties of the prompt and representing numbers in a symbolic way, and in my view it's hard to see how the simple task considered in this paper somehow has properties that reveal a unique capability in transformer reasoning that these papers do not. 
2. These papers also typically contain various methodological insights on how to perform interpretability, or analysis of training dynamics and "how" the models learned good algorithms, and which types of algorithms they are likely to learn, while this paper simply applies DAS, a technique from prior work, and does not contribute any new methods. This paper would benefit from a study of whether their "up-up" or "up-down" is more likely to be learned by a neural network for some systematic reason involving inductive biases, not just for the single network being studied.

### Questions
Do you think there is a reason networks should generally tend to learn the Up-Down algorithm rather than the others?

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
This paper investigates whether neural networks, specifically GRUs, LSTMs, and Transformers, can develop symbol-like number representations through next-token prediction (NTP) tasks. Using numeric equivalence tasks as a foundation, the authors apply causal analysis, notably Distributed Alignment Search (DAS), to explore whether the models’ hidden representations align with symbolic counting behaviors, expressed by 3 hypothetical programs: Up-Down, Up-Up, and Ctx-Distr. Experimental results conclude that RNNs mimic symbolic counting by incrementing or decrementing a variable; Transformers compute context step-by-step without cumulative counter states; and larger models produce less graded alignment than larger ones.

### Strengths
- Novel application of DAS to study the symbolic counting behaviors of RNNs and Transformers
- The experiments present interesting results to verify the hypothesis

### Weaknesses
 - The idea that symbol-like variables can emerge purely from next-token prediction objectives in neural networks is not surprising. Given the success of large language models (LLMs) trained with next-token prediction (NTP), numerous recent studies have empirically and theoretically validated NTP's effectiveness as a universal learning approach for many tasks including numerical reasoning [1,2]. 
- The paper merely highlights the alignment between the hypothesis program and the neural network representations, which does not strongly guarantee that this is the actual program the models follow. Recent research on symbolic emergence in RNNs, including studies on grammatical structures and counting without explicit symbol training, demonstrates that these neural architectures often simulate symbolic programs [3, 4]. Compared to this paper, previous works are more theoretically rigorous. Specifically, the paper does not address the potential for the observed alignment to be a spurious correlation, where the model's internal representations might achieve the same task performance without actually implementing the hypothesized counting mechanism. The analysis lacks a method to distinguish between the model truly implementing the proposed programs versus simply exhibiting behavior that aligns with those programs.
-  Similarly, the paper's findings on the counting capabilities of Transformers are superficial. Recent studies have provided a more comprehensive and systematic analysis of this ability [5], which diminishes the paper's overall contribution. The paper's analysis of Transformers does not delve into the specific mechanisms within the attention layers that enable counting, nor does it explore the role of positional encodings in these computations. A more thorough investigation would involve analyzing the attention weights and hidden states of the Transformer to understand how information is processed and propagated during the counting task.
- The paper focuses solely on a basic counting task, which weakens its broader claim of discovering "symbol-like variables." To substantiate this claim, more complex symbolic tasks should be explored [6]. The current task does not sufficiently demonstrate the generalizability of the discovered representations to more complex scenarios that involve, for example, nested operations or conditional counting. The lack of such exploration limits the impact of the findings and their relevance to more general symbolic reasoning.

### Questions
- In addition to alignment accuracy,  are there other methods to verify that the programs learned by the models are identical to those described in the paper? 
- Numerous alternative programs could assist the model in solving counting tasks (as discussed in [3, 4]),why necessarily Up-down or Ctx-Distr? 
- If theoretical support is lacking, additional experimental evidence through advanced alignment analyses or larger model evaluations would be highly valuable [7].

[7] Wu, Zhengxuan, Atticus Geiger, Thomas Icard, Christopher Potts, and Noah Goodman. "Interpretability at scale: Identifying causal mechanisms in alpaca." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
2

### Presentation
2

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
This paper investigates how neural networks, specifically recurrent networks and Transformer architectures, can generate symbol-like numeric representations purely from the next-token prediction (NTP) objective. The study reveals that recurrent networks tend to align closely with symbolic counting processes, while Transformers approach numeric tasks by recomputing quantities contextually at each step. Additionally, these symbol-like representations exhibit a graded nature and are influenced by task structure and model size.

### Strengths
1. The motivation of the paper is reasonable, and the description is very clear, making the thought process easy to follow. It’s worth mentioning that although I am not familiar with the field of causal abstraction, reading the paper and reviewing the related work allowed me to gain a general understanding of the field and appreciate the contributions of this work, which is commendable.

2. The experimental design appears to be reasonable and thorough. It identifies different characteristics of symbolic program approximation across various model architectures and analyzes the impact of model size and intervention magnitude on IIA.

### Weaknesses
1. As far as I can tell, the DAS interventions only really test within-distribution interventions. Despite some target quantities being held out, these are basically holes within an observed range of integers. Why not see if the model generalizes to numbers outside this range (e.g., 30) and at what value things begin to break down? Also, why not apply DAS for both the count variable and the phase variable in the Up-Down program, and then test to see if the model can be causally manipulated in more interesting ways (e.g., flipping the phase variable several times within the same sequence, even though at training time it only ever flips once and in one direction). These sorts of more aggressive causal interventions are important to understand the degree to which the learned function is symbol-like, since a hallmark of symbolic programs is their systematicity.
2. The explanation of DAS is, in my opinion, not written clearly. I understand that this was not the contribution of the current work, but given its centrality it should be explained with more intuition (including with a figure). If I had not already been familiar with DAS prior to reading this paper, I think a lot of it would have gone over my head.
3. Figure 3 right panel seems not to provide much interesting information, and I would suggest removing this result. It is obvious that increasing model size will increase task performance, and also obvious that all accuracy metrics (including symbolic alignment) should more or less improve over the course of training. Figure 3 left panel seems completely sufficient on its own to show the results of Section 4.2.
4. That the Same-Object task should yield unaligned models seems completely mysterious to me. If anything, I would have expected that models trained on Same-Object would be most aligned among the 3 tasks. Given that this paper is about mechanistic interpretability with respect to symbolic algorithms, I think it is extremely important that the strange behaviour for the Same-Object task, in which no symbolic algorithm is aligned, be explained.
5. Some ungrammatical sentences and typos peppered throughout the text (e.g., line 169, line 190, line 246, etc.) need to be corrected. Please proofread again for clarity.
6. The work lacks a bit of ambition, in my opinion. If one is going to investigate alignment to symbolic programs (which has already been done before in other settings, such as supervised learning), then why not go for more complex tasks which have more complex symbolic algorithmic solutions, with more variables that one could check alignment with respect to? I understand that this was intended as a proof of principle, but honestly the proof of principle in very simple tasks like these seems at once reminiscent of other work I have seen at various conferences, and does not tell me much about whether these sorts of results scale in practice to more complex reasoning tasks. In sum, the results seem to be a bit of a low-hanging fruit, and I would have liked to see a more ambitious project investigating alignment to more complex symbolic programs.

### Questions
Regarding the non-zero dimensions in D: How significantly does this hyperparameter impact the results? 

(PS:I am not familiar with this field, though I have a relatively strong understanding of the paper’s content and personally appreciate it—I believe the clarity of this paper’s description allows even those unfamiliar with the topic to gain valuable insights. However, since I may not have read some of the most relevant related research and cannot assess whether the related work is sufficiently comprehensive, I am not in a position to accurately gauge the contribution level of this work. I trust that the Area Chair will make an appropriate decision.)

### Soundness
3

### Presentation
4

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
The paper investigates the emergence of symbol-like number variables in the representations of sequence models trained on next-token prediction. The task is such that latent number variables are presumably required to solve it in the general case, but such variables are never given as explicit supervision targets and must be learned purely from the next-token prediction task pressure. This means that the findings have particular relevance to, for instance, language models. The methods used to investigate the presence or absence of number variables are taken from causality and mechanistic interpretability. The main finding is that simple RNNs do indeed appear to learn the correct symbol-like number variables on most tasks, albeit in an imperfect way.

My current leaning is to reject the paper, but I am willing to increase my score to a marginal accept if weaknesses 1-5 (along with my questions) are all addressed in the paper or satisfactorily rebutted.

### Strengths
1. The work is, for the most part, easy to follow. I understood the tasks, methods (although seem points below on DAS), and results.
2. The core claims appear to be well-supported.
3. I like the approach of using methods from causality and training using next-token prediction as opposed to more explicit pressure for symbolic number representations. The advantages of these methods are clearly articulated.

### Weaknesses
1. As far as I can tell, the DAS interventions only really test within-distribution interventions. Despite some target quantities being held out, these are basically holes within an observed range of integers. Why not see if the model generalizes to numbers outside this range (e.g., 30) and at what value things begin to break down? Also, why not apply DAS for both the count variable and the phase variable in the Up-Down program, and then test to see if the model can be causally manipulated in more interesting ways (e.g., flipping the phase variable several times within the same sequence, even though at training time it only ever flips once and in one direction). These sorts of more aggressive causal interventions are important to understand the degree to which the learned function is symbol-like, since a hallmark of symbolic programs is their systematicity.
2. The explanation of DAS is, in my opinion, not written clearly. I understand that this was not the contribution of the current work, but given its centrality it should be explained with more intuition (including with a figure). If I had not already been familiar with DAS prior to reading this paper, I think a lot of it would have gone over my head.
3. Figure 3 right panel seems not to provide much interesting information, and I would suggest removing this result. It is obvious that increasing model size will increase task performance, and also obvious that all accuracy metrics (including symbolic alignment) should more or less improve over the course of training. Figure 3 left panel seems completely sufficient on its own to show the results of Section 4.2.
4. That the Same-Object task should yield unaligned models seems completely mysterious to me. If anything, I would have expected that models trained on Same-Object would be most aligned among the 3 tasks. Given that this paper is about mechanistic interpretability with respect to symbolic algorithms, I think it is extremely important that the strange behaviour for the Same-Object task, in which no symbolic algorithm is aligned, be explained.
5. Some ungrammatical sentences and typos peppered throughout the text (e.g., line 169, line 190, line 246, etc.) need to be corrected. Please proofread again for clarity.
6. The work lacks a bit of ambition, in my opinion. If one is going to investigate alignment to symbolic programs (which has already been done before in other settings, such as supervised learning), then why not go for more complex tasks which have more complex symbolic algorithmic solutions, with more variables that one could check alignment with respect to? I understand that this was intended as a proof of principle, but honestly the proof of principle in very simple tasks like these seems at once reminiscent of other work I have seen at various conferences, and does not tell me much about whether these sorts of results scale in practice to more complex reasoning tasks. In sum, the results seem to be a bit of a low-hanging fruit, and I would have liked to see a more ambitious project investigating alignment to more complex symbolic programs.

### Questions
1. On line 140, what is the “Phase variable to track quantity at each step in the sequence”? What does the word “quantity” refer to here? I’m assuming this variable tracks whether the T token has been encountered yet (as for the Up-Down Program), but the sentence is confusing and doesn’t seem to indicate that.
2. Why is DAS in the Transformer case only applied to the hidden states between the two Transformer layers, as opposed to within things like MLP hidden states?
3. Why only investigate the presence of a single program variable? For instance, in the Up-Down Program, why not try to find and causally manipulate the representation of both the count variable and the phase variable (wee “weakness” above)?
4. Regarding Section 4.4, the proposed explanation for why representations of large numbers are less precise implies that task performance should also be worse at these larger numbers. Is there evidence of this? Despite the fact that all models achieve 99.99% accuracy, perhaps you can still check if it is true at earlier points in training.

### Soundness
3

### Presentation
3

### Contribution
2
