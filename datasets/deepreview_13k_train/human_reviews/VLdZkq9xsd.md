# Multiple-Frequencies Population-Based Training

- Decision: Reject
- Scores: 3, 8, 6

## Abstract
Reinforcement Learning's high sensitivity to hyperparameters is a source of instability and inefficiency, creating significant challenges for practitioners. Hyperparameter Optimization (HPO) algorithms have been developed to address this issue, among them Population-Based Training (PBT) stands out for its ability to generate hyperparameters schedules instead of fixed configurations. PBT trains a population of agents, each with its own hyperparameters, frequently ranking them and replacing the worst performers with mutations of the best agents. These intermediate selection steps can cause PBT to focus on short-term improvements, leading it to get stuck in local optima and eventually fall behind vanilla Random Search over longer timescales. This paper studies how this greediness issue is connected to the choice of *evolution frequency*, the rate at which the selection is done. We propose Multiple-Frequencies Population-Based Training (MF-PBT), a novel HPO algorithm that addresses greediness by employing sub-populations, each evolving at distinct frequencies. MF-PBT introduces a migration process to transfer information between sub-populations, with an asymmetric design to balance short and long-term optimization. Extensive experiments on the Brax suite demonstrate that MF-PBT improves sample efficiency and long-term performance, even without tuning hyperparameters. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Multiple-Frequencies Population-Based Training (MF-PBT), a hyperparameter optimization algorithm addressing the greediness issue in PBT. By employing sub-populations that evolve at different frequencies and an asymmetric migration process, MF-PBT aims to balance short-term and long-term optimization. Experiments on the RL locomotion tasks demonstrate that MF-PBT improves sample efficiency and long-term performance, even without tuning hyperparameters.

### Strengths
1. The idea of using multiple frequencies to mitigate PBT’s greediness is innovative and addresses a significant limitation in existing methods.
2.  The asymmetric migration process is a practical solution that could be applied to other population-based methods to improve their performance such as PB2.

### Weaknesses
1. All experiments were conducted on several locomotion tasks within the reinforcement learning context, which I believe is unacceptable. HPO has too many application scenarios, and I strongly recommend increasing the variety, such as the experiments in PB2 and PB2-Mix.

2. Other HPO methods (such as Bayesian optimization, e.g.,[1-2] ) are also recommended for comparison. Their experiments are also should be considered to run.

### Questions
None.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Multiple Frequency Population Based Training (MF-PBT), a novel evolutionary algorithm for hyperparameter optimization. The method allows different individuals in the population to evolve at different frequencies, rather than having all individuals update at the same rate. The authors demonstrate that performing parameter migration without hyperparameter migration helps avoid hyperparameter collapse, a common issue in standard PBT approaches.

### Strengths
1. Novel and well-motivated idea of having multiple evolutionary frequencies within a population, the issue of hyperparameter sensitvity in Reinforcement Learning is well known and the paper makes a good attempt at addressing it.
2. Strong empirical validation showing benefits over standard PBT and a smart use of random search to make sure greediness is avoided
3. Important insight about separating parameter and hyperparameter migration to prevent collapse are substantiated and that is a useful understanding for the community 
4. Fits well into existing literature on evolutionary dynamics in population-based RL methods
5. Motivated and detailed experimental setup and ablation studies

### Weaknesses
## Major Weaknesses
1. The evaluation and definition of "anytime performance" would benefit from formalization increasing the notion's rigor. Specifically, it's unclear whether the observed better early performance is consistently maintained throughout training or if it's merely an initial advantage. The paper should clarify if "anytime performance" refers to consistently superior performance at all training stages or simply faster initial learning. A more rigorous definition, perhaps relating to the integral of the performance curve or a comparison to the best performance found so far, would be beneficial.
2. Current results don't fully demonstrate if better early performance is due to high-frequency evolution or other factors such as good performance in the beginnings of training. It's possible that the high-frequency agents are simply lucky in their initial hyperparameter assignments, leading to a head start that is not necessarily due to the frequency of evolution itself. A more controlled experiment, perhaps with randomized initial hyperparameters across different frequencies, would help isolate the effect of frequency.
3. Limited exploration of different frequency spreads and not given enough weight in the main results (only two tested in supplementary section which are important to explore). The paper only briefly touches on the impact of different frequency spreads, and the main results focus on a single spread. A more comprehensive analysis of various frequency distributions, including both uniform and non-uniform spreads, is needed to fully understand the method's sensitivity to this parameter.
4. Not clear if the findings generalize beyond PPO. The paper's experiments are limited to PPO, and it's unclear whether the benefits of MF-PBT would extend to other reinforcement learning algorithms, such as those based on value functions or policy gradients.
5. Not clear how sensitive is MF-PBT to the choice of frequency spread. A more comprehensive analysis of different spreads would be valuable. The paper should explore the sensitivity of MF-PBT to different frequency spreads, including both uniform and non-uniform distributions, and provide guidelines on how to choose an appropriate spread for a given task.

## Minor Weaknesses
1. Results section organization could be improved by showing performance results before hyperparameter analysis. The current structure presents hyperparameter analysis before the main performance results, which makes it harder to understand the impact of the method.
2. The motivation for anytime performance could be better developed. The paper could benefit from a more detailed discussion of the practical implications of anytime performance, such as reduced training time or faster deployment.
3. While random search and PBT are good baselines, comparison to other hyperparameter optimization methods would strengthen the evaluation. The paper could be strengthened by comparing MF-PBT to other hyperparameter optimization methods, such as Bayesian optimization or evolutionary strategies, to better understand its relative strengths and weaknesses.

### Questions
1. How does the computational overhead of managing multiple frequencies compare to standard PBT when there is an asymmetry between the cost of evolutionary updates and gradient updates?
2. Could adaptive frequency selection (rather than fixed frequencies) provide additional benefits?
3. How does MF-PBT perform on tasks with different types of problems such as sparse rewards or high dimensional action spaces?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The work introduces an extension to population based training style hyperparameter optimization and evaluates the approach for reinforcement learning applications.

### Strengths
The work addresses an inherent issue of population based training style hyperparameter optimization. It clearly communicates the cause of these shortcomings and uses them to motivate the proposed changes to the PBT regime.
The work aims to provide an extensive empirical analysis based on the speedups gained by the Brax framework.

### Weaknesses
The work does not do a good job showing that their proposed sub-population scheme actually serves to improve the PBT training regime. In particular, the work identifies the frequency with which PBT calls the exploit-explore/mutation step as the root cause of PBTs inherent greedyness. However, I believe this ignores interaction effects of multiple hyperparameters in the PBT regime. First and foremost, the population size and the selection criteria play a crucial role. With a much larger population (such as 80 members, as suggested in the original PBT publication) the truncation method has a much larger pool of "survivor" members, which can keep constant hyperparameter settings. Similarly, if the fraction of "winners" and "losers" is reduced from 25% to, e.g., only 10 or even 5% then a similar effect is observed. This, essentially, leads to different frequencies with which the members are modified/replaced. Further, these two hyperparameters of PBT, joint with the "t_ready" flag have a huge impact on the overall training setting and are closely linked on how the overall training will progress. Out of these hyperparameters, only the "t_ready" has been studied in an ablation to show the impact on PBT, without adapting the population size of PBT. In this ablation it is clearly shown that PBT can reach similar good performances as the proposed modification even if the other hyperparameters are not further tuned. It is not unlikely that, with a bit of meta-tuning, PBT would achieve similar (or even better) performances than the proposed MF-PBT. As I could not find any mention on how sensitive MF-PBT is to its own hyperparameter settings (besides larger population sizes than 32 being hurtful), I am doubtful that MF-PBT is as much of an improvement as presented in the paper. However, due to the choice of a population size of 32, I am fairly certain that PBT underperformed. The recommendation of the original authors was to use at least a population of size 40 and reported best results for larger population sizes, such as 80.
I was surprised to see a huge number of validation episodes (512) to compute the fitness scores. This number is typically tried to be kept much lower since it adds a huge evaluation cost but many episodes are used to give an accurate fitness evaluation. I am curious if MF-PBT only performs well as it had access to so many evaluation episodes (something that is far from possible in more real world settings).

As the work decided to evaluate for excessively long training horizons which go far beyond the recommended training regime on the Brax environments, it can show large improvements compared to the baseline PBT. However, as reported in Table 1, the difference is not as huge on the standard training regime. It would have been better to use the available budget to compare against other methods such as PB2 or BG-PBT (with and without the multi-frequency adaptation) to show the actual impact of using the sbupopulations for with multiple frequencies.

I believe an important baseline is missing. PBT-BT (PBT with backtracking) as introduced by Zhang et al. 2021 (already cited in the work) uses an "elites" population to backtrack once PBT is stuck in a local optimum. To my understanding, this is done to better explore the hyperparameter search space at different steps in time. If I am not mistaken, this essentially also performs the "migration" across frequencies/time-steps as the population members can be replaced with earlier well performing members.
Further, since the work positions itself in the realm of HPO for RL it should also consider using other baselines common in this space (and not just static random search). Recently, multiple papers have shown that PBT (and PB2) are outperformed by classical HPO methods (see e.g. [Shala et al. 2022](https://openreview.net/forum?id=RyAl60VhTcG) [& 2024](https://openreview.net/forum?id=MlB61zPAeR), [Eimer et al. 2023](https://proceedings.mlr.press/v202/eimer23a.html) and [Becktepe et al. 2024](https://arxiv.org/abs/2409.18827?)) and in particular multi-fidelity approaches (commonly abbreviated MF due to which I would suggest a name change for MF-PBT). Counter to PBT style methods which potentially waste a lot of parallel compute to tune an agent, multi-fidelity approaches use partial trainings to explore the hyperparameter configuration spaces to quickly hone in on the best settings. Already the work by Zhang et al. 2021 that introduced PBT-BT showed that multi-fidelity approaches have complementary strenghts to PBT style tuning. As such, the work is incomplete without considering at least one multi-fidelity baseline or otherwise classical HPO baseline for the experiments. 

Seven random seeds seems too low given that Brax has provide huge computational speedups.

The claim in the abstract that PBT can generate hyperparameter schedules in a single training run is false as PBT requires vast amounts of parallel resources and has already been called out in the SEARL paper which is already cited in the paper.

Overall, while the work proposes an interesting idea for PBT style HPO, I believe the experiments are missing crucial baselines and unfairly treat PBT. Thus my vote is reject.

### Questions
* Can you achieve a similar effect as your proposed MF-PBT by changing standard PBT hyperparameters?
* How does PBT-BTs backtracking compare to your migration strategy?
* How does your approach compare to other HPO for RL methods?

### Soundness
2

### Presentation
2

### Contribution
2
