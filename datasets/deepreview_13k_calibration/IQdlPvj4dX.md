# On the Local Complexity of Linear Regions in Deep ReLU Networks

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 6, 6, 6, 5

## Abstract
We define the $\textit{local complexity}$ of a neural network with continuous piecewise linear activations as a measure of the density of linear regions over an input data distribution. We show theoretically that ReLU networks that learn low-dimensional feature representations have a lower local complexity. This allows us to connect recent empirical observations on feature learning at the level of the weight matrices with concrete properties of the learned functions. In particular, we show that the local complexity serves as an upper bound on the total variation of the function over the input data distribution and thus that feature learning can be related to adversarial robustness. Lastly, we consider how optimization drives ReLU networks towards solutions with lower local complexity. Overall, this work contributes a theoretical framework towards relating geometric properties of ReLU networks to different aspects of learning such as feature learning and representation cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a complexity measure of a neural network with ReLU activations, called local complexity.
Local complexity measures the density of linear regions in the neighbourhood of an input point.
Authors provide theoretical upper and lower bounds with respect to two other quantities.
First is local rank, also introduced by the authors, which connects to representation learning.
Second is total variation, which relates to robustness properties of the network.

Theoretical results are complemented by numerical experiments, where links between local complexity and local rank / total variation are studied.

### Strengths
Authors propose a clear mathematical quantity to compute local complexity of the network.
Furthermore, authors describe connections of local complexity of the network to representation learning and its robustness from theoretical viewpoint. Proofs are easy to follow, with some simple examples given to provide intuition.

Experimental results with visualization of the proposed complexity measure show that it captures the density of non-linearities. Authors are also clear with the possible limitations of the connection between metrics, by adding experimental results without clear correlations between, e.g., total variation and local complexity.

### Weaknesses
My main concern is that there is little discussion on the sharpness of the theoretical bounds. For example, lower bounds in Theorems 5,6 depend on $B$, number of active neurons, but estimates for $B$ are only given at the initialisation, not after training. To better understand the theoretical bounds, one could plot them empirically. The fact that bounds might be loose can also be seen at the experiments, where the connection between the quantities (eg local complexity and total variation) is not clear, as the authors point out in Appendix C.

Also, as authors mention themselves, proof of Theorem 2 essentially directly follows from (Hanin & Rolnick 2019a).

My concern regarding the sharpness of the bounds extends to the relationship between local complexity ($LC$) and the lower bound $A = \frac{TV L c^{\eta}_{\mathrm{bias}}}{\max \lVert W_1 \ldots W_L \rVert}$ introduced in Appendix B.4. The choice of $\eta = 1$ seems arbitrary, as $LC$ is independent of $\eta$ while $c^{\eta}_{\mathrm{bias}}$ decreases with increasing $\eta$. This implies that by choosing a sufficiently large $\eta$, one could make $A$ arbitrarily small, potentially smaller than $LC$, which would render the bound meaningless. Specifically, given that $c^{\eta}_{\mathrm{bias}}$ is an exponential term, even small increases in $\eta$ can drastically reduce the value of $A$. This raises questions about the practical utility of the bound and the rationale behind setting $\eta = 1$ without a clear justification. Furthermore, the effect of $B$ after training on the lower bounds remains unclear. While the authors provide initial estimates for $B$, its behavior during and after training is not discussed, which is crucial for understanding the tightness of the bounds.

### Questions
Is it possible to plot / show estimates of the bounds of Theorems 4,5? 

What is $R(\mathcal{N}\_{\theta})$ in Proposition 7? According to definition in line 398-399, one always trivially has $R(\mathcal{N}\_{\theta}) = 0$.

Discussion in lines 200-210 is not very clear. For example, why noise is only added to biases, and not to the input / weight matrices?

Line 386: "our theoretical result involves several interdependent components": could you clarify this sentence?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work defines the local complexity of a ReLU network and demonstrates the link between the complexity of linear regions and adversarial robustness. The local complexity is shown (roughly) equal to the expected input-gradient norm of neurons. Adversarial robustness relates to the total variation of a network, which is defined as the input-gradient norm of the network and thus can be linked to the local complexity. Empirically, it has been observed that the adversarial robustness shows a sharp increase during training when the ReLU network becomes geometrically simple in the input space (e.g., fewer linear regions). The authors confirm by numerical experiments that the sharp increase in adversarial robustness correlates with local complexity and rank.

### Strengths
- This study presents a rigorous connection between the geometric characteristics of the ReLU network and adversarial robustness. 
- The theoretical analysis links local complexity to the local rank, which relates to the input-space geometry of the ReLU network, and to the total variation of the ReLU network, which relates to the adversarial robustness, thereby linking the linear regions and adversarial robustness.

### Weaknesses
I raise the following as the major weaknesses of this work. 
1. The analysis of the time evolution of the local complexity and adversarial robustness is limited. 
2. The tightness of the bound is not discussed by theory or experiments.

I elaborate on the weaknesses below. 

1. The time evolution analysis 
As given in the introduction and related work, this study is interested in the observation of the sharp increase in adversarial robustness and more straightforward linear regions in the late stage of the training.
The authors provide the link between the robustness and the simplicity of the linear region but do not show their time evolution. Thus, no comprehensive answer to the motivating observation is provided. 
Proposition 8 and Corollary 8 give upper bounds for the local complexity in the rich regime, but there is no clarification about the kernel regime. Is there any lower bound for the local complexity in the kernel regime? Specifically, how does the local complexity evolve during training in the kernel regime, and how does this evolution relate to the observed changes in adversarial robustness? The paper lacks a detailed analysis of the dynamics of local complexity throughout the training process, particularly in the context of the kernel regime where parameters remain close to their initial values. This makes it difficult to fully understand the connection between the theoretical bounds and the empirical observations of increased robustness.

2. The tightness of the bound. 
This paper provides several bounds, such as Eq. (11), (12), and (13), but it is not clear how tight these bounds are. It may be theoretically hard, but at least it is doable to show it by comparing theoretical and empirical plots. For example, the bounds could be evaluated on a range of network architectures and training scenarios to assess their practical relevance. Without such an analysis, it is difficult to determine whether the bounds are meaningful or simply loose upper limits that do not provide much insight into the actual behavior of the network. The paper should include a more thorough investigation of the tightness of the derived bounds, potentially through a combination of theoretical analysis and empirical validation.

***Minor comments***
- [Below Eq. 17] Appendix 10 was not found (and it seems not the typo of Figure 10).

### Questions
Please answer the two weaknesses raised above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the concept of "local complexity" in deep ReLU networks, defining it as the density of linear regions. This complexity metric relates to representation learning, robustness, and parameter optimization. The authors show that networks that learn lower-dimensional features exhibit lower local complexity, which correlates with reduced total variation and improved robustness.

### Strengths
**Clarity and Quality**

Very well-written and clearly structured paper. The problem has been motivated nicely in the introduction. The related work section is rigorous and clearly details the current results for this problem.


**Theoretical Insights**

By linking local complexity to local rank (feature learning), total variation (robustness), and representation cost (parameter optimization), the authors build a solid theoretical foundation that advances the understanding of ReLU networks’ geometric properties.
Also, they empirically demonstrate such relations by conducting several experiments.

### Weaknesses
 **Originality**

- The authors define the local complexity of networks inspired by (Hanin & Rolnick, 2019b). However, there is no direct comparison between local complexity with complexity defined by (Hanin & Rolnick, 2019b) though definitions are quite similar.  I think this makes the contribution of this paper incremental. To highlight the novelty, it would be better to introduce the main difference.

e.g. Why local complexity is much more appropriate for analyzing local rank, total variation, and representation cost?


**Tightness**

As illustrated in the paper, relations between local complexity and others can be loose (i.e., loose inequality). Nonetheless, if such relations cannot be characterized by complexity defined by (Hanin & Rolnick, 2019b), it would be not a weakness. Thus, as explained above, please 
introduce the main difference.



### Questions
**Non-differentiable**

Though ReLU networks are non-differentiable at $0$, there is no explanation for it. Is every gradient in the paper subderivative?
If so, are several definitions (e.g. total variation) well-defined? For instance, to define total variation using a gradient, the function $f$ should be differentiable. 

**Piecewise linear activation**

The complexity of linear regions in networks using piecewise linear activation is often studied.[Hanin & Rolnick, 2019].
Can we get similar results (thm. 5~ Prop.8) for piecewise linear activation?

---

I am hoping that the authors will provide the clarifications stated therein in the rebuttal phase

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the concept of local complexity in neural networks with piecewise linear activations (specifically ReLU networks) as a measure of the density of linear regions over input data distributions. The authors demonstrate the connections between local complexity and total variation, adversarial robustness, and representation learning. The work contributes a theoretical framework relating geometric properties of ReLU networks, specifically the linear regions, to different aspects of learning.

### Strengths
- The paper presents a mathematical foundation for the definitions and claims of local complexity, including theorems and proofs that enhance the credibility of the findings. 
- The links drawn between local complexity, feature learning, and robustness are timely and relevant, aiming at understanding important aspects of deep learning. 
- Also, the empirical results help support the theoretical claims, providing a practical understanding of the phenomena discussed.

### Weaknesses
- Definitions and Assumptions: The definitions of local complexity, local rank, and good neurons, while mathematically interesting, may be too abstract for practical application. For instance, the reliance on noisy biases in the definition of local complexity, rather than noisy weights, warrants further clarification. A more intuitive explanation of why noisy biases are preferred and whether using noisy weights would lead to similar results would enhance the practical relevance of this concept. This is particularly important as weights can influence the linear regions in a more intricate manner. Additionally, some sections, especially the introduction and theoretical results, are quite dense. Simplifying these concepts and improving the flow would make the paper more accessible to a wider audience.

- Empirical Validation: The paper would benefit from more comprehensive empirical experiments to substantiate the claims regarding local complexity and its relationship with representation learning and adversarial robustness. The assertions concerning adversarial robustness, in particular, might be sensitive to specific training conditions or datasets. For example, conducting experiments across various architectures and datasets would help determine whether the observed phenomena are consistent or specific to certain experimental setups. A broader analysis across different scenarios is crucial to ensure that the findings are not artifacts of particular experimental setups.

- On Practical Implications: The paper does not thoroughly discuss the practical implications of the findings for model design and training. While the theoretical framework is valuable, providing insights into how practitioners can leverage local complexity in their work would significantly enhance the paper's impact. For example, discussing how the insights on local complexity could inform the design of new architectures or training algorithms would be highly beneficial.

### Questions
- Regarding the definition of local complexity: can authors provide more intuitive explanations on why the noisy biases are considered instead of noisy weights? Would the local complexity defined with respect to noisy weights lead to similar subsequent results? This can be a fundamental question as weights can affect the linear regions in a more complex way.

- Regarding Corollary 3: can authors provide more explanations on the defined constants $c_{bias}^\eta$ and $\bar{\xi}_{\eta}$? What is the meaning of these quantities and how are they related to the local complexity? Also, the definition of $\Theta$ seems missing.

- Regarding Theorem 6 and Proposition 7,8: How do these results directly relate to existing theories on model complexity and adversarial robustness? Are there specific studies that the authors see as complementary or contradictory to their findings?

- Regarding the applications: How can practitioners leverage the findings on local complexity in their model design and training processes? What specific recommendations can the authors provide based on their results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors define a novel notion of complexity for functions in relation to some data distribution, they call it Local Complexity. Local Complexity measures the average "density" of discontinuities in the gradient of the function in the input space. For ReLU networks, this translates to the number of linear regions under mild assumptions.

The authors show that Local Complexity is closely related to the notion of Local Rank.

The authors bound a notion of Total Variation of functions by their Local Complexity, thereby getting some proxy for the susceptibility of the function to adversarial examples, and whether "mode collapse" has happened during training.

The authors bound the Local Complexity of neural networks by their representational costs - the minmal norm of weights realizing the same networks, to conclude that weight decay and other forms of norm minimization lead to low Local Complexity and small number of linear regions which explains empirical observations.

Finally, they bound the Local Complexity at later, "rich" phases of training.

### Strengths
The paper presents a new measure of complexity for functions, connects it to different measures that haven been researched, and sheds some light on / provides directions as to how this measure might shed light on interesting open questions in the field.

### Weaknesses
I would like clarifications as of the significance of the notion of Local Rank. Cited works in the "Related Works" section mention roughly similar definitions, and the cited work (Chechik et al.) does not mention the term local rank, and discusses ranks of matrix transformations between gaussian variables, which seems unrelated. Specifically, how does the Local Rank, as defined in this paper, connect to other notions of rank used in the literature, such as the rank of the feature matrix or the rank of weight matrices? A more thorough discussion of these connections would strengthen the paper's contribution.

In the section on Total Variation, the theoretical connection between Local Complexity (LC) and Total Variation (TV) is presented, but it remains unclear how tight this bound is in practice. While the authors acknowledge its limitations, the empirical evidence provided in the appendix is insufficient to fully validate the proposed relationship. The single case of the bound's failure under standard initialization raises concerns about its general applicability. To address this, I suggest providing more extensive empirical evidence across various network architectures, datasets, and initialization schemes. Furthermore, a more rigorous theoretical analysis of the bound's tightness would be beneficial. Additionally, a clearer (not intuition based) explanation for the connection between TV and adversarial robustness is needed. Proposition 6 should be included or expanded upon to demonstrate how lower total variation implies a lack of adversarial examples near data points.

In the section about LC and optimization, clarify the significance of the bound in proposition 8. The dependence on the norm-relations seems to be additive, while the other term seems to be exponentially dependent on the depth. This I think could easily be looser than the bounds in Hanin et al., for example, which as far as I can tell use a measure that upper bounds the LC. A direct comparison to existing bounds, such as those presented in Hanin et al., would help clarify the novelty and significance of the proposed bound. Is this bound vacuous or does it offer a tangible improvement over prior work? As of corollary 9 - there is only one experiment in the appendix, which would enjoy the benefit of plotting the bounding quantity at hand ($\Theta(\log(1/\lambda))$). It would be valuable to visualize this relationship to assess the practical implications of the corollary.

### Questions
1. What is the significance of the notion of Local Rank? There are other notions of rank that are cited to have some results tied to them, but how is the LC connected to those?
2. How does the bound in proposition 8 fare against similar bounds (i.e. of Hanin et al.). I understand the setting is a bit different, and yet it is unclear whether this bound is vacuous or not.
3. What is the empirical\formal connection between Total Variation and Adversarial Robustness? Excluding of the intuitive explanation that is provided in the paper.

### Soundness
1

### Presentation
2

### Contribution
1
