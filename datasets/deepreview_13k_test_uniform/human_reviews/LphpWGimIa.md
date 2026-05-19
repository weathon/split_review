# Interpreting Attention Layer Outputs with Sparse Autoencoders

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Decomposing model activations into interpretable components is a key open problem in mechanistic interpretability. Sparse autoencoders (SAEs) are a popular method for decomposing the internal activations of trained transformers into sparse, interpretable features, and have been applied to MLP layers and the residual stream. In this work we train SAEs on attention layer outputs and show that also here SAEs find a sparse, interpretable decomposition. We demonstrate this on transformers from several model families and up to 2B parameters. 

We perform a qualitative study of the features computed by attention layers, and find multiple families: long-range context, short-range context and induction features. We qualitatively study the role of every head in GPT-2 Small, and estimate that at least 90\% of the heads are polysemantic, i.e. have multiple unrelated roles.

Further, we show that Sparse Autoencoders are a useful tool that enable researchers to explain model behavior in greater detail than prior work. For example, we explore the mystery of why models have so many seemingly redundant induction heads, use SAEs to motivate the hypothesis that some are long-prefix whereas others are short-prefix, and confirm this with more rigorous analysis. We use our SAEs to analyze the computation performed by the Indirect Object Identification circuit (\citet{wang2023interpretability}), validating that the SAEs find causally meaningful intermediate variables, and deepening our understanding of the semantics of the circuit. 
We open-source the trained SAEs and a tool for exploring arbitrary prompts through the lens of Attention Output SAEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper applies sparse autoencoders (SAEs), a popular technique in mechanistic interpretability, to the output of attention layers in pre-trained Transformer models, and develops a novel attribution method to deal with multiple attention heads. Using these techniques, the authors arrive at several insights such as identifying specific feature families in GPT-2, identifying different roles of the attention heads such as "long" and "short prefix induction", and a better understanding of position features for "indirection object identification". Based on these findings, the authors make the case for SAEs applied on attention layer outputs as an effective tool for mechanistic interpretability in transformers.

### Strengths
**1.** This work makes progress on an important question, namely mechanistic interpretability in transformer models.

**2.**  I found the paper to be very well written. Namely, the writing is concise and clear, and well motivates the authors approach and the problem setting in general. 

**3.** I very much appreciated how the authors describe their contribution in the introduction, and avoid making any overclaims. I also found the discussion of limitations throughout the paper to be very transparent.

**4.** The findings presented by the authors, particularly in Section 4.2 and 4.3, I found to be interesting and potentially impactful.

**5**. More generally, the empirical study conducted by the authors appears to be very thorough and varied, with numerous interesting findings. However, I cannot say this with complete confidence as I am not an expert in interpretability.

### Weaknesses
**1.** In terms of novelty, the paper is somewhat limited as it is essentially applying existing techniques to a new setting. However, I don't view this as a particularly notable weakness, and importantly, the authors are very upfront about this and their contribution in general.

**2.** One issue I had with this work is that I found the overall structure and presentation of results to be a bit convoluted and unfocused. Specifically, the authors have a large number of findings they want to include and discuss in the manuscript. However, presumably due to space constraints, many of these findings are discussed somewhat superficially in the main text and then the appendix is referenced for further details. Such appendix references occur very often throughout the paper, which made several findings feel rather non-thorough and superficial to me. To this end, I think the paper would have benefitted from focusing more thoroughly on a smaller number of core results.

**3.** My main issue with this work is that I found it difficult to interpret several experimental findings. Specifically, there are several instances throughout the paper, where I felt like the authors presented their findings, without sufficient explanations or experimental evidence to substantiate the claims. I think this was done for reasons similar to those described in **2.**. Namely, that the authors had many findings they wanted to discuss but limited space. Consequently, however, I often felt that I was just taking the authors word for a claim, and was not presented with evidence in the manuscript to understand the validity of the claim.

For example, in Section 4.1, the authors give a description of their findings on the role of different attention heads in GPT-2. However, I did not find any evidence presented to the reader substantiating these claims. Additionally, in Section 3.3 the authors discuss that there are features which take the role of "induction features". However, I found it difficult to understand how the authors verified this based on what was presented in the main text. I presume this was done via Figure 2, however, I had challenges making sense of this empirical protocol based on the explanations given. I am not an expert in this space, so it could be that I am missing something. However, perhaps the authors could explain in a bit more detail, how the "board induction" feature was identified and how this hypothesis was substantiated empirically.

### Questions
**1.** The authors mention three different feature families found in 3.3. How did the authors arrive at these three categories. At the surface, they feel a bit arbitrary, so I am curious how they were formulated.

**2.** Can the authors provide some empirical evidence, e.g. a few visual examples, to better understand the findings in 4.1.

**3.** As discussed above, can the authors give a deeper explanation of how the induction features in 3.3 were discovered and the empirical evidence to back this up.

### Soundness
2

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
This paper proposes using sparse autoencoders (SAEs) to mechanistically interpret the outputs of attention layers, similar to SAEs that have previously been used to understand LLM residual streams and MLP layers. The contributions of this work include open-sourcing many trained SAEs, qualitative analysis of the types of features learned by these SAEs, and providing a case study of using these attention layer SAEs to better understand the Indirect Object Identification circuit.

### Strengths
- The paper is clear, the writing is easy-to-understand, and the experiments are sound and logical.
- The IOI case study presents an interesting causal analysis of the findings that backs up what are otherwise mainly qualitative results.
- The insights into induction heads and the difference between “long” and “short” prefix induction are novel and interesting.

### Weaknesses
- Do the authors believe that the insights from this paper are specific only to attention output SAEs, or that the same insights could be derived from MLP or residual stream SAEs of great enough size? Further discussion of why the results are specific to attention output SAEs would significantly strengthen the contribution of the paper. 
- One of the contributions of this work is finding that SAEs learn /interpretable/ features when applied to attention outputs; however, it seems that interpretability is not well-defined in this work and is measured quite qualitatively/ad-hoc, as acknowledged by the authors in the limitations. As such, it would be very helpful if some random examples of interpretable and uninterpretable features were provided in the main paper and the process by which they were interpreted, such that reviewers/readers could calibrate their understanding of what it means without having to search through the visualizer.
- Is labeling scalable for attention output SAEs via methods such as auto-interpretability as it is with other SAEs? Without automatic labeling, do the authors see this method as a feasible way to achieve interpretability of language models or attention?

### Questions
- Given that prior work notes that looking only at top-activating features when interpreting SAE features is not optimal, is there a reason why this interpretation procedure was chosen (for example, see https://blog.eleuther.ai/autointerp/). Results from labeling with a distribution of activations would be interesting to see.
- What do the error bars in Fig 4 correspond to? It is unclear to me if the results shown are significant given the size of the error/std/etc bars.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper applies sparse autoencoders, a popular tool in mechanistic interpretability, to interpret attention layer outputs as opposed to residual or MLP layers in large language models, as is usually done. The paper argues that this is a useful tool to understand transformer circuits, based on qualitative analysis. The paper applies its methods to understand induction heads, and study the Indirect Object Indentification (IOI) task.

### Strengths
+ The paper is easy to read, and adequately discusses the recent related work on mechanistic interpretability, particularly sparse autoencoders

+ The paper attempts to also independently verify the SAE-based insights obtained via non-SAE-based analysis, i.e., by using both correlational and intervention-based evidence

### Weaknesses
- A critical drawback of this paper is the non-systematic and ad-hoc nature of its analysis. For example, the paper includes phrases such as "we manually inspect these features for all 144 attention heads in GPT-2 Small. Broadly, we observe that features become more abstract in middle-layer heads and then taper off in abstraction at late layers", and "We use our weight-based head attribution technique (see Section 4.1) to inspect the top SAE features attributed to two different induction heads and find one which specializes in long prefix induction (Goldowsky-Dill et al., 2023), while the other primarily does short prefix induction", where qualitative findings are directly stated without providing any details such as how such inferences are being made by the researchers. This renders the method and its results hard to reproduce, and its interpretability benefits impossible to independently verify. The qualitative nature of analysis alone is not a problem, as such analysis can be made systematic and rigorous using well-designed human studies, which, unfortunately, are missing in this paper.   

- This paper does not introduce any novel methods, ideas, or insights into interpretability. Rather, it claims that using SAEs on attention layers results in improved interpretability benefits, which, as mentioned above, is completely unverifiable. 

- The introduction section in this paper correctly identifies several use cases of mechanistic interpretability, such as (1) identifying and debugging model errors, (2) control and steering of model behavior, and (3) prediction of OOD behavior. Unfortunately, none of these downstream use-cases are demonstrated with the proposed approach; nor are they benchmarked against previous SAE approaches; making it hard to understand the purported advantages of the presented approach.

### Questions
N/A

### Soundness
1

### Presentation
2

### Contribution
1
