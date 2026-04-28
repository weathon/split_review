# Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 5, 5, 5, 5

## Abstract
\vspace{-5pt}
Knowledge Editing (KE) algorithms alter models' weights to perform targeted updates to incorrect, outdated, or otherwise unwanted factual associations.
To better identify the possibilities and limitations of these approaches, recent work has shown that applying KE can adversely affect models' factual recall accuracy and diminish their general reasoning abilities.
While these studies give broad insights into the potential harms of KE algorithms, e.g., via performance evaluations on benchmarks, we argue little is understood as to \textit{why} such destructive failures occur. 
Is it possible KE methods distort representations of concepts beyond the targeted fact, hence hampering abilities at broad? If so, what is the extent of this distortion?
Motivated by such questions, we define a novel synthetic task wherein a Transformer is trained from scratch to internalize a ``structured'' knowledge graph.
The structure enforces relationships between entities of the graph, such that editing a factual association has ``trickling effects'' on other entities in the graph (e.g., altering \texttt{X}'s parent is \texttt{Y} to \texttt{Z} affects who \texttt{X}'s siblings' parent is). 
Through evaluations of edited models and analysis of extracted representations, we show that KE inadvertently affects representations of entities beyond the targeted one, distorting relevant structures that allow a model to infer unseen knowledge about an entity.
We call this phenomenon \textit{representation shattering} and demonstrate that it results in degradation of factual recall and reasoning performance more broadly.
To corroborate our findings in a more naturalistic setup, we perform preliminary experiments with pretrained GPT-2-XL and Mamba models, reproducing the representation shattering effect therein as well.
Overall, our work yields a precise mechanistic hypothesis to explain why KE has adverse effects on model abilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the Representation Shattering Hypothesis, which posits that Knowledge Editing (KE) methods distort a model's latent representations, potentially to the point of losing the learned global graph structure—a phenomenon they call "representation shattering." The authors hypothesize that this mechanism underlies KE's negative impact on models' factual and reasoning abilities.

To test this hypothesis, they first create a toy knowledge graph to pre-train a language model on. Then, using a popular KE method called ROME, they edit facts within this graph, demonstrating that the extent of representation distortion correlates with how significantly an edit disrupts the graph's structure.

The authors further validate their hypothesis with a real language model, GPT2, by using ROME to corrupt the order of the months of the year. They show that this corruption distorts the ring structure of the month representations, with greater distortions occurring for larger edit distances.

### Strengths
- **Insight into Adverse Effects of KE:** With knowledge editing (KE) methods gaining popularity, this paper provides valuable insights into why KE can lead to adverse effects, offering a deeper understanding of its impact on model representations.

- **Clarity and Accessibility:** The paper is well-written and accessible, making complex concepts easier to understand for a broad audience.

- **Novel Toy Knowledge Graphs:** The authors introduce innovative toy knowledge graph (KG) tasks to explore KE and the phenomenon of representation shattering, providing a structured and interpretable framework for analyzing KE effects.

### Weaknesses
### Weaknesses

- **Limited Scope of Experimentation:**
  - The authors primarily experiment on knowledge graphs (KGs) with a ring-like structure, which is a somewhat artificial setup. Even the experiment with a real KG is restricted to a small subset with a similar ring configuration, limiting the generalizability of the findings. The use of a ring structure, while illustrative, does not capture the complexity of real-world knowledge graphs, which often exhibit hierarchical or more intricate relational structures. This narrow focus makes it difficult to ascertain whether the observed 'representation shattering' is a general phenomenon or an artifact of the specific graph topology used. Furthermore, the limited size of the graphs used in the experiments raises concerns about scalability and whether the findings would hold for larger, more complex knowledge bases.
  - Only one knowledge editing (KE) technique, ROME, is tested, leaving it unclear how the findings might extend to other KE methods. The lack of diversity in the editing techniques explored is a significant limitation. Different KE methods may operate on different principles and thus may not all exhibit the same degree of representation distortion. For example, methods that rely on gradient-based updates might behave differently than those that directly manipulate the model's parameters. Without testing a wider range of methods, the conclusions drawn about representation shattering remain specific to the ROME method and may not be broadly applicable.

- **Reliance on Visual Inspection of Representation Shattering:**
  - The approach seems heavily dependent on visually inspecting the breakdown of representations, which becomes infeasible for more complex, unvisualizable data. Although the authors propose using the Frobenius norm as a quantitative measure of shattering, it is only applied in one experiment. The visual inspection of representation changes, while intuitive for simple cases, is inherently subjective and lacks the rigor required for scientific validation. Relying on visual inspection makes it difficult to compare the degree of shattering across different experiments or models. Furthermore, the lack of a consistent quantitative metric makes it challenging to generalize the findings to higher-dimensional representations where visualization is not possible. The sporadic use of the Frobenius norm, while a step in the right direction, needs to be consistently applied and justified as a reliable measure of representation shattering.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The key idea of the paper is that knowledge editing (KE) alters the geometry of transformer models' representations, making them inconsistent or "shattered." The authors introduce the concept of "representation shattering" to explain why KE results in degradation of the model's performance. This perspective of geometric shattering is both insightful and novel, providing a deeper understanding of how targeted edits can inadvertently disrupt broader model behavior. The study is conducted using synthetic knowledge graphs (KGs), which allows the authors to identify specific geometric changes in transformer representations.

### Strengths
1. **Novelty**: This paper is the first to delve deeply into transformers' representations, providing a mechanistic understanding of why the detrimental impacts of KE occur. In contrast, previous work mainly treats transformers and LLMs as black boxes, focusing on observing the degradation of models' overall performance in targeted tasks.
2. **Unique Approach and Insightful Perspective**: The authors tackle the problem from the perspective of studying representation geometry, which offers a unique and insightful angle into how KE affects model consistency.
3. **Preliminary Results on LLM**: The authors extend their findings to a pretrained large model, GPT-2-XL, showing that the representation shattering phenomenon also applies to LLMs, not just to transformers trained on synthetic data.

### Weaknesses
Although the perspective and hypothesis of this paper are novel and insightful, I have concerns regarding the limitations of the experimental setup, specifically the reliance on cyclic structure in the synthetic KGs and the focus on only one KE method.

1.  **Why Cyclic Graphs?** The key assumption of this study is that transformers can learn a cyclic geometric representation when the training KGs have cyclic relation subgraphs. This assumption on its own makes sense. However, to my knowledge, real-world KGs often do not have relation subgraphs that conform to cyclic orders. For example, take the advisor relation that is used as the running example in the paper. It is unlikely that "Alice is the advisor of Bob", "Bob is the advisor of Charlie", and "Charlie is the advisor of Alice." In reality, most KG relations seem to form trees instead of cycles. This makes the study somewhat disconnected from real-world scenarios as cyclic relations are uncommon. Why not investigate the geometry of transformer representations in real-world KGs (or a semi-synthetic KG that more closely mimics the structure of real-world KGs) when the relation subgraphs are trees, and examine how KEs affect such geometry?
2.  **Knowledge Graph Construction**: The construction of the knowledge graphs, particularly the use of cycles, is not very intuitive and is challenging to understand. This is compounded by conflicting information in Section 3.2 (e.g., Line 202 states that the KG is defined to have 3 relations, but Line 205 later refers to 24 relations) and an explanation that omits critical details. Specifically, it is unclear what the exact cyclic orders are for the edit, retain, and test relations, and whether these relations are organized in such a way that each of the three groups has distinct orders. Additionally, Figure 3, intended to provide more intuition and details, is difficult to interpret due to unclear labeling, such as the meaning of different arrow colors and which edges were edited. Clarifying why the authors chose this specific construction, particularly the necessity of the use of different cyclic orders, and providing more transparent explanations of the data construction would greatly improve the reader's ability to understand the motivation behind the experimental setup.
3.  **Single KE Method (ROME)**: The paper only studies one knowledge editing method, ROME. The findings would be significantly strengthened if multiple KE methods were analyzed to determine whether the representation shattering phenomenon is a general property of transformer models occurring on a more fundamental representation level, independent of the KE method used. For instance, the paper shows that shattering occurs even for corrective edits, which is surprising because a perfect corrective edit should ideally refine the model's representation geometry. It is thus crucial to investigate whether this surprising phenomenon is specific to ROME or is a broader theme across different KE methods.
4.  **Lack of Mitigation Strategies**: While the paper does an excellent job of identifying the issue of representation shattering, it lacks discussion on potential ways to mitigate this problem. Including some hypotheses or suggestions for future work would provide direction for researchers interested in addressing this issue.

In addition, some other comments on readability and presentation:

5.  **Figures**: The Figure 1 is somewhat confusing, particularly in panel (b). It is unclear how the ring structure is represented in the visualization, and what the labels "182" and "608" refer to. Additionally, Figure 1 is not mentioned in the introduction, which makes it difficult to understand its relevance early on. It would help if the illustration was used to convey the high-level intuition of the findings. Similarly for Figure 3, mentioned in W2.
6.  **Undefined Terms**: The abbreviation "DGP" (Figure 1 caption, line 67) is undefined. I assume it stands for "Data Generating Process"—clarifying this would improve readability.
7.  **Entity and Relation Naming**: The naming conventions for entities and relations are unclear. For instance, on line 235, it is not immediately evident that "1," "3," etc., are entities, and that "I_C4," "III_A2," etc., are relations. In addition, there are clues in Figure 3 that the number of "I"'s stand for the different cyclic order, but this is not mentioned and explained in the main text. An explanation of the naming convention and its significance (e.g., whether the number of "I"s corresponds to hops in the KG) would be helpful.
8.  **Typo**: On line 291, the phrase "it changes fact $(x_i l r, x_j)$" should probably be "it changes fact $(x_i, r, x_j)$"
9.  **Unclear Sentence**: On line 366, the caption of Figure 5 reads: "We plot the mean drop in accuracy against the in the Frobenius norm of the difference in..." This sentence does not make sense as written and needs to be revised.

### Questions
1. **Possibility of Studying Geometry on Real-World KGs**: As previously raised in W1, would it be feasible to apply the same methodology to real-world KGs to examine how the representation geometry shatters under KEs? Would the lack of cyclic orders make this significantly more challenging? Additionally, could the Isomap visualization technique still be used effectively in this scenario to visualize a tree-like structure rather than rings?
2. **Training Setup Clarification**: Are all edit, retain, and test relations used during the pre-training of the transformer, and the test relations are only held out specifically for the KE process but they are all observed by the transformer during pre-training? If so, a clarification near line 213 would be helpful.
3. **Logical Inference Task**: For the logical inference task, could you elaborate on how the "hold out" process works? For example, if the inverse relation (say "advisee") is held out and unobserved during training, how can the model know that the held-out relation token "advisee" is the inverse of the observed relation "advisor"?

### Soundness
2

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper provides a way to investigate the representation scattering hypothesis during knowledge editing. It proposed a test for using synthetic entities to probe if the representation scattering happens.

### Strengths
* A new hypothesis, representation scattering,  is proposed
* Experiments are done to test the hypothesis proposed,

### Weaknesses
 * Only the GPT model is studied, which makes the scope limited in the model architecture.
* The result seems hard to reproduce.

### Questions
* Is the assumption still valid on different model architectures, including encoder-decoder models like T5, and Mamba?
* Is the assumption still valid on larger LLM models like Lamma, Gemma, Phi 3.5 etc?

### Soundness
2

### Presentation
2

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
The paper constructs a synthetic dataset with cyclic knowledge graphs and investigates the influences of knowledge editing on the synthetic datasets. The results show that KE inadvertently affects representations of entities beyond the targeted one, distorting relevant structures that allow a model to infer unseen knowledge about an entity.

### Strengths
1, The synthetic dataset is well-designed in a way that all the relations are related in a clear semantic meaning. And Figure 3 clealy demonstrates the structure of the synthetic dataset.

2, The visualization is really good. It clearly shows the representation shattering after the knowledge editing (Figure 4, 5, 6 and 8).

### Weaknesses
1, The expected answers (or the ground truth answers) after knowledge editing is not clearly stated in the paper. For example in Figure 3 Ring I, after the editing of $1.I\_C2 = 3$, is $1.I\_C2 = 2$ still true (so that entity 1 now have 2 entities for relation I_C2) or does this edge simply disappear? Which one of the following is considered the ground truth for evaluation after the editing: $1.I\_C3 = 4$ or $1.I\_C4 = 4$? In the proposed synthetic dataset, it could still have a consistent logic for LLMs even after knowledge editing. The paper should make the true facts after the knowledge editing more clear.

2, The prompt templates and codes are not released. How the query and the structural information of KGs are provided in the prompt will have a big influence on the final experiment results. Can the authors provide them during the rebuttal? And can authors show some examples of the LLM outputs in natural languages after knowledge editing to help readers better understand the mistakes LLMs make?

3, More knowledge editing baselines should be included. In this paper ROME is the mainly considered knowledge editing methods. There are other 'locate and edit' methods such as PMET[1]. And there are other types of knowledge editing with extra parameters such as GRACE[2]. Including more knowledge editing methods will make the 'representation shattering' hypothesis more convincing.

4, Some typos need to be fixed. For example, $(x_i, a, x_j)$ should be  $(x_i, r, x_j)$ in line 191. Why is “1 IC_4 3 IIIA_2 7 IIIA_3 2 IIC_2 6” in line 235-236 a plausible sequence in figure 3? $(x_i lr, x_j)$ is not clear in line 291.

### Questions
Please refer to the questions mentioned in the Weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a mechanistic explanation of the ripple effects of knowledge editing. This explanation considers how the representations of the model changes during the KE. This paper considers a particular cyclic structure. When the model’s training data are generated from this cyclic structure, the learned representation gradually forms a geometry that resembles the cyclic structure of the data. KE, both corrective edits and counterfactual edits, shatter this cyclic structure. In this way, the ripple effect change in the model’s behavior after edits can be illustrated by the change in the representations.

### Strengths
- The ripple effect of knowledge edit has been studied, but the prior works have not explained the effects from a mechanistic viewpoint. This paper takes a nice step toward explaining this effect mechanistically.
- The angle toward explaining this ripple edit effect is interesting (despite a bit niche). Cyclic structure is a commonly occurring structure in natural language, and there is a nice illustration in the representation space.
- This paper uses a nice combination of qualitative and quantitative illustrations to describe the representation shattering effect.

### Weaknesses
 - The quantitative explanation part can take up more space in the writing. Currently only Figure 5(c) involves quantitative description of representation shattering, and other parts are qualitative. Table 1 presents the overall effects of knowledge editing, which is not really the quantitative descriptions.
- Additionally, the definition for describing the representation shattering effect should be introduced earlier. Currently it’s hidden at lines 413-415 at page 8, closer to the end of the paper. This should be moved to the front.
- Subsection 3.3 can be made clearer. Based on the example presented, I struggled at understanding how the nodes are connected, and e.g., what I/III/ABC refer to.
- The effects are tested on a 2-layer nanoGPT Transformer, plus a GPT2. These limit the generalizability of the finding. I’d recommend experimenting on at least two models on each size — perhaps containing a mixture of uni-directional models (like *GPT) and bidirectional models (like BERT).

### Questions
Could you elaborate on the synthetic data generation process? Do A/B/C refer to the entities and the numbers refer to the edges?

### Soundness
3

### Presentation
2

### Contribution
3
