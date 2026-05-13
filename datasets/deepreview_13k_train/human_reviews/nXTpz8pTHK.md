# Reweighting Local Mimina with Tilted SAM

- Decision: Reject
- Scores: 6, 6, 8, 5

## Abstract
Sharpness-Aware Minimization (SAM) has been demonstrated to improve the generalization performance of overparameterized models by seeking flat minima on the loss landscape through optimizing model parameters that incur the largest loss within a neighborhood. 
Nevertheless, such min-max formulations are computationally challenging especially when the problem is highly non-convex. Additionally, focusing only on the worst-case local solution while ignoring potentially many other local solutions may be suboptimal when searching for flat minima. 
In this work, we propose Tilted SAM (TSAM), a generalization of SAM inspired by exponential tilting that effectively assigns higher priority to local solutions that are flatter and that incur larger losses. TSAM is parameterized by a tilt hyperparameter $t$ and reduces to SAM as $t$ approaches infinity. We prove that (1) the TSAM objective is smoother than SAM and thus easier to optimize; and (2) TSAM explicitly favors  flatter minima as $t$ increases. This is desirable as flatter minima could have better generalization properties for certain tasks. We develop algorithms motivated by the discretization of Hamiltonian dynamics to solve TSAM. 
Empirically, TSAM arrives at  flatter local minima and results in superior test performance than the baselines of SAM and ERM across a range of image and text tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Inspired by the idea of exponential tilting in probability and statistics, this paper introduces a generalized and smoothed variant of SAM, termed TSAM. The authors highlight two key attributes of TSAM: smoothness and preference for flatter minima. They further develop an algorithm to practically solve TSAM. Finally, they verify the generalization improvement of TSAM over SAM and ERM via extensive experiments.

### Strengths
1. The idea of reweighting multiple points in the neighborhoods of the local minima instead of focusing on the single worst solution is intuitive.

2. The paper is well-written and supports its claims through theory and comprehensive experiments.

### Weaknesses
1. There seem to be conflicting explanations for why TSAM outperforms SAM regarding generalization. On one side, the authors suggest that TSAM improves generalization by considering a broader range of local solutions rather than concentrating solely on the worst-case scenarios, indicating that TSAM's objective function is inherently superior for identifying solutions with better generalization. Conversely, TSAM is said to favor flatter minima as $t$ increases. As $t$ approaches infinity, TSAM converges to SAM, suggesting that SAM might ideally be the best at finding flatter minima, if not for practical optimization challenges. Thus, TSAM's enhanced performance in practice may stem from its balanced trade-off between optimizing for flatter minima and maintaining optimization efficiency.

2. The generalization bounds presented in Section 3.3 are confusing regarding the message they aim to convey. The authors seek to demonstrate that TSAM has smaller upper bounds on generalization error compared to SAM and ERM. However, in their theoretical framework, the bound for SAM is worse than that for ERM, which contradicts the superior generalization performance of SAM in practice. This contradiction undermines the validity of the comparative advantage attributed to TSAM over both SAM and ERM.

3. The improvement of TSAM over SAM and ERM is marginal in the transformer experiments (the second table in Table 1). Moreover, TSAM requires more computation than SAM and ERM, thus raising the question: if variants such as ESAM1 or ESAM2 were to be tested, would the marginal improvements provided by TSAM diminish further?

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new version of the sharpness-aware minimization algorithm (SAM) called tilted SAM (TSAM). 
TSAM uses exponential tilting to smooth the objective. TSAM comes with a temperature parameter t.
 As t approaches infinity TSAM converges to classic SAM.
The paper shows exponential tilting leads to an easier optimization problem while still favoring flat solutions.
TSAM's theoretical analysis shows that it enjoys good generalization properties.
Moreover, the numerical experiments show TSAM performs superior to other SAM-style algorithms on several benchmark tasks.

### Strengths
**Clarity**

The paper is well-presented and easy to read.

**Theory**

The paper provides good theoretical guarantees for the algorithm, establishing that the solution found by the algorithm generalizes well under standard hypotheses.

**Experiments**

TSAM performs better than existing SAM-like approaches on standard ML tasks. 
Moreover, the competitors are tuned, which is good. 

**Overall** 

This is a solid paper and could be of interest to certain subcommunities working on deep learning theory and optimization.

### Weaknesses
 **Technical Contribution**

The argument for establishing the main result, Theorem 2, seems standard. It consists of a standard application of Hoeffding's inequality combined with a technical lemma proved by Aminian et al. (2024).

**Numerical Experiments**

The paper only reports performance over epochs and not wall clock time. It should report both; if the proposed algorithm runs significantly slower than existing methods, that's problematic.

For the HMC portion of the algorithm, to generate $\epsilon$, the authors mention they set $N=1$ for computational efficiency.
Given the experimental results, this approximation seems to work.
Nevertheless, it would have been nice to have some ablation in the appendix with larger values of $N$ to show the impact increasing this parameter has on performance.
This would help validate the setting of $N=1$ and show if there is any tradeoff between speed and performance in setting $N$.

### Questions
1. Could you add wall clock times in the revision?
2. Could you add an ablation to the appendix for the $N$ parameter.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an approach named Tilted Sharpness-Aware Minimization (TSAM), which extends the Sharpness-Aware Minimization (SAM) method to improve generalization in overparameterized machine learning models. SAM optimizes model parameters by focusing on minimizing the maximum loss in a neighborhood, aiming to find flat minima that enhance generalization. However, SAM's approach can be computationally challenging and overly focused on the worst-case local solutions. 

TSAM addresses these issues by introducing a "tilt" parameter formulation $t$, which allows for reweighting local minima, focusing on flatter solutions that could generalize better. The authors demonstrate that as the tilt parameter increases, TSAM smooths the optimization landscape, favoring flatter minima. To effectively solve the TSAM objective, the authors propose a novel Hamiltonian Monte Carlo-inspired algorithm to sample and estimate gradients efficiently. Empirical evaluations across image and text tasks show TSAM’s superiority in test performance over SAM and ERM, including fine-tuning ResNet18 and Vision Transformers on CIFAR-100, ImageNet, and DTD datasets, and fine-tuning DistilBert model on the GLUE benchmark

### Strengths
- TSAM’s approach to generalization via tilting provides a novel and flexible framework, allowing it to optimize for both worst-case and average-case scenarios, unlike SAM’s rigid min-max formulation.Theoretical proofs and empirical results support that TSAM achieves flatter minima than SAM, correlating with improved generalization on test data.

- TSAM is tested on a diverse range of tasks and models (e.g., CNNs, transformers, and GLUE benchmark tasks), demonstrating its robustness and adaptability to different domains.

- By using a Hamiltonian Monte Carlo method to sample neighborhood perturbations, TSAM optimizes for flatter minima more efficiently than naive sampling would allow, enabling practical deployment in high-dimensional optimization tasks.

### Weaknesses
 - The algorithm introduces additional parameters (e.g., tilt parameter $t$ and sampling frequency), requiring careful tuning, which could be challenging in resource-constrained environments.

- Although TSAM is more efficient than a straightforward min-max approach, it still requires multiple gradient evaluations per iteration. Can the authors analyze the runtime complexity of the optimization algorithm? Moreover, it would be better to provide a comparison of running time between the baselines in the paper.

### Questions
How can one tune the hyper-parameter $t$? It would be better to provide a clear method/intuition for selecting an optimal $t$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents Tilted SAM (TSAM) that generalizes Sharpness-Aware Minimization (SAM) by incorporating exponential tilting. While SAM aims to minimize the worst-case loss in a neighborhood around the model parameters to attain flatter minima, TSAM enhances this approach by emphasizing local solutions that are flatter but allow for larger losses, controlled by a tilt hyperparameter $t$. Compared to SAM, TSAM is less aggressive as it adjusts the perturbation between worst-case scenarios and other states. The paper includes theoretical proof of TSAM's properties, describes an algorithm inspired by Hamiltonian dynamics for solving TSAM, and presents empirical results demonstrating TSAM's superior generalization performance and ability to achieve flatter minima.

### Strengths
1. TSAM, a smoother objective for SAM, achieves flatter minima through the use of exponential tilting.

2. The paper defines sharpness in terms of loss variance and provides proof that TSAM can achieve flatter minima.

3. The authors propose a practical algorithm inspired by Hamiltonian Monte Carlo.

4. Experimental results show that TSAM achieves better generalization and attains flatter minima in both image and language classification tasks.

### Weaknesses
1. Section 3.2 demonstrates that TSAM prefers a flatter model as $t$ increases. However, the relationship between flatness and generalization is still unclear as the authors mentioned in related works. Although the authors analyze the generalization of TSAM in Section 3.3, it's a bit weak since Remark 1 just claims that TSAM _can_ obtain a smaller linear population error of ERM or SAM. The theoretical analysis lacks a direct connection between the proposed tilted objective and improved generalization, relying on an upper bound argument that does not fully explain the empirical gains.

2. Lack of experiments on large-scale datasets like ImageNet-1K, which is a standard dataset in SAM-related works. This limits the assessment of TSAM's scalability and performance on more complex, real-world scenarios. Furthermore, the absence of comparisons with multiple architectures on each dataset makes it difficult to assess the robustness of TSAM across different model types.

3. In Figure 3, it seems $t$ is a sensitive hyperparameter and it needs to be tuned on different datasets, which adds extra computational cost. In addition, as $t$ increases that should lead to flatter minima as discussed in Section 3.2, but it doesn't always improve the generaliation. How to pick effective $t$ becomes a problem. The lack of a clear strategy for selecting the hyperparameter $t$ makes the method less practical, as it requires a computationally expensive grid search for each new task.

4. Why choose $\mathrm{E}[L(\theta^\star + \epsilon)]$ and $\mathrm{var}[L(\theta^\star + \epsilon)]$ representing sharpness in Section 5.2? Hessian spectra, the maximum eigenvalue, and $\lambda_1/\lambda_5$ are the most common methods to describe the sharpness in SAM-related works (e.g. SAM paper and VASSO paper, both of them mentioned in this paper). Therefore, the authors should explain the reason, and that would be better if adding additional results. The choice of sharpness metrics is not well-justified, and the paper should include more standard measures like Hessian eigenvalues to allow for better comparison with existing literature.

5. Computational cost is too much. TSAM requires 3 or 5 times the computational cost of SAM, which makes it impractical. Don't even mention the costs of tuning $t$ and $s$. The increased computational cost due to multiple perturbation evaluations per iteration, coupled with the hyperparameter tuning overhead, makes TSAM less appealing compared to other SAM variants that achieve similar or better performance with lower computational demands.

6. It's not very clear about experimental settings. For example, what's the noise level of Noisy CIFAR100? Are the results of Table 1 mean values, how many runs of each experiment, and could you provide the standard deviation? The lack of detailed experimental settings and statistical reporting makes it difficult to reproduce the results and assess their statistical significance.

### Questions
1. What's the meaning of '(1)' at the end of line 281?

2. What's the role of $\hat{\theta}$ in Algorithm 2? Why not compute $\epsilon$ directly?

3. Is it a typo in line 475? When $t=0$, TSAM reduces to SAM objective or average weight perturbation?

### Soundness
2

### Presentation
2

### Contribution
2
