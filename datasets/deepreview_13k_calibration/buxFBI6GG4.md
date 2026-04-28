# Breaking the $\log(1/\Delta_2)$ Barrier: Better Batched Best Arm Identification with Adaptive Grids

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
We investigate the problem of batched best arm identification in multi-armed bandits, where we want to find the best arm from a set of $n$ arms while minimizing both the number of samples and batches. We introduce an algorithm that achieves near-optimal sample complexity and features an instance-sensitive batch complexity, which breaks the $\log(1/\Delta_2)$ barrier. The main contribution of our algorithm is a novel sample allocation scheme that effectively balances exploration and exploitation for batch sizes. Experimental results indicate that our approach is more batch-efficient across various setups. We also extend this framework to the problem of batched best arm identification in linear bandits and achieve similar improvements.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the classical best-arm-identification (BAI) problem in the batched setting. The batched setting means that the agent has only limited number of batches. In each batch the agents can arrange which arms and how many pulls for each arm and only receive the results of the pulls after this batch. In this setting, the classical BAI algorithms are not viable. 

The authors propose new batched BAI algorithms with adaptive batch sizes (the number of arms pulled in each batch), and achieve a sample complexity of \tilde{O}(\sum_i 1/\Delta_i^2), which is the first to break the bound of \tilde{O}(n/\Delta_2^2), where Delta_2 is the largest reward gap between the optimal and sub-optimal arms.

The authors also extend the batched BAI problems to the linear bandit scenarios and achieved similar results.

### Strengths
First, this paper studies a pretty interesting problem. Batched BAI is a very practical setting in industry. For instance for parameter tuning, people will not wait for the last model to complete training before starting another one, given each model training takes days. Batched BAI is a more practical setting for parameter tuning. However, there have not been enough works in this area. Hence, I think this paper is studying an impactful problem.

Second, the results in this paper are good. Ignoring the logarithmic parts, the algorithms have achieved the same sample complexity as the best of BAI. Although I guess ultimately, we should be able to achieve n\log(\delta^-1) sample complexity as classical BAI someday, the n\log(n)\log(n/\delta) is still good enough at this stage. The authors further extend the works to linear bandits. 

Third, the algorithms have some novelties. The algorithm uses precise allocations of the batch sizes in order to keep both sample complexity and batch complexity low.

### Weaknesses
Some numerical comparisons will strengthen this paper, and also illustrate the improvements of the proposed algorithms. 

Some minor suggestions about the writing. 1. Better not use \Delta_2 in abstract while not explaining it. It may cause confusion to some readers. 2. Present more details about the works in CL area, as they share a lot of similarities to the problem in this paper. 3. In the introduction, before using heavy math notations, try to use more natural words to explain what BAI is and what batched BAI is, which can help readers understand what this paper is doing.

### Questions
Any study on the lower bound on sample complexity given the lower bound batch complexity?

### Soundness
4

### Presentation
3

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
The paper considers the problem of batched best-arm identification with a goal of minimizing the batch complexity, which could be an issue for fixed-confidence best-arm identification depending on the minimal gap between the best arm and the second-best arm. The contributions include new algorithms for both k-armed bandit and linear bandit settings as extensions of classic algorithms.

### Strengths
- The first algorithm reduces the batch complexity dependence on the minimal gap between the best arm and the second-best arm.
- The paper is well-written and very easy to understand.

### Weaknesses
 - There are some improvements in the experiments, showing roughly a 2x gain, but it's hard to call them impressive, as the experiments are limited in scale and only cover simple problem instances. Additionally, there are no experiments on the linear bandit setting.
- The contribution mainly reduces a logarithmic factor in batch complexity by transferring it to sample complexity. However, it’s difficult to see an absolute impact on the field.

### Questions
The RAGE algorithm, which serves as the building block algorithm in this paper, has publicly available code. Since the proposed algorithm is an extension of it, I wonder if the authors could reproduce some results to demonstrate the improvements.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes two algorithms, instance-sensitive successive elimination and RAGE, where the batch complexities can outperform the $\log(1/\Delta_2)$ bound.

### Strengths
(1) Theoretically, the paper demonstrates that the proposed algorithms achieve near-optimal sample complexity while breaking the barrier for batch complexity.

(2) An instance-sensitive quantity, $R_I$, is introduced.

### Weaknesses
 (1) A significant issue is that the two algorithms lack empirical support, making it challenging to convince readers of their practical value.

(2) Breaking the $\log(1/\Delta_2)$ barrier appears to be conditional, depending on the number of arms with nearly optimal means being relatively limited compared to the total number of arms. In such cases, the allocation may rapidly focus on only a few arms. I am uncertain whether these algorithms offer any advantage over the original SE under these conditions.

(3) The issue of a small gap $\Delta_2$ is more serious in the fixed-budget setting and has been observed in Bayesian Best Arm Identification (BAI). For example, the paper Exploration for Fixed-Budget Bayesian Best Arm Identification (arXiv: 2408.04869) discusses this. More related work should be considered.

(4) Some parts of the paper are difficult to read, possibly due to the theoretical depth. For instances, it’s challenging to understand $R_1$ from Definition 1.1 across the three examples in Figure 1. $\Delta_2$ is undefined, though it appears to represent the gap between the best and second-best arms.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors conducted a study of the batched BAI problem in both MAB and linear bandit settings, and improved the existing bounds. They proposed IS-SE and IS-RAGE, which stem from the previous algorithms and both have good performance in some cases (outperformed the O(1/Delta) bound). The experiments also corroborated these results.

### Strengths
The authors proposed a new algorithm that, in some ways, improves the original result in MAB and linear bandits setting. The theoretical result is solid. The experiment was compared with the SE algorithm comprehensively.

### Weaknesses
The authors need to compare with more algorithms beyond SE. The novelty of the proposed algorithm is not clearly stated. Also, why is the proposed solution better?

The examples mention that: in certain cases, IS-SE can have fewer batches than log(1/Delta). Why is this the case and when would this happen?
- In this case, do other algorithms also need log(1/Delta) batch, or just the same as IS-SE？
- Does it truly imply O(1) batches ( since SE still need log(1/Delta))? This is not so clear.

### Questions
The examples mention that: in certain cases, IS-SE can have fewer batches than log(1/Delta). Why is this the case and when would this happen?
- In this case, do other algorithms also need log(1/Delta) batch, or just the same as IS-SE？
- Does it truly imply O(1) batches ( since SE still need log(1/Delta))? This is not so clear.

Post-rebuttal: the authors have provided responses that help answer these questions.

### Soundness
3

### Presentation
2

### Contribution
2
