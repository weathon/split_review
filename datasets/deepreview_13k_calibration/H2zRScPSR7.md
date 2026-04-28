# A Framework for Finding Local Saddle Points in Two-Player Zero-Sum Black-Box Games

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Saddle point optimization is a critical problem employed in numerous real-world applications, including portfolio optimization, generative adversarial networks, and robotics. It has been extensively studied in cases where the objective function is known and differentiable. Existing work in black-box settings with unknown objectives that can only be sampled either assumes convexity-concavity in the objective to simplify the problem or operates with noisy gradient estimators. In contrast, we introduce a framework inspired by Bayesian optimization which utilizes Gaussian processes to model the unknown (potentially nonconvex-nonconcave) objective and requires only zeroth-order samples. Our approach frames the saddle point optimization problem as a two-level process which can flexibly integrate existing and novel approaches to this problem. The upper level of our framework produces a model of the objective function by sampling in promising locations, and the lower level of our framework uses the existing model to frame and solve a general-sum game to identify locations to sample. This lower level procedure can be designed in complementary ways, and we demonstrate the flexibility of our approach by introducing variants which appropriately trade off between factors like runtime, the cost of function evaluations, and the number of available initial samples. We experimentally demonstrate these algorithms on synthetic and realistic datasets, showcasing their ability to efficiently locate local saddle points in these contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new framework for finding local saddle points in zeroth-order black-box saddle point optimization. 
The authors propose a bilevel framework inspired by Bayesian Optimization (BO) that leverages Gaussian Processes (GPs) to model the unknown objective function. The lower-level game uses confidence bounds from the GP to define a general-sum game, the solution of which (a local Nash point) is used to guide sampling of the objective function. The high-level game updates the GP model with the new samples and iteratively searches for a local saddle point. The empirical results show that BSP variants outperform baseline approaches like naive random sampling and zeroth-order gradient descent-ascent on these problems.

### Strengths
This paper addresses a problem that has received limited attention in the literature: the optimization of black-box games. It introduces a novel framework that combines a diverse set of techniques to tackle this challenge, making it a noteworthy contribution.

### Weaknesses
 - Limitations of modeling with GP: We know that the required number of samples to accurately model the objective function grows exponentially, leading to increased computational complexity and potentially reduced accuracy. Do you plan to address this limitation in future work?
- The experiments are ultimately not convincing: while the experiments on synthetic data successfully achieve the optimal merit function, the real-world examples are less successful compared to the only other baseline and require further improvement.
- Lack of sufficient theoretical guarantees for the method: While Lemma 4.1 demonstrates the convergence of LLGAME to a Local Nash Point (LNP), the paper lacks a theoretical analysis proving the convergence of the overall Bayesian Saddle Point (BSP) algorithm to a Local Saddle Point (LSP). This is particularly important, as the authors acknowledge that the LNP returned by LLGAME might not necessarily be an LSP of the original objective function.

### Questions
Did you consider comparing your method with first-order algorithms? Incorporating them as a baseline can provide valuable insights.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the problem of finding local saddle point in two-player zero-sum games, in which the objective function is unknown and can only be accessed through zeroth-order samples. The authors approach the problem through Bayesian optimization, introducing a bi-level optimization algorithm where the lower-level solves a general-sum game and upper level uses Gaussian processes to build a surrogate model for the objective. The authors illustrate the algorithm performance through numerical simulations.

### Strengths
The paper targets an important problem, which is to solve two-player zero-sum games in the general nonconvex-nonconcave setting with only zeroth-order samples. The introduction and description the algorithm makes general sense. The numerical simulation verifies the algorithm performance to a certain extent.

### Weaknesses
My main concern is that the authors do not provide sufficient understandings for the proposed algorithm either in theory or through experiments.

The paper lacks rigorous mathematical justification, and the explanation on why the proposed algorithm is expected to work is made in a very hand-wavy manner. Most existing works on two-player zero-sum games come with end-to-end analysis on convergence rate/sample complexity. Rigorous theoretical results allow us to judge algorithms in terms of efficiency, restrictiveness of assumptions, etc. Without such theoretical results, it is hard to compare the proposed algorithm with those in the existing literature and those to be introduced in the future.

Regarding the takeaways highlighted in line 478-510 -- this is a plausible explanation that matches the observation from a few small-scale experiments. Much more extensive experiments need to be conducted to verify the statement. In the absence of theoretical convergence guarantees, systematic numerical simulations are especially important for understanding the algorithm performance, but they are currently missing.

### Questions
Minor comments:

1) The phrasing of the abstract and introduction line 043-046 gives the impression that the authors consider $f$ which is not necessarily differentiable. However, it turned out later a second-order differentiability assumption is needed. The abstract and introduction should be revised for better clarity.

2) In Algorithm 1 line 4 and Algorithm 2 line 7, you are not returning $\bar{x}^*,\bar{y}^*$/$x^*,y^*$. You are returning the iterates as an estimate of $\bar{x}^*,\bar{y}^*$/$x^*,y^*$.

### Soundness
3

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
This paper presents a novel framework for finding local saddle points in two-player zero-sum black-box games. The authors propose a bilevel approach that combines Gaussian processes to model the unknown, nonconvex-nonconcave objective and a lower-level game to identify sampling locations.

### Strengths
1. The framework innovatively combines ideas from Bayesian optimization with saddle point optimization in a black-box setting. It offers a zeroth-order technique for finding saddle points.
2. The explanation of the bilevel optimization framework is well-organized. 
3. The ability to identify saddle points in nonconvex-nonconcave black-box settings is highly relevant for a wide range of applications, particularly those involving adversarial dynamics and game theory.
4. The experimental results are comprehensive, and the ablation studies have been conducted.

### Weaknesses
1. The theoretical guarantees of the algorithm in this paper are somewhat insufficient, with only Lemma 4.1 used to show that the algorithm converges to a local Nash point, and the assumptions made are rather strong.
2. The paper lacks a dedicated "Related Work" section. It appears that the related work has been split into two parts, placed separately in Section 1 and Section 2.

### Questions
1. Could you provide more theoretical analysis of the algorithm? The current analysis is somewhat limited, and there is no discussion on the rationale behind the assumptions in Lemma 4.1. Please offer an explanation here.
2. I suggest reorganizing Section 1 and Section 2. The current structure is somewhat disorganized and lacks a systematic introduction to prior work.
3. How to incorporate second-order sufficient conditions to enhance the performance of your approach? Please gives further explanation.

### Soundness
3

### Presentation
3

### Contribution
3
