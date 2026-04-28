# Optimization by Parallel Quasi-Quantum Annealing with Gradient-Based Sampling

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 3, 8

## Abstract
Learning-based methods have gained attention as general-purpose solvers due to their ability to automatically learn problem-specific heuristics, reducing the need for manually crafted heuristics. However, these methods often face scalability challenges.
    To address these issues, the \underbar{i}mproved \underbar{S}ampling algorithm for \underbar{C}ombinatorial \underbar{O}ptimization (iSCO), using discrete Langevin dynamics, has been proposed, demonstrating better performance than several learning-based solvers. 
    This study proposes a different approach that integrates gradient-based update through continuous relaxation, combined with \underbar{Q}uasi-\underbar{Q}uantum \underbar{A}nnealing (\textbf{QQA}).
    QQA smoothly transitions the objective function, starting from a simple convex function, minimized at half-integral values, to the original objective function, where the relaxed variables are minimized only in the discrete space.
    Furthermore, we incorporate parallel run communication leveraging GPUs to enhance exploration capabilities and accelerate convergence. 
    Numerical experiments demonstrate that our method is a competitive general-purpose solver, achieving performance comparable to iSCO and learning-based solvers across various benchmark problems. 
    Notably, our method exhibits superior speed-quality trade-offs for large-scale instances compared to iSCO, learning-based solvers, commercial solvers, and specialized algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this study, the authors present PQQA, an optimization approach that integrates QQA, gradient-based updates, and parallel run communication. The results indicate that PQQA performs comparably to or better than iSCO and other learning-based solvers across a range of combinatorial optimization (CO) problems. Notably, for larger problem instances, PQQA offers a superior trade-off between speed and solution quality.

### Strengths
The authors did a great job explaining the problem being considered, including the background, methodology, theoretical properties, and related work. The numerical experiments also effectively highlight their proposed method. While I did not check the validity of the proof in the Appendix, the setup and results are very convincing.

### Weaknesses
n/a

### Questions
1. In Table 1, some of the ApR values are greater than 1. Could the authors clarify what this means?

2.  While the authors mention runtime in the paper, there seems to be a discrepancy that needs further explanation. For example, in Table 1, iSCO takes about 5–15 minutes to achieve an ApR of 0.996, whereas PQQA takes over an hour for the same result. 

3.  Line 314 refers to Table 1 as Table 5.1. Please check for similar mistakes in other parts of the paper and ensure that table references are consistent throughout.

4. In line 60, the term "parameters" is used. Could the authors clarify what specific parameters are being referred to in this context?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes Parallel Quasi-Quantum Annealing (PQQA), a sampling-based algorithm for combinatorial optimization problems.  Specifically, with a continuous relaxation of the combinatorial optimization problem, an entropy metric to measure discreteness and sampling based on the Boltzmann Distribution, the authors develop an efficient general-purpose approach for combinatorial optimization.  Empirically, this approach yields high-quality solutions efficiently.

### Strengths
- **Novelty.**  Overall, this paper proposes a novel sampling-based approach for finding high-quality solutions to combinatorial optimization problems.  In particular, using $\alpha$-entropy with the extended Boltzmann Distribution is a well-motivated and novel approach for combinatorial optimization.  

- **Numerical Results.**  The authors provide extensive numerical comparisons on a wide variety of benchmarks.  These results demonstrate the PQQA can compute high-quality solutions on all instances, often at a reduced runtime compared to other methods.

### Weaknesses
Overall, I have quite a favorable opinion of the paper.  However, one significant weakness/limitation is provided below.  
- **Simple Constraints in Benchmarks.**  The authors evaluate the maximum independent set, max clique, max cut, graph partitioning, and graph coloring.  While these constitute many combinatorial optimization problems, they all have relatively simple constraints compared to problems such as TSP, which has an exponential number of constraints.  Approaches such as iSCO are capable of dealing with this type of structure.  However, it is unclear if something similar can be done with PQAA, given the reliance on continuous relaxation, which may be less tractable for problems with exponentially many constraints.  Overall, this may limit the applicability of such approaches.  Furthermore, the authors do not acknowledge this as a limitation or discuss this at all.  I would be happy to discuss this further in the discussion period.

### Questions
**Questions**
- How are the binary solutions obtained after running PQQA?  
- How often are these solutions feasible?  If infeasible, what is done with the solutions?
- Do the authors have any insight into how the strength of the LP relaxation of a problem affects the downstream solution quality?  
- Why is iSCO not compared against in Table 2?
- Why is this method not benchmarked on TSP?
- Is there a reason iSCO is much faster on Maximum Independent Set but slower on Max Clique?  

**Minor Remarks**
-  I suggest keeping the evaluation of times consistent, i.e., always use seconds or average time to solve an instance.  Comparing performance is difficult when switching between metrics for different tables and even within tables.  
-  Incorrect reference in Table E.1 in line 1125.

### Soundness
3

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
2

### Summary
The authors proposed a learning based method for CO problems by combing Quasi-Quantum Annealling and gradient-based update
through continuous relaxation. Performance are compared with iSCO on various benchmark problems.

### Strengths
parallel implementation on GPUs accelerates the solution process.

### Weaknesses
It seems that the algorithm does not have converence guarantees.

The algorithm cannot guarantee finding a feasible solution. constraints are moved to the objective function as a penalty term.

On benchmarks like SATLIB, it performs worse than traditional OR solvers like Gurobi.

The authors may consider larger benchmarks like MIPLIB 2017 to test the performance.

### Questions
The paper is based on the continuous relaxation of the discrete variable. Then why not directly solving the resulting linear programming problem?

### Soundness
3

### Presentation
3

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
The manuscript proposes a new methodology for combinatorial optimization, based on the integration of gradient-based updates and Quasi-Quantum Annealing. The manuscript is well-written using easy-to-comprehend language which led to a joyful read. The background is well-explained including prior work in the field. The computational experiments are well-chosen and comprehensive.

### Strengths
This is a strong paper. 
- Very good coverage of prior work (While I am not an expert in this field the sheer amount and frequency of citations is convincing)
- Clear introduction and background
- The main contribution seems novel
- The experimental results are very convincing

### Weaknesses
This is a strong paper in my opinion, and I identified only a few shortcomings. 
-  The results of the computational experiments are somewhat confusing. How can time be measured when so many different algorithms are involved? Aren't these codes in different languages? You might be able to give the reader a better intuition of your compute-time measurements. Specifically, the reported time measurements, denoted as [s/g], lack clarity regarding what is being measured. Is this time per gradient evaluation, or is it the total runtime? The comparison across different algorithms, some of which are gradient-free, makes this metric particularly difficult to interpret. Furthermore, the use of different programming languages and hardware platforms for the various algorithms introduces significant confounding factors that are not adequately addressed.

### Questions
- What do time measurements [s/g] really mean when different algorithms are compared? 
What is the time spent on? 
Are the time differences purely due to implementation differences? 
How do the different approaches scale?

### Soundness
4

### Presentation
3

### Contribution
4
