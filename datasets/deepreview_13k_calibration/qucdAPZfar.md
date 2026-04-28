# Hide & Seek: Transformer Symmetries Obscure Sharpness & Riemmanian Geometry Finds It

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 6, 8, 3, 6

## Abstract
The concept of sharpness has been successfully applied to traditional architectures like MLPs and CNNs to predict their generalization.
  For transformers, however, recent work reported weak correlation between flatness and generalization. We argue that existing sharpness measures fail for transformers, because they have much richer symmetries in their attention mechanism that induce directions in parameter space along which the network or its loss remain identical.
  We posit that sharpness must account fully for these symmetries, and thus we redefine it on a quotient manifold that results from quotienting out the transformer symmetries, thereby removing their ambiguities.
  Leveraging tools from Riemannian geometry, we propose a fully general notion of sharpness, in terms of a geodesic ball on the symmetry-corrected quotient manifold. In practise, we need to resort to approximating the geodesics. Doing so up to first order yields existing adaptive sharpness measures, and we demonstrate that including higher-order terms is crucial to recover correlation with generalization.
  We present results on diagonal networks with synthetic data, and show that our geodesic sharpness reveals the correlation for real-world transformers on ImageNet.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a more general notion of sharpness measurement based on a geodesic ball on the symmetry-corrected quotient manifold, which accounts for the symmetry equivalence of the original network. Experiments with Diagonal Networks on synthetic data and transformers on the ImageNet dataset show that Geodesic Sharpness has a stronger correlation with the model’s generalization performance compared to Adaptive Sharpness.

### Strengths
- The paper introduces a novel approach to sharpness by leveraging quotient manifolds, reflecting the symmetry of the parameter space. This effectively addresses a gap in previous work that has not considered network symmetry.
- The methodology is theoretically well-founded, employing tools from Riemannian geometry to incorporate network symmetry to the sharpness measure in a principled way.
- Geodesic sharpness is shown to achieve a higher Kendall Tau correlation with the relevant metrics than Adaptive sharpness in both synthetic and ImageNet experiments.

### Weaknesses
The experimental section should be strengthened. Assessing the correlation between the proposed sharpness and the generalization of transformers trained on other tasks, such as time series forecasting or language modeling, would further support the findings.

### Questions
- Could you include additional experiments on real-world data beyond vision transformers? This would enhance the experiment effectiveness and demonstrate the predictive capacity of the proposed Geodesic sharpness across a broader range of tasks.
- Could you provide a time complexity analysis of the proposed method relative to Adaptive sharpness?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method for measuring the sharpness of neural networks, called geodesic sharpness, which takes into account the symmetries present in the network architecture. The authors argue that previous sharpness measures fail to accurately capture the sharpness of transformers because they do not account for the rich symmetries present in the attention mechanism. The authors clearly motivate the need for a new sharpness measure that is invariant to these symmetries. However, the paper need to be polished more to fix typo and clearer explanation, especially experiments.

### Strengths
From theoretical aspects, the authors' main theoretical contribution is the application of Riemannian geometry to the study of neural network parameter space symmetry. They propose to use the geometry of the quotient manifold, which is obtained by removing the symmetries from the parameter space, to define a sharpness measure that is invariant to these symmetries. This approach is general and can be applied to a wide range of symmetries. The authors show that ignoring the curvature introduced by the symmetries leads to traditional adaptive sharpness measures. 

From experiment aspects, yo validate their approach, the authors conduct experiments on both synthetic and real-world data. They analytically derive the geodesic sharpness for diagonal networks and show that it correlates strongly with generalization. They also apply their method to large vision transformers and find that geodesic sharpness has a stronger correlation with generalization than any previously reported measure, both for in-distribution and out-of-distribution settings.

The main strength of the paper is its novel and principled approach with the use of Riemannian geometry to account for symmetries in sharpness measures, which can apply to more problem like equivariant neural functional network.

### Weaknesses
The paper, while presenting a promising theoretical approach to measuring sharpness, suffers from certain shortcomings related to the experimental validation of the proposed method and the potential computational cost involved:

-   **Limited empirical support:** The experiments conducted on real-world transformers lack breadth. It would be good if the authors can demonstrated in the natural language task too, like language modeling with wikitext103. Furthermore, the current experiments on vision transformers only use a single dataset and model architecture. Expanding the experiments to include more diverse tasks, datasets, and model architectures would provide stronger evidence for the general applicability of the proposed sharpness measure. For example, exploring the performance of geodesic sharpness on different vision tasks such as object detection or image segmentation, and different vision transformer architectures would be beneficial.

-   **Effect of assumptions:** The paper makes an assumption regarding the full column rank of weight matrices in attention layers. A relaxation parameter is introduced to handle potential violations of this assumption, but the impact of this parameter on the results is not thoroughly investigated. Specifically, the paper lacks a sensitivity analysis to show how the choice of this relaxation parameter affects the computed geodesic sharpness and its correlation with generalization. It is crucial to understand the range of values for this parameter that yield reliable results, and how the results might change when this assumption is violated in practice.

-   **Computational burden:** The paper acknowledges the potential computational demands of calculating geodesic sharpness, especially for large models. However, it lacks a detailed analysis of the computational cost, including aspects like time complexity, memory requirements, and actual runtime measurements. Such an analysis should include a breakdown of the computational cost associated with each step of the algorithm, such as the projection onto the horizontal space and the optimization process.  A comparison of the computational cost with that of adaptive sharpness would also be helpful to understand the practical overhead of the proposed method. This analysis would enable a better understanding of the feasibility of employing geodesic sharpness in practical scenarios, particularly when dealing with large-scale models.

### Questions
1. "RIEMMANIAN" -> "RIEMANNIAN" in title
2. ",and" -> ", and" in line 39
3.  In my opinion, the contributions can be collated, where (b)-(c) and (d)-(e)-(f) are collated into two contributions: the development of geodesic sharpness and experiments for it.
4. Diagonal network experiment:  it is not clear to me what Figure 3 is showing. What is the meaning of the x axis and y axis? What is the ideal result? Why only show 50 data points when you have 200 model trained? Why the points in adaptive average case aligned in different direction in comparison with two other cases? I suggest adding more detailed captions and axis labels to Figure 3, and include explanations for these points in the corresponding text.
5.  Assumption 5.1: Does Assumption 5.1 are too strong? What if the assumption is violated? Can we still calculated the result but with wrong value, or not able to calculate it at all? It would be good if the author can provide the evident and explanation of effect of adding $\epsilon I_h$ into $GH$ since there have not any for the assumption. Also, including a discussion of the implications of violating Assumption 5.1 and provide empirical evidence for the effects of adding the $\epsilon I_h$ term.
6. Can the authors describe in detail how you treat the multi-layer schema of transformers model? It is not clear at this time. It would be good if the author can provide the diagram illustrating the approach for multi-layer transformers.
7. Experiment diversity: it would be good if we can demonstrated in the natural language task too, like language modeling with wikitext103, to ensure that it works across domains.
8.  In order to find the geodesic approximation, you need to solve the optimization using SGD, what is the quantitative performance, i.e. wall clock time or time/memory complexity of this approach in comparison with adaptive sharpness? How does it scale with large models like LLMs?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a new approach to measuring model sharpness using Riemannian geometry. This approach takes into account the symmetries in model parameters, removing ambiguities that these symmetries can cause. As a result, it provides a clearer and more reliable sharpness measure compared to previous methods.

### Strengths
1. This work takes a broader view of parameter symmetries and introduces a more robust metric for measuring sharpness.

2. The theoretical framework and assumptions are well-grounded, and the experimental results are both strong and consistent.

### Weaknesses
1. $\textbf{Geodesic sharpness}$ in section 5.2 is abbreviated. Providing a clear, explicit formula for geodesic sharpness, including the specific metric used and how it relates to the parameter space, would improve comprehension. The current description lacks sufficient detail to fully grasp the practical computation of this metric.

2. The discussion of geodesic sharpness in transformers (Section 5.3) is brief. Including a detailed description of how geodesic sharpness is specifically applied to different layers within transformers, particularly the attention layers, would make the analysis more thorough. A breakdown of how the symmetries are handled in each layer, and how this impacts the sharpness calculation, is needed. Furthermore, a more explicit explanation of how adaptive sharpness is applied to each layer, and why it is considered more appropriate for some layers than others, would be beneficial.

3. The paper aims to propose a metric that surpasses previous methods. Therefore, I would expect comprehensive experimental results demonstrating both the effectiveness of the proposed approach and its superiority over existing methods. While the experiments provide sufficient evidence of the method’s effectiveness, the comparative analysis with previous methods seems limited. Specifically, a more thorough comparison across a wider range of datasets and model architectures is needed, including a quantitative comparison of the correlation between the proposed metric and generalization performance against existing sharpness measures.

Minor points:

$ullet$ Example 3.2 "(Self-attention Vaswani et al. (2017))" $\to$ "Example 3.2 (Self-attention (Vaswani et al., 2017))".

$ullet$ $\textbf{Geodesics}$ in section 5.2: "... the geodesics of metric 15" $\to$ "... the geodesics of metric (15)".

### Questions
1. In Case A), the second-order term in Equation (12) is omitted because it is considered small compared to the first-order term. However, I wonder if this omission might be overly convenient. Since there is no indication of how small $\rho$ can be, I’m unsure about the relative scale of the first and second orders. Would it be possible to retain the second-order term and, perhaps, combine the results of both cases to reach the conclusion?

2. Could you provide further clarification on why "adaptive sharpness is more appropriate" in Section 5.3?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel analysis of sharpness in machine learning, with a particular focus on its implications for generalization. The authors argue that existing sharpness measures are inadequate due to their failure to account for the symmetries which arise in parameter space, especially the complex symmetries inherent in transformer architectures. To address this limitation, they leverage tools from Riemannian geometry to propose a refined definition of sharpness (their so-called geodesic sharpness) that explicitly removes these symmetries by instead focusing on the quotient space. This construction draws upon concepts from the theory of quotient manifolds. The authors validate their theoretical framework through experiments on both toy models and vision transformer models trained on ImageNet.

### Strengths
I found this to be an interesting paper. The authors explore the notion and role of sharpness in machine learning and shed light on how sharpness is affected by the symmetries which arise in parameter space for these large machine learning models. They use interesting ideas from Riemannian geometry and provide a clear, detailed analysis of difficult ideas. The ideas are original and they provide a creative way and mathematically sound way to define a new notion of sharpness (i.e., geodesic sharpness) which mitigates this issue of symmetry in parameter space.

### Weaknesses
Based on my understanding of the author's work, here are the weaknesses I see

There are a few conceptual gaps for me. While the use of quotient spaces to address parameter symmetries is conceptually nice, certain aspects of their construction are unclear to me. In particular, the choice of Riemannian metric on the total space $\bar{\mathcal{M}}$ appears to be crucial, as exemplified by the metric defined in equation (15) for attention layers.  This metric is not unique or canonical. Would similar results hold for any metric, except I suppose for the standard Euclidean one? It is unclear whether the proposed sharpness measure is invariant under different choices. One could conceive of a metric on $\bar{\mathcal{M}}$ that yields a different value for geodesic sharpness. Is that right? Or should all measures for geodesic sharpness be invariant under the R. metric of the total space as well? This technique is marketed in the introduction/conclusion as a "one-size-fits-all" technique for appropriately measuring sharpness but this choice of total R. metric doesn't feel that way to me. To address this concern could the authors
 1. Explain the rationale behind choosing the specific metric in equation (15)
 2. Provide some discuss around how sensitive the results are to different choices of Riemannian metrics on the total space
 3. Clarify if there's a principled way to select an "optimal" metric for a given architecture.
These points would help evaluate whether the method is truly "one-size-fits-all" as claimed.

Also the details of how to actually compute the geodesic sharpness for the attention layer example (Sec 5.2) is lacking, see line 468-469. It's not clear to me what that means to "...plug Eq. 16 into Eq. 17 and solve the resulting optimization problem using SGD". Would it be possible to include the details for that computation and optimization solution details/setup? To address this concern, could the authors
 1. provide the explicit form of the optimization problem after plugging Eq. 16 into Eq. 17 and clarify the specific SGD algorithm used to solve it and hyperparameters used, and
 2. provide any additional constraints or modifications needed to ensure the optimization remains on the manifold

It would be nice to see more experiments or at least some more computational examples. The paper only addresses, in a careful way, very simple diagonal networks and attention layers in transformers. Nothing in between. The experiments are limited to correlational studies. It would be good to have more architectures and datasets to help convince the reader of this new technique. To address this, the authors could
 1. test this measure of geometric sharpness on intermediate architectures between diagonal networks and transformers, such as MLPs or CNNs; or ideally, architectures that are more closely comparable with other measures of sharpness in the literature.
 2. apply the technique to different datasets beyond ImageNet
 3. conduct ablation studies to isolate the impact of different components of the 'geodesic sharpness' measure

Also, the final takeaway message from Figure 4 (see line 488) is that the "...geodesically sharpest models studied on ImageNet are those that generalise best." This seems counter to the typically held belief that less sharp or more flat models generalize better. It would be nice to have more experiments or theory to explain why we see the opposite behavior here than previously in the literature. Or it would be nice to recreate the experiments in the literature which demonstrate that less sharp models generalize better (e.g. the original SAM paper and followups) and show that the geodesic sharpness behaves in the opposite way. To address this concern, could the authors
 1. provide a theoretical explanation or justification as to why 'geodesic sharpness' might behave differently from traditional sharpness measures
 2. conduct a direct comparison with previous sharpness measures on the same models and datasets. This, in particular, would be very nice. And
 3. discuss potential implications of this result for providing better understanding of generalization in deep learning

There are also some parts of the exposition that I found confusing or misleading (in either the concepts or lack of details in plots) and quite a large number of typos which made the paper hard to follow at times. I've outlined these points in the questions section below.

### Questions
- line 112. in contribution (d) you claim that Figure 1 shows that there is a strong correlation between generalization and sharpness. Is this a typo? Can you better explain the connection between Figure 1 and generalization?
- In general, the paper appears to only address symmetries that arise as group actions of GL. Is it obvious that this captures all possible symmetries in the parameter space? What is the effect of your construction of the geodesic sharpness when not all symmetries are removed? 
- in contribution (f) and in the paper you make a comparison with the CLIP  experiments from Andriushchenko et al. However, those models were not trained to convergence and one could argue that the role of sharpness in generalization is only evident for well-tune and converged models. Does that also apply to your measure of geodesic sharpness?
- line 279, why denote the points in total space by $\bar{x}^{(')}$. I'm confused by this notation.
- line 280, is this a typo? Do you mean x,y for points in the quotient space?
- line 297. Can you clarify the details in the section "Linear embedding space". When you say "On the outer most layer, we are given a linear Euclidean space E…" what does this mean? Do you mean the $d$ parameters relating to the outermost layer of the network? Also, why define the loss $\overline{\overline{\ell}}$ just on these outer layer parameters? How are $\overline{\overline{\ell}}$ and $\overline{\ell}$ related to each other?
- then on line 304, you reference the "Riemannian generalization" The R. generalization of what? The gradient?
- line 318, i mentioned this above, but here you reference endowing the total space $\overline{\mathcal{M}}$ with a smooth inner product. Yes. it is possible to endow any smooth manifold with a Riemannian metric. However, this R. metric is not unique. You reference defining it in Appendix B.4 but that just points to a definition of what a Riemannian metric is. This is confusing and crucial aspect of this work. 
- Section 4. When defining the geodesic sharpness, I'm surprised to not see mention of the exponential map to define geodesics in the manifold using vectors in the tangent space. Would it not be possible to reformulate your construction looking only at vectors in the tangent space? And restrict yourself to vectors of a certain size in order to keep them within a fixed ball when projected to the manifold. 
- In Figure 3, you plot sharpness vs test loss for diagonal models. But only for 50 of the 200 models from the experiment setup? Why only 50 and why those?
- How natural or reasonable is Assumption 5.1? There is a low-rank bias in deep learning when training overparameterized models. Can you provide a reference that this assumption is usually satisfied in multi-head attention layers for default choices of $d_v, d_k$?
- line 453: Is it possible to endow the total space with any smooth Riemannian metric? Why this one? Admittedly I'm less familiar with the reference (Absil et al 2008) but it would be nice to see a computation verifying this is indeed a Riemannian metric and why this inner product was chosen.
- line 514: Can you clarify what you mean when you say "..attention weights approach being singular" here? How are you defining singular. Also you mention a relaxation parameter but I'm not clear on the role this 'relaxation parameter' plays. You indicate that "..in practise we found out results were robust to this parameter". Can you explain more what robustness analysis you conducted to justify this claim.

typos/nits
 - (typo) Do you mean $L_{\mathbb{S}}$ not $L_{S}$  in equations (1) and (2)? same in equation (3)
 - (nit/personal preference) := is more common that :- for definitional equivalence
 - (typo) line 229. Do you mean $\overline{\overline{f}}$ is symmetric…?
 - the Figures have been resized and the font is very small, difficult to read
 - line 434: what do you mean that the GL(h) symmetry is 'dealt' by geodesic sharpness?
 - line 463: 15 should be (15)

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper generalizes the (adaptive) sharpness concept by considering both the first-order perturbation and the (second-order) curvature of the loss landscape, presented under a Riemannian geodesic framework. It aims at solving the inconsistency in the literature on the correlation between sharpness and generalization, and addresses the failure of existing sharpness in measuring the generalization of Transformers with larger symmetry, explained by the scaling/rescaling symmetry of the parameter space. The symmetry is formalized as the quotient group. Experiments on both a toy diagonal network and fine-tuned vision transformers show that the geodesic sharpness has a significant correlation with the generalization gap.

### Strengths
The motivation is strong, the theoretical discussion is rich and sound, and the curvature-aware sharpness significantly depends on the generalization gap. I appreciate the insights of the Attention symmetry and the strong theoretical connections.

### Weaknesses
- My main concern is the practical effectiveness of the proposed method: does it really improve existing adaptive sharpness? In Figure 4 the improvements are not quite visible, and the parameter $\tau$ is neither explained nor aligned by column. The lack of a clear explanation of $\tau$, specifically how it's calculated and what its values signify in the context of the results, makes it difficult to assess the significance of the reported improvements. The absence of column alignment further complicates the comparison across different models or settings.
- The experiments are not described in detail, which affects reproducibility. For self-containedness, the method used in the experiment from Wortsman et al. (2022) could be explained better in detail. For example, what are the hyperparameters, how are the models trained, what is the precise algorithm, etc.? The description of the training procedure, including optimization algorithms, learning rates, batch sizes, and other crucial hyperparameters, is missing. This lack of detail makes it impossible to replicate the experiments and verify the claims made in the paper. The specific algorithm used to compute the geodesic sharpness is also not clearly defined, which is essential for reproducibility.
- It is questionable whether the attention's symmetry argued by the author is indeed the practical reason rather than a hypothesis. It would be helpful if the author could give a stronger argument or some illustrations. To give an example, ensure that the scaling symmetry causes irregularity in pre-trained models by measuring the conditional number, and modulating out this symmetry indeed corrects the sharpness---or any other way you prefer. The argument about the scaling symmetry of attention mechanisms is not sufficiently supported by empirical evidence. Measuring the condition number of weight matrices in pre-trained models and demonstrating how modulating this symmetry affects sharpness would provide a more compelling argument. Without such evidence, the claim remains speculative.
- I believe the paper's writing could benefit greatly by being more concise. Many sentences in the introduction seem to wander around and are not precisely to the point.
- Minor issues: Figures 2, 3, and 4 are not referenced.

### Questions
- I don't understand the role of the $\tau$ variable in the result figures. For example, could you explain how it is chosen, and how it relates to the results?
- I don't understand why in Figure 3 (left), the average-case adaptive sharpness is claimed to reveal a correlation with the test loss (generalization gap). To me, it looks not obvious, and the dependency is reversed.
- $c$ inconsistently appears in Appendix D. Do the experiments of geodesic sharpness also choose a vector $c$ by taking $c=|w|$ to normalize each parameter tensor? If not how to guarantee fair comparison? In Appendix D $c$ is preset, but I don't understand whether the geodesic is invariant over scaling?
- I wonder if normalizing QK embeddings will fix the concern in the paper that Transformers have GL group symmetry? It is shown in practice that it stabilizes training (such as [1]). [2] also uses spherical projection for theoretical convenience. Or if not, are there alternative ways to address the scaling symmetry?

[1] Scaling rectified flow transformers for high-resolution image synthesis. Esser et al. 2024.
[2] The emergence of clusters in self-attention dynamics. Geshkovski et al. 2024.

### Soundness
4

### Presentation
2

### Contribution
3
