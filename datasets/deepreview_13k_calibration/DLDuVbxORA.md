# OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 8, 6

## Abstract
The recent paradigm shift to large-scale foundation models has brought about a new era for deep learning that, while has found great success in practice, has also been plagued by prohibitively expensive costs in terms of high memory consumption and compute. To mitigate these issues, there has been a concerted effort in post-hoc neural network pruning techniques that do not require costly retraining. Despite the considerable progress being made, existing methods often exhibit a steady drop in model performance as the compression increases. In this paper, we present a novel approach to compressing large transformers, coined OATS, that utilizes the second moment information in the input embeddings to decompose the model weights into a sum of sparse and low-rank matrices. Without any retraining, OATS achieves state-of-the-art performance when compressing models by up to $60\%$ on large language models such as Llama-3 and Phi-3 and vision transformers such as ViT and DINOv2 while delivering up to $1.37\times$ the CPU acceleration versus a model that was comparably pruned.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces OATS (Outlier-Aware Pruning Through Sparse and Low-Rank Decomposition), a method designed to compress large transformer models without the need for retraining. The central concept involves representing weight matrices as the sum of a sparse and low-rank matrix.

The authors propose an iterative alternating thresholding technique to compute the joint sparse and low-rank decomposition of a matrix. They also focus on preserving outliers by scaling weights according to input embeddings prior to decomposition. The results indicate that OATS performs effectively on both language and vision tasks, outperforming other pruning methods proposed for transformers across various compression levels and tasks. Additionally, OATS offers speed improvements on the CPU.

### Strengths
- The concept of compressing a model as a sum of a sparse and low-rank matrix is very promising. Unlike most prior methods, which focus on one approach, OATS leverages both to potentially enhance performance.

- OATS is retraining-free, which is crucial for practical applications where even a single backpropagation pass can be computationally prohibitive.

- The framework has been tested on state-of-the-art models like Llama and ViT, demonstrating competitive performance.

- The Alternating Thresholding technique in OATS heuristically finds an effective combination of low-rank and sparse components and accommodates different sparsity patterns.

- By scaling the weight matrix $W$ with a diagonal rescaling matrix $D$, OATS emphasizes outliers, enabling outlier-aware compression that avoids performance degradation.

### Weaknesses
One concern is that the method relies on multiple calls to truncated SVD, which can be computationally intensive. Specifically, finding the top-$r$ singular values of an $m \times n$ matrix has a time complexity of $O(mnr)$. Given that compression speed is a significant factor for practical applications, it would be helpful if the authors could clarify the time complexity and wall-clock time spent on the compression process of the overall algorithm. This would offer a more concrete understanding of its practicality. For instance, how does the compression time scale with the model size, the desired sparsity level, and the rank parameter? Providing a table comparing the compression time of OATS with other methods, such as standard pruning techniques, on benchmark models like Llama and ViT would be beneficial. Furthermore, a detailed breakdown of the time spent on each step of the algorithm, such as the SVD computation, the thresholding, and the scaling, would help identify potential bottlenecks.

### Questions
One potential extension of this work could involve incorporating quantization into the proposed framework. Although this addition may be a long shot, integrating quantization could make the model a unified approach to transformer compression. Could the authors provide insights on whether quantization can be integrated with their current framework, or if not, what are the main challenges?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces OATS, a novel compression technique for large-scale transformers that combines sparse and low-rank approximations to reduce memory and compute costs without requiring costly retraining. OATS scales model weights by the second moment of input embeddings to preserve essential outlier features in transformers, ensuring model performance is maintained during compression. This approach addresses the typical performance degradation seen with increasing compression in existing pruning methods.

### Strengths
+ Low-rankness plus sparsity is a good fit for compressing LLMs without retraining.
+ By separating the model into a sparse and a low-rank part, the approximation error can be theoretically reduced as the two parts can compensate for each other. 
+ This paper provides measurements for practical speedups on CPUs with existing sparse computation frameworks.

### Weaknesses
 - The novelty is limited. The combination of low-rankness and sparsity is an old topic that has been explored for many years [R1, R2]. Applying the well-established approximation techniques to decompose/compress the large matrices in LLMs has little technical contribution. Besides, compressing DNN models using low-rank and sparse decomposition has already been well explored in [R3]. This paper just scales it to larger models and matrices. Authors are encouraged to specify the unique difference from existing approaches and why this difference is also unique for LLMs.
- The proposed Truncated SVD and Threshold strategies to achieve low-rankness and sparsity are too trivial. It is unknown how to decide the rank and number of zeroes. Besides, the order of applying SVD and thresholding has a significant impact on the approximation errors. Authors are encouraged to clearly explain why using such decomposition strategies.
- This paper claims "outlier information" in this paper. However, I have not seen any analysis or explanation for the "outlier information," and the proposed solution is not related to the "outlier information." Instead, this paper seems to directly apply the pruning approaches proposed in Wanda. The authors are encouraged to provide explanations of why the diagonal matrix is related to "outlier information" and why it is good for compression.
- Many works have been proposed to compress LLMs with low-rankness and sparsity [R4-R6]. The authors have not presented the main differences among them and the unique contributions that stand out from those works.
- Even though theoretical analysis may not have a practical guarantee of accuracy, the authors are encouraged to provide.
- The paper presentation could be improved, especially the math equations.

### Questions
See the Weakness. Additionally, why use inverse transformation to reach the compressed weight? What is the actual speedup when using N:M sparsity on GPUs.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a relatively novel model compression technique aimed at Transformer architectures, in which weight matrices are approximated as a sum of a sparse and a low-rank matrix. To control for the (previously documented) outlier feature problem, weights are also scaled by the second moment of their input.

### Strengths
The method proposed by this paper is well-explained and well-justified. The actual practical algorithm is easy to follow. 

Real-time speedup is shown in the CPU setting.

The experiments cover a range of model sizes (3.8-14B parameters). I especially liked seeing results on fairly small models, since those may be harder to compress. 

Section 5 is an interesting way to look at the problem, which I think can lead to interesting further work in the direction of interpretability.

### Weaknesses
The choice of the rank ratio parameter could have been better explored (in particular, looking at multiple architectures/tasks). 

Typos:
Line 18: “approximating each weight” -> “approximating each weight matrix”
Line 142: “the activations are calculated through a calibration set that is propagated through the compressed layers” - should be uncompressed?

### Questions
It would be nice to see a bigger hyperparameter selection section with more architerctures considered.

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
4

### Summary
In this paper, the author presents a novel approach to compressing large transformers, coined OATS, that utilizes the second moment information in the input embeddings to decompose the model weights into a sum of sparse and low-rank matrices. The author also conducts a lot of experiments showing that OATS is able to consistently outperform prior state-of-the-art across multiple benchmarks and compression rates while also improving on speed-up.

### Strengths
1.This paper propose a novel method for large transformers compression that utilizes the second moment of the input embeddings to approximate the model’s weight matrices as a sum of a sparse matrix and a low-rank matrix.

2.Extensive experiments on recent large language models demonstrate the effectiveness of the proposed method, which also generalizes well to vision Transformers.

### Weaknesses
1. The author has clarified the differences between Wanda and OATS. However, an ablation study would further illustrate the impact of the low-rank term on performance. How much does the low-rank term contribute to the performance boost compared to Wanda alone?
2. The hardware speedup on GPU with N:M sparsity patterns can be shown and discussed in Section3.4.
3. The paper lacks details on how the sparsity pattern is defined for a matrix composed of a sparse matrix S plus a dense matrix LLL, especially within the context of N:M sparsity and structured pruning. Providing more detailed explanations would enhance clarity. 
4. The baseline for models are all originally designed for LLMs. It would be valuable to compare against pruning metrics specifically designed for ViTs. This would present a stronger baseline to effectively showcase the proposed method’s advantages.
5. The motivation behind the choice of outlier information for the sparse term S is not entirely clear. Given that there are various methods for selecting the sparse components, such as using magnitude-based or gradient-based criteria, it would be helpful to know if the authors experimented with these or other selection methods.
6. Given that most pruning studies report results on 70B-parameter models, has the author tested their method on larger language models, such as Llama2-70B or the newer Llama3-70B?

### Questions
1. The author has clarified the differences between Wanda and OATS. However, an ablation study would further illustrate the impact of the low-rank term on performance. How much does the low-rank term contribute to the performance boost compared to Wanda alone?
2. The hardware speedup on GPU with N:M sparsity patterns can be shown and discussed in Section3.4.
3. The paper lacks details on how the sparsity pattern is defined for a matrix composed of a sparse matrix S plus a dense matrix LLL, especially within the context of N:M sparsity and structured pruning. Providing more detailed explanations would enhance clarity. 
4. The baseline for models are all originally designed for LLMs. It would be valuable to compare against pruning metrics specifically designed for ViTs. This would present a stronger baseline to effectively showcase the proposed method’s advantages.
5. The motivation behind the choice of outlier information for the sparse term S is not entirely clear. Given that there are various methods for selecting the sparse components, such as using magnitude-based or gradient-based criteria, it would be helpful to know if the authors experimented with these or other selection methods.
6. Given that most pruning studies report results on 70B-parameter models, has the author tested their method on larger language models, such as Llama2-70B or the newer Llama3-70B?

### Soundness
3

### Presentation
2

### Contribution
3
