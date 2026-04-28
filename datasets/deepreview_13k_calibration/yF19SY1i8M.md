# Towards More Robust NLP System Evaluation: Handling Missing Scores in Benchmarks

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
The evaluation of natural language processing (NLP) systems is crucial for advancing the field, but current benchmarking approaches often assume that all systems have scores available for all tasks, which is not always practical. In reality, several factors such as the cost of running baseline, private systems, computational limitations, or incomplete data may prevent some systems from being evaluated on entire tasks. This paper formalize an existing problem in NLP research: benchmarking when some systems scores are missing on the task, and proposes a novel approach to address it. Our method utilizes a compatible partial ranking approach to impute missing data, which is then aggregated using the Borda count method. It includes two refinements designed specifically for scenarios where either task-level or instance-level scores are available. We also introduce an extended benchmark, which contains over 131 million scores, an order of magnitude larger than existing benchmarks. We validate our methods and demonstrate their effectiveness in addressing the challenge of missing system evaluation on an entire task. This work highlights the need for more comprehensive benchmarking approaches that can handle real-world scenarios where not all systems are evaluated on the entire task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission addresses the significant and increasingly relevant problem of benchmarking on multiple datasets when not all systems have been run on all tasks, or even all instances in a task. They propose a novel formalism to derive system rankings (with confidence) from results missing some scores, and show that this improves robustness compared to simply averaging over only available scores.

### Strengths
This is clearly a relevant problem -- benchmarking general-purpose models is increasingly done by comparing results on multiple datasets and tasks, but due to many reasons (outlined in the paper) not all systems may be run on all tasks, which makes simple averaging impractical.

The method is clever. It combines 1) estimates based on the proportion of total orders with a given pairwise ordering that are compatible with the observed partial ordering, 2) Borda count on the task orderings into a final ranking, 3) confidence intervals on the resulting rankings.

The formalisation of the problem is clear and useful, and a lot of detail is provided in the appendix. One of the contribution is a practical, non combinatorial method solving the non-trivial problem of estimating the proportion of total orders compatible with an observed partial order.

The method seems to yield much improved robustness compared to simple averaging, and the resulting ranking remains much closer to reference ranking when the proportion of missing scores increases.

### Weaknesses
Although the methodology is well described overall and there is a lot of useful detail in the paper and the (extensive) appendix, the motivations are sometimes lacking. For example, is averaging still the right way to combine estimated ranks? Also, imputation methods usually don't use naive distribution estimate, but try to leverage observed data to improve the missing data imputation -- e.g. if scores are missing for systems i and j on a given task, but i usually outperforms j whenever they are both observed, it seems sub-optimal to set M_ij to 0.5 (step 2, p. 5). The assumption of a uniform distribution over total orders compatible with the observed partial order seems particularly naive, and it is not clear that this is the best approach. The paper feels rushed at times and there are lots of readability issues, including with the notation (see below).

This is a substantial paper with a lot of material. The downside is that it is hard to pack that much material in 9 pages, and difficult to follow the paper without the appendices. There seems to be simply too much material re. experimental results in the last three pages. As a consequence, the Figures are mostly unreadable or unclear and the experimental section does not do a good job supporting the arguments and conclusions of the paper. Specifically, the choice of datasets and the evaluation protocol are not sufficiently justified. The lack of error bars on the figures also makes it hard to assess the statistical significance of the results.

To be clear, I think this is an interesting paper with significant results, but the presentation does not do it justice.



### Questions
It was not fully clear why the 'argsorts' are systematically doubled (p.3, p.6). E.g. in Eq. 3, it seems that computing the average of estimated scores, one sort would be enough to recover the permutation with correct ranking?

Clarity:
* "input" in Sec. 3.2.1 is likely "impute" (the missing data/information)?
* Still Sec. 3.2.2: p_{i,j} pops up in the last paragraph -- is that M_{i,j}?
* Sec 3.2.3, step 3.: Need some reference to a publication or appendix for Borda count aggregation
* Figures are overall way too small and often unreadable. Their positioning is odd, for example Fig. 2 (top p.7) is referenced on p.9. 
* The x-axis in Fig 2 and Fig 5 seem to show the proportion of scores observed rather than proportion of scores removed. As described in the text, Kendal Tau tends to 1 when there is no (0%) missing data.
* What is "[4]" in Sec. 5.1?
* Sec 5.2: "in the robustness experiment" -> not clear what you mean by that and where those are described.

Typos:
* Citations lack brackets in most places -- likely an issue with \cite[] usage with the style file
* p.2: "Our includes..."
* p.3: "previously mentioned." ... article?
* p.3: "on a k of test instances" -> on k test instances?
* p.5, l-4: Superscripts of M seem messed up
* p.9: "in Ssec 5.3" is likely 5.2 (we are in 5.3)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper tackles the problem of system benchmarking with some scores missing. The proposed approach utilizes a compatible partial ranking approach to impute the missing data and use the Borda count method to do the aggregation. Two scenarios are considered, task-level or instance-level scores are available. The evaluation is done by comparing the system ranking against the groundtruth of complete results.

### Strengths
* Tackles the important task
* The proposed approach empirically outperforms the baseline
* Both task-level and instance-level evaluations are covered

### Weaknesses
 * Lack of closer looks at the correlation between tasks, since similar tasks might be "easier" to predict

### Questions
* Are there any other stronger baselines or previous works to compare with?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends a method to rank systems proposed by Colombo et al. (2022) to an incomplete set of scores in tasks (and task instances). The evaluation method is empirically compared to a very simple baseline, with good results. The experiments are performed on a synthetic dataset and an extension of an existing dataset.

### Strengths
The main technical contribution of the paper is to extend Colombo et al. (2022) in order to cover for missing task (or instance) scores, via a combinatorial method.

The results are positive in favor of the proposed technique, although the more complex two-level method is not better than the simpler one-level method.

### Weaknesses
Originality is low and the contributions weak, as the main contributions are an efficient implementation for a combinatorial problem that allows to extend two pre-existing methods (Colombo et al. 2022) to missing scores, and enlarging an already existing dataset. Unsurprisingly the methods proposed in (Colombo et al. 2022) also are effective in this setting. 

The main empirical weakness is that it does not compare to any strong baseline. For instance the baseline that ignores data  using mean aggregation, has too intermingled issues: that of ignoring data and that of using scores from different scales. Thus, from figure 2 it's not clear whether its worse results are caused by one or the other, or, in other words, whether the proposed method is better because it uses ranks (instead of scores) or because it models missing scores. Colombo et al. 2022 already showed that these two methods are better than such a baseline.  

The figures have very small fonts, unreadable without extensive zooming.

Minor issues:

* Fig 3 is not readable, same with other figures
* Reference missing in: "We did not use the data from [4]"
* Citations use the wrong format "authors (year)" instead of "(authors, year)"

### Questions
In section 4, it seems that the toy experiment is only applied to robustness scaling and pairwise confidence analysis, but as I started to read I was expecting more development experiments. Could you mention why you only check those two factors and not other?

From figure 5, it would seem that instance level information is not helpful and is harmful in three datasets, but there is no explicit elaboration on this (only a brief mention in the conclusions).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of combining multiple partial system rankings (from multiple evaluation tasks/instances) to form a single complete ranking. The proposed method consists in building fractional ranking matrices where missing evaluation are replaced by the proportion of permutations compatible with the partial information, and then combining those matrices with the consensus-oriented Borda aggregation method (sum of ranks). The method is adapted to both instance- and task-level aggregations and a O(n³) algorithm is proposed for counting the number of system orderings compatible with a partial rank. Synthetic results on a set of 20 systems, 20 tasks, 20 instances show the potential of the method against a baseline that averages metrics, ignoring missing values. Then, a large set of instance-level and task-level scores is produced and made available for popular benchmarks. Evaluation on this set confirms synthetic data results, however, as noted by the authors, the final rankings produced by Borda aggregation are very different from the mean ranking.

### Strengths
The problem of handling large benchmarks with missing evaluations is important because of the cost of running larger and larger benchmarks, and because of the unavailability of evaluation results when systems are closed.

The proposed approach relies on Borda consensus which yields a different outcome to benchmark aggregation.

A O(n³) algorithm for counting the number of permutations that agree with a partial ranking allows completing the ranking matrices.

A large dataset of instance-level evaluation results is released for fostering research in this area.

Both synthetic and real data experimental results are convincing.

The paper is clearly written and easy to read.

### Weaknesses
As noted in the paper, Borda aggregation yields very different results from mean aggregation, even in the absence of missing values. This should be investigated before accepting that the resulting rankings are truthful.

The degradation from missing values is the same for Borda and mean aggregations in realistic scenarios with less than 20% missing values, showing a potential lack of interest by practitioners.

Experiment results should be analyzed more thoroughly.

The addressed problem is not NLP-specific although experimental results are restricted to the field of NLP.

"enables us to leverage the Borda aggregation inheriting its theoretical and practical advantage" => what are they?

Why is sum of ranking matrices (and more generally Borda count) a good aggregation criterion?

How does the method handle misleading evaluation results, when the evaluation metric failed because of the dataset sample bias, or because it is itself an approximation of human evaluation?

Scaling corruption (Fig 3) is not detailed enough. How are the tasks selected for being scaled? How many tasks are being scaled? What is the evaluation metric? Why are there two regimes, starting at 1 or 0 when eta is 0? Font in Figure 3 is also too small

Why is the correlation of sigma_l very different from sigma_2l for some datasets of Fig. 5 while it is very similar for others?
It is not clear from the figures whether # scores (%) is the percentage of removed or kept scores. The discussion is misleading in that regard.

What is the proportion of missing scores in the comparison of rankings by sigma_l and sigma_mu in table 1 and 2?

Confidence analysis (Fig 6) should be compared to other methods such as ANOVA. This section is not very useful to main point of the paper and can be removed in favor of more analysis of previous experiments.

### Questions
"enables us to leverage the Borda aggregation inheriting its theoretical and practical advantage" => what are they?

Why is sum of ranking matrices (and more generally Borda count) a good aggregation criterion?

How does the method handle misleading evaluation results, when the evaluation metric failed because of the dataset sample bias, or because it is itself an approximation of human evaluation?

Scaling corruption (Fig 3) is not detailed enough. How are the tasks selected for being scaled? How many tasks are being scaled? What is the evaluation metric? Why are there two regimes, starting at 1 or 0 when eta is 0? Font in Figure 3 is also too small

Why is the correlation of sigma_l very different from sigma_2l for some datasets of Fig. 5 while it is very similar for others? 
It is not clear from the figures whether # scores (%) is the percentage of removed or kept scores. The discussion is misleading in that regard.

What is the proportion of missing scores in the comparison of rankings by sigma_l and sigma_mu in table 1 and 2?

Confidence analysis (Fig 6) should be compared to other methods such as ANOVA. This section is not very useful to main point of the paper and can be removed in favor of more analysis of previous experiments.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
