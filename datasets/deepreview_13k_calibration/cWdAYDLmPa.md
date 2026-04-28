# State Representation Learning Using an Unbalanced Atlas

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
The manifold hypothesis posits that high-dimensional data often lies on a lower-dimensional manifold and that utilizing this manifold as the target space yields more efficient representations. While numerous traditional manifold-based techniques exist for dimensionality reduction, their application in self-supervised learning has witnessed slow progress. The recent MSimCLR method combines manifold encoding with SimCLR but requires extremely low target encoding dimensions to outperform SimCLR, limiting its applicability.}. We investigated and engineered the DeepInfomax with an unbalanced atlas (DIM-UA) method by adapting the Spatiotemporal DeepInfomax (ST-DIM) framework to align with our proposed UA paradigm. The efficacy of DIM-UA is demonstrated through training and evaluation on the Atari Annotated RAM Interface (AtariARI) benchmark, a modified version of the Atari 2600 framework that produces annotated image samples for representation learning. The UA paradigm improves existing algorithms significantly as the number of target encoding dimensions grows. For instance, the mean F1 score averaged over categories of DIM-UA is \(\sim \)75\% compared to \(\sim \)70\% of ST-DIM when using 16384 hidden units.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper developed a state representation learning method leveraging an unbalanced atlas (UA). The authors have modified the ST-DIM algorithm to align with the proposed UA paradigm. Although the main contribution is not stated intuitively, empirical evaluations on 19 games of the AtariARI benchmark suggested an improved performance compared with three established baseline methods (many existing self-supervised methods are omitted for comparison). Furthermore, the authors performed a comprehensive ablation study for the design choices of the proposed method.

### Strengths
+ The experiments are conducted across 19 games of the AtariARI benchmark, covering a variety of vision tasks.

+ There are comprehensive ablation studies for the technical components of the proposed method.

### Weaknesses
- The clarity of the introduction could be enhanced by providing a more explicit context for the specialized terminology introduced. Specifically, the first sentence of the third paragraph introduces concepts such as *manifold*, *atlas*, *local structure*, and *chart*. These terms require a more thorough explanation to ensure the reader can fully grasp the theoretical underpinnings of the proposed method. For instance, a concise definition of a manifold in the context of state representation learning, followed by how an atlas is used to represent it, would greatly improve clarity. Similarly, explaining what constitutes a "local structure" within this manifold and how a "chart" captures it would be beneficial.

- The comparison would benefit from the inclusion of key baseline models which are currently absent. While SimCLR is mentioned, the paper does not compare the proposed method with other self-supervised learning methods, particularly generative models. The absence of comparisons with relevant generative models, especially considering their prevalence in state representation learning, weakens the empirical evaluation. Including such comparisons would provide a more comprehensive understanding of the proposed method's performance relative to the broader landscape of self-supervised learning.

- Tables 1 and 2 appear to be redundant, presenting analogous results through different evaluative metrics (F1 score and Accuracy, respectively). Although a comprehensive evaluation is encouraged, putting these two sizable tables back to back in the main paper gives the impression of lacking sufficient materials for the paper. It would be more appropriate to consolidate these findings, perhaps through a combined analysis or in supplementary materials, to avoid repetition and maintain the conciseness of the paper.

- the paper lacks a clear statement of its underlying motivation and significance, which is pivotal for readers to comprehend the value and potential impact of the research. The concept of an *atlas*, and particularly the distinction between *unbalanced* and *balanced* atlases within this framework, needs clarification. Furthermore, the introduction does not clearly articulate why the unbalanced atlas (UA) paradigm is important or advantageous. The terms *prior distribution* and *membership probability distribution* introduced later also lack clear definitions, further obscuring the motivation. Additionally, the statement about representing a manifold with a larger number lacks context and does not explain why this is a significant contribution. A more explicit articulation of the problem being addressed and the significance of the proposed solution would greatly enhance the paper's impact.

### Questions
1. The introduction used specialized terminology that may not be universally familiar, necessitating additional clarification for a broader audience. Specifically, the first sentence of the third paragraph introduces concepts such as *manifold*, *atlas*, *local structure*, and *chart*, which would benefit from further exposition to contextualize the study and its objectives.

2. The paper's motivation remains unclear, partly owing to the use of undefined terms. The concept of an *atlas*, and particularly the distinction between *unbalanced* and *balanced* atlases within this framework, needs clarification. The terms *prior distribution* and *membership probability distribution* introduced later also lack clear definitions, impeding the reader's understanding.

3. In the 3rd paragraph of Section 4, *d* and *n* are used without proper definition.

4. This paper suggests that pre-training a model using a reinforcement learning task and then fine-tuning it on downstream reinforcement learning tasks is beneficial. However, this point is not fully demonstrated because the authors did not compare the proposed method with other self-supervised learning methods, as reviewed in the introduction, e.g., contrastive models (SimCLR is compared) and generative models (none is compared).

5. From the introduction section, it is not intuitive to me why this study is important. For example, the last paragraph lists technical achievements but does not convey their broader significance. Specifically, (1) fitting the ST-DIM to UA paradigm (why UA paradigm is important?), (2) detailed ablations for better design choices (that's standard, not sure if it counts as a contribution), and (3) representing a manifold with a larger number (why this is important anyway?). Not limited to the introduction section, the authors did not describe the significance of the proposed method and all these ablation studies in the entire paper.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of learning a low-dimensional manifold from high-dimensional data in the context of state representation learning. A new approach based on self-supervised learning is proposed in order to learn an unbalanced atlas representation. The proposed approach is called DeepInfomax with an unbalanced atlas (DIM-UA) and is evaluated on 19 Atari games of the AtariARI benchmark. The evaluation shows good performance in this benchmark.

### Strengths
The paper addresses an important topic in the area of state representation learning. The proposed algorithm seems novel and yields good performance in the tested benchmarks.

### Weaknesses
I am struggling to understand the rationale behind the DIM-UA algorithm. What is the motivation for redefining the score function L_GL? The paper mentions dilated prediction targets, but it's not clear how this necessitates a change in the score function itself. Specifically, how does the use of dilated targets interact with the InfoMax principle to justify the modified L_GL? Equation 9 has a hyperparameter for L_Q but not for L_GL or L_LL. Why is there a need for a hyperparameter to control the MMD loss on membership probabilities (L_Q), but not for the other loss terms? It's unclear why the learning rate alone would be sufficient to control the influence of L_GL and L_LL, especially given that they are also involved in the overall optimization process. The writing of the paper is not clear in several points as some parts are difficult to follow. For example, Figure 1 is not quite clear to me and the caption is not very explicit. Additionally, the results could be presented in a more concise fashion (esp. Table 1 and 2 - showing the best results in bold would increase the readability). The improvements reported in table 2 seem relatively small, especially when considering the complexity introduced by the unbalanced atlas approach. The benefits of this added complexity need to be more clearly justified with more substantial performance gains. Why is the linear evaluation accuracy on CIFAR10 a suitable evaluation metric? The improvements shown here (table 3) are very marginal at best. It's not clear how this metric relates to the core problem of learning state representations in reinforcement learning environments.

### Questions
- What is the motivation for redefining the score function L_GL? 

- Equation 9 has an hyperparameter for L_Q but not for L_GL or L_LL. Why?

- The improvements reported in table 2 seem relatively small. Can you comment on this further?

- Why is the linear evaluation accuracy on CIFAR10 a suitable evaluation metric? The improvements shown here (table 3) are very marginal at best.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose to use multiple heads at the end of an encoder for
contrastive learning, instead of one. These heads are considered to
model different charts in an atlas, mapping the data manifold to the
embedding space. For a given sample, a score is computed to determine,
probabilistically, which chart should be used to encode
it. A theoretical discussion is presented to support outputting a
weighted average of charts based on scoring function, which relies on
Minkowski sum of open sets to which charts map. The scoring function
is forced to be different than a uniform distribution, thus the
unbalanced nature of the mapping. Experiments are conducted to
understand whether using multiple heads and weighted averaging at the
output leads to better representations than using a single head with
the same number of latent dimensions.

### Strengths
1. More expressive models for contrastive learning are very relevant
   and interesting for the community. Here authors point out that when
   the embedding dimension is very high, naive contrastive learning
   may not use the embedding space very well. Instead of using a
   single projection head, authors proposal to use multiple projection
   heads seem to lead to better results according to Tables 1
   and 2. This is a simple yet - seems to be - an effective
   modification.  
2. Results of the ablation study shown in Figure 2 are very
   convincing. This simple approaches surely uses the dimensions much
   more efficiently, and provides the expected gains in accuracy.
3. The difference between +MMD and the proposed version, which I
   assume is -MMD, is striking.
4. This reviewer appreciates the experiments with CIFAR.

### Weaknesses
1. Technical contribution is not at a very high level, but the
   contribution is focused and pertinent.
2. In the ablation study, the model "-UA" is not clearly specified. If
   authors do not use the modifications of 7, that means the -MMD loss
   is also void. What does that yield? Are authors using a single
   projection head in this case?
3. CIFAR experiments show that the gains are much lower in these
   experiments compared to the ones obtained in ATARI games. A
   discussion towards this end is not provided but it would be very
   valuable for the readers.
4. Notation in the presentation of the method seems a bit
   inconsistent. I recommend authors to improve the consistency in the
   notation.

### Questions
1. can authors discuss further why the CIFAR experiments do not show a
   similar improvement?
2. can authors please improve the notation consistency in the
   presentation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
