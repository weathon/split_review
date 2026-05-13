# Extending Contextual Self-Modulation: Meta-Learning Across Modalities, Task Dimensionalities, and Data Regimes

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Contextual Self-Modulation (CSM) is a potent regularization mechanism for the Neural Context Flow (NCF) framework which demonstrates powerful meta-learning of physical systems. However, CSM has limitations in its applicability across different modalities and in high-data regimes. In this work, we introduce two extensions: $i$CSM, which expands CSM to infinite-dimensional tasks, and StochasticNCF, which improves scalability. These extensions are demonstrated through comprehensive experimentation on a range of tasks, including dynamical systems with parameter variations, computer vision challenges, and curve fitting problems. $i$CSM embeds the contexts into an infinite-dimensional function space, as opposed to CSM which uses finite-dimensional context vectors. StochasticNCF enables the application of both CSM and $i$CSM to high-data scenarios by providing an unbiased approximation of meta-gradient updates through a sampled set of nearest environments. Additionally, we incorporate higher-order Taylor expansions via Taylor-Mode automatic differentiation, revealing that higher-order approximations do not necessarily enhance generalization. Finally, we demonstrate how CSM can be integrated into other meta-learning frameworks with FlashCAVIA, a computationally efficient extension of the CAVIA meta-learning framework (Zintgraf et al. 2019). FlashCAVIA outperforms its predecessor across various benchmarks and reinforces the utility of bi-level optimization techniques. Together, these contributions establish a robust framework for tackling an expanded spectrum of meta-learning tasks, offering practical insights for out-of-distribution generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors investigate model based meta-learning approaches that involve learning a dataset-specific context for learning function changes across datasets, which they refer to as contextual self modulation (CSM). They specifically introduce an infinite-dimensional, stochastic meta-learning approach that extends recent work and apply the method to different settings including image completion, control and dynamical system reconstruction.

### Strengths
Context-based meta learning has become a popular approach for training models that can adapt to new data in few-shot settings. There are limited studies investigating the strengths and weaknesses of these methods – making this an overall well motivated and interesting problem to address. The authors report the performance of their approach under diverse experimental settings, demonstrating the wide applicability of CSM to different domains. That being said, I have various concerns that I highlight below.

### Weaknesses
Presentation
* In the introduction, the authors motivate the paper as a systematic comparison of contextual meta-learning approaches but only focus on a recently proposed method Neural Context Flow (NCF) and Cavia which seems a little misleading.
In the Introduction R2 (line 064), I find the authors’ introduction of task dimensionality a little confusing. At the beginning, it seems like the authors are referring to function spaces like vector fields for which several approaches have been proposed but then discuss a non-stationary variable as an example. I could be misunderstanding something, but it would be useful to further clarify this point and how exactly the iCSM addresses this.
* The main contributions – the infinite-dimensional CSM and stochastic NCF could to be better motivated and further expanded because it is a little unclear. Specifically, I don’t fully understand the motivation for iCSM and how it is different from approaches that use context-conditioned hypernetworks, like CoDA. In lines 192-194, the authors claim that “This extension allows our model $f_{\theta}$ to adapt to a broader range of changes and potentially leverage Lie group symmetries for dynamical systems and translation equivariance for images” – I don’t see why this would be the case. 
* While FlashCavia offers strong improvements over Cavia, I don’t see how it relates to the proposed approach, unless I’m misunderstanding something. 

Experiments
* The empirical results are highly variable across experiments. While it is not important to have the best performance across the board, the lack of consistent trends makes it hard to evaluate the proposed approach. For instance, FlashCAVIA has the best performance on Sine Regression, in the Image Completion task, the performance does not co-vary with K for either approach considered. 
* Limited baselines are considered, and they are not evaluated consistently across experiments. If there are optimization issues because of the higher order gradients in Cavia, it would still be interesting to consider how the specific parametrization they proposed compares to the NCF/iNCF. In general, a more thorough related works section and additional baseline comparisons would be helpful.

### Questions
* Why do the authors use NCF* (line 428) in the image completion task?
* From what I understand, CoDA relies on low-dimensional adaptation of weights. Why do the authors use a context size of 256? In the original paper, the method is only used with a context dimensionality of 1 or 2. It would be good to additionally include the case where the context is low-dimensional. 
* Did the authors compare their approach to CAMEL (Blanke & LeLarge, 2024)? It also seems like an important baseline to consider, specifically, for measuring performance with higher-order Taylor expansion terms.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to meta-learning in high-data regimes by combining contextual self-modulation with CAVIA, an efficient optimization-based meta-learning framework. The main goal of this methodology is to expand the use of context information to infinite-dimensional spaces, addressing challenges such as handling a high volume of predictions when incorporating context. Additionally, the method employs a high-order Taylor expansion to effectively leverage context information for enhanced predictions.

To validate their approach, the authors conducted experiments on optimal control and forced pendulum tasks, demonstrating its applicability within scientific machine learning contexts. The results indicate that this model offers a more generalizable and efficient way to incorporate contextual information across low, medium, and high-data regimes, outperforming existing methods in both interpolation and extrapolation.

### Strengths
- This paper provides experimental validation showing that the proposed method maintains stability across a range of hyperparameter values, such as the order of Taylor expansion and the number of training steps. The results demonstrate that, even with variations in these newly introduced hyper-parameters, the method consistently outperforms previous algorithms, highlighting its robustness in hyper-parameter selection in curve-fitting experiments.

- This study explores the application of gradient-based meta-learning in the context of image completion. Specifically, family of gradient-based meta learning has traditionally seen limited success, on the other hand, this paper combining well-suited context self modulation structures illustrates that optimization-based meta-learning can indeed be effective for image completion, even in high-number prediction settings, thus broadening the potential applications of gradient-based meta learning approaches.

### Weaknesses
 - This paper lacks a clearly defined contribution compared to existing models. This makes its core message difficult to understand. While the authors emphasize the performance of Context Self Modulation, high-order Taylor expansion, and FlashCAVIA or NCF as the backbone, the proposed method appears simple combination of these techniques on selected tasks. To convince the proposed method’s efficacy, I believe that a clearer illustration of the limitations of existing models and the way this approach effectively addresses would be necessary compared to existing methods. However, a majority part of the paper is to describing components to enhance the impression of this paper rather than substantiating significant performance improvements.

- While the paper emphasizes the potential of Context Self Modulation, its application is restricted to models like FlashCAVIA and NCF. Although the authors suggest broad applicability based on a variety of experiments, the focus remains on algorithms tailored to these specific frameworks, which may exaggerate the method’s generalizability.

- The necessity of high-order Taylor expansion for effectively leveraging context information is still ambiguous. The authors propose that this component is crucial, but Figure 1 does not show a substantial performance impact. This raises the question of whether a simpler, linear use of context information could be equally effective. Without compelling evidence for the necessity of high-order Taylor expansion, the paper does not convincingly establish why this feature is essential to the proposed method.

- The paper would benefit from the schematic figures to provide a clearer overview of the methodology. Additionally, numerous notational errors and inconsistencies impede understanding of the finer details. For instance, symbols such as $k$ and $K$ are used interchangeably despite having different meanings, and there is no clear explanation distinguishing $N$ from $K$. These issues with notation are unstructured and make it challenging for readers to follow the paper’s technical details accurately.

### Questions
- This paper requires additional parameters for Context Self Modulation compared to models like Neural Processes or MAML, yet does not address this increase anywhere in the discussion. To address the limitations of gradient-based methods, Context Information is utilized, but a clear comparison of this approach against existing methods is necessary. Specifically, it would be helpful to see how the number of Context Self Modulation parameters or the nature of the task impacts performance relative to established models. Especially for curve fitting experiments including forced pendulum and optimal control.

- Secondly, Figure 3 reveals significant underfitting, raising questions about the actual impact of Context Self Modulation. Given the observed underfitting in these experimental results, it remains unclear how effectively Context Self Modulation contributes to model performance. A closer examination of whether Context Self Modulation is indeed causing this underfitting would clarify its role in the training process.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper extends Neural Context Flows (NCFs) [1], a recent method also in submission to this same conference, designed for meta-learning in dynamical systems applications. In particular, this work: 1) Extends a component of NCF (named iCSM) by applying it on the parameters of small networks (rather than finite vectors as in the original paper) 2) Proposes a new stochastic training strategy where the meta-learning tasks to optimize are randomly subsampled at each iteration. 3) Provides a new updated implementation of the CAVIA [2] algorithm and shows its compatibility with iCSM.

[1] Nzoyem, Roussel Desmond, David AW Barton, and Tom Deakin. "Neural Context Flows for Learning Generalizable Dynamical Systems." arXiv preprint arXiv:2405.02154 (2024).

[2] Zintgraf, Luisa M., et al. "Fast Context Adaptation via Meta-Learning." arXiv preprint arXiv:1810.03642 (2018).

### Strengths
1. There are several different orthogonal incremental contributions (e.g., iCSM, StochasticNCF, FlashCAVIA) with different purposes, which seem valuable and natural extensions to the NCF paper.

2. I found some of the qualitative analyses of the smoothing behavior, from introducing CSM to FlashCAVIA, insightful in obtaining an intuitive understanding of the methodology.

3. Overall, the writing is relatively clear, with most of the related background for understanding CSM and NCF introduced early on.

4. While I did not carefully check the code, the paper and results seem fully reproducible.

### Weaknesses
Main:

1. On its own, each contribution seems relatively minor e.g., to my understanding, stochasticNCF simply corresponds to randomly subsampling a set of environments during backpropagation of the meta-gradient. Similarly, FlashCAVIA is simply a port of CAVIA onto Jax, with minor changes to integrate it with CSM. While I did not carefully check the code, there do not seem to be new CUDA kernels introduced, as the name would seem to suggest. Thus, I am unsure whether these contributions are of enough novelty to stand as a full paper.

2. Given the incremental nature of this work over a still-not-established, recent prior method, I am not convinced of its relevance for the broader ICLR community.

3. The majority of the experimental evaluation is dedicated to toy domains (e.g., sine curve fitting/parametric ODEs). In contrast, the closely related CAVIA,  while being from 2018, still provided results on canonical benchmarks such as mini-imagenet and relatively complex Mujoco RL environments. While surely this paper's results can be insightful, they did not convince of the general applicability and potential impact of the methodology.

Minor:
 
1. Overuse of acronyms/abbreviations (e.g., InD, OoD, CSM, CNP, GBML, NCFs,...) can make the text hard to follow.

### Questions
Please, I would appreciate it if the authors could address the criticism raised above and, potentially, correct any mistakes in my current understanding of this work.

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
2

### Summary
This paper proposes to extend Contextual Self-Modulation (CSM), which is an uncertainty-handling mechanism of Neural Context Flow (NCF). NCF is a robust meta-learning framework of neural ODE that includes self-modulation with high-order Taylor expansion around contexts. The authors focus on generalizing CSM into high data regimes and designed StochasticNCF and FlashCAVIA, which take CSM in various directions. From comparative experiments, the author verified that the NCF can be successfully extended to various optimization and meta-learning techniques.

### Strengths
1. This paper proposed various possibilities of neural context flow that can contribute to studies of meta-learning in dynamical systems. 
2. The authors have proposed various efficient and scalable extensions to CSM, which can be comprehended at a high level.
3. The study advanced the applicability of CSM to a wide spectrum of tasks and modalities.

### Weaknesses
1. I believe this paper is not clearly written.
    * iCSM: It is briefly mentioned that the space of iCSM is "an infinite-dimensional variation" that utilizes "a space of multi-layer perceptrons, whose weights are flattened into a 1-dimensional tensor." I do not find a good enough explanation, mathematical notation, or relevant resources to understand this concept fully. Specifically, the mapping from the context to the MLP weights is unclear, and the dimensionality of the flattened tensor is not explicitly defined in relation to the MLP architecture. The authors should clarify how the context vector influences the weights of the MLP and provide a concrete example with a specific MLP architecture to illustrate the process.
    * StochasticNCF: this translates high-order Taylor expansion to standard SGD estimation. Then, Isn't it just another formulation of the first-order Taylor expansion? If it is just a specific case of applying the Taylor expansion, it might not be considered a pure contribution of this work. Moreover, the author should have provided meaningful theoretical or experimental results of this design. The authors should clarify the specific conditions under which StochasticNCF provides an advantage over standard first-order methods, and provide empirical evidence to support claims of its effectiveness. The connection to high-order Taylor expansion is not clearly justified, and further clarification is needed to understand the theoretical underpinnings of this approach.
    * FlashCAVIA: FlashCAVIA is claimed as a powerful upgrade of CAVIA, in terms of efficiency and custom optimizer. First, the presentation of CAVIA in the manuscript is not appropriate; for example, I do not understand why specifically CAVIA is chosen among various meta-learning approaches. Also, not much theoretical advances of FlashCAVIA from CAVIA (Algorithm 1) can be found to be an "upgrade." If the "custom optimizer" is one of the key improvements, its benefit must theoretically be validated within the same number of gradient updates. The authors should provide a detailed comparison of FlashCAVIA and CAVIA, highlighting the specific modifications that lead to improved performance. The choice of CAVIA should be justified with respect to other meta-learning algorithms, and the theoretical advantages of the custom optimizer should be clearly demonstrated through analysis or experiments.
2. Building on the previous point, the contributions of this paper primarily lie in the implementation of dynamical meta-learning frameworks. While I do believe these technical contributions are important, certain claims on efficiency and scalability require additional experiments for full validation. The authors should provide more rigorous benchmarks to support their claims, including comparisons with state-of-the-art meta-learning algorithms and a detailed analysis of the computational complexity of their proposed methods. The current experiments do not fully validate the scalability of the proposed approach.
3. It is crucial to demonstrate the performance of FlashCAVIA-100, MAML-100, and CAVIA-100, along with the total elapsed time measurements for training. The lack of this information makes it difficult to assess the practical value of the proposed methods. The authors should provide a comprehensive performance comparison, including both accuracy and training time, to allow for a fair evaluation of their work.
4. As stated in Section 4.2, some essential benchmarks for meta-learning need to be included.

### Questions
Please see the Weaknesses section.

### Soundness
3

### Presentation
1

### Contribution
2
