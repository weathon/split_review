# Demystifying the Token Dynamics of Deep Selective State Space Models

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Selective state space models (SSM), such as Mamba, have gained prominence for their effectiveness in modeling sequential data. Despite their outstanding empirical performance, a comprehensive theoretical understanding of deep selective SSM remains elusive, hindering their further development and adoption for applications that need high fidelity. In this paper, we investigate the dynamical properties of tokens in a pre-trained Mamba model. In particular, we derive the dynamical system governing the continuous-time limit of the Mamba model and characterize the asymptotic behavior of its solutions. In the one-dimensional case, we prove that only one of the following two scenarios happens: either all tokens converge to zero, or all tokens diverge to infinity.  We provide criteria based on model parameters to determine when each scenario occurs. For the convergent scenario, we empirically verify that this scenario negatively impacts the model's performance.  For the divergent scenario, we prove that different tokens will diverge to infinity at different rates, thereby contributing unequally to the updates during model training.  Based on these investigations, we propose two refinements for the model: excluding the convergent scenario and reordering tokens based on their importance scores, both aimed at improving practical performance.  Our experimental results validate these refinements, offering insights into enhancing Mamba's effectiveness in real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the dynamical properties of tokens in a pre-trained Mamba model, a type of selective state space model (SSM). Despite the empirical success of Mamba, a comprehensive theoretical understanding of its internal mechanisms is lacking in various areas. The authors address this gap in one area by deriving the dynamical system governing the continuous-time limit of the Mamba model and analyzing its asymptotic behavior. In the one-dimensional case, they prove that the system exhibits one of two behaviors: either all tokens converge to zero or diverge to infinity. They provide criteria based on model parameters to determine which scenario occurs. Empirically, they verify that the convergent scenario negatively impacts model performance, while in the divergent scenario, tokens diverge at different rates, contributing unequally during training.
Based on these findings, the authors propose two refinements to improve model performance:
* Excluding the Convergent Scenario: By ensuring certain conditions on model parameters, they prevent the tokens from converging to zero.
* Reordering Tokens: They reorder tokens based on their importance scores to account for the unequal contribution during training.

Experimental results on language modeling and image classification tasks validate these refinements, showing improved accuracy and convergence speed.

### Strengths
- Originality: The paper addresses a gap in the theoretical understanding of selective state space models, specifically Mamba, by analyzing the continuous-time dynamics of tokens.
- Theoretical Rigor: Provides rigorous mathematical proofs for the asymptotic behavior of tokens, offering clear criteria based on model parameters.
- Practical Implications: The findings lead to actionable refinements that improve model performance, validated through experiments on language modeling and image classification tasks.
- Clarity: The paper is well-structured, with logical progression and clear explanations that make complex mathematical concepts accessible.

### Weaknesses
 - Simplifying Assumptions: Using time-independent parameters and excluding other layers for mathematical convenience may oversimplify Mamba's actual behavior in practical settings. The analysis focuses on a simplified, continuous-time limit of the Mamba model, which may not fully capture the complexities of the discrete-time implementation used in practice. Specifically, the assumption of time-independent parameters neglects the dynamic nature of the model's weights during training, potentially leading to discrepancies between theoretical predictions and empirical observations. Furthermore, by excluding other layers, such as normalization layers and non-linear activation functions, the analysis might not accurately reflect the behavior of tokens in a complete Mamba architecture. This simplification could limit the generalizability of the theoretical findings to real-world scenarios.
- Experimental Scope: Though supportive, experimental validation could be more extensive. Including additional datasets and comparisons with other models would strengthen the claims. The experimental validation is limited in scope, primarily focusing on language modeling and image classification tasks. While the results are promising, the lack of experiments on a broader range of tasks and datasets makes it difficult to assess the robustness and generalizability of the proposed refinements. Moreover, the absence of comparisons with other state-of-the-art models, including other sequence models and Transformers, limits the ability to contextualize the performance gains achieved by the proposed approach. A more thorough evaluation would involve benchmarking against a diverse set of models and tasks, providing a more comprehensive understanding of the strengths and weaknesses of the proposed refinements.
- Limited Discussion on Limitations: The paper could benefit from a more thorough discussion of the limitations of the proposed refinements and potential challenges in practical implementation. The discussion of limitations is somewhat brief, failing to fully address the potential challenges in practical implementation. For instance, the computational overhead of the token reordering technique, while mentioned, could be explored in more detail, including its impact on training time and memory usage for larger models and datasets. Additionally, the paper could benefit from a more in-depth discussion of the sensitivity of the proposed refinements to hyperparameter settings and the potential for instability or performance degradation under certain conditions. A more comprehensive analysis of these limitations would provide a more balanced and realistic assessment of the proposed approach.

### Questions
1. Could you extend the theoretical analysis to higher-dimensional cases?
2. Can you provide more details on how the token importance scores are computed and how the reordering is implemented? What is the computational overhead of this process?
3. Do your findings and proposed refinements generalize to other selective state space models beyond Mamba?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper "Demystifying the Token Dynamics of Deep Selective State Space Models" explores the theoretical behavior of tokens in the Mamba model, a type of Selective State Space Model (SSM) used in sequence tasks like language modeling and image processing. Despite Mamba's empirical success, its internal dynamics are not well understood.
The authors show that in a one-dimensional case, tokens either converge to zero or diverge to infinity, depending on model parameters. Convergence harms performance, while divergence leads to unequal contributions from tokens during training. To address this, the paper proposes two improvements: eliminating the convergent scenario and reordering tokens by importance. Experiments confirm these refinements improve accuracy and speed, particularly in image classification tasks.
This study offers new theoretical insights into token dynamics and suggests practical adjustments to improve the Mamba model's performance.

### Strengths
- **Originality**: The paper makes a meaningful contribution by exploring the often overlooked internal dynamics of tokens in Selective State Space Models (SSMs), specifically the Mamba model. While SSMs are well-known for their efficiency in sequence modeling, this work tackles a fresh problem—understanding how token behavior impacts model performance. By analyzing the continuous-time limit of token dynamics, the authors open up a new line of inquiry that could lead to more informed model designs and optimizations. The refinements proposed—eliminating the convergent token scenario and reordering tokens by their importance—are practical ideas that could lead to significant performance gains.
- **Quality**: The paper is technically solid, with rigorous theoretical analysis that provides clear criteria for determining whether tokens in the Mamba model will converge to zero or diverge to infinity. This kind of formal, mathematical foundation is a strong aspect of the paper, ensuring that its claims are well-supported. The empirical results on large-scale tasks such as ImageNet classification offer clear evidence that the proposed refinements are effective in improving model accuracy and convergence speed. The experiments directly tie into the theoretical findings, showcasing a strong link between the analysis and practical outcomes.
- **Clarity**: The paper is clearly structured, with a logical flow from the problem statement, through the theoretical analysis, to the empirical validation. The technical content, while dense in some areas, is well-explained, and the use of diagrams and tables helps to clarify key findings. The authors do a good job of contextualizing their work within existing research, making it clear how their contributions build on prior work in SSMs and neural ODEs. Overall, the clarity of the presentation allows readers to follow the complex theoretical insights without becoming lost in technical details.
- **Significance**: The significance of the work lies in its potential to impact both the theoretical understanding and practical application of SSMs. By uncovering how token dynamics influence model performance, the paper provides a foundation for improving not only Mamba but other models that rely on similar state-space mechanisms. The proposed refinements—removing harmful convergent behaviors and reordering tokens based on importance—offer actionable insights that can directly improve model training efficiency and accuracy, as shown by the experimental results. Given the growing use of SSMs in fields such as language modeling, computer vision, and reinforcement learning, these contributions could lead to broader advancements in how such models are designed and optimized.

### Weaknesses
 - **Theoretical Scope is Too Narrow**: 
While the paper makes a valuable contribution by exploring token dynamics in the one-dimensional case, the focus is too limited. The analysis is restricted to this specific setting, which weakens the generalizability of the conclusions. The authors mention extending their findings to higher-dimensional cases, but without any concrete exploration of these cases, the scope of the theoretical contribution feels incomplete. Actionable Insight: A more comprehensive exploration of higher-dimensional token dynamics should be included. If full proofs are too complex for this paper, at least preliminary results or conjectures, backed by empirical evidence, would make the work stronger. Additionally, comparisons with more sophisticated state-space approaches (such as diagonal vs. non-diagonal state space models) could show how the proposed ideas generalize.
- **Insufficient Diversity of Experiments**: 
The empirical validation is focused on tasks like ImageNet classification, which is a strong benchmark, but does not provide sufficient diversity to substantiate the claims made in the paper. The experiments demonstrate the refinements' effectiveness in vision tasks, but the proposed improvements—such as reordering tokens by importance—are presented as potentially broadly applicable to sequence models across various domains. The paper could have benefited from testing the refinements on different types of data and tasks, such as language modeling or reinforcement learning, where SSMs are also commonly applied. Actionable Insight: Expanding the experiments to include tasks like language modeling(e.g., WIKITEXT or other sequence-based datasets) or sequence-based tasks in reinforcement learning would provide stronger evidence that the proposed refinements generalize beyond vision tasks. This would substantiate the claim that these refinements are broadly beneficial across domains.
- **Shallow Investigation of Practical Impact**: 
The paper claims that eliminating the convergence scenario and reordering tokens significantly improves the performance of Mamba. While the empirical results show improvements in accuracy and convergence speed, there is little discussion on the practical implications of these refinements in real-world applications. For instance, the computational cost of implementing token reordering or of checking for convergence scenarios during training is not discussed. Additionally, the analysis of why these changes work, especially in larger-scale, practical deployments, is somewhat superficial. Actionable Insight: Including an analysis of the computational overhead or potential trade-offs of implementing these refinements in large-scale models is crucial for practical relevance. Furthermore, deeper explanations of why these adjustments improve performance, with specific references to token dynamics, would enhance the practical significance of the work. For instance, analyzing the impact of token reordering on different architectures or showing how it interacts with other model components would provide more actionable insights for model developers.
- **Limited Novelty of Some Contributions**: 
While the paper presents the analysis of token convergence and divergence as a central contribution, this analysis—though useful—builds heavily on well-known concepts from continuous-time neural networks (e.g., neural ODEs) and does not introduce significantly new ideas. The observation that token dynamics can either converge to zero or diverge to infinity, depending on model parameters, is mathematically rigorous but not particularly surprising in the context of dynamical systems. This reduces the novelty of the contribution. Actionable Insight: To strengthen the originality of the work, the authors could extend the analysis beyond what is currently expected in dynamical systems and neural ODEs. For instance, they could explore more complex behaviors in the interaction between tokens, such as the emergence of periodic behavior, chaotic dynamics, or the impact of noise on the stability of the token trajectories. Alternatively, a deeper comparison with transformer-based models (such as interpreting token dynamics in transformers vs. Mamba) would increase the novelty of the work.
- **Lack of Comprehensive Comparison to Prior Work**: 
The paper briefly acknowledges prior work on SSMs and transformers but lacks a comprehensive comparison to alternative models. Given the ongoing research in state space models and their applications, a more thorough evaluation against recent models like GSS (Generalized State Spaces) or HiPPO-based models would provide a stronger benchmark for the proposed refinements. Additionally, since the paper suggests that Mamba can be a more efficient alternative to transformers, it should compare the computational efficiency and performance against contemporary transformer models on long-range sequence tasks. Actionable Insight: The authors should include a more detailed experimental comparison against state-of-the-art models in SSMs and transformers. They should also explicitly compare their proposed refinements with other model optimizations, such as low-rank approximations or efficient attention mechanisms in transformers. This would give the community a clearer picture of where Mamba, with its refinements, stands in the current landscape of sequence modeling.

### Questions
**Summary of Actionable Improvements**:
- Expand the theoretical analysis to higher dimensions or at least provide empirical evidence for higher-dimensional token dynamics.
- Broaden the experimental validation to include diverse tasks beyond vision (e.g., language modeling and reinforcement learning).
- Discuss the computational costs and trade-offs of the proposed refinements in real-world applications.
- Increase the novelty by exploring more complex dynamical behaviors or offering a deeper comparison with existing models like transformers.
- Provide a more comprehensive experimental comparison to other recent SSMs and transformers, including computational efficiency.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper provides a theoretical analysis of the dynamical properties of tokens in input-varying SSMs, particularly focusing on the Mamba architecture. The authors derive and analyze the continuous-time limit of the Mamba model, characterizing how tokens evolve through the network. Their key finding is that under several assumptions, in the one-dimensional case, tokens either all converge to zero or all diverge to infinity, with specific criteria determining which scenario occurs. For the divergent case, they prove that different tokens diverge at different rates, suggesting unequal contributions during training. Based on these theoretical insights, they propose two practical improvements: 1. excluding scenarios where tokens converge to zero, as this negatively impacts performance, and 2. reordering tokens based on importance scores. They validate these improvements experimentally on language modeling and image classification tasks.

### Strengths
- I believe this is the first paper to present theoretical analysis related to how the token dynamics evolve through the networks across the depth of deep SSMs. This can be valuable to help provide insights into how these models process information
- The mathematical analysis appears to be sound and the empirical results provide some evidence that the theory can lead to insights that can improve performance
- The paper is well-structured and Figures 1-3 are useful.

### Weaknesses
 - The effects of the assumptions made for the analysis are not thoroughly explored
    - The analysis ignores the effects of important practical additions used in these networks such as layer normalization, short convolutions and the dense linear operations or MLPs often used between layers. The analysis focuses on a simplified version of Mamba, and it's unclear how much the theoretical results apply to the full architecture. For instance, layer normalization introduces a non-linear scaling and shifting of the token embeddings which could significantly alter the dynamics. Similarly, the short convolutions and MLPs introduce additional non-linear transformations and interactions between tokens that are not accounted for in the analysis.
    - The analysis assumes weights are shared across layers, which is not the case in standard implementations. This assumption simplifies the analysis but may not reflect the behavior of the model in practice. The weights in each layer are typically learned independently and can have different distributions and magnitudes, which could affect the token dynamics.
    - The analysis assumes the one-dimensional case and excludes the possibility of complex eigenvalues in the input/output projection matrix. This is a significant simplification, as the token embeddings are typically high-dimensional vectors. The behavior of the system in high dimensions, with potentially complex eigenvalues, could be very different from the one-dimensional case considered in the paper. The presence of complex eigenvalues could lead to oscillatory or rotational dynamics that are not captured by the current analysis.
    - All of these assumptions are fine for the sake of getting started with a simple case of analysis, but I would have liked to have seen a more thorough discussion of these assumptions and exploration in the empirical results.

- The empirical results seem promising but modest. In addition, it is unclear how much the proposed improvements actually help. In particular, the scenarios investigated empirically seem to have strayed far from the assumptions in the theory (e.g. I believe no weight sharing, higher dimensions, and layer norm, short conv and MLPs included). I would have liked to have seen a series of ablations that build up from the simplified case considered in the theory to the full models that are used in practice. This would give a better sense of how important the assumptions are, and how much the proposed improvements are contributing to the performance boost. For example, starting with a model that closely matches the theoretical assumptions (no layer norm, convs, or MLPs, weight sharing, 1D inputs) and then progressively adding these components would allow for a more controlled study of their impact.

- More care should be taken to distinguish between the depth direction of the network and the sequence direction of the network. SSMs such as S6 come from the prior S4 and S5 methods which are based on continuous-time parameterized ODEs that evolve along the sequence length (often thought of as the "time" direction) and are then discretized. In this work, the continuous-time formulation is taken to be across the depth (i.e. layers) of the network and the "time" is referred to in this depth direction. However, this could lead to much confusion and I would recommend being much more explicit about what the "time" direction is more often throughout the paper to prevent confusion. E.g. in line 212, it is very unclear that time-independent parameters here is meant to mean the parameters are shared across layers and not shared across the sequence length (i.e. a LTI SSM sytem).

### Questions
My main concerns I would like addressed are listed in the weaknesses section. Here are some additional comments or questions:

- Perhaps you could start with a model pretty close to that presented in the theory: no layernorm, convs or extra MLPs; weight sharing, 1 dimensional, and then ablate these different choices. How much do each of these choices affect the results? Would also be interesting to see how the results vary with a varying number of layers, e.g. increasing the number of layers to better approximate the "continuous-time limit".

- Wikitext 103 is very much a toy language task that is known to be very sensitive to hyperparameters. How robust are these results to different random seeds? Or different hyperparameters?

- Line 075: The input, output, and state matrices are mislabeled


Update: I have increased my score to reflect my updated view of the paper after the rebuttal period.

### Soundness
2

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
3

### Summary
Deep selective state-space models have achieved promising results on sequence modelling tasks. Yet, theoretical understanding of these models remain limited. This paper proposes to study how the embedding of different tokens evolve as they are processed through Mamba layers. In particular, they show that they either converge to 0 or diverge to infinity, based on some criteria that they provide. Importantly, this divergence speed depends on the position of the token. Motivated on their findings, the authors propose some modifications to the standard Mamba architecture that improve its performance.

### Strengths
Given the very little theoretical understanding of these models, such a theoretical contribution is valuable to the community. Despite its theoretical focus, the paper is easy to follow and one can grasp the main insights without having to delve into the math. The empirical improvements the theory motivates seem to be significant.

(Score increased from 5 to 8 after the discussion period)

### Weaknesses
My main concern with the paper is that its conclusions remain limited compared to what the analysis could, in my opinion, deliver. Here are a few questions that would help, once answered, to improve this point:
- How does the token dynamics in Mamba compare to the ones of Transformers? Are there some qualitative differences? Does it lead to some insights on the different inductive biases of these architectures.
- Is it possible to extend the analysis to the bidirectional case, i.e. without the causal masking (the implicit attention matrix would not be lower triangular anymore)?
- Similar question than the previous point but this time to extend the analysis to gated RNNs such as LSTMs or GRUs, whose simplified versions have some similarity with Mamba.

While it is totally fine to restrain the theoretical analysis to the 1D, simulations assessing whether the conclusions of the analysis on the 1D case also hold in higher dimension are missing. One example of such simulations would be to initialize a Mamba layer in the same way as it is usually done in practice, give it random inputs, and observe how tokens evolve. It might be interesting to play with how correlated the random inputs are and with the magnitude of $a$.

Finally, I remain suspicious of the empirical results given that no learning rate tuning was reported. Without such tuning I find the results hard to trust.

### Questions
See above.

### Soundness
4

### Presentation
3

### Contribution
2
