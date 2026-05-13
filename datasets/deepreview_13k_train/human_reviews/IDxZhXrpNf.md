# SOAP: Improving and Stabilizing Shampoo using Adam

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
There is growing evidence of the effectiveness of Shampoo, a higher-order preconditioning method, over Adam in deep learning optimization tasks. However, Shampoo's drawbacks include additional hyperparameters and computational overhead when compared to Adam, which only updates running averages of first- and second-moment quantities. This work establishes a formal connection between Shampoo (implemented with the 1/2 power) and Adafactor --- a memory-efficient approximation of Adam --- showing that Shampoo is equivalent to running Adafactor in the eigenbasis of Shampoo's preconditioner. This insight leads to the design of a simpler and computationally efficient algorithm: \textbf{S}hampo\textbf{O} with \textbf{A}dam in the \textbf{P}reconditioner's eigenbasis (SOAP).

With regards to improving Shampoo's computational efficiency, the most straightforward approach would be to simply compute Shampoo's eigendecomposition less frequently. 
Unfortunately, as our empirical results show, this leads to performance degradation that worsens with this frequency.
SOAP mitigates this degradation by continually updating the running average of the second moment, just as Adam does, but in the current (slowly changing) coordinate basis. Furthermore, since SOAP is equivalent to running Adam in a rotated space, it introduces only one additional hyperparameter (the preconditioning frequency) compared to Adam. We empirically evaluate SOAP on language model pre-training with 360m and 660m sized models. In the large batch regime, SOAP reduces the number of iterations by over 40\% and wall clock time by over 35\% compared to AdamW, with approximately 20\% improvements in both metrics compared to Shampoo.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces SOAP (ShampoO with Adam in the Preconditioner’s eigenbasis), an optimizer designed to improve the efficiency and stability of Shampoo by integrating Adam updates within Shampoo's eigenbasis. SOAP simplifies Shampoo by reducing its hyperparameters and computational overhead while maintaining its benefits.

### Strengths
(1)  This paper is well-organized.

(2) This work has significant implications for large language model training.

### Weaknesses
(1) The evaluation in this paper is limited, as it only tests the proposed SOAP on 360M and 660M language models. It is unclear whether SOAP can scale effectively to larger models, such as 1B or 7B, or how it performs in fine-tuning settings. Specifically, the paper lacks experiments demonstrating the optimizer's behavior with respect to increasing model size, a crucial aspect for practical applications in large language model training. The absence of such scaling experiments makes it difficult to assess the true potential of SOAP for state-of-the-art models.

(2) Given that SOAP is intended as a general optimizer, it would be valuable to assess its performance across diverse tasks, including vision and graph tasks, to better understand its generalization. The current evaluation is narrowly focused on language modeling, leaving open questions about its applicability to other domains. For instance, the optimizer's performance on tasks with different loss landscapes and data characteristics, such as image classification or node prediction on graphs, remains unknown.

(3) While the paper establishes a theoretical connection between Shampoo and Adafactor that motivates SOAP, it remains unclear why SOAP outperforms both Shampoo and Adam. The paper does not provide a detailed analysis of the optimization dynamics or convergence properties of SOAP that would explain its superior performance. Without a deeper understanding of the underlying mechanisms, it's challenging to assess the robustness and reliability of SOAP.

(4) Since SOAP is inspired by the connection between Adafactor and Shampoo, it is essential to include Adafactor as a baseline to fully evaluate SOAP's effectiveness. The absence of Adafactor as a comparison point makes it difficult to isolate the specific contributions of SOAP and to determine whether its performance gains are truly novel or simply a result of incorporating elements from Adafactor.

### Questions
(1) What's the performance of SOAP in other tasks such as vision and graph tasks?

(2) why can SOAP perform better than Shampoo? Is there any rationale behind this?

(3) What's the performance of SOAP in fine-tuning settings?

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
The paper establishes a connection between Shampoo and Adafactor and shows that Shampoo with the ½ power is equivalent to running Adafactor in the eigenbasis of Shampoo’s preconditioner. 
Building on this insight the paper proposes to continually update the running average of the second moment, just as Adam, but in the slowly changing coordinate basis. 
The new optimizer SOAP only introduces one additional hyperparameter (the preconditioning frequency) compared to Adam.
In language modeling experiments up to model sizes of 660m parameters the authors demonstrate that SOAP outperforms Adam and Shampoo on pre-training tasks.

### Strengths
This paper draw a novel connection between Shampoo and Adafactor, which has not been done before (to the best of my knowledge). 
The paper is very well written and clear in the description of its method. The authors also provide code.
In general the conducted experiments are very thorough (especially the experiments on batch size scaling and efficiency) and demonstrate the benefits of SOAP compared to Adam or Shampoo. They authors also provide detailed analysis of the memory consumption of SOAP in the Appendix.

### Weaknesses
The main weakness of this paper (which is also acknowledged by the authors) are the rather small scale experiments in language model pre-training compared to current state of the art or production models. 
I believe that showing good performance compared to AdamW on the 1B to 7B parameter scale, would strongly support the adoption of SOAP. 
Also, it would be interesting how the new optimizer SOAP performs in combination with newly emerging Linear Recurrent Models (like Mamba).



### Questions
- L.350: n -> In (typo)
- Did you observe any influence of SOAP on training instabilities (e.g. grad norm slikes / rise or loss spikes) in language model pretraining?
- It would be helpful for others adopting SOAP if the authors provide learning curves for other common metrics monitored during pre-training (e.g. parameter norms, gradienten norms, validation loss, etc.)? This would help compering other training setups to your suggested one.

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
5

### Summary
In this paper, the authors propose SOAP, ShampoO with Adam in the Preconditioner’s eigenbasis. They starts with an insight: Shampoo is equivalent to running Adafactor in the eigenbasis of Shampoo’s preconditioner. SOAP continually updates the running average of the second moment as Adam does.In the large batch regime, SOAP reduces the number of iterations by over 40% and wall clock time by over 35% compared to AdamW, with approximately 20% improvements in both metrics compared to Shampoo.

### Strengths
* Interesting connection and insights between Adafactor in Shampoo’s eigenspace and SOAP
* The name is funny
* Experiment results seem pretty promising

### Weaknesses
 * I am a bit confused by the main contribution of this paper overall, algorithmetic insights on connection between adafactor and shampoo are interesting, hence I am recommending acceptance. However, beyond that, the rest seems to be a special case of galore [see my comments in the question below.]. Maybe a more efficient implementation?
* As far as I know, in pytorch, SVD was also implemented via power iteration but at cuda kernel level. The difference proposed here seems to be how many iterations it runs.
* Please also do some downstream evaluations on checkpoints output by different optimizers, just for the sake of completeness.

### Questions
* In theory, how is this different from running GaLore under "full" mode + adam/adafactor? Please refer to the following code snippet  in official galore repo for the context: 
```python
low_rank_grad = torch.matmul(self.ortho_matrix[0].t().to(full_rank_grad.device.type), full_rank_grad) @ self.ortho_matrix[1].t().to(full_rank_grad.device.type)
```
https://github.com/jiaweizzhao/GaLore/blob/2cc66f88cce189e505affbb91042a8e77f5bf4e9/galore_torch/galore_projector.py#L39 

* What happens if you use power iterations to approximate SVD in galore, does that still work? it feels like that should be included as a baseline too. [1] seems to suggest it works?

* Why does higher frequency lead to worse results? Intuitively, it should provide better and more up-to-date approximation to the eigenspace?

[1] Liang, Kaizhao, et al. "Memory-efficient llm training with online subspace descent." arXiv preprint arXiv:2408.12857 (2024).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
I would like to preface my review: I am not an expert in this area. I have published a single paper in this area a very long time ago, but have not touched optimization since. I have asked several of my colleagues, who are among the most qualified researchers to review this paper, and they responded with very positive feedback. Still, I ask the AC to down-weight my review and defer to the other reviewers who may be more familiar with this space.

This work proposes a new optimization algorithm, called SOAP, that extends several of the (largely untested) concepts presented in Appendix B of the second Shampoo paper. In particular, they make changes to the computation of the Shampoo preconditioners---using dataset averages rather than running averages and computing the eigenvectors of L and R every $f$ steps---that make this algorithm now work.

Additionally, the authors prove a correspondence between the Shampoo parameter update and running Adafactor in the eigenbasis of Shampoo's preconditioner.  They then extend this to running Adam in Shampoo's preconditioner eigenbasis, and provide experimental results that demonstrate the effectiveness of their optimization algorithm.

### Strengths
This paper is exceptionally well written and easy to follow. Prior and related work are excellently summarized, and the contribution of work in the context of the overarching field is clear. The experimental results evaluate on a very relevant setting (LLM pre-training), the baselines are appropriate (direct comparison with Shampoo and AdamW), and the results demonstrate that SOAP is quite effective. I also appreciate the discussion of the hyperparameter sweeps in the appendix -- not conducing this comparison has caused some unfortunate situations in the past within the optimization community.

As an aside, the naming is excellent (shampoo, rinse, lather, and now soap...).

### Weaknesses
To be frank, I do not see any substantial weaknesses. One could argue that it doesn't go far enough in certain directions, but these areas are acknowledged by the paper and "left to future work" (which I believe is appropriate given this paper's scope).

This is, in my view, a very good paper.

### Questions
The authors write Soap is equivalent to running Adam in a rotated space; however, is transformation to the eigenbasis $G' \leftarrow Q_L^TGQ_R$ necessarily unitary? What is the specific operation in SO(d)?

Several nits: 

Using $\phi$ rather than $\mathcal{L}$ or $L$ to denote the loss seems unusual (although perhaps this is to distinguish from the Shampoo preconditioner $L$).

### Soundness
4

### Presentation
4

### Contribution
4
