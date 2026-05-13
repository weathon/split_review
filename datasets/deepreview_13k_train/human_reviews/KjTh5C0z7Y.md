# ShortCircuit: AlphaZero-Driven Generative Circuit Design

- Decision: Reject
- Scores: 6, 5, 5, 3, 3, 5

## Abstract
Chip design relies heavily on generating Boolean circuits, such as AND-Inverter Graphs (AIGs), from functional descriptions like truth tables.
This generation operation is a key process in logic synthesis, a primary chip design stage.
While recent advances in deep learning have aimed to accelerate circuit design, these efforts have mostly focused on tasks other than  synthesis, and traditional heuristic methods have plateaued.
In this paper, we introduce \OurMethod{}, a novel transformer-based architecture that leverages the structural properties of AIGs and performs efficient space exploration.
Contrary to prior approaches attempting end-to-end generation of logic circuits using deep networks, \OurMethod{} employs a two-phase process combining supervised with reinforcement learning to enhance generalization to unseen truth tables.
We also propose an AlphaZero variant to handle the double exponentially large state space and the reward sparsity, enabling the discovery of near-optimal designs.
To evaluate  the  generative performance of our model , we extract 500 truth tables from a set of 20 real-world circuits.
\OurMethod{} successfully generates AIGs for $\QSuccessRate\%$ of the
8-input
test truth tables, and outperforms
the state-of-the-art logic synthesis tool, \texttt{ABC}, by $\percentdiff{\QABC}{\QOurMethod}\%$ in terms of circuits size.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a transformer-based architecture designed to generate AND-Inverter Graphs (AIGs) from Boolean truth tables, enhancing logic synthesis efficiency in chip design. The methodology combines supervised learning for the action models and then trains the overall model using reinforcement learning (RL). The work was evaluated using 500 truth tables from 20 real-world circuits, successfully generating AIGs for 98% of the 8-input test truth tables and outperforming the state-of-the-art logic synthesis tool, ABC, by 18.62% in terms of circuit size.

### Strengths
The work considers a novel framework of converting a truth table into an AIG instead of optimizing the synthesis process. Combining the supervised learning of a transformer-based network and the RL is also new, and the results look promising.

The paper is well written and easy to understand.

### Weaknesses
The experiments were focused on the 8-input circuits. It is unknown that if the proposed method is scalable and reuse-able to other sizes of the designs. It is also unknown why only this size of the designs were shown in the experiments.

### Questions
Is the trained model applicable to other sizes of the designs? Why did you only show results of 8-input circuits?

### Soundness
3

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
4

### Summary
This paper presents a transformer-based architecture, “ShortCircuit” to generate optimized AIGs for chip design. ShortCircuit addresses the limitation of large search space of generating AIGs with a two-phased approach consisting of SL and RL. AlphaZero’s framework  was adapted to handle the expansive state space and ShortCircuit achieved 98% success rate on generating AIGs and 18.62% smaller designs compared to the state-of-the-art tool.

### Strengths
1. The paper effectively explains the importance of reducing the search space in AIG generation. A notable point is the statement that "smaller AIGs are generally preferred as they simplify subsequent tasks such as placement and routing," which underscores the multi-level optimization required in chip design. This highlights the practical impact of the work in addressing real-world challenges in the design process.

2. The paper introduces a significant and novel application of machine learning to a critical chip design task. The task is well-defined, and the related works are organized to show how this approach addresses existing gaps, underscoring its relevance and importance in the field.

### Weaknesses
1. Dependence on MCTS for High Success Rate: The reported 98% success rate achieved by ShortCircuit relies on iterative MCTS simulations rather than solely on the ShortCircuit model. While ShortCircuit's primary contribution lies in reducing AIG generation time by narrowing the search space, the use of MCTS adds iteration and time costs, which may offset some of these efficiency gains.

2. Limited Novelty of the Method: The approach lacks strong novelty, as it closely resembles other transformer-based architectures with permutation-driven data augmentation and supervised learning (imitation learning) applied to chip design problems. For instance, a similar work, DevFormer by Kim et al. (2023), employs transformer-based models with supervised learning for device placement, with the main distinction being ShortCircuit’s use of reinforcement learning (off-to-online learning). This raises questions about the unique contributions of this work beyond the addition of reinforcement learning.

### Questions
1. Based on Figure 4, the addition of resyn2 appears to significantly improve performance. Could this be applied to ShortCircuit as well? If so, what level of improvement might be expected?

2. Could you comment on the scalability of this method? It was verified on 8-input truth tables, but would it remain effective when applied to larger-input truth tables?

3. Could you perform an ablation study comparing models that use only Supervised Learning (SL), only Reinforcement Learning (RL), and the combination SL+RL? Additionally, please provide an ablation study on the effect of the amount of offline data used and the impact of data augmentation on performance.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the ShortCircuit, a transformer-based model that combines supervised learning with AlphaZero-style reinforcement learning to generate compact And-Inverter Graphs (AIGs) directly from Boolean truth tables. ShortCircuit overcomes the challenges of circuit generation which has double-exponential state space grows rapidly with the number of inputs. It introduce a novel approach using an iterative process that predicts the next logic gate. That optimizes for circuit size by utilizing truth table representations at each step. Experimental results indicate that ShortCircuit produces AIGs up to 18.62% smaller than the state-of-the-art ABC synthesis tool and achieves good success rates on randomly sampled AIG test sets from EPFL benchmarks.

### Strengths
1. The model leverages transformer-based architecture for stepwise AIG generation. It models structure in Boolean logic through self-attention. This approach reduces the combinatorial explosion by focusing only on the relevant states for each one additional of AND gate.

2. It combines supervised pre-training with reinforcement learning similar in Alphazero. It prunes the search space and achieves near optimal circuit sizes. This two-phase training approach is suitable for the high-dimensional and sparse state space of AIG synthesis.

3. ShortCircuit achieves a circuit size reduction of 18.62% over the ABC synthesis tool, a significant improvement in AIG synthesis. Its reinforcement learning mechanism contributes to generating smaller circuits with high accuracy.

### Weaknesses
1. It is unclear that how well ShortCircuit scales to AIGs with more complex logic structures or significantly more inputs. The paper only demonstrate mid-size circuits (8-input circuit). As circuit size grows, the computational complexity grows exponentially, and could limit the model’s effectiveness. 
2. Only the EPFL benchmark is used, more dataset (such as OpenABC-D Dataset) with diverse circuits should be added in the evaluation.

minor
1. a space after "model" in line 022
2. Line 085: our model architecture "in section" 4

### Questions
1. How does ShortCircuit handle scaling for truth tables with more than 8 inputs, and are there planned optimizations to extend the model's capacity for larger circuits?

2. What are the specific implications for shortcircuit's performance if it were tested on actual hardware? How would the model account for memory constraints or latency issues on FPGA or ASIC platforms?

3. Is there possibility for ShortCircuit to incorporate other graph structures or non-AND gates in its synthesis process, and how would this impact model accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an ML method to generate and-invert graphs (AIG) from truth tables. The goal of the method is to minnimize the number of nodes which is a proxy circuit complexity. The generation of the AIG is modeled as a sequential autoregressive inference step and a transformer-based model (LLAMA inspired) is proposed.   Results show that the number of nodes of the generated AIGs is competitive with optimized logic synthesis scripts for small combinational logic functions (8 inputs).

### Strengths
The paper addresses a hot problem, i.e. the synthesis of digital circuits using ML methods - the problem statement and assumptions are clearly stated. 
The formulation of the ML model and how it i used in inference to generate the candidate AIGs from truth tables is also clearly explained. 
The idea of formulating the graph construction as an autoregressive inference is interesting
Results are presented in an understandable way, including the generation of training data

### Weaknesses
Results are weak. even though the authors claim 18% with respect to a baseline, the baseline is trivial, in fact the improvements with respect to the  optimized flow in ABC do not show any significant improvement over the optimized generation of AIGs with classical methods (resyn2)

While this is not necessarily bad, there are two other major issues:
1. resyn does not need any training, it is a constructive algorithmic method, and by nature it does not require extensive data collection
2. resyn also scales to much larger number of inputs and outputs, while the scalability of the proposed method is not assessed. 

So we can state that the proposed method does not represent an improvement over "classical" non-ML based SoA. 

Moreover since the same data corpus is used for training and test (of couse different samples of trees), there is danger of lack of domain diversity, and it's not clear on how this method will fare if the test set is completely un.correlated from the training set.

### Questions
1. comment on the scalability of the method to larger functions are needed
2. how is boolean matching of the generated AIG with the targeted function guaranteed? You have not 100% matching rate, so are you  ensuring that th AIGs you chose to report results in the comparisons are actually correct AIG from the boolean matching viewpoint?
3. how would you apply this method on practical combinational circuits with many more inputs and outputs than 8-1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces ShortCircuit, a novel transformer-based framework that employs reinforcement learning to generate optimized AND-Inverter Graphs (AIGs) from truth table inputs. According to the experimental results, ShortCircuit outperforms traditional synthesis tools, such as ABC, and other learning-based approaches in terms of circuit size reduction.

### Strengths
1.ShortCircuit provides an effective solution for generating optimized AIGs based on truth tables and addressing exact synthesis task. 
2.This paper is commendably clear in its motivation and methodology.

### Weaknesses
1.The improvement is not significant. ShortCircuit only further reduce 0.26% AIG nodes than ABC+resyn2. 
2.The experimental setup is not sufficiently convincing. First, while ABC is a well-known logic synthesis tool, it is not the SOTA method for exact synthesis and resyn2 is only a preset logic synthesis flow. Comparison with more recent exact synthesis methods would be better. Second, the learning-based method Boolformer is not a suitable comparison since it performs significantly worse than ABC, as shown in Figure 4(b). How does ShortCircuit compare to Circuit Transformer, which the authors mention in the related work?
3.While ShortCircuit performs well with 8-input truth tables, the paper does not discuss in detail how the approach scale with more inputs.

### Questions
1.How could ShortCircuit adapt to handle circuits with K-inputs, where K is not 8? Should we need to retrain the model with K-cut circuits? What is the scalability if K is much greater than 8. 
2.The targeting task is similar as IWLS contest 2023, which synthesizes minimal AIGs based on the given truth tables. While the contest benchmark has very large truth table size than 8, could ShortCircuit handle such benchmark effectively?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces ShortCircuit, a novel transformer-based architecture for generating digital circuits from functional descriptions. The authors address the task of synthesizing optimal AND-Inverter Graphs (AIGs) from truth tables, a critical step in chip design. ShortCircuit employs a two-phase process, combining supervised and reinforcement learning, to achieve this goal. The model is first pre-trained using a dataset of AIGs extracted from real-world circuits. It is then fine-tuned using an AlphaZero-inspired approach to navigate the vast search space and discover compact AIG designs. Experimental results demonstrate that ShortCircuit outperforms traditional logic synthesis tools and other learned methods in terms of AIG size, achieving a significant reduction in the number of AND gates required.

### Strengths
1. The paper introduces a new transformer-based model specifically designed for AIG generation, effectively capturing the structural properties of AIGs. The authors chose to represent AIG nodes as truth tables, which allows the model to learn the relationships between nodes and their functions more effectively. Additionally, the use of positional encodings to distinguish between built nodes and the target truth table enables the model to focus on the relevant information during each step of the generation process.    
2. The two-step training process, combining supervised and reinforcement learning, is well-motivated and addresses the challenges of reward sparsity and large state space. The supervised pre-training step provides the model with a good starting point by learning from a large dataset of AIGs. The subsequent AlphaZero-inspired fine-tuning phase allows the model to explore the search space more effectively and discover compact AIG designs that would be difficult to find using traditional methods.
3. ShortCircuit demonstrates a significant improvement over state-of-the-art logic synthesis tools, producing smaller AIGs for a set of real-world benchmark circuits. The authors show that ShortCircuit can generate AIGs that are up to 18.62% smaller than those produced by ABC, a widely used logic synthesis tool. This reduction in AIG size can lead to significant improvements in chip design.

### Weaknesses
1. The AlphaZero-based fine-tuning can be computationally expensive, potentially limiting its applicability in resource-constrained settings. The authors used 8 MCTS simulations before each action in their experiments, which can be time-consuming for larger AIGs. While they show that reducing the number of simulations can improve runtime while maintaining reasonable performance, this trade-off may not be acceptable for all applications.

2. While the results are promising for 8-input truth tables, the scalability to larger truth tables, commonly encountered in complex chip designs, needs further investigation. The authors acknowledge that the computational cost of their approach can be high, especially for larger AIGs. Future work could explore ways to improve the scalability of ShortCircuit, such as developing more efficient search algorithms or using distributed training techniques.    

3. Lack of Ablation Study. A more detailed ablation study would be beneficial to understand the individual contributions of different components of the proposed architecture and training process. For example, the authors could investigate the impact of different positional encoding schemes, the number of transformer layers, or the choice of activation functions. This would provide valuable insights into the design of ShortCircuit and guide future research in this area.

4. Limited Comparison with Other Learned Methods. The paper primarily compares ShortCircuit with traditional logic synthesis tools and only briefly mentions Boolformer, another learned method. A more comprehensive comparison with other recent deep learning approaches for circuit design would provide a better understanding of ShortCircuit's strengths and weaknesses.

### Questions
1. The format of citations are not unified, e.g., the third paragraph of the first section.
2. Could the authors compare the computation cost of different methods?
3. A more in-depth discussion on the generalization ability of ShortCircuit to unseen truth tables and different types of circuits would strengthen the paper.   
4. Investigating alternative reward functions in the reinforcement learning phase could potentially lead to further improvements in AIG quality.

### Soundness
2

### Presentation
3

### Contribution
2
