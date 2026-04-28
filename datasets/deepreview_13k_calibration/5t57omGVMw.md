# Learning to Relax: Setting Solver Parameters Across a Sequence of Linear System Instances

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
vspace{-1.5mm}
	Solving a linear system $\*A\*x=\*b$ is a fundamental scientific computing primitive for which numerous solvers and preconditioners have been developed. 
	These come with parameters whose optimal values depend on the system being solved and are often impossible or too expensive to identify;
	thus in practice sub-optimal heuristics are used.
	We consider the common setting in which many related linear systems need to be solved, e.g. during a single numerical simulation.
	In this scenario, can we sequentially choose parameters that attain a near-optimal overall number of iterations, without extra matrix computations?
	We answer in the affirmative for Successive Over-Relaxation~(SOR), a standard solver whose parameter $\omega$ has a strong impact on its runtime.
	For this method, we prove that a bandit online learning algorithm---using only the number of iterations as feedback---can select parameters for a sequence of instances such that the overall cost approaches that of the best fixed $\omega$ as the sequence length increases.
	Furthermore, when given additional structural information, we show that a {\em contextual} bandit method asymptotically achieves the performance of the {\em instance-optimal} policy, which selects the best $\omega$ for each instance.
	Our work provides the first learning-theoretic treatment of high-precision linear system solvers and the first end-to-end guarantees for data-driven scientific computing, demonstrating theoretically the potential to speed up numerical methods using well-understood learning algorithms.\looseness-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers an online parameter optimization problem for sequentially solving linear system equations with a specific iterative algorithm (SOR) with a parameter.  The goal is formulated as a regret minimization where each cost per trial is defined as the number of iterations with the parameter at the trial. The critical observation is that the cost is further upper bounded by a convex surrogate function and analyzed under the online convex optimization framework.

### Strengths
The problem is well-motivated (even though the algorithm looks slightly restrictive). The critical observation is that the SOR iteration is bounded by a convex surrogate function with the parameter. The observation is non-trivial and thus the paper shows a new and interesting application of the online convex optimization framework.

### Weaknesses
Maybe a weakness of the paper is that the reduction to OCO is restricted to a certain type of algorithm (SOR) only so far. But I do not think the weakness is not so crucial since it shows, to the best of my knowledge, a new application of numerical optimization from OCO.

### Questions
Is it possible to extend this framework to other algorithms for solving linear equations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This a paper about learning a good choice of a parameter of a linear system solver in an online (bandit-like) fashion. The goal is to minimize the number of iterations (and, as a consequence, the running time) of the solver. The paper is theoretical in nature – the authors prove regret bounds; simple proof-of-principle-style experiments serve only a complementary role.

The solver of choice for the paper is Successive Over-Relaxation (SOR). It is not the most widely used in practice solver nowadays, but it has some uses, and it has the advantage of being simple and easy to analyse. The authors mention extending their theory to more complex solver as an important direction of future research.

SOR is an iterative solver, and it has a single parameter, denoted by omega. The authors study the following setting: a sequence of linear systems is solved one by one. Before we start solving each system we can pick a value of omega, and after the system is solved we only learn for how many iterations the solver was running.

The authors propose to use Tsallis-INF bandit algorithm (a variant of more popular Exp3) to learn the parameter omega. The challenge lies in analysis – the number of iterations as a function of the parameter is non-Lipschitz. Instead, the authors use a continuous surrogate upper bound on the number of iterations, which they claim is reasonably tight. Unfortunately, this means they can only prove that the surrogate cost of their algorithm is close (up to a sublinear regret) to optimal surrogate cost (not the real cost, which might be much smaller) for a fixed parameter chosen in hindsight.

The second setting studied is in the spirit of contextual bandits. The authors assume all coefficient matrices are the same up to a linear shift of the diagonal. They show that under this assumption it is possible to obtain sublinear regret with respect to best choice of the parameter for each value of the shift separately. Since for a fixed shift there is a fixed optimal parameter, it means that the benchmark is just the optimal unconstrained choice of parameter. This is a very strong result (though only under a strong assumption about input, and still about the surrogate cost).

Finally, the authors also study a setting where target vectors (but not coefficient matrices) are drawn from a distribution, and in this setting they are able to show sublinear regret bounds using the actual (not the surrogate) cost of the algorithm.

### Strengths
The setting studied is very natural and this paper can easily stimulate further research in the area.

The algorithm used is a standard one, so the proposed approach seems more practical than if it was an ad-hoc algorithm designed specifically so that the analysis works.

The paper is nicely written – the authors explain why they do certain things instead of just presenting proofs out of the blue.

It seems that the technical content is novel and nontrivial – though I do not know the area well enough to be certain about that.

### Weaknesses
The results are either about the surrogate loss, or under the assumption that part of the input is stochastic and not adversarial. This significantly limits the practical applicability of the theoretical results. The surrogate loss, while claimed to be reasonably tight, is not the actual cost of the algorithm, and it's unclear how much the performance on the surrogate translates to the actual performance. The stochastic input assumption, while allowing for stronger results, is also quite restrictive, as it does not cover the more general adversarial setting that is often encountered in practice. The fact that the analysis relies on a continuous surrogate for a discontinuous function is also a concern, as it introduces an approximation that may not always be accurate.

Experiments are very basic. While the paper is positioned as a theory paper, the lack of more comprehensive experiments is a weakness. The experiments do not explore the performance of the proposed algorithm on real-world data or compare it against existing practical methods. The experiments also do not explore the sensitivity of the algorithm to different parameters or the impact of the surrogate loss on the actual performance. It would be beneficial to see experiments on larger scale problems and with more realistic data to better understand the practical implications of the theoretical results.

It is not clear whether the limitations imposed (surrogate loss or stochastic input) are necessary to prove sublinear regret bounds. The authors do not provide a strong argument for why these assumptions are needed, and it would be beneficial to see a more detailed discussion of the challenges in proving sublinear regret bounds without these assumptions. It is also unclear why the analysis cannot be extended to more general settings, and what are the fundamental obstacles that prevent this generalization. The lack of a clear understanding of the necessity of these assumptions makes it difficult to assess the true limitations of the proposed approach.

### Questions
Do you have any (even soft) argument that the limitations imposed (surrogate loss or stochastic input) are necessary to prove sublinear regret bounds?

It seems that learning optimal parameters for iterative methods (LP solvers, linear systems solvers, GD, etc.) should be similar and explainable with a single theory. Do you have any understanding why it does not seem to be the case, and we have separate results for each of these methods?

How your work compares to what people do in practice? Is it clear why they are not using similar methods? Would it be feasible to compare empirical performance of your approach to what is already done in practice?

Minor remarks:

Abstract: "we prove that a bandit algorithm (...) can select parameters (...) such that the overall cost is almost as good as that the best fixed \omega would have obtained" – this sentence is technically not true, you prove it only for the surrogate upper bound and not for the actual cost

Page 2: "ir" -> "it", "in-addition" -> "in addition"

Page 4: "known scalars c_t" – I'm not sure what "known" means here; even if the scalars are not given explicitly, they can be trivially inferred from the input.

Page 4: please remind the reader that rho denotes the spectral radius – it might be clear for optimization people but not necessarily for learning people.

Page 14: ",e.g." -> ", e.g."

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study different settings of sequentially solving a series of (related) linear systems using Successive-Over-Relaxation (SOR). The problem is that the runtime/number of iterations of SOR highly depends on the "relaxation parameter" $\omega$, so the challenge is to learn online good choices of $\omega$. They look at two settings. First, a deterministic setting where we assume the instances are close enough to the "asymptotic regime" where the convergence rate of SOR decreases linearly with respect to the spectral radius of a specific problem-dependent matrix. The second setting we assume the target vector is randomly sampled from what we can think as a truncated Gaussian distribution. In both cases, they show how bandit algorithms can be used to pick parameters $\omega$ online that work well on average. Furthermore, they show how to use contextual bandits in the case when we have more structured information about the linear systems we need to solve.

### Strengths
- This is a paper with a very solid contribution on data-driven algorithm design (and a few interesting technical bits for adversarial badits), with interesting new ideas applied to a simple but interesting problem, and I believe will likely lead to interesting follow-up work.

    More specifically, generalizing bandits algorithms in the adversarial setting for functions that are not exactly Lipschitz continuous for the use in algorithms with predictions/data-driven algorithm design is very interesting and seems to work quite well. The extension to the use of Contextual Bandit algorithms when we are looking at a series of systems with shifted diagonals is interesting, and how we can exploit the stochastic case and skip the use of a surrogate function at all are quite interesting.
    
    Even if some of the bounds do not seem to lead to very informative regret guarantees, it seems to be full of interesting technical ideas and does a good job of showing what are the difficulties of controlling the dependency of problem-parameters in these regret bounds.
    
- As the authors themselves mention, this is an interesting case where they designed algorithms of two related lines of work (algorithms with predictions and data-driven algorithm design)

- The authors are very careful to not over-sell their contributions: caveats and weaknesses are often immediately mentioned and discussed, together with a summary of these drawbacks at the conclusions sections;
- The presentation is not perfect, but very good considering how much ground the authors cover in 9 pages. I believe this paper covered a lot of ground, and after skimming a few parts of the appendix it does seem to be very thorough
- Although it is in the appendix due to space limitations, I really enjoyed reading the related work section since I lack the background in linear system solvers and the related literature;

### Weaknesses
 - As mentioned by the authors, some of performance guarantees seem to be very loose (mainly the ones in section 3 with the dependency on dimension); specifically, the regret bounds in Section 3 exhibit a polynomial dependence on the dimension $n$, which is not ideal for practical applications where $n$ can be large. Ideally, one would hope for logarithmic or at most linear dependence on $n$. The high-order polynomial dependence (e.g., $n^4$) on spectral quantities in the bounds is also a concern, as this can lead to very large regret even for moderately ill-conditioned matrices.
- I am more acquainted with the online learning and optimization literature, and probably did not have enough background to judge how good some of the bounds were (mainly, the dependency on problem parameters in Thm 2.2 and 2.3). Although this is a problem with my lack of background, I believe the authors could add a bit of discussion of what would be "ideal" (?) dependencies here; for instance, it would be helpful to clarify what are the typical dependencies on spectral properties that are usually achieved in similar contexts, and what are the main challenges in achieving better bounds in this specific setting. The current discussion leaves the reader without a clear understanding of the gap between the obtained results and the state-of-the-art.
- It seems to be that having stochastic target vectors with independent entries is a very strong assumption. The authors acknowledge that assuming the vectors come from a (scaled and somewhat truncated) Gaussian is restrictive, but it was not clear if mild correlation between the entries (positive definite correlation matrix with small off-diagonal entries?) would make the analysis break down; the assumption of independent entries is quite strong and might not hold in many practical scenarios. It would be beneficial to discuss how the analysis would be affected by introducing some correlation between the entries of the target vector, and if there are any known techniques to handle such dependencies. Moreover, it is not clear how sensitive the results are to the specific choice of the truncated Gaussian distribution, and if similar results could be obtained with other distributions.
- Although the experiments are not the focus of the paper, I do believe they are a bit too simplistic. I do no think the authors should spend time coming up with more experiments, but I think that discussing the limitations of the experiments would be helpful; the experiments are performed on relatively small-scale problems and do not fully capture the challenges of real-world applications. It would be useful to discuss the limitations of the experimental setup and how the results might generalize to more complex scenarios, and what are the main challenges in scaling up the experiments.

### Questions
- A few times the authors mention that they provide "end-to-end" guarantees, but I am not sure if I can parse what you mean by this. Could your briefly mention that do you mean by this? 
- If the authors have time, could you expand a bit on the poor dependency on the spectral properties of the instances in theorem 2.3 (and maybe 2.2)? The authors mention that these dependencies are not ideal, but I do not have enough context to know what are dependencies that would be more "acceptable";
- On the assumption on $b_t$'s in sec 3, is it really necessary for the entries to be independent of each other? Moreover, how much do you depend on $b_t$'s being exactly the distribution you have? I probably could answer this questions myself if I had the time to go carefully over the proofs, but if the authors could briefly comment on this, it would be great;

### Suggestions
- The discussion on "asymptocity" in sec 2.2 is very unclear. At some point I think I understood more or less what you meant, but this is a very confusing part early on in the paper, and there is not enough context to interpret the plot. Maybe this is more of a note, but if you could expand on this in a revised version of the paper, it would be great.
- In Theorem 2.1 you cite "Lemma 2.1.2" to mean item 2 of Lemma 2.1, which is a bit weird since this is easily misunderstood as a separate lemma (that does not exist);
- Although I mentioned about one of the plots in Fig 2 before, I think all of the plots in Fig 2 need more context. It is not clear to me what the middle plot is trying to show, and the last plot is great but I only managed to understand that all of the algorithms there were algorithms proposed in the paper by the end of the paper. So when I first read this plot I was very confused;

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper establishes learnability result for the overrelaxation parameter in SOR method. Online learning algorithm and regret bounds are analyzed for solving a sequence of linear systems.

### Strengths
The paper theoretically justifies that algorithm parameter in linear system solving is learnable. Online algorithm with provable regret guarantees is given. The context setup and analysis are novel to my knowledge.

### Weaknesses
The paper adopts an upperbound surrogate loss function. Although this is reasonable due to the hardness in characterizing instance-specific convergence behavior of iterative methods, this still results in a potential gap between theory and practice. Specifically, the surrogate loss may not accurately reflect the true convergence rate of the SOR method for a given linear system, and the learned parameter might not be optimal in practice. Furthermore, the analysis relies on bounding the spectral radius of the iteration matrix, which can be a loose bound, especially for ill-conditioned matrices. This could lead to a learned overrelaxation parameter that is overly conservative.

The paper focuses on online learning algorithms. In practice, this may still be inefficient in the exploration phase, as the algorithm needs to try different overrelaxation parameters to learn the optimal one. This exploration could be costly, especially if the linear systems are large and require significant computational resources to solve. The regret bounds, while theoretically sound, might not be tight enough to guarantee practical efficiency in the early stages of the online learning process. 

The paper assumes iterative methods start from scratch. This is a simplification, as in many practical applications, when solving a sequence of linear systems that are potentially from the same distribution, a common practice is to warm-start with previous solutions. This warm-starting often speeds up convergence significantly. The analysis does not account for the potential benefits of warm-starting, which could lead to a discrepancy between the theoretical results and practical performance.

### Questions
1. This paper focuses on online learning algorithms. In practice this may still be inefficient in the exploration phase. Is it possible to adopt a static learning model and prove learnability result using tools from statistical learning theory? (e.g., train a classifier/regressor to predict the best $\omega$)
2. The paper assumes iterative methods start from scratch. When solving a sequence of linear systems that are potentially from the same distribution, a common practice is to warm-start with previous solutions, and it often speeds up convergence. Is it possible also to incorporate this into your analysis?

**Minor typos and stylistic issues**

1. Page 14

   guarantes => guarantees

2. Page 26 

   folloows => follows

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
