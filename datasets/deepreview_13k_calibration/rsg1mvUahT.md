# Federated Wasserstein Distance

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
We introduce a principled way of computing the Wasserstein distance between two distributions in a federated manner.
Namely, we show how to estimate the Wasserstein distance between two samples stored and
 kept on different devices/clients whilst a central entity/server orchestrates the computations 
 (again, without having access to the samples). To achieve this feat, we take advantage of the geometric 
properties of the Wasserstein distance -- in particular, the triangle inequality -- 
 and that of the associated {\em geodesics}: our algorithm, \ours (for Federated Wasserstein Distance), iteratively approximates 
 the Wasserstein distance by manipulating and exchanging distributions from the
  space of geodesics in lieu of the input samples. 
  In addition to establishing the convergence properties of \ours,
   we provide empirical results on federated coresets and federate 
   optimal transport dataset distance, that we respectively exploit for
   building a novel federated model and for boosting performance of popular federated learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a novel algorithm for computing the widely used Wasserstein distance (WD) that is in line with federated learning (FL). In particular, as WD is used in a wide range of tasks where privacy is of major concern, FL is a favorable paradigm to conduct its computation in practice. To this end, the paper proposed to utilize the structure of WD and to communicate between server and each client individually. For each iteration of the proposed algorithm, a measure is sent from server to a client, and a barycenter between this and the clients data is computed and sent back. The paper provides theoretical guarantees that the resulting aggregated distance converges to the actual WD in the limit, and in some cases even in 1 step. Computational complexity of the proposed algorithm is also discussed, with certain reduction possible. Various experiments are given to illustrate the performance of the proposed algorithm compared to the vanilla WD, showing that the performance is not compromised.

### Strengths
The paper is overall well presented and the writing is clear. The contribution is original to the knowledge of the reviewer.
Some main strengths:
1: The main problem the paper, i.e. FL for WD, is novel and deserves attention. As WD heavily depends on both data sets at the same time, how to minimize the exposure of the raw data is of theoretical importance. The paper proposes a framework that is in line with FL.
2. The paper covers most major aspects of practicality of FL for WD, including both theoretical and computational properties.

### Weaknesses
Although the idea of FL for WD is indeed interesting and deserves attention, I have a major concern on whether the proposed algorithm is really compliant with FL principles. Specifically, for each iteration, the server sends a distribution $\xi$ to client with data $\mu$, then a $t$-barycenter $\xi_\mu$ is sent back to the server. By structure of WD geodesic, with knowledge of $\xi$ and $\xi_\mu$ it is already very immediate to reconstruct $\mu$. For instance, if $\xi = \frac{1}{n}\sum_i \delta_{x_i}$ and $\mu = \frac{1}{n}\sum_i \delta_{y_i}$ are both $n$ points uniformly distributed, with optimal correspondence being $T:x_i\to y_i$, then $\xi_\mu = \frac{1}{n}\sum_i \delta_{(1-t)x_i+ty_i}$, and the optimal correspondence between $\xi$ and $\xi_\mu$ will be $T':y_i\to (1-t)x_i+ty_i$. Thus by computing $T'$ between $\xi$ and $\xi_\mu$ on server, the server gains full information of the raw data. Surely $t$ is needed, but can also be inferred from the ratios of WDs between $\xi$ and $\mu$, and between $\xi$ and $\xi_\mu$ (to be fair the paper claimed that WD is not necessary to report to the server). The reviewer does not claim full expertise in FL, but does believe that this not fully in line with the FL paradigm, which seeks to minimize the revealing of data from the client to the server. It would be great if this point can be addressed by the authors.

Furthermore, the paper introduces an approximation by using a fixed small number $S$ as the support size of the iterations $\xi$. While this seems to add more privacy and alleviates complexity, it's unclear why it makes theoretical sense (e.g. consistency), as using S different from n can be substantially different from solving (9), thus potentially hindering the guarantees such as convergence. This discrepancy between the practical implementation and the theoretical guarantees needs to be addressed. Finally, the proof of convergence in Theorem 2 is confusing. The reviewer believes that convergence should hold even with random choices of $t$, but the proof does not seem to address this case. The proof states "Hence, by choosing t = 0 and t = 1 in the definition of the interpolating measure", which is confusing as 1) explicit choice of such t is not allowed as remarked in the proof, and 2) there does not seem to be a mechanism to drive $t$ to 0 and 1. The proof, as presented, does not seem correct.

### Questions
The main question is: under an FL setting, is it in line to essentially reveal raw data to the server? As I remarked above, the server essentially have all of the raw data once it receive both responses, so it is unclear why it cannot just compute WD thereafter. Please see above (section Weaknesses) for more details.

Certainly some amount of information has to be revealed to the server in FL, as client is communicating with the server with a locally trained object. Thus one possible way to address this is to perhaps quantify the privacy guarantee in the framework. I'm happy to raise score once this is fully addressed.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an algorithm for a federated computation of the wasserstein distance, where the datasets are held by different agents. Intuitively, this algorithm finds a fixed point $(\xi,\xi^\mu,\xi^\nu)$ of the following system of equations:
$$\xi^\mu=BC(\xi,\mu)$$
$$\xi^\nu=BC(\xi,\nu)$$
$$\xi=BC(\xi^\mu,\xi^\nu)$$
where $BC$ is the operation of computing a Wasserstein barycenter. The authors show communication cost, convergence and a theoretical analysis of some special cases. The proposed algorithm is then applied to a variety of problems.

### Strengths
I think the authors propose an algorithm which could be valuable in federated learning and other data-science applications in the federated setting. The paper is well written and the concepts and development is easy to follow. I especially found Figure 1 to be very insightful. The Theorems support the claims and are valuable. While the setting of Theorem 3 is arguably a bit restrictive, the result is nonetheless very interesting. Specifically the fact that you can compute the Wasserstein distance in only one communication round!

### Weaknesses
Two main desiderata of federated learning are privacy and low communcation cost.
While the problem of communication cost is addressed with (10), the problem of privacy remains largely unanswered. 
If the authors convincingly address the problem of privacy leak, I am open to change my recommendation.
If I correctly understand the reasoning at the bottom of page 4, the authors propose to randomly select $t$ such that the server cannot easily infer $d_{\mu,\xi^{(k)}}$. While I agree that this is improves the privacy, I think that the server can, after just two communication rounds, infer $\mu$ and $\nu$. Consider the simplified setting of theorem 3. 
If the server knows $(m_{\xi^{(k)}}, m_{\xi^{(k)}\mu})$ and $(m_{\xi^{(k+1)}}, m_{\xi^{(k+1)}\mu})$, she knows that $\mu$ must line on the line through $(m_{\xi^{(k)}}, m_{\xi^{(k)}\mu})$ and on the line through $(m_{\xi^{(k+1)}}, m_{\xi^{(k+1)}\mu})$. These lines must cross at $m_\mu$ by construction. (Here, $m_{\xi^{(k)}\mu}$ denotes the mean of $\xi^{(k)}_\mu$).

### Questions
I have two minor comments/questions:
- In Algorithm 1, you use $d_{\mu,\xi^{(k)}}$. While I can infer from the context what it probably means, this symbol has not been used before. I recommend defining it somewhere.
- In the experiments, for the Wasserstein Coreset it does not seem straight forward how your algorithm can be applied to this problem. Could you please explain it to me which agents hold which distributions and where your algorithm enters the computation?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper motivates the Federated Wasserstein distance that would be useful in situations where we what to know the distance between two distributions while the samples of the two distributions are not shared. The authors propose a converging algorithm that can compute such a Federated Wasserstein distance.

### Strengths
I found the problem is well motivated. The theoretical treatment is nice and sound. The numerical experiments are convincing.

### Weaknesses
The presentation of the manuscript could be better.

Theorem 1 seems to be less general than Theorem 2, and it is not clear why we need Theorem 1. Specifically, the conditions under which Equation 10 provides the same result as Equation 5 should be more explicitly stated. The current presentation makes it difficult to understand the specific use cases where the approximation in Equation 10 is valid and beneficial, and how it relates to the more general result in Theorem 2.

It would be beneficial to include an experiment where the datasets are unbalanced, such as one dataset being a constant multiple in size of the other dataset. This would help to understand the robustness of the proposed method under varying data conditions. It is also unclear how the method performs with different data distributions, and an experiment comparing Gaussian and non-Gaussian assumptions would be helpful to show the convergence speed under different scenarios.

### Questions
1. Do we need the two distributions to be discrete and the samples of the two distributions to be the same? Theorem 1 seems to be less general than Theorem 2. If so, the motivation of Theorem 1 should be emphasized and highlighted.

2. I think an experiment where the datasets are unbalanced would be super helpful; say what if a dataset is always a certain times of the other dataset.

3. An experiment that compares the Gaussian & non-Gaussian assumptions to show the convergence speed could be better.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Federated Wasserstein Distance, an algorithm to compute the Wasserstein distance between two measures in the setting of federated learning. Due to the setting, a measure on a client cannot be transferred to the server or the other client to compute the distance. Therefore, the paper utilizes the geometry of Wasserstein distance i.e., triangle inequality and interpolating measure to create transferable measures. To ensure privacy of two interested measures $\mu$, $\nu$, three measures are created $\xi$, $\xi_\mu$, $\xi_\nu$ where $\xi_\mu$ is the interpolating measure between $\xi$ and $\mu$,  $\xi_\nu$ is the interpolating measure between $\xi$ and $\nu$, and $\xi$ is  the interpolating measure between $\xi_\mu$ and $\xi_n$. For a fast computation, McCann’s interpolation is used for constructing the interpolating measure. Experiments on toy examples (Gaussian data) show that FedWD can approximate the Wasserstein distance with a small error. In addition, FedWD is used as the approximation for Wasserstein in coreset classification model, Geometric dataset distances, and  Boosting FL methods. Overall, FedWD shows a "similar" transportation cost as the exact Wasserstein distance.

### Strengths
* The paper tackles a new practice setting for computing Wasserstein distance i.e., federated learning. This is the first work that considers computing Wasserstein distance in this setting.
* The usage of the interpolating measures is the key in this setup which is a novel contribution. 
* There are some (asymptotically) theoretical guarantees for the approximation from FedWD.
* Experiments are conducted on various applications of Wasserstein distance to show a wide range of applications.

### Weaknesses
 * Despite interpolating measures being well-defined for general measures, the paper only considers discrete measures setting. In this setting, interpolating measures can be computed in closed form (after knowing the transportation plan). In the continuous setting, this could be not doable (it seems that a transport map or a parametric measure must be used as the proxy in this setting). Considering the continuous setting e.g., with square L2 cost, could make the paper much stronger.
* The gradient approximation scheme should be discussed. For example, If an application wants to estimate the gradient with respect to the support of a measure of the Wasserstein distance, could FedWd yield any approximations for the gradient?

### Questions
* Could FedWd be extended to continuous cases?
* Could FedWd yield any approximations for the gradient?
* For some ground costs that are not metric e.g., in domain adaptation application, the corresponding Wasserstein cost is not metric hence there is no triangle inequality. In this case, could we have any solutions?
* How does $t$ affect the performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
