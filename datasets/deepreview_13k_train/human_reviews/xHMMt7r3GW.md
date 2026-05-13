# LieRE: Generalizing Rotary Position Encodings to Higher Dimensional Inputs

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
Rotary Position Embeddings (RoPE) have demonstrated efficacy and gained widespread adoption in natural language processing. However, their application to other modalities has been less prevalent. This study introduces Lie group Relative position Encodings (LieRE), which extend beyond RoPE by accommodating n-dimensional inputs. LieRE encodes positions of tokens by replacing the RoPE rotation matrix with a dense, high-dimensional, rotation matrix generated via a learned map. We conducted empirical evaluations of LieRE on 2D and 3D image classification tasks, comparing its performance against established baselines including DeiT III, RoPE-Mixed, and Vision-Llama.
Our findings reveal significant advancements across multiple metrics as compared to the DEIT III basline: LieRE leads to marked relative improvements in accuracy (10.0% for 2D and 15.1% for 3D compared to DeiT). A 3.9-fold reduction in training time for the same accuracy was observed. LieRE required 30% less training data to achieve comparable results.
These substantial improvements suggest that LieRE represents a meaningful advancement in positional encoding techniques for multi-dimensional data. The implementation details and reproducibility materials will be made openly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a position encoding technique that can be used with attention mechanisms for 2D and 3D data. In contrast to RoPE which learns a block diagonal (2x2 blocks) rotation matrix transformation of key and query matrices from relative position information, LieRE learns a general rotation matrix transformation of key and query matrices from absolute position information. While this introduces additional parameters, the authors mitigate this by sharing parameters across attention heads. The authors show that with the combination of these strategies, LieRE improves predictive performance, training efficiency and data efficiency.

### Strengths
The authors propose a novel position encoding scheme with improved performance over baseline models. The improved performance is in terms of predictive performance, training efficiency, and data efficiency. Moreover the model can be used for 2D and 3D data.

### Weaknesses
The writing could be improved. The document would benefit from additional proofreading. For example, in several places (Lines 169, 173) the text reads ‘equation equation’; ‘figure’ and ‘table’ should be capitalized (Line 187, 397); and the notation for updated keys and queries is inconsistent (Line 188, 189, 209). The clarity of the document would be improved. For example, it would benefit the reader if the equation for the attention mechanism were provided 3.1; some text describing the algorithm would benefit the reader; it would be nice to show that LieRE-Commute and RoPE-mixed are special cases of LieRE.

The organization could be improved. Using subsubsections in the related work doesn’t seem necessary, and takes up space that might be used to clarify the method section. Some details of the method are presented for the first time in the Results section (e.g., that the parameters of LieRE and its variants are shared across attention heads). Figures are often far from where they are referenced.

### Questions
* When the authors say ‘generator space’ do they mean Lie algebra?
* In the definition of R_{LieRE} consider using A(x) as the argument to the exponential map
* (Line 400) Broken figure reference 
* Do the authors have thoughts on why LieRE improves training/data efficiency 
* Should the final statement in eq 2 be exp(V)^-1 exp(U)?

### Soundness
3

### Presentation
1

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
This paper proposes a symmetry-aware method for positional encoding (LieRE) that outperforms the state-of-the-art methods (RoPE), by considering subspace rotations of dimension higher than $2$ in the self-attention's dot-product (the orthogonal symmetry group action given by $(R,(q,k))\mapsto (Rq,Rk)$). Using a Lie group theory the resulting rotation encoding is deduced as $R=\exp(\sum_iA_ix_i)$ where $i$ is each domain dimension and $A_i$ is learnable skew-symmetric matrices. Furthermore, shuffling patches causes more accuracy drop in LieRE than RoPE, which verifies that the model relies more on positional encodings by using LieRE. It also outperforms existing methods in terms of training time and dependency on dataset size.

### Strengths
- The positional encoding structure is fundamentally important in Transformer architectures. Improving over the state-of-the-art has a great impact. 
- I find it particularly interesting to treat the spatial and embedding dimensions of the hidden states equally, which I believe results in a unified understanding of the embedding space as a tensor field. Lie group generalizes rotary positional embedding from dimension $2$ to $n$ by regarding RoPE as a commutative special case.
- I find it interesting that sharing parameters across layers (LieRE-Commute over RoPE-mixed) improve learnable positional encodings.

**Update**: Thanks for adding the experiments to validate LieRE’s performance. I have raised the presentation score to 4, and feel more confident on my recommendation. Good luck.

### Weaknesses
1. Although the relative gain over existing methods is fair and remarkable, <70% accuracy on CIFAR100 and ImageNet and ~50% on UCF101 is far from optimal. For example, the referred paper (Heo et al. 2024) reports >80% accuracy. It would be more convincing to improve the baseline. The current results, while showing improvement over RoPE, still leave a significant performance gap compared to state-of-the-art methods. This raises questions about the practical applicability of the proposed method in scenarios requiring high accuracy.
2. The 3.5x reduction in training time is compared under the wall time of 200 epochs, which means the same performance is obtained at around 57 epochs for LieRE. I wonder how these methods compare in terms of the best test loss, and the converged training loss (which means after 200 epochs). Running longer experiments may also help remedy poor baselines. It's crucial to understand if the faster training time comes at the cost of not reaching the optimal performance achievable with longer training. The comparison should focus on the best achievable performance, not just the time to reach a specific performance level.
3. I find the compute efficiency less informative than the learning curve. The FLOPs analysis is of practical interest but looks trivial since positional encoding is a lightweight part of the model. The analysis of FLOPs for positional encoding is not as critical as understanding the impact on overall model convergence and performance. A detailed learning curve would provide a more comprehensive view of the training process and the effectiveness of the proposed method.

Minor issues: 
- Table 2: I find the word "stem" in Table 2 confusing and unnecessary. Clarifying it in the text rather than just in Figure 3a would help.
- Many \citet should be \citep
- Table 2 line 381: Rope should be {RoPE}. 
- Line 400: Figure ??

### Questions
1. I don't understand why commutativeness in the RHS of Equation (2) is not $\exp(V)^{-1}\exp(U)$, but $\exp(U)^{-1}\exp(V)$. Is it a typo?
2. Should line 201 "We present attention with LieRE and LieRE-Commute in Algorithm 1 and 2" reverse the order? 
3. Would it be better to clarify the relation between "LieRE-Commute, learnable RoPE and RoPE-mixed" already here in the method section (now this does not appear until 5.3.3), and remind the reader in the background why the group $SO(d)$ not abelian if $d>2$, preferably with some one-line intuitions?
4. Do you have more intuition to justify the reason why the stem option outperforms layer or head heterogeneous implementations? For example, does it suffice to think of the $O(n)$ symmetry in the dot product that only needs one representative element in the quotient group, instead of striving to learn it repeatedly in every layer or head subspace?
Based on this, would you think it is possible to unify the representation by rotationally aligning the subspaces of each layer?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposed an extension to the prior work RoPE attention. The central idea is to extend the 1-d position encoding in RoPE to handle higher-dimension position indices. In RoPE, the feature vectors are rotated before the attention inner products to take into account the distance between two tokens. For each feature vector of d-dimension, d/2 rotations in 2d space were used. The authors argue that using 1 rotation of d-dimension space, taking into account multiple token indices, is better.

Lie theory is used to map position indices to "rotations", via the exponential map.

### Strengths
The use of Lie groups for position-aware attention is a novel and interesting idea.

### Weaknesses
 - The method is not clearly defined, with proper mathematical description. By code segment in the appendix, is also not explained, particularly not in a way that connects with the main text.
- It is not intuitive why a single rotation is better than multiple rotations. Actually, multiple rotations of RoPE have the benefit of adaptively capturing different levels of distance effects.

### Questions
- Please define the A matrix in detail. Clarify the notation n and d in Section 3.2 (use them consistently please).
- Can you conduct experiments on a data set with varying image sizes and resolutions? In other words, a single dataset with different scales of spatial correlation.

### Soundness
2

### Presentation
2

### Contribution
2
