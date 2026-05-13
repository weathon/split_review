# The Perils of Optimizing Learned Reward Functions: Low Training Error Does Not Guarantee Low Regret

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
In reinforcement learning, specifying reward functions that capture the intended task can be very challenging. Reward learning aims to address this issue by \emph{learning} the reward function. However, a learned reward model may have a low error on the training distribution, and yet subsequently produce a policy with large regret. We say that such a reward model has an \emph{error-regret mismatch}. The main source of an error-regret mismatch is the distributional shift that commonly occurs during policy optimization. In this paper, we mathematically show that a sufficiently low expected test error of the reward model guarantees low worst-case regret, but that for any \emph{fixed} expected test error, there exist realistic data distributions that allow for error-regret mismatch to occur. We then show that similar problems persist even when using policy regularization techniques, commonly employed in methods such as RLHF. Our theoretical results highlight the importance of developing new ways to measure the quality of learned reward models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the theoretical challenges of using a learned reward function in policy optimization, particularly focusing on the "error-regret mismatch" problem—where a learned reward function has low expected error on a given data distribution. Yet, the resulting policy incurs high regret when evaluated against a true reward function. This issue primarily arises from the distributional shift. To frame the problem, the authors define "safe" and "unsafe" data distribution for any given MDP. A data distribution is classified as safe if any reward function with low expected error will reliably produce a low-regret policy. They provide theoretical analysis across both unregularized and regularized policy optimization scenarios, reaching consistent conclusions. The paper’s key theoretical insights are: (1) ensuring low regret may require prohibitively low expected error on the learned reward function, and (2) in certain large MDPs, all data distributions might inherently be unsafe.

### Strengths
The paper is overall well-written. The theoretical framework is clearly laid out, making the findings more comprehensible despite the inherently abstract nature of the paper.

The paper studies an important issue related to AI alignment (the potential pitfalls of using learned reward functions without proper evaluation). 

The theoretical statements appear rigorous, and the authors provide intuitive explanations for deriving those results (although I did not review the proofs in the appendix).

### Weaknesses
The paper could benefit from a discussion of realistic scenarios where unsafe data distributions may lead to undesirable behaviors. An example would help clarify the practical implications of the theoretical results and provide more concrete context for the error-regret mismatch problem.

Regarding Definition 2.1: how detrimental unsafe data distributions can be in real-world practice? For instance, in the case of an unsafe data distribution, it is possible for a learned reward function with low expected error to either induce high regret ("bad" reward function) or low regret ("good" reward function). Understanding the likelihood of selecting a "good" reward over a "bad" one in practical settings would provide a more nuanced perspective on the applicability of the theoretical findings.

### Questions
What practical insights can a reward learning practitioner derive from this theoretical analysis? Are there actionable steps to avoid high-regret policies when using learned reward functions?

In Section 7, the paper discusses alternative reward evaluation methods. Do these alternatives alleviate the issues presented, or do they also have limitations?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper theoretically studies the conditions that when learned reward models in RL will and will not lead to large regret in policy optimization. It shows that if the reward model's expected test error is suffient small (with respect to a threshold provided), then it would lead to low regret during policy optimization; otherwise, there are cases it would lead to large regret. The theoretical results highlight the need for careful consideration when employing learned reward functions in policy learning and underscore the importance of advanced reward function design.

### Strengths
The paper is clearly written, the results are interesting.

### Weaknesses
While high-level ideas are clearly presented, and the paper includes proof sketches, I generally found the paper to be quite dense, hard to read, and some parts quite confusing. Overall, the paper is not polished: the figures (Fig 1 and 2) look disproportionately large; some notation does not appear to be adequately explained when introduced (e.g., $\max J_R$ and $\min J_R$ in the 2nd paragraph of Sec 2); writing could be improved throughout the paper, as some sentences are unclear. For example, the paper mentions

> Our results highlight the challenge of deriving useful PAC-like generalization bounds for current reward learning algorithms. While this is possible (and has been done, see (Nika et al., 2024; Cen et al., 2024)), we showed that realistic bounds on the error in the learned reward function do not provide meaningful guarantees. 

but does not explain what the authors actually mean by this. The cited references seem to provide guarantees on the suboptimality gap and regret. The paper also considers the RLHF setting but does not mention relevant references that study similar problems in this context, e.g., Sun et al., The Importance of Online Data: Understanding Preference Fine-tuning via Coverage. At the moment, it is not clear to me how to compare these results. It would be useful if the authors could clarify this in the rebuttal. In general, the related work section provides many references without actually explaining how they relate to the paper.

Regarding the results, it doesn’t seem surprising to me that a low error (Eq. (1)) can lead to high regret; this seems simply due to the distribution mismatch between the data used to learn $R$ and that used to train $\pi$. The intuition behind the proof of Proposition 3.3 follows this argument. However, it is well known that coverage assumptions are necessary for offline RL, including in RLHF settings, as argued in the references above. Hence, the conceptual novelty of the presented results is somewhat unclear to me. It would be great if the authors could clarify this.

It is also somewhat unclear what conclusions to draw from these results. The paper does not provide a concrete solution on how to approach the problem at hand, making it difficult to assess the practical significance of the findings. Moreover, the paper lacks experimental results that demonstrate the importance of the theoretical findings.

### Questions
1. On line 161, $J^R$ is policy evaluation function for reward function R with respect to which policy? The maximum and minmum is taken with respect to what? Policy or reward function?

2. I have a question on Proposition 3.1 and 3.3. Since the unsafe data distributions cover positive data distributions, is it possible that the $\epsilon$ in Proposition 3.3 satisfies the assumption in Proposition 3.2, which leads to a contradiction (say, D in unsafe(R, \epsilon, L) by prop 3.3 and D in safe(R,\epsilon,L) by prop 3.1)?

3. Can you justify the assumptions in Corollary 3.4? Since you are studying the tubular MDP setting, I was wondering if the second bullet, say, the supports of the policies are completely disjoint with each other, is too strong to hold, especially given that the $\epsilon$ should be set as a resonably samll value (not as small as that in Prop 3.2 though) and thus the number of policies in the policy set $\Pi_L$ is large. Maybe a toy example would help illustration.

4. On line 372, I found it hard to understand the sentence "a provided data distribution is safer than an initial reference policy".

5. On line 402, how $\hat{R}$ can be defined to be equal to R which is unknown?

6. I was wondering if there exist similar results as Proposition 3.2 and Theorem 3.5 under the setting ERROR-REGRET MISMATCH FOR REGULARIZED POLICY OPTIMIZATION.

7. If the resutls in this paper can motivate some novel algrithms for reward design? Any insight?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the problem of reward learning: given a data distribution, and assuming that the learner enjoys a guarantee bounding the error over the data distribution of the form

$$E[|R(s,a)-\widehat R(s,a)|/R_{max}] \le \varepsilon,$$

the authors are interested in understanding how good the policy $\widehat \pi$ corresponding to $\widehat R$ is w.r.t. the true MDP.

To this aim, the authors provide several results, most of the negative. Indeed, since the visiting distribution of the optimal policy may be very different from the distribution of $D$ from which state-actions are sample during the learning of the reward, having a relatively small $\varepsilon$ does not guarantee small "regret" (as the authors define it).
Controversely, there are examples where, in order to get a small regret, $\varepsilon$ needs to be of order $(S\times A)^{-1}$.

The authors then study the case of deriving, from $\widehat R$, a policy that is regulared, rather than the optimal one relative to $\widehat R$. Also in this case, a low reward error does not guarantee low regret, as proved in Theorem 4.2.

The paper closes with a discussion about the impact of these results the RLHF, and in particular to Large Language Models.

### Strengths
The paper is very well written, the presentation is clear, and the figures are perfect to convey the message.

Also, the importance of the problem is explained in a very detailed and precise manner, and the setting is defined in a way that is very "user-friendly".

The paper provides several different results, which answer many of the questions anyone may have about the setting.

### Weaknesses
My main concern with the results of the paper is that the results somehow lack novelty.

Propositions Proposition 3.1., 3.2, 3.3, Corollary 3.4. are very intuitive and natural (this is of course a quality), but aren't they somehow a consequence of the well-known lower bounds for offline learning?

Indeed, lower bounds for offline learning in case of tabular MDPs always contain some measure of coverage of the offline dataset. This coverage coefficient writes, for the evaluation of an arbitrary policy $\pi$ as

$$C_\pi=\sup_{s,a}\frac{d^\pi(s,a)}{D(s,a)}.$$

If we look at the worst possible policy, as in Proposition 3.3, it is clear that the coverage coefficient becomes of order $S\times A$, no matter the choice of data distribution $D(\cdot,\cdot)$. As lower bounds show that, in worst case, the sample complexity of any algorithm must scale with $C_\pi$, if follows that by outputting the policy which is optimal w.r.t. the reward function estimated over $D$, we could be making an error of order $C_\pi \varepsilon$ over is estimated return. This result seems to be very similar to what the authors get in Proposition 3.3.

Moreover, the choice made in equation (1),

$$E[|R(s,a)-\widehat R(s,a)|/R_{max}] \le \varepsilon,$$

that is assuming a bound on the Mean Absolute Error seems unjustified. Why didn't the author focus on the MSE, which is what gets minimized by most supervised learning algorithm?

Despite the  these criticisms, I must however point out that the paper seems to have its own narrative such as to frame the results in a new and interesting framework. Therefore I do not think that these weaknesses should compromise the acceptance of the paper.

### Questions
See weaknesses

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies learning-theoretic challenges related to reward modeling in RL. More specifically, it examines how the regret of an RL algorithm responds to errors in the reward model. It demonstrates that the regret diminishes as the error vanishes. Conversely, with a fixed error, the regret can become large. The authors refer to this property as *error-regret mismatch*. The analysis extends to RL with regularization techniques, including RLHF.

### Strengths
The paper provides an extensive analysis of the *error-regret* mismatch property in tabular MDPs. This includes RL objectives with regularization, as in RLHF. The main ideas are relatively easy to follow. I haven’t checked the full analysis in the appendix, but the arguments presented in the main text appear sound.

### Weaknesses
While high-level ideas are clearly presented, and the paper includes proof sketches, I generally found the paper to be quite dense, hard to read, and some parts quite confusing. Overall, the paper is not polished: the figures (Fig 1 and 2) look disproportionately large; some notation does not appear to be adequately explained when introduced (e.g., $\max J_R$ and $\min J_R$ in the 2nd paragraph of Sec 2); writing could be improved throughout the paper, as some sentences are unclear. For example, the paper mentions

> Our results highlight the challenge of deriving useful PAC-like generalization bounds for current reward learning algorithms. While this is possible (and has been done, see (Nika et al., 2024; Cen et al., 2024)), we showed that realistic bounds on the error in the learned reward function do not provide meaningful guarantees. 

but does not explain what the authors actually mean by this. The cited references seem to provide guarantees on the suboptimality gap and regret. The paper also considers the RLHF setting but does not mention relevant references that study similar problems in this context, e.g., Sun et al., The Importance of Online Data: Understanding Preference Fine-tuning via Coverage. At the moment, it is not clear to me how to compare these results. It would be useful if the authors could clarify this in the rebuttal. In general, the related work section provides many references without actually explaining how they relate to the paper.

Regarding the results, it doesn’t seem surprising to me that a low error (Eq. (1)) can lead to high regret; this seems simply due to the distribution mismatch between the data used to learn $R$ and that used to train $\pi$. The intuition behind the proof of Proposition 3.3 follows this argument. However, it is well known that coverage assumptions are necessary for offline RL, including in RLHF settings, as argued in the references above. Hence, the conceptual novelty of the presented results is somewhat unclear to me. It would be great if the authors could clarify this.

It is also somewhat unclear what conclusions to draw from these results. The paper does not provide a concrete solution on how to approach the problem at hand, making it difficult to assess the practical significance of the findings. Moreover, the paper lacks experimental results that demonstrate the importance of the theoretical findings.

### Questions
Please see my comments in *Weaknesses*.

### Soundness
3

### Presentation
2

### Contribution
2
