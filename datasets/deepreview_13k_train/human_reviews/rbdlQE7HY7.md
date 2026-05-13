# Uniform Wrappers: Bridging Concave to Quadratizable Functions in Online Optimization

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
This paper presents novel contributions to the field of online optimization, particularly focusing on the adaptation of algorithms from concave optimization to more challenging classes of functions. Key contributions include the introduction of uniform wrappers, establishing a vital link between upper-quadratizable functions and algorithmic conversions. Through this framework, the paper demonstrates superior regret guarantees for various classes of up-concave functions under zeroth-order feedback. Furthermore, the paper extends zeroth-order online algorithms to bandit feedback counterparts and offline counterparts, achieving a notable improvement in regret/sample complexity compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides an in-depth exploration of advanced techniques for online optimization, particularly focusing on transitioning algorithms from concave optimization to more complex classes. This work contributes by introducing "uniform wrappers," a framework for adapting standard online convex optimization (OCO) algorithms to handle non-convex, quadratizable functions while preserving sublinear regret bounds.

### Strengths
- The paper considers a challenging and important problem in online optimization, namely, how to extend algorithms from the convex to the non-convex setting.
- The core idea of uniform wrappers allows traditional OCO algorithms to handle quadratizable functions by converting feedback and actions within a structured wrapper framework. This wrapper effectively bridges the gap between simpler convex optimization and more complex quadratizable function classes. Moreover, this framework is general and can be applied to a wide range of function classes.
- This paper obtains or matches the state of the art algorithm in several online optimization settings considered. For classes such as weakly DR-submodular functions under
zeroth order feedback, the framework provides superior regret guarantees, surpassing prior results in the field.

### Weaknesses
 - The paper is quite dense and difficult to follow. The theoretical framework is complex, with multiple layers of definitions (e.g., quadratizability, up-super-gradients, and uniform wrappers) that might limit accessibility for a broader audience. While this complexity is necessary to cover a broad class of functions, it risks making the approach difficult to understand for readers unfamiliar with the field. The presentation could be improved by providing more intuition and examples to help readers understand the core ideas and contributions. 
- The paper cites and builds upon prior work in DR-submodular and up-concave optimization (e.g., Pedramfar & Aggarwal, 2024), but it lacks a clear differentiation of its unique contributions. The proposed framework appears to be an incremental improvement rather than a groundbreaking advance. I suggest the authors to clarify the novelty and significance of their work compared to existing methods in the field.
- I am quite confused about the necessity of the uniform wrappers. The paper does not provide a clear motivation for why uniform wrappers are needed or how they improve upon existing methods. A more detailed discussion on the limitations of current approaches and how uniform wrappers address these limitations would be beneficial.

### Questions
- I wonder the significance of the upper quadratizable/linear functions. Why are these functions important, and how do they relate to real-world applications? It would be helpful to provide more context on the motivation behind this class of functions and why they are relevant in practice.
- What are the conditions under which uniform wrappers can be applied? Are there any limitations that restrict the applicability of this framework to certain function classes or settings?
- I am interested in the regret defined in Line 203. Can the results reduce to the dynamic regret and adaptive regret? If so, how do they compare to existing methods in these settings?

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
3

### Summary
This work gives a framework that reduces the problem of online optimization with quadratizable functions (Pedramar & Aggarwal, 2024a) to OCO. This results in state-of-the-art guarantees in several settings and improvements in some others.

### Strengths
- The framework provides improvements in the state-of-the-art regret bounds in several settings.
- The presentation is sufficiently clear.

### Weaknesses
Although there might be some small improvements in the analysis of Pedramar & Aggarwal (2024a), the framework appears to be nearly identical to that in Pedramar & Aggarwal (2024a). Nearly every technical result in the paper is due to Pedramar & Aggarwal (2024a), e.g. Lemma 1, Lemma 2, Lemma 3, ... I do not see any novelty in techniques or approach. The core idea of reducing online optimization with quadratizable functions to online convex optimization (OCO) is already present in Pedramar & Aggarwal (2024a). While the current work claims to generalize the results of Pedramar & Aggarwal (2024a), the specific improvements seem marginal. The paper essentially re-derives existing results within a slightly broader framework, but the underlying methodology and analysis remain largely unchanged. The claimed generalization does not introduce significant new technical challenges or insights, and the practical implications of this generalization are not clearly demonstrated.

### Questions
What is the technical novelty with respect to Pedramar & Aggarwal (2024a)?

### Soundness
3

### Presentation
3

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
This article develops a general framework for transferring the algorithms and their regret guarantees from online convex/concave optimization to online quadratizable optimization. Within this framework, the authors employ a variant of Follow-the-Regularized-Leader (FTRL) from [1] to enhance the regret guarantees for several classes of weakly DR-submodular functions under zeroth-order and bandit feedback.

[1] Ankan Saha and Ambuj Tewari. Improved regret guarantees for online smooth convex optimization with bandit feedback. In Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics, pp. 636–642. JMLR Workshop and Conference Proceedings, 2011.”

### Strengths
1.The authors have improved the regret bound for online optimization problems across three function classes under zeroth-order feedback, from $\tilde{O}(T^{3/4})$ to $\tilde{O}(T^{2/3})$.

2.The authors have enhanced the regret bound for online optimization problems across three function classes under bandit feedback, improving it from $\tilde{O}(T^{4/5})$ to $\tilde{O}(T^{3/4})$.

### Weaknesses
1.The technical contribution is quite limited. Although the upper quadratizable function is highly non-convex, many previous articles, especially [2], have shown that this upper quadratizable function satisfies a first-order variational inequality similar to that of a convex function (Lemma 1, 2, 3). Therefore, we can consider the upper quadratizable function as a special type of "quasi-concave" function. Consequently, it is quite natural for this paper to use a variant of FTRL [1] to improve the regret bounds in zero-order and bandit scenarios.

2.This paper lacks an in-depth discussion of the applications of the upper quadratizable function and a practical evaluation of the newly introduced algorithms. This statement may make readers feel that the authors are merely exploring a new function without clarifying its relevance or impact on the machine learning community.

3.From the full text and Definition 2, it appears that the primary purpose of introducing the upper quadratizable function is to study $\gamma$-weakly continuous DR-submodular functions. So, why not focus on "$\gamma$-weakly continuous DR-submodular functions" as the main subject of the paper? Can the authors provide examples of applications where the target function is upper quadratizable but not $\gamma$-weakly continuous DR-submodular functions?

### Questions
1. Could the authors provide a detailed personal perspective on how their technical contributions differ from those in references [1] and [2]?
2. Could you provide a detailed explanation of the applications of upper quadratizable functions and conduct an empirical evaluation of the newly proposed algorithms?  
3. Can the authors provide examples of applications where the target function is upper quadratizable but not $\gamma$-weakly continuous DR-submodular functions? 
4. Why not focus on "$\gamma$-weakly continuous DR-submodular functions" as the main subject of the paper?

### Soundness
3

### Presentation
3

### Contribution
2
