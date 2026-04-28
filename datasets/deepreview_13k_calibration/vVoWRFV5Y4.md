# Solving the Quadratic Assignment Problem With Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 1, 5, 3

## Abstract
The Quadratic Assignment Problem (QAP) is an NP-hard problem which has proven particularly challenging to solve: unlike other combinatorial problems like the traveling salesman problem (TSP), which can be solved to optimality for instances with hundreds or even thousands of locations using advanced integer programming techniques, no methods are known to exactly solve QAP instances of size greater than 30. Solving the QAP is nevertheless important because of its many critical applications, such as electronic wiring design and facility layout selection. We propose a method to solve the original Koopmans-Beckman formulation of the QAP using deep reinforcement learning. Our approach relies on a novel double pointer network, which alternates between selecting a location in which to place the next facility and a facility to place in the previous location. We train our model using A2C on a large dataset of synthetic instances, producing solutions with no instance-specific retraining necessary. Out of sample, our solutions are on average within 7.5\% of a high-quality local search baseline, and even outperform it on 1.2\% of instances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Quadratic Assignment Problem (QAP) is an NP-hard problem with significant challenges, especially for larger instances. The paper proposes using deep reinforcement learning (DRL) to address the QAP, introducing a novel double pointer network to tackle the Koopmans-Beckman formulation of QAP. The method is trained using A2C on synthetic datasets, and its performance is benchmarked against a swap-based local search heuristic.

### Strengths
Using deep reinforcement learning to address the QAP is an innovative method, setting it apart from traditional optimization techniques. The double pointer network alternates between selecting locations and facilities, providing a dynamic solution approach. The model is trained on a large dataset of synthetic instances, making it robust and generalizable.

### Weaknesses
The method is tested primarily for QAP instances up to size 20, highlighting a potential scalability concern. While the DRL approach shows promise, there is still a performance gap when compared to the swap heuristic and the Gurobi solver. Unlike traditional optimization methods which provide a solution and its optimality certificate, this DRL approach only gives a solution. The performance gap is not clearly defined, making it difficult to assess the practical significance of the results. The lack of a clear definition of the performance gap, specifically whether it is a standard duality gap or something else, makes it hard to compare against other optimization methods. The training time, limited to 20 minutes and 1 hour for n=10 and n=20 respectively, raises questions about the convergence of the DRL model and whether longer training could yield better results.

### Questions
Why was the swap-based local search heuristic chosen as the baseline? 
Is the performance gap mentioned equivalent to the standard duality or MIP gap commonly used in optimization? If not, how do they differ? The obscurity in the definition makes it difficult to assess the performance of the new method. 
How does the DRL method scale with larger problem sizes, especially when compared with traditional algorithms?
Why is training limited to 20 minutes and 1 hour for n = 10 and n = 20? How will performance improve if the training time is increased?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an RL method to solve quadratic assignment problems. The authors reformulate the original QAP as a seq2seq problem. However, the paper is not easy to follow. The motivations and contributions of the work are not clear.  The details of the method are missing. The experimental evaluation is not good enough. Therefore, I think the paper is under the bar of ICLR in its current form.

### Strengths
The topic of using RL to solve the quadratic assignment problem is interesting.

The authors reformulate the original QAP as a seq2seq problem.

### Weaknesses
The motivation and contribution of the work is not clear.

The paper is not easy to follow.

The literature review is not good enough. A lot of classic literature is missing.

The experimental evaluation is not enough. Only Gurobi and swap-based local search heuristic is compared. Which makes the paper less convincing.

The size of QAP used in the experiment is quite small.

The performance is quite poor, which cannot outperform simple heuristics such as SWAP.

### Questions
Please see the weeknesses.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper delves into the end-to-end application of Deep RL for solving the QAP. Because the QAP necessitates assignments between a set of facilities and locations, the authors introduce a novel autoregressive model that sequentially selects a location and then a facility (to make a pair), and then repeats this process until the assignment is done. The results are promising. The derived solutions are, on average, within 7.5% of those generated by a heuristic method.

### Strengths
This paper represents the pioneering effort to tackle the QAP using a neural network-based approach, marking an important milestone in the field. The paper is well-structured, with contents presented in a manner that's easy to follow and understand.

### Weaknesses
The results are too weak for ICLR publication. While one could argue that the considerable optimality gap might be attributed to the intrinsic complexity of the QAP, it's evident that a notable portion arises from the authors' dependence on a neural net model and the training methods that closely mirror the early contributions of Bello et al. that might not be the best fit.

To draw a parallel, when the pointer network was initially applied to solve the TSP in an end-to-end manner, there existed an optimality gap of around 7% for 100-node TSPs. However, with subsequent refinements in models and training techniques, that gap has been narrowed to almost 0% now. 

It's plausible that similar methodological advancements could significantly benefit the QAP approach presented here. I'd recommend reconsidering the use of the Critic network for such combinatorial optimization tasks, especially given the challenges of predicting the final outcome midway through solution construction.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors investigated the Quadratic Assignment Problem (QAP) solving using deep reinforcement learning with double pointer networks, where an upper pointer network selects locations and a lower pointer network selects facilities. And the proposed method is evaluated on synthetic QAP instances.

### Strengths
1- This paper is well motivated as the QAP has been rarely studied using DRL;
2- It seems the proposed method works on the self-generated dataset.

### Weaknesses
1- It seems that from the DRL based heuristic perspective, the objective function in QAP does not make difference compared with the ones in ILP, both of which are just captured by a reward in DRL. In this sense, the QAP in this paper is almost the same as the vehicle and customer assignment in VRPs with linear objectives, such as
[a] Deep Reinforcement Learning for Solving the Heterogeneous Capacitated Vehicle Routing Problem. IEEE T Cybernetics;
[b] Learning to Solve Vehicle Routing Problems with Time Windows through Joint Attention. Arxiv;
[c] Solving NP-hard Min-max Routing Problems as Sequential Generation with Equity Context. Arxiv.
Those works also involve sequentially or parallelly selecting vehicles and customers, while using (advanced) Transformers rather than pointer network.

2- Besides, the Transformers in 'Learning Improvement Heuristics for Solving Routing Problems. TNNLS' outputs a probability matrix, which could also be tailored to the probability of facility and location pair with proper masking.

3- The evaluation is quite simple, which solely focuses on one single problem with randomly generated instances. And the baselines are also insufficient and not strong enough.

### Questions
Please see the above weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
