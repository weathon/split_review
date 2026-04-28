# Federated Learning Under Second-Order Data Heterogeneity

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
We consider the problem of Federated Learning over clients with heterogeneous data. We propose an algorithm called SABER that samples a subset of clients and tasks each client with its own local subproblem. SABER provably reduces client drift by incorporating an estimate of the global update direction and regularization into each client's subproblem. Under second-order data heterogeneity with parameter $\delta$, we prove that the method's communication complexity for nonconvex problems is $O\left(\delta\varepsilon^2\sqrt{M}\right)$. In addition, for problems satisfying $\mu$-Polyak-Lojasiewicz condition, the method converges linearly with communication complexity of $O\left(\left(\frac{\delta}{\mu}\sqrt{M} + M\right)\log\frac{1}{\varepsilon}\right)$. To showcase the empirical performance of our method, we compare it to standard baselines such as FedAvg on a few empirical problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript studies the federated leaning problem over clients with second-order data heterogeneity. The authors propose an algorithm called SABER, which combines FedProx and SCAFFOLD. Theoretically, they derive the communication complexity of SABER for both general non-convex and $\mu$-PL objective functions. Several experiments are performed to evaluate the proposed algorithm.

### Strengths
The problem studied in this paper is well motivated. 

The authors carefully compare the difference between first-order and second-order data heterogeneity. 

They provide a convergence analysis for SABER with deterministic gradient by constructing a local objective function consisting of a bias correction term and a regularization term.

### Weaknesses
1. The novelty of the paper seems limited. The local objective function constructed by the author is an intuitive combination of FedProx and SCAFFOLD. The similar idea can be found in Lin et al. (2023)

2. The algorithm design of SABER is not surprising to the reviewer in the sense that the proposed SABER algorithm uses the similar idea of SVRG to deal with data heterogeneity. Specifically, the use of control variates to correct for client drift is a well-established technique, and SABER's approach appears to be a straightforward application of this idea within the federated learning context.

3. Technically, the main proof techniques used in the paper are standard in federated learning. The authors make no concrete improvements to existing SOTA results. Furthermore, it seems that there is no significant difference in the techniques used to analyze the objective function that satisfies the \mu-PL condition and the convex condition, especially for the deterministic gradient scenario. The analysis for the \mu-PL case appears to follow a similar structure to the convex case, without introducing novel analytical tools or insights.

4. The writing of the paper needs to be improved. In section 3.3, the result for \mu-PL objectives should be formulated as a formal theorem.

### Questions
Refer to weeknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for improving FL in the presence of second order data heterogeneity. This is achieved by mitigating client drift over the training duration by estimating the global update direction while also regularizing the local objective.

### Strengths
The paper does good over outlining prior art and motivating the problem sufficiently. The tackled domain is of particular importance in Federated Learning as assuming in certain instances first-order heterogeneity can be problematic. The method seems sound and the theoretical bounds provided for both general cases as well as in the case of μ-PL are also appreciated.

The paper is quite dense but given the content packed I found it easy to read.

### Weaknesses
There are a few questions that I would like to ask the authors,

- The method is claimed to be stateless by design, but what the authors mean in practice is not clearly defined nor tested in the experiments. Specifically, it is unclear how the method handles scenarios where clients might drop out randomly or rejoin after a period of inactivity, and how this affects the convergence and stability of the global model. The paper lacks a clear definition of 'stateless' in the context of federated learning and does not provide any empirical validation of this claim.
- Lack of discussion on what happens in the case of node errors, communication drop-outs, and/or stragglers. The paper does not address the practical challenges of real-world federated learning deployments, such as clients experiencing network issues or computational delays. It is unclear how the proposed method would perform in such scenarios and whether it includes any mechanisms to mitigate the impact of these issues on the training process. For example, how does the method handle a client that is consistently slower than others or a client that drops out mid-training?
-  Lack of discussion on what happens if clients have different dataset sizes and how this affect the training. The paper does not consider the implications of varying dataset sizes across clients. It is not clear how the method would handle scenarios where some clients have significantly more data than others, and whether this could lead to biased or suboptimal global models. It is necessary to discuss whether the method is robust to such data imbalances and how it compares to other methods that explicitly address this issue.

### Questions
I have a few questions about the manuscript,

- Have the authors tampered with the template? I found that I could not search using my accessibility tools and no text was selectable - is there any particular reason for doing this? I find that people that use specialty equipment might struggle with this...
- Why the code was not included in the paper submission? I understand that this can be made public after review but I think it is an essential for proper review and it can be attached as supplementary material not disclosed publicly.
- Clarify what the authors mean by "stateless by design" as per weaknesses above.
- What happens if a client drops during the computation? Is that handled?
- Does the framework assume equal participation of clients? What happens in the case that there are clients that "dominate" the training? Does this affect the end result (perhaps, due to the uniform sampling used...?)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose a novel algorithm for FL under Hessian similarity assumption. Authors provide theoretical analysis for the proposed method, showing $O(\delta \epsilon^{-2} \sqrt{M})$ complexity for general non convex problems and $\tilde{O}(\delta/\mu \sqrt{M} + M)$ complexity for problems under PL condition. Experiments on logistics and NNs are provided and support the theory.

### Strengths
1. Novel method SABER for non convex FL under Hessian similarity. 
2. Theoretical analysis, showing that the convergence rate of SABER aligns with the rate of Gradient Descent ($O(\epsilon^{-2})$).
3. Extensive numerical experiments supporting the theory.

### Weaknesses
1. Solution of the subproblem. The subproblem can be non convex. In this case GD for the subproblem would require $\epsilon^{-2}$ iterations to find $\epsilon$-stationary point. That might significantly slow down the convergence of the whole procedure. Moreover, it is assumed that the subproblem could be solved exactly. In my point of view, this not only makes the method impractical, but also simplifies the theoretical analysis.
2. Partial participation. Authors claim that SABER allows for partial participation (PP). As far as I understand, SABER with PP is listed as Algorithm 2. However, theoretical analysis is only presented for Algorithm 1, where participation of all clients is necessary, consequently relegating Algorithm 2 to a heuristic approach.
3. The experiments were conducted with a single local step for all methods. This setup might not be appropriate for Federated Learning (FL) algorithms with local steps, given that the primary aim is to reduce the number of communications by leveraging local updates.

### Questions
1. Abstract, first bulletpoint on page 3, page 6. I think it should be $O(\delta \epsilon^{-2} \sqrt{M})$ instead of $O(\delta \epsilon^{2} \sqrt{M})$. 
2. I think it is better to replace argmin in algorithm with first-order optimality condition and $\phi_k(w_{k+1}) \leq \phi_k(w_k)$, as according to the proof in non convex case finding the actual argmin is not necessary.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a federated learning algorithm called SABER that seeks to mitigate client drift by making each client optimize a modified local function that is the sum of the actual local function and a bias correction term like SCAFFOLD (Karimireddy et al., 2020) and a prox term like FedProx (Li et al., 2020a). Under second-order heterogeneity with parameter $\delta$ (Assumption 1 in the paper), SABER is shown to converge to an $\varepsilon$-stationary point in $\mathcal{O}(\frac{\sqrt{M} \delta}{\varepsilon^2})$ rounds of communication for smooth non-convex functions (the paper mistakenly reports the communication complexity as $\mathcal{O}(\sqrt{M} \delta \varepsilon^2)$ throughout). In addition, under the $\mu$-PL assumption, the complexity improves to $\mathcal{O}((\frac{\delta}{\mu}\sqrt{M} + M) \log \frac{1}{\varepsilon})$. Empirical results on CIFAR-10 and FEMNIST show the benefits of SABER compared to some baseline algorithms.

### Strengths
1. This paper proposes a way to address the important issue of client drift in federated learning. Specifically, it maintains one control variate for all the clients which is efficient.

2. Sharp $\mathcal{O}(\frac{\sqrt{M}}{\varepsilon^{2}})$ complexity in the smooth non-convex case (although this result is under the strong assumption of $w_{k+1} = \text{argmin } \phi_k(w)$ as I have mentioned in Weakness #1).

3. The second-order heterogeneity assumption is well motivated.

4. Appreciable improvement over FedAvg, FedProx and SCAFFOLD (although I have some reservations about these results which I have described in Weakness #4).

### Weaknesses
The authors mistakenly report the communication complexity as $\mathcal{O}(\sqrt{M} \delta \varepsilon^2)$ for the smooth non-convex case; I guess it should be $\mathcal{O}(\frac{\sqrt{M} \delta}{\varepsilon^2})$.

**Weaknesses/Concerns:**

**1.** The definition of $w_{k+1} \approx \text{argmin } \phi_k(w)$ in Algorithm 1 is very vague; how is $\approx$ quantified? 
Further, for the theoretical results in Section 3.2, as far as I understand (by looking at the proof of Lemma 3), $w_{k+1}$ has been taken to be exactly $\text{argmin } \phi_k(w)$. The authors have not discussed this point. *It is unreasonable to expect that $\phi_k(w)$ can be exactly minimized* and I'd like to see a result where $w_{k+1}$ is an approximate minimizer of $\phi_k(w)$, for e.g., an $\varepsilon$-stationary point of $\phi_k(w)$ as written in Section 3.1. 


**2.** Moreover, the complexity of minimizing $\phi_k(w)$ to obtain $w_{k+1}$ has been completely ignored in Section 3.2; this is an important aspect that has not been considered. This could have been captured if there were *local steps* in the proposed algorithm; specifically, I'd find the result more convincing if there were some $H \geq 1$ local steps of (S)GD on $\phi_k(w)$ to *approximately minimize* it and the final convergence bound in Theorem 1 would be a function of both $K$ and $H$. 

I understand that the emphasis is probably on reducing the communication complexity but deriving results assuming that the local surrogate functions can be *exactly* minimized is unrealistic and too strong according to me. I'd like to see the theoretical results capture the inexactness of the approximate minimizer of $\phi_k(w)$ as this would probably entail practically important tradeoffs.

**3.** [1] and [2] (cited below) are two relevant works that have not been touched upon by this paper. Step 5 in Algorithm 1 of this paper is virtually the same as Step 4 in Algorithm 1 (PAGE) of [1]. Note that [1] is for the centralized setting. [2] proposes a federated version of PAGE called FedPAGE. *But unlike SABER, (Fed)PAGE does not need to minimize any surrogate function*. Moreover, (Fed)PAGE also attains $\mathcal{O}(\frac{\sqrt{M}}{\varepsilon^{2}})$ complexity. So it appears that the algorithms proposed in [1] and [2] are similar to SABER and attain the same complexity as SABER *without* its compute-intensive part, viz., minimizing $\phi_k(w)$. A detailed comparison of SABER with (Fed)PAGE is needed and this includes experiments.

[1]: Li, Zhize, et al. "PAGE: A simple and optimal probabilistic gradient estimator for nonconvex optimization." International conference on machine learning. PMLR, 2021.

[2]: Zhao, Haoyu, Zhize Li, and Peter Richtárik. "FedPAGE: A fast local stochastic gradient method for communication-efficient federated learning." arXiv preprint arXiv:2108.04755 (2021).

**4.** I also have some concerns w.r.t. the experimental results in the paper. As per Section 4.1, $p=0.5$ and 50 out of 100 clients are used in line 8 of Algorithm 2 for CIFAR-10. So 50% of the clients are used in every other round. It is not clear to me if the benefits of SABER are because of this. For FEMNIST, I could not find the total number of clients (the authors should clearly state this) but it is mentioned that 100 clients are used in line 8 of Algorithm 2 again with $p = 0.5$. Anyway, I think $p = 0.5$ is too large and the algorithm is practically useful only if it works with much smaller values of $p$ such as 0.1, etc. I'd like to see an ablation study showing the effect of varying $p$. Also, it is not clear to me if the hyper-parameters were tuned for the other algorithms. Finally, as I mentioned in point #3, there should be some empirical comparisons with FedPAGE too given its similarity to SABER.

Due to the above weaknesses, I can only give a score of 3 for now.

### Questions
Please address the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
