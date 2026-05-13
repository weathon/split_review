# You Only Scan Once: Efficient Multi-dimension Sequential Modeling with LightNet

- Decision: Reject
- Scores: 5, 3, 3, 8

## Abstract
Linear attention mechanisms have gained prominence in causal language models due to their linear computational complexity and enhanced speed. However, the inherent decay mechanism in linear attention presents challenges when applied to multi-dimensional sequence modeling tasks, such as image processing and multi-modal learning. In these scenarios, the utilization of sequential scanning to establish a global receptive field necessitates multiple scans for multi-dimensional data, thereby leading to inefficiencies. This paper identifies the inefficiency caused by a \enquote{multiplicative} linear recurrence and proposes an efficient alternative \enquote{additive} linear recurrence to avoid the issue, as it can handle multi-dimensional data within a single scan. We further develop an efficient multi-dimensional sequential modeling framework called LightNet based on the new recurrence. Moreover, we present two new multi-dimensional linear relative positional encoding methods, MD-TPE and MD-LRPE to enhance the model's ability to discern positional information in multi-dimensional scenarios. Our empirical evaluations across various tasks, including image classification, image generation, bidirectional language modeling, and autoregressive language modeling, demonstrate the efficacy of LightNet, showcasing its potential as a versatile and efficient solution for multi-dimensional sequential modeling. \blfootnote{\noindent $^\textrm{\Letter}$ Indicates corresponding author (Email address: \textit{zhongyiran@gmail.com}).}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
1. The paper presents *LightNet*, a new variant of State Space Models (SSMs) incorporating an additive decay/selectivity parameter. Unlike Mamba or Linear Attention (LA) with decay, LightNet avoids recursion-based parallelization, achieving faster parallelization using only matrix multiplications, similar to LA without decay.

2. To address permutation invariance in non-causal settings (a characteristic it shares with LA), the authors introduce two multi-dimensional positional encodings MD-TPE and MD-LRPE.

3. The model is evaluated across diverse tasks, including autoregressive and bidirectional language modeling, image classification and generation.

### Strengths
1. The authors identify that SSM-based methods like Mamba and LA with decay suffer from slow GPU performance due to recursion-based parallelization. In contrast vanilla LA is fully parallelizable via matrix multiplications but underperforms other SOTA SSMs.
 
2. To introduce decay to improve LA's performance while retaining full parallelizability, they derive the mathematical formulation of the linear operation induced by a decayed recurrence and using this they motivate an “Additive” decay mechanism, that allows for a decay with matrix multiplication-based parallelization.

3. They evaluate their model across a broad range of tasks and demonstrate near competitive performance against SOTA methods.

### Weaknesses
 **1. Saturation of Additive Decay for Long Sequences**

The proposed additive decay mechanism, defined as $g(t) = \sum_{s=1}^{t} \delta(s)$, tends to saturate for long sequences. As the decay accumulates $\delta$ values over the course of a long sequence, $g(t)/g(s)$ reaches a point where it can no longer distinguish between nearby tokens effectively. This may be problematic for language modeling as it has a strong local bias.

This saturation effect will likely be more pronounced with very long sequences or on large-scale models. **I am curious how LightNet might perform compared to Mamba in this setting**, which has the opposite issue: difficulty paying attention to very distant tokens despite selectivity. I suspect LightNet may struggle with paying attention locally at scale, potentially leading to underperformance on long sequences.

**2. Comparing LA and LightNet on Long Sequences**

In line with the reasoning above, I feel that LA and LightNet may have similar performance at scale. This is due to LightNet's decay factor saturating to 1. To better understand this, an ablation study comparing LightNet directly with Linear Attention, keeping all other factors constant, would be useful. Specifically, I suggest replacing the additive decay with vanilla LA’s $\phi(K)$ (substituting `softmax(K)` with $\phi(K)$). Additionally, scaling up model sizes could reveal whether the performance gap between LightNet and Linear Attention narrows, providing insight into the effectiveness of additive decay.


**3. It is unclear how much of the heavy lifting is being done by the position embeddings**.

I believe there is a chance that the position embeddings may be doing a lot of the heavy lifting in getting good performance. For instance Toeplitz matrix in itself is a performant SSM [1] and may artificially boost the apparent efficacy of Additive Decay. Can authors maybe use 2D rope as the position embedding and see if they improve/compete with original LightNet, LightNet with no position embeddings and Linear Attention.

### Questions
1. In the paper you do claim that you have results on 1B language modeling as well. Could you please share them?
2. Could you also compare against vanilla LA especially on larger scales. This helps prove/disprove my hypothesis.
3. Could the authors please explain how is the method implemented through matrix multiplications in the causal setting? I am not able to figure out the vectorized formula for the same that computes in O(Sequence Length) time.
4. Could the authors please clarify what they mean by "parameter tiling strategy" in Line 266, and if and why this is not implemented for non-causal settings?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper addresses the question of how to efficiently model multi-dimensional data with modern architectures. The authors first categorize existing linear recurrence approaches into additive and multiplicative scans, demonstrating that the additive approach is significantly more efficient. By exploring the fundamental formulation of additive scans, they propose LightNet - a linear-attention-based model variant that can be implemented in a single scan, resulting in a highly efficient model. Empirical analysis shows that LightNet achieves competitive results in both language modeling and vision tasks.

### Strengths
-	The paper addresses an important question: how to efficiently process multimodal data using modern DL models.

-	The proposed '1 Scan' strategy significantly reduces latency.

-	The results are promising, demonstrating improvements over the selected baselines.

### Weaknesses
 
**W.1. The paper lacks clarity** and contains numerous typos in critical sections, making it difficult to understand key aspects of the methods and results. For example:

- In the method section, line 280, a softmax operation is mentioned, yet the authors claim the transformer relies on linear attention. This inconsistency is especially problematic given the absence of a reference code. The use of softmax within the Key module, while not directly related to Softmax Attention, still requires clarification regarding its specific role and impact on the overall linear attention mechanism. The authors need to elaborate on why a softmax activation is used here, and how it interacts with the linear attention framework, especially given that other linear attention variants often omit this step.

- In the method section, line 283, the variables W_{u1} and W_{u2} are referenced, but they do not appear to be introduced or explained. The lack of explicit definitions for these weight matrices makes it difficult to reproduce the results and understand the underlying architecture. The authors should provide a clear explanation of how these matrices are derived or initialized, and how they contribute to the gating mechanism.

- In the method section, line 247, there seems to be a double exponent function. Is "exp(-exp(x))" correct, or is this a typo? The use of a double exponential function for decay is unusual and requires a more detailed explanation. The authors should justify this choice and discuss its implications for the model's behavior, especially in comparison to more standard decay functions.
- Broken references are present (lines 180, 401).

- Unclear notation: In Section 4.1, equations (7-9), the distinction between bold and standard letters is not defined. The lack of clear notation makes it difficult to understand the mathematical formulation of the proposed method. The authors should explicitly define the meaning of bold and standard letters, and ensure consistency throughout the paper.

- Additional typos: line 159 (“E.q 3” should be “Eq. 3”), line 413 (“modeling..” should be “modeling.”).

**W.2. Missing Baselines (and related work) in linear attention variants:** The paper does not discuss several existing transformer-based linear attention models that have demonstrated improved performance in certain contexts. Examples include Mega [2] and Megalodon [3], which are also based on gating and decay mechanisms. The authors should also include a discussion, possibly in a new subsection, on how LightNet (equations 7-9) compares to similar variants that omit the softmax. The absence of a thorough comparison with these models makes it difficult to assess the novelty and advantages of the proposed approach. A detailed analysis of how LightNet differs from these methods, particularly in terms of computational efficiency and performance, is crucial.

**W.3. Missing Baselines and related work on N-Dimensional position encoding:** As far as I understand, the authors did not discuss or benchmark previously proposed N-D position encoding methods. Is this correct? Numerous approaches address this, see [1] as an example. The authors need to justify the design choices for their N-dimensional position encoding scheme, and explain why existing methods are not suitable or less efficient. A comparative analysis with existing N-D position encoding techniques is necessary to demonstrate the advantages of the proposed approach.

**W.4. Limited scope of experimental validation**: While the paper claims to support n-dimensional data, experiments are conducted only on 1-D and 2-D cases. The lack of experiments on higher-dimensional data limits the generalizability of the results. The authors should provide empirical evidence demonstrating the effectiveness of LightNet on datasets with more than two dimensions.

**W.5. The statistical significance** of the results is not well-defined. Were the experiments run over multiple seeds? In some cases, such as the ablations without PE, performance gains are marginal. Could the authors clarify the robustness and significance of these results? The absence of statistical significance analysis makes it difficult to determine whether the observed improvements are genuine or due to random chance. The authors should provide confidence intervals and p-values to support their claims.

### Questions
Q.1. Can the authors present FLOPs and latency analysis against highly optimized implementations, such as FlashAttention and Mamba?

Q.2. Selective mechanisms, such as Mamba and the selective transformer, emphasize empirical advantages. Can these (or similar variations) be incorporated with the 1-S approach?

See additional questions under Weaknesses (e.g., W.5).

### Soundness
2

### Presentation
1

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
This paper proposes a formulation for the decay function of the linear attention models in order to enable single-pass processing of multi-dimensional signals (such as image) in transformers. The authors also propose two positional embedding functions for multi-dimensional data, extending the previous formulations in the literature to multi-dimensional settings.

### Strengths
The paper tackles an important problem re: processing of multi-dimensional data using linear transformers and its performance implications. 

The paper also proposes two novel positional embedding formulations for multi-dimensional data which are interesting and to my limited knowledge novel.

The range of the empirical study is also quite wide and contains image classification, image generation and language modeling with lots of comparisons across different models.

### Weaknesses
1- Overall, this paper is poorly written; the general argument is quite vague, and the derivation is unclear with vague notation. In particular:

A) What does it mean that $a_t$ "cannot provide global information"? What do authors mean by "global information" here? I can think of any monotonic function of $t$ to capture the global information re: the position, or any aggregation function (sum, product, etc) to capture the global information re: the value. The authors need to clarify what specific properties of $a_t$ they consider to be lacking for capturing global information, and why a simple function of $t$ cannot suffice.

B) In Sec 3. the decay function is presented as a function of $t$; however, in Sec 4. all of the sudden the decay is a function of the key variables themselves with no further explanation. Why should the decay be a function of keys and not simply their time indices? There's no explanation whatsoever. This shift in the decay function's dependency is not justified and lacks a clear motivation. The authors need to provide a rationale for why a data-dependent decay is necessary and how it relates to the goals of single-pass processing.

C) Figure 3 is not consistent with the formulation presented in Eqs. 7, 8 & 9. For instance, it's not clear if the $phi$ transformation is applied on $U$ or not and if so, why should that be the case. The diagram needs to be revised to accurately reflect the mathematical operations and clarify the role of the $\phi$ transformation.

D) What is "y" in Eq. 10 & 11? Also there's no intuitive explanation of where these formulations come from. The authors need to provide a clear definition of "y" and explain the motivation behind these specific positional encoding formulations. The connection to existing positional encoding methods should also be discussed.

I'd highly recommend the authors to (I) rewrite Sec 4 and their preceding arguments in a clear manner, (II) provide a section or appendix re: any background relevant to their work because the current manuscript is not self-contained, and (III) make sure all the notations used in the paper are consistent and clearly defined.

2- The main contribution of the paper is not clear. In particular,

A) Theorem 3.1 is simply the textbook solution for the first-order non-homogeneous recurrence equations with variable coefficients (which is what Eq. 3 is, mathematically speaking), which is already a established result. The authors need to clearly articulate the novelty of their approach, beyond simply applying a known mathematical result. The specific insights gained from this application should be highlighted.

B) The distinction between the "multiplicative" and "additive" cases is not clear. The additive case is indeed a special case of the multiplicative case where one chooses $\rho$ to be the ratio proposed for the additive case. In other words, the proposed supposedly "additive" decay formulation is in fact multiplicative underneath. The authors should clarify the fundamental differences between their proposed decay formulations and avoid using potentially misleading terminology. A more rigorous mathematical analysis of the properties of each decay function is needed.

Instead of using confusing terminology, I'd recommend authors to clearly state their contribution re: their choice of decay function and the theoretical intuitions behind it.

3- The empirical results are not particularly conclusive. More precisely,

A) If the main contribution of the paper is achieving better results with a single pass, then it makes sense for the baselines to run on single pass setting as well and then measure the potential improvement the proposed method has achieved using the proposed decay formulation. For the current reported results, it's not exactly clear where the benefit comes from. The authors need to conduct a more controlled experiment where the baselines are also evaluated in a single-pass setting to isolate the impact of the proposed decay function.

B) In table 1, it's really hard to pinpoint the main source of improvement as there are many other factors among these models that are not controlled. The authors should provide a more detailed analysis of the results, controlling for other factors that might influence the performance, such as model architecture and training parameters.

C) In addition to controlling for the number of passes, the authors should also control for model size. For instance, in Table 3, the model sizes need to be reported. The authors should report the model sizes for all experiments to allow for a fair comparison.

D) Since language is not a multi-dimensional signal, it is not clear what hypothesis exactly the authors are trying to test by the language experiments. In particular, is the comparison against other linear attention models of the same size? Or is it against any model of the same size? Or is it against any model whatsoever (i.e. beating the leaderboard)? In other words, what exact part of the proposed framework are we testing here and how do we control for other factors that are NOT being tested? There are too many uncontrolled factors here: models' architectures, models' sizes, models' kernel embedding functions (for linear attention models), the decay formulation, etc. This means that the presented results are to be interpreted as leaderboard benchmark results, but is that your claim to beat the leaderboard for these tasks? The authors need to clearly define the experimental setup for the language modeling task and justify the choice of baselines. The specific contribution of the proposed method in this context needs to be clarified.

E) The "parameter sharing" contribution is first mentioned in the ablation study section and unlike what is claimed there, there is no single mention of it in the methodology sections before! Is it another contribution of the paper? If so, then it needs to clearly stated so and fully explained in the methodology section.

### Questions
Please see my comments above.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors start by exploring the space of linear recurrences, and when they can represent linear combinations.  They then define a constraint to keep this recurrence numerical stable, and two different ways to satisfy the constraint.  They call these “additive” and “multiplicative”.  

They show that the SSMs normally use a “multiplicative” linear recurrence, which stops information from “future” of the sequence affecting the current position, requiring two scans along a sequence, one forward and one backward.   Instead, they modify their “additive” linear recurrence to be a “global” summary of information present by modifying the normalization. They show this modified and novel “additive” linear recurrence is significantly computationally cheaper than a 2-scan approach (Figure). This is particularly useful when dealing with multi-dimensional arrays, where there is no natural scan order, and multiple scans in different orders might be required.    They also demonstrate that using one-scan is significantly faster in practice (Figure 2), but they do not compare speed for their other experiments.

However, their ‘additive’ linear recurrence loses the relative position of tokens, so they introduce two new forms of positional encoding they call Multi-Dimensional Toeplitz Position Encoding (MD-TPE), and Multi-Dimensional Linearized Relative Positional Encoding (MD-LRPE), where MD-TPE is applied after the input embedding and MD-LRPE is applied after each Q/K computation.   

Together, they use their one-scan attention and MD-LRPE blocks to construct a LightNet Attention (LNA) block, which alternates with a Gated Linear Unit (GLU) to construct what they call the LightNet.  

They empirically test the performance of LightNet in both multi-dimensional image classification and generation tasks, as well as at word modeling tasks.  

In image classification, they show that they perform similar to the system doing full softmax attention or multi-scan attention , while they only require their one scan system, which should be faster.  In Image generation, they demonstrate SOTA FID compared to the other methods.

In the bidirectional language modeling, they compare in 24-hour training regime, and LightNet significantly outperforms all other methods.  In autoregressive LM, they match MAMBA performance, which makes sense.

### Strengths
Originality:
To my knowledge both the “additive” linear recurrence and corresponding improvements to the positional encodings system are novel, and important for non-linear regimes.  

Quality:
The technical claims are clear and appear to be solid. However, see note about it being hard to compare the computational efficiency of their methods vs. competitors due to not reporting timings in weaknesses section.  

Clarity:
The paper is clearly written and relatively easy to follow, with experiments described in sufficient detail that they could be reproduced, as well as network.  However, note that the appendices also appear to be missing, which includes one of the smaller proofs from the paper.

Significance:
They demonstrate SOTA on some of their tasks, so it is definitely the best method to use in at least certain situations.  This combined with their claims of gains in computational efficiency could make LightNet the network of choice in various situations.  It’s also surprising that their modification works as well as it does, so that itself may lead to more interesting results and modifications.

### Weaknesses
It would be more informative if the timing information for the evaluation/training iteration per experiment were reported along with the results, as opposed to only being shown in Figure 2.  As it is, it is hard to judge what computational speed difference it makes in practice, which is one of the main attractions of their method.  Assuming the results in Figure 2 apply to the other methods, it would make it more impressive.  At least why this wasn't included should be addressed in the text.  

There are no error bars on any results, which makes it harder to be sure that the differences are meaningful.  However, this could be understandable given the computational expense involved.  A comment on how much variability was seen if multiple runs were performed would be useful. 

Their results table a not that easy to parse - bolding winners on each table would make it quicker and easier to read.  

There are some places where an appendix is referenced, but there are no appendices. E.g., the proof of Equation 4 is missing.

There is still a “directionality” in the additive linear recurrence, as the terms before and after a specific position have different weightings (there is a sum to the LHS, but not the RHS of a term).  Could you provide more intuition about why this asymmetry doesn't matter in practice?

### Questions
There is still a “directionality” in the additive linear recurrence, as the terms before and after a specific position have different weightings (there is a sum to the LHS, but not the RHS of a term).  Could you provide more intuition about why this asymmetry doesn't matter in practice?

It’s not clear what the setup is in Figure 2 - you say you substitute the attention block, but in what setting/dataset?

### Soundness
3

### Presentation
3

### Contribution
3
