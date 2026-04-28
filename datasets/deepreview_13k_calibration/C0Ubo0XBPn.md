# Hierarchical Information Flow for Generalized Efficient Image Restoration

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
While vision transformers show promise in numerous image restoration (IR) tasks, the challenge remains in efficiently generalizing and scaling up a model for multiple IR tasks.
To strike a balance between efficiency and model capacity for a generalized transformer-based IR method, we propose a \textbf{h}ierarchical \textbf{i}nformation flow mechanism for \textbf{i}mage \textbf{r}estoration, dubbed \textbf{Hi-IR}, which progressively \revise{propagates information} among pixels in a bottom-up manner. 
Hi-IR constructs a hierarchical information tree representing the degraded image across three levels. 
Each level encapsulates different types of information, with higher levels encompassing broader objects and concepts and lower levels focusing on local details. 
Moreover, the hierarchical tree architecture removes long-range self-attention, improves the computational efficiency and memory utilization, thus preparing it for effective model scaling.
Based on that, we explore model scaling to improve our method's capabilities, which is expected to positively impact IR in large-scale training settings. 
Extensive experimental results show that Hi-IR achieves state-of-the-art performance in seven common image restoration tasks, 
affirming its effectiveness and generalizability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Hi-IR, a hierarchical information flow mechanism structured as a tree for image restoration. In Hi-IR, information moves progressively from local areas, aggregates at multiple intermediate levels, and then spreads across the entire sequence. By using this hierarchical tree design, Hi-IR eliminates long-range self-attention, enhancing computational efficiency and memory usage. Extensive experiments across seven image restoration tasks demonstrate the effectiveness and generalizability of Hi-IR.

### Strengths
- The motivation for this paper is twofold: (1) information flow plays a pivotal role in decoding low-level features, and (2) it is not always necessary to implement information flow through fully connected graphs. Proposing hierarchical information flow via tree-structured attention is a reasonable approach to balancing complexity and the efficiency of global information propagation.
- The paper proposes a model scaling-up solution, such as replacing heavyweight $3 \times 3$ convolutions with lightweight operations. The authors reasonably justify why this approach is effective in Section 4 and Appendix B.1.

### Weaknesses
 - The authors state that the simple permutation operation facilitates the distribution of $l_1$ information nodes across all windows (L238-239); however, there is no specific explanation of how the permutation is applied. Could the authors answer to the questions below?
   1. Specify exactly which components the permutation is applied to
   2. Clarify if the permutation is random or deterministic  
   3. Provide an ablation study isolating the impact of the permutation compared to the tree structure

   This would provide valuable insight into how the permutation contributes to the model's performance. 
- The authors mention that the actual implementation of the tree structure, such as the depth of the tree and the number of child nodes, can be configured to ensure computational efficiency (L199-201). However, no accompanying ablation study has been conducted on these parameters. The authors are required to do below: 
   1. Conduct experiments varying the tree depth and number of child nodes
   2. Show how these choices impact both performance and computational efficiency
   3. Discuss how different configurations balance local and global information modeling  

   This would provide concrete evidence for the effectiveness of the hierarchical design.
- Additional feedbacks:  
   - It is essential to provide specific details for the clarity. For example:
     1. Add SR task specification to Table 6 caption
     2. Clarify in main text whether Hi-IR-B or Hi-IR-L is being referred to (Section 5)
     3. Add reference to Table 7 when discussing efficiency analysis (L409-L412)
     4. Spell out "Dn" as "denoising (Dn)" on first use (Table 7)
   - There is a typographical error in the sentence (L257) where the first letter should be capitalized. "for each" should be changed to "For each.”
   - There is a sentence fragment that lacks a main clause (L375-L376).
   - Can authors show the GT in Figure 5?
   - The proposed Hi-IR does not outperform all methods in every instance; therefore, the expression "the proposed Hi-IR outperforms all other comparison methods under both settings" (L474-L475) should be softened.
   - There appear to be discrepancies between the experimental results in the table and the results described in the text in Section 5.2. Could the authors verify this?

### Questions
- The reviewer has two questions related to model scaling-up. First, could the authors specify which part of the proposed Hi-IR structure involves replacing heavyweight $3 \times 3$ convolutions with lightweight operations? Second, could the authors explain why applying warming-up and using dot product instead of cosine similarity attention leads to improved scaling-up? Simply showing improved performance with a larger model is insufficient to demonstrate they contribute effective scaling-up convincingly.
- In the paragraph discussing the effect of L1 and L2 information flow (L374-L376), could the authors explain why v3 is superior among v1, v2, and v3? Alternatively, could the authors explain the rationale behind the experimental design for v1 to v3? Simply showcasing the best one among the three designs does not provide informative insight for the reader.

### Soundness
3

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
5

### Summary
This paper proposes a hierarchical information flow principle for general image restoration tasks, which aims to address three significant problems in image restoration including a generalized and efficient IR model, model scaling, and the performance of a single model on different IR tasks. The paper comprehensively analyzes different configurations of model scaling and provides sufficient evaluation results on different image restoration tasks.

### Strengths
1. The paper clearly describes the motivations of the proposed method, and the structure of the paper is well-organized, and easy to follow.

2. The paper provides comprehensive experiments to evaluate the performance of different model scaling configurations, which are convincing.

3. The paper demonstrates that the proposed hierarchical information flow design is effective for performance improvement in different IR tasks.

### Weaknesses
1. The proposed method appears to have limited novelty. First, it adopts the U-Net structure, whose efficiency has already been evaluated in works like Uformer [1] and Restormer [2]. Second, the hierarchical information flow design seems to be another variation of existing efficient self-attention mechanisms. Specifically, the paper does not adequately differentiate its approach from other hierarchical attention mechanisms that also progressively aggregate information across different scales. The core idea of using a tree-based structure for self-attention, while potentially efficient, needs more justification regarding its advantages over existing methods.

2. The claim that generalization and efficiency are inherently a trade-off may not be entirely accurate. Why would a model with strong generalization capabilities be considered inefficient? Is there any external reference or evidence to support this claim? It is not clear why a model capable of handling diverse image restoration tasks would necessarily be less efficient than a specialized model. The paper needs to clarify the specific mechanisms that cause this trade-off, rather than stating it as an inherent property.

3. The paper does not clearly explain the details of the tree-based self-attention mechanism. How is the tree structure specifically applied within the self-attention mechanism? For instance, how are the nodes in the tree defined, and what is the specific operation performed at each node to aggregate information? Please provide more details or examples to clarify this. The paper should also explain how the permutation operation is integrated with the tree structure to facilitate information flow.

4. The paper claims that the proposed method can handle images with various degradations, but the experiments mainly show its effectiveness on individual IR tasks. Since real-world images often have multiple types of degradations, how does the proposed method perform when applied to such images? The paper should include experiments that evaluate the method's performance on images with combined degradations, such as noise and blur, or compression artifacts and rain streaks, to demonstrate its practical applicability.

### Questions
1. It is better to clarify what distinguishes your approach from these prior works.

2. Why would a model with strong generalization capabilities be considered inefficient? Is there any external reference or evidence to support this claim?

3.  How is the tree structure specifically applied within the self-attention mechanism? Please provide more details or examples to clarify this.

4. How does the proposed method perform when applied to real-world images for image super-resolution and image denoising? More experiment results should be included.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an efficient image restoration (IR) method called Hi-IR. Specifically, it introduces a hierarchical information flow that efficiently aggregates global context for each pixel. The authors also scale up the network and offer insights into training larger models. Extensive experiments across seven tasks validate the effectiveness and generalization capability of Hi-IR.

### Strengths
1. The experimental results on seven IR tasks validate the strong task generalization ability of the proposed method. The ablation studies also provide evidence of the effectiveness of individual modules.

2. The exploration of scaling IR models may provide practical insights for future research. 

3. The writing is clear and easy to follow.

### Weaknesses
Major:
1. The details of the permutation operation in Section 3.2 are not fully explained. Various types of permutations could be considered, such as random and circular permutations. I believe this operation is the main technical difference from the window-shift operation used in SwinIR [1]. Additional information on the permutation approach would enhance clarity. Specifically, it is unclear how the permutation is applied to the feature map and whether it is consistent across different layers or if it varies. The lack of a clear mathematical definition makes it difficult to assess the impact of this operation on the overall performance.

2.From my perspective, the core concept: hierarchical information flow (HIF for short) is essentially a window attention [1] without shifting (L1 information) and a new cross-window interaction operation (L2 information, i.e. permute then MSA). Therefore, the technical novelty is limited. The author may give more discussion on the other realizations of HIF. It is not clear why the specific permutation and MSA combination is superior to other possible cross-window interaction methods. A more detailed justification of the design choices is needed.

3.I believe a complexity analysis of the proposed HIF is beneficial to show the efficiency advantage of Hi-IR. On the other hand, it will provide more insights on how to choose better realizations of HIF (Line 078). The analysis should include both time and space complexity, and should also consider the impact of different permutation strategies on the overall complexity. Furthermore, the analysis should compare the complexity of the proposed method with other existing methods, such as global attention and window attention.

Minor:
1. In the second paragraph of Related Work, the authors introduce several attention mechanisms for IR (Line 131-133), whereas the corresponding reference is missing.  

2. The spacing between some captions and corresponding figures/tables (e.g. Figure 5, Table 15) is not well set.

3. Some typos (e.g. Line 016 remove propagation, Line 244 change Fig.3(c) to Fig.3(b)).

### Questions
1. I’m curious about the model's performance when scaled to a larger size (e.g., ~100M parameters). Is the proposed scaling method effective for models of this size?

2. Figure 2 is somewhat unclear. Could you clarify what the different colors represent?

### Soundness
2

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
5

### Summary
This paper proposes a hierarchical information tree structure to represent degraded images across three levels, aiming to balance efficiency and model capacity. The hierarchical tree architecture also supports effective model scaling. Extensive experiments are conducted to validate the approach.

### Strengths
1. The paper is well-motivated and easy to read.
2. This paper studies the model scaling problem in image restoration, which is valuable. 
3. Extensive experiments have been conducted.

### Weaknesses
Although the paper presents a compelling narrative, the challenge lies in balancing the scope and complexity of window attention while improving global information propagation efficiency, a topic that has been widely studied in recent years [1]. The proposed solution—window self-attention, permutation, and window self-attention—follows a similar approach as in [2]. These methods are missed and are not discussed. Please explicitly compare the hierarchical information flow mechanism with the random shuffle and spatial shuffle approaches in [1] and [2],and highlight key differences or advantages. Additionally, the paper appears somewhat rushed, with several mistakes. For example, in line 244, "Fig.3(a)" not "Fig.3(c)", and in line 218, "Convplutional" is misspelled.

### Questions
Why are the experiments in Tables 3, 4, 5, 6, and 7 conducted on different datasets?
Why are 2× and 3× scales used in Table 3, while 2× and 4× scales are used in Table 5?
Please provide a brief explanation in the paper for why different datasets and scale factors were chosen for each set of experiments, and how this impacts the interpretation of the results. This would help improve the paper's clarity and consistency.

### Soundness
2

### Presentation
2

### Contribution
2
