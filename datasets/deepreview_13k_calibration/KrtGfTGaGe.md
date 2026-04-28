# The Wasserstein Believer: Learning Belief Updates for Partially Observable Environments through Reliable Latent Space Models

- Decision: Accept
- Avg Score: 4.50
- Scores: 1, 5, 6, 6

## Abstract
Partially Observable Markov Decision Processes (POMDPs) are used to model environments where the full state cannot be perceived by an agent. As such the agent needs to reason taking into account the past observations and actions. However, simply remembering the full history is generally intractable due to the exponential growth in the history space. Maintaining a probability distribution that models the belief over what the true state is can be used as a sufficient statistic of the history, but its computation requires access to the model of the environment and is often intractable.
    While SOTA algorithms use Recurrent Neural Networks to compress the observation-action history aiming to learn a sufficient statistic, they lack guarantees of success and can lead to sub-optimal policies. To overcome this, we propose the Wasserstein Belief Updater, an RL algorithm that learns a latent model of the POMDP and an approximation of the belief update. Our approach comes with theoretical guarantees on the quality of our approximation ensuring that our outputted beliefs allow for learning the optimal value function.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies latent space models for POMDPs, where the authors present theoretical guarantees on the quality of the learned state representation, i.e., capturing the dynamics of the environment, and its suitability for policy optimization. A key ingredient of the proposed formulation is the assumed access to the true state of the environment during the training phase, e.g., available through simulators or additional high fidelity sensors. This assumption enables a latent space model consisting of an augmented MDP with an associated POMDP amenable for learning, where the original POMDP is recovered as a variance parameter defining the latent POMDP observations goes to zero. The authors proceed to establish bounds on the difference in value functions upon conditioning the policy on the latent representation, i.e., the value function of the latent space model vs the true value function, in addition to a Lipschitz-like bound on the value difference in terms of the divergence between the embedded belief states. To evaluate the proposed method, the authors consider three types of POMDPs requiring long-term memory, inferring hidden states, and robustness to noise, where the proposed belief updater shows significant gains.

### Strengths
- Proposes the utilization of extra information available during training to guide the learning.
- Makes an important contribution to learning of POMDPs, grounded in a clear connection to an underlying MDP, with an effective learning strategy that comes with theoretical guarantees.
- Excellent exposition with detailed derivations and illustrations.

### Weaknesses
Some assumptions need to be highlighted early on with a clear account of where they may break, or how to workaround them in practice; see below.

**Missing technical discussion:**
- Assumption(2) requiring an episodic RL process appears (out of nowhere) in S3.2.
  - It would help to anticipate the need for this assumption earlier in the introduction
  - It would also help to discuss how restrictive this assumption is, as was done for Assumption(1), and whether it is mainly a technicality for some of the theoretical derivations.
  - Perhaps related to this additional assumption, the future work section mentioned adaptations under relaxed assumptions, with a citation to (Lambrechts et al. 2022). It would help to elaborate on some of those potential relaxations.

**Presentation:**
- Abstract:
  - Assumptions regarding access to the true state during training should be mentioned in the abstract.
- Section 3:
  - It would help to introduce a simple diagram showing the relationship between the different (PO)MDPs, perhaps including the symbols for key new constructs. (I see the authors already have illustrations under Fig.6 on P.20. It appears the authors preferred to include Fig.1, so perhaps readers like me could benefit from at least a pointer to Fig.6 somewhere on P.5.)
  - (Follow up): I see now I missed how "bar" symbols refer to the latent MDP. The definition of $\bar{V}_{ar{\pi}}$ appears right before Thm.3.2. It would help to establish this notation early in S3.1.
  - Let me also suggest to break up the paragraph before Eq.3.
  - Value difference bounds:
      - The big fraction on Eq.6 reappears on that of Eq.7, with only one extra term in the numerator. Since Thm.3.2 applies to the optimal policy, perhaps it would be possible to make the connection more explicit. (Indeed, this seems to appear halfway through the proof on P.29.)
      - The variance assumption in Thm.3.3 appears to be a technicality, which I worry it hinders the actual message. Looking at the proof, I see it's only needed for the value function to be almost Lipschitz. Following the pointer to Remark-2 (which only appears *after* Thm.3.3, I see that smoothing the observation in the first place was only introduced to enable training (also alluded to earlier in S3.1). I suggest to amend the statement of Thm.3.3 to clarify how the variance will be made to vanish by design, e.g., *as learning converges to the deterministic mapping ensured by ...*. (I see Fig.4 is obatiend *at the late stage of training*).
      - (Follow up) Based on the above, I don't see why Remark-2 appears where it is right now.

**Nitpicking:**
- Abstract: is can be used

I'd like to see a more compelling response addressing reviewer's Rz6s comments regarding:
- Related works with related formulations/results.
Quoting reviewer Rz6s:
> [..] there is a fair amount of literature on provable guarantees for exploration in POMDPs under latent observability (e.g. Lee et al. ICML 2023 and related/followup work) or under structural conditions for POMDPs (e.g. Liu et al. 2022 and related/followup work) which is not mentioned here
- The nature of the theoretical guarantees:
  - How it may or may not serve as a useful end-to-end guarantee.
  - A more detailed comparison to known results using bisumulation metrics, with a more through review of this literature clarifying how the present contribution fits there.

### Questions
**Missing technical discussion:**
- Assumption(2) requiring an episodic RL process appears (out of nowhere) in S3.2.
  - It would help to anticipate the need for this assumption earlier in the introduction
  - It would also help to discuss how restrictive this assumption is, as was done for Assumption(1), and whether it is mainly a technicality for some of the theoretical derivations.
  - Perhaps related to this additional assumption, the future work section mentioned adaptations under relaxed assumptions, with a citation to (Lambrechts et al. 2022). It would help to elaborate on some of those potential relaxations.

**Presentation:**
- Abstract:
  - Assumptions regarding access to the true state during training should be mentioned in the abstract.
- Section 3:
  - It would help to introduce a simple diagram showing the relationship between the different (PO)MDPs, perhaps including the symbols for key new constructs. (I see the authors already have illustrations under Fig.6 on P.20. It appears the authors preferred to include Fig.1, so perhaps readers like me could benefit from at least a pointer to Fig.6 somewhere on P.5.)
  - (Follow up): I see now I missed how "bar" symbols refer to the latent MDP. The definition of $\bar{V}_{\bar{\pi}}$ appears right before Thm.3.2. It would help to establish this notation early in S3.1.
  - Let me also suggest to break up the paragraph before Eq.3.
  - Value difference bounds:
      - The big fraction on Eq.6 reappears on that of Eq.7, with only one extra term in the numerator. Since Thm.3.2 applies to the optimal policy, perhaps it would be possible to make the connection more explicit. (Indeed, this seems to appear halfway through the proof on P.29.)
      - The variance assumption in Thm.3.3 appears to be a technicality, which I worry it hinders the actual message. Looking at the proof, I see it's only needed for the value function to be almost Lipschitz. Following the pointer to Remark-2 (which only appears *after* Thm.3.3, I see that smoothing the observation in the first place was only introduced to enable training (also alluded to earlier in S3.1). I suggest to amend the statement of Thm.3.3 to clarify how the variance will be made to vanish by design, e.g., *as learning converges to the deterministic mapping ensured by ...*. (I see Fig.4 is obatiend *at the late stage of training*).
      - (Follow up) Based on the above, I don't see why Remark-2 appears where it is right now.

**Nitpicking:**
- Abstract: is can be used

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a model-based procedure, the Wasserstein Belief Updater (WBU), for learning/optimizing POMDPs. The components are a latent model learner, a belief update learner, and a policy optimizer. The authors make an assumption that the POMDP latent states can be accessed during training time. They provide some theoretical approximation error bounds which bound the model quality and the representation quality resulting from their losses. The authors provide details on how to practically implement their proposal (Section 4), and provide experimental evaluations for their algorithm (Section 5).

### Strengths
- The paper presents a few interesting ideas for learning bisimulation-type metrics for POMDPs, which is a reasonable extension from the MDP case due to the additional structure of needing to approximate the belief states. Some of the ideas are certainly interesting and potentially worth further development. 
- The problem of representation learning in POMDPs is difficult and interesting.
- The theoretical results do provide some amount of theoretical backing, and at a glance the proofs for the approximation error bounds seem non-trivial due to the partially observable problem setting. I have not checked the proofs very carefully. 
- The ideas and theory are supported by experiments which show some improvement over baselines.

### Weaknesses
 - The biggest drawback to this work is the latent observability condition. The methodology being presented is fairly depend on this condition, since it attempts to learn the latent transition model, observation model, and belief states. This simplifies the problem setting quite a bit by making the POMDPs more or less a complicated involved MDP. It is not clear how much applicability this method has beyond the settings where this assumption holds. The assumption allows the method to bypass the core challenge of POMDPs, which is dealing with uncertainty about the true state, and instead focuses on learning a model in a setting where the state is actually observed during training. This significantly limits the practical relevance of the approach.
- In terms of related work, there is a fair amount of literature on provable guarantees for exploration in POMDPs under latent observability (e.g. Lee et al. ICML 2023 and related/followup work) or under structural conditions for POMDPs (e.g. Liu et al. 2022 and related/followup work) which is not mentioned here. The lack of discussion of these works is a significant oversight, as they directly address the same problem setting (latent observability) and provide alternative approaches and theoretical results.
- The current theoretical guarantees are similar to the other papers on learning with bisimulation-like metrics, in that the extent of the theoretical results is a bound on the approximation error incurred via the population loss functions. I would argue that this is not an "end-to-end" theoretical guarantee that is useful, since there are many questions about how one can minimize such a loss when only given access to samples from the distribution (i.e. how close are the empirical losses and the population losses, are there any double-sampling issues, is one sampling from distributions one does not have access to, etc.) and if we can minimize it on policies that actually matter for downstream performance rather than only on the on-policy distributions (currently it is simply an "on-policy" bound which holds only for the distribution under which the data was collected). As an example of the weakness of such a bound, the usual bisimulation metric in tabular MDPs satisfies a similar bound (Theorem 5.1, Ferns et al. 2004), but there is still an exponential lower bound for learning any bisimulation-like abstraction (Appendix B of Modi et al., 2020). Thus, the argument that this paper presents theory that can be used to give guarantees is either incomplete or inaccurate, depending on one's perspective. The authors could perhaps support their theory by experimentally verifying that the (population) losses are indeed minimized and verifying that the quantities on the LHS of their bounds are controlled by their procedure. The theoretical results, while non-trivial, do not provide a practical guarantee on the performance of the learned policy, and the connection between the theoretical bounds and the empirical results is not clearly established.
- In terms of writing and presentation, I feel that more effort should be put into streamlining the notations and explanations. For example, even after several re-reads, it is still difficult to keep track of the notation for the different models MDPs/POMDPs being passed between, to type-check things (e.g. the state embedding functions depend on different things at different points), and to grok which ideas are essential/novel and which are simply details. The lack of clarity in the notation and explanations makes it difficult to understand the core contributions of the paper and to reproduce the results.
- Similarly, there is a fair amount of statements which are "fake rigorous" i.e. do not check out formally. Here is a list:
 1. "Unlike in MDPs, stationary policies that are based solely on the current observation of P do not induce any probability space on trajectories of M". This is probably not what the authors meant to say, since any policy (stationary or not) induces a distribution over trajectories.
 2. "This procedure guarantees \bar{M} to be probably approximately bisimlarly close to M as \lambda \rightarrow 0". Is this a formal claim? There is no PAC bound given here nor in the cited prior work on WAE-MDPs.
 3. Lemma 3.1: "There is a well defined probability distribution [...] over histories likely to be perceived at the limit by the agent when it executes \bar{\pi} in P". What does this mean? I can try to guess what this mean, but as a formal statement this does not make sense.
 4. Theorem 3.3: there is a "for any \epsilon > 0" in the statement and in the bound but no other quantities in the bound depend on $\varepsilon$
- The experimental results mild improvement over the baselines in some environments, and no improvement over the baselines in other environments. What is the source of this varying degree of improvement? Can more experiments be performed to understand when this specific approach yields benefits? The lack of consistent improvement across all environments raises questions about the robustness and generalizability of the proposed method. The experimental section should include more analysis to explain the varying performance.

### Questions
There are several technical questions which I have:
1. What does "we assume that we have access to the latent model learned by the WAE-MDP" mean?
2. What does Lemma 3.1 mean?
3. In paragraph "Local losses", how is one expected to sample from $\tau^\star(h)$, the true belief function for history $h$.
4. What does $\varepsilon$ represent in Theorem 3.3?
5. It is interesting that Theorem 3.3. only holds on the optimal policy $\bar{\pi}^\star$. What is the source of this, and can this not be extended to work for other policies of interest?
6. Figure 3: Belief loss. How can the loss be negative?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an algorithm that learns the belief in POMDP. 

## Learning the Environment
The algorithm first learns an estimation of the true MDP via the WAE-MDP method, under assumption that the underlying model in POMDP is accessible in training (*Assumption 1*). The WAE-MDP learns a latent MDP model which encodes not only the true state transition of the POMDP but also the observation mechanism, thus it induces all information of the original POMDP, if it is exactly learned (but WAE-MDP learns an estimation instead).

## Theoretical results
Under the episodic assumption of the POMDP (*Assumption 2*),
the estimation of the difference between values from the underlying (true) MDP and from the latent MDP is upper bounded theoretically by certain linear combination of local losses and Belief losses, which are expected Wasserstein distances or reward differences between the underlying (true) MDP / belief system and latent MDP / belief system. And in the variance zero limit, choosing a different learning history would result in an upper-bounded difference in optimal Value functions.

## Learning the Belief
Once the POMDP is known via the latent MDP, one can use the first-order belief evolution formula derived from Bayesian method to calculate the belief from timestep 0 to any timestep. But Bayesian method requires intractable integration over current belief, so the final method is to train another model to learn the belief. 

Training belief follows online optimization of the objective function which is the expected Wasserstein distance between $\overline{\tau}$ and $\phi$. And due to computational difficulty, expected KL divergence is used as objective instead.

## Experiments
The paper tested the algorithm in several environments such as Space Invaders, Stateless Cartpole, etc., compare with R-A2C and DVRL.

### Strengths
- The paper provides a solid math ground (theoretical analysis of the POMDP dynamics) by
    - proving the existence of a distribution on training history set.
    - uses the distribution above to estimate certain bounds of learning effectiveness (Thm 3.2) and learning variance (Thm 3.3).
The results guarantees the learning algorithm would converge to a good approximation.

- Proposed learning methods (objectives) are from theoretical results.

- Outperforms R-A2C and DVRL in certain POMDP environments.

### Weaknesses
 - Wasserstein Belief Updater finally chooses the objective function to be KL divergence as a Wasserstein proxy. I agree with the difficulty of optimizing Wasserstein (which is quite singular). But probably the authors can thing about the entropy-regularized version of Wasserstein distance? Hope the work after the following paper could help.
[ Marco Cuturi, Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances ]
[ Marco Cuturi, et. al., Fast Computation of Wasserstein Barycenters ]

- I did not see what are the requirements of the sets we discuss? I guess they are at least discrete to make certain Markov chain theoretical results hold. But as the paper talked about Cartpole, I guess the theory would meant to be possibly applied to continuous state spaces (real manifold at least).

- In the theoretical part, the existence of $\mathcal{H}_{\overline{\pi}}$ is relying on the ergodicity of an episodic MDP (Huang Bojun, 2020), where the state space $\mathcal{S}$ is assumed to be discrete (finite or countably infinite). I want to know the topology (and geometry) of the history space. 

- Is it the collection of all $(a,o)$ sequences such that $(\mathcal{A}\cdot \Omega)^*=Map(\mathbb{N}, \mathcal{A}\times \Omega)$, or it is the collection of all finite-length tuples that $(\mathcal{A}\cdot \Omega)^*=\bigsqcup_{n\in\mathbb{N}}(\mathcal{A}\times \Omega)^n$? Categorically speaking, is it a direct product (product) or direct sum (coproduct)? See https://en.wikipedia.org/wiki/Product_(category_theory).

- Is there any theoretical result on the continuous spaces such as CartPole? The definition of ergodicity is slightly different there.


Typos
- I could hardly analyse the second sentence of the abstract, .
- Page 4, first line is hard to read. (But the meaning is clear)

### Questions
Questions:
- In the theoretical part, the existence of $\mathcal{H}_{\overline{\pi}}$ is relying on the ergodicity of an episodic MDP (Huang Bojun, 2020), where the state space $\mathcal{S}$ is assumed to be discrete (finite or countably infinite). I want to know the topology (and geometry) of the history space. 

- Is it the collection of all $(a,o)$ sequences such that $(\mathcal{A}\cdot \Omega)^*=Map(\mathbb{N}, \mathcal{A}\times \Omega)$, or it is the collection of all finite-length tuples that $(\mathcal{A}\cdot \Omega)^*=\bigsqcup_{n\in\mathbb{N}}(\mathcal{A}\times \Omega)^n$? Categorically speaking, is it a direct product (product) or direct sum (coproduct)? See https://en.wikipedia.org/wiki/Product_(category_theory).

- Is there any theoretical result on the continuous spaces such as CartPole? The definition of ergodicity is slightly different there.


Typos
- I could hardly analyse the second sentence of the abstract, .
- Page 4, first line is hard to read. (But the meaning is clear)

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Wasserstein Belief Updater which is based on the Wasserstein Auto-encoded MDP (WAE-MDP) framework to learn a latent model to update beliefs for partially observable problems. Due to partial observability, in addition to WAE-MDP components, the proposed method learns a latent observation function and a latent belief encoder which recursively updates the beliefs. Experiments show that the RL agent using the updated belief outperforms previous RNN based algorithms.

### Strengths
- Every step of the proposed approach is explained well, and their connections to prior work are clearly discussed.

- The WBU approach nicely extends WAE-MDP to the partially observable settings, and the paper also provide theoretical guarantees that extends bisimulation bounds in WAE-MDP to POMDPs.

- The architecture of the latent belief encoder seems to be a novel by having the Masked Auto-Regressive Flows as the output layer on top of a sub-belief encoder. The training of the sub-belief is then done without back-propagation through time.

- Experimental results suggest that the beliefs updated by the latent belief encoder are useful information for decision-making with partial observations. The WBU agent achieves strong performance in several POMDP environments, and it especially outperforms existing algorithms by a significant margin in the environment requiring long-term memorization.

### Weaknesses
 - Even though the method is called Wasserstein Belief Updater and the theoretical analysis is for the Wasserstein belief loss, the actual algorithm uses a KL loss for the belief updater part. Hence, the guarantees do not necessarily hold for the actual algorithm.

- The algorithm doesn't have any step for updating the MAF. Is there something missing or is the MAF pre-trained by some other way?

- In Section 4, the authors claim that the training of the sub-belief encoder does not require the challenging BPTT as in RNN. But given the recursive structure of the sub-belief encoder, it is not clear why the claim is true. Even when the sub-belief encoder is updated only by the belief loss, the gradient flow might still need to propagate back if the previous sub-belief is also generated by the same sub-belief encoder. Back-propagation might stop if the previous sub-belief is actually generated by other networks, like using (3), but this part is a bit unclear. The argument that beliefs progress forward does not justify the unnecessity of BPTT, since the same forward recurrence argument would also apply for the latent state process used in previous RNN approaches. Gradient stop is used in training the model, which means that the gradients computed by the proposed method are only approximations. The justification for using approximate gradients, and why they would be better than the actual gradients (computed by BPTT without gradient stop) in the belief case, is missing.



### Questions
- Can you provide more details on MAF training?

- Can you provide more details on how the sub-belief encoder is trained and why BPTT is not needed with some gradient analysis? 

- Some possible typos and missing definitions: 
  - Is $\varphi^*$ defined somewhere?
  - In equation (5), should the Wassertein distance be given by $D$ or?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
