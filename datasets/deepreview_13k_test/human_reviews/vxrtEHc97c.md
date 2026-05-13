# LagEncoder: A Non-Parametric Method for Representation Learning

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
Non-parametric encoders offer advantages in interpretability and generalizability. However, they often perform significantly worse than deep neural networks on many challenging recognition tasks, and it remains unclear how to effectively apply these techniques to such tasks. In this work, we view all AI recognition tasks as function approximation problems and introduce LagEncoder, a non-parametric, training-free feature extraction method based on finite element basis functions. Our encoder features a universal architecture that can be applied to various types of raw data and recognition tasks. We found that LagEncoder effectively overcomes the limitations of neural networks in regression problems, particularly when fitting multi-frequency functions. The LagEncoder-based model converges quickly and requires low training costs, as only the head is trained. Additionally, LagEncoder provides a parameter-efficient fine-tuning approach. Our experiments on the ImageNet-1K and WikiText dataset demonstrate that pre-trained models using LagEncoder achieve performance improvements within just one training epoch. Furthermore, it does not require adjustments to the original training recipe, extra training data, and the model's total parameters remain nearly unchanged. Our evaluation of the scaling law for model performance indicates that using the LagEncoder is more cost-effective than merely increasing the model size.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces LagEncoder, a non-parametric, training-free feature extraction method based on Lagrange basis function.

### Strengths
The method have some empirical success in terms of regression and NLP and CV tasks.

### Weaknesses
1. The figure 4 is really hard to see.
2. The Computer vision results imporvement is really minor. Considering the extra computation it needed, it doesn't supervise me there is some improvement
3. The paper doesn't provide a good reason why I want to use this methods.

### Questions
1. If you still need a trainable backbone, how can you have strong mathematical explainability? Or do you believe your method have better explainability than a trainable linear layer?

### Soundness
2

### Presentation
2

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
The paper presents LagEncoder, a nonparametric, training-free feature extraction method based on finite element basis
functions. 
The encoder can be combined with various model architecture withr reasonable performances. 
The experiments on the ImageNet dataset demonstrate that pre-trained models using
LagEncoder achieve performance improvements within just one training epoch.

### Strengths
The paper idea is novel and the results are encouraging.

### Weaknesses
The writing of the paper is super bad. It is very hard to track different symbols and the symbols sometimes are wrong.
1. In Eq.(4), the paper introduces p but never defined before or at the equation.
2. For matrix T, the meaning of the values in the matrix are never defined. In my understanding, each column of the matrix should describe the seven simplices relationship to the corresponding nodes. 
3. The relationship of i,j,k in Eq.(5) is not clearly defined. It takes me time to figure out the meaning of n, n_t and d.
4. In Algorithm 1, you introduced completely new symbol definitions compared to previous versions, which further decreases the readability of the paper.
5. In algorithm 2, what is v(i) in compute loss step? I would guess it is x(i).

### Questions
1. For the benchmark in NLP, what is the performance if the freedom n of LagEncoder increased?
2. The paper claims interpretability, which I completely did not see from experiments. I think some attributions to the input is the interpretability.  The experiments in 3.1.2 is unconvincing.
3. The few epochs extra training is very impressive. However, can this method be combined with original architecture and directly train from scratch? Will that also improve the performance? 
4. For the experiments in table 1, what is the performance change if we increase d and n?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes using the Finite Element Method (FEM) for training-free feature extraction, particularly using the Lagrange basis function. Furthermore, the paper re-derives the Lagrange basis to exploit parallelism in a deep learning setting. The proposed LagEncoder is universal and is demonstrated on regression, image classification, text classification. Since LagEncoder can have high computational demands when dealing with high dimensional data, the paper demonstrates how it can be incorporated as a parameter efficient fine-tuning method. Scaling laws show that LagEncoder can outperform purely scaling model size.

### Strengths
* To the best of my knowledge, application of the Finite Element Method for representation learning is a novel contribution. 
* Other contributions of the paper include tricks to adapt the Lagrange basis to a deep learning setting, e.g., a re-derivation that allows parallelism, incorporating it into PEFT modules. 
* Scaling laws show that incorporating LagEncoder with a negligible amount of parameters can reach the same performance as a scaled-up version of the base model. 
* Experiments are conducted for multiple domains: regression, vision, text classification. One particularly compelling result is matching a 6.13 million parameter word2vec model using only 256 parameters.

### Weaknesses
* The biggest limitation is addressed by the paper itself. It is extremely expensive to use LagEncoder directly on high dimensional data, which "restricts its direct application to large-scale datasets."
* For the NLP task, LagEncoder is compared against word2vec which is more than ten years old, limiting the relevancy of this evaluation. Can LagEncoder be incorporated in modern language models?
* For the vision tasks, the improvements from LagEncoder seem negligible with a fraction of a percent improvement. 
* The paper lacks comparison against other PEFT methods such as LoRA.

### Questions
* Can LagEncoder be incorporated in modern language models?
* How does LagEncoder compare against the widely used PEFT method LoRA? The PCA and residual mentioned in Section 2.3 are highly reminiscent of LoRA.

### Soundness
3

### Presentation
3

### Contribution
2
