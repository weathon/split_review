# Rethinking Addressing in Language Models via Contextualized Equivariant Positional Encoding

- Decision: Reject
- Scores: 5, 8, 3, 8

## Abstract
Transformers rely on both content-based and position-based addressing mechanisms to make predictions, but existing positional encoding techniques often diminish the effectiveness of position-based addressing. Many current methods enforce rigid patterns in attention maps, limiting the ability to model long-range dependencies and adapt to diverse tasks. Additionally, most positional encodings are learned as general biases, lacking the specialization required for different instances within a dataset.
To address this, we propose TAPE: con**T**extualized equivari**A**nt **P**osition **E**mbedding, 
a novel framework that enhances positional embeddings by incorporating sequence content across layers. TAPE introduces dynamic, context-aware positional encodings, overcoming the constraints of traditional fixed patterns. By enforcing permutation and orthogonal equivariance, TAPE ensures the stability of positional encodings during updates, improving robustness and adaptability. Our method can be easily integrated into pre-trained transformers, offering parameter-efficient fine-tuning with minimal overhead.
Extensive experiments shows that TAPE achieves superior performance in language modeling, arithmetic reasoning, and long-context retrieval tasks compared to existing positional embedding techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Increased the score from 3 -> 5 after rebuttal.

====

In the current Transformer architecture, the interaction between positional embedding (PE) and token embedding (TE) is simplistic and favors methods that mainly rely on tokens (e.g. natural language generation) rather than tasks that require positions (e.g. addition). The paper proposes better integration of PE and TE. The proposed method TAPE, updates PE along with TE throughout the layers such that the functions that contextualize PE and TE with respect to each other obey constraints such as permuation invariance and orthogonal equivariance. The main motivation for the method is to improve the stability of PEs during updates. The method shows competitive performance on tasks that require position indexing.

### Strengths
1. The problems with current PE and the related work on PE are explained nicely.
2. The idea of imposing constraints such that updates to PE and TE are permutation invariant and orthogonal equivariant is neat.

### Weaknesses
1. The complexity of the method is not justified. For example, it is not clear why there should be PEs corresponding to blocks of input? And why should the PE be a tensor? The motivation for using block-wise PEs and tensorial representations is not sufficiently explained. The paper should elaborate on the specific benefits of these design choices compared to simpler alternatives, such as using a single vector PE for the entire input or treating PEs as vectors rather than tensors. The lack of clear justification makes it difficult to assess the necessity of the proposed architecture's complexity.
2. The method is motivated in terms of increasing stability of PEs, but there is no empirical evidence presented. The paper lacks many ablations that justify the design decisions of the new architecture. The claim of increased stability needs to be supported by concrete experiments. The paper should include ablations that systematically evaluate the impact of different design choices on PE stability, such as comparing the proposed method with simpler PE update strategies or analyzing the variance of PE updates during training. Without these, the stability claim remains unsubstantiated.
3. The method increases the number of parameters. A fair comparison should be provided for baselines by making sure the number of parameters is same. The increase in parameters should be carefully considered and controlled for in the experimental setup. The paper should either provide a comparison with baselines that have a similar number of parameters or demonstrate that the performance gains are not solely due to the increased model capacity. This is crucial for a fair evaluation of the proposed method's effectiveness.
4. It is unclear if the performance of the proposed method is stronger than existing proposals. For example, based on Figure 2 (caption), it seems to me that the method performs poorly than FIRE.
5. Baselines such as NoPE (no position encoding) and FIRE are missing for experiments (NoPE for Sec 4.1 and 4.2, and FIRE for Sec 4.2).
6. The method is mainly motivated for permutaion invariance but all evaluation is performed with causal models which are permutation variant.

### Questions
1. Is the description of Figure 2 incorrect because it doesn't match the description provided in lines 361--365.
2. Where are the ablation results for design decisions? For example, what happens if you treat PE as a vector instead of tensor, what if the PE is the same for all blocks?
3. Can you visualize attention patterns or some qualitative analysis on where the proposed method shines?
4. The paper mainly motivates that TAPE ensures "stability." What do you mean by that and how do you measure it? Where is the empirical evidence for that?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a new positional embedding method called TAPE, which extends the RoPE positional embedding to be both learnable and context-dependent. Experimental results show that TAPE achieves better performance. Additionally, the authors developed a kernel to reduce TAPE's runtime latency, which could be highly beneficial if released as open-source.

### Strengths
This paper systematically generalizes the RoPE positional embedding. The authors begin by introducing two essential properties that a positional embedding design should satisfy, then propose TAPE to meet these criteria. I especially appreciate the kernel implementation, which significantly reduces TAPE's runtime. I've seen several complex positional embedding designs, and a common drawback is their slow runtime in practice. I'm glad the authors of TAPE have addressed this issue.

### Weaknesses
1. **Illustration of TAPE Method**: It would be highly beneficial if the authors could include an illustration of the TAPE method. Visualizing it with a block diagonal matrix and context-dependent data flow should be feasible and would greatly enhance readers' understanding of TAPE’s operations.

2. **Missing Hyperparameters**: Some important hyperparameters are not specified. For instance, is \( B = L = D = 2 \) used across all experiments? Additionally, details on hyperparameters like learning rate, batch size, and optimizer are missing and should be included.

3. **Potential Error in Figure 2 Caption**: The caption for Figure 2 may contain an error. It states, "The average accuracy across the heatmap is 26.12%, 26.12%, 49.44%, and 41.42% respectively for RoPE, RandPE, FIRE, and TAPE." This appears to contradict line 364, which mentions that "TAPE shows a remarkable 51.9% relative improvement."

4. **Explanation for Improved Arithmetic Task Performance**: More explanation is needed on why TAPE improves performance on arithmetic tasks. Are the authors suggesting that TAPE has inherent advantages in this area?

5. **Clarification on TAPE’s Task Performance**: It’s unclear *how* TAPE improves performance across all reported tasks. Does TAPE enable more flexible attention patterns? Could you, for instance, visualize the \(\phi\) function block by block in equation (6) to provide further insights?

6. **Compatibility of T5 with Flash Attention**: I’m unsure if it's accurate to state that T5 is incompatible with flash attention. While support is currently lacking, compatibility could be achieved with implementation. For instance, see [here](https://github.com/Dao-AILab/flash-attention/pull/956) and [here](https://github.com/Dao-AILab/flash-attention/issues/332).

### Questions
See above. In addition, will the code be released?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new method - TAPE - to incorporate context into positional encodings to enhance model's ability to reason over longer context. Authors propose to 1) extend positional encodings to a multi-dimensional format, by dividing each token into M segments, and assigning  each segment a matrix-form positional embedding. Authors show that RoPE is a special case of TAPE; 2) update positional encodings using attention layers' weights. Experiments on one Arithmetic, four long-context and two language modeling tasks demonstrate that TAPE can outperform the baselines used in the paper.

### Strengths
1. The proposed method of incorporating into positional encodings is novel.
2. TAPE method does not require significant additional computations and can be incorporated into existing models during fine-tuning.
3. Proposed approach shows improvements across several evaluation tasks.

### Weaknesses
Overall, the motivation and design principles are clear. However, the experimental part lacks thorough evaluation, ablation, and explanation, in particular:
1. In Section 3.2 Authors introduce a number of hyperparameters, specific to TAPE. However in 4.1 and 4.2, where models are trained from scratch, authors do not specify how TAPE was initialized. For ex, what are M, B, L, D, B', E, etc? How those where selected and why? In finetuning things are more clear, where TAPE was initialized to align with RoPE , but what's the size of W1/2 (B`) and how it was selected?
3. Authors perform evaluation on selected tasks claiming "superior performance in language modeling, arithmetic reasoning, and long-context retrieval tasks": 
a. Arithmetic learning task: superior performance belongs to Abacus Embeddings (McLeish et al., 2024), that can solve problem with up to 100 operands. Regarding embeddings including in the comparison, I find information in caption and in text confusing: on pictures, FIRE and TAPE look almost identical, your report "The average accuracy across the heatmap is 26.12%, 26.12%, 49.44% and 41.42% respectively for RoPE, RandPE, FIRE and TAPE." - i.e. TAPE performs *worse* than FIRE. But then in the text of Section 4.1 authors claim "Compared to FIRE, which achieves 25.24% ..., TAPE shows a remarkable 51.9% relative improvement." - which seem to contradict the picture.
b. Evaluation on SCROLLS task is further confusing: this benchmark contains 6 datasets, with test partitions kept in private. Authors report performance only on 4 selected datasets out of 6. Not clear what data where actually used for evaluation, and what was the evaluation setup. It's even more surprising to see low scores on QuALITY benchmark, which is multi-choice QA dataset, where random guess achieves 25% accuracy, while the best performance reported is 11.6%. If authors used another evaluation pipeline, it should be thoroughly described in the paper.
c. Finetuning: authors report perplexity on language modeling task, and accuracy on Passkey retrieval, but did not investigate performance on standard reasoning evaluation benchmarks, or even long-context QA reported in section 4.2. With all that, author's claim about "TAPE’s superiority in both arithmetic reasoning and long context language modeling task" is questionable.
4. Performance capability beyond 155M to be explored.
5. Authors did not perform or report any ablations on hyperparameters introduced in the paper, or how those were selected.

It worth noting that tensorial positional encodings idea seems to be very similar to LieRE embeddings, that also introduces multi-dimensional rotation matrix  (Ostmeier, 2024).

Finally, there are multiple typos across section 4 that need to be fixed before publishing (see "Questions" section).

### Questions
1. Why do you think TAPE outperforms other baselines on long-context tasks, especially on QuALITY?

+ See "Weaknesses" section.

Some typos:
Line 311: " inEq. 8" -> " in Eq. 8" (space)
Lines 326-328: "rely absolute" -> rely on absolute;  (Sec. 3.3). ->  (Sec. 4.3).
Line 359: " demonstrate TAPE ’s superior" ->  demonstrate TAPE’s superior (space)
Line 376: "RoPE (Kitaev et al., 2020) ALiBi" -> "RoPE (Kitaev et al., 2020), ALiBi" (comma)
Line 451: "of parameters The" -> "of parameters. The"
Line 479: "Inn con" -> "In con"
Line 483: "Table 4 , the" -> "Table 4, the"
Line 503: " we proposes" ->  we propose

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces TAPE, a novel positional encoding that dynamically adapts to sequence content. By incorporating context-aware encodings across layers, TAPE more effectively captures long-range dependencies. Experiments show its superior performance on long-text tasks.

### Strengths
1. The paper introduces TAPE, a remarkable method that uses contextualized information to update positional encodings.
2. TAPE is a plug-and-play approach that can be seamlessly integrated into common LLMs based on RoPE.
3. Experimental results show that TAPE significantly enhances long-context processing capabilities.
4. The paper is well-written and easy to follow.

Overall, I think this is a valuable work. TAPE effectively integrates positional and semantic information through multiplicative positional encoding to improve model performance. Unlike traditional static encodings or those modified solely by attention scores, this method allows positional encodings to evolve dynamically with layer depth, similar to hidden states.

### Weaknesses
The authors did not remove the empty Appendix section in the template.

### Questions
1. Could the authors provide additional results on length extrapolation (training on short sequences, testing on longer ones) and short-text capabilities, such as MMLU?

2. If an LLM is trained with TAPE, is directly extending the model's context window as challenging as with RoPE? If extending the context window is difficult, are there methods similar to NTK or PI to achieve effective and efficient context window expansion?

3. Could the authors conduct ablation studies on the impact of the Attention and MLP blocks in updating TAPE?

### Soundness
3

### Presentation
3

### Contribution
4
