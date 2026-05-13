# Resolving Lexical Bias in Edit Scoping with Projector Editor Networks

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Weight-preserving large language model editing techniques rely heavily on scoping mechanisms that determine when to apply edits to the base model. These mechanisms typically use distance functions in the representation space. However, we demonstrate that distance-based scoping functions struggle with strong lexical biases, leading to issues such as applying edits to irrelevant prompts with overlapping words. This paper presents Projector Editor Networks for Model Editing (PENME), a principled approach that learns the optimal representation space for scoping using contrastive learning. Specifically, PENME forms a disentangled representation space that facilitates precise localization of edits by maintaining substantial distance between irrelevant prompts while preserving proximity among paraphrases. In our empirical study, we show PENME achieves state-of-the-art model editing results while being more computationally efficient during inference and adaptable across different architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper points out that knowledge editing methods based on scoping mechanisms are limited by lexical bias. It proposes using a projector network to decrease the distance between edits and paraphrases, and increase the distance between edits and neighbors to address this issue.

### Strengths
* The paper highlights the challenge of lexical bias in knowledge editing, providing valuable guidance for future research in this field.
* The paper proposes using a projector network to enhance retrieval within the codebook, effectively improving the generalization of edits and preventing misfires.

### Weaknesses
 * The authors didn't fully explain their method. In discussing the construction of key-value memory, they described how to create the keys and set the threshold but didn't explain how to obtain the corresponding values.
* The paper claims that PENME enables faster edit retrieval and simplifies edit removal or updates. However, it lacks supporting experimental evidence.
* The hyperparameter m in the loss function is crucial for the projection network's performance, yet the paper lacks ablation studies on this.
* Many methods were selected for performance comparison, but the authors did not explain why these specific methods were chosen.
* The images in the paper are disorganized and difficult to interpret. Combining multiple experiment results into single images reduces readability.
* The organization of the main text and appendix is unclear. For example, ablation experiments present results for different similarity thresholds for edit-to-edit pairings, but this hyperparameter isn't introduced in the main text, making it hard to understand.
* The paper doesn’t provide detailed explanations of the projector networks, such as their parameter dimensions.

### Questions
* Why choose L2 distance in the loss function instead of cosine similarity?
* Why choose cosine similarity for edit-to-edit pairings instead of L2 distance?
* What impact does the hyperparameter m have on the projection network's performance?
* What is the architecture of the projection network? Is it similar to a feed-forward layer in a transformer?
* How is the memory value in the key-value memory obtained?
* The paper proposes two data-driven thresholding schemes. Was Option 1 chosen over Option 2 based on experimental results?
* Why were these methods chosen as baselines in the paper? Is it because they achieved state-of-the-art results on certain metrics or share similarities with PENME?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses an important question in model editing: the tradeoff between generalization (e.g., paraphrase handling) and locality (e.g., avoiding unintended edits on irrelevant queries). To tackle this issue, the authors propose PENME, which consists of two components: (1) a projection network trained with a contrastive objective to separate paraphrased and irrelevant prompts in the representation space, and (2) a memory-based retrieval scheme that enhances editing precision by applying a similarity threshold as a scoping mechanism. Experiments on three models demonstrate the effectiveness of PENME compared to other baselines.

### Strengths
1. This paper addresses an important topic in model editing: the tradeoff between generalization and locality. Though the problem is already well-defined, the two proposed methods are simple yet effective to improve editing's effectiveness.
3. The experimental results are significant, showing improvements over several state-of-the-art editing methods.

### Weaknesses
1. I don’t have strong negative feedback on this paper, but additional analyses would be helpful. See the Questions section for more details.
2. The presentation could be improved; all figures are quite blurry and lack high quality.
3. The writing, especially in the experiments section, needs clarification. The baseline setup is hard to follow as the authors haven't provided an overview of all compared baselines (e.g., MELO). For instance, it’s unclear why Llama-2-7b wasn’t tested on MELO and no T5 for MEMIT.

### Questions
1. An ablation study on each proposed component would strengthen the analysis.
2. Could you provide a visualization of the representation space showing edits, paraphrases, and neighbors before and after editing? This would nicely complement the current analysis.
3. Fig6: LAMA->LLaMA
4. Adding more editing methods in the scaling experiment can help to confirm the robustness of PENME.

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
The paper introduces Projector Editor Networks for Model Editing (PENME), a novel approach to improving large language model editing techniques. PENME addresses the wrong when deal with incorrect edits on irrelevant prompts with similar words by using contrastive learning to create an optimized representation space. This space allows precise localization of edits by maintaining distance between irrelevant prompts while keeping paraphrases close. The empirical study demonstrates that PENME achieves great results in model editing.

### Strengths
* Propose the lexical bias in Model editing which is a new aspect to improve the performance of model editing.
* Propose a projection network that maps the model’s representation space to a new representation space where lexical dominance is minimized

### Weaknesses
 * This paper suggests that lexical bias refers to different editing subjects with the same relation, such as "The twin city of Pittsburgh is" and "The twin city of Portsmouth is." However, the prevalence of such cases in the CounterFact and ZsRE datasets is unclear. The paper does not provide a clear analysis of how often such cases occur, making it difficult to assess the significance of this bias.

* Figure 3 and Figure 7 illustrate the "Percentage of samples where edits are closer to unrelated neighbors," but this is insufficient to demonstrate lexical bias. At lower model layers, high similarity may result from underdeveloped sentence representations, while at higher layers, the reduced percentage indicates greater differentiation between sentences. The figures lack a comparative analysis showing the distribution of similarity scores across different layers and between related and unrelated prompts. The current presentation does not convincingly isolate lexical bias as the primary factor.

* The results in Table 1 show that GRACE is a strong baseline. PENME, which extends GRACE by using a projection network to map data representations, needs to clearly highlight the differences between PENME and GRACE. The paper does not provide a detailed ablation study to isolate the impact of the projection network. It is unclear how much of the performance gain is due to the projection network versus other factors.

* PENME focuses on addressing lexical bias, so it should perform well on Loc and Para. However, in Table 1, only Para shows improvement, which is insufficient to fully support the paper's contributions. The lack of improvement in Loc, despite the focus on lexical bias, raises questions about the effectiveness of the proposed approach in achieving its stated goals. The paper needs to provide a more detailed analysis of why the locality metric does not improve.

### Questions
* It is better to give more example to shown what is  lexical bias and lexical overlap in the paper.
* Some results in Table 1 is not clear enough (close to 0.0), such as why GRACE on zsRE get the 0.00 in Loc on Llama2-7b?
* In Figure 6, it is better to add the resutls on GRACE.

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
The paper proposes to address lexical bias in continual model editing (i.e., token similarity affecting edit decisions). The framework is similar to existing clustering-based setups (e.g., GRACE [1]). This seems to be achieved by explicitly training a projection network and discouraging exploiting lexical correlations. The paper shows improved performance on CounterFact and zsRE. 

[1] Aging with GRACE: Lifelong Model Editing with Discrete Key-Value Adaptors (Hartvigsen et al., 2023)

### Strengths
The paper highlights the problem of lexical bias in clustering-based editing approaches, which can raise awareness of this particular issue.

### Weaknesses
It is difficult to tell exactly what parts of the paper are novel contributions. I think the main difference is that in GRACE the cookbook representations are manually maintained whereas here they're learned. The related work section needs to tell the reader why this work is different from the previous works, not just describing them.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2
