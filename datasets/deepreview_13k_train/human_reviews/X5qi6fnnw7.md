# Conservative World Models

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Zero-shot reinforcement learning (RL) promises to provide agents that can perform _any_ task in an environment after an offline pre-training phase. _Forward-backward_ (FB) representations represent remarkable progress towards this ideal, achieving 85% of the performance of task-specific agents in this setting. However, such performance is contingent on access to large and diverse datasets for pre-training, which cannot be expected for most real problems. Here, we explore how FB performance degrades when trained on small datasets that lack diversity, and mitigate it with _conservatism_, a well-established feature of performant offline RL algorithms. We evaluate our family of methods across various datasets, domains and tasks, reaching 150% of vanilla FB performance in aggregate. Somewhat surprisingly, conservative FB algorithms also outperform the task-specific baseline, despite lacking access to reward labels and being required to maintain policies for all tasks. Conservative FB algorithms perform no worse than FB on full datasets, and so present little downside over their predecessor. Our code is available anonymously at [https://anonymous.4open.science/r/conservative-world-models-4903](https://anonymous.4open.science/r/conservative-world-models-4903).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper concerns itself with the OOD issue in zero-shot offline RL. It primarily makes CQL-like modifications to the objective for learning Forwad-Backward representations. From this arise two variants, the value-conservative variant which samples task representations uniformly and the measure conservative variant which uses the backward representation $B(s^+)$. Thorough experiments have been done on the ExORL benchmark where the method is compared to single-task RL (TD3, CQL) and non-conservative FB. It performs favorably in comparison to the baselines, sometimes even outperforming the single-task algorithms.

### Strengths
Addressing the issue of OOD actions arising  through maximization in offline RL is important, also in the zero-shot or multi-task case such as the case for FB.

Good experimental evaluation has been conducted.

I mostly didn't have trouble reading the paper, I think it's well-written.

The method is simple (application of CQL to FB) and therefore easy to understand.

### Weaknesses
Some parts of the theory are not clear, or maybe there were typos in the equations. The most essential thing for me is to clarify the treatment of the task representation vectors in  the VC and MC case and how do they connect to the original FB definition (see questions).

Why does VC outperform MC sometimes has been clarified to a certain extent in the discussion, however it is only intuition and no evidence for the claims have been given.

Some of the equations, specifically equation 5, lack clarity. The $z$ variable, representing the task embedding, does not appear as an explicit argument to the Q function, which is inconsistent with the typical formulation of task-conditioned Q-functions. This makes it difficult to understand how the task representation influences the Q-value estimation. Furthermore, the connection between equation 5 and 6 is unclear. In equation 6, the forward representation is defined as a function of the same $z$, i.e. $\langle F(.., z), z \rangle$, which seems inconsistent with the Q-value definition in (5), where the Q function is conditioned on a policy $\pi_z$ that is implicitly dependent on $z$. The subsequent sampling of $z$ independently from $s^+$ in MC-FB further obscures the relationship between the backward representation and the task embedding, raising questions about the validity of this approach. The lack of clarity in how the task representation is used in the forward model and Q-function makes it difficult to assess the soundness of the proposed method.

The justification for the introduction of MC-FB, which argues that sampling task vectors uniformly might be suboptimal and that focusing on relevant tasks via the backward representation is better, is not fully supported by the experimental results. Figure 4 shows that the zero-shot performance of the MC variant is often lower than that of VC, which contradicts the stated rationale. This discrepancy is only addressed in the discussion, but it should be commented on earlier in the paper, especially since it is a central motivation for the MC-FB variant. The paper would benefit from a more thorough analysis of why MC-FB underperforms in certain scenarios, and a more rigorous justification for its introduction, beyond the intuition provided.

### Questions
Would be useful if you would properly define the abbreviations for VC-FB and MC-FB in the text before using them.

In equation 5  the $z$  variable is not an argument to the Q function, as it should be?

Broken english in line before equation 6. What is the connection between (5) and (6)? In (6) the forward representaiton here is a function of the same $z$, i.e. $\langle F(.., z), z \rangle$, however this is not how the Q value is defined in (5). Later you sample z's independently from $s^+$, hence the backward representation is completely independent of the task $z$ in the MC-FB. How is this valid? My questions here are:

* In which cases does the $z$ correspond to the backward representation?
* Follow up to the previous question, why does you MC-FB version  treat the backward representation and $z$ independently, while the VC-FB version does not, shouldn't the z in the F(...) be essentially the output of $B(s^+)$ as per your description?

The argument for the introduction of the MC-FB is  that it might not make sense to sample task vectors uniformly, but to focus on the ones that we care about (via backward rep), yet in figure 4 the zero shot performance of the MC variant is lower than VC? Can you clarify this? Also in the paper. (I realize that you have this in the discussion, however I think that it should be commented on earlier).

in 4.3, what does "stochastically dominate" mean?

Can you explain the failure cases of MC-FB in comparison to VC in figure 5?  For the Walker2D environment, the MC variant completely fails for the RND dataset - I suspect that the reason is low task coverage? Also, in some cases  there is a big gap between CQL and your method (random jaco).


If you address these concerns I will raise the score appropriately (the most important concern is the one about the dot-product).

### Soundness
3 good

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
This paper proposes two novel reinforcement learning methodologies for learning arbitrary tasks from unsupervised transition data. The key is that the datasets are not as large and diverse as in previous work. The goal is to pre-train a model on small transition datasets and at test time, zero-shot generalize to arbitrary reward functions that are characterized by some distribution. The work builds on the idea of forward-backward learning in which successor information is employed to make statements about past and future visitation counts of a policy. These counts are then related to reward information during test time. The proposed algorithms use conservativeness to combat large Q-value predictions in unseen state-action areas which is an idea that has previously been used successfully in standard offline RL. The work validates the functionality of the method with an intuitive toy example and then goes on to evaluate on larger benchmark suites where the proposed methods outperform baselines on several tasks.

I would like to mention that while I am aware of the offline RL literature, I am not familiar with the forward-backward literature specifically. I did not check the math in section $2$ for correctness since it is already published work.

### Strengths
Motivation
* The motivation of the work is clearly established. The ability to extract dynamics information that can be leveraged for arbitrary downstream tasks is a promising direction towards building general-purpose representations. The reasoning for the employment of forward-backward methods is clearly established.

Contextualization with prior work
* Specifically, the first few sections do a good job of making sure that prior work is mentioned and highlight clearly which parts of the manuscript are novel and which ideas are taken from previous work.

Structural clarity
* The paper has a very clear structure and is easy to follow. The origins of the method are clear and the toy example helps understand the internal mechanisms of the network. The language is clear and the manuscript is well-written.

Limitations section
* The work provides a good limitations section that highlights some of the practical challenges and outlines future directions of work. In general, I think this section is very beneficial for readers of the paper and I think it is a nice addition.

Experimental Evaluation
* The experimental section is structured well and asks $3$ very relevant questions to analyze the proposed algorithms. Specifically, experiment Q3 in the paper shows that in most cases it is likely not bad to simply add conservativeness to the existing approach as long as the data quality is high is convincing. 
* The benchmark suite is sufficiently sized and provides several different types of environments.

Novelty
* As mentioned before, I’m not familiar with this specific type of model but given the recency of publication of prior methods, it seems reasonable to assume that the contribution is sufficiently novel. I also think the contribution adds sufficient new content to the existing approach and highlights the relationship between conservative offline RL approaches and how the procedures transfer to forward-backward methods.

### Weaknesses
Mathematical clarity
* Specifically section 2 might benefit from clarity improvements and re-ordering of some of the references.
  * The relationship between the task structure of the set of MDPs and the reward functions is unclear. The MDP framework outlined in section $2$ paragraph $1$ does not come with such structure and the structure is only mentioned but not well-defined in the problem formulation section. As a result, it is not clear to me where the differences in the sets of tasks come from (see Q1). It might be beneficial to mention the distribution of task vectors earlier and how it relates to reward functions in paragraph $2$ (Problem formulation.).
  * Relatedly, should the forward model function be defined as $F: \mathcal{S} \times \mathcal{A} \times \mathcal{Z} \mapsto \mathbb{R}^d$? Do the tasks and the policies share the same space? Is the embedding space always the size of the task vector space? In this context, it is not clear what the following notation means: $\pi_z : \mathcal{z} ∼ \mathcal{z}$.
  * I was looking for a reference for the derivation of some of the claims in section $2$ and that reference is only provided at the end of the section. I personally would have benefitted from this being at the beginning. This would make it both clear that the derivation comes from previous work and possible for the reader to open up the reference on the side before I dive into the math.
  * The actor-critic formulation is only mentioned very briefly at the end of the section but as far as I understand it might be quite crucial to running the experiments and deriving the actual method.

Contextualization with prior work
* There is an abundance of literature on conservativeness in RL and the paragraph on this in the related works section contains a total of 7 references. This contextualization could be a little stronger. The downside of this lack of contextualization shows somewhat in the experiments as I will outline later. Less detail about the cited methods and concise statements about previous literature’s commonalities might provide a way to condense the text in this section.

Experimental Evaluation
* The evaluation metrics are not fully specified. The text mostly talks about performance but it is not clear what is being measured. I’m going to assume that the experiments measure performance in terms of cumulative reward. Relatedly, in Figure 4, It is not clear to me what a Task Score x is.
* The following statement is probably not well-qualified. “CQL is representative of what a conservative algorithm can achieve when optimizing for one task in a domain rather than all tasks”. CQL was an impressive step towards using offline data in RL but since then many more conservative methods have been established that show significantly stronger results but even more importantly are easier to train and more stable. This is one of the weaknesses of CQL (and the proposed method) that is highlighted in section 5 and I strongly agree. As a result, CQL might not be the best baseline to establish that the method performs as well as common offline RL methods. It might make sense to compare to an offline method that provides better stability. A common choice would probably be Implicit Q-Learning. That being said, CQL is a reasonable choice in the sense that it tries to achieve a similar objective as the proposed method and as such provides a comparison against a non-forward-backward approach with similar mechanistics. Still, there might be better baselines to strengthen the claim that the method competes with sota offline RL approaches.
* Some of the claims may be overstated and the text could be a little more detailed on the actual findings.
  * While I think the idea of reporting percentage improvements can be nice to establish a clear performance difference, this difference is only really strong if the baseline performance is already good. I could, for instance, say that the method performs $1000\%$ better on the Jaco RND experiment than the non-conservative baseline. However, this would be rather misleading because neither method might be close to solving the task. Depending on how these measures are now aggregated, the performance of the method might look inflated. I think a clear definition of what’s being measured and how the measures are aggregated would be useful to provide context for the numbers and a more detailed description of when the method works well.
  * The claim that conservativeness is not harmful is only supported on what is referred to as a high-quality dataset. In this case, the dataset is already providing decent coverage and the Q-values should be easy to approximate (see Q3).
  * The difference between VC-FB and MC-FB is highlighted in section $3$ but the effects of the differences are not explicitly analyzed in the experiments.

Minor textual clarity suggestions
* Figure 1’s caption could probably mention earlier that this is not simply an illustration but the data is from an actual experiment.
* Equation $(1)$ is currently not an expectation without assumptions on the distribution.
* The statement “Since the successor measure satisfies a Bellman equation” would benefit from a citation.
* “$s_+$ is sampled independently from $(s_t, a_t, s_{t+1})$”, the latter is not a distribution but a tuple, this should probably be the dataset?

### Questions
Q1: How is the task distribution $\mathcal{Z}$ defined in practice? It is not quite clear to me, for instance, how I would define such an abstract distribution for either of the given environments in section $5$ other than by possibly defining a distribution over final states which would have to be as large as the state space? Can you give an example of what this would look like in, e.g. the Cheetah environment? 

Q2: Traditional CQL samples the data it’s minimizing its Q-values over from the policy distribution rather than employing a max operator. What is the reasoning for choosing a max operator here rather than just sampling from the distribution? The latter seems to be easier to implement.

Q3: What do we expect to happen when we run the conservative version of the proposed algorithm on full datasets with poor quality? Are the trends similar to what we see in the small-scale experiments?

Q4: Is it possible to deduce up-front when this approach performs as well as or better than its single-task offline RL counterparts? In other words, what types of environment properties make the method work?

Q5: It is a little counterintuitive to me that conservativeness seems to work better when the datasets are of higher quality rather than when datasets provide poor support. Do you have any idea why that is?

Q6: (Feel free not to answer since this is a question about previous work rather than your work really.) Are $F$ and $B$ learned solely through equation (4) in the original FB approach? How can we be sure they are actual distribution summaries then?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors propose what they call a "conservative world model", essentially a general model that can demonstrate zero-shot RL through offline data. The conservative mentioned in the title refers to an approach to be more conservative with the values of out-of-distribution state-action pairs, which can allow for more general policies in some cases. The authors cover their approach in detail, present two variations of their approach and compare their performance to a non-conservative baseline across four standard domains. Their results demonstrate comparable or better performance with the non-conservative baseline.

### Strengths
This paper demonstrates a fair amount of clarity around the approach, with well-written arguments around the potential benefits. The work is original, to the best of my knowledge, in terms of its weighting approach for the training data for offline RL problems. The quality of the work in terms of the number of domains and overview of the results if good. Those interested in offline RL, and particular RB approaches, will likely find the work of some significance.

### Weaknesses
This paper has a number of weaknesses.

First, a relatively minor one is the choice of the phrase "world model" to describe the approach. World models already are a well-established and distinct approach in this area [1].

Second is the relative lack of novelty. The approach is essentially a reweighing of training data, but similar reweighing strategies have already been proposed and are not compared against [2].

Third is the evaluation setup. It's odd to have two variants of the approach in comparison to a single baseline, which essentially gives the approach twice the opportunity to outperform the baseline. For simplicity, it might have been better to stick with VC-FB and leave MC-FB to the appendix. However, it's also unfair that both approaches are given 3 times the training duration to FB. Ablations or additional baselines could have helped to avoid this issue.

Fourth is the presentation of the results. The paper repeatedly aggregates over distinct problems, whose scores are not comparable and presents these results as summed values and percentages. I don't believe this is appropriate. The claims made are also not reflective of the results, which show an inconsistent improvement by VC-FB and MC-FB over FB. This is especially worrying in the Random case, where the approaches are essentially identical. Given the claims around the value of conservative world models, I would have assumed that they would have outperformed FB the most when the dataset was of a poorer quality.

### Questions
1. Is there a relationship to the more typical usage of World Model that I'm missing?
2. Are there no other appropriate baselines that could have been included in the evaluation?
3. Why is it appropriate to aggregate the results across evaluation domains?
4. Why would the authors' approach perform worst with worse datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the integration of conservative terms into the Forward-Backward (FB) loss function, aiming to mitigate the risk of overvaluing out-of-distribution state-action pairs—a factor that could significantly impair FB’s performance. The empirical results presented in the study effectively validate the utility of these conservative terms.

### Strengths
- The rationale behind implementing conservative terms is well-founded and convincing.
- The experimental evidence provided clearly demonstrates the efficacy of the conservative terms.
- A didactic example is skillfully used to elucidate the impact and functionality of the conservative terms.

### Weaknesses
 - The “world model” as described in the paper seems to be potentially mischaracterized. The referenced document, [2209.14935.pdf (arxiv.org)](https://arxiv.org/pdf/2209.14935.pdf), elucidates that "Both SFs and FB lie in between model-free and model-based RL, by predicting features of future states, or summarizing long-term state-state relationships. Like model-based approaches, they decouple the dynamics of the environment from the reward function. Contrary to world models, they require neither planning at test time nor a generative model of states or trajectories." Therefore, the paper’s description might need a revision for accuracy.
- The set of baselines employed in the experimental section appears to be inadequate. As depicted in Figure 2 of [2209.14935.pdf (arxiv.org)](https://arxiv.org/pdf/2209.14935.pdf), FB does not have the "sufficient performance gap" as claimed by the authors, necessitating the inclusion of a broader spectrum of baselines for a more comprehensive performance comparison. Specifically, the performance difference between FB and other methods in the referenced figure appears marginal, suggesting that the claimed superiority of FB might not be as substantial as presented. A more rigorous comparison against a wider array of methods is needed to substantiate this claim.
- The concept presented is relatively straightforward, essentially adapting the conservative term from Conservative Q-Learning (CQL) in offline reinforcement learning to the zero-shot reinforcement learning context. Given the moderate domain gap between offline RL and zero-shot RL, the idea appears to be somewhat lacking in novelty. The adaptation of a conservative term, while potentially beneficial, does not introduce a fundamentally new approach or insight into the problem. The core mechanism remains largely unchanged from its offline RL counterpart, raising questions about the significance of this contribution.

### Questions
- Could the authors revisit and verify the usage of the term "world model" in the manuscript? The source [2209.14935.pdf (arxiv.org)](https://arxiv.org/pdf/2209.14935.pdf) suggests a possible misclassification of FB, and by extension, the methodology in this paper, as a "world model".
- The term "world model" seems to have limited relevance and is infrequently used throughout the paper. Could its significance to the paper’s core content be clarified, or is it a concept that could potentially be omitted without loss of clarity?
- To bolster the robustness of the study, it would be beneficial for the authors to incorporate a wider array of zero-shot RL baselines, particularly those utilized in [2209.14935.pdf (arxiv.org)](https://arxiv.org/pdf/2209.14935.pdf). Additionally, considering the 2022 inception of the FB method, it may be pertinent to include more recent and relevant baselines in the analysis.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
