# Learning to Achieve Goals with Belief State Transformers

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
We introduce the ``Belief State Transformer'', a next-token predictor that takes both a prefix and suffix as inputs, with a novel objective of predicting both the next token for the prefix and the previous token for the suffix. The Belief State Transformer effectively learns to solve challenging problems that conventional forward-only transformers struggle with, in a domain-independent fashion.  Key to this success is learning a compact belief state that captures all relevant information necessary for accurate predictions.
Empirical ablations show that each component of the model is essential in difficult scenarios where standard Transformers fall short. 
For the task of story writing with known prefixes and suffixes, our approach outperforms the Fill-in-the-Middle method for reaching known goals and demonstrates improved performance even when the goals are unknown.   
Altogether, the Belief State Transformer enables more efficient goal-conditioned decoding, better test-time inference, and high-quality text representations on small scale problems.
\begin{comment}
We propose a transformer trained to decode in both forward and backward directions.  This "Belief State Transformer" empirically learns to solve hard problems which more common forward transformers struggle to address in a domain independent fashion.  Analyzing why this is so, we note that transformers are fully capable of representing the solution but discover that certain forward transformer learning problems require learning to solve a parity problem, which is notoriously difficult for gradient-based approaches.  We next show that a successfully learned Belief State Transformer recovers a compact full belief state as input to the output head, unlike other approaches.  This result is therefore maximal: since the belief state contains \textit{all} the information useful in predicting the future, no more complex objective can elicit more information.  We further reinforce this by studying ablations of the Belief State Transformer empirically, finding that all components of the new approach are necessary on problems exposing the weaknesses of a forward transformer as predicted by the theory.  We then experiment with the implications of backward decoding in a small text domain, discovering that it can be used to connect well to a known goal in a manner substantially superior to the "Fill in the Middle" approach at our data scales.  Furthermore, even when a goal is unknown the backward decoder can be effectively used to value and hence select amongst multiple rollouts to amplify performance compared to a forward only approach.  We conclude with an empirical study of the created compact belief state embeddings, discovering that they yield high information  representations which are useful for several purposes.  Altogether, the Belief State Transformer enables a qualitatively more capable reflexive goal conditioned policy, better test time inference, and high quality embeddings which summarize a piece of text.
\end{comment}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper trains a belief state transformer, that learns to predict the next token given the suffix and previous token given the prefix. The training is done jointly on both these objectives. The paper proposes that the training in this fashion can lead to better look-ahead when the goal state is present in the input representation. This is demonstrated with a simple planning task of star graphs where the model needs to choose a correct path to reach the goal state. Results show that this training results in a 100% success, whereas next token prediction results in chance performance. Further evaluation on tinyStories (with prefix) and unconditional generation is also performed showing superior performance.

### Strengths
The paper presents a new form of training that results in better belief state representation learning for LMs. This is shown with the performance on the star graph task where the belief state transformer achieves 100% performance. Similarly, the results on TinyStories also shows that this training regime achieves better LLM-as-Judge scores for completion of stories with prefix and suffix provided.

### Weaknesses
The task StarGraph seems to be very specific to the type of training objective proposed in the paper. The training involves learning the tokens left-to-right and right-to-left which seems aligned to the problem. Specifically, such an solution was mentioned in Bachmann & Nagarajan (2024), where the LM can learn to predict from "right-to-left" starting at the goal and ending in the start state. In order to claim that the proposed training objective results in a better belief state representation in general, would require more evaluations on planning problems like BlocksWorld etc. Specifically, showing the effectiveness on planning problems from benchmarks like PlanBench [1] and ACPBench [2] would make the claim of the paper stronger. 

[1] Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S. and Kambhampati, S., 2024. Planbench: An extensible benchmark for evaluating large language models on planning and reasoning about change. Advances in Neural Information Processing Systems, 36.

[2] Kokel, H., Katz, M., Srinivas, K. and Sohrabi, S., 2024. ACPBench: Reasoning about Action, Change, and Planning. arXiv preprint arXiv:2410.05669.

### Questions
- For the StarGraph experiments, how was the backward latent $B(\emptyset)$ computed? How would the performance change if the training objective had $B$ but during inference $B(\emptyset)$ was not used?
- In the ablation section, what is the difference between `Belief w/o Backward` and single transformer next token prediction setup?
- Was this model trained on any other planning tasks that required look-ahead (for example stacking blocks to reach a goal state) and how did it perform in those cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the Belief States Transformer, a model that predicts the next token for the left context (prefix) and the previous token for the right context (suffix) using two distinct encoders. The authors evaluate the proposed approach on two tasks: finding paths on star-shaped graphs and generating stories using the TinyStories dataset. The results show that the proposed method outperforms models trained only in the left-to-right direction and the Fill-in-the-Middle (FIM) approach, which predicts the next token conditioned on both left and right contexts.

### Strengths
- The paper addresses the important challenge that modern architectures lack planning ahead mechanisms to rely on before generating solutions.
- By predicting both the next token for the left context and the previous token for the right context, the model uses a more complex training scenario with more training signal (O(n^2)) compared to FIM and regular next-token language modeling.
- Despite the more complex training, the model retains the same autoregressive inference mechanism as regular language models, ensuring compatibility with existing model inference scenarios.
- The authors select a set of tasks (path finding on star-shape graphs and story generation) that test models' abilities to make generations that follow certain goals. They show that proposed Belief State Transformers outperform regular next-token prediction models and FIM, indicating the effectiveness of their approach.

### Weaknesses
- Comparison with FIM on Star-Shaped Graphs. The paper does not provide results for the Fill-in-the-Middle (FIM) approach on the star-shaped graph task. Including FIM as a baseline in this task would offer a more comprehensive comparison and help determine whether the improvements are due to the model architecture or the specific training objectives.
- The paper does not discuss whether a backward language model could solve the star-shaped graph task more effectively than a forward LM. Exploring this could provide insights into the benefits of using bidirectional information in the model.
- Models like BERT, trained with a Masked Language Modeling (MLM) objective, consider information from both directions and can be adapted for generation with additional techniques (e.g., refer to “BERT has a Mouth, and It Must Speak: BERT as a Markov Random Field Language Model”) or generate multiple tokens at once. The paper does not compare Belief State Transformer with MLM models, which could highlight the advantages or limitations of the proposed approach.
- Since the star-shaped graph task is stated to be equivalent to parity problems, the authors do not demonstrate the model’s ability to solve parity tasks. Including such experiments would strengthen the claim about the model’s capabilities in handling these types of problems and prove that the proposed approach is superior to regular next-token transformers.
- The paper lacks clarity in description of some results and experiments (refer to questions section).

### Questions
- It is unclear how the model handles unconditional text generation. Specifically, does the generation proceed left-to-right with only the scoring head for the reverse direction, or some other way?
- The term "teacherless" (Fig. 2) might be confusing. Would it be more appropriate to refer to this approach as "multi-token prediction"? Clarifying the terminology could improve the paper’s readability.
- Figure 5, left: It is not clear whether the probe tests the model's ability to predict nodes on the correct path several steps ahead, or nodes that the model would generate an inference (including possible errors). Forward-only model has low scores on star graph tasks, but could it possibly predict its own outputs based on internal state?
- Figure 6: What is meant by “graph description”? What is on the x-axis? It is challenging to interpret the results presented in Figure 6.
- On TinyStories authors use goal-conditioned planning algorithm for inference (Alg.1). Can this algorithm be adapted to FIM?
- The paper does not specify whether FIM was trained on full sequences or if samples were truncated during training. Was FIM trained on full sequences or truncated samples? Could training on incomplete sequences or limitations in generation length impact its ability to generate complete outputs? Could FIM and BST results from Sec 5.2 be improved by setting suffix to “.”, so both models would know that they should end generation with end of sentence.
- There are several aspects that should be made clear for each experiment: is generation done from left-to-right or right-to-left? Are generations scored based on the next-token head, previous-token head, or both?

Related work could mention BERT as a bidirectional model trained with MLM objective and ELMo as one of the first popular language models that incorporated information from two directions.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a new Transformer model architecture capable of both next and previous token prediction. The model leverages two separate auto-regressive Transformer decoders, one processing input sequences forward and the other backward, the outputs of which are concatenated together and fed into the model’s output head to predict each token conditional on its prefix and suffix.  Apart from efficient training, this design enables the model, called Belief State Transformers (BSTs), to effectively learn good representations for token prediction, supports more flexible inference (such as goal-conditioned decoding or backward evaluation),  and demonstrates success on complex tasks, such as star graphs, where conventional next-token-prediction Transformers are known to fall short.  In addition, BSTs also achieve better performance in story-infilling tasks than prior baselines.

### Strengths
- This paper addresses an important problem in improving the non-myopic prediction capabilities of current auto-regressive language models. Although this study is limited to small-scale settings, its design contributes meaningfully to expanding the architectural space of flexible language models.
- The proofs in Section 4 further strengthen the findings and nicely highlight the biases present in modeling non-myopic dependencies across various objectives (namely BSTs, next token prediction, and teacher-less training).
- The probing experiments, as demonstrated in Figure 5, Section 5.4, are particularly interesting, as they effectively showcase the improved quality of learned bidirectional representations.

### Weaknesses
The study lacks experiments on more realistic, large-scale settings or with larger model sizes. For instance, evaluating bidirectional representations in tasks like code infilling could provide more robust insights.

### Questions
1. In Line 269, the footnote mentions “the fact that the forward-only approach does not produce a compact belief state is well known”. Could you clarify what defines a belief state as “compact”?
2. How does FIM perform specifically on star graph tasks?
3. What is the training overhead of BSTs compared to conventional auto-regressive Transformer decoders, particularly in terms of sequence length and batch sizes?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Belief State Transformer, a next-token predictor that leverages both prefix and suffix inputs to enhance prediction capabilities. By learning a compact belief state, the model overcomes the limitations of traditional forward-only transformers, excelling in goal-conditioned tasks such as story writing.

### Strengths
- The idea of learning a compact belief state that captures all relevant information for future predictions is pretty interesting.
- The paper is mostly well written, with controlled experiments and analysis of the proposed method.

### Weaknesses
- The methods and implementations are somewhat confusing, as detailed in the question section.
- There is no analysis regarding scaling AR and the Belief State Transformer. Considering cost issues, it might be possible to examine this on relatively small series models. The concern is whether the forward AR inherently encodes a "belief state" as AR model size increases.

### Questions
- Based on the model parameter details in section C.1, are the forward and backward encoders shared? If so, does this mean that by simultaneously learning the backward objective, the forward encoder obtains some future information, leading to a better representation of $f_t$? Furthermore, would not using a shared encoder cause the model to fail?
- I'm a bit confused about the proof about Theorem 3. Given the proof of Theorem 2, it seems we can also derive a similar proof to show AR also encodes a belief state through forward decomposition. The authors provide a counterexample for AR, but stating that "F(A)=F(B)=(−1,1)” seems unreasonable, as a normal encoder won't produce exactly the same encodings for different inputs.
- Could the authors elaborate more on lines 725-726 and show how the belief state transformer constructs a belief state that corresponds to the {ACA, BCB} distribution?
- Why the belief state transformer performs better than FIM training? Could the authors give some intuitions about this?

### Soundness
3

### Presentation
3

### Contribution
3
