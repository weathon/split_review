# Efficient Discovery of Pareto Front for Multi-Objective Reinforcement Learning

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 8, 3, 5

## Abstract
Multi-objective reinforcement learning (MORL) excels at handling rapidly changing preferences in tasks that involve multiple criteria, even for unseen preferences. However, previous dominating MORL methods typically generate a fixed policy set or preference-conditioned policy through multiple training iterations exclusively for sampled preference vectors, and cannot ensure the efficient discovery of the Pareto front. Furthermore, integrating preferences into the input of policy or value functions presents scalability challenges, in particular as the dimension of the state and preference space grow, which can complicate the learning process and hinder the algorithm's performance on more complex tasks. To address these issues, we propose a two-stage Pareto front discovery algorithm called Constrained MORL (C-MORL), which serves as a seamless bridge between constrained policy optimization and MORL. Concretely, a set of policies is trained in parallel in the initialization stage, with each optimized towards its individual preference over the multiple objectives. Then, to fill the remaining vacancies in the Pareto front, the constrained optimization steps are employed to maximize one objective while constraining the other objectives to exceed a predefined threshold. Empirically, compared to recent advancements in MORL methods, our algorithm achieves more consistent and superior performances in terms of hypervolume, expected utility, and sparsity on both discrete and continuous control tasks, especially with numerous objectives (up to nine objectives in our experiments).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a two-stage algorithm, Constrained Multi-objective Reinforcement Learning (C-MORL), to efficiently discover the Pareto front in multi-objective reinforcement learning (MORL) problems.  The first stage, Pareto initialization, trains a set of policies in parallel, each with a specific preference vector.  The second stage, Pareto extension, selects policies from the initial set based on their crowd distance and performs constrained optimization to maximize one objective while constraining others.  This approach aims to address limitations in existing MORL methods, such as difficulty covering the complete Pareto front.  The authors demonstrate the effectiveness of C-MORL on various MORL benchmarks, including discrete and continuous control tasks with up to nine objectives, showing superior performance in hypervolume, expected utility, and sparsity compared to baselines.

### Strengths
--Originality: The paper introduces a novel perspective by combining constrained policy optimization with MORL, leading to a unique two-stage algorithm for Pareto front discovery. 

--Quality: The paper provides a rigorous theoretical analysis of the proposed C-MORL algorithm. The experimental evaluation covers a diverse set of MORL benchmarks with varying state/action spaces and objective dimensions.   

--Significance: The proposed C-MORL algorithm provides a more efficient and effective way to discover the Pareto front, especially for complex tasks with high-dimensional objective spaces.

### Weaknesses
Clarity: While the core idea is clear, in general it's difficult to follow this paper. The paper could be made more accessible. The algorithm has many stages (Pareto initialization, policy selection, Pareto extension) with different hyperparameters (number of initial policies, number of extension policies, constraint relaxation coefficient) and design choices (C-MORL-CPO vs. C-MORL-IPO, crowd distance vs. random selection). The paper could benefit from a more streamlined presentation of the algorithm and a clearer explanation of the implications of these different choices. Many of these design choices are not studied and the implication of them is not clear. I would suggest the authors move some of the theoretical analysis to the appendix and use the space to discuss these design choices and hyperparameters better.

### Questions
How difficult is to determine the specific values for hyperparameters like the number of initial policies, the number of extension policies, and the constraint relaxation coefficient in the experiments? Does this require problem-specific knowledge such as the range of rewards?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel approach for solving multi-objective reinforcement learning (MORL) problems using a two-stage algorithm called Constrained MORL (C-MORL). The authors proposes to frame the MORL problem as a Constrained MDP. Specifically, in the first stage, C-MORL trains a diverse population of policies across various preference vectors, initializing a set of initial solutions. The second stage then improves these policies via constrained optimization, guaranteeing a targetted expansion of the covered Pareto front.  The authors addressed challenges with existing methods, including limited Pareto front coverage and low training efficiency. The authors show that C-MORL achieves state-of-the-art results on multiple MORL benchmarks in terms of hypervolume and expected utility metrics.

### Strengths
**1. Good presentation** 

Firstly, the presentation of the paper is well-done, motivations and preliminaries are well set-up from the beginning, and the flow of the paper was coherent. It was easy to read.

**2. Novelty** 

The proposed idea is novel in the *MORL* field. It seems to be inspired by approaches from the MOO field, such as Epsilon-constraint methods, but the crossover is done in a creative way that addresses the unique challenges of sequential decision-making setting in MORL. Most contrained MORL problems are more focussed on the aspects of safety constraints, so formalizing the evolution of policies as a constrained optimization problem is novel in MORL, to my best knowledge.

**3. Theoretical rigor** 

The paper provides sound propositions and proofs; albeit built upon theoretical foundations already established in CMDPs. One of the more interesting contributions is Proposition 4.3, which provides a practical guideline and sufficient condition for a constrained optimization problem to yield Pareto-optimal solutions. This aspect is a novel adaptation tailored to the requirements of MORL. The condition provided by the proposition is not overly restrictive or computationally intensive to verify. The complexity proof (proposition 5.1) is compelling, and provides strong support for using C-MORL over PGMORL

**4. Extensive experiments** 

The authors did a *very* extensive set of experiments across *10* distinct benchmarks, both discrete and continuous. The results are clearly indicative of significant improvements over existing approaches.

### Weaknesses
 **1. Comparisons against utility-based/preference-conditioned methods can be improved** 

The paper mentions that preference-conditioned methods approaches struggle with scalability, I don't fully agree with that. Evolutionary approaches like C-MORL face significant scalability limitations too, for e.g., you can't evolve a population of CNN-based policies (agents) without significant memory overhead. This is worrisome especially if we want to deploy agents to real-world setting with image-based observation spaces. Next, evolutionary approaches seem ideal because you can learn many densely-packed solutions w.r.t. tracing the true optimal Pareto front but they present practical challenges when it comes to policy selection. It is unclear how different users can select the policies they desire for evolutionary approaches whereas utility-based/preference-conditioned methods places these preferences at the forefront. These concerns do not critically impact my overall assessment of this paper, but addressing these points would help clarify the limitations and appropriate use cases of C-MORL for the research community.

**2. No comparisons against the MORL/D algorithm** 

The MORL/D algorithm by [1] is very similar to PGMORL and C-MORL, all three of which are evolutionary approaches with populations initialized using preference vectors sampled across the unit simplex. It has state-of-the-art results across many benchmarks, and demonstrates a vast improvement over PGMORL. A significant drawback of PGMORL is perhaps the reliance on prediction models to guide the training, which MORL/D does not depend on. The algorithm is provided in the same code repository as GPI-LS, i.e. [2]. I can imagine the differences between C-MORL and MORL/D in terms of performances being much tighter. Comparisons against this method would be necessary for the results to be more compelling. Specifically, testing against MORL/D with PSA weight adaptation would be very much desired.

### Questions
**1. How are comparisons between GPI-LS/CAPQL vs PGMORL/C-MORL made?** 

As far as I know, CAPQL and GPI-LS are linear scalarization methods and conventionally they are evaluated by sampling preference vectors uniformly across the unit simplex, to form their approximate Pareto front. For evolutionary methods however, they usually keep an archive of policies and their associated vector performances, and then the approximate Pareto front is made during evaluation by filtering the non-Pareto dominated policies. However, this can be concerning during evaluations, especially for metrics like sparsity. If you allow CAPQL/GPI-LS only 100 preference vectors for evaluation, but allow PGMORL/C-MORL and unbounded archive of policies for evaluation, the metrics are naturally going to gravitate in favor of the latter group. Clarification w.r.t. to this aspect needs to be made for me to be more certain about the results of the paper.

**2. How would C-MORL react to concave Pareto fronts?** 

In the end of the paper, you mentioned that 
> *"...observe that in some benchmarks, the current constrained policy optimization method fails to adequately extend the policies toward certain objective directions"*. 

I am curious as to how C-MORL would react to concave pockets on the Pareto fronts? Could the constrained optimization cause the policy to prefer easier paths in convex regions?

**3. Please answer questions in weaknesses**

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel method for learning a Pareto set of policies for solving multi-objective reinforcement learning (MORL) problems in which the reward is a vector composed of multiple conflicting objectives. The paper introduces Constrained MORL (C-MORL), an algorithm that maintains a population of policies to approximate the Pareto front. At each iteration, it learns novel policies that are optimized to solve a constrained MDP such that the solution to it lies in the Pareto front. The method was evaluated in several benchmarks with varying numbers of objectives and characteristics in terms of different MORL evaluation metrics.

### Strengths
- The problem of deciding which directions in the objective space are more relevant to learn when approximating a Pareto front is very relevant to the MORL community.
- The evaluation considers many challenging benchmarks with discrete and continuous action spaces and up to 9 objectives.

### Weaknesses
 - The paper can significantly be improved in terms of clarity (see below).
- The method requires learning a separate neural network for each policy, which does not scale in terms of memory. This is in contrast with previous MORL algorithms that train a single model conditioned on the weight vector $w$.
- There are many experimental details missing in the paper that need to be addressed (see Questions below).

### questions:
 Below, I have questions and constructive feedback to the authors:

1) “(Alegre et al., 2023) further introduce a novel Dyna-style MORL method that significantly improves sample efficiency while relying on accurate learning of dynamics”.
They also introduce a model-free version of their algorithm (GPI-LS), which parallelizes the training of the CCS.

2) Minor comment about the notation: The letter $G$ is usually used in the RL literature to denote the random variable of the return, and not its expected value. The expected value is usually denoted with the letter $J$ or by $V(S_0)$. I would suggest considering changing this notation to avoid confusion.

3) In the definition of the space of preference weights, $\Omega$, you should also restrict $w_i\geq0$.

4) It is not clear how the projection operators $\Gamma_\lambda$ and $\Gamma_\pi$ are defined. What does it mean to project $\lambda$ and $\pi$ into a compact and convex set?

5) In Proposition 4.4, it is not clear how the policy update works. Are you assuming $pi_r$ is a parameterized policy? Is this equation updating the parameters of the policy? What is a “fixed point of MORL policy”?

6) In Theorem 4.5, what is the Slater’s condition?

7) “we also maintain a solution buffer to enhance policy diversity.” What is a solution buffer, and how does it enhance policy diversity? Tihs is not explained in this section.

8) In Eq. 3, how is the hyperparameter $\beta$ selected? How can it impact the optimality of the method, in theory?

9) In Eq. 5, how is the parameter $t$ of the function $\phi$ selected?

10) I am not sure Proposition 5.1 is making a fair statement. Although the algorithm running time is linear in the number of extension policies $N$, it is expected that the number of policies $N$ required to cover the Pareto front would probably increase exponentially with the number of objectives. Of course, a user can use the same value of $N$ independently of the number of objectives $n$, but that would probably be sub-optimal. That is, it is expected that one should increase $N$ as $n$ increases.

11) It is not very clear in the paper when C-MORL-CPO or C-MORL-IPO are used. Which one is used in the proposed algorithm?

12) Why does PG-MORL have to solve a knapsack problem with $K$x$N$ points? This is not mentioned in the paper of Xu et al., 2020.

13) In Table 2, the authors denote in bold some metrics which are overlapping with the competitors. For instance, in MO-Ant-2d, HV of $3.10\pm0.25$ and $3.13\pm0.20$ and EU $4.28\pm0.19$ and $4.29\pm0.19$ overlap.

14) There are many experimental details missing in the experimental section:
- How many random seeds were used in each experiment? Are the metrics averaged over how many runs?
- Which version of CAPQL and GPI-LS did the authors use? How were the hyperparameters of the competitors chosen?
- CAPQL and GPI-LS are based on SAC and TD3, while C-MORL is based on PPO. This could significantly impact the results, and it makes it difficult to infer whether the performance gains come from SAC vs. PPO or the expansion technique introduced in the paper.
- Alternatively, did the authors reimplement CAPQL and GPI-LS to use PPO as the underlying policy learning technique?
- How were the PFs in Figure 4 generated? Are those points average over how many episodes? How many weight vectors were used to evaluate the learned policies for different utilities?

15) The authors mention that “each method is tested across three
runs with the same seeds”. Three runs are very unlikely to be sufficient to provide significant statistical results. 

16) I suggest including the ablation of the Pareto Extension procedure and comparing it with solving for random linear weights since this procedure is arguably more important than the Policy Selection procedure. It would be important to observe if the overhead of employing CPO or IPO is really providing performance gains.

17) The idea of the paper of solving constrained MDPs to identify new policies in the Pareto front is similar to that of (Willem et al., 2024, “Divide and Conquer: Provably Unveiling the Pareto Front with Multi-Objective Reinforcement Learning”). Please add a discussion explaining the similarities and differences.

### Questions
Below, I have questions and constructive feedback to the authors:

1) “(Alegre et al., 2023) further introduce a novel Dyna-style MORL method that significantly improves sample efficiency while relying on accurate learning of dynamics”.
They also introduce a model-free version of their algorithm (GPI-LS), which parallelizes the training of the CCS.

2) Minor comment about the notation: The letter $G$ is usually used in the RL literature to denote the random variable of the return, and not its expected value. The expected value is usually denoted with the letter $J$ or by $V(S_0)$. I would suggest considering changing this notation to avoid confusion.

3) In the definition of the space of preference weights, $\Omega$, you should also restrict $w_i\geq0$. 

4) It is not clear how the projection operators $\Gamma_\lambda$ and $\Gamma_\pi$ are defined. What does it mean to project $\lambda$ and $\pi$ into a compact and convex set?

5) In Proposition 4.4, it is not clear how the policy update works. Are you assuming $pi_r$ is a parameterized policy? Is this equation updating the parameters of the policy? What is a “fixed point of MORL policy”?

6) In Theorem 4.5, what is the Slater’s condition?

7) “we also maintain a solution buffer to enhance policy diversity.” What is a solution buffer, and how does it enhance policy diversity? Tihs is not explained in this section.

8) In Eq. 3, how is the hyperparameter $\beta$ selected? How can it impact the optimality of the method, in theory?

9) In Eq. 5, how is the parameter $t$ of the function $\phi$ selected?

10) I am not sure Proposition 5.1 is making a fair statement. Although the algorithm running time is linear in the number of extension policies $N$, it is expected that the number of policies $N$ required to cover the Pareto front would probably increase exponentially with the number of objectives. Of course, a user can use the same value of $N$ independently of the number of objectives $n$, but that would probably be sub-optimal. That is, it is expected that one should increase $N$ as $n$ increases.

11) It is not very clear in the paper when C-MORL-CPO or C-MORL-IPO are used. Which one is used in the proposed algorithm?

12) Why does PG-MORL have to solve a knapsack problem with $K$x$N$ points? This is not mentioned in the paper of Xu et al., 2020. 

13) In Table 2, the authors denote in bold some metrics which are overlapping with the competitors. For instance, in MO-Ant-2d, HV of $3.10\pm0.25$ and $3.13\pm0.20$ and EU $4.28\pm0.19$ and $4.29\pm0.19$ overlap.

14) There are many experimental details missing in the experimental section:
- How many random seeds were used in each experiment? Are the metrics averaged over how many runs?
- Which version of CAPQL and GPI-LS did the authors use? How were the hyperparameters of the competitors chosen?
- CAPQL and GPI-LS are based on SAC and TD3, while C-MORL is based on PPO. This could significantly impact the results, and it makes it difficult to infer whether the performance gains come from SAC vs. PPO or the expansion technique introduced in the paper.
- Alternatively, did the authors reimplement CAPQL and GPI-LS to use PPO as the underlying policy learning technique?
- How were the PFs in Figure 4 generated? Are those points average over how many episodes? How many weight vectors were used to evaluate the learned policies for different utilities?

15) The authors mention that “each method is tested across three
runs with the same seeds”. Three runs are very unlikely to be sufficient to provide significant statistical results. 

16) I suggest including the ablation of the Pareto Extension procedure and comparing it with solving for random linear weights since this procedure is arguably more important than the Policy Selection procedure. It would be important to observe if the overhead of employing CPO or IPO is really providing performance gains.

17) The idea of the paper of solving constrained MDPs to identify new policies in the Pareto front is similar to that of (Willem et al., 2024, “Divide and Conquer: Provably Unveiling the Pareto Front with Multi-Objective Reinforcement Learning”). Please add a discussion explaining the similarities and differences.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces C-MORL, a two-stage policy optimization algorithm aimed at efficiently discovering the Pareto front through a constrained optimization framework for multi-objective reinforcement learning (MORL). C-MORL effectively manages complex tasks with multiple discrete and continuous objectives, as demonstrated in experiments involving up to nine objectives. To achieve solutions without additional computational costs, the paper presents an interior-point-based approach for solving a relaxed formulation, ensuring the derivation of Pareto-optimal policies under specified conditions. Extensive evaluations across diverse MORL benchmarks, including robotics control and sustainable energy management, highlight C-MORL’s superior capability to explore a broader Pareto front under unseen preferences.

### Strengths
The paper builds a solid foundation for its optimization approach by employing extensive constraint theories. The experimental section thoroughly evaluates state-of-the-art MORL methods on multi-objective optimization problems, with a comprehensive analysis specifically on the newly introduced Building-9D benchmark. The proposed two-stage method partially addresses certain challenges in multi-objective optimization (MOO). The conclusions align well with the research questions posed, demonstrating consistency between the methodology and findings.

### Weaknesses
1. **Lack of Innovation and Convincing Results:**
   The structure of the paper is reasonable, but the main idea and innovation seem insufficient. The contribution appears to be limited to encapsulating PGMORL or any single RL algorithm by using crowding distance to select policies for constrained optimization. For preferences that have not been trained, the method merely matches them to an existing best policy without discovering new policies corresponding to those preferences. This results in policies that are locally optimal rather than truly globally optimal in the CCS, which is unconvincing. The core issue is that the method does not actively explore the policy space for novel solutions, instead relying on a selection process from previously trained policies. This approach may not effectively discover diverse and high-performing policies, especially in complex, high-dimensional environments.

2. **Selection of Extreme Solutions:**
   Since extreme solutions have already reached performance bottlenecks on particular objectives, selecting them by default does not facilitate the exploration of the potential Convex Coverage Set (CCS). This approach may limit the discovery of more diverse and optimal policies. By focusing on extreme points, the algorithm may miss out on intermediate solutions that could offer a better trade-off across multiple objectives. This is especially problematic when the Pareto front is non-convex, as the extreme points may not be representative of the overall solution space.

3. **Efficiency and Resource Intensity:**
   The main idea—selecting policies to train based on crowding distance and storing all intermediate policies in a buffer—is straightforward. However, constructing the CCS through a vast number of policies is highly resource-intensive and inefficient. This method may not be practical for large-scale applications due to its computational demands. The reliance on a large buffer to store intermediate policies can lead to significant memory overhead, and the process of calculating crowding distance for a large number of policies can be computationally expensive, especially in high-dimensional objective spaces.

4. **Time Complexity Comparison:**
   Given that the work uses PGMORL for initialization, comparing the time complexity to PGMORL is not entirely fair since it is already part of the proposed algorithm. A more appropriate comparison would isolate the additional computational overhead introduced by the proposed method. The comparison should focus on the specific cost of the constrained optimization and policy selection steps, rather than including the initialization phase which is common to both methods. This would provide a clearer picture of the actual computational benefits or drawbacks of the proposed approach.

5. **Unclear Initialization and Preference Distribution:**
   The paper does not clearly explain how many policies are selected during initialization, how many corresponding weight preferences are chosen, and how they are distributed—an important aspect of the methodology. In subsequent policy selection and optimization, the distribution of preferences remains unchanged. This could lead to policies converging around certain preferences, hindering further exploration of the CCS. While PGMORL addresses this issue effectively with a utility prediction method, your paper does not mention the problem. Consequently, it is unclear whether the filling of CCS gaps in the experimental results belongs to the same cluster. The lack of clarity on the initialization process and preference distribution makes it difficult to reproduce the results and understand the algorithm's behavior.

6. **Overuse of Formulas and Theorems:**
   The paper includes a large number of formulas and theorems, which detracts from the reading experience. These mathematical details contribute little to the core algorithm, especially regarding policy selection and assignment. Simplifying or reducing the emphasis on these formulas could improve clarity and accessibility. The extensive use of mathematical formalism does not significantly enhance the understanding of the core algorithm, and it may obscure the key ideas and practical aspects of the method.

7. **Inconsistency in Method Presentation:**
   Similar to the previous point, C-MORL-IPO and C-MORL-CPO are defined with extensive formulas and theorems, but only C-MORL is used in the experimental results. It is unclear which method is employed in the policy extension process of C-MORL (i assume IPO?). These two methods do not appear in the baselines, nor are there corresponding ablation studies to support them, i.e., there is no evidence in the main results support the claim 'C-MORL-IPO is more computationally efficient than C-MORL-CPO'. Their reappearance in the supplementary materials without integration into the main results creates a fragmented reading experience and causes confusion.

8. **Statistical Significance in Comparison Results:**
   In the comparison results table for the MO-Ant-2d environment under HV and EU metrics, the error of the standard deviation between C-MORL and GPI-LS exceeds the error of mean difference. Therefore, it cannot be considered as a solid surpassing to the baseline.

### Questions
1. **Selection of Mujoco Environments:**
   Why were only certain environments from the Mujoco suite selected as baselines for demonstration while other significant environments were omitted?

2. **Unclear Initialization and Preference Distribution:**
   The paper does not clearly explain how many policies are selected during initialization, how many corresponding weight preferences are chosen? And how they are distributed?

3. **Efficiency and Resource Intensity:**
The main idea of selecting policies for training based on crowding distance and storing all intermediate policies in a buffer is straightforward. However, constructing the CCS through a vast number of policies seems highly resource-intensive and inefficient. In each MO-problem, How many policies do you store, and how many are used to construct the CCS? Compared to PGMORL, do you utilize more or fewer policies in this process?

4. **Selection of Extreme Solutions:**
   Since extreme solutions have already reached performance bottlenecks on particular objectives, selecting them by default does not facilitate the exploration of the potential Convex Coverage Set (CCS). Why are they selected as default for next training round?

### Soundness
2

### Presentation
1

### Contribution
2
