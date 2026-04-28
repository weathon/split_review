# Enhancing Offline Reinforcement Learning with an Optimal Supported Dataset

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 8, 6, 5, 5, 3

## Abstract
Offline Reinforcement Learning (Offline RL) is challenged by distributional shift and value overestimation, which often leads to poor performance. To address this issue, a popular class of methods use behavior regularization to constrain the learned policy to stay close to the behavior policy. However, this approach can be too limiting when the  behavior policy is suboptimal. To overcome this limitation, we propose to conduct behavior regularization directly on an optimal supported dataset, which can both ensure that the learned policy is not too far removed from the dataset, and reduce any potential  bias towards the optimization objective. We introduce \textit{\textbf{O}ptimal \textbf{S}upported \textbf{D}ataset generation via Stationary \textbf{DI}stribution \textbf{C}orrection \textbf{E}stimation} (OSD-DICE) to generate such a dataset. OSD-DICE is based on the primal-dual formulation of linear programming for RL. It uses a single minimization objective  to avoid  poor convergence issues often associated with this formulation, and incorporates two key designs to ensure polynomial sample complexity under general function approximation and single-policy concentrability.  After generating the near-optimal supported dataset, we instantiate our framework by two representative behavior regularization-based methods and show safe policy improvement over the near-optimal supported policy. Empirical results validate the efficacy of OSD-DICE on tabular tasks and demonstrate remarkable performance gains of the proposed framework on  D4RL benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author introduces a method for reweighting datasets to optimize the behavior policy in behavior-regularized offline Reinforcement Learning (RL) for enhanced performance. The effectiveness of behavior-regularized offline RL algorithms is contingent on the behavior policy that accumulates the dataset. A prevalence of low-return trajectories in the behavior policy’s collected data results in diminished performance of the offline RL algorithms. The proposed method modifies the behavior policy by adjusting the dataset weights, employing the density importance correction estimation (DiCE) technique to optimize these weights, thereby enhancing the performance of the behavior policy. Experimental outcomes indicate performance enhancements in several D4RL offline RL datasets.

### Strengths
- The proposed method is well-motivated, and using DiCE for weighting data is new.
- The theoretical results are encouraged.

### Weaknesses
 - Lack of baselines and related works discussion. Re-weighting offline RL training objectives or optimizing the dataset has been studied in prior works [1, 2, 3, 4]. However, the author didn't discuss and compare with them. Without comparing with these works, it would be difficult to answer the significance of this work.
- Implementation details of the baselines are not presented. The results of Table 1 look pretty similar to the official codebase of AW/RW. However, it should be noted that the official codebase of AW/RW uses offline RL hyperparameters (e.g., the regularization weight of CQL) different than Sun 2023. It's necessary to set those offline RL's hyperparameters to be the same for fair comparison. It'd be great if the author can upload their baseline implementation and scripts to reproduce experiments.
- Hyperparameter search results of baselines are not presented even though the author claims that the baselines' hyperparameters are also optimized.
- The baseline scores in Table 1 don't have a standard deviation.
- Performance improvement is limited, except for maze2d. From Table 1, OSD doesn't show a significant performance gain in MuJoCo tasks. Checking Lee et al. (2021), we see that their method also performs the best in maze2d but underperforms or match the baselines in others. But, the author doesn't compare Lee et al. (2021) in Table 1, which makes the contribution of OSD-RL unclear.
- OSD-RL requires training two additional models, which increases the run time. The author should compare the run time (wallclock time) with the baselines. For this method to be impactful, the increased runtime should be proportional to their performance gain.

### Questions
- What's the difference between OptiDiCE + SquareReg and OSD-DiCE?
- It would strengthen the paper's impact if the author could show the performance in all D4RL datasets, Atari domains, and potentially the imbalanced datasets proposed in AW/RW paper.
- I encourage the author to upload the source code and the scripts to reproduce the experiments as D4RL experiments shouldn't take long time to run.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new approach to improve offline RL by addressing the distributional shift and value overestimation issues that degrade policy performance. The core contribution is Optimal Supported Dataset generation via Stationary DIstribution Correction Estimation (OSD-DICE), a method that formulates the generation of an optimal supported dataset through a refined primal-dual linear programming process. This approach simplifies the optimization to a single minimization objective, avoiding the instability of traditional methods, and is theoretically robust, offering polynomial sample complexity with general function approximation and single-policy concentrability.

To validate their approach, the authors incorporate the generated dataset into two behavior regularization methods—Behavior Cloning (BC) and Conservative Q-Learning (CQL)—creating osd-BC and osd-CQL. They demonstrate that these methods achieve safe policy improvement and enhanced performance on D4RL benchmarks. The experiments confirm the efficacy of OSD-DICE and suggest that using an optimal supported dataset can substantially benefit offline RL tasks.

### Strengths
- Theoretical analysis: The OSD-DICE framework presents a theoretically sound approach, advancing the field with its single minimization objective that resolves the complexity and instability issues found in traditional primal-dual optimization methods for optimal support dataset methods.

- Empirical results: The paper supports its theoretical claims with robust empirical evidence, demonstrating significant performance improvements on well-established D4RL benchmarks, which suggests the method's practical effectiveness in offline RL tasks.

### Weaknesses
The presentation of Equation (3) lacks an intuitive explanation. The paper would benefit from a clearer exposition of this optimization problem, helping readers better grasp its significance within the OSD-DICE framework and enhancing overall accessibility.

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The contribution of this paper is two-fold:
- Proposes an algorithm called OSD-DICE that learns a model and adopt a squared regularization for w for better convexity. There is some theoretical backups for the regularization. In finite MDP experiment, the improvement over OptiDICE is shown.
- Proposes a dataset resampling algorithm based on BC and CQL is introduced using the weight optimized from OSD-DICE, and shows the improvement over baseline offline RL algorithms in D4RL environments.

### Strengths
- Strong theoretical analyses on OSD-DICE.
- Shows much improvement in experiments. OSD-DICE shows improvement over OptiDICE with its corrections. In D4RL experiment, it is shown that CQL can be benefit from OSD-DICE based importance sampling.

### Weaknesses
 - OSD-DICE requires additional learning of a model compared to OptiDICE, and it is not certain whether the performance improvement over OptiDICE is worth learning a model in complex domains. For finite domains, while the squared regularization seems to improve a lot, but using a model for unbiased estimator does not seem to improve much. It is counterintuitive as model learning makes the estimator unbiased, while squared regularization does not change the optimal solution (in theory).
- While OSD-DICE seems to be an improved version of OptiDICE, in the importanced sampled RL part, the proposed algorithms are not compared against OptiDICE-based algorithms. This makes two contributions of the paper to feel very separated.


### Questions
- As far as I understood, the additional regularization allows us to make the problem well defined even for 0 like $\alpha$, as it offers additional convexity. But shouldn't the optimal solution be the same? What's the main reason that the adoption of regularization can improve from OptiDICE in finite MDP? we should be able to optimize to the optimal solution in finite MDPs, so the solution should stay the same?
- Among two contributions of this paper (1. OSD-DICE against OptiDICE, 2. OSD-DICE based importance sampled offline RL), the second one seems to be very similar to that of [1]. Does the proposed method perform better than [1]?

[1] Beyond Uniform Sampling: Offline Reinforcement Learning with Imbalanced Datasets

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to address the limitation of suboptimal datasets for offline reinforcement learning within the framework of DIstribution Correction Estimation (DICE) algorithm. Specifically, this paper proposes Optimal Supported Dataset generation via Stationary DICE (OSD-DICE) method to learn the density ratio for the regeneration of near-optimal dataset. Like prior OptiDICE, the proposed method also adopts a single minimization objective, and incorporates two designs (adding strong convexity terms and learning transition model for the objective) for better optimization and sample complexity.

### Strengths
1. Sufficient theoretical analysis of the proposed method;
2. The idea of the proposed method is general and can be extended to other similar offline RL methods.

### Weaknesses
1. Lack the sufficient comparison with current SOTA offline RL algorithm, such as, EDAC, IQL, RORL, or it's worth considering combing this learned near-optimal dataset with these SOTA algorithms;
2. Compared with original OptiDICE, the main innovations of this paper focus on two design, but it rarely explains and verifies what key problems these designs can solve.
3. The proposed two improvements lacks sufficient novety, adding strong convexity regularization term (last term in e.q.3) is a popular trick in this type of methods.

### Questions
1. It's better to supplement more comparison with current SOTA offline RL methods;
2. It's said that, when estimating the Bellman error $e_\nu$, this paper explicitly considers the transition probability of the next state which is believed to bypass the bias issue. Would you please make it more clear why the original single-transition estimation suffers from the bias issue? In my opinion, this estimation is based on Monte Carlo sampling and hence being unbiased but have high variance. Besides, introducing an extra approximate transition probability fucntion $\hat{P}$ doesn't seems reliable to address the bias issue - how can you ensure the accuracy of the model?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with the distribution shift problem in offline reinforcement learning through the lens of optimal supported dataset. 

Classical methods rely on behavior regularization to constrain the learned policy close to the behavior policy induced by the offline dataset. Such methods have limitations when the behavior policy is sub-optimal. The paper proposes to overcome this drawback by constructing an optimal supported dataset, which can then be used for offline learning via classical regularization-based methods.

The paper starts from the linear programming formulation for MDPs, with the density ratio being a variable. After learning the optimal density ratio, the original dataset can be reweighted. The problem is that a minimax problem is computationally hard to solve. Thus this paper introduces a relaxation and reduces the problem into a single minimization problem. 

Furthermore, optimality guarantee is given thanks to the MLE of the transition model and convexity of the objective function brought by an added squared regularization term. Experimental results on RL benchmark D4RL confirms the efficacy of the proposed method.

### Strengths
**Significance**: this paper studies the distribution shift problem in offline reinforcement learning, which is an important problem. Furthermore, this paper looks at this problem from the lens of an optimal behavioral dataset, which seems an interesting angle. 

**Originality**: this paper contains some original ideas.

### Weaknesses
1. **Presentation**:

$(i)$ In LaTex, please use \citet and \citep properly.

$(ii)$ there are some questions not throughly addressed in the paper, which left me very interested. I leave them to the **Questions** session.

2. **Clarity**:

$(i)$ the writing of this paper has a huge room for improvement. It is a bit hard to read. I suggest the authors use tools like ChatGPT to refine the wording. Furthermore, the overall presentation requires a major refinement. Equations like (3) are hard for the readers to interpret if it is just put there without proper elaboration. For example, one possible way is to split eq. 3 into several terms with a notation for each term, and then explain the motivation for each term separately.

$(ii)$ I was a bit confused by the definition of $f$ when I first read the paper. Is it a function class (from Alg.1 line 1) or f-divergence (eq.1)? Things like this need to be defined more clearly.

**Overall**, I think a major modification is necessary for the current manuscript.

### Questions
1. The paper claimed that it has computational advantage compared to previous works. However, it seems that solving eq2 requires computation of quantities of MLE. How can this be efficient in cases other than tabular MDPs? 

2. Please elaborate on why the added regularization term does not change the optimality. Is bring convexity to the objective function the only purpose of the regularization term?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work follows the weight approach in offline RL, proposes a new algorithm to find the optimal weight, and further uses the weight to re-weight the dataset, and find the optimal policy.

### Strengths
The approach proposed is shown to find a well-behaved policy, with theoretical proofs. The experiment results also verify the capability to find a goo policy.

### Weaknesses
1. The writing of this paper should be improved. There are some of the notations that are not pre-defined, which make it hard to read this paper. For example, what is $\mathcal{V}$ in Assumption 1? What is $\mathcal{D_m}$ in page 4? Why does the learner have access to this additional dataset to learn $\hat{P}$? What is $d^*_\alpha$ in (4)? These undefined notations make the paper difficult to understand.
2. There are too many assumptions made to imply the results, which are hard to verify. Also, some justifications should be made regrading these assumptions. For example, how do you verify Assumption 5? In Thm6, some additional assumptions are made. How do you justify those?
3. The sample complexity in Remark 9 is $O(\epsilon^{-4})$, which is much greater than the previous typical results for offline RL, i.e., $O(\epsilon^{-2})$. Why is the result worse than the previous ones?
4. The idea of using weight technique is not new. The importance weight technique has been used in RL for a long time, even in the offline RL setting. What is the novelty of this work?

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
