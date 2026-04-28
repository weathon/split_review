# Robust Model Evaluation over Large-scale Federated Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
\vspace*{1mm}
In this paper, we address the challenge of certifying the performance of a machine learning model on an unseen target network, using measurements from an available source network. We focus on a scenario where heterogeneous datasets are distributed across a source network of clients, all connected to a central server. Specifically, consider a source network 'A' composed of $K$ clients, each holding private data from unique and heterogeneous distributions, which are assumed to be independent samples from a broader meta-distribution $\mu$. Our goal is to provide certified guarantees for the model’s performance on a different, unseen target network “B,” governed by another meta-distribution $ \mu' $, assuming the deviation between $\mu$ and $\mu'$ is bounded by either the {\it Wasserstein} distance or an $f$-{\it divergence}. We derive theoretical guarantees for the model’s empirical average loss and provide uniform bounds on the risk CDF, where the latter correspond to novel and adversarially robust versions of the Glivenko-Cantelli theorem and the Dvoretzky-Kiefer-Wolfowitz (DKW) inequality. Our bounds are computable in polynomial time with a polynomial number of queries to the $K$ clients, preserving client privacy by querying only the model’s (potentially adversarial) loss on private data. We also establish non-asymptotic generalization bounds that consistently converge to zero as both $K$ and the minimum client sample size grow. Extensive empirical evaluations validate the robustness and practicality of our bounds across real-world tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the generalization capabilities of federated models against unseen clients. Specifically, they aim to provide certified guarantees for the model's performance on a different and unseen target network. Theoretical analysis reveals the importance of the obtained results, where the deviation between different networks is bounded by $f$-divergence or Wasserstein distance.

### Strengths
* The topic is important for the real-world deployment of federated learning models.
* The idea is intuitive and enjoys strong guarantees.
* Extensive experiments have been provided.

### Weaknesses
 * The paper studies federated learning under IID distribution, while the current real-world application leans more toward non-IID clients. In the Introduction, the authors have used many examples to motivate the generalization capabilities of federated learning, which fundamentally stems from non-IID data.
* The presentation of the paper can be improved. For example, the contributions can be listed as bullet points in the Introduction.
* The third part of the related work is confusing. The study of the paper is on IID data, as illustrated in Section 4. Yet, the authors discuss intensively federated learning algorithms under non-IID data. Moreover, the discussion mingles personalized federated learning with non-personalized ones without distinctions. 
* Theorem 5.2 is a strong guarantee in the sense that the generalization gap does not produce a non-vanishing term related to $\epsilon$. However, the authors fail to reason the root cause behind it. Specifically, it is unclear why the adversarial perturbation $\epsilon$ does not directly influence the generalization bound, which is unusual in standard generalization analysis.
* The authors claim that $\hat{B}^{*}(\epsilon)$ is asymptotically minimax optimal. Yet, Theorem 5.2 is a one-sided bound. To claim it is asymptotically optimal, both lower and upper bounds have to be provided. The same concern goes to Theorem 6.2. Furthermore, the notion of 'asymptotically' needs to be rigorously defined in the context of the number of clients and data per client.
* The authors present extensive experiment results, yet, they do not provide codes to reproduce them.

### Questions
* Is it possible to extend the results to non-IID setups? What would be the potential obstacles?
* Can the authors discuss why no non-vanishing term related to $\epsilon$ appears in Theorem 5.2? In addition, what conventional bounds are the authors referring to?
* Can the authors elaborate more on the minimax optimal bounds?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies the problem of model evaluation on unseen clients. The assumption is that each client is associated with a data distribution, and these distributions are from a meta distribution. The evaluation goes as follows: the server requests the client to evaluate a model on its private dataset, and the client returns an adversarial risk. The goal is to provide an upper bound for the risk of the model. Theoretical bounds are provided with assumption that the unseen clients have close data distribution, characterized by f-divergence or Wasserstein distance. Experiments are conducted to support the theoretical claims.

### Strengths
The proof involves multiple advanced results in robust estimation and looks solid.

### Weaknesses
 - It seems that this paper is purely theoretical and it is not clear if the work has real-world applications. For instance, the assumption is that the data distribution for the unseen clients is close in f-divergence or Wasserstein distance. What does this mean for heterogeneous data distribution? Does this assumption work with non-IID data distribution generation in previous research like [1]? Also, the client needs to return a query value with complicated forms; is it feasible to compute? It is a supremum of expectations. 

- It is hard to parse the experiment results. There is no comparison with other methods, making it difficult to evaluate the novelty of this work. Multiple CDF curves are provided, but it is not clear the meaning of the curves. Is the goal to show the correctness of Theorem 5.5 and Theorem 6.2? But these are asymptotic bounds, and it is not clear to me why you can use experiments to show the correctness.

### Questions
- Why is this work related to Federated learning? As far as I can see, the main result is saying if we evaluate a model on some clients, and another client has data distribution that is close enough to those clients, then we can have some bounds on the model risk on this client. The model itself can be arbitrary and does not need to be trained with some FL algorithm. Can the authors elaborate a bit more on the connection with federated learning? 
- The paper also mentions "large-scale" in the title. Is it indeed relevant? The evaluation algorithm does not seem to depend on model structure or can be accelerated for large neural networks.
- Text in Figure 3 is too small to read.

### Soundness
2

### Presentation
2

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
This paper provides certified guarantees for the performance of a model, which is trained on a federated learning network, on an unseen network/clients. The data distribution of the clients in the unseen network follow a meta distribution with bounded deviation from the meta distribution of the training network. The deviation is measured in terms of f-divergence and Wasserstein distance. The upper bounds provided for the performance of the model are in terms of empirical average loss (for both the deviation measures above) and CDF of the loss (for f-divergence only). As the main contribution of the work, the generalization gap in the derived bounds vanishes as number of clients and their dataset sizes grow.

### Strengths
* Despite being a theoretical paper, it is well-written and it is easy to read.
* The work is theoretically rigorous with helpful and easy-to-read explanations about each part.
* The experimental results clearly support the theoretical derivations in the work.

### Weaknesses
There are some weaknesses about the work:
* The existing results in the literature that are closely related to this work are not discussed enough. 

* The authors claim (line 227) that the main advantage of their work is that the generalization gaps in their derived bounds do not have a non-vanishing term, unlike many existing bounds. However, they have not compared their results with at least the best result that exists in the literature. This could be discussed in a separate paragraph after each of the Theorems 5.2, 5.5 and 6.2 (or even deferred to the appendix). Such a discussion would provide a more clear and convincing view of the main contribution and novelty of this work. This could be extended to the experimental results too. 

* There are some experimental results that could improve the draft. I have asked about them in the following questions.

### Questions
Other than the weaknesses mentioned above, which are recommended to be addressed, I have some questions as follows:

* In all the three main theorems, the clients are queried by the server about their "expected" non-robust or robust risk values. What is the main benefit of knowing $n_k$ for the server? From the theorems, we see that $n_k$ appears in either the server's queries (in theorem 5.5) or in the generalization gaps (in theorems 5.2 and 6.2) (and not both). Can we eliminate the $n_k$ from the server's queries and replace them with a lower bound for them? This way, the server would just need a lower bound to do its queries without even knowing the clients' dataset sizes, hence providing some extra privacy. Remember that in some FL settings, the aggregation weights for clients are not based on their dataset sizes, but based on their empirical average risk, e.g., in some FL algorithms addressing performance fairness [1]. In such algorithms, the server does not know the clients' dataset sizes.

[1] Tian Li, Ahmad Beirami, Maziar Sanjabi, and Virginia Smith. Tilted empirical risk minimization. In International Conference on Learning Representations, 2020.


*  Unlike in theorems 5.2 and 5.5, where the query budget is one for each client, in theorem 6.2, the server queries clients about their robust risk values with "polynomially many" values of $\rho$ (robustness radii). What is the value of query budget considered for this case in your experiments? (e.g., in Fig. 3 right). Also, I am wondering how this would affect the bound computed in your experiments? An ablation study on the query budget, when ranging from 1 (similar to theorems 5.2 and 5.5) to larger values would reveal its behaviour when the "computational complexity/communication budget" changes.


* What exactly is the difference between Fig. 1 and Fig. 5? From what I see they are the same. How exactly the "adversarial budget" changes between the two? 


Minor comments:
* line 063: "both" should be dropped?
* line 093: there are two "the"s

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper considers the problem of certifying a model’s performance over a federated clients drawn from an unseen meta distribution that is close to a set of federated clients drawn from a seen meta distribution. 
The theoretical results for certification are given for Wasserstein distance and f-divergence respectively with the help of Glivenko-Cantelli theorem and the Dvoretzky-Kiefer-Wolfowitz (DKW) inequality. Such certification can be computed within polynomial time.

### Strengths
- Having certificates of model’s performance can be important in practice.

### Weaknesses
The paper is presented in a way which is very difficult to understand:

- Important definitions and assumptions are deferred to the appendix.
- Theoretical results are given without much explanation. I don’t know why B^hat is subject in the current form and it is hard to tell if the theorems in the paper makes sense or not. Specifically, the motivation behind the reweighting scheme used to define B^hat is unclear, and the connection to the generalization bounds is not well-established. The paper lacks a clear explanation of why this particular form of reweighting is necessary or sufficient for the stated goals.
- Why for f-divergence we use QVs with rho=0? The intuition behind setting the adversarial perturbation parameter ρ to zero for f-divergence is not adequately explained. It's unclear why this choice is optimal or even reasonable, and how it relates to the overall goal of robust model evaluation under f-divergence shifts. A more thorough justification is needed.
- The name of Definition 5.1 is “meta-distributional f-divergence Ball”,  but the equation (4) additionally assume the Lambda-bounded density ratio which means you don’t actually prove for the entire f-divergence ball. Despite the descriptions above the definition talks about what does Lambda-bounded density ratio do, it is not clear to me is this really necessary or is it just another assumption that makes your proof easier? This discrepancy between the definition's name and the actual condition imposed by equation (4) is confusing. The paper needs to clarify whether the Lambda-bounded density ratio is a necessary condition for the results or simply a simplifying assumption, and if the latter, what the implications are for the generality of the findings.
- The “Lambda-bounded density ratio” assumption is listed in the appendix without any references. Is this new or already exists in the literature. You need to either cite previous works or justify this assumption is realistic. The lack of context for the Lambda-bounded density ratio assumption makes it difficult to assess its validity and relevance. The paper should either provide references to prior work that uses this assumption or offer a compelling justification for why it is a reasonable assumption in the context of federated learning.
- What exactly are c_1 and c_2 in Eq (5) since we need to approximate B^hat? The paper does not provide sufficient detail on how the constants c_1 and c_2 are derived or how they affect the approximation of B^hat. A more thorough explanation of their origin and their impact on the tightness of the bounds is needed.
- For f-divergence, distributions sharing same support should be explicitly listed as an assumption. The paper needs to explicitly state the assumption that the distributions share the same support when dealing with f-divergence. This is a crucial condition for the validity of the theoretical results, and it should not be left implicit.
- It is claimed that the term in line 220 decreases with increasing K and \min n_k. However, it does not specify how fast \min n_k grows. If \log K outgrows  \min n_k then the term does not decrease. The claim that the term in line 220 decreases with increasing K and min n_k is not sufficiently justified. The paper needs to specify the growth rate of min n_k relative to log K to ensure that the term indeed decreases as claimed. Without this clarification, the theoretical results are not fully convincing.
- Line 235 “Additionally, any inherent “wellness” or “robustness” of the target model h is directly reflected through a low value for Bb∗(ε)” There is no guarantee that B(ε) and QK is small. The paper makes a claim about the relationship between the model's wellness and the value of Bb*(ε) without providing sufficient justification. The paper needs to address the possibility that B(ε) and QK may not be small, and explain how this would affect the overall conclusions.
- Certificate of Privacy: I doubt the significance of the claims here. Data recovery attacks are targeting the training where gradients are exchanged in each iteration whereas the task here is to estimate the loss here. Not really fair comparison.

Therefore I don’t think this paper in the current form is ready for publication.

### Questions
See above

### Soundness
2

### Presentation
1

### Contribution
2
