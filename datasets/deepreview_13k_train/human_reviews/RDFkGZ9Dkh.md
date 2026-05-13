# Large Language Models as Markov Chains

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Large language models (LLMs) have proven to be remarkably efficient, both across a wide range of natural language processing tasks and well beyond them. However, a comprehensive theoretical analysis of the origins of their impressive performance remains elusive. In this paper, we approach this challenging task by drawing an equivalence between generic autoregressive language models with vocabulary of size $T$ and context window of size $\cxtsize$ and Markov chains defined on a finite state space of size $\mcal{O}(T^K)$. We derive several surprising findings related to the existence of a stationary distribution of Markov chains that capture the inference power of LLMs, their speed of convergence to it, and the influence of the temperature on the latter. We then prove pre-training and in-context generalization bounds and show how the drawn equivalence allows us to enrich their interpretation. Finally, we illustrate our theoretical guarantees with experiments on several recent LLMs to highlight how they capture the behavior observed in practice.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies the learning theoretical properties of auto-regressive model ( which the author claim to be LLM ) on Markov Chains.
In particular, they prove the convergence of MC and the generalization guarantees of learning the parameter $\Theta$. They also carried out numerical experiments on it.

### Strengths
The strength is the theoretical results look pretty solid. And the author writes this paper in a very clear fashion. making it very readable. Also the results follow from the uniform concentration bound of MCs, presented in a rather classical learning theoretic (a.k.a. VC style) fashion.  I believe this result is relevant to the learning theory community although I cannot decide how much technical innovations are made here. The reviewer believes that this result adapt previous results by many other learning theory researchers who develop theory on estimating the transition kernel of MC given single path observations.

### Weaknesses
The major weakness is the connection to LLMs. The first thing is whether the class F is sufficiently large to include some instances of LLMs. Right now it seems only takes a single input $v_{I}$ instead of $v_{I-1},v_{I-2},\ldots,v_{I-k}$. Though it may not be feasible anymore to learn MC due to the Markovian properties after we make this change.  However, real world language might not be treated as Markovian, which is a very stylized assumption here. The reviewer believes this will affect the impact of this work in the LLM community.

Another huge concern is that $F$ is regardless of the structure of the model itself. It can either be an RNN, Transformer, or a LSTM, and the result continues to hold. It can even be non-NN model. This does not actually reveal why LLM is a powerful machine since it highly depends on the NN as its backbone. Therefore these limitations significantly affect its contribution to the modern LLM theory community.

The reviewer is still not convinced that such function class is specific to Transformers. In particular, this does not fully leverage the attention+MLP structure of the Transformers. Given the definition in line 324, the reviewer believes that ML researchers can actually construct so many models that are not Transformers but still satisfy the conditions given by the LLMs in this work. However these models might be very bad in practice and LLMs won't succeed on them while the theoretical results remain untouched. In particular the reviewer thinks that LSTMs and RNNs do not necessarily take the input as a whole and can perform exactly the same as Transformer here. I also checked the proof and realized that the Transformer architecture is not necessary in the proof either.

The proof idea seems to be quite standard in the literature or the author does not highlight it in the contribution. The reviewer believes that this result adapt previous results by many other learning theory researchers who develop theory on estimating the transition kernel of MC given single path observations.

### Questions
Overall this work is very well written, which is the reason why the reviewer gives a 5 rather than a 3. The reviewer believes that this work is not very relevant to the LLM community but more relevant to the traditional learning theory (a.k.a. VC theory) community (given that the author changes the way this work is presented by replacing most of the LLMs to autoregressive models and maybe draw connections in a milder way).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors first enstablish the equivalence between autoregressive models and first-order Markov chains with number of states proportional to $T^K$, where $T$ is the alphabet size and $K$ is the context window, proving results about the stationary distribution of such chains. In the second part of the paper, the authors prove pre-training and in-context generalization bounds for LLMs, validating them with several experiments.

### Strengths
The paper is well written. I was not able to check all the proofs but the math seems sound to me and the results are interesting.

### Weaknesses
My main concern is that it is not clear to me what is the connection between the first part (equivalence between autoregressive models and Markov chains) and the second part (generalization bounds) of the paper. As it is, the paper looks like two different papers glued together.

I struggle to understand the implication of the results of the first part for LLMs. In particular, what does it mean for LLMs to converge to their stationary distribution? Does that mean that the model's loss has converged to some minima? Does that mean that the LLM inference performance cannot be improved further?

I was curious about the choice of the TV distance in the risk definition (2). Would it be easy to move to some more popular loss choice for LLMs such as the cross-entropy loss? Intuitively, it shouldn't be too hard since cross-entropy loss is basically KL divergence, which in turn is connected to TV distance through Pinsker's inequality.

### Questions
I have a few questions that would make it easier for me to understand the results of the paper and its impact:
1) What is the connection between the first and second part of the paper? Are the results of the first part important for the derivation of the generalization bounds? If so, what are the key steps when the equivalence proved in the first part is useful in the second part? What is the intuition?
2) I struggle to understand the implication of the results of the first part for LLMs. In particular, what does it mean for LLMs to converge to their stationary distribution? Does that mean that the model's loss has converged to some minima? Does that mean that the LLM inference performance cannot be improved further?
3) I was curious about the choice of the TV distance in the risk definition (2). Would it be easy to move to some more popular loss choice for LLMs such as the cross-entropy loss? Intuitively, it shouldn't be too hard since cross-entropy loss is basically KL divergence, which in turn is connected to TV distance through Pinsker's inequality.

### Soundness
3

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
This paper theoretically characterizes the inference mechanism of large language models (LLMs) as a finite-state Markov chain, providing insights into LLM properties based on the transition kernel of the associated Markov chain. Specifically, by modeling an LLM as a Markov chain, the authors show that the output distribution of the LLM converges to a specific stationary distribution and that the convergence rate depends on certain parameters in the LLM. They also derive generalization bounds for the pre-training and in-context learning of LLMs and experimentally verify the behavior of some recent LLMs using these theoretical results.

### Strengths
* This paper introduces a unique approach by modeling LLMs as finite-state Markov chains. This approach provides a clear explanation of the inference process and convergence properties of LLMs to a stationary distribution and also provides a new perspective on understanding LLM behavior theoretically. This approach is expected to expand our understanding of the overall model structure of existing LLM schemes, such as autoregressive models with self-attention mechanisms.
* A major contribution is the derivation of generalization bounds for pre-training and in-context learning, applying the concentration inequality from Markov chain theory to gain a quantitative understanding of LLM's learning characteristics. This increases confidence in the accuracy and inference capabilities of LLMs and is also helpful for comparing different LLMs.

### Weaknesses
 * As noted above, while modeling LLMs as a Markov chain provides a new perspective, there is no new development in Markov chain theory itself. The author's theoretical framework is limited to an extension of existing Markov chain theory, and it remains unclear to what extent this framework fully captures the complex structure and dynamic properties unique to LLMs. Due to the multilayered structure and self-attention mechanisms within LLMs, it is unclear to what extent these can be accurately presented using Markov chains. Specifically, the transition probabilities in an LLM are not fixed but rather depend on the entire history of generated tokens, a feature not typically captured by standard Markov chains where transitions are memoryless. This raises concerns about the validity of applying a standard Markov chain framework to model the dynamic, history-dependent behavior of LLMs.
* The effect of temperature parameters on convergence rate is analyzed, but the influence of other hyperparameters and model structure, such as depth, number of heads, and layer-specific settings, on convergence and inference performance, is not examined in detail. Consequently, the paper provides insufficient guidance for optimal parameter design in LLMs. The analysis focuses primarily on the temperature parameter, while neglecting the impact of crucial architectural choices like the number of attention heads, the dimensionality of the hidden layers, and the specific configurations of the feed-forward networks within each transformer block. These architectural parameters can significantly affect the convergence behavior and overall performance of the LLM, and a comprehensive theoretical treatment should address these factors.
* I believe that Fig.3(d) on line 243 might be a typo for Fig.3(c). Setting that aside, what is the meaning of Fig.3(c)? If the parameter $K$ is only assigned to Llama and GPT, there seems to be no additional information added to Proposition 3.3. Could the authors explain how to evaluate the specific value of $\epsilon$ in LLMs?
* Fig.4(d) presents the temperature dependence of $\epsilon$, but how was this obtained? I may have missed something, but I would appreciate clarification from the authors. It is obvious that convergence is faster at high temperatures, so I am curious about the functional form of $\epsilon(T)$.
* The probability distribution formula on line 327 seems redundant.
* In evaluating the generalization bound, it is assumed that the pre-training data is generated from the Marton coupling. Is this condition essential for obtaining the bound?
* In Fig.5(right), the context length $N_\text{icl}$ dependence of the risk is presented for several values of $t_\text{min}$. While the results for small $N_\text{icl}$ deviate from the scaling law, the theoretical prediction is $\sqrt{t_\text{min}/N_\text{icl}}$. Did the authors attempt to plot the results as a function of $t_\text{min}/N_\text{icl}$ or $N_\text{icl}/t_\text{min}$ to check for a universal curve, indicating a crossover?

### Questions
* I believe that Fig.3(d) on line 243 might be a typo for Fig.3(c). Setting that aside, what is the meaning of Fig.3(c)? If the parameter $K$ is only assigned to Llama and GPT, there seems to be no additional information added to Proposition 3.3. Could the authors explain how to evaluate the specific value of $\epsilon$ in LLMs?

* Fig.4(d) presents the temperature dependence of $\epsilon$, but how was this obtained? I may have missed something, but I would appreciate clarification from the authors. It is obvious that convergence is faster at high temperatures, so I am curious about the functional form of $\epsilon(T)$. 

* The probability distribution formula on line 327 seems redundant.

* In evaluating the generalization bound, it is assumed that the pre-training data is generated from the Marton coupling. Is this condition essential for obtaining the bound?

* In Fig.5(right), the context length $N_\text{icl}$ dependence of the risk is presented for several values of $t_\text{min}$. While the results for small $N_\text{icl}$ deviate from the scaling law, the theoretical prediction is $\sqrt{t_\text{min}/N_\text{icl}}$. Did the authors attempt to plot the results as a function of $t_\text{min}/N_\text{icl}$ or $N_\text{icl}/t_\text{min}$ to check for a universal curve, indicating a crossover?

### Soundness
3

### Presentation
3

### Contribution
3
