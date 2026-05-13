# In-Context Editing: Learning Knowledge from Self-Induced Distributions

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
In scenarios where language models must incorporate new information efficiently without extensive retraining, traditional fine-tuning methods are prone to overfitting, degraded generalization, and unnatural language generation. To address these limitations, we introduce Consistent In-Context Editing (\method), a novel approach leveraging the model's in-context learning capability to optimize towards a contextual distribution rather than a one-hot target. \method introduces a simple yet effective optimization framework for the model to internalize new knowledge by aligning its output distributions with and without additional context. This method enhances the robustness and effectiveness of gradient-based tuning methods, preventing overfitting and preserving the model's integrity. We analyze \method across four critical aspects of knowledge editing: accuracy, locality, generalization, and linguistic quality, demonstrating its advantages. Experimental results confirm the effectiveness of \method and demonstrate its potential for continual editing, ensuring that the integrity of the model is preserved while updating information.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents ICE, a regularization loss that aims at addressing the limitations of the traditional fine-tuning loss to update knowledge. Experiments on the KnowEdit dataset show its effectiveness to update the model's knowledge especially in the continual editing setting compared to other baselines.

### Strengths
- The paper is clear, well-motivated and the idea is novel as far as I know.
- Compared to other baselines, this method is the only one capable of effectively editing knowledge continually.

### Weaknesses
 - The paper is clear, well-motivated and the idea is novel as far as I know.
- Compared to other baselines, this method is the only one capable of effectively editing knowledge continually.

 - The pipeline is quite heavy, relying on sampling at every optimization step and GPT-4 for augmented contexts.

 - "we sample sequences x_c from the model conditioned on $[c, q, x^∗]$"(L.246): Could you explain the rationale behind including $x^*$ in the sampling of $x_s$ ? what happens if the sampling is only conditioned on $[c, q]$ without the target ? (which better corresponds to Eq.4).
- I'm concerned about the context generation process, you mention that you use GPT-4 however, it somehow defeats the purpose since GPT-4 can be prone to hallucinations due to its training data becoming obsolete. I'm really not convinced by the prompt that you used: *"Please help me generate five complete statements as [context]s according to the semantics of incomplete facts '{prompt}' and '{target}'"*. In fact, if GPT-4 hallucinates, it will provided non factual contexts, hindering the optimization process and potentially incurring further hallucinations. Consider adding a 'Limitations' section that addresses the potential risks of using GPT-4 for context generation, including the possibility of hallucinations or outdated information. This section could also explore potential mitigation strategies or alternative approaches for context generation.
- From L.431, could you provide a clear definition of what 'temperature' refers to in this context ?
- In Algorithm 1, only $L_\text{ICE}$ is shown in the optimization process. If $L_\text{FT}$ is also used, could you update the algorithm to reflect this? Additionally, an ablation study on the effect of $\lambda$ would provide valuable insights into the relative contributions of $L_\text{ICE}$ and $L_\text{FT}$ to the overall performance.

*Typos:*
- Figure 1: for the fine-tuning part, it should be $p_{\theta_s}(x | q)$ in the FT loss (and not $p_{\theta_s}(x)$).

### Questions
- "we sample sequences x_c from the model conditioned on $[c, q, x^∗]$"(L.246): Could you explain the rationale behind including $x^*$ in the sampling of $x_s$ ? what happens if the sampling is only conditioned on $[c, q]$ without the target ? (which better corresponds to Eq.4).
- I'm concerned about the context generation process, you mention that you use GPT-4 however, it somehow defeats the purpose since GPT-4 can be prone to hallucinations due to its training data becoming obsolete. I'm really not convinced by the prompt that you used: *"Please help me generate five complete statements as [context]s according to the semantics of incomplete facts '{prompt}' and '{target}'."*. In fact, if GPT-4 hallucinates, it will provided non factual contexts, hindering the optimization process and potentially incurring further hallucinations. Consider adding a 'Limitations' section that addresses the potential risks of using GPT-4 for context generation, including the possibility of hallucinations or outdated information. This section could also explore potential mitigation strategies or alternative approaches for context generation.
- From L.431, could you provide a clear definition of what 'temperature' refers to in this context ?
- In Algorithm 1, only $L_\text{ICE}$ is shown in the optimization process. If $L_\text{FT}$ is also used, could you update the algorithm to reflect this? Additionally, an ablation study on the effect of $\lambda$ would provide valuable insights into the relative contributions of $L_\text{ICE}$ and $L_\text{FT}$ to the overall performance.

*Typos:*
- Figure 1: for the fine-tuning part, it should be $p_{\theta_s}(x | q)$ in the FT loss (and not $p_{\theta_s}(x)$).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work presents an auxiliary loss for finetuning an LLM which steers it towards new knowledge and applied in the knowledge editing domain. This is through “in-context editing” (ICE), which minimizes the distances of the output *distribution* of the original model without the new knowledge to that of a model which is conditioned on the new knowledge in the prompt. Besides accuracy and fluency, other facets of generation are evaluated, like whether unrelated knowledge is affected and whether the learned new knowledge generalizes to related knowledge. Compared to prior methods (ROME, MEMIT, FT-L, FT-M), ICE performs relatively well on most metrics.

### Strengths
1. The method is novel for knowledge editing by identifying an issue with prior approaches for targeted knowledge editing. While there has been prior work on fine-tuning and naive work on in-context (prompt-based) knowledge editing, the combination of distilling the in-context editing directly into the parameters has not been done.

2. The empirical results, while not perfect on all metrics and datasets, show promise across the baseline methods presented and on the standard metrics and perplexity.

3. Ablation studies emphasize the importance of both dynamically updating the target distribution during training and on the importance of the context. In particular, an in-depth analysis of the static target distribution shows that dynamic targets actually lead to better convergence.

4. More analysis shows that as the model is edited (updated) more, the degradation of the model is less prominent than the other baseline methods.

### Weaknesses
1. The method is similar to knowledge/context distillation or gisting, and so a connection should be drawn there. Still, applying this method appears novel for knowledge editing. However the lack of references to KD/gisting makes it hard to place how related (or not) this idea is to that line of work.

[Snell et al., 2022](https://arxiv.org/abs/2209.15189) - Context Distillation

[Mu et al., 2023](https://arxiv.org/abs/2304.08467) - Gisting

2. The paper advocates for conditioning on “context” to generate target token distributions. It isn’t clear based on the data that this “context” is what makes the ICE method good, as opposed to the training objective. 

  The method requires GPT-4 outputs to generate the context, while the other baselines being compared against are not allowed any access to this (external model) context. If the method is instead interpreted as knowledge distillation, it is less clear how whether this is possible without this context from a stronger LLM.

  Concretely, the effect of context should be isolated from the distillation-like training objective. The latter targets the one-hot problem motivated by the introduction of the paper, but the former is discussed heavily by this paper.

  If I understand the ablations table correctly, the rows with x in “Context” gives us a view of what the distillation-like objective could do for model editing. It looks competitive (or even better) than the baselines presented in Table 3, and so I wonder what the context actually adds? 

3. In addition, one way to explore this would be to measure an “upper bound” of how good the model could be if it were perfect with context, i.e. evaluate the model corresponding to $p_\theta(x, | c, q)$ both before and after training. 

4. The baselines included do not seem comprehensive and are a little misleading. In particular, MEND and SERAC are other method mentioned by Zhang et al., 2024 [survey] that achieve strong results only slightly worse than FT-M. The omission of those results make it seem like ICE is tied with FT-M, both much better than other methods. In reality, ROME/MEMIT are relatively weak baselines compared to the other methods.
5. Another limitation of the method that should be acknowledged or perhaps even addressed directly is the number of modified parameters and cost to make the edits. MEMIT/ROME are local, while FT-M, FT-L, and ICE are full-model. But my understanding is that the latter 3 are actually similar in terms of training cost and modified parameters

[Mitchell et al., 2021](https://arxiv.org/abs/2110.11309) - MEND 

[Mitchell et al., 2022](https://proceedings.mlr.press/v162/mitchell22a/mitchell22a.pdf) - SERAC.

### Questions
Questions


1. I don’t understand the direct optimization problem stated in L238 - why can't the loss be backpropped jointly through both distributions? Anyway, the solution of freezing the target distribution makes sense, but then I'm confused by the $s$ vs. $s+1$ in Equation 7 – wouldn't it be more accurate that both subscripts should be $\theta_{s}$ except we do not backprop through the left term of the KL term? That is what is stated (and drawn in the figure) but having $s+1$ in the subscript feels wrong because that’s in the future? 

2. How are stop/end-of-sequence tokens controlled in the output sequence, and how is fluency measured with respect to that? In the examples shown in D.6, all of the methods start to generate more (possibly unrelated) text after giving the correct answer. How does that unrelated text get factored into the various metrics?

3. I’m confused by “Observation 1” and the subsequent proof because empirically, this is the same as row 4 in the ablations table 4, and it looks like it is substantially better than the fine-tuning baselines. Actually, I’m confused whether 3.1 and 3.2 are actually represented empirically anywhere so we have a sense of where it stands relative to other methods.

4. This was mentioned above, but to ask more directly mostly out of curiosity: what is the cost (in terms of training time + prompting) for this loss? Is it substantially slower or faster than FT-M, and what about after factoring any hyperparameter tuning?

## Other minor comments not affecting the judgement:

In the implementation details, GPT-2 is mentioned but it isn’t mentioned elsewhere in the paper. It is in the appendix, and so the mention of GPT-2 would be less confusing if it was moved entirely to the appendix.

Throughout the paper, `` should be used instead of '' to start quotations.

I'd also suggest renaming the abbreviation ICE to CICE, as ICE was already used to refer to in-context editing in [Cohen et al., 2023](https://arxiv.org/pdf/2307.12976), which is also cited in the paper as [6].

Finally, contemporary work worth knowing about and citing in a future draft: [Rozner et al., 2024](https://arxiv.org/abs/2406.09920).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed a method for knowledge editing that is based on leveraging the in-context ability of the model. To learn a new fact by finetuning, the methods proposes to train the model with supervision coming from itself when it can answer the query correctly based on contextual information. 

What is interesting is that since the method relies and benefits from the in-context adapting ability of the model to have better update, better models would benefit even more from finetuning with this method [1, 2].

Overall, this is a good contribution with interesting potential for future work. I think the author could include a discussion about how much the base in-context ability of the models impact the success of the method.

[1] Yu et al 2023 Characterizing mechanisms for factual recall in language models.
[2] Monea et al. 2024. A Glitch in the Matrix? Locating and Detecting Language Model Grounding with Fakepedia

### Strengths
The paper proposes an interesting methods that is likely to be useful for future applications. 
The paper does a good job at demonstrating the usefulness of the method.

### Weaknesses
The paper only studies one base model, it is not clear how this generalizes to other model. In particular, I suspect that the size of the model and their base in-context capabilities might play an important role in the success of the method.

### Questions
I am curious to hear the thoughts of the authors about how much the base in-context ability of the models impact the success of the method.
The discussion section could be expanded with such consideration. It would be interesting especially since the paper does not experiment with different base models

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method of updating an LLM to incorporate some specific piece of new information.
The LLM prompt is prefixed with this new information and the output distribution is used as the target for training the same LLM without that additional context.
This loss is used as a regulariser, along with the main fine-tuning loss.
Results show good performance compared to the chosen baselines.

### Strengths
The idea is interesting and makes sense, as the probability distribution provides more detailed information compared to just a one-hot target.
Evaluation is performed on several different datasets and with a number of different metrics.

### Weaknesses
 A crucial baseline is currently missing. There needs to be an evaluation of the exact same proposed model but with lambda set to 0. Using only the fine-tuning (FT) training loss.
This is important to understand what effect the proposed regularising objective has on the model. As far as I can see, this has not been reported in the paper at the moment.
FT-M and FT-L are reported but these differ from the vanilla FT objective and update only 1 specific layer in the model. 
It is mentioned in the appendix that the proposed ICE model is trained by updating the same layers as MEMIT, which would be 5 layers.
There needs to be a baseline that updates the same layers as the proposed model using the same FT objective, with the only difference being that the proposed ICE loss component is turned off (lambda = 0).

The clarity of the paper could be improved.
For example, Section 3.2 seems to propose a method but the actual mechanics or motivation are unclear to me. And then it is said that actually this method is equivalent to the vanilla method described in the previous section anyway.

The novelty of the method is somewhat overstated in the paper. The technical solution is essentially the same as previous work such as Snell et al (2022), the main thing changed is the content of the prompt. That paper is indeed referenced but only among a list of different directions. The particular novel aspect of the paper should be made clear and previous work should be attributed accordingly. As far as I can see, the novel aspect is the application of this method to updating facts in the LLM.

---------------------------
Updated after discussion:

It seems the missing baseline is actually included, it was just not clear from the presentation. I have increased my score accordingly. Although it is still a bit unclear which of the two baselines is then the lambda=0 equivalent.

Regarding novelty compared to Snell et al (2022): Even though you frame this conceptually as a regulariser here, the practical method is still essentially the same. The author response did not present any specific differences. This previous work should be highlighted accordingly in the paper.

### Questions
What is the value of lambda used? Was a different value used for different datasets? How was this value found?

Why is the WikiBio dataset the only one missing the Portability score?

Perplexity is reported as an evaluation metric but is that the perplexity of the trained model itself or the perplexity of some other reference model on the generated text? 

It is said that one of the baselines "demonstrated nearly the best performance" in a survey. Why was the best model not reported as a baseline?

The information about which layers are updated by the proposed method should be in the main paper, not hidden deep in the appendix. The main paper currently only mentions this information for "other baselines" and the proposed model does not qualify as a baseline.

Given the very imminent US elections, the example used throughout the paper should probably be updated.

### Soundness
3

### Presentation
3

### Contribution
3
