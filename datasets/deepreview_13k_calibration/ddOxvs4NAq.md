# Generalization and Knowledge Transfer in Abstract Visual Reasoning Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3

## Abstract
We study generalization and knowledge reuse capabilities of deep neural networks in the domain of abstract visual reasoning (AVR), employing Raven's Progressive Matrices (RPMs), a recognized benchmark task for assessing AVR abilities.
Two knowledge transfer scenarios referring to the I-RAVEN dataset are investigated.
Firstly, inspired by generalization assessment capabilities of the PGM dataset and popularity of I-RAVEN, we introduce \emph{Attributeless-I-RAVEN}, a benchmark with four generalization regimes that allow to test generalization of abstract rules applied to held-out attributes.
Secondly, we construct \emph{I-RAVEN-Mesh}, a dataset that enriches RPMs with a novel component structure comprising line-based patterns, facilitating assessment of progressive knowledge acquisition in transfer learning setting.
The developed benchmarks reveal shortcomings of the contemporary deep learning models, which we partly address with
\emph{Pathways of Normalized Group Convolution (PoNG)} model, a novel neural architecture for solving AVR tasks. PoNG excels in both presented challenges, as well as the standard I-RAVEN and PGM setups.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the generalization and knowledge transfer capabilities of DNNs in abstract visual reasoning tasks. The authors introduce two new datasets, A-I-RAVEN and I-RAVEN-Mesh to assess generalization capacity of reasoning and progressive knowledge acquisition in transfer learning setting, respectively.  They show the lack of generalization for the contemporary models and propose PoNG to solve the problems.  The results reveals improvement over SOTA reference models.

### Strengths
1. Two new dataset were introduced to evaluate the generatilization and transfer learning in abstract visual reasoning tasks.

2. A new model PoNG was proposed to improve the generalization capacity of abstract visual reasoning.

3. PoNG aslo performs well on other AVR tasks (visual analogy problem),  showcasing its generality in analogical reasoning.

### Weaknesses
One main problem:

The I-RAVEN results from Table 2 are different from those in the original paper. For example, the result of PredRNet in original paper [1] is 96.5 while the authors report it as 88.8.

Some SOTA models are not included in the paper, such as DRNet [2] and SLOT-ABSTRACTOR [3].

### Questions
1. The I-RAVEN results from Table 2 are different from those in the original paper. For example, the result of PredRNet in original paper [1] is 96.5 while the authors report it as 88.8.

2. Some SOTA models are not included in the paper, such as DRNet [2] and SLOT-ABSTRACTOR [3].



[1]Yang L, You H, Zhen Z, et al. Neural prediction errors enable analogical visual reasoning in human standard intelligence tests[C]//ICML, 2023: 39572-39583.

[2]Zhao K, Xu C, Si B. Learning Visual Abstract Reasoning through Dual-Stream Networks[C]//AAAI. 2024, 38(15): 16979-16988.

[3]Mondal S S, Cohen J D, Webb T W. Slot abstractors: Toward scalable abstract visual reasoning[C]//ICML, 2024.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes two new benchmarks for abstract visual reasoning (AVR) based on Raven’s Progressive Matrices (RPM), called Attributeless-I-RAVEN comprising 10 generalization regimes, and I-RAVEN-Mesh, an extension of I-RAVEN with grid lines overlaid to evaluate progressive generalization in transfer learning setting. The authors evaluate the performance of state-of-the-art AVR models on these benchmarks, demonstrating their inability to generalize, and develop a new AVR model, called PoNG. PoNG consists of an encoder which generates an embedding for each image panel constituting the RPM problem, a reasoner module that processes the panel embeddings, and prediction heads for predicting the answer and the RPM rules. The reasoner module has four parallel pathways implementing standard 1D convolutions, grouped, and group-paired convolutions. The authors show that PoNG demonstrates state-of-the-art performance on the two proposed benchmarks, alongwith improvements on previous AVR benchmarks, I-RAVEN, PGM and visual analogy problems involving real-world images. Ablation studies demonstrate the effectiveness of grouped and group-paired convolutions, normalization in the parallel pathways of the reasoner module, and auxiliary losses for predicting matrix rules.

### Strengths
1. The authors propose two AVR benchmarks, Attributeless-I-RAVEN and I-RAVEN-Mesh for measuring the generalization and transfer learning capabilities of AVR models. 

2. The authors also propose a new AVR model, Pathways of normalized group convolution (PoNG), which demonstrate state of the art performance on the two proposed benchmarks.

3. PoNG also demonstrates improvements on previous AVR benchmarks, I-RAVEN, PGM and visual analogy problems involving real world images.

4. The paper is well-written and easy to follow.

### Weaknesses
1. The performance of the proposed model PoNG seems to heavily depend on auxiliary losses for predicting matrix rules, which might not be available or easily obtained for RPM datasets. If the other baseline methods aren’t trained with the auxiliary losses, the comparison is unfair.

2. The motivation behind the design of parallel pathways in the reasoner module is missing, and it is also not clear how this can be generally useful for non-AVR settings.

### Questions
1. How are the values of loss weights $\beta$ and $\gamma$ in line 340 chosen?

2. Are the baseline models also trained with the auxiliary loss to predict the rules like PoNG? 

3. It would be informative to see which of the two pathways (P3 or P4) play a major role in PoNG’s performance? Also are 4 four parallel pathways really necessary or just P3 and P4 are enough?

4. For I-RAVEN, and the two proposed benchmarks the authors should also evaluate ARII [1]. 

5. For PGM, the authors should also compare to other strong-performing baseline methods like ARII [1], MRNet [2], and Slot-Abstractors [3].

6. Can the authors share some intuition behind PoNG performing so well for Heldout Attribute pairs, and Heldout Triple pairs regimes of the PGM dataset but struggle with regimes like H-O-L-T, H-O-S-C, and Extrapolation?

7. The authors should also report the average performance over all PGM regimes in Table 4,  to better understand the overall SOTA performance.

8. A more rigorous test of transfer learning would be to test zeroshot performance on I-RAVEN-Mesh, with models only pretrained on I-RAVEN.

[1] -  Zhang, W., Mo, S., Liu, X. and Song, S., 2022. Learning robust rule representations for abstract reasoning via internal inferences. Advances in Neural Information Processing Systems, 35, pp.33550-33562.

[2] - Benny, Y., Pekar, N. and Wolf, L., 2021. Scale-localized abstract reasoning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 12557-12565).


[3] -  Mondal, S.S., Cohen, J.D. and Webb, T.W., 2024. Slot abstractors: Toward scalable abstract visual reasoning. arXiv preprint arXiv:2403.03458.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the generalization and knowledge transfer capabilities of deep neural networks in the domain of abstract visual reasoning (AVR), specifically focusing on Raven’s Progressive Matrices (RPMs). The authors introduce two new datasets, Attributeless-I-RAVEN and I-RAVEN-Mesh, and propose a new neural architecture called Pathways of Normalized Group Convolution (PoNG). The paper also takes a series of experiments to analysis different AVR models in these two datasets.

### Strengths
Pros:

1. The introduction of Attributeless-I-RAVEN with 10 generalization regimes is a contribution. It allows for a more comprehensive assessment of a model's ability to generalize to novel attributes and rule combinations, which is a crucial aspect of AVR. The detailed description of the regimes and the corresponding held-out attributes and rules provides a rich set of challenges for evaluating AVR models.

2. I-RAVEN-Mesh, with a grid-like structure embedded, is another valuable addition. It enables the study of progressive knowledge acquisition in a transfer learning setting, which is an important research direction in the field. The ability to overlay line-based patterns on the RPM matrices and the clear definition of the mesh component's attributes and rules add complexity and realism to the task.

3. This study presents a novel architecture that combines parallel design, weight sharing, and normalization techniques. The pathways block, with its four parallel pathways and the use of normalized group convolution operators, is a unique feature of the model. 

4. The authors conduct an extensive evaluation on the proposed benchmarks and other related datasets. This comparative analysis provides valuable insights into the performance and limitations of existing models in terms of generalization and knowledge transfer.

### Weaknesses
1. While the paper provides a detailed description of the datasets in terms of their composition and the rules governing the matrices, the process of generating the datasets could be more transparent. The use of a data generator is mentioned, but the specific algorithms and parameters used in the generation process are not described in sufficient detail. This makes it difficult for other researchers to fully understand the datasets. For example, what are the exact ranges for attribute values like color or size? How are the specific object types chosen and what is the distribution of these types? Without this information, it's hard to assess the dataset's complexity and potential biases.

2. The motivation behind certain design choices in the datasets, such as the specific combinations of held-out attributes and rules in Attributeless-I-RAVEN, could be further elaborated. A more in-depth explanation of how these choices were made and what they are intended to test would enhance the understanding of the datasets' significance. For instance, why were these particular combinations of attributes and rules selected for the extended regimes, and what specific aspects of generalization are they designed to challenge? The paper would benefit from a more detailed justification of these choices.

3. While the paper shows that current models struggle on the proposed benchmarks, the analysis of why generalization is difficult could be deeper. For example, what specific aspects of the held-out attributes or incremental structures make the tasks challenging? Are there any patterns or trends in the model failures that could provide more insights for future improvements? For example, are there specific rules or attribute combinations that consistently lead to poor performance? A more granular analysis of the failure modes would be valuable.

4. The paper could discuss more about the motivation of design choices of PoNG and why they are effective. For example, what is the intuition behind the parallel pathways and how do they contribute to better generalization? The paper mentions the use of normalized group convolution, but it does not provide a clear explanation of why this particular choice is beneficial for the task. A more detailed explanation of the architectural choices and their impact on performance is needed.

5. The evaluation of PoNG is mainly limited to RPM benchmarks and visual analogy datasets. It would be beneficial to test the model on a more diverse set of tasks to further validate its generality. As mentioned in the paper, there are other tasks in the AVR domain that could be explored. Moreover, the connection between the proposed benchmarks and real-world applications could be strengthened. How could the results of this research be applied in practical scenarios?

6. I found that the baseline results reported in this paper are inconsistent with several original models. For example, PredRNet and Relbase got 96.5 and 90.5 accuracy on I-RAVEN in their original study. This study only reports them as 88.8 and 89.6. This is also the case for CoPINet and SRAN. I suspect the authors deliberately tuning parameters to get bad results... which is strange and unacceptable.

### Questions
I outlined my questions above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigate the generalization and knowledge reuse capabilities of deep neural networks in abstract visual reasoning (AVR) using Raven's Progressive Matrices (RPMs). They introduce two novel benchmarks, Attributeless-I-RAVEN and I-RAVEN-Mesh, aimed at assessing the generalization of abstract rules and supporting progressive knowledge acquisition in transfer learning contexts. Furthermore, the proposed Pathways of Normalized Group Convolution (PoNG) model shows superior performance on these benchmarks as well as in visual analogy tasks, indicating its effectiveness in AVR beyond RPMs.

### Strengths
This work proposes a novel suite of generalization challenges stemming from I-RAVEN, the authors introduce Attributeless-I-RAVEN, comprising 10 generalization regime, and I-RAVEN-Mesh, a variant of I-RAVEN with a new grid-like structure overlaid on the matrices.
Finally, they propose Pathways of Normalized Group Convolution (PoNG), a novel AVR model. The paper is well-presented.

### Weaknesses
In this paper, the authors claim, "Compared to PGM, our datasets feature compositionality and variety of figure configurations, and their processing doesn’t require substantial computational resources." While this addresses some issues with PGM to a certain extent, it also constitutes a form of redundant work, and the newly generated Raven puzzles do not appear to be more difficult than those in PGM. Additionally, the proposed PoNG does not seem particularly novel. The parallel pathway proposed by PoNG shares similar concepts with DRNet (2024), which limits the novelty of PoNG. The performance of PoNG also does not appear to surpass that of DRNet (2024); the authors should provide a comparison with DRNet (2024). The authors should restate the significance of their proposed Attributeless-I-RAVEN and I-RAVEN-Mesh datasets.

### Questions
**Q1:** The parallel pathway proposed by PoNG shares similar concepts with DRNet (2024), which limits the novelty of PoNG.

**Q2:** The performance of PoNG also does not appear to surpass that of DRNet (2024); the authors should provide a comparison with DRNet (2024).

**Q3:** The authors should restate the significance of their proposed Attributeless-I-RAVEN and I-RAVEN-Mesh datasets.


Ref: Zhao, K., Xu, C., & Si, B. (2024, March). Learning Visual Abstract Reasoning through Dual-Stream Networks. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 38, No. 15, pp. 16979-16988).

### Soundness
3

### Presentation
3

### Contribution
2
