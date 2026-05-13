# Utilitarian Algorithm Configuration for Infinite Parameter Spaces

- Decision: Reject
- Scores: 5, 8, 6, 8, 8, 6

## Abstract
Utilitarian algorithm configuration is a general-purpose technique for automatically searching the parameter space of a given algorithm to optimize its performance, as measured by a given utility function, on a given set of inputs. Recently introduced utilitarian configuration procedures offer optimality guarantees about the returned parameterization while provably adapting to the hardness of the underlying problem. However, the applicability of these approaches is severely limited by the fact that they only search a finite, relatively small set of parameters. They cannot effectively search the configuration space of algorithms with continuous or uncountable parameters. In this paper we introduce a new procedure, which we dub COUP (Continuous, Optimistic Utilitarian Procrastination). COUP is designed to search infinite parameter spaces efficiently to find good configurations quickly. Furthermore, COUP maintains the theoretical benefits of previous utilitarian configuration procedures when applied to finite parameter spaces but is significantly faster, both provably and experimentally.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies utilitarian algorithm configuration, which is about automatically searching the parameter space of a given algorithm to optimise for its performance.

The first proposed algorithm is OUP.  It is a UCB style algorithm for finding configurations with good capped mean utility, with the addition of a scheme for periodically doubling the cap time.

The main algorithm is COUP. It builds on a new notion of optimisation goal called (epsilon, gamma) optimal. Epsilon is about being close to optimality and gamma controls how many configurations to sample. For fixed epsilon and gamma, the inner algorithm is for the most part just OUP. The novelty of the proposed algorithm is that it allows the sharing of trials over different epsilon and gamma.

### Strengths
The proposed method is general and there are extensive experiments demonstrating its performance.

### Weaknesses
The presentation of this paper is very hard to follow.

What is delta in OUP? I don't see it being referenced in the description of OUP. Is it only used in one of the subroutines?

### Questions
What is delta in OUP? I don't see it being referenced in the description of OUP. Is it only used in one of the subroutines?

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
An approach for algorithm configuration is presented based on a maximizing the utility of the target algorithm. The approach follows a line of work on "utilitarian procrastination (UP)", extending the previous work to function in continuous (infinite) spaces. An interesting aspect of the work is that this extension does not come at the cost of hurting performance on the finite-space case, in fact the performance improves. The resulting method, COUP, has bounds proven indicating essentially how good the configurations it finds are.

### Strengths
1. The paper moves the theoretical results for algorithm configuration in a very important direction, namely one step closer to real-world settings.
2. The paper is generally understandable at various levels of detail -- one need not delve into the math to understand the what and why of the paper. The math is clean and well-written, but I note that I could not completely evaluate all of the proofs.
3. The experimental results are quite good, especially in an area where the gains have been mostly small or just on different areas of the Pareto front of time vs quality. This approach is very competitive.

### Weaknesses
 1. There are a few minor clarity issues:
	1. The start of the paper is a bit of a slog. It would have been nice to get to the point faster.
	2. I do not understand why the notation for Algorithm 1 is introduced after the algorithm is explained. I needed the notation before reading the explanation, so I ended up just being confused until I found the notation, then had to go back and read it again. 
	3. In Algorithm 1, i is shadowed on line 7. Very minor, but it just seems weird (the same goes for Alg. 2).
2. I found the visuals in the experiments sometimes hard to read, and was confused by some aspects.
	1. Particularly the brown/purple/green combination has very similar shadings on some monitors/printers, another color scheme might be better. 
	2. In Figure 3, the green line for OUP goes backwards between total time 10^0 and 10^1. Something must be wrong there.
	3. The symbols in Figure 5 do not match the legend, and in all honesty I can barely figure out what is going on here. The figures are just too small with too many points crowded in the same spots. 

### Questions
1. See issues with experiments above.
2. On line 6 of algorithm 2, COUP samples new configurations at random, which is basically how all of the theoretical approaches to AC work. Is there no way of sampling configurations that might actually be good while maintaining guarantees? It feels like these approaches are all poking around in the dark rather than actually optimizing. (future work, I suppose)

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of algorithm configuration. There are two key elements that are not handled in combination by previous approaches: (1) infinite (potentially continuous) parameter spaces, and (2) utilitarian reward (which is a function of the running time).

A new algorithm is proposed, COUP, which is based on UCB, using doubling trick for extending cap on the running time, and sampling increasing numbers of arms to deal with the infinite arm's space. A simplified version for finite number of arms, OUP, is also considered. The algorithms are shown to achieve close to optimal configuration. 

The proposed algorithm is compared to another utilitarian algorithm UP, achieving faster convergence for the finite case. The COUP algorithm  seems to perform well empirically for the many configurations case as well.

### Strengths
The problem considered is important, and the proposed algorithms are sound.

The theoretical guarantees are valuable.

The paper is well written.

### Weaknesses
The infinite parametric space problem seems related to me to the bandit problems in continuous/metric spaces. For those problems, the performance of the bandit algorithm is compared to the optimal solution, which is facilitated by Lipschitz or stronger conditions on the reward function. In this work only the top percentile is considered (which is simpler with sampling), but I assume similar conditions on the utility could be considered here as well.

The experiments use a very limited set of baselines (UP). I think, it would have reasonable to test the algorithm against algorithms that minimize the running time (with the utility coinciding with the running time, or just using the running time as surrogate measure for those algorithms). Testing non-bandit based algorithm configuration approaches would also make sense.

### Questions
The questions for me are centered around the relation with metric space bandits, and the use of additional baselines.

### Soundness
3

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
3

### Summary
The paper introduces COUP (Continuous, Optimistic Utilitarian Procrastination) procedure, which explores the parameter space - possibly uncountably infinite - of a given algorithm to optimize its performance on a specified set of inputs, with performance measured through a utility function. The finite (parameter space) verison of the procedure, known as OUP, improves upon the UP (Graham et al., 2023b) by incorporating ideas from the UCB algorithm in bandit literature. Additionally, COUP generalizes the procedure to possibly uncountably infinite parameter space. While doing so, COUP retains the theoretical guarantees of the UP algorithm while being significantly faster, as demonstrated by both theoretical guarantees and empirical results.

### Strengths
1) The finite version (OUP) procedure improves over the previous (UP) procedure using ideas from UCB algorithm in bandit literature.

2) Extensions to the infinite parameter space algorithms.

3) Maintaining the theoretical guarantees provided by the UP procedure.

### Weaknesses
1) The presentation of Section 3 could be improved slightly; introducing the notation before presenting Algorithm 1 might enhance readability.

2) In Figure 1 - second row - third graph - there is a sudden drop in the total runtime (for OUP) around $\epsilon \approx 0.19$. Is this due to some specific structure of the problem/algorithm being analyzed?

3) The authors mention that Hyperband also performs well in the percentage-gap metric, but from Figure 5, it’s unclear to me that COUP/OUP actually outperforms it. Is there a reason to expect COUP/OUP would perform better, or is there something I might be overlooking?

### Questions
1) Anonymous repo link seems to be missing?

2) In Figure 1 - second row - third graph - there is a sudden drop in the total runtime (for OUP) around $\epsilon \approx 0.19$. Is this due to some specific structure of the problem/algorithm being analyzed?

3) The authors mention that Hyperband also performs well in the percentage-gap metric, but from Figure 5, it’s unclear to me that COUP/OUP actually outperforms it. Is there a reason to expect COUP/OUP would perform better, or is there something I might be overlooking?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduced a new procedure, COUP, which claims that 1) it can run on continuous space and 2) it is faster than UP in the case of discrete space. Later experiments confirmed their claims.

### Strengths
The paper appears organized and well-written. The authors effectively emphasized the big picture in Sections 1 and 2, providing a clear understanding of this new and improved algorithm.

The algorithm is general enough to be applied to many optimization problems. It includes theoretical properties; however, we did not check the appendix for the validity of the proof.

### Weaknesses
na

### Questions
na

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the problem of utilitarian algorithm configuration with inifinite number of parameters.
The key idea is i) to adopt the UCB (upper confidence bound) method rather than the SE (sequential elimination) method in balancing exploration and confirmation of the best parameter to reach the same guarantee with shorter run time, and ii) to relax the reference point of the guarantee from the best to quantiles.

### Strengths
- It is well-motivated, well-executed and well-written.
- The theoretical analysis looks intuitive and right.

### Weaknesses
 - The impact of the extension to continuous space is unclear. I would suggest to compare COUP with OUP + fixed discretization of continuous space.
- The continuous structure (similarities among neighbor parameters) is not utilized in COUP. So, C in COUP does not describe its nature accurately.  

Minor:
- In Lemma 2, don’t you need “with probability 1- \delta”?
- Why not using log scale for the vertical axes of Figure 1?

### Questions
Can you address the points I raised in Weakness?

### Soundness
3

### Presentation
4

### Contribution
2
