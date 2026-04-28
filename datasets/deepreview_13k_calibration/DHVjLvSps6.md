# Quantifying Memory Utilization with Effective State-Size

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 6, 6, 5

## Abstract
As the space of causal sequence modeling architectures continues to grow, the need to develop a general framework for their analysis becomes increasingly important. With this aim, we draw insights from classical signal processing and control theory, to develop a quantitative measure of *memory utilization*: the internal mechanisms through which a model stores past information to produce future outputs. This metric, which we call **effective state-size** (ESS), is tailored to the fundamental class of systems with *input-invariant* and *input-varying linear operators*, encompassing a variety of computational units such as variants of attention, convolutions, and recurrences. Unlike prior work on memory utilization, which either relies on raw operator visualizations (e.g. attention maps), or simply the total *memory capacity* (i.e. cache size) of a model, our metrics provide highly interpretable and actionable measurements. In particular, we show how ESS can be leveraged to improve initialization strategies, inform novel regularizers and advance the performance-efficiency frontier through model distillation. Furthermore, we demonstrate that the effect of context delimiters (such as end-of-speech tokens) on ESS highlights cross-architectural differences in how large language models utilize their available memory to recall information. Overall, we find that ESS provides valuable insights into the dynamics that dictate memory utilization, enabling the design of more efficient and effective sequence models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper frames many sequence modeling architectures as "input-varying linear operators" $u\mapsto T(u)u$, with $u$ being the sequence features. It then focuses on the linear operator $T(u)$ and introduces the "effective state size" (ESS) of this operator as the minimal possible hidden size of the state of an SSM representing $T$. The paper demonstrates that ESS is a relevant measure of the capacity to process memory in the model and compares it favorably to "total state rank" (see discussion below on its definition). The paper also demonstrates how insights about ESS of a model can drive architecture development, initialization and regularization techniques. Finally, the paper shows that the ability to change ESS along the sequence is helpful for real models in bigram recall.

### Strengths
- The ESS measure is clever, well justified theoretically through Thm 2.1, 2.2, and, to the best of my knowledge, novel.
   - Even just the rephrasing of other sequence models through the lens of input-dependent SSM parameters can be useful for the community.
- The paper performs _a lot_ of experiments to determine usefulness of ESS.  I especially liked the insight of ESS saturation for the GLA model at initialization.
- The approach is fairly multi-disciplinary within ML, with insights from neural ODEs, SSMs, and control theory.

### Weaknesses
 # Density
This should have been a journal article. The paper wants to say so much, that the related work section is completely moved into the appendix! The paper attempts to cover extremely wide ground, from theory about ESS to experiments clarifying the notion to at least three fixes to the learning pipeline, and becomes very difficult to follow. In my view, in the current state the paper cannot be accepted even though the contributions are sufficient for ICLR. Hence, I am giving a 5/10, but I will happily adjust the score if the density concerns are addressed. This would require the following:
- Increasing the size of the figures (Fig. 2 and 3 would be impossible to read on paper)
- Moving some of the findings or the related discussions to the appendix. See below for some findings that could be suitable for that, but I will leave it up to authors to decide on the things to move.
- Reintroducing related work, even if just a couple of paragraphs, in the main text

# Other concerns
- We already have a measure of model capabilities that is widely used by the practitioners and that, among other things, correlates with ability to store and recall memories. That is the model size (number of parameters). In my view, the biggest issue other than density is that the paper never discusses the size as a baseline, eg in Figure 2 when comparing TSS to ESS.
- The TSS measure, as discussed in appendix, is not a proper function of the operator T. While model size comes naturally with the architecture and hyperparams, TSS depends on a specific way of _rewriting_ the model's architecture. The paper mostly shows TSS in a negative light as an easy baseline for ESS. The need for introducing TSS is thus not clear to me.
- Finding 3 is too specific. I suspect that the "state collapse", namely the model not utilizing all of its potential, might also be relevant to hyperparameter selection.

## Typos
- Fig 6a y axis: should this be ESS? The text talks about ESS, and I don't think TSS changes over time?
- Fig 5a axis "vs" instead of "kv"

### Questions
- Although ESS is introduced as a per-token measure, when presenting most of the results (apart from last section)  ESS is presented as a single value. Is it maximum, average, or some other statistic, and is there intuition for this?
- Finding 6 tells us that GLA and WLA perform worse than LA on assortative recall. This is surprising to me. Shouldn't architectures like Mamba outperform simple linear attention on such things? Maybe it is the specific task, but it was chosen by Poli et al (2024) to be specifically correlated with real-world performance.
  - Related: if it is indeed ESS, how did authors compute it for Mamba 7B? The numbers are of the order of `6e6`, I am not sure we can run SVD on matrices with this number of this size.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides detailed analyses of memory utilization for many input-invariant and input-varying linear operators, including attention, convolutions, and recurrences. It introduces the metric called effective state size by leveraging rank or entropy. This metric is used to evaluate and compare the memory utilization of different linear operators from three model phases: initialization, mid-training, and post-training, with a lot of findings. The authors also showed using this to get better performance through better initialization, normalization, and distillation.

### Strengths
* The paper proposes considering memory utilization to evaluate the performance of various linear operators. Specifically, it introduces two metrics to measure effective state size, which can serve as a proxy for memory utilization.

* Empirical experiments are conducted across different phases of model training, yielding many interesting findings.

* The analyses of memory utilization may help people better understand the behavior and performance of different models and inspire further improvements.

### Weaknesses
 * For the recurrence, did the authors investigate the A matrix in the vectorized shape or the scalar value shape? The vectorized A is used in many classical RNN papers as well as in S4, S5, and S6. However, the scalar value A is used in the recent Mamba2 paper and RetNet, which directly builds the connection between attention and state-space models. I think this choice can affect the memory utilization and also efficiency. Specifically, the paper should clarify whether the analysis of the A matrix for recurrent models considers the full matrix or the individual scalar values, as this distinction significantly impacts the effective state size calculation and its implications for memory usage. For example, using a vectorized A matrix allows for parallel computation across channels but may not accurately reflect the memory footprint of models like Mamba2, which use a scalar A per head.

* Could the paper provide more discussion and analyses of memory utilization across different sequence lengths? I see the paper extends the analysis to a sequence length of 2048, but what about even longer sequences? Many state-space models highlight their long-context abilities more than attention, and long-context is also a crucial ability required in LLMs. The analysis should include a more thorough investigation into how effective state size scales with sequence length, particularly beyond 2048. Given the emphasis on long-context capabilities in state-space models, it is crucial to understand how memory utilization changes as sequence lengths increase to 4096, 8192, or even longer, as this is a key differentiator from attention mechanisms.

* While there are many findings (9 in the main paper) related to memory utilization, I wonder which are the most important. Could the authors highlight the most meaningful findings, perhaps in the introduction, to better emphasize the paper's contribution? The paper would benefit from a clearer articulation of the core findings, especially in the introduction. This would help readers quickly grasp the most significant contributions and the practical implications of the memory utilization analysis. It is currently difficult to discern which findings are most impactful.

* What is the direct conclusion regarding the memory utilization of different linear operators? I didn’t find a direct conclusion or explanation in the findings. The paper lacks a clear, concise conclusion that summarizes the overall implications of the memory utilization analysis. It should explicitly state which linear operators are more memory-efficient and under what conditions, providing a practical takeaway for model design.

* The terms GLA and WLA are ambiguous. Why do the authors label the input-invariant A matrix as weighted linear attention? Because the softmax attention is also weighted. Also, in line 242, the authors categorize Mamba as a GLA layer. However, Mamba or S6 is not exactly linear attention, although Mamba2 can be. The naming conventions for GLA and WLA are confusing and require clarification. The paper should justify why an input-invariant A matrix is termed 'weighted' linear attention, especially given that softmax attention also involves weighting. Furthermore, the categorization of Mamba as a GLA layer is inaccurate, as Mamba and S6 have distinct mechanisms compared to linear attention, although Mamba2 shares some similarities.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

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
This paper introduces the notion of effective state size (ESS), and demonstrate that it correlates with downstream performance on recall-based tasks better than theoretical state size (TSS).  The effective state size (ESS) is the smallest dimension required to represent the causal sequence operation as a linear recurrence.  They test their method for a variety of training runs, and task complexities.

### Strengths
* The effective state size metric is intuitive and of conceptual value.
* The experiments show better correlation with accuracy on recall tasks than theoretical state size
* The method may be useful to compare the effective memory capabilities of different architectures, in contrast with their theoretical expressivity.

### Weaknesses
 * The paper seems to be lacking ablations on network depth, at least in the main body.  Showing how the results change with the number of layers could make the paper stronger. Specifically, the impact of depth on ESS and its correlation with task performance is not explored thoroughly. It is unclear if the observed trends for 2-layer networks generalize to deeper architectures, which are more commonly used in practice.
* There is little discussion about the computational costs of the method.  The state sizes of modern SSMs like Mamba are very large, thus it would help to have some reassurance that the method is scalable to modern architectures. The authors should provide a more detailed analysis of the time and memory complexity of computing ESS, especially for large state spaces. This is critical for assessing the practical applicability of the proposed metric.
* The authors briefly mention hybrid architectures in the main body.  However, since Hybrid architectures are becoming more prominent, some further discussion might be warranted.  Since Hybrid architectures have attention layers and skip connections, we might expect that they have full recall capabilities within their context window, which could permit the SSM layers memorize less in their state. The interaction between attention mechanisms and SSM layers in hybrid architectures needs more investigation. It is unclear how the ESS of the SSM layers is affected by the presence of attention and how this impacts overall performance.

### Questions
Line 142: I believe $C \in \mathbb{R}^{d \times n_i}$ (dimensions should be swapped)

How expensive is it to compute the ESS?

“which are comprised of two sequence mixing and two channel mixing layers) detailed above”. Do you do any ablations to consider effect of greater depth?

What is (total ESS) vs ESS Figure 2?

Why such low correlation for WLA method with KV = 2^7 but high at 2^6?

Figure 4b is a bit confusing to read since ESS and Accuracy are on the same axis.  It would also to help explain the experimental process, as it seems there are multiple configurations and you take the mean accuracy across those.

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
5

### Summary
The paper proposes a quantitative measure of memory utilization for modern causal Large Language Models (LLMs). The proposed metric, called Effective State-Size (ESS) is obtained following standard results of realization theory of dynamical systems and can be used to analyze models employing different time mixing layers like Attention, convolutions and more recent (Selective) State Space Models. The paper shows that ESS is informative of the quality of initialization and regularization strategies for LLMs’ training.

### Strengths
The paper addresses an important and timely question on how modern LLMs’ sequence mixing layers modulate memory. The proposed metric ESS that is derived for input-invariant dynamical systems can be applied to many different modern architectures and is sound, as it is directly derived from standard results in realization theory of dynamical systems.

### Weaknesses
Novelty, the paper argues (Line 108) that one of the main contributions is to prove that the rank of submatrices of the input-output causal operator T determines the minimally realizable state-size of the recurrent operator. There is nothing to prove, this is textbook material reported verbatim from realization theory of linear time invariant dynamical systems. Please make sure to point the reader to proper textbook material for both Theorem 2.1 and Theorem 2.2, see [1, 2, 3].

While the main results on linear input-invariant recurrences are well known, in practice modern LLMs utilize input varying recurrences which are not as straightforward to analyze. This latter case is quickly and vaguely described in a single paragraph (starting in Line 175). This is the key novelty and contribution of the paper (aside from the empirical validation), however the current manuscript does not provide any theoretical guarantees and only describes, non-tight, bounds on the ESS of an input-varying recurrence using its input-invariant counterpart. The lack of theoretical grounding for the input-varying case is a significant limitation, as it leaves the reader unsure of the validity of applying the ESS metric in this context. A more rigorous treatment, even if it only provides bounds or approximations, would strengthen the paper.

A thorough related work section is missing, please consider adding one in the main text. Some references to complement the ones already cited that might be helpful to the readers are provided below (Questions section).

The paragraph starting in Line 175 is unfocused and hard to read, yet it should be the key novel contribution of the paper. How should one define ESS for input-varying recurrences in theory? The ESS needs to depend on the specific input being considered and can, indeed, oscillate depending on the type of the input signals. Have the authors considered using a set of test reference signals or an optimization procedure over the space of sequences of a given length that maximize the required state dimension of their equivalent realization? Are these feasible choices in practice? A deeper discussion about other possible choices that are more theoretically motivated yet not feasible in practice would be beneficial for the reader. The current discussion lacks the necessary depth to justify the application of ESS to input-varying systems.

Why ESS definitions in Eq. (3) and (4) do not depend on the time index i? Given a sequence and a linear input-invariant system of finite order, one needs to progressively increase the sequence length of the Hankel submatrices until the rank stabilizes to the value of the state dimension. However, Equations (3) and (4) do not scan over different sequence lengths. This makes the definition of ESS seem incomplete, as it does not account for the transient behavior of the Hankel matrix rank before it stabilizes.

Why in the empirical validation (section 3) Mamba-1 model has not been validated? I am specifically referring to Mamba-1 and not Mamba-2 since the latter is already closely matched by GLA that is already discussed by the authors. The absence of Mamba-1 is a notable gap, given its popularity and relevance in the field.

Can the authors explicitly define TSS for each architecture used in the empirical section? The lack of a clear definition for TSS makes it difficult to interpret the results and compare across different architectures.

Figure 3 is quite strange, GLA and WLA are strictly more expressive than LA yet accuracy of the latter is higher across all evaluations. Is it possible that this is due to some training instability/poor optimization/parametrization? Can the authors contextualize their results in light of the empirical study conducted in [5], specifically in Section 3.4? In particular, highlighting the relationship of fast decaying eigenvalues and normalization at initialization (this is relevant also for your section 4.1). The lack of discussion on potential training instabilities and how they might affect the results is a significant oversight.

Results in Section 4.2 are not surprising nor specific to the proposed metric and are in general well known, see a similar analysis in [4, 5]. A simple analysis of the eigenvalues of the recurrent updates will lead to the same insights. Is ESS providing further insights? The paper needs to clarify the unique contributions of ESS over simpler eigenvalue analysis.

Can the authors further comment on ESS for hybrid models? Why the order of Attention and Recurrent layers matters and how does ESS can guide the user to those insights? Recent Hybrid models that are worth mentioning/commenting are [4, 6, 7]. The discussion on hybrid models is insufficient, and the paper should explore how ESS can be used to understand the interplay between different layer types.

Why in Figure 6 the ESS decreases (almost symmetrically) near the end of the plot? And why do we expect dips in the ESS to account for a state reset? Take for example a LTI system whose state is set to zero at some random point in an interval of length N (where N is the LTI’s state dimension). The ESS value should not change since the state dimension is a structural property of the dynamical system being studied and not of the specific values taken by the state. The explanation for the observed dips in ESS is not convincing and needs further clarification.

Minor:
- Contributions’ section is rather generic; it is worth rewriting it.
- Line 142 typo on the dimension of C_i. Why does the dimension of the A matrix change? Is it to cover the Attention layers whose state needs to increase as the processed sequence length increases?
- Line 235 typo: “as is pertains”.

### Questions
1. The paragraph starting in Line 175 is unfocused and hard to read, yet it should be the key novel contribution of the paper. How should one define ESS for input-varying recurrences in theory? The ESS needs to depend on the specific input being considered and can, indeed, oscillate depending on the type of the input signals. Have the authors considered using a set of test reference signals or an optimization procedure over the space of sequences of a given length that maximize the required state dimension of their equivalent realization? Are these feasible choices in practice? A deeper discussion about other possible choices that are more theoretically motivated yet not feasible in practice would be beneficial for the reader.
2. Why ESS definitions in Eq. (3) and (4) do not depend on the time index i? Given a sequence and a linear input-invariant system of finite order, one needs to progressively increase the sequence length of the Hankel submatrices until the rank stabilizes to the value of the state dimension. However, Equations (3) and (4) do not scan over different sequence lengths. 
3. Why in the empirical validation (section 3) Mamba-1 model has not been validated? I am specifically referring to Mamba-1 and not Mamba-2 since the latter is already closely matched by GLA that is already discussed by the authors.
4. Can the authors explicitly define TSS for each architecture used in the empirical section? 
5. Figure 3 is quite strange, GLA and WLA are strictly more expressive than LA yet accuracy of the latter is higher across all evaluations. Is it possible that this is due to some training instability/poor optimization/parametrization? Can the authors contextualize their results in light of the empirical study conducted in [5], specifically in Section 3.4? In particular, highlighting the relationship of fast decaying eigenvalues and normalization at initialization (this is relevant also for your section 4.1).
6. Results in Section 4.2 are not surprising nor specific to the proposed metric and are in general well known, see a similar analysis in [4, 5]. A simple analysis of the eigenvalues of the recurrent updates will lead to the same insights. Is ESS providing further insights? 
7. Can the authors further comment on ESS for hybrid models? Why the order of Attention and Recurrent layers matters and how does ESS can guide the user to those insights? Recent Hybrid models that are worth mentioning/commenting are [4, 6, 7].
8. Why in Figure 6 the ESS decreases (almost symmetrically) near the end of the plot? And why do we expect dips in the ESS to account for a state reset? Take for example a LTI system whose state is set to zero at some random point in an interval of length N (where N is the LTI’s state dimension). The ESS value should not change since the state dimension is a structural property of the dynamical system being studied and not of the specific values taken by the state. 




Minor:
- Contributions’ section is rather generic; it is worth rewriting it. 
- Line 142 typo on the dimension of C_i. Why does the dimension of the A matrix change? Is it to cover the Attention layers whose state needs to increase as the processed sequence length increases? 
- Line 235 typo: “as is pertains”.


[1] B. L. HO, R.E. Kalman, “Effective construction of linear state-variable models from input/output functions.”, Regelungstechnik, vol. 14, pp. 545-548, 1966.

[2] Akaike. H. (1974b). Stochastic theory of minimal realization. IEEE Trans. Automatic Control. AC-19:667-674.

[3] L. Ljung, “System Identification: Theory for the User”, Prentice Hall, 1999.

[4] L. Zancato et al., “B'MOJO: Hybrid State Space Realizations of Foundation Models with Eidetic and Fading Memory”. arXiv preprint arXiv:2407.06324 (2024).
 
[5] A. Orvieto et al., “Resurrecting Recurrent Neural Networks for Long Sequences”, PMLR 202:26670-26698, 2023.

[6] De, Soham, et al. "Griffin: Mixing gated linear recurrences with local attention for efficient language models." arXiv preprint arXiv:2402.19427 (2024).

[7] P. Glorioso, et al. "Zamba: A Compact 7B SSM Hybrid Model." arXiv preprint arXiv:2405.16712 (2024).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a metric called "effective state size (ESS)" to capture the memory utilization of sequence modeling architectures. They compare the correlation between ESS and accuracy across various tasks and architectures, finding that ESS shows a stronger correlation with performance than the "theoretically realizable state size" in the SSM equations. They use ESS to guide initialization strategies and regularization methods. They also observe that ESS dynamically changes in response to inputs, particularly at EOS tokens, noting that this modulation effect is more stronger in more performant architectures.

### Strengths
- Identifying quantitative measures to compare different language modeling architectures is an important and timely problem.
- The framework proposed by the authors is broadly applicable to many sequence modeling architectures.
- The idea of the ESS is natural and connected to classical ideas in control theory.
- The authors’ observations on the phenomenon of "state modulation" are interesting from a linguistic perspective.

### Weaknesses
 * While the concept of ESS is relatively straightforward, the paper is very difficult to read since it constantly refers to the appendix (which is 30+ pages long) for definitions and empirical results.
* Notation and plots are often not explained in the main text (e.g., the meaning of "total ESS").
* The core concept of ESS is not clearly defined; although the authors present it as an architectural property, it also depends on the input (as noted in Sec 4.2), so it should vary with both data and task. The definition of ESS as rank(Hi) is insufficient, as it does not specify the dependence on input x and timestep i, which should be explicitly denoted as ESS(x)i. The authors also switch between different ways of computing ESS (tolerance vs entropy) and aggregating across layers, channels, and timesteps, which further complicates the definition.
* Key terms like "state saturation" and "state collapse" are introduced only informally.
* Although perhaps novel in this context, the basic idea of ESS is not new; for instance, it is closely related to the "semiseparable rank" in the Mamba2 paper.
* Beyond Finding 1, the other empirical findings seem to be very narrow and not especially useful or insightful.

### Questions
* Can the authors provide a clear definition of ESS, explaining whether it is a function of the model or the data, and describe how it is computed in practice? The two approaches introduced in Section 2.4 do not seem to be ever discussed in the paper again.
* Similarly, how is the TSS different from the conventional notion of state size?
* Minor: Why use the term "input-varying _linear_ operator"? Input dependence typically renders the operator non-linear, and I believe that any differentiable map $y=F(u)$ satisfying $F(0)=0$ can be expressed in the form $y = M_F(u) u$

### Soundness
2

### Presentation
2

### Contribution
2
