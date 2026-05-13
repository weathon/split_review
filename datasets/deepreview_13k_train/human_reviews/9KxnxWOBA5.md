# Towards Optimal Multi-draft Speculative Decoding

- Decision: Accept
- Scores: 8, 3, 5, 5

## Abstract
Large Language Models (LLMs) have become an indispensable part of natural language processing tasks. However, autoregressive sampling has become an efficiency bottleneck. Multi-Draft Speculative Decoding (MDSD) is a recent approach where, when generating each token, a small draft model generates multiple drafts, and the target LLM verifies them in parallel, ensuring that the final output conforms to the target model distribution. The two main design choices in MDSD are the draft sampling method and the verification algorithm. For a fixed draft sampling method, the optimal acceptance rate is a solution to an optimal transport problem, but the complexity of this problem makes it difficult to solve for the optimal acceptance rate and measure the gap between existing verification algorithms and the theoretical upper bound. This paper discusses the dual of the optimal transport problem, providing a way to efficiently compute the optimal acceptance rate. For the first time, we measure the theoretical upper bound of MDSD efficiency for vocabulary sizes in the thousands and quantify the gap between existing verification algorithms and this bound. We also compare different draft sampling methods based on their optimal acceptance rates. Our results show that the draft sampling method strongly influences the optimal acceptance rate, with sampling without replacement outperforming sampling with replacement. Additionally, existing verification algorithms do not reach the theoretical upper bound for both without replacement and with replacement sampling. Our findings suggest that carefully designed draft sampling methods can potentially improve the optimal acceptance rate and enable the development of verification algorithms that closely match the theoretical upper bound.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents several new results about Multi-Draft Speculative Sampling. 
1. It transforms the problem of computing the optimal acceptance rate into a subset selection problem.
2. For some cases it provides a practical solution of the problem. This provides a theoretical upper bound on the acceptance rate.

The authors then measure the theoretical upper bound on some datasets, and measure the gap between the upper bound and previous algorithms on these datasets.
They present a greedy algorithm which is able to match the theoretical upper bound in many cases.

### Strengths
The paper makes progress on understanding the acceptance rate of Multi-Draft Speculative Sampling. The authors show a clever transformation of the transportation problem formulation of optimal acceptance rates to a subset selection problem, and then show an algorithm to solve the subset selection if the draft distribution satisfies certain properties. 
They then propose a new greedy Multi-Draft Speculative Sampling algorithm, which is closer to the optimal acceptance rate on some datasets.

The results in the paper seem to me to be quite novel and significant.

### Weaknesses
The paper takes a bit of effort to read, partly because of a lot of notation, and partly because of results that may not be familiar to a lot f readers. I am not sure if the authors can do much about this.

### Questions
Do your results extend to trees of drafts in a straightforward way?

I would like to see a comparison to https://openreview.net/forum?id=N1L5TgtkAw

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper works on the dual problem of the transport problem of multi-draft speculative decoding and show that the optimal acceptance rate is equivalent to a subset selection problem. Then, the paper provides several methods to compute such rates for commonly used multi-draft proposal methods (sampling with replacement, sampling without replacement). The paper proposes a greedy draft construction method and provides several empirical results that showcase the benefit of the proposed algorithm.

### Strengths
It is interesting to see that two existing verification approaches (K-Seq and the widely used RRS) can be unified as solving the same optimal transport problem coresponding to sampling without replacement $p_{draft}$. Therefore, they share the same upper bound. Table 1 shows that for a variety of models and settings, the two methods are close enough to the optimal acceptance rates.

The proposed "greedy" draft generation approach and verification method is an interesting combination of the greedy decoding method and ordinary sampling method.

The ablation studies are informative with a clear comparison with other baseline methods across different temperature and number of draft tokens.

### Weaknesses
### significance

Much portion of the paper is dedicated to theoretical derivations of the optimal acceptance rate. However, the description and the development of the proposed algorithm is underplayed. 

The proposed methods deserve a proper name, clear demonstration of the verification algorithm (is the algorithm practical for $n>2 as compared to SpecHub?) and more thorough theoretical and experimental investigations to demonstrate the pros and cons compared with previous algorithms.


### clarity 

The clarity of the paper can be significantly improved, including but not restricted to:

(1). In Section 2.2, the informal description of speculative decoding is very confusing. This seems to be a short summary of the formal description below, but it is hard to understand what $\max P(i=j)$ means before going into the details of the optimal transport problem.

(2). The same problem also applies to Section 2.3, where the informal description of multi-draft speculative decoding is confusing. I would suggest reframing the descriptions and move the examples of $p_{draft}$ after the definition.

(3). Section 3 is dedicated to provide the proof for the subset selection problem (Eq. 8). I would suggest move the proof details to the appendix and optionally write a short proof sketch section that only displays the important idea behind the proof and/or the part of the proof that is needed for the development of the later sections. 

(4). The description of Theorem 3 and 4 can be improved. What is the definition of $Q$ and $q$ in these cases? What are the consequences of the special cases (with replacement and without replacement)? 

(5). In Table 1, are "greedy" and "verify" the proposed methods in Section 5.1 and 5.2?

### Questions
N/A.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is concerned with acceptance rate of MDSD in LLMs. Authors derive the dual problem, and then prove it has an integer optimal solution, furthermore, they provide a greedy algorithm that, in some cases, perform better without replacement.

### Strengths
Paper is mathematically rigorous; it is relatively easy to follow and grasp new concepts. Authors do a good job of highlighting the drawbacks of previous work and offer solutions.

### Weaknesses
Some claims are optimistic, such as "the upper bound has never been computed before", I personally refrain from making such certain statements. Some contributions are minor, as an example, deriving the dual of an LP is not a contribution, yet it is claimed to be in the first bullet point of contributions. Although paper is mathematically mature, it borrows a lot from previous publications, in other words, novel theoretical contribution is minor.

You stated that problem (equation 7) is intractable/difficult to solve. What algorithms did you use? modern LP algorithms such as interior point methods are quite capable at handling large problems (with exponential constraints), and recently there have been solvers implemented on GPU (see cuPDLD-C). Your greedy algorithm is another version of coin problem, in order for it to be optimal, the environment has to be canonical (see “Error Bounds and the Applicability of the Greedy Solution to the Coin-Changing Problem,”), I suggest you incorporate that in your proof. You have mentioned theoretical upper bound multiple times, however it is not explicitly defined, is it $\alpha^*$? I suggest you use Radix sort, which is linear in the size of input, and helps with the overall complexity of your problem.

### Questions
You stated that problem (equation 7) is intractable/difficult to solve. What algorithms did you use? modern LP algorithms such as interior point methods are quite capable at handling large problems (with exponential constraints), and recently there have been solvers implemented on GPU (see cuPDLD-C). Your greedy algorithm is another version of coin problem, in order for it to be optimal, the environment has to be canonical (see “Error Bounds and the Applicability of the Greedy Solution to the Coin-Changing Problem,”), I suggest you incorporate that in your proof. You have mentioned theoretical upper bound multiple times, however it is not explicitly defined, is it $\alpha^*$? I suggest you use Radix sort, which is linear in the size of input, and helps with the overall complexity of your problem.

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
This paper studies the problem of multi-draft speculative decoding (MDSD), where the draft model provides multiple draft tokens for each draft position. The authors first provide a way to compute the optimal acceptance rate. Then, they measure the theoretical upper bound of MDSD with large vocab size and quantify the gap between existing verification algorithms and this bound. Besides, the authors also provide a greedy draft sampling methods to approach the theoretical upper bound of MDSD.

### Strengths
1. The idea of transforming the problem into a subset selection problem and considering the dual of the problem is novel and makes sense. 
2. The authors rigorously give some theoretical findings, including the upper bound of MDSD and a efficient method to compute the theoretical acceptance rate.
3. The authors propose a greedy draft sampling method and conduct extensive experiments to demonstrate its effectiveness.

### Weaknesses
While this paper provides rigorous theory and analysis, I think there exists some weakness to further improve the manuscript.

1. The motivation and background should be clearly illustrated, and the authors could consider add some intuitive examples and figures to improve the presentation. 
2. Please discuss the connections to the related works. It is confusing for readers without the knowledge about SpecTr. Besides,  please give a clear notation section. For example, the number of draft tokens for each draft position and the number of draft length should be clarified. 
3. Please describe the whole algorithm of the greedy draft sampling method. For example, after constructing the first  $n$ draft tokens for the first draft position, how we can construct the following draft tokens? Besides, this algorithm is similar to the top-k sampling, with only an additional random sampled token. The authors should discuss their difference.
4. The experiments could be strengthen by evaluating the block-wise mean accepted tokens and real-world speedup. Besides, more experiments with different model scales (e.g. 33B, 70B) and different benchmarks (e.g. MT-Bench [1] and Spec-Bench[2]) are necessary to demonstrate the conclusions.

### Questions
1. In the real-world applications of speculative decoding, the acceptance rate of different position is usually not i.i.d. I wonder if this will affects the proposed theory and greedy draft sampling methods.
2. In Table 1, some results of empirical $\alpha$ is even higher than the theoretical upper bound. Could you please provide a detailed explanation? 
3. In ablation study 1, the authors show an interesting phenomenon that the impact of temperature is non-monotonic. Different methods consistently show a turn around temperature $T=0.9$. Could you please provide a detailed explanation?
4. Can proposed greedy draft sampling methods adapt to other retrieval-based speculative decoding methods? (e.g. Lookahead Decoding [1] and REST [2])

[1] Fu, Yichao, et al. "Break the sequential dependency of llm inference using lookahead decoding." arXiv preprint arXiv:2402.02057 (2024).

[2] He, Zhenyu, et al. "Rest: Retrieval-based speculative decoding." arXiv preprint arXiv:2311.08252 (2023).

### Soundness
3

### Presentation
2

### Contribution
2
