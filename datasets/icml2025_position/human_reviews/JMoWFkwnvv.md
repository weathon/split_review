## Human Reviewer 1

### Questions
1. Can the authors more concretely and specifically define the continual reinforcement learning problem in Section 2? The one currently provided seems a bit ad-hoc.
2. For k-percent tuning, how might researchers select the value of k? This seems to be another hyperparameter that might not be standardized for specific environments, and could lead to results that are difficult to compare (at different levels of k).

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Questions
1. One issue I see with $k$-percent tuning is that it seems senstive to the absolute value of the lifetime. I think we see this with some of your results, where $k$-percent tuning currently tends to lead to overly high learning rates. Do you think one part of the solution should maybe, in combination with $k$-percent tuning, simply be to run evaluations for much longer? Or would this put us back into overfitting territory again? I imagine that tuning hyperparams on only 10% of the lifetime if the lifetime is only 1M steps can lead to too high of a learning rate. But what if our evaluation lifetime is 100M steps, instead of just 1M? Wouldn't hyperparams tuned on 10% of that much larger lifetime already start to translate much more effectively?

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Questions
**Questions**

See weaknesses.

1. Why does the title of the first section mention “test set” when there is no mention about test set anywhere in paper? Moreover, there is no train-test split in continual RL which is causing more confusion.
2. What are the 14 hyperparameters in DQN? Can the authors include them in a footnote or the appendix for completeness?
3. In the catch game, how do you ensure that the agent can continue catching all the balls? That is, how do you ensure that the agent has sufficient time to catch two consecutive balls when they appear in extreme ends?
4. Typically, when part of the agent’s lifetime is chosen for selecting the hyperparameters, algorithms end up selecting aggressive values to accrue more returns (eg. higher learning rate). However, in Table 2, the learning rate value for the lifetime tuned agent is higher than the k-percent tuned. Why?

**Areas of improvement**

1. The final paragraph in the introduction (contributions) can be presented as bullet points to increase readability.
2. “[...] for the purposes of this paper, [...]” this line can benefit from citing [1].
3. Although k-percent tuning supports the stated position, it is still useful to list the downsides of the the proposed approach for tuning hyperparameters. For example, the designer doesn’t know how many steps exist in the agent’s lifetime or what’s the best k to choose.
4. It would be useful to highlight (a) how prevalent “lifetime tuning” is in continual RL by citing and highlighting the practice in the literature; (b) papers where k-percent tuning in different forms already exist (eg. PT-DQN uses 1.5M timesteps to select HPs while the results are reported for 2.1M).

**References**

[1] Sutton, Richard S., Anna Koop, and David Silver. "On the role of tracking in stationary environments." Proceedings of the 24th international conference on Machine learning. 2007.

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Questions
Catastrophic forgetting is mentioned rather later in the paper, but shouldn't this be introduced  earlier in the paper?
Isn't PPO also a way to  keep policy close to before?

### Rating
2

### Confidence
3