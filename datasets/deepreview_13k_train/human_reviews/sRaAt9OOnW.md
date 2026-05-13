# Uncovering Challenges of Solving the Continuous Gromov-Wasserstein Problem

- Decision: Reject
- Scores: 6, 5, 6, 8, 6

## Abstract
\vspace{-3mm}
Recently, the Gromov-Wasserstein Optimal Transport (GWOT) problem has attracted the special attention of the ML community. In this problem, given two distributions supported on two (possibly different) spaces, one has to find the most isometric map between them. In the discrete variant of GWOT, the task is to learn an assignment between given discrete sets of points. In the more advanced continuous formulation, one aims at recovering a parametric mapping between unknown continuous distributions based on i.i.d. samples derived from them. The clear geometrical intuition behind the GWOT makes it a natural choice for several practical use cases, giving rise to a number of proposed solvers. Some of them claim to solve the continuous version of the problem. At the same time, GWOT is notoriously hard, both theoretically and numerically. Moreover, all existing continuous GWOT solvers still heavily rely on discrete techniques. Natural questions arise: to what extent existing methods unravel GWOT problem, what difficulties they encounter, and under which conditions they are successful. Our benchmark paper is an attempt to answer these questions. We specifically focus on the continuous GWOT as the most interesting and debatable setup. We crash-test existing continuous GWOT approaches on different scenarios, carefully record and analyze the obtained results, and identify issues. Our findings experimentally testify that the scientific community is still missing a reliable continuous GWOT solver, which necessitates further research efforts. As the first step in this direction, we propose a new continuous GWOT method which does not rely on discrete techniques and partially solves some of the problems of the competitors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper discusses the challenges of solving the Continuous Gromov-Wasserstein Optimal Transport (GWOT) problem and emphasizes the need for a reliable and general-purpose method to address these issues. The authors claim that current solvers rely on discrete methods and struggle when dealing with uncorrelated data. They then introduce NeuralGW, which is claimed as a method that does not depend on discrete approximations and can therefore handle realistic scenarios with uncorrelated data. However, their method is unstable and requires a large amount of data for training.

### Strengths
- Analysis of existing GWOT solvers.
- Fill a gap in GWOT literature by questioning the assumptions under which existing solvers operate.
- Proposed partial solution for defined issues.

### Weaknesses
 - `Diversity`: The evaluation focuses on the GloVe dataset and the biological dataset. It's better to expand experiments to cover additional domains.
- ~The paper still has some issues that need to be addressed in order to support its claims~
- Lack of experiment setup details.

### Questions
- Given the high data requirements of NeuralGW's adversarial optimization, would you consider alternate training methods or adaptations to improve performance on smaller datasets? Further clarification on the trade-offs between data size and performance stability would also be insightful.
- Would it be possible to see an empirical or theoretical comparison between NeuralGW and other continuous GWOT methods, particularly on tasks where preserving intra-domain structure is less critical?
- Line 311, indices from the target are incorrect.
- Why were Top k-accuracy, cosine similarity, and FOSCTTM chosen for evaluation?

### Soundness
2

### Presentation
3

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
This paper studies the problem of solving the Gromov-Wasserstein (GW) problem numerically. It is shown, in particular, that the case where two datasets are sampled i.i.d. from distributions are particularly challenging for currently available methods.The paper also proposes a neural network-based solver which, in experiments, is seen to outperform other standard methods in the case that correlation between paired training samples is low.

### Strengths
The paper accurately identifies a deficiency in certain GW solvers related to training based on paired samples. The proposed neural network-based GW solver appears to be a reasonable way of dealing with this issue as evidenced by the numerical experiments.

### Weaknesses
I believe the findings of this paper are not very surprising. Indeed, many of the methods in the paper explicitly assume the setting of paired samples. Furthermore, the GW problem is, in general a computationally hard problem due to its nonconvexity.

Other than the above empirical observation, the paper does not present many results. Indeed, Lemma 5.1 and Theorem 5.2 are well-known in the literature; these are the only theoretical results provided. As such, the proposed neural approach is not coupled with any guarantees, I believe this severely limits the impact of this paper.

Finally, the numerical experiments are interesting, but are not very conclusive. Indeed, only one experiment is provided. On a related note, half of the methods to which the approach is being compared are labelled as "other methods" in the graphs; this is quite baffling to me and should be rectified.

### Questions
1. The authors state that some of the methods are trained on 3K samples whereas their method is trained on 200K samples. While it is acknowledged that this yields an unfair comparison, the difference is a consequence of the poor scaling of the other solvers. This begs the question of why experiments on a smaller scale were not performed to compare the methods fairly. 

2. It appears that the neural entropic Gromov-Wasserstein solver from T. Wang and Z. Goldfeld, Neural Entropic Gromov-Wasserstein Alignment, arXiv, 2023. would serve as a good method to compare to as no structure is assumed on the data generating process.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to study the continuous Gromov-Wasserstein (GW) problem, i.e. focusing on the scenario when discrete GW solver may not be scalable or not generate to unseen data. Specifically the paper discusses the applicability of GW to various tasks where a latently matched dataset is in place or not, resulting in different performance. The paper then proposes an algorithm with min/max/min formulation that solves the GWOT problem that is compatible with large scale data and does not rely on discrete GW solvers, thus mitigating the aforementioned issues.

### Strengths
The paper points out some issues that have been largely dismissed in the OT and GW community. First the discrete GW solver, when only having access to small batches of datasets that does not have a priori good matching but does have one on a large scale, could have inhomogeneous performance and could be hard to generalize (one such existing attempt is unbalanced GW). Another insight is on the apparent scalability of typical GW solvers, which makes the application of neural networks convincing. The experiments seem thorough, comparing several existing computational method of GW.

### Weaknesses
1. Soundness of the theoretical claims:
A major concern is on the main theorems (5.1, 5.2). These results use standard duality and reformulations that involve the optimal Monge map, but the existence is never justified. In particular, it is well known that GW or inner product GW does not necessarily have optimal map, i.e. the minimum may not be achieved [1]. Same for the existence of the optimal potential, see [2]. Thus the claims mostly only serve as heuristics, as theorem 5.2 is solely on characterization of the optimal map. More need to be discussion regarding why parametrizing by neural network is valid when the optimum may not be achieved.


2. Discussion of existing methods and novelty of the proposed algorithm: 
The paper claims to be the first in a comprehensive discussion of continuous GW, and the proposed statistical correlatedness is novel. However the paper is missing many discussions on related works. Most of the paper's missing claims on existence and regularity of Gromov-Monge map have been studied in [1],[3],[4]. The statistics question in section 1 " transition from the discrete to the continuous setup may be questionable from a statistical point of view" is discussed in [2]. Neural network based GW solvers have appeared in [5],[6], both claiming similar applicability to large scale data as mentioned in this paper. The existence of a discrete Gromov-Monge map is first shown in [7]. Detailed discussions on related methods should be added to further strengthen the proposed benchmark.


3. A minor comment on the presentation of Section 4: the paper made several claims about discrete GW problems, ranging from practical statistical assumptions to computational difficulties, but it is not entirely lucid what the main issue is: is it the learned map through extrapolation not generalizing, or the sample complexity is bad, or the optimization is harder with uncorrelated data? The argument could be strengthened with discussions on its relation to other classical learning concepts like generalization error, statistical sample complexity, optimization complexity etc.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper considers the continuous GWOT problem and presents a min-max optimization approach as a solution.
The authors focus on two main problems in the paper:
- establishing deficiencies in the existing solvers. In particular, the focus of this discussion is on the quality (or correlatedness) of training samples.
- proposing a solver that addresses the above-mentioned deficiencies by utilizing the smoothness of the underlying distributions.

The paper is well-written and clear. Moreover, the authors established the motivation for the problem and the scope of the study well. The results presented within are clear and concise. 

Having said that, I have the following comments. 
- This work seems to be one of the first to address this problem in a continuous setting. Thus, comparative studies are difficult, and hence, the significance of the work is hard to gauge.
- Moreover, the proposed method performs well in some aspects and poorly in others when compared to existing solvers. Hence, although the insight into the drawbacks of other solvers and the subsequent solution are interesting, I am uncertain if the results are important enough to recommend an acceptance strongly.

### Strengths
- The results seem consistent (or unaffected) by the correlatedness of the source and target samples. This is a significant advantage as the data preprocessing burden is reduced.
- Moreover, this method is proposed for continuous GWOT problems, which other solvers currently do not handle.

### Weaknesses
Based on my understanding, the following could be considered limitations of this approach:
- Since the method is exclusively for the continuous GWOT problem, the approach presented here would not be helpful in applications where a discrete measure makes better sense. 
- As the authors themselves identified, the method requires large datasets for training, and in general, the results seem to be sensitive to optimization parameters and training data variation.

### Questions
- I think the Toy 3D->2D problem section needs better explanation. I was quite lost when trying to understand the objective of the experiment or what was being done. Were the mixed Gaussian distributions in the 3D and 2D spaces the same? What do the colors in the plot represent? It might be better to move this part to the appendix because this step merely seems to be a way to validate the implementation of various solvers.
- Not much discussion or insight is present into the reason behind the performance seen in the simulation. What is the reason behind the better performance of NeuralGW when the source and target samples are uncorrelated? Does the smoothness of the underlying distributions affect the variance seen in repetitions? 
- Is there some way to quantify the algorithm's sensitivity to the optimization parameters?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is an attempt to answer the promising question of solving continuous Gromov-Wasserstein Optimal Transport (GWOT) problem. The authors crash-test existing continuous GWOT approaches on different scenarios, carefully record and analyze the obtained results, and identify issues. Their findings experimentally testify that the scientific community is still missing a reliable continuous GWOT
solver, which necessitates further research efforts. As the first step in this direction, the authors propose a neural continuous GWOT method which does not rely on discrete techniques. Their method is based on the key observation that the reformulation of dual continuous GWOT problem can be solved as a min-max-min optimization problem. By simply parameterization with neural networks, the authors use the alternating stochastic gradient ascent/descent/ascent method to train their parameters. The empirical performance is encouraging.

### Strengths
The paper conducts a deep analysis of existing papers and reveal that one important characteristic that may greatly affect practical performance is the considered data setup. By following these findings, the authors evaluate the performance of existing continuous GWOT solvers in more statistically fair and practically realistic uncorrelated data setups. To alleviate the dependence on the mutual statistical characteristics of the source and target training data, a continuous neural GW solver was proposed and performed well in practice.

### Weaknesses
1. The findings of this paper are interesting and reveal that the empirical success of the existing GWOT solvers seems to be a bit
over-estimated and requires to be treated more critically. However, the interpretation is not thorough. Does this limitation only come from that all existing continuous GWOT solvers heavily rely on discrete techniques?

2. Your continuous neural GW solver is insightful. Could you provide some theoretical guarantee? I do not think the complexity analysis is necessary but at least your method needs to be guaranteed to converge under certain condition.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2
