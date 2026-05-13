# SwapTransformer: Highway Overtaking Tactical Planner Model via Imitation Learning on OSHA Dataset

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
This paper investigates the high-level decision-making problem in highway scenarios regarding lane changing and over-taking other slower vehicles. In particular, this paper aims to improve the Travel Assist feature for automatic overtaking and lane changes on highways. About 9 million samples including lane images and other dynamic objects are collected in simulation. This data; Overtaking on Simulated HighwAys (OSHA) dataset is released to tackle this challenge. To solve this problem, an architecture called SwapTransformer is designed and implemented as an imitation learning approach on the OSHA dataset. Moreover, auxiliary tasks such as future points and car distance network predictions are proposed to aid the model in better understanding the surrounding environment. The performance of the proposed solution is compared with a multi-layer perceptron (MLP) and multi-head self-attention networks as baselines in a simulation environment. We also demonstrate the performance of the model with and without auxiliary tasks. All models are evaluated based on different metrics such as time to finish each lap, number of overtakes, and speed difference with speed limit. The evaluation shows that the SwapTransformer model outperforms other models in different traffic densities in the inference phase.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel time-series transformer architecture for the task of predicting lane change probabilities for overtaking exo vehicles. Their approach functions in the imitation learning context where a rule-based expert is used to generate training data of when the ego vehicle should switch lanes (section 2.2.2 and appendix A.3). They propose a swap operation transposing time and feature dimensions between encoder layers (section 3.1) and use auxiliary pose and vehicle distance metrics to improve training (section 3.2). The learner is integrated in a larger Travel Assist system (section 2.1) which controls the ego vehicle while their component only seems to deal with predicting lane change probabilities.

The authors evaluate their method in simulated highway traffic scenarios (section 4) where speed difference, time to finish and overtake ratio as used as metrics to compare against MLP and transformer baselines (Table 2).

The authors also describe the OSHA (Overtaking in Simulated HighwAys) dataset (section 2.3) which they plan to release.

### Strengths
- Novel architecture which appears to beat baselines (however I feel there is some approach issues, see weaknesses).
- The work is well written and clear.
- Included ablations are useful for analyzing the components of the proposed network.

### Weaknesses
 - There is no variance or confidence interval on the main results in Table 2 over repeated trials or different network seeds. Since some of the improvements are quite small compared to baselines (1-2%), it would be useful to know if the improvement is repeatable / consistent.
- I have some concerns on the training procedure: Was any form of validation set or early stopping used to help prevent overfitting and tune hyperparameters? Were multiple seeds used? The manuscript solely states that all models were trained for 300 epochs.
- I assume the Ours method in Table 2 is Transformer + Aux + Swap? Quite often is seems that the addition of the auxiliary loss or swap operation actually decreases performance but for some reason when combined together (ours approach) performance improves beyond the original transformer architecture. Can some intuition be given for this behavior?
- There does not appear to be any intuition as to why the swap operation would improve performance. This is further confusing by the fact that the transformer + swap architecture seems to harm performance versus the transformer architecture alone (Table 2).
- I feel that the evaluation metrics (speed difference, time to finish, overtake ratio) do not holistically evaluate the method. Although the proposed method finishes faster and overtakes more often is it possible that some of these were risky maneuvers (I.E. network predicted overtake when it shouldn’t of)? I think it would have been useful to show the model’s test prediction accuracy versus the expert to alleviate these concerns (I.E. is it switching lanes when it should be).
- Were the 50 test/evaluation episodes consistent across all models for fairness? I assume each was randomized but I would hope that the random conditions were repeated for all models.

### Questions
Questions are in part copied from the weaknesses section: 

- I have some concerns on the training procedure: Was any form of validation set or early stopping used to help prevent overfitting and tune hyperparameters? Were multiple seeds used? The manuscript solely states that all models were trained for 300 epochs.

- I assume the Ours method in Table 2 is Transformer + Aux + Swap? Quite often is seems that the addition of the auxiliary loss or swap operation actually decreases performance but for some reason when combined together (ours approach) performance improves beyond the original transformer architecture. Can some intuition be given for this behavior?

- I did not seem to find any intuition as to why the swap operation would improve performance. Can the authors clarify this point?

- Were the 50 test/evaluation episodes consistent across all models for fairness? I assume each was randomized but I would hope that the random conditions were repeated for all models.

- The description of the rule-based expert is somewhat ambiguous (appendix A.3) but can the authors clarify what advantages the learner has over this rule-based system? Does the rule-based system have additional ground-truth inputs that the learner does not possess during run-time or is the learner significantly faster?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper imitation learning as a planning approach for highway autonomy, focusing specifically on overtake and lane change maneuvers. 

The first contribution is a custom synthetic dataset for the task, generated in a Unity-based simulation environment. The second contribution is the formulation of the problem: instead of tackling this problem as a motion planning or trajectory forecasting challenge, it is assumed that a controller exists for ego which can perform lane keeping, adaptive cruise control, and controlled lane changes, and that the   task is to provide the controller with inputs indicating when to perform lane changes and in which direction. The final contribution is a proposed model along with comparisons to a variety of baselines.

The dataset abstracts away the perception system, collecting lane segmentations and object lists from the environment. These inputs are passed through a CNN and transformer architecture with a few auxiliary tasks. The auxiliary tasks include ego trajectory prediction (represented as Bezier curve conrol points) and predicting the pairwise distances between all vehicles in the scene. The core task is predicting the lane change maneuver as well as future ego velocity five steps ahead.

The paper compares a variety of models. The proposed model, SwapTransformer, uses decomposed attention with transpose operations in between. The input object list is represented with two spatial dimensions, one for the input feature and one for time; alternating transformer encoders with self attention on either dimension resembles common approaches for handling 2D inputs (somewhat similar to e.g. Axial Attention, Salimans 2019, for example). The baselines are a transformer without auxiliary losses, a transformer with axis swapping, and a simple MLP baseline; the proposed model outperforms these baselines on a few metrics such as the speed prediction accuracy.

### Strengths
The dataset and formulation of the problem are fairly original in my experience. The complex problem of highway driving is broken down into a lower level controller ("Traffic Assist") with a few key capabilities and a decision-making layer, with the paper focused on the decision-making component. The dataset is generated in simulation specifically for this formulation of the problem. While less ambitious than approaches that tackle full imitation learning for the controller, this formulation is potentially simpler to deploy in a real-world system building upon existing driving assist capabilities.

Overall, the quality of the writing is high and the descriptions are clear, with the caveat that system rests on the Traffic Assist system, the implementation of which is not documented besides a high-level explanation of its inputs and outputs

### Weaknesses
The biggest weakness of this paper is the challenge of placing its results in a wider research context. While the description is clear and the technical work is sound, it reads like a technical report; by using a custom dataset with a custom problem and a custom model, it is impossible to compare this work to open source or publicly available baselines for the same problem.

At the same time, this paper cannot be described as a significant dataset contribution: the dataset is generated with complex rule-based and simulation setups, which may be challenging to reproduce and have limited applicability to other challenges or datasets.

Overall, the key change I would make to this paper would be to find a way to connect it to other publicly available systems or research. If the key contribution is meant to be the dataset, I would recommend evaluating other future forecasting and prediction models (e.g. Wayformer) on the dataset; if the key is the model, I would consider focusing on public future forecasting benchmarks. If the main contribution is meant to be the problem decomposition, I would compare an end-to-end trajectory forecasting system with this proposed Traffic Assist-based decomposed model. Without these sort of connections to existing literature, it will be challenging for the community to derive value from this work.

### Questions
One question I would like to understand in more detail is if there is prior work on the Traffic Assist system in this paper, and if so, if there are any public benchmarks that could be added to this paper.

Another question is whether this system has been tested outside of simulation or deployed to real world systems. If so, reports on the results of this work would strengthen the work significantly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an ML planner approach to have the ego overtake other cars on highways.

The authors first collected a dataset through simulation. They used the SimPilot simulator and implemented a rule-based algorithm to have the ego overtake other agents. They used the rule-based driver as the ground truth expert.

The authors then designed a transformer-based architecture to make lane-change decisions. The inputs of the model are lane ID segmentation images and agent information. The main task of the model is to predict lane-change decisions and lane-change velocities. They also proposed two auxiliary tasks. One is to predict the ego vehicle's future positions, and the other one is to predict a distance matrix between all agents.

The model uses ResNet-18 to encode the lane ID image and uses an attention-based module to process agent information.

The authors evaluated the proposed model in the simulation environment. They compared against the following baseline methods: MLP only, transformer only, transformer + auxiliary tasks, and SwapTransformer. The result shows that the proposed model has the best performance in terms of speed difference, time to finish, and overtake ratio.

### Strengths
* The paper presents a good ML model architecture to make lane-change decisions.

* The proposed method has better performance than the baselines.

* Both the data and code will be released.

### Weaknesses
 * The baselines used in this paper are all variants of the author's own methods. There are no comparisons against other state-of-the-art methods. Specifically, the baselines lack diversity in terms of model architecture and training methodology. For example, the authors could have included a comparison against a learning-based planner that uses a different approach, such as a reinforcement learning-based method or a graph-based planner. This would help to better understand the strengths and weaknesses of the proposed method.

* The authors generated the ground truth with a rule-based driver. Does it mean the proposed method can only do as well as the rule-based method? What are the advantages of the proposed method over the rule-based method? It's unclear if the proposed method can generalize beyond the specific behaviors exhibited by the rule-based driver. The paper should include an analysis of the limitations of the rule-based driver and how the proposed method addresses these limitations.

### Questions
* The proposed method can only do as well as the rule-based method. What are the advantages of the proposed method over the rule-based method?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
