# SOO-Bench: Benchmarks for Evaluating the Stability of Offline Black-Box Optimization

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Black-box optimization aims to find the optima through building a model close to the black-box objective function based on function value evaluation. However, in many real-world tasks, such as design of molecular formulas and mechanical structures, it is perilous, costly, or even infeasible to evaluate the objective function value of an actively sampled solution. In this situation, optimization can only be conducted via utilizing offline historical data, which yields offline black-box optimization. Different from the traditional goal that is to pursue the optimal solution, this paper at first discloses that the goal of offline optimization is to stably surpass the offline dataset during optimization procedure. Although benchmarks called Design-Bench already exist in this emerging field, it can hardly evaluate the stability of offline optimization, and mainly provides real-world offline tasks and the corresponding offline datasets. To this end, this paper proposes benchmarks named SOO-Bench (i.e., Stable Offline Optimization Benchmarks) for offline black-box optimization algorithms, so as to evaluate the stability of surpassing the offline dataset under different data distributions. Along with SOO-Bench, we also propose a stability indicator to measure the degree of stability. Specifically, SOO-Bench includes various real-world offline optimization tasks and offline datasets under different data distributions, involving the fields of satellites, materials science, structural mechanics and automobile manufacturing. Empirically, baseline and state-of-the-art algorithms are tested and analyzed on SOO-Bench. Hopefully, SOO-Bench is expected to serve as a catalyst for rapid developments of more novel and stable offline optimization methods. The code is available at https://anonymous.4open.science/r/SOO-Bench-9025.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SOO-Bench, a new benchmark for offline black-box (BB) model-based optimization (MBO) algorithms, which allows for evaluating the algorithm stability, i.e., the ability of an algorithm to consistently and continuously improve upon existing solutions from the offline dataset. The authors frame stability as one of the core objectives of offline BB-MBO. Offline here stands for the fact that the optimization has to rely only on historical data, without having access to evaluating new solution candidates; an important property of the offline data is usually a narrow distribution that is exhibited, possibly because of the bias induced in the data collection, such that the search space is not equally covered. This is at the same time a big challenge for the offline BB-MBO algorithms. SOO-Bench allows for customizing the narrowness of the offline data distribution and proposes a stability indicator (SI) to quantify how stable an algorithm is. The benchmark consists of various real-world tasks and datasets, including a possibility to vary the difficulty of the dataset by aforementioned customization. A range of algorithms (for unconstrained and constrained optimization) are empirically evaluated on the proposed benchmark, giving insights into their stability measures.

EDIT: I raise my score in light of the rebuttal.

### Strengths
The presentation of the paper is clear, with clearly stated contributions. The proposed stability indicator is a novel and useful measure for offline BB-MBO. A wide range of structurally and behaviorally different BB-MBO algorithms is evaluated, showing that they greatly vary in terms of stability.

### Weaknesses
The authors claim multiple times that black-box optimization requires building a surrogate model from the available data (samples and their evaluations). This is not always true, as black-box optimization is very often addressed by model-free methods, which are typically iterative randomized optimization heuristics (i.e., population-based algorithms), usually stemming from the evolutionary computation field. CMA-ES is one such example: an evolution strategy that does not learn a surrogate per se, but adapts the probability distribution by means of updating the covariance matrix. It may be helpful to clarify early in the paper that you are focusing specifically (or mostly) on model-based approaches, while explaining the inherent differences of the algorithms you are considering. Furthemore, the details of the evaluated algorithms could be made clearer; related to this, it is not clear how the algorithms are selected in the first place. It would be good to include a brief description of each evaluated algorithm, perhaps in an appendix, and explain their criteria for algorithm selection. This would help readers better understand the scope and rationale of the benchmark.

### Questions
Could the authors clarify what is meant by ‘a guided training agent model’ which assists classic baselines (I assume BO and CMA-ES)?
How are the algorithms that are benchmarked selected?
Finally, correcting for the OOD data is widely used in machine learning. It would be interesting to see how the value of the stability indicator of an algorithm would change after incorporating some of these techniques (e.g., for covariate shift) into the algorithm.

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
5

### Summary
This paper proposes a new benchmark suite for offline optimization. The two key contributions are (1) the ability to adjust the left-out portion (top m% and bottom n%) in the construction of the offline dataset; and (2) a new evaluation metric called SI that measures the stability of the recommendations. The paper shows that existing methods have varying performances when adjusting the dataset difficulty via controlling the parameters m and n. Several experiments also reveal the unstable behaviors of previous methods. Finally, compared to the Design-Bench (which is the default benchmark for offline opt until recently), the proposed benchmark also offers several new constrained optimization tasks.

### Strengths
The paper points out some clear weaknesses of the Design-Bench and proposes practical solutions to fix them. Empirical results point out some interesting insights and fill in missing gaps in current offline opt research. The paper is also clearly written and well-motivated.

### Weaknesses
 - I get the point of the SI metric, but don't quite agree with its formulation. Other than the thresholding with respect to the best offline value, how is it fundamentally different from computing variance? The way I see it, even if we incorporate the best offline value into the formulation, the SI metric alone is not enough to reflect performance. For example, let's say the best offline value is 0, a recommendation of 0.1, 0.1, 0.1 .... 0.1 will obtain better SI score than -0.1, 10, 10, 10, 10 .... A better way might be to treat the list of recommendations as a distribution, then perform hypothesis testing to check if the mean of this distribution is greater than the best offline value. The p-value would then indicate the performance level. It doesn't seem like there is a need to reinvent the wheel here.

-  One would expect higher difficulty to be achieved by leaving out high values in the offline dataset. This seems to be the case with the FS metric (table 5 in appendix). In the Design-Bench paper I think the bottom 30% of the entire dataset was selected as the offline data, which is likely harder than most of the settings presented. Even at this difficulty, the baseline methods are already quite competitive -- each new paper will report a different set of result (typically indicating that it is best). Personally, I think the focus should be on making the benchmark more challenging without severing limit the size of the offline dataset.

- Additionally, the fluctuating performance of baseline methods suggest that randomness plays a huge factor in offline opt. I would be more interested in designing benchmarks to eliminate this factor.

- Finally, can the authors elaborate on the technical challenge behind creating this baseline? To me, both the new metric and the customizable dataset construction seem like straight-forward wrappers that can be added to the Design-Bench, without remaking it from scratch.

### Questions
Please see above

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors present an innovative benchmark for evaluating the stability of offline data-driven optimization problems. They employ a customized data distribution approach that removes points near optimal and suboptimal values, and introduce a Stability Improvement (SI) indicator to measure stability. Their evaluation compares various offline optimization algorithms — six for unconstrained problems, plus four for constrained ones. The results reveal diverse performance levels across the benchmark's instances, showcasing its effectiveness in assessing stability.

### Strengths
- The paper provides key insights into the stability of offline optimization methods, advancing this emerging field.
- It is clearly written and well-structured.
- The related work section is thorough, and the introduction effectively contextualizes the research.
- The benchmark is detailed, with clear explanations of its tasks and datasets.
- Open-source availability enhances interpretability and reproducibility, backed by comprehensive experiments.

### Weaknesses
 - There appear to be some typos, specifically "TTDEEA" in Table 2 and Section 6.2, and "TTDEA" in Appendix C. 

- For the new SI indicator, how should we best assess an algorithm's performance? In which cases would a lower FS be advantageous, and when should we prioritize a higher SI?

- I also have a question regarding the paper’s submission history. I was one of the reviewers for its NeurIPS submission this year, where I saw that all reviewers ultimately gave positive scores. However, I was surprised to see that the authors decided to withdraw the paper. Could you share the reason for this decision? Additionally, I noticed that some specific revisions the authors intended to make during the NeurIPS rebuttal are not reflected in the current ICLR submission.

### Questions
- There appear to be some typos, specifically "TTDEEA" in Table 2 and Section 6.2, and "TTDEA" in Appendix C. 

- For the new SI indicator, how should we best assess an algorithm's performance? In which cases would a lower FS be advantageous, and when should we prioritize a higher SI?

- I also have a question regarding the paper’s submission history. I was one of the reviewers for its NeurIPS submission this year, where I saw that all reviewers ultimately gave positive scores. However, I was surprised to see that the authors decided to withdraw the paper. Could you share the reason for this decision? Additionally, I noticed that some specific revisions the authors intended to make during the NeurIPS rebuttal are not reflected in the current ICLR submission.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes SOO-Bench, a benchmark suite to promote stable offline black-box optimization. Authors integrate several real offline optimization tasks and provide offline optimization tasks with different customizable difficulties by narrowing the dataset distribution. Besides, authors introduce an indicator called Stability Improvement (SI) to quantify the stability of the algorithms and conduct experiments to evaluate algorithmic stability and optimality.

### Strengths
1. This paper is claimed to be the first work to disclose stability as one of the core objectives in offline black-box optimization.

2. The paper integrates multiple real-world tasks with a unified API.

3. In the experiments, authors conduct comprehensive evaluation on state-of-the-art baselines and provide thoughful insights.

### Weaknesses
1. Narrowing data distribution by removing top and bottom solutions cannot address the uneven cover in real-world task dataset. As mentioned in the paper, personal biases, preferences for certain parameter settings, or prior knowledge might lead to uneven sampling in solution space, not the fitness space. Removing top and bottom solutions cannot reflect such situations since the solutions in the middle may still evenly cover the solution space, and the solutions sampled unevenly may also cover both top and bottom solutions. Therefore, narrowing data distribution by removing top and bottom solutions cannot address the uneven cover in real-world task dataset, perhaps narrowing the distribution in solution space could be better.

2. The Stability Improvement indicator proposed in this paper is imperfect in measuring the algorithm stability. According to Equation (2), the way to obtain highest SI is to achieve a solution better than the best solution in the offline dataset and at the first step and retain it till the end. In this case the SI can be 1, but such precocious behavior can lead to poor performance (i.e., COMMs in the experiments has high SI and poor performance). If we consider SI as an indicator only about stability and has nothing to do with performance, another case where the performance keeps increasing and achieves the best performance at the last step (i.e., Algorithm A's curve before achieving objective value a in Figure 2(b)), its SI can be lower than some unstable algorithms. However, we know that in this case, it is a stable algorithm with stable performance improvement along the optimization. In a word, the proposed SI cannot reflect the algorithm stability.

### Questions
See weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2
