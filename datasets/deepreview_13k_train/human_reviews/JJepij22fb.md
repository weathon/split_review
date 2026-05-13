# Reward-Robust RLHF in LLMs

- Decision: Reject
- Scores: 5, 1, 5, 6

## Abstract
As Large Language Models continue to progress toward more advanced forms of intelligence, Reinforcement Learning from Human Feedback is increasingly seen as a key pathway toward achieving Artificial General Intelligence. However, the reliance on reward-model-based alignment methods introduces significant challenges due to the inherent instability and imperfections of Reward Models (RMs), which can lead to critical issues such as reward hacking and misalignment with human intentions. In this paper, we introduce a reward-robust RLHF framework aimed at addressing these fundamental challenges, paving the way for more reliable and resilient learning in LLMs. Our approach introduces a novel optimization objective that carefully balances performance and robustness by incorporating Bayesian Reward Model Ensembles to model the uncertainty set of reward functions. This allows the framework to integrate both nominal performance and minimum reward signals, ensuring more stable learning even with imperfect RMs. Empirical results demonstrate that our framework consistently outperforms baselines across diverse benchmarks, showing improved accuracy and long-term stability. We also provide a theoretical analysis, demonstrating that reward-robust RLHF approaches the stability of constant reward settings, which proves to be acceptable even in a stochastic-case analysis. Together, these contributions highlight the framework’s potential to enhance both the performance and stability of LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an approach on building robust reward models (RMs) for stable RLHF. The main idea is to build a Bayesian reward model ensemble to model the uncertainty set of reward functions and then run RLHF with interpolation with the standard RLHF objective and the robust RLHF objective using the minimum reward score from the RM ensemble in the uncertainty set. The authors empirically show that the resulting approach can show gains in most of the language and reasoning tasks. The authors also show some theoretical insights and performed various ablations to show that the proposed method can indeed lead to underestimated reward scores and mitigate reward hacking.

### Strengths
1. The proposed method is simple yet effective. The idea is intuitive and easy to follow. The authors also provided some theoretical justifications on the algorithm, adding up the soundness of the paper.

2. The authors performed thorough evaluations on various benchmarks to show that the interpolation between standard RLHF and robust RLHF can lead to consistent gains across most of the benchmarks, making the paper more convincing.

3. The paper also includes some ablations to show that the proposed method indeed leads to underestimated rewards and can be useful for reducing reward hacking.

### Weaknesses
1. While the proposed method is neat, the difference between the method and previous approaches such as [1] and [2] is small IMO. The authors should discuss the comparisons in more details and also conduct some experiments to compare to [1] and [2] to show the superiority of the proposed algorithm. Without such discussion and empirical evidence, it's not clear if the paper is fully novel and improves over prior works.

2. While the authors show that the method can consistently improve over standard RLHF in various benchmarks, the gain seems relatively small (roughly within 1%-3%). Such small improvement could be just within the error bar of each of the benchmarks. The authors should also report the error bar of the results in the experiment section.

### Questions
see weakness section above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes a reward robust RL objective for RLHF alignment of lLMs

### Strengths
1. The paper addresses an important problem of being robust of uncertainty of learned reward functions.

### Weaknesses
1. Soundness and Writing: The paper lacks a principled approach or theoretical soundness. The paper is full of unsubstantiated claims, a few examples   in chronological order being "line 10: RLHF is a key pathway towards AGI", "Line 24: Reward Robust RLHF approaches stability of constant reward setting", "Line 36: RLHF leading to breakthrough of o1 models, line 48: challenge of both overfitting and underfitting in reward models", "Line 202: Obtaining an ideal RM is almost impossible".
Every statement made in the paper should be substantiated with evidence through a citation, theory or empirical evidence. The paper currently flows as a article rather than a research paper.

2. Improvements on prior approaches: Authors claim in line 147 that prior methods rely on empirical uncertainty estimation approaches. The methods authors propose is still empirical and without any guarantees.

3. Potentially wrong experimental protocol: The toy example in the paper, does not seem to explain that obtaining an ideal reward model is impossible. The situation in the experiment is artificially created to make sure that reward model is hard to learn. More details about experimental protocols are needed in the main paper.
For the main experiment, the experimental protocol is very sparsely explained. For example, what are 800 steps of PPO? are they data points or gradient steps? Where weren't standard training runs for fixed number of epochs done. Why are we comparing performances between epochs before the algorithm has seen all the training data?

4. Proofs that do not explain the phenomena: The proof in section 6.2 dubbed "Stochastic case analysis" are just trivial proofs that RL will not learn with constant reward. It is not clear how they are related to the method proposed in the paper.

### Questions
See weaknesses above.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose modifying the RLHF objective by introducing an ensemble of reward functions. When running PPO, the minimum of the predicted reward values is used.

### Strengths
* The general idea makes sense: do robust learning on the reward function, because there is often a lot of uncertainty over rewards.
* The authors test their method on a wide variety of benchmarks.
* As far as I know, applying robust optimization over the reward function for RLHF is a new combination not used before.

### Weaknesses
A good evaluation of "robust" optimization for RLHF would be useful to the community. However, at present the draft is a bit confusing, and I have a number of questions that I think need better explanation and in-text edits for the paper to cross the bar of publication. 
Specifically, there are several design choices which are not fully explained or ablated, and the method seems a bit complex. You have to train one reward model the standard way, then another ensemble with MSE. The authors haven't shown evidence that this step is important. 
Then, you need to additionally tune the lambda hyperparameter.

Weaknesses with respect to the method:
* The approach seems to be rather involved -- requiring the training of multiple different RMs. First a Bradley-Terry RM, then one trained with MSE.
* Why do the authors have to do this with the MSE loss? It is unclear to me why an ensemble of reward functions trained with the bradley terry model ("MLE" in the authors words) would not demonstrate the same trend.
* I don't udnerstand L791 and eq 8. How is the reward equal to the "mean" plus the action times a variance. The action is a vector of tokens and the reward is a scalar. Where is the first reward model used? does it output the mean? How is the standard deviation chosen?
* Why is this method "bayesian"? Changing the output to a distribution is still consistent with a frequentist perspective -- the authors say they use MLE on line 297. What prior are the authors using? Can the authors make the connection to being "bayesian" more clear as it is the name of their method?
* Why is the uncertainty set of size n? When did the authors define the uncertainty set? Are there results for different sizes of n? Is there a point where making n too large makes you too conservative? It seems like an ablation is missing here.
* The math presented in the paper does not cross the bar for being considered "theory" in my mind. I would encourage the authors to restructure this.

Weaknesses with respect to the experiments:
* I dont understand why evaluating on benchmarks like MMLU predictive of reward overoptimization or uncertainty, the problem the authors claim to be addressing, especially given the feedback data the authors use does not appear to be for these benchmarks.
* While I appreciate the authors time spent running the stochastic case analysis, I don't think I fully understand its purpose right now. Why would training LLMs using random reward functions provide insights about different methods? What would we want to see?
* 1000 Steps of PPO seems really small. Is this a standard choice? Sometimes when finetunig with RL performance goes down before going back up again.
* Fig 3: What is difference in scores calculated with respect to? Is it just the base model before RLHF?


## Edits
* L37 "on a preference data"
* I'm not sure it has been proven that RLHF is a key pathway to "achieveing AGI". I would personally calm down this language.
* Is it known that OpenAI o1 used RLHF? I was under the impression it was more  "RL" than "HF"?
* Line 49: This is confusing. The manuscript went from talking aobut optimization challenges to what seems like a bias problem in data. How does robust RLHF improve that?
* L94: Citations -- training a reward model on preferences was done wayyy back by Arkour (2004), Sadigh (2017), and more. This statemetn should be about language modeling or include more citations.
* L96: "widely recognized that these methods are suboptimal" is a bit strong.
* L102: How does PEBBLe by Lee et al show that diversity constraints lead to overfitting / underfitting problems? From what I understand, Lee et al. show that unsupervised pretraining is important for *online* RLHF so the initial sampled comparisons aren't of useless behaviors.
* L128: Does distributional RL not also belong here as a form of RL that considers the whole distribution of rewards?
* L147: How does Kwon et al. show that "uncertainty in the reward model" impacts final performance? From what I understand, Kwon et al use a pretrained LLM as the reward model for a game-playing agent.
* L182: Though as written it is still correct, its a bit strange that loss functions are written without the average, making their magnitudes dataset-size dependent.
* L245: "neglect of the uncertainty set" makes it sound like the uncertainty set is always there, but it seems like it is something the authors expliclty learn.
* L454: I don't think this deserves to be a Lemma.

### Questions
* Why is the authors method bayesian? Can this connection to the title be expalined the word bayes is barely mentioned in the text. 
* Why are evaluations on MMLU a good proxy for reward overoptimization from human feedback data? Do I mis-understand the experiemnts? Clarification would be appreciated.
* I don't understand L791 and eq 8. How is the reward equal to the "mean" plus the action times a variance. The action is a vector of tokens and the reward is a scalar. Where is the first reward model used? does it output the mean? How is the standard deviation chosen?
* Why are all the phases of reward training necessary?
* several more questions were posed in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a reward modeling method that aims to be robust despite what the paper refers to as inherent imperfections of reward models. To motivate their method, a toy model is constructed in which they do reward modeling with perfect preference data (i.e., there have been no labeling mistakes). They show that even with ideal data reward modeling is imperfect, which should be expected to worsen in a realistic setting.

Their method has two main components. The first is a technique for combining a conservative reward with a nominal reward. For the conservative reward, the lowest reward from a set of reward models is used. The overall objective is a weighted sum of the conservative and nominal rewards, controlled by a parameter λ. The second component is a reward model architecture where a shared 'base model' is first trained with a standard MLE loss. After a linear layer, there are multiple heads that each output a mean and standard deviation, forming a Gaussian distribution for each head. The head with the smallest standard deviation is the nominal reward, and the head with the lowest mean is the conservative reward.

The paper shows that combining these rewards can improve downstream policy model performance improvements over just using the nominal or conservative reward. They also show that the nominal reward of their reward model architecture causes better downstream policy model performance than a single head reward model, even without considering the conservative reward.

In another experiment, the paper shows that over-scoring the reward seems to be more harmful than under scoring, which supports their inclusion of the conservative reward.

### Strengths
- To my knowledge BRME is an original contribution, and the paper motivates the design and use of BRMEs well (e.g., via the toy model experiment).
- BRMEs seem convenient enough that a practitioner would consider using one, and when coupled with the combination of the nominal and conservative reward, the improved downstream performance of the policy model could justify this.
- In general the paper is clear. There are some small grammatical mistakes, but they did not hinder my understanding of the paper. The figures are also descriptive and helpful.
- The appropriate ablation experiments were performed. I do not have concerns about soundness.
- The experimental details in the Appendix are thorough and I do not have concerns with reproducibility, although an open source implementation of BRME would be valuable.

### Weaknesses
 - The performance gains from using BRME over a single head reward model seem modest (1.1% averaged over the benchmarks) despite the architecture being significantly more complex than a standard reward model.
- Combining rewards has been done in the robust RL literature before (including where one of the rewards is more conservative), and to my understanding contributes more to the performance improvement than the specifics of BRMEs. However, this is applied in a way that seems particularly well suited to BRMEs.
- The ablation study in Appendix C.4 does not fully address my request. It compares a traditional reward model with BRME, which is not what I asked for. It also compares the \lambda = 0.6 reward model with a mean reward, which also does not include a direct comparison with BRME. The comparison between the \lambda = 0.6 reward model and BRME is not explicitly shown, making it difficult to assess the individual contributions of the BRME architecture and the reward combination strategy.

### Questions
Could you give a comparison of BRME with a simpler reward model ensemble, or otherwise show how much of the performance gain can be attributed to the combination of nominal and conservative rewards versus the use of this combination with a BRME?

### Soundness
4

### Presentation
3

### Contribution
3
