# Long-Short Decision Transformer: Bridging Global and Local Dependencies for Generalized Decision-Making

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Decision Transformers (DTs) effectively capture long-range dependencies using self-attention but struggle with fine-grained local relationships, especially the Markovian properties in many offline-RL datasets. Conversely, Decision Convformer (DC) utilizes convolutional filters for capturing local patterns but shows limitations in tasks demanding long-term dependencies, such as Maze2d. To address these limitations and leverage both strengths, we propose the Long-Short Decision Transformer (LSDT), a general-purpose architecture to effectively capture global and local dependencies across two specialized parallel branches (self-attention and convolution). We explore how these branches complement each other by modeling various ranged dependencies across different environments, and compare it against other baselines. Experimental results demonstrate our LSDT achieves state-of-the-art performance and notable gains over the standard DT in D4RL offline RL benchmark. Leveraging the parallel architecture, LSDT performs consistently on diverse datasets, including Markovian and non-Markovian. We also demonstrate the flexibility of LSDT's architecture, where its specialized branches can be replaced or integrated into models like DC to improve their performance in capturing diverse dependencies. Finally, we also highlight the role of goal states in improving decision-making for goal-reaching tasks like Antmaze.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper targets two critical limitations in existing Decision Transformers (DTs)-based offline reinforcement learning: (1) DTs' weakness in capturing local dependencies which is associated with Markovian properties in many offline-RL datasets; (2) DTs’ struggles with goal-reaching tasks involving diverse goals and sparse rewards. To address these two issues, the authors propose a dual-branch architecture, Long-Short Decision Transformer (LSDT), that combines self-attention for global patterns and dynamic convolution for local features, along with a goal-state conditioning mechanism. The main contribution is the asymmetric dimension-splitting between branches. Experiments are conducted across diverse environments and the results demonstrate state-of-the-art performance on several D4RL benchmarks, particularly showing significant improvements in complex environments like Antmaze-medium and Maze2d-large.

### Strengths
**(S1) The Significance and Clear Presentation of Research Question:**
The paper addresses a critical challenge in Transformer-based offline-RL with great clarity and motivation. The key motivation lies in identifying and solving the global and local dependencies modeling, which has been a critical limitation in existing RL architectures. Unlike existing approaches that treated this as an either-or choice (DTs focusing on global, DCs on local dependencies), the proposed LSDT introduces dual-branch parallel processing that captures both types of dependencies simultaneously, and thereby hope to benefit offline-RL tasks.

**(S2) Technical Soundness:** 
The technical contributions of the proposed LSDT are well-reasoned. Concretely, the Dynamic Convolution in the short-term branch represents an improvement over static convolution methods. By dynamically generating weights based on current input rather than using fixed weights after training, the model may achieve better generalization across diverse environments. The connection between LSDT and the targeted question is clear and reasonable. This is evident in the experiments where LSDT achieves great performance in both Markovian environments (with strong local feature requirements) and the non-Markovian ones (with strong long-range modeling requirements). The asymmetric dimension splitting, controlled by ratio ξ, provides flexibility in adapting the architecture to different tasks. This is demonstrated through ablation studies showing how different ratio values optimize performance across various environments (e.g., ≥50% for Markovian and ≤50% for non-Markovian tasks). Complementing these components, the goal-state conditioning mechanism, while straightforward, addresses the path planning limitations in sparse reward settings. The results on Antmaze tasks (showing improvements from 0% to over 70% success rate) provide strong validation of this method. The optional Hybrid Fusion Module, though not always necessary, presents an approach to dynamic feature selection, with visualization studies clearly showing its ability to weight different features based on task requirements adaptively.

**(S3) Thorough Experiments and Ablation Studies:**
The experiments are thorough and well-structured. The authors conduct extensive experiments across diverse environments, including MuJoCo locomotion tasks, Maze2d navigation, AntMaze environments, and Adroit manipulation tasks. The ablation studies are comprehensive, examining the impact of different architecture choices, such as dimension ratio (across 20 different values), kernel size (from 6 to 18), and fusion methods. The performance gains are consistently shown across both Markovian datasets (achieving 82.0 average normalized score in locomotion tasks) and non-Markovian datasets (significant improvements in Maze2d-large and Antmaze-medium). The authors also provide an empirical analysis of failure cases and performance characteristics under different hyper-parameter settings, making the results valuable for practical implementation and future studies in the community.

### Weaknesses
 **(W1) Limited Theoretical Analysis and Foundation:** 
While the empirical results are impressive, the lack of formal analysis leaves several crucial questions unanswered. First, there is limited theoretical justification for why the combination of self-attention and dynamic convolution in parallel branches should perform better than sequential or alternative operations in RL. The paper does not provide any analysis regarding the conditions under which this specific parallel architecture would be optimal, nor does it explore the potential for interference or redundancy between the two branches. Second, the interaction between the two branches lacks theoretical examination. For instance, how information flows between them, and whether the information is complementary or redundant, remains unexplored. The paper does not discuss the potential for one branch to dominate the learning process or how the gradients are balanced between the two branches. Third, the paper provides no theoretical bounds or guarantees on the optimal dimension ratio ξ. While empirical guidelines are provided (e.g., ≥50% for Markovian tasks), a theoretical framework supporting these choices, such as a convergence analysis or a generalization bound, would make the approach more principled. The absence of such analysis makes it difficult to understand the fundamental properties of the proposed architecture and its limitations.

**(W2) Limited Technical Originality and Domain-Specific Analysis:** 
While the proposed dual-branch architecture exhibits strong empirical results, its design principle of combining global and local feature extraction has been extensively explored in other domains, particularly Computer Vision and NLP. As such, this work would significantly benefit from a more in-depth analysis of why and how this architecture specifically addresses the unique challenges in reinforcement learning. For example, a deeper analysis to show the relationship between Markovian/non-Markovian properties and global-local feature extraction is needed. The paper lacks a clear explanation of how local convolution patterns capture Markovian state transitions, while global attention mechanisms model longer-term dependencies in policy behavior. This could be supported by visualization that expresses how different types of dependencies are processed in each branch for decision-making, such as visualizing the receptive fields of the convolutional filters and the attention maps of the self-attention mechanism. Furthermore, the paper does not explore the potential for alternative architectures that could achieve similar or better performance with fewer parameters or lower computational costs.

**(W3) Architecture Designs and Computational Efficiency Concerns:** 
Several architectural choices raise concerns about practical applicability and scalability. The requirement for manual tuning of the dimension ratio ξ represents a fundamental limitation in the adaptability of LSDT architecture. While the authors provide general guidelines (≥50% for Markovian, ≤50% for non-Markovian tasks), the absence of an adaptive way for determining optimal ratios necessitates extensive experimentation for each new environment. This becomes particularly problematic in real-world applications where task characteristics may not be clearly Markovian or non-Markovian or may shift during deployment. Additionally, the computational complexity of the dual-branch architecture deserves deeper analysis. While the authors mention reduced context length requirements compared to standard DT, they don't provide a comprehensive analysis of the compute-performance trade-off. The paper lacks a detailed breakdown of the computational costs associated with each component of the architecture, such as the dynamic convolution and self-attention layers. This makes it difficult to assess the practical feasibility of the proposed method for large-scale RL problems.

### Questions
**(Q1)** Could the authors provide training curves showing the convergence behavior of both branches? This analysis would provide insights into how the dual-branch architecture learns to balance global and local features during training. Specifically, it would be valuable to see:

- The loss trajectories for each branch separately;
- The relative contribution of each branch to the final decision at different training stages;
- Whether one branch tends to converge faster than the other;

**(Q2)** Have the authors considered using adaptive dimension ratios that change during training? 

**(Q3)** To better understand the architecture benefits, I suggest the authors provide t-SNE plots of learned state representations from both branches. This could provide more insights into the technical contribution of this work.

**(Q4)** I suggest the authors conduct an empirical analysis of the computational efficiency. This would help practitioners in the community evaluate the practical trade-offs of implementing LSDT, including:

- FLOPs comparison with baseline models;
- Memory usage analysis for different dimension ratios;
- Training time comparison with single-branch architectures;

---
**Additional Comments:**

I hope my review helps to further strengthen this paper and helps the authors, fellow reviewers, and Area Chairs understand the basis of my recommendation. I also look forward to the rebuttal feedback and further discussions, and would be glad to raise my rating if thoughtful responses and improvements are provided.

---
## **-------------------- Post-Rebuttal Summary --------------------**

The additional experiments, discussions, and revised manuscript provided by the authors have significantly strengthened the work and addressed most of my concerns. I suppose this work can provide knowledge advancement to the community, and I look forward to the final version manuscript, which incorporates the additional insights and information presented in the rebuttal stage.

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
2

### Summary
The manuscript proposes the Long-Short Decision Transformer (LSDT), a model that effectively combines the strengths of Decision Transformer (DT) and Decision Convformer (DC) through a dual-branch architecture.
This architecture uses a dimension ratio, ξ, to dynamically control the proportion of channels processed by each branch—self-attention for long-range dependencies and convolution for local patterns.
The approach is simple yet intuitive, as it leverages complementary feature extraction methods to enhance both global and local dependency modeling, adapting flexibly to diverse reinforcement learning tasks.

### Strengths
The proposed Long-Short Decision Transformer (LSDT) presents an interesting approach by combining attention and convolutional pathways to handle both global and local dependencies effectively.
This dual-branch design not only enhances interpretability but also achieves strong performance across diverse reinforcement learning tasks, particularly outperforming benchmarks on the D4RL dataset.
The flexibility offered by the dimension ratio, ξ, adds adaptability, allowing LSDT to maintain robust performance in both Markovian and non-Markovian environments.
Additionally, the model’s simplicity and modularity enable straightforward integration into existing architectures, further extending its practical utility.

### Weaknesses
The experiments on the routing mechanism in the LSDT are limited, leaving open questions about potential improvements.
Given that the proposed method can be viewed as a two-expert MoE (Mixture of Experts) architecture, alternative ways of channel splitting and information routing could be explored.
For instance, introducing two separate linear projections with residual connections before feeding inputs to the branches could enhance feature extraction. Another approach might involve feeding the same embedding into both branches and combining the outputs with a learnable weighted sum. Evaluating these alternative configurations could offer insights into optimizing the dual-branch structure, potentially enhancing the model’s performance and efficiency.

### Questions
See weakness

### Soundness
3

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
3

### Summary
This submission presents a novel architecture for the decision transformer named LSDT that tries to capture both long-term and short range dependencies, such as local spatiotemporal associations, for offline RL tasks. This is achieveed by adding a second, convolutional block next to the self attention block, and the sizes of the two blocks (eg in terms of dimensions) can vary according to the needs of the task to solve.  The paper further proposes to incorporating goal states into the conditioning information for further performance gains in some cases. Experiments are conducted on the D4RL benchmark, where LSDT achieces performance comparable to state-of-the-art RL methods.

### Strengths
S1) The motivation if the proposed approach is clear and the paper is well written. The closest related works are cited and the contributions pf the paper are clearly presented and illustrated both qualitatively and quantitatively.
S2) Although the technical contributions are incremental, the paper presents clear figures that illustrate the strenghts of the proposed method, and also ablations that study the key points of the proposed architecture
S3) The method seems to achieve results comaprable to the state of the art.

### Weaknesses
W1) The technical contribution is following other works that propose two-branch transformer blocks: appending a convolutional branch in the architecture, and using a straighforward attention masking scheme to capture long vs short dependences.

W2) The split across the two branches is simple, ie across the channels dimension, and it is manual via hyper parameter \xi, an adjustment which is non trivial and highly task based. The submission would be stronger if an automatic way of selecting \xi was proposed. It would be great if the authors discussed potential methods for automating this. 

W3) An issue uncovered in Fig7 is the following: this paper is presenting a method for a compromize between DT and CDT, via splitting the dimensions across the two. However, we see in Fig 7 that in most cases there doesnt seem to be a "peak" inbetween the already existing edge cases.  Could the authors discuss this further? It would be nice to address this apparent discrepancy between one of the motivationsof their method and the results shown.

### Questions
Q1) Could the CDT subfig in Figure 1 also be depicting the Decision Convformer (DC)? It would be clearer if DT and DC were clearly marked if this is  the case

Q2) How well would the DC perform if one substitutes their conv filters with DynamicConv?

Q3) Are \xi identical across all datasets in Table 1? 

Q4) Is goal conditioning used in Table 1, and if not what is the performance of LSDT-gs in this case?

Q5) IS FIg3 depicting a  single sequence or averages over many?

### Soundness
3

### Presentation
4

### Contribution
2
