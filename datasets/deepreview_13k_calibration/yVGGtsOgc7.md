# Disentangling Representations through Multi-task Learning

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 6, 3, 6, 8

## Abstract
Intelligent perception and interaction with the world hinges on internal representations that capture its underlying structure (``disentangled'' or ``abstract'' representations). Disentangled representations serve as world models, isolating latent factors of variation in the world along approximately orthogonal directions, thus facilitating feature-based generalization. We provide experimental and theoretical results guaranteeing the emergence of disentangled representations in agents that optimally solve multi-task evidence aggregation classification tasks, canonical in the cognitive neuroscience literature. The key conceptual finding is that, by producing accurate multi-task classification estimates, a system implicitly represents a set of coordinates specifying a disentangled representation of the underlying latent state of the data it receives. The theory provides conditions for the emergence of these representations in terms of noise, number of tasks, and evidence aggregation time. Surprisingly, the theory also produces closed-form expressions for extracting the disentangled representation from the model's latent state $\mathbf Z(t)$. We experimentally validate these predictions in RNNs trained on multi-task classification, which learn disentangled representations in the form of continuous attractors, leading to zero-shot out-of-distribution (OOD) generalization in predicting latent factors. We demonstrate the robustness of our framework across autoregressive architectures, decision boundary geometries and in tasks requiring classification confidence estimation. We find that transformers are particularly suited for disentangling representations, which might explain their unique world understanding abilities. Overall, our framework puts forth parallel processing as a general principle for the formation of cognitive maps that capture the structure of the world in both biological and artificial systems, and helps explain why ANNs often arrive at human-interpretable concepts, and how they both may acquire exceptional zero-shot generalization capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the important question of how abstract (linear and approximately orthogonal) and disentangled (orthogonal without the necessity of linearity) representations can emerge in biological and artificial agents. 
The authors present both theoretical and experimental results demonstrating that multi-task learning, specifically within the framework of evidence aggregation classification tasks, can lead to the development of such representations.

### Strengths
The paper presents theoretical results that establish specific conditions—relating to the number of tasks, input dimensionality, input noise, and more—that lead to the emergence of abstract and disentangled representations in agents solving multi-task evidence aggregation classification tasks. The authors conduct thorough experiments across several architectures (RNNs, LSTMs, and transformers) to validate their theoretical results, showing that even architectures like GPT-2 can exhibit these properties. The work bridges AI and neuroscience, with potential explanations for how abstract, human-aligned representations might arise in artificial neural networks, making it valuable for both fields.

### Weaknesses
One notable limitation of this work is the assumption of factorization, as acknowledged by the authors. Additionally, the theoretical framework is tailored to a specific type of multi-task learning problem—evidence aggregation classification with linear decision boundaries—which may not capture the full diversity of tasks and decision boundaries that agents encounter in dynamic environments. It would be valuable to explore how these ideas generalize to other multi-task learning scenarios. Furthermore, the experiments focus on synthetic data with simple latent structures. While these experiments effectively support the theoretical results, testing the framework on slightly more complex data could provide further insights. The use of linear decision boundaries in the latent space, while simplifying analysis, might not fully reflect the complexities of real-world tasks where non-linear decision boundaries are common. The study also does not explore the impact of the encoder's architecture on the emergence of abstract representations, which could be a significant factor. Finally, the experiments do not thoroughly investigate the sensitivity of the results to changes in network architecture or hyperparameters, which could affect the robustness of the findings.

### Questions
- In Equation 6, could you clarify if $x_{in}$ is the encoded input, i.e., $f(x)$?

- Does the dimensionality of the latent state Z influence the results? Also, does the dimensionality of the encoded input play a significant role? Have these aspects been examined?

- Have you conducted experiments with other encoding functions, such as a quadratic mapping? 

- In Figure 5b, the blue curve for GPT appears to increase at the end. Could you clarify the reason behind this behavior?

- Since the noise at each time step is independent, temporal information isn’t modeled in this setup. How might the results differ if a transformer with self-attention layers was used? Would such a setup still yield disentangled representations?

- On the other hand, if the inputs contained some temporal structure, how might this affect the nature of the representations?

- Have you tested the framework with much larger values of $N_{task}$ and $D$ (e.g., over 100)?

### Soundness
3

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
The paper presents theoretical and empirical results showing that, in multi-task evidence aggregation classification tasks, representations become disentangled as the number of tasks N_task greatly exceeds the input dimensionality 𝐷 when the agent solves the tasks optimally.

### Strengths
1. Originality: the study of the emergence of disentangled representation in temporal tasks and models is relatively new. 
2. Quality: the empirical validation is comprehensive. 
3. Clarity: the theory is well explained. The background section is also very nicely written and thorough. 
4. Significance: The paper addresses the key problem of learning the world model in representation learning and also discusses in detail the biological relevance. The results offer meaningful insights for future research on disentangled representation in both artificial systems and the brain.

### Weaknesses
1. The theory assumes that agents are optimal multi-task classifiers, which may not be achievable in realistic settings where the input dimension D is already large and the number of tasks N_task >>D. This raises questions about the practical relevance of the regime considered in the paper. Additionally, it’s difficult to imagine a large number of orthogonal tasks in real-world settings. For instance, in the dSprite dataset, as the authors noted, how could a meaningful, larger set of tasks be constructed, and what implications would this have for the applicability of the framework? Specifically, the assumption of optimality is particularly concerning because it is unclear how an agent could achieve such performance with a large number of tasks, especially when the number of tasks greatly exceeds the dimensionality of the latent space. The paper does not address the computational complexity of learning these optimal classifiers, nor does it discuss the potential for overfitting when the number of tasks is very large relative to the available training data per task. Furthermore, the notion of 'orthogonal tasks' is not well-defined in the context of real-world data. While the authors provide an example of how to construct tasks for dSprites, it remains unclear how to systematically generate a large number of such tasks that are both meaningful and orthogonal in more complex datasets.
2. The connection to neuroscience also appears somewhat speculative. The authors could clarify how their findings might directly relate to brain function. For example, can the theory predict the relationship between the disentanglement of neural representations and the level of noise or variability in different brain regions? The paper's claims about the brain's parallel processing capabilities and the emergence of disentangled representations are not supported by direct empirical evidence. The link between the mathematical framework and actual neural mechanisms remains unclear. The paper does not specify how the proposed multi-task learning framework could be mapped onto the known architecture and function of cortical columns or other brain regions. The discussion of noise is also vague, as the paper does not distinguish between different types of noise (e.g., sensory noise, neural noise) and how they might affect the disentanglement process.
3. While explaining zero-shot generalization capabilities in artificial neural networks (ANNs) is a central claim, this remains a substantial challenge for most networks. The theory should address whether prior models fail in zero-shot generalization due to insufficient N_task and how practitioners could estimate an adequate N_task, especially in settings where underlying latent factors are unknown, making it impractical to sample random classification tasks as in the paper. The paper does not provide a clear methodology for determining the required number of tasks in real-world scenarios where the latent factors are not known a priori. It is unclear how to apply the theory when the tasks are not randomly sampled, and the paper does not discuss the potential for negative transfer between tasks if they are not carefully chosen. Furthermore, the paper does not address the issue of catastrophic forgetting, which is a common problem in multi-task learning, particularly when the tasks are not related.

### Questions
1. Most examples and empirical validations focus on low-dimensional cases (e.g., D=2). Could you provide examples using moderately higher-dimensional datasets, such as CIFAR or dSprites, to illustrate how N_task scales with D in these settings? 
2. For a given D, what is the maximum number of tasks N_task can be learned with low error? Additionally, how do the test and generalization errors scale with N_task if we keep the number of training data in at a realistic scale?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper extends the work of [Johnston and Fusi (2023)](https://www.nature.com/articles/s41467-023-36583-0)  by investigating how multiple supervised binary classification tasks can lead to abstract or disentangled representations in recurrent neural networks that accumulate evidence from noisy inputs. The authors present theoretical and experimental evidence suggesting that optimal multi-task classifiers can learn abstract representations of underlying ground truth factors.

### Strengths
The paper introduces a theoretical framework connecting optimal multi-task classification to disentangled representations, building upon the empirical observations in [Johnston and Fusi (2023)](https://www.nature.com/articles/s41467-023-36583-0) . To support these theoretical claims, the paper provides a range of experiments exploring different architectures, task structures, and decision boundary geometries.

### Weaknesses
A significant weakness of this paper is its heavy reliance on dense supervised signals to achieve abstract representations. Similar to [Johnston and Fusi (2023)](https://www.nature.com/articles/s41467-023-36583-0), this work utilizes multiple binary classification tasks, framed as "multi-task" learning. This framing implies a diversity of tasks that is not truly reflected in this setup. The dependence on numerous, highly similar, supervised tasks raises questions about the biological plausibility and real-world applicability of the proposed mechanism.

The requirement of a large number of tasks (N_task >> D) to achieve disentanglement adds to concerns regarding the model's biological plausibility and practical relevance. Biological and artificial agents operating in real-world environments rarely encounter such an abundance of supervised signals.

The authors assert (lines 486-493) that their Theorem 3.1 implies "the key factor driving convergence [to a Platonic representation of reality] is the diversity and comprehensiveness of the tasks being learned." This claim is not supported by the results presented. The tasks in this paper are essentially multiple variations of the same supervised classification task, a far cry from the genuinely diverse tasks (e.g., multimodal vision and language tasks) considered in the Platonic representation paper ([Huh et al., 2024](https://arxiv.org/abs/2405.07987)).

It is well-established that achieving disentangled representations in real-world, unsupervised settings is incredibly difficult, if not impossible, without incorporating appropriate inductive biases ([Locatello et al., 2019](https://arxiv.org/abs/1811.12359); which the authors cite). A substantial body of research, spanning decades, has demonstrated that source signals become non-identifiable when mixed non-linearly ([Hyvarinen and Pajunen, 1999](https://www.sciencedirect.com/science/article/pii/S0893608098001403)). Considering this extensive history of work in machine learning dedicated to tackling this complex problem, this paper's approach—attaining abstract or disentangled representations by providing the model with an abundance of supervised signals in the form of binary classification tasks—appears contrived and ultimately of limited practical value. The reliance on such a heavily supervised setting makes it difficult to see how these findings could generalize to more realistic scenarios where supervision is scarce and the underlying structure of the data must be inferred, rather than provided.

Overall, this paper makes incremental progress on the work of [Johnston and Fusi (2023)](https://www.nature.com/articles/s41467-023-36583-0)  but fails to address the fundamental concern of over-reliance on dense supervised signals. As suggested by [Johnston and Fusi (2023)](https://www.nature.com/articles/s41467-023-36583-0), exploring unsupervised mechanisms such as "predicting the sensory consequences of our actions," might offer a more promising path forward.

Instead of relying on a multitude of supervised signals to enforce disentanglement, future work in this area should investigate whether disentanglement can emerge from a smaller number of more diverse tasks, where the need for efficient generalization across tasks drives abstraction. This shift in focus would significantly enhance the biological plausibility, practical relevance, and overall impact of this line of research to understanding disentangled representation learning.

### Questions
**Sparsity:**

The emergence of sparsity in Fig. 4 is interesting. Could the authors specify if they applied any particular architectural constraints, such as regularization techniques or sparsity-promoting mechanisms, to encourage this behavior?

Additionally, quantifying the sparsity (e.g., lifetime sparsity, [Vinje and Gallant, 2000](https://www.science.org/doi/10.1126/science.287.5456.1273)) and examining how this metric varies with N_task, the number of latent dimensions, and specific RNN architecture choices would provide further insights into the effects of task density on network representation.

**More nonlinear encoding:**

The authors' use of a piecewise linear MLP+ReLU encoding of ground truth signals raises questions about the robustness of their empirical results under more complex nonlinear encodings.

Could the authors explore how the N_task vs. out-of-distribution r2 relationship (Fig. 3) might change if the encoding network incorporated more nonlinear functions such as exponential or power-law activations, to simulate more biologically plausible ([Priebe et al., 2004](https://www.nature.com/articles/nn1310)) nonlinear encoding? This line of inquiry is particularly relevant given that the choice of activation function significantly influences the geometry of representations ([Alleman et al., 2024](https://openreview.net/forum?id=k9t8dQ30kU)).

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of learning disentangled representations using a multi-task evidence aggregation approach. In contrast to previous works which have studied a similar problem of abstract and disentangled representations using contextual information, the authors here adopt an approach which simultaneously collects multiple streams of evidence to enable linear classification in multiple tasks at each step. They prove the emergence of an abstract representation of ground truth data given an optimal multi-task classifier, which is shown to be learnable using RNN, LSTM, and GPT-2 based transformer architectures.

### Strengths
The key contribution is an extension of the Johnston and Fusi (2023) feedforward framework to recurrent networks. They show that abstract variables are indeed represented in the latent states of RNNs, LSTMs and GPT-2 style transformer architectures when these models are trained using the multi-task paradigm. The results are interesting and point to a marked advantage in adopting the multi-task paradigm for understanding canonical neuroscience experiments in an AI framework. The discussion of these results in the context of contemporary neuroscience literature is also well framed and places this paper in a good position to appeal to both the broader neuroscience and task-learning communities.

### Weaknesses
While the experimental results are solid contributions, the theoretical contributions are less appealing. The key theoretical results follow from fairly straightforward arguments, but appear a bit overstated. This can potentially be remedied with some re-wording and clarifying statements.  

In my opinion, the following two sentences in the abstract are overstated for reasons that I expand further below:  "The key conceptual finding is that, by producing accurate multi-task classification estimates, a system implicitly represents a set of coordinates specifying a disentangled representation of the underlying latent state of the data it receives.....Overall, our framework puts forth parallel processing as a general principle for the formation of cognitive maps that capture the structure of the world in both biological and artificial systems, and helps explain why ANNs often arrive at human-interpretable concepts, and how they both may acquire exceptional zero-shot generalization capabilities". 

The conditions under which the authors prove the theoretical result are rather strong. Specifically, the authors require 1) that the network is an *optimal* classifier in the sense that the network correctly computes the N_task logits associated with each of the N_task tasks, 2) that decision boundaries in the world are linear in the space of abstract variables, and 3) a highly simplified evidence accumulation problem. 

It follows from 1) and 2) that the output of an optimal network encodes the distance to the N_task decision boundaries. The optimal network will thus represent a linearly transformed version of the input if N_task is larger than the dimensionality of the input (provided the decision boundaries are not degenerate). The mathematical proofs presented in this paper formalize this argument. I believe it will help clarify the results if the authors provide this intuition upfront. The proofs have various conceptual issues, for example, in the use of the data processing inequality in Theorem B.5 and the mix-up of random variables and their estimators (lines 1442-1445). 

The authors state that their framework offers a "general principle for the formation of cognitive maps". I believe it will be helpful if the authors can clarify what this general principle is -- is it the proposal that decision boundaries in the world are linear in the space of the abstract variables or that biological networks are solving multiple tasks at the same time? How is the current work related to the formation of cognitive maps and zero-shot generalization?

Comments:

Line 231: “...in the column space of (C^TC)^{-1}C^T potential with some element-wise non-linearity.” This statement seems too strong given that the restriction on the activation function g has been significantly relaxed. Are there any preliminary results to qualify this statement?

Corollary B9: While I agree with the results of this corollary, it would be good to explicitly connect the uniformity of the singular values to the corollary statement using the Marchenko-Pastur law. Also in this corollary, at line 1613, it is stated that the probability of being orthogonal vanishes as the dimensionality N_task increases. Was this supposed to be “non-orthogonal” instead?

Figure 2: This figure is particularly unclear, and it is perhaps one of the important foci in explaining all the experiments to follow. Upon first viewing with the caption, it is not clear what the arrows (two grey and one red) in Fig. 2a are supposed to imply.

Line 294: “…in the RNN’s hidden layer, when tasks span the latent space.” Does this really imply anything about the tasks formally spanning the latent space?

Figure 4a: I agree that the RNN representations are sparse, and this looks like a good spot to test if there is any lower threshold on the size of the hidden units before the latent encoding fails.

Line 450: “…which might explain their superior generalization performance to RNNs for lower N_task.” It is not really clear from Fig. S10 that the RNNs are indeed worse at orthogonalization than the GPT.

Line 1119/1120: “Figure S3b shows that the network still learns a disentangled, two dimensional continuous attractor.” Not convinced that this actually shows disentanglement since the metric for that qualification from before was the orthogonalization of different tasks. Did you mean to say abstract here? Also, small typo in the spelling of “disentangled”.

Minor comments:

Line 1321: \hat{Y}_i(t) is noted as a Bernoulli random variable. This implies the support of the estimator is {0,1}, but it should really be [0,1].

Line 1408: Similar comment here to Line 1321 on the use of Bernoulli variable for \hat{Y}(t).

Line 1426: In Equation 16, boldfaced t should be scalar.

Line 1592: “Proof: Recall equation (3)…” should be equation (4).

Line 1608: “B^TB is a symmetric for any matrix B.” Some LaTeX formatting errors here and possibly missing the word matrix following “symmetric”.

Line 309: “disentaglement” misspelled

Fig. 3d Caption: May be good to include a short statement about the inset on PCA components accounting for variance.

Line 1070: “Once the factors are perfectly, performance…” missing the word correlated after “perfectly”

Line 1162: “…for all lines in Figure S4a.” Did you mean all lines from Fig. 2a, shown in Fig. S4a?

### Questions
Comments:

Line 231: “…in the column space of (C^TC)^{-1}C^T potential with some element-wise non-linearity.” This statement seems too strong given that the restriction on the activation function g has been significantly relaxed. Are there any preliminary results to qualify this statement?

Corollary B9: While I agree with the results of this corollary, it would be good to explicitly connect the uniformity of the singular values to the corollary statement using the Marchenko-Pastur law. Also in this corollary, at line 1613, it is stated that the probability of being orthogonal vanishes as the dimensionality N_task increases. Was this supposed to be “non-orthogonal” instead?

Figure 2: This figure is particularly unclear, and it is perhaps one of the important foci in explaining all the experiments to follow. Upon first viewing with the caption, it is not clear what the arrows (two grey and one red) in Fig. 2a are supposed to imply.

Line 294: “…in the RNN’s hidden layer, when tasks span the latent space.” Does this really imply anything about the tasks formally spanning the latent space?

Figure 4a: I agree that the RNN representations are sparse, and this looks like a good spot to test if there is any lower threshold on the size of the hidden units before the latent encoding fails.

Line 450: “…which might explain their superior generalization performance to RNNs for lower N_task.” It is not really clear from Fig. S10 that the RNNs are indeed worse at orthogonalization than the GPT.

Line 1119/1120: “Figure S3b shows that the network still learns a disentangled, two dimensional continuous attractor.” Not convinced that this actually shows disentanglement since the metric for that qualification from before was the orthogonalization of different tasks. Did you mean to say abstract here? Also, small typo in the spelling of “disentangled”.

Minor comments:

Line 1321: \hat{Y}_i(t) is noted as a Bernoulli random variable. This implies the support of the estimator is {0,1}, but it should really be [0,1].

Line 1408: Similar comment here to Line 1321 on the use of Bernoulli variable for \hat{Y}(t).

Line 1426: In Equation 16, boldfaced t should be scalar.

Line 1592: “Proof: Recall equation (3)…” should be equation (4).

Line 1608: “B^TB is a symmetric for any matrix B.” Some LaTeX formatting errors here and possibly missing the word matrix following “symmetric”.

Line 309: “disentaglement” misspelled

Fig. 3d Caption: May be good to include a short statement about the inset on PCA components accounting for variance.

Line 1070: “Once the factors are perfectly, performance…” missing the word correlated after “perfectly”

Line 1162: “…for all lines in Figure S4a.” Did you mean all lines from Fig. 2a, shown in Fig. S4a?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper demonstrates the emergence of disentangled representations in recurrent neural networks and transformer architectures in classification tasks based on evidence aggregation or accumulation over time. The conditions under which disentangled (latent) representations emerge are studied in relation to the number of classification criteria, relative to the dimensionality of the input. The paper motivates its focus with reference to the neuroscience literature on evidence accumulation and offers a number of theorems predicated on mutual information and the functional forms of nonlinearities in various mappings, implicit in the network architectures that could be adopted.

### Strengths
The strengths of this paper rest upon a detailed treatment of the functional forms of mappings — implicit in neural network architectures — and how they can be unpacked in relation to maximising the mutual information between inputs and (classification) outputs. Another nice feature of this paper is its reference to neuroscience; in the sense of potential implications for neuronal processing in the brain.

### Weaknesses
The specific contributions of the analysis are not foregrounded sufficiently. For example, one could read the setup considered by the authors as characterising a mapping between inputs x and classification estimates (Y^) using a bottleneck architecture (i.e., mapping through a low dimensional latent space or manifold). If any such mapping were optimised with respect to cross entropy or mutual information, would the latent representations not be disentangled? In other words, is it a linear (orthogonal) disentanglement that qualifies as interesting disentanglement? And, if so, does this inherit from the assumptions and functional form of the mappings in question?

The second weakness is the rather colloquial appeal to the neuroscience literature. For example, evidence aggregation or accumulation would not be considered canonical in the cognitive neurosciences. Canonical paradigms will be things like oddball paradigms, psychophysical paradigms, working memory paradigms, attentional paradigms, and so on. Furthermore, most of neuroscience nowadays cast disentanglement in terms of predictive processing under hierarchical or deep generative world models (i.e., disentanglement is a way of describing the inversion of a generative model of how independent causes become entangled). This inversion is usually articulated in terms of predictive coding or belief propagation. Given that the authors mention Bayesian filtering — and predictive coding can be read as extended Kalman (Bayesian) filtering — there might have been a missed opportunity to join the dots between the authors work and current formulations of perceptual synthesis and evidence accumulation in the brain. 

Related to this, there is a long history of sparse coding models in neuroscience that speak to the current questions; for example, sparse coding models, variants of independent component analysis, liquid computation, echo state machines, and so on (Gros, 2009; Hu et al., 2020; Maass et al., 2002; Olshausen and Field, 1996; Simoncelli and Olshausen, 2001; Suh et al., 2016). More recently, people have been looking at latent representations at various hierarchical levels to address compositionality and disentanglement; especially in relation to spatiotemporal receptive fields that can be assessed empirically in the brain e.g., (Ficco et al., 2021; George et al., 2021; Rao et al., 2023).

### Questions
For the neuroscience reader, it would be good to clarify what multi-task means in this setting. Does it mean that there are many different classification criteria or decision boundaries that have to be met? In other words, is the multi-task aspect a way of saying that the number of classification criteria have to exceed the dimensionality of the underlying (ground truth) evidence? Perhaps it would be useful to have a simple example that people can imagine applying to a perceptual classification task in a psychophysics laboratory?

By evidence aggregation, did you mean evidence accumulation in the spirit of drift diffusion and race to bound models?

Is there any relationship between the functional form of your formulation and schemes based upon the principle of maximum mutual information (a.k.a. infomax principle) (Linsker, 1990). Canonical schemes here would include canonical variates analysis and non-linear versions, such as independent component analysis that take us into the realm of sparse coding models. One interesting aspect of independent component analysis is the identification of latent variables that have a non-Gaussian structure under the assumption that the random fluctuations are Gaussian. Is this related to your interesting observation that noise is required for the kind of disentanglement you are considering?

Can you formulate your evidence accumulation scheme as a Bayesian (e.g., extended Kalman Bucy) filter? If so, can you relate this to predictive coding in the brain (Rao, 1999)?

On a related note, can you formulate your description in terms of inverting a generative model? In other words, can you turn your scheme on its head and generate ground truth evidence from the ground truth classifications; i.e. causes. If so, is this one perspective on the requisite invertibility of f?

### Soundness
3

### Presentation
3

### Contribution
3
