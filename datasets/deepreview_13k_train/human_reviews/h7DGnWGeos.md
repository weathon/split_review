# Active Retrosynthetic Planning Aware of Route Quality

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Retrosynthetic planning is a sequential decision-making process of identifying synthetic routes from the available building block materials to reach a desired target molecule.
Though existing planning approaches show promisingly high solving rates and low costs, the trivial route cost evaluation via pre-trained forward reaction prediction models certainly falls short of real-world chemical practice.
An alternative option is to annotate the actual cost of a route, such as yield, through chemical experiments or input from chemists, while 
this often leads to substantial query costs.
In order to strike the balance between query costs and route quality evaluation, we propose an Active Retrosynthetic Planning (ARP) framework that remains compatible with the established retrosynthetic planners.
On one hand, the proposed ARP trains an actor that decides whether to query the cost of a reaction; on the other hand, it resorts to a critic to estimate the value of a molecule with its preceding reaction cost as input. 
Those molecules with low reaction costs are preferred to expand first.
We apply our framework to different existing approaches on both the benchmark and an expert dataset and demonstrate that it outperforms the existing state-of-the-art approach by 6.2\% in route quality while reducing the query cost by 12.8\%.
In addition, 
ARP consistently plans 
high-quality routes with either abundant or sparse annotations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
an RL based search algorithm that incorporates some definition of route quality for retrosynthesis is proposed.


edit after discussion
- I am still not 100% convinced about the novelty of this work, but nevertheless will raise the score.

### Strengths
- interesting new ideas of using RL for scoring applied to retrosynthesis

### Weaknesses
 - somewhat disconnected from previous evaluation
- the model to assign quality is not described in enough detail
- it is not convincingly defined what reaction quality is
- prior work is not correctly attributed

"Practical efficacy: we, for the first time, draw
an insight into the disappointing practicality of existing retrosynthetic planners that regard single-step probabilities as reaction qualities."

Different and flexible ways to incorporate step and route cost beyond single step probabilities) was already included in many prior works, for example Segler (2018), Coley (2019) and Schwaller (2020). These works also used reaction feasibility models, which are a proxy for quality. Please reference this accordingly.
also, the method seems to be very similar to Liu et al 2023, which is also a very flexible framework able to incorporate arbitary cost. this needs to be discussed more carefully.
I think the paper can receive higher score if prior work is referenced properly, but in the current form this is insufficient.

### Questions
- I would suggest to order the related work section, in particular the Multi-step planning section, by the order in which the works appeared, because subsequent works influenced each other.

### Soundness
3 good

### Presentation
2 fair

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
This paper aims to consider the route quality (i.e., yield of a reaction) in the retrosynthetic planning problem. Since querying such information requires labor-intensive lab/expert verification, this paper proposes an active planning framework to strike a balance between query cost and route quality. This framework consists of an actor that decides whether to query the cost of a reaction or not and a critic that evaluates whether to expand a molecule or not.

### Strengths
1. The route quality in terms of yield is of pivotal significance for practical CASP, and this paper is well motivated from this perspective;
2. The active planning framework is designed to consider route quality, with balancing the query cost; the actor-critic technique adopted in general is reasonable and justified;
3. The evaluation using defined metrics support the major claims of balancing query quality and rate.

### Weaknesses
1. The paper representation can be improved with better clarification. See details in Questions.
2. Some claims that motivate the method should be verified. See details in Questions.
3. Important related work [1] that targets on multi-step planning should be discussed.



### Questions
#### Unverified Claims
1. In reaction cost annotation, the authors adopt a surrogate model to provide reaction cost annotation, and hope “the model prioritizes the identification of high-yield reactions over high-frequency reactions”. Can the authors empirically verify this claim? 
2. Are there real cases when high-yield reactions and high-frequency reactions are not overlapping? Intuitively, high-frequency reactions are usually high-yield ones, otherwise they cannot be frequently collected in a dataset, right?

#### Method
3. How is the state encoder $\mathcal{E}$ trained? It should also wrap $s_t$ in Eq. (4), right?
4. In Selection, is there any exploration or possibility to generate multiple routes? 
5. How is the masked value M set?
6. During inference, does the method require the external surrogate model to obtain the reaction cost? How accurate/reliable is this surrogate model?

#### Writing
7. The term “reaction cost” is misleading and inconsistent: “cost” usually refers to some undesired property that should be as low as possible, however, this paper defines cost as yield (i.e., higher “cost” indicates better quality). This is misleading and counterintuitive. Meanwhile, “observing in Fig, 2 that a molecule with a low preceding reaction cost should be prioritized to expand first”, is clearly inconsistent with Fig. 2 (i.e., low-cost=low-quality route should not be prioritized). 
8. The description of Expansion in the inference stage is not clear. Q* sometimes refers to a value, or a function (i.e., in Eq. (5)), which is confusing. What is Q*(a) and Q*(s) exactly?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the challenge of retrosynthetic planning when the reaction cost is unknown during the planning process. To balance the trade-off between query costs and route quality evaluation, the authors introduce the Active Retrosynthetic Planning (ARP) framework. This framework employs an actor-critic model to decide whether to query reaction costs and to estimate molecule values. The ARP framework demonstrates a 6.2% improvement in route quality on a benchmark dataset and a 4.9% improvement on an annotated dataset, while reducing the number of query costs.

### Strengths
- The paper identifies a key issue in retrosynthetic planning: the assumption of knowing the reaction cost for every reaction during the planning phase is impractical. In response, the authors introduce a novel solution by leveraging an actor-critic framework from reinforcement learning to address this problem.
- The proposed method demonstrates strong empirical performance on top of state-of-the-art methods, as shown in comprehensive evaluations.
- The proposed method is generic, able to work alongside various existing retrosynthetic planners, enabling their capabilities to balance between query costs and route quality evaluation.
- The paper introduces the normalized route quality to normalize the scores for different synthesis routes, thus improving the accuracy of planning outcome evaluation.

### Weaknesses
 - In the ablation study, actor+critic does not show consistent and significant improvement on success rate compared with random+critic baseline. The paper should include additional discussion to clarify this issue.

### Questions
- In the ablation study, why doesn't the actor+critic consistently and significantly improve the success rate compared to the random+critic baseline, as observed with normalized route quality?
- Why doesn't the success rate change monotonically with the query rate, unlike the normalized route quality?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers multi-step retrosynthetic search in a scenario where an expensive-but-accurate reaction quality metric is available. This motivates the authors to develop an algorithm that decides to query said metric adaptively, so that it can learn to trade-off the cost of querying it against other costs/rewards inherent to the routes themselves. The authors then run experiments to compare with existing retrosynthetic planning algorithms.

### Strengths
(S1): The framework proposed by the authors is original, well-motivated, and generally reasonable. The paper also includes valuable discussion. 

- (a) In particular, the discussion on how routes produced by existing search algorithms may be not useful in the real world (due to e.g. the reaction being low yield or otherwise infeasible) is useful. This is something that should perhaps be given more attention in the ML-for-retrosynthesis  community. 

- (b) The high-level modelling and architectural choices are reasonable and appropriate for the task at hand.

- (c) There are interesting connections of this work to retro-fallback [1] - a very recent parallel work - which is also concerned with the fact that the routes found by off-the-shelf algorithms may not be of high quality. However, I think the attack angles are somewhat complementary, as [1] tries to find _several_ routes that complement each other in their shortcomings, whereas this work focuses on _more accurately estimating the quality of a single route_ through a (possibly expensive) quality oracle. 

(S2): The paper is generally well-written and easy to understand (although with some room for improvement; see the "Questions" and "Nitpicks" sections).

### Weaknesses
 (W1): My main concern is that it is not very clear to me what the quality metric would actually be in a real-life scenario and how it would be implemented. First, the framework proposed by the authors seems to only make sense if querying the quality metric is _expensive but not too expensive_: if the quality oracle is not much more expensive that the single-step model itself (e.g. if it's a yield prediction model), then there is no need for the adaptive querying; if the metric is very expensive (e.g. asking a human chemist or running the reaction in the lab) then it wouldn't make sense to allow the algorithm to query it autonomously, even if it only does so for e.g. 20% of the cases (as that would still be prohibitively expensive and the human/lab would become a bottleneck). What would a realistic quality metric be? The authors in the paper use a trained model, which perhaps falls into the category of "not expensive enough to bother with adaptive querying", unless the model is *much* larger than the single-step model itself. Or perhaps the quality metric could result from e.g. running expensive quantum chemistry simulation, but this is a bit forward-looking as I don't think any existing frameworks for such calculations are robust enough to plug them in directly. Overall, at the very least I would expect more discussion on how the quality metric should be realized in practice. Specifically, the paper should clarify that a practical implementation of the quality metric could involve querying a chemist, and discuss the implications of this choice, such as the potential bottleneck if the query rate is too high, and how to train the model to effectively use this type of oracle without excessive queries during training.

(W2): The related works section is missing several references of established/SotA models and algorithms. On the single-step side, it is missing LocalRetro [2], RetroKNN [3] and RootAligned [4]. On the multi-step side, it is missing PDVN [5].

### Questions
(Q1): Could you expand on "critic takes both the current molecule and its preceding reaction cost as input"? Is the previous reaction cost literally concatenated into the molecule representation somewhere as a single floating point number? 

(Q2): Is Equation 6 fully correct? I am confused about the fact that it does not include the discount factor $\gamma$, and also the way $N(s)$ is used seems slightly off; I may be wrong though. 

(Q3): Could you elaborate on how the quality metric is used by the baseline algorithms like Retro* to produce the results from Table 2? I understand that for the baselines it is assumed the quality metric is always queried, which leads to 100% query rate. Could you discuss how the resulting quality value is used by the algorithms themselves during optimization? 

(Q4): Is the depth of the exhaustive search used to normalize route quality the same as the maximum depth that the search algorithms are allowed to explore?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
