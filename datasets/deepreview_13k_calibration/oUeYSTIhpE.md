# DisCo-DSO: Coupling Discrete and Continuous Optimization for Efficient Generative Design in Hybrid Spaces

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
In this paper, we consider the challenge of optimizing within hybrid discrete-continuous spaces, a problem that arises in various important applications, such as symbolic regression and decision tree learning. We propose DisCo-DSO (Discrete-Continuous Deep Symbolic Optimization), a novel approach that uses a generative model to learn a joint distribution over discrete and continuous design variables to sample new hybrid designs. In contrast to standard decoupled approaches, in which the discrete and continuous variables are optimized separately, our joint optimization approach uses fewer objective function evaluations, is robust against non-differentiable objectives, and learns from prior samples to guide the search, which leads to significant improvement in performance and efficiency. Our experiments on a diverse set of optimization tasks demonstrate that the advantages of DisCo-DSO become increasingly evident as problem complexity grows. In particular, we illustrate DisCo-DSO’s superiority over the state-of-the-art methods for interpretable reinforcement learning with decision trees.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes DisCO-DSO, a generative modeling approach to learn a joint distribution over continuous and discrete variables. Prior works follow a decoupled approach, where the discrete and continuous variables are modeled separately, leading to inefficiency in the sampling and optimization procedure. DisCO-DSO uses an autoregressive model and produces two latent variables, one is used to generate the discrete distribution, and the other is used to generate the continuous distribution. This method requires one evaluation step per sample, whereas prior approaches use black-box optimization methods to sample the continuous variable for each discrete token. Experiments are performed on a newly proposed parameterized bitstring task, symbolic regression for equations, and learning decision tree policies for RL. The experiments demonstrate competitive performance with existing methods while improving efficiency.

### Strengths
This work proposes a fairly simple approach to model hybrid spaces, which improves the efficiency compared to existing work. The idea of modeling the discrete and continuous distributions using different latent vectors in this context is novel, to the best of my understanding. The parameterized bitstring task is simple yet effective for benchmarking the performance of hybrid space generative models. In my opinion, this work has a moderate impact on a specific sub-area of generative modeling. 

The presentation and quality of writing are mostly clear. The paper provides relevant context and then describes the proposed method along with model diagrams to illustrate the difference to prior work clearly.

### Weaknesses
The main weaknesses of the paper are poor baselines in the experiments and some organizational changes for clarity. The experiments consider baselines that decouple the discrete and continuous space optimization, but many of the recent works mentioned in the related works are not considered as baselines. Without this comparison, it is difficult to ascertain the empirical performance of DisCO-DSO. Another issue is that while the writing is clear, there are some minor organizational changes that can improve the readability of the paper.  See the questions below for more details.

**********************Comparison with prior work:********************** The related works section describes prior work in the area with different approaches to the problem of modeling joint discrete-continuous spaces, such as Petersen et al., 2021;  Kamienny et al., 2022; Sahoo et al., 2018 and specifically for symbolic regression such as Biggio et al., 2021; Landajuela et al., 2021. The comparison with Petersen et al., 2021 is especially relevant since DisCO-DSO uses the same risk-seeking policy gradient approach to optimize the reward-based objective. Without comparison with relevant prior work, it is difficult to accurately gauge the significance of the empirical contribution.

****************************************************************Choice of autoregressive model:**************************************************************** DisCO-DSO uses LSTMs for autoregressive sequence generation. It would be interesting to see the effect on performance if the backbone model was changed, possible options include GRUs and Transformers.

********************************************************Organization and structure:******************************************************** The readability of the paper can be improved by using paragraph titles to better organize large bodies of text, particularly Section 2, Section 3.2, Section 4.2 and Section 4.3.

### Questions
**********************Comparison with prior work:********************** The related works section describes prior work in the area with different approaches to the problem of modeling joint discrete-continuous spaces, such as Petersen et al., 2021;  Kamienny et al., 2022; Sahoo et al., 2018 and specifically for symbolic regression such as Biggio et al., 2021; Landajuela et al., 2021. The comparison with Petersen et al., 2021 is especially relevant since DisCO-DSO uses the same risk-seeking policy gradient approach to optimize the reward-based objective. Without comparison with relevant prior work, it is difficult to accurately gauge the significance of the empirical contribution.

****************************************************************Choice of autoregressive model:**************************************************************** DisCO-DSO uses LSTMs for autoregressive sequence generation. It would be interesting to see the effect on performance if the backbone model was changed, possible options include GRUs and Transformers.

********************************************************Organization and structure:******************************************************** The readability of the paper can be improved by using paragraph titles to better organize large bodies of text, particularly Section 2, Section 3.2, Section 4.2 and Section 4.3. 

**********************References:**********************

- Brenden K. Petersen, Mikel Landajuela, T. Nathan Mundhenk, Cl´audio Prata Santiago, Sookyung
Kim, and Joanne Taery Kim. Deep symbolic regression: Recovering mathematical expressions
from data via risk-seeking policy gradients. In 9th International Conference on Learning Rep-
resentations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021. [OpenReview.net](http://openreview.net/), 2021a. URL
https://openreview.net/forum?id=m5Qsh0kBQG.
- Pierre-Alexandre Kamienny, St´ephane d’Ascoli, Guillaume Lample, and Franc¸ois Charton. End-to-
end symbolic regression with transformers. arXiv preprint arXiv:2204.10532, 2022.
- Subham Sahoo, Christoph Lampert, and Georg Martius. Learning equations for extrapolation and
control. In International Conference on Machine Learning, pp. 4442–4450. PMLR, 2018. URL
http://proceedings.mlr.press/v80/sahoo18a.html.
- Luca Biggio, Tommaso Bendinelli, Alexander Neitz, Aurelien Lucchi, and Giambattista Parascan-
dolo. Neural symbolic regression that scales. In International Conference on Machine Learning,
pp. 936–945. PMLR, 2021.
- Mikel Landajuela, Brenden K Petersen, Sookyung Kim, Claudio P Santiago, Ruben Glatt, Nathan
Mundhenk, Jacob F Pettit, and Daniel Faissol. Discovering symbolic policies with deep rein-
forcement learning. In Marina Meila and Tong Zhang (eds.), Proceedings of the 38th International
Conference on Machine Learning, volume 139 of Proceedings of Machine Learning Research, pp.
5979–5989. PMLR, 18–24 Jul 2021c. URL https://proceedings.mlr.press/v139/
landajuela21a.html.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
As opposed to de-coupling the discrete and continuous representations, the authors concatenate the two of these are use autoregressive methods for optimization. The approach is applied to a toy problem in symbolic regression and reinforcement learning for decision trees.

### Strengths
The combination of discrete and continuous representations is an important direction for research, with the neuro-symbolic community making a lot of progress and several application domains of interest, including symbolic regression, combinatorial optimization, and symbolic distillation. The pedagogical example is an intuitive way to demonstrate the utility of the approach.

### Weaknesses
The concatenation of discrete and continuous variables into a single vector and the higher-level approach are very straightforward and their novelty seems limited. The method's core idea of combining discrete and continuous representations, while relevant, lacks a clear demonstration of significant advancement over existing techniques. Specifically, the paper does not adequately address the challenges associated with optimizing in a hybrid space beyond the basic concatenation, such as the potential for interference between the discrete and continuous components during optimization. The approach seems to be a direct application of autoregressive models to a concatenated space, without introducing any novel mechanisms for handling the inherent differences between discrete and continuous variables. This raises concerns about the method's ability to scale to more complex problems where the interplay between discrete and continuous variables is more intricate.

### Questions
Why are you comparing your method against the baselines you define as opposed to using baselines from the literature in the case of symbolic regression (Figure 3)? (For decision trees, baselines from the literature are used). Given recent work on neuro-symbolic regression, the authors should compare against methods in the literature.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a method for using reinforcement learning to train a model that outputs a sequence of both discrete and corresponding continuous values. The goal here is to tackle problems that involve predicting an object that has both discrete and continuous values such as a decision tree with selection of branching feature as well as the corresponding threshold, or producing a symbolic regression expression which is a combination of selected functions and constants. Their approach jointly produces both discrete symbol and a corresponding continuous value as opposed to previous work which focused on generating discrete backbones and then found the continuous values for the fixed skeleton. They evaluate their approach empirically by comparing against baselines that handle discrete and continuous decisions independently, as well as baselines from the literature for symbolic regression and interpretable RL (identifying a decision tree for solving simple RL problems). They demonstrate improved performance over previous approaches both in terms of solution quality, as well as in the efficiency as they require fewer calls to the evaluation metric to train their approach since the continuous variables don’t need to be optimized separately.

### Strengths
The main strength of the proposed approach is the empirical performance seems to be much better than previous approaches for solving optimization over hybrid discrete and continuous spaces. The results seem to indicate substantial improvement from the given model, and the evaluation is done on both symbolic regression and interpretable RL which are quite diverse domains. Furthermore, the approach itself may have broader impact for other settings in hybrid design spaces, and in identifying interpretable machine learning models.

### Weaknesses
Some of the small weaknesses here are in the motivation of the approach as well as tackling problems which require solutions that are more heavily constrained.
The approach is partially motivated by the idea that jointly generating the discrete and continuous objects makes the reward more aligned with the solution itself rather than approaches which generate the discrete backbone and then optimize the continuous variables after the fact. However, it seems that this approach also may have misleading rewards for the skeleton or continuous solution if neither are optimal. It may shy away from high quality discrete solutions even though there may be one setting of continuous variables which are highly performant.
It is also unclear how this approach may work on more complicated discrete-continuous settings where the feasible region may be more complex such as in solving mixed integer linear programming, or in other cases where the continuous space may be more decoupled from the discrete space such as in cases where there are many continuous decisions that need to be made but not all of them have a corresponding discrete decision.
Another small limitation is that it would be helpful to see the applicability of this approach on more tasks that have hybrid domains such as real world use cases of symbolic regression.

### Questions
How does this method avoid the issue of poor or misleading rewards for the right discrete skeleton? It might be the case that the continuous predictions are incorrect while the skeleton is correct.

Is it possible to generate continuous decisions that are unrelated to discrete decisions and thus uncoupled?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
DisCo-DSO is a novel approach for optimizing in hybrid discrete-continuous spaces. It uses a generative model to jointly optimize discrete and continuous variables, leading to improved performance and efficiency, especially in complex optimization tasks like interpretable reinforcement learning with decision trees.

### Strengths
I believe that research focusing on effectively exploring solutions while considering the impact of discrete and continuous variables on the objective function has its significance. This study proposes research that optimizes both discrete and continuous variables simultaneously, extending the conventional method of constructing solutions used in AI-based combinatorial optimization research to a continuous approach.

### Weaknesses
I believe there are various approaches to solving optimization problems that involve a mix of continuous and discrete variables. Instead of merely extending the existing modeling structure, I don't consider optimizing both discrete and continuous variables simultaneously as a significant contribution in itself. Research that effectively explores solutions while considering the impact of discrete and continuous variables on the objective function holds its own merit. This study, by proposing optimization of both discrete and continuous variables simultaneously and expanding the traditional approach used in AI-based combinatorial optimization research to a continuous one, may need to offer more than just an extension of the existing modeling structure to make a substantial contribution.

### Questions
1. I'm having difficulty understanding why an autoregressive policy structure is necessary for generating solutions to optimization problems involving a mix of continuous and discrete variables. While sequential structures are commonly used in reinforcement learning for combinatorial optimization problems to effectively learn policies for arbitrary problems, this study appears to be focusing on optimizing a specific given problem. In such a case, wouldn't it be more efficient to explore the entire solution space rather than constructing solutions sequentially?

2. How is the order for selecting optimization variables determined, and does this order have the potential to affect the performance?

3. Mixed Integer Programming (MIP) is a well-known class of optimization problems that involve optimizing both discrete and continuous variables, and many studies attempt to optimize MIPs using deep learning. How does this research differ from those studies involving MIPs?

4. The experimental content seems limited. While three types of problems are presented, the first problem only compares the number of function evaluations, and the second problem presents curves indicating the improvement in solutions for a specific problem. It would be beneficial to solve a more diverse set of problems and provide statistical evidence to validate the performance.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
