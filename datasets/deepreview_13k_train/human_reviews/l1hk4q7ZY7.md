# Relation Augmented Preferential Bayesian Optimization via Preference Propagation

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
In black-box optimization, when directly evaluating the function values of solutions is very costly or infeasible, access to the objective function is often limited to comparing pairs of solutions, which yields dueling black-box optimization. Dueling optimization is solely based on pairwise preferences, and thus notably reduces cost compared with function value based methods such as Bayesian optimization. However, an optimization performance gap obviously exists between dueling based and function value based methods. This is mainly due to that most existing dueling optimization methods do not make full use of the pairwise preferences collected. To fill this gap, this paper proposes relation augmented preferential Bayesian optimization (RAPBO) via preference propagation. By considering solution similarity, RAPBO aims to uncover the potential preferential relations between solutions within different preferences through the proposed preferential relation propagation technique. Specifically, RAPBO first clusters solutions using a Gaussian mixture model. After obtaining the solution set with the highest intra-cluster similarity, RAPBO utilizes a directed hypergraph to model the potential relations between solutions, thereby realizing relation augmentation. Extensive experiments are conducted on both synthetic functions and real-world tasks such as motion control and spacecraft trajectory optimization. The experimental results disclose the satisfactory accuracy of augmented preferences in RAPBO, and show the superiority of RAPBO compared with existing dueling optimization methods. Notably, it is verified that, under the same evaluation cost budget, RAPBO is competitive with or even surpass the function value based Bayesian optimization methods with respect to optimization performance. The codes can be found in https://anonymous.4open.science/r/RAPBO-E15F.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studied the dueling optimization problems under the framework of preferential Bayesian optimization (PBO). The key finding was that by leveraging directed hypergraphs to augment the relations among preference dataset, the optimization efficiency of (PBO) could be improved, and even competitive with the real-value-based Bayesian optimization method. Both synthetic functions and real-world tasks were considered to validate the effectiveness.

### Strengths
1. The idea of utilizing a directed hypergraph to model and augment the potential relations between solution seems noval.
2. The paper is easy-to-follow. It is easy to clarify the motivations and contributions.
3. The sample efficiency of dueling optimization problems is important in recommender and human-machine interaction systems.

### Weaknesses
1. The motivations may not be convincing. The dueling optimization problems were originally addressed by dueling bandits algorithms. In PBO, which considered continuous search space and the Bradley-Terry-Luce model, the Gaussian processes (GPs) was introduced with kernels and priors that had already defined the relation among solution in the latent space. Therefore, in my opinion, what this work did is to supplement the characterization of correlation that has been quantified by priors and kernel functions. If so, I think a more elegent way is  to modify the format of kernel functions and strictly follow the Bayes rule, rather than performing preference propagation following by constructing two GPs in a single round, as presented from Line 167 to Line 170 in Algorithm 1, which not only increases computational complexity but also weakens the principle of the Bayesian optimization.

3. The contributions, a.k.a. the introduction of GMM and directed hypergraph, were somewhat noval but not strong enough. No theoretical analysis nor design principles were used to underpin the rationality of the proposed algorithm.

2. The experiment results are not satisfactory. The big variance implies that the proposed method may not statistically outperform other baselines in most cases. Methods such as Wilcoxon rank sum test could be used to demonstrate this point.

### Questions
1. What is the essential difference between introducing the directed hypergraph and calibrating the kernel and prior functions of GPs?
2. Is there any evidence that value-based Bayesian optimization should be more efficient than pair-wise comparison PBO?
3. Compared with GP-UCB or PBO, what is the the computational complexity of RAPBO?

### Soundness
2

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
4

### Summary
This paper studies the problem of dueling black box optimization, an extension of black box optimization problem (or Bayesian Optimization (BO)). In the scenario of dueling BO, the agent does not have access to the function values, but can only sample two points at the same time and get only a noisy sample about whose function value is larger (i.e., a noisy comparison between these two points). This paper uses the logistic assumption for the comparison outcomes. 

The authors proposed a new algorithm relation augmented preferential Bayesian optimization (RAPBO) for dueling BO, and then make numerical experiments to compare the proposed algorithm with previous algorithms. The numerical results show some superiority of the proposed algorithm than previous algorithms.

### Strengths
This paper studies an interesting problem and proposed a new algorithm with some novelty. The numerical results are good and give some hints about the performance of the proposed algorithm.

### Weaknesses
This paper has a major weakness: lack of evidence to show the improvements of the proposed algorithm than previous algorithms. This paper does not have any theoretical conclusions of the proposed algorithm. It does have numerical experiments, but from the writing of the paper and small scales of the experiments, these experiments do not seem to be a standard benchmark for the dueling BO area. Hence, from the writing of the paper, it does not have enough evidence to demonstrate the significance of this paper's results.

### Questions
Is there any theoretical conclusion about the proposed algorithm, and how does it compare to existing algorithms?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a propagation technique based on directed hypergraph for data augmentation in Preferential Bayesian Optimization, which improves efficiency in the use of data and achieves competitive results to function-based BO.

### Strengths
(1) The paper identifies shortcomings of traditional methods in terms of under-utilisation of data and proposed a propagation method to improve data efficiency.

(2) The proposed method seem to significantly improve performance of PBO in both synthetic and real-world data.

(3) The paper is easy to follow.

### Weaknesses
 (1) The paper claim that "existing dueling optimization methods do not make full use of the pairwise preferences collected" but lacks of support. Why augmented relation can not be learnt in original algorithms, which indicates that relation propagation is necessary? I think the current experiment(Figure 4.) is not sufficient enough.

(2) The discussion on sensitivity is cursory. The PBO performance is naturally related to the clustering performance, since the assumption that similar solutions exhibit analogous relations holds only when exact clustering results is achieved.  Why RAPBO is consistent when k varies or clustering results?

(3) No investigation on other neighbor-based augmentation methods such as linear interpolation. That is, is GMM clustering + add edges unique to this problem?

(4) The contribution focus on the proposed augmentation method.

### Questions
Figure 4. (top plot) indicates that the original method have better Preference Num. than Augmented, which conflicts with the claim in the paper? Is this a typo or my understanding is wrong?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose relation augmented preferential Bayesian optimization (RAPBO) via preference propagation. RAPBO aims to uncover the potential preferential relations between solutions within different preferences through the proposed preferential relation propagation technique. The experimental results disclose the satisfactory accuracy of augmented preferences in RAPBO, and show the superiority of RAPBO compared with existing dueling optimization methods.

### Strengths
S1: The paper is easy to follow and well-organized.

S2: The authors open source the code for reproduction.

S3: The authors conduct extensive experiments to validate the efficacy of the proposed method.

### Weaknesses
W1: The font in Fig.1 is too small. Please kindly enlarge the font in Fig.1 to make it more readable.

W2: The authors should provide a notation in the methodology section.

### Questions
NA

### Soundness
3

### Presentation
2

### Contribution
2
