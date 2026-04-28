# OrthoRank: Token Selection via Sink Token Orthogonality for Efficient LLM inference

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Attention mechanisms are central to the success of large language models (LLMs), enabling them to capture intricate token dependencies and implicitly assign importance to each token. Recent studies have revealed the sink token, which receives disproportionately high attention despite their limited semantic role. In this paper, we first expand the relationship between the sink token and other tokens, moving beyond attention to explore their similarity in hidden states, considering the layer depth. We observe that as the layers get deeper, the cosine similarity between the normalized hidden states of the sink token and those of other tokens increases, and that the normalized hidden states of the sink token exhibit negligible changes. These imply that other tokens consistently are directed toward the sink token throughout the layers. Next, we propose a dynamic token selection method, called OrthoRank, using these findings to select important tokens. Specifically, in a certain layer, we define token importance by the speed at which the token moves toward the sink token. This is converted into orthogonality with the sink token, meaning that tokens that are more orthogonal to the sink token are assigned greater importance. Finally, through extensive experiments, we demonstrated that our method results in lower perplexity and higher zero-shot accuracy compared to layer pruning methods at the same sparsity ratio with comparable throughput.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper observes the cosine similarity between the hidden states of the sink token and those of other tokens, and finds that after the sink layer, other tokens gradually align towards the sink token. Based on the observation, the paper introduces a novel approach named OrthoRank for dynamic token selection in large language models (LLMs). OrthoRank prioritizes tokens that are more orthogonal to the sink token in hidden state space, hypothesizing that these tokens contribute more valuable information for inference. By focusing computation on these orthogonal tokens and bypassing others, OrthoRank aims to reduce computational costs while maintaining model performance. Experimental results demonstrate OrthoRank’s efficiency, showing improvements in language modeling and zero-shot tasks over traditional layer pruning methods under comparable sparsity levels.

### Strengths
1. The paper provides a fresh perspective on token selection by identifying a relationship between token importance and orthogonality to the sink token.
2. By dynamically selecting only important tokens, OrthoRank effectively reduces the computational load without a significant accuracy drop.

### Weaknesses
1. While the concept of orthogonality is central to the approach, the theoretical justification for why orthogonal tokens are inherently more valuable remains somewhat underexplored. Specifically, the paper lacks a rigorous explanation of why tokens with hidden states orthogonal to the sink token should be prioritized for computation. The observation that these tokens might exhibit faster update rates is not sufficiently substantiated with theoretical analysis or empirical evidence beyond the observed performance gains. A more in-depth exploration of the underlying mechanisms that link orthogonality to token importance is needed.
2. The selective layers are determined by using other layer pruning methods, such as SLEB. This results in a greater degree of inconvenience and computational burden when applying OrthoRank. The reliance on an external method for layer selection introduces an additional hyperparameter tuning step, which could be computationally expensive and less practical for real-world applications. The paper should explore the possibility of integrating layer selection into the OrthoRank framework, or at least provide a more detailed analysis of how the choice of layer selection method impacts the overall performance and efficiency.
3. As the model becomes larger (Llama2-7B -> Llama2-13B -> Llama2-70B), the pattern of cosine similarity between the normalised hidden states of the sink token across layers becomes increasingly disparate. The assumption concluded from the two observations might not be universally applicable. The paper should include a more detailed analysis of how the observed cosine similarity patterns vary across different model sizes and architectures, and discuss the potential limitations of the proposed approach when applied to very large models.

### Questions
1. Why do other tokens gradually align with the sink token after the sink layer?
2. How to understand the grouping phenomenon of the cosine similarity between the hidden states of the sink token?
3. Why does the cosine similarity between the sink token and other tokens decrease drastically after the sink layer? Does the sink layer exhibit consistency across different domains?
4. Why does selecting orthogonal tokens underperform the opposite approach in the final layer in Figure 4?
5. Is the KV cache of the unselected tokens stored during inference?

### Soundness
2

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
This paper first analyzes the relationship between sink tokens and other tokens and finds that 1) the similarity between attention sink tokens and other tokens increases throughout layers and 2) sink tokens remain relatively similar throughout layers. Using this observation, the authors propose a token selection method for attention where tokens that are more orthogonal to the sink tokens are kept and others are discarded. The method is compared to layer pruning methods, and outperforms them on current language models.

### Strengths
1. The  motivation behind a sink-based token selection method is an interesting extension of prior work on defining and characterizing attention sinks. 
2. This method is consistently better than some layer pruning based methods while maintaining a similar throughput in both PPL and zero-shot tasks. 
3. The ablation of random vs orthogonal selection criteria, KV vs no KV tokens, and normalization of the hidden states as input to OrthoRank are helpful in understanding the details of OrthoRank and their effect on performance. In particular, the Random vs Orthogonal and normalization ablations are helpful for understanding the components of the method. The same applies for Table 4 in testing different options to achieve the same sparsity.

### Weaknesses
1. Comparing the top 33% of token selection to the bottom 33% of tokens does not seem like an adequate method for comparing token selection ability in section 3.1. Rather than bottom 33%, a random 33% would be more appropriate for comparison.
2. The derivations in section 3.1 require more motivation for some of the simplifying assumptions made. For example, is there data to support that hidden states have approximately equal norms? How is step 3 computed from 2? The comparison of the cos(sink, hiddens) vs cos(hiddens, hiddens) in Figure 7 in Appendix B do not look clearly different, especially in Llama-2.
3. There are a few places where key reproducibility details are missing. For example, on line 148, where are the 500 sentences from and how are they sampled for this experiment?
4. There is not enough detail about how token selection is implemented during inference to understand how the forward pass is changing as a result of this method. For example, the authors include that KV computations are maintained in this method for the sake of attention, but where do the tokens actually not appear in the computation?

### Questions
1. What do  cosine similarity trends look like between sink tokens and a hiddens state much further out, like 100 or 1000 as opposed to 1-10? The Llama-2 and Mistral-7B context windows are thousands of tokens long, and prompts of length 2048 are used in the experiments, where experimental hidden state indices are 2048+. 
2. In Figure 3, what data are used to compute the similarities? Which token index is used for figure 3c and 3d? Is it an average across multiple tokens indices?
3. How is layer selection performed? Do you test each layer individually with OrthoRank and then keep a top-k?
4. What are the details on your throughput computation?
5. What is the token selection ratio for the results in Table 3/Section 4.3.1? 
6. How is token selection implemented into the forward pass of the transformer? Do the 66% of tokens maintained get smaller after applying OrthoRank again in another downstream layer?

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
3

### Summary
This paper introduces **OrthoRank**, a hidden-state-level pruning algorithm that selects important post-normalization tokens based on the cosine similarity between sink tokens and others. **OrthoRank** leverages the phenomenon of sink tokens, where a small portion of tokens receive a significant portion of attention, and selects tokens based on how fast other tokens are moving to sink tokens. The paper claims that in most cases, **OrthoRank** achieves better performance on perplexity with C4 datasets and higher accuracies on zero-shot tasks on various models, compared to one-shot pruning method shortened LLaMA and iterative layer pruning method SLEB.

### Strengths
1. **OrthoRank** proposes the pruning method at a hidden-state-level and uses an innovative method for token selection based on the orthogonality of tokens to a "sink token." 

2. Unlike existing pruning methods, which typically remove layers or tokens based on static characteristics or require additional training components, **OrthoRank** has a simple but effective algorithmic setup. 

3. The paper is overall well-written and organized with clear math expressions in methodology sections. The motivation behind **OrthoRank** and the logic flow of the design can clearly understood by readers.

### Weaknesses
1. The experiments are limited in terms of model choices and types of experiments. You can consider adding LLaMA-3.1 and evaluate on more tasks from LongBench datasets.

2. The authors didn't discuss advantages and disadvantages of **OrthoRank** compared to other sparse attention mechanisms that also uses token selection to estimate the tokens with the highest attention scores. 

3. The authors didn't include the results for end-to-end or attention efficiency. Given the matrix multiplication used for find cosine similarity, I am concerned about how this will affect the overall latency of the generation.

### Questions
1. How do authors define the attention sink and is the attention sink always the first token? 

2. How can authors conclude that an attention sink is formed given a new model and a new dataset, and what if the attention sink is never formed? 

3. Can authors evaluate the design on LLaMA-3.1 models and experiments covering more tasks using datasets, for example, from LongBench? The Table 2 provides mean scores across multiple datasets and can authors share the results for each individual task?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an algorithm for token-level early exiting during LLM inference. This means that only selected tokens are allowed to continue inference, based on the proposed “OrthoRank” heuristic, at any given layer, while the remaining tokens are decoded early. This is an approach to make LLM inference more efficient, and allow for greater sequence generation throughput. The “Ortho Rank” early exit algorithm selects the top k% of tokens to continue inference based on how orthogonal to the “sink” token, the remaining tokens are decoded early.

### Strengths
1. Paper tackles a timely problem, as LMs are increasing in size and inference is becoming increasingly computationally expensive.
2. Paper investigates LLMs of varying sizes and empirically demonstrates that OrthoRank results in better performance than other early exit approaches in most LMs.
3. Experiments are reasonable for validating that OrthoRank does not significantly harm the model.

### Weaknesses
Since the motivation for the “OrthoRank” algorithm is LLM inference efficiency (while preserving model inference performance), I think the authors should have included more results about how increasing throughput via OrthoRank effects model perplexity as one increases sparsity. I know in table 1, they provide a result for 10% and 20% sparsity, but it would be interesting to provide results for [10,20,30,40,50,60] % sparsity and show if/where the critical threshold for balancing sparsity and preserving model performance lies (with the speed tradeoff).

Figure captions need to be more specific. The authors do describe the experiments in the text, but it would be nice to provide further clarity directly in the captions so that readers who are doing a faster skim of the paper can quickly gain understanding of the experiment. For example, in the caption of table 2, I would specify which tasks you are reporting the mean accuracies of.

Writing could be made more clear. Further, there are some typos (i.e., intro paragraph 3, “outperforms” not “outperform”; page 4 last line “As the layers deepen” not “As the layer deepens”).

### Questions
The experiments in table 1 report results for a fixed sequence length of 2048. I am curious as to how the quality of sequence generation holds up as OrthoRank is applied to longer sequences?

Can you pair OrthoRank with further model fine-tuning to further mitigate the loss model performance (e.g., accuracy on zero shot tasks, perplexity)? If this was done, I would expect authors to report how computationally expensive the one-time fine tuning in comparison to the increased model throughput for long sequence generation.

### Soundness
3

### Presentation
2

### Contribution
3
