# ParFam -- (Neural Guided) Symbolic Regression via Continuous Global Optimization

- Decision: Accept
- Scores: 8, 3, 6, 5

## Abstract
The problem of symbolic regression (SR) arises in many different applications, such as identifying physical laws or deriving mathematical equations describing the behavior of financial markets from given data. 
    Various methods exist to address the problem of SR, often based on genetic programming. However, these methods are usually complicated and involve various hyperparameters. 
    In this paper, we present our new approach \mbox{\emph{ParFam}} that utilizes parametric families of suitable symbolic functions to translate the discrete symbolic regression problem into a continuous one, resulting in a more straightforward setup compared to current state-of-the-art methods. 
    In combination with a global optimizer, this approach results in a highly effective method to tackle the problem of SR. 
    We theoretically analyze the expressivity of ParFam and demonstrate its performance with extensive numerical experiments based on the common SR benchmark suit SRBench, showing that we achieve state-of-the-art results. 
    Moreover, we present an extension incorporating a pre-trained transformer network (\emph{DL-ParFam}) to guide ParFam, accelerating the optimization process by up to two magnitudes.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a SR method that fixes a rational function structure and optimizes it using MC-based optimization methods. They also present a version of this technique that uses pre-trained transformers as a starting point. Results are presented on many SR benchmark problems and include an analysis of expressivity.

### Strengths
The paper is well written and to my knowledge a fairly novel approach to SR that is well-contextualized. The authors have made very, very extensive experimental comparisons, although many of these are sent to the appendix. The authors also do a good job of providing a slightly deeper theoretical justification for their work than in typical SR papers which I enjoyed reading. I think the paper makes a good contribution to the field in showing another avenue for SR that revisits established global optimizers with a unique functional structure that can still find ground truth solutions with good fidelity.

### Weaknesses
The main weakness of the Feynman and Strogatz dataset comparisons is that many of the equation forms are very simple (especially Feynman). So, one way to do well on them is to restrict the complexity of models during optimization (or invent a method that happens to search over simple forms). That's why it's important to also consider benchmarks on real-world data. The authors are aware of this, but focus the main body of their text on these synthetic datasets and send real-world results to the appendix. I would be in favor of the real-world dataset comparisons from SRBench being more of a main result, especially if they are given an extra page in the revisions.

I would have also liked to see a stronger connection made between the expressive restrictions of their methods (e.g., inability to model deep unary functions) and the distribution of those types of expressions contained in those benchmarks. For instance, a quantitative analysis of the prevalence of deep unary functions in the Feynman and Strogatz datasets would strengthen the claim that the proposed method's limitations are not a significant drawback in these specific cases.

- I would have liked to see more motivation for the chosen representation of equations as rational functions earlier on. Why are shallow rational functions a good _hypothetical_ choice for representing any possible expression tree, before introducing your approach to measuring expressivity? A brief discussion on the approximation capabilities of rational functions compared to other functional forms would be beneficial.

- Typically, theorems are self-contained. So in Theorem 2.1, it would be more clear to define $c$, $x$, $l$, etc., rather than having to find them throughout the text. This would improve the readability and accessibility of the theorem.

- I found S 2.2 on the expressivity of ParFarm interesting, but I had trouble extracting an intuition for how expressivity scales from the description and from Table 1. It looks like $x$ is being reused for two different variables, and it also appears that the authors are only considering expressivity for $\u2060l = 1$⁠ i.e., equations with a single function. I would have liked to know how expressivity scales as functions grow in complexity ($l$) which seems equally or more important than scaling by the number of leaves ($n$) and unary functions ($k$). Providing a concrete example of how to calculate the coverage ratio for a given $l$, $n$, and $k$ using the data in Table 1 would significantly improve clarity.

- DL-ParFam seems to be extremely sensitive to small amounts of noise in the SRBench ground truth problems. I would have liked to see this mentioned in the results/discussion. A brief explanation of why this sensitivity occurs, possibly related to the optimization landscape or the model's inductive biases, would be valuable.

- misc
  - awkward phrasing: "to avoid the regularization to be circumvented"

> Typical formulas from the Feynman dataset [1], for instance, have a complexity of around 10.

What does this mean? Does it refer to the average depth of the expression tree, the number of nodes, or another metric? Clarifying the complexity metric used here would be helpful.

Table 1: It wasn't clear to me why ParFam's ability to cover possible expressions would increase as $n$ increased. Is it just because $n$ artificially inflates the proportion of copies of identical function forms with swapped leaves in $d$? Or something else? A more detailed explanation of the relationship between $n$, the number of binary operators, and the coverage ratio would enhance the understanding of this phenomenon.

### Questions
> Typical formulas from the Feynman dataset Udrescu & Tegmark (2020), for instance, have a complexity of around 10.

What does this mean?

Table 1: It wasn't clear to me why parfarm's ability to cover possible expressions would increase as $n$ increased. Is it just because $n$ artificially inflates the proportion of copies of identical function forms with swapped leaves in $d$? Or something else?

### Soundness
4

### Presentation
3

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
In this paper, we propose a symbolic regression algorithm ParFam, which treats symbolic regression problem as a global optimization problem. Compared with the traditional methods that treat symbolic regression problem as a combinatorial optimization problem, ParFAM improves the search efficiency and has the potential to solve high-dimensional problems

### Strengths
This paper proposes DL-ParFam, which uses a pre-trained model to predict ParFam's parameters, effectively improving its training efficiency. The authors claim that the training speed is 100 times faster. But the thinking of DL - ParFam and this article is a bit like (https://doi.org/10.48550/arXiv.2309.13705),

### Weaknesses
##### Weaknesses

1. Mentioned in the article with global optimization to solve the problem of symbolic regression is more efficient, but this is not the first to use global optimization algorithm to solve the problem of symbolic regression algorithm, for example, EQL (https://doi.org/10.1109/TNNLS.2020.3017010), MetaSymNet (https://doi.org/10.48550/arXiv.2311.07326). And this paper does not compare with these two algorithms. Please analyze the advantages of ParFam over the above two methods.

2. At the beginning of the **introduction**, the paper mentioned that the simplicity of the expression is very important, but the paper did not evaluate the expression complexity of the algorithm.
3. Why did the author only add the noise level of 0.01 in the anti-noise experiment? However, in many other symbolic regression algorithms, the anti-noise experiment is more adequate. I think the noise level should be increased to the order of 0.1 to better test the anti-noise ability of ParFam.

### Questions
##### Questions

1. It is not clear to me how the training data for the DL-ParFam is collected. Please describe it in more detail in the article and provide more details.
2. To reorganize what is the main innovation of this paper, I don't think using the global optimization problem as a knot symbolic regression problem is an innovation of this paper.
3. The article says that its ability to deal with high-dimensional symbolic regression is stronger than the existing algorithms, so does the article test and compare the ability of each algorithm to deal with high-dimensional symbolic regression problems?
4. Why does DL-ParFam not compare inference time with pre-trained symbolic regression methods represented by **Neural Symbolic Regression that Scales** and **End-to-end Symbolic Regression with Transformers**?

### Soundness
3

### Presentation
2

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
This paper presents ParFam, a novel approach to symbolic regression that reformulates the discrete optimization problem into a continuous one using parametric families of functions. The DL-ParFam extension introduces a neural-guided approach that incorporates a pre-trained Set Transformer to accelerate the optimization process. The method is evaluated on standard symbolic regression benchmarks and shows competitive performance.

### Strengths
- The authors provide a thorough theoretical analysis of ParFam's expressivity, demonstrating that it can still represent a substantial proportion of functions of a given complexity. 
- Results on standard benchmark datasets demonstrate ParFam's strong performance in terms of symbolic recovery rate and accuracy.

### Weaknesses
 - The pre-training phase for DL-ParFam is computationally expensive, though it only needs to be done once.
- In the figure 4, the label "Symbolic Solution Rate" may be incorrect and should be "Symbolic Recovery Rate".
- As shown in Figure 4, symbolic solution rate drops significantly when noise is introduced. This suggests that the methods are sensitive to even small levels of noise, which could limit their robustness in real-world scenarios where data is often noisy.
- The method still faces challenges when dealing with high-dimensional problems (more than 10 variables). As the number of parameters increases exponentially with the number of variables, optimization becomes more computationally intensive.
- The performance of the method is highly dependent on model parameter choices, such as the degree of polynomials and basis functions, requiring some prior knowledge or extensive experimentation to determine the optimal parameters.

### Questions
- For DL-ParFam, how robust is the pre-trained model to out-of-distribution data? Are there certain types of functions where it consistently fails to provide useful guidance?
- Could the authors elaborate on how ParFam's performance scales with the number of variables?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose a novel architecture, ParFam, to solve symbolic regression through continuous optimization. The authors also introduce the use of a neural network to predict optimal hyperparameters for ParFam.

### Strengths
The strength of this paper is that the proposed ParFam shows high accuracy on the Feynman and Strogatz datasets from SRBench. The idea of using a neural network to predict optimal hyperparameters is interesting.

### Weaknesses
The weakness of ParFam is that the advantage of ParFam over EQL and some recent EQL variants is not clearly demonstrated. The authors claim that EQL uses linear layers, while ParFam uses rational layers. However, EQL is not limited to using unary functions in basis functions, and if a division function were included in EQL, it would closely resemble ParFam.

Recent works have incorporated neural architecture search with EQL [2] [3]. These works appear to be a superset of the proposed method. The architecture proposed here is manually designed within the neural architecture search space. It is unclear what advantage ParFam has over these variants of EQL.

The idea of predicting hyperparameters using a transformer is interesting. In ParFam, the default method for hyperparameter optimization is grid search. However, Bayesian optimization is a more common approach. Please provide a comparison of the speedup achieved by hyperparameter optimization using a pre-trained transformer versus Bayesian optimization.

The training time of ParFam on the black-box datasets from SRBench is not shown. Please provide this information.

For the limitation related to high-dimensional data, it is claimed that "the number of parameters grows exponentially with the number of variables." However, from Figure 1, it is unclear why the number of parameters would grow exponentially with the number of variables. Please clarify.

### Questions
Here are some questions that need to be addressed:
1. The idea of using a division operator in EQL was proposed in ICML 2018 [1]. Please provide a comparison between ParFam and EQL with division operators to ensure a fair comparison.
2. Recent works have incorporated neural architecture search with EQL [2] [3]. These works appear to be a superset of the proposed method. The architecture proposed here is manually designed within the neural architecture search space. It is unclear what advantage ParFam has over these variants of EQL.
3. The idea of predicting hyperparameters using a transformer is interesting. In ParFam, the default method for hyperparameter optimization is grid search. However, Bayesian optimization is a more common approach. Please provide a comparison of the speedup achieved by hyperparameter optimization using a pre-trained transformer versus Bayesian optimization.
4. The training time of ParFam on the black-box datasets from SRBench is not shown. Please provide this information.
5. For the limitation related to high-dimensional data, it is claimed that "the number of parameters grows exponentially with the number of variables." However, from Figure 1, it is unclear why the number of parameters would grow exponentially with the number of variables. Please clarify.

References:

[1]. Sahoo, Subham, Christoph Lampert, and Georg Martius. "Learning equations for extrapolation and control." International Conference on Machine Learning. PMLR, 2018.

[2]. Dong, Junlan, et al. "Evolving Equation Learner for Symbolic Regression." IEEE Transactions on Evolutionary Computation (2024).

[3]. Li, Wenqiang, et al. "A Neural-Guided Dynamic Symbolic Network for Exploring Mathematical Expressions from Data." Forty-first International Conference on Machine Learning.

### Soundness
3

### Presentation
3

### Contribution
2
