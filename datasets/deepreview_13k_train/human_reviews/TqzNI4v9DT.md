# GeoBench: A new benchmark on Symbolic Regression with Geometric Expressions

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Symbolic regression (SR) is a powerful technique for deriving mathematical expressions from data. With the emergence of numerous SR methods, SRBench made a significant contribution by providing a standardized testing platform that includes 130 SR datasets and evaluates 14 SR methods. However, the methods included in SRBench are outdated, and the dataset does not feature results from more recent approaches such as TPSR. Additionally, the metrics used in SRBench do not adequately capture the full capabilities of symbolic regression methods, and the benchmark data has scientific problems. Although Matsubara et al. (2022) address some of these issues,
their approach remains incomplete.  In response, we propose a new benchmark consisting of 71 expressions derived from geometric contexts, categorized into three difficulty levels: easy, medium, and hard. We evaluate 20 SR methods on these expressions, focusing exclusively on the symbolic regression capability of each model, assessed through recovery rates across the different levels and overall. We provide a detailed methodology for reproducing the experiments and include results for newly developed SR methods within this updated benchmark. The results demonstrate significant variation in symbolic regression ability across models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper contributes a benchmark of symbolic regression methods using synthetic problems derived from 2D and 3d geometry. It includes a description of these problems, a review of other benchmarking work in SR, and a benchmark of several SR methods on the proposed benchmark.

### Strengths
The paper is easy to follow and covers a lot of existing literature. The description of the problems is clear and for the most part the benchmarked methods cover a wide swatch of proposed algorithms. It may be of interest to those looking to benchmark new symbolic regression techniques.

### Weaknesses
While the paper has many strengths, one of the main weaknesses is that it does not make it clear to the reader why this set of synthetic benchmark problems is a good assessment of the efficacy of these methods in any real-world applications. The benchmark datasets are noiseless geometric functions, which do represent some aspect of the real-world, but this reviewer is left wondering how a real-world problem in which SR would be applied would relate to these problems. The authors do describe the significance of the equations mathematically, but do not offer a compelling example of why one would expect the best algorithms from this benchmark to perform well in some significant real-world version of these problems.

As an example, with other benchmarks like Feynman and Strogatz, we can imagine a scientist collecting the observations that comprise the dataset from real-world phenomena and using SR to discover the underlying physical relation governing the system. Even these problems suffer from a lack of realism which is why noise is synthetically added in prior benchmarks (SRBench) or data is collected from physical examplar systems (Schmidt & Lipson 2009). But what is the equivalent real-world setting for these geometry problems? And, how well can we expect this benchmark's assessment of methods to transfer to those tasks, especially when the data is noiseless?

Below are some more specific critiques: 

> SR offers greater interpretability and superior generalization, avoiding the complexity often
associated with opaque models.

Two strong claims made without justification - I suggest softening the language or referencing examples. 

L046-065: I found this to be a confusing and somewhat apocryphal description of SR history. One might argue that polynomial fitting and/or even classification and regression trees are all versions of symbolic regression, but the authors are stretching in refering to those methods as the origin of SR. SR as it is thought of today (structural and parametric equation fitting to data) is typically dated to Koza's 1992 book Genetic Programming. The paragraph on constant optimization is also not representative of this history; constant optimization for expression trees didn't begin with a "linear regression framework", they started as "ephemeral random constants" (ERCs), i.e. additional terminals made of random values that were "tuned" via expression tree manipulation. The integration of constant optimization into expression tree SR is often attributed to Topchy and Punch 2003. The authors also seem to describe stochastic hill climbing of constants which made popular in Lipson's lab's papers (maybe first with Bongard & Lipson PNAS 2005 or Zykov, Bongard & Lipson IEEE 2005) but they don't describe it clearly or cite it appropriately. 

In their discussion of benchmarking history, the authors should also mention McDermott et al's 2012 paper, GP needs better benchmarks (http://dl.acm.org/citation.cfm?id=2330273), which was a bellwether moment for many in the SR community, who were often benchmarking on overly simplistic datasets. It was a key moment in this history as it incorporated community feedback and black-listed several overly simplistic SR benchmarks problems like the quartic polynomial and many of the Nguyen problems. Incidentally, as the field of SR has crossed to new communities, this step forward is often lost, and results in recent papers benchmarking on datasets that were deemed too easy many years prior. 

The introduction description of SRBench only describes half of the datasets in the benchmark paper, and neglects to mention (importantly) that half of SRBench was dedicated to benchmarking on real-world datasets. These are crucial for benchmarking since otherwise SR methods are being compared only on synthetic data which comes with a load of limitations. 

> Furthermore, the benchmark includes some scientifically unrealistic assumptions, such as treating the gravitational constant as a
variable, and has been criticized for its oversimplified sampling process and inappropriate formulas
(Matsubara et al., 2022).

The gravitational constant treatment is from the Feynman equations, and not specific to SRBench. Matsuraba et al's critique applied to the synthetic datasets in Feynman and ODE Strogatz, but the authors here attribute it to SRBench.

> DEAP (d’Ascoli et al., 2022)

This is the wrong reference; d'Ascoli et al 2022 is not about DEAP. 

Furthermore, it is puzzling that the authors benchmark against DEAP and gplearn, which are both super simple and traditional GP-based SR approaches (they date from 2012 and 2016 but implement the algorithm as it was in the 90s), and then against PySR which is more recent. Why not pick other more recent GP-based SR method that have performed well in other benchmarking works, e.g. Operon (2020) etc?

Figure 4 should label the subplots as easy, medium, hard. If space allows it would be nice for this figure to be in the main text.

### Questions
Please see above for questions

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper attempts to refine the existing Symbolic Regression (SR) benchmark, SRBench. The paper does this by introducing equation recovery datasets based on geometry and evaluating 20 different SR algorithms on these datasets.

### Strengths
The organization of the paper is clear.

### Weaknesses
This paper attempts to refine the existing Symbolic Regression (SR) benchmark, SRBench. The paper does this by introducing equation recovery datasets based on geometry and evaluating 20 different SR algorithms on these datasets.

This paper positions itself as one that addresses the weaknesses of SRBench [1] and SRSD [2]. However, the new datasets introduced lack important characteristics as elaborated below:

i). Lack of real-world datasets, which is important for benchmarking SR algorithms. SR is an important explainable machine learning method in which its performance on real-world datasets, which may not have an underlying ground truth equation, is important. The benchmark proposed which the paper claims to be “a refined version of the SRBench dataset”, seems to be a step backwards when compared to SRBench’s real-world datasets.

ii). No results on noise added to datasets, in contrast to existing benchmarks available such as SRBench and SRSD. SRBench even has varying noise levels as acknowledged in the paper itself.

Lack of R2 score, with a focus on only exact recovery rate, which again is a step backward from existing SR benchmarks. Both metrics are important because in the context of using SR for machine learning, the use-case may not always have an underlying ground-truth equation, so R2 score is an important metric that complements recovery rate.

Novelty of the paper is low, especially in comparison to [2], which does similar benchmarking on Physics equations. [2] also introduced the categories of easy, medium and hard equations. In the reviewer’s opinion, changing the domain from Physics to Geometry, while not introducing anything substantially new has low novelty.

Lack of strong justification for why a new dataset is required. The paper does not give a comparison of the conclusions drawn from the new datasets and the conclusions drawn from SRBench and SRSD. If there are similarities in the conclusions, then why is the new dataset required? If there are differences in the conclusions, then the paper should discuss why that is so. Currently, the paper does not even compare against the conclusions that SRBench and SRSD provide.

### Questions
How does this benchmark help SR researchers better evaluate SR algorithms compared to SRBench and SRSD? A comparison of the conclusions drawn from the new datasets and the conclusions drawn from SRBench and SRSD would make the paper more meaningful.

The error referred to in the paper is not clear. This is especially important given that fixed thresholds for this error is given in Algorithm 1. Does the paper use normalized error (e.g., R2 score, normalized MSE) or not (e.g., MSE)?

Would simply updating the set of SR algorithms evaluated for SRBench and SRSD be sufficient to address all the issues that this paper attempts to address?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new benchmark for symbolic regression (SR) based on 71 geometric expressions and 20 SR methods. The chosen expressions are used to describe properties of 2D and 3D geometric figures, for instance, the area of a triangle given the lengths of its three sides. These expressions are supposed to be meaningful for real-life applications and complement the current SR datasets. Moreover, the authors categorize the expressions into three difficulty levels.

### Strengths
- The problem addressed by the authors - designing a new benchmark for SR - is important.
- The authors provide a good overview of currently used SR methods and benchmarks, discuss their advantages and disadvantages.
- The proposed benchmark is extensive. It includes 71 equations as well as many contemporary SR methods, including recent ones.
- Geometric equations have not been extensively used previously for evaluating SR methods.

### Weaknesses
### Real-world applicability
I am not convinced that geometric expressions are appropriate for evaluating symbolic regression. Authors criticize other benchmarks for "lacking real-world applicability" (lines 80-81) and claim that their equations are "meaningful in real-world applications" (lines 103-104). However, I do not think people are going to use symbolic regression to discover simple mathematical expressions that are either known or can be derived in a few steps. I suspect SR to be much more useful when applied to real datasets to uncover *unknown* relationships. However, I doubt the proposed equations are representative of equations describing the real world, because *they lack constants*. Only several equations proposed contain constants and all of them are either small integers or $\pi$. However, in reality, we may need many different constants at least to take care of non-matching units. It seems unlikely that $x_1 x_2 \sin(x_3)$ (rectangle-6) fits the data well. A good fit is more likely to look like $(3.3 x_1 + 0.5)(5 x_2)\sin(1.2 + 13.1 x_3)$.

From what I understand, the dataset also does not contain any noise, which is quite unrealistic. 

In short, why should I evaluate a method on datasets that look very different from the ones I will apply it to? 

### Difficulty levels
The definitions of different difficulty levels seem a bit arbitrary. I understand that "easy" equations are mainly polynomials. But what is the defining feature of "medium" equations? They are supposed to involve "non-linear terms", but higher-order polynomials are already non-linear. "Hard" equations are defined as having a "longer and deeper mathematical structure". But this is very arbitrary. For each category, it is stated how much time is needed to find them but it is not stated using which algorithm. I imagine this may vary a lot for different methods. I do not understand why "vector3d-3" is classified as "medium" whereas "vector3d-4" is classified as "easy" and they are both just polynomials. Moreover, "sphere-4" is classified as "easy" even though it is not a polynomial.

### Algorithm 1
I would like to understand the overall intention behind this algorithm. What was the goal? When would you say two expressions are the same?

### Clarifications needed
- line 71: What is a "non-prime function"?
- line 72: What are "more fundamental expressions"?
- lines 108-109: What does "extended period" mean here?
- line 316: What is a "normal model" compared to "machine learning model"?
- line 443: KAN's output is not a symbolic expression by default. How is the expression extracted from the model?
- line 992: What does "in most models" mean here? Why would it be different for different models? The token set impacts the performance.
- SINDy is used to discover ODEs, how do you adapt it to static symbolic regression?
- How do you make sure the results are comparable in between methods like gplearn and pysr where the population size, the number of generations, or the number of iterations may have a big impact on the performance?

### Possible errors
-  lines 85-86: Although Feynman Symbolic Regression Database contains 120 equations, I think only 100 of them are from Feynman's lectures. The rest are from different sources.
- line 409: EQL has been proposed by Martius & Lampert (2017)

### Minor
- line 81: why is "log" bold?

### Questions
1. Why is the performance of an SR method at discovering these geometric equations significant? It is unlikely my dataset will be governed by such clear and nice equations that do not contain any constants or noise.
2. How are the difficulty levels defined exactly?
3. What was the overall goal of Algorithm 1? When would you say two expressions are the same?

In addition, please answer my questions in Weaknesses#Clarifications needed.

### Soundness
1

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
4

### Summary
This paper presents a new benchmark for symbolic regression, constructing 71 datasets on which the SR methods are tested. These datasets focus on 2D and 3D geometric problems and are categorized into three difficulty levels, in which recovery rate is used as a metric to evaluate the SR models.

### Strengths
The proposed benchmark integrates a variety of the newest SR methods as baselines, allowing the comprehensive comparison of their recovery performance for the following work.
The authors construct new datasets based on 2D and 3D geometric problems, complementing existing physical symbolic regression datasets.
Overall, the presentation of the paper is clear.

### Weaknesses
The paper lacks a description of the advantages of the proposed geometric datasets over the existing datasets like the feynman dataset in evaluating SR methods, in which I think the proposed geometric datasets should be one of the main contributions. 
The paper uses only recovery rate as the evaluation metric, missing assessments of other important factors, such as runtime and the robustness to noise for the SR methods. The paper also does not sufficiently address the potential impact of varying input data sizes on the performance of different SR methods, especially given the exponential growth of the search space with increasing dimensionality. Specifically, it is unclear if the fixed dataset size of 500 is adequate for all problem complexities, and how this might affect the fairness of the benchmark, particularly for the 'hard' category problems. Furthermore, the justification for the specific runtime constraints (1 hour, 5 hours, and 24 hours) for different difficulty levels is not provided, raising questions about their appropriateness and the potential for bias in the evaluation.

### Questions
From the hyperparameter settings, it seems the runtime of the presented methods may appear to vary significantly. Should runtime comparisons be included to better promote fairness, especially when different types of SR models are involved? For instance, in some algorithms, like gplearn, there are only 20 generations, which looks far away from the runtime constraints. The presentation of the runtime can also promote fairness for the comparisons of the follwing work, avoiding the simple trade-off of increased time costs for improved recovery performance.
Since the search space grows exponentially with the increase in input dimension, is the same 500 dataset size for each geometric problem sufficient for SR models to recover the geometric equations with high input dimensions, particularly for those classified as hard?
It is not exactly clear to me how the runtime constraints of 1 hour, 5 hours, and 24 hours are derived for different difficulty levels.
Given that the purpose of the datasets is to provide a comprehensive evaluation of symbolic regression models, it would be beneficial to strengthen the description on how the proposed geometric problem-based dataset offers unique advantages over the existing datasets like the Feynman datasets in terms of model evaluation.

### Soundness
2

### Presentation
2

### Contribution
2
