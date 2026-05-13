# PowerSoftmax: Towards secure LLM Inference Over Encrypted Data

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Modern cryptographic methods for implementing privacy-preserving LLMs such as \gls{HE} require the LLMs to have a polynomial form. Forming such a representation is challenging because Transformers include non-polynomial components, such as \Softmax and layer normalization. Previous approaches have either directly approximated pre-trained models with large-degree polynomials, which are less efficient over HE, or replaced non-polynomial components with easier-to-approximate primitives before training, e.g., \Softmax with pointwise attention. The latter approach might introduce scalability challenges. 

We present a new HE-friendly variant of self-attention that offers a stable form for training and is easy to approximate with polynomials for secure inference. Our work introduces the first polynomial LLMs with 32 layers and over a billion parameters, exceeding the size of previous models by more than tenfold. The resulting models demonstrate reasoning and in-context learning (ICL) capabilities comparable to standard transformers of the same size, representing a breakthrough in the field. Finally, we provide a detailed latency breakdown for each computation over encrypted data, paving the way for further optimization, and explore the differences in inductive bias between transformers relying on our HE-friendly variant and standard transformers. Our code is attached as a supplement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a modified version of the Transformer architecture, adapting it to the constraints of Homomorphic Encryption (HE) through a power-based self-attention variant that is compatible with polynomial representations. The proposed model achieves performance comparable to Softmax-based Transformers across multiple benchmarks while preserving the core design characteristics of self-attention. Additionally, the paper presents variants that incorporate length-agnostic approximations and enhanced numerical stability. This approach provides a more HE-friendly Transformer solution than previous methods, enabling efficient scalability to large language models with 32 layers and 1.4 billion parameters.

### Strengths
This paper proposes an HE-friendly self-attention variant, which minimizes non-polynomial operations while preserving the core principles of the attention mechanism. The approach is further extended by introducing a stable numerical training method and a length-agnostic computation strategy for inference, supporting secure and scalable inference. Leveraging this technique, the authors develop a polynomial variant of RoBERTa and train the largest polynomial model to date, comprising 32 Transformer layers and approximately 1.4 billion parameters.
Notably, this work expands the Approximation-Aware Training (AAT) approach for Transformers by replacing Softmax with a polynomial-friendly alternative, closely replicating its functionality. The proposed method enhances model performance and scalability while remaining compatible with homomorphic encryption operations.

### Weaknesses
The authors should provide critical information on latency and resource utilization, which is essential for assessing the feasibility of applying homomorphic encryption (HE) to transformers. Specifically, there is insufficient detail regarding the HE settings and parameters used, making it unclear what type of simulation was conducted. For instance, the specific choice of HE scheme (e.g., BFV, CKKS, or TFHE), the polynomial modulus degree, the ciphertext modulus size, and the noise variance are all crucial parameters that significantly impact both performance and security. Additionally, there is no information on the security model under which the HE simulations were performed. It is essential to specify the threat model (e.g., semi-honest, malicious) and the security level (e.g., 128-bit security). The description of the homomorphic implementation of matrix operations, including ciphertext-ciphertext multiplication beyond Softmax, needs to be included. The paper lacks details on how matrix multiplication is performed in HE, especially considering the ciphertext-ciphertext multiplications involved in the attention mechanism. This includes how the polynomial approximations are handled within the HE scheme and the associated computational overhead.

### Questions
The authors claim that their method is more efficient than existing approaches, even though no information is provided on latency. On what basis is this claimed efficiency over previous methods established? Additionally, what homomorphic encryption parameters were used in the simulations?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The most challenging aspect of implementing AI models based on homomorphic encryption is the implementation of nonlinear functions, such as softmax, in an encrypted state. This study aims to modify the Transformer model by reducing nonlinearity in the softmax function using a power function, thereby decreasing the homomorphic encryption computation load without compromising performance.

### Strengths
1. A very wide range of experiments was conducted.
- They experimented with various models, including BERT-based models, GPT-based models, and ViT-based models, and included many different tasks.
- The experiments also included models with different parameter sizes (e.g., 70M, 135M, 1.4B) and deep models with 32 layers.
- Since softmax is the main focus, they provided a comprehensive comparison of epsilon values used in softmax as well as a comparison with standard softmax, achieving thorough experimental results.
- They averaged results using three seeds, and all parameters used were recorded, indicating excellent reproducibility.

### Weaknesses
1. HE-based implementation was not conducted.
- They only referenced the time it takes for softmax in other papers, stating that their work could reduce that time by 6%.

2. Contribution seems limited.
- They introduced three modifications to the revised power-softmax:

       * Lipschitz Division

       * Stable PowerSoftmax

       * Length-Agnostic Range

- The first is simply adding epsilon to prevent division by zero, which, though not explicitly stated, is generally used in all implementations.
- The second scales the numerator and denominator of softmax, which is conceptually the same as dividing by maxX in regular softmax.
- The third, which involves using different functions for training and inference, was innovative. While producing the same output, it effectively narrows the range by applying the mean-based function for inference.
- Other methods like layernorm and range minimization are existing methods. In summary, the contributions boil down to introducing power-softmax and separating inference and training with length-agnostic range.

3. There is a reliability concern with the results of the zero-shot and 5-shot experiments.
- The paper states the following regarding the similar results in zero-shot and 5-shot experiments: 

      "These results mark a significant advancement, as no prior work has introduced polynomial LLMs with demonstrated ICL or reasoning capabilities. This is particularly evident on reasoning benchmarks such as AI2’s Reasoning Challenge (ARC), where our models perform competitively."

- However, the zero-shot and 5-shot results alone are insufficient to accurately gauge the effectiveness of the model. Due to the simplification of complex non-linear functions into a linear form, the initial convergence may be faster due to computational advantages, but it may not fully retain the non-linearity and expressive power of the original softmax. Showing fully-trained results would be more appropriate.

### Questions
See the weakness.

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
This paper introduces a variant of the self-attention module that reduces the overhead of Homomorphic Encryption (HE) computation during private Transformer inference. The authors first replace the exponential scaling in the original SoftMax function with polynomial scaling in the proposed PowerSoftMax function. The authors further introduce a stable variant of PowerSoftMax with Lipschitz division and division invariant, and a length-agnostic variant of PowerSoftMax with pre-computation. Experiments show that the proposed PowerSoftMax-based Transformers maintain reasoning and in-context learning (ICL) capabilities. The authors also offer a latency breakdown.

### Strengths
1. The research question is important and timely. Protecting the privacy of user data is important in LLM inference.
2. The proposed methods effectively improve the efficiency of the self-attention module during HE-based private LLM inference.
3. The evaluation and analysis are detailed. The authors present the source code and detailed results.

### Weaknesses
 1. The novelty is limited. Replacing non-polynomial functions (e.g., the exponential function) with polynomial counterparts is a commonly used technique in private LLM inference works. While the authors also propose to integrate techniques like Lipschitz division and division invariant (Section 4.3 and 4.4) to enhance the stability of the proposed PowerSoftMax function, strategies like pre-computation (Section 4.5) to improve the efficiency of the division operation, many of these techniques seem incremental upon existing works.
2. The scalability is questionable. While the authors show that the proposed PowerSoftMax-based Transformer can achieve similar reasoning capability as the SoftMax-based counterparts, the proposed method requires training from scratch. Retraining the LLMs is often impractical. Despite the authors trying to show the proposed methods are effective for a 32-layer Transformer, I am still concerned about how the proposed method can scale to large models.
3. The threat model is not clear. Although the authors briefly described the problem setting in Section 3, the security threats remain unclear to me. For example, it remains unclear why the model weights should be encrypted if there are only two parties. The threat model should be clarified with respect to the capability of the involved parties (e.g., client, model provider, and server) and the capability of the adversaries. Additionally, the security description about HE in untrusted environments is not accurate (line 109). In untrusted environments, HE also suffers from verifiability issues and side-channel attacks.
4. The HE experiments are not clear or comprehensive. While the main objective of this paper is HE-based private LLM inference, the only experiment related to HE I can find is in Figure 3, which is not clear to me. There is also a lack of comparisons with related works or baselines, making the evaluation of the proposed method not comprehensive.
5. There is some inconsistency in the presentation. For example, in Section 4.3, the authors introduce the division invariant property of the proposed PowerSoftmax. Yet, in Figure 2, it shows subtraction invariant ($x-\max(|x|)$). The readability should be enhanced.

### Questions
1. The breakdown in Figure 3 does not include the latency of the GELU function. Is the GELU function not used? Is SoftMax the main bottleneck during private inference?
2. If the model weights need to be encoded and encrypted, is this a one-time process that can be performed offline?
3. What is the multiplicative depth set in the HE experiments? Is bootstrapping performed after each operation (since every bar in Figure 3 contains bootstrapping)?
4. How do you decide the parameter $p$, the degree of the polynomial, in PowerSoftMax in practice? The choice of $p$ is pivotal since it determines the efficiency-utility trade-offs.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new HE-friendly self-attention layer for privacy-preserving transformer inference. The authors introduce two new variants of HE-friendly attention for model training and inference, respectively, and proposed a polynomial transformer construction algorithm. Finally, the authors conduct empirical studies to validate the effectiveness of the proposed method.

### Strengths
The main advantages can be listed as follows:

1.	The paper proposes a new HE-friendly attention by analysing the important properties the attention layer should have. The proposed variants of attention have better numerical stability for training, and can be transformed into polynomial.
2.	The paper conducts experiments and ablation studies on 8 datasets to show the effectiveness of the proposed method.

### Weaknesses
Despite the strengths, there are some issues with the paper as follows:

1.	The writing could be further improved. For example, $\epsilon’$ in Eqn. (5) and $\odot$ in Eqn. (9) are not defined ($\odot$ in Line 77 only defined for two ciphertext numbers, rather than matrices). Additionally, "x" in Line 258 should be written as "$x$". Moreover, Furthermore, Line 219 references Eqn. (6) without any prior description, making it challenging to follow the content.
2.	I am concerned about the novelty of this paper’s contributions. The main contribution appears to be the proposed attention layer, as described in Eqns. (4) and (6). However, other techniques such as the supplementary training procedure and polynomial approximations, are adapted from previous works rather than newly introduced. Furthermore, the $l_\infty$-norm regularizer introduced in Eqn. (8) is a well-known technique, which further diminishes the novelty of the proposed method.
3.	The paper’s significance may be limited without a detailed latency comparison for HE-based inference. Although the authors claim to present the first private LLM with 1B parameters, the primary challenge for HE-based large-scale models lies in the high latency of HE operations (in other words, building large-scale models is trivial if latency is disregarded). The paper lacks inference accuracy and latency comparisons with prior studies. Including such comparisons would significantly enhance the evaluation of the proposed method's effectiveness.

### Questions
1.	What is the inference latency of the proposed method, and how does it compare with previous HE-based neural network methods?
2.	In line 218, it is stated that “it is clear that Eq. (2) and Eq. (6) can lead to training instability…”. Could the authors provide a more detailed explanation regarding this point?

### Soundness
3

### Presentation
2

### Contribution
2
