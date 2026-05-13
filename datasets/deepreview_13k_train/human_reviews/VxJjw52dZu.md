# LION: A bidirectional framework that trains like a Transformer and infers like an RNN

- Decision: Reject
- Scores: 3, 5, 3, 8

## Abstract
We introduce LION, a novel sequence-to-sequence framework that unifies the bidirectionality and parallelized training of Transformers with the fast inference of recurrent neural networks. LION is built upon a mathematical formulation where full kernelized attention with a learnable mask is efficiently computed using a bidirectional selective recurrent model, matching the effectiveness of softmax-based attention with constant-time inference. Our framework naturally accounts for spatial and temporal relationships within input sequences, reducing reliance on heuristic positional embeddings and facilitating straightforward scalability in context length and resolution. Using our framework and inspired by the recent state-space models, we propose three main running examples LIOn-LIT, LION-RETNET, and LION-S, a transformer with selective mask and recurrent inference. Numerical evaluations on tasks such as language modeling, the Long-Range Arena, and image classification show that LION framework achieves performance on par with state-of-the-art models while delivering fast training and inference efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents *LION*, a bidirectional sequence modeling framework based on State Space-like Models (SSMs) such as Linear Attention and Mamba. Supplementing the standard parallel vectorized implementation, LION enables output computation through two recurrences, designed to preserve output fidelity with the parallelized approach. The main contributions are as follows:

1. Design linear recurrences that correspond to Linear Attention (LA) aka LION-LIT
2. Add Mamba's selectivity to those recurrences aka LION-S. 
3. Empirically test the model on the LRA task, GLUE, and image classification
4. The resulting model does not require position embeddings and can be extrapolated beyond the training length.

### Strengths
1. The paper is very well written and quite illustrative which makes it an easy read. 
2. The goals and the methodology proposed in the paper are easy to understand.
3. The paper shows that bidirectional linear attention (and its selective variant) can be written in a recurrent form.

### Weaknesses
 **1: Recurrence Form of Linear Attention is a straightforward extension**  
The claim that Linear Attention (LA) can be expressed as a recurrence seems like a straightforward calculation, given it is already known that causal LA can be written as a recurrence. To extend this to bidirectional settings, the numerator is simply a forward recurrence, $\sum_{j \leq i} q_i^Tk_j$, combined with a backward recurrence, $\sum_{j \geq i} q_i^Tk_j$, and a correction term $-q_i^Tk_j$ to account for double-counting. The same approach works with the denominator. While this is mathematically valid, the recurrence structure derived here seems like a straightforward extension of known results.


**2: LION's Continuous-Domain Selectivity is derived in Mamba**

The continuous selectivity mechanism in LION seems to be derived in Mamba’s formulation (see Eq. (4) in [1]). Mamba originally derived this expression into the form used here and then simplified it, i.e. they start with $\mathbf{\bar{B}} = (\Delta \mathbf{A})^{-1} (\exp(\Delta \mathbf{A}) - \mathbf{I}) \Delta \mathbf{B}$, and drop $(\Delta \mathbf{A})^{-1} (\exp(\Delta \mathbf{A}) - \mathbf{I})$ to simplify the term and notice no drop in performance. LION chooses the $\mathbf{A}$ matrix as identity which reduces the above expression to LION's (27a)


**3: No Position Encodings required is a consequence of using SSMs**  
The claim that this model achieves independence from position encoding and can hence be extrapolated to longer sequences is a standard characteristic of all State Space Models, which implicitly capture positional information through recurrence. This has been recognized and documented within the community (see [GitHub issue #29](https://github.com/state-spaces/mamba/issues/29)). I feel that is not a contribution of LION but SSMs at large.

**4: Practicality of Recurrent Inference**

I am unsure where the recurrence form in the paper may have practical utility. For language modeling using recurrence makes imminent sense because it helps in streaming out the output data to the user in real time. However, in case of bidirectional modeling the parallel implementation already achieves $O(L)$ space and time complexity which is the same as LION

The only limited application I can see this being used is if the memory constraints are such that we have $O(L)$ memory but the constant is probably not big enough, then instead of computing it in a purely recurrent fashion which would be very slow, it is standard practice in SSMs to processes input in chunks, using:
  - **Input:** [SSM's State, subset of contiguous tokens]
  - **Output:** [Updated SSM's State, corresponding output tokens]

 Each chunk can be computed using the parallel form under available memory without needing to fully unroll the recurrence which would be very slow on GPUs. I would like to note that the above approach is well-established in the SSM community.

**5: Experimental Validity Concerns**

- **GLUE Scores:** The reported GLUE scores seem low; prior works using selective recurrences and adding them without correction factors at 70M parameters has been shown to yield a GLUE score of 80.6 which is higher than LION's 78.5. (See [2])
  
- **Vision Task Comparisons:** In the vision tasks, the authors only compare their model with ViT-small, which was originally designed for distillation purposes. Training a 22M model directly for vision tasks is impractical; comparisons with a larger model, such as ViT-base (86M parameters), would be more convincing and relevant.

### Questions
N/A - see weaknesses

### Soundness
3

### Presentation
4

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
They show that applying two linear attention mechanisms in two directions would not be equivalent to an bidirectional Transformer. Hence, they propose to scale masked linear attention in a different way to make it more similar to birectional full attention. Furthermore, they propose LION-S that combines LION with the selective mechanism of SSMs.

### Strengths
1. They try to find an equivalent recurrence for the scaled attention, which is more accurate than linear attention.
2. The visualization of upper/lower triangular matrix is helpful.

### Weaknesses
1. Some equations/notations are not clear enough. For example, in Eq 6 and 7, it looks like equations A1/A2 are without masks while B1 and B2 are with masks, but this is not explained, and lambda is not defined. The lack of clarity around the masking in these equations makes it difficult to understand the precise mathematical operations being performed. Specifically, it is unclear how the mask is applied and whether it is element-wise or in some other manner. The definition of lambda is also crucial since it appears to be a scaling factor, and its precise mathematical definition is necessary for reproducibility and understanding.
2. LION-Lit performs worse than BERT or ViT, and the gap is not negligible. If LION is equivalent to full attention, the difference should not be that large. The performance gap between LION-Lit and established models like BERT and ViT raises questions about the practical effectiveness of the proposed method. If the core claim is that LION is equivalent to full attention, then the observed performance difference suggests that this equivalence may not hold in practice, or that there are other factors that significantly impact performance. The magnitude of the gap is concerning, as it indicates that LION-Lit might not be a viable replacement for these models in practical applications.
3. The advantage of adding selectivity is not well explained. Table 2 only shows LION-S results, but it does not compare it with LION. The lack of a direct comparison between LION-S and LION makes it difficult to assess the actual benefit of adding the selectivity mechanism. Without this comparison, it is unclear whether the performance improvements are due to the selectivity or other factors. The absence of a baseline makes it hard to determine the true value of the proposed modification.
4. The definitions of the architectural elements of figure 1 should be added to its caption. The lack of definitions for the architectural elements in Figure 1 makes it difficult for readers to understand the proposed model architecture. Without clear definitions, the reader is left to guess the function of each component, which hinders comprehension and reproducibility.

### Questions
1. Is this method limited to bidirectional models? Most generative models are not bidirectional. How does it apply to single-directional models?
2. Other than the theoretical improvement in complexity, how much is the improvement in reduction in latency, computation FLOPs, etc? Figure 3 only shows GPU memory for image classification. How does GPU memory change on language tasks?

### Soundness
2

### Presentation
3

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
LION a bidirectional sequence-to-sequence framework that casts attention (Transformers) as RNNs. 
The authors propose LION-S, a model which combines LION with Selective SSMs. 
LION-S achieves competitive performance with state-of-the-art vision and masked language transformer models while being more resource efficient.

### Strengths
The paper's illustrations and equations are written in a way that makes it easier to understand. The colour coding is a nice touch.

### Weaknesses
The paper proposes LION emphasizing that the framework casts bidirectional Transformers as bidirectional RNNs. 
The paper then introduces LION-S (a model based on state-space models) and focuses on comparisons with Transformers showing efficiency gains and substantial performance improvements. However, this is misleading since the framework LION and LION-S can be viewed simply as SSMs.

By viewing LION as simply SSMs, the claimed benefits of their proposed transformers are not surprising and are common in prior SSMs. For example, (1) "does not require any additional positional encoding, enabling it to extrapolate beyond the context length or resolution during inference.". (2) competitive performance and significantly more efficient than transformers. (3) Solving the Long Range Arena (LRA) task.

More concretely, consider Theorem 3.3 $y_i$'s numerator and denominator:
$$ 
	 y_i^F + y_i^B = q_i^T (S_i^F + S_i^B - k_i v_i)
$$
$$ 
	 c_i^F + c_i^B = q_i^T (z_i^F + z_i^B - k_i)
$$
$S^F, S^B, z^F, z^B$ are simply SSMs. Both $(S^F, z^F)$ and $(S^B, z^B)$ are computable with forward and backward parallel scans respectively. 
Essentially the numerator is two SSMs (1 forward and 1 backward) summed together ensuring bidirectionality. The denominator is also two SSMs summed together.

As a result, several experimental results are misleading. LION-S is grouped with "Transformer as Linear Recurrent Model" but it's essentially sums of SSMs with scaling. Viewing it as such, LION-S's similar performance to S4 and S5 is not surprising. Furthermore, its efficiency gains over Transformers are not surprising either. 
Notably, Figure 3 (right) efficiency gains are normal since it's essentially comparing SSMs with a Transformer. A more fair comparison in terms of performance efficiency would be to compare with Vision SSM models such as Vision Mamba.

Some other concerns I have are as follows:
 -  In Table 2, S5 results are worse than S4, and Mamba results are very poor compared to S4 and S5. However, one would expect Mamba and S5 to outperform S4 as these methods improved upon S4. It is very surprising to see Mamba perform so poorly and S5's performance significantly worse than what is reported in the original paper. Justification for these results is needed. 
 - The paper mentions "Transformers can be represented as SSMs," citing the Mamba-2 paper => This statement is imprecise. The Mamba-2 paper mentions in its footnote: "Technically speaking, these connections only relate to certain flavors of attention." The original Transformer (using Softmax) cannot be represented with a single SSM as it does not have a linear relationship. 
 - LION-LIT results are missing from Table 2.
 - LSTM and GRU are described in Table 1 as having bidirectionality. These methods are not bidirectional by default unless stacked in different directions. With a similar logic, the various modern RNNs such as linear transformers and state-space models are also bidirectional by stacking them in different directions. This has already been done in several works such as the S5 paper for their experiments. 
 - The paper mentions "SSMs often fall short in tasks requiring dense information processing". This is due to their bottleneck due to also being viewable as an RNN. The way the introduction is framed suggests to me that since LION is based on Transformers, it won't have this issue. However, LION should also have this issue since they are also viewable as RNNs (and are essentially being SSMs in different directions summed together).

### Questions
The paper focuses on LION-S as the main contributing method. However, to my understanding, LION-S would use the parallel scan algorithm. However, Figure (1) middle illustrates a matrix formulation during training instead. Could you clarify this? 

Long Range Arena's Text dataset is described with an input length of 2048 in Table 2, but in previous papers such as in "S5", the dataset is described with an input length of 4096. Could you clarify if it is indeed different?

Are 27a and 27b coefficients supposed to be $\exp(a_i)$ and $(1 - \exp(a_i))$ instead of $\exp(a_i)$ and $(\exp(a_i) - 1)$? Since $\exp(a_i) = \exp(\log(\sigma(w^T_a x_i + b))) = \sigma(w^T_a x_i + b)$, we have the sum of the two coefficients summing to $1$, ensuring an attention mask. If not, it's not clear to me why the second coefficient would be $(\exp(a_i) - 1)$.

Considering the similarities between LION(-S) with SSMs, what are the conceptual and practical differences compared with existing SSM approaches? In addition, what is the practical benefit of using LION(-S) over these SSMs?

Considering the poor performances of S5 and Mamba, could you explain these discrepancies and provide details on their implementation or experimental setup?

Could you include LION-LIT results or explain why they were omitted in Table 2?

Since the paper labels LSTMs and GRUs as bidirectional when they are traditionally unidirectional, could you include the definition of bidirectionality used in the paper and how it applies consistently across the different models in the table?

### Soundness
2

### Presentation
2

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
This paper introduces LION, a novel sequence-to-sequence framework that combines the bidirectionality and parallelized training of Transformers with fast inference of recurrent neural networks. 
More specifically this paper at first shows how Linear Attention and Gated Linear attention variants (including Selective State Space Models, such as Mamba-2) can be reformulated as bi-directional RNNs, such that they can use a parallel masked matrix multiply formulation (e.g. Y=scale(QK^T * M) V ) for training similar to transformers while still using the recurrent formulation for inference.

Then, the paper proposes LION-S a novel Gated or Selective Linear Attention variant with a specific parameterization gate or selectivity parameter inspired by zero-order hold discretization and LION-LIT a bi-directional non-gated Linear Attention variant, where the selectivity parameter is set to 1. 

Through extensive experiments on the Long Range Arena Benchmark, Masked-Language Modeling, Image classification and Causal-Language Modeling the paper demonstrates that their proposed recurrences LION-S and LION-LIT achieve competitive performance to state of the art Transformer and State Space Models.

### Strengths
This paper does an exceptionally good job in presenting the complex formulas and transformations in a very readable and understandable way. It also provides a very good overview of related work and provides lots of insights in relations between those works. 
Their experiments are very extensive and the paper also provides careful ablation studies on different design decisions of their LION-S recurrence (e.g. Table 6, Table 7). The authors also provide inference efficiency experiments in the appendix.

I enjoyed reading this paper and believe that it is a good contribution, therefore I recommend to accept this paper and hope the authors can clarify the questions and unclarities below:

### Weaknesses
 - There are only minor weaknesses such that the Causal Language Modeling and Vision experiments are rather small scale. Nevertheless, the paper demonstrates with these experiments the effectiveness of LION-S also on these compute-intense domains.

- The connection to the continuous domain of LION-S is rather loose and could be elaborated on further.

- It seems that the paper often uses the terms “attention”, “attention mechanism”, “full-attention” or “attention-formulas” interchangeably, which makes it sometimes hard for reader to disambiguate from the context whether softmax-attention, linear attention or causal (linear) attention is meant (e.g. L. 187, or L. 923). It would improve the readability if the terminology is unified in the paper. 

- L. 190 The terminology forward / backward path might be misleading, as the term backward path is usually used for computing the derivatives / delta errors. I would suggest to clarify this distinction at some point or rather use forward / backward recurrence always.
Out of curiosity: Why is it called LION?

- In Table 8, you apply a Non-linearity (elu) to q and k in addition to the LION-S mask. What is the default for LION-S? Only Mask and no non-linearity or mask and non-linearity?

- In equation 85, 88 and 101 is there the mask M missing?

- The exponential gating in the mLSTM (xLSTM) requires a stabilizer (or “max”) state in addition to S and z. See (eq. 15, 16, 17 and  74, 75, 80 in [2]). This is not explicitly addressed in 94 to 96, but the LION bidirectional reformulation should still be applicable.

- Have you tried using just the forward recurrence of LION-S, but reverse the order of the input sequence in consecutive blocks as it was done for example in “Vision-LSTM” [1] ? It would be interesting how this compares to the forward/backward LION-S. The same experiment could be also applicable to masked language modeling in Section 5.2.

### Questions
- It seems that the paper often uses the terms “attention”, “attention mechanism”, “full-attention” or “attention-formulas” interchangeably, which makes it sometimes hard for reader to disambiguate from the context whether softmax-attention, linear attention or causal (linear) attention is meant (e.g. L. 187, or L. 923). It would improve the readability if the terminology is unified in the paper. 

- L. 190 The terminology forward / backward path might be misleading, as the term backward path is usually used for computing the derivatives / delta errors. I would suggest to clarify this distinction at some point or rather use forward / backward recurrence always.
Out of curiosity: Why is it called LION?

- In Table 8, you apply a Non-linearity (elu) to q and k in addition to the LION-S mask. What is the default for LION-S? Only Mask and no non-linearity or mask and non-linearity?

- In equation 85, 88 and 101 is there the mask M missing?

- The exponential gating in the mLSTM (xLSTM) requires a stabilizer (or “max”) state in addition to S and z. See (eq. 15, 16, 17 and  74, 75, 80 in [2]). This is not explicitly addressed in 94 to 96, but the LION bidirectional reformulation should still be applicable.

- Have you tried using just the forward recurrence of LION-S, but reverse the order of the input sequence in consecutive blocks as it was done for example in “Vision-LSTM” [1] ? It would be interesting how this compares to the forward/backward LION-S. The same experiment could be also applicable to masked language modeling in Section 5.2.

[1] Alkin, B., Beck, M., Pöppel, K., Hochreiter, S., & Brandstetter, J. (2024). Vision-LSTM: xLSTM as Generic Vision Backbone. arXiv preprint arXiv:2406.04303

[2] Beck, M., Pöppel, K., Spanring, M., Auer, A., Prudnikova, O., Kopp, M., ... & Hochreiter, S. (2024). xLSTM: Extended Long Short-Term Memory. arXiv preprint arXiv:2405.04517.

### Soundness
4

### Presentation
4

### Contribution
4
