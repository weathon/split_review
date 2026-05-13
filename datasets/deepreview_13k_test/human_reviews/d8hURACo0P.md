# Using Reinforcement Learning to Investigate Neural Dynamics During Motor Learning

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Recent work characterized shifts in preparatory activity of the motor cortex during motor learning. 
The specific geometry of the shifts during learning, washout, and relearning blocks was hypothesized to implement the acquisition, retention, and retrieval of motor memories. 
We sought train recurrent neural network (RNN) models that could be used to study these motor learning phenomena.
We built an environment for a curl field (CF) motor learning task and trained RNNs with reinforcement learning (RL) with novel regularization terms to perform behaviorally realistic reaching trajectories over the course of learning. 
Our choice of RL rather than supervised learning was motivated by the idea that motor adaptation to a novel environment, in the absence of demonstrations, is a process of reoptimization. 
We find these models, despite lack of supervision, reproduce many behavioral findings from human and monkey CF adaptation experiments. 
Relearning is faster than initial learning, indicating formation of motor memories. 
Optimal reaches under a CF are not straight, but rather curved, which is optimal and has been observed in humans and macaques. 
These models also captured key neurophysiological findings. 
We found that the model’s preparatory activity existed in a force-predictive subspace that remained stable across learning, washout, and relearning. 
Additionally, preparatory activity shifted uniformly, independently of the distance to the CF trained target. 
Finally, we found that the washout shift became more orthogonal to the learning shift, and hence more brain-like, when the RNNs are pretrained to have prior experience with CF dynamics. 
We argue the increased fit to neurophysiological recordings is driven by more generalizable and structured dynamical motifs in the model with prior experience from pretraining. 
This suggests that the near-orthogonality of learning-washout neural geometry underlying motor memory may be influenced by structured dynamical motifs in the motor cortex circuitry developed from prior experience. 
Together, our work takes a step towards elucidating the factors that support motor memory, acquisition, retention, and retrieval during motor learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines how training recurrent neural networks with reinforcement learning introduces the concept of motor memory, i.e., allowing curl field adaptation to affect future reaches. This is performed by introducing two regularization terms in a standard actor-critic reinforcement learning framework to train a network to produce acceleration that is then affected by curl-field forces. The authors then evaluate the network on their ability to replicate characteristics introduced in Sun et al., 2022, such as curved reaches, faster re-learning, and shifts in preparatory activity. The authors end with examining the effect of training with curl-field perturbations on the orthogonality of the learning to washout phases.

### Strengths
The paper examines the alignment between monkey neural experimental data and neural networks. How can we understand motor learning in computational networks? This paper sets up a reinforcement learning approach to the question. Understanding how network activity shifts during different epochs of a trial as well as more slowly during learning is a valuable goal.

### Weaknesses
1) There are very few baseline comparisons - which parts of the framework (loss / architecture / training) are necessary to see their main results? The paper makes reference to Richards et al., 2019, but does not adequately address this. The networks trained with reinforcement learning are not compared with networks that are trained with supervised learning, which is more common in this field. 

2) While the resulting acceleration with the additional KL-regularization terms are shown, it is unclear which ones are more akin to the experiments since only a qualitative comparison is performed (and it seems like 'neither' is the most similar to the experimental data). In fact, the time axis is severely mismatched between the network and monkey data, and thus it is very difficult to compare the resulting traces. 

3) The resulting curved traces in Figure 2e as in the trained RNN are not very similar to the monkey traces.

4) The difference between learning and relearning are not quantified adequately in Figure 2g. Is there a significant difference?

5) The effect of the curl field seems to be quite small in the networks in Figure 3b, as compared to the monkey in Figure 3c.

6) All the comparisons between the experiments and neural networks are qualitative; there is a lack of quantitative comparisons throughout the paper.

### Questions
While the authors examine the organization of preparatory states using TDR, previous experimental studies have also analyzed this using PCA, as cited by the authors. Does this structure only emerge using TDR or also PCA?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presented an experiment with an LSTM model trained with PPO on a classic motion learning task. In the task, a monkey moves a handle from one location to another location, while a disturb is applied during the motion. Detailed comparisons between the results of the model and the monkey were discussed.

### Strengths
It is interesting to compare the RL results with animals' learning results. To reproduce the classic experiment, the authors implemented a new RL environment, designed the reward, implemented models, and designed a learning curriculum. The comparison is in detail in various aspects, which are much better for scores only.

### Weaknesses
The proposed model is pretty simple, almost a direct reuse of existing models. The mathematical introduction of the model is not very clear, mainly because many variables were not explained, although a reader who is familiar with the RL field could guess what the author tried to show.

The comparison did not discuss the impact of curriculum learning, which might not be used in the experiment with a monkey.

The paper mentioned "brain-like neural geometry", while the evidence is not solid. At least a method to compare the geometry should be suggested and treat proof of "brain-like neural geometry" as a future work.

### Questions
1. Is there any model of the monkey's arm in the implemented environment? Or the agent just conceptially moving a handle?
2. Line 218, 2e4 is not a good practice for $2^4$ in a paper.
3. Line 233. No GPU is used? Is there any parallel computing with the CPU?
4. Figure 3. How these dots are located? Define the learning axis and washout axis.
5. Where are Figures S1 to S4?
6. What if the KL penalty terms were not used? A comparison with and without them can support the claim in Line 496 better.

### Soundness
3

### Presentation
3

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
This paper use recurrent neural networks (RNNs) model to reproduce observations in a motor learning task with curl field adaptation.  The model is shown to replicate key behavioral and neurophysiological features observed in monkey experiments, such as faster relearning rates and stable force-predictive subspaces. It also showed that the inclusion of prior curl field experience enhances brain-like neural geometry in learning-washout shift orthogonality, supporting the hypothesis that structured dynamical motifs contribute to motor memory.

### Strengths
This work applies reinforcement learning to model motor learning dynamics, rather than supervised learning which are usually applied. 

The inclusion of new regulation terms in the objective function facilitate the reproduction of experimental observation (but see following).

The modeling is well-motivated and rigorous, providing a significant step forward for understanding motor adaption (but see following).

### Weaknesses
1. The inclusion of two regularization terms in the objective function of PPO helps to yield realistic trajectories. These two terms, representing smoothness and zeroness constraints, is motivated by the paper Berret et al. 2011. But how the 8 cost terms in the cited paper relating to the two proposed terms formulated as the divergence of policy needs more explanation and elucidation. 

From Fig.2a,b,c,  it seems that without the two additional terms in the objective function, the model performs ok when comparing the acceleration from the model to the monkey behavior. Therefore it need more justification about the inclusion of the two terms.

2. This work mainly reproduces the observation in Sun et al. 2022 paper. In that paper, the neural population trajectories in the PCA space were also presented for motor learning and washout. This was not examined in the current modeling work. A comparison of the population activity for trained RNN and those from monkey experiments will provide more information and justification of the model. 

Some variants of the tasks that applied in monkey experiments are not examined in the RNN modeling. For example, in the current paper, the curl field is applied only to one target. But in monkey experiments, the sequentially different or interfering curl field was also investigated. 

3. The environment in the model is based on gym and the algorithm was an extension of PPO. But some details are not clear from the method. For example, the input dim is denoted either 9D (Line 145) or 10D (Line 183). It would be much better to provide the code for evaluation and reproducibility.

### Questions
Could the authors provide more details on how the smoothness and zeroness constraints align with the cost functions in Berret et al. 2011?

Could the authors provide comparison of population activity from model and monkey experiment? 

Could the model reproduce observation in the task variants including sequentially different or interfering curl field as in monkey experiments?

There are some improvements about text and figures are needed: 
1. In Eq. 3, the two new added terms miss the expectation as in the PPO object function. 
2. Line 14: "We sought train", Line 431 "while while", Line 426: "inspite of"; Line 484: "a that"; L485: "closer to orthogonal”.
3. Some figures are not well illustrated. For example, in Fig.4b, lines extend outside of the figure boundary. In Fig.3g, no label for y axis.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
To understand the development of animal motor learning, the authors seek to match the behavioral and neural activity found in prior work within a recurrent neural network. Using reinforcement learning, the authors demonstrated that artificial models ability to perform in an adaptation task in a manner similar to that seen previously in animal models. By replicating previously behavioral work within simulation, the authors use these models to provide evidence that the learning-washout neural geometry underlying motor memory is influenced by prior neural representations.

### Strengths
A notable strength of this work comes from the authors' commitment to biological relevance over computational convenience, despite submitting to a computational conference. The intentional consideration of ecological validity sets this work apart; in replicating Sun et al.'s study, their model demonstrated emergent neural-like dynamics during motor adaptation, rather than being explicitly designed to simulate biological patterns. Particularly interesting was their finding regarding orthogonal shifts in memory storage - these patterns only emerged after pretraining. While the pretraining had minimal impact on reaching behavior, it led to activity patterns that more closely matched neurophysiological observations, suggesting the model naturally developed biologically relevant computational strategies.

### Weaknesses
The conclusions focus more on the neural dynamics of motor learning but most of the interpretations focus on behavioral performance. I suggest that the authors expand on the discussion with a deeper interpretation of the weight changes in the network, rather than focusing primarily on the behavioral performance.

### Questions
Outside of behavioral performance, how would you interpret the RNN neural weight development in relation to animal models?

### Soundness
4

### Presentation
3

### Contribution
4
