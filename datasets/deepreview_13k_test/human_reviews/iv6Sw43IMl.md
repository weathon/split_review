# Parameter Monte Carlo Tree Search: Efficient Chip Placement via Transfer Learning

- Decision: Reject
- Scores: 3, 3, 3, 3, 3

## Abstract
Automated chip placement is an important problem in enhancing the design and effectiveness of computer chips. Previous approaches have employed transfer learning to adapt knowledge obtained via machine learning from one chip placement task to another. However, these approaches have not notably reduced the necessary chip design time, which is crucial for minimizing the total resource utilization. This paper introduces a novel transfer learning approach called Parameter Monte Carlo Tree Search (PMCTS) that utilizes MCTS to transfer the learned knowledge from deep reinforcement learning (RL) models trained on one chip design task to another chip design by searching directly over the model parameters to generate models for efficient chip placement. We employ MCTS to escape the local optima reached by training from scratch and fine-tuning methods. We evaluate our methodology on four chip design tasks from the literature: Ariane, Ariane133, IBM01, and IBM02. Through extensive experiments, we find that our approach can generate models for optimized chip placement in less time than training from scratch and fine-tuning methods when transferring knowledge from complex chip designs to simpler ones.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new MCTS-based algorithm for parameter search in transfer learning. The proposed algorithm is used in the chip placement task, where a RL model is trained on a source chip circuit and then transfered to a new one. The results show that the proposed method can shorten the time needed in the transfering stage, compared with directly fine-tuning.

### Strengths
This paper identifies that transfer learning is an important task in chip placement, and proposes a MCTS-based transfer learning approach. The results on several chip circuits show that the proposed transfer learning approach is faster than fine-tuning approach.

### Weaknesses
1. The proposed PMCTS method is designed for general transfer learning task, rether than specifically designed for the chip placement task. If the authors claim that the core contribution of the paper is this general algorithm, they may need to evaluate the algorithm on general transfer learning tasks, rather than only considering chip placement.
1. The authors mainly compare the proposed method with directly fine-tuning. However, other transfer learning method should also be compared with.
1. The performance improvement is not significant. Moreover, since fine-tuning method may outperform transfer learning in a longer time, the authors may want to further extend the training time to see whether transfer learning approach still demonstrates a better performance after converggence.
1. Only limited models and datasets are used for evaluation. For example, ChiPFormer, a pretraining approach, is not considered for comparision.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a prior search-based transfer learning method for chip placement, in which pre-trained network parameters are updated via Monte Carlo Tree Search (MCTS). The proposed method enables cost-effective adaptation for chip placement. The authors validated the method on four different problems, comparing it to the full-training and fine-tuning approaches.

### Strengths
1. The proposed method directly updates network parameters through search, achieving improved time-performance.

2. The paper clearly showed the related works and explained their differences and limitations.

### Weaknesses
1. Lack of Background Information: There is insufficient background information regarding the objective of the target task. While the method aims to transfer knowledge from complex chip design tasks to simpler ones, it is unclear how practical this approach is given the increasing complexity of chip design, with more design components and constraints.

2. Limited Performance in Simple-to-Complex Transfer Learning: The performance of the method in transferring from simple to complex tasks is not promising. According to Line 341, "both from-scratch and fine-tuning approaches would eventually outperform the PMCTS models," indicating only a fast initial improvement. Additionally, Figures 1 and 2 suggest that the model may not be learning effectively, as costs do not consistently decrease. In Figure 2, the proposed method even concludes with a higher cost than its starting point.

3. Lack of Ablation Studies: The paper lacks ablation studies, particularly regarding the search method for parameter updates and the selection of hyperparameters.

4. Unclear Tables and Figures: The tables lack informativeness, and the figures are difficult to interpret. Adjusting the label sizes on figures would improve readability. Additionally, adding a column to the tables showing the time cost for each method would allow a clearer evaluation of time-performance across methods.

### Questions
1. Could you conduct an ablation study on the percentage of selecting the best-performing child node versus selecting a less-explored node, and report its effect on performance?

2. Is this method applicable to other domains?

### Soundness
2

### Presentation
1

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
This paper presents a transfer learning approach known as Parameter Monte Carlo Tree Search (PMCTS), aimed at optimizing model parameters for chip placement, thereby enhancing efficiency and reducing time. PMCTS exhibits superior performance and faster optimization compared to both training from scratch and fine-tuning methods. Experimental results across various chip design tasks indicate that the approach significantly enhances design efficiency, especially in situations involving knowledge transfer from complex to simpler designs.

### Strengths
The idea of transferring knowledge through MCTS in chip design is good.

The proposed approach demonstrates better performance than fine-tuning and training from scratch, which makes sense to me.

### Weaknesses
The quality of the figures is very poor. Please increase the font size and reduce the size of the figures.

The types of chips tested in the experiments are very limited. It is recommended to evaluate the results on popular benchmarks such as ISPD2005 and ICCAD2015.

The number of baseline methods for comparison is too few to assess the performance of this approach in the current chip placement domain.

Please check and revise the formatting of the references.

### Questions
None.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method to finetune a pretrained policy on chip designs to new tasks by employing MCTS on policy parameters. By perturbing certain layers with operators as addition and multiplication with random noise and applying MCTS, the resulting policy can be adapted faster when few time is allowed compared to from-scratch pretraining on finetuning. The proposed method shows promising results when adapting from complex to simpler problems while it underperforms classical finetuning when trying to generalize from simple to larger tasks.

### Strengths
The writing is clear, and several relevant related works are mentioned. The proposed method is simple enough to be adaptable to a wider range of tasks than just fine-tuning placement policies for chip design. Source code is provided, which is appreciated.

### Weaknesses
This paper raises several concerns in the current state.  

1. I believe the novelty is pretty limited. In my understanding, in terms of modeling, problem formulation, etc, the method is no different from Mirhoseini et al. (2020), for instance, Section 3.2 and 3.0.1.  The main contribution is the application of MCTS to the parameter search operators proposed in Singamsetti et al. (2021) and to chip design.I believe the proposed method could benefit from the further evaluation on different domains or other problems that involve finetuning in the same domain, as I do not see a lack of generality per se -- if the method is proven to work in other (toy) example problems, it would greatly strengthen the paper.
    
2. This is recognized by the authors -- the paper does not improve the performance against finetuning when generalizing from simple to complex designs. Although this is a weakness, I appreciate the authors in being straightforward.
    
3. The authors propose two search operators to randomly perturb model layers, i.e. adding and multiplying uniformly distributed noise. However, there is no ablation study about this or sufficient analysis on sensitivity to the operator choice.
    
4. I am not convinced by the performance shown in Figures 1 and 2. Namely, one would expect the performance to improve over time. However, it appears to me as if the performance is almost random (no clear trend over time). Moreover, performance actually gets much worse over time in terms of cost, as shown in Figure 2. How is this possible? Also - the authors should include zero-shot performance to Tables 1 to 4. Otherwise, it is hard to assess the improvement.

### Questions
1. When does finetuning become better than the proposed method? You mentioned ““We note that it is very likely, based on prior work, that both from scratch and fine-tuning approaches would eventually outperform the PMCTS models based on the results of prior work of Mirhoseini et al. (2020), but we are focused on speeding up the optimization process, thereby emphasizing this lower timeframe setting.”. I wonder what would be the convergence point in which finetuning is better.
    
2. Would it be possible to use PMCTS in combination with finetuning?
    
3. Which other tasks in the broader ML for optimization community could your method expand to?
    
4. What is the effect of search operators? I.e., if you just used the second one, would it perform as well?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a new transfer learning method in chip design called Parameter Monte Carlo Tree Search (PMCTS). It leverages Monte Carlo Tree Search (MCTS) to transfer knowledge from deep reinforcement learning (RL) models trained on one chip design task to another. By searching directly over the model parameters, it generates models for efficient chip placement.

### Strengths
1. Efficient chip placement can be achieved through transfer learning algorithms, and complex chip designs can be transferred to simpler chips.

2. The proposed PMCTS method has successful applications and outperforms other transfer learning methods across multiple chip designs tasks, but the paper does not seem ready for publication.

### Weaknesses
1. The paper lacks images to clearly illustrate the proposed method, making it difficult for readers to understand.

2. The paper lacks necessary ablation studies on the cost function, and it is important to discuss the impact of different weights $\gamma$ and $\beta$ on the results.

3. The paper does not provide a thorough discussion of the limitations of the proposed method.

4. The PPO used in the method lacks the introduction of necessary preliminaries for reinforcement learning, such as the definitions of MDP, state, and action.

5. Monte Carlo Tree Search requires significant computational resources. The authors mention the performance advantages compared to the baseline but do not address the issue of computational complexity. It is necessary to quantitatively compare the computational cost and GPU usage of the proposed method with the baseline.

6. The paper lacks necessary design illustrations, and they are not provided even in the appendix.

7. The authors need to provide more detailed information about the training process, such as the number and distribution characteristics of the training and test samples.

8. The authors did not provide the network architecture and training parameters. Presenting these in tables within the paper would allow readers to better understand the network's composition.

### Questions
Please check the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
