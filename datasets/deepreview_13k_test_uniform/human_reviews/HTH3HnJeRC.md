# DER-Solomon: A Large Number of CVRPTW Instances Generated Based on the Solomon Benchmark Distribution

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
The Solomon benchmark is a well-known resource for researching Capacitated Vehicle Routing Problem with Time Windows (CVRPTW), and has been used by many traditional methods. However, the limited scale of the Solomon benchmark poses challenges to effective utilization by learning-based approaches. To address this, we propose an expanded version with a large set of new instances, called DER-Solomon benchmark, which follows a similar distribution as the Solomon benchmark. First, we analyze the Solomon benchmark and use backward derivation to establish an approximate distribution, from which the DER-Solomon is generated, thereby significantly expanding the size of the benchmark. Next, we validate the distribution consistency between the DER-Solomon benchmark and the original Solomon benchmark using traditional algorithms. We then demonstrate the superiority and reliability of DER-Solomon compared to other similar Solomon-like datasets using state-of-the-art Deep Reinforcement Learning (DRL) algorithms. Finally, we train multiple DRL algorithms using the DER-Solomon benchmark and compare them with the traditional algorithms. The results show that the  DRL algorithms trained on the DER-Solomon benchmark can achieve the same level of solution quality as the traditional algorithms on the Solomon benchmark while reducing the computational time by over 1000 times on CVRPTW. All the results demonstrate that the DER-Solomon benchmark is sufficiently excellent, serving as an extension of the Solomon benchmark, which offers valuable tools and resources for further research and solutions to the CVRPTW problem.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work scales up the Solomon benchmark with backward deriving.  Distribution consistency has been verified between the generated dataset and the original one.

### Strengths
1. Effect solution to scale up the Solomon benchmark. 
2. Code is publicly available.

### Weaknesses
1. While effective, the contribution of this work is quite limited. I suggest authors consider applying this algorithm to scale more benchmarks.
2. The comparison with neural solvers is missed in Table  1.

### Questions
The figures are not well presented. Also hard to find the relevant descriptions. This paper is not ready to be published.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To deal with the limited scale of the well-known Solomon benchmark of the capacitated vehicle routing problem with time windows (CVRPTW) for learning-based approaches, this paper proposes a large set of new instances with a similar distribution to the Solomon benchmark, called DER-Solomon benchmark.

### Strengths
To deal with the limited scale of the well-known Solomon benchmark of the capacitated vehicle routing problem with time windows (CVRPTW) for learning-based approaches, this paper proposes a large set of new instances with a similar distribution to the Solomon benchmark, called DER-Solomon benchmark.

### Weaknesses
Besides the Solomon benchmark, the Gehring & Homberger benchmark is also a famous one of CVRPTW. It is better to further apply the proposed data generation method to the Gehring & Homberger benchmark.

### Questions
1. How many instances are included in the DER-Solomon benchmark?
2. How many DER-Solomon instances are used to train the learning-based method?
3. What and how many original Solomon instances are used to train the learning-based method?
4. How to calculate the std gaps reported in Table 1? They seem to be unequal to the relative gaps between the std values of two benchmarks.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies to use deep reinforcement learning to solve the classic optimization problem of capacitated vehicle routing problem with time windows. To make DRL possible, the paper proposes to create a training dataset that is based on the Solomon dataset that is small but comprehensive to test algorithms for CVRPTW problem. The paper creates the new DER-Solomon dataset by first estimating the probability distributions of the essential parameters of the Solomon dataset and then generating new problem instances by using the estimated distributions. The paper then trains a DRL model on the DER-Solomon dataset and shows comparable performance on the testing instances compared to optimization-based approaches.

### Strengths
1. The paper proposes a approach to effectively enlarge the training data for DRL on a specific classic optimization problem given a small but comprehensive instance set.

2. The paper shows that the learned DRL with the enriched dataset could achieve comparable performance compared to classic optimization methods.

### Weaknesses
1. The paper lacks background descriptions of the CVRP and CVRPTW problems and also probably some more detailed introductions on the existing traditional algorithm approaches. Given there is plenty of space for the paper, such background information could be very beneficial to the audience. VRP may be well-known in the community, but the variants are probably not.

2. A lot of details are not presented in the paper. E.g., given the estimated distributions of the parameters, how are the new instances sampled? Are all parameters considered independently? Why generate 1280k instances? Moreover, there are no given details on how the DRL model is trained using DER-Solomon.

3. The technical contribution is limited. It mainly estimates the distributions of a given small dataset to generate instances to form a larger dataset. It does not compare the proposed sampling method to some more basic methods. For example, what if we just add Gaussian noises to parameters in Solomon or use some uniform sampling to generate the instances?

4. Curretly I think parameters of the dataset are assumed to be independently samples (correct me if that is wrong). Is there a reason to make such an assumption? Would it be beneficial to consider a more complex distribution of the parameters?

5. The studied problem has a relative restricted scope. Could such techniques explored in the paper get applied to solving other classic optimization problems as well? Or what special properties of the Solomon dataset makes the approach most effective?


Minor:
1. Page 3:  "its frequency histogram is shown in Figure 2(a)" but there is no index of (a) or (b) in Figure 2.
2. X-axis of Figure 5 is not labeled.

### Questions
Please check the weaknesses part.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This is a dataset and benchmarking paper. The author proposes DER-Solomon, an expanded CVRPTW dataset, by approximating the original Solomon dataset with backward derivation. Experiments are conducted on traditional and DL-based algorithms to demonstrate its merits.

### Strengths
* Compared with Solomon-like datasets, the proposed method could better approximate the original Solomon dataset.
* The proposed dataset has values for further research in CVRPTW.

### Weaknesses
* The practicality is not clear. 
  * Is there any evidence to demonstrate that, with only 56 instances, the original Solomon benchmark is complex enough to test *all aspects* of (traditional or DL-based) algorithms? If a company trains a DL-based model on DER-Solomon, could we guarantee its reliability in practice?
  * Besides Solomon, is the proposed method generalizable to approximate other datasets?
* It seems only the distribution of the time window is approximated. However, other attributes, such as the customer location, may significantly affect the learned policy as well. Have you considered the variations of all attributes in DER-Solomon?
* For the traditional algorithms, it would be better to add HGS. For the DL-based method, some recent studies [1, 2] demonstrate superior performance on CVRPTW, it would be better to benchmark them as well.
* The provided link to the source code cannot be opened.
* The writing and presentation of this paper should be improved:
  * All figures should use PDF format. The current version is blurry when zooming in.
  * Better to provide some visualizations of the generated instances.
  * The best result (e.g., in all tables) should be in bold for a better view.

[1] Learning to delegate for large-scale vehicle routing. In NeurIPS 2021.   
[2] RBG: Hierarchically solving large-scale routing problems in logistic systems via reinforcement learning. In KDD 2022.

----

**Overall,** this paper only focuses on *one dataset of a single problem (i.e., CVRPTW)*, and therefore the contribution may not be enough for ICLR. Currently, I lean towards rejection, and I may adjust the evaluation after reading other reviews and the author's rebuttal.

### Questions
* Will you release the source code and datasets?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
