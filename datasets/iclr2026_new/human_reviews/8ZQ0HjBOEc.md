## Human Reviewer 1

### Summary
This paper studies the NTK regime of neural networks in the limit of increasing depth $L \to \infty$, i.e., the regime obtained by first taking the infinite-width limit $n \to \infty$ and then the infinite-depth limit $L \to \infty$. The analysis is restricted to the *ordered phase*, where the initialization variance $W_{ij} \sim \mathcal{N}(0, 1/n)$ leads to vanishing gradients as depth increases. In this setting, the NTK $\Theta(X,X)$ approaches a singular matrix as $L \to \infty$. The authors study the behavior of the *mean predictor*, defined as $\Theta(x, X)\Theta^{-1}(X, X)$, which corresponds to the expected kernel regression solution under the NTK. The main result appears to be a proof that, despite the convergence of $\Theta(X,X)$ to a singular matrix in this vanishing-gradient regime, the mean predictor itself admits a well-defined limiting form.

### Strengths
- **Relevance:** In general, scaling limits of neural networks beyond the standard infinite-width regime are in important and relevant topic in deep learning theory, and the paper aims to advance this line of work.

### Weaknesses
- **Lack of novelty:**  The presented results have appeared in various forms in prior work. For instance, Xiao et al. (2020) [1] show the existence of a well-defined limit for the mean predictor in Eq. (16). Related results and discussions of the limitations of the "$n \to \infty$ then $L \to \infty$" limit also appear e.g. in Seleznova & Kutyniok (2022) [2] and Hayou et al. (2022) [3]. This regime has long been considered trivial, as the covariance between distinct inputs converges to one, leading to effectivelly constant predictions for any input. Moreover, it seems like the paper uses unnecessarily complex machinery of rough differential equations to prove convergence of the mean predictor, which is a result that can be obtained directly through standard linear-algebraic arguments.

- **Restricted initialization setting:**  The analysis considers only the initialization $W_{ij} \sim \mathcal{N}(0, 1/n)$, corresponding to the *ordered phase*, in which gradients vanish with depth. Prior works cited above studied a broader class of initializations and show that the behavior of the "$n \to \infty$ then $L \to \infty$" regime depends critically on this choice. The present paper does not acknowledge this and, in fact, never explicitly defines the initialization variance.

- **Lack of relevant literature discussion:**  Existing work on the regime $n \to \infty$, $L \to \infty$, $L/n \to 0$ is not discussed. The paper does not reference or contrast its results with any prior analyses of this limit.

- **Misrepresentation of prior results:**  The paper incorrectly summarizes the results of Hanin & Nica (2019) [4], which concern the *double-scaling* regime where $L, n \to \infty$ with $L/n \to \lambda > 0$. The text repeatedly claims that Hanin & Nica study the case where "the ratio of depth to width is unbounded" or where $L \gg n$, which is incorrect.

- **Lack of clarity and technical precision:** There are multiple problems with clarity and technical precision in the text. A few examples are:
  - The initialization distribution is never specified, so the source of randomness in the concentration results is unclear.  
  - "Case a" (lines 221–222) states that "if data points lie on a unit sphere, the NTK is invertible." This is trivially false, with a counterexample of taking the same point on a sphere multiple times. Moreover, the text references "Proposition 2 of Jacot et al (2018)" here. However, Jacot et al (2018) [5] does not contain Preposition 2.
  - "Case c" (lines 227–228) refers to "stereographic projection from $\mathbb{R}^{n_0}$ to $\mathbb{S}^{n_0-1}$." Such a projection does not exist.

## References

[1] Xiao, L., Pennington, J., & Schoenholz, S. (2020). *Disentangling trainability and generalization in deep neural networks.* ICML.  
[2] Seleznova, M., & Kutyniok, G. (2022). *Analyzing finite neural networks: Can we trust neural tangent kernel theory?* MSML.  
[3] Hayou, S., Doucet, A., & Rousseau, J. (2022). *The curse of depth in kernel regime.* NeurIPS Workshop.  
[4] Hanin, B., & Nica, M. (2020). *Finite depth and width corrections to the neural tangent kernel.* ICLR.  
[5] Jacot, A., Gabriel, F., & Hongler, C. (2018). *Neural tangent kernel: Convergence and generalization in neural networks.* NeurIPS.

### Questions
- What is meant by “stereographic projection from $\mathbb{R}^{n_0}$ to $\mathbb{S}^{n_0-1}$” mentioned several times in the paper?
- Why is it necessary to rely on rough differential equations to obtain the main result?
- How do the presented results differ from or improve upon the mentioned existing work?

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper analyzes the effect of increasing depth on the Neural Tangent Kernel (NTK) for infinitely wide, overparameterized ReLU networks. While prior work established that wide networks behave like kernel methods, the role of depth remains less understood. The authors prove that as depth increases (with depth growing slower than width), the normalized NTK converges to a matrix of ones, and the kernel regression solution approaches a fixed limit for data on the sphere. They characterize this convergence theoretically using rough path theory and identify key properties enabling generalization to other kernels. Experiments show that while some kernel components converge quickly, the full normalized NTK converges extremely slowly.

### Strengths
1. By characterizing the deterministic limit of the NTK and its corresponding solution as depth goes to infinity (under a specific regime), this paper provides novel theoretical insights into the fundamental properties of deep, overparameterized networks, moving beyond the established infinite-width paradigm.

2. The work demonstrates high technical quality through its use of advanced mathematical tools, such as rough path theory, to prove its central convergence theorem (Theorem 3). This sophisticated approach allows the authors to handle the challenging technical obstacle of the kernel matrix becoming singular in the limit, showcasing a rigorous and robust analytical framework.

3. By identifying a list of key properties that lead to the observed limiting behavior, the authors  provide a valuable template for analyzing other kernels and architectures. Furthermore, their empirical evaluation clarifies the practical implications, notably highlighting the extremely slow convergence rate of the normalized NTK, which is a crucial observation for connecting theory to practice.

### Weaknesses
1. The empirical validation is minimal, using only synthetic, uniformly distributed data on a sphere for very shallow depths ($L=1$ to $10$). This is insufficient to support the theoretical claim of "extremely slow" convergence, as the chosen depth range is too small to visually demonstrate the asymptotic behavior. To be more compelling, experiments should include benchmarks on real-world datasets and probe much larger depths to empirically quantify the convergence rate and its impact on test performance.

2. While the paper successfully characterizes the existence of a limiting solution, it provides little discussion on what this limit implies for generalization. Does convergence to a fixed limit imply a loss of representation power or a tendency towards simpler functions? A deeper analysis connecting the specific form of the limiting kernel solution to known generalization behaviors would significantly strengthen the significance of the theoretical results.

### Questions
1. Your theoretical results establish an "extremely slow" convergence of the normalized NTK to 1, yet your empirical results only show depths up to $L=10$. Could you provide a quantitative estimate of the depth $L$ required for the kernel solution $\kappa_x\kappa^{-1}$ to be within a small $\epsilon$ of its limit on, for instance CIFAR-10? This would greatly help in assessing the practical relevance of your limit for modern deep architectures.

2. Your analysis crucially relies on the depth growing slower than the width to maintain a deterministic NTK. Is this a fundamental requirement for your rough path theory technique to hold, or is it an artifact of the current proof? Could you comment on the feasibility and potential challenges of extending your analysis to the stochastic NTK regime described in Hanin & Nica (2020)?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper examines the role of network depth through the lens of Neural Tangent Kernel (NTK) theory. Within this framework, this paper shows that the normalized NTK converges to the all-ones matrix as depth increases for data on the sphere (with extensions via projection for more general data), under the assumption that depth grows more slowly than width. Empirical evidence illustrates that this convergence is very slow.

### Strengths
The background of NTK theory is clearly presented. Theorems appear to be rigorously argued, and the experiments are conducted to validate them.

### Weaknesses
Although the paper considers a different width and depth scaling than Hanin & Nica (2020), I do not think novelty of this result meets the bar for acceptance at this venue. The scope is limited to CNNs, omitting Transformers, now widely used in practice. 

The experiments explore depths up to only 10 layers, which is not particularly deep by modern standards.

### Questions
If I understand correctly, normalized NTK converge to the all-ones matrix and if so, it would become a deterministic kernel independent of the input data. Is this due to the normalization? And does it imply that the neural network just reduces to a kernel method with a trivial kernel?

Could the authors emphasize the key technical difficulties in the proof of Theorem 3 and explain how they overcame them in plain language?

Missing reference: Please include and discuss “Neural Tangent Kernel Analysis of Deep Narrow Neural Networks” (Lee et al., 2022) in the Related Work section.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper provides a theoretical and empirical analysis of how increasing depth affects the Neural Tangent Kernel (NTK) in infinitely wide, fully-connected ReLU networks. The authors show that as depth $L \to \infty$, the normalized limiting NTK $\bar{\Theta}^{(L)}$ converges to a matrix of ones, implying that all inputs become perfectly correlated in the infinite-depth limit. Despite this kernel degeneracy, the closed-form NTK predictor $f(x) = f_0(x) + \Theta_x^{(L)} [\Theta^{(L)}]^{-1} (y - y_0)$ converges to a finite, well-defined limit due to a cancellation effect between the numerator and denominator terms. Theoretical results are supported with toy experiments that visualize convergence rates and verify monotonic correlation growth.  
Overall, the paper clarifies the limiting behavior of NTKs with depth and its implications for overparameterized models trained in the kernel regime.

### Strengths
-- Rigorous theoretical grounding, with a clean progression from correlation dynamics to kernel limit to predictor stability.

-- Extends NTK theory by isolating the effect of depth, complementing prior focus on width.

--  Elegant use of normalization and rough differential equations to handle singular kernel limits.

-- Empirical plots and numerical validation reinforce theoretical claims (Fig. 1, lines L432--L446).

-- Results implications: very deep, infinitely wide ReLU nets become less expressive, converging to constant mappings.

### Weaknesses
-- Experimental section is minimal; only small-scale synthetic tests are shown. A broader empirical sweep would strengthen conclusions.

-- Intuition behind the RDE-based boundedness could be expanded—currently highly technical and somewhat opaque to non-specialists.

-- The convergence rate discussion could quantify how “extremely slow” the approach to 1 is (as noted in L446--L454) using asymptotic bounds.

-- The experimental section and conclusions feel somewhat underdeveloped, leaving the reader wishing for more explicit explanations or additional insights into the implications and experimental findings as per ICLR standards.

### Questions
-- Can the authors clarify how the convergence rate of $\phi^{(L)} \to 1$ depends on activation nonlinearity—e.g., would smoother activations yield slower or faster kernel collapse?

-- Since the NTK converges to a constant kernel, does this imply that in the deep infinite-width limit, gradient descent loses any data-dependent inductive bias?

-- Minor comments: 1) L051, L052: Proposition 4 and, Theorem 3 do not have hyperlink (which makes it easy to naviagte) and also does not give much insight as what the actually contributions are by just reading the contributing section, can be written better. 2) same issue with L218, no hyperlinks, poorly written ==>
This, in turn, allow us to aim at characterizing the output of such neural network,as done in the rest of the section. Indeed, from Proposition 2 and Proposition 2 from Jacotet al. (2018), we can immediately observe a few facts regarding the input data:

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3