# Causal Concept Graph Models: Beyond Causal Opacity in Deep Learning

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6

## Abstract
\emph{Causal opacity} denotes the difficulty in understanding the ``hidden'' \emph{causal structure} underlying the decisions of deep neural network (DNN) models.
    This leads to the inability to rely on and verify state-of-the-art DNN-based systems, especially in high-stakes scenarios.
    For this reason, circumventing causal opacity in DNNs represents a key open challenge at the intersection of deep learning, interpretability, and causality. This work addresses this gap by introducing Causal Concept Graph Models (Causal CGMs), a class of interpretable models whose decision-making process is causally transparent by design. Our experiments show that Causal CGMs can: (i) match the generalisation performance of causally opaque models, (ii) enable human-in-the-loop corrections to mispredicted intermediate reasoning steps, boosting not just downstream accuracy after corrections but also the reliability of the explanations provided for specific instances, and (iii) support the analysis of interventional and counterfactual scenarios, thereby improving the model's causal interpretability and supporting the effective verification of its reliability and fairness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents Causal Concept Graph Models (Causal CGMs), a concept-based architecture whose decision-making process is causally transparent by design. It avoids the unrealistic assumption that concepts must be causally independent and direct causes of the class prediction. The paper aims to design Deep Learning  models where each prediction can be traced back to a chain of
semantically meaningful causes.

### Strengths
-  The paper is well written.
-  The idea of introducing causal transparency in concept-based models is interesting.
-  The experiments are sound.

### Weaknesses
 -  > *Causal opacity refers to the difficulty in understanding the mechanisms behind a model’s decision-making process.* 

  The paper frequently references the concept of causal opacity, but it is too vaguely defined to be fully understood. It's unclear what specific properties of the model's decision-making process contribute to this opacity, and how this differs from a lack of interpretability in general. For example, does causal opacity refer to the inability to trace the influence of individual input features, or is it related to the complexity of the learned relationships between concepts?

- How the model performs abduction to answer counterfactual queries is unclear. The paper mentions inferring the value of exogenous variables, but it does not specify the mechanism for this inference. It is unclear how the model uses the observed input to determine the values of these variables, and how this process relates to the causal graph structure. The paper should clarify whether this inference is deterministic or probabilistic, and how it handles uncertainty.

- Minor: The description of Figure 3 is inconsistent with the picture. 

- It seems the proposed model sacrifices accuracy to improve interpretability. While interpretability is a valuable goal, the paper does not provide a clear justification for the degree of accuracy loss. It is not clear if the trade-off is optimal, or if there are ways to improve the accuracy without sacrificing interpretability. The paper should explore the space of possible trade-offs and provide a more detailed analysis of the performance of the model under different configurations.

### Questions
- > Concept Graph Models duplicate the layer of interpretable variables $V$ by introducing an additional layer of identical copies $V^{′}$ . Using this additional layer, Causal CGMs make predictions of each $v_{i} \in V$ using as possible inputs all $v_{j}' \in V^{′}$ for all $j \neq i$

How do you guarantee the causal graph will be acyclic?

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
3

### Summary
In their work, the authors construct causal concept bottleneck models (CCBMs), which are interpretable models that aim to reveal the underlying decision process of deep learning models. The models are built with the assumptions that all relevant human-aligned concepts are known a priori and that these concepts are direct causes of the class prediction. The authors propose measure the predictive power of concepts towards each other other to figure out variable parents. The authors leverage the assumption, that distribution predictions between features predicted by noise, and features predicted from the prior noise-predicted values are invariant. The recovered structure is then used to extract logic rules and trace-back decision.

The approach is evaluated on smaller image datasets, including CelebA and CIFAR 10, showing performance gains over other non-causal methods.


[Disclaimer: This is an emergency review]

### Strengths
The authors extend prior approaches by dropping the restriction of causally independent concepts and trying to approximate the underlying true graphical causal relation. This is an important extension, as most real-world settings, feature complex interactions between concepts and allows to inspect the consequences of interventions on the modeled process.

By observing predictive power among variables, the authors are able to (partially) recover the individual parents of the variables. If trained correctly, CCGM are therefore deep models, which are interpretable by design and possibly allow for human-in-the-loop adjustments.

The presented results improve over prior CBM and CEM, while lacking only slightly behind 'causally opaque' black-box models. The authors show good predictive performance under interventions, and are able to extract some underlying logic rules from the learned models.

### Weaknesses
The weaknesses concern extend to which the presented method 'is actually causal'. While existing works in the field of causality are mainly concerned with providing identifiability results, the presented method mainly leverages predictive power to identify causal relations between variables, which might not coincide with learning the correct causal structure and lead the model to learn spurious associations.

1) Measuring the predictive performance of features towards each other does guarantee to recovery the underlying causal structure. Generally, additional assumptions such as interventions or sufficient variability need to be assumed. In that regard, theorem 3.2 does not state any of these assumptions and is provided without proof.

2) In that regard the paper lacks a comparison and detailed discussion to existing methods in the field of causal representation learning [1], such as differences to other existing deep causal approaches ([2-4]), and -with regard to the prior point- guarantees on the identifiability of (latent) concepts [5-7].
3) Variables $v'_i$ are predicted just from their exogenous noise variables $u_i$. Assuming that, variables are indeed embedded into a causal structure, and assuming that at least for some $v_i$ the parent set is non-empty, it can not be that $p(v'_i\mid pa_{V'}(v_i),u_i) = p(v_i \mid u_i)$.
4) The experimental section compares to only non-causal methods (CEM and CBM) on their predictive performance (accuracy). Given the above discussion, it is unclear whether the models have actually learned the correspond process. No analysis or discussion towards identifiability and possible avoidance of confounding is presented. As a result a rather strong drop-off in performance between CCGM+CD (recovering the graph from ground-truth labels) and CCGM is observed. In particular, when the causal graph is recovered from data, the presented causal CGM+CD approach might by very similar to Neural Causal Models (NCM) [4].

**Minor**

* Table 1 is hard to read. I suggest breaking "semantic transparency" and "causal transparency" into two lines to make the texts bigger.

### Questions
My questions mainly concern the weaknesses mentioned above. I would kindly like to ask the authors the following questions:

1) How does method guarantee identifiability and non-confoundedness of concept predictions. Could the authors elaborate on the implications of theorem 3.2 towards this question and/or highlight possible limitations that might arise?
2) Regarding point 3: Could the further explain how distributions of Theorem 3.2 can be equal, given, that $v'_j$ are inferred from exogenous variables only?
3) How, does the presented approach compare to other causal deep-learning methods? Could the authors present further insights or explain, why other methods might not be comparable?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a new class of interpretable models whose decision-making process is causally transparent by design. The method represents relations between high-level concepts, associated with each data point, as a DAG allowing for interventional and counterfactual analysis of predictions and human improvements during the inference process.

The authors demonstrate that their approach matches the generalization performance of SoTA models. Additional experimental results showcase how explicit causal representation can be efficiently used to increase interpretability and improve performance with human interventions.

### Strengths
1. The paper is cleanly written. 
2. The approach is well-placed in the literature. 
3. The experimental section is extensive.
4. The method description is detailed and well-structured.

### Weaknesses
1. One bit of experimental evaluation is unclear to me (see Questions)

2. Table 3 has two columns titled “CELEBA”

### Questions
1. I do not understand the experiment described in the last paragraph of the experimental section (lines 463-476).  Could the authors please provide an example? How are variables i and j selected for each dataset? Are the results in Table 3. averaged over all possible pairs? How do the authors decide which variables to intervene on (i.e. what structure is used as Ground Truth)? Why is 0 a desirable outcome?  - the authors write that the aim of this procedure is debiasing, to my understanding 0 RCCE means no change.
2. Table 3 has two columns titled “CELEBA”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Over the past few years, there has been a lot of interest in designing models that are interpretable by construction. Concept Bottleneck Models are one such approach; they first predict an intermediate set of human-specified concepts and then use the concepts to predict the target. These intermediate concepts allow humans to understand the dynamics of model predictions through interventions. One key drawback of such an approach is that they assume each concept independently influences the predictions, while in practice, there is always a complex relationship between the concepts and how they influence the target variable. The paper addresses the above issue by introducing the Causal Graph Concept Graph Model, which is transparent by design and captures the complex dynamics of a model's decision processes.

### Strengths
A serious shortcoming of CBMs is that they assume that each human-specified concept independently influences the model's predictions. The authors address this issue by proposing a Causal Graph Concept model that captures the intricacies of the dependencies between the concepts & the target variable and among them.

As the proposed model is causally transparent by design, it allows a human to understand the inner workings of the model by enabling them to ask questions, such as:
- What is the relationship between feature x & label y?
- What happens to the prediction if I set feature x to k?
- What if feature x was k' instead of k?
The proposed model's performance matches or is within the ballpark of the opaque state-of-the-art models on the chosen set of benchmarks.

Theoretically, it also allows humans to intervene and correct erroneous intermediate reasoning steps.

### Weaknesses
 - The paper isn't written well, and some sections are hard to follow.
- One of the key weaknesses lies in the experiments.
     - Why only choose simpler benchmarks, like CelebA & CIFAR10, and benchmarks with semantically richer tasks like AwA2, CUB, etc.?
     - Understanding what the authors mean by joint training is a bit hard.
          - Are the concept encoders also trained along with the process of learning CGMs? 
          - What formulation of CBMs do the authors build on? (independent bottleneck, joint bottleneck, or sequential bottleneck?)
          - What is the architecture of the bottleneck layer? Does it influence the quality of CGMs learnt?
     - One contribution is that CGMs allow human-in-the-loop corrections of erroneous intermediate reasoning steps. I don't see any experiments to support this. Did you evaluate whether the learnt causal graphs are sound and valuable? Did you do a user study to assess their utility to users? 
     - Do you have any intuition about why there is a drop in Figures 4 and 5 for a certain number of intervened concepts?
     - Column 4 is Table 3 is CIFAR10?
     - Line 345 says CIFAR10 is an animal classification dataset. Did you use the entire dataset or a subset for evaluation?
- Another issue with CBMs is that they assume that human-specified concepts are readily available, which rarely happens in practice. Much work has been done in the literature to relax this assumption. I wonder why the authors build on the vanilla version of CBMs.

### Questions
Refer to Weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors introduce a generalization of *Concept Bottleneck Models* (CBM), called *Causal Concept Graph Models* (causal CGM). In contrast to existing CBMs, causal CGM allows for modeling causal relationships between latent variables. In contrast to causal representation learning, causal CGM aims at addressing causal opacity (interpretability) of deep learning models, rather than identifying specific variables and/or mechanisms. The claimed properties of Causal CGM are experimentally assessed on various data sets and compared with a black-box deep learning baseline, a non-causal CBM baseline and Concept Embedding Models.

### Strengths
1. The authors present an interesting perspective on causal representation learning, where the learned abstract variables and mechanisms are used to obtain insights into a trained model (interpretability) rather than aiming at generalizing to unseen domains. The latter is the main motivation of the related work that I am familiar with (e.g., [1, 2, 3]).

2. The manuscript is particularly well-written and the plots are great, too. The authors did an excellent job at presenting their work well.

3. There are plenty of experiments that (somewhat surprisingly) show that causal CGMs perform similarly to black box models that do not enforce a causal bottleneck.

[1] von Kügelgen, Julius, et al. "Nonparametric identifiability of causal representations from unknown interventions." Advances in Neural Information Processing Systems 36 (2024).

[2] Lippe, Phillip, et al. "Biscuit: Causal representation learning from binary interactions." Uncertainty in Artificial Intelligence. PMLR, 2023.

[3] Mengyue Yang, Furui Liu, Zhitang Chen, Xinwei Shen, Jianye Hao, and Jun Wang. Causalvae: Structured causal disentanglement in variational autoencoder. arXiv preprint arXiv:2004.08697, 2020.

### Weaknesses
1. In terms of the architecture and training of the proposed method, I am concerned about novelty. The method may seem novel within the CBM literature, where only independent latent variables have been considered so far. However, the proposed method seems to be (almost) identical to [1], which is branded as *causal variational autoencoder* rather than *concept bottleneck model*. Apart from the name and problem motivation, I cannot identify any differences. It would be great if the authors could highlight the differences, if they exist (I did not see them). Specifically, the use of high-dimensional embeddings for the latent variables, while a difference from the original Causal VAE, is not novel in the broader causal representation learning literature, where such representations have been explored in various contexts. For example, methods that learn causal representations from temporal data often utilize high-dimensional latent spaces to capture complex dynamics [1].

2. While the authors start with an interesting perspective on learning latent causal variables (see strength 1), it is unfortunate that this idea is not taken very far. Specifically, I would be interested in questions such as how such a causal graph could be efficiently inferred from any black-box model post training (just an example of the kind of questions that came up to me). Instead, causal CGM seems to be an existing causal representation learning method (see weakness 1), but without identifiability guarantee. I would advise the authors to develop the paper more closely along this original idea (strength 1), as I believe there is a lot of unused potential.

3. The *human-in-the-loop corrections* aspect seems contradictory to the motivation of the work: Causal CGM is introduced from the point of interpretability rather than identifiability of variables and mechanisms. Human-in-the-loop corrections indicate that specific variables (known the human) ought to be identified, which lies at odds with the causal opacity motivation. Therefore, I would suggest moving this aspect entirely to the appendix.

### Questions
line 88: (Minor comment) The authors write the causal CGM is related to XAI. Maybe it is more about interpretability than it is about explainability? To me, XAI methods aim at explaining black-box models. However, causal CGM is rather about constructing the model such that it is interpretable by construction.

line 91: As already explained in weakness 1, I am not convinced that causal CGM is a new architecture. 

line 105: I would challenge that structural causal models are *the* standard framework for causal modeling. Rubin causal models are also quite common. I would suggest rephrasing this. For example: *"Structural causal models are a widely used framework for causal modeling, alongside other approaches like Rubin causal models."*

line 111: *"which determine the values of each endogenous variable $v_i \in V$ by computing the conditional probability ..."* This sentence sounds contradictory to me. According to the SCM definition that I am familiar with, all endogenous variables can be expressed as a deterministic function of all exogenous variables (reduced form expression). Thus, this conditional probability should be just a Dirac measure? I would appreciate if the authors could clarify this.

line 115: I believe this should read *hard interventions*. There also exist other types of interventions where variables are not fixed to a value.

line 121: I am not too familiar with the literature on *concept-based models* (CBM). However, I do not understand how the term *concept* differs from *high-level feature* and how *concept-based modeling* is distinct from *representation learning* (see weakness 2).

line 199: (Minor comment) Doesn't theorem 3.2 follow from d-separation? I could imagine that the proof could be greatly simplified with such a graphical argument.

line 245: How does the training differ from the method proposed by [1] (see weakness 1)? It would be great if the authors could highlight this in detail.

line 257: *maximise the log-likelihood of v, v′* How can the likelihood of unobserved variables be maximized? I suppose you maximize a variational lower bound of $\text{log} \\; p(x)$?

line 481: *Causal CGMs focus on high-level human interpretable concepts* As mentioned in weakness 3, this seems to be at odds with the original motivation of the work.

### Soundness
4

### Presentation
3

### Contribution
1
