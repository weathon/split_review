# Diverse Preference Learning for Capabilities and Alignment

- Decision: Accept
- Scores: 8, 8, 5

## Abstract
As LLMs increasingly impact society, their ability to represent diverse perspectives is critical.  However, recent studies reveal that alignment algorithms such as RLHF and DPO significantly reduce the diversity of LLM outputs. Not only do aligned LLMs generate text with repetitive structure and word choice, they also approach problems in more uniform ways, and their responses reflect a narrower range of societal perspectives. We attribute this problem to the KL divergence regularizer employed in preference learning algorithms. This causes the model to overweight majority opinions and sacrifice diversity in exchange for optimal reward. To address this, we propose Diverse Preference Learning, which decouples the entropy and cross-entropy terms in the KL penalty — allowing for fine-grained control over LLM generation diversity. From a capabilities perspective, LLMs trained using Diverse Preference Learning attain higher accuracy on difficult repeated sampling tasks and produce outputs with greater semantic and lexical diversity. From an alignment perspective, they are capable of representing a wider range of societal viewpoints and display improved logit calibration. Notably, Diverse Preference Learning resembles, but is a Pareto improvement over standard temperature scaling.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the issue that alignment algorithms lead to a reduction in diversity. They motivate the need for diversity in a few ways: 1) societal implications, 2) better diversity might mean better inference-time problem solving (because you’re essentially doing a wider search in solution space), 3) better calibration.

Though temperature scaling is one way of addressing this issue, the authors demonstrate that it is not sufficient, as temperature scaling quickly leads to degradation in generation quality.

The authors address the problem by first observing that the KL divergence term is the culprit for drop in diversity (Proposition 1). Ie, the hyperparameter \beta controls both the reference policy’s weighting and the sharpness of the output distribution. 
The solution that the authors propose is to decouple the KL regularization term into a cross-entropy term and entropy term, but weigh them independently (with hyperparameters \alpha, \beta), which in turn ends up independently affecting the reference model’s output distribution and how much such distribution is weighted (proposition 2). 

The authors draw a couple of connections between their change and prior work – when \alpha == \beta, then this is the standard DPO regime. 
Similarly, their \alpha parameter can be thought of as temperature scaling, but done at a sequence level as opposed to token level (equation 14).

Finally, the authors demonstrate a series of empirical results that match their original set of motivations (1: better diversity, 2: better inference-time problem solving, 3: better calibration).

1) Diversity (Figure 2): The suggested approach method achieves better pareto curves when plotting diversity scores vs. generation quality
2) Problem solving (Figure 3): For hard problems, in which an increased number of generations helps solve the task, their suggested approach leads to higher performance, which they attribute to increase in diversity across generations (ie, doing a wider search in solution space).
3) Calibration (Figure 4): The authors show that *without affecting accuracy*, their suggested approach leads to improved calibration (according to ECE and Brier scores).

### Strengths
Well organized, lots of empirical results, the suggested approach is simple and principled.

### Weaknesses
 * At a high level, the authors attribute improved problem solving (which is actually not very evident in Figure 3) to improved diversity. Though I could imagine that diversity hypothetically can lead to improved problem-solving performance for methods that use inference-time scaling (because the model is essentially generating more hypotheses for solving a problem), it seems like Figure 3 is not quite telling this story.
* First of all, in the case of easy/medium difficulty problems, their suggested approach does not seem to be better than DPO – this is fine for the easy case – in which both DPO and DPL saturate to near perfect accuracy, meaning that the problems didn’t require a wide search in hypotheses in the first place.
* However, in the medium case, DPO outperforms DPL, with still a lot of room for improvement for both models (ie. we do not see high accuracy saturation).
* Though DPL outperforms DPO in the hard case, the improvement is rather minimal. 

* Perhaps more importantly, if more diversity does indeed lead to better problem solving, then even within DPL, we should see a relationship between temperature and best-of-N accuracy, which is not the case in Figure 3 – sometimes higher temperature is better, sometimes it’s not. Studying how accuracy is affected by varying temperatures would have been helpful.
* The author’s claim that improved diversity leads to better problem solving for methods that use inference-time scaling could be strengthened by actually trying an inference-time scaling approach – this is something that can be empirically studied. I realize this might be a big ask, but I am willing to raise my score significantly if indeed the authors demonstrate evidence of this. Otherwise, I think their claim that DPL leads to better problem-solving is not very convincing. 
* (While we’re at it - minor note regarding Figure 3: the color scheme (gradients of green + blue) makes it very very difficult to parse the results. Please consider changing it)

### Questions
Figure 2: There seems to be quite a large range in terms of win-rate/avg. reward/ref. policy CE when you consider points that lie below the Pareto curve (points with lighter shades). Do you have an explanation for such behavior? If the range of behavior is so wide, is it possible that the improved pareto curve is due to noise?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The contribution of this paper is simple, but well-motivated and addressing a real issue. 

The authors note that the $\beta$ parameter, which controls the KL regularisation strength in DPO, is involved in mode collapse to the majority option. Temperature sampling, they argue, does not fix this, as it causes disfluencies and broken outputs. To address this, they propose to decompose KL into an entropy and a cross-entropy term with the former, each with separate weights modulating the strength of the regularisation. They are able to bake this into DPO, proposing a new objective called DPL. They show how this objective can be thought of as temperature scaling on the sequence level. 

They perform two different flavours of evaluation: in the first one they assess the quality/diversity tradeoff on Arena-Hard and HH-RLHF and they found DPL to be Pareto-dominant; in the second, they show that in a best-of-N sampling setup (GSM8K and MATH), DPL helps on hard problems, but results are mixed on easy-medium. Finally, they show improved results on MMLU and TruthfulQA in terms of both accuracy and calibration error.

### Strengths
- To the best of my knowledge, the proposed method, while obvious in hindsight (as most good things are) is novel
- The problem is well posed and mostly convincingly discussed. Acting on the entropy of the distribution has been gaining momentum in the community
- Experiments are quite comprehensive, though some baselines should probably be included. (This is the main reason I am giving a 6 instead of an 8) (edit: improved after rebuttal)
- The quality of the writing is outstanding

### Weaknesses
 - The experimental setting could be stronger: DPL is mostly pitted against vanilla temperature scaling, which on its own does lead to bad outputs. However, top-k, top-p, and, more recently, min-p sampling are all relatively established solution that should have been incorporated in the analysis. The absence of these baselines makes it difficult to assess the true advantage of DPL over existing, well-established decoding strategies. Specifically, the paper should have explored how DPL compares when using these alternative decoding methods as a starting point, rather than just temperature scaling. This is critical to understand if DPL's benefits are orthogonal to these methods or if it simply provides a different way to achieve similar results.
- Basic REINFORCE (with no KLD in the reward), which has become very popular again without should also have been compared against. This is more of a desideratum than a hard requirement. The current analysis focuses on DPO and its variants, but a comparison against a more direct policy gradient method like REINFORCE, especially one without KL regularization, would provide a valuable perspective on whether the benefits of DPL are specific to the DPO framework or if they generalize to other reinforcement learning approaches. This would help clarify the contribution of the method.
- Figure 2 seems to show some brittleness of DPL, with many green dots substantially worse than the Pareto frontier. Some additional discussion about it would be helpful. The fact that some DPL configurations perform significantly worse than the Pareto frontier suggests that the method might be sensitive to hyperparameter tuning or that there are specific conditions under which it fails to provide the expected improvements. A more thorough analysis of these cases, including a discussion of the parameter settings that lead to suboptimal performance, would be beneficial.

### Questions
Suggestions:
- Figure 3 is hard to read

### Soundness
3

### Presentation
4

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
The paper discusses how alignment algorithms like RLHF and DPO reduce the diversity of large language models (LLMs), leading to less varied and overly homogeneous outputs. The study identifies the KL divergence regularizer in preference learning algorithms as a primary cause, which biases models towards majority opinions at the expense of diversity. To combat this, the paper proposes a new method, Diverse Preference Learning (DPL), which decouples entropy and cross-entropy terms in the KL penalty to allow more controlled diversity in LLM outputs. DPL demonstrates better performance in representing a broader range of societal perspectives and produces outputs with greater semantic and lexical diversity compared to traditional methods.

### Strengths
1. The theoretical analysis on KL-divergence sounds interesting.
2. The experimental design of the article is quite creative.

### Weaknesses
1. The objective of DPL (Eq. 9) appears interesting, yet the derivation process seems to have many inconsistencies, as detailed in the Questions section.
2. You should define Proposition 3.1, Corollary 3.2, and Proposition A for clarity.
3. The experiments lack comparisons with existing Diverse Preference Learning methods, such as [1,2], and are missing richer alignment baselines for analysis.
4. The experiments lack many implementation details necessary for readers to fully understand or reproduce the results. See Questions for details.
5. It appears that DPL does not perform better than DPO on mathematical tasks.

### Questions
1. In line 215, what if ``Empirical choices of β typically lie in the range [0.01, 0.1].''
2. Question towards Sec. 3.2:
  2.1. In Eq. 8, should it be H(π(·|x),πref (·|x))?
  2.2. In Eq. 22, should it be + απ^⊤ log π?
  2.3. In Eq. 23, should it be + α log π?
  2.4. From Eq. 25 to Eq. 26, should π = exp()-1?
  2.5. If Question 5 stands, does Eq. 26 stand?
  2.6. If in Eq. 28, it is proportional relation, you cannot use equal in Eq. 29.
3. How to calculate "1) general semantic diversity, 2) logical diversity or diversity of viewpoints, and 3) content diversity." and what's their meaning? What is "Embedding Cosine Distanc" in Figure 2?
4. Why do you generate 16 responses for each question?
5. How do you train the reward model, and why the rewards are all negative?
6. What is DPO t=1.2 in Figure3, and where is the definition of t?
7. Why do you use Mistral-7B-Instruct-v0.2 for DIVERSITY-QUALITY TRADEOFFS, while Mistral-7B base for the other two task?

### Soundness
2

### Presentation
2

### Contribution
2
