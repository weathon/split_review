# Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Reward Models (RMs) are crucial for aligning language models with human preferences. 
Currently, the evaluation of RMs depends on measuring accuracy against a validation set of manually annotated preference data.
Although this method is straightforward and widely adopted, the relationship between RM accuracy and downstream policy performance remains under-explored.
In this work, we conduct experiments in a synthetic setting to investigate how differences in RM measured by accuracy translate into gaps in optimized policy performance.
Our findings reveal that while there is a weak positive correlation between accuracy and downstream performance, policies optimized towards RMs with similar accuracy can exhibit quite different performance.
Moreover, we discover that the way of measuring accuracy significantly impacts its ability to predict the final policy performance. 
Through the lens of the Regressional Goodhart effect, we recognize that accuracy, when used for measuring RM quality, can fail to fully capture the potential RM overoptimization.
This underscores the inadequacy of relying solely on accuracy to reflect their impact on policy optimization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Research question of the paper is on how we should evaluate the quality of the reward models for RLHF. The paper conducts experiments to evaluate the evaluation metrics for RMs and show interesting findings that some confirm the intuition and the other are somewhat counterintuitive. The paper concludes that there should be more care on evaluating RMs instead of relying on a single benchmark.

### Strengths
Overall, the paper presents empirical results that evaluate the metrics of RMs, which the community has previously intuited but not with rigorous scientific evaluation. The experiments are designed to test hypotheses incrementally, helping the RLHF community build a comprehensive body of knowledge on RM evaluation.

- The paper tackles the question that the alignment research community needs to know the answer to.
- Table 2 is interesting as it shows counterintuitive results. One would guess that the RM should be evaluated for the samples generated from the policy to be trained. The paper also shows that instead, we should sample multiple responses and choose a pair of responses to evaluate the accuracy with care.

### Weaknesses
I don't see any critical weaknesses for the paper. If I were to come up with the weaknesses:

- Although policy regret is often referred to in the paper, its formal definition is not clearly stated. It would be better to have an equation defining the regret. Even if we do not have a way to compute it, the goal of the research is to estimate it so I would say that it is worth clarifying its definition formally.
- The scope of the paper is to show that the current evaluation scheme is not enough (which is a good enough contribution). The paper does not provide a solution to the problem of how we should evaluate the RMs (which I think is asking too much).
- The texts in Figures are a bit too small to read. It would be nice if it is a bit larger.

### Questions
- Randomly flipping some percent of the trains in the training dataset is a trick to make a pseudo proxy reward model used in several papers (e.g., AlpacaFarm; Dubois+ 2024). In reality, it is more natural to think that some kinds of instructions have more flips and others have less. I'm a bit concerned that the findings of the paper might only hold true due to the synthetic error model. It would be helpful to see whether this possibility is addressed or refuted (or let me know if I missed it).

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper revisits the soundness of current reward model evaluation procedures, which assess the accuracy of RMs over datasets of held-out preference data, showing they present the flaw not to necessarily translate into downstream improvement for models going through RLHF in a synthetic setting. They propose to improve RM evaluation by increasing the number of responses per prompt and/or (if available) using the rank of model responses to select preferred and rejected responses when building preference datasets.

### Strengths
The problem tackled is well introduced and presented.

Contributions are clear.

Having a synthetic and cheap setting that correlates with more realistic experiments is quite valuable for the research community (but see doubts expressed below).

Some very interesting findings in this setting:
* weak correlation between RM accuracy and downstream policy performance/regret
* correlation increase by increasing the number of answers per prompt
* correlation increase by picking answers based on their rank
* correlation increase by increasing the number of test samples

EDIT: I raised my score accordingly after convincing updates from the authors.

### Weaknesses
The key limitation from my perspective is that we have currently no solid evidence that the study will translate to real settings: diverse, heterogenous RMs potentially trained on different datasets. While this would be infeasible to run as many experiments and ablations as in the synthetic setting, showing that there is imperfect correlation between RewardBench scores and relevant, downstream RLHF settings (more generally, that some findings from the synthetic study do replicate) would make the paper much stronger. At least showing that RewardBench rankings are not preserved after downstream BoN / RLHF would be a great addition. 

In that regard, the fact that RMs used in the experiments are essentially the same architecture / same init / same hyperparameters trained on very similar data (i.e. up to random flips) is concerning: this is not capturing the diversity of RMs being trained and evaluated on popular benchmarks such as RewardBench. Authors should do a better job at showing that this is enough to capture phenomena that replicate in real settings.

Also, what about using a larger RM as proxy-golden? Seems like the default practice and would make for a more principled study, as this would likely reduce RM similarity with the proxy-golden RM.

Another limitation is that it is currently hard to evaluate whether the correlation increase authors get from applying the proposed improvements are significant or not. What is the correlation between proxy-golden RM accuracies on train and test data? This value would constitute an upper bound of what level of correlation is realistically achievable and provide a reference value that would alleviate the above concern.

Several ablations are missing AFAICT:
* Why is correlation higher for BoN vs PPO? Authors state that “This is expected, as BoN is a more localized and stable optimization algorithm, making it more predictable by reward model error.” I think this might be due to using unconstrained PPO (i.e. without KL regularization), which begs for an ablation study.
* Did authors conduct any form of investigation on low accuracy but high NDR PPO policies from Fig. 3 b)?
* It is currently unclear whether adding more samples (i.e. more than 5000 samples) in Fig 6 would improve correlation or instead saturate? This experiment would be a compelling addition to the study.
* Regarding using additional responses per prompt: the question of whether the policy matches or not the downstream policy matters or not is not studied in the current state
* What about using a different set of prompts to quantify whether the difference between test RM prompts and test RL prompts is meaningful?

Notations and equations:
* equation 2 uses $\pi’$ on LHS but not present on RHS -> please fix
* what is \pi_0 in equation 2? I suppose it is the initial policy, but this should be clarified in the main text
* is the regularization term from Equation 3 known/standard? if so, clarifying and including a citation to prior works is warranted 

Clarity can be improved a lot:
* “on the widely adopted benchmark dataset (Lambert et al, 2024)” -> authors should name it (RewardBench)
* “Regarding response distribution, we find that the rank of the responses can be more influential rather than the model from which it is sampled.” -> unclear sentence
* “The translation from the RM error to the policy regret can be seen as the result of the reward model overoptimization” -> “imperfect translation”? or “weak correlations”? unclear sentence for now
* “ the difficulty of constantly controlling optimization pressure” -> what do the authors mean by pressure here?
* is the Normalized Drop Ratio (NDR) a contribution of the authors’ work? if so this should be clarified in the text
* the use of NDR (as opposed to difference in average rewards) should be motivated better in the text, even if easy to interpret
* Fig 3 is a bit hard to read (dots / text could be made bigger)
* /!\ Using more responses per prompt to improve RM evaluation -> This is a key aspect of the paper that is quite unclear in the current state! As of now the details are in the appendix, but the main text should be much clearer about this aspect, notably that the fact that we have a golden-proxy RM allows us to estimate a correlation between the proxy rewards and the golden-proxy rewards.
* “Can we achieve a higher correlation by sampling responses specifically from the model used for downstream optimization? To examine this question, we construct test datasets with responses solely from different models.” -> I find these sentences puzzling as they seem to contradict each other, please clarify

Writing is sub-par in the current state, see examples:
* “The inherent difficulty of constructing an ideal RM require”
* “The latter, while straightforward, remains the question of whether such evaluation accurately predicts the performance of the downstream optimized policy”
* “A cartoon of RM error and policy regret”
* “We begin by investigate the influence of prompt and response distributions”
* “The correlation between policy regret and accuracy on datasets constructed from responses of different ranks assessed the by Spearman coefficient”

with more in the text.

### Questions
See questions above as well.

Fig 3 shows high correlation between accuracy and BoN perf at high accuracy. Do authors have an intuition on why that might be the case? Also, no RMs have an accuracy between 0.75 and 0.8, which might indicate a lack of diversity in the RMs trained, echoing an earlier remark on experimental design.

“As shown in Table 2, this approach does not consistently improve upon the original RewardBench dataset. This result suggests that sampling responses from the model used for optimization may not be necessary to achieve a strong correlation between accuracy and policy regret.” -> this is quite surprising. Do authors have an intuition here?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper questions the current approach to evaluating reward model performance, which is based evaluating downstream policy performance and looking at reward model accuracy on the train and eval preference datasets. The relationship between reward model performance and policy performance is explored in the context of policy regret, a new performance metric that examines the difference in policy performance when trained with the true versus inferred reward. Since the true reward is not typically available, a synthetic true reward model is used to conduct the analysis. The reward model and policy performance relationship is measured as the correlation between the reward model's accuracy and the policy regret. Evaluation relies on RewardBench. The authors find a weak positive correlation between the two, and conclude that accuracy alone is a poor proxy for downstream performance.

### Strengths
* Understanding the relationship between our measures of reward quality and policy quality is of vital importance.
* The goal and motivation for the work is well laid out at the start of the paper. The takeaways the reader should expect to have are presented from the start.
* The use of a synthetic ground truth reward function is well motivated and contextualized.
* Different methods for using a ground truth reward function (best-of-n and RL) are compared.

### Weaknesses
**High level**

The main weaknesses for this paper are not overly large and mostly involve clarifications to the text. While not big changes, they are important to address. Some of the conclusions in the main body need to be walked back and made more nuance to fully reflect the presented results. The biggest missing result is information about the relationship between the ground truth reward model and the proxy reward model. 

**Details**

* The experiments are set up such by taking a labelled preference dataset and then randomly flipping labels to create multiple preference datasets. A different reward model is then trained on each version of the dataset. The ground truth reward model is then arbitrarily chosen to be one of those and all others are treated at the proxy. It would be good to quantified the relationship between the ground truth and proxy reward models as part of the analysis. This could be as straightforward as looking at the percentage of agreeing labels in the training data.
* It would improve understanding of the experimental section to describe the RewardBench data and how it is used earlier. The very start of Section 3, would be a good place.
* It would  strengthen the results and analysis to include policy regret information where the ground truth reward is used as the proxy reward. This would help to understand the impact of randomness in policy learning. In practice, is the policy regret 0?
* Some of the statements made early in the paper (e.g. introduce) are difficult to interpret in the absence of having read the whole paper. For example, "...we find that  the rank of the responses can be more influential..." and "...increasing the number of responses per prompt". It would be helpful to add some description about what is meant by rank and what it means to increase the number of responses in terms of the evaluation.
* It is challenging to interpret the results in Figure 4. Adding axis names would be beneficial. 
* The conclusion that "While the correlation on PPO continuously weakens as we paragraph a larger number of prompts", the nuance that this depends on the correlation metric should be called out, especially as no single correlation measure has been identified as "best".
* Please add more descriptions of the different methods used to evaluate Finding 4. Specifically things like "Bo5" where a citation would also be helpful.
* It is not clear how all of the metrics in Table 4 were computed. For example, what is the Pearson corr. measured between?
* The conclusion about the impact of number of responses per prompt does not fully reflect the results in Figure 7 (a). For the smaller annotation budgets, the benefit of extra responses drops off quickly. The trends for PPO should be summarized and described and extra responses are not beneficial.
* The paragraph immediately after "Finding 2" (lines 238 - 244) were not clear to me, so it is difficult for me to assess or validate them. Parts such as "solely from different models" was not clear. It is not clear exactly how the data is different from what was used previously.
* Some small spelling issues, typos, and confusing phrases throughout the paper. These are not impacting my score, would be good for the authors to clean up.
     * line 071 "investigate" -> "investigating"
     * line 089 "This offers valuable for both reward model training...."
     * line 129 "...we focus on a few interested factors and keep the rest fixed" - "interested" -> "interesting"
     * line 134 "...perform investigation..."
     * line 319 "...expect calibration error..." -> "...expected calibration error..."

### Questions
* How do the results here relate to the findings in "Preference Learning Algorithms Do Not Learn Preference Rankings" (NeurIPS 2024)?
* Where does the data used to evaluate the policy and measure policy regret come from?
* How do the results about prompt versus response distributions relate to the paper "On the Limited Generalization Capability of the Implicit Reward Model Induced by Direct Preference Optimization" (Lin et al., 2024)?
* It seems the paper does not account for noise. Why is that not important here?
* In equation (2), what is $\pi_{0}$? Is this the SFT/IFT'ed model?
* What is your motivation for setting the KL penalty to 0 (line 160)?
* For the analysis of Figure 3 supporting the conclusion that  "policy regret can very considerably even within similar accuracy ranges", is it possible that accuracy and NDR exist on different scales making it look like there is more variation along one dimension that the other? Can you report the results normalized so that they fall on the same scale?
* For the results reported in Figure 3, how OOD versus ID is the data for each the reward model and the policy?
* How were the bins that were used to assign response rankings determined? Was the ground truth reward model for that experiment used?
* It is surprising that seeing higher reward samples was not more beneficial. Can you elaborate more on why this is the case?
* For Figure 4, what does it mean when the bin is 0 for both the x and y axis? Does it mean the two responses are of equal rank? In this case, how does labelling work?
* For the results looking at the impact of response rank, how was the label flipping or disagreement with the ground truth reward function's training data accounted for? For the flipped labels spread uniformly over the rank bins? 
* Why is Table 3 not symmetric along the diagonal?
* What is the hypothesis for why extra responses help in the case of BoN and not PPO?
* In "We observed that there should be an approximate linear relationship between them" (line 454), "observed" + "should be" in unclear. You assume? You know? Also how? Why?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper empirically investigates whether "reward model (RM) accuracy" (i.e., agreement with a preference dataset), which is commonly used for evaluating reward models, is a good metric for evaluating reward models. It begins with the premise that the true measure of a reward model is the quality of the policies it produces, and proceeds to investigate the relationship between RM accuracy and the regret of the downstream policy. It does this by synthesizing several "noisy" reward models, which can each serve as both a "gold" reward model providing ground truth labels for both preferences and policy performance, or a proxy reward model (when another RM is the gold reward model). The authors then proceed to conduct several empirical investigations into the RM accuracy vs Policy regret. They conclude that (1) RM accuracy is not perfectly correlated with downstream policy regret, (2) the predictive power of RM accuracy declines as the distribution on which policy regret is measured shifts away from the original distribution, and (3) ultimately conclude that RM accuracy is not adequate as a measure of RM quality.

### Strengths
The research question is a good one. That is, it is known from the RL literature that the best reward models for learning are not necessarily the ground truth reward models (e.g. Singh et al. 2009, Where Do Rewards Come From?), so it seems natural that some proxies of ground truth rewards (well, in case of LLMs, trajectory returns) will be better than other proxies of ground truth rewards --- can we ascertain whether this is the case, and if, so can we find ways to craft better proxies and/or better measures of proxy quality. I think this is an important question of great interest to a variety of researchers. I also think it has not really been studied in the case of language reward models, so it is good to have a paper that prompts the discussion. 

To answer this question, this paper contains several experiments that show the relationship between RM accuracy and downstream policy performance. The questions that drive the experiments are generally interesting. There are a lot of experimental outcomes here, which may be interesting to different researchers. Although some thinking is necessary on part of the reader to understand what the authors are doing, the paper is fairly written through Section 4.

### Weaknesses
Issue: The fact that your hyperparameters for training the policy are held constant does not imply that the policy extraction / learning process is not noisy. So any characterizations of the correlation as being "weak" (L63, L530) or "room for enhancing" (L213) are IMO unsubstantiated, as the upper bound for correlation may be much lower than 1 due to variance in the policy optimization process. This noise also explains why correlation with PPO is weaker than correlation with BoN (which you correctly point out at L190). *So the major issue I have is that, even after reading this paper, I expect RM accuracy to be a better measure of expected downstream policy quality than single seed downstream policy quality.* (and this is the main cause for my low review score; the experiments do not convince me that RM accuracy is an insufficient target for designing RMs)

Although the experiment at L246-256 / Figure 4 is interesting, the descriptions are insufficient to properly understand Figure 4 (which axes is which, how does (a) map on to what you wrote in the text?). Further, what is the practical import of this experiment --- would we need humans to rank multiple samples for this to be relevant? And if so, wouldn't it then be better to just use all the samples as you investigate later on? 

Finding 4... it would be good to provide an intuition for the reader as it was not immediately obvious to me why this is happening. Namely that the number of comparisons (and therefore samples with which to reduce variance) grows factorially in the number of responses. Once stated this way, I would note that past work has used multiple responses/ human labels per prompt, see e.g., Hwang et al. 2023, Sequential Preference Ranking for Efficient Reinforcement Learning from Human Feedback and Wu et al. 2023, Fine-Grained Human Feedback Gives Better Rewards for Language Model Training. (This is not to say Finding 4 is not interesting, but I would still rather see an analysis of how the annotation budget affects the RM accuracy, as opposed to the downstream Policy Regret). This all being said, perhaps if this finding were fleshed out more, to show how you can use it to improve RewardBench, it could be a lot more impactful. 

Section 5: I'm afraid I do not really understand this section. I'm not sure the Goodharting / overoptimization / exogenous variable language is doing much good here (what would be an example of an exogenous variable impacting the relationship, and why is implied by the experiments here?). It seems you are assuming that rewards follow a Thurstone Choice model (whereas most literature assumes Bradley-Terry-Luce; which is fine, they are very close), and then in Figure 8(a) comparing the percentage of reward variance owed to the ground truth reward (vs noise term) to the RM accuracy. What is Figure 8(b) showing? How do we know what $d_\pi$ is in the "actual" setting? I don't understand what the takeaway from Figure 9 should be, if we can't see the reward accuracy, and don't know the sample size under which it computed, etc. There is detail missing here.

Important (but minor review-wise): 
L139: alpha is never specified (except in Fig 9)
L159: n is never specified!
And generally, I think there are details left out / I would not be able to reproduce everything given current manuscript; e.g. what hparams were used for PPO, etc. How are confidence bands in Table 2 computed, etc. 

Minor:
- L141: N x (N-1) pairs
- L48: "human golden reward function" --> "empirical human rewards"  (the human reward 'function' is noisy, and we cannot quantify the error between learned RM and the human reward fn) 
- L50: "the goal of RM eval is to estimate policy regret" (no, it's to estimate the quality of the reward model --- policy optimization introduce a whole range of additional noise / issues -- see commentary above) 
- L429: I would not say the entire translation is due to overoptimization... in fact, there may be NO overoptimization if we do early stopping, right?

### Questions
1. Do you have any potential solutions for the issues you have identified (how do we go beyond RM accuracy)? 

2. Can you clarify if I am missing something re: my major concern above, or make me doubt the view that "RM accuracy is a better measure of expected downstream regret than single seed downstream regret". An experiment that shows insufficient correlation given multiple seeds might do the trick (even if you can't do PPO, you should be able to run this experiment quickly in the BoN setting).

### Soundness
2

### Presentation
2

### Contribution
2
