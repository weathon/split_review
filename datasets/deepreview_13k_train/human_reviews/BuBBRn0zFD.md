# Automated Discovery of Pairwise Interactions from Unstructured Data

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Pairwise interactions between perturbations to a system can provide evidence for the causal dependencies of the underlying underlying mechanisms of a system. When observations are low dimensional, hand crafted measurements, detecting interactions amounts to simple statistical tests, but it is not obvious how to detect interactions between perturbations affecting latent variables. %
We derive two interaction tests that are based on pairwise interventions, and show how these tests can be integrated into an active learning pipeline to efficiently discover pairwise interactions between perturbations.
We illustrate the value of these tests in the context of biology, where
pairwise perturbation experiments are frequently used to reveal interactions
that are not observable from any single perturbation. 
Our tests can be run on unstructured data, such as
the pixels in an image, which enables a more general notion of interaction than
typical cell viability experiments, and can be run on cheaper experimental assays. 
We validate on several synthetic and real biological experiments that our tests are able to identify interacting pairs effectively. 
We evaluate our approach on a real biological experiment where we knocked out
50 pairs of genes and measured the effect with microscopy images. We show that
we are able to recover significantly more known biological interactions than
random search and standard active learning baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel active learning method to discover pairs of highly correlated variables. Concretely, we imagine that an experimentalist has access to an observations space $\mathcal{X}$, which change as a function of perturbations. Crucially, some pairs of perturbations $\delta_i, \delta_j$ jointly operate ($\delta_{ij}$) differently on $\mathcal{X}$ relative to their marginal individual effects. The key idea of this paper is to estimate three densities — $p(x|\delta_i), p(x|\delta_j), p(x|\delta_{ij})$ — which capture the distribution of $x$ based on marginal and joint perturbations and compare them to $p(x|\delta_0)$, the world in which no perturbations are applied.

The authors formulate their active matrix completion problem in a statistical hypothesis testing framework. In particular, at each step, they estimate a posterior over $\mathbf{R}$, a matrix of test statistics for all pairs of perturbations, and greedily selects a batch of experiments to run in the next step.

The authors apply this framework to CRISPR knockouts on pairs of 50 genes. Their dataset includes observations for all pairs in this 50 gene set, so the authors simulate an active experimental design by assuming the gene pair perturbations observations are masked and then simulating matrix completion by progressively revealing observations. Their method, which they term IDS, quickly discovers top gene pairs relative to standard baselines, and minimizes natural errors like regret.

### Strengths
This paper is well-written and proposes an interesting method for active experimental design. Estimating the joint density and comparing to the marginal density is an interesting idea, both for the disjointedness analysis and for the separability analysis. 

Although prior work (e.g., GEARS) has formulated CRISPR pair perturbation response prediction as a matrix completion problem, the active learning formulation seems novel, especially in dealing with imaging modalities (as opposed to RNAseq). The authors additionally spell out their assumptions — such as a set of latent variables $Z$ which capture all the information about perturbations — clearly. Their statistical testing framework is clear and well-motivated.

The authors additionally compare to plenty of baselines on their experiments. Although they only perform experiments on one real-world dataset, experimentation in this domain is expensive, so this is a natural choice and should not be seen as a limitation of their work.

 The appendix thoroughly explains the architecture and the methodological choices.

### Weaknesses
The use of a statistical test for matrix completion is a little poorly motivated. In particular, given an n x n matrix completion problem, at least one pair is likely to have a large test statistic. Given this is an active learning problem, multiple hypothesis testing is not as core of a concern, but I'd like the authors to discuss in their rebuttal what a "null" set of interaction pairs might look like. Concretely, suppose that in a module of 50 genes (so 1225 gene pairs) only 5 gene pairs interact with each other. Can this method be used to decide a "stopping" criterion for experimentation — i.e. would you be able to note that the posterior on the test statistics obey the null distribution once those 5 gene pairs have been found. Could you:
1. Describe the null distribution of test statistics in this framework
2. Discuss how this method could be used to decide a stopping criterion


Second, I think the authors did not explain why one would use imaging data for this matrix completion problem, instead of the more structured RNAseq data. Could you please justify why RNAseq data isn't used instead of imaging data?

Third, I did not get a sense of how often the joint distribution differs from the product of the marginals in this setting. There is some prior work that very few perturbations actually obey this relation, e.g. https://www.biorxiv.org/content/10.1101/2024.09.16.613342v1.full.pdf. How often is this method necessary, and why can't we just take experiment on the pairs $\delta_{ij}$ for which $\delta_i, $\delta_j$ are marginally most different from $\delta_0$. Could you provide quantitative analysis on how often joint distributions significantly differ from products of marginals in this dataset?

### Questions
Q1) See weaknesses section on detecting that all relevant gene pairs have been found

Q2) How many gene pairs usually have non-linear interactions? Or interactions that are significantly different from the raw pair?

Q3) Please include a baseline in which we reveal $\delta_ij$ on the pair $i,j$ for which $\delta_i, $\delta_j$ are marginally most different from $\delta_0$, perhaps taking the sum of the log density ratios.

Q4) How many samples are required for Appendix B.1 to become a faithful estimator of the densities? What happens if our densities are very far off?

### Soundness
3

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
5

### Summary
This paper proposes a new method for exploring the structure of a black-box system of interest by introducing perturbations, specifically focusing on identifying "interacting pairs"—pairs of perturbations that yield results significantly different from the effects of each perturbation applied individually. The paper proposes two methods to examine whether given pairs of perturbations exhibit a non-trivial "interaction effect" in this sense. The first method is a "separability" test, which checks if the effects of a pair of perturbations provide information beyond that obtained from each perturbation alone. The second method is a "disjointedness" test, which quantifies whether each perturbation in the pair influences distinct subsets of the outcome space. The separability test uses a criterion based on KL divergence, while the disjointedness test uses an MMD-based two-sample test for identity. Additionally, they treat the task of calculating each test statistic for all pairs (i, j) as a matrix completion problem and apply an active learning-based sequential experimental design using ADS (Xu et al., 2022) to identify pairs (i, j) with potentially having larger test-statistics values. Experiments demonstrate the superiority of the proposed method on benchmark synthetic data that meets the study's assumptions, and they conduct a synthetic lethality test to determine if two gene knockouts result in cell lethality, empirically confirming the method’s effectiveness in real biological systems.

### Strengths
- The paper addresses the problem of identifying pairwise interactions, specifically highlighting cases where the effect of two perturbations, such as cell lethality from double gene knockout, is entirely different from the effects of each perturbation alone. In the experiments, gene knockout was actually performed to validate effectiveness.
- The two proposed tests are technically intriguing. Each test is well-organized with necessary assumptions and effectively leverages existing theories, incorporating reasonable methods such as MMD-based two-sample tests (Gretton, 2012) and ASD (Xu et al., 2022) to construct a effective procedure.
- Despite potentially abstract topic of identifying "interaction effects", the Introduction clearly explains the ideas and intentions. The discussion is grounded with examples, such as validation on synthetic data and actual biological applications, making the logic easy to follow.

### Weaknesses
 - The two proposed interaction tests are not compared with any standard methods. The problem in question is not new; it has a long history in statistics as the "interaction effect," where the combination of two or more factors produces an effect greater (or less) than the sum of their individual effects [1][2]. Traditional applied statistical methods (likelihood-ratio tests, two-way ANOVA, etc) have also been used for identifying synthetic lethality [3], so a comparative analysis and discussion of differences with conventional methods are necessary. The paper only includes internal comparisons among variations of the proposed method, offering limited basis for objectively assessing its effectiveness against previous methods.
   - [1] Cox, D. R. (1984). Interaction. International Statistical Review / Revue Internationale de Statistique, 52(1), 1–24. https://doi.org/10.2307/1403235
   - [2] Amy Berrington de González, & Cox, D. R. (2007). Interpretation of Interaction: A Review. The Annals of Applied Statistics, 1(2), 371–385. http://www.jstor.org/stable/4537441 
   - [3] Akimov Y, Aittokallio T. Re-defining synthetic lethality by phenotypic profiling for precision oncology. Cell Chem Biol. 2021 Mar 18;28(3):246-256. doi: 10.1016/j.chembiol.2021.01.026.

- Biologically, this issue is known as "epistasis," a well-researched topic with substantial existing literature. While statistical interaction tests have been applied, domain knowledge and modeling of underlying structures are essential (e.g., [4][5]). Although this study treats synthetic lethality as a special case and even conducted biological experiments, it does not discuss this background, leaving unclear what value this research or its new methods can provide on the top of many traditional studies on this long-standing research topic.
   - [4] Segrè, D., DeLuna, A., Church, G. et al. Modular epistasis in yeast metabolism. Nat Genet 37, 77–83 (2005). https://doi.org/10.1038/ng1489
   - [5] Terada A, Okada-Hatakeyama M, Tsuda K, Sese J. Statistical significance of combinatorial regulations. Proc Natl Acad Sci U S A. 2013 Aug 6;110(32):12996-3001. doi: 10.1073/pnas.1302233110.

- Consequently, the adaptive sampling and bandit approaches proposed in Section 4 to identify pairs with interaction effects “without directly measuring pairwise effects” are unconvincing and require additional justification, clearer assumptions, and validation. By definition, determining the presence of an "interaction effect" would seem to require measuring both pairwise and single effects at least. For example, in synthetic lethality, there are gene pairs where knocking out either gene alone is non-lethal, but a double knockout is lethal. In this case, we have no observable clues suggesting that this pair is likely to have an "interaction effect." While assumptions in Sections 3.1 and 3.2 seem related to this point, some, such as the "low-rank R with a Gaussian prior on the columns" in line 350, appear ad hoc and inadequately justified. This point requires thorough analysis and explanation for proper justification of the proposed method.

- Further, introducing bandit (specifically, best-arm identification) for this problem requires clarification. In bandit approaches, sampling each arm multiple times is generally assumed, making the theory inapplicable in settings with no sampling for many (i,j) pairs. For synthetic lethality, for instance, it would be necessary to test double knockouts across all (i, j) pairs with replicates. Figure 6 compares the method with random search and conventional bandit methods, but the meaning of this comparison is unclear, necessitating additional justification.

- While the paper aims to address general "interaction effect" identification, its validation is limited to synthetic lethality, providing insufficient evidence for its general effectiveness across other cases.

### Questions
- For research proposing a new method, it would be essential to compare its advantages and accuracy against existing approaches. There are various statistical methods (likelihood-ratio tests, two-way ANOVA, etc) to identify interaction effects, so did you conduct comparisons with these standard methods?

- In terms of detecting synthetic lethality, I believe there are several studies in genetic statistics related to identifying "epistasis." Did you consult this literature?

- What are the primary reasons you believe traditional methods are inadequate for this purpose and we need new methods?

- Two methods for testing the interaction effect are proposed, but their distinct purposes and value are unclear. Which method appears more promising, and under what conditions should each be used?

- How do you test for the KL divergence identity condition required for the "separability test"? Is this a simple binary decision based on whether the KL divergence is below a certain threshold, rather than a hypothesis test? If so, how did you determine the threshold?

- The theoretical justification for the entire Section 4 seems insufficient; could you provide additional support if available? The "interaction effect" as defined in this paper seems fundamentally based on comparing the effects of "double perturbation" with "individual perturbations." Given this, the rationale for identifying promising pairs with interaction effects using adaptive sampling or bandit without actually conducting double perturbations is unconvincing. If you view this as an application of bandit’s best-arm identification, typically, double perturbation across all (i, j) pairs would need to be measured several times to gain meaningful information on arm expectations. Could you provide the following information?
   - A clearer explanation of what prior information or assumptions allow us to predict interaction effects without measuring pairwise effects
   - More rigorous justification for the low-rank and Gaussian prior assumptions

- For the evaluation of the main claim of "automated discovery of pairwise interactions" as suggested in the paper's title, could you:
   - Clarify how the proposed approach handles the lack of repeated sampling for many (i,j) pairs?
   - Explain the assumptions and modifications needed to apply bandit methods in this setting?
   - Provide a more detailed interpretation of Figure 6, explaining what insights can be gained from the comparison to random search and conventional bandit methods?

- Have you conducted any validation beyond the synthetic lethality example? As the title suggests, this paper aims to propose a general method for testing "interaction effects," but with no examples beyond synthetic lethality, it might be more suitable to focus claims on identifying biological "epistasis."

- For instance, when generating test cases in software development, identifying bugs that occur only under certain condition combinations could fit within this paper’s defined "interaction effect." A system might function correctly when condition 1=True or condition 2=True, but malfunction when both are true. Do you think this method is also effective for such identification? Specifically, what is the rationale for identifying this condition combination as promising without observing the behavior under condition 1=True and condition 2=True? Would this not be challenging in black-box testing?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a method for detecting pairwise interactions between gene perturbations. 
It first proposes two statistical tests for deciding whether two perturbations are separable or disjoint.
The statistical test of disjointness is employed in a greedy active matrix completion algorithm that decides which pair of perturbations to examine in the next step. The proposed method is evaluated in sythetical settings showing the validity of the statistical tests as well as in a real gene perturbation experiment where it performs better against other baselines that consider different choice of policy in the active matrix completion procedure.

### Strengths
The proposed methodology is interesting. 
The main strength of this work is that it makes the biological experimental process more efficient and with lower costs. 
The theoretical claims are justified with mathematical proofs and the effectiveness of the algorithm is empirically validated.

### Weaknesses
I am not a specialist in the biological field of gene perturbations experiments, but based on my understanding I would point out the following potential weaknesses for the improvement of the paper.

1. It is not quantified how much the biological experiments benefit from the active learning algorithm in terms of the total number of necessary perturbations.
How much more efficient is your algorithm compared to a standard exhaustive approach that would consider all possible perturbations? Specifically, what is the reduction in the number of experiments needed to achieve a comparable level of interaction discovery? A concrete comparison, perhaps in terms of the percentage of the search space explored, would be beneficial.

2. I am not sure if it possible but it would make sense to additionally compare the proposed method against causal discovery methods that utilize interventions, for example, DCDI [1] or GIES [2], or methods specifically designed for gene regulatory networks [3]. It would be interesting to see what would be the performance of a causal discovery method for a subset of given perturbations. Ofcourse that would require transforming the data into a format that contains a single value for every node for each sample. It's unclear why the authors are not considering methods that explicitly aim to discover causal relationships, especially given that the concept of 'interaction' is closely related to causal influence. The argument that causal discovery methods require all variables to be observed is not entirely convincing, as many methods can handle latent confounders or unobserved variables to some extent. A more thorough justification for not comparing against these methods is needed.

[1] Brouillard, Philippe, et al. "Differentiable causal discovery from interventional data." Advances in Neural Information Processing Systems 33 (2020): 21865-21877.

[2] Hauser, Alain, and Peter Bühlmann. "Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs." The Journal of Machine Learning Research 13.1 (2012): 2409-2464.

[3] Aibar, Sara, et al. "SCENIC: single-cell regulatory network inference and clustering." Nature methods 14.11 (2017): 1083-1086.

### Questions
I have the following questions.

1. By pairwise interactions do you mean causal dependencies or correlations? Can you also discover causal relations?
2. What do you mean by "unstructured data"? I would say that an image is structured as a grid of pixels.
3. Line 094 please elaborate on what you mean "by this notion of interaction".
4. Line 374 what are 3 dimensional tabular data? Please provide the dimensions.
5. Line 478 "Genes from the same pathway are ordered adjacently". Please rephrase/explain what it means.
6. Line 509. Can you explain more about how the top 5% pairs are chosen? Are they among the known interactions?
7. Line 511. How is the regret computed?

Some recommendations:
1. The first two sentences in the introduction require citation.
2. The font size in Fig. 1 is very small.
3. Increase the font size of the colormap in Fig. 2.
4. The font size in Fig. 3 (labels on images on the right) is very small.
5. In Fig. 3 you need to explain what the image on the right shows (presence or absence of interaction).
6. In Fig. 4 you should add a label in each figure and increase the font size of the colormap.
7. For Fig. 5 the same, nothing is visible.

I would like to hear your opinion on my feedback first and then be willing to raise my score.

### Soundness
3

### Presentation
3

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
The authors propose two test statistics to measure the separability and disjointness between pairs of perturbations. Perturbations are separable if they affect disjoint subsets of latent variables, and are disjoint if they affect disjoint parts of the observation. Their separability metric is validated on two synthetic datasets where the ground-truth data generating process is known (i.e. the graph of the perturbation and latent variables), as well as on a real cell painting dataset. They also show that the disjointness metric can be used in an active learning context on cell painting data to better uncover perturbations with pairwise interactions relative to several baselines.

### Strengths
* The authors tackle the important problem of determining whether it is worthwhile to run a costly experiment where two perturbations are applied simultaneously.
* The evaluation is thorough, and demonstrates utility on a real-world problem.

### Weaknesses
 * This is an applied paper, and I believe the novelty is weak.
* The separability metric essentially measures the mutual information between the latent variables corresponding to a pair of perturbations. There are many different ways to instantiate this, and it's unclear whether the authors' proposed metric itself is a valuable contribution. Specifically, the separability metric, defined as the absolute difference between the joint and individual KL divergences, could be computed using various methods beyond the one presented (e.g., iVAEs or other density estimation techniques). The paper does not explore the sensitivity of the conclusions to the choice of KL divergence estimator.
* A similar statement also holds for the disjointness metric. The disjointness metric, relying on additivity testing in a learned representation space, also lacks a clear justification for the specific approach taken. The paper does not discuss the impact of the representation learning method on the disjointness metric.
* Essentially, this paper combines many existing methods to achieve an empirical (and somewhat narrow) goal. I believe this is a valuable contribution, but it may be suited for a more applied venue.

### Questions
* Can you counter my points (in weaknesses) regarding the lack of novelty in this work?

Minor points:
* The right-hand side of the bottom equation on p.4 seems off; isn't $p_{Z_i}$ a distribution over a scalar random variable, and the argument $g^{-1}(x)$ is a vector?
* I think the clarity can be improved (and some space saved) if you apply a log to both sides of Equation (1) and go directly to Equation (3), without writing Equation (2).

### Soundness
3

### Presentation
3

### Contribution
3
