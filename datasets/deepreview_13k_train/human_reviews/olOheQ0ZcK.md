# Distance Estimation for High-Dimensional Distributions

- Decision: Reject
- Scores: 8, 6, 1, 8

## Abstract
We study the distance estimation problem for high-dimensional distributions. Given two distributions $\mathcal{P}$ and $\mathcal{Q}$ over $\{0,1\}^n$, and a parameter $\varepsilon$, the goal of distance estimation is to determine the statistical distance between the two distributions up to an additive tolerance $\pm \varepsilon$. Since exponential lower bounds (in $n$) are known for the problem in the standard sampling model, research has focused on models where one can draw conditional samples. 

Among these models, \textit{subcube conditioning} ($\mathsf{SUBCOND}$), i.e., conditioning on arbitrary subcubes of the domain, holds the promise of widespread practical adoption owing to its ability to capture the natural behavior of distribution samplers. In this paper, we present the first polynomial sample distance estimator in the conditional sampling model, and our algorithm makes $\tilde{\mathcal{O}}(n^3/\varepsilon^5)$ \subcond queries. We implement our algorithm to estimate the distance between distributions arising from real-life sampling benchmarks, and we find that our algorithm easily scales beyond the naive method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of estimating the total variation distance between distributions $P$ and $Q$ on $\{0,1\}^n$. This problem is known to require $\exp(n)$ samples if we only get access to queries. This paper considers the SUBCOND model, where you are allowed to sample from a distribution conditioned on a certain prefix. It proves that one can estimate the TV distance with query complexity $poly(n, 1/\epsilon)$. I found this statement surprising (although I am not familiar with the literature in the area which is vast).   In terms of techniques, the paper seems to make use of prior results which adding some new ingredients of its own. I think this is a nice contribution that ought to be accepted.

### Strengths
1. The problem of TV estimation is important. The existing lower bounds are very strong, which motivates looking for other models where it is easier to estimate. The SUBCOND model is fairly natural for the Boolean hypercube setting.

2. I found the result in itself surprising, though I am not an area expert. After understanding the paper better, maybe I am a little less surprised, but I still think its a great result. 

3. Technically, the paper is sound, and above the bar for acceptance. There seem to be two novel ideas, the simpler one is to  "tame" the distribution so that there is some non-trivial probability on both the subcubes $x_i = 0$ and $x_i =1$. This is achieved essentially by adding some noise to the distribution. The second is using the conditioning oracle to get a multiplicative approximation to the probability of string, using the formula $\Pr[x =a] = \Pr[x_1 =a_1]\cdot \Pr[x_2 =a_2|x_1 =a_1] \cdots$.  It is simple and elegant. They plug this into a previous result that lets you estimate the total variation distance given good enough estimates of the importance weights.

### Weaknesses
1. The title promises too much compared to what the paper delivers. When most people think of high dimensional distributions, they don't have the Boolean hypercube in mind as the domain, they would think of $\mathbb{R}^n$. I would suggest adding "discrete distributions" to the title, and possibly mentioning the need for conditional samples.

2. On a related note, the SUBCOND model is very natural in the discrete setting (for product domains). I wonder to what extent these techniques can extend to other domains, and what a reasonable analog of this model might be.

### Questions
- It appears that your results allow you to estimate the importance weights  $Q(x)/P(x)$ for $x \sim Q$. If so, this might be useful for estimating various other divergences such as KL and Renyi.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
It is known that estimating TV distance between two discrete probability distributions over $\{0,1\}^n$ has a sample complexity lower bound of $\Omega(2^n/n)$. In this work, the authors focus on a more powerful model, namely SUBCOND, which takes a prefix as input and returns the full string according to the conditional distribution. With this model, the authors design DistEstimate algorithm that makes $\tilde{O}(n^3\log(1/\delta)/\varepsilon^5)$ calls to SUBCOND and returns an estimate of the TV distance with margin of error $\varepsilon$ with probability $1-\delta$.

### Strengths
- The authors provide clear motivation in terms of why a stronger model is needed for distance estimation.
- The explanation of the algorithm is clear.
- The proof of the main theorem is mostly self-contained. The proofs, from a quick read, seem sound. The technique of computing expectation of number of queries using properties of negative binomial distributions is really nice.
- A direction for future research is also discussed.

### Weaknesses
 - There needs to be an example in the introduction that describes scenarios in which the SUBCOND query is available. Personally, I have been very curious in such scenarios until I read the Application section.
- In the experiment, $\varepsilon=0.5$ is too large considering the scale of the TV distances. Also, there should be error bars in Figure 1, at least for small numbers of dimensions in order to demonstrate the stability of the algorithm.



### Questions
- Algorithm 1 returns the average of  $1-p_i-q_i$. Should the definition of $Z$ in Lemma 1 be divided by $m$ as well?
- I suggest the authors add a simulation to confirm that DistEstimate attains $\varepsilon$-estimation error with probability at least $1-\delta$.

Minor comments:  
- The notations for the probability distributions are not consistent. Some times they are $P,Q$, the other times they are $\mathcal{P},\mathcal{Q}$. Please check throughout the paper.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper claims itself presents the first polynomial sample distance estimator in the conditional sampling model. This paper provides detailed proofs and simple experiments for this paper.

### Strengths
This paper presents the first polynomial sample distance estimator in the conditional sampling model. I roughly check the proof, and they are OK to me at this time. Consequently, in theory aspect, I am satisfied with authors' contributions.

### Weaknesses
Although I am satisfied with authors' theoretical contributions, I am "extremely' unsatisfied with experiment part of this paper. Figure 1 and Table 1 just do not make any sense to me. If authors could improve that part, I will largely raise my rating.

1. Please conduct 'enough' experiments to justify your theorem. This can be plots of repeated experiments showing the relationships between $n$, $\delta$, and $\epsilon$, which is widely used in this area. 

2. Dimensions in your experiments are not high enough, and $\epsilon$ is too large. 

3. If possible, provide a comparison of your method with other existing methods, which could further demonstrate the significance of your method.

### Questions
Is that possible to provide a high probability bound with respect to the number of queries? If not, could your provide the technical hardness?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of estimating the distances between two distributions $P$ and $Q$ over the $n$-dimensional Boolean hypercube. Since the problem is known to require $\Omega(2^n/n)$ samples from $P$ and $Q$ to estimate the distance up to an additive constant, this paper considers the subcube conditioning query model, where each query can be made from $P$ and $Q$ conditioned on a specified subcube of the domain. This paper gives an algorithm for estimating the distance to additive $\varepsilon$ using $\tilde{O}(n^3/\varepsilon^5)$ queries as well as a lower bound showing that $\Omega(n/\log n)$ queries are necessary in the subcube conditioning model for constant $\varepsilon$.

### Strengths
+ To the best of my knowledge, the problem of distance estimation has not previously been studied in the subcube conditioning model. 
+ The polynomial query complexity in the subcube conditioning model is an exponential improvement over the known $\Omega(2^n/n)$ query complexity lower bound in the standard model.

### Weaknesses
 - Although there is good intuition for parts of the main result, I think the paper could benefit from additional algorithmic/analytic intuition rather than the full formal proofs. For example, I would have liked to see more details about how the tamed distribution could be accessed using subcube conditioning queries. Specifically, the paper mentions 'taming' the distribution, but it's not clear how this is achieved algorithmically through subcube conditioning. The connection between the theoretical notion of 'taming' and the practical implementation using subcube queries needs further clarification. I would have also liked to see intuition on where the $n^3$ and $1/\varepsilon^5$ factors come from. The paper provides the final query complexity but lacks a breakdown of how these factors arise from the different steps of the algorithm and analysis. This makes it difficult to understand the bottlenecks of the approach.
- It is not clear to me that the applications of distance estimation with subcube conditioning queries is well-suited for the particular learning theory community at ICLR. The paper touches on applications, but these feel somewhat disconnected from the core interests of the ICLR audience, which tends to focus on more mainstream machine learning problems. The motivation for studying this particular query model in the context of ICLR is not entirely convincing.
- Although I do not think experiments are necessary for a paper with solid theoretical foundations, I think the experimental section of this paper is a bit unclear (see questions below). The description of the experimental setup is vague, particularly regarding the generation of the scalable benchmarks and the representation of real-world circuits. This lack of clarity makes it difficult to assess the practical relevance of the proposed approach.

### Questions
1) How is the distance estimation problem applied to constrained samplers? 
2) How was the scalable benchmark generated and how are the real-world circuits represented by the Boolean formulas?
3) How does the tradeoff between sample complexity and TVD look like for these datasets?
4) What are additional applications of distance estimation with subcube conditioning queries?

EDIT (Post-rebuttal): Thanks for answering my questions. I think my main concerns about the intended audience at ICLR have been addressed by additional discussions on 1) applications of subcube conditioning queries, though perhaps slightly less mainstream and 2) intuition on the main algorithm and proof. Although I think this paper is a good theoretical work by itself, I see that additional experiments have also been included in the discussion phase. Thus I have adjusted my score accordingly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
