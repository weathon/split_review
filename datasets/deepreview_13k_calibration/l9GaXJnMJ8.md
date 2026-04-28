# Fast Stochastic Kernel Approximation by Dual Wasserstein Distance Method

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 1, 8

## Abstract
We introduce a generalization of the Wasserstein metric, originally designed for probability measures, to establish a novel distance between probability kernels of Markov systems. We illustrate how this kernel metric may serve as the foundation for an efficient approximation technique, enabling the replacement of the original system's kernel with a kernel with a discrete support of limited cardinality.
To facilitate practical implementation, we present a specialized dual algorithm capable of constructing these approximate kernels quickly and efficiently, without requiring computationally expensive matrix operations. Finally, we demonstrate the effectiveness of our method through several illustrative examples, showcasing its utility in diverse practical scenarios, including dynamic risk estimation. This advancement offers new possibilities for the streamlined analysis and manipulation of Markov systems represented by kernels.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new kernel based on Wasserstein distance for Markov systems. More specifically, the author proposes a Wasserstein distance between two kernels $Q$ and $\tilde{Q}$ (definition 2.1). Then, the computationally efficient algorithm is provided and the efficacy of the proposed method is demonstrated in numerical problems.

The approach seems to be new. However, it has several problems needed to be addressed further. Moreover, the experimental section can be further expanded

### Strengths
1. The problem in this paper is interesting.

### Weaknesses
1. The paper is generally poorly written and contains numerous typos in both the explanations and equations.
2. The experimental section could benefit from additional elaboration and expansion.
3. The definition 2.1 is very confusing. More specifically, it explains $Q(\dot | x)$ is a kernel that transforms $x$ to the probability measure. It seems $Q(\dot | x)$ is a probability density function estimated and it does not look like a kernel functions. Could you please elaborate this part?
4. Equation (9) presents a variation of the Wasserstein barycenter problem. However, the manuscript lacks a comprehensive discussion of the Wasserstein barycenter, and it would be beneficial to explicitly address this concept. Additionally, a comparison of the proposed method with relevant baselines is warranted.

### Questions
1. The definition 2.1 is very confusing. More specifically, it explains $Q(\dot | x)$ is a kernel that transforms $x$ to the probability measure. It seems $Q(\dot | x)$ is a probability density function estimated and it does not look like a kernel functions. Could you please elaborate this part?
2. Equation (9) presents a variation of the Wasserstein barycenter problem. However, the manuscript lacks a comprehensive discussion of the Wasserstein barycenter, and it would be beneficial to explicitly address this concept. Additionally, a comparison of the proposed method with relevant baselines is warranted.
3. Numerous typographical errors are present in the manuscript. For instance, on page 1, there is a repeated "the the." Equation (6) is lacking the variable $p," and these issues need prompt correction for the manuscript to maintain clarity and accuracy.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a generalized Wasserstein distance to quantify the difference between transition kernels of Markov system. The authors also propose an optimization algorithm that approximates system true dynamics efficiently. The effectiveness of this approach is validated in a simple numerical example.

### Strengths
- The problem itself seems to be an interesting topic. The modeling formulation seems sound. The problem has clear applications, such as optimal stopping problem as studied in Section 4.

### Weaknesses
I am regret to tell the authors that I must recommend rejection of this paper. The overall writing of this paper  remains to be improved. Besides, for the theoretical part, 
- The authors solve the mixed-integer linear optimization formulation (11) by relaxing the boolean variable constraint $\gamma\in\{0,1\}$ with $\gamma\in[0,1]$. However, such a relaxation will usually induce large optimization error. Besides, the authors claim that "However, for large dimensions, the gap is minimal, as our experience demonstrates." When I look at the numerical results in Table 2, the optimization gap actually increases when the data dimension increases. Therefore, I think Section 3 does not present a reasonable approach for optimization. 
- Several citations are missing. For example, in the last paragraph of Section 2, the authors introduced particle selection problem using the Wasserstein distance but did not include a citation. It is confusing to tell the specific application or problem formulation the authors are referring to.
- Numerical study is too stylized.

### Questions
N/A

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper has a few contributions. First the authors introduce a way to measure distances between kernels via the Wasserstein distance. This distance is then leveraged in a sampling scheme of a Markov process.

### Strengths
The authors do a good job of incrementally introducing the complexity of the problem. Some of the problem statements are quite dense but they are motivated and presented well. The paper thus tells a full story with reasonable conclusions.

The distance for kernels is fairly novel (although it really is just an expected Wasserstein distance) but the authors treat it as a tool without examining its efficacy. Perhaps this is a tangent but demonstrating properties of this distance would have been great. This distance is a strength though because of the strength inherent to Wasserstein distance. It could perhaps be well applied in future works.


Minor comment: the conclusions start with a typo "W"

### Weaknesses
The notation can be hard to follow due to all the indices and characters, admittedly this could be unavoidable though. One thing which is avoidable though is switching to using "j" as iterations.

For definition 2.1 it would be beneficial to the authors to make it clear this is a contribution

I understand this a limited space issue but i wish the experimental results were more involved. I do see there is more results in the appendix, though. The experimental results are a bit underwhelming given the very nice theory presented earlier.

### Questions
In (11a) d_{sik} is defined as the distance between x and zeta, I am unclear as to why it's zeta and not z, any elaboration would be appreciated.

Since the authors propose solving their optimization problem via the dual rather than the primal, my question would normally involve the gap; the authors claim in 3.1 that for large dimensions the gap is minimal, could the authors elaborate on this?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
