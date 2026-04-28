# Qinco2: Vector Compression and Search with Improved  Implicit Neural Codebooks

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Vector quantization is a fundamental technique for compression and large-scale nearest neighbor search. For high-accuracy operating points, multi-codebook quantization associates  data vectors with one element from each of multiple codebooks. An example is residual quantization (RQ), which iteratively quantizes the residual error of previous steps. Dependencies between the different parts of the code are, however, ignored in RQ, which leads to suboptimal rate-distortion performance. Qinco recently addressed this inefficiency by using a neural network to determine the quantization codebook in RQ based on the vector reconstruction from previous steps. In this paper we introduce Qinco2 which  extends and improves Qinco with (i) improved  vector encoding using  codeword pre-selection and beam-search, (ii) a fast  approximate decoder leveraging codeword pairs to establish  accurate short-lists for search, and (iii) an optimized training procedure and network architecture. We conduct experiments on four datasets to evaluate Qinco2 for vector compression and billion-scale nearest neighbor  search. We obtain outstanding results  in both settings, improving the state-of-the-art reconstruction MSE by 44% for 16-byte vector compression on BigANN, and search accuracy by 24% with 8-byte encodings on Deep1M.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a variant of QINCo which predicts codebooks per step according to the previous encode part. QINCov2 develops many tricks such as a better training procedure, beam search, etc., to improve its performance. Extensive experiments across multiple benchmark datasets demonstrate its superior performance.

### Strengths
- The proposed method achieves state-of-the-art performance on several benchmarks
- Extensive experiments demonstrate the effectiveness of each component.

### Weaknesses
 - The task scenarios are not convincing. Previous work shows that QINCo [1] has significantly lower encoding and decoding speeds than PQ and RQ, and there is no obvious improvement in the paper. Figure 6 also shows nearly an order of magnitude less QPS than PQ/RQ in the low recall region. The authors should provide more explanation of why improving accuracy at the cost of QPS is necessary.
- Latency comparison with other methods is not considered in experiments.

### Questions
- Figure 6 demonstrates the retrieval accuracy/efficiency trade-off, but only R@1 is considered. How would the QPS/task accuracy trade-off be affected if a re-rank stage is added to RQ and PQ with relaxed settings such as R@10?
- Figure 4 only demonstrates the encoding/decoding speed of QINCov2. It is recommended to provide a more comprehensive comparison with QINCo, etc., similar to Table 3 in [1].
- It is advised to add a latency comparison of the full retrieval pipeline with other methods.

[1] Residual Quantization with Implicit Neural Codebooks

### Soundness
2

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
3

### Summary
The paper presents QINCO2, an advanced method for vector compression and large-scale nearest neighbor search, building on the QINCO framework. QINCO2 introduces several key enhancements to improve the efficiency and accuracy of vector quantization, including: (i) QINCO2 incorporates codeword pre-selection and beam search, which improve encoding precision without exhaustive evaluations of all codebook options; (ii) an approximate decoder based on codeword pairs; (iii) an optimized training approach. The paper validates QINCO2's performance on datasets such as BigANN and Deep1M, demonstrating substantial improvements.

### Strengths
1. QINCO2’s use of beam search for vector encoding and codeword pre-selection represents a significant advancement over previous methods, optimizing both encoding time and quantization accuracy.
2. The introduction of a fast, approximate decoder based on codeword pairs offers a novel solution to the computational challenges of large-scale vector search, enhancing speed without a major sacrifice in accuracy.
3. The paper conducts thorough empirical evaluations across multiple datasets, showing substantial reductions in mean squared error (MSE) for vector compression and improvements in search accuracy compared to the original QINCO and other state-of-the-art models.

### Weaknesses
1. It would be beneficial to compare QINCO2 with other non-uniform quantization methods, specifically those that employ adaptive codebook selection or dynamic bit allocation, to better contextualize its performance gains. Furthermore, the paper should explore the potential for extending QINCO or QINCO2 to work with other large language models (LLMs), such as the LLaMA family, by investigating how the method could be adapted to handle different embedding spaces and dimensionality. 
2. The inference time remains high, especially in large-scale applications, which limits the practical applicability of the method in real-time scenarios. The paper should provide a more detailed analysis of the computational bottlenecks and explore potential optimization strategies, such as hardware acceleration or algorithmic improvements, to reduce the latency.
3. This method requires multiple heuristics and iterative steps to reach an optimal solution, which makes it appear more like a refinement rather than a groundbreaking improvement over QINCO. The reliance on iterative training and hyperparameter tuning could limit the robustness and generalizability of the approach. Including more mathematical analysis or theoretical proofs, particularly regarding the convergence properties of the beam search and the optimality of the codeword pre-selection, would strengthen the approach.
4. In line 205, you mention that "$g$ uses the same architecture as $f$." Did you experiment with alternative architectures for $g$, such as a simpler linear projection or a shallow neural network, and if so, what were the trade-offs in terms of computational cost and accuracy? A more detailed discussion of the design choices for $g$ is needed.
5. In Figure 2, you note "Keep A candidates for each beam." Did you consider keeping a single candidate set for multiple beams, and if so, what were the effects on the search accuracy and computational efficiency? Exploring the impact of sharing candidate sets could provide insights into potential optimizations.

### Questions
Please refer to Weakness.

### Soundness
3

### Presentation
3

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
QINCo2 is a deep-learning based vector quantizer that improves off of QINCo. The basic idea of both is to extend the idea of residual quantization (RQ) via deep learning. RQ is a greedy approach that quantizes a vector by doing each successive codeword selection to minimize the assignment loss so far. The QINCo family of quantizers adds a neural network that adapts the current codeword depending on the quantized representation so far, i.e. if $\hat{x}_i$ is the quantized representation of $x$ after $i$ codes, RQ does $\hat{x}_i=\hat{x}\_{i-1}+c_i$ while QINCo does $\hat{x}_i=\hat{x}\_{i-1}+f(c_i,\hat{x}\_{i-1})$ with learned $f$.

The main improvements from the original QINCo are:
1. Faster encoding by leveraging a faster, approximate $f$ to generate initial quantization candidates, and only re-ranking the top candidates with the full $f$.
1. Beam search during encoding, to make up for quality loss from approximate $f$ above.
1. Slight tweaks to model architecture and training hyperparameters.
1. Using a pairwise codebook procedure during decoding so that the vanilla additive decoder more closely resembles QINCo's implicit codebook results.

### Strengths
1. Figures are well-crafted and make the paper easy to understand
1. Extensive empirical results that break down the effect on quantization quality and encode/decode time for each adjustment relative to QINCo

### Weaknesses
1. Lack of source code release: considering these are fairly small models trained on open datasets, releasing code for reproducibility shouldn't have been difficult.
1. Limited novelty: this work only only suggests a minor change to the QINCo idea.



### Questions
1. A detailed description of an ANN use case that clearly benefits from QINCo2 would strengthen this paper. This paper currently shows that QINCo2 outperforms other quantizers at iso-bitrate in terms of quantization error, but pays more in terms of decoding cost. It could perhaps be argued that using other quantization methods to compress the vectors, and storing such compressed data on a cheaper storage medium (ex. flash) could perhaps beat QINCo2 in both storage cost and decoding cost. Quantifying whether or not this is the case would be very useful.
1. Source code?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
QINCO2 is an improved version of the original QINCO model for residual MCQ. It improves search efficiency in large datasets and reconstruction error. Both methods use neural network to dynamically adapt codebooks after each step of residual quantization. Instead of static codebook (conventional RQ), QINCO2 (and QINCO) uses neural network to adjust the codebook based on the current approximation and base codebook values. The network inputs the residual vector and partial reconstruction and produces centroids that more accurately encode the residuals. The original QINCO dramatically increased computational complexity of the quantization process and memory usage.
QINCO2 improves encoding speed by introducing codeword pre-selection which narrows down the search of centroids. It uses another neural network of smaller parameters to calculate top $A$ candidates (among possible centroids) which is further used for adaptive quantization. Furthermore, QINCO2 applies beam search to improve quantization quality by exploring multiple encoding paths in parallel, which helps to minimize the quantization error and refine the encoded representation more accurately.
To address the high computational cost during decoding, QINCO2 introduces a pairwise additive decoder, which enables faster approximate decoding by combining pairs of codewords, effectively capturing dependencies between codewords

### Strengths
- Proposed method significantly improves quantization error and retrieval accuracy
- It is faster for retrieval tasks, which is important for industry scale applications

### Weaknesses
The theoretical contribution is rather low. Authors mainly engineered existing methods together to improve inference of the model.
The paper is very hard to follow, it is not completely clear why introducing another neural network for pre-selection can speed it up (furthermore, increasing training training time)

Both this paper and the original Qinco paper leave the optimization process of the model somewhat unclear. While the presented loss function is non-differentiable, the authors state that SGD is employed, yet they provide only vague details about how the optimization is actually carried out.

The comparison of the proposed method to conventional RQ and PQ methods is conducted in the R@1 setting, which is unusual. Typically, comparisons are made in more relaxed settings, such as R@5 or R@10. Furthermore, the proposed method is significantly slower than traditional approaches. In more relaxed settings, it is possible that the recall gap between the methods would narrow considerably (while the decoding time would still be much slower).

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper enhances QINCo in both the encoding and decoding processes. To tackle the significant complexity of encoding, the authors introduce codeword pre-selection and beam search strategies, which improve encoding efficiency and approximation capabilities. Additionally, to mitigate the limited search accuracy of the AQ decoder, the authors propose a fast approximate decoder based on pairwise additive code, which creates accurate shortlists for fast searching. Experimental results demonstrate that QINCo2 improves both efficiency and search accuracy.

### Strengths
1.	The proposed method seems concise and effective, especially in speeding-up the QINCo encoding and searching process.
2.	The pairwise additive decoding looks like an effective tool to create more accurate approximation of non-independent neural codebooks.
3.	The experiments and analysis are quite extensive and the improvements are significant. 
4.	The paper is well-written and easy to read.

### Weaknesses
1.	In Table 3, “Improved Architecture” slightly improves the search accuracy on BigANN and Deep datasets with lower vector dimension. Since the performance of original QINCo is largely affected by the network scale, the question is whether the “Improved Architecture” in QINCo2 affects the performance by improving the network parameters. It is better to provide the comparison of parameters, specifically detailing the number of layers, the size of each layer, and the activation functions used, to understand the architectural changes more thoroughly. A simple parameter count might not be sufficient to explain the performance gains.
2.	Compared to the original QINCo, the “Improved Training” approach used in this paper incorporates more training samples. Results in Table 3 shows that the introduction of large training set brings limited performance improvement. With a fixed training epoch of 70 and the sequential acquisition of each 10M splits, wonder if the model achieves optimal convergence with such a large training set. It would be beneficial to include a convergence analysis, showing the training loss over time for both the original QINCo and QINCo2, to justify the training procedure and the choice of 70 epochs. Also, it's unclear if the learning rate was adjusted during the training process with the increased dataset size, which could impact the convergence.

### Questions
1.	The dataset names in Table 3 should be consistent with other results in Sec. 4.2, i.e., BigANN1M, Deep1M, Contriever1M, and FB-ssnpp1M.
2.	A little confused on the “2M successive least-squares problems” in RQ-based codebook approximation (mentioned in Sec. 4.3), as there are only M steps in RQ.
3.	The R@10 and R@100 results of QINCo2 are not included in this paper, despite the authors' claim in Section 4.1 that recall percentages at ranks 1, 10, and 100 have all been considered.

### Soundness
3

### Presentation
3

### Contribution
3
