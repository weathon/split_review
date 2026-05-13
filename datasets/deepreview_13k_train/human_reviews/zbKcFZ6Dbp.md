# Shadow Cones: A Generalized Framework for Partial Order Embeddings

- Decision: Accept
- Scores: 6, 6, 6, 6, 8, 6

## Abstract
Hyperbolic space has proven to be well-suited for capturing hierarchical relations in data, such as trees and directed acyclic graphs. Prior work introduced the concept of entailment cones, which uses partial orders defined by nested cones in the Poincar\'e ball to model hierarchies.
Here, we introduce the ``shadow cones" framework, a physics-inspired entailment cone construction. Specifically, we model partial orders as subset relations between shadows formed by a light source and opaque objects in hyperbolic space. The shadow cones framework generalizes entailment cones to a broad class of formulations and hyperbolic space models beyond the Poincar\'e ball. This results in clear advantages over existing constructions: for example, shadow cones possess better optimization properties over constructions limited to the Poincar\'e ball. Our experiments on datasets of various sizes and hierarchical structures show that shadow cones consistently and significantly outperform existing entailment cone constructions. These results indicate that shadow cones are an effective way to model partial orders in hyperbolic space, offering physically intuitive and novel insights about the nature of such structures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce the "shadow cones" framework for constructing entailment cones in hyperbolic space. Unlike prior work that utilized nested cones in the Poincaré ball, shadow cones model partial orders based on subset relations between shadows created by a light source and opaque objects.  This framework extends beyond the Poincaré ball, allowing for more diverse formulations and hyperbolic space models. Shadow cones offer advantages over existing constructions, particularly in terms of optimization properties. Experimental results demonstrate the consistent and significant outperformance of shadow cones compared to existing entailment cone constructions across datasets of varying sizes and hierarchical structures.

### Strengths
1. The introduction of shadow cones presents an innovative approach to defining entailment relations in hyperbolic space. Drawing inspiration from physical phenomena adds an intuitive and captivating aspect to the concept.

2.  The authors provide a comprehensive mathematical formulation for shadow cones, enhancing the rigor of their work and enabling further exploration and development by other researchers in the field.

3.  The experimental results across four datasets demonstrate the superior performance of the proposal compared to the current state-of-the-art methods.

### Weaknesses
1. While the authors tested their framework on four datasets, it would be beneficial to see how the framework performs on a wider variety of datasets, including those from different domains or those with different characteristics (like KG, recommender system datasets and so on). This would provide a more comprehensive evaluation of the framework's performance and versatility.

2.The work builds on the entailment cone but a few partial order methods have been proposed and a thorough comparison or discussion is needed.

3. Captions for the figures are brief and ambiguous, hindering their readability.

### Questions
see weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a physically intuitive partial order embedding framework "shadow cones" that generalizes the well-known "hyperbolic entailment cones". Also, this framework generalizes to two different hyperbolic models, the Poincaré disk and Poincaré half-space. The experiments shows that the generalized "shadow cones" outperform the "hyperbolic entailment cones" baseline.

### Strengths
1. The paper is well-motivated and has a good connection to existing research.
2. It considers two hyperbolic models, the Poincaré disk and the Poincaré half-space.
3. The theoretical analysis provides nice properties of the proposed models.

### Weaknesses
1. Compared with the novel and interesting motivation, the description, especially the figures, lacks explanation, almost all the symbols in the figures are not mentioned in the captions or corresponding text.
2. The experiment is not very supportive of the claim. For example, In the experiment, Poincaré ball based cones performed worse than Poincaré half-space based cones. While in the important baseline "hyperbolic entailment cones", the Poincaré ball is used, if the proposed cone generalizes "hyperbolic entailment cone", it should be as good as the "hyperbolic entailment cone".
3. The use of different definitions for light source in the Penumbral cone and the Umbral cone is somewhat inconsistent.

### Questions
Please see the weaknesses.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the use of (light) cones to learn embeddings of posets in hyperbolic space. Specifically, the paper looks at two models depending whether the data or the light source has mass. The paper proves a variety of consistency results such the fact that inclusion of the cones form a poset.

### Strengths
The idea of using cones is quite interesting to me. The paper shows that it results in a loss at least at the optimal point that does preserve the partial order structure. Further, it does so in a way that gives coordinates from which we can extract the partial order. Hence I think this is quite interesting and quite novel. I think of these are strong strengths. 

The paper is mostly easy to follow however there are a few details I would like added. Please see weaknesses and questions

### Weaknesses
1) The first weakness for me is the context for the work. I think some more discussion to related concepts such as DAG learning, which is learning DAGs from data [1,2,3], other hyperbolic hierarchical learning like hyperbolic tree learning, which is about learning trees to represent hyperbolic data or embed in hyperbolic apace [4,5], graph embeddings in hyperbolic space [6,7,8], and hyperbolic link prediction [9] would be great. Specifically, the paper should discuss how the proposed method relates to or differs from these existing approaches. For example, how does the light cone approach compare to methods that directly learn DAG structures or those that embed graphs into hyperbolic space while preserving hierarchical relationships? A more detailed discussion of the specific advantages and disadvantages of the light cone approach compared to these alternatives would be beneficial.

2) I think the experimental setup could be further expanded upon. First, I think it should be clarified that we can do the link prediction without the embedding step (this would have a 100% accuracy) and then mention that you do the embedding step to understand the how well the embedding performs. As part of the experiment, it would be good to have a baseline for Euclidean poset embedding. However, I admit I do not know of one. Maybe on of the DAG learning papers has a baseline that could be used. It's not clear how the reported link prediction accuracy relates to the quality of the learned embeddings. It would be helpful to see a comparison against a more direct Euclidean embedding of posets, even if a direct baseline is not readily available, perhaps by adapting a method from the DAG learning literature. The paper should also clarify how the embedding is evaluated beyond link prediction, and what metrics are used to assess the quality of the learned poset structure.

3) Building on the above it would be good to show that such embeddings can be used other non-trivial down stream tasks and that such embeddings provide an advantage. The paper should demonstrate the utility of the learned embeddings in downstream tasks beyond link prediction. For example, could these embeddings be used for classification tasks where the hierarchical structure is relevant? Or could they be used to improve the performance of other models that rely on hierarchical information? Showing a concrete example of how the embeddings can be used in a downstream task would significantly strengthen the paper's contribution.

### Questions
I have a few questions. 

1) In the loss function $P$ and $N$ haven't been defined. 

2) For the cones I do not understand the boundary computation. Could the authors please expand on that? I did not see anything in the appendix either. 

3) Why do we need the ball around $y$ to be in the shadow for $y$ to be in the umbral cone, but only need the point $y$ to be in the shadows for the penumbral cone? I see that the umbral method seems to perform the best. I imagine based on how the loss in formulated this pushes the point to the interior of the cone rather than leaving it on the boundary where we might have numerical issues. 

4) Could the authors provide intuition for why umbral cones are not geodetically convex? I believe in this regard calling them cones might be a bit confusing, because cones in Euclidean space are not only convex, but contains these geodesic rays. I would have thought the same is true for the hyperbolic ones. Hence was surprised when I saw this result.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Hyperbolic space have been shown to be particularly well suited to encode the latent structure of complex objects such as trees or graphs. In particular, using random graphs with an hyperbolic latent space are known to exhibit properties often found in real world networks such a the small world phenomenon or the scale free property. 

In this paper, the authors introduce the so-called shadow cones framework: a methodology that allows to define a partial order embedding of hierarchical data. The authors show that such framework can be particularly efficient to learn a latent embeddings of nodes for trees or more generally for DAGs. Their method extends to the concept of entailment cones previously introduced by Ganea. On three different datasets, the authors show that using their method to learn the hierarchical structure of partially observed DAGs can allow to infer unseen edges better than previous approaches.

### Strengths
- Hyperbolic spaces have been shown to be very promising latent space to model graph data. This paper is focused on DAGs and proposes a new framework to learn embedding for hierarchical data. 

- The authors did an excellent job in ensuring the comprehensibility of their method, notably by incorporating highly insightful illustrations.

- As a by product, the paper provides a comprehensive overview of various approaches to incorporate 'shadows' for embedding points in hyperbolic space, employing the concepts of umbral and penumbral cones. This lucid exposition elucidates the source of the limitations observed in prior methods, particularly with regard to the $\epsilon$ hole problem.

### Weaknesses
 - I think the authors should better stress the concrete applications of their method. For example, are there applications related to structure learning?  

- In my opinion, the authors should include in their comparison methods that do not rely on hyperbolic spaces (but rather on Euclidean ones for example or with manifold with positive curvature).


### Questions
I thank the authors for their nice submission.

Apart for my questions presented in the previous section (i.e. use of the method for applications and comparison with methods not using hyperbolic spaces), I would be interested to know if the method could be used in more general settings. In particular:

- How the method could be used for real world graphs that are not (exactly) DAGs?

- How the method could be used for multiclass hierarchical problems?

Here are some typos and additional comments: 

- In the loss function (cf. Eq(1)), if think N and P are not properly defined in the text.

- At the end of the first paragraph of the introduction of Section 3, I think there is an error. Should the last sentence rather be "Specifically, $v$ is in the shadow cone of $u$ iff $v \subset$ the shadow of $u$." ?

- After Theorem 4.2, I think the first "their" should be removed from the sentence "which is
designed to draw child nodes v closer to their the cones of their patent nodes".

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of learning representations to model hierarchical relationships using hyperbolic space. The authors introduce several formulations of *shadow cones*, a novel and unifying framework of physics inspired representations. Entailment relations are defined by the containment of shadows of the object representations given a fixed light source and boundary if hyperbolic space. The authors present two different shadow formulations each in two different hyperbolic spaces. A smooth loss function is introduced to train shadow cones in a stable manner, avoiding some of the training issues presented in prior work. The effectiveness of the presented method is shown on standard open source datasets.

### Strengths
* The proposed approach is novel and well-motivated, avoiding many of the issues in prior work
* The proposed representation formulation encapsulates previous approaches
* The paper is well written and includes many intuitive figures and diagrams to illustrate the proposed approach
* The empirical results demonstrate the efficacy of the proposed methodology on standard datasets for this task

### Weaknesses
 * The paper uses quite a bit of space introducing all four formulations of shadow cones, leaving less space for additional empirical results
* At the end of Section 4, the authors make claims about ease of training, but do not justify claims beyond just a statement by fiat. 
* The proposed approaches are only compared against a single baseline -- even though this is the supposed state of the art in hyperbolic representations it would be beneficial to see comparisons with other methods.
* The empirical results are all demonstrated on the same singular type of task. It would benefit the paper to see experiments on different types of tasks such as collaborative filtering.

### Questions
* What advantages might this method have over a different representation learning paradigm such as box embeddings (e.g. [1])?
* Why is there such a big discrepancy in the results between Penumbral-Poincaré-ball and Entailment cones in Table 2? These formulations are mathematically equivalent, but perform quite differently in some cases. Is this attributable to the loss function or training procedure in some way?
* What is the relationship between convexity and performance? The non-convex method seems to perform better. Why is this the case?
* What are the potential challenges to learning representations in the half-space formulation?

[1] Dasgupta S, Boratko M, Zhang D, Vilnis L, Li X, McCallum A. Improving local identifiability in probabilistic box embeddings. Advances in Neural Information Processing Systems, 2020

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposed physically-intuitive embedding method for partial order hierarchy. The method uses shadow cones, which generalize existing hyperbolic entailment cones. The author also constructed the algorithm to optimize the shadow cones.

### Strengths
1. The paper provides novel multiple variants of the existing hyperbolic entailment cone method. The techniques provided for handling shadow cones are significant technical contributions in the area.
1. The physics-inspired explanation, with plenty of intuitive figures, of the proposed method helps readers understand the proposed method's concept and algorithm. The explanation also provides another explanation of why existing hyperbolic entailment cones cannot be defined for a point around the center of the Poincare ball.
1. Table 1 summarizes the proposed 4 methods well.

### Weaknesses
Overall, the paper is well-written as a technical report but has room for improvement in terms of scientific discussion or presentation.
1. Although the light-source-shadow-based explanation is quite helpful in understanding WHAT the proposed methods are doing, but does not explain at all WHY they do so. Specifically, we do not see what the shape and size of the light source and the size of embedding in the umbral cases imply in the context of partial order or semantics. Also, readers do not see how we select one of the 4 proposed methods depending on the situation.
2. Overall, the paper is written as a technical extension of the hyperbolic entailment cone method, but the current draft does not position the proposed method well in the context of the whole partial order embedding area. It is not an unacceptable way, but limits the readers. The authors might want to compare it with other methods such as Order embedding, Gaussian embedding, Box embedding, etc.
3. The title of the paper lacks essential keywords and confuses readers. It should include the word "shadow cone." Also, if possible, the words "hierarchy" or "partial order" could be included. Readers might think the phrase "dark side" indicates the surface of a hemisphere, rather than a shadow cone. Also, from the word "moon," readers feel the impression that the embedding has a volume. However, this is not the case for the penumbral cone embedding. I am aware that we have many styles on which we title a paper, but, at least, we need to avoid confusing readers.

### Questions
1. Why the experimental results by Entailment Cone and Penumbral-Poincaré-ball are different while they are equivalent according to Theorem 3.2?
1. What do the shape and size of the light source and the size of embedding in the umbral cases imply in the context of partial order or semantics?
1. How do we select one of the 4 proposed methods depending on the situation?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
