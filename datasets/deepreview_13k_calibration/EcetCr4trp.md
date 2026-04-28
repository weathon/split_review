# Understanding Convergence and Generalization in Federated Learning through Feature Learning Theory

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Federated Learning (FL) has attracted significant attention as an efficient privacy-preserving approach to distributed learning across multiple clients. Despite extensive empirical research and practical applications, a systematic way to theoretically understand the convergence and generalization properties in FL remains limited. This work aims to establish a unified theoretical foundation for understanding FL through feature learning theory. We focus on a scenario where each client employs a two-layer convolutional neural network (CNN) for local training on their own data. Many existing works analyze the convergence of Federated Averaging (FedAvg) under lazy training with linearizing assumptions in weight space. In contrast, our approach tracks the trajectory of signal learning and noise memorization in FL, eliminating the need for these assumptions. We further show that FedAvg can achieve near-zero test error by effectively increasing signal-to-noise ratio (SNR) in feature learning, while local training without communication achieves a large constant test error. This finding highlights the benefits of communication for generalization in FL. Moreover, our theoretical results suggest that a weighted FedAvg method, based on the similarity of input features across clients, can effectively tackle data heterogeneity issues in FL. Experimental results on both synthetic and real-world datasets verify our theoretical conclusions and emphasize the effectiveness of the weighted FedAvg approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the convergence and generalization properties of FedAvg for two-layer convolutional neural networks (CNNs). To do so, the authors consider a setting where the input data is divided into a signal part and noise part, with the signal being different across different clients and the noise being independently sampled from a Gaussian distribution. The analysis then tracks the coefficients of the signal and noise in the model updates done by clients and also in the global averaging step done in FedAvg. Based on this analysis, the authors show that FedAvg can provably benefit from the communication across clients by increasing the signal to noise ratio (SNR) in the global model updates. In some regimes, this can lead to FedAvg achieving near-zero test error while individual local training at clients achieves a large constant error. These theoretical results are then verified experimentally on a synthetic dataset. The authors also propose a weighted FedAvg approach which is tested empirically on some real-world datasets and shown to outperform FedAvg.

### Strengths
* The analysis clearly establishes feature learning for this particular class of NNs, unlike most existing work on NNs which are focused on the lazy training regime and hence are not really doing feature learning.

* The analysis shows that FedAvg provably benefits from collaboration among clients, by increasing the SNR compared to local training. This in turn leads to better generalization guarantees for FedAvg.

### Weaknesses
 * The presentation of the neural network model can be improved. The authors refer to this as a CNN model but it is not clear immediately what is the channel size, width and stride of this CNN model. It would be nice if authors could illustrate this in a figure either in the main text or appendix. Additionally, the authors also assume the weights of the second layer are fixed, which simplifies the problem. The description lacks detail on how the convolution operation is applied across the two patches, specifically how the filter $\mathbf{w}_{k,j,r}$ interacts with $\mathbf{x}^{(1)}$ and $\mathbf{x}^{(2)}$. A visual representation would greatly aid in understanding the model's architecture. Furthermore, while fixing the second layer simplifies the analysis, it also limits the practical relevance of the results, as it deviates from standard CNN training procedures where all layers are typically optimized.

* Assumptions need to be justified better. For instance, I don't understand why $d$ has to be large to ensure an over-parameterized setting. In my understanding, just increasing $m$ should be enough to imply over-parameterization as done in [1]. Also please specify what the are 'statistical properties' that are maintained using Assumption 2. The explanation for why a large $d$ is necessary for over-parameterization is not convincing. It's not clear how the orthogonality of noise vectors is directly related to the over-parameterization of the network. The authors should provide a more rigorous justification for this assumption. Furthermore, the 'statistical properties' mentioned in Assumption 2, which are only vaguely described as being related to Lemmas B.1 and B.2, need to be explicitly stated in the main text for clarity and better understanding of their implications. It is not clear why the width of the network and number of samples need to be polylogarithmic in $d$. 

* There either seems to be a major typo/mistake in Equation (6) (and consequently Equation 8) or I am misunderstanding something. The LHS of Eq. (6) has a $k'$ but the RHS has no dependence on $k'$. Effectively this is implying that $w_{k',j,r}^{(t)}$ is going to be the same for any $k'$, which does not seem to be correct. The equation as written suggests that the updated weight $\mathbf{w}_{k,j,r}^{(t)}$ is independent of the client index $k'$ which is clearly not the intended behavior in a federated learning setting. This needs to be corrected or clarified to show how the averaging step incorporates client-specific updates.

* The analysis does not discuss the effect of the number of local epochs $E$ on the convergence of FedAvg in Theorem 4.3. For instance, in the i.i.d case when $\mu_1 = \mu_2 = \dots, \mu_K$, we would expect that doing more local steps leads to faster convergence. However, if we substitute the lower bound on $\eta$ from Assumption 3 in Theorem 4.3, then it appears that doing more local steps slows down convergence regardless of the data heterogeneity. The analysis should explicitly discuss how the number of local epochs $E$ impacts the convergence rate, especially in the context of i.i.d. data. The current presentation gives the impression that increasing local epochs always slows down convergence, which contradicts common understanding in federated learning. A deeper analysis is needed to reconcile the theoretical results with practical expectations.

* I'm not sure if Lemma 5.2 is implying convergence due to the dependence of $\bar{w}^{\*}_{j,r}$ on $\log(2/\epsilon)$. In my understanding, if we set $\epsilon \rightarrow 0$ then this would imply $\bar{w}^\*_{j,r} \rightarrow \infty $ and hence $\|\|\bar{W}^{(T_1)}-\bar{W}^\*\|\|_F^2 \rightarrow \infty$. The dependence of $\bar{w}^{\*}_{j,r}$ on $\log(2/\epsilon)$ raises concerns about the convergence claims. As $\epsilon$ approaches zero, the norm of the optimal weight vector seems to diverge, which would contradict the notion of convergence. This aspect needs to be thoroughly addressed and clarified.

* The authors should add personalization baselines in the experiments on measuring the performance of Weighted FedAvg. I'm not surprised to see Weighted FedAvg outperform FedAvg in Table 1 and Table 2 given that each client has a personalized model for Weighted FedAvg. Also the authors should make it clear in the abstract and introduction that Weighted FedAvg is a personalization method. The experimental section lacks a comparison with established personalization methods. Without these comparisons, it is difficult to assess the true benefit of the proposed Weighted FedAvg. The fact that each client has a personalized model in Weighted FedAvg makes it necessary to benchmark against other personalization techniques to properly evaluate its performance.

### Questions
* What are some of the novelties/challenges of this analysis compared to Cao et al. (2022) and Kou et al. (2023)? It seems that many of the proof techniques such as using coefficient dynamics is similar to these works.

* Can the analysis be extended the case where clients have signals of different kinds (say with some bound on the dissimilarity of signals at a particular client)? Restricting the data at one client to belong to only one signal is a bit too restrictive in my opinion.

* How is $P$ defined in Section 3.2?

* What is the difference between Lemma 5.3 and Theorem 4.4? It seems they are almost stating the same thing. 

* I would also advise the authors to use different superscripts when referring to local iteration steps versus global averaging steps. One common notation is to use $w_k^{(t,r)}$ for the local models where $t$ refers to the round number and $r$ refers to the iteration number in the $t$-th round. In the current analysis the authors use $t$ for both the local update (Eq. (4)) and global update (Eq. 5) which is a bit confusing.

Typos

* $F_{-1}(W_{+1}, x) $ should be $F_{-1}(W_{-1},x) $ in the line above Eq. (2)
* Summation should be over $n_k$ in the Eq. (4) and not $n$
* $<$ should be outside the bracket in the definition of $L_{D_k}^{(0-1)}(\bar{W}^{(t)})$
* $L_{D_k}$ in Lemma 5.3 is not defined. Maybe the authors meant $L_{D_k}^{(0-1)}$
* "Provably" and not "Probably" in the heading of Section 4.2



**References**
[1] Du, Simon S., et al. "Gradient descent provably optimizes over-parameterized neural networks." arXiv preprint arXiv:1810.02054 (2018).

### Soundness
3 good

### Presentation
2 fair

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
The paper does joint generalization and convergence analysis of FL, using 2-layer NNs.

### Strengths
The paper is largely well-written and seems to be a good work. I have some basic questions which I have asked below.

### Weaknesses
Minor writing issues:
- Page 2, para 1: "under" (rather than "in") a certain condition. Last sentence in this para is not clear. Didn't you earlier say that local algo has no comm.?
- At a few places, mathematical symbols or terms are used before being defined. E.g, $\sigma_p$ in Assum. 4.2, weighted FedAvg in the para above Sec. 6.2.
- Questions are listed below.

3.2 Data Model:
- Why is $y_{k,i}$ Rademacher if $\mathbf y_k$ are labels? Are you assuming a balanced dataset? What is the distr. $P$?

4.1:
- Eq. (6) and (8) are not clear. What is $k'$? And why is there a sum over $k$ present? Where is $k'$ on r.h.s.?

4.2:
- Why is using the same training size for all clients without loss of generality?
- Assum 4.2: what is $\sigma_p$?
- What is the motivation for the defn of $\bar{SNR}_k$?
- Theorem 4.4: in the following discussion, it is stated that $\mu_c$ are orthogonal, are you assuming that $K \geq C$?

Experiments:
- In Assum 4.2 it was assumed that $d$ is larger than $\bar{n} m$. But, in experiments in Sec 6.1, that's not the case ($d=1000 < \bar{n}_{train}.m=5000$). Why?
- In Assum 4.2, $\eta \lesssim 1/d$ is assumed, but in experiments, $\eta=1$ is chosen. Can you explain this divergence?
- In some rows of both Tables 1 and 2, singleset has better performance than FedAvg, e.g., CIFAR10 with Dirichlet or SVHN in Table 2. Why is this happening?

### Questions
3.2 Data Model:
- Why is $y_{k,i}$ Rademacher if $\mathbf y_k$ are labels? Are you assuming a balanced dataset? What is the distr. $P$?

4.1:
- Eq. (6) and (8) are not clear. What is $k'$? And why is there a sum over $k$ present? Where is $k'$ on r.h.s.?

4.2:
- Why is using the same training size for all clients without loss of generality?
- Assum 4.2: what is $\sigma_p$?
- What is the motivation for the defn of $\bar{SNR}_k$? 
- Theorem 4.4: in the following discussion, it is stated that $\xi_k \geq 1$. Since $\{\mu_c\}$ are orthogonal, are you assuming that $K \geq C$?

Experiments:
- In Assum 4.2 it was assumed that $d$ is larger than $\bar{n} m$. But, in experiments in Sec 6.1, that's not the case ($d=1000 < \bar{n}_{train}.m=5000$). Why?
- In Assum 4.2, $\eta \lesssim 1/d$ is assumed, but in experiments, $\eta=1$ is chosen. Can you explain this divergence?
- In some rows of both Tables 1 and 2, singleset has better performance than FedAvg, e.g., CIFAR10 with Dirichlet or SVHN in Table 2. Why is this happening?

### Soundness
3 good

### Presentation
3 good

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
This paper studies a scenario where each
client employs a two-layer CNN for local training
on their own data by tracking the trajectory of signal learning and noise
memorization in FLs. The paper shows
that FedAvg can achieve near-zero test error by effectively increasing the signal-to-noise ratio in feature learning, while pure local training without communication
achieves a large constant test error. Inspired by the theoretical results, the paper proposes a heuristic weighted FedAvg which leverages the similarity of local representations into mixing weights.

### Strengths
The paper presents a fresh perspective and innovative techniques. It successfully demonstrates fruitful results, offering valuable insights into the generalization of FedAvg.

### Weaknesses
1. My primary concern with this work is its inability to effectively account for the influence of local training rounds (i.e., $E$ in the paper) on generalization performance. The paper only demonstrates that when $E=\infty$, which signifies no server-worker communication, the generalization performance is inferior compared to the scenario with $E<\infty$. This can be partly attributed to the reduced amount of data utilized in client collaboration. It will be more exciting to see any trend within the regime $1\leq E<\infty$. 

2. The paper establishes that training convergence is independent of data heterogeneity, a finding that appears to contrast with a substantial body of research and empirical observations in FL. It would be greatly beneficial if the authors could provide further elucidation regarding why this particular model exhibits this behavior.

I am open to raising my score if the two points can be adequately addressed.

3. A minor point relates to the clarity of the writing. The paper's notations appear somewhat redundant and disorganized. For instance, the notations $\mu^{(1)}, \dots, \mu^{(C)}$ are not used beyond Section 3.2, and the definition of $\sigma_p$, which plays a pivotal role in signal-to-noise ratios, is missing. In Equation (4), it might be more appropriate to replace $n$ with $n_k$. I recommend that the authors thoroughly review the manuscript to enhance its overall clarity and coherence.

### Questions
NA


=================================

I raised my score after the rebuttal.

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
This paper studies the optimization dynamics and generalization behavior of FedAvg several neural networks in federated learning. Inspired by feature learning theory, they prove that FedAvg converges with gradient descent optimization under a certain data-generating model.

### Strengths
The paper is generally well-written, making me easy to follow the logic flow. The motivation is strong, and the theoretical results are intuitive. Moreover, the authors honestly discuss the limitations of the paper in conclusion.

### Weaknesses
The contribution of this paper is still a bit unclear to me, probably since I am not familiar with federated learning: It seems that the optimization dynamics turns to be *explicit* in the setting of this paper (a certain data-generating model, homogeneous two-layer CNNs and gradient descent optimization), and the results seem *direct* under the classical analysis of gradient descent. I am wonder whether this setting is representative enough, could the authors elaborate the technical innovations on this point?

Another thing that I am concerned is that the current result are strongly related to the neural networks. In my understanding, federated learning is a topic *independent* of neural networks. Could the authors discuss the probabilities that the theory in this paper can go beyond just using two-layer CNNs to be individual models? 

(minor) Some symbols and equations should be defined and clearly explained. The authors should check Section 3 and 4 to make sure that all symbols are defined in their occurances.

### Questions
- It would be better if the authors explain the rationale behind the two-patch feature generation model again *just below* its definition. Moreover, should the signal patch and the noise patch necessarily have same dimension? 
- What is the expression of the distribution $P(\mu^{(1)},\mu^{(2)},\cdots,\mu^{(C)})$?
- Page 3: $F_{-1}(W_{+1}, x)$ should be $F_{-1}(W_{-1}, x)$
- Page 4: $yf(\bar{W}^{(t)}, x<0)$ should be $yf(\bar{W}^{(t)}, x)<0$
- What is $w_{k',j,r}$ in eq.(6) and (8)? It seems that the right-hand-side is independent of $k'$.
- (minor) Theorem 4.3 is a "best-iterate" result. Could it be turned into a "last-iterate" or "average-iterate" guarantee?
- The discussion below Theorem 4.4 could be made more accessible. Specifically, when justifying the superiority of FedAvg compared to local training, could the authors elaborate more, rather than just discussing on two equations on SNR?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
