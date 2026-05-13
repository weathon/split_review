# Seeing Eye to AI: Human Alignment via Gaze-Based Response Rewards for Large Language Models

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Advancements in Natural Language Processing (NLP), have led to the emergence of Large Language Models (LLMs) such as GPT, Llama, Claude, and Gemini, which excel across a range of tasks but require extensive fine-tuning to align their outputs with human expectations. A widely used method for achieving this alignment is Reinforcement Learning from Human Feedback (RLHF), which, despite its success, faces challenges in accurately modelling human preferences. In this paper, we introduce GazeReward, a novel framework that integrates implicit feedback -- and specifically eye-tracking (ET) data -- into the Reward Model (RM). In addition, we explore how ET-based features can provide insights into user preferences. Through ablation studies we test our framework with different integration methods, LLMs, and ET generator models, demonstrating that our approach significantly improves the accuracy of the RM on established human preference datasets. This work advances the ongoing discussion on optimizing AI alignment with human values, exploring the potential of cognitive data for shaping future NLP research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper examines the possibility of using eye-tracking data to train language reward models. The authors integrate synthetic eye tracking data from existing models into the reward model using two strategies: concatenation or addition of eye tracking features. They test their methods across multiple eye tracking models and LLMs and show that eye tracking data can improve reward models at a small to medium scale.

### Strengths
S1. The idea of using eye tracking data as reward model signal is exciting, interesting, and well-explored in this work. The paper analyzes several methods of integration and discusses the pros and cons of (synthetic or real) eye tracking data.

S2. The paper is beautifully written and clearly lays out prior work in both reward modeling and eye tracking for NLP. It was very easy to follow.

S3. The appendix reports details on hyperparameter tuning, implementations, and modeling assumptions. I believe it would be easy to replicate this work with the details provided.

### Weaknesses
W1. Very minor, but I think section 2+5 could be better structured, perhaps by moving them both into section 2. I was a bit surprised on my first read to see a related work section near the end, since section 2 discusses much of the reward modeling literature; I think it makes sense to put these in the same spot, and I liked the placement near the beginning.

W2. Because the datasets are somewhat constrained, it's not clear that this would provide consistent gains over existing reward models in a large-scale setting (could this be a useful signal only in small data regimes?). I don't think the paper necessarily needs to provide evidence against this concern, as this might require excessive amounts of compute, but I think more discussion of this possibility would help temper the claims in the work.

### Questions
Q1. You don't scale this approach to larger models/datasets (understandably!). Do you foresee any potential challenges of scaling this approach other than compute cost? Do you believe this data would be best used to fully replace existing methods for reward modeling, or in conjunction?

Q2. Somewhat related to the above-- do you have a sense of any error category differences between RMs trained with eye tracking data and without?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces GazeReward, a framework that incorporates eye-tracking data into the reward modeling phase of RLHF to better align LLMs with human preferences. This represents a novel solution to the reward modeling task with extra information from eye-tracking features. Experimental results also show the effectiveness of the proposed approach with an impormvent in reward modeling accuracy.

### Strengths
+ Eye-tracking is being introduced as a novel feature to assist reward modeling. 
+ Substantial performance improvements with the GazeReward framework

### Weaknesses
+ The experiments show that eye-tracking signals can improve the accuracy of reward modeling. As the reward model is used for RLHF processes like PPO and Best-of-n sampling, I would suggest the authors add relevant experiments to show the improvement in this down-stream application of the reward model.
+ What is the size of eye-tracking feature extractor? If the size of the eye-tracking component is not negligible, it might not be a fair comparison between the original model the model with eye-tracking feature extractor.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work incorporates features extracted from eye-tracking prediction models into reward models for RLHF. They find that adding eye-tracking information improves reward modeling accuracy on two reward modeling datasets. In addition, the authors also perform ablation studies to study what type of eye-tracking features lead to the highest reward modeling accuracy.

### Strengths
The idea behind incorporating eye-tracking features to reward models is quite original, and to my knowledge, has not been previously explored. The authors are also able to demonstrate accuracy gains in reward modeling after adding eye-tracking features, which brings a positive impact to RLHF that is widely used in current LLMs.

### Weaknesses
I find two main weaknesses that prevent me from recommending this paper for acceptance, but that could be feasibly addressed by the authors. First, it is difficult for me to assess whether the improvements on reward modeling reported in the paper are significant. According to Table 2, the test sets used for reward model evaluation are quite small (416 and 364 examples) and I did not find information on the statistical significance of the differences in results. I am also skeptical whether the improvements in scores would be robust to different random seeds and other parameters. It would be beneficial to add statistical significance tests and further discussion on how you ensured your findings are robust.
The second weakness is the lack of motivation in using eye-tracking data. There are a few points the authors allude to in the introduction (see some of my questions below), but it would be very helpful to explain the intuition on why eye-tracking data would have a connection or be correlated with human preferences. Intuitively, I would think that people would spend more time gazing at sentences that are difficult to parse for example, rather than having a preference.

### Questions
- L.46-48 Could you elaborate how eye-tracking data mitigates the problems you cited in human feedback for RLHF? Would the eye-tracking features not also reflect biases from humans from which the ET models were trained on, or their domain expertise?
- L.48-49 How is scalable oversight relevant to the problem studied in this paper?
- L. 73 It's unclear what you mean by "better temporal and spatial resolution", could you please clarify?
- L. 74 What is the connection to attention patterns and human preference for reward modeling?
- S. 3.1 It would be helpful to describe more in this section what these ET models are trained on, the accuracy of these ET models.
- I would be curious to see results, or if not feasible a discussion, on how your GazeReward framework compares to if we used eye-tracking data directly collected on the preference prompts instead of features generated by an ET prediction model
- Please also discuss the ethical impact of this work, mainly to address concerns that incorporating an ET model may amplify biases present in the ET models
- Suggestion: make the text in your figures bigger

### Soundness
2

### Presentation
2

### Contribution
3
