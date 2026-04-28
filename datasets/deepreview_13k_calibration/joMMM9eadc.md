# Effective Generation of Feasible Solutions for Integer Programming via Guided Diffusion

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Feasible solutions are crucial for Integer Programming (IP) since they can substantially speed up the solving process. In many applications, similar IP instances often exhibit similar structures and shared solution distributions, which can be potentially modeled by deep learning methods. Unfortunately, existing deep-learning-based algorithms, such as Neural Diving \citep{nair2020solving} and Predict-and-search framework \citep{han2023a}, are limited to generating only partial feasible solutions, and they must rely on solvers like SCIP and Gurobi to complete the solutions for a given IP problem. In this paper, we propose a novel framework that generates \emph{complete} feasible solutions \emph{end-to-end}. Our framework leverages contrastive learning to characterize the relationship between IP instances and solutions, and learns latent embeddings for both IP instances and their solutions. Further, the framework employs diffusion models to learn the distribution of solution embeddings conditioned on IP representations, with a dedicated guided sampling strategy that accounts for both constraints and objectives. We empirically evaluate our framework on four typical datasets of IP problems, and show that it effectively generates complete feasible solutions with a high probability (> 89.7 \%) without the reliance of Solvers and the quality of solutions is comparable to the best heuristic solutions from Gurobi. Furthermore, by integrating our method's sampled partial solutions with the CompleteSol heuristic from SCIP \citep{maher2017scip}, the resulting feasible solutions outperform those from state-of-the-art methods across all datasets,  exhibiting a 3.7 to 33.7\% improvement in the gap to optimal values, and maintaining a feasible ratio of over 99.7\% for all datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a learning based IP solver. For problem and solution embedding, the solver took the GCN framework, combined with contrastive learning inspired by CLIP. In addition the authors adapted DDPM/DDIM by introducing IP specific guidance into the sampling procedure. Experiments on several IP problems showed superior performance to both Neural Diving and SCIP.

### Strengths
Several key components were designed to make the solver specifically effective for IP. Experiments are solid.

### Weaknesses
To better validate that the quality of the proposed solver, comparison between the found optimal objective value and the ground-truth (global optimum) would be more convincing, the paper only provided relative comparison between the proposed solver and two baseline approaches.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

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
A solution generation method is adopted to estimate binary solutions of integer programming. The method includes a contrastive learning  gaining initial representations of solutions and instances, and a conditioned generative model estimating binary solutions. Guided sampling is adapted from present diffusion models to increase the feasibility ratio.

### Strengths
Applying cutting-edge deep learning to solve integer programming problems is encouraging. This research focuses on generating feasible solutions by generative model and borrows the powerful representation learning capability of neural networks. The method is technically sound by simply applying contrastive learning and diffusion model for solution estimation.

### Weaknesses
My first concern is the insufficient comparison in experiments. As described in related work, considerable literature attempted to improve the diving method in solvers. Except Neural Diving (Nair et al., 2020), many follow-up works continue similar research topics. More recent methods should be compared. Even by only comparing Neural Diving, the results are not enough. The training time and resource usage are not clear, which is important to show practicality and efficiency of applying multiple deep neural networks in the proposed method. Moreover, the functions of contrastive model and generative model are not showcased by ablation study.

Many works apply deep learning methods to solve integer programming problems with totally feasible solutions. To name a few, "A general large neighborhood search framework for solving integer linear programs", "Learning large neighborhood search policy for integer programming", "Mip-gnn: A data-driven framework for guiding combinatorial solvers". The advantage of this research over this line of works is not clear. The use case of the given method is not given. Many descriptions are not well explained (see questions).

### Questions
1. Why SCIP is chosen in experiments but not Gurobi, given the fact that Gurobi often performs better than SCIP. 
2. GCN is described by "It does not explicitly incorporate objective and constraint information during sampling, often resulting in infeasible complete solutions." In Gasse et al. (2019), GCN always gains feasible solutions.
3. Any integer programming problem can be converted into a 0-1 programming. But the conversion increases the number of constraints a lot. How large integer programming can the method solve?
4. What is the advantage of contrastive learning compared to supervised learning? Additional experiment should be provided to see the effect of contrastive learning without labeled solutions

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel framework that generates complete feasible solutions end-to-end (i.e., assigning all variables using neural networks) for Integer Programming (IP) problems, in contrast to most prior works that generate partial solutions (i.e., only assigning a subset of variables using neural networks).
Specifically, it proposes a contrastive learning approach to capture the relationship between the IP instances and the solutions, a diffusion model to generate solution embeddings, and a guided sampling strategy to enhance the feasibility and quality of solutions.
Experiments on four datasets show that the proposed method outperforms previous state-of-the-art methods in terms of feasible ratio and objective value.

### Strengths
1.	This work is well motivated and the paper is easy to follow.
2.	While most previous methods can only generate partial solutions, this work represents a valuable attempt to an end-to-end framework to generate complete feasible solution.
3.	Experiments demonstrate the effectiveness of the proposed method.

	a)	Experiments on four datasets demonstrate the effectiveness of the proposed methods compared with Neural Diving and SCIP in terms of feasible ratio and objective value.

	b)	The scalability test demonstrates that the proposed method can generalize to large instances.

	c)	The ablation study demonstrates the effectiveness of the IP guidance.

	d)	The authors also conduct hyperparameter tuning experiments to investigate the effect of the gradient scale $s$ and the leverage factor $\gamma$.

### Weaknesses
1.	The authors may want to add [1] as a baseline.
2.	The prediction loss defined in Eq. (3) empirically performs better than that from general diffusion models. It would be better to provide some intuitive interpretation. Moreover, the authors may want to provide the inference algorithm of the modified diffusion model.
3.	As diffusion generative models may suffer from inefficiency in both training and inference, the authors may want to report the training and inference time.

### Questions
1.	Is this work the first one to generate complete solutions? 
2.	See Weakness 2. The training loss defined in Eq. (3) is different from general diffusion models. Does it cause a different inference algorithm?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of finding feasible solutions to integer programming problems. The authors propose a novel framework that generates complete feasible solutions end-to-end. Their framework learns the embeddings for IP instances and their solutions and then uses diffusion models to learn the distributions. Finally, they perform sampling with trained models.

Key results: From their experimental results, it appears that their sampling methods provide solutions with a higher proportion of which are feasible solutions and have smaller objectives than our approaches.
Trained on small-size datasets, their models are able to scale to large-scale instances.

### Strengths
1. From their experimental results, it appears that their sampling methods provide solutions with a higher proportion of which are feasible solutions and have smaller objectives than our approaches.
2. Trained on small-size datasets, their models are able to scale to large-scale instances.

### Weaknesses
Major comments:

1.	“For SCIP, we adopt the first solution obtained through non-trivial heuristic algorithms during the solving phase.” I don’t know whether this comparison is fair. Did you try, for example, using the solutions they get within a fixed window of time? It's crucial to understand how the heuristic solutions from SCIP compare when given a similar computational budget, rather than just the first solution found. The current comparison might not reflect the true potential of SCIP's heuristic search capabilities.

2.	Why do you compare your algorithm mostly with SCIP instead of Gurobi which is possibly a much better solver. Gurobi is often considered a state-of-the-art commercial solver, and a comparison against it would provide a more robust benchmark for the proposed method. The choice of SCIP as the primary baseline needs further justification, especially considering the availability of more powerful solvers.

3.	How does the objective value that you sampled compare to the optimal solution? How close are they? If they are far from each other, having a high feasible ratio does not mean anything. The feasible region increases exponentially, so there could be a large number of feasible solutions that are far from the optimal solution. It's essential to quantify the quality of the feasible solutions generated, not just their feasibility. A high feasibility ratio is meaningless if the solutions are significantly suboptimal. A comparison to the optimal solution or a known lower bound is necessary to assess the practical value of the proposed approach.

Minor comments:

1.	In “Related work”, you mentioned “our method aims to learn the latent structure …, without any reliance on the IP solver.”, but you still need to complete partial solutions use Completesol heuristic from SCIP. This reliance on SCIP's heuristic for completing partial solutions contradicts the claim of not relying on IP solvers. This needs clarification, as it suggests a hybrid approach rather than a completely solver-free method.

2.	In page 8, the first paragraph, you mentioned “the coverage is set to 0.1 and 0.2 due to the difficulty in finding feasible partial solutions when C > 0.2.”. What do you mean by difficulty? Does it mean that you cannot find any feasible partial solutions within 30 generated solutions? The term 'difficulty' is vague. It's important to specify the exact issue encountered when C > 0.2. Does it mean that the sampling process fails to generate any feasible partial solutions within a given number of attempts, and if so, what is that number?

3.	Is it possible to generate repeated solutions so that the performance is not improving?
Possible typoes: Page 3 last paragraph: DDIM then

### Questions
Combined in the "Weaknesses"

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
