# Direct Imitation Learning: RLHF Secretly Performs Imitation Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
This work studies the alignment of large language models with preference data. We address this problem from a novel imitation learning (IL) perspective. We establish a close connection between alignment and imitation learning, which shows that existing alignment objectives implicitly align model and preference data distributions. Built upon this connection, we develop a principled method DIL to
directly optimize the imitation learning objective. DIL derives a surrogate objective for imitation learning with direct density ratio estimates, allowing effective use of preference data. DIL eliminates the need for complex adversarial training required by current IL methods, and optimizes the IL objective through simple density ratio estimation losses, achieving lightweight and efficient fine-tuning for large language
models. This paper provides a unified imitation learning perspective on alignment, encompassing existing algorithms as special cases while naturally introducing new variants. Bridging IL and RLHF, DIL opens up new opportunities to improve alignment by leveraging tools from imitation learning. Extensive experiments demonstrate that DIL consistently and significantly outperforms off-the-shelf methods on
various challenging benchmarks, including Open LLM Leadboard and AlpacaEval 2.0. Code for DIL is available at https://github.com/Code-DIL/DIL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper makes a connection between various approaches for RLHF of large language models and imitation learning. In particular the authors re-derive a well known connection between probabilistic inference and reinforcement learning which associates the reward function with the energy of a Boltzmann distribution (see e.g. [1] for a good review of all the related methods and derivations) for the special case of RLHF.
From this perspective classical reward model learning can be derived as matching the energy to the generated responses with highest reward. Based on this the authors then derive a surrogate objective (DIL) that is closely related to DPO and other RLHF algorithms that exist, but which makes less assumptions on the form of the reward model. They show empirical evaluations on language modeling which match/gives slight improvement over DPO.

[1] Levine, Sergey. "Reinforcement learning and control as probabilistic inference: Tutorial and review." arXiv preprint arXiv:1805.00909 (2018).

### Strengths
- The connection between RLHF and imitation learning approaches is highly relevant to the community and the first part of the paper (background and initial derivation up to Eq.12-14) is well presented and leaves the reader with a condensed and improved understanding of how different existing algorithms relate (although perhaps more references to the literature could help, see weaknesses below).
- Any improvement over DPO (which is perhaps the predominant algorithm at least for offline RLHF from fixed datasets) is relevant to the community.
- The benchmarks used are open and relevant and at reasonable scale (i.e. 7B models)

### Weaknesses
 - My first main gripe with the paper is that the idea that RLHF in it's entirety is performing imitation learning seems to stand on shaky foundations. A lot of leaps from one objective to another are required to arrive at this conclusion and a lot of the nuances in the differences between different objectives get lost along the way (that are already well discussed in the literature see e.g. Sergey Levine's review and also existing literature on offline RL as probabilistic inference). For example, the title says "RLHF secretly performs imitation learning" then up to Eq. 12 this thread is followed closely, and I find the connection that is made between reward model learning and the imitation learning perspective insightful, however directly after the authors make a leap to knowledge distillation / minimizing the reverse KL, which then attains the actual RL objective. This objective then is no longer directly related to learning from a dataset of reference or "chosen" examples (as would be the case in imitation learning) but instead can be understood as imitating an optimal policy (and not any policy that generated the dataset) on the state distribution induced by the currently learned policy (see also [3]). It thus really is RL (and not just imitation learning) and has to "deal" with all the problems RL comes with, i.e. exploration of the energy landscape of the optimal policy is required, premature convergence could be an issue etc.. The fact that the energy itself is given by a reward model that comes from matching chosen examples on a pre-collected dataset has no bearing on this. This is easy to see as depending on the temperature (which also pops out wihtout explanation) chosen in Eq 13. the policy may collapse to matching a single mode of the energy model but may also result in much higher energy / better reward than the chosen policy. The authors do discuss some of these nuances below in a short section on why SFT (which uses a forward KL) might underperform the reverse KL approach. But all this does is it leaves the reader with the impression that the authors painted too broad a picture to derive a connection that then, in practice is not relevant. This could be rectified by perhaps framing the paper as "RLHF can be seen as imitating an optimal policy based on human preferences" and toning down some of the quite strong language, e.g. "learning without an RL loop" etc.
- The paper seems to be derived backwards as some of connections made feel slightly contrived upon reading. E.g. the jump from the original objective to knowledge distillation mentioned above. The steps taken to arrive at a DPO like objective from density ratio estimation etc. The paper requires a lot of steps to arrive at a simple algorithm that the authors probably had in mind from the get-go and started from.
- The knowledge distillation connection seems tenuous (and already known), it seems more straightforward to think of the entire process as imitating a better policy as in MARWIL [2] or as chaining a specific variant of an improvement operator and distillation as already derived in detail for many different variants in [3].
- A lot of the derived formulas and connections are already known in the literature but this is often not explicitly stated, e.g. "
In this section, we connect RLHF to the imitation learning framework. We show that RLHF is a special
case of imitation learning problem by defining the following specialized energy-based mode" in front of Eq 9, which very clearly is already derived in the DPO paper and literature on RL as probabilistic inference. It is fine to re-state such derivations but then please say: we built on a well known connection between RL and energy based models/probabilistic inference.
- The key innovation that the paper hinges on seems to be the approximation of the log ratio between chosen and current policy but the derivation seems very ad-hoc and on shaky foundations. To be explicit: in order to arrive at their Eq. 21 (and thus Eq 24 which is their DIL objective) they make the assumption that the reference policy is the same as the policy that generates the rejected samples only and disregard any terms on the positive examples; i.e. "Here, we use the set of rejected responses y_l ∼ π_ref(y | x) to approximate the expectations under π_ref(y | x)". This is simply a wrong assumption. I do not know why the authors have chosen to make the assumption, but it feels like a contrived way to come to Equation 24 and form a connection to a DPO like objective. 
- The results are on relevant benchmarks, but the improvement over DPO seems minor in most cases. In this scenario what would be nice would be to analyze qualitative differences, e.g. examples which DIL seems to have stronger performances on compared to DPO. Or an analysis on how closeness (in KL) wrt. to the reference policy evolves during the course of optimization for different algorithms and how this affects performance. Or a plot that have the DIL objective on the x axis and win-rate (over different models, e.g. reference policy and DPO) on the Y-axis.

### Questions
A discussion and answers regarding the weaknesses listed above would be appreciated. And if the authors can provide some more rationale and clean-up the derivations the score could be improved.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- This paper reinterprets preference alignments methods like RLHF and DPO as special cases of a more general imitation learning objective. 
 - They mathematically show how the RLHF and DPO objective functions fit within a general imitation learning framework. 
 - They develop a new alignment method DIL based on imitation learning with the objective as minimizing the reverse KL loss between the optimal policy and current policy and derive a preference data based learning objective which suppresses the likelihood of generating dispreferred responses while increasing the likelihood of generating preferred responses. 
 - They empirically show that DIL results in a better policy compared to other offline alignment methods across reasoning and alignment benchmarks.

### Strengths
- This paper is well written and presents intriguing connections between imitation learning and human preference alignment. 
 - They derive a new alignment framework based on imitation learning and show empirical improvements on existing baseline.  
 - DIL shows significantly better training dynamics compared to SimPO by ensuring that the likelihood of generating chosen responses is maintained.

### Weaknesses
 - The amount of data needed for satisfactory alignment with DIL compared to other methods is not clear. The authors claim that DIL is more efficient, so it would be nice to see some metrics that measure this, specifically in terms of the number of preference pairs required to reach a certain performance level compared to methods like DPO or SimPO. It's unclear if the efficiency gains are in terms of computational cost or data requirements, and this needs to be clarified with empirical data.
 - All the models in the experiments are smaller (<10B parameters) so it’s not clear how effective DIL would be for larger models. The scaling properties of DIL need to be investigated, and it's important to understand if the observed improvements hold when applied to models with significantly more parameters, as the dynamics of training can change drastically with model size.


### Questions
- Since DIL doesn’t suppress the likelihood of dispreferred responses as much as SimPO, how does this affect alignment from a safety perspective? Is the model more prone to generate harmful responses?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new method called Direct Imitation Learning (DIL), which is derived based on an imitation learning perspective on the alignment problem. Specifically, instead of minimizing the forward KL divergence as in SFT, DIL aims to minimize the reverse KL instead. This turns out to require estimating the density ratio $\frac{\pi_{\mathrm{chosen}}}{\pi_{\mathrm{ref}}}$, which the authors show can be done through a Bregman divergence objective. Then, through a similar change-of-variables trick as used in DPO, the authors show that this reward objective can be instead minimized directly in terms of the relevant policies. Hence, the final objective directly optimizes $\pi_{\theta}$ through the Bregman divergence objective. 

The authors also show that PPO and DPO can be seen as special cases of the proposed imitation learning formulation. Specifically, reward learning in RLHF can be formulated as a forward KL between $\pi_{\mathrm{chosen}}$ and $\pi_{\phi}$, and the RL step can be seen as a knowledge distillation process (through minimizing a reverse KL) into a final policy $\pi_{\theta}$. 

From the experiments side, the authors use the UltraFeedback Binarized dataset for evaluation on the Open LLM Leaderboard and show DIL is generally the best method across the board. For dialogue generation and summarization they use the Anthropic HH dataset and the Reddit TL;DR dataset and show through win rates (as judged by GPT-4) that DIL generally performs best against the SFT, Chosen, and Average responses. Finally, the authors also investigate the likelihood patterns of DIL and SimPO, which generally seem to show that the likelihood of chosen responses stay roughly the same while the likelihood of rejected responses goes down. This is unlike SimPO for which the likelihood of chosen responses also decreases.

### Strengths
The paper has several strengths:
1. The paper provides new mathematical connections between imitation learning formulations (various forms of forward and reverse KL optimizations) and previously established RLHF methods like PPO and DPO. As far as I'm aware, these connections are novel and have not been highlighted in past work, making them valuable insights for the community to further build on. 
2. To optimize the proposed imitation learning objective, the paper integrates ideas from density ratio estimation [1] and a change-of-variables approach [2] (rewards -> policies) to directly learn the target policy $\pi_{\theta}$, avoiding complexities such as adversarial training.
3. Strong empirical results: the new method DIL seems to generally outperform all baselines in both the Open LLM Leaderboard as well in the summarization and dialogue generation settings.

[1] Masashi Sugiyama, Taiji Suzuki, and Takafumi Kanamori. Density-ratio matching under the bregman divergence: a unified framework of density-ratio estimation. Annals of the Institute of Statistical Mathematics, 64:1009–1044, 2012.

[2] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in Neural Information Processing Systems, 36, 2024.

### Weaknesses
The paper has several weaknesses:
1. While the empirical results seem to consistently outperform prior methods, I’m a bit worried about the statistical significance since the margins seem rather small sometimes (e.g. for Table 2, the improvements are almost always smaller than 1 percentage point). Could the authors include some significance tests or at least standard errors / CIs to provide a better sense of the significance of these improvements?
2. The exposition of the math/theory in the paper could have been a bit clearer (section 4). It took me some time to understand what actually is the final objective that DIL optimizes, and how it came to be. This is because, for example, at the end of section 4.3 the authors state “With the estimated density ratio reward, the surrogate imitation learning objective in Equation (17) can then be solved with any RL algorithms.”, which initially made it seem like DIL would have to resort to RL optimization anyways. But then reading section 4.4 it turns out that’s not what happens and there is actually a different objective that’s maximized (eq. 24). Maybe one thing that could help here is to add a summary box either at the beginning or end of section 4 that summarizes the key steps to go from the general DIL objective (eq. 16) to the formulation in eq. 24. 
3. Some parts of the paper require further clarification - please see the Questions section for this.

### Questions
1. In Section 5 under the models paragraph, the authors state “For fine-tuning on UltraFeedback Binarized dataset, we use Zephyr-7b-SFT (Tunstall et al., 2023) and Llama3-8b-SFT used in (Meng et al., 2024) as our base models.”, but then in Table 2 the top results are labeled as Mistral-7B-Base. Should that be Zephyr-7B-SFT instead?
2. In Section 5, the authors mention KTO as part of the baselines, but it doesn’t seem the result tables include it? Also, SLiC is included in the result tables, but is not discussed in the baselines paragraph?
3. Could the authors include the base model (SFT) performances in Table 2?
4. In Table 3, what is the difference between Chosen and Average?
5. In Table 3, it might be interesting to compare win rates of DIL directly with DPO or other baselines. Is there a reason the authors didn't include this?
6. At the end of section 6.1, the authors state that “We hypothesize that these improvements can be attributed to avoiding the BT assumption and preventing the decrease in the likelihood of chosen responses.” Could the authors elaborate on why avoiding the BT assumption could lead to these improvements? Do they have examples in mind where BT might not be the right model?
7. I’m a bit confused as to how $\pi_{\mathrm{chosen}}$ is defined. Is it essentially defined to be the policy that, given a preference dataset of $ (x, y_w, y_l) $ triplets, was responsible for generating all the $y_w$ pairs?
8. In the beginning of section 4.3, the authors state that “In the tabular setting, we can directly compute $\pi_{\mathrm{ref}}(y | x)$ and $\pi_{\mathrm{chosen}}(y | x)$.” Could the authors please elaborate on this a bit? It’s not clear to me what the tabular setting here means.
9. Is the Y-axis in figures 1 & 3 the *negative* log likelihood? And for the margins figure on the right, is it a difference of negative log likelihoods? This could use some better labeling. Putting the model name on the y-axis is a bit confusing, and might be better put in the caption.
10. At the end of section 4.1: “achieving this in practice requires full data coverage and infinite models that are rarely met”. What is meant by “infinite models” here?
11. In the paragraph right after equation 22, what’s $\pi_{\mathrm{data}}$?
12. In the paragraph right after equation 22, why is there no log before the reward $r$ in $Z(x)$? Shouldn’t there be since there is one in equation 22 as well?
13. In the paragraph after equation 22, the authors state “This characteristic, determined by the reward definition in Equation (17), is super beneficial as it allows our imitation learning to theoretically generalize to a broader class of loss functions beyond the pairwise BT preference model used in DPO.”. Could the authors please elaborate on this? What does "this characteristic" refer to? And how does it allow the imitation learning to generalize to a broader class of loss functions beyond BT?
14. At the end of section 4.5 the authors state “Specifically, we demonstrate that DPO also falls under the imitation learning objective in Equation (16) and essentially employs the CPC method for density ratio reward estimation.”. While I agree CPC indeed estimates the correct density ratio, it’s unclear to me that this is used in equation 27. Specifically, the learned $f^*$ from equation 26 doesn’t seem to show up in equation 27?
15. Towards the end of 6.1, the authors state “Notably, we observe DPO and SimPO hurt the overall performance in most reasoning-heavy tasks such as GSM8K”. Is this compared to some base model performance? And if so, where is this reported?
16. This statement in 6.1 could use some clarification: “For instance, on LLama3, the improvements are notable on the Math and AlpacaEval 2 benchmarks, with relative gains exceeding 7.5% and 18.2%, respectively.” Is this for DPO or SimPO?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper generalizes preference learning or RLHF frameworks to an imitation learning framework, (DIL). Using this framework they propose multiple offline preference learning methods with different preference modeling such as Bradley-Terry for DPO and LSIF for the best DIL model. Moreover, its performance on benchmarks like Alpaca Eval 2 and Open LLM leaderboard is considerably better than other offline preference learning objectives.

### Strengths
* The paper is well-written and easy to follow.

* The first paper to connect RLHF with imitation learning if not mistaken

* Very strong results against popular DPO-variants

### Weaknesses
## Is RLHF a form of imitation learning?
Paper frames reward learning as imitation learning and RL as knowledge distillation (KD) and I dont think either of them is correct.

RL: Equation 13 is the reverse KL between the behavior and optimal policy however knowledge distillation is forward KL between teacher (optimal) and student(behavior). KD (forward KL) is distribution fitting or mean seeking whereas reverse KL  is mode seeking which makes the policy focus on high-reward regions rather than fitting the entire distribution with forward KL as in SFT. Overall, the KD claim by the paper is incorrect. Lastly, equation 13 is a known result from DPO paper which is the penultimate step of the optimum solution of equation 14th.


Reward Learning:

In standard RLHF, the reward model is a separate LLM with an additional MLP to predict the scalar reward. So by training a reward model, one does not imitate the expert or optimal policy. What we are doing is fitting a reward model to a predetermined preference model however the caveat is that the optima policy trained by the RL can be parametrized by the reward model trained with which was already proven by the DPO. Lastly, DPO parametrizes the reward model in terms of the policy so when the reward learning objective is trained, we obtain the actual policy.

On the other hand, this paper defines a Boltzmann distribution $\pi_\phi$ (equation 9) in an EBM framework which is the optimal policy induced by the $r_{\phi}(x,y)$. This distribution is maximized on the chosen preferences generated by the $\pi_{expert}$ or imitates $\pi_{expert}$. Following derivations leads to reward likelihood training objectives whereas I am unsure whether $\pi_{ref}$ approximation is free because it introduces rejected responses while IL objective only minimizes on chosen preferences. Nonetheless, this derivation is possible because the $pi_\phi$ has a reward equivalence whereas it does not tell anything for other forms of policy. Overall, I would interpret it as imitating reward rather than policy, not vice versa.

## Direct Imitation Learning
I dont think DIL is novel because it is the backtracking of the derivation of the DPO objective. After all, the 16th equation is the same as the 14th equation of the DPO without the partition and assuming $\pi_{expert} = \pi^*$. DIL is redefining the reward function of DPO, excluding the density ratio estimation part. All in all, I believe this part(excluding density ratio) is already present in DPO.


### Questions
Q1) You mention that DIL does not depend on Bradley-Terry but you introduce new reward training with different objectives such as LSIF, UKL, and BCE which are essentially replacements for BT, so doesn't the DIL still rely on some preference modeling assumption?

Q2) In 6.3 you discuss learning dynamics DPO, SimPO, and DIL however Figure 3 does not have DPO, is the discussion from some other paper?

Q3) Do you have additional results on MT-Bench or Arena Hard?

### Soundness
2

### Presentation
2

### Contribution
2
