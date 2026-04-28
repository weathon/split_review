# Connecting Federated ADMM to Bayes

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 5, 6, 6

## Abstract
We provide new connections between two distinct federated learning approaches based on (i) ADMM and (ii) Variational Bayes (VB), and propose new variants by combining their complementary strengths. Specifically, we show that the dual variables in ADMM naturally emerge through the "site" parameters used in VB with isotropic Gaussian covariances. Using this, we derive two versions of ADMM from VB that use flexible covariances and functional regularisation, respectively. Through numerical experiments, we validate the improvements obtained in performance. The work shows connection between two fields that are believed to be fundamentally different and combines them to improve federated learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work provides a new link between two well-known federated learning approaches: i) Alternative Direction Methods of Multiplier (ADMM) and Partitioned Variational Inference (PVI). The driving idea is that PVI updates have a line-by-line correspondence to the ADMM algorithm, which is even more similar under the assumption of isotropic Gaussian distributions for the family $Q$ of variational densities. In this direction, the authors introduce FedLap, a Laplace-approximation based version of PVI. Such derivation suggests that there exists an almost identical duality between ADMM and the common Bayesian approach to the federated learning problem. Later, having established such a connection, two more variants of FedLap are introduced, the first one (FedLap-Cov) puts a bit more structure in the candidate set Q, such some improvement is observed given some increment in the computational cost. The second variant (FedLap-Func) extends ideas from (Khan & Swaroop, 2021) by allowing the FedLap update of the global server to be an optimization problem and assuming that some inputs are available between local and global servers. Empirical results confirm the hypotheses made and the improvement in the accuracy for the three new FedLap-based methods.

### Strengths
**[S1]** - The work is clear, well-written, and polished. I particularly liked the spirit of first building the connection between ADMM and PVI, for later proposing three new methods/variants of FedLap that incrementally improve the accuracy performance. For those familiar with the probabilistic perspective of federated learning, PVI, and Laplace approximation, the work and particularly the contributions are easy to follow and nice to be proven on the empirical results.

**[S2]** - The drawing of correspondence between ADMM and PVI is elegant, and for sure is a great novel contribution if it has not been done before (I think it hasn't). Despite the introduction of the diagonal covariance in FedLap-Cov made sense to me, and the adaptation of updates seemed also correct. I liked the final technique to ensure the positive definiteness of local and global precision matrices in the paragraphs after (14), quite interesting and useful.

**[S3]** - Despite I did not particularly see the advantages of FedLap-Func in Section 3.4, I see its utility and the spirit of even improving a bit more the performance of FedLap. Here, my experience with such methods is that the ratio improvement/computational-cost-increment is not as favorable as in the FedLap-Cov. I imagine that could have limited the experiments to 10-100 clients only.. I could be wrong on this aspect, though.

### Weaknesses
Despite the fact that I think the work has significant strengths in its current version for being accepted, I detect some unclear parts, or at least "corners" where there is not much light to understand what is going on. Some of these are:

**[W1]** - Computational cost is for sure one. While reading the paper, the missing aspect of the computational cost always rings the bell of an average reader. I say this mainly because the connection between ADMM and PVI is fantastic, but once the improvement is made with FedLap and its variants, it is not explicitly indicated what are we paying to get that extra improvement in the performance. In this direction, I want to say that I am just missing the analysis and the clarity in that regard of the problem. For example, a detailed breakdown of the FLOPs for each method, including local client updates and server aggregation, would be beneficial. Furthermore, the communication overhead, especially the size of the messages exchanged between clients and the server, should be quantified, as this is a critical factor in federated learning.

**[W2]** - I'm fine with Eq. (15) and setting up the update as an optimization problem, but then I do not really know if sharing some soft labels or inputs between local clients and the central server is worth it.. It kind of modifies a bit the spirit of federated learning and introduces extra issues like privacy, etc, that are ignored imho. The practicality of this approach is questionable, as it requires a trusted server and introduces potential vulnerabilities. The assumption that clients can share inputs, even a small number, is a strong one and not always feasible in real-world federated learning scenarios. A discussion of the privacy implications and potential mitigation strategies would be necessary.

**[W3]** - It makes a lot of sense to put the work in the context of Laplace approximation methods, BNNs, etc where basically the parameter times parameter dimension of matrices is a huge problem for scalability. Some light-light indication of this is said around L224-225, but overall, I feel that all of this between Eq. 10 and Eq. 14 is ignored, or at least not being highlighted for the reader (the dimensionality problem, or an indication of what are we considering here). I am particularly concerned about V_k and the client updates. The paper should explicitly state the dimensions of the matrices and vectors involved in the updates, especially $V_k$, and discuss the computational implications of these dimensions. The use of diagonal approximations for the covariance matrices should be justified more thoroughly, and the potential limitations of this approximation should be acknowledged. The impact of this approximation on the accuracy of the method should also be discussed.

**[W4]** - Experiments are fine, but Table 1 is somehow limited. I basically missed some larger datasets, where there is not that much similarity or structure in the data as in MNIST or FMNIST (i.e. Imagenet or similar), and augmenting a bit the number of clients to see what is really the flexibility/resistance of new variants to such challenges. The experimental evaluation should be expanded to include more diverse datasets, such as those with higher dimensionality and more complex structures. The performance of the proposed methods should also be evaluated with a larger number of clients to assess their scalability. It is important to investigate how the performance of the methods changes with varying degrees of data heterogeneity across clients.

### Questions
Some minor questions that I thought about while reading and writing the review:

**[Q1]** - I'm curious to know where the term ‘sites’ in L112 is coming from

**[Q2]** - How does this delta approximation work in L185? How does this approximation affect the general problem?

**[Q3]** - What is the dimension of the second auxiliary/dual variable? I'm always afraid of the use of preconditioning.. could the authors add a bit more details in that regard

**[Q4]** - I didn't understand very well what is indicated in L309

**[Q5]** - L342: M_k = null space, Isn’t this obvious?

**[Q6]** - For Algorithm in Eq. 17. How many training steps per round and updates?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Federated learning is the problem of training a model where training data is distributed over clients and due to privacy must stay on clients. Given $K$ clients and a parameterzed model with paramters $w$, each client can optimize its parameters $w_k$ for $k=1,..,K$ and we need to merge the information to learn a global model $w_g$.

Many methods have been proposed and within which Alternative Direction Methods of Multiplier is a method that ensures the clients and the 
global model converge to the same stationary point, the clients send a $v_k$ vector to the server that (loosly) shows the weight change from the global model $w_k - w_g$, the global model aggregates and updates and replies with the new global model $w_g$.

Similarly Bayesian methods learn an approximate posterior distribution over weights $q(w)$ where clients have their learn their own model $q_k()$ send the server an approximate likelihood function $\hat{t}(w)$. The server aggregates likelihoods, updates the global approximate posterior $q_g()$ and sends it back to the clients, Partitioned Variational Inference (PVI) is a recent work that constructs a common framework covering many prior work methods.

The paper describes the above frameworks. Then the authors show that for a particular choice of $q_k()$, $q_g()$ in the PVI framework, notably where they are Gaussian with a priori fixed variance so only the mean is learnt, corresponds almost exactly line by line with ADMM, i.e. ADMM is a MAP estimate of some specific Gaussian distributions. The authors propose FedLap-Cov that simply generalizes this observation by allowing learnable covariance matrices in the Gaussian distributions. Finally FedLap-func is proposed that effectively allows a subtle data sharing between client and server hence the server can perform weight optimization as well.

Experiments are performed across a range of standard benchmarks showing FedLap variants outperform both poor (FedAvg) and strong (FedDyn) baselines.

### Strengths
## Main Comments
- __intuitive demonstration of equivalence__: models trained by minimizing a loss function and a regularizer are often easily shown to correspond to a log likelihood and a log prior hence correspond to a MAP estimate. This work shows the same connection in a less obvious setting.
- __intuitive extension__: as corollary from above, generalizing the ADMM method for more general distributions makes perfect sense and allows a natural update equations, notably the precision matrix "weighted sum" of global and local models.
- __well written__: the paper takes the reader on a well paced journey through prior works ADMM, PVI using very readable mathematical notation (more readable than the original works in my view). FedLap is then presented to specifically bridge the gap between the prior discussion and the new discussion of FedLap-Cov and FedLap-Func.
- __extensive benchmarks__: UCI datasets, MNIST and Cifar10 experiments are provided and a deeper dive in to FedLap vs FedDyn is given in the appendix. Hyper-parameters were tuned for all methods.

## Minor comments
- I personally like that the authors avoid saying "our method" and opt for the more humble approach of using the method name "FedLap" throughout the paper.

### Weaknesses
I felt the paper was very good and only have minor comments.

### Minor Comments
- __limitations__ I may have missed this but limitations do not seem to be clearly discussed
- __computational complexity__ on P6 only discusses the diagonal covariance case which has linear added complexity. While if I understand correctly, the FedLap-Cov has a quadratic additional parameters, upper triangle of a cov matrix. A few concerns come to mind (1) one goal of federated learning is handling unstable client connections by minimising communication rounds, but presumably also minimising traffic, FedLap-Cov seems to add significant traffic (2) the scalability of the FedLap-Cov to many parameters is limited, e.g. resnet-50, although a quick look at past works suggest small applications like UCI datasets, Cifar10 and MNIST are common benchmarks (and not imagenet).
- __final model is point estimate__ I may have misunderstood, but I could not find explicit mention about what weights at inference time, I assume a single set of weights $w_g$ was used, there was no marginalising. I.e. FedLap methods learn a Bayesian distribution over weights, but the benchmarks have just used a point estimate.
- __Equation 13__: I apologize if I am mistaken but I was rather confused, the first $m_k$ may be a typo? As I understand, in a delta approximation, normally, we would make a 2nd order Taylor approximation of loss $l_k(w)$ around $w=m$. But to avoid headaches with a hessian term with both $m$ and $S$ interacting as we optimize, we freeze the hessian to a value from a prior iteration $w=m_{old}$ artificially removing the dependence on $m$, this is arguably not an accurate Taylor approximation anymore, is this a common practice?


### Possible Typos
- Equation after Eqn 9: $\mathbb{E}[\hat{t}_k(w)]$ missing $\log()$
- Equation 12 square brackets on the second term
- Equation 13: first $l_k(m_k)$ -> $l_k(m)$

### Questions
- for the benchmarks, the weights used in to make predictions were just the MAP estimate? Was there any marginalising predictions over the distributions of weights?
- Equation 13 uses gradients from a point in space that is not the centre of the Taylor approximation, is this principled or just a necessary hotfix?
- Equation 16: can the authors provide some context as to why the new weight space term is subtracted?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors provide new insights connecting ADMM (Alternating Direction Method of Multipliers) and variational Bayesian (VB)-based approaches for federated learning. The main finding reveals that the dual variables utilized in ADMM naturally correspond to the 'site' parameters in VB.

### Strengths
1. connections between ADMM and VB-based approaches may be interesting for federated learning.

### Weaknesses
1. Whether the federated locals can be used to recover the global solution is not justified both theoretically and numerically.

2. Why do you want to connect ADMM to Bayesian? Bayesian learning is known to be the go-to method for conducting uncertainty quantification and non-convex optimization. The algorithm is only evaluated in the optimization perspective. The Bayes interpretation is only used as a preconditioner. If this is the only purpose, the connections to Bayes are not needed at all.

3. Bayes seems to be an important component in this paper. However, the connections to Bayes are not fully evaluated empirically. I recommend the authors to see how the uncertainty experiments are evaluated in [1,2,3].

### Questions
Missing important literatures in Bayes federated learning:

[1]. Federated Learning via Posterior Averaging: A New Perspective and Practical Algorithms. ICLR. 2021.

[2]. On Convergence of Federated Averaging Langevin Dynamics. UAI 2024.

[3]. Bayesian Federated Learning with Hamiltonian Monte Carlo: Algorithm and Theory. JCGS. 2024

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides a first connection between two federated learning approaches, one based on ADMM and another based on Variational Bayes (VB). Based on this connection, the paper proposes two variants that incorporate the full covariance information and functional regularization. The proposed methods improve the ADMM baseline in various benchmarks.

### Strengths
- The connection between ADMM and VB is novel and interesting, which opens up new avenues for improving the algorithm from a variational / Bayesian perspective. 

- The overall empirical results are convincing, showing improvements of the proposed methods against the baseline.

### Weaknesses
The paper can be improved  by adding more discussions on complexity and limitations, as well as empirical results quantification. In particular, the key weaknesses are the following.


- missing discussion on limitations. What is the complexity of the extended VB approaches against the baselines, in particular when full covariance estimates are considered. Additionally, FedLap-Func is used in the setting where some inputs are shared globally. Can you discuss the practical implication of that?

- the empirical comparison needs more statistical rigorousness. Table 1 displays the average accuracy with standard deviation in parentheses, and top two performing algorithms are bolded. Can you elaborate how do you define the "top two"? A more standard practice in statistics is to highlight the top results within 2 *standard errors*, in that case I would imagine, for example, FedDyn and FedLap to be statistically equally performant on CIFAR10 with comm Round=50 (last row of the table 1).

### Questions
see the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper establishes the connection between federate learning and variational Bayes through the "site" parameters in partition variational inference (PVI). For particular choice of variational distribution in VB, PVI could (almost) be identified as an Alternative Direction Methods of Multiplier (ADMM), hence named FedLap. Base on such connection, the authors propose two improvements of FedLap (ADMM) by considering full covariances (FedLap-Cov) and function space (FedLap-Func) information coming from VB literature. Then multiple benchmark tests are carried out to demonstrate the superior performance of the proposed improvements compared with vanilla FedLap and competitive federate learning algorithms including FedAvg, FedProx, and FedDyn.

### Strengths
A nice connection is drawn between federate learning and variational Bayes. Two algorithms improving upon ADMM are proposed based the newly discovered connection. There is good potential in proposed methods, both numerically and methodologically.

### Weaknesses
FedLap-Func only provides marginal improvements over FedLap-Cov and sometimes even makes it worse. Did you explore other problems outside the benchmarks to seek possibly more appropriate applications?

### Questions
* Could you please include a paper outline at the end of Section 1?

* Could you bring the definition of $\hat t^*_k=\frac{q_k}{q_g}$ from (5) to (4) where it appears for the first time? I guessed $\hat t^*_k=\frac{q_k}{p_0}$ while at equation (4).

* `FedLap` seemingly indicates the Laplace variant of the PVI. But it is still Gaussian used as the variational distribution. Why is it called "Lap"? Would you please elaborate?

* FedLap-Func only provides marginal improvements over FedLap-Cov and sometimes even makes it worse. Any explanation?

### Soundness
3

### Presentation
3

### Contribution
2
