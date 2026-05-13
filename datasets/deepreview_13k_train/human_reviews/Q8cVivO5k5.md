# Large-Batch, Iteration-Efficient Neural Bayesian Design Optimization

- Decision: Reject
- Scores: 3, 6, 5, 8

## Abstract
Bayesian optimization (BO) provides a powerful framework for optimizing black-box, expensive-to-evaluate functions. 
It is therefore an attractive tool for engineering design problems, typically involving multiple objectives.  
Thanks to the rapid advances in fabrication and measurement methods as well as parallel computing infrastructure, evaluating many design engineering problems can be heavily parallelized. 
This class of problems challenges BO with an unprecedented setup where it has to deal with very large batches, shifting its focus from sample efficiency to iteration efficiency. 
We present a novel Bayesian optimization framework specifically tailored to address these limitations. 
Our key contribution is a highly scalable, sample-based acquisition function that performs a non-dominated sorting of not only the objectives but also their associated uncertainties.  
We show that our acquisition function, in combination with different Bayesian neural network surrogates, is highly effective in extremely large-batch regimes with a minimal number of iterations. 
We demonstrate the superiority of our method by comparing it with state-of-the-art multi-objective optimizations.
We perform our evaluation on two real-world problems - airfoil design and 3D printing - showcasing the applicability and efficiency of our approach

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method to perform multi-objective BO with the large-batch setting. It proposes to use a Bayesian Neural Network (BNN) created by Deep Ensembles as a surrogate model. It also proposes an NSGA-II based acquisition function that is claimed to be able to scale to large-batch setting better than current acquisition functions. The main idea for the proposed acquisition function (2MD acquisition function) is to simultaneously maximize the predicted objectives and the associated uncertainties, both are given by the BNN surrogate model.

The method (LBN-MOBO) is evaluated on synthetic functions (1 in the main paper and 4 in the appendix), and 2 real-world problems.

### Strengths
- The paper tackles an important problem which is performing multi-objective BO with the large-batch setting.
- The paper proposes an acquisition function for applying large-batch when performing BO while the current acquisition functions (qEHVI, qParEGO, qNEHVI) struggle, in terms of computation time. The concept of the proposed acquisition function is intuitive: it seems to further encourage explorative behavior, because it also maximizes the uncertainties in the surrogate model.

### Weaknesses
 - Some technical details are not described clearly, making it sometimes hard to catch the main idea of the paper. For example, the formal problem statement is not described, the proposed method makes use of only epistemic uncertainty but the concept of epistemic uncertainty is not explained in the Background. The organization of the paper is sometimes a bit confused, for example, the overall process of BO should not be placed in method section.
- The use of BNN as the surrogate model to enhance the performance is surely promising, however, BNN has many problems. For example, the tuning of its hyperparameters could be another optimization problem or the uncertainty provided by the BNNs could be inaccurate. However, these problems are not discussed in the paper. Furthermore, I don't understand why the proposed method only requires the epistemic uncertainty. There are no motivation, explanation, or insights about this choice and why it work.
- The proposed acquisition function of optimizing both the prediction and the uncertainty and the usage of NSGA-II to optimize this acquisition function seems to be not too novel for me. The idea is very similar to UCB. There are no deep analysis regarding this proposed acquisition function and why it will work well.
- The experimental evaluation is very limited. It doesn't compare against other baselines in the main paper. In Section 5.1, it is not convincing to choose the surrogate model (inference method) by using only 1 synthetic experimental result. 
- Related works should mention other types of surrogate models apart from GP and BNN, such as TPE and RF. And also, it is worth mentioning why BNN is preferred over these models.
- Section 4.1 only covers the modification for Deep Ensembles method. It is not clear how to apply the modification for other inference methods (SGHMC, HMC, DKL, IBNN), so as to compare in Figure 3. 

Minor:
- Authors should use \citep{} and \citet{} separately when citing the references.

### Questions
Apart from my comments in the Weaknesses section, the authors can answer the following questions:
- The concept of the 2MD acquisition function is quite similar to Upper Confidence Bound with a specific exploration factor. It seems that in UCB, both the prediction and the uncertainty are incorporated to compute the acquisition function, while 2MD use the two values as separate objective to optimize. Can the authors point out some differences between the UCB and 2MD?
- In Figure 1, why there is no surrogate SGHMC, HCM, Deep Ensembles paired with qNEHVI and qParEGO. How many function evaluations in total for this experiment?
- Is batch size b > 1000 a normal batch size in real-world problem? There seems to be no reference to any applications using such large batch.
- The two real-world problems use b=15,000 for airfoil problem and b=20,000 for printer problem, on a total of 10 iterations. With such a large number of function evaluations (150,000 and 200,000), can LBN-MOBO outperform Evolutionary Computation methods, e.g., MOEA/D, NSGA-II? These two EC methods are quite powerful for solving multi-objective optimization problems.

[1] B. Paria, K. Kandasamy, and B. Póczos. A flexible framework for multi-objective Bayesian optimization using random scalarizations. In Proceedings of The 35th Uncertainty in Artificial Intelligence Conference, volume 115, 2020

[2] Daulton, Samuel, David Eriksson, Maximilian Balandat, and Eytan Bakshy. "Multi-objective bayesian optimization over high-dimensional search spaces." In Uncertainty in Artificial Intelligence, pp. 507-517. PMLR, 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the problem of designing Bayesian optimization algorithms for the setting of large batches of evaluations in order to optimize a black-box function. An acquisition function is constructed as multiobjective optimization over multiple predictive mean and uncertainty functions modeled by a deep ensemble. Experiments are performed on two real-world benchmarks.

### Strengths
- The paper considers an important problem relevant to real-world applications in engineering design.

- I especially like the real world evaluation on two interesting benchmarks: airfoil design and 3D printing. It would be an interesting contribution to the BO community if they are released in the open-source code. 

- The idea is simple and works well on the benchmarks.

### Weaknesses
 - Although I like the simplicity of the approach, the reasoning behind choosing this instantiation of multiobjective optimization is not entirely clear. Please considering some more analysis about the principles behind the proposed acquisition function. 

- Some relevant related work that can be useful to discuss in the paper:
	- A very similar idea utilizing multiobjective acquisition function with predicted mean and variance as objectives. 

	[1] Gupta, S., Shilton, A., Rana, S., & Venkatesh, S. (2018, March). Exploiting strategy-space diversity for batch Bayesian optimization. In International conference on artificial intelligence and statistics (pp. 538-547). PMLR.
	- There has been a bunch of work on making thompson sampling work for large batch sizes in both continuous and combinatorial design spaces. 

	[2] Hernández-Lobato, J. M., Requeima, J., Pyzer-Knapp, E. O., & Aspuru-Guzik, A. (2017, July). Parallel and distributed Thompson sampling for large-scale accelerated exploration of chemical space. In International conference on machine learning (pp. 1470-1479). PMLR.

	[3] Deshwal, A., Belakaria, S., & Doppa, J. R. (2021, May). Mercer features for efficient combinatorial Bayesian optimization. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 35, No. 8, pp. 7210-7218).

	[4] Vakili, S., Moss, H., Artemev, A., Dutordoir, V., & Picheny, V. (2021). Scalable Thompson sampling using sparse Gaussian process models. Advances in neural information processing systems, 34, 5631-5643.

- Probably a nit, but I think calling deep ensembles as a bayesian neural network is not entirely correct.

### Questions
Please see weaknesses section above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a setting in which BO is applied to solve black-box optimization problems where there are multiple objectives and a query is expensive, but the batch size can be extremely large. To address this challenge, the authors propose an acquisition function that is more scalable and takes into account the uncertainty of candidates. Empirically, this BO algorithm is applied to solve two realistic black-box optimization problems in this setting.

### Strengths
1.	The paper considers a novel black-box optimization setting where there are multiple objectives and the batch size can be very large. The authors empirically observe that contemporary multi-objective batch acquisition functions do not scale well with respect to the batch size.
2.	To solve this issue, the authors propose a modified version of Deep Ensembles to approximate BNN and an acquisition function to maximize both predicted objectives and the uncertainty measure.

### Weaknesses
1.	Contribution is not enough. The innovation of the paper can be summarized into a new predictive model with a minor modification on the original Deep Ensembles model and a new multi-objective batch acquisition function. For the predictive model, the reason for modifying the uncertainty measurement part from aleatory noise to epistemic noise is unclear. Also, the benefit from this change is not verified in the paper. Moreover, the novelty of 2$\textit{M}$D acquisition compared to the other acquisition functions is not clear either, except for being more scalable.
2.	The empirical results presented are somewhat unconvincing. The reason why the authors choose deep ensembles as a surrogate to test in the two subsequent realistic tasks is that its runtime is shorter and achieves higher hypervolume. However, since this appears in only one experiment, its generalized performances to other tasks are not necessarily better than other surrogates. 
3.	More benchmark models should be considered in the two realistic tasks. In these two tasks, only two models are considered, i.e., modified deep ensemble + 2$\textit{M}$D and dropout + 2$\textit{M}$D. Therefore, whether the modified deep ensemble + 2MD indeed performs well enough is not clear. It would be great if the authors can also consider more models as benchmarks.
4.	Limited theory is developed for this new BO method.

### Questions
1.	How is the “time” defined in Figures 1 and 3? 
2.	How well does the modified deep ensemble quantify uncertainty, compared to the original deep ensemble?
3.	How does 2MD work? It looks like a key ingredient of the new acquisition is the NSGA-II. However, this is not explained in the main body of the paper. Also, how to implement the acquisition function, one of the most important parts in this paper, is not clearly explained. The only relevant statement is the last three lines in page 6. 
4.	In reality, the magnitude or the range of $F$ is usually unknown. How do the authors suggest to balance the tradeoff between the output of the predictive model and the uncertainty?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a Multi objective optimisation algorithm with a focus on large batch sizes (up to 1000s of points) and few iterations (as low as 10).

Given an objective functions $f:\mathcal{X}\to \mathbb{R}^M$ where $\mathcal{X}\subset \mathbb{R}^d$,  the method is a Bayesian model based algorithm, they propose to use Bayesian neural networks as the surrogate model to predict $\underline{y}=\hat{f}(x)$ as well as the epistemic uncertainty $Var(\hat{f(x)})$, these models which can scale to large dataset sizes much more effectively than the more traditional Gaussian processes.

In order to determine a new batch of points to be evaluated, the authors propose to concatenate the model predictions and uncertainties $[\hat{f(x)}, Var(\hat{f}(x))] \in \mathbb{R}^{2M}$, which can then be fed into NSGA-II, a popular evolutionary aglgorithm, which can find the set of pareto optimal points $x_1,...,x_B\in \mathcal{X}$ that form the pareto front in the augmented output space $\mathbb{R}^{2M}$. In other words, these are point that are predicted to have high value and/or high uncertainty.

The authors perform experiments with a range of off-the-shelf Bayesian neural network methods and determine Deep Ensembles to be the best candidate surrogate model.

### Strengths
- Simplicty, elegance.
  - Bayesian neural networks have become a work horse surrogate model in the Bayesian Optimization community in recent years
  - NSGA-II is a very popular well established mainstream algorithm in the multi objective community
  - concatenating predictions and uncertainties to be fed into NSGA-II seems a very reasonable good idea
  - altogether the method avoids introducing any sophisticated new engineering, and instead opts to intelligently combine established components from the community with some well justified tweaks.

- clearly written, I enjoyed the exposition of related work.

- Section 5.4, running algorithm without using uncertainties I felt was a very nice experiment and cleawrly demonstrated their benefit.

### Weaknesses
I only have minor comments

- I see the authors discuss this in Appendix E but MOO is an very large field and I would be very surprised if batch construction by finding the pareto front of concatenated predictions and uncertainties has not been considered before, (it _seems_ so obvious!), 
- upon first reading, I felt the title was somewhat cluttered.

### Questions
- presumably for small use cases, optimising 2 simple objectives over 2 dimensions batchsize 2, i.e. the ideal use case for any GP-BO, the proposed method would suffer, is there a crossover from where more simple GP-BO methods fail and LBN-MOBO would be best?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
