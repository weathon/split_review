# If Optimizing for general parameters in chemistry is useful, why is it hardly done?

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
General parameters are highly desirable in the natural sciences — e.g., reaction
conditions that enable high yields across a range of related transformations. This
has a significant practical impact since those general parameters can be transfered
to related tasks without the need for laborious and time-intensive re-optimization.
While Bayesian optimization (BO) is widely applied to find optimal parameter
sets for specific tasks, it has remained underused in experiment planning towards
such general optima. In this work, we consider the real-world problem of condi-
tion optimization for chemical reactions to study whether performing generality-
oriented BO can accelerate the identification of general optima, and whether these
optima also translate to unseen examples. This is achieved through a careful for-
mulation of the problem as an optimization over curried functions, as well as
systematic benchmarking of generality-oriented strategies for optimization tasks
on real-world experimental data. Empirically, we find that for generality-oriented
optimization, simple optimization strategies that decouple parameter and task se-
lection perform comparably to more complex ones, and that effective optimization
is merely determined by an effective exploration of both parameter and task space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the setting of Bayesian optimization where some variables can be manipulated as decision variables, and others must be optimized over in some aggregate measure, providing a measure of generality. This is motivated by the challenge of optimizing chemical reactions over general parameters (i.e., finding reaction conditions that perform well for multiple substrates), an area that is beneficial but underexplored in practical applications. The authors compare several Bayesian Optimization (BO) methods to identify reaction conditions that can be effectively applied across a range of simulated chemical reactions, giving a sense of the practical challenges involved in this task. The work emphasizes the difficulty of generality-oriented BO due to the partial observability of results (evaluations can only be performed on singletons or subsets of possible substrates), necessitating innovative BO algorithms.

### Strengths
- The problem formulation and motivation are presented well. The approach of using curried functions to define the setting of generality-oriented optimization adds some mathematical clarity and supports further research in this direction, though I am unsure how much of this is novel to this work. 
- The use of real-world datasets and extensive comparisons across various algorithms, including recently proposed algorithms, provide good insights into the current challenges in the area of generality-oriented BO and the effectiveness of currently available strategies.

### Weaknesses
My main concern with this paper is its suitability for ICLR. In terms of length, many of the details required to understand the paper are moved to the appendix, making the paper difficult to read. In terms of content, many of the details concern practical challenges related specifically to the application of chemical reaction engineering (is this method applicable in ML or other domains?). For example, how to modify the simulated chemistry benchmarks to better suit this exact domain problem setting. For both reasons, this paper is likely better suited as a full-length journal article in chemistry, chemical engineering, or data-driven engineering.

A related concern is that, while the domain-specific elements are interesting and discussed in detail, the ML elements are not, leaving many open questions (especially without the appendices, which reinforces the above point). For example, the authors find that randomizing the selection of elements within $w$ to sample at works well. This suggests that the surrogate model of $w$ used to select optimal elements is ineffective, or the prior distribution is wrong. The selection of how to build a statistical model over the unordered elements of should be discussed in detail so that the reader can understand the approach taken.

### Questions
-	Regarding the connection to multiobjective optimization, is the case considered here equivalent to scalarizing a multiobjective problem, where all objectives are given equal weights (thus producing the mean)? 
-	Similarly, does not the choice of $m<n$ elements of $w$ to sample effectively produce a multi-fidelity setting?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies Bayesian optimization (BO) for general parameters discovery in chemistry, especially formulating the problem as a generality-oriented optimization, where the authors aim to identify general reaction conditions that perform well across diverse substrates. They benchmark the recent algorithms and discuss the difficulty of applying BO for this scenario.

### Strengths
1. This work focuses on general parameters discovery in chemistry, which is a significant scientific problem. 
2. This work proposes a well-established benchmark for this problem.
3. The code implementation is well-structured and clear.

### Weaknesses
1.	Lack of discussion with related topics. The formulation of generality-oriented optimization is quite similar to the definition of stochastic optimization [1] and distributionally robust optimization, with the context variables (i.e., substrates in this paper) sampled from a distribution determined by the aggregation function $\Phi$, and the framework of generality-oriented BO aligns with the simulator setting of stochastic/distributionally robust BO [2, 3, 4, DRBO]. However, this work lacks a systematic discussion and an experimental comparison between generality-oriented BO and stochastic/distributionally robust BO.

2.	Weak experimental analysis and discussion. While the authors aim to investigate the challenges in optimizing general parameters, as indicated by the title, their conclusion attributes these difficulties primarily to the substrate sampling strategy. However, this conclusion appears to be drawn from a limited comparison between random acquisition and posterior variance acquisition of \textbf{w}\textsubscript{next} under a single fixed strategy of \textbf{x}\textsubscript{next}. A more comprehensive analysis would involve comparing various acquisition policies for \textbf{w}\textsubscript{next} across different effective strategies of \textbf{x}\textsubscript{next}. Such strategies could include UCB with varying $\beta$, or pure exploration for continuous/discrete/mixed-variable spaces, as demonstrated in Vizier Bandit [5]. To conclude, I will be glad if the authors could add a discussion on the impact between acquisition policies for both \textbf{w}\textsubscript{next} and \textbf{x}\textsubscript{next}.


3.	Limited insights into the design of BO algorithms. As an AI paper, it would be better to offer broader insights beyond introducing the problem. Unfortunately, the work is mainly an application of BO methods, making the algorithmic novelty somewhat limited.

4. The paper contains some minor language problems, including

- line 44, “efficiency. (Clayton et al. 2019; …).” → “efficiency (Clayton et al. 2019; …).”

- line 173, “thresholdBetinol et al. (2023)” → “threshold (Betinol et al. 2023)”

- line 265, “work in this field” → “works in this field”

- inconsistent tenses in Section 3 and Section 4, where Section 3.1 uses present tense while the remaining sections use past tense

- line 490, “RDKit: Open-source cheminformatics” → “Greg Landrum. RDKit: Open-source cheminformatics”

- inconsistent capitalization style of section headings. The paper uses title case only in Appendix A.1 and its subsections (A.1.1, A.1.2), while all other sections follow sentence case format

- line 850, “at time point $k$ $p(g_k(\mathbf{x}))$” → “at time point $k$, $p(g_k(\mathbf{x}))$”

- line 892, “SAA” lacks a citation

- line 1278, a citation of GPyTorch is needed

- line 1293, “Bandit Wang et al. (2024)” → “Bandit (Wang et al. 2024)”

- line 1403, “substrates for chosen for” → “substrates chosen for”

- line 1565, “, that” → “, which”, “(i.e. above)” → “(i.e., above)”

### Questions
1.	As in weakness addressed, can the author provide discussion or experimental comparison with stochastic/distributionally robust BO?

2.	In Figure 3, the efficiency of augmented search space is not so trivial, especially for the N.S-Acetal formation, and it will be better if the authors could show the improvement of Spearman correlation coefficient. 

3.	Since the authors have shown that the better transferability of the augmented search space, why not just provide the results on the augmented search space? What is the meaning of providing results on the original search space?

4.	In line 419, what is the full name and the nature of the metric GAP? E.g., its scale and is it better to maximize it?

5.  Is the pretrained random forest regressor a reasonable oracle? Except for MAE and MSE metric in Appendix A.2.2, metrics like Spearman correlation coefficient on the held-out test set should also be shown, as the random forest regressor for Superconductor task in Design-Bench [1].

I am more than happy to increase my score if the authors can address my questions.

[1] Trabucco et al. Design-Bench: Benchmarks for Data-Driven Offline Model-Based Optimization. ICML 2022.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Despite Bayesian optimization (BO) being a common method for identifying the best parameter sets for individual tasks, its application in planning experiments to achieve these universal optima is not as prevalent. The authors addresses the real-world challenge of optimizing chemical reaction conditions to assess if a focus on generality in BO can quicken the discovery of universally optimal conditions and if these optima are applicable to new, unseen scenarios. This assessment is conducted by meticulously framing the problem as an optimization of curried functions and by rigorously comparing generality-focused approaches against real-world experimental data. Their findings indicate that the optimization of general reaction conditions is influenced by the way substrates are sampled, with random sampling proving to be more effective than strategies that rely heavily on data.

### Strengths
* The paper is well written, and the method is well described.
* I greatly appreciate the author for providing a multitude of real chemical experiment scenarios and testing the algorithm's performance on them, which has given us considerable insight into the practical application of BO.

### Weaknesses
 * Although I appreciate the extensive work done by the authors, there is a significant issue with this article in Section 2, the problem formulation. In fact, problem (2) is not a new issue in the field of BO, depending on the form of $\phi(\cdot)$. For instance, when $\phi(\cdot)$ takes the form of Mean aggregation, Threshold aggregation, and MSE aggregation, such problems are referred to as Bayesian Optimization with Expensive Integrands[1,2]. When $\phi(\cdot)$ takes the form of Minimum Aggregation, these problems are known as Robust Bayesian optimization [3] (or minimax Bayesian Optimization). Therefore, the statements in section 2.2.2 are not representative, and a substantial revision may be needed for the Section 2.

* Although the authors have compared the BO method with those in the chemistry-related field, given that there are already many good methods in the BO field, these methods should also be evaluated on the chemical dataset. In fact, the conclusions of the article are thus questionable—whether the random selection performs better because it truly has good performance, or just because the comparative methods were not chosen correctly?

### Questions
I notice that many methods involving random selection tend to show a sudden surge in performance on the figures. What could be the cause of this situation?

### Soundness
3

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
This is an applications paper where the authors look at the problem of choosing conditions for running chemical reactions for different reactants (substrates).  This is viewed as an optimisation problem where we want to maximise the expected performance based on limited data.  The task is to choose which experiments to run in order to make good predictions.  The authors test a number of different strategies, and find a random greedy algorithm does as well if not better than more sophisticated methods.

### Strengths
The experiments set out seem to be comprehensive and well done.  I appreciate that this presents a "negative result".  It is refreshing for authors to report results where a surprisingly simple method beats more complicated approaches.

### Weaknesses
I question whether this work is of high interest to researchers interested in learning representation.  There is undoubtedly value and interest in this work, but it doesn't seem to match the ICLR audience.  There is very little on representation learning.  I slightly struggled to understand this paper.  Setting up the problem in terms of generality-oriented Bayesian Optimisation seems unnecessarily complicated.

There are a few sentences that did not make much sense to me.  E.g. the penultimate sentence on page 1 "Attempts to reduce..." is hard to understand.  Clearly this is a minor weakness that can be easily rectified.

### Questions
Is there are cleaner description of your problem as generality-oriented BO is hard to understand?
Likewise the use of currying functions makes your objectives obscure.  Are you not just trying to estimate the expected performance of some reaction conditions?

### Soundness
3

### Presentation
2

### Contribution
2
