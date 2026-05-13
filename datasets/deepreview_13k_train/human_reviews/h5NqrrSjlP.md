# GESR: A Geometric Evolution Model for Symbolic Regression

- Decision: Reject
- Scores: 5, 3, 5, 5, 5

## Abstract
Symbolic regression is a challenging task in machine learning that aims to automatically discover highly interpretable mathematical equations from limited data. Keen efforts have been devoted to addressing this issue, yielding promising results. However, there are still bottlenecks that current methods struggle with, especially when dealing with complex problems containing various noises or with intricate underlying mathematical formulas.
In this work, we propose a novel Geometric Evolution Symbolic Regression(GESR) algorithm. Leveraging geometric semantics, the process of symbolic regression in GESR is transformed into an approximation to an unimodal target in n-dimensional topological space. Then, three key modules are proposed to enhance the approximation: (1) a new semantic gradient concept, proposed to assist the exploration, which aims to improve the accuracy of approximation; (2) a new geometric search operator, tailored for approximating the target formula directly in topological space; (3) the Levenberg-Marquardt algorithm with L2 regularization, used for the adjustment of expression structures and the balance of global subtree weights to assist the proposed geometric semantic search operator. With the proposal of these modules, GESR achieves state-of-the-art accuracy performance on multiple authoritative benchmark datasets and demonstrates a certain level of robustness against noise interference. The implementation is available at https://anonymous.4open.science/r/12331211321-014D.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper identifies a problem with the prevailing genetic programming (GP) methods for symbolic regression: the random cross-over policy adopted makes GP less effective in generating promising formulas. Consequently, the paper introduces a semantic geometric evolution algorithm, which maps the expression search space into a target semantic search space to approximate the mutation operations. The semantic gradients and the geometric semantic method are proposed to help guide search in the high dimensional sub-semantic search space for mutations, with the Levenberg-Marquardt algorithm with L2regularization adopted for constants optimization and local structure adjustments.

### Strengths
**1)** The motivation for the paper is clear, and the semantic geometric evolution algorithm is an interesting idea to incorporate guidance for mutations.

**2)** The proposed semantic gradients address the inconsistency of the sub-semantic space and the target semantic space.

**3)** Conducted experiments on well-recognized SRBench and other datasets. Ablation studies support the claimed ideas.

### Weaknesses
 **1)** The definitions for the notations and terminologies are ambiguous and missing, making the methodology part hard to follow. For example:
 ***1.*** In line 159 "n-dimensional semantic space", what does $n$ represent here? Is it the dimension of the feature or the dimension of the train set as explained in line 249? Same question as in equation (2).
***2.*** In line 187, what does  $s_i$ represent here? I understand it may refer to the semantics of the subtree, but only list subtree $tr$ may be misleading. 
***3.*** In line 232, what is the dimension of the subtree? Is it the same dimension of $n$?
***4*** Notation conflicts for $k$ in 269 "top-k" candidates and equation (7)
***5.*** In equation (11), is the summation over $j$? In line 324 and equation (11), what do $i$ and $j$ represent here as the superscript?

**2)**  A typo in line 269: following m subtree(subtrees) for each $tr_1$ is(are) chosen to form the candidate set.

**3)** The benchmark baseline models are not state-of-the -art.

**4)** The organization of the notations is unclear. For instance, in line 259, the syntax "migrate the distribution of candidate semantics $s'$ to the sub-target semantics $st$" is not immediately clear. It would be more effective to position the syntax closer to its definition. Without this adjustment, readers might struggle to identify which term represents the candidate semantics in Equations (4) and (5).

**5)** The syntax currently employs a complex system of subscripts and superscripts, and several symbols appear without explicit definition (e.g., notations in Figure 1). This makes the paper hard to follow and requires the reader to make assumptions about the meaning of the symbols.

**6)** From Figure 4 (model size) and Table 9 (appendix), it seems that GESR tends to generate formulas that are notably large and lengthy, even after simplification. This might suggest a tendency for GESR to produce high-complexity expressions that may indicate overfitting to the Feynman problems. While this behavior might be acceptable if accuracy is the primary evaluation metric, it becomes problematic when using recovery rate, which requires the generated expressions to match the exact ground truth form.

### Questions
**1)** Can you provide explanations concerning the above notations and terminologies?

**2)** How do you obtain the sub-target semantics $st$ for the loss calculation in line 274 as well as the semantic gradients in equation (3)?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the geometric evolution symbolic regression (GESR) algorithm which introduces new concepts of semantic gradients and semantic mutation to the existing geometric semantic genetic programming.

### Strengths
Sufficient relevant literature is cited in related works.

### Weaknesses
The clarity of the paper could be improved with clearer self-contained definitions of the terminologies used. For example, in the introduction, the paper should have a self-contained description of what ‘semantic space’ is in the context of this paper, to avoid potential misinterpretation that it is a novel concept introduced. “Underlying n-dimensional topological space” is not a sufficient description given that “n” is not even defined. 

The paper should also be clearer on what is novel. For instance, the section on constant optimization might be misinterpreted as a novelty when it has been used in several prior works such as [1] and [2]. The paper introduces the Levenberg-Marquardt algorithm as a key module that is proposed/introduced by the paper, when it has already been utilized in many prior works like [1] and [2]. The paper states that "Then, three key modules are proposed to enhance the approximation: (1) ...; (2) ...; (3) the Levenberg-Marquardt algorithm with L2 regularization, used for the adjustment of the expression structures and the optimization of constants." This phrasing suggests that the use of the Levenberg-Marquardt algorithm for constant optimization within symbolic regression is a novel contribution, which is not the case. Similarly, the statement "(3) We introduce the concept of using a continuous optimization algorithm to assist in adjusting the expression structure." is also misleading, as other works have used continuous optimization for similar purposes [1,2]. The core issue is that the listed contributions are not sufficiently precise and can be easily misinterpreted as overlapping with existing methods.

Selection of SR algorithms used for comparison are not consistent across datasets. In SRSD datasets, more recent works such as E2E and uDSR are evaluated, but these are missing in the SRBench datasets. Likewise, non-SR based algorithms are evaluated in the SRBench datasets, but not for SRSD datasets. The paper lacks comparison against more recent SR algorithms such as [3]. This is important because the main strength of the algorithm introduced in this paper is in its prediction performance, which should include more recent works which also claim to have improved prediction performance. Otherwise, the paper should explain the criteria for selecting comparison algorithms and include a strong justification if recent methods are excluded. For example, Operon, which has a largely overlapping R2 score range with GESR but a much smaller, non-overlapping model size, is not considered in the SRSD evaluation. This inconsistent selection of baselines makes it difficult to assess the true performance of the proposed method.

The paper lacks important comparison against geometric semantic evolution algorithms. Examples such as GSGP (and others mentioned in line 105 to 106 of the paper) are cited in the second paragraph of “Related Works”, but never compared to in the evaluation. The algorithm proposed seem impractical for real-world usage since the equation size is large (above a size of 100 on average), especially in comparison to existing symbolic regression methods, as shown in Figure 4. Since the paper introduces SR as a machine learning method with the key strength of interpretability, the size of the equations discovered by the proposed method does not seem consistent with the interpretable aspect. The paper should also tune the hyperparameters of the benchmark SR methods to encourage larger model size to determine if higher R2 test performances could be achieved by trading-off equation size. Currently, it is unclear if GESR simply performs better on R2 test because it allows for a larger equation size. Since the semantic approach does not scale as well with the size of the data, a runtime analysis of the methods (i.e., training time) should be conducted and reported. Currently, it is unclear to the reader whether the comparison against existing SR algorithms was done under fair settings.

### Questions
In the abstract, methodology and conclusion, why is the Levenberg-Marquardt algorithm framed as a key module that is proposed/introduced by the paper when it has already been utilized in many prior works like [1] and [2]?

Can the paper use a consistent set of SR benchmark algorithms across the various datasets and include comparison against existing geometric semantic genetic programming algorithms (see works cited in lines 105 to 106 of the paper)?

The paper states that "The proposed algorithm significantly improves the fitting performance of symbolic expression while
effectively tackling concerns associated with tree bloating", yet the results (specifically Figure 4), do not provide evidence for this.

[1] Kommenda, M., Burlacu, B., Kronberger, G., & Affenzeller, M. (2020). Parameter identification for symbolic regression using nonlinear least squares. Genetic Programming and Evolvable Machines, 21(3), 471-501.

[2] De Melo, V. V., Fowler, B., & Banzhaf, W. (2015, November). Evaluating methods for constant optimization of symbolic regression benchmark problems. In 2015 Brazilian conference on intelligent systems (BRACIS) (pp. 25-30). IEEE.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose GESR, a symbolic regression method Leveraging geometric semantics. the process of symbolic regression in GESR is transformed into an approximation to an unimodal target in n-dimensional  topological space.  A new geometric search operator is proposed to improve the search efficiency of the algorithm. The experimental results show that GESR has good performance.

### Strengths
1. Introducing SGP into symbolic regression. To a certain extent, it can indeed improve the traditional GP algorithm mutation and crossover without guidance, improving the overall efficiency of the algorithm.

2. From the experimental results of the paper, GESR obtained very good results.

### Weaknesses
1. Why is the maximum noise level chosen in the article only 0.01? I remember that the noise level of the SRBench dataset was added to 0.1. Please explain why the algorithm's performance at 0.1 noise level was not tested.
2. The experiment is not complete, there is no inference time (for the same expression, the time spent by different algorithms to obtain the same index, which is related to the operation efficiency of the algorithm), expression complexity evaluation (such as the number of symbols of the expression. Because it is meaningless to obtain a good goodness-of-fit with a very complicated expression), which is extremely important to prove the performance of the algorithm.
3. The baselines selected in this article are quite old. Why did the author choose these baselines? I suggest that the author compare with the latest algorithms.  Such as SNIP(https://doi.org/10.48550/arXiv.2310.02227) and so on. And, if we have DSR, why not compare it with the stronger DSO(NGGP):https://doi.org/10.48550/arXiv.2111.00053?  These strong baselines are more reflective of the comprehensive performance of GESR.

### Questions
1.  I hope the author highlights and emphasizes your motivation more clearly in the introduction section. 
2. The algorithm needs to be improved in the methods section, which as a whole is hard to follow and took a long time to understand. I also want to reorganize the language. For example, how GESR guides mutation and crossover.
3. Below Equation 1. Semantic genetic programming (GP) -- > Semantic genetic programming (SGP).
4. The resolution of the pictures in Figure 4 and Figure 5 seems to be insufficient, and they are blurred when enlarged

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a new method for symbolic regression based on geometric semantics. They introduce the Semantic Gradient, a novel approach that guides adjustments to an expression tree by indicating the direction and magnitude of changes required within each subtree. This approach enables more targeted and effective mutations during the evolutionary process. Additionally, the authors introduce other key steps, such as a variance-based constraint and a novel evaluation function, to avoid local overfitting and enhance exploration. The constants are then optimized using the Levenberg-Marquardt (LM) method with L2 regularization to improve robustness.
In their experiments, they demonstrate that this new methods achieve state-of-the-art performance (in terms of R2>0.999) on both the SRBenchmark and the SRSD+ Dataset.

### Strengths
The authors demonstrate that their method achieves state-of-the-art performance across a wide range of benchmarks.
They have released the code with their submission (which however could not be run due to the absence of the requirements.txt file)

### Weaknesses
The methodology is unfortunately difficult to follow and understand. A clear example guiding the reader through the key steps and illustrating how these steps work together (either in the main paper or in an appendix) would have been valuable.

For the SRSD+ dataset, there appears to be a significant performance improvement over other baselines; however, some important methods are missing from the comparison (though they are included in SRBench). The authors should also consider testing competitive baseline methods such as Operaon and SBP-GP on this benchmark. The lack of consistent baselines across benchmarks makes it difficult to assess the true performance gains of the proposed method. Specifically, the claim that the method improves by a certain percentage over the second-ranked method is potentially misleading, as different methods are used in different benchmarks, and it is possible that a method from the SRBench comparison would outperform the second-ranked method on the SRSD+ dataset. The inconsistent use of terminology, such as “SRSD+ Dummy Variables” in Table 1 versus “SRSD” in the text, further complicates the comparison.

An analysis of computational requirements is missing. It is unclear how long the algorithm takes to fit an equation and how this compares to other baselines. Ideally, it would be useful to see the performance of this novel method against some of the other baselines with an equivalent computational budget.

### Questions
In your experiments, did you use the same computational budget as the baselines? If not, could you conduct an evaluation where the same compute time is allocated to your approach, Operaon, and SBP-GP, and analyze the results?

How does your method compare with others in terms of interpretability? Are the resulting formulas human-readable, or do they tend to be extremely long? It might be interesting, for example, to have the symbolic form of all your expressions on the Feynman dataset.

A similar approach, SBP-GP, seems almost equivalent to your method in terms of performance in Figure 4 and Table 9, yet you outperform it on Feynmann and Strogatz (Figure 5). Do you have an explanation for this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors propose a concept of semantic gradient to help genetic programming evolve better.

### Strengths
The strength of this paper is its strong performance on SRBench.

### Weaknesses
The weakness of this paper is that the contribution is unclear. The paper needs significant improvement to clarify the advantages of the proposed method over traditional semantic backpropagation. Here are some questions that need to be addressed:
1. What is the difference between the proposed method and traditional semantic backpropagation with linear scaling [1]? The current explanation of semantic gradient is not convincing, as the gradient should be with respect to the loss, not the function itself, to directly reflect its impact on the loss.
2. Using the Levenberg-Marquardt algorithm to optimize constants is not novel in the symbolic regression domain [2]; it should not be claimed as a contribution. Furthermore, without L1 regularization, it is unclear how the method can effectively prune redundant subtrees, as L2 regularization tends to shrink all coefficients rather than eliminating them.
3. The definition of $M$ on line 324 is confusing, as both $i$ and $j$ are mixed. Please ensure consistent notation.
4. In Equation (6), it seems the proposed method linearly combines two subtrees with weights. Why doesn’t this method suffer from the issue of exponential growth [3]? Please explain.
5. Equations (8) and (9) only eliminate some candidates from the candidate set, and the remaining candidates are evaluated. How does the proposed method ensure a fair comparison of computational complexity with baseline methods?
6. A related question is that training time is not shown in Figure 4. Without a comparison of training times, it is hard to know whether the proposed method genuinely improves existing methods or simply increases computational budget to achieve better results.
7. Pseudocode 1 should be included in the main paper instead of the supplementary material. Without the pseudocode, it is difficult to understand the proposed method.
8. The final section, "Conclusion," is missing a section number. Please fix this issue.
9. There should generally be a space between the text and references. Please add spaces where needed.
10. It is unclear why both $\alpha$ and $k$ are needed in Equation (6). $\alpha$ alone should be sufficient, and least squares can determine the optimal $\alpha$. On page 6, $t$ and $m$ are two hyperparameters that determine the number of combinations for trials. Please provide the specific values used in this paper.

### Questions
Here are some questions that need to be addressed:
1. What is the difference between the proposed method and traditional semantic backpropagation with linear scaling [1]?
2. Using the Levenberg-Marquardt algorithm to optimize constants is not novel in the symbolic regression domain [2]; it should not be claimed as a contribution.
3. The definition of $M$ on line 324 is confusing, as both $i$ and $j$ are mixed. Please ensure consistent notation.
4. In Equation (6), it seems the proposed method linearly combines two subtrees with weights. Why doesn’t this method suffer from the issue of exponential growth [3]? Please explain.
5. Equations (8) and (9) only eliminate some candidates from the candidate set, and the remaining candidates are evaluated. How does the proposed method ensure a fair comparison of computational complexity with baseline methods?
6. A related question is that training time is not shown in Figure 4. Without a comparison of training times, it is hard to know whether the proposed method genuinely improves existing methods or simply increases computational budget to achieve better results.
7. Pseudocode 1 should be included in the main paper instead of the supplementary material. Without the pseudocode, it is difficult to understand the proposed method.
8. The final section, "Conclusion," is missing a section number. Please fix this issue.
9. There should generally be a space between the text and references. Please add spaces where needed.
10. It is unclear why both $\alpha$ and $k$ are needed in Equation (6). $\alpha$ alone should be sufficient, and least squares can determine the optimal $\alpha$.

[1]. Virgolin, Marco, Tanja Alderliesten, and Peter AN Bosman. "Linear scaling with and within semantic backpropagation-based genetic programming for symbolic regression." Proceedings of the Genetic and Evolutionary Computation Conference. 2019.  
[2]. Kommenda, Michael, et al. "Parameter identification for symbolic regression using nonlinear least squares." Genetic Programming and Evolvable Machines 21.3 (2020): 471-501.  
[3]. Martins, Joao Francisco BS, et al. "Solving the exponential growth of symbolic regression trees in geometric semantic genetic programming." Proceedings of the Genetic and Evolutionary Computation Conference. 2018.

### Soundness
2

### Presentation
2

### Contribution
2
