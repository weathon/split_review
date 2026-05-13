# Signature Kernel Conditional Independence Tests in Causal Discovery for Stochastic Processes

- Decision: Accept
- Scores: 8, 6, 10, 8

## Abstract
Inferring the causal structure underlying stochastic dynamical systems from observational data holds great promise in domains ranging from science and health to finance. Such processes can often be accurately modeled via stochastic differential equations (SDEs), which naturally imply causal relationships via `which variables enter the differential of which other variables'. In this paper, we develop conditional independence (CI) constraints on coordinate processes over selected intervals that are Markov with respect to the acyclic dependence graph (allowing self-loops) induced by a general SDE model. We then provide a sound and complete causal discovery algorithm, capable of handling both fully and partially observed data, and uniquely recovering the underlying or induced ancestral graph by exploiting time directionality assuming a CI oracle. Finally, to make our algorithm practically usable, we also propose a flexible, consistent signature kernel-based CI test to infer these constraints from data. We extensively benchmark the CI test in isolation and as part of our causal discovery algorithms, outperforming existing approaches in SDE models and beyond.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an innovative approach to uncovering causal relationships in stochastic processes, using conditional independence (CI) tests based on signature kernels to detect causal links within stochastic differential equation (SDE) models. It presents a comprehensive algorithm to reconstruct causal graphs, even with partially observed data and irregular sampling patterns. Benchmark tests show this method outperforms existing causal discovery techniques (in small graphs) in continuous-time settings, showing particular strength in cases with incomplete data and path-dependence (without need for hyper parameter tuning)

### Strengths
- Provides a solid framework for causal inference in continuous-time SDEs, going beyond the limitations of traditional discrete-time models.
- Introduces a practical CI test using signature kernels, suited for handling path-dependent random variables.
- Shows strong performance with incomplete data and irregularly sampled time series.
- Empirical tests and real-world examples, like pairs trading, demonstrate the algorithm’s practical effectiveness and accuracy.
- Method is not heavily dependent on hyper parameters.

### Weaknesses
 - The paper assumes stationarity and acyclicity, which may restrict its use in scenarios where causal relationships change over time. Specifically, the stationarity assumption limits the applicability of the method to systems where the underlying data generating process does not evolve, which is a strong assumption in many real-world scenarios. Furthermore, the acyclicity assumption prevents the method from being applied to systems with feedback loops, which are common in biological and economic systems.
- Limited discussion on performance of the algorithm if the IC Oracle is wrong. The paper does not thoroughly explore the impact of errors in the conditional independence tests on the final causal graph. This is a critical issue because in practice, these tests are based on finite samples and are therefore prone to both Type I (false positive) and Type II (false negative) errors. The propagation of these errors through the algorithm could lead to significant inaccuracies in the inferred causal structure.
- While I appreciate the rigor in the paper, the length of the paper, considering the appendix is more than $2 / 3$ of the page limit. Might be more suitable for a journal setting.

### Questions
- The  Oracle used for this algorithm, how likely it is to be wrong? How much it would affect the performance?
- What happens if the underlying causal graph has a cycle? How does the algorithm handle this situation?
- How does the algorithm handles the case where the observation in time is limited (subsampled) ?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a sound and complete causal discovery algorithm for stochastic processes, incorporating a consistent signature kernel conditional independence test. The stochastic process is modeled using a stochastic differential equation (SDE), and the entire process is segmented into intervals that exhibit the Markov property with respect to an acyclic dependence graph.

### Strengths
1. The effect working on the 'continuous-time' path sequence is impressive.

2. The signature kernel conditional independence test is a novel CI test for path sequences.

3. The paper is well written, and the framework of the paper is straightforward.

4. The proposed algorithm has been applied to a series of simulations and one real-world dataset.

### Weaknesses
 1. There seems to be no assumption sections. The acyclic assumption seems like a common assumption used in many causal discovery methods; however, it is more restricted in this paper as a cycle could be easily created if the causal relations exist for both $X^i_{0,s}$ to $X^j_{s,s+h}$ and $X^j_{s+h,s+2h}$ to $X^i_{s+2h,s+3h}$. Such pairs of causal relations are allowed in many causal discovery methods for time series, such as PCMCI. Therefore, though the authors claim that the proposed algorithm will not rely on the 'discrete-time' assumption, they did not discuss the impact of not assuming a time lag based on the 'discrete-time' assumption and the additional limitations from the acyclic assumption in this paper, compared to many previous causal discovery algorithms. Hence, the limitation discussion and comparison is not comprehensive. The acyclic assumption in this context is not very practical.

 2. Does the proposed CI test only work in the specific setting of this paper? Could it be utilized outside of this setting, for more general time series?

 3. In the limitations and requirements section, it is stated that the proposed algorithm far exceeds other existing causal discovery methods for time series data, which may not be the best way to frame the discussion. For instance, in part (b), it is mentioned that the proposed algorithm can handle confounders; however, there are already many algorithms that allow for confounders in time series, such as LPCMCI [1] and tsFCI [2]. Additionally, there are algorithms for non-stationary time series, such as CD-NOD [3], and those with special periodic patterns, such as PCMCI$_{\Omega}$ [4]. Therefore, it is difficult to conclude that the proposed algorithm far exceeds other related work, given different settings and assumptions.

 4. The number of baselines in the experiment results is limited for both causal discovery and the CI test. Please refer to the questions section for more details.

 5. Please correct me if I am mistaken, but it seems there is no computational complexity analysis or running time results provided.

 6. I may have misunderstood, but does the first selected interval of $[0, s], [s, h]$ have to start at the beginning? Based on line 233, there are two copies of vertex $V$. Does this imply $h = T$? If not, how many intervals are possible? If multiple intervals are allowed, can the acyclic assumption be relaxed since different time-ordered intervals resemble the concept of "time lag" in a 'discrete-time' setting?

 7. By intuition, is having $V_0$ and $V_1$ essentially a sub-sampling technique, where samples in $[0,s]$ and samples in $[s,h]$ are considered? The full causal graph that the algorithm aims to discover is restricted to this $V_0$ and $V_1$, and the estimated causal graph will be influenced by the intervals selected. Again, the full causal graph discussed here is different from the one in many causal discovery algorithms, referred to as the full time causal graph, which does not require sub-sampling and is more comprehensive. Therefore, this discussion needs to be handled with care.

### Questions
1. Could you briefly explain how to incorporate or partially incorporate PC and FCI into the proposed algorithm, given that both assume IID samples? Is any adjustment needed for non-IID samples?

2. Do KCIPT and SDCIT require IID samples as well? If so, a similar question arises as in item 1.

3. Are the simulated datasets used in the experiments 'continuous-time'? If so, how do you choose the discretization interval for PCMCI and other baselines that assume 'discrete-time'? Does using different discretization intervals influence their performance? How do you compare the output of PCMCI and the proposed algorithm, given that PCMCI includes time lags and may cause 'cycles' according to the definitions in this context?

4. Are you considering using more baselines designed for time series, particularly non-stationary time series? The number of baselines included is limited. Is there a specific reason for not using metrics such as F1 score, precision, and recall but just SHD?

5. Is there a power analysis for the conditional test, and how does it perform with different conditioning sets?

6. Could you explain how to obtain bi-directed edges as shown in Figure 4?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper makes contributions to causal discovery in stochastic dynamical systems. In particular, it introduces a novel framework of conditional independence constraints in SDE processes, which are then leveraged to provide a causal discovery (CD) algorithm. The authors also provide a conditional independence (CI) test to evaluate these constraints from data. The authors evaluate the CD algorithm on synthetic data and compare it to other state-of-the-art baselines. They also evaluate their CI test on synthetic data and in a small case study on stock trading pairs.

### Strengths
The paper is well-written and a pleasure to read. All theoretical claims are backed by careful proofs, and care is taken to ensure reproducibility of their experimental results. The authors openly address the limitations of their methodology,  and additional interesting results and discussions are provided in a well-organized and comprehensive appendix.

I believe the paper earns its place in the suite of tools for causal inference with time-series data from dynamical systems. In my opinion, this is a high-quality paper that deserves acceptance.

### Weaknesses
The only major weakness is the lack of real-world experiments for the causal discovery algorithm, which I understand to be the main contribution of the paper. Only the CI test has a real-world data experiment on a downstream task, which I found creative and is well-documented in the appendix.

Naturally, because we are in causal inference, real-world data with a ground truth can be difficult to find. However, I would like to point the authors to two recent papers that provide real-world data with a causal ground truth and whose settings appear to be a good fit for the method in this paper:

**“[Causal discovery in a complex industrial system: A time series benchmark](https://arxiv.org/abs/2310.18654)” by Mogensen et al. (2023).**

The paper presents a real-world dataset from a dynamical system with partially observed data. The authors provide a ground-truth causal graph (section 2.4). The paper comes with a website (https://soerenwengel.github.io/essdata) with links to the dataset and preprocessing code.

**“[The Causal Chambers: Real Physical Systems as a Testbed for AI Methodology](https://arxiv.org/abs/2404.11341)” by Gamella et al. (2024)**

The authors build two physical devices, one of which (wind tunnel) produces real-world, time-series data from a dynamical system. There is a causal ground-truth graph for this system (Figure 3), which the authors use to benchmark the PCMCI+ algorithm (Figure 6a). I believe this is an extension of one of your baselines (PCMCI), which makes me suspect your method is also applicable. The authors provide a well-documented [notebook ](https://github.com/juangamella/causal-chamber-paper/blob/main/case_studies/causal_discovery_time.ipynb) to download the dataset and reproduce the PCMCI+ experiment. Using your method may be plug-and-play in this case.

There may be other suitable real-world datasets, but I found none after this search. A real-world experiment for the main contribution of the paper (the causal discovery algorithm) would further elevate the value of the paper, and I would be happy to raise my score as a result. This is only a suggestion, and my decision to accept is independent of whether the authors do this or not.

### Questions
Some minor typos and unclear sentences:

- Line 421: “even in the settings it was tailored to” -> what was tailored to these settings, SigKer or the state of the art?
- For figure 2, maybe explicitly say which graph is the lifted graph (right) and which is G (left)
- Line 157: “is inapplicable” -> “it is inapplicable”?
- Some pedantic styling comments:
- Line 105: you have double parenthesis with the citation to Laumaann et al.
- Lines 170,200,420:  you appear to be using hyphens (-) instead of em dashes (---) for interjections. See the JMLR formatting guide (under dashes): https://www.jmlr.org/format/format.html

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach for causal discovery in stochastic processes modeled by stochastic differential equations (SDEs). The authors propose a conditional independence (CI) test based on signature kernels, which enables the identification of causal relationships in continuous-time dynamical systems, even under irregular or partially observed data. Key contributions include a causal discovery algorithm that leverages the directionality of time, as well as an efficient signature kernel-based CI test.

### Strengths
1. The paper is well-motivated, presenting a clear need for improved causal discovery methods within the context of stochastic processes.
2. Extensive experimental evaluations support the effectiveness of the proposed approach. The method demonstrates consistent superiority over several baseline models, underscoring its potential contributions to the field.

### Weaknesses
1.	The paper’s claims regarding diffusion-dependence cases may be somewhat overstated. In particular, for SDE models involving "driving noise" (i.e., cases where the diffusion coefficient depends on $X_t$), certain **causal graphs may not be identifiable from observational data**. See example 5.5 in [1]. Specifically, when the diffusion matrix is not constant or a simple function of time, but rather depends on the state variables ($X_t$), the identifiability of the underlying causal structure becomes problematic. This is because the observed data may not uniquely determine the drift and diffusion terms of the SDE, leading to multiple SDEs that are consistent with the same observed trajectories. In such cases, identifying the generator of the SDE model—so as to identify the post-interventional distribution—may be a more reasonable goal, as explored in [2] for linear SDEs. This may also provide some insight into the **diffusion-dependence** results presented in Table 1, where the proposed method shows comparatively lower performance.

[1] Hansen, Niels, and Alexander Sokol. "Causal interpretation of stochastic differential equations." (2014): 1-24.
[2] Wang, Yuanyuan, et al. "Generator identification for linear SDEs with additive and multiplicative noise." Advances in Neural Information Processing Systems 36 (2024).

2.	The section on signature kernels in Section 2 is mathematically dense and may be challenging for readers unfamiliar with the topic. Including more intuitive explanations would enhance accessibility. The current presentation assumes a level of familiarity with rough path theory and iterated integrals that many readers may not possess. A more gradual introduction, perhaps with illustrative examples of how different path features are captured by the signature transform, would be beneficial.
3.	Given the extensive use of mathematical notations, a summary table listing the key notations could be helpful for readers in following the manuscript’s developments. The paper introduces a number of symbols and mathematical objects, and a consolidated reference would greatly aid comprehension and reduce the cognitive load for the reader.

### Questions
The experimental setup involves setting small parameters for self-loops (e.g.,  $a_{ii} \sim  U([-0.5, 0.5])$), while the parameters influencing causal effects between different variables are set higher (e.g., $a_{ij} \sim U([-2,-1] \cup [1, 2])$). While I understand this may help to emphasize inter-variable causal relationships, practical applications may not always exhibit this distinction so clearly. Additionally, could the authors clarify whether errors related to self-loops are reported in the Structural Hamming Distance (SHD) results?

### Soundness
3

### Presentation
3

### Contribution
3
