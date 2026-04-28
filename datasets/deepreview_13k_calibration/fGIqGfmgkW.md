# OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
Scaling inference-time computation is increasingly seen as the next frontier in scaling laws for large language models. Previous work in mathematics and coding has demonstrated the remarkable potential for inference-time scaling. During such scaling, fine-grained supervision through process-based reward models (PRMs) is essential for enhancement. However, exploration of inference-time scaling and PRMs in open-domain problems remains limited, where lacking exact answers and obtaining process supervision prove challenging. In this paper, we explore the construction of PRMs for open-domain tasks, specifically for instruction-following tasks. Utilizing existing outcome-based reward models (ORMs), we develop sentence-level preference trees based on the prefix similarity of parallel sampled candidates from datasets like UltraFeedback. This setup allows us to derive weak supervision for processes via back-propagation from outcome-level rewards. Subsequently, we integrate ORMs and PRMs under the same pairwise ranking objectives, resulting in our newly developed reward models, named OpenPRM. This approach significantly enhances the scalability of process-level supervision in open domains at minimal cost. We assess the performance of OpenPRM across various reward benchmarks, demonstrating its competitive edge over traditional ORMs in open domains and PRMs in specialized domains. Additionally, we investigate the scalability of inference-time computation for open-domain instructions. Our results highlight the limitations of ORMs’ scalability, while OpenPRM shows superior performance in scaled settings. Despite these advances, achieving  automatic fine-grained supervision for open-domain inference-time scaling remains a substantial challenge. We hope these findings will spur further development of process supervision reward models in open-domain scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents OpenPRM, a reward model designed to incorporate both outcome-based and process-based rewards. The authors leverage outcome-based reward models to generate sentence-level preference trees, subsequently backpropagating these outcome rewards to provide weak supervision for process rewards. By jointly training the model on both types of signals, OpenPRM achieves huge improvements over existing ORMs and PRMs. Additionally, the authors demonstrate that OpenPRM can be effectively used during inference to guide the decoding process, with model performance scaling positively with the number of samples.

### Strengths
This model could provide substantial value to the RLHF research community. Although similar ideas have been extensively explored in prior work, particularly in domains like math and coding that focus on reasoning, few of those works released their models and datasets. By extending to more open-domain tasks, this model could facilitate RLHF research beyond specialized tasks.

### Weaknesses
One minor weakness is the lack of novel technical contributions; however, given the value this model brings to the RLHF research community, this is not a major concern. A more significant weakness is the lack of detailed analysis of the experimental results. While the authors demonstrate that OpenPRM generally outperforms existing reward models, they do not provide a breakdown of the results. Specifically:
1. The improved outcome-level reward performance is not clearly attributed—it's uncertain whether the gains come from the method itself or simply from better data. The data used (including UF, HS2, and additional math/coding datasets) may be better than that used in FsFairx or internRM. It would be helpful to see a baseline where these models are fine-tuned on the same data but with only outcome-level supervision to isolate the impact of the method.
2. Although OpenPRM shows better results overall, its performance on Chat is consistently lower. An analysis explaining this discrepancy would strengthen the results.
3. Figure 3 highlights the scaling effect of BoN, but no analysis is provided on PBM, which would provide a more complete picture.

Additional minor issues include:
1. Figure 3 lacks clarity due to overlapping lines, making it difficult to interpret the results.
2. The authors might consider evaluating with the OffsetBias dataset, which could offer a more fine-grained assessment of bias in reward models.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors proposed a method to create tree-like process supervision data. Specifically, it samples a great amount of trajectories from a set of samplers (LLMs) and merged those with similar prefix (measured by edit distance) to construct a tree. They trained different PRMs using this data and conducted experiments of Best-of-N and beam-search. The PRM-assisted method performed better on some of the selected benchmarks.

### Strengths
1. Process supervision and PRM are very important topics in the field. Especially given the improving importance of LLM reasoning and the success of OpenAI o1 model. This is an emergent topic and an open-accessible dataset is valuable to academia.
2. The inference-time scaling experiment is very valuable. Experimenting with scaling law is always a very important thing in today's LLM research. Although it's often infeasible for most academic labs due to the resource constraints. I am very happy to see such analysis in the papers nowadays. The results are not very convincing though but experimenting it should be awarded with credits.

### Weaknesses
1. The biggest issue is the presentation of the paper. Seems many details are missing. For example: how the data merge exactly work. The paper only presented the general idea but I cannot find any detailed description, e.g., the edit distance threshold. Another example is table 2, I cannot find what metrics the table used. Is that per-step accuracy? If so, how could you evaluate PRMs using RewardBench (that's for ORM I remember?)
2. They are some potential errors in the review of previous method. For example, I don't think any of the reward models are trained with MSE loss. It doesn't make sense to train a reward model with 0~1 labels where the label represented a probability using MSE loss. This is not a regression problem. And the Step-DPO work didn't train a reward model at all I believe.

### Questions
You mentioned one of the motivation of the proposed method is to save compute. But I don't don't think there are compute difference for crafting a process supervision label. You still need to same amount of compute to sampling the trajectories. Please correct me if I didn't understand correctly here.

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
4

### Summary
This paper presents OpenPRM, a novel approach to developing process-based reward models (PRMs) for open-domain tasks like instruction following. The authors argue that while outcome-based reward models (ORMs) have shown success, their coarse-grained nature limits their effectiveness in supervising complex tasks. OpenPRM leverages existing ORMs and preference trees based on parallel sampled candidates to generate process-level rewards, leading to improved performance on various benchmarks. The paper also explores scaling inference-time compute in open-domain settings and finds OpenPRM superior to traditional ORMs in scaled settings. 

The fundamental of this paper is about the generation of PRM training data, and it is using the similar method as Math-Shepherd and OmegaPRM. The key innovation of the this paper lies in the idea of merging solutions from the same question into a tree structure based on the similarity of the steps. Given this method would greatly reduce of the cost of the tree, the write and the experiments are not discussed throughly.

### Strengths
1. The paper addresses a significant gap in the research by extending the application of PRMs from specialized domains like mathematics to open-domain tasks. The proposed preference tree construction using readily available ORMs is a creative and cost-effective solution to generate process-level supervision.
2. OpenPRM consistently outperforms existing ORMs on RewardBench, particularly in challenging tasks like Chat Hard and Reasoning. Furthermore, it surpasses specialized PRMs in open-domain benchmarks, highlighting its generalizability. OpenPRM also shows promising results in scaling inference-time compute, outperforming other models in best-of-N sampling.
3. The paper provides a detailed analysis of the limitations of ORMs in process-level supervision, highlighting the issue of cumulative error. The authors theoretically and empirically demonstrate how OpenPRM mitigates this problem by identifying key divergent steps in the process. The paper also addresses potential concerns like rationality of process aggregation and length bias, strengthening the validity of the proposed approach.

### Weaknesses
1. The tree building in OpenPRM is not convincing. The steps are separated by “.\n”, and the similarity of steps are based on the edit distance between them, and threshold is pre-defined 0.88. The solutions are sampled with temperature 0.5. This temperature may not be high enough to generate solutions that are diverse enough for the reward calculation. I interpret this temperature is needed to generate steps that similar enough to convert into tree, but it affects the diverse of the solution and the rewards may not be precise. And how this 0.88 threshold selected was not mentioned in the paper, and the affect of different thresholds is not discussed either. As the key innovation of this paper, this is not a solid foundation.
2. How the PRM is trained given the data collected was not discussed clearly in the paper. Some information about the mixture and hyper parameters are given, but how the data was structured into training examples, how the rewards are predicted during inference and how the rewards for steps are aggregated into final reward are not discussed. Without these information, it is hard to have a good picture of the PRM training and how to interpret the results presented in the paper.
3. Only one example was given in the Appendix, and it was not clear. I would be very interested to see an real example of how the original solutions are like and how the final tree built looks like.

### Questions
Questions would be around the points in Weaknesses section.

1. Why pick the temperature of 0.5 as most of the time, people would use high temperate to get diverse solutions.
2. How the threshold 0.88 for similarity is picked and how does it affect the data and final result?
3. How the training data is formatted and what loss was used? As there are different way of PRM training available, which one was used?
4. During the inference time, how the rewards for each step/solution is calculated and aggregated?
5. Can you give more detailed example of the solution and tree building as it is the core contribution of the paper?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a sentence-level process reward data collection method using Monte Carlo Tree Search (MCTS). The authors use outcome-based rewards and iteratively sample, segment outputs, aggregate at nodes, and apply back-propagation. Experimental results demonstrate that the collected process reward data effectively trains the process reward model.

### Strengths
Clear and well-structured writing makes the methodology easy to follow.
The method addresses the popular and relevant area of automatic process reward data collection.
Effective use of MCTS enhances the quality of data for training process reward models.

### Weaknesses
Compared to previous MCTS-based solutions for process reward models, the novelty of the data creation method is unclear. Further explanation from the authors on this point would be beneficial.

The authors conducted additional experiments to clarify the contributions of OpenPRM compared to MCTS. From the rebuttal results, it is evident that MCTS remains a strong baseline in terms of performance. While the authors claim that OpenPRM is 10x more efficient than MCTS, they also state that both methods can process 3.84M examples within 24 hours. This apparent contradiction requires further clarification from the authors. Overall, OpenPRM's novelty appears limited, positioning it as an incremental improvement.

### Questions
In Table 2, could the authors clarify how comparisons are made across different backbones and training data to ensure an "apple-to-apple" comparison?

Regarding Table 3, could the authors provide the results from the outcome reward model?

### Soundness
3

### Presentation
3

### Contribution
3
