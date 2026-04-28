# Objectives Are All You Need: Solving Deceptive Problems Without Explicit Diversity Maintenance

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
Navigating deceptive domains has often been a challenge in machine learning due to search algorithms getting stuck at sub-optimal local optima. Many algorithms have been proposed to navigate these domains by explicitly maintaining diversity or equivalently promoting exploration, such as Novelty Search or other so-called Quality Diversity algorithms. In this paper, we present an approach with promise to solve deceptive domains without explicit diversity maintenance by optimizing a potentially large set of defined objectives. These objectives can be extracted directly from the environment by sub-aggregating the raw performance of individuals in a variety of ways. We use lexicase selection to optimize for these objectives as it has been shown to implicitly maintain population diversity. We compare this technique with a varying number of objectives to a commonly used quality diversity algorithm, MAP-Elites, on a set of discrete optimization as well as reinforcement learning domains with varying degrees of deception. We find that decomposing objectives into many objectives and optimizing them outperforms MAP-Elites on the deceptive domains that we explore. Furthermore, we find that this technique results in competitive performance on the diversity-focused metrics of QD-Score and Coverage, without explicitly optimizing for these things. Our ablation study shows that this technique is robust to different subaggregation techniques. However, when it comes to non-deceptive, or ``illumination" domains, quality diversity techniques generally outperform our objective-based framework with respect to exploration (but not exploitation), hinting at potential directions for future work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an approach based on objective sub-aggregation designed to address potentially misleading domains by optimizing a set of specified objectives via lexicase selection, thereby converting the fundamental search problem into a Multi-Objective Optimization (MOO) challenge. The authors argue that by utilizing lexicase selection to optimize the sub-aggregated objectives, maintaining explicit diversity measures becomes unnecessary, as implicit diversity is ensured. This objective-driven method surpasses the performance of the cutting-edge quality diversity algorithm, MAP-Elites, specifically on misleading domains, achieving competitive results even though it does not explicitly prioritize diversity. Additionally, an ablation study confirms the reliability of the sub-aggregation technique by demonstrating that various sub-aggregation strategies produce comparable performance, showcasing the algorithm's adaptability.

### Strengths
1. The research explores a promising direction, illustrating the effectiveness of implicit diversity preservation in Multi-Objective Optimization (MOO) problems using lexicase selection. This approach is widely adopted for MOO tasks, facilitating diverse solutions without direct optimization for diversity.

2. The conducted experiments and ablation study offer a thorough examination. The selection of Knight’s Tour and Maze (both Deceptive and Illumination) domains is thoughtfully explained, including the specific objectives, sub-aggregation, objective counts, and other pertinent details.

3. The paper is well-structured with a coherent flow, especially evident in the well-crafted "Introduction" and "Related Work" sections that provide comprehensive and specific insights.

4. Comparative analysis based on Best Score, QD-Score, and coverage presents valuable insights into the proposed approach's effectiveness and implicit diversity preservation.

### Weaknesses
1. In Section 4.2 under “Objective for Deceptive Maze”, the first two lines of the paragraph seem contradictory.

2. The introductory paragraph of Section 3 mentions the limitations of explicit diversity maintenance and proposes
implicit diversity maintenance as a viable alternative. Instead of just a mention, a thorough explanation with
suitable illustrations would be better. For instance, consider the following line - “More importantly, in more complex or deceptive search spaces where the relationship between phenotypic traits and fitness is not straightforward, these explicit measures can
inadvertently steer the search away from optimal or even satisfactory solutions.” The author(s) could have
taken a particular deceptive domain, pictorially representing how the search deviates from the optimal and
how implicit diversity solves this issue.

3. Could deceptive domains from OpenAI Gym/Atari be included? Montezuma’s Revenge is a classic example!
The authors claim that objectives are all we need for solving any deceptive domain. A performance comparison
of the proposed approach to other SOTA algorithms in these domains would make the claim stronger.

4. The author(s) also claim that this approach enhances exploration in deceptive domains. However, it is also
important to evaluate the performance of RL agents (trained by the proposed algorithm) in non-deceptive
MuJoCo environments. This would validate the algorithm’s sensitivity to the choice of the sub-aggregation
schemes.

5. An algorithm is missing! The entire approach should have been formalized as an algorithm and written clearly
in the main paper.

### Questions
I would like the author(s) to address the points mentioned in the “Weaknesses” section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an approach to avoid getting stuck in local optima in deceptive domains by optimizing a large set of automatically extracted objectives. While most approaches in evolutionary computation to avoid deception are based on explicitly rewarding diversity, like novelty search or quality diversity, the presented approach directly optimizes for a set of objectives. It is evaluated on two domains: knight’s tour and a deceptive 2D maze.

### Strengths
- Automatically extracting objectives from the environment is a promising approach to elivate some of the issues with many quality diversity algorithms
- Promising results in two deceptive domains

### Weaknesses
 - Easy read for somebody in EA community but should be more motivated for why the broader ML community should care.
- MAP-Elites is not introduced when first mentioned in the introduction
- This description should be extended to make it very clear for the reader "The idea of lexicase selection is that instead of compiling performance metrics over the training dataset, we can leverage individual performance to sift through a population via a sequence of ran domly shuffled training cases.”
- More complex domains should be tested and the approach should be compared to RL-based approaches as baselines to increase its impact on the broader ML community 

Minor comment:
- I would suggest not another “all you need” title...
- It should be noted in Figure 2 that n is the number of objectives in lex_n. Is lex_1 equivalent to not having any lexicase, just a standard selection?
- Add a description of lexicase to the abstract/introduction

### Questions
- Can this approach be extended to RL methods, which would significantly increase its impact?
- How would the reward aggregation work in higher-dimensional domains, i.e. learning directly from pixels? Would it be necessary to manually define the objectives in that case?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Some search algorithms can achieve improved performance by promoting exploration through the encouragement of higher diversity within their solution pool. Traditionally, achieving this has necessitated the manual engineering of appropriate diversity measures and incorporating them explicitly in the algorithm. In this paper, the authors introduce a new approach: they transform the original single objective into multiple objectives for the search algorithms, which promotes better exploration as well. This strategy produces superior results in the two domains that present deceptive challenges for search algorithms when compared to the performance of MAP-Elites.

### Strengths
The comparison between the proposed algorithm and the MAP-Elites algorithm has been fair and the results have been analyzed carefully and thoroughly.

### Weaknesses
The range of problems where the proposed algorithm would be useful, as covered by the two example problems given in the paper, are too narrow. Both problems take place on a 2D plane where the space-based subaggregation method can be applied naturally. I would like to see the proposed method applied in broader domains.

### Questions
For example, can this approach be used in solving Travelling Salesman Problems?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
