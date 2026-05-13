# How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
Transformers pretrained on diverse tasks exhibit remarkable \emph{in-context learning} (ICL) capabilities, enabling them to solve unseen tasks solely based on input contexts without adjusting model parameters. In this paper, we study ICL in one of its simplest setups: pretraining a linearly parameterized single-layer linear attention model for linear regression with a Gaussian prior. We establish a statistical task complexity bound for the attention model pretraining, showing that effective pretraining only requires a small number of independent tasks. Furthermore, we prove that the pretrained model closely matches the Bayes optimal algorithm, i.e., optimally tuned ridge regression, by achieving nearly Bayes optimal risk on unseen tasks under a fixed context length. These theoretical findings complement prior experimental research and shed light on the statistical foundations of ICL.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates a single-layer linear attention model, which is equivalent to a linear model with parameters derived from a one-matrix-step gradient descent from the origin. The authors make Gaussian data generating assumptions and consider the population ICL risk, identifying the optimal step size. They demonstrate that applying gradient descent to the step size parameterization can lead to an excess risk characterized by an exponential decay plus a 1/T-like decay. The authors also compare this with the Bayes optimal estimator, analyzing their respective risks.

### Strengths
The paper's originality lies in analyzing the single-layer linear attention model with its one-step gradient descent parameterization. The authors' identification of the optimal step size under Gaussian data generating assumptions is a valuable contribution. The quality of the paper is evident in the rigorous mathematical analysis.

### Weaknesses
The paper's clarity could be improved.

- The assumption of the pretraining algorithm in equation (6) seems arguable, as the equivalence of the function classes does not necessarily imply identical behavior under different parameterizations in gradient descent. Specifically, while the function classes might be equivalent, the optimization landscapes induced by different parameterizations can be drastically different, leading to different convergence properties and final solutions. The paper does not adequately address this potential discrepancy.
- The paper is heavily reliant on mathematical notation and could benefit from more intuitive explanations to aid understanding. The lack of clear, conceptual explanations makes it difficult to grasp the significance of the mathematical results for a broader audience.
- The choice of step size in Theorem 4.1 is not adequately justified, and the assumption that the initialization Γ0 commutes with H is not clearly motivated. The specific form of the step size schedule, a piecewise constant decay, is not explained in the context of the problem. The assumption that Γ0 commutes with H is a strong condition that limits the generality of the result and lacks a clear justification.
- The assumption that H can be diagonalized without loss of generality (WLOG) is also not sufficiently explained. While it is true that any matrix can be diagonalized through a change of basis, the implications of this transformation on the subsequent analysis are not clearly discussed. It's not obvious how the diagonalization simplifies the analysis without loss of generality.
- The paper could be enhanced by including some numerical results in the main body. The absence of numerical results makes it hard to assess the practical relevance of the theoretical findings.
- The terminology used is occasionally confusing, such as the use of "number of contexts".

### Questions
- Could you provide more justification for the pretraining algorithm assumed in equation (6)?
- Could you explain the choice of step size in Theorem 4.1?
- Why is it reasonable to assume that the initialization Γ0 commutes with H in Theorem 4.1?
- Could you provide more insight into why H can be assumed to be diagonal WLOG?
- Would it be possible to include some numerical results in the main body to support the theoretical findings?
- Could you clarify the term "number of contexts"? It reads like the number of in-context samples, but I guess you mean the number of sequences/datasets.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper dives into the statistical understanding of pre-training of a single linear layer attention on in-context examples generated with Gaussian data and linear regression with a Gaussian prior.  The important theoretical contributions can be summarized as follows.

(a) The authors first show the optimal solution and its excess risk in terms of the pre-training sequence lengths and the covariance matrix underlying the Gaussian data.

(b) The authors then show the behavior of the excess risk with training steps via SGD, where each step uses a randomly sampled sequence from the underlying distribution.

(c) The authors further show that when evaluation sequence lengths match to the training sequence lengths, the model matches the Bayes optimal solution. However, discrepancies between the two can lead to sub-optimalty. 

Overall, the paper takes an important step toward statistical understanding of the dependence of pre-training data and in-context abilities of attention models.

### Strengths
The main strength of the paper lies in its clinical approach to relate the existing literature on ridge regression with Gaussian prior to the statistical understanding of linear attention pre-training. Furthermore, the authors introduce novel techniques like operator polynomials to solve order-8 tensors that show up in the risk analysis of SGD training, which might be of independent interest to the community. 

The advantages of the theoretical framework can be summarized as follows. First, a single linear attention model reaches the optimal linear regression solution with SGD. The framework gives statistical convergence bounds with dependence on training sequence lengths and the data covariance matrix. Secondly, one can pinpoint the gaps between evaluation and training based on the discrepancies in data properties e.g. sequence length. Overall, the paper will be an important addition to the theory community.

### Weaknesses
Overall, the paper doesn't have many pitfalls and issues as is.

I have a question about the theoretical setup. Linear attentions used in practice have a query $Q$, key $K$, and value $V$ matrix. However, the authors use structural modifications in $Q$, $K$, and $V$ to represent the formulation with a single matrix $\Gamma$ and compute SGD convergence of $\Gamma$. Without the modification, I believe the optimal solution can be shown to be a $3$-matrix factorization of the optimal solution $\Gamma^*$ given in theorem 1. But what will be the statistical bounds of training these $3$ matrices (or any pair among the $3$ matrices)? Can the authors discuss whether it is answerable from their theoretical framework and if not, the difficulties one might face to solve?

Furthermore, how will the theory change when instead of using training sequences of a single length, we use randomly sampled training sequences with varying lengths? How will the excess risk in theorem 5.3 change then?

The authors also conduct a few experiments in the appendix on a real-world transformer to verify their theoretical claims. It would be interesting to empirically check the training time convergence with different singular value behaviors (as they pick in corollary 4.2) and observe differences in convergence and ICL performance throughout training.

Finally, I haven't looked deeply into the proof, since it is extremely long to read through. But at a glance, the paper seems to be utilizing similar proof techniques that prior works have used for ridge regression with Gaussian prior. Hence, I still recommend strong acceptance.

### Questions
Please see my questions in the previous section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a statistical task complexity bound for a one-layer linear attention model in solving fixed-length linear regression problems. The authors investigate the required number of independent sequences or tasks necessary for pretraining the model. They conclude that only a small number of sequences are needed compared to the model parameters, and this is independent of the input dimension. Additionally, the paper theoretically demonstrates a performance drop when the number of in-context examples during evaluation differs from the training phase.

### Strengths
1. The paper is well-organized, with clear contributions and promising results in the statistical analysis of in-context learning for linear regression problems using a one-layer linear attention model.
2. The theoretical results provided in the paper address the sample complexity of learning linear regression problems, highlighting that it is approximately $O(1/T)$. This indicates that the number of tasks required for learning the model is independent of both the model size and the input dimension ($d$).
3. The paper underscores the significance of context length during testing, proving that optimal prediction is attainable only when the number of context examples matches that of the pre-training phase.

### Weaknesses
1. While the theoretical analysis presented is commendable and contributes to our understanding, the paper could be greatly enhanced by including more empirical results. Given that implementing linear regression over a transformer model is feasible and has been achieved in prior work, specific implementations that could improve this paper include:

    - Demonstrating through examples that training models on linear tasks of varying dimensions yields similar performance, supporting the paper's claim that task complexity is independent of the task dimension $d$.
    - Conducting experiments to show that a pre-trained model performs poorly when there is a significant discrepancy between the in-context length during testing and training.
2. The paper’s assertion that task complexity is independent of $d$ is counterintuitive. It is typically expected that the number of tasks required would be on the order of $O(d^2/T)$ since the task distribution or covariance, encompassing at least $d^2$ parameters, needs to be retrieved. The authors are encouraged to provide additional clarification on this aspect of independence. Furthermore, the experiments presented seem to contradict the paper’s statement, as $T$ appears to be exponentially larger than $d^2$, which doesn’t align with the claim that "$T$ could be much smaller than $d^2$".

3. Despite Equation (9) not explicitly showing dependence on $d$, it seems that $d$ is implicitly involved in the matrix operations, which should be addressed for clarity.

### Questions
1. Is it possible to ensure that the first term of Equation (9) will consistently reach zero? Given the exponentially decreasing learning rate $\gamma_t$, this relationship does not seem immediately apparent.
2. In Theorem 4.1, the learning rate $\gamma_0$ is upper bounded. Could the authors elaborate on the reasoning behind this? Is it connected to the implicit convergence rate of gradient descent in linear problems? Additionally, what are the considerations and trade-offs in selecting an appropriate initial learning rate $\gamma_0$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Using a modified version of a single-layer linear attention model, the authors derive a dimension-independent complexity bound which suggests that efficient pretraining is possible even with a large number of model parameters for effective in-context learning. In the process, the authors demonstrate novel techniques for analyzing higher-order tensors that may be independently applicable.

### Strengths
- The authors provide a timely contribution to an important phenomenon of in-content learning.
- I am positive that this work provides a good theoretical checkpoint for future work to build on top of the provided analysis. 
- The text is fairly well-presented and the research community will appreciate it as such.
- I also specially highlight that the authors have made proper effort to delineate the assumptions behind the theoretical results.

### Weaknesses
 - The obvious shortcomings of the theoretical results come from the nature of assumptions that deviate from standard practice - the choice of linear attention and a restricting the structure of Q/K/V matrices. Also see Question 1.
- While the community is focused on Transformers, I am wondering if the analysis also holds for a different linear parametrization of the function $f$. In the broader context, if similar results hold for another parametrization, then attention would not appear that unique of a function. As an example, imagine a different parametrization that also leads to a dimension-free bound. In the broader context, such a result would then not distinguish what attention brings to the table, when in practice we have ample evidence that other parametrizations don't carry as flexible and generalizable inductive biases.
- Regarding the distributional assumptions of the fixed sized dataset in Assumption 1, it would be great to have experiments where the model is misspecified. Please correct me if I missed, but I don't think I see such an experiment in Appendix A. Misspecification is really important, since for all practical purposes, our models are misspecified, i.e. the data does not really come from the distribution we assume to be. If Transformers can still achieved a good decay of the empirical risk as the number of pretraining tasks increase, it would certainly be a unique characteristic. Also see Question 2.
- I would strongly recommend highlighting the experiments and moving them up to the main text. Perhaps Section 6 could be compressed a little to accommodate.

### Questions
1. Could the authors confirm if the restrictions are significantly restrictive? It would appear significant at face value. I certainly don't discount the fact that the work aims to provides theoretical grounding for similar observations in literature.
2. In Theorem 4.1, how is the inner product between matrices defined?
3. It would appear that the theorems do not necessarily say anything about misspecification, except that the excess risk is controlled via terms in Equation 8. In a sense, the Gaussian assumptions are used for derivations so anything in the Gaussian family would qualify for the bound. Is that the correct assessment?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
