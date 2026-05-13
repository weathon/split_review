# A Model of Place Field Reorganization During Reward Maximization

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
When rodents learn to navigate in a novel environment, a high density of place fields emerge at reward locations, fields elongate against the trajectory, and individual fields change spatial selectivity while demonstrating stable behavior. Why place fields demonstrate these characteristic phenomena during learning remains elusive. We develop a normative framework using a reward maximization objective, whereby the temporal difference (TD) error drives place field reorganization to improve policy learning. Place fields are modelled using Gaussian radial basis functions to represent states in an environment, and directly synapse to an actor-critic for policy learning. Each field's amplitude, center and width, as well as downstream weights, are updated online at each time step to maximize cumulative reward. We demonstrate that this framework unifies the three disparate phenomena observed in navigation experiments. Furthermore, we show that these place field phenomena improves policy convergence when learning to navigate to a single target and relearning multiple new targets. To conclude, we develop a normative model that recapitulates several aspects of hippocampal place field learning dynamics and unifies mechanisms to offer testable predictions for future experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper uses a representation learning perspective to understand how the reorganization of place fields under experience and reinforcement supports RL. The authors aim to recapitulate three experimentally observed phenomena: the timeline of dense place fields emerging at rewarded locations, lengthening of fields against the direction of motion, and stable performance amidst place field drift. They also include a number of additional experiments and analyses characterizing features of the model.

### Strengths
- Overall it's a nice approach to relating hippocampal activity to downstream RL computations. Also seems like a very plausible constraint on neural activity. The model is minimally complex while still allowing insight on representation learning
- Model is capturing some phenomena in the data very nicely.
- In particular, the model is capturing the robustness against drift and modeling potential normative benefits of drift is a nice contribution -- this has been hypothesized in a number of places (eg Driscoll, Duncker et al 2022) and is well-demonstrated in the deep learning context (as the paper cites), but I don't know of any computational work demonstrating it in the context of a hippocampal navigation model.

### Weaknesses
Weaknesses

- unclear comparisons / mismatches with data.

First, the density of the place fields that is reported typically measures the number of fields with centers near the goal, not the total summed firing at a location. The prediction of increased place field density at the reward location should therefore be a larger number of place fields with centers near or before the goal. The plots in Fig 1 seem to actually show the opposite (with the possible exception of T=1000) -- place fields *spread out* near the goal location but get much larger. It is unclear how the model's definition of density relates to the experimental measure of place field density.

Also, Gauthier & Tank report that these cells are reward specialized, and therefore remap with reward. I believe that would not be a prediction of this model -- enabling this would require adding reward / reward-predictive landmarks as as an observation dimension and observe this.

Authors note that there is a rapid increase in the density of place fields near the goal location which quickly changes, with fields spreading out a lot and getting larger amplitude. I don't believe the latter observations are consistent with the data. The model's dynamics of place field size and amplitude changes are not clearly supported by experimental findings.

It appears that the number of place fields associated with non-rewarding, but frequently visited regions might go down. I believe this is not consistent with data, where home locations (and even salient landmarks) have many place fields. The model's behavior in non-rewarded but frequently visited locations needs further clarification and comparison with experimental data.

- robustness

Does the same thing happen each time? no error bars in a lot of the plots (particularly regarding density). The lack of error bars makes it difficult to assess the consistency of the model's behavior across different runs.

- confusing benchmarks

Only one benchmark -- SR fields. This was described as predicting future location occupancy p(x_{t+1} | x_t), but I believe the SR is in fact encoding a discounted sum of future occupancy \sum_{t=0}^\infty \gamma^t p(x_{t+1}|x_t) (aka, the expected number of visits to future states). The implemented SR benchmark does not seem to match the standard definition of the successor representation. Another relevant benchmark is also Fang et al 2024 which also do representation learning in a deep RL framework, and show clustering at reward and skewing (but do not look at drift / skew against the direction of motion).

- needs tidying in some places

eperience
hippocamppal
weighs -> weights
delta defined indirectly in expectation
"The agent’s transition in the environment is smooth as we use a low-pass filter using a constant" didn't understand this.

- argument about number of fields seems speculative. Authors argue it could be because it's in weak feature learning regime, but don't see any evidence of that (and an efficient coding hypothesis seems more likely).

- T's not matched up for Fig 2C?

### Questions
- What is going on with the giant place field in Fig 2C?
 
> "To determine an agent’s reward maximization performance during navigational learning we track the true cumulative discounted reward"

why not just reward rate?

- Place fields form in the absence of any reward, and many characteristics of place fields with respect to reward appear to also occur for salient landmarks. Time spent in a region of space and sensory complexity also alters place fields in the absence of reward. What happens to place fields in this model absent reward?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper models the reorganisation of place fields on linear track by backpropagating the reward-based TD error gradient to the parameters of Gaussian place field basis features. The methods are sound and paper is presented well, however I have reservations about the conclusions drawn, particularly the links to changes in field density, neural drift and the reliance on a reward signal for the learning - which are at odds with certain aspects of the experimental hippocampal literature which the model is trying to explain

### Strengths
The paper provides and executes a novel idea with the intention of explaining certain aspects of the hippocampal literature. The observed backwards skewing of place fields, opposite to the direction of motion, provides an alternative account of place field skews (Mehta et al 2000), which so far has mainly been explained by predictive mechanisms (e.g. Mehta et al 2000) like the successor representation (Stachenfeld et al 2017).

### Weaknesses
The model claims to find increased place field density at reward locations - however if the definition of field density from the experimental literature was used, the authors would find their the model actually yields the opposite results to what is observed in the experimental literature. To be specific, Gauthier and Tank 2018 find increased density of field centre of masses - i.e. fields are more numerous at goal locations, however what the authors show is mean activity of place firing rate is greater at at the goal location, which is caused by a sparse number of place fields at the goal location with incredibly high firing rate (in order to create a ramping value toward the goal location). In fact, the majority of the place field centre of masses are shown to expand and skew backwards down the track, opposite to the direction of motion (as reported in the next result) thus if the authors used the density of field centre of masses - as the experimental literature does - they would actually find an increased field density in the locations on the track preceding the goal location, and a decreased field density at the goal.

The authors also claim the model captures observed neural drift of hippocampal place cells - this is quite a stretch. Place cells have been shown to be stable for very long periods of time - up to 153 days (Thompson & Best 1990). Indeed, reward expectation has actually been shown to decrease neural drift, opposite to the claims of the authors here (Krishnan & Sheffield 2023). Essentially what the the authors show is drift in the population vector over time - which is observed in the hippocampus - however the authors' drift is because place fields actually drift around the track, which is not observed in real life - place fields are generally stable. In fact, it is likely hippocampal neurogenesis, which is heavily triggered by exercise, is responsible for driving some features of the observed representational drift (Snoo et al 2023).

Finally the comparison to successor representation (SR) is apt, however a favourable quality of the SR model is it is not dependent on an external reward signal to trigger these changes, and thus can explain phenomena such as latent learning when no reward is present. In fact the model presented here implies experimentalists would observe huge differences in hippocampus based on whether or not reward is present, when if fact periods of exploration in the absence of reward only improves future reward based learning (Tolman 1948)

### Questions
Based on the above, I would recommend the authors:
1. Use the same measures on their data that the experimental results they are attempting to explain use
2. Consider dropping the neural drift part of the results, as the underlaying mechanism in the model is at odds with many aspects of the hippocampal literature
3. Consider focussing on a set of experimental results better suited to the model e.g. the Dupret et al 2010 cheeseboard task

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper develops a reinforcement learning model that uses tunable place fields to simulate learning dynamics observed in rodent navigation. The model represents place fields as Gaussian radial basis functions connected to an actor-critic RL framework, updating field parameters to maximize accumulated rewards based on temporal difference error. The model replicates key experimental findings: increased place field density near rewards, field expansion along navigational trajectories, and field drift that doesn’t disrupt performance. The model suggests a potential framework for studying place fields learning dynamics, offering predictions for future hippocampal experiments.

### Strengths
Explaining the emergence of three observations about place field reorganization in a normative approach. 

Comparing with competitive model, such as successor representation.

Ablation study to understand contribution of different place field parameters to policy learning.

Well written, well organized.

### Weaknesses
The learning rate for place field parameters are 100 times slower than the actor and critic weight parameters. This separation of learning process by implementing different learning rates is not biologically grounded. Are there any potential biological mechanisms that might support different timescales of plasticity. 

The pace fields has been found to have more complex shapes, rather than simple gaussian shape. For example, the center-surround structure in the place field (which could be modeled as difference of gaussians) was shown to have important functional role (Sorscher et al 2022 Neuron). It is not clear how using more complex place field shapes might affect the model's results or conclusions. 

The number of place fields appears to be a crucial hyperparameter, as the model’s resemblance to experimental data is observed only within a specific range of values for this parameter. The authors examined the effect of the number of place fields on model performance in Supplemental Figures 6 and 7. However, it is important to explore methods to enhance the model’s robustness to variations in this parameter, which is relevant to the model's potential scalability to larger environmental spaces.

Randomness in field parameters, rather than in actor/critic weights, appears essential for the RNN to replicate field drifting and perform tasks with changing targets. This distinction highlights two types of noise in the RNN, each with distinct functional roles; however, a discussion on the possible biological origins of this noise and its functional distinctions is lacking. In the current work, field drifting is modeled by manually injecting noise into field parameters. Could the ring attractor mechanism identified in Sorscher et al. (2022, Neuron) provide a more mechanistic interpretation of field drifting?

### Questions
The paper takes a normal approach, using gaussian radial basis function to model place fields. There are multiple works that modeling place field using RNN without specific place field parameter assumptions, but taking them as emergent features. Could the place field reorganization be explained in such approach? 

Could the authors consider incorporating center-surround structures or other non-Gaussian shapes and discuss how this might impact their findings?

The learning rate for place field parameters and the actor/critic weight parameters possess distinct time scales.  Could the authors explore how varying the learning rate ratio affects the model's behavior and ability to replicate experimental findings. Could the model still work after removing this assumption?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a computational model for hippocampal place field reorganization during reward-based navigation learning. The model integrates reinforcement learning via actor-critic with place fields represented through Gaussian radial basis functions. The learning system is capable to create high-density place fields near reward locations, field elongation along the trajectory, and drift in place fields. The TD signal is used to tune field properties such as amplitude, centre, and width. As in similar other studies, the use of noise helps learning and generalization.

### Strengths
- The paper is clearly written and well structured
- The paper makes an effort to provide a unified theory for multiple place field phenomena
- The integration of the actor-critic RL system with pace fields is biologically relevant and interesting
- The model is compared against the well known successor representation model
- The link between a normative approach via reward maximisation and the emergence of place field representation could be valuable to interpret biological dynamics. 
- The use of noise to modulate the learning flexibility is interesting and potentially insightful for neuroscience
- The results are provided with 10 seeds runs and confidence intervals

### Weaknesses
 - While the contributions are clear, it is less clear exactly in which why this model advances previous models and what we now understand better. I am also generally struggling with words such as 'recapitulate' that don't seem to mean much to me; do the authors means to say that this models reproduces for the first time the biological neural dynamics observed in the hippocampus? If so, it would be better to be more explicit.

- The authors mentioned very briefly about the use of backpropagation and the future requirement for a biologically plausible rule. I feel that this part is not sufficiently expanded. Can the author speculate whether the model would work at all with alternatives, e.g. STDP-like rules? And if so, how would that affect the model and the ability to reproduce biological neural dynamics?

- How foes noise in the model relate to biological systems? While there are a few relevant papers that are cited in that respect, it would useful to have a motivation that is more grounded in biological dynamics. E.g. it is known that neuromodulatory activity could be regulating exploratory or exploitative behavior, possibly affecting neural dynamics with different level of noise or signal to noise ratio.

- It's not clear to me how the model would work without rewards, as this is the case in biology where place cells and place fields develop also in the absence of reward. It would good to have at least some indications on how the model could be adapted to work without an explicit reward.

- Maybe I missed it, but the supplementary information says "Refer to the Github code repository for
implementation details." but I didn't find the link to it.

### Questions
The list of weaknesses contains questions. The authors are encouraged to consider them and possibly update the paper to account for this points and provide responses.

### Soundness
3

### Presentation
3

### Contribution
3
