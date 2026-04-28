# Analytic DAG Constraints for Differentiable DAG Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Recovering underlying Directed Acyclic Graph (DAG) structures from observational data presents a formidable challenge due to the combinatorial nature of the DAG-constrained optimization problem. Recently, researchers have identified gradient vanishing as one of the primary obstacles in differentiable DAG learning and have proposed several DAG constraints to mitigate this issue. By developing the necessary theory to establish a connection between analytic functions and DAG constraints, we demonstrate that analytic functions from the set 
$\\{f(x) = c_0 + \sum_{i=1}c_ix^i|c_0 \geqslant 0; \forall i > 0, c_i > 0; r = \lim_{i\rightarrow \infty}c_{i}/c_{i+1} > 0\\}$
can be employed to formulate effective DAG constraints. Furthermore, we establish that this set of functions is closed under several functional operators, including differentiation, summation, and multiplication. Consequently, these operators can be leveraged to create novel DAG constraints based on existing ones. Using these properties, we designed a series of DAG constraints and designed an efficient algorithm to evaluate these DAG constraints. Experiments on various settings show that our DAG constraints outperform previous state-of-the-arts approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The submission presents a mathematical derivation of a family of analytical DAG constraints that can be used in the recent proposals of smooth optimization for DAG search, 
Theoretical results are proposed to show that the derivation is valid and that the proposed family has favorable properties to be used in the optimization algorithms. 
Additionally, a large set of experiments is performed.

### Strengths
- The paper is generally well written (except for some minor details, see suggestion section in Questions) and well structured. 
- The experiments section is quite extensive (even if the number of replications could be bigger). 
-  The theoretical part seems sound and it is well written (I have not checked the full proofs on the supplementary). 
- The subject is interesting even if theoretically it is restricted to equal noise variance and linear SEM.

### Weaknesses
 - In the simulation experiments, it would be nice to have a larger number of replicates instead of 10.  I understand the time complexity but 
maybe lower dimensional systems could be explored with a higher number of repetitions to have a set of more robust results that could complement the proposed ones. 
- In the experiments section the CausalDiscoveryToolbox is used to run some of the state-of-the-art methods. I would discourage that. the CausalDiscoveryToolbox would be a nice tool, but unfortunately, it is no longer maintained, While probably there are no issues in running the wrapper of other algorithms provided there I would suggest the author of this submission use other implementations. For example, PC and GES in the CausalDiscoveryToolbox are wrappers of the pc-alg R implementations, I would suggest to use directly those for reproducibility and additional safety. 
- Is the code for the experiments and the implementation available somewhere? I did not find it in the submission

### Questions
### suggestions

For general suggestions see Weaknesses, additionally:

1. In the first paragraph of the Introduction: "the recovered DAGs can constitute a causal graphical mode"  --> "the recovered DAGs could be interpreted causally" or something similar, as the DAG by itself can't be a causal model since it lacks at least a compatible model for the probabilities or more generally a functional causal model.
2. End of second paragraph in Introduction: "w.r.t number of nodes(Chickering, 1996" a space is missing after "nodes".
3. In "as demonstrated in Wei et al. (2020). This study reveals that"  The  "This" in the beginning of the second sentence refer to Wei et al. (2020) but it could be mistakenly taken as "This study == this paper" I suggest to change the wording to clearer reflect that the following is work in Wei et al. (2020).
4. Section 2 Preliminaries: Similar to suggestion 1. above,  I think $\mathcal{G}$ should only denote a DAG (that is a graph). And not a DAG model (which is not even clear what a DAG model is). Then given a DAG the authors could define what a compatible statistical model or directly a compatible SEM is (that is when the probability factorizes according to the DAG or for the linear SEM with indep. noise that the matrix B encodes a weighted adjeceny matrix of the graph G). 
5. It would be nice to have an extended intuitive explanation for the following: "Due to the fact that the adjacency matrix of a DAG must form a nilpotent matrix, we do not need a function with infinite convergence radius"
6. before section 4 starts, "mainly due to the non-convexity of the overall objective functionNg et al. (2023)." a space is missing after "function" and before "Ng et al.". 
7. In caption of Table 1: "t state-of-the-arts DAGMA(Bello et al., 2022)," a space is missing after DAGMA. 
8. Table 3, is the value for GES wrong? it seems to be one order of magnitude bigger ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
the paper proposes a framework on continuous DAG constraints, based on analytic functions. It shows many existing dag constraints can be unified under such a framework. Specific choices on the analytic functions can improve computation efficiency, and in experiments even accuracy due to vanish gradient problems.

### Strengths
- The paper investigate in depth some properties of analytic function based DAG constraints, which shows some insights 

- Empirically extensive experiments are performed. The results show the method can outperform existing baselines.

### Weaknesses
 - Some convergence statements, such as convergence rate and eror bound, of using these analytic functions would be good to further improve the understanding of these constraints. 

- Experiments contain some mixed messages, and it seems performance depends on data property and choices of orders. These make the proposed constraints harder to use in practice.

Specific Comments:
- L136: f(B) in the form of eq 3 or eq 4?
- L152: how efficient of these algorithms?
- L158: beside exponential, polynomial also holds the property. Any other function classes with such property? Could they be used as DAG constraints, any pro and cons?
- L224: how much can this acutally save in practice?
- What is the complexity of Algoritahm 1, compared to standard computations?
- L305~307: missing sentences here?
- Given the convergence property of analystical functions, one natural question to ask is: what are the convergence rates and error bounds of  the formulation using these function based dag constraints? how does different convergence radius affect these bounds?
- Experiments shows different orders of the propsed constraint, but it is unclear which order should be used in practice. 
- Computation time comparison on constraints here would also be good to justify author's claim on efficiency. 
- What are the differences between table 5 and 6? Titles are the same but the results are very different. Table 6 and 7 also show DAGMA are better, instead of the claim in table titles? Is the message that DAGMA should be use for large scale graphs? I assume this is true because longer paths exists and hence needs more orders?

### Questions
see above

---------------------- after rebuttal
thank the authors for the new updated results. It would be good to have a formal statement around error bounds, which is not yet in the draft. I have raised my score accordingly.

### Soundness
3

### Presentation
2

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
The paper tackles the gradient vanishing problem of the DAG constraints in differentiable DAG learning methods. The main contributions are:
1. Showing that any analytic function can be used as a DAG constraint and unifying existing constraints into this framework. In addition, the closeness property of the function class allows for easy generation of constraints with large gradient magnitude.
2. An algorithm for choosing the spectral radius to amplify the gradient during training.
3. Demonstrating the outperformance of the proposed method through extensive experiments on linear simulated data and non-linear real data.

### Strengths
1. The class of analytic DAG constraints unifies the existing DAG constraints. In addition, the author provides a simple solution to amplify the gradient by multiplying the constraint function.
2. The discussion on the convexity of the DAG constraints provides intuition on the behavior of the high-order constraint, suggesting a tradeoff between the convexity and the gradient magnitude may be considered.
3. The experiments are extensive. The proposed method is evaluated on different DAGs ranging from low-dimensional to high-dimensional and the outperformance is well-established.

### Weaknesses
1. Some statements could be more rigorous. For example, 
   * Lines 304-307, the discussion of the optimization objective (17). Why the statement is only restricted to Gaussian SEMs? According to Loh and Bühlmann, (2013), MSE is valid for the linear equal variance model and is proved to have good performance by Bello et al. (2022). For unequal noise variance, MSE can be inconsistent. The second sentence is also not well-structured. Why is this a problem with convexity rather than the score function?
   * Lines 362-367, same as above, MSE is not a consistent object for unequal scale, and therefore, it may not be a matter of the convexity that leads to bad results.
2. I think the evaluation of the method on the non-linear data could be even more sound if the author also considers simulations on synthetic data with equal noise variance as Bello et al. (2022).

### Questions
1. For the experiments on linear SEM with unknown variance, which score function is used? MSE or the log-likelihood? Is the SHD on the Markov equivalence class?
2. Does Table 7 describe the runtime? The caption seems to be incorrect.
3. It would be nice if the author could compare the choice of $s$ (and/or gradient magnitude) for the proposed method and DAGMA on an example to visualize the effectiveness of Algorithm 1 and the DAG constraint on dealing with gradient vanishing.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors provide a theoretical analysis of analytic matrix functions serving as acyclicity constraints in the context of differentiable DAG learning.
They first show that analytic functions are valid DAG constraints, that the gradients of analytic functions are easily computable, and that analytic functions do not suffer from vanishing gradients (in contrast to other acyclicity constraints). Next, the authors show that the family of analytic functions is closed under differentiation, addition, and multiplication, thus introducing an entire family of new acyclicity constraints. Additionally, a theoretical analysis of the non-convexity of said constraints is provided, indicating that there is a trade-off between high/informative gradients and non-convexity that has to be considered when designing acyclicity constraints. Finally, an experimental evaluation shows that differentiable DAG learners equipped with acyclicity constraints based on analytic functions perform better than other constraint functions.

### Strengths
- the paper provides an interesting and important contribution to analyzing acyclicity constraints for differentiable DAG learners formally
- the theoretical contributions (i.e., the propositions in 3 and 4) are mathematically sound, and the proofs are correct. Note that I rated soundness with "fair" due to major weaknesses in the experimental section. The theory section is strong.
- the work provides a theory-backed "out-of-the-shelf" approach to design acyclicity constraints using differentiation, addition or multiplication of analytic functions. This simplifies the process of constructing new acyclicity constraints.
- it is shown that the proposed family of acyclicity constraints does not suffer from vanishing gradients
- the experimental section shows that analytic acyclicity constraints indeed can lead to better performances in DAG learning

### Weaknesses
 - line 106-107: "However, these methods are known to perform poorly when applied to normalized data since they rely on scale information across variables for complete DAG recovery." This statement is a bit confusing since the findings in [1] and [2] (which generalized [1]) show that it is not the acyclicity constraint that leads to bad performance but the loss itself (MSE in this case). It would be more accurate to state that the performance degradation is linked to the inconsistency of the MSE loss when data is normalized, rather than attributing it to the acyclicity constraint directly.
- line 127-129: the claim that Eq. 4 converges if the spectral radius of $\mathbf{A}$ is smaller than $r$ is correct. However, it would be good to provide some intuition (and maybe proof in the appendix) since most propositions are based on that claim/assumption. The convergence of the power series is a crucial aspect of the proposed method, and a more detailed explanation of why this condition is sufficient for convergence would be beneficial for the reader.
- line 154-156: while I agree that in terms of computational efficiency, it is desirable to have acyclicity constraints whose gradient is representable by itself, the evaluation of these constraint functions can still be costly if not carefully chosen. It would be good if the authors could elaborate a bit more on that and provide an intuition why analytic functions are computationally efficient beyond the gradient computation. Specifically, the computational cost of evaluating the infinite sum in the analytic function needs to be addressed, as truncating this sum introduces approximation errors that need to be considered.
- Eq. 10: Could the authors provide a more detailed derivation of the constraints? It's easier to see where the constraints in Eq. 10 come from if Prop. 1 and 2 are actually applied to the functions in Eq. 9. A step-by-step derivation would greatly improve the clarity of this section.
- Eq. 11: shouldn't it rather be $\frac{\partial f^s_{\text{log}}(x)}{\partial x} = -s (s -x)^{-1} = -s \cdot f^s_{inv}$? This seems to be a minor error in the derivative calculation that needs to be corrected.
- line 223: the authors claim that $(\mathbf{I} - \mathbf{B} / s)^{-1}$ can be cached. However, $\mathbf{B}$ will change in each iteration and thus hast to be re-computed, right? The caching claim needs to be clarified, as it's not immediately obvious how this would work given the iterative nature of the optimization process.
- Prop. 5: Couldn't the fact that the gradient of the trace of $(\mathbf{I} - \mathbf{B} / s)^{-n}$ is smaller than that of $(\mathbf{I} - \mathbf{B} / s)^{-n-k}$ potentially lead to exploding, rather than vanishing gradients? A brief explanation on this would be appreciated. The relationship between the order of the constraint and the magnitude of the gradient needs further clarification to avoid potential misunderstandings about gradient behavior.
- Algorithms 1 and 2 are not properly discussed in the main text. Especially, it is not entirely comprehensible from the text what the parameters of the algorithms mean. The lack of detailed explanations for the algorithms makes it difficult to understand the practical implementation of the proposed method.
- the text in Sec. 4 and 5 reads a bit "rushed" and is not polished. The writing in these sections could be improved to enhance readability and clarity.
- I think the experiments miss the main message the authors try to convey: In Sec. 3 and 4 the authors provide a strong theoretical analysis of the acyclicity constraints. However, the experiments seem to be mostly based on the paragraph in line 356-367 where the authors briefly discuss the learning dynamics of differentiable DAG learners when the scale of the data is known/unknown which is not the main contribution of this paper. The authors only show that analytical DAG constraints yield better results on simulated data (except Tab 4 where results are not significant and standard deviation is missing). While this is an important result and demonstrates that the proposed family of acyclicity constraints positively affects learning on simulated data, it remains unclear from an empirical perspective if the initial goal of solving the vanishing gradient problem was achieved. To underline the paper's important theoretical contributions, the authors should revise their experiments and rather analyze the learning dynamics and gradient statistics over learning instead of focusing on evaluating the methods' accuracies with the new acyclicity constraints. Also, since the acyclicity constraint is not primarily affected by data scale, the focus of the experimental evaluation is questionable.

### Questions
- line 195-198: that's an interesting property but what is it actually good for? Because using the gradient/derivative of an analytic function essentially yields another analytic function with a shift by one in the polynomial degrees. As we only need a nilpotent matrix to ensure DAGness, this property may not necessarily yield a benefit? Could the authors please provide some more information on that?
-  paragraph in line 356-367: Since most of your experiments are built upon this paragraph, could the authors please provide more intuition on why the known/unknown variance has an influence on MSE. What about other losses like LL? Is this related to the findings of [2]?


# References
[1] Reisach et al. Beware of the simulated dag! causal discovery benchmarks may be easy to game. NeurIPS 2021.

[2] Seng et al. Learning Large DAGs is Harder Than You Think. ICLR 2024.

### Soundness
3

### Presentation
3

### Contribution
3
