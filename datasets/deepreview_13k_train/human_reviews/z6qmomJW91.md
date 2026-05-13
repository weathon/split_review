# RotRNN: Modelling Long Sequences with Rotations

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Linear recurrent neural networks, such as State Space Models (SSMs) and Linear Recurrent Units (LRUs), have recently shown state-of-the-art performance on long sequence modelling benchmarks. Despite their success, their empirical performance is not well understood and they come with a number of drawbacks, most notably their complex initialisation and normalisation schemes. In this work, we address some of these issues by proposing \model{} -- a linear recurrent model which utilises the convenient properties of rotation matrices. We show that \model provides a simple and efficient model with a robust normalisation procedure,
and a practical implementation that remains faithful to its theoretical derivation. \model also achieves competitive performance to state-of-the-art linear recurrent models on several long sequence modelling datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new linear recurrent model using rotation matrices. The aim of introducing rotation matrices is to enforce the theoretical constraints of LRU that are missing in its practical implementation. Parametrizing recurrent state matrix as rotations allows the authors to present a fast method of matrix powers and also allows then to present a normalization process that helps near constant hidden state norms, both of these are essential for linear RNNs especially in long sequence domain.

### Strengths
*  Good theoretical justification of parametrizing recurrent state matrix as rotation matrix:
    * Show how rotations can be easily decomposed for efficient matrix power computation
    * Show how orthogonality of rotation matrices is used for normalization, leading to almost constant hidden state norms

* Very effective normalization enabled by the orthogonality of rotation matrices (as seen in figure 3) ensuring that hidden state norms do not vanish/explode across long sequences, which is important for stable training.

* Reproducibility: detailed hyperparameters and jax code are provided for reproducibility.

### Weaknesses
 * The proposed approach does not seem to improve the performance on the LRA benchmarks. As shown in the table 1, the proposed approach is better than baselines only on text and that too with a very small margin. While on other benchmarks and on average, it performs significantly worse (upto 10 percent points in case of Path-X).

* Also on speech commands classification task of table 2, the proposed approach is not better than any of the shown baselines.

* Although the proposed implementations using rotation matrices in this paper enables theoretical constraints of LRU, they don’t improve the performance on downstream tasks. Also, the paper does not show how efficient the proposed method is compared to the baselines in terms of compute/resource use. Specifically, the paper lacks a detailed analysis of computational cost, such as FLOPs or wall-clock time, for training and inference. This makes it difficult to assess the practical value of the proposed method, especially since it does not offer significant performance improvements. The absence of such analysis raises concerns about whether the theoretical benefits translate into practical advantages.

### Questions
The authors never concretely show (in terms of any sensible metrics, such as GPU hours etc) how efficient their model is compared to the baselines. It would be great if they could do a more thorough job at comparing their models against the baselines. The value of this question is particularly important, especially since their model performance is not significantly better than the baselines. Why wasn't their model compared rigorously in terms of efficiency?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper presents a linear state space model, where the recurrent state is transformed by a rotation matrix, A, that is an exact rotation matrix, and input is transformed by an input matrix. In prior works like LRU, careful initialization is performed to ensure that the rotation matrices at the start of learning are orthogonal and that outputs of the state space model are real values . However, as training proceeds, it is possible that complex parts arrive and are ignored. In this paper, the authors propose RotRNN - a parameterization of rotation matrices that is exact (although it doesn't cover the space of all rotation matrices, if I understood correctly). To do this, the authors show that any general matrix M can be smoothly mapped to the special orthogonal group by taking the matrix exponential of M-M^t.  Now, P = exp(M-M^T) can be mapped to the special orthogonal group rotation matrix A, through a block diagonal matrix $\theta$ by A= $ P \theta P^t$.
Using this scheme orthogonal recurrent rotation matrices can be generated. 

Aside from ensuring that an orthogonal rotation matrix can be produced, the authors also ensure that the hidden state $x_t$ is well behaved an preserves a constant norm in expectation. This is performed by using a normalization constant $\alpha$ to counteract the decay factor $\gamma$ applied to the rotation of the recurrent states. In practice this is actually done by rescaling the output of the application of the input matrix to the input.


Results of using the method are shown on LRA benchmarks and on Raw Speech classification using the Speech Commands classification task.

### Strengths
While I didn't look at the detailed linear algebra proofs, they seemed correct to me mathematically and made sound intuitive sense. There are also results showing that norms of the state are well preserved when the model is run, so that part of the proposal also seems to work well. The provided Jax code also makes it clear to see how the implementation matches the technical details of the paper.

### Weaknesses
While I am moved by the simplicity of their parameterization compared to prior works, I am not sure if the contribution is enough to merit a paper in ICRL with the kind of experimental exploration performed. I think a proper paper would run much further with the proposed method than the author(s) have done here. Speech commands is quite a small dataset and the results on it, and on LRA shed little light into the details of their method. And the results on these datasets are not necessarily better than prior methods. So the selling point of the method from a standpoint of improved results over LRU is not clear. Furthermore, other than showing the norms of the states are well behaved, the paper does not offer more technical insight either, for others to build upon. Without that, this is more of an exposition of a mathematical trick rather than a full contribution.

### Questions
How well do you think this model can scale up, compared to other approaches ? 
Does it interact well as a preprocessing layer into transformer based models ? 
The block diagonal matrices look like blocks of rotations in 2D. Are these the only kinds of block rotation matrices that are possible for theta ? 
Is it possible to control the periodicity of rotations using the block diagonal 'blocks' in some way ?

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
3

### Summary
State-based models have reduced the long-path problem of traditional recurrent models, but require complicated initialization procedures in order to avoid vanishing/exploding gradients.  This paper demonstrates a new linear recurrent unit in which the recurrence is constrained to be a rotation, scaled by a head-wise decay constant.  The head-wise decay constant is matched to the amplitude of the input coefficients, in order to guarantee that the magnitude of the state vector remains constant over time, avoiding the vanishing/exploding gradient problem without complicated initialization procedures.

### Strengths
The factorization of the linear recurrence matrix into cosine and sine rotations is elegant, and was a pleasure to read.

### Weaknesses
The key weakness of this paper is a minor oversight in the analysis of LRU, which calls into question the value of this paper's contribution.

The proposed algorithm is very similar to LRU, except that it forces the eigenvalues of the recurrence matrix to come in complex conjugate pairs.  The manuscript notes this as a weakness of LRU: that LRU does not require the eigenvalues to come in complex conjugate pairs, and instead, LRU simply takes the real part of the output of the linear layer.   It seems that the authors of this paper do not realize that taking the real part of the output of the network solves the problem of arranging eigenvalues into complex conjugate pairs, because the real part of any complex number is the average of the complex number and its complex conjugate: Re(z) = (z+z*)/2.  Thus, if z(t)=P Lambda^t P^T z(0), and if z(0) is real, then Re(z) = (1/2)(P Lambda^t P^T + P* Lambda*^t P*^T) z(0).  By taking the real part of the output, LRU is pairing each explicit eigenvalue with an implicit eigenvalue equal to the complex conjugate of the explicit eigenvalue, thus effectively doubling the dimension of the recurrent layer, at no extra computational cost. 

Since LRU already has each eigenvalue paired with an implicit conjugate eigenvalue, the only remaining difference I can see between the proposed algorithm and LRU is the proposed input normalization, which guarantees that the recurrent state vector maintains constant norm.  In theory, this seems like a useful contribution, since it explicitly avoids gradient vanishing/explosion.  In practice, it's not clear that LRU suffers from problems of gradient vanishing or explosion.  In the example shown, the norm of LRU gets large, but it never seems to overflow.  The proposed algorithm has better performance than LRU on a toy example, but it is not clear that the difference is statistically significant.

### Questions
Given that the real-part operation at the output of LRU implicitly pairs each eigenvalue with its complex conjugate, what are the remaining important differences between the proposed algorithm and LRU?

Which of the performance differences shown are statistically significant?

### Soundness
3

### Presentation
3

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
This paper proposes a new class of linear recurrent unit (LRU) which is uprising efficient state-of-the-art model class for long-range sequence modeling. The proposed model, RotRNN, utilizes rotation matrix-based parameterization for state transformation and the explicit normalization method. Based on strong mathematical backgrounds, RotRNN could be simply implemented and strictly guarantees preservation of hidden state magnitude across time-steps. This paper compares RotRNN with former LRU and state space models (SSMs) in theory and experiments to give in-depth understanding for readers.

### Strengths
Rigorous mathematical background: The math backgrounds behind the rotation matrix-based parameterization and explicit normalization method are proved with easy-to-read derivations. In addition, those backgrounds lead the simple implementation of RotRNN. 

In-depth comparison between former architectures: The theoretic comparisons between RotRNN and (LRU/SSM) are helpful to posit RotRNN within this field.

Strong, latest baselines: This paper compares RotRNN with latest and state-of-the-art baselines (such as S5 and Liquid-S4) in long-range sequence modeling benchmarks.

### Weaknesses
Majors:
- Limitation of rotation matrix parameterization: I think there would be drawback with constraining state transformation matrix to be rotation matrix, which might limit expression power of the model. Specifically, the rotation matrix parameterization, while ensuring norm preservation, may restrict the model's ability to learn complex, non-orthogonal transformations of the hidden state. This could be a significant limitation when dealing with data that requires more flexible state transitions. The constraint to rotations might prevent the model from capturing certain types of dependencies that a more general matrix could represent.
- Potential drawback of explicit normalization method: It is unclear that whether the explicit normalization method is beneficial for performance. I understand that this method constrains the operation to target a specific range of dependency based on the trained value of $gamma$, so it looks constraining the model’s expressivity. Although it successfully guarantees the converged norm of hidden states during training, its performance-wise effect is not demonstrated in results. An ablation study would be helpful to see its benefit. The explicit normalization, while preventing exploding or vanishing gradients, might also limit the model's capacity to learn diverse temporal dynamics. By forcing the hidden state to a specific norm, the model might lose the ability to represent subtle variations in the input sequence that could be crucial for performance. The lack of ablation studies makes it difficult to assess whether this constraint is beneficial or detrimental.
- Overall, it is questionable how RotRNN could be advantageous in practice. Comparison of computational efficiency (in terms of FLOPS) would be helpful to show that RotRNN is ‘efficient to compute’. Without a clear demonstration of computational advantages, it is difficult to justify the practical use of RotRNN over existing methods. The paper should provide a detailed analysis of the computational cost of RotRNN, including FLOPS, memory usage, and training time, compared to other state-of-the-art models.

Minors:
- Weak motivations for rotation matrix parameterization: The three motivations written at the beginning of section 3 aim to simple implementation thanks to the rotation matrix parameterization. However, there is no motivation related to hidden state processing despite of rotation matrix’s unique characteristic (such as regularity). And, it is not clear why real-valued matrix can make it robust to initialization? The motivation for using a rotation matrix is primarily focused on implementation simplicity, but it lacks a strong justification in terms of the model's representational capacity. The paper should elaborate on why the specific properties of rotation matrices, such as their orthogonality and norm-preserving nature, are beneficial for hidden state processing, beyond just ease of implementation. The claim that real-valued matrices make it robust to initialization is not clear and requires further explanation.
- Arguable interpretations of experiment results: The sentence “we find that our model performs best on domains with more discrete input data, such as ListOps, Text and Retrieval, achieving the highest score of all the baselines” seems not clear from the result table. Except ‘Text’ task, Liquid-S4 and S5 achieved the highest scores in ListOps and Retrieval tasks, respectively. The interpretation of the experimental results is not entirely accurate. The claim that RotRNN performs best on domains with discrete input data is not fully supported by the results, as other models achieve higher scores on some of these tasks. The paper should provide a more nuanced analysis of the results, acknowledging the strengths and weaknesses of RotRNN across different tasks.
- Confronting claims: This paper argues the unnecessity of SSM model’s theory-based initialization method (HiPPO) in practice (Section 2.3). However, this paper aims to build RotRNN on rigorous theoretic backgrounds. I think those claims are confronting with each other. The paper's critique of theory-based initializations in SSMs seems inconsistent with its own emphasis on the theoretical underpinnings of RotRNN. The paper should clarify its position on the role of theory in model design and initialization, addressing the apparent contradiction.

### Questions
What does $A^{t-k}$ mean in Equation 2?

### Soundness
3

### Presentation
4

### Contribution
1
