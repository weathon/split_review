# Unleashing the Potential of Fractional Calculus in Graph Neural Networks with FROND

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
We introduce the FRactional-Order graph Neural Dynamical network (FROND), a new continuous graph neural network (GNN) framework. Unlike traditional continuous GNNs that rely on integer-order differential equations, FROND employs the Caputo fractional derivative to leverage the non-local properties of fractional calculus. This approach enables the capture of long-term dependencies in feature updates, moving beyond the Markovian update mechanisms in conventional integer-order models and offering enhanced capabilities in graph representation learning. 
We offer an interpretation of the node feature updating process in FROND from a non-Markovian random walk perspective when the feature updating is particularly governed by a diffusion process.
We demonstrate analytically that oversmoothing can be mitigated in this setting.
Experimentally, we validate the FROND framework by comparing the fractional adaptations of various established integer-order continuous GNNs, demonstrating their consistently improved performance and underscoring the framework's potential as an effective extension to enhance traditional continuous GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a fractional variation for graph diffusion methods and its derivative methods. The author provides numerical solutions, theoretical support, and experimental data to support their claim that fractional variation performs better than vanilla graph diffusion methods.

### Strengths
- The method is novel and is a good direction for exploring graph neural diffusion methods.
- The paper is detailed and easy to read
- The paper has extensive comparisons between methods
- The paper answers the question about its computation cost with detailed experiments in appendix.

Overall, this paper is an updated version of a paper I've reviewed before. The authors have answered all my questions in this version. I think this paper starts from a nice idea and contains all the details required, so I would recommend acceptance.

### Weaknesses
N/A

### Questions
N/A

### Soundness
3 good

### Presentation
4 excellent

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
FROND is a method that uses concepts from fractional calculus applied to GNNs. 
The method is based on defining the Caputo derivative and a solver that integrates the ODE. 
The authors provide ample theory and several experiments to show the benefit of adding the fractional derivative component to GNNs.

### Strengths
1. The paper is well written. It was easy to follow and understand.

2. The authors show how the proposed method can encapsulate existing models such as GRAND or GraphCON.

3. The experiments show that adding a fractional derivative is useful.

### Weaknesses
1. Missing neural ODE literature: 'Stable Architectures for Deep Neural Networks' and 'A Proposal on Machine Learning via Dynamical Systems'.

2. Missing graph ODE literature: recent papers like 'Anti-Symmetric DGN: a stable architecture for Deep Graph Networks' and 'Ordinary differential equations on graph networks'.

3. In one of the main contributions, it is said that "We provide an interpretation from the perspective of a non-Markovian graph random walk when the model feature-updating dynamics is inspired by the fractional heat diffusion process. Contrasting with the traditional Markovian random walk implicit in traditional graph neural diffusion models whose convergence to the stationary equilibrium is exponentially swift, we establish that in FROND, convergence follows an algebraic rate.". Why is it true? if $\beta=2$ then the process is not diffusive at all. Rather, it is oscillatory, as shown in GraphCON (Rusch et al.)

4. In section 2.3, the authors should also discuss FLODE ('A Fractional Graph Laplacian Approach to Oversmoothing') which is very similar to this work and also uses fractional calculus.

5. In section 3.1 the authors discuss the initial conditions of the ODE. It is not clear to me how do you initialize $\beta$ time steps. From the text I can infer that it is the same condition as the input features. Is that was was actually done? If so, does it make sense from an ODE perspective? Have the authors tried other initialization procedures?

6. The authors mention that here only $\beta$ is only considered between 0 and 1. I wonder why. How would your model behave theoretically and practically if it larger than 1?

7. I am not sure it is correct that the model can have global or 'full path' properties if $\beta$ is smaller than 1. For example, I think it is fair to say that if $beta$ is indeed smaller than 1, then a second order process as in GraphCON cannot be represented by the model. 

8. The experiments indeed show that the proposed method improves compared to baselines produced by the authors, but they are quite narrow and show a partial picture of the current state of the art and existing methods. I would expect that the authors compare their work (experimentally) with other methods like FLODE, CDE, GRAND++, as well as other recent methods like ACMII-GCN++ ('Is Heterophily A Real Nightmare For Graph Neural Networks To Do Node Classification?') or DRew ('DRew: Dynamically Rewired Message Passing with Delay').

9. The authors state that the proposed method can be applied to any ordinary differential equation GNN, so can the authors please also show the results when applied to other baseline methods as discussed in the paper?

10. $\beta$ is a hyperparameter. What would happen if you learn it? how will it influence the results and the stability of your solver? Is there a principles way to choosing the hyperparameter?

11. I am not certain that the method is novel, as it was also shown in 'Fractional Graph Convolutional Networks (FGCN) for Semi-Supervised Learning'.

12. Missing literature about skip connections in GNNs: 'Understanding convolution on graphs via energies'.

13. A general point - the focus of the paper is the mitigation of oversmoothing. But, also as the authors state, there are many methods that already do it. Then my question is what is the added value of using this mechanism ? Also, another important issue is oversquashing in graphs. Can the authors discuss how and if would the proposed method can help with that issue?

### Questions
I left questions in the review and I am looking forward to seeing the author's response.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends the graph neural ODE framework by allowing fractional (Caputo) derivatives in the time variable. By leveraging on global information in the fractional derivatives, the authors prove a slow mixing theorem that prevents oversmoothing of node features. Experimentally, the authors demonstrate this fractional calculus framework over different graph ODE models and show they achieve good performances.

### Strengths
Novelty: To the best of my knowledge, this is the first approach to directly generalize graph neural ODE to fractional derivatives and demonstrate its applicability in real-world datasets.

Flexibility: The framework is general enough to be incorporated to a wide range of existing graph neural ODE in the literature, such as GRAND, GRAND++, GREAD, etc.

Experiments: Empirical study conducted is extensive and results are explained comprehensively. Showing competitiveness of the new framework over existing ones in many different dimensions.

### Weaknesses
I have not studied the appendix closely so it is possible that some of these questions are addressed there. 

It is not immediately clear how this current approach quantitatively/qualitatively compares to existing approaches that exploit long-range memory in the modeling process, for instance Maskey et al. 2023 (see question 1).

Due to the long-range memory information, I believe it is expected that this approach is more computationally heavy than traditional neural graph ODE. It would be more complete to have a discussion of this increased cost, if there are any, as well as techniques used to overcome it. This is crucial in scaling the approach to larger datasets. 

I am very willing to raise my score if these issues are addressed sufficiently.

### Questions
Is it possible to get a clearer distinction between the approach of this work, which is modeling node feature evolution through the layers as a FDE, versus Maskey et al. 2023, which proposes using fractional graph Laplacian in the usual ODE framework. It appears that Maskey et al. 2023 approach also tackles oversmoothing via long-range dependency of the dynamics, which is the main theoretical justification of the current work as well. More specifically, are there simple examples in which one framework strictly encapsulates another? Most importantly, what is the advantage of using this framework over Maskey et al. 2023 framework? 

I understand fast mixing of graph random walk results of Chung 1997 and its dependence on various factors, such as eigenvalues of the adjacency/Laplacian. However, it is not immediately clear to me that the same fast rate carries over to graph neural ODE (which has some kind of skip connection across depths). Can this be explained more thoroughly?

Is it possible to give a proof sketch/intuition of Theorem 2, in particular, why should we expect the slow algebraic rate? It is also interesting that the rate is tight. Following the proof in the appendix seems to suggest that this come from a deeper result by Mainardi but there is not a lot of intuition there.

Minor issues:
M1: F(s) in equation (1) is not defined (I assume it is the Laplace transform of f). The variable s is also not defined (I assume it is the variable of the transformed function). 
M2: There should also be conditions under which the Laplace transform exists (and the Laplace transform of the derivative)

---
After the rebuttal phase, the authors have addressed my concerns and I am raising my score to an 8.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Fractional-Order graph Neural Dynamical network (FROND), a novel learning framework that enhances traditional graph neural ordinary differential equation (ODE) models by integrating the time-fractional Caputo derivative. This incorporation allows FROND to capture long-term memories in feature updating due to the non-local nature of fractional calculus, addressing the limitation of Markovian updates in existing graph neural ODE models and promising improved graph representation learning.

### Strengths
1. The paper is well-written, providing a clear and straightforward presentation of the content, which enhances the overall readability.

2. The innovative integration of time-fractional derivatives into traditional graph ODEs is a novel approach that effectively addresses key issues like non-local interactions and over-smoothing.

3. The proposal is supported by theoretical motivations.

4. An extensive evaluation of the framework is presented, demonstrating its effectiveness and versatility across various settings and providing substantial empirical evidence of its performance.

### Weaknesses
The correlation between beta and fractal dimemsion is not clear.  For instance, despite Pubmed having a higher fractal dimension of 2.25 compared to Airport, the optimal beta for it is set at 0.9. This observation raises curiosity about the specific conditions or types of datasets under which FROND demonstrates significant performance improvements. Clarification on this matter would greatly enhance the reader’s understanding and application of FROND in various contexts.

To further highlight the strengths of FROND and to provide clearer guidance on its optimal application scenarios, I would recommend conducting additional evaluations on datasets that necessitate long-range interactions[1]. 

The content in section 3.3 offers valuable insights, and I believe it could be enriched with additional technical details and formulations related to the graph layer. This enhancement would aid readers in developing a more comprehensive and profound understanding of the model.


Drawing a more explicit connection between fractal characteristics and FROND’s efficacy, particularly in handling tree-like data, would contribute to a more coherent narrative and justification for the framework. I kindly suggest expanding on this aspect.


[1]Dwivedi, Vijay Prakash, et al. "Long range graph benchmark." Advances in Neural Information Processing Systems 35 (2022): 22326-22340.

### Questions
What is the computational complexity of FROND? What is the T chosen for each experiment? and how is the short memory principle applied?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
