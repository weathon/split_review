# SteBen: Steiner Tree Problem Benchmark for Neural Combinatorial Optimization on Graphs

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
The Steiner Tree Problem (STP) is an NP-hard combinatorial optimization problem with applications in areas like network design and facility location. Despite its importance, learning-based solvers for STP have been hindered by the lack of large-scale, diverse datasets necessary to train and evaluate advanced neural models. To address this limitation, we introduce a standardized dataset comprising over a million high-quality instances with optimal solutions, spanning various problem sizes and graph structures. Our dataset enables benchmarking of neural combinatorial optimization methods across both supervised and reinforcement learning paradigms, encompassing autoregressive and non-autoregressive inference approaches. Our experiments show that supervised learning excels in in-distribution settings, while reinforcement learning generalizes better to unseen problem sizes, highlighting a trade-off between solution quality and generalization. We compare NCO methods across different STP scales and graph types, and demonstrate that solvers trained on our datasets generalize well to real-world instances without fine-tuning, proving its practical utility. We hope this benchmark promotes further STP research and advances NCO techniques for broader combinatorial optimization challenges.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents SteBen, a benchmark for the Steiner Tree Problem (STP) that provides a large, diverse dataset for training and evaluating neural combinatorial optimization (NCO) methods. SteBen compares supervised and reinforcement learning approaches and shows potential for NCO models trained on synthetic data to generalize effectively to real-world STP instances.

### Strengths
1. comprehensive evaluation frameworks, which compares four NCO method types (autoregressive/non-autoregressive, supervised/reinforcement learning). 
2.  The paper is well-structured, providing clear definitions of the dataset, benchmark tasks, and each NCO method used.

### Weaknesses
1. A notable weakness is the limited novelty in the methodological approach, as the paper largely applies existing NCO techniques to the Steiner Tree Problem (STP) without introducing new algorithms or solution strategies specifically tailored to STP’s unique challenges. The adaptation of methods primarily designed for the Traveling Salesperson Problem (TSP) to STP, a problem with distinct structural characteristics, raises concerns about the suitability and performance of these methods. Specifically, the core difference lies in the solution space: TSP seeks a Hamiltonian cycle, while STP aims for a minimum-cost tree connecting a subset of nodes. This fundamental difference necessitates tailored approaches rather than direct application of TSP-centric methods.
2. the paper could benefit from further exploration of scalability, especially in handling large graphs. The evaluation of the proposed benchmark and methods on graphs with up to 1000 nodes, while a step forward, does not fully address the scalability challenges inherent in real-world STP instances, which can involve much larger networks. The absence of analysis on how these methods perform with increasing graph size, particularly in terms of computational cost and solution quality, limits the practical applicability of the benchmark.

### Questions
1. All these methods used in this paper are for TSP, why use these methods for benchmarking Steiner Tree Problem?
 These 2 problems have distinct structural characteristics and solution requirements. TSP methods focus on finding a closed tour visiting all nodes exactly once, whereas STP requires finding a minimum-cost tree connecting a terminals.
2. What's advantage over the dataset used in the SCIP-Jack paper?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present SteBen, a benchmark dataset of randomly generated Steiner Tree Problems (STP), and evaluate several approaches in various settings. The authors evaluate recent learning-based approaches that use autoregressive, and non-autoregressive solution generation schemes as well as reinforcement learning (RL) or supervised learning (SL) training paradigms. Additionally, the authors evaluate the traditional baselines of an exact solver and a 2-approximation heuristic. Lastly, the authors compare approaches based on generalization to larger instances, generalization to real-world instances from another benchmark dataset, and sample efficiency of the two most competitive approaches, one supervised and one using RL.

### Strengths
The main strength of the work is providing a benchmark dataset of interesting problems for an area that has been understudied in the space of ML for combinatorial optimization, Steiner Tree Problems.

Additionally, the authors thoroughly evaluate several recent and reasonable learning-based heuristics, adapting them to STP instances. 

The authors also evaluate approaches in terms of generalization to larger and out of distribution instances, demonstrating tradeoffs between various approaches which has been understudied in the previous work.

Another strength is that this paper seems to demonstrate that most of the learning-based approaches don't seem to outperform the non-learning baseline, leaving room for future work. It would be interesting to investigate that further to determine how different methods compare to SCIP-Jack or other non-learning approaches.

The paper itself is well motivated and the authors engage well with the literature on learning for combinatorial optimization and previous STP benchmarks.

### Weaknesses
One main area for improvement is the evaluation of non-learning baselines. It would be helpful to more comprehensively report results for non-learning baselines. For instance, it would be helpful for table 1 to also include information for SCIP-Jack given a very short time limit comparable to some of the highlighted learning approaches to see how well the internal solver heuristics perform without the need for proving optimality. For instance, on STP10, SCIP-Jack gives the optimal solution in 3 minutes, but is it possible that it found solutions better than the PtrNet sampling approach in the 43s of time that PtrNet took? Similarly, for STP100, it takes 1h for SCIP-Jack to find the optimal solution, but is it possible that it finds higher quality solutions than the baselines which take less time? Note that the highlighted rows of DIFUSCO both take longer than SCIP-Jack while not obtaining optimality.

It would also be helpful to discuss runtime vs performance potentially in a plot. It seems that SCIP-Jack provides a good tradeoff between runtime and performance compared to the learning-based approaches. It might help to visualize that performance tradeoff.

In a similar vein, it seems that some approaches may generate intermediate feasible solutions. It would be interesting to compare the approaches in terms of gap over time as they progress through the “solving” process. Understanding how quickly different methods “close the gap” might give insight into how performant they are for various levels of time cutoff.

It is unclear how difficult these instances are, it seems that SCIP-Jack solves all but the largest instances in between 3 and 5 minutes. Additionally, is it the case that SCIP-Jack takes exactly 1 hour on the largest instances? Is it that 1hr is the time limit? Or it actually takes an average of 1.0 hr (considering that DIFUSCO takes 2.4hr and 14.2hr.

Given that the benchmark consists of Erdos Renyi, Watts Strogatz, random regular, and grid graphs, it would be interesting to see the breakdown of performance by these various types to identify where different methods succeed and fail and if anything can be interpreted from the results. It is currently unclear how the results from the different graphs are aggregated in table 2 and 3.

The paper is missing some experimental details in the text such as how the metrics are computed and what subsets of data are considered during training and testing for the various experiments. 

Minor comments:
Line 137: Quato -> quota

It is a bit unclear what is meant by the example in figure 1, it seems that TSP can also exhibit the global dependence property in that moving one node slightly may require that the full tour needs to be recomputed. Similarly, it can sometimes be the case that moving a node slightly for STP may not change the edges.

### Questions
How well do non-learning baselines like SCIP-Jack perform on these instances when in a similar setting of finding heuristic solutions (rather than exact solutions)?

Why is SCIP-Jack not present in table 2 and 3? It seems performant in table 1 and it should be able to run on those instances as well. 

How is the evaluation of SCIP-Jack performed? Is it given a time limit for the specified time? Or is it just asked to solve to optimality?

Could you compare SteBen more with the related Quota and Respack datasets? It seems that removing the costs and capacities would result in problems applicable here. Are there any different considerations that they had compared to SteBen?

It is a bit difficult to interpret table 2. What is the relative gap and how is it measured? Is it that a gap of 0 is optimal? Why are there several examples with relative gap of 1? What does the blue highlighting mean? Additionally, what graphs are used here for testing? All of the different graphs combined? Do any of the graph distributions generally yield “harder” or “easier” instances and if so, is it the case that some methods may outperform others on “harder” instances while underperforming others on “easier” instances?

### Soundness
2

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
This paper presents a new benchmark, featuring a synthetic dataset and multiple baseline algorithms tailored for the Steiner Tree Problem. The dataset encompasses millions of instances that vary in size and graph structure. Additionally, the authors also conduct extensive experiments to assess the performance of various baseline algorithms on the newly generated dataset.

### Strengths
1. The paper is well-organized, with a logical flow.
2. The chosen baseline algorithms span a comprehensive range of categories, covering supervised learning, reinforcement learning, and both autoregressive and non-autoregressive models.
3. The evaluation of baseline algorithms is thorough, incorporating experiments across in-distribution, out-of-distribution, and real-world scenarios.

### Weaknesses
1. The distinctiveness of the instance generation approach compared to existing methods is not clear. If the generation is merely an aggregation of existing techniques, the contribution may not be sufficient for a top-tier conference such as ICLR.
2. The specific benefits and unique characteristics of the proposed dataset are not clearly highlighted. In lines 56-58, the authors note that existing datasets are limited in sample number, but this could potentially be mitigated with data augmentation methods, such as perturbation. Additional comparisons and analysis would help clarify the dataset’s advantages.
3. There are residual comments and colored highlights in the manuscript from the revision process. For example, lines 193, 851–960, and 1018–1036. The authors should ensure that all revision markers and annotations are removed in the final version to maintain a clean and professional presentation.
4. On the data side, it will be more helpful to have a more in-depth analysis about the instances you have generated. Please classify the result dataset in more subcategories (or attributes), such as dense/sparse, robustly connected or loosely connected, how easy it is to be solved by SCIP-jack or by an MILP solver as is and how easy they are after pre-solving techniques. These attributes are in addition to the input parameters you used for generating the instances. 
5. We know you have more instances than others, but we do not know how helpful they are to analyze to performance of well-known solvers (including the baseline solvers in these papers). It would be nice to use all the attributes at your disposal to analyze the strength and weakness of each algorithms separately, including the heuristics and NCOs, please find out the most important factors which impacts each algo's performance and result quality. This can certainly help design new hybrid algorithms.
6. The results in many tables are very preliminary. It does not show the effectiveness of the NCO at all. SCIP-jack was run on CPU and it is compared to the inference on GPU, and the NCO's advantage is not obvious, either in terms of solution quality and in running time.
7. The authors argue that data augmentation techniques can not preserve optimal solution of the baseline data. But I thought you solved each instances in your benchmark dataset individually using exact solvers for comparing the gaps etc. Why do we need to preserve the optimal solution of the baseline data?

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a benchmark on the Steiner Tree Problem (STP) for neural combinatorial optimization. The authors collected a million STP instances and solved their optimal solutions, creating a benchmark for training and evaluating neural network solvers. The authors test supervised learning vs reinforcement learning and autoregressive vs non-autoregressive methods. The authors also study the generalization ability to different sizes of STPs and training with less amount of data.

### Strengths
* STP is a family of interesting problems to study and benchmark on.
* The comprehensive study of supervised learning vs reinforcement learning and autoregressive vs non-autoregressive methods is interesting and novel.
* The provided STP dataset has optimal solutions, which is great for neural combinatorial optimization.

### Weaknesses
As a dataset and benchmark paper, this work lacks some inspiration and insights for guiding future methodology development. I have the following questions and concerns:
* **Motivation for Focusing on STP:** Why should researchers prioritize STP over more well-studied problems like TSP? The motivation for this focus is not well-justified (see comments on Figure 1). What unique challenges does STP pose? Is there a particular application with significant market value that justifies this focus? (If the emphasis is on applications, would it be more valuable to create an application-specific dataset?)
* **Insights for Methodology Development:** What lessons can be drawn from the benchmark results for future methodology development? For instance, while Table 1 suggests DIFUSCO is preferred, other results seem to imply the opposite. What are the key principles learned from this benchmark in designing successful neural combinatorial optimization (NCO) methods?
* **Consideration of Solving Time:** Solving time is a crucial metric in combinatorial optimization but is not carefully considered or controlled in this benchmark. This oversight is significant, as theoretically, a slow enumeration algorithm could always find the optimal solution. As shown in Table 1, there is considerable variance in solving times among the methods. Therefore, it’s questionable to claim that DIFUSCO outperforms PtrNet and DIMES, given its significantly longer solving time, especially considering that SCIP solves the optimal solution in just 3 minutes for STP10.
* **Scope of STP Problems Considered:** The benchmark seems to focus only on an "easier" subset of STP problems (where SCIP solving time <1 hr, most of them <5 min). This limitation raises questions about the impact of the benchmark, especially for smaller datasets (STP10-50), as SCIP can solve these in about 5 minutes, leaving minimal room for improvement by neural networks.

**Additional Comments on Content:**
* **Toy Example in Figure 1:** The example in Figure 1 lacks informativeness. Both TSP and STP are combinatorial optimization problems, implying that small changes in problem parameters across a critical boundary can lead to shifts in the optimal solution. For other areas, minor disturbances may not affect the optimal solution. This example merely illustrates a case where TSP is far from this boundary while STP is closer to it. The example indicates that TSP and STP exhibit different characteristics but does not clarify which problem is more challenging. Consider incorporating more comprehensive metrics to support motivation, such as the average change in solutions concerning perturbations, solver runtime, average optimality gap, etc.
* **Clarification of Colors in Table 2:** The meaning of colors in Table 2 is unclear.
* **"Relative Gap" Metric in Table 2:** The "Relative Gap" metric in Table 2 is confusing for comparing methods. If a method consistently underperforms, it could still appear favorable in terms of relative gaps. This inconsistency may result in the inaccurate labeling of such methods as “generalizing well.” A more informative metric would be the gap to optimal. This issue similarly affects Figure 2, where it may appear that PtrNet performs better with less training data, though the text suggests otherwise.

### Questions
I like the idea of developing standard datasets and benchmarks for neural combinatorial optimization, and I believe STP could be an important and interesting problem to study. But I think this paper needs more careful consideration in its details. In the rebuttal, I would love to hear from the authors about my comments raised in the "weaknesses" part:
*  What are the specific characteristics of STP that make it an important problem to study in the context of neural combinatorial optimization (except for what's mentioned in Figure 1)? What are the unique challenges STP has put to existing NCO methods?
* Please provide a dedicated section summarizing key insights from the results. For instance, which aspects of STP (e.g., graph structure, problem size, terminal node distribution) seem to most significantly affect the performance of different NCO approaches, and how these insights might guide the development of new methods tailored for STP or similar problems.
* I would suggest improving the benchmarking results by more systematically considering the trade-off between solving time and optimal gap. You may set low/medium/high time limits for all methods, or plot the Pareto front between solving time and the optimal gap.
* You may include a wider range of problem difficulties in their benchmark. Specifically, it would be nice to include some instances that are challenging even for SCIP (e.g., requiring several hours or more to solve optimally), and to discuss how the performance of NCO methods changes as problem difficulty increases.

### Soundness
3

### Presentation
2

### Contribution
2
