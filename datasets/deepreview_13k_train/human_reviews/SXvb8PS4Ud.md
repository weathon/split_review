# ParallelSpec: Parallel Drafter for Efficient Speculative Decoding

- Decision: Reject
- Scores: 6, 5, 5, 5, 8

## Abstract
Speculative decoding has proven to be an efficient solution to large language model (LLM) inference, where the small drafter predicts future tokens at a low cost, and the target model is leveraged to verify them in parallel. 
However, most existing works still draft tokens auto-regressively to maintain sequential dependency in language modeling, which we consider a huge computational burden in speculative decoding.
We present \MODEL, an alternative to auto-regressive drafting strategies in state-of-the-art speculative decoding approaches. 
In contrast to auto-regressive drafting in the speculative stage, we train a parallel drafter to serve as an efficient speculative model.
\MODEL learns to efficiently predict multiple future tokens in parallel using a single model, and it can be integrated into any speculative decoding framework that requires aligning the output distributions of the drafter and the target model with minimal training cost. % mention the training cost somewhere later
Experimental results show that \MODEL accelerates baseline methods in latency up to 62\% on text generation benchmarks from different domains, and it achieves 2.84$\times$ overall speedup on the Llama-2-13B model using third-party evaluation criteria.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a parallel drafting model as an alternative to traditional auto-regressive speculative decoding (SD) drafters for large language models (LLMs). Traditional SD models often draft tokens sequentially, resulting in latency that scales linearly with sequence length. PARALLELSPEC innovates by using a parallel drafter that predicts multiple tokens in a single forward pass, achieving notable reductions in draft latency (up to 62%) and overall speedups of up to 2.84x on the LLaMA-2-13B model. The model’s integration into frameworks like Medusa and EAGLE showcases its compatibility and effectiveness, while a group-wise training strategy ensures alignment with the target model’s output distribution. This method maintains theoretical losslessness through a rejection sampling algorithm, preserving the original LLM distribution.

### Strengths
+ The paper’s parallel drafter introduces a novel alternative to sequential SD models, advancing speculative decoding with efficient multi-token generation.
+ Empirical evaluations across multiple benchmarks and models, along with sound theoretical justifications, confirm the validity of the approach.
+ The work has strong implications for real-time, large-scale LLM applications, especially with the demonstrated integration into established frameworks like Medusa and EAGLE.
+ By employing rejection sampling, PARALLELSPEC maintains a lossless decoding process, preserving the original output distribution of the target model.

### Weaknesses
 - Unlike speculative decoding approaches that can use pre-trained models or lightweight modifications, PARALLELSPEC requires a dedicated training process for the parallel drafter. This additional training step may increase setup time and computational cost, which could limit the method’s immediate applicability in certain use cases.
- The absence of publicly available code for the training and experimental setups raises concerns about reproducibility. Without the code, it may be challenging for others in the community to replicate the experiments or validate the results independently, limiting the impact and accessibility of this work.
- The group-wise parallel training could use clearer explanations or diagrams, particularly the role of attention masks and mask tokens in aligning the drafter with the target model’s distribution. The current explanation lacks sufficient detail on how the attention masks prevent information leakage between parallel groups during training, and how the specific arrangement of mask tokens ensures consistent behavior between training and inference.
- Handling of Token Uncertainty: While effective in low-temperature settings, PARALLELSPEC may experience reduced alignment at higher temperatures. Further discussion on managing token misalignment under these conditions would enhance robustness, particularly compared to EAGLE's feature-based uncertainty handling. The paper does not sufficiently explore the trade-offs between speedup and accuracy at higher temperatures, and lacks a detailed analysis of how the rejection sampling mechanism behaves when the draft distribution diverges significantly from the target distribution.

### Questions
1. Could the authors elaborate on the sensitivity of PARALLELSPEC’s performance to the number of tokens generated in parallel (i.e., the parameter k)? Are there guidelines for selecting k based on specific model or task characteristics?
2. How does PARALLELSPEC’s memory usage compare with traditional auto-regressive drafters, particularly in large models? Does the use of multiple [MASK] tokens introduce significant memory overhead?
3. In high-temperature settings, where acceptance rates may decrease, what are possible strategies to maintain drafter alignment without significantly impacting speedup?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes ParallelSpec, which replaces the traditional autoregressive draft model in speculative decoding with parallel draft model to achieve better inference efficiency. Previous work such as Medusa already considers parallel draft model. The difference between ParallelSpec and Medusa is: Medusa trains additional heads to predict tokens at different positions, while ParallelSpec uses different mask tokens to do that. The authors claim their approach can maximally exploit the parameter sharing and hance is more effective. The experiment results in temperature=0 cases support this claim. But the experiments do not include the comparison with Medusa in temperature=1 cases. The main challenge in ParallelSpec is that it requires a different training mask and attention mechanism. The authors address this challenge reasonably.

### Strengths
1. The intuition of why ParallelSpec can accelerate EAGLE is convincing. Based on the experiment results shown in Table 1, although ParallelSpec generates less tokens per iteration, it improves the drafting efficiency via parallel drafing, so it improves the overall efficiency.

2. The paper is well-written and easy to understand.

3. The paper includes comprehensive discussion on how to integrate the proposed method with state-of-the-art framework such as EAGLE and Medusa.

### Weaknesses
1. One of my main concern is the comparison between the proposed method and Medusa. Although authors provides an intuitive explanation that ParallelSpec has better parameter sharing, I am not fully convinced. So I expect to see a comprehensive comparison between Medusa and ParallelSpec in the experiments. However, in Table 1, the comparison between Medusa and Medusa+ParallelSpec only covers the temperature=0, but not temperature=1. The lack of temperature=1 results makes it difficult to assess the robustness of ParallelSpec under more stochastic decoding conditions. It's crucial to evaluate how the parallel drafting strategy performs when the model is not operating in a purely greedy manner, as this is more representative of real-world usage scenarios.

2. In Table 1, I believe the two settings (temp=0 and temp=1) are equally important. But temp=1 only covers a subset of baselines and target models. So the evaluation is not comprehensive to me. The absence of a full comparison at temperature=1 raises concerns about the generalizability of the findings. The paper should include a complete set of experiments across all baselines and target models at both temperature settings to ensure a thorough evaluation.

3. Although the proposed method could accelerate EAGLE, the improvement is somewhat marginal (only about 1.1$\times$ speed up). This limits the contribution of this paper. The modest speedup, especially when considering the added complexity of the proposed method, raises questions about its practical significance. A more substantial performance gain would be necessary to justify the introduction of a new training paradigm and attention mechanism.

### Questions
1. Can authors complete the evaluations in Table 1?

2. Is the code open-sourced?

3. The EAGLE uses autoregressive decoding as drafers. Is it possible to combine Medusa and EAGLE, meaning it also trains different decoding heads for different token positions?

4. It would be helpful if authors could provide detailed breakdown (e.g., draft time, verification time) of different methods. And compare how much does the propsoed method accelerate the draft time of EAGLE.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new drafter architecture for speculative decoding methods, which drafts several tokens in parallel rather than auto-regressively. It suggests a process for training these drafter models, shows how to incorporate it into several state of the art speculative decoding methods such as Medusa and EAGLE, and shows that it manages to achieve around 37-62% additional speedup for Medusa, and 9-17% additional speedups for EAGLE.

### Strengths
**Originality:** While the idea of parallel drafting in speculative decoding was already explored, this paper is the first time the effectiveness of this method is demonstrated with a separate drafter.

**Clarity**: Overall the method is simple, elegant, and clearly presented.

**Significance**: Speculative decoding is a widely used technique for accelerating language model inference, and speeding up state of the art speculative decoding methods is an important problem with clear implications for both research and industry. The demonstrated speed-up of ~15% on top of EAGLE is notable, highlighting the practical value of this work.

### Weaknesses
While accelerating speculative decoding methods is an important problem, and the ~15% speedup over existing methods is commendable, I believe the paper should be rejected for the following reasons: (1) the method is not novel enough as it is very similar to ideas already present in existing works (2) the results are not overly convincing and their magnitude is generally far below the 62% reported in the abstract. (3) There are some reproducibility issues, though I think these can be easily clarified by the authors in the follow up discussions.

**Novelty**: The core idea of drafting tokens in parallel instead of autoregressively was already presented by Stern et al (“Blockwise Parallel Decoding for Deep Autoregressive Models”), Monea et al (“PaSS: Parallel Speculative Sampling”) and to some extent Medusa, and the architecture presented in the paper closely resembles Monea et al, though their work was limited to the case where the same target model also generates the look-ahead drafts. This paper, while incrementally different, applies the concept with a separate drafter.

**Reproducibility**: The paper lacks sufficient details regarding the construction of the token tree. The main text refers to Appendix A.3, which only states that each node is expanded with “top-k highest probabilities”, where k is based on “manually crafted rules”. Without more specific details for how k is chosen, this process cannot be fully reproduced. Also, figure 6 may be unintentionally misleading, as from the text description the number of children of each node on a given depth should be the same (the “k” chosen for that depth). To enhance reproducibility, I suggest including a more detailed explanation in Appendix A.3 of how k is chosen for each depth level, and perhaps including pseudo-code.

**Clarity**: There are some mistakes and inaccuracies, mainly in “algorithm 1” which I believe should be revised. I’ll outline these in the Questions/Suggestions section. These issues can likely be addressed before publications, so they did not impact my score.

**Experimental results**: 
* A speed-up of ~15% over a state of the art method like EAGLE is notable, and could offer important inference improvements. However, there is some discrepancy between the results presented here and the ones presented in the SpecBench paper.
* Most importantly, for Medusa (which this paper claims to gain significant speed-ups of 30-60% over), the results presented in table 1 show significantly worse speed-ups than those in table 6 from the SpecBench paper (e.g. on 7B, SpecBench reports 2.42x while ParallelSpec paper reports 1.42x, on 13B SpecBench reports 2.16x while ParallelSpec paper reports 1.84x). I think it’s important to clarify these differences, as the 62% additional speedup reported in the abstract is the one achieved on top of these sub-par Medusa results. 
* The EAGLE reported speedups are also a bit lower than in the SpecBench paper, but by a smaller magnitude (e.g. for 7B, 2.39x in SpecBench paper vs 2.18x in ParallelSpec).Still, this ~10% difference is significant since ParallelSpec only reports an improvement of 15% over EAGLE.
* The 62% speedup claim in the abstract is based on results from the Medusa 7B baseline, which demonstrates particularly subpar performance compared to SpecBench (and according to table 1, seems to be slower than even vanilla SpS or lookahead methods).

### Questions
**Concrete action items for the experimental results:**
1. I think it would be more accurate to temper the claim in the abstract, as the speedup for other baselines is around 9%-17% which is still notable.
2. Why are the reported speedup results for Medusa and EAGLE differ from those in the SpecBench paper, especially for Medusa where the difference is especially significant? I think it would strengthen the paper to add an explanation for this discrepancy.

**List of more minor things that could be improved in the paper:**
1. Figure 1 left - I think the arrows could be bolded or colored to clarify the distinction between “Auto-regressive Drafting” and “Parallel Drafting”. Currently the difference is a bit hard to spot.
2. End of intro section - since relative improvement (62.7%) is mentioned for Medusa, it should also be mentioned for Eagle (where I think it is 9-17%).
3. Related Work / Parallel Decoding - I believe "Blockwise Parallel Decoding for Deep Autoregressive Models" can also be mentioned here and possibly Medusa as well
4. Background / Speculative Decoding Procedures -  inconsistent notation for $x_k$. “Drafted token sequence $x_1,...,x_i$ where $x_{t+i} \sim q(y_{t+i})$” should be “Where $x_k \sim q(y_{t+k})$”.
5. I found algorithm 1 a bit hard to follow and suggest a few corrections below. However, since AFAIU this algorithm is simply standard tree speculative decoding as presented e.g. in SpecInfer, I believe it can be omitted or moved to the appendix if needed.
6. Experiments / Baselines - For SpS, it is not clear which gamma was chosen (how many draft tokens are generated on each iteration). Was gamma optimized to maximize speed-up or was it chosen based on some other criteria?

**Algorithm 1 issues:**
1. “Given … initial prefix sequence $x_{<n}$” should be $x_{<t}$, otherwise the line “Initialise n ← t” doesn’t make sense (since n can’t be initialized after it’s already used).
2. As written above, “Draft future token tree N” the details of how this tree is generated are not precisely written in the paper.
3. “O = TreeParallelDecode(N, p)”: O is set but never used. Instead, this should say something like - compute all logits p(x|x<n,{all paths from root to any node}) with the target model using N and tree attention.
4. “$\tilde{x}_s=H(s)$”: this notation is not clear, as H is a set of tree nodes and s is a node in the tree selected from $H$. I understand from the context $\tilde{x}_s$ is the token corresponding to node s in the tree but it should be made clearer.
5. I understand the notation $q(x|x_{<n},...,MASK_t)$ (since the … denotes the other mask tokens), but why $p(x|x_{<n},...,V)$? Why not just $p(x|x_{<n},V)$?
6. Normalize the residual line has an extra “+” at the end of the line.
7. The term $x_{<n}$ uses the n that keeps growing (initialized to t and then grows until it’s T or above). However, x never changes and it’s always the initial prefix of only t tokens. Should probably be changed to $x_{<t}$ everywhere.

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
To deal with the speculation overhead from the auto-regressive draft model in speculative decoding, the paper proposes a parallel decoding approach for speculation by adding additional mask tokens in the vocabulary. Within a single draft model forward step, several future tokens can be speculated in parallel with the [mask] tokens used as temporary input tokens. The parallel speculated tokens are then fed into the target model for verification.  Empirical evaluations show that, assisted with this parallel decoding scheme proposed by the paper, current state-of-the-art speculative decoding frameworks, including EAGLE and Medusa, can further achieve a higher speed-up ratio due to the reduction in the speculation overhead while preserving a similar speculation accuracy.

### Strengths
1. The problem is well-motivated as the speculation overhead can indeed play a crucial role in the end-to-end speed-up ratio brought by speculative decoding. 
2. The paper's empirical evaluations show promising results for the proposed ParallelSpec approach, where the EAGLE+ParallelSoec and Medusa+ParallelSpec can consistently achieve a better speed-up ratio than the base version. 
3. The presentation is clear and illustrative.

### Weaknesses
1. The concept of parallel decoding is not new. In fact, [1] has proposed a similar idea based on a parallel-decoded drafter and a target model as a verifier for speculative decoding. Additionally, Medusa itself is a parallel decoded speculation approach. Compared with these existing works, this paper mainly differentiates in its draft model architecture design that leverages the [MASK] tokens as a placeholder to predict future tokens within one model forward pass. However, this design is similar to the approach proposed in [2].

2. Though the empirical evaluations in the paper demonstrate promising end-to-end speed-up results on Vicuna-7B/13B and LLaMA-2-7B/13B, the evaluations on a larger model (e.g., LLaMA-2-70B) are missing. I guess this is due to the speculation overhead for a larger target model being less dominant as the theoretical improvement of minimizing speculation overhead is $\frac{\text{Latency(Verification)+Latency(Speculation)}}{Latency(Verification)}$ assuming that the speculation accuracy is the same. However, the speculation accuracy and overhead are usually a trade-off, so achieving this theoretical speed-up in practice is hard. 

3. If I understand correctly, even using the same dataset, the way you trained your draft model results in a larger processed dataset due to the existence of parallel groups, making the training of your drafter less efficient than EAGLE. 

4. Minor: as the EAGLE results in the SpecBench are a bit outdated, it would be interesting to compare your methods against the latest version (EAGLE-2).

### Questions
1. **Technical**-wise, how is your work different from [1] and [2] given that they both are parallel speculation frameworks and [2] even has the same [MASK] token design?
2. **Empirical**-wise, it is important to have evaluation results for a larger model (LLaMA-2-70B) where the inference speed-up is more crucial. Although the current results can show the potential of your draft model design when scaled to a larger model, it would be great if your method could still consistently achieve the best speed-up ratio on a 70B model. If time allows, it is more promising if you can compare it with EAGLE-2.

Minor issue: The wall time trace diagram (right) in Figure 1 is a bit misleading. The latency saving shown in the diagram is only guaranteed if the parallel decoded draft model has the same speculation accuracy as the auto-regressive decoded draft model. So, I would suggest adding this assumption in the caption and the paragraph that mentions the figure (the second paragraph in the introduction section).



**references**

[1]. Stern, Mitchell, Noam Shazeer, and Jakob Uszkoreit. "Blockwise parallel decoding for deep autoregressive models." Advances in Neural Information Processing Systems 31 (2018).

[2]. Xia, Heming, et al. "Speculative decoding: Lossless speedup of autoregressive translation." (2022).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new technique, ParallelSpec, to advance the topic of speculative decoding. The proposed method addresses the efficiency barrier in autoregressive decoding within the draft-then-verify paradigm by adding new [MASK] tokens and predicting the next $K$ tokens in a single draft model call. ParallelSpec is orthogonal to methods that require training a draft model through distillation with the target model. To improve the ability to predict multiple subsequent tokens, the paper proposes "group-wise parallel training," where groups of [MASK_1] ... [MASK_K] are inserted after each token in the training corpus, with predicting the correct token at the corresponding position as the training objective. Extensive experiments evaluate the effectiveness of ParallelSpec's design. ParallelSpec is implemented on Llama-2-chat-7B/13B and Vicuna-7B/13B, trained on top of Medusa and EAGLE, and evaluated on SpecBench, where it is compared to popular baselines for speculative decoding. ParallelSpec outperforms all baselines on the tested data, achieving greater wall-time speedup ratios. The paper also includes comprehensive ablation studies, investigating the effects of different $K$ values and self-distillation. Overall, ParallelSpec is an effective technique that can be combined with most speculative decoding algorithms to improve efficiency.

### Strengths
This paper makes significant contributions to the topic of speculative decoding, offering a technique that can enhance speedup ratios. There are several strengths of this paper (which I personally find very inspiring), and the most important ones are listed below:

1. Clear presentation. The paper clearly outlines the background for developing this technique, and the introduction to related works is distinct and comprehensive. Figures and tables are presented well, making them easy for readers to understand. Important hyperparameters and experimental settings are clearly stated. The way experimental results are presented is highly readable.

2. Simple but effective method. The idea of transforming the autoregressive decoding process of the draft model into parallel decoding is brilliant, and the implementation of group-wise parallel training is simple, clear, and effective. The adaptations to existing methods are minor, and the proposed method can be integrated with most prior work.

3. Strong performance. The experimental results show a substantial speedup gain when ParallelSpec is applied. The proposed method outperforms state-of-the-art methods without significant training costs.

4. Well-designed experiments. ParallelSpec is compared with popular baselines in this field using mainstream benchmark datasets. The ablation studies focus on key components of the system's design.

### Weaknesses
Although this paper makes valuable contributions, there are certain flaws that prevent it from receiving a higher rating. The weaknesses are listed as follows, and the overall rating could be improved if these issues are addressed:

1. Unfair competition between standalone Medusa and Medusa+ParallelSpec. In the original Medusa setup, the Medusa heads are organized in an MLP-like architecture. However, when Medusa is adapted with ParallelSpec, the draft model is a single-layer Transformer model (lines 266-267). To what extent is the speedup gain due to the change in draft model architecture, as opposed to predicting draft tokens in parallel? A baseline should be provided where the only alteration is the draft model architecture. Otherwise, the modified setting should be given a different name, as the current name might create confusion regarding the draft model architecture.

2. Unclear presentation of how EAGLE is adapted with ParallelSpec. The description in lines 355-357 is insufficient. It would greatly improve clarity to provide a more detailed explanation of the training and inference process when adapting EAGLE, even in the Appendix if space in the main text is limited. This weakness is further elaborated in Question Q1.

### Questions
Here are my questions and some suggestions for this paper:

1. EAGLE adaptation. In the standalone EAGLE algorithm, assuming the input embeddings are $e_{< t}$, the first step of drafting proceeds as $\tilde f_{t} = \pi (f_{<t}; e_{<t})$, and the second step goes as $\tilde f_{t+1} = \pi([f_{<t}, \tilde f_{t}]; [e_{<t}, \tilde e_t])$, where $[\cdot, \cdot]$ represents concatenation, and all other notations follow this paper. Given that the hidden states $f$ are also generated autoregressively, how is this handled in ParallelSpec? In my understanding, the draft model should forward once to generate all the draft tokens, i.e., $\tilde f_t, \dots, \tilde f_{t+K+1} = \pi ([f_{<t}, ?\dots ?]; [e_{<t}, {[MASK_1]}, \dots, {[MASK_K]}])$. What should be placed in the question marks, or is my understanding of EAGLE+ParallelSpec's drafting process incorrect?

2. Inconsistency results with official SpecBench. The baseline results of Medusa and EAGLE in Table 1 seems to be lower than the official SpecBench [1] results. The speedup of Medusa on Vicuna-7B is 1.42 in Table 1 while the official SpecBench gives 1.78, and speedup of EAGLE on Vicuna-7B in Table 1 is 2.18 while the official result is 2.29. Could you provide an explanation on the reason why the speedup gap occurs?

3. The organization of Table 2. The upper and lower halves of Table 2 should be presented in separate tables. They cover different topics: the upper half focuses on self-distillation, while the lower half discusses Llama-3.

4. Compatibility with dynamic draft trees. I am curious about the speedup gain of ParallelSpec when applied to dynamic draft trees, such as in EAGLE-2. Is this method compatible with dynamic trees, and would its strong performance persist? This is just a question for discussion, and the authors are not required to conduct such experiments during the review process.

[1] https://github.com/hemingkx/Spec-Bench/blob/main/Leaderboard.md#vicuna-7b-v13

### Soundness
3

### Presentation
3

### Contribution
4
