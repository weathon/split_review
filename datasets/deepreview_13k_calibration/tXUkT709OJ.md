# COFlowNet: Conservative Constraints on Flows Enable High-Quality Candidate Generation

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Generative flow networks (GFlowNet) have been considered as powerful tools for generating candidates with desired properties. Given that evaluating the property of candidates can be complex and time-consuming, existing GFlowNets train proxy models for efficient online evaluation. However, the performance of proxy models is heavily dependent on the amount of data and is of considerable uncertainty. Therefore, it is of great interest that how to develop an offline GFlowNet that does not rely on online evaluation. Under offline setting, the limited data results in insufficient exploration of state space. The insufficient exploration means that offline GFlowNets can hardly generate satisfying candidates out of the distribution of training data. Therefore, it is critical to restrict the offline model to act in the distribution of training data. The distinctive training goal of GFlownets poses a unique challenge for making such restrictions. Tackling the challenge, we propose Conservative Offline GFlowNet (COFlowNet) in this paper. We define unsupported flow, edges containing unseen states in training data. Models can learn extremely few knowledge about unsupported flow from training data. By constraining the model from exploring unsupported flows, we restrict COFlowNet to explore as optimal trajectories on the training set as possible, thus generating better candidates. In order to improve the diversity of candidates, we further introduce a quantile version of unsupported flow restriction. Experimental result on several widely-used datasets validates the effectiveness of COFlowNet in generating high-scored and diverse candidates. All implementations are available at https://anonymous.4open.science/r/COFlowNet-2872.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the generation task, which aims to search for state transitions with high rewards. The fundamental task strongly impacts generating or searching for plausible candidates of sequences, where its possible applications include molecule design or path generation.
To this end, the authors have proposed COFlowNet, which focuses on finding high-reward state transitions by simply regularizing unsupported flows. The efficacy of the method is confirmed in Hypergrid and Molecule Design tasks.

### Strengths
**Strength 1:** The main strength of this work is the broad impact on any candidate-generation tasks.
- I feel that the method can be applied to any candidate-generation task, such as molecule design. Also, as pointed out in the paper, flow generation can be further used to search plausible flows to find the optimal decision-making in the RL study.

### Weaknesses
 **Weakness 1:** The comparison with prior works and the evaluations seem limited.
- By referring the baseline paper of GFlowNet, it is compared with other non-flow-based approaches such as MCMC (MARS) and PPO. However, COFlowNet is only compared with GFlowNet, which makes it hard to figure out the quantitative gains of COFlowNet over MCMC and PPO. It is better to add these two baselines in the experiments. Specifically, the performance of COFlowNet should be directly compared to MCMC and PPO using the same evaluation metrics, such as average top-k rewards and diversity metrics. This would provide a more comprehensive understanding of the method's strengths and weaknesses relative to established baselines.
- Moreover, only the main experiment considered in this paper, which includes the comparisons with others, is Molecule Design. (I have not published works for this topic) In literature, is there any other task to demonstrate the efficiency of the proposed method? A single demonstration seems to be limited to say the consistent and meaningful gains of COFlowNet over others. The evaluation should include a broader range of tasks, especially those where GFlowNets have been previously applied, to demonstrate the general applicability of the method. For example, tasks involving combinatorial optimization or sequence generation could be considered.

**Minor Comment 1:** For consistency, please choose the one among COFlowNet or COFlownet.

### Questions
**Questions 1:** Regarding the weakness in literature, is there any other task to demonstrate the efficiency of the proposed method? If so, it would be much better to add one or two more results of COFlowNet.

### Soundness
4

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
4

### Summary
The paper present a method to the problem of offline GFlowNet training. Many conventional approaches require approximating training scores/rewards of candidate model outputs to provide a variety of generated candidate solutions, however, this approach is sensitive to out-of-distribution data. In this work the authors remove any reliance on proxy models for estimating the candidate to reward optimization objective for GFlowNet training. The authors propose to constrain the actions that a GFlowNet model may take to generate an output sample such that only actions supported by the training data are permissible. The authors show that their flow regularization only positively affects training on the supported flow paths, and that their approach is truly offline and can improve candidate model diversity.

### Strengths
The authors demonstrate originality in their work by clearly outlining their research problems in the context of other popular works and systematically laying out solutions for them with corresponding theorems and proofs. While maintaining an easy-to-read and high-level dialogue in addressing their approach’s significance, aim, and scope, the authors also manage to spare no mathematical details when necessary. Theorem 1 and the writing in sections 3.3 and 4 show formally the details required to both implement and understand the proposed approach.

### Weaknesses
In theorem 2, the use of the phrase “be more close to policy of offline dataset” seems too imprecise to be in the theorem statement. Since the proof is rather short this could perhaps be moved to the end of the proof, so that reader’s still get the high-level point that the author is trying to convey. Additionally, the conclusion of the proof for theorem 2 seems to be absent, although the technical/algebraic details seem sound. 

Although the authors effectively demonstrate the efficacy of COFlowNet on the Molecule Design problem, providing experimental results on datasets from other domains would help show the success of their method beyond a shadow of a doubt.

### Questions
1. No references are provided for vanilla GFlowNet and QM-GFlowNet. There is no justification that these are the state-of-the-art methods.
2. Although COFlowNet w/o shows that the regularization term enhances performance, but can not beat the competing method QM-GFlowNet. The experiment results are weak. If the experiment results can not be improved, please provide a more in-depth analysis of where COFlowNet falls short compared to QM-GFlowNet.
3. Are there other potential ways of increasing diversity during GFlowNet regularization that were explored aside from the quantile matching algorithm? 
4. Can COFlowNet be easily extended to other domains where RL is popular, like game playing and autonomous vehicle driving for example?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the author introduces COFlowNet, an offline Generative Flow Network (GFlowNet) designed to generate high-quality and diverse candidates without relying on online evaluations. The effectiveness of COFlowNet is validated through experiments on commonly used datasets.

### Strengths
+ Adapting GFlowNets for offline scenarios is a valuable idea.
+ The proposed method shows superiority over baseline models like QM-GFlowNet and FM-GFlowNet.

### Weaknesses
1. The authors conduct experiments on Hypergrid and molecule design tasks. Could the proposed method be generalized to more tasks and real applications? It is recommended to conduct experiments on additional tasks.

2. How much time and computational cost are saved by training in the offline setting? Could the authors compare the training cost between the proposed method and traditional methods?

3. It would be better to use \textbf{} for the first sentence in figure and table captions to indicate their targets clearly.

4. It would be  better to indicate the meaning of 'mixed', 'expert', and 'random' in Figure4.

5. Do number of modes and ℓ1 error are commonly used in evaluation of GFLowNets? Are there more metrics to measure the performance?

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3
