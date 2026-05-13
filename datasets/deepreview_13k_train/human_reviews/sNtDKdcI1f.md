# A Long Way To Go: Investigating Length Correlations in RLHF

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Great success has been reported using Reinforcement Learning from Human Feedback (RLHF) to align large language models, with open preference datasets enabling wider experimentation, particularly for ``helpfulness'' in tasks like dialogue and web question answering. Alongside these improvements, however,
RLHF also often drives models to produce longer outputs. This paper demonstrates, on three diverse settings, that optimizing for response length is, much more than previously thought, a significant factor behind RLHF.
Studying the strategies RL optimization uses to maximize reward, we find improvements in reward to largely be driven by 
increasing response length, instead of other features. Indeed, we find that even a \emph{purely} length-based reward reproduces most downstream RLHF improvements over supervised fine-tuned models. Testing a comprehensive set of length-countering interventions, we identify the dominant source of these biases to be reward models, which, by studying training dynamics, we find are non-robust and easily influenced by length biases in preference data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the length corrections with the RLHF paradigm for language model (LM) training. Specifically, it has been observed that models finetuned with RLHF tend to generate longer sentences. In this paper, the authors study the causes of the phenomenon through multiple aspects, including the RL algorithm (i.e., PPO) for training the LM, the reward models (RM), and preference data. They demonstrate the PPO generally increases the length compared to the supervised model regardless of the reward engineering applied to mitigate the issue. In addition, altering the data for reward model training does not fully solve the issue either. Lastly, they show that solely optimizing for the length recovers most of the performance improvements. 

The highlight of the paper is it clearly documents the length-increasing issue in the RLHF pipeline. They conduct experiments on several datasets across different domains to demonstrate the issue.

However, the paper is rather descriptive than prescriptive. Specifically, the authors describe the correlation between length increasing and standard PPO training without providing the underlying reason for the phenomenon. Although they propose several heuristic-inspired remedies, the problem is not fully resolved. Therefore, it might not directly contribute to improving the existing RLHF method.

### Strengths
The paper clearly documents the length-increasing issue in the RLHF pipeline. They conduct experiments on several datasets across different domains to demonstrate the issue.

### Weaknesses
The paper is rather descriptive than prescriptive. Specifically, the authors describe the correlation between length increasing and standard PPO training without providing the underlying reason for the phenomenon. Although they propose several heuristic-inspired remedies, the problem is not fully resolved. Therefore, it might not directly contribute to improving the existing RLHF method.

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies whether RLHF scores are correlated with the length of responses. Given that length preference is a well-known issue in the RLHF literature, in the work, the authors explore how much of the optimization and improvement in RLHF is based on length, as opposed to other factors.

Using a comprehensive set of experiments, the paper shows that length constitutes the majority of the reward, indicating that length may play a much larger role than previously documented.

Finally, the authors discuss the implication of these findings on the RLHF and state the importance of developing better and more robust algorithms.

### Strengths
The paper offers a well-executed investigation of a well-known pattern: the correlation between RLHF scores and length. The findings are persuasive and supportive of the conclusions

### Weaknesses
The paper's comprehensibility is somewhat challenging. The conclusions drawn from the tables and figures lack clarity, and it's not easy to discern the key takeaway from the experiments presented. The paper would be improved with some rewriting and clarification.

The experiments themselves are well-executed, and they do support the main message. However, it's worth noting that this pattern has been observed in numerous other studies, and strategies to address this bias/reward hacking have been extensively documented elsewhere. Consequently, the contribution of this paper does not look very strong for an ICLR  conference.

### Questions
NIT
* The "STD" term was introduced in Figure 2 way before defining it later in the text. 
* For Figure 3, why not have both settings (red and black) for all the lengths? Does that mean that sometimes there are no examples in a particular bin for a particular setting or are there some missing datasets in the figure?

### Soundness
3 good

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
This paper explores how length correlates with performance improvement in RLHF. The author starts by examining the output length increase in RLHF and the correlation between output length and reward model scores, and then they reveal that some intervention in PPO can mitigate the length increase to some extent. Further, they find that the reward model can only learn "easy" examples, i.e. the examples that can be correctly predicted according to the length heuristic. The authors examine several intervention methods for reward modeling and find that there could be a trade-off between length bias and reward model accuracy in some cases. Finally, they show that purely optimizing the policy model for increasing output length can lead to an improvement in output quality.

### Strengths
This paper focuses on a very important problem: what role does length play in RLHF? The paper conducts extensive experiments to demonstrate the correlation between length and reward model scores and explores several ways to mitigate length bias. The results can provide constructive guidance for future research.

### Weaknesses
1. The most confusing part for me is the evaluation. What is the rationale for adopting a length-bias metric, GPT-4 evaluation [1], when evaluating the correlation between length and RLHF performance? Two potential factors can be affected by length, making it hard to disentangle the attribution of length correlation. Or do you aim to reveal the bias issue of GPT-4 in this paper? Then could you please explain more clearly what you mean by "length correlations in RLHF" and what the length correlates with? The reward modeling? The optimization algorithm? The evaluation? Or all of them? If so, I'd suggest investigating them separately.
2. I am skeptical about the experiment and claim that "reward models are not able to make progress on most training examples" (sec 4.1). The results may, at least partly, be due to the reward model capacity. I suppose that reward modeling is a relatively difficult task, so weak models may only capture some shallow features. With a more capable reward model, the "hard" samples may be learned. A supporting evidence is that, as shown in Table 3, the length heuristics accuracy on WebGPT is 55.7%. However, in the result of a recent paper [2], a more powerful reward model that is not trained on WebGPT can yield 65.2% accuracy. Therefore, according to this paper, at least 9.5% of counter-biased samples are learned by the reward model. Perhaps the authors can supplement experiments by adopting more powerful reward models, e.g. scaling the base from LLaMA-7B to 70B following the original LLaMA-2 paper [3] (if computation allowed), and see if the learning patterns remain the same.

### Questions
Please refer to weaknesses.

### Soundness
3 good

### Presentation
2 fair

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
The authors show that when applying RLHF for optimize helpfulness, much if not most of the gain comes simply from learning to increase the length of the response, and in fact solely optimizing for length can achieve most of the gains of optimizing for helpfulness in many cases.

### Strengths
--comprehensive evaluations on a few different RLHF settings/datasets for helpfulness optimization

--nice in-depth exploration confirming the extent of a phenomenon (length correlations for helpfulness optimization) that i think hasn't been comprehensively analyzed previously

### Weaknesses
 --presentation: it's quite difficult to parse what several of the abbreviations mean in the tables (and honestly i'm still a bit confused on what exactly you're showing in the first couple of figures and tables after looking at them for several minutes). it would be great if you could make the figs/tables more self-contained, e.g., define abbreviations in the captions and summarize takeaways, so i don't have to keep bouncing between the figs/tables and the text.



### Questions
--even if we're just optimizing for length, your model still learns something nontrivial, right? an interesting point of comparison might be an extra baseline where instead of sampling 8 outputs from the base LM and picking the longest one, you just sample one output and forcibly make it keep generating past the end - i imagine this would perform a lot worse. so intuitively, i feel that optimizing for length is also somehow optimizing for some less trivial notion of comprehensiveness, maybe?

--just to confirm, weighted reward gain i should think of as measuring how much reward improves within a particular bin of length, i.e. the reward gain that comes from factors other than length?

--would be curious also if you have any qualitative sense of what are the non-length axes along with helpfulness improves in your experiments (i.e., any intuitions for the remaining 10-30% of helpfulness that wasn't attributed to increased length?).

--as you wrote in the conclusion, it would be interesting to just see a quick experiment on e.g., harmlessness or honesty, if only to confirm our intuition that length is primarily a heuristic for optimizing helpfulness and not really applicable to other common tasks we RLHF for. (not necessary if it's troublesome to setup though.)

--i'm not very clear on the concrete actionable suggestions for practitioners based on your analysis? (though they're not strictly necessary - i see that you did try a few ways to regularize length already)

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
