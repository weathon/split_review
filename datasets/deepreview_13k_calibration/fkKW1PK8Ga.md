# Generalization Gradient Descent

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
We propose a new framework for evaluating the relationship between features
and generalization via a theoretical analysis of the out-of-distribution (OOD)
generalization problem, in which we simultaneously use two mathematical methods:
a generalization ratio that quantitatively characterizes the degree of generalization,
and a generalization decision process (GDP) that formalizes the relationship of loss
between seen and unseen domains. By combining the concepts of informativeness
and variation in the generalization ratio, we intuitively associate them with OOD
problems to derive the generalization inequality. We then introduce it to the GDP to
select the best loss from seen domains to gradient descent for backpropagation. In
the case where the classifier is defined by fully connected neural network, the entire
system is trained with backpropagation. There is no need for any model selection
criterion or operating on gradients during training. Experiments demonstrate the
potential of the framework through qualitative and quantitative evaluation of the
generalization ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel framework for analyzing out-of-distribution (OOD) generalization, integrating a generalization ratio to quantify generalization capacity and a generalization decision process (GDP) to link losses across seen and unseen domains. This framework enables backpropagation-based training without model selection, using a combination of informativeness and variation in generalization to derive a generalization inequality, with experiments showcasing its effectiveness in improving generalization ability.

### Strengths
1. They designed an algorithm focused on enhancing the generalization ability of gradient descent, leveraging the concept of a generalization ratio and insights from reinforcement learning.
2. They experimentally demonstrate that the algorithm outperforms traditional gradient descent.

### Weaknesses
1. The title is intriguing. Would it be clearer to use 'Gradient Descent with the Generalization Ratio: Enhancing.......' instead?
2. In my view, GGD is proposed based on reinforcement learning and the generalization ratio. However, the motivation behind the algorithm design could be clarified further.
3. There is considerable overlap with the paper by Ye et al. (2021). It might help to elaborate more on the ideas behind the algorithm's design.
4. The writing could be improved, as there are several grammatical errors throughout.

### Questions
1. You introduced the concept of the generalization ratio (GR) in this paper. Could you clarify the functional difference between V_KL for different e_i sets and GR?
2. As a novel and important criterion, could you elaborate on the properties of GR and why it serves as a strong evaluation metric?
3. Could you design some experiments that demonstrate the advantages of using GR instead of V_KL as Ye et al. (2021) also provided a model selection criterion?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper tackles the out-of-distribution (OOD) generalization problem. The main ideas are to consider the distribution of features invariant to domain shifts and to formulate them as the ideal feature matrix function, generalized model, and non-generalized model.  The paper also introduces the variation, the informativeness, and the generalization decision process (GDP) to propose a new algorithm called the generalization gradient descent (GGD) based on the framework of reinforcement learning. The GGD performs better than the traditional gradient descent in their experiment.

### Strengths
The paper discusses the generalization problem mathematically rigorously. The ideas of generalization ratio and generalization decision process are novel and the introduction of reinforcement learning framework is unique.

### Weaknesses
It is not clear whether the framework is practical or not since the definition of the ideal feature matrix function that the posterior distributions of y are the same seems too strong to exist in real problems. The reviewer recommends showing some examples. The experiment is rather small and specific, that is, it compares only GGD and TGD. The effectiveness of the proposed algorithm should have been confirmed with a larger number of problems. In addition, this work strongly depends on the previous work (Ye+ 2021) and its difference seems not large since many of the concepts were introduced there.

### Questions
None.

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
2

### Summary
The paper proposes a variation of the framework of (Ye et al., Neurips 2021) to analyze out-of-distribution generalization, then propose a training algorithm that uses these concepts to offer cross-domain generalization performance.

Ye et al. (2021) studies how to use a small set of domains Eavail to construct a classifier that works across a larger set of domains Eall that we obviously are not expected to know in advance. They provide bounds that depends on an essentially unknowable "expansion function" that measures how features qualities expand from Eavail to Eall.  This paper instead assumes that all domains are available in a set Eavail that is partitioned into training domains Etrain and validation domains Eval. There is no Eall anymore, and one wonder why one should not train using all the known domains of Eavail (which are all the domains that matter) rather than a subset.  Other differences relative to (Ye et al. 2021) include an attempt to talk about features in all network layers (instead of just the penultimate one).

### Strengths
This is an ambitious paper.

### Weaknesses
This paper instead assumes that all domains are available in a set Eavail that is partitioned into training domains Etrain and validation domains Eval. There is no Eall anymore, and one wonder why one should not train using all the known domains of Eavail (which are all the domains that matter) rather than a subset. The authors do not provide a compelling reason for this partitioning, especially given that the goal is to perform well on Eavail itself. This setup seems to unnecessarily complicate the problem, as standard domain generalization techniques are typically motivated by the need to generalize to unseen domains, which is not the case here.

There is something disturbing in equation (3) [Thm 2.1]. Remember that W(X) is a dxN matrix. An expression of the form P(W(X^{e_i})|...) should be normalized over the values taken by this matrix, not over the i indice representing the domains. Either the notation is inadequate (meaning that the authors mean something else) or the theorem is wrong. The probability should be over the space of possible weight matrices given the class label, not over the different domains.

Through definition 3.8, algorithm GGD depends on all the domain distributions in Eavail and not just the domain distributions in Etra. Since one wishes to be robust in Eavail (unlike Ye et al. (2021), there is no Eall here], why not use Eavail directly. The only justification that comes to my mind would be when Etra is small and Eval is much larger. But evaluating GR_{KL}(W, Eavail) does not seem cheap. The computational cost of evaluating this term across all domains in Eavail is not discussed, and it is unclear how this would scale to a large number of domains. Furthermore, if the goal is to be robust across Eavail, it is unclear why a subset of Eavail should be used for training, since this seems to discard valuable information.

### Questions
Please see the weaknesses section.

### Soundness
2

### Presentation
1

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
This paper introduces a new way of performing gradient descent.  Firstly, this paper defines a certain kind of generalization capability. Then, this paper proposes a method  which selects training sample of each step in a reinforcement learning (RL) manner, thereby improving the gradient descent process.

### Strengths
This paper presents a novel approach to gradient descent. It proposes an innovative method that selects the training samples for each step using a RLstrategy, which enhances the overall gradient descent process. This approach demonstrates a creative combination of RL and optimization techniques, potentially leading to improvements in training efficiency and model performance. The integration of RL for sample selection is a unique aspect that sets this work apart from traditional gradient descent methods, which is quite interesting.

### Weaknesses
Line 149: eature -> feature

Line 176: The definition of $W^*$ is a little confusing. Do you mean $\forall W^* \in \mathcal{W}^*$ or $\exists W^* \in \mathcal{W}^*$?

Line 505: The font in the image is too small to be readable.

In Definition 3.1, this paper introduced the definition of the Ideal feature matrix function. However, I still don’t have an intuitive sense of it, and it feels like it’s missing some explanation here. I think it would be better if the reasoning behind this definition or references to relevant literature could be provided.

Theorem 4.2 provides an upper bound of the generalization error. Is the generalization upper bound tight? Additionally, I noticed that the upper bound of the generalization error is composed of both the generalization ratio (GR) and the training error. The optimization in the RL section is performed with respect to GR. However, as the sample size n increases, which part—GR or training error—will dominate the generalization error? If there are some theoretical results regarding this, I believe the results could be more complete.

In the RL section, the paper uses Q-learning to adjust the training set. The state space is the set of G, and the action space is the selection of training samples. However, I’m a bit confused: for a highly complex model, can its state really be represented by a one-dimensional scalar G (Generalization Ratio)? The theory here seems a bit not solid enough. The representation of the state space in reinforcement learning is crucial; the state variable must capture the essential information of the environment to make informed decisions. Representing the state of a complex model with a single scalar, the generalization ratio, seems overly simplistic and may not adequately reflect the nuances of the model's learning process. This raises concerns about the validity of applying standard reinforcement learning techniques in this context.

### Questions
Theorem 4.2 provides an upper bound of the generalization error. Is the generalization upper bound tight? Additionally, I noticed that the upper bound of the generalization error is composed of both the generalization ratio (GR) and the training error. The optimization in the RL section is performed with respect to GR. However, as the sample size n increases, which part—GR or training error—will dominate the generalization error? If there are some theoretical results regarding this, I believe the results could be more complete.

In the RL section, the paper uses Q-learning to adjust the training set. The state space is the set of G, and the action space is the selection of training samples. However, I’m a bit confused: for a highly complex model, can its state really be represented by a one-dimensional scalar G (Generalization Ratio)? The theory here seems a bit not solid enough.

Overall, I think the idea of this paper is interesting, but I still have these concerns. I would be happy if the authors could address my questions. Thank you.

### Soundness
2

### Presentation
2

### Contribution
2
