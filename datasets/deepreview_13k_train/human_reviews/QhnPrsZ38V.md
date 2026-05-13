# Explainable self-supervised learning by spiking functions: a theory

- Decision: Reject
- Scores: 3, 5, 1, 5, 5

## Abstract
Deep neural networks trained in an end-to-end manner have been proven to be efficient in a wide range of machine learning tasks. However, there is one drawback of end-to-end learning: The learned features and information are implicitly represented in neural network parameters, which are not explainable: The learned features cannot be used as explicit regularities to explain the data probability distribution. To resolve this issue, we propose in this paper a new machine learning theory, which describes in mathematics what are 'non-randomness' and 'regularities' in a data probability distribution. Our theory applies a spiking function to distinguish data samples from random noises. In this process, 'non-randomness', or a large amount of information, is encoded by the spiking function into regularities, a small amount of information. Then, our theory describes the application of multiple spiking functions to the same data distribution. In this process, we claim that the 'best' regularities, or the optimal spiking functions, are those who can capture the largest amount of information from the data distribution, and then encode the captured information into the smallest amount of information. By optimizing the spiking functions, one can achieve an explainable self-supervised learning system.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a theory on learning regularities from data using spiking functions.

### Strengths
The theoretical framework presented in this paper is intriguing and can provide valuable insights, if backed up by empirical evidence.

### Weaknesses
 - Lack of Empirical Validation: The theory is purely speculative without an implemented model, making it difficult to assess practical effectiveness. The absence of empirical results leaves the core claims untested, particularly regarding the ability of spiking functions to effectively capture and differentiate meaningful regularities from noise in real-world data. Empirical results demonstrating its impact on existing self-supervised learning models would strengthen the paper. Specifically, the paper lacks any quantitative evaluation of the proposed metrics (spiking efficiency, conciseness, etc.) on standard datasets.
- Implementation Feasibility: The authors acknowledge that practical implementation of their theory remains to be developed, leaving a significant gap between theory and application. The paper does not address the computational complexity of optimizing the proposed spiking functions or the potential challenges in scaling the approach to high-dimensional data. The lack of a concrete algorithm makes it difficult to assess the practical viability of the theoretical framework.
- Limited Practical Contribution: As the paper is theoretical, it lacks direct benchmarking that could contextualize it within existing explainability methods in machine learning. The absence of comparisons with established methods for self-supervised learning interpretability makes it hard to gauge the relative advantages or disadvantages of the proposed approach. Without such comparisons, it is unclear whether the proposed theory offers a significant improvement over existing methods or provides unique insights.

### Questions
Please see weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new mathematical theory that leverages spiking functions to encode non-random information as explainable regularities within self-supervised learning. The main aim is to establish a theoretical framework that uses spiking neural functions to differentiate data distributions from random noise. By applying information theory, the authors argue that optimal regularities — learned through the application of spiking functions — can support explainable self-supervised learning.

Approach: The authors construct a mathematical foundation to measure non-randomness by quantifying the information a spiking function can capture when applied to a data distribution. Key theoretical elements include spiking efficiency, conciseness, and ability of functions, with metrics based on the Kullback-Leibler divergence to quantify differences between data and random distributions. The theory is developed further by extending single spiking functions to sequences, allowing for layered information encoding. However, no empirical or implemented models are provided, with only theoretical demonstrations and hypothetical examples discussed.

Contribution: This work's theoretical contributions lie in redefining regularities and explainability in self-supervised learning using spiking functions. It could potentially provide the ICLR community with new perspectives on interpretability in self-supervised systems. However, the lack of empirical results or application contexts limits the practical insights offered by this submission.

### Strengths
- Novelty in Explainability: This paper proposes a unique approach to interpretability in self-supervised learning by defining explainable regularities through spiking functions.
- Mathematical Rigor: The theoretical basis is thorough, relying on information theory principles to quantify spiking efficiency and regularity, potentially valuable for theoretical advances.
- Significance: If validated empirically, this approach could influence future models of explainable self-supervised learning and contribute to theoretical advancements in spiking neural networks and information theory.

### Weaknesses
The paper discussed purely theoretical ideas, that reformulate ML theory, including complexity measures and non-randomness. 
Bold statements need strong evidence to show its usefulness. In my opinion the authors failed to provide such evidence:
I cannot see the necessity for the connex with spiking networks. The f_k are simple indicator functions. The biological motivation is just anecdotal.

The presented non-randomness analysis is nothing else than classification learning, with P and P' being the sources of the two classes. SE is a reformulation of the empirical (in the limit the true) risk. The authors fail to show this IMHO trivial connection therefore overcomplicating the derivations.

There might be an important insight in the idea of an optimal encoder, yet due to the wired presentation as a new theory and due to the lack of any application the goes beyond the extremely simplified toy example, is is impossible for me to see the meaning and impact of that.

The presented research might be a ground start of a residual structural learning theory, if correctly set into the context of structural risk minimization, but it should be presented in a context (decision functions, VC theory, statistical learning theory) that makes it accessible.

The idea of a "size" of a function, given by the number of its parameters is IMHO terribly flawed. The authors might consider VC-dimensions of hypothesis classes, instead of reinventing complexity measures here (problems with that kind of definition of a complexity measure: What about binary parameters, what about parameters that cancel out or are redundant like (a+b)*x, what about regularization effects). Maybe the idea of the "ability" of a function (and its optimization) should be put in relation to structural risk minimization (Vapnik).

I cannot see, why the authors use a KL divergence just for comparing the two ratios p_hat and p_hat' (which are just empirical risks). This artificial construction of a Bernoulli-distribution just seems to overcomplicate things.

If the individual elements of a sequence can be seen as "explanation" is IMHO largely dependent of what one wants to see as an explanation. There is no clear optimization goal defined, therefore it is impossible to judge if for real world examples those sequence elements would count as explanations. There is no discussion about the number K of functions in the sequence. The statement in line 482, that the distribution would determine the number only applies to the most trivial toy-examples and is by itself a complicated problem in the realm of optimal clustering (and clustering is precisely what the functions f_k are aiming for).

### Questions
- In section 3,1, is there a typo in defining the theoretical spiking efficiency and observed spiking efficiency? The KL divergence definitions for both look the same. The difference between the two is understood after seeing equation 2 and 3.
- Could the authors discuss potential applications or contexts in which their theory might be validated empirically?
- What challenges do the authors foresee in implementing this framework for real-world self-supervised learning tasks?
- Has any thought been given to potential benchmarks or comparisons with existing self-supervised explainability models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper describes a mathematical theory for explainable self-supervised learning through spiking functions. This theory seeks to make machine learning models more interpretable then end-to-end learning by defining and detecting non-randomness or regularities in data distributions  as compared to a base random distribution using spiking functions. Thereby also a new complexity measure for the functions is introduced and balanced against the spiking efficiency. The paper outlines how optimizing these functions can capture maximal information concisely, thus achieving an explainable, self-supervised learning system.

### Strengths
The definitions and derivation of the mathematical concepts is in itself correct. The mathematical arguments are clear and the formalisation is correct (I did not check the derivations of the appendix).

The author clearly show their understanding of the mathematics of the tools they use and the ability to formalize correctly. The paper is in itself written in a clear language style and explains the newly introduced concepts in an understandable way.

### Weaknesses
1. Though I appreciate a fully theoretical paper, this one stands out because the authors propose a new mechanism for explainable self-supervised learning through spiking functions—yet it lacks the essential empirical validation to support its claims. Without any concrete examples, simulations, or experimental evaluations, it is hard to assess the practical utility of the proposed framework, especially considering the complexity and abstraction of the presented mathematical formalism. The absence of empirical results makes it difficult to ascertain whether the proposed spiking functions can effectively capture meaningful regularities in real-world data, or if the theoretical benefits translate to tangible improvements in explainability. Furthermore, it is unclear how the proposed optimization criteria would perform in practice, and whether they would lead to efficient and stable learning. 

2. Theorems presented in the paper rely on several implicit assumptions, such as bounded data distributions and well-behaved spiking regions. These assumptions are not explicitly stated or discussed. For instance, the mathematical derivations seem to assume that the data distribution is smooth and does not have any abrupt changes or discontinuities. This is a critical assumption that needs to be explicitly stated and justified, as real-world datasets often exhibit complex and irregular distributions. Additionally, the concept of 'well-behaved spiking regions' is not clearly defined, making it difficult to assess the validity of the theoretical results under different conditions.

3. The mathematical formalism is highly abstract, with concepts like spiking efficiency and conciseness not being illustrated with practical examples or visualizations. This makes the ideas difficult to understand and limits accessibility for a broader audience. The lack of concrete examples makes it challenging to grasp the practical implications of these concepts. For instance, it is unclear how one would measure spiking efficiency in a real-world dataset, or how conciseness relates to the interpretability of the learned representations. The absence of visualizations further compounds the issue, making it difficult to develop an intuitive understanding of the proposed framework.

### Questions
The analysis of the multiple function sequences could be acceptable as contribution to a residual learning framework. Yet the authors fail to clearly define corresponding loss functions for those residuals.

The idea of a "size" of a function, given by the number of its parameters is IMHO terribly flawed. The authors might consider VC-dimensions of hypothesis classes, instead of reinventing complexity measures here (problems with that kind of definition of a complexity measure: What about binary parameters, what about parameters that cancel out or are redundant like (a+b)*x, what about regularization effects). Maybe the idea of the "ability" of a function (and its optimization) should be put in relation to structural risk minimization (Vapnik).

I cannot see, why the authors use a KL divergence just for comparing the two ratios p_hat and p_hat' (which are just empirical risks). This artificial construction of a Bernoulli-distribution just seems to overcomplicate things.

If the individual elements of a sequence can be seen as "explanation" is IMHO largely dependent of what one wants to see as an explanation. There is no clear optimization goal defined, therefore it is impossible to judge if for real world examples those sequence elements would count as explanations. There is no discussion about the number K of functions in the sequence. The statement in line 482, that the distribution would determine the number only applies to the most trivial toy-examples and is by itself a complicated problem in the realm of optimal clustering (and clustering is precisely what the functions f_k are aiming for).

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a theoretical framework for explainable self-supervised learning through the use of spiking functions. The key objective is to explicitly capture regularities in data distributions to address the lack of interpretability in traditional deep learning. The authors present a new way to define and quantify non-randomness and regularities using information theory, and they propose optimization criteria for spiking functions to enhance explainability.

### Strengths
1. The introduction of spiking functions as a mechanism to formalize and quantify non-randomness in data is an interesting and novel contribution. The connection made between spiking neural networks (SNNs), information theory, and explainability could pave the way for a more formal approach to interpretable machine learning.
2. The paper develops a rigorous mathematical formalism for explaining the relationship between spiking functions, information capture, and conciseness. This formalism could potentially add value to how explainability is approached, particularly in self-supervised settings.

### Weaknesses
It seems that Definition 2 is ambiguous. In Definition 2, authors define the size of a function $f$ as the number of adjustable parameters in $f$, where adjustable parameters are parameters that can be adjusted without changing the computational complexity of $f$.
1. It is hard (or at least not direct) to define which parameters can be adjusted without changing the computational complexity in mathematics. The first reason is that the current definition considers computational complexity, and the measurement of computational complexity is not clearly defined at least in the current version. The second reason is that a complicated function may have different expressions, and different expressions may lead to different computational complexities. Although we can define the computational complexity as the minimum one of all possible expressions, I think that such a definition is hard to calculate in practice since it is hard to traverse all possible expressions (which may be infinite). Based on these reasons, I think that Definition 2 is not rigorous.
2. There are many existing measurements of the complexity of function classes, such as the Vapnik–Chervonenkis dimension. However, the Vapnik–Chervonenkis dimension is defined for a function class, while Definition 2 considers the size of a single function. Is it possible to modify the proposed theory such that the Vapnik–Chervonenkis dimension can be used to measure the function complexity? The introduction of the Vapnik–Chervonenkis dimension may make the proposed theory more rigorous.

Authors consider Lebesgue measure throughout the paper but the presentation and proofs of theories can be more rigorous.
1. In Lemma 1, the set $S$ needs further conditions. The current version only requires bounded $S$, thus it does not exclude the case of immeasurable $S$. If $S$ is not Lebesgue measurable, then it is easy to construct a counterexample of Lemma 1.
2. The proof of Lemma 1 requires $S$ to be an open set, which is not mentioned in Lemma 1. In the proof, the authors claim that the ball $B(X,\delta)$, where $X$ satisfies $f(X) > 0$, is a subset of $S_f$. However, this only holds when $S$ is an open set, and $\delta$ is smaller than the distance between $X$ and the boundary of the open set $S$.

There is a minor mistake in line 313. In line 313, "for any function" should be "for some function" since $S_f$ consists of vectors that make at least one function in $f$ to spike, as explained in line 314.

### Questions
1. How would the authors implement these spiking functions in practice, and how would the spiking efficiency behave in an actual dataset? Including even simple experiments on synthetic data could significantly strengthen the validity of the claims.

2. There are several implicit assumptions that are critical to the proofs but are not explicitly discussed in the paper. For instance, Theorem 1 assumes that the probability density of the data distribution g(X) is uniformly bounded. In real-world datasets, distributions can have extreme values or unbounded regions. How do the authors envision handling situations where g(X) is not bounded or when the data density is highly irregular?

3. The paper introduces concepts like spiking efficiency, conciseness, and ability, but these terms remain abstract without concrete examples. It would be helpful to include examples or visualizations to illustrate how these quantities behave in a simple scenario. For instance, could the authors show what the spiking efficiency looks like in a 2D synthetic dataset?

4. Could the authors clarify the practical significance of these bounds? For example, do these bounds provide any guidance for selecting or designing spiking functions ? The implications of these results are not sufficiently discussed, and more clarity on this point would be beneficial.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel theory to describe regularities in a data probability distribution.
1. Firstly, the authors define the spiking frequency of a function $f$ on a data set by calculating the ratio of points in the data set satisfying $f(x) > 0$.
2. Secondly, authors define the spiking efficiency of a function $f$ with respect to a data distribution $P$ and a random distribution $P'$ by the Kullback-Leibler divergence of the spiking distribution of $f$ on $P$ over that of $P'$.
3. Thirdly, the ability of $f$ is its spiking efficiency divided by its size.
4. Based on these concepts, the regularities in data are captured by the functions with the highest ability. Such functions can capture the largest amount of information from the data distribution and encode the captured information into the smallest amount of information.

### Strengths
1. The proposed theories aim to explain what are regularities. This is an important problem in self-supervised learning (and I believe it is also important in machine learning and mathematics) since it can help us understand what is learned by complicated models. To the best of my knowledge, existing works about explainable machine learning mainly focus on empirical experiments and visualization rather than rigorous theories.
2. The proposed theories are novel, explained in detail, and supported by sufficient examples.

### Weaknesses
It seems that Definition 2 is ambiguous. In Definition 2, authors define the size of a function $f$ as the number of adjustable parameters in $f$, where adjustable parameters are parameters that can be adjusted without changing the computational complexity of $f$.
1. It is hard (or at least not direct) to define which parameters can be adjusted without changing the computational complexity in mathematics. The first reason is that the current definition considers computational complexity, and the measurement of computational complexity is not clearly defined at least in the current version. The second reason is that a complicated function may have different expressions, and different expressions may lead to different computational complexities. Although we can define the computational complexity as the minimum one of all possible expressions, I think that such a definition is hard to calculate in practice since it is hard to traverse all possible expressions (which may be infinite). Based on these reasons, I think that Definition 2 is not rigorous.
2. There are many existing measurements of the complexity of function classes, such as the Vapnik–Chervonenkis dimension. However, the Vapnik–Chervonenkis dimension is defined for a function class, while Definition 2 considers the size of a single function. Is it possible to modify the proposed theory such that the Vapnik–Chervonenkis dimension can be used to measure the function complexity? The introduction of the Vapnik–Chervonenkis dimension may make the proposed theory more rigorous.

Authors consider Lebesgue measure throughout the paper but the presentation and proofs of theories can be more rigorous.
1. In Lemma 1, the set $S$ needs further conditions. The current version only requires bounded $S$, thus it does not exclude the case of immeasurable $S$. If $S$ is not Lebesgue measurable, then it is easy to construct a counterexample of Lemma 1.
2. The proof of Lemma 1 requires $S$ to be an open set, which is not mentioned in Lemma 1. In the proof, the authors claim that the ball $B(X,\delta)$, where $X$ satisfies $f(X) > 0$, is a subset of $S_f$. However, this only holds when $S$ is an open set, and $\delta$ is smaller than the distance between $X$ and the boundary of the open set $S$.

There is a minor mistake in line 313. In line 313, "for any function" should be "for some function" since $S_f$ consists of vectors that make at least one function in $f$ to spike, as explained in line 314.

### Questions
See weakness. My main concern is the first weakness.

### Soundness
2

### Presentation
4

### Contribution
4
