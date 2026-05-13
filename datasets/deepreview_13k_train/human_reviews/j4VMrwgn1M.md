# Training Graph Transformers via Curriculum-Enhanced Attention Distillation

- Decision: Accept
- Scores: 8, 8, 6, 5

## Abstract
Recent studies have shown that Graph Transformers (GTs) can be effective for specific graph-level tasks. However, when it comes to node classification, training GTs remains challenging, especially in semi-supervised settings with a severe scarcity of labeled data. Our paper aims to address this research gap by focusing on semi-supervised node classification. To accomplish this, we develop a curriculum-enhanced attention distillation method that involves utilizing a Local GT teacher and a Global GT student. Additionally, we introduce the concepts of in-class and out-of-class and then propose two improvements, out-of-class entropy and top-k pruning, to facilitate the student's out-of-class exploration under the teacher's in-class guidance. Taking inspiration from human learning, our method involves a curriculum mechanism for distillation that initially provides strict guidance to the student and gradually allows for more out-of-class exploration by a dynamic balance. Extensive experiments show that our method outperforms many state-of-the-art approaches on seven public graph benchmarks, proving its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a curriculum-enhanced attention distillation method that involves utilizing a Local Graph Transformer as the teacher model and a Global Graph Transformer as the student model. They also introduce the concepts of “in-class” and “out-of-class” regions and introduce out-of-class entropy and top-k pruning. Experiments are conducted on 7 node classification benchmarks, which show the performance benefits of the proposed method.

### Strengths
The paper proposes an effective method of training Graph Transformers. The method is verified in multiple node classification benchmarks. The distillation comparative studies show that the method generally outperforms both the teacher and student models. The paper is well-written with justified motivations and reasonable solutions.

### Weaknesses
Some of the implementation details are unclear. Please see the questions listed below.

Q1: The distillation losses are calculated by distances between the teacher and student attention coefficients, which are averaged over graph nodes and attention layers, as demonstrated by Equation (7). Does the averaging calculation smooth out the signal?

Q2: What is the exact distance metric $d$ do you use?

Q3: For the top-k pruning, what is the exact $k$ do you use? Does it vary significantly between datasets? For example Pubmed has 19,717 nodes while Cornell and Texas only have 183 nodes, does the k values different?

Q4: What are the specific LGT and GGT models do you use in the experiments?

### Questions
Q1: The distillation losses are calculated by distances between the teacher and student attention coefficients, which are averaged over graph nodes and attention layers, as demonstrated by Equation (7). Does the averaging calculation smooth out the signal?

Q2: What is the exact distance metric $d$ do you use?

Q3: For the top-k pruning, what is the exact $k$ do you use? Does it vary significantly between datasets? For example Pubmed has 19,717 nodes while Cornell and Texas only have 183 nodes, does the k values different? 

Q4: What are the specific LGT and GGT models do you use in the experiments?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel curriculum-enhanced attention distillation method to improve the training of graph transformers for semi-supervised node classification. The key ideas and contributions are: 

- Proposes using attention coefficients from a Local Graph Transformer (LGT) teacher to guide an untrained Global Graph Transformer (GGT) student via layer-to-layer attention distillation. - Introduces the concepts of in-class and out-of-class attention. Proposes two techniques - out-of-class entropy and top-k pruning - to encourage active out-of-class exploration by the student. 

- Inspired by curriculum learning, proposes curriculum distillation where the teacher gradually allows more out-of-class exploration via dynamic scheduling of distillation loss weights. 

- Achieves significant performance gains over strong baselines on seven benchmark graph datasets, demonstrating the ability to improve training and generalization of graph transformers.

Overall, the work makes multiple innovations in adapting knowledge distillation for graph transformers in a semi-supervised node classification setting. The curriculum-based attention distillation framework is intuitive and achieves strong empirical results.

### Strengths
-  The work presents a novel perspective of applying attention-based knowledge distillation for graph transformers. Using the teacher's attention maps to guide the student is an original idea. The curriculum distillation framework that balances in-class and out-of-class attention over time is also a creative approach.

-  The methodology is technically sound, with clear algorithm descriptions, reasonable design choices, and rigorous empirical evaluation. The curriculum scheduling strategies are grounded in educational learning principles. The improvements for out-of-class attention demonstrate thoughtful analysis.

-  The paper is well-written and easy to follow. The motivations are clearly explained, and the methodology sections provide sufficient details. Figures aid understanding of the core concepts like curriculum scheduling.

### Weaknesses
 - The proposed method relies on selecting the right teacher-student pair, but the criteria for these choices are not fully analyzed. How does performance vary for different teacher-student combinations? Specifically, the paper lacks a systematic exploration of how the architectural differences between the teacher and student impact the distillation process. For instance, what happens if the teacher has significantly more parameters or a different number of layers? The current analysis only considers a single teacher-student pair, which limits the generalizability of the findings.

- While outperforming baselines, the absolute performance gaps are sometimes small (~1-2%). The gains may not justify the added complexity in some applications. Furthermore, the paper does not provide a detailed analysis of the computational overhead introduced by the distillation process. How does the training time and memory consumption compare to training the student model directly? A thorough analysis of the trade-offs between performance gains and computational costs is needed.

- Curriculum scheduling adds hyperparameters like epoch boundaries. The impact of these hyperparameters could be studied more systematically. In addition, I highly recommend that authors use auto-distillation (KD-Zero: Evolving Knowledge Distiller for Any Teacher-Student Pairs (NeurIPS-2023, Automated Knowledge Distillation via Monte Carlo Tree Search (ICCV2023)) to optimize different parameter options.


- Attention distillation for other graph model families besides transformers could also be promising but is not explored. It is essential to incorporate a thorough discussion of relevant KD-related studies, including Self-Regulated Feature Learning via Teacher-free Feature Distillation (ECCV2022), NORM: Knowledge Distillation via N-to-One Representation Matching (ICLR2023), Shadow Knowledge Distillation: Bridging Offline and Online Knowledge Transfer (NIPS2022), DisWOT: Student Architecture Search for Distillation Without Training (CVPR2023) . This discussion will help position the proposed approach within the existing literature, establish connections, and provide valuable insights for potential comparisons.

### Questions
see Weaknesses


-------------------------------------------


The author's response addressed my concerns well, so I'm improving my score to acceptance, thanks!

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel curriculum-enhanced attention distillation approach to enhance the training of Graph Transformers (GTs). This method leverages attention coefficients as knowledge representations for more effective knowledge transfer from a limited graph transformer (LGT) teacher to a general graph transformer (GGT) student. The approach also incorporates out-of-class entropy and top-k pruning to promote active exploration and the surpassing of the teacher's performance by the student. Additionally, curriculum distillation is introduced to manage the attention focus dynamically between in-class and out-of-class learning phases, thereby improving the overall performance. The proposed method has been empirically validated across multiple datasets, demonstrating its efficacy in improving the GTs training process and their generalization capabilities

### Strengths
- The paper is well-written and presented.
- Empirical results are promising.

### Weaknesses
 - The novelty is limited. Not a big concern, but the paper combines a few well-known methods. 
- The approach is a bit complicated.

### Questions
- The loss function is complex with a few components. In Table 4 the authors evaluated their pipeline's performance sensitivity to each of the components. My first question is how sensitive the model is to variation of these hyperparameters (e.g. $\gamma$, $\beta$)? Both in case of stability and performance.
- Can authors please comment on the scalability of this model? Does it scale to bigger datasets? If yes, have they tried running their model on those?
- Have the authors witnessed a difference in student or teacher behavior in datasets with relatively high homophily values differences?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the challenge of training Graph Transformers for semi-supervised node classification with limited labeled data. The authors propose a curriculum-enhanced attention distillation method that utilizes a Local GT teacher and a Global GT student. By introducing the concepts of in-class and out-of-class, and incorporating out-of-class entropy and top-k pruning, the authors facilitate the student's exploration under the teacher's guidance. Inspired by human learning, the method gradually allows for more out-of-class exploration while maintaining a dynamic balance. Extensive experiments demonstrate the effectiveness of the approach, surpassing state-of-the-art methods on seven public graph benchmarks.

### Strengths
1. The authors identified the limitations of GTs in the task of semi-supervised node classification and effectively addressed them through knowledge distillation, which is a reasonable and effective approach.
2. The proposed two significant improvements, out-of-class entropy and top-k pruning, can constrain the student’s behavior during out-of-class exploration and enhance its generalization capability.
3. The experiments demonstrate enhanced performance and improved generalization capability of the method.

### Weaknesses
1. My major concern is the motivation of the distillation of GTs. Why not apply distillation on other graph networks to obtain more significant performance, e.g. GCNs? The paper does not adequately explore the potential benefits of applying the proposed method to other architectures, particularly simpler models like GCNs, which might reveal whether the performance gains are specific to Graph Transformers or a general benefit of the distillation framework. Furthermore, the method's applicability to other networks is not clear, and the paper should discuss the modifications needed to adapt it to models that do not have inherent attention mechanisms.
2. In Ablation, which components are the most important? Why "w.o. $\gamma$" , "Global uniform distribution" bring such damage for the performance? The ablation study lacks a detailed analysis of the relative importance of each component. It is not clear why removing the distillation loss term ($\gamma$) or using a global uniform distribution for attention weights has such a detrimental impact on performance. A more in-depth discussion is needed to explain the underlying mechanisms and the specific roles of these components.
3. Why not compare to some general KD methods for classification task, e.g. KD, AT, FitNets, DKD, CRD? The paper does not compare the proposed method with existing general knowledge distillation techniques for classification tasks. A comparison with methods like KD, AT, FitNets, DKD, and CRD would help to contextualize the performance of the proposed method and highlight its specific advantages or disadvantages compared to established approaches.
4. Please provide the details of Teacher and student, including architecture, parameters, etc. If the utilized "Graph Transformer" equal to "Graphormer" or "Nodeformer"? If not, why not conduct distillation on them? The paper lacks crucial details about the teacher and student model architectures, including the number of layers, hidden dimensions, and specific parameter settings. It is also unclear whether the utilized "Graph Transformer" is equivalent to existing models like "Graphormer" or "Nodeformer". If not, the rationale for not using these models and the potential benefits of applying the distillation method to them should be discussed.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
