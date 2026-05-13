# Is Free Self-Alignment Possible?

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Aligning pretrained language models (LMs) is a complex and resource-intensive process, often requiring access to large amounts of ground-truth preference data and substantial compute. Are these costs necessary?
That is, \textit{it is possible to align using only inherent model knowledge and without additional training?} We tackle this challenge with $\SYSNAME$, a novel approach that uses (1) self-generated preference data and (2) representation editing to provide nearly cost-free alignment.
During inference, $\SYSNAME$ modifies LM representations to reduce undesirable and boost desirable components using subspaces identified via self-generated preference pairs. Our experiments reveal that this nearly cost-free procedure significantly narrows the gap between base pretrained and tuned models by an average of 31.6\%, observed across six datasets and three model architectures. Additionally, we explore the potential of using $\SYSNAME$ as a means of \emph{expediting} more expensive alignment procedures.  Our experiments show that $\SYSNAME$ improves DPO models tuned only using a small subset of ground-truth preference data. Lastly, we study the conditions under which improvement using $\SYSNAME$ is feasible, providing valuable insights into its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces AlignEZ, a method for aligning large language models (LMs) with human preferences without using additional training data or fine-tuning. The approach addresses the high costs associated with traditional alignment methods that require extensive human-annotated data and fine-tuning. AlignEZ leverages self-generated preference data by prompting the base model to produce examples of “helpful” and “harmful” responses, thereby creating synthetic data that approximates human preferences. During inference, AlignEZ performs representation editing, modifying model embeddings to accentuate desirable (helpful) and reduce undesirable (harmful) components. This enables alignment without training, relying instead on adjustments to the model’s representations in real time.

Empirically, AlignEZ narrows the performance gap between base and aligned models by 29.1% on average across multiple datasets and architectures, demonstrating that it can boost alignment quality in a cost-effective manner. In experiments, AlignEZ also expedites traditional alignment processes like Direct Preference Optimization (DPO), enhancing model performance even when only a small subset of ground-truth data is available. Additionally, AlignEZ integrates effectively with prompting techniques, yielding further improvements beyond what prompting alone can achieve.

### Strengths
1. By eliminating reliance on costly fine-tuning and human-annotated preference data, AlignEZ offers a more resource-efficient alternative to traditional alignment techniques, making it potentially scalable for larger or real-time applications.
2. AlignEZ presents a conceptually straightforward approach, leveraging self-generated preference data and representation editing to achieve alignment without the need for extensive fine-tuning or additional ground-truth annotations.
3.  Empirically, the approach demonstrates substantial performance gains over DPO baselines, showing that AlignEZ is effective even when traditional alignment data is limited. It also improves data efficiency by expediting existing RLHF methods, like DPO. 
4. Moreover, AlignEZ integrates well with prompting strategies, enhancing alignment performance beyond what prompting alone achieves and expanding its usability with other alignment techniques. Prompting method is another cheap way to align LLMs without much cost and it's good to see both methods can be combined strongly.

### Weaknesses
1. While AlignEZ combines self-generated preference data and representation editing effectively, both of these approaches are well-established methods. Techniques for generating synthetic preference data have been extensively studied in self-alignment literature, which limits the technical novelty of this work. To strengthen its contribution, the authors could further emphasize unique aspects of their integration of these techniques or explore additional novel dimensions, such as adaptive mechanisms for more refined, context-dependent alignment adjustments. Specifically, the method could benefit from a more detailed exploration of how the self-generated data is selected and weighted, as this is crucial for avoiding issues like confirmation bias or mode collapse, which are common in self-training scenarios.
2. The concept of "free" alignment in AlignEZ may be somewhat overstated, as both the self-generation of preference data and embedding modifications require non-negligible computational resources. While ALIGNEZ reduces reliance on human-labeled data, it does not entirely eliminate costs, especially when scaling to larger models. Clarifying these claims by discussing cost reductions relative to traditional methods, rather than "free" alignment, would provide a more balanced and realistic portrayal of AlignEZ's cost efficiency. The computational cost of generating synthetic data, even if less than human annotation, should be quantified and compared to other alignment methods, including prompting-based approaches.
3. Similarly, the title, “Is Free Self-Alignment Possible?” may prioritize entertainment value over clarity, providing limited insight into the paper’s actual contributions. A more precise framing, such as “Cost-Efficient Self-Alignment through Representation Editing and Self-Generated Data,” could better communicate the scope and implications of the study. The title should accurately reflect the core contributions and avoid potentially misleading claims about the method being "free."
4. The theoretical analysis presented in Section 3 is built on simplifying assumptions that may not fully capture the complexities of real-world model behavior. Specifically, the assumption that LLM space is orthonormal is oversimplified. Also, the conclusion is unclear enough to specify whether the singular vectors from AlignEZ are strong enough or whether the kNN smoothing is good enough, etc. The analysis needs to address the limitations of the orthonormality assumption and provide a more robust justification for the use of k-NN smoothing, perhaps by exploring its sensitivity to different values of k and the distribution of data points in the embedding space.
5. The empirical results are based on relatively small language models (7B and 8B parameters), which, given the rapid advancements in AI, are now considered less representative of state-of-the-art capabilities. Applying ALIGNEZ to significantly larger models (e.g., 100B+ parameters) would provide stronger evidence of its scalability and effectiveness in larger, more complex architectures. While it is challenging to access larger models due to their proprietary nature, exploring ways to adapt ALIGNEZ for environments where parameter access is limited, or testing it on larger open-source models, could strengthen its empirical validation. Additionally, the reliance on open-source models might be seen as a minor limitation, as this restricts ALIGNEZ’s applicability to cases where model weights are accessible, potentially narrowing its practical impact in real-world, production-level systems that often employ closed-source models.

### Questions
1. While the paper shows the compatibility of this method with the prompting method, I wonder about the head-to-head comparison of the proposed technique and prompting technique in improving the alignment performance of LLMs, since both are very cheap methods,
2. Any fun visualization or analyses on the "help" and "harm" vector space?
3. Any thoughts on the reward-guided test-time alignment techniques? This is related to the efficiency alignment techniques, although it's not closely related to the techniques in this paper per se.

### Soundness
3

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
4

### Summary
The paper introduces AlignEZ, a cost-efficient approach for aligning pretrained language models without the need for large-scale ground-truth preference data or extensive computational resources. Instead, AlignEZ utilizes self-generated preference data and representation editing to adjust model outputs during inference. By modifying model representations to suppress undesirable traits and enhance preferred ones using identified subspaces, AlignEZ significantly improves model alignment. Experimental results across five datasets and two architectures demonstrate a 29.1% average improvement, narrowing the gap between pretrained and fine-tuned models. Additionally, AlignEZ shows potential for expediting more expensive alignment methods by enhancing models trained with limited ground-truth preference data.

### Strengths
1. The paper is well-written and easy to follow.
2. The performance results presented, particularly in Table 1, demonstrate the effectiveness of AlignEZ. As an inference-time alignment technique, AlignEZ significantly improves the alignment recovery compared to other test-time alignment baselines.
3. The authors conduct additional experiments to confirm that their method is orthogonal to prompting techniques such as URIAL. This enhances the practicality and robustness of the proposed approach.

### Weaknesses
1. The comparison with the baselines appears somewhat unfair. While the baseline test-time alignment techniques utilize ground-truth preference signals, these signals are sourced from a different dataset (HH-RLHF), introducing a distribution shift compared to the data used in AlignEZ. To provide a more balanced comparison, I suggest evaluating AlignEZ using the same HH-RLHF data during inference.

2. Concerning practicality and efficiency, the authors do not provide details on the overhead induced by their method, particularly in terms of inference latency or memory utilization. It would be beneficial to compare these overheads against those of the baseline methods.

3. It remains unclear whether AlignEZ affects other critical aspects, such as model safety or propensity for hallucination. I recommend including a discussion or experiments that assess the potential impact of AlignEZ on these factors.

4. A highly viable and practical application of test-time alignment is personalization, rather than just general helpfulness (which is already addressed by the aligned versions of many models). Moreover, the dataset used in this paper is somewhat outdated. Providing experiments or insights focused on personalization could offer valuable contributions and make the paper more relevant.

### Questions
1. What would the impact be if only the “helpfulness enhancement” or solely the “harmfulness suppression” (as described in Section 2.3) were applied individually? Could you provide insights or experiments on this?

2. Could using k-nearest neighbor (kNN) search to retrieve responses as in-context examples when prompting the model further enhance its alignment abilities, instead of just using this in the sample-conditional estimation of helpful and harmful direction.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ALIGNEZ, a method that utilizes the inherent knowledge of pretrained language models to achieve low-cost alignment using only self-generated preference data. It employs a KNN approach to identify the top n-closest preference data points for a given query, followed by SVD to extract the most relevant representations related to helpful and harmful preferences. By adjusting these embeddings during inference, ALIGNEZ effectively narrows the performance gap between pretrained and aligned models, guiding them to generate more helpful responses without requiring additional training or human-annotated data.

### Strengths
1. Self-Generated Data: ALIGNEZ relies solely on self-generated data from the language model, eliminating the need for additional manual annotation, which is promising for scalability.

2. Performance Improvement: Experimental results show that this alignment approach effectively reduces the performance gap compared to traditional training-based methods, without requiring any additional training.

3. Data Efficiency: By using only 1% of preference data for DPO training, ALIGNEZ achieves results comparable to those obtained with 25% of preference data, demonstrating compatibility with existing preference alignment methods.

### Weaknesses
1. Unclear Methodology: The description of the method's details is vague, particularly regarding the origin of queries used for generating self-generated preference data. Additionally, it's unclear which dataset was used for the experiments shown in Figures 3 and 4, and whether the reported $\Delta\%$ represents an average score across multiple datasets or results from a single dataset.

2. Dependence on base LM: The base LM may generate incorrect preference data, and the paper does not clarify how it ensures that self-generated preference data accurately reflects the correct preference relationships. This lack of clarity could significantly impact the results. Furthermore, while the method shows some effectiveness on the base LM, its performance on instruction-tuned LMs remains unexplored, limiting its contribution. For example, in the experiment for Figure 3, the performance with and without ALIGNEZ when the DPO dataset is expanded to 100% is not assessed.

3. Generalizability Issues: ALIGNEZ uses a statistical method (kNN) to obtain feature vectors for embedding editing during inference, raising concerns about its generalizability. It may only be effective when the inference input data is strongly correlated with the statistical data, making it difficult to handle out-of-distribution (OOD) situations.

4. Narrow Focus on Helpfulness: A significant limitation of the paper is its narrow focus on helpfulness, which does not convincingly demonstrate the overall effectiveness of ALIGNEZ. This raises doubts about whether ALIGNEZ is universally applicable to other aspects, such as safety or more complex alignment scenarios that involve a mix of helpfulness and safety. More extensive testing would strengthen the paper's claims.

5. Dependency on LLM's Instruction-Following Ability: Since ALIGNEZ relies on self-generated data to identify subspaces in the LM's embedding spaces corresponding to helpful and harmful directions for alignment, it requires a high degree of instruction-following capability from the LLM. This suggests that the method is better suited for models that have undergone instruction fine-tuning or alignment. However, the experiments are primarily conducted on the base pretrained model, which may not adequately reflect the method's potential effectiveness in more refined contexts.

### Questions
1. In the claim, 'With this nearly cost-free procedure, we effectively narrow the performance gap between pretrained and aligned models by 29.1% across two model architectures and five datasets,' how was the 29.1% calculated?

2. Line 239 may be intended to refer to $z_{help}$ and $z_{harm}$.

3. In Figure 4 (right), what insights can be drawn from the statement 'The lowest cosine similarities are observed in the middle layers (layers 10 to 25)'?

4. In line 303, the term "DPOed" is used, which is not a formal expression. 

5. The main experiments lack detailed descriptions. It's not clear how to implement the method across different datasets.

### Soundness
2

### Presentation
2

### Contribution
2
