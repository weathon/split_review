# The Advancement in Stochastic Zeroth-Order Optimization: Mechanism of Accelerated Convergence of Gaussian Direction on Objectives with Skewed Hessian Eigenvalues

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
This paper primarily investigates large-scale finite-sum optimization problems, which are particularly prevalent in the big data era. 
In the field of zeroth-order optimization, stochastic optimization methods have become essential tools. 
Natural zeroth-order stochastic optimization methods are primarily based on stochastic gradient descent ($\texttt{SGD}$).
The method of preprocessing the stochastic gradient with Gaussian vector is referred to as $\texttt{ZO-SGD-Gauss}$ ($\texttt{ZSG}$), while estimating partial derivatives along coordinate directions to compute the stochastic gradient is known as $\texttt{ZO-SGD-Coordinate}$ ($\texttt{ZSC}$).
Compared to $\texttt{ZSC}$, $\texttt{ZSG}$ often demonstrates superior performance in practice.
However, the underlying mechanisms behind this phenomenon remain unclear in the academic community.
To the best of our knowledge, our work is the first to theoretically analyze the potential advantages of $\texttt{ZSG}$ compared to $\texttt{ZSC}$.
Unlike the fundamental assumptions applied in general stochastic optimization analyses, the quadratic regularity assumption is proposed to generalize the smoothness and strong convexity to the Hessian matrix. 
This assumption allows us to incorporate Hessian information into the complexity analysis.
When the objective function is quadratic, the quadratic regularity assumption reduces to the second-order Taylor expansion of the function, and we focus on analyzing and proving the significant improvement of $\texttt{ZSG}$. 
For other objective function classes, we also demonstrate the convergence of $\texttt{ZSG}$ and its potentially better query complexity than that of $\texttt{ZSC}$. 
Finally, experimental results on both synthetic and real-world datasets substantiate the effectiveness of our theoretical analysis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a separation result between zeroth-order stochastic gradient descent and zeroth-order stochastic finite-difference method under a certain quadratic regularity assumption. The results essentially extends similar results in the deterministic setting to the stochastic finite-sum setting.

### Strengths
The paper address an important problem of providing separation results between two competing algorithms.

### Weaknesses
The main idea in the paper is (i) tr(M) ≪ d λ_max(M) and (ii) one algorithm has tr(M)  and the other has d λ_max(M), the complexity of the former algorithm is better than the latter. Without a formal lower bound for the latter, such a conclusion cannot be made. The paper does not provide a rigorous lower bound for the convergence rate of the algorithm that depends on d λ_max(M), making the comparison incomplete. The argument relies on the intuition that tr(M) is much smaller than d λ_max(M) for real-world problems, but this is not a sufficient justification without a formal proof or a more detailed analysis of the conditions under which this holds true. The analysis lacks a clear explanation of how the stochasticity affects the separation result. The paper only extends the deterministic results to the stochastic finite-sum setting, but it does not provide a novel analysis of the stochasticity itself, which is a critical component of the problem. 

Even ignoring this, similar results have been obtained in the deterministic setting previously and extension to the stochastic finite-sum setting is not significant and raise up to the level of ICLR acceptance. The paper's contribution is incremental, as it primarily adapts existing techniques from the deterministic setting to a stochastic scenario. The novelty of the analysis is limited, and the paper does not introduce any new theoretical tools or insights that significantly advance the field. The paper does not address the limitations of the zeroth-order methods in high-dimensional spaces, such as the increased variance of the gradient estimates, which could potentially negate the benefits of the improved complexity.

### Questions
please see above

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates large-scale finite-sum optimization within the zeroth-order (ZO) stochastic optimization paradigm, focusing specifically on two methods: ZO-SGD-Gauss (ZSG), which pre-processes the stochastic gradient with a Gaussian vector, and ZO-SGD-Coordinate (ZSC), which estimates partial derivatives along coordinate directions. The study addresses the notable performance gap between ZSG and ZSC, aiming to provide theoretical insights that explain ZSG's empirically observed advantages. To achieve this, the authors introduce the "quadratic regularity assumption" on the Hessian matrix, a relaxation of typical smoothness and strong convexity assumptions. They demonstrate that this assumption allows for incorporating Hessian information into complexity analysis, yielding convergence rates that reveal ZSG's improved efficiency in certain settings. The authors validate their analysis through synthetic and real-world experiments.

### Strengths
The authors reinforce their theoretical findings with experimental results on both synthetic and real-world datasets, which enhances the paper's credibility. The empirical results are presented clearly and support the theoretical claims regarding convergence rates and query complexity.

### Weaknesses
The paper seems to be very interesting, however, the following points are present in the paper which hinder the perception of readiness and clarity of the paper:

- Introduction. The introduction is not well designed.... It is possible to improve this point, for example, a table where the result of the work will be clearly visible, as well as the efficiency compared to other algorithms.

- Could not find a link to github or other source where I can find the code of the experiments.

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studies zeroth-order methods for finite-sum optimization and compares the complexity of two algorithms, ZSG and ZSC. The authors claim in the paper to rigorously and theoretically prove that ZSG is better than ZSC, under the quadratic regularity assumption.

### Strengths
The study on zeroth-order optimization is a trendy and important topic in optimization and machine learning, given lots of interesting applications in black-box attack, reinforcement learning, and fine-tuning language models.

### Weaknesses
1. The authors prove that ZSG converges with $tr(M)$, while previous work suggests that ZSC converges with $d\lambda(M)$. Based on this, the authors claim that ZSG is better when $tr(M)\leq d\lambda(M)$. I don't think this is a correct statement. There is no result in the paper showing that ZSC cannot achieve the rate $tr(M)$, and its $d\lambda(M)$ rate may come from the fact that previous analysis is not tight. To make the claim mathematically rigorous, the authors should provide the lower-bound under the current quadratic regularity assumption, showing that the rate of ZSC is $\Omega(d\lambda(M))$. Only then it is valid to say ZSG $\leq tr(M) \leq d\lambda(M) \leq$ ZSC.

2. I am also not sure why ZSC cannot achieve the rate $tr(M)$. The current ZSC considered in the paper queries all $d$ dimension at each iteration. Its complexity is thus deducted as $d$ times that of first-order methods. However, in ZSC, one can also only do random sampling at each iteration. For example, sampling from $\{1,2,\cdots,d\}$ instead of iterating over all $d$ dimension. This also builds a gradient estimator similar to ZSG, and similar analysis could apply. Specifically in the previous paper [Hanzely et al, 2018] and [Wang et al, 2024] mentioned by the authors, the rate of ZSC is also $tr(M)$ under the quadratic regularity assumption, e.g., Table 1 of [Hanzely, et al, 2018]. I am confused why authors say ZSC only achieves $d\lambda(M)$.

3. The rate of zeroth-order method has already been extensively studied under similar assumptions as the quadratic regularity assumption, e.g., [Malladi et al, 2023], [Yue et al, 2023], [arXiv: 2310.09639]. Stochastic mini-batch settings are also considered in these paper. Therefore, I am not sure how novel and challenge to obtain the results in the current paper given all these previous works.

4. The author claims in Corollary 4.4 that the algorithm will not converge with a fixed stepsize. I don't think this is correct. One can choose $\eta=(\log T)/T$, and then the algorithm converges with rate $T=(1/\epsilon)\log(1/\epsilon)$. Or can the authors clarify what they mean by a "fixed" step. In Corollary 4.6, when choosing $\sigma=0$, the complexity should reduce to the deterministic linear rate $\log(1/\epsilon)$. Is the current analysis tight?

5. I feel the paper is written in a rush and not well polished. There are lots of mistakes in grammar. For example, it should be smoothness assumption and strong convexity assumption in line 144; line 162-163 is not well written English; In Theorem 4.3, 4.5, it should be "let objective be quadratic" and "let x be update", etc.

### Questions
See weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies zeroth-order optimization methods (aka. black-box optimization). Specifically, the authors provide theoretical explanation for an observation in practice that the zeroth-order Gaussian gradient descent (ZSG) usually outperforms the zeroth-order version of coordinate descent (ZSC). They show that the improvement mainly comes from the skewness of the Hessian matrix of the objective function. Loosely speaking, the iteration complexity of ZSG scales with $Trace(H)/ \lambda_{\min}(H)$, while the complexity of ZSC scales with $d*\lambda_{\max}(H)/\lambda_{\min}(H)$ where $H$ is the Hessian matrix, $d$ is the dimension. They also perform numerical experiments to show that ZSG outpeforms ZSC in practice.

### Strengths
The paper is well-written and the research motivation is clear. Zeroth-order optimization plays a crucial role in domains where privacy in training is essential or where model size makes gradient computation impractical. The theoretical findings are also interesting.

### Weaknesses
While the authors managed to show the improvement of ZSG over ZSC when the objective's Hessian is skewed for the quadratic function, the claim is not so clear for the general function. For example, the factor $\gamma_u / \gamma_l^2$ in eq (23) can be quite uncontrollable compared to the advantage gained from the skewness. I suggest the authors discuss this trade-off more, i.e., pinpoint cases where the improvement is meaningful.

(1) Does ZSC have the "alpha term" that you ignored from the complexity of ZSG?  Does this alpha term affect the comparison between the two algorithms given that it is not ignored?

(2) Please provide more explanation on the sentence in lines 172 and 173. E.g., why are those parameters independent of the condition number of the data?

(3) Regarding conditions (2) and (3), is it  "exists z" or "for all z"? Please discuss these conditions more, especially how strong they are compared to "L-smooth" and "strongly convex"? Some discussions would be helpful instead of just citing [Frangella el at. 2023].

### Questions
(1) Does ZSC have the "alpha term" that you ignored from the complexity of ZSG?  Does this alpha term affect the comparison between the two algorithms given that it is not ignored?

(2) Please provide more explanation on the sentence in lines 172 and 173. E.g., why are those parameters independent of the condition number of the data?

(3) Regarding conditions (2) and (3), is it  "exists z" or "for all z"? Please discuss these conditions more, especially how strong they are compared to "L-smooth" and "strongly convex"? Some discussions would be helpful instead of just citing [Frangella el at. 2023].

### Soundness
3

### Presentation
3

### Contribution
2
