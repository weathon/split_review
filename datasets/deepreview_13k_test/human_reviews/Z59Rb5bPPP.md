# Trajeglish: Traffic Modeling as Next-Token Prediction

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
A longstanding challenge for self-driving development is simulating dynamic driving scenarios seeded from recorded driving logs. 
In pursuit of this functionality, we apply tools from discrete sequence modeling to model how vehicles, pedestrians and cyclists interact in driving scenarios.
Using a simple data-driven tokenization scheme, we discretize trajectories to centimeter-level resolution using a small vocabulary. We then model the multi-agent sequence of discrete motion tokens with a GPT-like encoder-decoder that is autoregressive in time and takes into account intra-timestep interaction between agents.
Scenarios sampled from our model exhibit state-of-the-art realism; our model tops the Waymo Sim Agents Benchmark, surpassing prior work along the realism meta metric by 3.3\% and along the interaction metric by 9.9\%. We ablate our modeling choices in full autonomy and partial autonomy settings, and show that the representations learned by our model can quickly be adapted to improve performance on nuScenes.
We additionally evaluate the scalability of our model with respect to parameter count and dataset size, and use density estimates from our model to quantify the saliency of context length and intra-timestep interaction for the traffic modeling task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a language modeling inspired approach to data-driven traffic simulation. The key step involved is tokenizing future driving scenario data into a sequential, language-style format, for which this paper compares several tokenization schemes. Once tokenized, a simple transformer encoder-decoder architecture is proposed to encode the initial scene state and autoregressively decode the tokenized scene future. Training the model follows the standard next token prediction objective as in language modeling, with an optional noise term on the ground truth tokens to deal with distribution shifts caused by teacher forcing. A diverse set of experiments on the Waymo Open Motion Dataset (WOMD) provide several insights on how design choices for this new formulation impact simulation quality.

### Strengths
The key strengths of this work lie in its conceptual and architectural simplicity in comparison to existing methods. The idea is well-motivated and the presentation is clear. Besides this, the paper provides a detailed experimental analysis on different aspects of the proposed design space.

### Weaknesses
1. The benchmarking in Table 1 follows a much simpler setting with fewer max agents (24 vs. 128) and a shorter time horizon (6 seconds vs. 8 seconds) than prior work on WOMD [1,2,3]. 
2. As a result of this simpler benchmark and missing comparisons to any prior architecture, this paper does not address the key question of whether the proposed method is competitive to the current state-of-the-art despite its simplicity. At a glance, it seems to be much worse, with a minADE >3m in comparison to the SoTA methods with minADE < 1m on the more challenging standard WOMD setting. 
3. The paper is not self-contained, with important details (e.g., related work and several figures referenced during discussions in the main paper) only available in the appendix

[1] https://arxiv.org/abs/2209.13508

[2] https://arxiv.org/abs/2306.17770

[3] https://arxiv.org/abs/2309.16534

### Questions
1. Please see “Weaknesses” - these are the key points with the most influence on my rating. If addressed via a fair and direct comparison to existing work, I am inclined to improve my rating.
2. Given the simple and scalable architecture, it would be interesting to analyze the importance of scale (in terms of #parameters in the encoder/decoder) towards the performance of the proposed model.
3. The clarity of Figure/Table captions and their placement within the document could be improved, currently, they are often very far from the text referencing them.
4. How are actors ordered in the decoder? Is this randomized for each scene during both training and inference?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
“Trajeglish: Learning the Language of Driving Scenarios” proposes a model that can create scene-consistent rollouts for a subset of agents in a scene. In particular, the proposal consists of a tokenization algorithm, “k-disks”, for tokenization an agent’s motion, and a transformer-based model architecture that autoregressively and causally rolls out agents’ future trajectories. The authors provide competitive results on WOMD and transfer to nuScenes.

### Strengths
* Strong tokenizer k-disks outperforming kMeans baselines with low discretization errors and convincing ablation study
* Autoregressive and casual rollouts
* Experiments demonstrating the benefits of intra-timestep dependence of agents
* Experiments demonstrating the transfer to nuScenes

### Weaknesses
* Missing WOMD baseline results from other models
* Similar contributions as the recently published “MotionLM: Multi-Agent Motion Forecasting as Language Modeling” (https://arxiv.org/pdf/2309.16534.pdf)

### Questions
* How does your approach compare to the recently published “MotionLM: Multi-Agent Motion Forecasting as Language Modeling” (https://arxiv.org/pdf/2309.16534.pdf)?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method called Trajeglish to generate future trajectories for traffic participants in a scenario. In particular, they propose a method to tokenize trajectory data using a small vocabulary. Besides, they propose a transformer-based architecture for modeling the action tokens on map information as well as initial states of traffic participants. To evaluate Trajeglish, the authors compare it with a behavior cloning method and a baseline that only models single agent trajectories. The result shows that their method achieves superior performance.

### Strengths
### 1.The idea of tokenization using a small vocabulary is moderately novel.

### 2.The visualization and illustration are well made and help the readers to understand the paper.

### Weaknesses
## Major:

### 1.motivation of using tokenization (compared with using the actual values as in most of existing work in Appendix B) is not very clear.

### 2.the experimental results are not very impressive

(1) Improvements in Table 1 seem quite small. Can you show standard deviations for the results? 

(2) only evaluate on open-loop simulation but not on close-loop simulation

(3) the baseline details are not given (e.g., “The “marginal” baseline is an equally important baseline designed to mimic the behavior of models such as Wayformer (Nayakanti et al., 2022) and MultiPath++ (Varadarajan et al., 2021) that are trained to model the distribution over single agent trajectories instead of multi-agent scene-consistent trajectories.” However, it is unclear if this baseline really can achieve similar performance as Wayformer / MultiPath++ as the authors did not give further details) and it is hard for one to assess if they are really strong baselines.

### 3.motivation of having a model that take order into account is not very convincing

In particular, the idea of having this order seems very unnatural. For example, in the real world the likelihood of equally capable drivers (whether human or AI) to have collisions should be equal?

## Minor:

### 1.missing some relevant work on multi-agent trajectory prediction:

Hivt: Hierarchical vector transformer for multiagent motion prediction, Z. Zhou, L. Ye, J. Wang, K. Wu, and K. Lu.

Language-Guided Traffic Simulation via Scene-Level Diffusion, Z. Zhong, D. Rempe, Y. Chen, B. Ivanovic, Y. Cao, D. Xu, M. Pavone, B. Ray

### 2.did not discuss the limitations of the current work

### Questions
-What’s the motivation of using a small vocabulary compared with using the actual values as in most of existing work (as in Appendix B)?

-The provided video is a bit confusing. How do you control other vehicles that are neither replay nor trajeglish? In some videos the legends only show these two types but there are vehicles of other colors.

-Can you also show the variance for Figure 8?

-Figure 9 why the collision rate decreases when the rollout becomes longer?

-Trajgelish behavior under longer horizon rollout (e.g., 200 timesteps)?

-For the experiments, 16 scenarios are sampled for every clip in WOMD? Or only 16 clips in total?

-Can you also provide some qualitative visualization for nuscenes in Appendix?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
