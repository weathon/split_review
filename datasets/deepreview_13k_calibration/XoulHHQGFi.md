# IntersectionZoo: Eco-driving for Benchmarking Multi-Agent Contextual Reinforcement Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Despite the popularity of multi-agent reinforcement learning (RL) in simulated and two-player applications, its success in messy real-world applications has been limited. A key challenge lies in its generalizability across problem variations, a common necessity for many real-world problems. Contextual reinforcement learning (CRL) formalizes learning policies that generalize across problem variations. However, the lack of standardized benchmarks for multi-agent CRL has hindered progress in the field. Such benchmarks are desired to be based on real-world applications to naturally capture the many open challenges of real-world problems that affect generalization. To bridge this gap, we propose \textit{\ourEnv{}}, a comprehensive benchmark suite for multi-agent CRL through the real-world application of cooperative eco-driving in urban road networks. The task of cooperative eco-driving is to control a fleet of vehicles to reduce fleet-level vehicular emissions. By grounding \ourEnv{} in a real-world application, we naturally capture real-world problem characteristics, such as partial observability and multiple competing objectives. \ourEnv{} is built on data-informed simulations of 16,334 signalized intersections derived from 10 major US cities, modeled in an open-source industry-grade microscopic traffic simulator. By modeling factors affecting vehicular exhaust emissions (e.g., temperature, road conditions, travel demand), \ourEnv{} provides one million data-driven traffic scenarios. Using these traffic scenarios, we benchmark popular multi-agent RL and human-like driving algorithms and demonstrate that the popular multi-agent RL algorithms struggle to generalize in CRL settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
**Overview**  
This work proposes a new benchmark for testing the generalizability of MARL algorithms across different MDP settings. With the background of reducing $CO_2$ emission by controlling vehicle fleets, progress on this benchmark may potentially generate real-world impact and advance the development of MRL. 

**Method**  
Specifically, intersections were collected for 10 major cities in the US and reconstructed in the SUMO simulator with a set of configurable parameters (context) like vehicle throughput, speed limit, temperature, the ratio of autonomous cars, and so on. The parameter distribution is provided by referring to literature from the transportation department. Thus, sampling parameters from these distributions allow the simulator to build intersection scenarios similar to its real-world counterpart. Each parameter combination forms a special MDP, and thus training agents with scenarios sampled from the same distribution allows benchmarking in-distribution performance. Testing agents in scenarios built with another parameter distribution can reflect the algorithm's OOD performance.

**Experiment**   
The experiment shows that the current SOTA MARL method struggles to do even in-distribution generalization, indicating there is a large room for improvement.

### Strengths
1. It is a good application for MARL researchers to study how to build algorithms to further reduce exhaust emissions and make a real-world impact. 
2. The scenarios database is large. With realistic context distribution, IntersectionZoo is a good place to study the generalizability of algorithms. Also, the whole system including the intersection data, simulator, metric, and training framework is built reasonably and solidly.
3. As an open-sourced benchmark, the code is of good quality with documentation included. Seems it is ready for use.

### Weaknesses
1. The writing is poor. The experiment figures are hard to understand. Specifically, what does the total count mean? Though I can roughly infer it, it would be better to explain it in the paper. For the benefit percentage, does 0.5 means 0.5% or 50%. If it is 0.5%, it seems the emission doesn't change a lot by switching to MARL control, and the key is that MARL agents can not achieve the same level of throughput as human drivers. However, it seems GCRL agent is close to human drivers' performance. I suggest giving more analysis and explanation to these figures. It can be done in the captions since I found the captions of Figure 5 and Figure 6 are simple copy-paste. Also, is it possible to provide more visualizations in the appendix or even provide a video? So readers can know how different the map topologies and vehicle distributions are for these cities. I can not imagine a large dataset from pure text.
2. More experiments or results are needed. Though the experiments show that MARL can not generalize well, we don't know if it is due to the algorithm itself or if the task is too difficult to learn for RL agents, i.e. improper reward function and observation or MDP definition. One way to clarify this is to provide training performance as well. It needs to be proved first that the MARL can overfit the training scenarios and exceed human driver performance. Then we can confirm that the simulation design is appropriate, so MARL agents have the chance to surpass humans, and the failure on the test set is indeed due to poor generalizability. Also, parameters are fixed for the experiments like the adoption rate, which is 1/3. Did the authors conduct experiments to see which factor affects the performance most? I believe the adoption rate is an important factor since the MARL performance would be largely influenced by the population size. Also, a baseline can be added to use the IDM vehicle control these CVs to see if the MARL can outperform this simple rule-based baseline at least at training time. With such a trend, we can conclude it shows some signs that MARL can achieve better performance, and thus work on this benchmark is promising.

### Questions
1. How would the temperature and humidity affect the policy behavior? For example, is it better to drive at low speed in summer to reduce the CO2 emission? But it would reduce the throughput right?
2. As far as I know, the OSM data only provides the location of the traffic light and doesn't tell which lane it controlls. How does this information be completed in IntersectionZoo?
3. Type: Appendix, table 3. evaluation -> training

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper the authors introduce a new benchmark for multi-agent reinforcement learning (MARL) called IntersectionZoo, designed to address the cooperative eco-driving task within urban networks. The objective of cooperative eco-driving is to control a fleet of vehicles at signalized intersections to minimize fleet-wide emissions with minimal impact on individual travel times.

The authors discuss the benchmark in the context of Multi-Agent Contextual Reinforcement Learning (MA-CRL) and highlight how IntersectionZoo is purposefully tailored to generate multiple scenario variations (i.e., contexts) and evaluate the generalization capabilities of MA-CRL agents across such variations. Specifically, IntersectionZoo addresses a range of contextual factors, including intersection configuration, vehicle type distribution, fuel type distribution, human driver models, weather conditions, eco-driving adoption rates, peak and off-peak traffic patterns, among others. The benchmark leverages data across 10 cities and over 16,000 signalized intersections and is built on open-source software, e.g. SUMO for microscopic traffic modeling, and RLLib for RL training.

### Strengths
I resonate with the overall purpose of this work: bridging the gap between RL research (focused on benchmarks and generality of algorithms) and impactful, real-world applications. The paper is generally well-written and straightforward to follow. The authors thoroughly compare their benchmark with a comprehensive body of literature in the field. Based on my understanding, this work entails significant data collection and processing, which could provide substantial benefits to the broader transportation research community.

### Weaknesses
In my opinion, the primary limitation of this work is its relatively narrow contribution to the broader RL, or specifically multi-agent RL, community. Although the authors claim that IntersectionZoo aims to serve as a novel standardized benchmark for MA-CRL research, many of the benchmark’s design decisions and characteristics are highly tailored to cooperative eco-driving and to the specific problem formulation adopted within this work. While evaluating generalization performance across different scenario characteristics is important for this application, it seems questionable to assert that results and insights on IntersectionZoo would extend to MA-RL research more broadly. This, to me, somewhat undercuts the fundamental purpose of a benchmark.

For instance, while scenario factors vary, the overall application and formulation remain fixed. This impacts algorithmic choices as well, such as the mandatory choice of a continuous action space (acceleration of the controlled vehicles), a specific reward function design, limited environment scale (restricted to single intersections), predefined driver models, and no significant uncertainty sources. These are just a few examples.

To the best of my understanding, this work would have greater impact if it concentrated more on the application side—namely, contributing novel algorithms to address a critical problem—rather than positioning this benchmark to generate deep insights into MA-RL algorithm development. 

Furthermore, the experimental analyses in this work need _considerable_ improvement. The authors provide a brief comparison of PPO, DDPG, MAPPO, and GCRL, concluding that these algorithms fail to generalize and perform poorly across all tested conditions. While experimental evaluation may not be the core focus of this paper, a thorough and insightful assessment of established MA-RL algorithms is essential in order to evaluate the usefulness of a benchmark. Is it the case that no algorithm performs adequately in any of the examined scenarios? The authors should consider expanding the experimental section by exhaustively benchmarking popular RL algorithms on the proposed benchmark, with in-depth evaluation and analyses.

### Questions
- Can the authors elaborate on how IntersectionZoo is expected to benefit the broader MA-RL community? What features of the cooperative eco-driving task are common to other MA-RL tasks? To what extent the insights obtained on IntersectionZoo can be extended to broader MA-RL settings? More specifically, could the authors suggest particular MA-RL domains where insights from IntersectionZoo are likely, or unlikely, to transfer? Providing both positive and negative examples would help the readers with assessing whether IntersectionZoo could serve as a relevant benchmark for their own purposes.

- Can the authors provide a more extensive experimental analysis of MA-RL algorithms on this benchmark? If no algorithm performs well on the benchmark, what are the underlying causes for such a performance gap? For example, IntersectionZoo focuses on two performance metrics: average emission benefits and average intersection throughput benefits. While these metrics are interesting from a domain-driven perspective, the paper would benefit from considering additional algorithm-driven metrics relating to, e.g., sample efficiency, stability of training, etc. Moreover, a qualitative visualization of the resulting policy would further improve the experimental assessment.

### Soundness
2

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
The paper proposes a benchmark suite, IntersectionZoo, for contextual reinforcement learning evaluation. The suite is designed based on a complex real-world task, i.e., cooperative eco-driving at signalized intersections. This paper well summarizes the recent work related to RL benchmark. Several experiments are conducted to test some popular multi-agent RL algorithms and show that all the adopted algorithms perform poorly on generalization. The open-source code is also provided to facilitate the community.

### Strengths
The originality is good. This paper addresses the problem of contextual reinforcement learning by creating a comprehensive benchmark for eco-driving simulation.

The problem formulation is presented clearly and in detail. 

The literature review offers an extensive and in-depth overview of related work.

The proposed IntersectionZoo benchmark can be a boost for contexture RL research.

Open-source code is provided to support the research community.

### Weaknesses
* The main content seems to exceed the page limit – the 8. The Reproducibility Statement is on the 11th page.

* PPO and DDPG are not specifically for multi-agent RL but are only used with independent agents. It seems not reasonable to choose these two algorithms for testing. Besides, for systematicity and productivity in generalization tests, the authors only use PPO and DDPG for evaluation, which is confusing.

* From your experiments, it’s hard to get the conclusion in Line 532 that “the popular multi- agent RL algorithms struggle to generalize in CRL settings” since only two MARL-based methods, i.e., MAPPO and GCRL, are adopted for evaluation, and just on the in-distribution generalization.

* Given the unsatisfactory results of the chosen multi-agent RL algorithms on this benchmark, it would be better to briefly review the latest multi-agent RL to justify why you chose PPO, DDPG, MAPPO, and GCRL for evaluation.

* What does the “baseline” refer to in “Both DDPG and PPO fail to systematically generalize; baseline performs better in almost all cases” in Line 497?

### Questions
What does the “baseline” refer to in “Both DDPG and PPO fail to systematically generalize; baseline performs better in almost all cases” in Line 497?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes IntersectionZoo, a comprehensive benchmark suite for multi-agent CRL through the real-world application of cooperative eco-driving in urban road networks. The authors ground IntersectionZoo in real-world applications, and capture real-world problem characteristics that are neglected in previous datasets, including partial observability, and multiple competing objectives. Also, IntersectionZoo covers 16,334 signalized intersections derived from 10 major US cities, enabling the testing of policy transfer between different cities. Using traffic scenarios in the proposed dataset, the authors benchmark various popular multi-agent RL and human-like driving algorithms and demonstrate their performance in Eco-driving.

### Strengths
1. This paper focus on benchmarking the task of cooperative Eco-driving. The idea of this task is to control a fleet of vehicles to reduce fleet-level vehicular emissions. The task sounds interesting and is absolutely beneficial to reduce air pollution in the era of global climate change.
2. The authors ground IntersectionZoo in real-world applications, and capture real-world problem characteristics that are neglected in previous datasets, including partial observability, and multiple competing objectives.
3. The author model a wide range of major factors affecting vehicular exhaust emissions, including temperature, road conditions, travel demand, making the traffic scenarios provided in IntersectionZoo more realistic and reliable.
4. The dataset is of substantial volume, including one million scenarios simulated in 16,334 signalized intersections derived from 10 major US cities. This enable robust testing results of a given algorithm.

### Weaknesses
1. In this paper, the framework of IntersectionZoo looks sophisticated, but there lacks experimental results that illustrate how precise the simulation results are. Can they reflect the real-word vehicular exhaust emissions precisely?
2. When benchmarking popular algorithms with IntersectionZoo, the authors show the performance of some algorithms from various aspects. However, what is the rationality of these results? How do they strengthen the contribution of the proposed dataset?
3. The authors test the performance of some algorithms from various aspects with IntersectionZoo, but there lacks the testing results with other comparable benchmarks (like the ones in Table 1). How do the results on other benchmarks differ from the results on IntersectionZoo? Will the differences illustrate the advantage of IntersectionZoo?

### Questions
1. Could you please provide some experimental results to verify that IntersectionZoo can reflect the real-word vehicular exhaust emissions precisely?
2. Could you please explain the rationality of your benchmarking results? How do they strengthen the contribution of the proposed dataset?
3. Could you please provide some major testing results of the popular algorithms on other existing benchmarks? How do the results on other comparable benchmarks differ from the results on IntersectionZoo? Will the differences illustrate the advantage of IntersectionZoo?

### Soundness
3

### Presentation
3

### Contribution
3
