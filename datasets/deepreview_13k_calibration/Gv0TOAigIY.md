# Remove Symmetries to Control Model Expressivity

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
When symmetry is present in the loss function, the model is likely to be trapped in a low-capacity state that is sometimes known as a ``collapse." Being trapped in these low-capacity states can be a major obstacle to training across many scenarios where deep learning technology is applied. We first prove two concrete mechanisms through which symmetries lead to reduced capacities and ignored features during training. We then propose a simple and theoretically justified algorithm, \textit{syre}, to remove almost all symmetry-induced low-capacity states in neural networks. The proposed method is shown to improve the training of neural networks in scenarios when this type of entrapment is especially a concern. A remarkable merit of the proposed method is that it is model-agnostic and does not require any knowledge of the symmetry.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach for addressing the limitations posed by symmetries in neural network training, which often lead to low-capacity model states. The authors propose a method called "syre", which can effectively remove almost all types of symmetries from neural networks, thereby enhancing model expressivity and performance across various training scenarios. The method is both model and symmetry group agnostic and straightforward to implement, requiring only minimal changes to existing training pipelines.

### Strengths
1. The proposed method is theoretically sound. Authors have rigorously proved many useful results like Proposition 3 which shows symmetry reduces parameter dimension.
2. Their proposed solution is generalizable across different architectures and does not require detailed knowledge of the model’s symmetries.
3. The empirical evaluations demonstrate significant improvements in model performance and capacity, particularly in challenging scenarios like continual learning and self-supervised learning setups.

### Weaknesses
1. Some of the theoretical explanations are dense and might be challenging for readers not familiar with the detailed aspects of symmetry in neural networks. Having decent knowledge of symmetries in neural networks I still struggled a bit with some sections like Section 5. Summarizing early on what the main theoretical result of each section might make it easier for reader to appreciate the contributions of the paper better.

2. The limitations of the method are not thoroughly discussed, which could be beneficial for practitioners to know when to use this technique with caution. 

3. The formatting of the paper seems off. All the headings are pretty close to the previous paragraph hurting the readability.

### Questions
1. It would be beneficial to see further exploration into the limits of the method, especially in more complex or less controlled environments than those tested. Also, maybe trying some transformer architecture based methods for SSL might make the architecture agnostic point stronger? 

2. Could the authors elaborate on any potential computational overhead or scalability issues when implementing syre in larger or more complex models?

### Soundness
3

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
Main contributions are:
- Builds on (Ziyin 2024) to introduce two ways that symmetry may reduce model capacity— a) that in the lazy training limit, the P-symmetry ‘masks’ certain features around a symmetric solution and b) the parameter dimension is reduced by the rank of P when around a symmetric solution. 
- Introduces a straightforward approach to eliminate these symmetric solutions by both fixing a random bias on the neurons (to handle finite symmetries) and also modifying weight decay to use a norm with respect to a positive diagonal matrix D (to handle infinite symmetries, e.g. like those that appear in the residual stream of a transformer). Also introduce a measure to quantify the degree to which a symmetry is broken. 
- Experiments that measure the extent of symmetry removal for some linear regression set-ups and some vision tasks, and continual learning in an RL setting.

### Strengths
- As noted, provide some plausible and interesting explanations for some mechanisms for how symmetry may reduce capacity that nontrivially build on (Zivin 2024).
- In some settings and experiments, their algorithm (syre) seems to usefully outperform baselines/another symmetry removal method?

### Weaknesses
Experimental shortcomings
- The authors make strong claims around the ability of symmetry-removal to improve performance for a) SSL, b) a supervised continual learning problem, and c) an RL continual learning problem. They do not implement proper baseline comparisons for any of these settings nor go beyond toy experiments. If they want to claim that (some degree of) symmetry removal is helpful for training models in practical settings, they need to either show that a) symmetry removal is reasonably competitive in mildly (compute/FLOP-controlled or at least aware) realistic settings or b) symmetry removal explains some % of the success of methods that do well in these settings. The experiments provided do not sufficiently demonstrate that the observed performance gains are directly attributable to symmetry removal, as opposed to other regularization effects. For example, the improved performance in continual learning could be due to the modified weight decay acting as a form of regularization that prevents catastrophic forgetting, rather than specifically addressing symmetry-related issues. It is crucial to isolate the effect of symmetry removal from other confounding factors.
- On the other hand, the authors only very loosely test their explanations in Prop. 2/3. Presumably, if this explanation is correct, shouldn’t models with more/less symmetries be less/more stuck in neuron-collapsed solutions (e.g. in the spirit of the Zivin 2024 experiments)? Fig. 1 only shows one case. If this claim around the science of models is to be taken as a main contribution of the paper, more experimental evidence of the propositions is needed. The current experiments do not explore a wide range of architectures or datasets to validate the generality of the proposed theory. The experiments should include a more systematic analysis of how the degree of symmetry affects the model's tendency to get stuck in low-capacity solutions, and how the proposed method mitigates this issue across different settings.


Miscellaneous
- Typo on line 65-66: “$\|\theta\|_D^2:=w^T D w$ is the norm of $w$ with respect to $D$” should be “$|w|_D^2:=w^T D w$ is the norm of $w$ with respect to $D”

### Questions
- How does your syre do on the (Lim 2024) LMC experiments?
- Do you have any (even at a very high level) design rules for how a training-algorithm designer may usefully modulate the symmetries in a model?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of symmetries in neural network loss landscapes and their role in causing models to get trapped in low-capacity states. The authors first prove that symmetries in the loss function can lead to reduced model capacity through two mechanisms: feature masking and parameter dimension reduction. They then propose SYRE, a simple modification to neural network training that aims to remove symmetries by adding a random bias to the parameters along with weight decay. For cases with uncountably many symmetries, they propose an advanced version that additionally uses a random diagonal matrix in the weight decay term. The method is model-agnostic and requires no knowledge of the underlying symmetries. The authors demonstrate their method's effectiveness across several applications where symmetry-induced capacity reduction is a concern, including supervised learning, variational autoencoders, self-supervised learning, and continual learning. They particularly show improvements in scenarios where models typically suffer from various forms of collapse, such as posterior collapse in VAEs and loss of plasticity in continual learning.

### Strengths
Here are the main strengths of the paper:

1. Addresses an important practical problem of symmetry-induced model collapse that affects multiple domains in deep learning (VAEs, continual learning, self-supervised learning).

2. Proposes a remarkably simple solution that requires minimal code changes and no architectural modifications, making it easily adoptable in practice.

3. Shows promising results in continual learning scenarios, demonstrating improved plasticity and performance maintenance over time compared to standard approaches.

4. Makes an interesting connection between symmetries and model collapse, providing a framework for thinking about how symmetries might limit model expressivity.

### Weaknesses
1. **Conceptual confusion about symmetries**: 
   - The paper discusses "removing symmetries" but primarily analyzes fixed points where $P\theta_0 = 0$
   - This misses the key aspect of symmetries - their group orbits and the associated degeneracies. The analysis focuses on specific points rather than the broader symmetry structure, which is characterized by orbits under group actions. For instance, in the case of a linear network, the relevant symmetry is not just the fixed points but the entire set of equivalent solutions related by transformations in $GL(h).
   - In the simple case of a two-layer linear network $F(x) = UVx$, the important symmetry structure lies in the $GL(h)$ orbits $(U,V) \to (Ug, g^{-1}V)$, not in fixed points. The paper's focus on fixed points neglects the continuous nature of these symmetries and their impact on the loss landscape.

2. **Overly restrictive theoretical framework**: 
   - The condition $P\theta' = \theta'$ for $(\theta', P)$-reflection symmetry is artificially restrictive. This condition limits the scope of the analysis and does not capture all possible reflection symmetries. The paper should consider a more general definition of reflection symmetry that does not impose such a constraint.
   - Simple examples show valid reflections that violate this condition. For instance, in 2D with $\theta' = (0,1)$ and reflection in x-direction $P = ((1,0),(0,0))$, we have $P\theta' \neq \theta'$ yet this is a perfectly valid reflection symmetry. This demonstrates that the current definition is not sufficiently general to cover all relevant cases.

3. **Questionable arguments about gradient vanishing**: 
   - The paper suggests symmetric points trap models due to vanishing gradients. However, this claim is not universally valid. While gradients may vanish at specific points, this does not necessarily imply that these points are trapping. The paper needs to provide a more nuanced analysis of the gradient behavior around these symmetric points.
   - However, in the UV example, fixed points along $U=V$ line have nonzero gradients except at origin and minima. Gradients naturally vanish along symmetry orbits (they're level sets of the loss), but this doesn't imply trapping as claimed. The paper needs to differentiate between gradients vanishing along orbits and gradients vanishing at specific points.

4. **Limited analysis of regularization effects**: 
   - The D-norm modification merely changes spherical weight decay to ellipsoidal weight decay. The \theta_0 shift changes the center of the regularization. While these modifications may improve optimization, it's not clear they "remove symmetries" as claimed. The paper does not provide sufficient justification for how these modifications fundamentally break the underlying symmetry structure.
   - In the UV example, these modifications may select preferred points along symmetry orbits (like weight decay does) but may not fundamentally break the symmetry structure. The paper needs to demonstrate that the proposed method does more than just select a different point within the same symmetry orbit.

5. **Experimental limitations**: 
   - Lack of systematic comparison with standard weight decay baseline. The paper should include a more thorough comparison with standard weight decay to isolate the effects of the proposed method. Without this, it's difficult to determine if the improvements are due to the symmetry-breaking mechanism or simply a different form of regularization.
   - Only a few experiments (particularly continual learning) show clear improvements over weight decay. The paper needs to provide more comprehensive empirical evidence to support the claims, including a broader range of tasks and datasets. The current results suggest their method might be a useful variant of weight decay, but not necessarily for the theoretical reasons provided.

### Questions
Those are good questions. Here are those formatted plus a few additional ones I think would be helpful:

1. **Fixed Points vs Symmetries**:
   - Do you mean fixed points (invariant sets) when discussing "symmetric points" where $P\theta_0 = 0$? If so, consider revising terminology to avoid confusion with symmetry orbits.
   - Why focus on fixed points rather than the full symmetry orbits which characterize the degeneracies in the loss landscape?

2. **Gradient Analysis**:
   - Can you clarify the argument around equation (2) about vanishing gradients? How does this differ from the natural vanishing of gradients along symmetry orbits?
   - In the expansion around fixed points, do you consider gradients in directions orthogonal to the symmetry?

3. **Initialization and Fixed Points**:
   - For a simple network $F(x) = UVx$, the origin $(U,V)=(0,0)$ is a fixed point, but why is this relevant when standard initialization (Glorot, etc.) avoids such points?
   - Do your arguments about trapping at fixed points apply to more realistic initialization schemes?

4. **Regularization Effects**:
   - Can you provide ablation studies comparing your method with standard weight decay?
   - For the D-norm modification, how does making weight decay ellipsoidal fundamentally differ from standard weight decay in terms of symmetry breaking?

5. **Theoretical Claims**:
   - The condition $P\theta' = \theta'$ seems unnecessarily restrictive. Can your results be generalized without this condition?
   - For continuous symmetries (like $GL(h)$ in linear networks), can you make precise what subset of symmetries your method breaks?

6. **Empirical Validation**:
   - Could you provide standard weight decay baselines for all experiments?
   - In scenarios where your method outperforms standard weight decay (like continual learning), what mechanism explains this improvement?

Would you like to add any other questions?

### Soundness
3

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
This paper addresses the problem of low-capacity states, often referred to as "collapse," that arise when neural network loss functions contain inherent symmetries. The authors prove two mechanisms through which symmetries reduce model expressivity, leading to these collapsed states and propose a method called syre to eliminate such symmetries. The syre algorithm introduces static random biases alongside weight decay, providing a simple yet effective means to remove almost all symmetry-induced constraints without requiring knowledge of the specific symmetries. The method is claimed to be model-agnostic, applicable to a broad range of architectures, and effective in both theoretical and practical contexts. Empirical results support the effectiveness of the proposed method in diverse settings, including supervised learning, self-supervised learning, and continual learning.

### Strengths
- The paper presents a novel approach to tackling symmetry-induced collapses in neural networks. The proposed method uses static random biases to remove symmetries, a simple yet innovative solution. The theoretical insights connect symmetry and expressivity in a new way, offering a significant advancement.
- The theoretical contributions are rigorous and well-supported with proofs. The authors also provide a range of empirical validations that align with their theoretical claims, making a strong case for the method’s effectiveness across various scenarios.
- The paper is clearly structured, with a logical flow from problem setup to solution. The core concepts are well-explained.
- The method's simplicity and general applicability make it impactful. By addressing a fundamental problem in deep learning training, syre has potential benefits for diverse architectures and tasks, opening new research avenues into model expressivity and optimization.

### Weaknesses
 - Experiments are limited to small- or medium-scale models. The method’s applicability to real-world, large-scale tasks is insufficiently demonstrated. Benchmarks on high-impact datasets, such as ImageNet, and large-scale architectures, like transformers, would add credibility.
- The impact of completely removing symmetries on generalization is not well-discussed. Symmetry sometimes acts as a regularizer, and the absence of analysis on this potential downside is a gap.

### Questions
- How does syre scale to large models like transformers? Have you tested its efficiency or computational impact on such architectures?
- Would an adaptive bias approach improve the method compared to using a static bias throughout training?
- How sensitive is syre to hyperparameter choices, and do you have heuristics to guide practitioners in tuning them?

### Soundness
3

### Presentation
3

### Contribution
3
