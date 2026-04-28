# Bayesian Analysis of Combinatorial Gaussian Process Bandits

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 8, 5, 5

## Abstract
We consider the combinatorial volatile Gaussian process (GP) semi-bandit problem. Each round, an agent is provided a set of available base arms and must select a subset of them to maximize the long-term cumulative reward. We study the Bayesian setting and provide novel Bayesian cumulative regret bounds for three GP-based algorithms: GP-UCB, GP-BayesUCB and GP-TS. Our bounds extend previous results for GP-UCB and GP-TS to the \emph{infinite}, \emph{volatile} and \emph{combinatorial} setting, and to the best of our knowledge, we provide the first regret bound for GP-BayesUCB. Volatile arms encompass other widely considered bandit problems such as contextual bandits.
Furthermore, we employ our framework to address the challenging real-world problem of online energy-efficient navigation, where we demonstrate its effectiveness compared to the alternatives.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors derive Bayesian regret bounds for various algorithms applied to combinatorial volatile GP semi-bandit problems. Specifically, the authors derive regret bounds for 3 algorithms: GP-UCB, GP-BayesUCB, and GP-Thompson Sampling. In comparison to previous works, this is the first regret bound for GP-Bayes UCB, and in addition, extend the existing regret bounds for GP-UCB and GP-TS to infinite, volatile and combinatorial setting (which is also includes the popular contextual bandit setting).

The authors apply these algorithms to the problem of online energy-efficient navigation to demonstrate the performance of the various algorithms.

### Strengths
The main strengths of the paper is the theory. I do believe the GP semi-bandit problems considered in this paper are important, and having regret bounds for the algorithms discussed in this paper is also useful. 

Specifically, it is nice to see sub-linear regret bound for all three algorithms.

Furthermore, I also believe that the general techniques developed here may be useful to derive regret bounds for other bandit settings.

### Weaknesses
1. I think the paper lacks some clarity, and the exposition can improve significantly. For example, it requires recalling previous literature to properly understand the set-up in Section 2.1: Is A a finite set? 2^A is the set of a all subsets of A? What happens when A is infinite as in Section 3.2?  The paper should explicitly define the set A and its properties, especially when transitioning from finite to infinite settings. The current description is ambiguous and makes it difficult to follow the theoretical development.
2. Though the dependency on T is sub-linear, I am not sure how to view the dependency on K. Especially in the infinite case. Are there any lower bounds for these settings? It is hard to view how good or bad the bounds are with lack of comparisons. The paper needs to provide a more thorough discussion on the implications of the dependency on K, especially in the infinite setting. Without lower bounds or comparisons to other works, it is difficult to assess the quality of the derived bounds. The authors should also clarify if K refers to the number of base arms or the size of the selected combination.
3. Building on top of 2 above, I am curious to know if this is the best dependency on T you can get. I am used to seeing \sqrt{T} regret bounds for bandit algorithms -- is this not achievable in such settings? The paper should address why the standard \sqrt{T} regret bound is not achieved and discuss the potential limitations of the current approach. It would be beneficial to see a discussion on the tightness of the derived bounds and whether there are fundamental barriers to achieving better regret dependencies.
4. I thought that the experimental section was too artificial. If the motivation is to solve the problem in best possible way, there are probably better ways of solving the problem (for example using RL), than naively applying the semi-bandit learning algorithms. If the point is to show the performance of various algorithms, a simple example would suffice. In my opinion, the addition of these experiments does not add any additional value to the paper, and does not change the fact that the papers main (only) contributions are the theoretical bounds.

### Questions
Please respond to my above concerns.

In addition, I would request the authors to add theorems / propositions after Theorems 3.2 and 3.6, without any \gamma_t and \beta_t terms. Or more generally, with as few variables as possible.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the combinatorial volatile Gaussian process (GP) semi-bandit problem and provides the first Bayesian regret bounds for the GP-BayesUCB algorithm. In addition to this novel contribution, the authors extend their theoretical analysis to include Bayesian cumulative regret bounds for the GP-UCB and GP-TS algorithms, effectively addressing a notable research gap as highlighted in Table 1. To demonstrate the practical relevance of their framework, the authors apply their methods to a real-world problem: online energy-efficient navigation.

### Strengths
1.	Clear and Structured Presentation:
The paper is well-written, with clear explanations and illustrations of the research gaps. The novelty of this work is effectively communicated, making it accessible even to readers who may not be deeply familiar with the field.
2.	Solid Theoretical Contributions:
The authors provide rigorous theoretical analysis and establish new Bayesian regret bounds for multiple algorithms, including GP-BayesUCB, GP-UCB, and GP-TS. The paper addresses a significant gap in the literature by formalizing regret bounds for these settings. Full proofs are provided in the appendices, showcasing the depth of their analysis (though the correctness of these proofs was not verified).
3.	Practical Application:
The real-world application of their framework to online energy-efficient navigation is both relevant and interesting. It demonstrates the practical utility of their theoretical advancements and highlights the potential for real-world impact.

### Weaknesses
1.	Lack of Discussion on Theoretical Challenges:
While the paper provides new theoretical results, it does not clearly articulate the specific challenges encountered in deriving these results for GP-BayesUCB, GP-UCB, and GP-TS. A discussion on the theoretical hurdles and how they were addressed would provide valuable insight into the novelty and difficulty of these contributions. Specifically, the paper lacks a discussion on how the authors handled the non-standard error function within the GP-BayesUCB algorithm, which deviates from typical Gaussian process upper confidence bound derivations. Furthermore, the complexities of extending the analysis to a combinatorial semi-bandit setting, with its inherent partial feedback, are not sufficiently addressed. The paper should elaborate on the specific mathematical challenges in adapting existing techniques to this setting.
2.	Reproducibility Concerns:
No code is provided for the experiments. This absence raises concerns about the reproducibility of the empirical results. The paper should include code or a detailed description of the experimental setup to ensure the results can be independently verified.

### Questions
1.	Connection Between Theory and Empirical Results:
The online energy-efficient navigation application is a compelling demonstration of the framework’s practical utility. However, it would be helpful to clarify how the empirical results relate to the theoretical findings. Specifically, can the empirical results be used to verify or illustrate key observations from the theoretical analysis? If this connection is not direct, could you design controlled simulated experiments that more explicitly validate the theoretical regret bounds or insights?
2.	Extended Comparison in Table 1:
Including the regret rates alongside the regret bounds in Table 1 would greatly enhance its utility. This addition would allow readers to quickly compare the performance of different algorithms in terms of their theoretical guarantees. An extended table with this information would provide a clearer overview of the contributions and situate the work more firmly within the existing literature.
3.	Discussion of Theoretical Challenges:
As mentioned in the weaknesses, a dedicated section or paragraph discussing the theoretical challenges faced in deriving the regret bounds for GP-BayesUCB, GP-UCB, and GP-TS would add significant value. This discussion could cover aspects such as handling the volatility in combinatorial settings, managing the complexities introduced by semi-bandit feedback, or other technical hurdles specific to these algorithms.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper claims to present a novel Bayesian regret bounds for GP-UCB and GP-TS in combinatorial, volatile and infinite arms setting. Further they present the experimental results for a real world application of online energy efficient navigation.

### Strengths
The paper provides the bounds for the Bayesian regret for GP-BUCB, GP-UCB and GP-TS.

### Weaknesses
1. Though the work claims to present the bounds for volatile case but the proof for the bounds do not seem to consider it. As an example what would happen when the best arm is not present among the observed arms?
2. Not significant contribution, the paper mainly builds on the works of Russo & Roy 2014, Srinivas et al 2012 and Takeno et al 2023, where in to compute the Bayesian regret one only needs to compute the expectation over the high probability regret bounds given by the above works.
3. Lemma 3.1 the results are considered for different regimes of horizons for different cases of the ratio, why not choose the limits as 1 to T for the 3rd case, wouldn't that be a tighter bound?

### Questions
See the weakness section

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies Gaussian process bandits in the contextual volatile semi-bandit setting. The contribution of the paper is mainly theoretical as it provides novel Bayesian regret bounds for previously designed algorithms. In addition, there is an interesting application of their framework in online energy efficient navigation. This experimental application builds on top of the previously designed experiment of the same application in bandit papers.

### Strengths
The paper is building on top of other previously published frameworks, however, it is not a straightforward extension of the previous works. 

The experiments (application of their framework) in online energy-efficient navigation problem seem to have added some novelties and value to the paper. 

The paper is written in an excellent way. The explanations for the most important parts of the algorithms are clear. Also the similarities and differences (novelties) of their framework in comparison to the state-of-the-art is clarified properly.

### Weaknesses
No synthetic data experiment. Not even in the supplementary material. In my opinion, synthetic data experiments can significantly add to the development of intuitions about the framework. Also since you have much more control over the creation of the data, it can reveal interesting properties of the framework [in comparison with state-of-the-art].

Also, I could not find an experiment with the horizon more than 500 rounds. I am curious about the performance of the frameworks as the horizon goes well beyond T=500. I believe that proper comparison of bandit frameworks [most of the times] comes with running the experiments for long horizons.

I did not notice any discussion in the paper about possible extensions and future directions and further impacts of their research.

### Questions
Does the type of directed graph affect the applicability of the framework? For instance, how does the graph [being cyclic or acyclic] affect the performance of the framework? 

I did not notice any discussion in the paper about possible extensions and future directions and further impacts of their research, not even in the supplamentary section. Why? Can you please clarify?

### Soundness
3

### Presentation
4

### Contribution
2
