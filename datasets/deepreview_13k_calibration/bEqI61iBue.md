# Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Fine-tuning large language models (LLMs) is necessary for specific downstream tasks, but classic first-order optimizer entails prohibitive GPU memory because of the back propagation. Recent works such as MeZO have turned to zeroth-order optimizers for fine-tuning, which reduce substantial memory by using two forward passes. However, heterogeneous curvatures across different parameter dimensions in LLMs often cause model convergence instability or even failure. In this work, we propose HiZOO, a diagonal \textbf{H}essian \textbf{i}nformed \textbf{Z}eroth-\textbf{O}rder \textbf{O}ptimizer , which is the first work to leverage the diagonal Hessian to enhance ZOO for fine-tuning LLMs. We provide theoretical proof for \nameo and visualize the optimization trajectories on test functions to illustrate how it improves convergence in handling heterogeneous curvatures. Extensive experiments on various models (RoBERTa, OPT, Phi-2 and LLama3, with 350M$\sim$66B parameters) indicate that \nameo significantly reduces training steps and enhances model accuracy, while keeping the memory advantage of ZOO. For example, on SST2 task HiZOO achieves $8\times$ speedup and 1.55\% accuracy improvement over MeZO across different models. Code is available at https://anonymous.4open.science/r/HiZOO-27F8.
\nnfootnote{$^*$ Equal contribution. $^\dagger$ Correspondence to: yehaishan@xjtu.edu.cn}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Motivated by the limited optimization effectiveness of zeroth-order optimizers in deep learning, this manuscript leverages a diagonal Hessian to enhance the optimization quality. Though introducing second-order curvature information to aid the optimization is standard, the manuscript is quite comprehensive: it builds methods step-by-step, provides a theoretical justification, and verifies the effectiveness across various model architectures and datasets.

### Strengths
* The manuscript studies an interesting problem: efficient and effective zeroth-order fine-tuning. The manuscript has a clear motivation in the introduction part, with a thorough step-by-step explanation in Section 3.3. Extensive empirical studies consider evaluating both encoder-decoder and decoder-only neural architectures on the GLUE benchmark over several baseline methods. The evaluation uses the number of forward passes (which is very good) and discusses memory usage and time efficiency.
* The manuscript has some preliminary convergence analysis.

### Weaknesses
1. The convergence analysis part can be strengthened. It would be great if the analysis could cover the case of MeZO (and other zeroth-order algorithms) and carefully explain the gain introduced by the diagonal Hessian. See some examples in [1], where the query complexity can be discussed and compared. Specifically, the analysis should delve into how the diagonal Hessian approximation affects the condition number of the optimization landscape and subsequently the convergence rate. A more rigorous treatment of the stochasticity introduced by the zeroth-order gradient estimation is also needed, especially concerning its interaction with the Hessian approximation. The current analysis lacks a detailed comparison of the convergence behavior with and without the diagonal Hessian, making it difficult to assess the true benefit of the proposed method.
2. The manuscript structure can be improved. E.g., some detailed derivates in Sec 3 can be simplified, and the definition of three test functions in Sec 3.5 can be moved to the main text. The current presentation of derivations in Section 3 is overly verbose, potentially obscuring the core ideas. The test functions in Section 3.5, which are crucial for understanding the method's behavior, should be introduced earlier in the main text to provide context. Furthermore, the manuscript could benefit from a clearer separation of the theoretical contributions from the empirical evaluations, making it easier for readers to follow the logical flow.
3. Extending to other LLM SFT datasets: it would be great if the manuscript could verify the effectiveness of HiZOO on some SFT datasets. The current evaluation is limited to GLUE benchmark and a few LLMs, which may not fully represent the diverse challenges in SFT tasks. The manuscript should consider evaluating the method on more diverse datasets, including those with different data distributions and task complexities. This would provide a more robust assessment of the method's generalization capabilities.

### Questions
NA

### Soundness
3

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
This paper proposes the Hessian-informed Zeroth-Order Optimizer (HiZOO), which achieves faster convergence than traditional zeroth-order SGD (specifically, MeZO) in LLM fine-tuning scenarios by leveraging Hessian information through a zeroth-order approach. Although HiZOO requires one additional forward pass compared to MeZO (totaling three forward passes), it demonstrates faster convergence in terms of the number of function calls. Furthermore, HiZOO outperforms MeZO in terms of model generalization for various tasks in LLM fine-tuning and the authors also provide convergence guarantee of their HiZOO method in theory.

### Strengths
1. The first approach that leverage the second-order information via zeroth-order construction for fine-tuning LLMs
2. Illustration of HiZOO on some test functions with superior generalization ability of the method
3. Convergence guarantee of HiZOO with their diagonal inverse Hessian estimator

### Weaknesses
1. The Hessian estimator from Equation (3) appears to estimate the Hessian matrix only if the matrix $\Sigma$ is close to the inverse Hessian. 
However, according to Algorithm 1 in the paper, I saw that the matrix (actually, the vector) $\Sigma_0$ is initialized simply as the identity matrix, which suggests that this estimator may not accurately estimate the (diagonal) inverse Hessian. Furthermore, since the initial value is merely an identity matrix, it is difficult to consider the subsequent estimated $\Sigma_t$ values as accurate estimations of the diagonal inverse Hessian. 
Instead, it seems more likely that HiZOO are estimating something positive definite.

---

2. The theoretical result seems a bit unusual. 
Typically, convergence results are derived as bounds on the norm of the true gradient (i.e. the gradient evaluated on the entire training dataset) rather than the norm of the stochastic gradient. 
Consequently, Theorem 3.2, which presents the current convergence result, is very confusing and may need to be revised for clarity.

---

3. In addition to the second concern, the convergence rate in Theorem 3.2 is on par with first-order methods. However, given that second-order information, such as the diagonal Hessian, is utilized—even if constructed solely from function values—there should ideally be an advantage in convergence compared to existing methods like MeZO or other vanilla SGD-based approaches. This expected benefit, however, does not seem apparent. Moreover, $\max_t \mathrm{Tr}(\Sigma_t)$ would also depend on $d$. 
For example, given that Algorithm 1 initializes $\Sigma_0$ as the identity matrix, the quantity $\mathrm{Tr}(\Sigma_0)$ becomes $d$, so $\max_t \mathrm{Tr}(\Sigma_t)$ is at least on the order of the parameter dimension $d$. 
If the order of $\max_t \mathrm{Tr}(\Sigma_t)$ exceeds $d$ (e.g., something like $d\sqrt{d}$), the convergence rate would actually be slower than zeroth-order vanilla SGD (ZO-SGD), which undermines the theoretical contributions of the proposed algorithm.
(To the best of my knowledge, the convergence of ZO-SGD can be derived faster than $O(d)$). Also, importantly, the advantage of leveraging second-order information should be apparent in terms of theory.

---

4. Looking at the comparison on the test function, it appears to be a comparison of just optimization from scratch rather than fine-tuning. 
I'm curious about the hyperparameter settings, as it seems to perform better than Adam. 
If this advantage holds, there should also be experiments demonstrating the use of zeroth-order methods not only in fine-tuning but also in pre-training.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work presents a novel optimization method called HiZOO, designed for fine-tuning large language models (LLMs). HiZOO addresses this by incorporating a diagonal Hessian estimation through an additional forward pass, allowing it to act as a pre-conditioner that adjusts updates based on parameter curvatures. This approach reduces training steps and improves accuracy while maintaining efficient memory use, scaling well even for models with billions of parameters. The authors also propose HiZOO-L, a low-rank version that significantly cuts down on memory cost while preserving performance.

### Strengths
1. The introduction of HiZOO, a Hessian-informed zeroth-order optimizer, is original.
2. The proposed low-rank variant, HiZOO-L, which reduces memory overhead, demonstrates a approach to solving memory constraints while maintaining optimization quality.
3. The paper is well-organized, with clear sections outlining the motivation.

### Weaknesses
1. The code implementation assumes that  u_i Hadamard product u_i is treated as a diagonal matrix. However, this is incorrect as \( u_i u_i^T \) is an outer product in the algorithm description in the paper resulting in a rank-1 matrix. This assumption could introduce inconsistencies or inaccuracies in the Hessian estimation and parameter updates.

2. The value for `Hessian_smooth` in the implementation is set to \( 1e^{-6} \), which seems quite small. This could imply that the contribution of the Hessian information is not significant enough to make a substantial impact on convergence or stability. 

3. Tables 1 and 3 present results for a range of NLP tasks, but no generation tasks are included. This limits the understanding of HiZOO’s performance in broader language modeling applications where generative capabilities are critical.

4. While Table 5 reports promising results on SST2, Figures 12 to 14 reveal that HiZOO demonstrates poor training performance and even training failure in some cases. This discrepancy raises concerns about the stability and reliability of the optimizer under different conditions.

5. Line 9 in Algorithm 2 is unclear. Calculating \( R^{-1} \) and \( C^{-1} \) involves significant computational overhead, making this step inefficient.

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

### Contribution
2
