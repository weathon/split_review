# Mimetic Initialization Helps State Space Models Learn to Recall

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Recent work has shown that state space models such as Mamba are significantly worse than Transformers on recall-based tasks due to the fact that their state size is constant with respect to their input sequence length.
But in practice, state space models have fairly large state sizes, and we conjecture that they should be able to perform much better at these tasks than previously reported.
We investigate whether their poor copying and recall performance could be due in part to training difficulties rather than fundamental capacity constraints.
Based on observations of their ``attention'' maps, we propose a structured initialization technique that allows state space layers to more readily mimic self-attention. Across a variety of architecture settings, our initialization makes it substantially easier for Mamba to learn to copy and do associative recall from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper discusses the problem of improving recall/copying performance of State Space Models (Mamba). In particular, the paper claims that the difficulties in recalling from distant past instants of Mamba-like models are not due to the finiteness of their state and instead are due to poor initialization of their state transition maps. The main contribution of the paper is a novel structured initialization that allows state space layers to improve their recall capabilities.

### Strengths
The paper addresses an important and timely question on how to improve recall capabilities of modern State Space Models (SSMs). The proposed initialization is thoroughly ablated with many toy experiments designed to test recall/copy abilities.

### Weaknesses
While the proposed initialization scheme is sound, the novelty of the idea and technical contribution is incremental. Furthermore, the scope of the work is only limited to Mamba-like models and it is not generic to State Space Models (as stated in the title). To increase the scope of this work, given the relatively small scale experiments conducted, I’d suggest the authors extend their results to other SSM models like: GLA [5], LRU [4] and RetNet [8]. If only Mamba-like models are studied it would be good to modify the title since at the moment it reads as if it is applicable to “State Space Models” in general. 

The current manuscript is sometimes confused, SSM layers cannot mimic full Attention since the state of an SSM layer is fixed at the outset before seeing any sample, while the Attention’s state progressively increases as more and more samples are processed. This is a fundamental difference that cannot be bridged by keeping the same functional form of the SSM and only changing its initialization. Based on the results in the paper the proposed initialization avoids the collapse of the receptive field of the SSM’s state rather than mimicking Attention. 

Some important related references are missing, please see the Questions section below, can the authors discuss them? In particular, it is worth adding an explicit comparison with the analysis conducted in [4] which would help the reader contextualize the contribution of this work in the landscape of modern SSM models.

### Questions
1. Line 90, Why does valinna linear attention improve recall? This is not what has been observed in previous works and it is one of the main reasons for the relatively low adoption of vanilla linear Attention in modern architectures (linear Attention variants have been proposed since 2020, see [1, 2]). For example, the lack of recall capabilities of vanilla linear attention is one of the main motivations in [3] (this work is already mentioned in the manuscript). 
2. The paragraph starting in Line 354 is confusing (especially the sentence starting in Line 365). It is well know that Mamba layers are more expressive than Linear Attention as the latter is a special case of the former obtained when the state transition map does not fade (i.e. A=1), see for example [5, 6]. 
3. Line 202. What do the authors mean by “likely exploiting an implicit position embedding learned by the preceding Mamba layers”? Can they be more precise and point to an experiment showcasing that the Mamba layer learns positional encodings implicitly? 
4. Line 260. In past works [6, 7] it has been shown that such convolution is critical to further expand the state dimension of the SSM layer and that removing it could cause serious recall issues. Setting it to the identity (i.e. removing it) does not seem to be a good initialization in general. As this manuscript also mentions in Line 269. Do the authors have a theoretical motivation for the difference between Mamba 1 and Mamba 2 when it comes to the effects of the conv1d layer? 
5. The proposed method does not help for large scale experiments as the current initialization strategy is learned throughout training (line 520). Have the authors tested their initialization on larger scale language pre-training experiments? Do they expect their initialization to help when models are learned on larger scale experiments that are not only focused on copy/recall toy tasks?
6. Can the authors report the size of the state of the SSM models they studied in the paper? 


*Minor:*
Line 36 and Line 107, the Mamba layers are input dependent linear transformations, not time-dependent. 


[1] K. Choromanski et al., “Rethinking attention with performers”, arXiv preprint arXiv:2009.14794 (2020).

[2] S. Wang et al., “Linformer: Self-attention with linear complexity”, arXiv preprint arXiv:2006.04768 (2020).

[3] S. Arora et al., “Simple linear attention language models balance the recall-throughput tradeoff”, arXiv preprint arXiv:2402.18668 (2024). 

[4] A. Orvieto et al., “Resurrecting Recurrent Neural Networks for Long Sequences”, PMLR 202:26670-26698, 2023.

[5] S. Yang et al., “Gated Linear Attention Transformers with Hardware-Efficient Training”, arXiv preprint arXiv:2312.06635 (2023).

[6] L. Zancato et al., “B'MOJO: Hybrid State Space Realizations of Foundation Models with Eidetic and Fading Memory”. arXiv preprint arXiv:2407.06324 (2024).

[7] S. Yang et al., “Parallelizing linear transformers with the delta rule over sequence length.” arXiv preprint arXiv:2406.06484, 2024

[8] Y. Sun et al., “Retentive Network: A Successor to Transformer for Large Language Models”, arXiv preprint arXiv:2307.08621, 2023

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides an initialization scheme that allows SSM layers to learn copying tasks faster than the default initialization strategy.  They demonstrate that their mimetic initialization scheme allows SSM architectures to learn recall based tasks quickly.  They test their method on a variety of configurations, changing state size, embedding dimension, sequence length, and vocabulary size.

### Strengths
* The paper presents a wide array of experiments that vary state size, vocabulary size, sequence length, and embedding size to validate their results
* The paper is well written and easy to follow
* The paper provides a way to estimate the capabilities of SSM layers on copying tasks without expensive pretraining

### Weaknesses
 * This paper specifically trains for recall tasks, so it is unclear if this initialization scheme would lead to benefits for pretraining and not lead to performance regressions on non recall tasks
* Since hybrid models with attention layers that have inherent copying abilities combined with SSM layers are starting to become more prominent over pure SSM architectures, it is unclear if the copying abilities of the SSM components are of prime importance. Specifically, in many hybrid architectures, the attention layers are used sparingly, primarily for long-range context, while SSM layers handle the bulk of the sequence processing. The benefit of improved recall in the SSM layers might be marginal if the attention mechanism is already handling the long-range dependencies effectively. It would be beneficial to understand the interplay between the recall capabilities of the SSM layers and the attention layers in such hybrid architectures.
* The paper does not provide any results for pretraining with this initialization scheme. This is a significant limitation, as the ultimate goal of many sequence models is to perform well on downstream tasks after pretraining. Without pretraining results, it is difficult to assess the practical impact of the proposed initialization scheme. Furthermore, it is unclear how this initialization scheme would interact with other pretraining techniques, such as masked language modeling or contrastive learning.

### Questions
* Did the authors try pretraining with this initialization scheme?
* Can the authors provide evidence that this initialization scheme would not lead to performance regressions on the basic language modeling tasks or non-recall based benchmarks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the challenges faced by State Space Models (SSMs), such as Mamba, on recall-based tasks compared to Transformer architectures. The authors propose an initialization technique that encourages SSM layers to behave more similarly to self-attention. They empirically show that this initialization significantly improves Mamba's ability to learn memory-related tasks.

### Strengths
The paper is well-written and addresses a fundamental limitation of SSMs compared to Transformers, which is still not fully understood. The proposed approach of initializing SSM layers to mimic self-attention is well-motivated, and the observed attention patterns suggest notable similarities in the behavior of the two. The authors present extensive experiments across various tasks and architectural configurations, confirming that the initialization generally improves performance. They also provide comparisons with linear attention and pretrained Mamba models.

### Weaknesses
While the authors motivate the problem well, I find that they do not spend enough time discussing the broader implications of their work. From a theoretical perspective, the initialization approach is mainly heuristic, and does not provide a fully satisfactory understanding of why SSMs struggle with such tasks. On the empirical side, it is unclear whether the proposed initialization could improve performance on language-based tasks. Additionally, I have some concerns about the robustness and clarity of the presented results (see questions below). The differing behaviors between Mamba and Mamba2 are also somewhat concerning, given that the motivation for the initialization does not distinguish between the two. To sum up, I would like the authors to clarify the main theoretical and empirical takeaways of their work.

* The plots showing attention patterns should be explained more clearly. What inputs were used to generate these visualizations? How dependent are they on the seed used for training? How do these patterns evolve over time? I think that this last question would be especially interesting given that the authors try to align SSM and self-attention at initialization, and I wonder whether this causes the dynamics to overall behave similarly, or rather that they simply start close and gradually diverge.
* I find the results in Figure 3 strange: first, it seems that the initialization has relatively small effect on Mamba 1(with accuracy going at best up to 50%) while the Figure 2 shows every different behavior (>90%). Am I misunderstanding something? Second, even the results for Mamba 2 seem to vary greatly based on seed, which is quite undesirable and detracts from the conclusions of the paper.
* Why do the authors believe there is such a large difference between Mamba 1 and Mamba 2? They mention this briefly on line 307, but I think this question deserves more attention.
* Similarly, why should Mamba perform better than Linear Attention, given that it was initialized to mimic its behavior?

Minor:
* Line 258: "who suggest these weights should not be strictly equal" — It may be useful to provide some motivation for this.
* Figure 8 mentions Mamba 1/2, but I believe only Mamba 2 is shown.
* l.485: I believe that the authors use a fixed T_i to initialize all S_j (since L and M are different) but this is not clear.

### Questions
* The plots showing attention patterns should be explained more clearly. What inputs were used to generate these visualizations? How dependent are they on the seed used for training? How do these patterns evolve over time? I think that this last question would be especially interesting given that the authors try to align SSM and self-attention at initialization, and I wonder whether this causes the dynamics to overall behave similarly, or rather that they simply start close and gradually diverge.
* I find the results in Figure 3 strange: first, it seems that the initialization has relatively small effect on Mamba 1(with accuracy going at best up to 50%) while the Figure 2 shows every different behavior (>90%). Am I misunderstanding something? Second, even the results for Mamba 2 seem to vary greatly based on seed, which is quite undesirable and detracts from the conclusions of the paper.
* Why do the authors believe there is such a large difference between Mamba 1 and Mamba 2? They mention this briefly on line 307, but I think this question deserves more attention.
* Similarly, why should Mamba perform better than Linear Attention, given that it was initialized to mimic its behavior?

Minor:
* Line 258: "who suggest these weights should not be strictly equal" — It may be useful to provide some motivation for this.
* Figure 8 mentions Mamba 1/2, but I believe only Mamba 2 is shown.
* l.485: I believe that the authors use a fixed T_i to initialize all S_j (since L and M are different) but this is not clear.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses problems with copying (and more generally recall) in state-space models by proposing a novel "mimetic initialization" scheme based on the following two observations:

1. **State-space models as a generalization of linear attention**: The trainability of the $A_i$ matrices in state-space models allows them to act as a generalization of linear attention. However, this also can give rise to time decay that is too aggressive to learn copying tasks.
2. **Preserving correlation structure between input tokens**: By initializing the product of the $B$ and $C$ projection matrices to be the identity, the authors aim to maintain the correlation structure between input tokens.

By leveraging these two observations to construct an initialization scheme, the authors demonstrate that the resulting mimetic Mamba 1 and Mamba 2 architectures outperform the default Mamba 1 and Mamba 2 architectures on both copying and MQAR tasks. The authors extend the results across multiple task and model hyperparameters and conclude by demonstrating how mimetic initialization can be interpreted as an efficient alternative to model pretraining.

### Strengths
The main strengths of this paper lie in the simplicity of the proposed initializer and the robustness of the empirical results. In particular, I note the following:

1. The empirical findings are strong. Specifically, the mimetic Mamba models achieve significantly higher performance on both copying and recall tasks compared to the default Mamba models. They also reach this performance at a much faster rate.

2. The empirical evaluation is thorough. The authors conduct extensive sweeps across various vocabulary sizes, state sizes, and sequence lengths, demonstrating that mimetic Mamba consistently outperforms default Mamba across these settings.

3. The authors offer insight into how mimetic Mamba functions as a pretraining prior, providing intuition for why the initializer is effective.

4. The work appears reproducible based on the statement provided by the authors, although code has not yet been released.

### Weaknesses
The weaknesses in this paper primarily lie in lack of presentation, novelty, breadth, and clarity. In particular, I note the following:

1. The paper is not particularly well-written. It seems rushed, and while the overall story makes sense, it lacks the logical flow both within and between sections that would make it easier for readers to follow. Some examples of this include the related works which would benefit from bolded paragraph headers like the authors use throughout the paper, rewriting the "Correlated tokens should attend to each other" section which is currently quite confusing to parse, moving the figures so they are actually near the text the author is reading, and more generally adding transitions between the sections that motivate why we need to do the next analysis so the story flows better. Also, I would consider moving the pretraining section after the first set of results since it provides nice intuition as to why the initializer works. 

2. The idea is not particularly novel compared to "Mimetic Initialization of Self-Attention Layers" (Trockman 2023), which is cited throughout the paper. Specifically, the authors adopt the concept of correlating the query and key projection matrices to maintain correlation structure amongst tokens from this prior work and simply apply it to the analogous components of Mamba.

3. The authors’ use of an identity prior on $A$ aligns with the intuition of orthogonal/unitary non-linear RNNs, a related line of work that is entirely ignored in the paper. Although the focus here is on linear systems, it seems incomplete not to mention this prior work. From my understanding, the approach presented in this work effectively reduces the rate at which the gradient vanishes over time, which is a longstanding idea in RNN research.

4. The authors restrict their results to synthetic tasks and do not demonstrate the applicability of this initializer (or any intuition derived from it) on language tasks, limiting the scope of the findings. Maybe something like the Pile is appropriate here?

5. The authors do not analyze other SSMs outside of Mamba (e.g., GLA, RWKV, Hyena, etc.), despite claiming that this initializer improves performance in SSMs more broadly. Intuitively, mimetic initialization should extend to something like GLA which has a distinct functional form from Mamba in the state-to-state dynamics. This would be nice to show. 

6. The authors benchmark this initializer only against the default Mamba initializer, even though the original Mamba paper presents other initializers that could have been included for comparison (these could be included in supplementary materials).

### Questions
Given the weaknesses listed above, I will recommend that this paper be rejected. While the proposed initializer is simple, intuitive, and seems effective, it lacks novelty, and the downstream analyses lack breadth. Furthermore, there is little theoretical justification in this paper (most of which appears to be drawn from prior work). This is acceptable only if a varied empirical analysis compensates for it, which is currently lacking. I think this paper would benefit significantly from another iteration. In particular, I would like to see the following addressed:

1. Explain why the line of work on orthogonal RNNs is not relevant here. If it is, please incorporate it into the paper. In particular, a more extensive related work section in the appendix would add substantial value.

2. Figure 2 is confusing. If the dots correspond to 10 random seeds, why not present the plot as an average with error bars? A more thorough multidimensional display could better reveal the meaningful variations across the ablated dimensions discussed later in the text.

3. The legend in Figure 5 is obscuring half of the plot.

4. Producing results that demonstrate utility beyond synthetic tasks would significantly improve the paper.

5. The authors note that Mamba outperforms linear attention on synthetic tasks but do not offer any intuition for this. Additionally, are the authors using the short convolution from the Mamba block in linear attention? If not, how is this a fair comparison? Please clarify

6. Much of the paper builds on linear attention, as this architecture is intended to serve as a prior in the mimetic initializer. If only one other SSM is to be benchmarked against, why choose Mamba? Isn’t GLA (or even S6) a more appropriate architecture for comparison? Mamba’s discretization step and short convolution are acting as unnecessary confounding factors. More generally, this initializer would be stronger if its effectiveness was demonstrated across a broader range of SSMs rather than just Mamba. Even so, could the authors at least please justify their choice of Mamba as the primary comparison model?

7. To what extent do the models deviate from the initialization prior after training?

8. In which regimes is the initializer most effective? Is it with many tokens to copy, long sequence lengths, etc.? Some plots potentially contain these results, but are hard to parse and there is no discussion in the paper.

9. Can the authors clarify the purpose of the MQAR analysis? Is it intended as a supplemental synthetic analysis, or does it show something distinct from copying? The paper’s claims primarily focus on copying, with MQAR briefly mentioned at the end.

### Soundness
3

### Presentation
2

### Contribution
2
