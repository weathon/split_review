# Large Language Model Alignment via Inverse Reinforcement Learning from Demonstrations

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Aligning Large Language Models (LLMs) is crucial for enhancing their safety and utility. However, existing methods, primarily based on preference datasets, face challenges such as noisy labels, high annotation costs, and privacy concerns. 
In this work, we introduce **_Alignment from Demonstrations_** (AfD), a novel approach leveraging high-quality demonstration data to overcome these challenges. We formalize AfD within a sequential decision-making framework, highlighting its unique challenge of missing reward signals. Drawing insights from forward and inverse reinforcement learning, we introduce divergence minimization objectives for AfD.
Analytically, we elucidate the mass-covering and mode-seeking behaviors of various approaches, explaining when and why certain methods are superior.
Practically, we propose a computationally efficient algorithm that extrapolates over a tailored reward model for AfD. We validate our key insights through experiments on the Harmless and Helpful tasks, demonstrating their strong empirical performance while maintaining simplicity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies the large language model (LLM) alignment problem in the learning from demonstration framework. Under this framework, the widely adopted supervised finetuning (SFT) paradigm can be interpreted as matching the policy distribution and an unknown expert demonstration distribution with the forward KL distance measure. The authors then propose to consider distribution matching with the reverse KL distance. This problem has been studied in the imitation learning literature. A standard method is to train a discriminator to distinguish the policy trajectories and the expert trajectories and then train the policy by reinforcement learning with reward signals derived from the discriminator's outputs. This work adopts this method in the context of LLM alignment and evaluates it empirically on the Harmless and Helpful dataset. Experiment results show that the proposed method performs better than or on par with the SFT baseline and learning from human annotated preference data.

### Strengths
This paper does a good job at interpreting LLM alignment under the learning from demonstration framework. It successfully frames the alignment problem in the language of distribution matching. The idea of using the reverse KL distance follows naturally.

The authors identify the heterogeneity problem in the naive adoption of the discriminator-as-reward method and propose the Init-SFT RM as a solution to mitigate the heterogeneity gap. Init-SFT RM demonstrates strong performance in the experiments. This idea provides insights into learning from demonstration and can be applied to a broader class of problems beyond LLM alignment.

### Weaknesses
Important details of the method is missing from the main text. Section 3.2 talks about extrapolating the learned learned reward models but does not provide any detail on how it works in the context of alignment. Perhaps as a consequence, the results presented in Section 4.3 are confusing to me. It looks like the only difference to Section 4.2 is the evaluation metric being GPT4 as a judge rather than the golden reward model.

Another weakness of this work is the lack of understanding of the behavior of the proposed method. The distinction between forward KL distance and reverse KL distance lead to two different methods in SFT and discriminator-as-reward. The authors also discussed the mass-covering and mode-seeking behavior in Section 3. One natural question to ask here is how it impacts the behavior of the alignment algorithms and if they yield different outcomes. However, the discussion in Section 4 is rather hand-wavy. The authors simply characterize the harmless dataset and the helpful dataset as less divergent and more divergent. I think a deeper analysis on the mass-covering and mode-seeking behavior in alignment can greatly improve this work.

In terms of writing, citation format is misused through the manuscript. Please proofread the paper carefully and use the proper citation command (e.g., \citep{} vs \citet{}) in the revision.

### Questions
1. Could the authors clarify on why this work falls into the inverse reinforcement learning category? I might be wrong, but my understanding of inverse reinforcement learning is about uncovering the underlying reward function from expert trajectories. This work is not about finding the hidden "true reward function" but about matching the demonstration distribution. Thus I am confused by the use of the term "inverse reinforcement learning".

2. In a typical alignment pipeline, learning from annotated preference data like RLHF comes after SFT. RLHF often yields mode-seeking distributions in contrast to SFT. Could the authors comment on the compatibility of the proposed method and RLHF? Should we expect RLHF to provide further improvement given that the AfD method is already mode-seeking?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Alignment from Demonstrations (AfD), a new method for aligning large language models (LLMs) using high-quality demonstration data rather than traditional preference-based reinforcement learning from human feedback (RLHF). AfD addresses issues of noisy labels, cost, and privacy by framing alignment within a Markov Decision Process, applying insights from forward and inverse reinforcement learning to create a computationally efficient, trajectory-based mechanism. The approach is validated through theoretical and empirical analyses, showing improvements on “Harmless” and “Helpful” tasks with the Anthropic HH-RLHF dataset.

### Strengths
1. **Innovative Use of RL Concepts:** The authors effectively integrate RL concepts—such as inverse RL, reverse KL, and forward KL divergence—into the LLM alignment framework. This combination with RLHF provides a fresh, rigorous perspective on alignment, enriching AfD’s theoretical foundation and adaptability.

2. **Reduced Dependence on Preference-Based Data:** By bypassing preference data requirements, AfD proposes a scalable alternative that minimizes interaction with human annotators while still achieving alignment, making it potentially more feasible for large-scale applications.

### Weaknesses
1. **Overly Complex Presentation:** The paper’s presentation is somewhat dense, with extensive theoretical detail that can make it harder to grasp the core contributions. A more streamlined focus on the main insights and practical implications of AfD could enhance clarity and accessibility for readers. The current structure buries the key novelties within a large amount of background material, making it difficult to quickly assess the unique value proposition of the proposed method. The theoretical derivations, while rigorous, could be presented in a more digestible manner, perhaps by relegating some of the more intricate details to an appendix. This would allow the main text to focus on the core mechanics and results of AfD, improving the overall readability and impact of the paper.

2. **Potential Overlap with Existing Methods:** The unique contribution of AfD relative to SPIN isn’t entirely clear. SPIN leverages a DPO-like objective to align LLMs directly without relying on a reward model, while AfD introduces alignment through a reward model. Clarifying the specific advantages or improvements AfD provides over methods like SPIN would strengthen the paper’s case for its distinct value. The paper needs to more explicitly address how the explicit reward modeling in AfD leads to different outcomes compared to the implicit reward modeling in SPIN, especially in terms of the final policy's performance and robustness. A more detailed comparison, perhaps including a theoretical analysis of the differences in the optimization landscapes, is needed to establish the novelty of AfD.

3. **Efficiency Clarification Needed:** Although the paper suggests that AfD offers greater efficiency than traditional RLHF, it’s unclear where these efficiency gains are realized. The pseudocode presented appears similar to RLHF workflows, with steps involving reward model training and optimization. Providing more concrete details on how AfD reduces computational overhead or training time compared to RLHF would clarify the practical benefits of this approach. The paper should specify which aspects of the AfD process contribute to reduced computational costs, such as fewer training iterations, smaller model sizes, or more efficient data usage. Without these details, the claim of increased efficiency remains unsubstantiated and weakens the overall argument for AfD.

### Questions
1. Could the authors clarify why they chose to rely primarily on the golden reward model for evaluation rather than using GPT-4 as a critic throughout in Section 4.1? Would the golden reward model alone provide a sufficiently fair or robust assessment of alignment performance, especially given GPT-4’s nuanced evaluation capabilities?

2. Could the authors clarify the key distinction between AfD and SPIN, particularly regarding their reliance on reward models? From my understanding, SPIN uses a DPO-like objective to align LLMs directly without a reward model, whereas AfD relies on a reward model for alignment. Given this, could the authors elaborate on the specific advantages AfD provides over SPIN in terms of contribution to the field?

3. The authors mention that AfD is more efficient than traditional RLHF methods, but it would be helpful to understand precisely where these efficiency gains come from. Could the authors specify which parts of the AfD process contribute to this claimed efficiency, particularly in comparison to standard RLHF?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors cast LLM alignment as an imitation learning problem, opening up the possibility of learning from demonstrations alone and leveraging insights from inverse RL.

### Strengths
- This is an exceptionally well-written paper with crystal-clear exposition and take-aways -- kudos to the authors!

### Weaknesses
 - (Minor) RLHF is usually framed as KL-constrained /MaxEnt RL, rather than standard RL problem formulation in Eq. 2.

- (Minor) Another good citation for intransitive preferences in RLHF might be https://arxiv.org/abs/2401.04056.

- I would argue that the fact that SFT is BC is fairly well known. It also doesn't seem that surprising that doing SFT on data generated by a super high quality model works well -- the question is of course how we train such a powerful supervisor model in the first place, for which preference data still appears to be neccesary. So, it's hard for me to give many points for novelty for that section of the paper.

- For the most preferred RM strategy (comparing $\pi_{SFT}$ to $\pi_{init}$) , we know the optimal discriminator in closed form -- it is precisely $d^{\star}(x, y) = \log \pi_{SFT}(y|x) - \log \pi_{init}(y|x)$ (if a logistic loss is used, otherwise could be the density ratio in Eq. 9). I don't see the added value in actually learning a separate discriminator for the best-of-N sampling procedure -- it seems like we could only do worse rather than using the log ratio.

- It is a bit disappointing that the final policy requires a BoN step -- I would have liked to see the results of proper policy optimization procedure on the learned RMs.

- I'm not entirely convinced by the argument that BC is only action matching, and not trajectory matching. The KL divergence between expert and learner trajectory distributions can be expanded, and the dynamics cancel out, leaving the standard BC objective. Thus, BC is always minimizing forward KL between trajectory distributions. The authors should clarify the distinction they are trying to make here, as it is not clear why one would care about explicitly minimizing occupancy measure divergence when trajectory matching implies occupancy matching.

### Questions
1. If it is computationally feasible, could you compare to the closed form for the optimal discriminator in your BoN experiments?

2. If I am understanding correctly, if you used the "golden" RM for BoN, you'd get a win rate of 1?

3. Also, is the model you're sampling from here just the result of SFT on the demos from $\pi_{\beta}$, aka $\pi_{SFT}$? If so, is their a theoretical interpretation of the effect of the BoN procedure with the "closed form" discriminator I mention above?

4. Could you provide more explanation for why the win rate goes down with higher N for several lines in figure 4?

5. If you have space, could you move up the comparison to SPIN to the main paper? I think it is quite interesting and under-appreciated in the broader community -- I have struggled to convince people of precisely the point you are making.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents AfD, a sort of framework for learning from demonstrations in LLMs. The authors do a number of different experimenst within this framework on a number of different methods.

### Strengths
* The work attempts to unify a number of diverse ideas, which is helpful
* The work makes nice use of different colored boxes so things can easily be found.

### Weaknesses
 **Novelty**
I am unsure what exactly is novel in this work. To my knowledge nothing the authors introduce is explicitly new, or has new experiments.
* Sec 2.2: This MDP breakdown for LLMs is well known 
* Sec 3.1: It is well known that SFT = BC
* Sec 3.1: I have not looked into the descriminator objective to see if it is in prior work, but the authors don't use it in experiments.
* Sec 3.2: The idea of using the model generations as negatives is done in SPIN and in DITTO (Show don't tell, Shaikh et al.) DITTO also does something similar to this paper by SFTing the model first before sampling.
* Sec 4.1: These experiments show SFT > RLHF on the same number of demos. I don't find this surprising, similar results are also in Shaikh et al.
* Sec 4.2: I think the section may be where the authors find novelty?

Overall, the paper seems to focus a lot on unifying different ideas that have existed for a while. While this is OK, the paper is not written as if it were a survey and at present it sounds like the authors are claiming AfD to be some new framework that has not been extensively studied before.

**Writing**
The paper is a bit hard to follow since there are so many subjects. I was initially confused as to what was being evaluated in each experimental sesction. For example, it was initially unclear to me what the different baselines were in Sec 4.1. 

**Experiments** 
* the experimental results at present do not seem compelling.
* Sec 4.1: It makes sense that SFT with demos does better than RLHF. The amount of data isn't reported on however, and so its unclear what the cost of data collection vs performance tradeoff is.

**Missing Citations**
This work brings together a lot of different ideas, which is great, but the authors seem to miss a ton of related work which has already covered very similar ideas:

* IRL: Ziebart is the OG in maxEnt IRL.
* From r to Q* by Rafailov et al. - Token level MDP
* Show don't tell: Aligning LLMs with demonstrated feedback by Shaikh et al has very similar ideas
* Preference Fine-Tuning of LLMs Should Leverage Suboptimal, On-Policy Data by Tajwar et al. covers mode seeking behavior.
* Imitating language via scalable inverse reinforcement learning by Wulfmeier et al for IRL on LLMs

### Questions
Can the authors summarize the main contribution of the work? Is there something I am missing?

### Soundness
2

### Presentation
2

### Contribution
1
