# Wavelet-based Positional Representation for Long Context

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
In the realm of large-scale language models, a significant challenge arises when extrapolating sequences beyond the maximum allowable length. 
This is because the model's position embedding mechanisms are limited to positions encountered during training, thus preventing effective representation of positions in longer sequences.
We analyzed conventional position encoding methods for long contexts and found the following characteristics.
(1) When the representation dimension is regarded as the time axis, Rotary Position Embedding (RoPE) can be interpreted as a restricted wavelet transform using Haar-like wavelets. 
However, because it only uses a fixed scale parameter, it does not fully exploit the advantages of wavelet transforms, which capture the fine movements of non-stationary signals using multiple scales (window sizes). 
This limitation could explain why RoPE performs poorly in extrapolation.
(2)
Previous research as well as our own analysis indicates that Attention with Linear Biases (ALiBi) functions similarly to windowed attention, using windows of varying sizes.
However, it has limitations in capturing deep dependencies because it restricts the receptive field of the model.
From these insights, we propose a new position representation method that captures multiple scales (i.e., window sizes) by leveraging wavelet transforms without limiting the model's attention field.
Experimental results show that this new method improves the performance of the model in both short and long contexts. 
In particular, our method allows extrapolation of position information without limiting the model's attention field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors proposed wavelet-based positional encoding for the length extrapolation problem of language models. The motivation is based on an observation that the widely used Rope is related to wavelet transform via simple Haar wavelet functions with a fixed scale. By further investigating the properties of ALiBi, the authors modified the form of relative positional encoding to use wavelet transform based approaches. Several experiments are conducted to demonstrate the performance of the proposed positional encoding.

### Strengths
1. The paper is easy-to-follow. 
2. The length extrapolation problem is important for language models.

### Weaknesses
 1. **There exist gaps from the motivation to the proposed approach**. In Section 3 and 4, the authors provide analysis on the relationship between RoPE and wavelet transform, and the properties of ALiBi like positional encodings. The ability of ALiBi to accommodate multiple window sizes is concluded as the key point for better length extrapolation performance, while RoPE is claimed to be worse. Based on these statements, a natural question is, what is the advantage of using wavelet transform? The authors do not provide enough supportive quantitative evidence for it, but directly modify the relative positional encoding by using wavelet transform. If it has superiorities, why don't we follow the form of RoPE to use wavelet transform instead of RPE? These points should be better clarified to make the motivation of the proposed approach more convincing.

2. **The design choice for the proposed approach should be better supported**. In Section 5, the authors propose to use Ricker Wavelet as the base function of wavelet transform, and set the shift and amplititude parameters with predefined strategies. However, the reasons to choose these designs are not well clarified (except lines 294-303, which are rather superficial).

3. **The empirical improvement is marginal**. From Table 2 and 3, we can see that the proposed PE does not show significant improvement compared to compared approaches such as ALiBi, which is proposed in 2022 and is not the state-of-the-art nowadays. The evaluations are also limited in task types and scales. Overall, the empirical results are not convincing to show the superiority of the proposed approach.

### Questions
See the Weaknesses.

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
the paper presents a novel positional encoding method leveraging wavelet transforms to address the challenges of limited receptive field and  extrapolation in LLMs. 

The proposed wavelet-based approach aims to overcome these limitations by introducing a multi-scale analysis that captures the fluidity of natural language and enhances the model's ability to extrapolate beyond its training context length.

In extrapolation experiments, model that used Ricker-based wavelet positional embedding had the lowest PPL trained on the WikiText-103 dataset, compared with RoPE, ALibi, Transformer-XL.

### Strengths
- The authors provide a solid theoretical foundation by drawing parallels between RoPE and wavelet transforms, and by extending this analogy to propose their method.
- The proposed method has the potential to be widely applicable to various transformer-based models
- The paper is easy to read and positions itself clearly with respect to related work.

### Weaknesses
 - The paper primarily evaluates the method on language modeling tasks. It would be valuable to see how the approach generalizes to other NLP tasks such as question answering or text summarization.
- The paper does not provide sufficient experimental evidence to support the authors' claim that Wavelet Transform can capture the dynamic changes in a sequence over positions.（L84-85）
- See my questions/suggestions below

### Questions
- How did the “shift and scale parameters” been decided? Is there any ablation study or results for this particular setting?
- Did you compare the length extrapolation results with other RoPE-based methods? (eg. relative works you mentioned in L47-L48)
- Both RoPE and Wavelet methods aim to model distances at different scales by placing them in different dimensions [1]. In Figure 3, the diagonal lines in the RoPE plot appear because the model can focus on the features of specific token distances. However, Wavelet functions do not have this stable frequency inductive bias, which is why they do not produce diagonal patterns in the attention scores. Do you think this is a desirable property?
- In the experiment represented by Figure 3, what kind of text is input into the model? Why is the initial word particularly important? Which specific tokens does the model attend to? Is this phenomenon common?

[1] Hong, Xiangyu, et al. "On the token distance modeling ability of higher RoPE attention dimension." arXiv preprint arXiv:2410.08703 (2024).

### Soundness
2

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
4

### Summary
The paper proposes a wavelet transform-based positional representation for transformer models. It begins with highlighting the properties of existing position representation techniques such as relative position bias, RoPE and ALiBi. The authors then show how RoPE can be interpreted as a single scale wavelet transform with a Haar-like wavelet. Then the authors present a position embedding based on wavelet transform. This multi-scale embedding can be viewed as a generalization of RoPE and possess attractive "multi-window" properties of ALiBi. Experiment results have been reported on short and longer-context scenarios showing improved perplexity over existing methods and better extrapolation properties.

### Strengths
- The paper is well-written barring some typographical errors. It motivates the problem well, starts with a well-defined goal, describes existing methods clearly, and presents the proposed method in a manner which is easy to appreciate.
- The paper tackles a critical problem of context length extrapolation which often arises in practical settings. The method holds significance, not just for the language modeling community, but also other domains such as time series forecasting where context length extrapolation may improve the performance of models on high-frequency data (see [1]). 
- The proposed method is novel to the best of my knowledge. It creatively relates RoPE to time-frequency analysis and proposes a promising method based on wavelet transforms. 
- The method outperforms alternatives and scales gracefully with extrapolated context lengths. 

[1] Ansari, Abdul Fatir, et al. "Chronos: Learning the language of time series." arXiv preprint arXiv:2403.07815 (2024).

### Weaknesses
 - The paper is well-written barring some typographical errors. It motivates the problem well, starts with a well-defined goal, describes existing methods clearly, and presents the proposed method in a manner which is easy to appreciate.
- The paper tackles a critical problem of context length extrapolation which often arises in practical settings. The method holds significance, not just for the language modeling community, but also other domains such as time series forecasting where context length extrapolation may improve the performance of models on high-frequency data (see [1]). 
- The proposed method is novel to the best of my knowledge. It creatively relates RoPE to time-frequency analysis and proposes a promising method based on wavelet transforms. 
- The method outperforms alternatives and scales gracefully with extrapolated context lengths. 

 - While the discussion of related methods is generally well done, discussion of RoPE scaling techniques (linear, NTK-aware) is missing. A discussion and comparison with these techniques would significantly improve the positioning of this work. Specifically, the paper should discuss how the proposed wavelet-based approach compares to methods that scale the RoPE frequencies, such as linear interpolation or NTK-aware scaling, in terms of both performance and computational cost. The absence of this comparison makes it difficult to assess the true advantage of the proposed method.
- The results reported in sections 6 and 7 are excellent proofs of concept but they lack comprehensiveness. Particularly, in section 7, evaluations beyond the CodeParrot dataset would be needed to thoroughly appreciate the proposed method. Furthermore, the paper only evaluates the model in term of the perplexity. For a stronger evaluation, this needs to be augmented with task-based evaluations. Apart from common language tasks, you might also want to consider associative recall tasks [2] and the long range arena [3] since the focus of this work is context length extrapolation. To further demonstrate the robustness of the proposed method, domains beyond natural language may also be considered, for example, DNA modeling [4], audio generation [4] and time series forecasting [1]. The current evaluation is limited to perplexity on language modeling tasks, which does not fully capture the potential of the method for long-range dependencies and extrapolation. For example, the paper should also consider evaluating the method on tasks that require reasoning over long contexts, such as question answering or document summarization. Furthermore, the paper should consider evaluating the method on tasks that require extrapolation to longer sequences than seen during training, to fully demonstrate its extrapolation capabilities.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper conducts a unified analysis of positional encoding methods in large language models and proposes a novel wavelet-based approach. The work begins by demonstrating that RoPE can be interpreted as a restricted wavelet transform using Haar-like filters operating at a fixed scale. The authors then analyze ALiBi, revealing that it functions similarly to windowed attention with varying window sizes but is limited by constraints on the attention mechanism's receptive field. Building on these insights, the paper introduces a new wavelet-based positional representation method that leverages multiple scales through wavelet transforms. The method is designed to capture both local and long-range dependencies without restricting the model's receptive field. The authors validate their approach through experiments on short and long contexts.

### Strengths
1. The motivation and connection are clear as the authors provide a unified analysis of the positional encoding methods.
2. The paper introduces a new wavelet-based positional representation method that leverages multiple scales through wavelet functions.
3. The proposed wavelet positional embedding shows improvements across tasks.

### Weaknesses
1. Novelty Concerns:
- The core idea of wavelet-based positional encoding has been explored in the previous work GMT (Ngo et al., 2023a,b), which uses graph wavelets to generate node positional representations that can capture the structural information of a center node on the graph at different resolutions, though in a different domain. However, there is insufficient discussion of how this approach differs fundamentally from or improves upon prior works.
2. Mathematical Rigor:
- The unified comparison for different positional encodings is not rigorous as the wavelet property needs stronger mathematical justification. The proposed "Haar-like wavelets" in Equation (7) require verification of wavelet admissibility conditions beyond just square integrability. Specifically, the zero-mean condition, a crucial aspect of wavelet theory, is not explicitly addressed or verified for the proposed functions. Furthermore, the connection between the proposed 'Haar-like' functions and actual Haar wavelets is not rigorously established, potentially leading to misinterpretations of the theoretical underpinnings.
3. Experimental Design:
- Limited exploration of wavelet families (only four tested). The choice of wavelet families seems arbitrary, and there is no clear justification for why these specific families were selected over others. This lack of exploration limits the generalizability of the findings. Furthermore, the paper does not explore discrete wavelet transforms, which are commonly used in signal processing and could offer computational advantages.
- Insufficient analysis of scale parameter choices (only two tested). The paper does not provide a systematic analysis of how the scale parameters affect the performance of the proposed method. The choice of only two scale parameters is insufficient to draw meaningful conclusions about the optimal parameter settings. The lack of sensitivity analysis on these parameters makes it difficult to assess the robustness of the method.
4. Minor issues:
- The paper lacks of clear notation definition and problem setup affects readability. For example, the specific meaning of the time variable 't' in the context of sequence data is not clearly defined, and the relationship between 't' and the sequence index is not explicitly stated. This lack of clarity makes it difficult to understand the mathematical formulation of the method.
- Inconsistent terminology between abstract ("simple Haar wavelets" in Line 18) and technical content ("Haar-like wavelets" in Sec 3.2).
- The phrase 'single window size' (in Line 19) should be replaced with 'fixed scale parameter' to align with standard wavelet terminology, as it specifically refers to the dilation factor in wavelet transforms.
- The space definition L⊭(R) in Line 135 appears to have a typographical error - it should be L²(R), the space of square-integrable functions.
- Some mathematical notation is not explicitly defined. For example, the superscript T in equation (3) seems to represent the length of a discrete sequence, but this isn't explicitly defined.

### Questions
1. How does your approach fundamentally differ from MGT's wavelet position encoding?
2. Can you provide formal verification of the wavelet admissibility conditions for the proposed "Haar-like wavelets"? Or what else condition you might need to add to make it a wavelet?
3. Why were these specific wavelet families chosen? Have you explored other wavelet families, particularly discrete wavelets like Daubechies or biorthogonal wavelets?
4. What guided your choice of scale parameter ranges? Have you conducted sensitivity analyses on these choices?
5. What is the theoretical justification for removing the $\frac{1}{\sqrt{a}}$ amplitude term?

[1] Ngo, Nhat Khang, Truong Son Hy, and Risi Kondor. "Multiresolution graph transformers and wavelet positional encoding for learning long-range and hierarchical structures." The Journal of Chemical Physics 159.3 (2023).

### Soundness
2

### Presentation
2

### Contribution
2
