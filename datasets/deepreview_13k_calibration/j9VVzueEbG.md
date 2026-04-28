# ZETA: Leveraging $Z$-order Curves for Efficient Top-$k$ Attention

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Over recent years, the Transformer has become a fundamental building block for sequence modeling architectures. Yet at its core is the use of self-attention, whose memory and computational cost grow quadratically with the sequence length $N$, rendering it prohibitively expensive for long sequences. A promising approach is top-$k$ attention, which selects only the $k$ most relevant tokens and achieves performance comparable to vanilla self-attention while significantly reducing space and computational demands. However, causal masks require the current query token to only attend to past tokens, preventing existing top-$k$ attention methods from efficiently searching for the most relevant tokens in parallel, thereby limiting training efficiency. In this work, we propose ZETA, leveraging Z-Order Curves for Efficient Top-k Attention, to enable parallel querying of past tokens for entire sequences. We first theoretically show that the choice of key and query dimensions involves a trade-off between the curse of dimensionality and the preservation of relative distances after projection. In light of this insight, we propose reducing the dimensionality of keys and queries in contrast to values and further leveraging Z-order curves to map low-dimensional keys and queries into one-dimensional space, which permits parallel sorting, thereby largely improving the efficiency for top-$k$ token selection. Experimental results demonstrate that ZETA~matches the performance of standard attention on synthetic tasks Associative Recall and outperforms attention and its variants on Long-Range Arena and WikiText-103 language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces ZETA, a model leveraging Z-order curves and Adaptive Cauchy-Softmax for efficient top-k attention, specifically aimed at handling long-sequence tasks. The authors propose a novel approach to reduce dimensionality for keys and queries, preserving locality while enabling faster token retrieval through Z-order-based projections. Their experimental results demonstrate competitive or superior performance on various benchmarks, suggesting ZETA’s potential as an efficient alternative for long-range attention tasks.

### Strengths
Originality : The paper introduces a novel use of Z-order curves for dimensionality reduction in attention mechanisms, adding a fresh approach to efficient top-k attention.
Quality:  Methodologically sound with theoretical insights like the Johnson–Lindenstrauss Lemma for dimensionality reduction. Experimental results across benchmarks support the model’s performance, though more tests could strengthen findings.
Clarity : The paper is well-organized and accessible, with clear explanations of techniques like Adaptive Cauchy-Softmax and Z-order projection, aiding reader comprehension.
Significance : ZETA shows potential in handling long sequences more efficiently, which could benefit applications in NLP and large-scale modeling. Further testing on diverse tasks would solidify its impact.

### Weaknesses
bout the experiment about  d_k​ in Experiments:
The authors test a narrow range of dkd_kdk​ values (1, 2, 3, 8, and 32), which may not reflect real-world applications where larger dimensions are common. Why weren’t higher dkd_kdk​ values explored? Expanding this range, particularly with larger model dimensions, could yield more generalizable insights. It is unclear if the performance gains observed with smaller $d_k$ values would hold with more standard, higher dimensional keys and queries. The choice of $d_k$ seems somewhat arbitrary without a clear justification for why these specific values were chosen and why larger values were not explored, especially given the common use of much higher dimensional key/query vectors in transformer models.

Unclear Transferability of \gamma in Adaptive Cauchy-Softmax:
The transferability of the trainable parameter γ\gammaγ in Adaptive Cauchy-Softmax across different tasks or datasets is unclear. Could the authors offer evidence or discussion on its robustness beyond the tested contexts? It is not clear if the learned \gamma is specific to the training dataset or if it generalizes to other tasks, and the lack of analysis on this aspect limits the practical applicability of the proposed method.

Lack of Formal Justification for Euclidean Distance Claim:
The claim that Euclidean distance is more effective for low-dimensional top-k methods lacks formal support. Providing a proof or theoretical justification would enhance the validity of this argument. The paper does not provide a clear theoretical explanation for why Euclidean distance should be preferred over other distance metrics, such as cosine similarity, when using low-dimensional key/query projections for top-k attention.

### Questions
Why choose ASSOCIATIVE RECALL in section 4.2 ?
Testing different d_k values on more Long Range Arena (LRA) tasks would provide a fuller picture of task-specific impacts on dimensionality selection. Could the authors evaluate dkd_kdk​ across a wider range of LRA tasks to strengthen their findings?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Paper is well written, with solid experimental work and theoretical analysis.
Authors introduce Efficient Parallel Top-k Attention by utilising Z-order Curves.  As this implies approximation, thorough experimental evaluation is performed to on several datasets including Long Range Arena, WikiText, MQAR to estimate computation efficiency vs model performance  tradeoffs. On top of this of paper investigate effects of Dimensionality Selection for Key and Query Pairs and Adaptive Cauchy-Softmax Mechanism which help to carefully select tradeoffs.

### Strengths
Paper address important area of computation cost (quadratic run time) of classical self-attention, which may be significant for long context. Novel Efficient Parallel Top-k Attention by utilising Z-order Curve was proposed, carefully analysed and evaluated.
On top of this paper this paper investigate dimensionality of keys and queries the trade-off between the curse of dimensionality
and the preservation of relative distances for keys and queries and introduces Adaptive Cauchy-Softmax which allows dynamic adjusting of receptive fields to enhance attention’s flexibility.

### Weaknesses
 - Evaluation is done on very small scale models (125M), so it could be that they won't translate to large size models.
- While Top-K should take O(N log N) and potentially should be more computation efficient,  it is not clear how much was gained in practice.  Also providing some more details about experiments (what is number of chunks, etc) would be helpful.
- The explanation of the top-k search using binary search on the Z-order curve is unclear. It is not obvious how a single binary search can identify the nearest neighbors, as the Z-order curve is not a space-filling curve that preserves locality perfectly. It seems likely that multiple segments of the Z-order curve would need to be inspected to avoid missing true nearest neighbors, and this process is not clearly described.

### Questions
'The insertion position of a query in the key sequence can then be found using a binary search (e.g. with torch.searchsorted), allowing us to retrieve the top-k attended tokens using a window centered on the insertion position'
Could you please clarify this. As far as I understand to find nearest k neighbours,  inspecting several segments of Z-order curve should be necessary or some false positives would be included?


Could you please share computation efficiency measurements (for example average training step time) for baseline transformer and ZETA?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors study an important and timely problem of addressing the quadratic complexity of dot-product attention in Transformers and propose leveraging sparsity by attending to only k most similar keys.

The authors aim to preserve query-key distances ||query_i - key_j|| after projecting queries and keys to a single scalar. To do so, they first reduce the dimension via a random projection per the Johnson-Lindenstrauss lemma.

KNN in d-dim is further reduced to sorting in 1D via the following trick: Let q and k be d-dim vectors. Let the binary representation of the i'th element q[i] be (q_i_31,...q_i_0). Then we can represent q as a number N(q) having a large binary representation (q_0_31,...,q_d-1_31,...q_0_0,...,q_d-1_0). Then |N(q)-N(k)| is likely to preserve the ordering of ||q-k|| as distances are more influenced by more significant bits of each element. This is not always true as q_0_31,...,q_d-1_31,... imposes an ordering on the dimensions whereas ||q-k|| is symmetric. Also note that most data types are limited to 64 bits.

Assuming that this does preserve the pairwise distances of queries and keys, we can sort the key scores N(k1),..,N(kL) and for each q_i use binary search to determine the most similar keys to attend to. The authors point out that for causal LM, we need to exclude future keys from being considered, and propose to use a chunking mechanism where positions are chunked and future key chunks are excluded from consideration.

As the above method is suitable for ||q-k|| and not <q,k>, the authors propose replacing dot-product attention with Cauchy attention where similarity of q and k is computed as 1 / (||q-k||^2 + gamma^2) instead of exp(<q,k> / sqrt(d)). Recent work on linear attention has shown this kernel to be performant.

### Strengths
1. The proposed method is interesting, and the trick of projecting to 1D for query-key similarity computation is intuitive.

2. Significant and comprehensive theoretical justification is provided for dimensionality reduction via random projection and is well-supported via detailed proofs.

3. The authors show that this method works well on the multi-query associative recall task that has been used to justify the in-context learning abilities of Transformers. On language modeling on Wikitext-103, the method also works as well as vanilla Transformer.

4. The authors demonstrate that this method outperforms full dot-product attention on Long Range Arena, which is a popular benchmark for stress testing long-range abilities across various modalities.

5. The authors have included a pytorch implementation of their method. I appreciate this and will take it positively into account in my evaluation.

### Weaknesses
1. Distances are not preserved even for modest key dimensions, which might be an issue when scaling up. It is not clear if this method can be used as a drop-in replacement for existing pretrained models due to the change in attention similarity.

2. The authors claim that smaller key dimensions do not affect performance. This is not a well-established fact - more comprehensive experiments are required to justify this claim.

3. The chunking part of keys and queries could have been more clearly written, or pseudocode of the method in an appendix would have helped. I looked at the provided torch code in the supplementary but this part looks involved.

4. Benchmarking of speedup / memory usage is not provided.

5. SOTA performance on LRA benchmark is much higher. The performance on the Path-X task is not included, and the authors do not mention this exclusion.

### Questions
1. Can you include more details on the chunking part. Also explain where efficiency is coming from.
2. Can you provide resource usage results especially for long-sequences. Also include it for flash attention and other methods such as SSMs which perform better on the tasks that you include the paper.
3. Can you discuss the limitations of your method.
4. Can you provide results on Path-X task in LRA?

~~I am willing to change my score if the authors can address these concerns.~~  
**[Post author rebuttal]**: The authors have largely addressed my concerns and I have increased my score.


Typos:
- Equation 6: "(q-Ki)" should be "||q-Ki||"
- Line 232: Period missing after Lemma 3.1

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
This paper introduced ZETA, a model to enhance the top-k attention using Z-order curves, reducing the complexity from N^2 to N log N. ZETA's query & key dimensions are much smaller than the value dimension. This is to ensure the speed and locality preservation of the Z-order curves. The authors also replaced the Softmax operation with the Cauchy-Softmax to enhance the performance of ZETA. Experiments showed that ZETA matched the performance of the attention models on Associative Recall while outperforming the attention models on Long-Range Arena and WikiText-103 language modeling.

### Strengths
* The paper is well-written and the method is believable.
* Compared with the attention models, the ZETA model matches the performance on Associative Recall while outperforming on Long-Range Arena and WikiText-103 language modeling.

### Weaknesses
 * The effect of $d_K$ needs clarification.
  - In section 3.2.1, line 202, the authors mentioned: "a lower $d_K$ loses locality between tokens, which is crucial for efficient query".
  - However, in section 4.4, line 454, the authors mentioned that "Lower $d_K$ values exhibit a higher level of locality preservation across all sample sizes."
  - There seems to be a contradiction between these two statements, so the effect of $d_K$ needs clarification. Specifically, the relationship between $d_K$ and locality preservation needs to be more rigorously defined. The authors should clarify whether the locality being discussed in section 3.2.1 refers to the original input space or the transformed space after applying the Z-order curve. It is unclear how the dimensionality of $d_K$ impacts the quality of the Z-order curve mapping and the subsequent locality preservation. A more detailed analysis of how different $d_K$ values affect the distribution of tokens in the 1-dimensional space is needed.
* Can the authors clarify the binary expansion? What is the precision of the original d-dimensional vector?
  - Eq. (4) introduced Z-order curves, which rearrange a d-dimensional vector into a one-dimensional binary representation.
  - Suppose d=3. Suppose the precision of the numbers in the d-dimensional vector is 32 bits (e.g., the float32). Then the resulting Z-order curves will have 3*32=96 bits. 
  - Will this result in an overflow? If not, how did you set the precision of the original d-dimensional vector? The paper lacks a clear explanation of how the original d-dimensional vector is converted into a binary representation. The authors should specify the exact bit precision used for each dimension before applying the Z-order curve. It is crucial to understand whether the original floating-point values are directly converted to binary or if they are first discretized. The potential for overflow during the bit interleaving process needs to be addressed, along with a discussion of how the chosen precision impacts the accuracy of the Z-order mapping.
* Can the authors provide a comparison of the time and space usages for ZETA model and the attention-based models?
  - The authors claimed that ZETA reduces the time and space complexity to N log N. So I assume that ZETA runs faster and uses less memory. However, there is no actual number on this. So, the run-time metrics on time and space are needed. The paper needs a more thorough empirical evaluation of the computational efficiency of the ZETA model. The authors should provide detailed benchmarks comparing the runtime and memory usage of ZETA against standard attention mechanisms, including optimized implementations like Flash Attention. These benchmarks should be conducted across a range of sequence lengths to demonstrate the scalability of ZETA. Furthermore, the authors should provide a breakdown of the memory usage, specifying how much memory is used for storing keys, queries, and values, and how this compares to attention-based models.

### Questions
* The recent state-of-the-art LLMs have at least 100k context length. Gemini 1.5 Pro even supports 2M context length. How does this impact the selection of your $d_K$ and other hyperparameters? Will $d_K$ go to 2 or even 1?

### Soundness
4

### Presentation
3

### Contribution
4
