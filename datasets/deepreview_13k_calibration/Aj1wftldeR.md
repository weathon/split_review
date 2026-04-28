# D5RL: Diverse Datasets for Data-Driven Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Offline reinforcement learning algorithms hold the promise of enabling data-driven RL methods that do not require costly or dangerous real-world exploration and benefit from large pre-collected datasets. This in turn can facilitate real-world applications, as well as a more standardized approach to RL research. Furthermore, offline RL methods can provide effective initializations for online finetuning to overcome challenges with exploration. However, evaluating progress on offline RL algorithms requires effective and challenging benchmarks that capture properties of real-world tasks, provide a range of task difficulties, and cover a range of challenges both in terms of the parameters of the domain (e.g., length of the horizon, sparsity of rewards) and the parameters of the data (e.g., narrow demonstration data or broad exploratory data). While considerable progress in offline RL in recent years has been enabled by simpler benchmark tasks, the most widely used datasets are increasingly saturating in performance and may fail to reflect properties of realistic tasks. We propose a new benchmark for offline RL that focuses on realistic simulations of robotic manipulation and locomotion environments, based on models of real-world robotic systems, and comprising a variety of data sources, including scripted data, play-style data collected by human teleoperators, and other data sources. Our proposed benchmark covers state-based and image-based domains, and supports both offline RL and online fine-tuning evaluation, with some of the tasks specifically designed to require both pre-training and fine-tuning. We hope that our proposed benchmark will facilitate further progress on both offline RL and fine-tuning algorithms. Website with code, examples, tasks, and data is available at \url{https://sites.google

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission proposes a new benchmark for offline RL algorithms.
The benchmark modifies previous domains or adds new domains to evaluate unsolved challenges in offline RL.
Experiments demonstrate that existing offline RL algorithms do not perform well for the tasks in the benchmark.

### Strengths
The introduction of new domains and offline datasets in the benchmark offers the community a broader range of choices, potentially supporting the easier development of offline algorithms.

### Weaknesses
It is unclear whether promoting the use of this benchmark within the community will indeed accelerate offline RL algorithm development.
- the benchmark does not *specifically* address current challenges in offline RL. While the paper broadly covers various challenges of offline RL,
  - some of these challenges could be already observed in previous benchmarks. Evaluating temporal compositionality seems  possible using previous benchmarks (D4RL Maze2D, AntMaze, FrankaKitchen-Mixed, Calvin). The proposed benchmark has less diversity than D4RL, and different levels of data distribution are also discussed in D4RL. However, the text does not explicitly claim why using this new benchmark is better than using previous benchmarks for each challenge.
To encourage using this benchmark, the paper should address questions like: when to choose this benchmark? Are previous works successful on prior benchmarks likely to fail on this new benchmark specifically due to one of specific challenges?
  - addressing offline-to-online learning adaption appears to be incremental. As almost all previous offline RL benchmarks are based on simulation environment and rule-based reward function, implementing online fine-tuning on the top of exisiting benchmarks is feasible.
  - More information or resource should be provided to challenge the community to solve the image observation version of Franka Kitchen. Is the failure of existing works attributed to the incompleteness of offline RL algorithms or the lack of image representation learning? Can this task be intuitively completed solely with the provided offline data? If not, is there an alternative data source that the community can leverage to address this challenge?

- Even if the benchmark doesn't specifically address one of those challenges, it can still be beneficial to have a domain with a collection of challenges if it is important to solve the domain. However, the provided domains are not significantly more realistic or different compared to existing tasks, making them less of an important target domain that the community aims to solve.

### Questions
Questions are included in weakness section.

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes D5RL, a novel benchmark that aims to facilitate the development of offline RL algorithms. The benchmark focuses on robotics environments based on real-world robotic systems. To address the drawbacks of existing benchmarks, D5RL includes a suite of tasks that pose different challenges for offline RL algorithms, including learning from various (sub-optimal) data distributions, image observations, temporal compositionally, generalization to randomized scenarios, and offline-to-online settings. Experiments show that existing methods that perform well on standard benchmarks fail to achieve meaningful performances on D5RL.

### Strengths
Overall, I think the paper is a good attempt to replace existing benchmarks that are likely saturated, and having a new benchmark would have a high impact on the offline RL community. The paper is well structured, where it first motivates the need for a new benchmark, presents a list of criterion for it, and proceeds to describe the benchmark and how it satisfies the criterion. The datasets and tasks are also well explained.

### Weaknesses
My biggest concern about the paper is the benchmark results section.
- My impression from Tables 1 and 2 is the proposed benchmark is too difficult for existing offline RL methods to achieve meaningful performances, since most methods except BC and IQL have near-zero returns. While having a challenging benchmark is good, a too-challenging benchmark will not provide much signal to improve the performance of current methods. It's unclear if the near-zero returns are due to the methods failing to learn anything or if the reward function is too sparse, making it difficult to observe any progress. The lack of variance in the reported results also raises concerns about the robustness of these findings.
- The paper is currently lacking ablation studies to understand what components of the benchmark are challenging and/or why current algorithms fail. For example, it would be useful to know if the difficulty stems from the visual complexity, the long time horizons, the sub-optimal nature of the datasets, or a combination of these factors. Without this analysis, it's hard to pinpoint the specific bottlenecks.
- I would like to see a random policy as a simple baseline. I wonder if the benchmarked methods even do better than a random policy. It's crucial to establish that the reported results are not simply due to random chance.
- Why is there such a big gap between IQL and other similar methods such as CQL and TD3+BC? These methods often perform very similarly in D4RL, at least in the locomotion tasks. The discrepancy suggests that there might be some hidden factors in the benchmark design that favor IQL or that the implementation of other methods is not optimal for this specific benchmark.
- The paper did not choose a good collection of RL algorithms to benchmark. There are too many value-based methods, while return-conditioned methods (or generative methods) such as DT [1] and DD [2] are not mentioned. These methods have been shown to surpass value-based methods in sparse-reward and long-horizon tasks. Online DT [3] is also a good method for the offline-to-online setting.

Other comments:
- Section 5.2 states that the goal of the Frank Kitchen environment is to study offline RL and online fine-tuning, but the following text does not mention how the proposed task facilitates online finetuning.

### Questions
- Is there only one dataset for the legged locomotion domain? Can we have multiple datasets with various qualities similar to D4RL?
- How accurately it tracks the target speed of 0.75 m/s --> How is accuracy measured here? Is it the l2 distance between the actual and target speed?
- Is hiking a sparse-reward task?
-

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new dataset benchmark for offline and online fine-tuning RL methods. The paper comprised of tasks which are of great interest to real-world robotics such as locomotion and manipulation. Also provides the diversity in domain of representation, as it covers both state-space and image domains.

### Strengths
* The tasks in the dataset capture various challenges that are encountered in real-world robotics such as extrapolating policies, changes in environment, different viewpoints, etc.
* Both image-based and proprioceptive modes of states are covered across settings and tasks.
* The datasets are gathered for platforms that are embodied in the real-world and hence will allow for sim-to-real transfer to some extent.

### Weaknesses
 * Limited number of tasks for the A1 legged locomotion. Tasks such as jumping, obstacle avoidance, etc. can also be of interest in this.
* No evaluation of any of these tasks/settings in the real world. To what extent can the models trained on these datasets transfer to the real-world?

### Questions
Don't have any major questions

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new benchmark for offline RL, which includes additional domains (such as legged locomotion and robotic manipulation) and new modalities (such as visual observation).

Several SOTA methods are also evaluated in this new benchmark, under both the pure offline setting and the online finetuning setting. Low performance is observed across domains and tasks, showing the potential space for improvements for current RL algorithms.

### Strengths
- This work improves D4RL by introducing some new domains and new modalities. These efforts could be helpful toward deployable offline RL, mainly for robotics.
- The benchmark provides the evaluation results for online fintuning, which has its meaning. Most of works in offline RL only utilize offline data, while neglecting the benefit of a small portion of online data to address the distribution shift issue.

### Weaknesses
I appreciate the works from authors to push forward the benchmarking in Offline RL. However, there still exist some critical issues for this work, that make me tend to give a strong reject:
- **The proposed benchmark does not include much more diverse domains compared to D4RL.** I think with some past works such as RoboMimic [1] and some recent works such as RL-ViGen [2], similar and even more diverse benchmarks could be easily made, by running RL agents to collect offline datasets. The manipulation tasks, while including different objects, still revolve around similar pick-and-place actions. The core challenge remains the same, lacking the diversity seen in other benchmarks that incorporate more varied tasks such as tool use or complex assembly. The inclusion of different robot arms is a minor variation, not a fundamental shift in task complexity or diversity. The continuous distribution shifts, while present, are not as significant as those found in more diverse environments, such as those with dynamic obstacles or changing goals.
- **Low technical contributions.** This is fine, but I think for papers qualified for ICLR, low-technical papers should possibly provide some new insights. The paper primarily focuses on data collection and benchmarking, without introducing novel algorithms or analysis techniques. While benchmarking is valuable, the lack of technical depth makes it less impactful for a top-tier conference like ICLR. The insights gained from the benchmark are limited, as the evaluation results primarily show the failure of existing methods, without providing a clear direction for improvement.
- **Possibly unfeasible settings.** As shown by evaluation results, most SOTA algorithms are not working well on this benchmark. This could possibly be attributed to the difficulties of the task, but from my perspective, there could also be some key factors that are not right, such as the problem formulation and the framework of offline RL. (This point might be not significant, but it is my personal concern about the benchmark.) The poor performance of SOTA algorithms raises concerns about the suitability of the benchmark for evaluating offline RL methods. It is unclear if the benchmark is truly representative of real-world challenges or if it introduces artificial difficulties that hinder the performance of existing algorithms. The lack of clear problem formulation and the framework of offline RL makes it difficult to pinpoint the root cause of the poor performance.
- **Overclaim of the paper title**. This work names the newly proposed benchmark as D5RL, which is obviously following the name of D4RL. However, this could be misleading for the entire community to keep pursuing the limited improvements on a new but essentially similar benchmark.

### Questions
See `weakness`.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
