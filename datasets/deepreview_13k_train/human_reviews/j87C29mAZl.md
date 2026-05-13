# On Expressive Power of Looped Transformers: Theoretical Analysis and Enhancement via Timestep Encoding

- Decision: Reject
- Scores: 6, 8, 3

## Abstract
Looped Transformers offer advantages in parameter efficiency and Turing completeness. However, their expressive power for function approximation and approximation rate remains underexplored. In this paper, we establish approximation rates of Looped Transformers by defining the concept of the modulus of continuity for sequence-to-sequence functions. This reveals a limitation specific to the looped architecture. That is, the analysis prompts us to incorporate scaling parameters for each loop, conditioned on timestep encoding. Experimental results demonstrate that increasing the number of loops enhances performance, with further gains achieved through the timestep encoding architecture.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into the approximation rate of Looped Transformers for continuous sequence-to-sequence functions, offering a comprehensive mathematical analysis of the strengths and limitations of looped architectures. Specifically, it examines Looped Transformers by defining critical concepts such as sequence, contextual, and token continuity, which significantly influence the approximation rate. The authors propose a single-loop topology for contextual mapping that requires only a single-layer network for universal approximation.
This paper's novel contribution is the introduction of a new time-stepping encoding method, which addresses the approximation errors typically associated with Looped Transformers. This method incorporates a time-dependent scaling parameter, effectively discretizing variations in the target function. The study demonstrates that time-dependent Looped Transformer models can mitigate approximation errors arising from contextual and token continuity issues.
Experimental results support these claims, showing that accuracy increases linearly with the number of loops when using timestep-encoded models, in contrast to time-dependent models, which tend to saturate in training and accuracy. Additionally, the proposed approach offers resource optimization by reducing the number of layers in the neural network and decreasing the number of parameters by approximately 90% compared to previous works.

### Strengths
The presented methodology introduces a novel approach that effectively addresses the known limitations of Looped Transformer model architectures. The paper provides a robust background, thoroughly reviewing previous studies in the field. It includes rigorous mathematical demonstrations that substantiate the claims, and the experimental results are consistent with these theoretical findings.

### Weaknesses
The redaction can be challenging to follow in certain sections, particularly where large equations are interspersed with text (e.g., Theorem 3.7, Lemma 4.2). To enhance clarity, it would be beneficial to include comparison charts against current Looped Transformer models. These charts would help to emphasize the advantages of the proposed methodology and illustrate the behavior observed across different models. Furthermore, the experimental section lacks a thorough ablation study, making it difficult to assess the individual contributions of the different components of the proposed time-stepping encoding method. For instance, the impact of the time-dependent scaling parameter and the single-loop topology should be analyzed separately. The paper also does not adequately discuss the computational overhead of the proposed method compared to standard Looped Transformers. While the authors claim a reduction in parameters, the computational cost of the time-dependent scaling parameter and its effect on training time should be explicitly addressed.

### Questions
Are you planning to scale up experiments by using different models? Is it anticipated to be feasible to apply the proposed architecture to different scenarios? Are there any future work plans?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a theoretical exploration of the expressive power of Looped Transformers, particularly regarding their function approximation capabilities. The study justifies that Looped Transformer, while offering parameter efficiency and Turing completeness, suffers from some limitations in the approximation rate, and it addresses it by introducing timestep encoding, which enhances expressive capacity by conditioning on time-dependent scaling factors.

### Strengths
1.	The paper is well-written. The problem formulation, theoretical analysis, and experimental results are described clearly. 
2.	The paper's contribution is relatively significant. It derives bounds on the approximation rate of a looped transformer to demonstrate the limited approximation ability. 
3.	The paper provides strong theoretical justifications that lead to its design (of timestep encoding) on loop transformers. In particular, looped architecture is revealed to have exponential asymptotic approximation rate decay, which leads to the incorporation of timestep encoding.

### Weaknesses
1.	The experimental validation is relatively limited. In particular, only one task is evaluated on the timestep encoded model compared with the baseline. The authors are encouraged to test on more tasks including basic ones (e.g. inductive heads) for better validation of the model improvement and use ablation studies for more detailed characterization.


### Questions
1.	How tight is the approximation rate bound derived from the paper? It would be interesting to see empirical results that validate equation (9) or (10).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper theoretically investigates the approximation capabilities of Looped Transformers. Through theoretical analysis, it is found that scaling parameters for each loop can enhance the expressive power of Looped Transformers.

### Strengths
One of the strengths of this paper is the detailed theoretical analysis, which is clearly articulated. The definitions of the notation are well presented, making the paper relatively easy to read.

### Weaknesses
My main concern lies with the novelty of the work. It is well known that Looped Transformers can be viewed as a type of tied-parameters transformer, and the universal approximation theory for transformers has already been extensively studied. Moreover, the theoretical analysis presented does not yield any novel conclusions regarding the training of Looped Transformers. The finding that performance increases with the number of loops does not seem particularly innovative. Therefore, I have not yet identified any significant conclusions from this work.

My second minor concern is that the theoretical research on Looped Transformers may have lost its research value. Looped Transformers were proposed to address tasks that transformers struggle with, which RNNs can accomplish easily, while also offering parameter efficiency. However, transformers have now completely supplanted RNNs in various domains through various training techniques. In the most critical application areas for transformers, such as autoregressive models and LLMs, Looped Transformers are not commonly used, and their performance does not match that of transformer architectures.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
1
