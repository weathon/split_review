# ITPNet: Towards Instantaneous Trajectory Prediction for Autonomous Driving

- Decision: Reject
- Scores: 5, 6, 8, 8

## Abstract
Trajectory prediction of moving traffic agents is crucial for the safety of autonomous vehicles, whereas previous approaches usually rely on sufficiently long-tracked locations (e.g., 2 seconds) to predict the future locations of the agents. However, in many real-world scenarios, it is not realistic to collect adequate observations for moving agents, leading to the collapse of most prediction models. For instance, when a moving car suddenly appears and is very close to an autonomous vehicle because of the obstruction, it is quite necessary for the autonomous vehicle to quickly and accurately predict the trajectories of the car with limited tracked trajectories.  In light of this, we focus on investigating the task of instantaneous trajectory prediction, i.e., two tracked locations are available during inference. To this end, we put forward a general and plug-and-play instantaneous trajectory prediction approach, called ITPNet. At its heart, we propose a backward forecasting mechanism to reversely predict the latent feature representations of unobserved historical trajectories of the agent based on its two observed locations and then leverage them as complementary information for future trajectory prediction. Moreover, due to the inevitable existence of noise and redundancy in the predicted latent feature representations and the difficulty of automatically determining the optimal length of unobserved trajectories, we further devise a Noise Redundancy Reduction Former (NRRFormer) module, which attempts to filter out noise and redundancy from a longer sequence of unobserved trajectories and integrate the filtered features and the observed features into a compact query representation for future trajectory predictions. In essence, ITPNet can be naturally compatible with existing trajectory prediction models, enabling them to gracefully handle the case of instantaneous trajectory prediction. Extensive experiments on the Argoverse and nuScenes datasets demonstrate that ITPNet outperforms the baselines by a large margin and shows its efficacy with different trajectory prediction models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work aims to solve the task where the observation is two points for motion prediction. They proposes to first reconstruct the unobserved longer history feature and then use them to update agent vector by attention. It could bring performance gains for existing works.

### Strengths
1.  According to the experiments, it indeed improves performance in this specific task.

2. It is plug-and-play for any trajectory prediction model, which could be useful.

### Weaknesses
1. The baselines is too old. Though LaneGCN and HiVT are both classic works, they are far from state-of-art-performace. Open sourced works like QCNet, MTR might worth trying.

2. Limited usage. The instantaneous trajectory prediction is interesting. However, the proposed method brings lots of extra parameters and computations.  Let's discuss an actual deployment problem: I observe that even ITPNet+HiVT < HiVT with 2s inputs and during your training, all parameters of HiVT are tuned without freezing. Thus, during actual deployment , the system should run an extra inference of the ITPNet+HiVT for those instantaneous objects while running the original HiVT for all the other fully observed agents. I am not sure whether worth it to double the inference for those instantaneous objects.

3. Some experiments and ablations are unclear, which seems that the work is incomplete and the working part is unclear. See question section.

4. The NRRFormer and backward forecasting steps N=10 seems harmful for the best mode (K=1).

5. The contrastive loss seems have little influence. The authors might consider multiple tries.

### Questions
1. **One interesting perspective is that: the proposed method might benefit from the extra training signals of the task of predicting history instead of only future,  which could better utilize data like in Forcase-MAE [1].**  How would the authors think about it?

2. Why only single-mode forcasting for history instead of multi-mode like for future prediction?

3. Did you compare the results of predicting waypoints and predicting features?

4. The NRRFormer and backward forecasting  steps N=10 seems harmful for the best mode (K=1).

5. The contrastive loss seems have little influence. The authors might consider multiple tries.

[1] Forecast-MAE: Self-supervised Pre-training for Motion Forecasting with Masked Autoencoders. ICCV 23.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the task of trajectory prediction for autonomous driving when limited prior observations are given (such as when a newly tracked exo-vehicle appears from an obstruction). They note and experimentally show that existing methods – which typically assume a lengthy observations history (such as 2s or 20 discrete timesteps) - are ill-suited for this task (Figure 1). The authors show that this trend persists when the model is trained with few or many prior observation timesteps.

To ameliorate performance, they propose two adjustments (summarized in Figure 2) when forming the latent state to be used for downstream trajectory prediction: 

1) They reconstruct previous timestep latent states corresponding to unobserved poses through a backward forecasting loss (section 3.3, equation 2). An additional loss term is also introduced encourage variability between latent states of different timesteps (equation 7). 

2) They propose a self-attention module to limit redundancy and noise in the latent state representation dubbed NRRFormer (section 3.4)

The final latent state representation from their network is then input into a downstream trajectory prediction module (HiVT or LaneGCN).

Their approach is validated in trajectory prediction using the Argoverse and NuScene datasets using only 2 prior observations (section 4). They find improved ADE performance compared to baselines (section 4.4, Table 1). An ablation study is included in Table 2 assessing the effects of the proposed adjustments. 

They further assess the effect of changing the number (N) of predicted unobserved prior poses (Table 3) where they find that performance gradually increases with N before dropping which they assert is caused by the introduction of noise and redundancy. Although they find that their NRRFormer potentially eliminates this issue.

Finally, they visually inspect the predicted trajectories (Figure 4) and find their approach to yield more diverse and accurate trajectories compared to baselines.

### Strengths
-	Tackles important research area (trajectory prediction under limit prior observations) often overlooked.
-	State-of-the-art performance.
-	Ablation study included.
-	Well written and easy to understand.

### Weaknesses
 - The addition of the cts loss and NRRFormer in abalation study results (Table 2) appear to have very small / questionable performance gains. Given the small change, can the authors speak to the consistency of these results? Given the small change, were multiple network seeds or trials done and do the same improvements remain? I would have found it useful to report a confidence interval or variance over the results although perhaps it is not conventional in this area. 

- It would have insightful to report how the NRRFormer affects performance for smaller values of N in Table 3. As it currently is, section 4.4 “Analysis of Different Lengths $N$” seems somewhat rushed with mentions of how the usage of the NRRFormer was done “without tuning it carefully”.

- It would be useful to show how the method’s performance changes for different number of prior observed locations (T) since only 2 prior observations are considered in this work (Table 4). During practical usage, I would assume that we would want to use all available prior observed locations for future trajectory prediction and so the T value will change. The authors have shown that their method outperforms baselines at T=2 prior observations, but does this trend continue for higher values of T? Does the method improve performance at all values of T versus baselines or is there a point where it is a detriment. For example, given a test trajectory with T=10 prior observations, do we trust the author’s method over baselines? 

- Although not needed at test time, the method requires ground-truth positions of unobserved states for the backward forecasting reconstruction loss during training. Depending on the dataset collection procedure, these may be hard to obtain. Furthermore – from what I understand – the HiVT and LaneGCN baselines in Table 1 are only trained with 2 observed prior locations and so it could be argued that the proposed approach requires more labeled data (predicts additional timesteps of prior locations which requires ground-truth labels). Although, at least for the HiVT method, the authors assert that training on all historic prior locations actually decreases performance (Figure 1) and so the second part of this criticism may be a moot. Nonetheless, I wonder if the additional labeled data could be used by the baselines in some other way (for example, training with variable length sequences).

- The approach assumes given 2d locations as prior observations instead of raw sensory input. For the problem cases that this work attempts to address (example: vehicle suddenly emerging behind obstruction), I would wonder how accurate these 2d locations may be given limited tracking timesteps. Noisy or inaccurate initial 2d poses may have negative downstream consequences when input into the authors’ method and thus reduce the reported performance gains that they assert in their results. From what I understand, the authors simply truncated longer fully observed trajectories to 2 observations and so the unique circumstances of the previous problem case may be ignored.

__Minor wording corrections to improve the final version (no effect on score):__

- On page 2, the usage of “straightly” in “Let’s consider a scenario where a vehicle travels straightly …” is awkward. Perhaps simply replace with the word “straight”.

### Questions
-	Did the authors try reconstructing raw 2d positions instead of their corresponding latent states (equation 2). Can they speak as to why one was done over the other?
-	The addition of the cts loss and NRRFormer in abalation study results (Table 2) appear to have very small / questionable performance gains. Given the small change, can the authors speak to the consistency of these results? Given the small change, were multiple network seeds or trials done and do the same improvements remain? I would have found it useful to report a confidence interval or variance over the results although perhaps it is not conventional in this area. 
-	Is the margin parameter $\delta$ in equation 7 output by the network or a set hyper-parameter?
-	Can the authors clarify with how many prior observations the baselines were trained with in Table 1? Matching the results with Table 4 in the appendix, it appears to be 2, but I would appreciate if this was clarified.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a plug-and-play approach for instantaneous trajectory prediction when there are only two observations. 
The proposed ITPNet considers the lack of information as the reason for poor prediction when there are few observations, and uses backwardly prediction to predict unobserved representation as complementary information. 
The authors discovered that as this additional information increases, the amount of information increases, but the quality deteriorates. 
Therefore, they proposed an NRRFormer that can filter this. 
The proposed method significantly improved the prediction performance when added to the existing prediction model.

### Strengths
* This paper deals with a practical problem of instantaneous trajectory prediction. The idea of using backwardly prediction and using it as complementary information proposed by the authors is novel. They also showed experimentally that as the amount of predicted complementary information increases, noise and redundancy increase, and it makes sense to adequately propose a module, NRRFormer to overcome this.

* The effectiveness of the proposed method was verified in two famous datasets and two prediction models. It also showed superior prediction performance compared to MOE and Distill, which dealt with the same topic.

* The paper is well-organized and easy to read. And the authors’ claim is somewhat well supported by experimental evidence.

### Weaknesses
Some details are missing. 
* Why does $\hat{v}^{unobs}_1$ become mean of $V^{obs}$ on page 5? Is this mean for i=1,2 and all agents? It is unclear how the mean is calculated and if it is a global mean across all agents and time steps or a per-agent mean.
* There seems to be a lack of analysis on why cts loss enables better reconstruction on the last line of page 5. Personally, I think that if only recon loss is used, the network may fall into a trivial solution that creates the same unobserved representation regardless of time step and agent, and cts loss prevents this. I’m curious about the authors’ thoughts on this, and I think it would be good to add it to the manuscript. The role of the continuous loss is not clearly explained, and it is not clear why it would prevent a trivial solution, especially given the use of ground truth unobserved features as supervision. A more detailed explanation of the loss function and its impact on the learned representations is needed.
* In the main result of Table 1, how was the baseline model (LaneGCN, HiVT) trained? The nuScenes and Argoverse prediction data already include data with short observation lengths. When training the baseline model, did you filter out data with full length for training, or did you filter out data with only 2 observations for use, or did you use all data? The training procedure for the baseline models needs to be clarified, specifically how the variable observation lengths in the datasets are handled during training. It is important to know if the baseline models were trained with the same data as the proposed method to ensure a fair comparison.

### Questions
* In comparison experiments with MOE or Distill, they do not seem to use HiVT or LaneGCN as backbone. But isn’t MOE or Distill also plug-and-play? For example, Distill still seems to be able to applied on HiVT or LaneGCN while maintaining the encoder and decoder structure and doing knowledge distillation. It seems fair to compare with MOE or Distill using same backbones (HiVT and LaneGCN).
This may be the critical part for the fairness of the main experimental result, so if this is clarified, I think i can keep my rating more confidently.
* Trajectory prediction generally predicts multiple futures, not one future. The proposed backwardly prediction seems to predict only one past, but have you ever experimented when predicting multiple pasts?"

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors identified an important limitation of the traditional trajectory prediction approaches that they require 2 seconds of observations to make accurate predictions. They took the HiVT model as an example, and its prediction performance drops significantly when only two observations are available. However, for an autonomous driving vehicle to safely operate, a trajectory prediction model needs to be able to make accurate predictions for an agent before it has been observed for 2 seconds.

To tackle this limitation, the authors proposed an instantaneous trajectory prediction approach, called ITPNet. ITPNet is able to make predictions with only two observations.

The key idea of ITPNet is to use a backward forecasting module to reconstruct the unobserved latent feature representations of the agent using the two observed ones.

The authors also proposed a Noise Redundancy Reduction Former (NRRFormer) module to filter the reconstructed unobserved features.

ITPNet is a generic plug-and-play approach that can be used in combination with any trajectory prediction backbones. In this paper, the authors applied ITPNet on HiVT and LaneGCN backbones. They evaluated the resulting ITPNet+HiVT and ITPNet+LaneGCN models on the Argoverse and nuScenes datasets. The evaluation results show that, when using two observations, ITPNet significantly improves the prediction performance over the HiVT and LaneGCN baselines.

The authors also performed ablation studies to evaluate the contributions from the reconstruction loss and NRRFormer.

### Strengths
* I like the motivation of this paper. It attempts to tackle an important limitation of the traditional trajectory prediction approaches.

* ITPNet is a generic plug-and-play approach that can be used in combination with any trajectory prediction backbones. The authors applied applied ITPNet on two popular open-sourced backbones, HiVT and LaneGCN. This makes it a lot easier for other people to adopt this work.

* The result shows ITPNet significantly improves the prediction performance over the HiVT and LaneGCN baselines when using two observations.

* From author's response during the rebuttal, I now understand that the model is able to make predictions using all the available observed history, which makes it a practical solution for a real-world autonomous driving system.

### Weaknesses
 * From the method and evaluation sections of the paper, it's not very clear whether this method is able to make predictions using all the available observed history. In the method section, it will be useful to clarify this and explain how this method is able to do so. In the evaluation section, it will be useful to make a curve plot to compare the prediction performances when different lengths of observed history are available. To match a real-world deployed prediction system, you should only have one ITPNet+HiVT model and do predictions with different lengths of available history. It will also be useful to make a curve for the HiVT baseline model as well.

* The ablation study result was incomplete in the original submission, but I am good with the additional results provided in the rebuttal.

* From Table 2, NRRFormer barely provides any performance boost.

### Questions
* Is ITPNet able to able to adaptively adjust the length of history used for different agents?

* Will N=3 with NRRFormer enabled yield better result?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
