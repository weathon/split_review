# Round and Round We Go! What makes Rotary Positional Encodings useful?

- Decision: Accept
- Scores: 8, 5, 8, 5, 5

## Abstract
Positional Encodings (PEs) are a critical component of Transformer-based Large Language Models (LLMs), providing the attention mechanism with important sequence-position information. One of the most popular types of encoding used today in LLMs are Rotary Positional Encodings (RoPE), that rotate the queries and keys based on their relative distance. A common belief is that RoPE is useful because it helps to decay token dependency as relative distance increases. In this work, we argue that this is unlikely to be the core reason. We study the internals of a trained Gemma 7B model to understand how RoPE is being used at a mechanical level. We find that Gemma learns to use RoPE to construct robust `positional' attention patterns by exploiting the highest frequencies. We also find that, in general, Gemma greatly prefers to use the lowest frequencies of RoPE, which we suspect are used to carry semantic information. We mathematically prove interesting behaviours of RoPE and conduct experiments to verify our findings, proposing a modification of RoPE that fixes some highlighted issues and improves performance. We believe that this work represents an interesting step in better understanding PEs in LLMs, which we believe holds crucial value for scaling LLMs to large sizes and context lengths.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper delves into the role of Position Embedding (PE) in LLMs, challenging the traditional view that RoPE primarily attenuates attention weights as the relative distance between words increases. It proposes a new hypothesis that RoPE constructs position-attention patterns (e.g., diagonal or previous-token focus) using high-frequency components while leveraging low frequencies to convey semantic information. Several case studies and theoretical analyses support this hypothesis.

Overall, the paper provides insightful findings and hypotheses on a key component of LLMs: position encoding. However, the arguments mainly rely on case studies with gemma-7B, and the experiments lack diversity in the foundation models (e.g., missing LLaMA series) and tasks (e.g., language model vs. QA vs. code...). Additionally, some parts of the proofs contain errors.

### Strengths
1. This paper successfully challenges, both theoretically and empirically, the traditional view that RoPE attenuates attention weights as relative distance between tokens increases. 
2. The authors' hypothesis about the roles of the high-frequency and low-frequency components of RoPE is novel and insightful.

### Weaknesses
1. The experimental validation lacks diversity in both foundation models and datasets.
2. Some perspectives and proofs regarding NoPE contain errors, while they don't affect the main conclusion, they may mislead readers.
3. The discussion of related work is insufficiently thorough, and few papers are cited (only about one page).
4. Throughout Section 4, the authors conceal a core assumption: that attention scores are interpretable or meaningful. Higher attention scores for certain tokens imply a meaningful preference in the model, giving special significance to the larger norms in Equation at Line 257. I want to point out that this assumption is still being debated, and I suggest that the authors make it explicit.
> Is Attention Explanation? An Introduction to the Debate (Bibal et al., ACL 2022)

### Questions
1. In practice, do the phenomena observed on gemma-7b apply to other LLM backbones, such as llama-2 or llama-3?
2. The phenomena observed in this paper are based on what scale and type of data? Could the findings be validated across various tasks, such as language modeling, code, or QA?
3. In Line 190, the authors claim that NoPE has strong OOD capabilities, but Kazemnejad et al., 2024 only validated this for sequences of length up to 50, where NoPE performed slightly better than other PEs, without exhibiting exceptionally strong OOD performance (refer to their Figure 3). The following works explored NoPE's extrapolation, and it can be seen that the generalization ability of the NoPE baseline is limited:
> Length Generalization of Causal Transformers without Position Encoding (Wang et al., Findings 2024)
> 
> [Neurips24 spotlight] Exploring Context Window of Large Language Models via Decomposed Positional Vectors
4. In Line 497, the authors state, "p-RoPE is in spirit similar to the idea of increasing the wavelength of RoPE from 10,000 to 500,000," so I suggest that Table 2 should include RoPE with a base of 500,000.
5. How do the observations in Section 4 change across different RoPE variations, such as 0.25-RoPE, 0.75-RoPE, RoPE_10000, and RoPE_500000? For example, in Figure 3, how does the norm distribution of low frequencies vary across these models?
6. In Line 726, this proof only applies to the first layer of NoPE’s attention heads. Starting from the second layer, the assumption 
$a_{3,3}=<q_3, k_3>=<q_3, k_2>=a_{3,2}$ 
no longer holds.
7. Attention heads with specific patterns have been widely studied. Besides the patterns discussed in this paper (e.g., diagonal or previous-token focus), could the authors observe and analyze other representative attention patterns, such as special token focus, punctuation focus, and locality focus? Please refer to typical patterns in the following paper:
> [ICLR24] Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs

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
This paper investigates the role of Rotary Positional Encodings (RoPE) in Transformer-based Large Language Models (LLMs). The authors challenge the common belief that RoPE's usefulness comes from its ability to decay token dependency with increasing relative distance. Instead, they explore how different frequencies in RoPE are utilized, particularly within the Gemma 7B model. The paper provides both theoretical and empirical analyses, proposes a modified RoPE, and highlights the importance of understanding positional encodings for scaling LLMs.

### Strengths
1. The paper provides a fresh perspective on RoPE, questioning existing assumptions and offering new explanations for its effectiveness.
2. The authors present mathematical proofs to support their claims, enhancing the credibility of their findings.
3. The use of the Gemma 7B model for empirical analysis adds practical relevance to the theoretical insights.

### Weaknesses
1. Although the observed phenomena and mathematical proofs can support the paper's point of view, the experimental performance does not seem good enough. The paper hopes to adapt to any context length, but the actual experimental results only have one result on 8K. And the evaluation of PPL is not comprehensive enough.
2. At the semantic level, the results of the models in Table 2 should be compared on the general benchmark or other tasks that are more representative of semantics, which will be more convincing.
3. At the positional level, it should be compared with similar experiments such as needle in a haystack or Ruler on long contexts to prove its long context expansion ability.
4. I have some doubts about the display of Figure 2. Normally, for the same qk, different relative distances should have a gradually decreasing effect. But does different qk introduce different variables, making the comparison unfair?
5. The author's description of semantics and position in Table 1 is not experimentally verified.

### Questions
1. I have some doubts about the display of Figure 2. Normally, for the same qk, different relative distances should have a gradually decreasing effect. But does different qk introduce different variables, making the comparison unfair?
2. Is there any empirical experiment on how many frequencies are cut off for the best effect?
3. Will removing low-frequency RoPE make the effect on short text worse?

### Soundness
2

### Presentation
3

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
Authors explore how transformer models use RoPE frequencies to learn semantic and positional information. Authors provide a theoretical proof that RoPE does not force the decay in attention coefficient with distance, but instead can create specific patterns. In their experimental study of the Gemma 7B model, authors show that transformers mostly rely on low frequencies, while some heads display high frequency bands, mostly in 1st and last layers of the model. Authors further show that high-frequencies in RoPE provide a mechanism to encode positional information. Low frequencies are used as information channels that are not robust over long context. Finally, authors propose p-RoPE encoding that cuts low frequencies and can help to improve model's performance.

### Strengths
- The authors conduct a novel theoretical and empirical study of RoPE encodings in transformer models.
- They provide detailed proofs of their main claims.
- The paper is clear and well-written.
- This study can help researchers better understand the underlying mechanisms of popular transformer architectures and encourage research into alternative improved solutions.

### Weaknesses
 - The empirical study is limited to a single Gemma architecture. While this is unlikely, some results may be artifacts of the specific model selected. The analysis would benefit from a more diverse set of model architectures to ensure the findings generalize beyond the specifics of the Gemma model. For example, models with different attention mechanisms or varying numbers of layers could reveal whether the observed patterns are consistent across different transformer implementations.
- In Section 3 authors train 2B model and show improvements on validation perplexity. While these results are positive, perplexity improvements do not always results in overall improvements in model's abilities. Authors could provide evaluation results on popular benchmarks* to build more convincing picture. The perplexity metric, while useful for assessing language modeling performance, does not directly translate to downstream task performance. Therefore, it is crucial to evaluate the proposed p-RoPE encoding on a variety of tasks, such as question answering, text classification, or summarization, to provide a more comprehensive understanding of its effectiveness.

* see, for ex, Section 2.3 in https://arxiv.org/pdf/2307.09288

### Questions
1. Pre-training model from scratch is expensive and not always feasible. I was wondering if you can instead continuously train other (Gemma-7B, Llama-3 1/3/8B, etc) models for fewer steps but with p-RoPE approach? Do you think it would work or no and why?

2. Please, correct me if I'm wrong, but in the proof of Proposition 3.1:
for k>1, g_k=theta^{-2(k-1)/d} is not necessarily rational, but algebraic. Therefore, Lemma A.1 should be stated not for rational g, but for algebraic g, and it should use the fact that pi is transcendental.
line 680, cos(j-i-r) -> cos(j-i+r)
line 680, the comma in the displayed equation should be a period.
line 684, cos(j-i-r) -> cos(j-i+r)

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides practical insights into positional encoding for decoder-only models. However, further investigation is needed to establish the effectiveness and reliability of the theories presented.

### Strengths
Pros:

1. The paper offers a fresh discovery of Rotary Positional Encoding (RoPE), challenging the belief that it primarily helps decay attention coefficients with distance.

2. The paper gives an analysis of high and low RoPE frequencies, their roles in positional and semantic attention, and an innovative RoPE modification (p-RoPE) that demonstrates improvements in some cases.

3. Every section has a summary part which makes the whole paper clear and ready to read.

### Weaknesses
Cons:

1.  The figures in the paper are somewhat confusing. For instance, while the paper emphasizes frequency aspects, Figure 1 illustrates vectors with identical frequency differences, which does not fully align with the paper’s focus. Additionally, the results are primarily presented using heat maps, which may appear monotonous and lack of expressiveness. Given that this is a language modeling task, presenting some results in natural language format would enhance readability and interpretability.

2.  (MAIN LIMITATION) The experiments are limited to decoder-only models, making it unclear whether the findings can generalize to other transformer architectures. Whether the observed improvements stem from specific model structures (e.g., encoder-only or encoder-decoder models) rather than from a comprehensive enhancement applicable to diverse positional encodings of transformer. Additionally, the authors did not consider the impact of long-range dependencies or how the choice of positional encoding influences masked attention performance of decoder-only model. It would be valuable if the authors could report comparative results using unmasked attention (e.g., with encoder-only transformers) to examine these effects.

3.  (MAIN LIMITATION) The proposed modification p-RoPE appears to primarily integrate elements of RoPE and NoPE, which may lack novelty. While the study advances understanding of RoPE, its applicability to other positional encoding methods, such as Alibi, remains limited, potentially constraining its relevance for models with alternative encoding schemes. The authors should consider incorporating other positional encoding methods and propose more innovative improvements to enhance the usage of lower and higher frequencies.

4.  The paper states that higher frequencies correspond to positional attention, while lower frequencies correspond to semantic attention. However, the authors provide an ablation study only for the lower frequencies, without addressing both low and high frequencies. This aspect is insufficiently explained in the ablation experiments.

### Questions
Why did the authors provide an ablation study only for the lower frequencies rather than for both low and high frequencies?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studied the inner workings of rotary positional embedding. The authors started by challenging the common belief that RoPE decays with distance. Then, the authors showed in Gemma 7B that most RoPE usages appear in low frequencies. The authors explained that high frequencies are for positional information while low frequencies are for semantic information. Finally, the authors observed that the low-frequency components are not robust. Based on this observation, the authors proposed p-RoPE to remove (1-p)*100% of the low-frequency component and showed that this improved the performance of Gemma 2B models.

### Strengths
* The paper is well-written and the key points are delivered clearly.
* The authors made a good point that RoPE doesn't necessarily decay with distance.
* The figures clearly showed that most attentions happen in low frequencies, and some high-frequency heads and frequency bands exist.

### Weaknesses
 * The claim that high-frequency components are for positional information is unclear.
  - The reasoning seems to be: (a) RoPE can learn a diagonal or off-diagonal pattern. (b) NoPE cannot learn a diagonal or off-diagonal pattern. So RoPE can learn positional information. However, it doesn't necessarily mean the high-frequency components contribute to the diagonal/off-diagonal pattern. So the function of high-frequency components remains unclear. It is possible that the ability of RoPE to learn these patterns is due to the overall structure of the embedding and not specifically the high-frequency components. A more detailed analysis is needed to isolate the contribution of high frequencies.
  - Some prior works provide evidence that NoPE can still encode positional information [1][2]. So the fact that NoPE cannot learn a diagonal or off-diagonal pattern may not imply it cannot encode positions. The argument that RoPE is more efficient at encoding positional information is not sufficiently supported by the current analysis.
* The authors experimentally show that truncating the lowest frequencies can help RoPE learn better. However, it is based on a claim that "RoPE lacks robust semantic channels". 
  - This claim comes from an analysis on a 2-dimensional case. However, it is possible that the 2D case is too restrictive and a higher dimensional case could have a different result. The analysis should be extended to higher dimensions to ensure the claim holds true in more realistic scenarios. The current analysis does not provide sufficient evidence that the 2D case is representative of the higher-dimensional embeddings used in practice.

### Questions
* Is your p-RoPE having a similar flavor as the partial rotary?
  - Partial rotary means the whole dimension is divided into rotary part and non-rotary part. The rotary part will be treated by RoPE while the non-rotary part is treated by NoPE.
  - Partial rotary embedding has been known by the community for a while (see https://github.com/lucidrains/x-transformers/issues/40). It is known that the partial rotary is slightly better than rotary positional embedding.
  - Because the proposed p-RoPE is interpolating between NoPE (p=0) and RoPE (p=1), it is possible that p-RoPE is similar to partial rotary.

### Soundness
3

### Presentation
3

### Contribution
2
