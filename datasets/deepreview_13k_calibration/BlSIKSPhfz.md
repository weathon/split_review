# Non-Equilibrium Dynamics of Hybrid Continuous-Discrete Ground-State Sampling

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
We propose a general framework for a hybrid continuous-discrete algorithm that integrates continuous-time deterministic dynamics with Metropolis-Hastings steps to combine search dynamics with and without detailed balance. Our purpose is to study the non-equilibrium dynamics that leads to the ground state of rugged energy landscapes in this general setting. Our results show that MH-driven dynamics reach ``easy'' ground states faster, indicating a stronger bias in the non-equilibrium dynamics of the algorithm with reversible transition probabilities. To validate this, we construct a set of Ising problem instances with a controllable bias in the energy landscape that makes one degenerate solution more accessible than another. The constructed hybrid algorithm demonstrates significant improvements in convergence and ground-state sampling accuracy, achieving a 100x speedup on GPUs compared to simulated annealing, making it well-suited for large-scale applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new algorithm that combines chaotic search and Metropolis-Hastings. The goal seems to solve optimization problems in discrete non-convex energy landscapes. The proposed algorithm is tested on several combinatorial optimization tasks.

### Strengths
- The empirical results include multiple baselines and comparisons in terms of different metrics.
- The visualization in Fig.1 clearly shows the main algorithmic idea.

### Weaknesses
 - The problem that this paper aims to solve is vague. Is the goal to develop an algorithm that samples better in non-convex energy landscapes, or for optimization in discrete landscapes? Or is the goal to understand non-equilibrium dynamics in non-convex energy landscapes? The paper needs to clearly define the specific problem it is addressing, as these are distinct goals with different evaluation criteria. The current framing makes it difficult to assess the significance of the results. Similarly, the motivation of the proposed algorithm which combines chaotic search with Metropolis-Hastings is not well-explained. Why is this combination expected to be beneficial, and what specific challenges in the target problem does it address?
- The novelty of the proposed algorithm is unclear. Is the algorithm a straightforward combination of chaotic search and MH? If not, what is the challenge, and how does the paper solve the challenge? The paper needs to articulate the specific technical contribution beyond simply combining two existing methods. What are the non-trivial modifications or insights that make this combination effective, and how does it differ from a naive implementation?
- The empirical improvement is not consistent. For example, Fig.2 shows that CACm is better than proposed method also the variance of the proposed is significantly larger than the baselines. The paper should address why the proposed method does not consistently outperform baselines and provide a more detailed analysis of the conditions under which it excels or fails. The high variance also needs to be explained, as it suggests instability or sensitivity to parameter settings.
- The runtime comparison only considers simulated annealing. It will be better to include other baselines as well. The choice of baseline algorithms for runtime comparison is limited, and the paper should include more relevant and state-of-the-art methods to provide a comprehensive evaluation of the proposed algorithm's efficiency.
- The paper compared the standard Gibbs with gradient which is developed for combinatorial optimization. It will be more convincing to compare with gradient-based discrete MCMC that is developed for CO, such as [1].

### Questions
NA

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Overall, this paper proposes a promising hybrid continuous-discrete sampling framework that demonstrates clear benefits in convergence speed and sampling accuracy for rugged energy landscapes. This paper could benefit from additional theoretical insights and comparisons with established methods.

### Strengths
(1)The proposed method effectively leverages the Metropolis-Hastings method within a continuous-discrete framework, enhancing sampling efficiency for ground-state discovery in challenging discrete landscapes. This approach demonstrates practical advantages, such as notable improvements in convergence speed and sampling accuracy on GPU architectures.

(2) The method’s focus on non-equilibrium dynamics and its capacity to identify accessible ground states faster than traditional approaches offer a valuable contribution to optimization in rugged energy landscapes.

### Weaknesses
(1) Although the paper demonstrates the practical benefits of the hybrid continuous-discrete approach, the theoretical understanding of the sampling properties of the MHCACm algorithm remains unaddressed. I wonder if the authors could provide a discussion on potential directions for analytical proof of the sampling capabilities of MHCACm, such as convergence rates or mixing times. Specifically, it is unclear how the introduction of auxiliary variables and the Metropolis-Hastings correction affect the ergodicity of the Markov chain, and whether the algorithm can escape local minima effectively in complex energy landscapes. A more detailed analysis of the algorithm's stationary distribution and its relationship to the target distribution would be beneficial.

(2) I would like to suggest the authors include more comparison with other prominent sampling algorithms using collective variables, for example, 'Sampling metastable systems using collective variables and Jarzynski–Crooks paths' by G. Stoltz et al. In particular, a detailed comparison should discuss how the proposed method's use of auxiliary variables compares to the use of collective variables in enhancing sampling efficiency, and whether the proposed method can be combined with techniques that utilize collective variables to further improve performance. It is not clear how the continuous relaxation in the proposed method relates to the use of collective variables for exploring free energy surfaces.

(3) While the method achieves a 100x speedup over simulated annealing on GPUs, a discussion of any limitations or computational trade-offs encountered in specific scenarios (such as highly multimodal landscapes) would be beneficial, for instance, I wonder if the authors could provide specific examples of problem types or landscapes where their method may face challenges. For example, it would be useful to understand how the algorithm's performance is affected by the presence of many local minima with similar energy values, or by the existence of narrow energy barriers separating different basins of attraction.

(4) I wonder if the authors could provide additional insights into how MHCACm scales with increased problem complexity, for instance, if the authors could demonstrate how the empirical scaling results and the performance of proposed algorithm changes with increasing complexity for a range of benchmark examples. Specifically, it would be helpful to see how the algorithm's runtime and memory requirements scale with the number of variables in the system, and whether the algorithm's performance degrades for very large-scale problems.

(5) The paper implies that the method’s bias towards “easy” ground states is advantageous, but this effect could also limit the algorithm’s ability to reach more challenging or rare ground states. I wonder if the authors could provide quantitative results on the algorithm's performance in finding both "easy" and "hard" ground states across different problem instances. It would be useful to see the distribution of times to find different ground states, and how this distribution changes with the complexity of the problem.

(6) Additionally, I wonder if the authors could discuss potential modifications to the algorithm that could help balance the performance of exploration of both easy and hard ground states. For instance, it is unclear whether the current implementation of the Metropolis-Hastings step is optimal for exploring the full energy landscape, and whether alternative acceptance criteria or adaptive sampling techniques could improve the algorithm's ability to find rare ground states.

### Questions
(1)  While the method achieves a 100x speedup over simulated annealing on GPUs, a discussion of any limitations or computational trade-offs encountered in specific scenarios (such as highly multimodal landscapes) would be beneficial, for instance, I wonder if the authors could provide specific examples of problem types or landscapes where their method may face challenges.

(2) I wonder if the authors could provide additional insights into how MHCACm scales with increased problem complexity, for instance, if the authors could demonstrate how the empirical scaling results and the performance of proposed algorithm changes with increasing complexity for a range of benchmark examples.

(3)  The paper implies that the method’s bias towards “easy” ground states is advantageous, but this effect could also limit the algorithm’s ability to reach more challenging or rare ground states. I wonder if the authors could provide quantitative results on the algorithm's performance in finding both "easy" and "hard" ground states across different problem instances. 

(4) Additionally, I wonder if the authors could discuss potential modifications to the algorithm that could help balance the performance of exploration of both easy and hard ground states.

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
2

### Summary
The paper proposes a class of hybrid continuous-discrete algorithms by integrating continuous dynamics with Metropolis-Hastings steps. The paper also constructs a set of Ising problems with a tunable parameter to trade off between easy ground states and hard degenerate ground states, in order to experiment with the bias of different algorithms. The proposed class of algorithms are also fast solvers that achieve a great amount of acceleration on GPU due to a parallelizable structure.

### Strengths
* The paper writing is nice and structured, with a comprehensive literature review and detailed problem set-up.
* The paper looks technically sound with solid mathematical proof.
* The proposed algorithm is evaluated on multiple tasks and compared with various other benchmark methods, showing competitive performance.

### Weaknesses
 * I am not very familiar with the literature, but seems that the tasks of ground-state sampling are not formally defined in the paper, as well as the idea of non-equilibrium dynamics.
* The connection between ground-state sampling and deep learning optimization/generalization mentioned in the paper is interesting, but the discussion is very limited. 
* For numerical experiments, the definition of TTS is hard to comprehend. Does smaller TTS indicate better algorithmic performance?

### Questions
* Based on the algorithmic design in this paper, is there any insight we can draw on what an ideal optimizer for deep neural nets should look like?
* Can you elaborate more on the numerical performance of CACm and MHCACm? From the charts, the two performances seem to be close to each other.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents two variants of the CAC (chaotic amplitude control) algorithm, namely CAC with momentum (CACm) and Metropolis-Hastings CAC with momentum (HMCACm). CACm is a deterministic continuous-time dynamical model for combinatorial optimization, and HMCACm is a Metropolis-Hastings adjusted version of CACm with the Boltzmann distribution as the theoretical equilibrium. MHCACm can be regarded as a unified framework that generalizes many existing methods, including simulated annealing, Hopfield neural networks, analog iterative machines, and CAC(m). Numerical results show that this method illustrates faster relaxation time on NP-hard problems. In particular, MHCACm exhibits excellent performance in sampling from easier ground states, which may be relevant to training over-parametrized neural networks.

### Strengths
- State-of-the-art algorithms exploiting relaxation to a continuous state form discrete combinatorial optimization do not sample fairly from the Boltzmann distribution due to the lack of detailed balance. The MHCACm algorithm fills in this conceptual gap by adding a Metropolis-Hasting step. This new design ensures that MHCACm samples fairly from a discrete distribution while iterating over the relaxed (continuous) search space. 
- The numerical results look strong. Table 3 shows that MHCACm has a success probability higher than dSBM, another well-known Ising solver based on GPU. 
- MHCACm is well-suited for large-scale deployment on GPU because its computational bottleneck is matrix-vector multiplication.

### Weaknesses
 - Little theoretical justification for the effectiveness of MHCACm is provided. Specifically, it is not clear why a fair sampling strategy in the CAC framework would lead to a better performance in an optimization (ground state finding) problem. Relaxation to the ground state does not necessarily need to go through a detailed-balance algorithmic path. It would be nice to discuss how the Metropolis-Hastings step interacts with the CAC dynamics to potentially improve optimization performance. For instance, does the Metropolis-Hastings step primarily act as a mechanism to escape local minima, or does it play a more fundamental role in shaping the overall trajectory towards the ground state? The paper should delve deeper into the interplay between the continuous-time dynamics of CAC and the discrete updates of the Metropolis-Hastings step, perhaps by analyzing the acceptance rate of the Metropolis-Hastings step as a function of the CAC dynamics' progress.
- No empirical results for real-world optimization problems. While the performance of MHCACm has been benchmarked over the dWPE instances and GSET, these test instances are highly artificial and may not reflect the performance of the algorithm in a practical setting (e.g., quadratic assignment problems, portfolio optimization problems, etc.). The current benchmarks do not adequately demonstrate the practical applicability of the proposed method. It is crucial to evaluate the algorithm on problems with real-world constraints and objective functions to assess its robustness and scalability.


### Questions
- The paper only reports the TTS in the experiments on dWPE instances (section 4.4). It would be more transparent if the success probability and runtime data could be provided as well, as it is not clear whether the advantage comes from a higher success probability or a shorter wall-clock runtime due to GPU parallelization. 
- Can you elaborate more on the "dual-primal Lagrangian approach" and its difference from CAC?
- Some minor typos: e.g., line 122 "in order (to) benchmark this algorithm's ability".

### Soundness
3

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
3

### Summary
The authors propose a novel hybrid continuous-discrete algorithm that combines deterministic continuous dynamics with Metropolis-Hastings (MH) steps for ground-state sampling in non-equilibrium dynamics.

### Strengths
1. The combination of chaotic dynamics with an MH step to ensure convergence to a target distribution represents an innovative approach to hybrid sampling.
2. The hybrid algorithm shows potential for improving ground-state sampling performance in combinatorial optimization
3. The authors address parallelization for efficient computation on GPUs
4. The discussion on combining chaotic dynamics with probabilistic methods provides a useful context for researchers working at the intersection of machine learning and statistical physics.

### Weaknesses
While the authors present an interesting optimization algorithm, the clarity of the writing is a major concern. The main ideas are difficult to follow in the current presentation. I would encourage the authors to reconsider their notation and improve their writing to convey their ideas more effectively to readers.


**Major concerns**
1. The momentum and pre-conditioning typically serve different roles in optimization: momentum accumulates past gradients, and pre-conditioning captures curvature information. I do not think the connection demonstrated in Section 3.2 is trivial. A detailed explanation is needed in the main text to connect them.
2. The paper lacks theoretical guarantees regarding the convergence or performance of the proposed algorithm.
3. Since the algorithm incorporates a momentum variable, it would be more consistent to account for this momentum within the MH step (Equation (7)), rather than applying it solely to $\boldsymbol{\sigma}$. The current implementation appears to accept or reject the position variable $\tau$ based on the Metropolis-Hastings criterion, while neglecting the momentum and auxiliary variables $u$ and $e$ that also influence the dynamics. This approach may lead to a violation of detailed balance, as the acceptance probability should consider the joint distribution of all variables, not just the marginal distribution of the position variable. The algorithm's convergence to the target distribution is therefore questionable.

**Other suggestions**
1. The paper lacks clear definitions for essential variables (e.g., $\boldsymbol{u}$ and $\boldsymbol{e}$ in Equation (1)).
2. The time variable $t$ is used ambiguously. It denotes continuous evolution in Equation (1) but has discrete updates in Equations (4)-(5).
3. Although the authors appear to focus on ground-state sampling, the formulation provided in Section 3.2 is more oriented toward sampling from a Gibbs measure rather than explicitly defining the ground-state sampling.
4. Ensure that all variables and abbreviations are clearly defined. For example, abbreviations such as SA, HNN, and CACm used in Table 1 should be explicitly explained in the main text.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
