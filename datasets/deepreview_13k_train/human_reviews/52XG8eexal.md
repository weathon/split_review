# State-space models can learn in-context by gradient descent

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Deep state-space models (Deep SSMs) have shown capabilities for in-context learning on autoregressive tasks, similar to transformers. 
However, the architectural requirements and mechanisms enabling this in recurrent networks remain unclear. 
This study demonstrates that state-space model architectures can perform gradient-based learning and use it for in-context learning.
We prove that a single structured state-space model layer, augmented with local self-attention, can reproduce the outputs of an implicit linear model with least squares loss after one step of gradient descent.
Our key insight is that the diagonal linear recurrent layer can act as a gradient accumulator, which can be `applied' to the parameters of the implicit regression model.
We validate our construction by training randomly initialized augmented SSMs on simple linear regression tasks. The empirically optimized parameters match the theoretical ones, obtained analytically from the implicit model construction. 
Extensions to multi-step linear and non-linear regression yield consistent results.
The constructed SSM encompasses features of modern deep state-space models, with the potential for scalable training and effectiveness even in general tasks. 
The theoretical construction elucidates the role of local self-attention and multiplicative interactions in recurrent architectures as the key ingredients for enabling the expressive power typical of foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper investigates the ability of SSMs to perform ICL through gradient descent during the forward pass over recurrent steps. It provides a theoretical analysis of various ICL scenarios, demonstrating that simple SSMs, equipped with input and output-dependent processing, can accurately mimic gradient descent when data is presented as a sequence. This theory offers an explanation for the capacity of modern SSMs to execute ICL and outlines a network circuit capable of handling such tasks. Empirical experiments confirm that the proposed circuit can effectively learn and perform small-scale synthetic tasks in practice.

### Strengths
(1) Enhances understanding of inductive biases in SSMs for ICL tasks.

(2) Bridges key domains such as SSMs, ICL, and mechanistic interpretability.

(3) Demonstrates generality by extending results to multi-step cases, multiple layers, and multi-dimensional data.

(4) Empirical analysis shows practical alignment with the theory-based construction in simple cases.

(5) Clarity: While some aspects could be improved (such as adding a figure to illustrate the main ideas in Section 3.1), the paper is clear, well-motivated, and easy to follow. It starts with simple cases and provides clear definitions, making it an enjoyable read!

### Weaknesses
 (1) The authors have **overlooked important related work in this domain**. For example, [1] presented at NeurIPS 2016, demonstrates that **RNNs can perform gradient descent during the forward pass**. Additionally, Section 3.1 in the current paper shares several similarities with Section 2 of [1]. To be clear, this is not an accusation of plagiarism, but rather an indication of missing key references. While there is a difference in scope (RNNs versus SSMs), this oversight reduces the originality of contribution #1. I kindly ask the authors to specify the principal differences between the approach taken by [1] and the approach used by SSMs in their work to better highlight the novel contributions. 

(2) **Overlooks simple alternative approaches:** While the theoretical analysis is accurate, the authors overlook significant alternative approaches. References [2-4] demonstrate the connection between S6 layers and attention, showing that S6 can be more expressive than attention without the softmax. Additionally, various ICL studies for transformers omit the softmax (see [5-6] as an example), allowing direct conclusions that could extend to SSMs. **Given the extensive exploration of ICL capabilities in transformers, discussions on the ICL potential of SSMs should consider this reduction approach**. I recommend that the authors evaluate whether this approach could yield additional theoretical developments to strengthen their analysis. Moreover, I suggest that the authors explicitly state the advantages of their approach compared to the proposed alternatives. For instance, Section 3 introduces specific circuits that cannot be achieved through simple reductions. 

(3) **Understanding ICL in SSM variants can be enhanced** by examining their sub-components. Previous research indicates that S6 layers exhibit significantly better ICL capabilities than earlier SSMs [7]. However, while the authors highlight input and output-dependent processing as crucial features, they do not empirically ablate these features across various ICL tasks, nor do they provide a detailed theoretical analysis to substantiate this claim explicitly. I recommend adding a subsection that explores these aspects in depth. It is also important to note that input- and output-dependent processing can be implemented through various gating mechanisms. Hence, this claim could be considered somewhat ambiguous, as gated state-space models have been previously studied without demonstrating the same level of ICL capabilities as models like Mamba / S6.


(4) **The claims regarding GD-SSM** (“Our construction, which we call GD-SSM, is not restricted to in-context learning tasks and performs well on general-purpose prediction problems”) do not hold, and much **more empirical analysis is required to justify** them.

### Questions
Please see weaknesses 1-3.

### Soundness
3

### Presentation
3

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
This paper investigates how state-space models (SSMs) can perform in-context learning through gradient descent. The authors provide both theoretical and empirical evidence that SSMs augmented with local self-attention can emulate gradient descent on implicit regression models. Their key insight is that the diagonal linear recurrent layer in SSMs can act as a gradient accumulator.

### Strengths
- To my knowledge, the insight viewing SSMs as a gradient accumulator allowing them to emulate gradient descent on in-context learning tasks is novel and the combination with local self-attention for preprocessing is interesting
- The mathematical theory appears to be sound
- The presentation of the material and step by step walk through of the theory from simple cases to more complex is clear and helpful
- The theoretical findings potentially point to a mechanistic understanding of architectural requirements (for SSMs or other models) that enable types of in-context learning

### Weaknesses
 - While the paper does a good job of explaining the theory and formulation of GD-SSM and empirically validating GD-SSM on regression tasks, I didn't feel like it shed that much insight into the currently used SSM variants used in practice.
   - Note that line 488 says: "These findings not only explain the success of recent SSM variants in in-context learning tasks but
also provide valuable insights for the design of future sequence models."
   -  Note that Lines 052-053 say, referring to the modern SSM variants : "Which features of these successful models contribute to in-context learning, as opposed to earlier variants? Using a constructive approach, we pinpoint input-dependent input and output processing, as the key features required for in-context learning".
   - But I do not think the current version of the paper supports either of the claim that this paper sheds light on these questions
   - The approach constructed seems to be very different from those used in practice. In addition, the methods commonly used in practice do not appear to do well on the regression ICL tasks in this paper. So it is unclear what I should take away from this related to prior SSM methods?
   - I think the empirical results were an opportunity to provide insight here, but didn't seem to fully achieve this. Please see my questions below which may clarify this for me.

- Related to the above, the experimental section is light on architectural details, making it hard to determine what exactly is being compared empirically and what conclusions can be drawn. Please include more experimental details including the architectures and hyperparameters.

- The paper is often unclear on the terminology of local self-attention and local linear self-attention. The formulation in Section 3.2 appears to only require local linear self-attention, yet other times in the paper local self-attention is used. In the related works section the two are contrasted. I would recommend being very explicit and consistent on this point as the two are very different.

- The paper is limited to regression style in-context learning. This is interesting and amenable to theoretical analysis, but also limits the impact of the investigation. See https://arxiv.org/abs/2401.12973 and https://arxiv.org/abs/2402.04248 for other papers that have empirically investigated other types of in-context learning in different architectures.

### Questions
1. Can you explicitly define GD-SSM? Perhaps even provide pseudo-code? What are its learnable parameters? It is defined in 283 after the fact, but I think a more explicit definition would be helpful.

Questions related to experiments and first two bullets in Weaknesses section above:

2. How do the results in this paper explain the success of recent SSM variants (as claimed in lines 488)? Line 052-053 say : "Which features of these successful models contribute to in-context learning, as opposed to earlier variants? Using a constructive approach, we pinpoint input-dependent input and output processing, as the key features required for in-context learning". I hoped the paper would provide insight into this question. However, it seems that the constructed GD-SSM is quite different from the currently used SSM architectures (e.g. Griffin, Mamba), and performs much better empirically in the experiments. Meanwhile the currently used SSM architectures do not seem to perform regression in-context learning (at least for one layer). So how do the results in this paper answer (or point to answering) the first question in line 052 or support the claim in line 488? This is my main question regarding this paper. I list some additional questions below that are an attempt to clarify some of the presented empirical results below.

3. Why does Griffin do so poorly compared to linear transformers and S5? Shouldn't Griffin be a mix of sliding window attention and SSM (the RG-LRU), making it similar to the GD-SSM formulation? Or is the model referred to as Griffin just RG-LRU?

4. Why does the time-invariant S5 appear to consistently outperform the input-dependent Mamba and Griffin models (even though all fail to converge)? I would have expected the models with input-dependent dynamics to perform ICL better.  Is this difference at all interesting?

5. Does it benefit the other architectures (1 layer linear attention, S5, Griffin, Mamba) to also provide them with the local self-attention preprocessing? Shouldn't they then be able to potentially learn the GD-SSM model if provided this? If not, why not?

6. Can 2 layers of the SSMs solve the task? Note that combining the local self attention with the diagonal SSM is a combination of 2 sequence processors.


Other questions and comments:

7. Where is the 1-step GD in Figure A?

8. In Figure 4B, the 1 or 2 layer GD-SSM formulation always seems to achieve lower loss than the corresponding number of steps GD model. Why is this? What happens if we compare more layers and more steps, e.g. 5 or 10 steps/layers? 

9. Note that the color scheme in Figure 4C etc is hard to read and tell which line corresponds to which model.

10. Note that LSA is first introduced in equation 2, but only later defined in line 119.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In-context learning (ICL) is one of the surprising capabilities of LLMs at scale. Seminal results have shown that Transformer-based architectures have this ability and more recent ones confirmed that SSMs also do. This work studies shows that SSMs can implement ICL by gradient descent. They provide a constructive proof showing that 1 layer can implement one GD step and confirm empirically on toy tasks that the networks find this solution.

### Strengths
The paper is overall well written and easy to follow. The theoretical part is sound and experiments convincingly demonstrate the paper's claims in toy settings.

### Weaknesses
I am concerned by the novelty of this paper. [Zucchet et al. 2023](https://arxiv.org/abs/2309.01775) show that 1 SSM layer can implement any linear self-attention layer. This results implies that any ICL algorithm LSA can implement, an SSM can. This holds for 1 GD step studied in this paper, but also for any other algorithm the community has been studying over the last few years. Additionally, this paper also have very similar experiments to the ones presented here. 

To the best of my understanding and as mentioned above, the results presented here are a subset of the results presented in Zucchet et al. 2023. Can the authors compare their work to that paper and highlight what their insights are?

### Questions
To the best of my understanding and as mentioned above, the results presented here are a subset of the results presented in Zucchet et al. 2023. Can the authors compare their work to that paper and highlight what their insights are?

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper imitates Transformers learn in-context by gradient descent(https://arxiv.org/abs/2212.07677). This paper proves that a single structured state-space model layer with local self-attention can reproduce the outputs of an implicit linear model with least square loss. (The task considered is not general)

### Strengths
1. The paper demonstrates that the state-space model with LSA can learn in-context learning tasks on linear and nonlinear regression problems. While I do not dispute the claim that state-space models can achieve in-context learning via gradient descent, my concern lies in whether the specific modification introduced warrants the detailed calculations provided. The conclusions, as presented, seem to offer limited insights into how this work might advance research on improving in-context learning capabilities. A clearer connection to meaningful improvements in this area would significantly enhance the paper's contribution.
2. The experiments compare the state-space model with Griffin and Linear Transformer, but they are restricted to shallow architectures of 1 or 2 layers. This setup is inconsistent with typical in-context learning scenarios, where models need to be sufficiently large for emergent phenomena and meaningful in-context learning capabilities to surface. The current experiments do not effectively capture these dynamics, making it difficult to observe such phenomena in shallow sequence models. Expanding the experiments to include deeper architectures would provide a more realistic assessment of in-context learning in state-space models.

### Weaknesses
1. The paper addresses a theoretical statement about the transformer model, specifically that it can learn in-context through gradient descent. However, this concept is already well-known and documented. In theoretical research, it is widely recognized that transformers, convolutional models, and recurrent models, such as state-space models, are universal approximators and are capable of learning continuous target relationships. Therefore, demonstrating the same for state-space models does not appear to offer significant theoretical advancement. If the authors wish to underscore the importance of this work, I would recommend showing that previous work in approximation theory does not extend to the in-context learning case. Without this distinction, the contribution seems to fall within a subset of known results that hold limited value for theoretical study.

2. The notion of in-context learning, as presented, lacks practical interest. Simply stating that a model "can learn" through in-context learning is insufficient, as the same argument could be made for various methods, including Newton's or quasi-Newton's methods. There is no compelling reason for practitioners to assume that, when state-space models engage in in-context learning, the behavior in terms of loss convergence or asymptotic rates would align with that of gradient descent. Clarifying this distinction would strengthen the paper’s contribution. Could you provide empirical comparisons of convergence rates or asymptotic behavior between your method and alternatives like Newton's or quasi-Newton's methods.

3. The paper introduces a state-space model with local self-attention, which is not a commonly adopted approach in practice. It would be more beneficial to align the framework with models that are widely used in real-world applications. A method akin to the linear transformer might be more appropriate and could provide a better point of reference for practical utility.

### Questions
1. See Weakness.
2. The behavior of GD and 1-D GD-SSM appears different. Could the authors provide an explanation for this discrepancy? Clarifying this would help the readers better understand the distinctions in learning dynamics between these approaches.
3. Figure 3: The font size in Figure 3 is too small and could be increased for readability.

### Soundness
3

### Presentation
2

### Contribution
1
