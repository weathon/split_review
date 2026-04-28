# Understanding Optimization in Deep Learning with Central Flows

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 5, 8, 8

## Abstract
Optimization in deep learning remains poorly understood, even in the simple setting of deterministic (i.e. full-batch) training. A key difficulty is that much of an optimizer's behavior is \emph{implicitly} determined by complex oscillatory dynamics, referred to as the ``edge of stability.''
The main contribution of this paper is to show that an optimizer's implicit behavior can be explicitly captured by a \emph{central flow}: a differential equation which models the time-averaged optimization trajectory. We show that these flows can empirically predict long-term optimization trajectories of generic neural networks with a high degree of numerical accuracy. By interpreting these flows, we reveal for the first time 1) the precise sense in which RMSProp adapts to the local loss landscape, and 2) an \emph{acceleration via regularization} mechanism, wherein adaptive optimizers implicitly navigate towards low-curvature regions in which they can take larger steps. This mechanism is key to the efficacy of these adaptive optimizers. Overall, we believe that central flows constitute a promising tool for reasoning about optimization in deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates optimization methods in deep learning, focusing on the "edge of stability" regime. Since the gradient flow differential equation fails to capture both the oscillatory behaviors and the averaged trends of gradient descent in many neural network training scenarios, the authors introduce central flows, a new differential equation that approximates the "time-averaged" optimization dynamics up to high accuracy. The paper also provides valuable insights into adaptive optimizers, such as RMSProp, and introduces the concept of acceleration via regularization, where adaptive optimizers naturally steer trajectories toward low-curvature regions, enabling larger steps and improving optimization efficiency.

### Strengths
1. The article is clearly written and reader-friendly, with insightful discussions on the oscillatory behavior of optimization methods.

2. The time-averaging and Taylor expansion framework is intuitively sound and appears to be broadly applicable, capable of handling various adaptive optimizers, and could potentially be extended to more general optimization methods.

3. Extensive empirical results are presented, supporting the validity of the central flow.

Overall, I think this is a nice paper.

### Weaknesses
The central flow derivations are grounded in empirical observations, and several mathematical steps rely on informal reasoning. For example, it is not clear how to rigorously justify the time averaging step and quantify the high-order error in the Taylor expansion. Rigorous proofs or formal analysis would enhance the robustness of the claims.

### Questions
The authors present extensive numerical experiments that demonstrate the central flow as a strong approximation to average optimization dynamics. While the numerical results are impressive, could the authors discuss any potential limitations or scenarios where the central flow may not perform as effectively? Understanding the boundaries of the method’s applicability would provide helpful context for further investigation.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work develops a central flow approach with which to study the training dynamics of neural networks. The authors use this approach to investigate the edge of stability and optimization via RMSProp. The authors argue that their analysis can shed new light on how RMSProp adapts to a local loss landscapes.

### Strengths
1. This work was well written and well structured, making it easy to follow along. 

2. The authors analyzed a wide range of neural networks, including modern architectures such as ViT.

3. The authors developed their approach in settings where the interpretation was straightforward to make their point more clear. 

4. The figures were well done and easy to read. 

5. The authors convincingly show that their central flow approach accurately captures the general behavior of neural network model training. 

6. The identification of a possible weakness of the pre-conditioning of RMSProp is interesting and suggestive of a way in which to use the authors' work to improve DNN optimization.

### Weaknesses
1. My main reservation of this work as it stands (which I hope the authors can easily clarify for me), is the claim that the central flow analysis of RMSProp-Norm demonstrates how the optimizer regularizes against sharpness and moves towards regions of parameter space with lower sharpness. While I understand the argument mathematically, and the analysis of the central flow (Fig. 5) illustrates this point, it does not seem consistent with the results of training ViT (Fig. 4). In particular, in Fig. 4 the Hessian eigenvalues increase with training and $2/S$ decreases (which more closely mirrors the ablation in Fig. 5). This seems to suggest that training is moving towards a region with greater sharpness. How do the authors reconcile this? Are the authors claiming that the network would be headed towards an even more sharp region if it was not for RMSProp-Norm, and that the optimizer is reducing sharpness, albeit not as completely as in the case of just analyzing the central flow? 

2. I think this work would also benefit from showing the sharpness of the full RMSProp. Providing numerical evidence that use of RMSProp steers the network away from sharp areas of parameter would make this point more salient. It is not clear if the preconditioning of RMSProp is actually leading to a reduction in sharpness, or if it is simply changing the effective step size in a way that is not directly related to sharpness.

3. While the goal of understanding edge of stability was motivated, I think this work could also benefit from more discussion on how the central flow approach could be used for other training dynamics phenomena. In particular, as I understood this work, one of the keys to utilizing the method successfully was the ability to find $\sigma$. This was only possible since the training limited to some fixed value. How general do the authors expect this kind of solving for $\sigma$ to be? It is unclear if this method can be applied to more general optimization scenarios where such an equilibrium is not reached.

4. The authors show that the distance between the central flow weights and the GD weights are small (Fig. 3). Is this because the distance is an average across many weights? Or is the difference between oscillations and no oscillations a matter of small differences in the weights? It is unclear if the small distance is a result of averaging over many parameters, or if the central flow is indeed capturing the essential dynamics of the optimization process.

5. One last point that was unclear to me is why $x_t u_t$ are not present in Eq. 2, since they are time varying and I would expect $d w(t) / dt$ to depend on their value. It is not clear why this term is omitted, given its time-varying nature and potential impact on the trajectory.

### Questions
1. Why is there a mismatch between Fig. 4 and Fig. 5, in terms of sharpness and $2/S$? 

2. How does the sharpness evolve (for a numerical example) when optimizing using full RMSProp? 

3. Do the authors think this approach can be used when there may not be an obvious choice of $\sigma$? 

4. Why are $x_t u_t$ not present in Eq. 2?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors developed a methodology for creating optimizers in the context of deep learning. They empirically demonstrated that central flows govern long-term optimization trajectories, providing insight into the behavior of optimizers.

### Strengths
The work presents novel contributions. Additionally, it represents an advancement in the study of locally analyzed optimizers and suggests progress for other optimizers.

### Weaknesses
1. In the abstract, the introduction and related work the authors repeats the same phrase 'Optimization in deep learning remains poorly understood' (lines 11, 26 and 68).  Maybe the authors can phrases like: 'How optimization works in deep learning continues to be largely unclear' or 'The optimization process in deep learning is still not well understood.'
2. The contributions of the work are unclear in the introduction, which is somewhat difficult to follow in that sense. Maybe the authors can add a explicit numbered list with the contributions.
3. In general, it would have been valuable to provide a bit more discussion or formal mathematical argumentation on how some equations were derived (e.g., equations 1 or 7).
4. The proofs are generally well-written and clear, but since they are in the appendix, the flow of the paper's main narrative can sometimes be interrupted. Would be helpful to add some discussion of the results.

### Questions
What are the geometric implications of the curvature penalty?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper shows that an optimizer's implicit behavior comprising complex oscillatory dynamics (EOS) can be captured explicitly by ODE (termed as "central flow" by authors) modeling a time-averaged optimization trajectory. This a very interesting idea and probably the first explicit & numerically precise characterization that predicts a long-term optimization path well. Using central flow they analyze the local adaptivity of RMSProp and provide insight into an interesting phenomenon termed "acceleration via regularization" which attempts to reason the efficacy of adaptive optimizers in general.

### Strengths
1. This is a novel study to deeply understand an optimizer's implicit dynamics and attempt to explicitly characterize it. The authors exploit central flow as a tool to analyze adaptive optimizers (RMSProp) and consequently draw interesting observations regarding their efficacy. They provide a strong theoretically backed argument as to how the EOS regime leads to implicit step size selection and curvature reduction.
2. A new characterization of phenomena "acceleration via regularization" (observed using central flow) where they show how adaptive optimizers (RMSProp) navigate to a low generalization landscape where they can take larger steps. This claim is backed by a comprehensive set of experiments that showcase their claim precisely. 
3. The development and intuition of central flow and how it tracks time-averaged optimization trajectory to account for precise implicit behavior is robust. While the derivation might have started from informal reasoning (as accounted in the paper) I find the subsequent logic intuitive and reasonable. Each claim is backed by theoretical analysis in the Appendix which also looks correct. 
4. Detailed explanation of the experimental setup and good accounting of the limitations. They make it extremely clear what is the purpose of their work while also providing a comparison against other ODE methods like stable flow. Each claim is backed by a relevant ablation or experimental evaluation. 
5. There are comprehensive notes for the reader to provide quick additional reference or context to a claim being made in the paper which is very useful.

### Weaknesses
Some comments
1. In the large-scale evaluation reported, I majorly see MSE loss being used. How does the ODE analysis deviate or negatively impacted by commonly used loss functions for classification tasks, such as cross-entropy? While this might be part of future work I think addressing such limitations in the main body would improve the paper. Specifically, it is unclear if the central flow accurately captures the dynamics when the loss landscape is highly non-quadratic, as is often the case with cross-entropy loss in deep learning models.
2. The analysis relies heavily on the largest eigenvalue estimation for ODE analysis. I think it might be helpful to account for how precise/reliable such estimations are when empirically implemented. The paper should discuss the sensitivity of the central flow to errors in the eigenvalue estimation, and how this might affect the accuracy of the predictions, especially in high-dimensional spaces where eigenvalue computations can be challenging.
3. I might have missed this but I do not see any ablations on the behavior of $\sigma^2$, that models $\mathbb E[x_t^2]$ (equation 2). Is it because it has a fixed value due to the 3 desiderata described in line 249? In either case, I think it might be good to show its evolution across training to support its expected behavior. It would be beneficial to see how the variance of the oscillations changes over time, and how this relates to the central flow's predictions.

Minor weakness
1. Figure 1: x-axis labels missing. While I can infer what is being plotted I think the figures should be precise on labels for faster understanding.
2. Figure 3, the legend is difficult to read might be possible to increase the font a bit.  
3. Figure 4: The gray curves are mostly hard to see. I think it might be helpful to use a color palette that makes the curves more discernable.

### Questions
1. The ODE derivation is quite general. However, I wonder if it's possible to analyze non-convex objective functions with central flow and if they still track real optimization trajectories. 
2. Can the authors comment on why they chose to analyze RMSProp only as opposed to using ADAM? What sort of issues did they face of trying with ADAM, if any?
3.  Central flow clearly shows how adaptive optimizers like RMSProp additionally account for the curvature regularization induced by oscillations. While it can be seen that they bias trajectory towards lower curvature, I wonder if central flow helps understand what happens in the presence of pathological curvatures (specifically low-curvature critical points such as saddle points). Does central flow demonstrate whether these points are circumvented when using adaptive optimizers?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper uses mathematical reasoning to derive central flows of optimization functions. Central flows are functions which predict the averaged behavior of oscillating optimization functions when applied to neural networks.  These functions are empirically accurate, and reveal several interesting insights into the behavior of different optimization functions.

In gradient descent, central flows are used to describe the oscillatory effects of sharpness, and the sharpness-decreasing effects of oscillation, resulting in a steady-state (on average) of the sharpness of the points of the path taken by gradient descent.  These effects have been described previously, but not so generally.

In RMSProp, central flows are used to reason about what the paper calls effective sharpness.  They show that RMSProp, despite being a first-order algorithm, nonetheless adapt to the second-order curvature.  The path of the optimizer is driven to low-curvature spaces, where it can safely take large steps, improving its performance.

### Strengths
- The work is important.  Understanding the behaviors of optimization algorithms is very important, and this paper provides new insights through a novel approach.
- The paper is engaging.  It is well written and easy to read.
- Conclusions and key takeaways are clearly stated.
- The work is wide-ranging, and makes a number of important conclusions in a single paper.

### Weaknesses
The main weakness is that this is not really a conference paper.  Essential parts that justify the work (the mathematical derivations and experimental results that support the conclusions) are included in the 41-page appendix.  There is some point where the appendix is so essential, this cannot really be considered a 10-page paper.  The work is interesting, important, and well laid out, but the ten pages are not, on their own, an acceptable paper, as the appendices are so voluminous and essential that the reader would have insufficient reason to believe the claims of the authors without them. I cannot find anything in the reviewer guidelines to help me understand the expectations in this area, so I leave it to the AC for guidance and discussion.

If this is a problem for the conference, the most useful thing to promote to the core paper would be some of the experiments which demonstrate the fidelity of the predictions from the central flows to the true observed optimizations.  If it's not a problem, I believe this otherwise-excellent paper should be highlighted by the conference.

I have skimmed these appendices, but not closely checked the mathematics.

### Questions
Would the creation of central flows be easily created for other optimization algorithms, or do they depend upon specific characteristics of these two algorithms?  If they were second-order algorithms, would the derivation break down?

### Soundness
2

### Presentation
4

### Contribution
4
