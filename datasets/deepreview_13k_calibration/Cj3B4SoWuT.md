# Latte: Latent Attention for Linear Time Transformers

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 5, 1

## Abstract
The time complexity of the standard attention mechanism in transformers scales quadratically with sequence length. We propose a probabilistic framework for attention, enabling us to derive a novel low-rank linear re-parameterisation of both bidirectional and causal cases, based on defining a latent variable model. Our method can be seamlessly integrated as a drop-in replacement for the standard attention mechanism. Additionally, this framework provides a natural extension for combining local standard attention with our global linear attention. This approach allows us to extend the context length of existing large pre-trained models with only a few additional training steps. The resulting ``Latte Transformer'' achieves performance comparable to standard attention and other state-of-the-art models, while maintaining linear time and memory complexity, along with constant-time next-token prediction during inference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to alleviate the well-known problem of Transformers -- quadratic complexity. The main idea of this paper is instead of storing all KV cache, it adopts a fixed number $L$ of latent tokens with the goal of embedding global information into the fixed number of states. By having a fixed number of the latent tokens, it has a fixed computational complexity that's independent of input sequence lengths. The authors also present an efficient causal update mechanism which is significantly important during inference. Finally, by adding additional techniques such as sliding window attention and RG-LRU, the proposed module shows competitive performance comparing to the vanilla self attention while maintaining efficiency.

### Strengths
The paper is very easy to follow and the derivation of its bidirectional and causal forms is succinct. It also shows various connections to many different previous works such as Vanilla attention, SSMs, Linear attention, and etc. By cleverly reformulating the algorithm, the module can be adapted to the causal setting, which is significantly important lately due to auto regressive training. The paper demonstrates its competitiveness in diverse settings.

### Weaknesses
- Dependence on SWA and LRU. Compared to recent SSMs like Mamba, it doesn't have a clear advantage given that it is dependent of other methods and slower inference.
- While the authors mention that the implementations of Luna and Latte differ substantially, it is unclear how they are fundamentally different. Without the additional techniques that Latte integrates such as SWA and LRU, it is uncertain whether Latte clearly has substantial performance-wise benefits over Luna. If so, why is there a mathematical reason?
- Although the causal variant is efficient during inference, parallel training requires Jax framework, which again hinders independence of this method from other settings.
- For a fair comparison, I believe previous models that can be used as a counterpart of Latte should be reevalated by replacing Latte with those models and have other components like SWA++ and RG-LRU the same.

typo:
- line 69 : $\sum^T$ to $\sum^t$

### Questions
- Are the runtime results for transformers measured using FlashAttention [A]?
- The sequence extrapolation is very interesting, but I wonder if it is mainly due to sliding window attention. Does Latte itself also extrapolates well?

[A] Dao et al. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a linear complexity attention mechanism for sequence modeling. The central concept involves processing the Q and K matrices with the softmax operation independently. Additionally, the paper explores mixed attention through sliding window attention, demonstrating enhanced performance in language modeling. Experimental results on both language modeling and LRA tasks indicate competitive performance. The paper also presents distillation results using pre-trained models.

### Strengths
The paper is well-written.

### Weaknesses
1. The concept is quite similar to Efficient Attention: Attention with Linear Complexity. Although the author clarifies the differences, such as from vision tasks to language modeling and latent variable interpretation, I believe the novelty is still limited. First, vision tasks are a 2D sequence modeling problem, which is more complex than a 1D language modeling problem. Second, the latent variable interpretation treats the Q and K matrices as attention matrices, which seems a bit strange to me. The interpretation lacks a clear justification for why the Q and K matrices, when independently processed with softmax, should represent meaningful latent states or token clusters. The connection between the mathematical operation and the proposed interpretation is not sufficiently established, making the claim of latent variable representation speculative.

2. There is a significant lack of linear models for comparison in this context. For instance, models such as HGRN (NeurIPS), HGRN2 (COLM), Lightning Attention (ICML), and GLA (ICML) are missing. Additionally, it is well-known that linear models may perform well on a small scale but often fail to scale effectively. The experiments conducted with 150 million parameters are insufficient to validate the actual scaling capabilities of the proposed method. Furthermore, the distillation results do not provide evidence of these scaling capabilities. The distillation experiment uses a relatively small base model, and the improvement observed might not be indicative of the method's performance when applied to much larger models. The absence of experiments with larger models makes it difficult to assess the true scaling potential of the proposed approach.

3. Is the standard causal attention implemented with flash attention or not for the speed comparison? If not, the comparison results are not helpful. Also I would suggest include sota linear attention variants for comparison as well. The lack of clarity regarding the implementation of standard causal attention makes it difficult to interpret the speed comparison results. Without knowing whether flash attention was used, the comparison is potentially misleading. Furthermore, the absence of comparisons with state-of-the-art linear attention variants makes it difficult to assess the relative performance of the proposed method.

4. It is well known that the limitation of linear models is their retrieval capability. The paper lacks experiments on "Needle in a Haystack" to demonstrate its performance on long sequence modeling. The absence of "Needle in a Haystack" experiments is a significant oversight, as it is a standard benchmark for evaluating the retrieval capabilities of sequence models, especially in long-sequence contexts. This omission makes it difficult to assess the practical utility of the proposed method in scenarios requiring precise information retrieval from long sequences.

### Questions
As above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose Latte, a sub-quadratic attention alternative based on a low-rank re-parameterization – a latent state is defined, and input tokens attend to this latent to break the quadratic dependence on sequence length. Additionally, a hybrid model that combines local standard attention and Latte is proposed to improve local processing.  

For language modeling, small-scale pre-training experiments on 8B tokens of OpenWebText are conducted, and the proposed attention alternatives are compared to other attention variants in terms of test perplexity.  In addition, the model is compared to other efficient attention ops on Long Range Arena (LRA), and up-training experiments to extend Gemma 2.6B by replacing attention with Latte-Macchiato  are conducted.

### Strengths
- Though many linear attention variants have been proposed over the past two years, the approach in this paper appears novel
- It compares favorably on small-scale PPL and reasonably on LRA evaluations compared to other recent proposals
- The Latte operation is well-motivated and clearly derived
- The experimental transparency on hyperparams, training code and experimental details is commendable

### Weaknesses
The primary weakness of this paper is the experimental evaluation -- it is unclear from the experiments in this paper the extent to which the results would extend to natural-language and long-context evaluations.  A number of prior works (T2R [1], Hedgehog [2] and SUPRA [3] which are missing in the discussion in Section 4.5) take pre-trained vanilla attention Transformers and fine-tune / adapt them to linear and efficient alternatives.  The findings in the SUPRA study [3] show that there are gaps between efficient attention models and standard attention for long-context tasks.  Thus proper comparisons on natural language evaluations (Hellaswag, ARC, etc.) and long-context (Scrolls [4]) tasks would illuminate the strength of Latte/Latte-Macchiato vs standard attention.

Others:
- In Figure 6, is the context length for vanilla attention Gemma extended using the YaRN [5] trick? Since there is a standard fine-tuning free approach that is now commonly used when context length exceeds pre-training context, it should be used for fair comparison with vanilla attention

### Questions
Larger-scale experiments to fully validate Latte/Latte-Machiatto compared to vanilla attention may be expensive, but the finetuning experiments already conducted in Section 4.5 may be suggestive of natural language performance.

At the 2.6B scale there should be signal in terms of standard natural language and long context evaluations -- running the trained Gemma-Macchiato on the standard harness of natural language (Hellaswag, MMLU, etc.) and natural language long-context evaluations (Qasper, NarrativeQA, etc.) would go a long way toward verifying that performance is maintained with the base model at short context, and improves at long context tasks.  It may also be interesting to conduct these experiments with the other proposed Latte variants.

Especially interesting would be results of these experiments on MMLU, where linear attention variants have struggled (as in SURPA [3] above, where the gap between the base and linearized models are small on Hellaswag but very large on MMLU).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The attention mechanism used in transformers has a time scaling of $O(N^2)$, where $N$ is the number of tokens. The reason for this quadratic scaling is due to the fact that the dot product between the query and keys is calculated for each pair of tokens when calculating softmax. The authors claim the presence of latent variables and show that by utilizing latent variables, they can approximate the softmax in $O(NL)$ time, where $L$ is the number of latent variables. They further improve their work by adding a sliding window attention, which calculates the original attention with respect to the neighboring tokens for each token. They evaluate their work by comparing the forward pass time against original attention, and the expressivity against original attention and a number of other transformers that have a timescaling of $O(N)$.

### Strengths
- The idea of replacing softmax$(QK^T)$ with softmax$(Q)$softmax$(K)^T$  is novel and has potential. However, the overall process is clustering (see weaknesses for more details).
- Including the literal code as an appendix is a good practice.

### Weaknesses
 - The idea of replacing softmax$(QK^T)$ with softmax$(Q)$softmax$(K)^T$  is novel and has potential. However, the overall process is clustering (see weaknesses for more details).
- Including the literal code as an appendix is a good practice.

 - "Latent Variable" is a very specific term used to describe the presence of a hidden variable that has a causal effect on the observed variables. The vectors you define as latent variable, $l$, are learnt so that the result of Equation 7 optimizes your objective function. In other words, the actual value of $l$ is determined by the specific values of the queries and keys, which themselves are derived by passing the tokens through a neural network. This makes the causal graph to be $x$ -> $(q,k)$ -> $l$. What your algorithm is doing is to perform a clustering with centers $l$ with respect to some objective.

- Regardless of the notion of transformers, if you are claiming the presence of a "latent variable", you need to perform proper causal inference techniques to prove your claim.

- Assuming the existence of latent variables, you should explain what these latent variables are supposed to represent. You should provide some intuition on why a hidden variable would be present, and what it might be. Otherwise, how could you argue about it's existence?

- The assumption of independence of $s$ from $t$ given $l$ in Definition 1 is not valid. The $s$ and $t$ are iterating over the same set of tokens. Each token $x$ directly affects the probabilities as written in Equation 6. Since they share a parent, they are correlated and not independent.

- Since the main motivation behind the design is improved time and memory complexity, the comparisons should've been made with FlashAttention [1]. Given that FlashAttention is calculating the softmax-based attention (regular attention) in an efficient manner, and is prevalent (arguably more prevalent the standard attention), it is not fair to compare your time and memory with the standard implementation of attention.

- In Equation 13, you're double counting the attention score for the nearby tokens of each token. Once through the sliding window and once by the Latte mechanism. This would: 1. over-emphasize on nearby tokens by assigning a higher score and 2. cause the sum of scores to be higher than $1$, voiding the mechanism of being a valid attention.

- In summary the overall idea has potential, but the math explaining why their method works is not sound. I encourage the authors to rewrite their paper with a clustering point of view, and include a time and memory comparison against FlashAttention and at least one of the other linear cost attentions.

### Questions
- How dose "Latte Macchiato" compare with a transformer using just the sliding window attention? Specifically, a sliding window with a size of 128.

- Is the number of latent variables a hyper parameter, or is there a specific reason to choose them? i.e. does it scale with the input sequence length? Also, what is the number of latent variables in your experiments.

- In Figure 4, your forward pass scales sub-linearly with $N$. In fact it's almost constant. Why is the forward pass time not affected by the input sequence length?

- In Figure 7, you have mentioned that a benefit of Latte over other attentions with linear complexity is not collapsing. Could you elaborate what that means and why it would be troublesome. If collapsing is a well known phenomena you should add a citation.

### Soundness
1

### Presentation
4

### Contribution
1
