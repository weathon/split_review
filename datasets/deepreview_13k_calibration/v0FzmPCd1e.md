# Selective Attention Improves Transformer

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Unneeded elements in the attention's context degrade performance.
We introduce \emph{Selective Attention}, a simple parameter-free change to the standard attention mechanism which reduces attention to unneeded elements.
Selective attention improves language modeling performance in a variety of model sizes and context lengths.
For example, a range of transformers trained with the language modeling objective on C4 with selective attention perform equivalently to standard transformers with $\sim$\textbf{2X} more heads and parameters in their attention modules.
Selective attention also allows decreasing the size of the attention's context buffer, leading to meaningful reductions in the memory and compute requirements during inference.
For example, transformers with 100M parameters trained on C4 with context sizes of 512, 1,024, and 2,048 need \textbf{16X}, \textbf{25X}, and \textbf{47X} less memory for their attention module, respectively, 
when equipped with selective attention, as those without selective attention, with the same validation perplexity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a parameter-free modification to the transformer attention mechanism called Selective Attention, which reduces the attention to irrelevant or unneeded tokens in a sequence. This approach enhances performance in language modeling tasks by reducing memory usage and computational costs without compromising model quality. Experiments show that transformers with Selective Attention achieve comparable performance to larger models with traditional attention mechanisms, providing improved efficiency and effectiveness across various model sizes and tasks.

### Strengths
1. **Efficient Memory Management**: The Selective Attention mechanism effectively prunes unneeded tokens, significantly reducing memory usage during inference without degrading model performance. This efficiency gain is particularly valuable for scaling transformers in resource-constrained environments.
2. **No Additional Parameters**: Selective Attention operates without introducing new parameters or significantly increasing computational overhead, which preserves the simplicity of the transformer architecture.
3. **Theoretical Motivation and Experimental Rigor**: The paper provides a thorough theoretical motivation for selective attention, supporting it with extensive experimental results on benchmarks like HellaSwag and C4, which demonstrate the effectiveness of the approach.

### Weaknesses
1. **Limited Scope of Model Architectures**: The experiments are primarily conducted on decoder-only transformer models. Further analysis is needed to verify if Selective Attention can similarly benefit encoder models or encoder-decoder models used in other tasks, such as translation or summarization. The current scope limits the applicability of the method to a subset of transformer architectures, and it is not clear if the same performance gains can be achieved in more complex architectures. For instance, encoder-decoder models often require different attention patterns to effectively capture the relationships between input and output sequences, and it is not clear if the proposed method would be compatible with these requirements.

2. **Potential Over-Reliance on Hyperparameter Tuning**: Selective Attention’s performance may depend on optimal memory budget settings per layer, which could complicate deployment in different tasks or models. Although a memory reduction process is described, further tuning could be required in practical applications. The paper does not provide a clear methodology for determining the optimal memory budget per layer, and it is possible that the performance of the method is highly sensitive to this parameter. This could make it difficult to apply the method to new tasks or datasets without extensive hyperparameter tuning.

3. **Dataset and Task Diversity**: While Selective Attention shows improvements in language modeling tasks, testing it on a wider range of tasks (e.g., text generation or long document understanding) would strengthen the case for its generalizability and adaptability to diverse applications. The current evaluation is limited to language modeling, which may not fully capture the capabilities of the proposed method. It is important to evaluate the method on a wider range of tasks to determine its effectiveness in different scenarios. For example, tasks such as text generation and long document understanding require different types of attention mechanisms, and it is not clear if Selective Attention would be effective in these contexts.

4. **Comparison with Similar Methods**: The paper could benefit from a more detailed comparison with other recent efficient attention mechanisms, such as sparse attention or adaptive attention approaches, to highlight any relative advantages Selective Attention may have. The paper does not provide a clear comparison with other efficient attention mechanisms, which makes it difficult to assess the relative advantages of the proposed method. It is important to compare the method with other approaches to determine its strengths and weaknesses.

### Questions
1. Have you considered evaluating Selective Attention on other architectures, such as encoder or encoder-decoder transformers? If so, could you share any preliminary results or insights?

2. How sensitive is the performance of Selective Attention to the memory budget per layer? Could you offer guidelines on tuning this budget for tasks beyond language modeling?

3. Have you tested Selective Attention on tasks other than language modeling, such as question answering or text summarization? How might the approach handle tasks with varied context and attention needs?

4. Could you provide further comparisons between Selective Attention and other efficient attention methods, such as sparse or linear attention, to clarify the unique advantages of Selective Attention?

5. How does context pruning with Selective Attention affect tasks requiring long-range dependencies? Are certain types of tokens or information more prone to being pruned?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces *Selective Attention*, a parameter-free modification to the standard attention mechanism in transformers which helps reduce the attention given to irrelevant elements in the context. To do so, they introduce a *selection mask* in the attention computation to mask “irrelevant” token, and propose using the previous tokens’ attention on other tokens (on a specific head) as masking for future attention computations. On language modelling on C4, results show that transformers equipped with Selective Attention can achieve comparable performance to standard transformers with twice the attention heads and parameters, and slightly better performance on the downstream task of HellaSwag.

The authors then propose a method that uses the selection mask to prune elements from the attention's context buffer, reducing memory and computational demands during inference, and show that it can lead to significant memory saving (up to 47x for large context sizes) while preserving performance of non-selective attention transformers.

### Strengths
- Given the simplicity of the proposed approach and the reported performance gains, it seems that selective attention could be a significant addition to the transformer architecture if it is further validated.
- Even without the performance gains, the efficiency gains (particularly without having to modify the pretraining loss) are quite relevant and make Selective Attention look like a viable alternative to other efficient attention mechanisms.

### Weaknesses
The main problem of this paper is weak experimental validation. The authors only show gains in the language modelling task (using the relatively noisy and deprecated C4 dataset) and on a single downstream task (where they show smaller gains). They don't compare to existing pretrained models or other efficient attention mechanisms. While the (limited) experimental results are promising, they are not enough to validate the approach. I suggest replicating the recipe of an existing (state-of-the-art) pretrained LLM, replacing the attention mechanism with Selective Attention. Additionally, in the current LLM area, more downstream tasks need to be tested to validate the approach. For the efficiency section, the authors should compare with other efficient attention mechanisms.

The presentation paper could also be better: it uses a whole page for a single figure and further page for intuition, both of which could be much shorter. It then moves decently important plots to the appendix. I suggest restructure the paper to give more space to the experimental results and comparison to other methods.

### Questions
- In the selection attention computation, why use a single head’s logits to mask all heads? Did you try keeping each head separate (i.e. using the logits head i for the selection mask of head i)?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper argues that, for transformer-based language models, selectively attending to a subset of the tokens in the context can improve the model's quality. Motivated by this intuition, the paper proposes a new attention technique, where if a token has already received high attention weights by previous tokens, it means that its content has already been "absorbed" in the model's representations, and therefore it should receive less attention weights onward. The paper proposes an implementation for this idea by reusing the attention logits of one of the attention heads, and thereby adding no additional parameters and only a small amount of computational overhead. Further, the proposed method also allows for pruning some tokens from the context when they will never be attended to again, which leads to memory saving.

Experiments with a 100M transformer based LM trained on the C4 dataset suggests that the proposed approach achieves promising results on language modeling perplexity and one downstream task (HellaSwag).

### Strengths
- The motivation is clear, and the execution of the idea to not to tokens that are already attended to is clever and clean
- The proposed method is easy to implement, adds no parameters, and saves memory overhead
- Interesting results and analysis

### Weaknesses
 - My main concern is about the limited empirical evaluation where only one downstream task is considered. As the paper argues, "different tasks have different requirements," it is crucial to explore whether selective attention is broadly applicable by evaluating it on a diverse set of tasks with different requirements. This can be complemented with synthetic evaluations that might require the model to store the entire sequence, e.g., counting the number of a certain token in a sequence. 
- Besides a more comprehensive evaluation, I also encourage the authors to strengthen their findings by trying selective attention on larger-scale models and datasets

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents selective attention, a method for adjusting the attention weight of tokens based on the amount of attention they received from previous tokens. The authors also propose to use this method to drop some of the history tokens with the lowest (adjusted) weight, also proposing a new loss term to transformer-based LLM training. Extensive experiments show that this method both consistently improves performance, and reduces memory requirements substantially.

### Strengths
- The method is simple and intuitive
- Results are very strong and consistent, showing both accuracy improvements, and very impressive memory reduction
- Experiments are quite extensive
- Given these results, overall I tend to agree with the authors' statement in Section 9: " Given that it adds no new parameters, only a negligible amount of compute, and provides consistent improvements, *selective attention might be a good default for transformer decoders*."

### Weaknesses
While I like this paper a lot, I have several reservations.

First, the level of novelty is not huge. The idea of pruning the least important token in each iteration is similar in spirit to cache-pruning methods such as H20 (Zhang et al., 2023), TOVA (Oren et al., 2024) and others. The authors basically apply a similar approach at training time. While this method works great (as noted above), which is a sufficient contribution on its own, and also present some novel concepts (e.g., the new loss term), it would be better to tone down the novelty claims a bit.

Second, I am not sure I am fully convinced by some of the major claims in the paper.
 
(a) the examples in Section 2 are very appealing, but they are missing a critical baseline: how much attention does the vanilla transformer assign the pruned tokens in such cases? Perhaps it already knows it needs to ignore them? Again, the method works great so obviously something good is happening, but it is not clear the intuition is capturing the essence of it.

(b) similarly, the authors say (#113) "if token b has determined that token a is irrelevant or even misleading to future tokens such as c, there is nothing it can do in the given layer to correct for this.". But I am not sure how their method allows the transfer of such negative signal. If I understand correctly, the authors penalize tokens that received high attention in previous steps (I.e., their value in F is high). I am not sure how information about irrelevant or misleading tokens can be propagated in such cases. Furthermore, if a token is deemed irrelevant and receives no attention, it seems that this information cannot be propagated to future tokens, which is a crucial limitation.

Third, while the writing is generally clear, I found section 3 a bit confusing, requiring several reads to understand a fairly simple method. For instance, it is never explicitly mentioned that each token is penalized by the amount of attention it got from all subsequent tokens. I would also advise the authors to formally define masking, as it is not entirely trivial in this context.

### Questions
The authors mention that they compute the S matrix using "one of the existing heads" (#167). Their code indicates that they simple take the first one. Is this ablated in any way? Does taking a different head / an average of all heads make much difference?

### Soundness
3

### Presentation
3

### Contribution
4
