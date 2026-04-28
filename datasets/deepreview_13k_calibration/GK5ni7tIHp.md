# Training-free Guidance in Multi-modal Generative Flow for Inverse Molecular Design

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Given an unconditional generative model and a predictor for a target property (e.g., a classifier), the goal of training-free guidance is to generate samples with desirable target properties without additional training. As a highly efficient technique for steering generative models toward flexible outcomes, training-free guidance has gained increasing attention in diffusion models. However, existing methods only handle data in continuous spaces, while many scientific applications involve both continuous and discrete data (referred to as multimodality). Another emerging trend is the growing use of the simple and general flow matching framework in building generative foundation models, where guided generation remains under-explored. To address this, we introduce TFG-Flow, a novel training-free guidance method for multimodal generative flow. TFG-Flow addresses the curse-of-dimensionality while maintaining the property of unbiased sampling in guiding discrete variables. We validate TFG-Flow on four molecular design tasks and show that \method has great potential in drug design by generating molecules with desired properties.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors develop a training-free approach to guide a pre-trained multimodal flow model to generate molecules with specified properties.  They do so by introducing  the guided velocity and guided rate matrix.

### Strengths
Training-free guidance makes it computationally advantageous over other flow-based molecular generation models.

### Weaknesses
 * To me, the biggest weakness lies in the following missing piece of the explanation of the "mutlimodal flow model". My understanding of the base model is the following. We train the model $p_{1|t}(G_1 | G_t)$, we then use it to estimate marginal velocities described in Equations (7), (9) and (10). This allows us to take a small step to estimate $G_{t + dt}$ based on $G_t$. This implicitly implies that $p_{1|t}$ is efficient to sample from. Otherwise, this procedure would be very expensive. My question is the following: "If we know how to efficiently sample from $p_{1|t}$, why bother with the flow model at all? Why not just sample $G_0 \sim p_0$ and directly sample $G_1 \sim p_{1|0}(G_1 | G_0)$ ? I read the paper that authors build on [1], but I do not think this is explained properly there either. Here are follow-up questions:
  * How is $p_{1|t}$ parametrized? I do not mean what architecture of the model, but what kind of a model? Is this a generative model? If so, what kind? (GAN, NF, VAE, sth else?). The paper does not specify the exact form of the distribution $p_{1|t}$, which is crucial for understanding the sampling process and the validity of the derived equations. The notation suggests a probability distribution, but the text only mentions a neural network outputting a sample, which is insufficient to define a distribution. Without a clear definition of $p_{1|t}$, it's difficult to assess the theoretical soundness of the approach. For example, is it a Gaussian with a mean and variance predicted by the network, or is it something else entirely?
  * The marginal flow is given by an expectation under $p_{1|t}$. I assume that this is approximated using Monte Carlo estimation? How many samples are used? What variance does this exhibit? The paper does not specify how the expectation under $p_{1|t}$ is computed. If Monte Carlo estimation is used, the number of samples and the resulting variance should be reported, as these factors directly impact the accuracy and stability of the method. The lack of this information makes it hard to evaluate the practical performance of the proposed approach.
  * In lines 196-197 you say that $g$ parametrizes this model and for input $G_t$ returns "sample/likelihood of $G_1$". What does the slash "/" mean? Does it return both the sample and the corresponding likelihood? I think this narrows down the choices for $p_{1|t}$, because not all generative models can return do both: generate samples and their corresponding likelihoods. The notation "sample/likelihood" is ambiguous. It is not clear whether the model outputs both a sample and its likelihood, or if it outputs one or the other depending on the context. This needs to be clarified, as it restricts the possible choices for the underlying model $p_{1|t}$.
  * If one can efficiently sample from $p_{1|t}$ why not just generate a collection of $G_1 \sim p_{1|t}(G_1|G_t)$ and choose the one with the highest value of our property predictor $f$? Have the authors considered such a baseline? How would this compare to the proposed method?  think that this is very closely related to what authors are actually doing implicitly (see Question 2 is the questions section below)
* Benchmark model size/runtime comparison in Tables 1, 2 and 4. I think that the model comparison would be much more meaningful if we had the following information:
  * What are the model sizes?
  * What is the runtime of each model, both training and inference? The lack of information about model sizes and runtimes makes it difficult to compare the proposed method with the baselines in terms of computational efficiency. A table summarizing the total training time, total parameter count, and total sampling time for each method would be very helpful.
* Lack of comparison with optimization-based structure-based drug design methods. In table 4, I would strongly suggest comparing with optimization-based method like Autogrow4. E.g. in [3] it was shown to be a very strong baseline and it makes a fair comparison, because the method you are proposing is an optimization-based method and not merely generative one like the ones used as baselines.

### Questions
1. Could you explain why the conditional independence of trajectory and target holds? 
2. Could you elaborate on how the hyperparameter \alpha_t is chosen or tuned in practice?
3. Since the method depends on a predictor to guide property adherence, is there any evaluation of how predictor quality or accuracy impacts the overall performance of the guided generation?
4. There is typo in Table 4, for Vina score, TFG-Flow was falsely bolded.

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
5

### Summary
This paper studies the conditional generation problem in the context of molecular generation. Specifically, the authors propose a "classifier-guidance" approach for inherently multimodal molecular structures (atom token and coordinate) with flow matching/rectified flow-based generative models. Experiments are conducted on several molecular optimization problems.

### Strengths
* Conditional generation is an important and practical problem in molecular design. In fact, previous work in this space (recent trend of diffusion-based generative models) has under-studied how to do conditional generation and molecular optimization.
* The proposed method is straightforward and effective based on validations from experiments.

### Weaknesses
* Even though conditional generation is under-studied in the small molecular generation domain, it is well-studied in other domains (especially on exact guidance; see questions). [1,2,3]
* Molecular optimization has been a long-standing challenge in this field and unfortunately, almost none of them are mentioned or compared, see the review [4] for references.

[1] Lu, C., Chen, H., Chen, J., Su, H., Li, C. and Zhu, J., 2023, July. Contrastive energy prediction for exact energy-guided diffusion sampling in offline reinforcement learning. In International Conference on Machine Learning (pp. 22825-22855). PMLR.

[2] Wu, L., Trippe, B., Naesseth, C., Blei, D. and Cunningham, J.P., 2024. Practical and asymptotically exact conditional sampling in diffusion models. Advances in Neural Information Processing Systems, 36.

[3] Zhao, S., Brekelmans, R., Makhzani, A. and Grosse, R.B., Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo. In Forty-first International Conference on Machine Learning.

[4] Du, Y., Jamasb, A.R., Guo, J., Fu, T., Harris, C., Wang, Y., Duan, C., Liò, P., Schwaller, P. and Blundell, T.L., 2024. Machine learning-aided generative molecular design. Nature Machine Intelligence, pp.1-16.

### Questions
* Is the guidance exact? i.e. if you write down the conditional vector field of the target distribution, is it equal to Eq 15? It seems you only have the term for guidance without the original vector field. In addition, in the diffusion literature, it is known that evaluating the guidance gradient as $\nabla E(\mathbb{E}_{X_1|X_t}(X_1))$ is not exact, where $E$ is the energy here, e.g. see [1].
* for Eq 15, should it be $X_{t+1} \leftarrow X_{t} + \cdots$?
* The rate matrix R is not properly defined, i.e. what does $R(\cdot, \cdot)$ mean?
* In Sec 3.2, why is the expectation calculation exponentially growing? Since you only need to model for each atom their rate matrix, is it in the order of $n|A|$?
* Is the Monte Carlo estimator for Eq 12 biased?
* In structured-based drug design, there exist methods for property optimization, e.g. see [2] using an evolutionary algorithm.

[1] Lu, C., Chen, H., Chen, J., Su, H., Li, C. and Zhu, J., 2023, July. Contrastive energy prediction for exact energy-guided diffusion sampling in offline reinforcement learning. In International Conference on Machine Learning (pp. 22825-22855). PMLR.

[2] Schneuing, A., Harris, C., Du, Y., Didi, K., Jamasb, A., Igashov, I., Du, W., Gomes, C., Blundell, T., Lio, P. and Welling, M., 2022. Structure-based drug design with equivariant diffusion models. arXiv preprint arXiv:2210.13695.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors tackle the problem of training-free guidance in multi-modal generative flow. Specifically, the work builds on the recent development of "Multiflow", i.e. a flow-based generative model for mixed modality data (i.e. discrete and continuous). This paper describes how one can perform guidance in such models without any additional training and only requiring access to time-independent property predictor. Emprically, superiority over other training-free guidance methods is demonstrated.

### Strengths
* I think that the paper is very well written. The problem setup and motivation are clearly explained; the method and contributions are described in a way that is easy to understand.
* Theoretical contributions, which are precisely stated and proven.
* Encouraging experimental results.
* Submitted code for improved reproducibility.

### Weaknesses
* To me, the biggest weakness lies in the following missing piece of the explanation of the "mutlimodal flow model". My understanding of the base model is the following. We train the model $p_{1|t}(G_1 | G_t)$, we then use it to estimate marginal velocities described in Equations (7), (9) and (10). This allows us to take a small step to estimate $G_{t + dt}$ based on $G_t$. This implicitly implies that $p_{1|t}$ is efficient to sample from. Otherwise, this procedure would be very expensive. My question is the following: "If we know how to efficiently sample from $p_{1|t}$, why bother with the flow model at all? Why not just sample $G_0 \sim p_0$ and directly sample $G_1 \sim p_{1|0}(G_1 | G_0)$ ? I read the paper that authors build on [1], but I do not think this is explained properly there either. Here are follow-up questions:
  * How is $p_{1|t}$ parametrized? I do not mean what architecture of the model, but what kind of a model? Is this a generative model? If so, what kind? (GAN, NF, VAE, sth else?).
  * The marginal flow is given by an expectation under $p_{1|t}$. I assume that this is approximated using Monte Carlo estimation? How many samples are used? What variance does this exhibit?
  * In lines 196-197 you say that $g$ parametrizes this model and for input $G_t$ returns "sample/likelihood of $G_1$". What does the slash "/" mean? Does it return both the sample and the corresponding likelihood? I think this narrows down the choices for $p_{1|t}$, because not all generative models can return do both: generate samples and their corresponding likelihoods.
  * If one can efficiently sample from $p_{1|t}$ why not just generate a collection of $G_1 \sim p_{1|t}(G_1|G_t)$ and choose the one with the highest value of our property predictor $f$? Have the authors considered such a baseline? How would this compare to the proposed method?  think that this is very closely related to what authors are actually doing implicitly (see Question 2 is the questions section below)
* Benchmark model size/runtime comparison in Tables 1, 2 and 4. I think that the model comparison would be much more meaningful if we had the following information:
  * What are the model sizes?
  * What is the runtime of each model, both training and inference?
* Lack of comparison with optimization-based structure-based drug design methods. In table 4, I would strongly suggest comparing with optimization-based method like Autogrow4. E.g. in [3] it was shown to be a very strong baseline and it makes a fair comparison, because the method you are proposing is an optimization-based method and not merely generative one like the ones used as baselines.

---

References

[1] Campbell et al "Generative Flows on Discrete State-Spaces: Enabling Multimodal Flows with Applications to Protein Co-Design" (ICML 2024)

[2] Spiegel et al. "Autogrow4: an open-source genetic algorithm for de novo drug design and lead optimization" (ChemInf 2020)

[3] Karczewski et al. "WHAT AILS GENERATIVE STRUCTURE-BASED DRUG DESIGN: TOO LITTLE OR TOO MUCH EXPRESSIVITY?" (Arxiv)

### Questions
* Line 317: "Mathematically, we expect...". Why do we expect this? Could the authors elaborate? Is this a heuristic with desirable properties (favouring larger values of $f$) or is this more principled?
* Line 319: "One can show..." I am not sure that this is true. To me this looks more like gradient ascent of $x \to \log f (\mathbb{E}(X_1|X_t=x, a_t))$ than generating samples according to some distribution. Could the authors elaborate?
* Table 1: I think that highlighting the results for TFG-Flow in bold is misleading. I was under the impression that this is the best method overall and not only among training-free methods. I think that the authors should make the rank of methods more transparent. This also goes back to the point of Weakness (2): Perhaps the training-free methods are not even faster, since we do not know the runtime of the baselines and the proposed method, I do not think this is justified to evaluate them separately (i.e. TFG-Flow should not be in bold since it is significantly worse than EEGSDE). If, however, it is much faster due to being training-free than one can argue why they might be considered in different categories.
* Lines 470, 473:  The authors say that they train the drug quality prediction network, but then they say that there is no need to train the oracle target predictor. So what is trained and what does not need to be trained?
* Line 479 - Is this a reasonable definition of the target? Do we want to match the quality to the reference or do we want to maximize it? The current formulation looks like it wants to match (maximized at $\mathcal{E}(G) = c$). Why not maximize?
* Line 1499 - why is this assumption incorrect?

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
In this paper, the authors present a guidance approach multi-modal continuous normalizing flows trained using flow matching. This field is currently very active, but the authors present a new formal approach to this problem, which they claim does not need any further training: Using a "foundation model," (modeling p(x)) and an off-the-shelf predictive model (modeling y=f(x)), they generate conditional samples p(x|y). 
Minor comment:
The transport/continuity equation is repeatedly referred to as the Fokker-Planck equation.

### Strengths
- Strong formal framework. Broad applicability beyond molecular examples shown in this work.
	- Good results, and transparency about limitations and cases where performance is less good.
	- Several experiments targeting different molecular problems.

### Weaknesses
- Main condition for the paper is training free guidance, all the benchmarks shown where the results stand out, use models which are trained for the purpose guidance. 
        - Presentation suffers somewhat from being overly compact.

### Questions
- One of the key contributions is Theorem 3.4, which provides a sampling estimator for the conditional rate matrix (guided discrete flow). The scaling property is good compared to the baseline, but may still be prohibitive in many applications, e.g. experimental design. How does, the variance of the estimator grow if k<K samples are used? Are there some ways to further improve on this estimator to make it useful in other application domains?

### Soundness
3

### Presentation
2

### Contribution
3
