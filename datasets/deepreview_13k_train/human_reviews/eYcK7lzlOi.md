# Unleashing Graph Transformers with Green and Martin Kernels

- Decision: Reject
- Scores: 8, 8, 5, 5

## Abstract
Graph Transformers (GTs) are rapidly emerging as superior models, surpassing traditional message-passing neural networks in graph-level tasks. For optimal performance, it is essential to design GT architectures that embed graph inductive biases and utilize global attention mechanisms through effective structural encodings (SEs). In this work, we introduce novel SEs derived from a rigorous theoretical analysis of random walks (RWs), specifically leveraging the Green and Martin kernels. The Green and Martin kernels are mathematical tools used to observe the long-term behavior of RWs on graphs. By integrating these kernels into the encoding process, we enhance their capability to accurately represent complex graph structures. Our empirical evaluations demonstrate that these approaches enable GTs to achieve state-of-the-art performance on 7 out of 8 benchmark datasets. These include molecular datasets characterized by intricate, non-aperiodic substructures such as benzene rings, and directed acyclic graphs common in the circuit domain. We attribute these performance improvement to the effective capture of the characteristics of non-aperiodic substructures and directed acyclic graphs by our extending encodings. The results not only validate the effectiveness of integrating the Green and Martin kernels into RW-based encodings but also underscore their potential to substantially enhance the learning capabilities of GTs across diverse applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes two graph structural encodings, GKSE and MKSE, based on Green and Martin kernels, respectively. These encodings are evaluated for their theoretical expressiveness, and also empirical performance on multiple datasets when combined with GRIT. The results demonstrate the advantage of GKSE and MKSE as structural encodings.

### Strengths
1. The paper is well-motivated. The authors build upon the known theoretical and practical strengths of RRWP and propose natural extensions (GKSE and MKSE) by considering the steady-state behavior of random walks on graphs.
2. The main claims of the paper are well-supported. The paper provides theoretical analysis on the expressivity of GKSE and MKSE, as well as experimental result demonstrating good performance when combined with GRIT.
3. The paper is self-contained and well-organized. I particularly like how the authors combine mathematical reasoning with intuitive explanations and figures.

### Weaknesses
Despite the paper's solid contributions, I find the explanation regarding the efficacy of GKSE and MKSE (lines 479-509) somewhat unconvincing. To demonstrate this, I will present alternative interpretations of examples presented in these paragraphs, to support the opposite argument: RRWP is more preferable.
1. Figure 1 suggests that RRWP provides a more decoupled representation of graph structures compared to GKSE and MKSE. Although RRWP encodings might not visually resemble the original graph (particularly for even $k$), this decoupling could make it easier for the model's learnable linear encoder to extract structural relationships such as multi-hop neighbors. In contrast, GKSE and MKSE encodings across different $k$ values appear more uniform, which may make it more difficult to extract structural features.
2. The non-aperiodic substructures of a graph causes RRWP to oscillate, as evident in Figures 1 and 3. This provides a reliable way for the model to identify non-aperiodic substructures, which is prevalent in molecular graphs. On the contrary, GKSE and MKSE are not as sensitive to non-aperiodic substructures, making it harder for the model to identify them.
3. For DAGs, RRWP naturally produces a sparse, decoupled representation, as illustrated in Figure 2. This sparsity can enhance the model’s capability to identify structural features, with an added advantage of selecting a suitable value of $K$ based on knowledge of the dataset (e.g., $K=4$ in Figure 2). GKSE and MKSE, in contrast, generate dense, often redundant information across different values of $k$ when applied to DAGs.

These arguments are not presented to promote RRWP, but to highlight the need that lines 479-509 be further clarified to convince the reader that your interpretations are preferable to alternative interpretations, like those presented above. If these claims are speculative, they should be framed as such, and additional supporting evidence would be valuable.

Despite this issue, the paper's overall contributions remain valid and meaningful.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Graph transformers due to their lack of structural awareness, require effective structural encodings. This paper presents two effective structural encodings, called GKSE and MKSE, based on the Green and Martin kernels that can extend the concept of random walks. The authors have supported the effectiveness of GKSE and MKSE via both theoretical and empirical results.

### Strengths
- The paper is well-written and well-motivated. The authors provided enough details about the approach that made its understanding simple. 
- The proposed method is intuitive, relatively simple (yet effective), and is a natural extension, which I believe is very important.
- Recently, several approaches have focused on using shortest path encoding, which is very efficient, to better learn the structure of the graph. The authors have provided theoretical results that how GKSE and MKSE are more powerful and expressive than shortest path encoding.

### Weaknesses
 - My main concern is about the efficiency of the proposed methods: How can GKSE and MKSE affect the memory usage and training time of graph transformers (compared to common structural encodings and shortest path encodings)?  
- Recently, for the sake of efficiency, several GTs have used more complex tokenization (e.g., NAGPhormer). Due to their scalability, they are more practical and also they have a better inductive bias about the graph structure. It would be interesting to see the effect of GKSE and MKSE on these models.
- I believe the current experiments cannot support the effectiveness of GKSE and MKSE as they show the performance gain only on GRIT. Is this performance gain limited to only this model? How can using GKSE and MKSE as the structural encoding for other methods (GPS, NAGphormer, etc.) affect performance?
- Is there any trade-off between GKSE and MKSE? Is there any performance gain if we use both? (e.g., their concatenation)
- (Minor) I suggest using a different citation format (e.g. using [13] instead of (13)). The current format results in confusion whether this is a citation or a reference to an equation (for example lines 222, 274, etc.).

### Questions
- Why there are inconsistencies in the chosen baselines across different benchmarks? E.g., why GraphSAGE’s results are not reported for all benchmarks?
- Is there any performance gain if we use both GKSE and MKSE? (e.g., their concatenation)
- How can using GKSE and MKSE as the structural encoding for other methods than GRIT (e.g., GPS, NAGphormer, etc.) affect performance?
- How do GKSE and MKSE affect memory usage and training time?

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
5

### Summary
The paper introduces novel structural positional encodings (PEs) for graph transformers, based on the Green and Martin kernels. Both capture certain aspects of the long-term behavior of random walks. The former captures the expected number of visits to one node from another, the latter represents the probability that a RW starting from one node will reach another node within finite time. The model is evaluated over a range of graph datasets of different kinds.

(Please note: I did not check the theory in Sec 4.2 in detail)

### Strengths
- The paper is well-written and nice to read.
- The motivation and general consideration of the research topic make sense to me.
- The evaluation covers a wide range of datasets of different kind.

### Weaknesses
 - The performance improvements seem minimal, if existent. Most of the numbers (if I didn't miss anything) are within standard deviation of the next best existing model, which is in several cases +RRWP.
- Given that this seems to be a general PE proposal a consideration of different graph transformers would be more suitable, i.e., beyond just GRIT. The current evaluation does not sufficiently demonstrate the broad applicability of the proposed positional encodings.
- A suitable baseline on the DAG data would be DAG transformer [1]

### Questions
- Why is Table 3 missing the +RRWP baseline?
- The analysis in Fig. 1 is interesting, but the results shown in the tables do not show great differences. The text says "Consequently, RRWP, which is based on these transition probabilities, may fail to capture the structural properties of graphs containing non-aperiodic substructure". Could one maybe select corresponding data (sub)sets to show and test this? 
- Could it make sense to combine RRWP and/or these PEs?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Graph Transformers have become very popular in graph-level tasks recently, and their success significantly depends on the employed structural encodings. This paper introduces two new encodings which are derived from the theory of random walks, namely the Green and Martin kernels. The authors define finite-step variants of the two kernels which capture random walk patterns within a limited number of steps. The encodings from the two kernels are integrated into the GRIT model and are evaluated in graph classification and regression tasks. In most cases, the encodings enhance the performance of GRIT and lead to state-of-the-art results.

### Strengths
- The paper provides an extensive experimental evaluation of the proposed structural encodings. The evaluation does not only focus on molecules, but also on other types of graphs such as circuits modeled as DAGs and images modeled as graphs.

- The proposed structural encodings seem to lead to performance improvements and to state-of-the-art results. GRIT+GKSE and GRIT+MKSE outperform the baselines on 7 out of the 8 considered benchmark datasets.

- It is shown in the paper that MKSE possess a unique expressiveness independent of RRWP. Thus, MKSE can potentially capture properties of graphs that cannot be captured by RRWP.

### Weaknesses
 - As discussed above, GRIT+GKSE and GRIT+MKSE outperform the baselines on 7 out of the 8 considered benchmark datasets. However, even though GKSE and MKSE are experimentally shown to perform better than their main competitor (RRWP encodings), it is not clear to me whether the improvements provided by the proposed encodings are statistically significant. On almost all benchmark datasets, the improvement over GRIT+RRWP appears to be minor.

- Some details about the proposed models and the experimental setup are missing from the paper. The values of the different hyperparameters are provided in Tables 6 and 7 in the Appendix, but I could not find any details about the employed architecture. It is mentioned that the proposed encodings are integrated into GRIT, but for the paper to be self-contained, I would suggest the authors add a description of GRIT into the Appendix. More importantly, some details about how the proposed encodings are integrated into the models are also missing from the paper. GKSE and MKSE are defined (in l.216-l.222) over pairs of nodes. Hence, in my understanding, those encodings could not be used as initial node-level structural encodings. They could potentially be utilized as edge-level structural encodings. I would suggest the authors provide more details about the model.

- I would encourage the authors to better motivate the use of the proposed encodings. Since RRWP encodings are also derived from the theory of random walks, why should one prefer the proposed encodings over RRWP encodings? Table 10 shows that computing GKSE and MKSE is computationally more expensive than computing RRWP encodings. Therefore, the authors should justify why one should choose the proposed encodings for a particular application.

- Even though the paper is not hard to read, there exist some typos and other types of errors. For example, in l.126, "matrixwith" should be replaced with "matrix with". Also in l.290 (Theorem 3, part 2) "GKSE" should be replaced with "MKSE".

### Questions
The proposed kernels appear to be very similar to the hitting times and commute time distances, two popular tools which are commonly used to analyze the structure of graphs. Is there a connection between the proposed kernels and hitting and commute times? If there is some connection, can you please provide more details?

### Soundness
4

### Presentation
3

### Contribution
2
