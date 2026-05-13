# Binary Hyperbolic Embeddings

- Decision: Reject
- Scores: 5, 1, 6, 6

## Abstract
As datasets grow in size, vector-based search becomes increasingly challenging in terms of both storage and computational efficiency. Traditional solutions such as quantization techniques involve trade-offs between retrieval speed and accuracy, while hashing methods often require further optimization for binarization. In this work, we propose leveraging the compact nature of hyperbolic space for efficient search. Specifically, we introduce Binary Hyperbolic Embeddings, which transform complex hyperbolic similarity calculations into binary operations. We prove that these binary hyperbolic embeddings are retrieval-equivalent to their real-valued counterparts, ensuring minimal loss in retrieval quality. Our approach can be seamlessly integrated into FAISS to achieve improved memory efficiency and running speed while maintaining performance comparable to full-precision Euclidean embeddings. \tblue{Notably, binary hyperbolic embeddings can also be combined with product quantization}. We demonstrate significant improvements in storage efficiency, with a natural byproduct of speeding up, with scaling potential to larger datasets. A portion of the code is included in the supplementary materials, and the full implementation will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Paper introduces a new binary quantizater scheme for hyperbolic embeddings to capture similarity. 
Traditional models use Deep Learning machinery to produce "euclidean vectors" for objects so that the L2 distance between vectors is smaller for more similar documents. 

Recently over last few years, there has been work on exploring non euclidean geometries. Namely, hyperbolic geometries and distances has emerged as a way to capture similarities, especially hierarchies of "semantic concepts" are seemingly better captured by hyperbolic embeddings. 

This paper shows that we can effectively "quantize" each dimension using a simple linear quantizer, and then use hamming distance to rank the vectors to retrieve similarity based on original hyperbolic distances. 
They compare the quality of their embedding, retrieval speed, and other metrics on 2-3 datasets to show that the current method outperforms good and competitive baselines.

### Strengths
* The hyperbolic geometrics are increasingly becoming more popular, and this paper is timely in that regard
* paper has interesting theory and empirical results
* experiments are well thought out and cover many ablation studies to prove their case

### Weaknesses
Proposition 3.1  and 3.2 talk about preserving rankings. Not about how close the distances are after the transformations. 
In particular, it could be that original distances are 10 and 20 and 25, and after transformation, become 10, 11, and 12. This is particularly important as for large-scale datasets, we often use approximate nearest neighbor search and not exact search. So ranking is less important than the preserving the distance gaps.

Abstract says your approach is modular and can be combined with other methods like PQ, but not shown any details. There are comparisons with PQ but not detailed how to combine the two methods. 

The datasets compared for benchmarks are somewhat dated, and not using the latest models/ embeddings. Maybe these are standard in hyperbolic literature, but not clear how they predict the applicability in newer LLM-based models like LLama, GritLM, etc.

There is quality comparison with PQ, but not speed comparisons. 

There could be a more gentler introduction into hyperbolic geometries, and why they are useful. It seems to suddenly be thrown at the reader. Of course, this matters only for the unfamiliar reader. Also how the hierarchy of concepts topic is covered is a little abrupt and out of place.

### Questions
Line 62: "under retrieval" what this means?

Line 144: Why is the computational complexity high? Elaborate more

Line 148: Is this symmetric distance? Is there a rewrite which makes it symmetric?

Line 197: "five models": elaborate which five, many readers might be unaware.

Table 2: Retrieval speed: is it per query, or total across N queries for some N. Does it include the neural network time, or just the ranking of binary embeddings

Table 1: What is S^d?

4.4: Line 417: The paragraph is not clear. Make it more elaborate.

Can we combine with LSH type quantization methods instead of simple linear scaling of the values into bits?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents a solution for using quantized hyperbolic embeddings for vector search. To the best of my understanding the authors do not seem to be proposing a new model for computing the hyperbolic embeddings, and follow Long et al. (2020) for this. The innovation resides in the binarization to overcome the inefficiencies of the hyperbolic distance computations. With the proposed approach, memory is spared and speed is gained while maintaining accuracy.

### Strengths
- The authors show that quantizing hyperbolic embeddings leads to almost no decrease in accuracy in the supervised vector search setting. Even going as low as using 2 bits per value seems to provide good results
- The authors provide a sound comparison showing that using hyperbolic embeddings yields better accuracy and compression than using linear or spherical maps when dealing with labeled data with a hierarchical structure.

### Weaknesses
First of all, I believe that the overall presentation is slightly misleading. By reading the abstract, introduction, and most of the paper, it seems that this is a general method that could replace any of the standard embedding methods in vector search. However, it is clear in Appendix A that the authors are only dealing with the supervised setting. This should be clearly stated. Moreover, the use of vector search in research and industry for GenAI is moving away from the supervised setting. This does not imply that this setting is not interesting in itself, but it serves a narrower scope and this should be clearly stated.

More importantly, the whole work hinges on the statement that "calculating the distance between embeddings [in the hyperbolic space] involves slow vector operations." Although true strictly speaking when looking at Equation (2), I argue from two different perspectives that this is not a constraint in practice.

- Perspective 1: If one can replace one distance with another that is easier to compute and that preserves ordering, one can perform vector search. Here, only the total order induced by the distance to the query matters. The authors use the well known relationship in Equation (14) of Appendix B, found in (Ganea et al., 2018a) for example. This lead to Equation (15):

$$||q - x_1||^2 / (1 - ||x_1||^2) < ||q - x_2||^2 / (1 - ||x_2||^2)$$

where I have omitted the term $1 - ||q||^2$ on both sides as it does not change the total order. The authors should explain why the dissimilarity $||q - x||^2 / (1 - ||x||^2)$ is such a computational burden. In the worst case scenario that we do not know $||x||$ (more on this next), it requires twice the number of multiplications than the squared Euclidean distance. Given modern arithmetic speed in CPUs and GPUs, once the data has been fetched  from memory this 2x increase seems trivial. If this is not the case, the authors should clearly explain why it is not the case.

- Perspective 2: The authors seem to be using class membership as the ground truth (please correct me if I'm wrong). The angle between two vectors in hyperbolic space is sufficient to determine the class they belong to. This observation was also done by Long et al (2020), where the $1 - \cos(q,x)$ is used as the dissimilarity measure. This means that we could pre-normalize all vectors in the database and simply use $1 - <q,x>$ as the dissimilarity measure. Using fused-multiply-add instructions, this calculation is extremely fast.

Notice that these two perspectives do not require any type of conditions or assumptions on the embedding vectors, contrarily to Proposition 3.1.

The main condition in Proposition 3.2 states that $<x,y>$ should be proportional to $<g(x),g(y)>$. Then, the derivation in equation (26) of the appendix does not lead to proportionality of the squared distance, but to inequalities for it since the different terms will have different proportionality constants. For example,
- $<x,x> \propto <g(x),g(x)>$ with scalar constant $a$
- $<y,y> \propto <g(y),g(y)>$ with scalar constant $b$
- $<x,y> \propto <g(x),g(y)>$ with scalar constant $c$

This will lead to prove either that $d_R^2(x,y) \leq d_H(x,y)$ or that $d_R^2(x,y) \geq d_H(x,y)$ depending on $a, b, c$. Then the Proposition stops being useful, unless the constants are tight, which requires a much more detailed analysis.

However, the use of the symbol $\propto$ in Equation (9), may indicates that the authors are using it to indicate proximity (commonly noted $\approx$) and not proportionality (commonly noted $\propto$). If it is proximity , then Proposition 3.2 does not seem to be very useful. It boils down to stating that g is such that if $x \approx g(x)$, then $d_R^2(x,y) \approx d_H(x,y)$, which is trivial unless you characterize mathematically the nature of the proximity (as was done in locality-sensitive hashing (LSH), for example).

In any case, the word equivalence is too strong for this type of result. That is why the seminal LSH is considered an approximation.

Regarding the binary quantization, I do not understand the rationale. Coming back to my previous paragraph about notation ($\approx$ versus $\propto$), maybe the authors mean something different than what they actually wrote in Equation (9). Because of the quantization step in Equation (7), $<x,y>$ is not proportional to $<x_{int}, y_{int}>$. Moreover, it seems that the authors are reinventing base 2 integer arithmetics. Any modern CPU/GPU can perform $<x_{int}, y_{int}>$ with extreme efficiency at the hardware level using intrinsic SIMD instructions. For example, for vectors with 512 or 256 bits, this computation can be done with a single instruction on modern CPUs. If using less than 8-bit quantization, this will require a few more instructions but the point still stands). However, the authors opt to bypass it with the software implementation in Equation (10), which clearly needs many CPU instructions, even for 256-bits or 512-bit vectors.

Minor editorial comments:
- In Section 2, there are quite a few references that do not use the proper citet/citep format. This complicates reading these paragraphs. This occurs in other parts of the paper as well.
- In line 368, the reference to "Figure 4.4" is wrong. It should be "Figure 4" 
- There are figures that are never been referenced in the text, Figure 2 for example. Please make sure that all figures and tables are properly referenced in the main body.
- Footnote 1 on page 4 refers to Appendix D and it should refer to Appendix C.
- There seem to be missing terms in Equation (9). Maybe the authors missed writing "+ ... +" before the last term.
- Please provide two contrasting colors and different line styles for the curves in Figure 3.

### Questions
- Is there a way to apply the proposed approach in the unsupervised setting?
- Please explain and clarify whether the inefficiencies of the hyperbolic distance computations are truly a bottleneck for the application addressed in this paper.
- Please clarify the mathematical notation ($\approx$ versus $\propto$), and be more precise in the language of the proposition (find a better term than equivalence)
- Please evaluate whether Proposition 3.1 has a simpler alternative in line of the arguments I provided.
- Please evaluate whether binarization (Proposition 3.2 and Section 3.3) is even needed, as working with integers seems to be more efficient than decomposing their arithmetic.
- Please clarify how the training is done regarding the data (separation into training/evaluation/test sets, etc.)
- The common operation in scalar quantization is to perform rounding (e.g., floor(x + 0.5)) instead of truncation as it yields a lower quantization error. Why are the authors using truncation in Equation (7)?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Binary Hyperbolic Embeddings, an approach to vector similarity search that take the advantages of binarised hyperbolic space. The objective is to combine the fast retrieval capabilities of binary operations with the compact and hierarchical properties of hyperbolic embeddings. While hyperbolic space is effective to capture hierarchical relationships, its practical applications show low computational efficiency of metric calculations. This study addresses these challenges by transforming hyperbolic similarity metrics into binary Hamming distance operations, enabling faster and more efficient retrieval.

### Strengths
1. A key contribution in this paper is the proof of retrieval equivalence. The authors show that search results obtained using hyperbolic distance remain identical when replaced with Hamming distance, given certain conditions. This allows the method to maintain the quality of retrieval outcomes while significantly reducing computational overhead. 

2. Another key contribution is the integration of their approach with FAISS. By combining their binary hyperbolic method within FAISS, the authors present improvements in both memory usage and processing speed, without compromising the precision achieved with full-precision embeddings. 

3. The paper also highlights the robustness of binary hyperbolic embeddings in preserving retrieval quality across a wide range of datasets. This characteristic is particularly beneficial for tasks that involve hierarchical structures, such as image or video retrieval. They evaluate the performance across several datasets, including CIFAR100, ImageNet1K, and Moments in Time. 

4. Additionally, the study explores the trade-offs between memory efficiency, retrieval speed, and accuracy. Their experimental results show that binary hyperbolic embeddings not only meet but often surpass the performance of other state-of-the-art methods. 

Overall, Binary Hyperbolic Embeddings present a practical and powerful solution for similarity search, especially in large-scale scenarios where fast processing and memory optimisation are essential. This approach successfully bridges the gap between the theoretical strengths of hyperbolic space and the practical demands for efficient, scalable retrieval systems.

### Weaknesses
For experiment:
1.	In the captain of Table 1, “Our binary hyperbolic embeddings at 512 bits can maintain this performance while being much faster to evaluate, thereby getting the best of both worlds.”  I cannot find the time cost comparison of different methods regarding these three datasets. The claim of faster evaluation lacks concrete evidence within the table itself, making it difficult to assess the actual speedup achieved by the proposed binary hyperbolic embeddings compared to other methods. The absence of explicit time measurements for each method in Table 1 makes the comparison subjective and weakens the claim of superior speed.
2.	In line 346-347, “On ImageNet1K, we obtain a mAP@50 of 63.44% compared to 63.24% and 63.14% for the Euclidean and hyperspherical baselines.”  I am confused on what this statement is trying to show. Statistically, the mAP of 0.6344 (std 0.0011) is not significantly better than 0.6314 (std 0.019) or 0.6324 (std 0.0037). You might present more description for this statement, or use other results to favour your hypothesis. The reported mAP differences are marginal and fall within the standard deviations, which raises concerns about the statistical significance of the claimed improvements. The lack of a proper statistical test to validate the improvements further weakens the argument.

For theory:
Since the binary hyperbolic embeddings is an approximate method, it is worthy to discuss its relationship with the sketching methods such as LSH methods.

### Questions
Can you discuss the relationship of binary hyperbolic embeddings with sketching methods such as LSH and random projection?

Minor comments:
1.	SmAP is not defined in the main manuscript, but in Appendix.
2.	Figure 3 is not discussed in the main context.
3.	Line 368-369, no Figure 4.3 found in manuscript.
4.	Line 369-370, “The trade-off between embedding dimensions and quantization levels on ImageNet1K.” is not a full sentence.

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
3

### Summary
This paper proposes a method, Binary Hyperbolic Embeddings, that combines the advantages of Binary Euclidean and Hyperbolic embeddings, offering both speed and low dimensionality.

### Strengths
The paper is highly original and novel, with well-substantiated arguments and no overclaims.

### Weaknesses
1. Some tables are not expressed appropriately; for instance, using "s" to indicate speed in Table 3.
2. Some figures are not expressed appropriately; for example, in Figure 1, the image comparing Binary Hyperbolic and Hyperbolic embeddings does not clearly convey the concept of "Binary."

### Questions
1. What is the cost (in terms of time and space complexity) when transitioning from Euclidean to Binary Hyperbolic?
2. In which other scenarios does this method still perform less effectively?

### Soundness
2

### Presentation
2

### Contribution
3
