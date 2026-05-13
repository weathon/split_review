# Systematic Outliers in Large Language Models

- Decision: Accept
- Scores: 8, 8, 3, 6, 5

## Abstract
Outliers have been widely observed in Large Language Models (LLMs), significantly impacting model performance and posing challenges for model compression. Understanding the functionality and formation mechanisms of these outliers is critically important. Existing works, however, largely focus on reducing the impact of outliers from an algorithmic perspective, lacking an in-depth investigation into their causes and roles. In this work, we provide a detailed analysis of the formation process, underlying causes, and functions of outliers in LLMs. We define and categorize three types of outliers—activation outliers, weight outliers, and attention outliers—and analyze their distributions across different dimensions, uncovering inherent connections between their occurrences and their ultimate influence on the attention mechanism. Based on these observations, we hypothesize and explore the mechanisms by which these outliers arise and function, demonstrating through theoretical derivations and experiments that they emerge due to the self-attention mechanism's softmax operation. These outliers act as implicit context-aware scaling factors within the attention mechanism. As these outliers stem from systematic influences, we term them systematic outliers. Our study not only enhances the understanding of Transformer-based LLMs but also shows that structurally eliminating outliers can accelerate convergence and improve model compression. The code will be released upon acceptance to support further research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a systemic analysis of outliers in transformer language models, which as extremely large values in weights and or activations. Through a set of experiments they show how different types of activations are connected to each other, and how they are all connected to attention scores in the end. In particular, the authors propose outlier activations are used to scale attention activations and allow for a 'zero' update when there is no need to update the residual stream. They verify this hypothesis by training transformer models with different transformer setups and show that including a specific scale parameter removes the existence of outliers from the model.

### Strengths
- Very well written. Presents a nice and easy to follow story of a complex topic. Good figures.
- Good experiments to analyze the situation and support their hypothesis well
- Provides a good explanation for a mysterious and sometimes troublesome behavior observed in transformer models.
- Proposes a (few) modified architectures that solve this problem

### Weaknesses
 - Notation is a little different from what I'm used to. I think it would be more clear to refer to MLP-layer, Attention layer and residual stream in Figure 4. In particular, down projection input is discussed early on in the paper without explaining what it is, would be useful to at least refer to Fig.4 when its first mentioned.
- Could use some more experimental details at least in the appendix to explain the experimental setups etc in more detail.
- After reading more related work, I have a concern related to the novelty of this approach, in particular the similarity with [1] and whether that is fairly represented in the current manuscript. In particular, I'm concerned with Section 5, where first reading made it seem like the approaches that fix this problem (d and e in Table 2) are original contributions of this paper, while previous work suggested approaches that don't work i.e. (b). However this is not the case and a working approach (d) was directly proposed by [1]. I think at minimum this need to be made more clear in the section, for example by adding citation to [1] on the row for (d) in Table 2. 

### Questions
Couldn't the model alternatively learn to do ~0 updates by outputting a value matrix V with all the values small? Do you have any hypothesis why current models instead learn to use attention with an outlier connected to a small vector in V instead of making all vectors in V small?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper systematically analyzed the weight / activation / attention outliers in Transformer-based LLMs and find that they are correlated and are related to the design of the self-attention mechanism. The Transformer is trained to have these outliers because the model needs to learn the implicit context-aware scaling factors. After adopting a variant of self-attention that incorporates an explicit context-aware scaling factor in GPT-2, these outliers will disappear. To solidify the finding, the author also trained a GPT-2-sized model with the sigmoid attention, and showed that it does not have the outlier problem.

### Strengths
The paper provided an empirical analysis of the outliers in LLMs's weights / activations and attention outputs. The author first analyzed the outliers in different LLM layers and found that they are highly correlated. This leads to three hypotheses about these outliers: 1) they act as fixed but important biases, 2) they act as context-aware biases, 3) they act as context-aware scaling factors to the attention mechanism. The author trained GPT-2 with different attention variants to verify these hypotheses. The experimental results suggest that the outliers should be acting as implicit context-aware scaling factors. The reasoning process of the paper is clear and convincing. The self-attention with explicit context-aware scaling factor can also stabilize LLM training.

### Weaknesses
The author claims that the work "deepens the theoretical understanding" of outliers in LLMs in the Conclusion section. However, there is no theory involved in the analysis and the finding is mostly empirical. On the other hand, the author only conducted experiments with GPT-2. Since the Llama architecture is not exactly the same as GPT-2, the author can also verify the finding with small-scale Llama model.

### Questions
Have you tried changing the self-attention in Llama to the "explicit context-aware scaling factor" variant? Will it also remove the outliers?

### Soundness
3

### Presentation
4

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
This paper presents an investigation into systematic outliers in Large Language Models (LLMs), categorizing them into three types: activation outliers, weight outliers, and attention outliers. The authors analyze their distribution patterns, lifecycle, and potential role in the attention mechanism. They propose that these outliers function as implicit context-aware scaling factors and suggest modifications to the attention mechanism to address them. The paper includes empirical analysis across several LLM architectures and proposes potential improvements for model convergence and compression.

### Strengths
1.	Addresses an important topic in LLM research with potential practical implications for model optimization
2.	Provides comprehensive visualization of outlier patterns across different model architectures
3.	Makes an attempt to connect different aspects of model behavior (outliers, attention mechanism, model performance)
4.	Includes analysis across multiple popular LLM architectures (LLaMA2, Mistral, Phi-2)
5.	The paper's exploration of outlier lifecycles offers an interesting perspective on how these patterns emerge and evolve

### Weaknesses
• Unclear Research Focus and Scattered Investigation:
The paper suffers from a lack of clear research direction and keeps shifting between multiple topics without thoroughly investigating any single aspect:
  - It starts by identifying three types of outliers (activation, weight, and attention outliers) but doesn't provide a rigorous mathematical definition of what constitutes an "outlier" in each case, specifically lacking a clear thresholding mechanism or statistical measure for their identification. The absence of a formal definition makes it difficult to reproduce the findings or compare them with other studies.
  - The investigation jumps from outlier identification to lifecycle analysis to attention mechanisms without establishing strong connections between these aspects. For instance, the link between the observed outlier lifecycles and their functional role in the attention mechanism remains unclear, making the progression feel disjointed.
  - Section 5's transition from outlier analysis to attention mechanism modification feels abrupt and inadequately motivated. The proposed modifications lack a strong theoretical basis and do not clearly address the specific issues identified in the outlier analysis.

• Empirical Weaknesses and Methodological Issues
  - The paper relies heavily on empirical observations without sufficient statistical rigor:

         # The identification of outliers appears to be based purely on visual inspection of heatmaps (Figures 1-3) without any quantitative thresholds or statistical measures. This subjective approach introduces bias and makes it difficult to validate the results. For example, the heatmaps could be interpreted differently by other researchers, leading to inconsistent conclusions.
         # The claim about "95% overlap" between activation and attention outliers (Table 1) lacks details about the methodology used to calculate this overlap. Without a clear definition of how overlap is measured (e.g., using intersection over union or other metrics), the claim is not verifiable.
         # The paper doesn't provide error bars or statistical significance tests for any of its quantitative claims. This lack of statistical validation makes it impossible to determine whether the observed effects are genuine or due to random chance.

• Previously Known Results Presented as Novel 
  - All of these papers are cited, yet several of the paper's "findings" have been previously established in the literature:

        # The presence of activation outliers and their impact on model compression was already documented by Dettmers et al. (2022) [1].
        # The "Attention Sink" phenomenon and its relationship to specific tokens has been thoroughly analyzed by Xiao et al. (2023b) [2].
        # The connection between outliers and layer sparsity was previously established by Yin et al. (2023) [3].

• The experimental validation of key claims is often insufficient:
  - The paper proposes five attention variants (Table 2) but doesn't provide comprehensive ablation studies. It is unclear which specific modifications contribute to the observed performance changes, and whether these changes are statistically significant.
  - The convergence improvements claimed in Figure 15 are shown for only 50 steps without baseline comparisons. This short training period is insufficient to demonstrate long-term convergence behavior, and the lack of a baseline makes it impossible to assess the true impact of the proposed modifications.
  - The proposed context-aware scaling mechanism is not thoroughly evaluated against existing solutions. The paper does not demonstrate that the proposed mechanism provides any advantage over existing techniques, such as adaptive scaling or other normalization methods.

• Unsupported Claims and Logical Gaps
  - Several key claims lack proper substantiation:

        # The paper asserts that systematic outliers serve as "implicit context-aware scaling factors" but doesn't provide a mathematical proof or rigorous demonstration. The claim is based on empirical observations, but lacks a theoretical framework to support it.
        # The connection between softmax attention and the emergence of outliers (Section 6) is speculative and lacks any formal analysis. The paper does not provide a mathematical derivation or simulation to demonstrate how softmax properties lead to outlier formation.
        # The claim about improved model compression is made without quantitative comparisons to existing compression techniques, and already well established in literature. The paper does not provide a quantitative comparison with state-of-the-art compression methods, making it difficult to assess the practical impact of the proposed approach.

• Limited Scope of Analysis
  - Despite claiming to provide a "systematic" analysis, the investigation of fine-tuned models is superficial, only looking at surface-level patterns. The paper does not explore the impact of fine-tuning on outlier behavior in sufficient depth, limiting the generalizability of its findings.

### Questions
Methodological Clarity:

1.	Given that outlier identification is central to your analysis, one would expect quantitative definitions of outliers? What specific statistical thresholds or metrics have been proposed by you for systematically identifying each type of outlier (activation, weight, attention)?
2.	Your analysis of the "lifecycle" of outliers suggests causal relationships between different types of outliers. How can you establish these relationships are truly causal rather than merely correlational? What controlled experiments validate these claims?

Theoretical Foundation:
Your hypothesis about softmax attention being the root cause:

•	Can you provide a mathematical proof linking softmax properties to outlier formation?
•	Have you considered alternative mechanisms beyond just sigmoid?
•	How does this hypothesis explain the layer-wise variation in outlier patterns?

Quantitative Memory Efficiency: 

What is the quantitative impact on memory consumption when using context-aware scaling compared to baseline models? Providing precise memory benchmarks would clarify its effectiveness for large-scale deployment.

Effect of Sequence Length: 

How does sequence length influence attention outliers? Do variations in sequence length amplify or suppress these outliers, and which sequence lengths are most prone to generating them?

After reviewing the revised paper and updates, I find that some of my questions have been partially addressed. However, the evaluations rely on relatively outdated LLMs, raising concerns about whether these results would hold true for current state-of-the-art LLMs. As a result, I remain unconvinced of the impact of this primarily empirical work in the context of today's rapidly evolving LLM landscape. Thus, I will maintain my score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an empirical study of activation, weight, and attention outliers in LLMs. The authors investigate their roles and functions, uncovering important findings that could potentially deepen the understanding of LLMs.

### Strengths
The paper investigates two important questions: where do outliers exist in LLMs, and what roles they play. The experiments are comprehensive and detailed.

### Weaknesses
1. While the experimental results are detailed, they are largely empirical, which raises concerns about the paper's technical novelty. For EMNLP, this empirical focus might be a better fit. However, for ICLR, a stronger mathematical analysis would be beneficial, such as a more in-depth exploration of the roles of these outliers. Specifically, the paper lacks a theoretical framework explaining why these outliers emerge and how they contribute to the model's functionality. A more rigorous analysis, perhaps involving information theory or dynamical systems, would significantly strengthen the paper's contribution.

2. The paper lacks comparison with existing methods. For example, the authors suggest that their findings could be used for pruning, but they should include comparisons with existing pruning methods for LLMs to substantiate this claim. The absence of such comparisons makes it difficult to assess the practical significance of the findings. It is unclear if the proposed approach offers any advantages over established techniques like magnitude-based pruning or more advanced methods that consider the sensitivity of different parameters.

3. What is the relationship of this work to Sun et al. [1]?. Is this study an extension from focusing on massive activations to also examining massive weights, activations, and attention? The paper needs to clearly articulate its novelty compared to existing work, particularly in relation to the specific contributions of Sun et al. It is not clear if the current work simply expands the scope of the previous study or offers fundamentally new insights.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work relates three different kinds of outliers: activation, weight, and attention outliers. The authors then show that these outliers implicitly scale attention coefficients, which are validated empirically. Finally, the paper proposes an attention-scale to eliminate outliers for downstream benefit.

### Strengths
1. Figure 15 is an intriguing result and a strong argument for smoothing out outliers using the proposed method. The potential for converging to a lower loss at a faster rate is certainly desirable. I would argue that this should be the central focus, when anyone asks about the practical value of understanding outliers in such detail.
2. Figures 1-3 are well illustrated. It's clear that there are outliers clustered in just single channels, which is odd to see and interesting to call out. It's also interesting that activation outliers occur at very specific points in the network, per Figure 4.
3. Sec 5.2 is interesting. I believe this would be strengthened if you highlighted where each attention variant was pulled from. (d) looks similar to the attention bias that StreamingLLM introduced to fix attention sinks (but I may be wrong here) -- if that's true, it would be beneficial to highlight that only your specific combination of variants successfully inhibits outliers.
4. The summary sections are helpful for understanding what we've "learned" so far at that point in the paper, and they help me contextualize the ablations and analysis. Thanks for including these.

### Weaknesses
1. In Sec 5, you've shown that data-dependent scaling factors completely remove outliers. However, how does this affect quality? That seems like an important question to answer. What if outliers are mitigated but quality now plummets? "Quality" here mean zero-shot accuracy, ppl, MMLU etc.
2. It's unclear what the takeaway for this paper is. For example, in sec 5, why do we want to remove outliers? Luckily, you've actually already pitched a possible angle on this question -- per strength #1, figure 15 shows that convergence may be significantly improved. I believe this is a very interesting idea and should be the focus of the paper. The plot only runs for 50 steps. What happens at step 75, 100, 200? 1000? Does this trend continue, and does the smoothed model converge to a lower loss? If so, that would be a phenomenal result, but that would take more than a rebuttal period to flesh out I believe -- especially if it becomes the "Table 1". (But I'm open-minded about being wrong, since you technically have the ability to upload a new copy of the paper)
3. I can't find a definition of "outlier". From my understanding, LLM.int8 has a strange definition of activation outliers for example -- where entire channels are considered "outlier or not". From the figures, I can see that outliers are clearly very disproportionately large values, but how do you determine if a token has or doesn't have an outlier? For example, for Figure 5b. 
4. In a similar vein to Weakness #3, where is "alignment" defined? I understand the rough idea that weight outlier feature dimension should match the activation outlier's (for example), but what if this dimension alignment occurs for token #1 and doesn't occur for token #2 -- does that mean the entire sequence is now misaligned? Why is the consistency percentage such an even number? Is this because you consider entire sequences to be aligned or misaligned, instead of individual tokens?

### Questions
- nit: Many of the figures could have been moved to the appendix, and the paper could have been shortened to fewer pages -- e.g., figs 2, 3, 8, 11. Unless they add to the story substantially, they just increase the distance between figure 1 and the rest of the story.
- nit: The figures could use captions to help guide the reader to focus on certain attributes of the figures - figures 5, 6, 7 for example. For what it's worth, the figure titles are very descriptive, so that's helpful.
- nit: One of the critiques of previous papers in L91 is that previous methods "focus on isolated instances or targeted solutions," but it seems like we could have ignored weight and activation outliers, then focused on just attention outliers for this paper.
- nit: Sec 6 reads like a rebuttal. Granted, this is just the last 1.5 pages -- and it includes the result I'm most excited about -- but it could be better integrated into the rest of the paper. And you probably don't want any reviewer thinking this is a resubmission.
- nit: There are a few figures that aren't mentioned in the text, such as Figures 2 and 3. And, since the captions are brief, I only have my own observations to make (e.g., a few large-magnitude values are clustered). But perhaps there are other observations you would like the reader to make, and I wouldn't know.
- nit: Per Figure 5b, does this mean activation outliers never occur in any other token, of the thousands of possible tokens that exist?

Summary: All in all, this is an interesting idea, but lack of practicality and clarity make it hard to recommend an accept. An application paper focuses on the former, and an understanding paper (which I believe this aims to be) focuses on the latter. However, your paper has an interesting insight: The outliers that everyone else observes are all related somehow AND smoothing these outliers can lead to better convergence. I find this last idea particularly exciting, but I think it would take further experimentation to truly make this the focus. Given the paper has many redundant figures that could be moved to the appendix, I believe there is enough room to add a rigorous set of experimental results for convergence studies. I'm also not sure how Sec 4 is related to the method (how do we use it?) or the analysis (why does this happen?), but the fact that it happens consistently across models is certainly thought-provoking. I do believe in this paper's core insight strongly -- I just don't think the current presentation is focused enough for me to have a clear, memorable takeaway. I look forward to the rebuttal though, and I'm certainly willing to bump up my score if you have an idea of how to address these issues + show a promising update to the paper.

### Soundness
4

### Presentation
2

### Contribution
2
