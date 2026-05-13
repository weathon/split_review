# CrossMPT: Cross-attention Message-passing Transformer for Error Correcting Codes

- Decision: Accept
- Scores: 6, 6, 8, 6, 6

## Abstract
Error correcting codes~(ECCs) are indispensable for reliable transmission in communication systems.~The recent advancements in deep learning have catalyzed the exploration of ECC decoders based on neural networks.~Among these, transformer-based neural decoders have achieved state-of-the-art decoding performance.
In this paper, we propose a novel Cross-attention Message-Passing Transformer~(CrossMPT), which shares key operational principles with conventional message-passing decoders.
While conventional transformer-based decoders employ self-attention mechanism without distinguishing between the types of input vectors (i.e., magnitude and syndrome vectors), CrossMPT updates the two types of input vectors separately and iteratively using two masked cross-attention blocks.~The mask matrices are determined by the code's parity-check matrix, which explicitly captures the irrelevant relationship between two input vectors.
Our experimental results show that CrossMPT significantly outperforms existing neural network-based decoders for various code classes.
Notably, CrossMPT achieves this decoding performance improvement, while significantly reducing the memory usage, complexity, inference time, and training time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel transformer-based architecture called CrossMPT(Cross-attention Message-Passing Transformer) for decoding error-correcting codes(ECCs). The key innovation lies in the use of cross-attention mechanisms to separately and iteratively update magnitude and syndrome vectors, in contrast to conventional transformer-based decodes that employ self-attention without distinguishing between different types of input vectors. The mask matrices in CrossMPT are derived from the code’s parity-check matrix (PCM), explicitly capturing the relationships between magnitude and syndrome vectors. Results demonstrate that CrossMPT significantly outperforms existing neural network-based decoders across various code classes, while also reducing memory usage, computational complexity, inference time, and training time.

### Strengths
1. Innovative architecture: introduced the cross-attention mechanisms to separately handle magnitude and syndrome vectors is a notable advancement, bridging concepts from traditional message-passing algorithms and modern transformer architectures.
2. Performance Gains Significantly: in the experiments show significant improvements to existing decoders across various code classes, including BCH, polar, LDPC, and turbo codes.
3. Efficiency Improvements: By reducing memory usage and computational complexity, CrossMPT addresses practical concerns associated with deploying transformer-based decoders, especially for longer codes. 
4. Use of PCM-derived Masks: Aligning the mask matrices with the PCM directly incorporates code-specific structural information into the model, enhancing its ability to learn relevant relationships.

### Weaknesses
The architectural modification proposed in the paper with respect to ECCT is rather trivial. In that sense, it does not have significant technical novelty, on the other hand, given its impact on the performance, I believe it is a worthy contribution. 

The paper presents only BER performance results. It is not clear if the proposed approach actually provides any gains in terms of the block error probability, which would really matter for the code.



### Questions
1. FER Results: In [1], the authors present their results using the Frame Error Rate (FER) metric, while your results are reported using Bit Error Rate (BER). Could you please explain why you chose to report BER over FER in your evaluation? Are there specific challenges or reasons that prevent you from providing FER results for your approach? Including FER results would be helpful for assessing the practical decoding performance and for making a direct comparison with the results in [1].

2. Training Convergence and Speedup: In Appendix I, authors mention that CrossMPT achieves faster training convergence compared to ECCT. However, the figure provided does not clearly demonstrate a significant speed up. Could you please provide specific data quantifying how much faster CrossMPT converges during training? For instance, you could report metrics such as: wall-clock training time taken by each model to achieve comparable performance levels and percentage improvement in convergence speed or reduction in epochs/time needed.

3. Reproducibility: Do you plan to release the source code or detailed experimental records? Reproducibility is essential for validating the results and facilitating future research based on your work.

[1] A Foundation Model for Error Correction Codes

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the neural network based decoding of conventional error correction codes. In essence, decoding of an error correction code is a classification problem. Conventional belief propagation based decoders rely on the code structure to iteratively improve their beliefs on the message bits. An alternative approach is to parameterize the decoder as a neural network, and train it on various codewords. Given the large number of codewords, it is challenging to design such a decoder without exploiting the code structure. An obvious approach is to use the code structure and the basic steps of the belief propagation decoder, but unroll the iterations on the layers of a neural network. This work follows the recently introduced ECCT decoder in this direction, and exploits a transformer architecture for the decoder. In particular, by transforming the decoding operation into the estimation of the sign of the multiplicative noise component, and by separately representing the magnitude of the received signal and its syndrome as two separate pieces of information, the authors train separate masked cross-attention blocks to update the embeddings of these two blocks before reaching the final decision. Through experiments, they show that the resultant decoder can achieve a lower bit error rate (BER) compared to ECCT in decoding a number of different channel codes, with a slightly lower computational complexity.

### Strengths
The decoding of error correction codes is an important problem with significant potential impact in practice. Using neural network based decoders is a promising approach that has been receiving significant attention recently. The paper improves the state of the art transformer-based architecture with a simple yet effective enhancement in the architecture. Given that the magnitude and the syndrome provide different types of information on the transmitted symbols, it makes sense to process them separately, and learn different cross-attention modules. Despite the fact that the architectural modification is simple, the improvement in BER performance is significant. The authors also provide a good explanation of their motivation and the impact of their architecture on the decoding process (e.g., attention scores). Overall, it is a well-written paper with clearly highlighted contributions.

### Weaknesses
Although I think the paper is strong, I found a couple of minor weaknesses.

1. The actual inference time reduction from ECCT is not as great as the FLOPs improvement. Also, runtime evaluation and complexity analysis need more details about the environment. See Questions 3-5.
2. Related works on cross attention in other domains are missing, e.g., language (Vaswani et al., 2017), vision (Chen et al., 2021), text-based image generation (Rombach et al., 2022), etc.

### Questions
- The performance measure presented in the paper is BER; however, what really matters for a channel code is the block error probability (BLER). Therefore, I would ask the authors to include BLER results to clearly show that the proposed approach does actually improve the performance with respect to ECCT or other baseline decoding algorithms. Improvements in BER are still important, but correct decoding of the message bits would still require the concatenation of the code with an outer code, which would further increase the decoding complexity, and would diminish the gains of the proposed approach. I believe, not presenting the BLER results at all is not fair, and does not show the real performance of the approach. 

- How does the complexity compare with the more conventional BP decoders and neural BP (NBP) decoders? Are the numerical results presented in Fig. 4 for the same complexity decoders, or for the same number of decoder iterations? If it's the latter, the comparison is not fair. If each iteration of the NBP decoder has half the complexity of the proposed approach, it can run twice the number of iterations, and potentially achieve lower BER. 

- Why is the double-masked ECCT not included in the comparisons?

### Soundness
3

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
5

### Summary
The paper proposes cross-attention-based message-passing transformers (CrossMPT), which solve the ambiguous masking problem of the naïve self-attention-based approach (ECCT). The magnitude and syndrome information are processed using two cross-attention layers, similar to message-passing algorithms, incorporating a mask defined by the parity check matrix. The proposed scheme achieves superior performance on various codes and SNRs consistently over ECCT and other baselines. The cross-attention map provides some degree of interpretability, while cross-attention itself enjoys reduced complexity compared to full self-attention, enabling the processing of long codes.

### Strengths
1. The update in the attention layer built upon ECCT is well-motivated and shows meaningful performance improvement. Although cross-attention is a well-known technique in the community, it is placed at the right position to improve the performance and efficiency of the previous self-attention-based approach.
2. The paper is easy to follow and provides sufficient details.
3. The experimental results effectively support the claims.
4. The in-depth analysis of the proposed method helps readers understand the paper better.

### Weaknesses
1. One common troubling trend in comparing the performance of neural decoders is the choice of weak classical baselines. While I understand the difficulty of a common decoder architecture outperforming the highly specialised decoders for each of the class of codes, the comparison should neverthless be done for completeness. For instance, in Fig.4, only BP classical baseline is considered. It is known that BP is not optimal for many codes. For instance, when comparing with BCH codes, Berlekamp-Massey decoding algorithm should be used as the classical non-learning baseline and similarly for Polar codes, successive cancellation list decoding should be used. I strongly suggest authors to include the best classical baselines for each code to clearly show the gap with respect to the SOTA neural decoder, whether it is positive or negative.

2. I beleive authors chose the format of the negative log BER for presenting the results based on the original ECCT paper. But this format is not very informative and very uncommon in information and coding theory literature. While it is easy to identify which scheme is doing better, the gap between the performances is hard to interpret as the scale is not very intuitive. Rather, the standard format of SNR gap in dB for a target BER/BLER (ex. BLER target of $10^{-5}$) is more informative. 

3. While the idea and results are interesting, the changes in the algorithm/architecture are only incremental compared to the original ECCT paper, which limits the novelty to some extent.

4. As with the case of other model-free neural decoders, there is a lack of interpretation for the neural decoder presented. Since the algorithmic contributions are limited, I would suggest atleast adding a discussion on interpretation and analysis, similar to the analysis and interpretation of neural belief propagation codes. A couple of references I can think of are: [1], [2]

### Questions
1. Why was the magnitude chosen instead of another quantity, such as LLR? What is the intuition behind using the magnitude?
2. What happens if the syndrome information is placed as the query in the first attention layer? Does changing the order make any difference?
3. Is the inference time in Table 2 evaluated on the GPU?
4. What is the peak memory requirement? 
5. Was the inference runtime evaluation conducted after code compilation (e.g., using `torch.compile()`)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a new cross-attention based decoding schemes for linear block codes using transformer architecture. The masking and the cross attention mechanism depend on the parity check matrix of the block code, thus introducing the domain knowledge about the code into the decoding architecture. This work seems to be built on Error Correction Code Trabsformer (ECCT), NeurIPS 2022.

### Strengths
1. The idea of treating syndrome and magnitude as two separate entities and using cross-attention to capture the relation is novel and interesting. From a error correction point of view, this is more intuitive and understandable than existing approches. 

2. The performance improvement over ECCT is compelling and non-trivial, while maintaining similar or lower complexity.

3. Overall well written and self-contained. Easy to understand and follow the ideas, even for reader unfamiliar with prior work.

### Weaknesses
I'm concerned about the complexity analysis and thus the claim of superiority of the method over ECCT.

Cross-MPT adopts a **sequential** processing approach that appears **after** the self-attention, which is the only module in ECCT.
This sequential processing (1 self-attention + 1 cross-attention) is then necessarily slower than ECCT's single parallel processing (1 self-attention only) on modern parallel computing HW.

It obviously allows better decoding performance, making the comparison unfair, even if the parameters are shared.

### Questions
Included in the weaknesses

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents an extension of the existing ECCT by splitting, as with classical message-passing decoding (BP), the self-attention module between variable and check nodes. This is done similarly to classical Transformers decoders via the additional cross-attention while the original ECCT has only self-attention layers.

### Strengths
The paper is well-written and clear.

The paper is well-presented and has extensive ablation studies.
 
The method is interesting and sounds natural given classical message-passing decoders.

The method improves over the original ECCT and allows more memory efficient training on GPUs.

### Weaknesses
I'm concerned about the complexity analysis and thus the claim of superiority of the method over ECCT.

Cross-MPT adopts a **sequential** processing approach that appears **after** the self-attention, which is the only module in ECCT.
This sequential processing (1 self-attention + 1 cross-attention) is then necessarily slower than ECCT's single parallel processing (1 self-attention only) on modern parallel computing HW.

It obviously allows better decoding performance, making the comparison unfair, even if the parameters are shared.

### Questions
1 - The authors should integrate clearer information regarding the complexity as explained in the Weakness section.

2 - There is a large gap remaining with SCL decoding. The authors should explain and investigate why the (cross) ECCT and its variants struggle with it.

3 - The authors should provide comparisons between the methods for various dimensions/layers, as done with the ECCT and its extensions.

### Soundness
3

### Presentation
3

### Contribution
2
