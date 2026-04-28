# Contextual Position Encoding: Learning to Count What’s Important

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
The attention mechanism is a critical component of Large Language Models (LLMs) that allows  tokens in a sequence to interact with each other, but is \textit{order-invariant}.
Incorporating position encoding (PE) makes it possible to address by position,
such as attending to the $i$-th token.
However, current PE methods use token counts to derive position, and thus cannot generalize to higher levels of abstraction, such as attending to the $i$-th sentence.
\if 0
The attention mechanism is a critical component of Large Language Models (LLMs) that allows  tokens in a sequence to interact with each other.
Since %the attention operation is order-invariant,
attention is order-invariant,
position encoding (PE) makes it possible to address by position, such as attending to the $i$-th token.
However, current PE methods use token count to derive position, and thus cannot generalize to higher levels of abstraction, such as attending to the $i$-th sentence.
\fi
In this paper, we propose a new position encoding method, 
\emph{\oursfull{}} (\ours{}), that allows positions to be conditioned on context by incrementing position  only on certain tokens determined by the model.
This allows more general position addressing such as attending to  the $i$-th particular word, noun, or sentence.
We %empirically 
show that \ours{} can solve the selective copy, counting and Flip-Flop tasks  where popular position embeddings fail, and improves perplexity on language modeling and coding tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies word and sentence counting problems for transformer-based language models. The authors observe that transformers require position encodings (PE) to access to a specific word or sentence. They further argue that existing PE methods are context-independent, which leads to limitations in word and sentence counting problems.  Therefore, the authors suggest a new PE method, CoPE, to integrate context and position addressing together. CoPE shares the idea of relative PE but replaces the second term with a learnable vector called contextual position.

To verify the method, the authors conduct experiments on counting problems, long-context problems, language modeling, and code modeling. The experimental results provide evidence to support CoPE.

### Strengths
1. Counting is a challenge for models so the research problem is significant. 
2. It is interesting to address the problem from the angle of position encodings.
3. Experiments are solid.

### Weaknesses
1. The major concern is the novelty. The learnable vector or contextual position is based on the idea of position interpolation and fractional positional encoding explored in Insert Transformer, particularly in [1]
2. Experimental settings are not transparent and consistent.  For example, Table 2 considers Absolute PE and RoPE as baselines, while Tables 3,4 and 5 consider other baselines. I do not see any particular consideration in changing the baseline.
3. There is one unclear point. The authors add CoPE to the model for several layers, while baseline methods are only considered for the input. Is this a factor to affect the final results?
4. In Table 7, LLMs can be prompted to explain counting. It is interesting to show a similar result from CoPE. Therefore, we might understand that LLMs with CoPE can "understand" counting tasks instead of guessing a good number.
5. Minor points for presentations:
    - Word count and word index are not exchangeable in some contexts. It is better to make this more concise. For example, in the abstract "However, current PE methods use token counts to derive position," I suppose this should be "token index" instead of "token count"
    - Visualizations should be consistent. The style of Figure 5 is different from others.

### Questions
1. Refers to Weakness.
2. Have you tried your pretrained model for language understanding task?

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
4

### Summary
This paper extends transformers with relative position encodings that can count intervening events. For each query position i and key/value position j, each intervening position k computes a gate value g_{ik} between 0 and 1, and the relative position encoding from i to j depends on the sum of the intervening gate values.

The new encoding, called CoPE, strongly outperforms absolute PEs and RoPE on some synthetic tasks. CoPE+RoPE outperforms RoPE alone on counting words, and improves perplexity on several language modeling tasks.

### Strengths
The idea of adding gates and position encodings that count gate values instead of positions is very nice, and seems to be effective at least for the tasks attempted.

### Weaknesses
The mapping from a count (p_{ij}) to an embedding (eq. 5) is fine, but the rounding to the nearest integer count seems a little complicated, and learning different embeddings for every integer count adds a lot of parameters and imposes a maximum count. What would be wrong with treating p_{ij} as an angle and converting it to a vector using a sinusoidal encoding? It seems worthwhile to compare this simpler scheme with eq. 5.

Perplexity doesn't seem like the best way to measure language model performance any more; a benchmark like MMLU would have been much more convincing.

In Table 5, why is only CoPE+RoPE tested? Does CoPE alone not perform well? Even if so, the results should be reported.

### Questions
In Table 5, why is only CoPE+RoPE tested? Does CoPE alone not perform well? Even if so, the results should be reported.

### Soundness
3

### Presentation
3

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
This paper proposes a new position encoding method,  CoPE, which enhances the attention mechanism in LLMs by allowing position conditioning based on context, thereby enabling more nuanced interactions such as attending to specific words, nouns, or sentences, and outperforming existing position embeddings in various tasks.

### Strengths
1. The paper identifies a novel issue within the PE component of current LLMs and presents insights that could inspire future research directions.  
2. The writing is clear, and effective, and conveys the paper's main arguments.

### Weaknesses
1. A core issue here is whether the series of problems currently described are truly caused by PE.  
2. The analysis in Table 1 attributes the problems to the current PE, but the analysis is insufficient and may be due to the inadequate reasoning abilities of LLMs. Specifically, the analysis does not sufficiently rule out the possibility that the observed issues stem from the models' inability to properly parse and understand complex contextual relationships, rather than a fundamental limitation of the position encoding itself. 
3. One problem with this work is that it requires extensive training; perhaps optimizing during the reasoning phase could resolve these issues (as mentioned in Table 1). The paper does not explore or discuss potential alternative approaches that might mitigate the identified issues through more efficient means, such as targeted fine-tuning or prompt engineering strategies, which could potentially reduce the need for extensive retraining of the entire model. 
4. Since this work is general, the experiments on generality (Table 12) should not only compare RoPE with RoPE+CoPE but also display the performance of CoPE alone. The absence of a direct comparison with CoPE alone makes it difficult to isolate the specific contribution of the proposed method and assess its standalone effectiveness. 
5. The content in lines 32 to 36 of the Introduction is somewhat redundant and could be moved to the related work or background section.

### Questions
1. Why emphasize OOD in the experiment? For PE, does improved OOD indicate better generalizability and extensibility of the method? 
2. Could you provide examples of correct outputs from the experiments in Table 7? This would allow us to better understand the output patterns of LLMs on this task, thereby gaining insights into issues related to PE.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study presents a position-encoding (PE) method that is context-dependent. The authors use token similarities to calculate a score for each pair of tokens in the sequence. In simple terms, this score represents how many times the query token (or a token very similar to the query token) is seen until now in the sequence. The authors argue that the proposed way of counting allows the capturing of various abstractions in a given sequence, such as token, sentence, paragraph, section etc. With multiple experiments, the authors show the effectiveness of the proposed method CoPE, especially in tasks where counting of words is important.

### Strengths
- The study presents a very unique way of modeling positions for the transformer-based language models

- The authors show the advantages of the proposed methods on multiple tasks such as flip-flop, symbolic counting, word counting, language modeling, and common benchmarks.

### Weaknesses
 - Scalability: The presented method is a parameterized method of encoding positions. The authors mention that to control the number of added parameters one could control the value of p_max (line 227). However, the effect of limiting p_max on performance is unclear, especially for longer sequences (say >10k tokens). Secondly, for CoPE one would need to write ‘qk’ dot product and hence cannot use the sub-quadratic attention methods such as flash attention and ring attention. This is a crucial limiting point because sub-quadratic attention has been a key for scaling transformer LLMs to process longer sequences. Furthermore, if one is not able to use flash/ring-attention for training the model then naturally resorting to shorter sequences is a practical solution. This brings me to the last scalability issue. Interpolation and extrapolation methods have been published in the literature to effectively take an LLM trained on shorter sequences to extend the capabilities to longer sequences. However, how these methods can adapt to parameterized PE methods is a challenging question. The authors show in Section 5.5 (figure 3) that the model trained on a sequence length of 512 can have reducing PPL values until the context reaches 2.5k tokens. It is then critical to see how long this pattern stays stable. Or if the authors could present some analysis regarding the relationship between p_max and extension limit for different model sizes, that’d be helpful for the readers. 

 - It is also crucial to report cost analysis, including the additional time and memory required by the CoPE method compared to RoPE (with and without flash attn), in order to compare the methods fairly. This will give readers and practitioners a clear idea of the required compute investment for better performance.

 - PE for different levels of abstraction: The authors' primary argument concerns a feature of positional encodings (PE): that the PE method should be able to differentiate between a token and a sentence (i.e. different levels of abstraction). In other words, the counting of basic units of the text sequences must happen at different paces for different levels of abstraction e.g., counting should be faster for tokens than the sentences. This, I believe, is indeed one feature of the RoPE. RoPE operates on d//2 subspaces and each subspace counts positions (rotation angle) at a different pace. Hence, we can loosely argue that subspace-1 counts tokens and subspace-2 counts sentences, likewise, in a non-discrete fashion. If this is true and both RoPE and CoPE are doing the differential counting then my main concern is that the difference in the results may primarily be due to the difference in the number of parameters between the two. It would be helpful if the authors could show that this is untrue. 

 - The details regarding experiments are often missing (see below in the questions). Figure 5 and other figures in the appendix are difficult to read.

### Questions
Line 41-42: This position variance increases …: Can authors please cite the reference for the sentence length statistic?

Line 251: Experiments
Which GPUs? How much memory?
What are the p_max values for different experiments? The value seems to be reported only for the language modeling experiments. 
How is the test error calculated, non-exact match?

Flip-flop task:
Line 864: Table 8 in Appendix: OOD performance of CoPE across different architectures is worse than RoPE. This is further impacted if CoPE parameters are only added for 1st layer. How do the authors explain this variability in the performance? 

Mean (STD): 
RoPE: 17.59 (4.99)
CoPE: 17.90 (9.69)

Symbolic counting
Line 324: Table 3/4: Why RoPE is not included in this comparison? Can authors also report the standard deviation values for tables 3 and 4?

Word counting task 
Line 367: Is it the full fine-tuning or some lighter fine-tuning like LoRA?
Line 371: The reported performance of Llama-3.1-70B is with or without fine-tuning? If it is without fine-tuning then please report how many shots were used? 

Language modeling
Why did the authors choose to train for 100 epochs? For pre-training phase, it is generally 1 epoch or some upsampling of the data (x2-4).
Line 378: Table 6: Why RoPE is not reported for the Wikitext experiment?
Line 378: Table 6: Are embedding parameters included in the reported parameters in both tables?
Line 428: context length extension is conducted on the models pre-trained in section 5.5?
Line 452: The capping idea is similar to the Alibi-style context length extension. Is there any specific reason why Alibi (or PI/Yarn) was not selected for comparison in this experiment? 
Line 918: Please consider improving Figure 6. It is very difficult to read.
Line 945: Does Table 9 report non-embedding parameters only? Why changing the p_max value does not have any effect on the number of parameters?

Large language modeling
What was the pre-training context length?

### Soundness
2

### Presentation
2

### Contribution
2
