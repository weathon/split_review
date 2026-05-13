# Accelerating neural network training: An analysis of the AlgoPerf competition

- Decision: Accept
- Avg Score: 7.00
- Scores: 10, 5, 6, 8, 6

## Abstract
The goal of the AlgoPerf: Training Algorithms competition is to evaluate practical speed-ups in neural network training achieved solely by improving the underlying training algorithms. In the external tuning ruleset, submissions must provide workload-agnostic hyperparameter search spaces, while in the self-tuning ruleset they must be completely hyperparameter-free. In both rulesets, submissions are compared on time-to-result across multiple deep learning workloads, training on fixed hardware. This paper presents the inaugural AlgoPerf competition's results, which drew 18 diverse submissions from 10 teams. Our investigation reveals several key findings: (1) The winning submission in the external tuning ruleset, using Distributed Shampoo, demonstrates the effectiveness of non-diagonal preconditioning over popular methods like Adam, even when compared on wall-clock runtime. (2) The winning submission in the self-tuning ruleset, based on the Schedule Free AdamW algorithm, demonstrates a new level of effectiveness for completely hyperparameter-free training algorithms. (3) The top-scoring submissions were surprisingly robust to workload changes. We also discuss the engineering challenges encountered in ensuring a fair comparison between different training algorithms. These results highlight both the significant progress so far, and the considerable room for further improvements.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper presents an analysis of the results of the recent AlgoPerf Training benchmark, in which a variety of community-submitted algorithms were evaluated on multiple workloads and in multiple settings to identify those which yield improved training algorithms. A variety of details from the benchmark results are presented, leading to some broad trends (e.g., the best optimizers are those that are "consistently reasonable" as no one approach dominated all workloads) as well as suggestions for future directions. The paper also includes lessons learned and commentary on the benchmark itself, and on the engineering efforts involved.

### Strengths
The paper summarizes and analyzes the results of the AlgoPerf Training benchmark, providing a valuable focal point to the community for driving future progress in training algorithms and setting the agenda for research. The current advances and limitations of training algorithms are highlighted, helping to clearly identify areas for improvement in the community.

Equally valuable, the paper has a detailed discussion of lessons learned and suggestions from the process of running the competition. These are details that are often not widely disseminated, and are valuable for others seeking to build similar benchmarks. This includes a discussion of engineering challenges involved in ensuring fair and reasonable comparisons across submissions and frameworks.

Overall the paper is clear, well-written, and likely to help drive progress in the ML community.

### Weaknesses
I have no notable concerns about the paper.

Very minor typo: L382, "framekworks" -> "frameworks"

### Questions
n/a

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper details the experience of the "AlgoPerf Competition: Training Algorithms". The goal of the competition is to evaluate neural network training speeds by improving the training algorithms. The competition evaluated submissions under two rulesets: external tuning (using predefined hyperparameter search spaces) and self-tuning (completely hyperparameter-free). The competition also demonstrated that the top-scoring algorithms generalized across workloads. For the former, distributed shampoo outperformed other techniques, and for the latter, Schedule Free AdamW demonstrated superior performance.

The paper also describes future training algorithm developments -- emphasizing the importance of fair benchmarking, providing complete algorithm specifications, and different hyperparameter tuning strategies. The paper is written like an experience paper, demonstrating methods and techniques that help with neural network speedups, as well as conducting a fair evaluation of different methods.

### Strengths
- The papers' winners (Dist. Shampoo, and Adam W) are interesting to note, and offer strong baselines for the workloads used in the paper.
- The paper describes engineering effort needed to bring parity between Jax and Pytorch, which can be useful in understanding   accuracy/performance differences between the two frameworks related to specific features/API calls that were used in the competition.
- The paper details the engineering and compute needed in hosting a systematic model evaluation framework/process.
- The paper is well-written, and describes the methodology, results and lessons clearly.

### Weaknesses
 - Weak conclusions:  The authors are encouraged to draw stronger conclusions from the experience. While it is acknowledged that these types of papers are difficult to write, the broad applicability or lessons can be difficult to grasp for the reviewer. The specific nuances in performance evaluation is interesting. But can these results be made more general or useful to improve the paper?  E.g. can you claim that Pytorch/JAX parity is impossible to achieve for specific workloads?
- Unclear fit with ICLR: The paper reads more like an experience report (e.g. Kaggle summaries), rather than a research paper. While the experiences are interesting, the novel contributions/lessons are limited. The lack of a test set and lack of common workloads also limit the applicability. The paper would be likely be a better fit for a software engineering conference both in terms of fit and conference attendee interests.
- Challenges with methodology: The competition evaluation is resource intensive and uses a validation test. Most competitions are evaluated on test sets, and a note describing how the results/methodology can be extended to include test sets would help improve the paper.

### Questions
1) Please describe a fit with ICLR, and how publishing this paper helps the broader ICLR community.
2) Can you please provide more insights into the specific reasons behind the significant compute costs, and are there suggestions for optimizing the evaluation process without compromising the robustness of the benchmark?
3) Can you comment on increase in compute costs if test sets and LLMs are considered for model evaluation?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper analyses the results of the AlgoPerf competition. For that, it presents a summary of the methodology, a detailed description of the winning submissions, how the evaluation was carried out, the implementation details of the competition itself, and the engineering challenges they faced. The main goal of the competition is to evaluate the effectiveness of training algorithms. This is done by measuring how long submissions take to achieve some evaluation goal on some defined workload with restricted runtime and budget. In general, results highlight the competitiveness of the benchmark, as few of the submissions were able to do well on all the different workloads, indicating lots of room for improvement.

### Strengths
- Authors provide a detailed analysis of their competition, including the methodology, the best results, and lessons learnt.
 - Originality of the work lies in having the initiative to setup the competition (organisation, dissemination, infrastructure set up), and reporting the results obtained. 
 - Analysis is extensive. Authors provide tables and graphics to showcase the results of the competition.
 - Authors provide low level details and lessons learnt also on the implementation and mainteinance of the benchmark, comparing Pytorch and JAX.

### Weaknesses
 - Novelty: Besides the competition results and the insights obtained, novelty is not high. Contributions are mainly the insights extracted from the submissions. It feels more like a report (summarising results obtained from a competition). I would encourage authors to further highlight the contributions they make, clearly stating that this benchmark is solving a gap, and backing up the claims. In addition, I believe that some of the lessons learnt highlighted in bold are not novel but already established practises (e.g. "having fair comparisons in a competition" is something widely known and established).
 - Clarity: Narrative can be improved in some sections. E.g. Section 3 is specially dense to read, and is not always clear what the authors want to convey. I encourage authors to include, at the start of each paragraph in section 3, a sentence that summarises the main findings of that paragraph. (Eg. ResNet workload subsection. Then, main takaway sentence. Then, the rest of the details, numbers, statistics, etc.)
 - I believe authors could improve the significance of the work by better motivating the need of this benchmark. Why is this benchmark important and needed? Is it the first benchmark to allow evaluation of training algorithms? What makes it different from other benchmarks?  The current paper is lacking a strong motivation background and more evidence. For example, that there is a real need for self-tuning algorithms.

### Questions
- "Although a radical change from the current practice of published training algorithms that aren’t runnable without setting various hyperparameters, publishing families of update rules and abdicating responsibility for tuning entirely to the user only adds to the community’s confusion on what to actually use". This is an interesting comment that is hidden in the bulk of the text. It would be interesting if the authors clarified this comment, and expanded on it further.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper describes the methodology and results of the "AlgoPerf: Training Algorithms" competition, which aims to evaluate the speed-ups of neural network training by modifying the underlying training algorithm.

The competition covers two rulesets: "external tuning", which requires a hyperparameter search space that is workload agnostic, and "self-tuning", which is hyperparameter-free. This paper details the winners of both rulesets "Distributed Shampoo" and "Schedule Free AdamW".

Finally, the authors detail the issues they encountered while developing this competition, highlighting compatibility and performance issues between different frameworks and improving the respective implementation by copying the better-performing one.

### Strengths
S1: Ensuring a fair comparison with JAX and PyTorch is likely impossible, but the authors did a good job of tracing most issues (mathematical correctness, comparing kernel runtimes, etc.). They stopped at memory allocation patterns, which is arguably impossible to get outside of creating an intermediate translation layer between NVIDIA GPU drivers and whatever TPUs are using. This decision showed improvement potential in both frameworks, as the direct comparison between them showcased performance gaps that could be easily closed by copying the better-performing implementation.

S2: The lessons learned are very interesting for practitioners and future competition creators, outlining gaps in current algorithmic development and the dependency on hyperparameter tuning to get the best results.

### Weaknesses
W1: I am missing a more detailed analysis of why the winners of the respective rulesets came first. While this paper is more about the competition itself, I would love for it to be slightly more useful for practitioners questioning whether they should drop AdamW for Distributed Shampoo in their experiments. Other questions like whether the current on-trend LLM training will see significant changes due to the results from AlgoPerf (due to the significant cost to training these models) might provide a slightly better outlook and highlight the impact of this competition.

Minor issues:
- Typo in Line 382: "framekworks"

### Questions
I would like the authors to address W1.

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
1

### Summary
This paper investigates the AlgoPerf competition and provides insights into model training acceleration. Some findings are reasonable and could potentially guide the design of training algorithms. As this is a survey rather than a technical paper, I am not sure whether it is qualified to be published in ICLR. Therefore, I seek to consider the opinions of other reviewers.

### Strengths
Some interesting findings are provided and they may help to design more efficient training algorithms.

### Weaknesses
I am not an expert in evaluating this kind of survey paper, and I am curious about how the findings can be applied to refine existing algorithms. Specifically, while the paper presents results from the AlgoPerf competition, it lacks a clear articulation of how these results translate into actionable improvements for training algorithms. The findings are presented as observations, but the paper does not delve into the underlying mechanisms that cause certain algorithms to perform better than others. This makes it difficult to extract concrete principles that can be used to guide the design of new training methods or refine existing ones. For example, the paper might highlight that a specific optimizer performs well on a particular workload, but it does not explain why this is the case, or how this insight could be generalized to other scenarios. The lack of mechanistic understanding limits the practical impact of the findings.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
