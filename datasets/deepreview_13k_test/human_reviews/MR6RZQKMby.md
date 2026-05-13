# Exploring Model Kinship for Merging Large Language Models

- Decision: Reject
- Scores: 3, 8, 6, 6

## Abstract
Model merging has become one of the key technologies for enhancing the capabilities and efficiency of Large Language Models (LLMs). However, our understanding of the expected performance gains and principles when merging any two models remains limited. In this work, we introduce \textit{model kinship}, the degree of similarity or relatedness between LLMs, analogous to \textbf{biological evolution}. With comprehensive empirical analysis, we find that there is a certain relationship between model kinship and the performance gains after model merging, which can help guide our selection of candidate models. Inspired by this, we propose a new model merging strategy: Top-$k$ Greedy Merging with Model Kinship, which can yield better performance on benchmark datasets.}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces the concept of model kinship, drawing an analogy to genetic hybridization in biology, with the aim of providing guidance for effective performance improvements in the field of model merging. The authors first empirically validate the relationship between kinship and performance gains, demonstrating their consistency. Building on the concept of kinship, they propose a Top-k Greedy Merging method that shows some performance enhancements compared to baseline approaches.

### Strengths
1. The research area is significant, and the introduction of the kinship metric, drawing an analogy to biological evolution, presents a human-like perspective that adds depth to the discussion of model merging.

2. The paper effectively establishes a connection between kinship and performance gains, providing empirical evidence that supports the proposed approach.

### Weaknesses
1. The definition of the problem is unclear, and the paper lacks a thorough discussion of specific scientific issues within the model merging field. The research motivation is insufficient, leading to a lack of logical clarity in the arguments presented.

2. While introducing human-like concepts or analogies from other fields can be a valuable approach to problem-solving, the kinship metric designed in this paper lacks a reasonable formulation and effective validation, which undermines its applicability.

3. The logical coherence and rigor of the writing require significant improvement to enhance the overall quality of the paper.

4. The conclusions drawn in the paper lack persuasive power due to the absence of quantitative experimental analysis. The methodology and experimental design appear relatively crude, which detracts from the credibility of the findings.

### Questions
As mentioned in the above weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes model kinship to evaluate the degree of similarity between LLMs. Then the authors did experiments to validate that model kinship moderately correlates with merge gain, and found that the performance improvement during model merging can be divided into learning stage and saturation stage. Finally, the paper proposes a practical use case to apply model kinship into top-k greedy merging to improve the performance of model evolution.

### Strengths
This paper targets at solving an important task. Also, this paper is very complete and well-written, from introducing the concept of model kinship, to empirically verify its value, and finally provide a practical scenario to apply model kinship to improve the model merging performance. I feel this is a complete work.

### Weaknesses
1. The bold fonts in this paper emphasize the relationship between model merging and biological evolution. Actually, I don't quite get their correlation. Biological evolution is based on nature selection while in this paper, model merging is done based on model similarity. Can the authors further elaborate on this?

2. Since all the experiments in this paper are only verified on one model set and one task set, there is no guarantee that the proposed pipeline can be generalized to other real-world scenarios.

### Questions
Please see above weakness.

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
2

### Summary
1. The paper explores the concept of "model kinship," which measures the similarity or relatedness between large language models (LLMs), drawing a parallel to biological evolution. Through empirical analysis, the authors demonstrate that this kinship can predict the performance gains when merging models, offering a basis for selecting suitable candidates for merging.

2. Building on this, they propose a strategy called Top-k Greedy Merging with Model Kinship, which improves performance on benchmark datasets. The study shows that using model kinship not only helps avoid local optima during model evolution but also serves as an early stopping criterion, enhancing efficiency. The authors suggest that their findings provide valuable insights for future LLM merging and evolution.

### Strengths
1. The paper introduces a novel exploration of the kinship between LLMs, using a heuristic approach inspired by biological evolution to guide the selection of models for merging. The overall idea is interesting.

2. The narrative of the paper is well-structured, and the authors validate their experiments using Mistral as the primary architecture.

### Weaknesses
1.  The experimental section lacks clarity. It is recommended that the authors add a dedicated subsection analyzing the datasets used and explaining why these specific datasets (e.g., general-purpose or domain-specific test data) were chosen for performance evaluation.

2. In the appendix (Figure 8), the authors present performance analysis based on various merging experiments using the Mistral architecture. However, it is unclear whether the results are applicable to other architectures like LLaMA, which suggests the idea may have some limitations. Although the authors mention in the limitations section that the performance on other architectures remains unknown, I strongly recommend testing on LLaMA or other types of LLM architectures to make the argument more robust and solid.

3. In Algorithm 1, the authors use Greedy Merging with Model Kinship; it is suggested to include an ablation study to demonstrate that the greedy algorithm is indeed the optimal choice.

### Questions
1. Please respond to the weaknesses mentioned in my review. I will adjust the score accordingly based on your response.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a notion of model kinship, which attempts to measure the relatedness of two language models. The paper also presents an algorithm that leverages the degree of model kinship to inform model merging strategies. In particular, the paper suggests that merging highly performant models with low kinship to a target model outperforms greedily merging with the top performing model when iteratively merging models. The results in the paper suggest that a model kinship aware strategy for model merging leads to superior benchmark results over model kinship unaware strategies.

### Strengths
The paper posits and provides evidence for the importance of kinship aware strategies when performing iterative model merging. This is a highly active and impactful area of research, and the paper presents empirical results with sufficient theoretical justification that they should be noted by the broader research community.

### Weaknesses
The paper lacks experimental breadth, and in some cases, seems to have critical typos. The paper would benefit from expanded experiments, particularly with additional merge lineage studies and with simulations on base models beyond Mistral 7b.

### Questions
086-087 should have a comma after improvements

table 1 and the significance of the p values for absolute gain seem to indicate that the variability of the merge gain is inversely related to the degree of model kinship. it may be worth remarking on this around line 233. 

297-299 make references to a “notable correlation” between model kinship and average task performance in figure 4, but no formal correlation analysis is presented.

311 makes reference to 3 learning stages, but line 086 makes reference to only two. this complicates the narrative

345 comma after convergence should be a period.

algorithm 1 has what seems to be some typos:

- should line 2 have M_k, not M_n, as the last element in the set?

- should line 3 replace “top m” with “top k”?

- should line 7 replace “select k pairs” with “select k models?”

- should line 9 be “identify the model M_f \in S with the lowest kinship…”? the discussion on lines 414-416 seems to indicate so.

- line 11 should expand on what “model-gen-id” is

line 429 seems to have an unlinked figure reference (perhaps to figure 6?)

### Soundness
3

### Presentation
3

### Contribution
3
