# Improving equilibrium propagation without weight symmetry through Jacobian homeostasis

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
\Ac{EP} is a compelling alternative to the \ac{BP} for computing gradients of neural networks on biological or analog neuromorphic substrates. 
    Still, the algorithm requires weight symmetry and infinitesimal equilibrium perturbations, i.e., nudges, to yield unbiased gradient estimates.
    Both requirements are challenging to implement in physical systems.
    Yet, whether and how weight asymmetry contributes to bias is unknown because, in practice, its contribution may be masked by a finite nudge. 
    To address this question, we study generalized \ac{EP}, which can be formulated without weight symmetry, and analytically isolate the two sources of bias.
    For complex-differentiable non-symmetric networks, we show that bias due to finite nudge can be avoided by estimating exact derivatives via a Cauchy integral.
    In contrast, weight asymmetry induces residual bias  through poor alignment of \ac{EP}'s neuronal error vectors compared to \ac{BP} resulting in low task performance.
    To mitigate the latter issue, we present a new homeostatic objective that directly penalizes functional asymmetries of the Jacobian at the network's fixed point. 
    This homeostatic objective dramatically improves the network's ability to solve complex tasks such as ImageNet~32$\times$32. 
    Our results lay the theoretical groundwork for studying and mitigating the adverse effects of imperfections of physical networks on learning algorithms that rely on the substrate's relaxation dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Equilibrium propagation, an alternative to backprop requires weight symmetry and nudges to yield unbiased gradient estimates. Generalization of Equilibrium proportion to non-symmetric dynamical system exists but shown to work only for simple problems.  
The paper proposes an extension of holomorphic EP to non-symmetrical dynamical systems and shows good results across different vision benchmarks.

### Strengths
- Analysis of bias in gradient estimation is helpful to the reader. 
- Incorporating functional symmetry through the use of matching jacobians is an interesting idea. It’s similar to reconstruction error term used in methods like Target Propagation. Here, authors optimize the homeostatic loss with respect to all the weights as compared to using only feedback weights.

### Weaknesses
 - The paper is generally well written, though introduction is a bit complex if the reader is not aware of previous work (holomorphic EP).


### Questions
No further questions as such. The paper has good results across different vision benchmarks.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
_Disclaimer: I have reviewed this paper recently again at a different venue. It has since been revised slightly. Some of my comments still apply to this version and are copied here verbatim from my previous review._

The paper focuses on Equilbrium Propagation (EP), i.e. a learning algorithm for neural networks that was introduced relatively recently and aspires to be more biologically plausible and more suitable for analog hardware than back-propagation (BP). The theoretical version of EP relies on an infinitesimal perturbation (which is not feasible to achieve in physical settings) and on symmetric weights (which are also unrealistic in biology and constrain hardware design). The paper aims to understand the impact of each of these two issues separately. It achieves to do so in the "holomorphic EP" (hEP) setting, i.e. under the assumption of complex-valued neurons. The authors achieve this by extending the theory of hEP to asymmetric connectivity, where they show that it is possible to obtain exact estimates of the gradient despite finite perturbations, therefore suggesting that the bigger issue is weight asymmetry. They then proceed to tackle the problem of asymmetry by introducing a loss term that penalizes it directly, and they show experimentally that this term improves the performance of hEP significantly in asymmetrically-initialized networks, in certain visual tasks using a 4-layer convolutional network.

### Strengths
The paper is mostly nicely written and clear. The theoretical contributions of the paper are not trivial, as they require a deep understanding of a very specific algorithm i.e. the holomorphic version of EP, as well as a degree of comfort with certain mathematical concepts that is rare among neural network practitioners and possibly even theoreticians. More generally, the paper aims to contribute to an area that is of broad interest, as it relates to machine learning, neuromorphic engineering, and theoretical neuroscience. Furthermore, it truly advances the empirical results of the EP-related literature.

### Weaknesses
While this is obviously a valuable piece of work in certain respects, I believe it is also significantly limited in other key aspects.

Significance: The work ultimately aspires to improve aspects of backpropagation that are indeed important and relevant to multiple large disciplines (ML, neuromorphic hardware, neuroscience), however, concretely, the resulting contribution is very narrow. Namely, it improves the performance and the theoretical understanding of hEP somewhat, specifically in the case of asymmetric weights, but it doesn't resolve the problem of asymmetry completely, as can be seen in the performance comparison to symmetric weights (Table 2). Moreover, hEP is a specialized version of EP that makes additional assumptions for complex-valued networks, which limits the applicability and generality of the algorithm. Furthermore, EP itself more broadly is interesting but is a rather limited method in terms of achieving its goals of good performance, efficiency, useful hardware demonstrations, or deep learning, in comparison with other methods that have similar goals that have been more successful. Its biological compatibility could also be debated, given its requirement for multiple network-wide iterations before a weight update. Therefore, it could be argued that the significance of the results only relates to a very narrow subfield. Furthermore, the theoretical advance separating the impact of the finite nudge from that of the asymmetry in hEP is not trivial, but I wonder how useful it is to the ICLR community, beyond the very narrow sub-community that specializes in hEP. In the broader picture, and given the already existing better-working alternatives, the progress made here towards biological plausibility or neuromorphic computation seems small, in my view.

Novelty: The main novelty of the paper is in the theoretical results, since the empirical fact that improving performance by dealing with asymmetric weights is not a new result. Nevertheless, I suspect that to someone with a good understanding of the earlier mathematical work that introduced hEP (Laborieux & Zenke, NeurIPS 2022) the new theoretical results might not be very surprising. However, it should be noted that I am not in a position to judge this fully. In any case, the insight from the theory is the impact of asymmetrical weights, relative to that of finite nudge, which seems to be also covered by the empirical result, therefore the added value from the theory in this case might not be substantial. Regarding the paper's empirical or practical contributions, some novelty exists in the objective function that penalizes asymmetries in the weight matrix. However, the novelty of this is limited because much older learning rules that achieve weight symmetry do exist (Kolen & Polak, IJCNN 1994; see also Payeur et al., Nat. Neurosci. 2021). In fact, these rules do not rely on global iterative equilibria, so the present paper's implementation of learnable weight symmetry could be characterized as a step-back in this regard. It should be recognize though that the new method is applicable when the connectivity is not reciprocal, whereas previous ones probably were not.

Contextualization in the literature: The paper does (now) cite some of the works that had similar aims, but only in passing, only in the discussion as opposed to the motivation section, discounts the better empirical results that the other works achieved, attributing this only to the lower simulation cost of the alternatives, and does not mention that some of these methods not only perform better in classification benchmarks, but also require fewer assumptions for compatibility with biology and for efficiency in learning hardware, e.g. by circumventing the need for backward passes of information completely.
Some examples are: Payeur et al., Nat. Neurosci. 2021; Greedy et al., NeurIPS 2022; Mengye Ren et al., ICLR 2023; Journé et al., ICLR 2023.

It would be very helpful to the readers and the targeted research communities if the authors motivated their choice to focus specifically on EP as opposed to alternative methods that have similar goals, but don't have the same limitations. This could be a way to mitigate the weaknesses of the paper to some extent.

To be clear, some of the algorithm's limitations in comparison to alternatives are: reliance on complex-valued networks; constraints in network architecture and depth, expensive simulations for the equilibrium dynamics (e.g. a multi-GPU cluster was used according to the supplementary material, despite the small networks and simple tasks); questionable bio-plausibility of the necessity for equilibrium; hardware implementations of EP are mostly theoretical. To their credit, the authors have mentioned some of these limitations in the discussion. They also provided some solutions or counterarguments, however these are largely theoretical, vague, or speculative.

All in all, I believe that the work's value might be able to increase if the manuscript could explain its motivations and its contributions in a context broader than the EP literature. At present, this is not clear enough or supported well enough, in my view.

### Questions
The discussion suggests that "analog substrates could achieve this relaxation “for free” through device physics (Yi et al., 2023; Kendall et al., 2020)". Could the authors please clarify, does any analog substrate achieve the relaxation "for free", or what are the requirements, more specifically? For example, the Kendall et al. reference seems to rely on a very peculiar and ad hoc hardware implementation.

Also, in the most efficient hypothetical hardware implementation, I suspect that "for free" is far from the truth, as, even there, the relaxation phase would include multiple weight updates, which consume power; in fact commonly more power than weight reads. Wouldn't alternative algorithms that do not have this relaxation phase be significantly more efficient? The provided references do not seem to disagree with this, so in which sense do the references support the "free" claim?

I would appreciate the authors' insight in these questions.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied the weight asymmetry in the weight transport problem extending the Holomorphic Equilibrium Propagation algorithm (hEP), through investigations about the Jacobian of the network, with experiments and theoretically analysed the reasons for the experimental results. Based on the analysis results, some new features were proposed to enable the algorithm to evade the need for perfect weight symmetry without affecting the functional symmetry. A new form of Jacobian homeostasis was introduced to maintain functional symmetry, without directly addressing weight symmetry. Finally, several experiments, including the investigation of weight symmetry evolution during training and comparative experiments, were conducted to verify the effectiveness of the proposed algorithm, and the work’s performance exceeded the networks with Recurrent Backpropagation (RBP), even on larger datasets.

### Strengths
*Relatively new perspective

This paper shows a new perspective on studying the weight transport problem with the Jacobian of the network. It explains the connections between weight symmetry, functional symmetry and Jacobian homeostasis.

*Relatively rigorous analysis and persuasive experiments

This paper shows the efforts in investigating the weight symmetry evolution during training in section 4. If the observations could be discussed more deeply with the figure would be better. 

*The part about ‘Jacobian homeostasis improves functional symmetry’ in section 4 is very detailed and well analysed.

### Weaknesses
 *Some expressions with flaws

Although ‘hEP’ is the abbreviation of ‘holomorphic Equilibrium propagation’ can be understood after reading. However, this abbreviation has not been indicated in parenthesis when mentioning its full term for the first time.
The last sentence ‘It is worth nothing that…’, in Definition 1 of section 2.2, might be miswritten, which should be ‘It is worth noting that…’ based on the context. Also in this paragraph, the sentence after Eq. (6) ‘Importantly, the quantities …, which applies only to EBMs.’, is a little longer and complex. It might confuse readers, for convenience of understanding, it would be better to split it into two simpler sentences.

*Some disadvantages in the layout

In section 3.2, the paragraph with Eq. (9) is intersected by Figure 2, which could be rearranged to provide enhanced readability. The same disadvantages happen in Figure 3 and Table 1.

*The performance of the proposed method is relatively not so advanced. And the method for comparison is relatively not so new, making the work of this article not very convincing.

*The discussion of the experimental results in section 4 lacks depth. While the paper presents the evolution of weight symmetry during training, the analysis of these results, particularly in relation to the figures (Fig. 4 c, g, k), is superficial. The metric used to quantify symmetry, the ratio of the norm of the symmetric component to the sum of the norms of the symmetric and antisymmetric components of the Jacobian, is not sufficiently explained in the context of the observed trends. For example, the paper notes that the metric approaches one in Fig 4c, but does not explain why this is expected given the reciprocal connections. Similarly, the lack of convergence to one in Fig 4g is not thoroughly discussed, nor is the significance of the angle between forward and feedback weights in Fig 4k, beyond a simple statement that the homeostatic loss makes the angle smaller.

### Questions
Please refer to the above weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors suggest a modification to the holomorphic equilibrium propagation algorithm, that helps it deal with cases where the Jacobian is not symmetric, by adding a term which penalizes asymmetry of the Jacobian. They show this approach outperforms standard holomorphic equilibrium propagation.

### Strengths
The method improves over previous holomorphic equilibrium propagation in the applications tested. 

As someone who is not in this field, I found section 2 to be informative introduction to the area.

### Weaknesses
It was not entirely clear to me what the motivation for this work is. While the authors suggest that hEP is potentially biologically plausible, this seems like a stretch. Not only does it require neurons to do computations with complex numbers, but it also seems to require that the network settle to equilibrium at multiple phases of an ongoing oscillation. This does not seem likely in the brain: the period of the gamma oscillation is tens of milliseconds, which certainly would not allow enough time, and even the theta oscillation seems too fast for this. It also was not clear what computational advantages this might lead to in purely artificial systems for which biological plausibility was not important. Specifically, the authors should elaborate on how the proposed modification, which penalizes asymmetry of the Jacobian, translates to tangible benefits in terms of learning speed, accuracy, or efficiency compared to standard backpropagation or other state-of-the-art learning algorithms in artificial neural networks. The lack of a clear explanation of the potential advantages in artificial systems makes it difficult to assess the practical significance of this work beyond the theoretical contribution.

### Questions
Most important for me is to explain how this could be helpful in artificial learning systems, or why the problem of settling time does not apply to biological systems (which seems unlikely to be honest).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
