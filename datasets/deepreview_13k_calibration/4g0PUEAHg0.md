# Transformers Learn Bayesian Networks Autoregressively In-Context

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 1, 5, 3

## Abstract
Transformers have achieved tremendous successes in various fields, notably excelling in tasks involving sequential data like natural language processing. Despite their achievements, there is limited understanding of the theoretical capabilities of transformers. In this paper, we theoretically investigate the capability of transformers to autoregressively learn Bayesian networks in-context. Specifically, we consider a setting where a set of independent samples generated from a Bayesian network are observed and form a context. We show that, there exists a simple transformer model that can (i) estimate the conditional probabilities of the Bayesian network according to the context, and (ii) autoregressively generate a new sample according to the Bayesian network with estimated conditional probabilities. We further demonstrate in extensive experiments that such a transformer does not only exist in theory, but can also be effectively obtained through training. Our analysis showcases the potential of transformers to effectively learn complicated probabilistic models, and contributes to a better understanding of the success of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper theoretically constructs a simple transformer model that learns to sample from a Bayesian Network (BN) from in-context samples. A BN is an ordered set of variables that has a causal ordering among their variables and satisfy various conditional probabilities. The paper shows that for a BN of bounded maximum indegree, a simple 2-layer transformer can approximate the conditional probabilities and generate new samples. The proof is simple and basically constructs positional embeddings that mimic the parent structure of the BN and then applies MLE. Experiments are conducted to validate the theory on simulated BNs and also probe the number of layers needed. The target audience are people interested in theoretical machine learning.

### Strengths
- There has been a lot of growing interest in theoretically studying whether transformers can learn certain structures [1, 2, 3]. The problem this work studies, whether transformers learn bayesian networks, is very interesting and relevant to the ICLR community.

- The general problem of learning a BN is very tricky (even with transformers) and the work simplifies it nicely using a curriculum approach so only a few variables are introduced at each stage. However, while the idea is novel, this does limit the usefulness of this algorithm (see weaknesses below).

#### References:

- [1] Transformers Learn Shortcuts to Automata
- [2] Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers.
- [3] (Un)interpretability of Transformers: a case study with bounded Dyck grammars

### Weaknesses
 - While the result is nice to have, it's unclear whether how the main theorem of this work compares to results from existing works on universal approximation capabilities of transformers. Specifically, the paper does not clearly articulate how the in-context learning setting they consider differs fundamentally from standard function approximation, where transformers are known to be universal approximators. It would be beneficial to explicitly state what aspects of the in-context learning task make the theoretical analysis non-trivial, given existing results.

- Moreover, it's also unclear whether gradient descent or standard approximation methods used to learn such models will extract some sort of similar structure. The authors state this in their conclusion, however this is a relevant weakness of this work and limits its utility. The theoretical result shows that a specific parameterization exists, but it does not guarantee that standard training procedures will converge to such a parameterization. This is a significant gap between theory and practice, and the paper should acknowledge this limitation more explicitly.

- The curriculum setup sounds interesting, however it seems to require apriori knowledge of the causal order and this may not be available in practice. The requirement of knowing the causal order beforehand significantly limits the applicability of the proposed method to real-world scenarios where the causal structure is often unknown or needs to be inferred. This assumption should be discussed in more detail, including its implications for the practical use of the method. Furthermore, in the definition of a BN, the causal order seems to respect the index order. Does the main theorem hold when the ordering is not known, i.e. the variables are permuted uniformly in the samples?

- While experiments on simulated data validate the theory, it would also be nice to have some validation on real-life data (even on few variables). The lack of experiments on real-world datasets makes it difficult to assess the practical relevance of the theoretical findings. While simulated data is useful for verifying the theory, real-world data often presents additional challenges that are not captured in simulations. It would be beneficial to include experiments on a few real-world datasets to demonstrate the applicability of the proposed method.


### Questions
Some questions were raised above. 

- In the definition of a BN, the causal order seems to respect the index order. Does the main theorem hold when the ordering is not known, i.e. the variables are permuted uniformly in the samples?

#### Typos:

- L152: will-known -> well-known
- L198: paramter -> parameter
- L294: missing citation for visualization
- L667: nad -> and

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper considers the ability of Transformers to estimate in-context the conditional probabilities of categorical variables. Theoretically, the paper seeks to prove that for any joint distribution over categorical variables and an ordering over them, there exists a two-layer Transformer that can represent the true conditional probabilities of each variable given those that are earlier in the ordering. Empirically, the paper considers experiments on synthetic data where Transformers are trained on samples from different Bayesian networks that all come from some family of graphs. The paper compares the probabilities estimated in-context to the ground truth as well as those estimated via naive Bayes and Bayesian inference, finding trends that suggest that Transformers have the capacity to estimate conditional probabilities in-context.

### Strengths
This paper investigates whether Transformers are capable of estimating multivariate discrete distributions in-context. In and of itself, this research question has not been studied yet, to the best of my knowledge.

### Weaknesses
 + A key flaw with this paper is a misrepresentation of the problem: this is not a paper about learning Bayesian networks in-context; rather, it is a paper about whether Transformers can estimate conditional probabilities of discrete variables in-context. In lines 106-107, where the problem is introduced, note that the Bayesian network that is specified is not the true Bayesian network (BN) that defines the joint distribution of the variables: it is simply a factorization of the distribution via chain rule given a particular variable ordering. This factorization is generic and valid for any distribution. By contrast, the __true__ BN that underlies a distribution can entail far more conditional independences than is given by the chain rule. Even if this paper was about learning BNs, BNs are anyways not identified by observed data: it is known theory that multiple BNs entail the exact same set of conditional independences.

+ Following up on the previous point, the paper can be interpreted as asking: can Transformers estimate joint distributions of discrete variables in-context? The technical result is in service of showing that true conditional probabilities can be captured by the hypothesis class of two-layer Transformers. But, the significance of this finding lacks context: what is the broader implication if Transformers can estimate multivariate discrete distributions in-context? What questions will this help us answer in the broader context of machine learning? The authors need to properly contextualize the questions and finding in their paper. 

+ The technical setup lacks clarity about details that are essential to a paper about Transformers and in-context learning: what is the precise objective by which the Transformer is trained? Is it a causal decoding Transformer trained to minimize the negative log likelihood of the next categorical variable given the previous ones in a particular sample? Details about how the Transformer is trained are completely missing. Further, for completeness, the authors should also properly define every piece of notation like $0_{dm}$ and $\mathbf{e}_{N+1}$ -- I imagine these define a matrix of 0s and the $N+1$-th standard basis vector, respectively? But readers shouldn't have to interpret key pieces of notation. 

+ There are technical details that do not appear to be correct. For example, in Eqn. 3.2 that defines the input matrix $\mathbf{X}$ to the Transformer, the dimensions do not make sense: each $\mathbf{x}_{ij}$ entry is a $d$-dimensional one-hot encoding, as stated in in line 117, but the vector $p$ is $(M+1)d$-dimensional according to Eqn. 3.1. Thus, the last row of the input $\mathbf{X}$ seems to have more columns than the rows above. Another example is in line 190: to specify the output of the model, the authors indicate $\mathbb{R}^d$ and define operations that would produce a $d$-dimensional real-valued vector, but for categorical variables, we need to output vectors in the $d$-dimensional simplex. The composition of the $\mathrm{Read}(\cdot)$ and $\mathrm{Linear}(\cdot)$ functions would not produce vectors that are probabilities that sum to 1, as needed for evaluating the log likelihood or for sampling discrete variables.

+ The empirical studies also lack clarity about key details. For example, in lines 261 and 262, the phrase "the probability distribution of those graphs ..." is not parseable. What is this referring to? Second, the methods that are compared with a Transformer -- naive Bayes and Bayesian inference -- are significantly lacking in clarity. How is naive Bayes being applied to the density estimation problem considered in this paper? Bayesian inference is not a model, it is a method, so what is the underlying model on which Bayesian inference is applied and what is the posterior being inferred? These details are not clear from the paper and limit the ability of a reader to make sense of the empirical findings.

### Questions
+ Can you please clarify the problem formulation in this paper? I don't think it's accurate to say that this paper is about Bayesian network learning. However, I'd like the authors to reflect on this aspect, and clarify this point.

+ Can you elaborate significantly on how the Transformer is trained, including details about: is it a causal decoding Transformer? Is it trained to minimize the negative log-likelihood of the next variable given previous ones? Include all details that can help a reader clearly understand the training objective.

+ Can you shed light on the dimensions of the input $X$ and in particular, clarify the apparent mismatch in dimensions of the last row against the previous rows?

+ Can you clarify how the output of the final linear layer is transformed to produce a proper vector of probabilities for a categorical distribution?

+ Can you clarify the missing details about the empirical studies that I noted in the "weaknesses" section?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The main goal of this paper is to demonstrate how transformers can learn Bayesian networks in context. The paper provides a theoretical proof showing that transformers are capable of modeling Bayesian networks in context. Additionally, The paper provides an evidence that transformers trained on such tasks can make Bayes-optimal predictions for new samples in an autoregressive manner.

### Strengths
1. The paper proposes a theoretical construction that transformers are capable to capture  Bayesian networks in context.
2. The paper presents a well-defined experimental framework to explore how transformers learn Bayesian networks in context,  which could inspire further research.
3. The paper compares prediction accuracy by varying the variables and types of Bayesian networks, providing a detailed description of qualitative differences among various instances.

### Weaknesses
1. The paper does not provide evidence on whether the trained transformer implements the algorithm proposed in Theorem 4.1 and Section 6. Other previous works on similar topics utilizes attention pattern analysis and causal studies through ablations.
2. The paper lacks explanations of terms like “naive bayes” and “bayesian inference” and does not clarify how the accuracy of these algorithms is calculated in the accuracy plots in Figures 2, 4, and 6.
3. The paper does not address the robustness of the results under more realistic settings, such as with positional embeddings.

### Questions
1. Could you specify “naive bayes” and “bayesian inference” in main text?
2. Could you provide whether the trained transformers implement an algorithm proposed at Theorem 4.1 and Section 6?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the problem of in-context learning in transformers. In particular, it focuses on whether transformers are able to learn Bayesian networks in-context. In this setting, the model, given N different realisations of a specific graph and a query sample, is tasked to predict the probability distribution associated with a missing variable (see construction in Eq. 3.2). The assumption is that, if the model is able to infer the conditional probabilities associated with the Bayesian network, it can then use them to predict the value of the missing variable. In addition, once the model has captured such conditional probabilities, it is in principle able to generate new samples from the inferred graphical model (Algorithm 1). 

The authors first provide a theoretical construction for a two-layer transformer which is capable of estimating the conditional probabilities of the Bayesian network according to the context, and autoregressively generating a new sample according to the Bayesian network with estimated conditional probabilities (Theorem 4.1 and Lemma 6.1 and Lemma 6.2). 

The authors also conduct an empirical analysis to show the performance of trained transformers (with up to 6 layers) on the task of in-context learning three graph structures, namely a "general graph", a "tree" and a "chain". The performance of the model is studied by varying the number of in-context examples seen at training time and evaluating the model on different number of test in-context samples. The results show some evidence that transformers are capable of learning Bayesian networks in-context.

### Strengths
- The paper follows a relevant and fruitful line of work studying in-context-learning (ICL) on controlled settings.

- The paper proposes the interesting benchmark of Bayesian networks to study ICL capabilities of transformers.

- The paper provides a theoretical construction of a simple 2-layer transformers capable of estimating conditional probabilities of Bayesian networks and of generating a new sample autoregressively from the inferred graphical model.

### Weaknesses
 - I find the notation quite confusing and the way the paper is organised makes it a bit hard to follow. For example, looking at Algorithm 3.1, it seems that the input to the model is of size (2M+1)d x (N+1) where the N+1 factor takes the query into account, while it seems the Read Function takes as input a tensor of size (2M+1)d x (N). In addition, I found a bit hard to follow the description of how the training and test datasets are generated (paragraphs Datasets and Metrics in Section 5.1). Could the authors clarify these points?

- As far as I understand, the paper focuses on only three different Bayesian networks with a fixed structure (shown in Figure. 1). If my understanding is correct, I believe more varied and diverse graph structures should be considered to better support the author's thesis. Can the analysis be extended to other graphs? 

- On a related note, why only binary variables are considered? It would be interesting to extend the analysis to variables taking values from a vocabulary of a certain size. 

- In section 5.1 (model paragraph), the dimensions of p and p_q changes compared to Eq. 3.1 where they were defined. Could the authors please clarify?

- From the experiments in section 5.3 a one layer transformer seems to be enough. This result contrasts with the theoretical construction which in principle would require a 2-layer model. Could the authors better elaborate on this point? 

- Several typos across the manuscript. See, for example, missing link in the "Curriculum Design" paragraph ("A visualization of the curriculum is in XXX")

### Questions
See weaknesses part.

### Soundness
1

### Presentation
2

### Contribution
2
