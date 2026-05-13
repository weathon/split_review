# Pyramid Vector Quantization for LLMs

- Decision: Reject
- Scores: 8, 6, 1, 5

## Abstract
Recent works on compression of large language models (LLM) using quantization considered reparameterizing the architecture such that weights are distributed on the sphere. This demonstratively improves the ability to quantize by increasing the mathematical notion of coherence, resulting in fewer weight outliers without affecting the network output. In this work, we aim to further exploit this spherical geometry of the weights when performing quantization by considering \textit{Pyramid Vector Quantization} (PVQ) for large language models. Arranging points evenly on the sphere is notoriously difficult, especially in high dimensions, and in case approximate solutions exists, representing points explicitly in a codebook is typically not feasible due to its additional memory cost. Instead, PVQ uses a fixed integer lattice on the sphere by projecting points onto the 1-sphere, which allows for efficient encoding and decoding without requiring an explicit codebook in memory. To obtain a practical algorithm, we propose to combine PVQ with scale quantization for which we derive theoretically optimal quantizations, under empirically verified assumptions. Further, we extend pyramid vector quantization to use Hessian information to minimize quantization error under expected feature activations, instead of only relying on weight magnitudes. Experimentally, we achieve state-of-the-art quantization performance with pareto-optimal trade-off between performance and bits per weight and bits per activation, compared to competitive methods. On weight-only, we find that we can quantize a Llama-3 70B model to 3.25 bits per weight and retain 98\% accuracy on downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the problem of quantization in llms. They introduce PVQ which is a  codebook-free and search-free vector  quantization scheme .

### Strengths
-

### Weaknesses
-please provide proper  referencing for  “coherence processing” on page 2. 
- on page 3, the   \hat{W} is not well introduced. how is it differen from W ? also \hat{W} should be bold since it is a matrix.
- move the legend in fig 2
- introduce all sets and params before their first appearance: S_D,k , P_D,K not introduced in  section 2.4. sets are better be  distinguishable from matrices  , you could use  caligraphic S and P for  sets. 

define “G”  in eq 7.  

- scalars better be represented by small letter. W for number of  words can be mistaken with W for weights. 

-please address the following  typos/grammatical errors:

“we achieves”, “

“compared to
compared methods”

“maximised”

“, making use for quantization costly.”

“The table can be precomputed a table of N”

“quantised” in fig 6

“On top” , “ to also quantize gains also enabling”

- this is not undestandable:  “to which we refer for a more detailed description of this for attention and fullyconnected layers found in most” - L1 ball should be $l_1$ - E8 ,RTN are not properly intriduced. 

-Figure 3 seems to be quantization on a Gaussian source not a neural network. provide mean and variance of the distributon of the Gaussian.

### Questions
What is the superiority of your  quantization scheme over the renowned  1.58   llm  quatization scheme?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to use a known vector quantization (VQ) method called Pyramid VQ (PVQ) to compress a large language model (LLM) at the bit level. The goal is to maximize the tradeoff between LLM's performance and the number of bits per weight. 

The paper describes the process of applying PVQ to LLMs, provides performance evaluations and comparisons to other VQ methods, and provides a result about the distribution of a normal random vector projection onto a sphere.

### Strengths
The topic of quantizing LLM's is timely and important. Quite a few commercial tools offer bit-level compression of LLMs and it appears that theoretical treatment of the topic is lagging.

Analyzing and discussing PVQ in the context of LLMs are solid contributions because the method is used in some applications. The PVQ description and illustrations are clear and engaging. 

Performance comparison to other methods is generally relevant although I have comments below.

### Weaknesses
The discussion concerning the advantages of PVQ over other quantization techniques is misleading because the advantage of an implicit codebook generally exists in all practical VQ techniques.  See standard references in the topic like:

[1] Gray, Robert M., and David L. Neuhoff. "Quantization." IEEE Transactions on Information Theory 44, no. 6 (1998): 2325-2383.

Additionally, there is no discussion on the motivation for using VQ compared to scalar quantization in LLMs. Here I'd expect the authors to mention some property of the distribution of attention weights (say) like dependency that makes VQ particularly effective. Other competing methods such as RTN, QuaRot, and QGPT mentioned in the paper are also not fully explained and it is unclear what are the benefits of the proposed method and whether they can be truly attributed to PVQ or the detailed implementation. The coherence processing is perhaps attractive from a practical perspective but it ``hides'' structure in the signal that is ideally exploited by the compressor (not to be confused with `dithering' in scalar quantization that has a different effect). 

Numerical evaluations are only against three methods. Because encoding and decoding are not straightforward, I believe that you should also compare runtime information. Indeed, one can easily think about an elaborated lossy weight compression procedure that would certainly outperform all methods but spend considerable time for encoding and decoding (again, see discussion in [1]). There is no comparison to the popular scalar quantization methods (such as the one described in https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit), no comparison to the E8 method that the paper references. There is no explanation of what are the zero-shot tasks. PPL values appear small -- perhaps you mean log(PPL)? 

In Section 3.2 the authors say that E8 is a ``state-of-the-art'' method that exploits ``geometric structure''. Both terms in parentheses need explanation. 

The theoretical result (Theorem 1) appears to be a reformulation of well-known properties of the distribution of projection of Gaussian vectors. I've found via a quick search the reference: 
[2] Frankl, Peter, and Hiroshi Maehara. "Some geometric applications of the beta distribution." Annals of the Institute of Statistical Mathematics 42 (1990): 463-474.
which explains the main point and includes references to earlier works. 

For the amplitude ('gain'), the authors first argue that it makes sense to use a scalar quantizer optimized for the Beta distribution (Theorem 1). However, the quantizer they describe is obtained via quantile transform of a Beta-distributed random variable and is not optimal in general. See the discussion about optimal scalar quantization form [1] and from
[3] Lloyd, Stuart. "Least squares quantization in PCM." IEEE Transactions on Information Theory 28, no. 2 (1982): 129-137.

In Section 2.5, it is said the encoder maps a vector to its **closest point** on the pyramid, but the mapping procedure to follow does not necessarily lead to the closest point in the Eecleadian sense.  

In Section 3.1, the fact that decoding is done by an ``algorithm'' is meaningless unless you can say something about the runtime of this algorithm. 


There are several writing issues: 
Unclear what is "infeasibly large". 
The 0.01 in Step 5 is misplaced.
Eq. (8) has a weird text.
Typo in Theorem 1 (s_h should probably be s_g)
PPF in Eq. (10) is undefined.
I suggest the following notational changes: 'gain' -> 'amplitude', 'shape' -> 'direction', 'SNR' -> 'QSNR' (Read: signal to quantization-noise ratio).

### Questions
The background and motivation need improvement. First, I suggest motivating VQ over scalar quantization which is already widely used in LLMs. Next, you can make the case that PVQ is an interesting VQ technique: It can be implemented in high-dimension due to an implicit codebook (like some other VQ techniques) and is also used in some applications. It appears to me that PVQ provides useful encoding under an L1 metric, whereas other methods would be better under, say, the more common L2. Analyzing the performance of PVQ may still be a solid contribution, but the discussion must be more comprehensive.  

Please explain more about the E8 method you provided as "state of the art". Can you compare performance to this method?
Please elaborate more on the other competing methods. Could you also show the performance of 4-bit scalar quantization, say using: https://huggingface.co/docs/bitsandbytes/en/reference/nn/linear4bit

It is well known, hence should be mentioned, that in high dimensions the information in the amplitude ('gain') is negligible compared to the information in the direction ('shape'). For example, see
[4] Kipnis, Alon, and Galen Reeves. "Gaussian approximation of quantization error for estimation from compressed data." IEEE Transactions on Information Theory 67, no. 8 (2021): 5562-5579.

The quantizer you used for the vector's magnitude is not optimized for the Beta distribution in any known sense. The authors either implement the optimal quantization method (under, say, mean squared error) or justify their approach.

Concerning Theorem 1, the authors should discuss how their result relates to or builds upon existing works like [2].

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a quantization method based on using representative points on a sphere to compress LLM weights and activation. The authors claim that it provides a significant improvement over existing art, and it is "codebook free" and "search free".

### Strengths
The idea of using spherical code to compress weight and activation may be worth studying. If it can be shown convincingly that this approach indeed outperforms others, then it can make a worthwhile contribution to the area of LLM quantization/compression.

### Weaknesses
I found the paper poorly written, lacking clarity, and missing some important baseline comparisons to be convincing.

1. Quantization can be used for different purposes in LLMs. It is done for compressing LLMs (either for storage and transportation across platforms, or for reducing memory usage by reusing weights), but it can also be done for approximate computation. Depending on the targetted usage scenario, the evaluation needs to be designed more carefully. It was never made clear what scenario this work was aiming at. I assume the authors are targeting LLM compression for storage and transportation across platforms since bits were used in the evaluation. This assumption, however, leads to another issue. In data compression, after quantization, an entropy coding step (e.g. Huffman or LZ) is usually taken. The authors seem to have completely ignored this step. It is not clear to me why this is not considered since it is considered common practice.

2. The claim of codebook-free and search-free are dubious. The authors appear to take the naive lookup table implementation as the literal interpretation of "codebook" and "search". However, a structured set of representation points, like the proposed pyramid vectors, is still a codebook. Some codebooks have more structure than others, for example, the simple scalar-quantizer is very structured, but a randomly generated codebook may be the least structured. Representation points obtained by K-mean are not well-structured, but it can also be forced to take certain structures if needed. "Search-free" is also not an accurate term. Even for a completely unstructured codebook, there are approximation methods to simplify the "search" step, for example, using a sum of component-wise differences as an estimate to prune away most candidates. I found using the claim of advantage ambiguous in terms of these two "codebook-free" and "search-free" 

3. The authors did not compare the approach to standard approaches of "lattice quantization", "lattice quantization+entropy coding", and even "scalar quantization" and "scala quantization+entropy coding". Lattice does not require a lookup table, and has efficient enumeration techniques. In Fig. 3, we see that E_8 lattice is already performing better than the proposed approach. However, the authors did not include E_8 and other lattices in all the other comparisons. In fact, A^*_8 may be even better than E_8 in dimension-8. The lattice-based quantization has been known for over 40 years to perform well, and there are very efficient algorithms that avoid "search". See for example: (a) Conway, John, and Neil Sloane. "Fast quantizing and decoding and algorithms for lattice quantizers and codes." IEEE Transactions on Information Theory 28.2 (1982): 227-232. (b) Conway, J., and N. Sloane. "A fast encoding method for lattice codes and quantizers." IEEE Transactions on Information Theory 29.6 (1983): 820-824. I found the lack of comparison with these well-known techniques unacceptable.

4. Another quantization approach is trellis-based quantization, and it is known to also perform well and reduce computation. The authors should consider providing a comparison. 

5. The paper is quite poorly written. A few extreme examples are as follows 1) There is still an unremoved comment in equation (8). 2) Page 4, below (6), it should be "at most" T<D steps. 3) RTN appears in many figures in Section 3, but was not introduced until Section 4. 4) equation (1) is incorrectly/inaccurately written. H is already the Hessian with the expectation over x, then the last expression in (1) should not need to take expectation over x. 

6. I do not believe the claim of "the only method with non-integer shape bits" holds water. The codebook size is not chosen arbitrarily, since it is determined by N(D,K). Therefore, though the number of bits is not necessarily an integer, the number of codewords can still only take discrete values. 

7. The example given in 3.1 is quite ridiculous. In practice, no one would store a quantization table in this manner. Even for an unstructured codebook, only the representative points will be stored, and then the quantization procedure will find one representative point in the codebook through some algorithm, either more direct or searching.

### Questions
1. What is the targetted application?
2. Why is the lattice-based approach not compared carefully?
3. Why is the trellis-based approach not compared?
4. Is scalar quantization compared? Is it significantly worse? How about scalar quantization plus entropy coding?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors propose a new post-training quantization algorithm for the quantization of LLMs.
The key idea is to apply a classic pyramid vector quantization (PVQ).
To validate the efficacy of the proposed method, the authors conduct experiments and provide kernels that allow hardware-accelerated encoding and decoding of PVQ.

### Strengths
A classic pyramid vector quantization (PVQ) method is well-combined with conventional tricks (e.g., coherence processing, quantization error compensation, Hessian) for the quantization of LLMs.

### Weaknesses
1. The authors need to improve the presentation of this paper. It seems that the authors just employed classic encoding and decoding algorithms in the pyramid vector quantization (PVQ) field. Although it is true, the authors need to explain the intuition and meaning of those algorithms. In the current version, the authors just mentioned that they used classic PVQ algorithms, and their pseudocode is provided in the Appendix. Furthermore, the detailed experimental setup is missing. How did the authors construct a calibration dataset? How many data samples are used for the quantization? What is the test dataset? 

2. The authors claimed that one key benefit of PVQ is that decoding is search-free while conventional vector quantization algorithms rely on look-up-table-based search. However, this claim is not justified. Why is this a benefit? Is the PVQ decoding process faster than look-up-table-based decoding? Also, while the authors analyze the time complexity of PVQ encoding/decoding in Table 5, actual processing time has not been measured, and thus the reviewer cannot judge whether the proposed algorithm is efficient.

3. The most crucial concern is that while the authors consider vector quantization, all the compared algorithms (GPTQ and QuaRot) are uniform quantization methods. It is natural that vector quantization methods exhibit better performance, but uniform quantization methods are much more hardware-friendly. The authors need to compare the proposed method with existing **vector quantization** methods [1, 2, 3, 4, 5].

### Questions
See the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
