# Few for Many: Tchebycheff Set Scalarization for Many-Objective Optimization

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Multi-objective optimization can be found in many real-world applications where some conflicting objectives can not be optimized by a single solution. Existing optimization methods often focus on finding a set of Pareto solutions with different optimal trade-offs among the objectives. However, the required number of solutions to well approximate the whole Pareto optimal set could be exponentially large with respect to the number of objectives, which makes these methods unsuitable for handling many optimization objectives. In this work, instead of finding a dense set of Pareto solutions, we propose a novel Tchebycheff set scalarization method to find a few representative solutions (e.g., 5) to cover a large number of objectives (e.g., $>100$) in a collaborative and complementary manner. In this way, each objective can be well addressed by at least one solution in the small solution set. In addition, we further develop a smooth Tchebycheff set scalarization approach for efficient optimization with good theoretical guarantees. Experimental studies on different problems with many optimization objectives demonstrate the effectiveness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a scheme for many-objective problems with large number of objectives (e.g > 100) where the idea is to find a few representative solutions that address them.
To make this scheme possible they use their newly proposed Tchebycheff Set scalarization function that is an extension of the original. Now instead of trying to find a point that minimizes the scalarized problem, is trying to find multiple points that minimize it, allowing it to be bad for some of the m objectives, but it should at least minimize some subset of it.
The original Tchebycheff function is non differentiable to the max and min operators, which makes it not the best option to work with gradient based optimization. Therefore they extend the smooth Tchebycheff function in the work Lin et.al 2024 to work on set of solutions.

### Strengths
Scalarization that is well known to perform well on multi-objective problems as seen on different variants of the evolutionary algorithm MOEA/D. Tchebycheff as the scalarizing function has also been shown to cover the non-convex solutions in the Pareto Front. The regular approach only aims to have a solution per direction, by modifying the function to instead search for a set of points that while being good for the other objectives it should be the best for a subset of all objectives.

The text introduces well non multi-objective practitioners to the setting, the difficulty present in many-objective problems, and previous work and results on scalarization with the simple weighted sum and the Tchebycheff function.
Appendices further explore the effect of the smoothness parameter and complement the main text with more experiments.

### Weaknesses
It would have been nice to touch or at least mention dimensionality reduction techniques and problems with redundant objectives. Seems its the other side of the coin, given that there is some correlation in the objectives for them to be satisfied or addressed well with a single solution. As shown in Figure 2, each solution address 20 of the 100 objectives, does this mean that the underlying 100 objective problem can be summarized by a 5 objective problem? The paper does not explore the implications of this potential redundancy, particularly how the method's performance might vary across problems with different degrees of objective correlation. Furthermore, the method's computational cost, especially with a large number of objectives, is not sufficiently addressed. While the authors extend the smooth Tchebycheff function, the computational overhead of evaluating this function for a large set of solutions and objectives is a concern that should be discussed in more detail. The paper also lacks a discussion on how the number of solutions affects the performance of the proposed method. The experiments do not explore the sensitivity of the method to the number of solutions, and how this parameter should be chosen for different problems.

### Questions
Is possible this scheme to solve many-objectives problems works well due to some redundancy in the objectives, meaning, objectives are correlated so some solutions that perform well on one of them should also perform well in the positively correlated objectives.
Have you consider some dimensionality reduction techniques to maybe reduce which objectives should be evaluated during the scalarization?

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
4

### Summary
This paper proposes a novel scalarization method called TCH-Set to produce a limited number of solutions that handle many objectives. A relaxed version is also proposed to tackle the non-smooth situations. The theoretical properties of the proposed method are investigated, and an empirical study is conducted to verify its effectiveness.

### Strengths
1. This paper is well-written and easy to follow.
2. The proposed method is well-motivated. 
3. The technical details are clearly presented, and the theoretical analyses seem correct. 
4. The literature review is comprehensive.

### Weaknesses
My major concern is about the problem setting. The proposed method aims to find a few solutions that collaboratively optimize many objectives. This problem setting is quite different from the common setting in multi- or many-objective optimization, which aims to find some solutions with diverse trade-offs. I agree with the authors that one of the main obstacles in many-objective optimization is that, with the increase in the number of objectives, the number of solutions has to increase exponentially to cover the whole PF. The idea proposed in this paper is interesting; however, I do not think it really solves this problem. When the number of objectives is very high, it only searches for extreme points, that is, solutions with very low values for some objectives but significant sacrifices in others. By putting together these multiple extreme points, it appears as if multiple objective functions can be "simultaneously" optimized. Actually, although many MOAs output a set of solutions, after multi-objective decision-making, typically only one solution is finally selected, and, in practice, solutions with a more balanced tradeoff are often preferred. Therefore, while the TCH-Set offers a novel idea for many-objective optimization, I think its practical impact and significance are limited.

### Questions
Please refer to "Weaknesses". Additionally, I suggest the authors summarize a notation table in the appendix.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Different from general multi-objective optimization aiming to find a dense Pareto set, this paper focuses on identifying a few solutions that cover a large number of objectives in a complementary manner for many-objective optimization. To achieve this, a smooth Tchebycheff set scalarization approach is developed with good theoretical guarantees.

### Strengths
1. This paper introduces a novel and practical prospective in tackling for many-objective optimization.
2. This paper develops a smooth Tchebycheff set scalarization approach under the few-for-many prospective.
3. The theoretical analysis is thorough and well-supported.

### Weaknesses
Some descriptions lack clarity, and minor writing errors are present. Please refer to the questions below for the details.

1. After the Tchebycheff set scalarization, how is the scalarized problem solved, given that a set of solutions needs to be optimized?
2. Did the methods compared in the experiments also propose the few-for-many prospective for many-objective optimization?
3. What optimization methods are used under the scalarization methods for the convex multi-objective optimization in Section 4.1?
4. A brief analysis of why STCH-Set performs slightly worse than SoM in two cases in Table 4 would be beneficial.
5. It should be clarified why the part results of MosT are “-” in Table 6.
6. All mathematical symbols (e.g., $K$ and $m$) in the tables should use the correct mathematical formatting.
7. In line 227, a space is missing after the period.
8. In line 1473, there is an incorrect line break, and “term0” appears to be a typo.
9. In line 1487, a space is missing before “(S)TCH”.
10. An open question is whether the proposed approach is especially suited for many-objective optimization with non-conflicting objectives. How would it perform when all objectives are conflicting?

### Questions
1. After the Tchebycheff set scalarization, how is the scalarized problem solved, given that a set of solutions needs to be optimized?
2. Did the methods compared in the experiments also propose the few-for-many prospective for many-objective optimization?
3. What optimization methods are used under the scalarization methods for the convex multi-objective optimization in Section 4.1?
4. A brief analysis of why STCH-Set performs slightly worse than SoM in two cases in Table 4 would be beneficial.
5. It should be clarified why the part results of MosT are “-” in Table 6.
6. All mathematical symbols (e.g., $K$ and $m$) in the tables should use the correct mathematical formatting.
7. In line 227, a space is missing after the period.
8. In line 1473, there is an incorrect line break, and “term0” appears to be a typo.
9. In line 1487, a space is missing before “(S)TCH”.
10. An open question is whether the proposed approach is especially suited for many-objective optimization with non-conflicting objectives. How would it perform when all objectives are conflicting?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Authors propose a novel Tchebycheff set scalarization method to find a few representative solution to cover a large number of objectives
 in a collaborative and complementary manner so that each objective can be well addressed by at least one solution in the small solution set.

### Strengths
* This paper is well-written and easy to follow.

* The experiments are comprehensive and include necessary analyses, and the results are convincing.

* The necessary proofs are included.

### Weaknesses
 * This novelty is somewhat limited. It seems the line 74 “a novel Tchebycheff set (TCH-Set) scalarization approach”  has been proposed in [1] and the line 75 “a smooth Tchebycheff set (STCH-Set) scalarization approach” has been proposed in [2].

* The motivation is not quite clear. Why should you find a few representative solutions to cover a large number of objectives?  The paper does not adequately explain the practical need for this specific problem formulation. It is unclear why a single, well-balanced solution would not suffice in many scenarios, and what inherent limitations of existing methods necessitate this approach.

* The work is not tied to particular applications. Can you briefly provide some scenarios where your method is applicable? The paper lacks concrete examples of real-world problems that would benefit from the proposed method. Without specific use cases, it is difficult to assess the practical impact and relevance of the research.


### Questions
* The experiments are conducted with different K, how to choose the K of your algorithm?

* Since the preference $\lambda$ can greatly impacts the final result, could you please provide with some hints for choosing  $\lambda$?

Reference：
1.  Eng Ung Choo and DR Atkins. Proper efficiency in nonconvex multicriteria programming. Mathematics of Operations Research, 8(3):467–470, 1983.
2.  Xi Lin, Xiaoyuan Zhang, Zhiyuan Yang, Fei Liu, Zhenkun Wang, and Qingfu Zhang. Smooth tchebycheff scalarization for multi-objective optimization. arXiv preprint arXiv:2402.19078, 2024.

### Soundness
2

### Presentation
3

### Contribution
3
