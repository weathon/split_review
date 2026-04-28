# As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Direct Preference Optimization (DPO) has emerged as a more computationally efficient alternative to Reinforcement Learning from Human Feedback (RLHF) with Proximal Policy Optimization (PPO), eliminating the need for reward models and online sampling. Despite these benefits, DPO and its variants remain sensitive to hyper-parameters and prone to instability, particularly on mathematical datasets. We argue that these issues arise from the unidirectional likelihood-derivative negative feedback inherent in the log-likelihood loss function.
To address this, we propose a novel LLM alignment loss that establishes a stable Bidirectional Negative Feedback (BNF) during optimization. 
Our proposed BNF loss eliminates the need for pairwise contrastive losses and does not require any extra tunable hyper-parameters or pairwise preference data, streamlining the alignment pipeline to be as simple as supervised fine-tuning.
We conduct extensive experiments across two challenging QA benchmarks and four reasoning benchmarks. 
The experimental results show that BNF achieves comparable performance to the best methods on QA benchmarks, while its performance decrease on the four reasoning benchmarks is significantly lower compared to the best methods, thus striking a better balance between value alignment and reasoning ability. 
In addition, we further validate the performance of BNF on non-pairwise datasets, and conduct in-depth analysis of log-likelihood and logit shifts across different preference optimization methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an alternative to DPO and its variants such that $|\frac{\partial{\mathcal{L}}}{\partial{z_y}}|$, the norm of the derivative of the loss with respect to the logits of a given outputs, decreases linearly as $p(y|x)$ deviates from the $p_{ref}(y|x)$ in either direction. The loss is called Bidirectional Negative Feedback, in contrast to what the paper describes as unidirectional negative feedback in the likelihood loss, namely that $|\frac{\partial{\mathcal{L}}}{\partial{z_y}}|$ increases as $p(y|x)$ decreases. 

The paper also demonstrates how various DPO-series methods avoid excessive decreases in the likelihood of dispreferred samples relative to a loss that just applies NLL to the preferred samples and its negation to dispreferred samples: the gradient for these losses includes and additional scaling term $\mathcal{C}(y_w, y_l, p_\theta, p_{ref})$ that decreases as the gap between $p_\theta(y_w|x)$ and $p_{ref}(y_l|x)$ increases. However, they argue that these losses are unideal due to their sensitivity to the hyperparameter $\beta$.

Experimentally, BNF outperforms other DPO-style losses overall when evaluated across 2 instruction-following QA datasets and 4 logical reasoning datasets, using the preference training datasets from the SimPO paper. Moreover, because BNF is not a pairwise contrastive loss, it is applicable even with non-pairwise data (e.g., sometimes just a preferred or a dispreferred sample without a counterpart), and experiments show that BNF can still improve over the base model in such settings. The authors also show that BNF exhibits the least amount of log likelihood shifts as well as the lowest Gini coefficient in the logit shifts across tokens in a sequence.

### Strengths
1. The paper exhibits strong experimental results supporting the use of BNF over the baselines tested.
2. The paper is easy-to-follow and makes progress on a relevant topic for the ICLR community.
3. BNF is novel and well-motivated by the desire to decrease gradient norms as the log probs deviate more from the reference log probs.
4. BNF improves upon DPO-like methods empirically and in applicability (going beyond pairwise data alone).

### Weaknesses
1. The authors point to two problems for DPO-like baselines (i.e., training collapse and alignment tax) but only seem to show positive results of BNF for one, i.e., less alignment tax. It would be helpful to see a precise definition of training collapse and show that BNF experiences less of it (or avoid framing the paper's story with training collapse). The paper does not provide a clear definition of training collapse, nor does it demonstrate that BNF mitigates this issue. The experiments in Appendix D, while helpful, do not directly address the specific degradation in performance during training that the authors seem to imply by the term 'training collapse'.
2. The authors mention that DPO-like baselines with an additional NLL term have limitations (i.e., poor chat and QA performance), but it is not clear to me that BNF overcomes these specific limitations when trained on the same datasets. While the paper introduces CPO as a baseline, it is not clear if the performance issues of DPO-like methods with an NLL term are overcome by BNF on the same datasets, especially in chat and QA scenarios. The experiments should explicitly compare BNF against DPO+NLL baselines on the same datasets to validate this claim.
3. While I believe that the paper makes sound and sufficient contributions, #1 and #2 point to a misalignment between the motivation for the work in the introduction and the contributions demonstrated in the body of the paper. Section 2.3 and Figure 2 are another example; they discuss various challenges and limitations, but it is not clear how each relates back to the paper's contributions. Also, for how focused this section is on the specifics of pairwise preference data in reasoning tasks, it is strange that the experiments don't explore training on such data. The paper's motivation, particularly around the limitations of DPO-like methods with NLL terms, is not fully supported by the experimental results. Section 2.3, while discussing relevant challenges, does not clearly link these issues to the specific contributions of BNF. Furthermore, the experiments do not fully explore the nuances of pairwise preference data in reasoning tasks, despite the discussion in Section 2.3.
4. The paper could benefit from being more careful in distinguishing claims from hypotheses. For instance, in lines 496-471: "This suggests that BNF achieves a balanced optimization strategy, reducing the gradients for tokens already showing large differences from the reference, thereby effectively preventing over-fitting and reducing the alignment tax." The logical leaps from smaller gradients for large differences to less overfitting and less alignment tax are not directly supported in the paper. Also, in the same section, it is not clear why a lower Gini coefficient is necessarily desirable in the first place; for instance, for some sequences it may be more desirable to just decrease the probability of the incorrect tokens rather than all tokens. Moreover, lines 54-55 state: "we argue that the instability of DPO stems from a more fundamental cause: the unidirectional likelihood-derivative negative feedback inherent in log-likelihood loss." While this is a reasonable hypothesis, it is not a claim that has been definitively proven; thus, rephrasing this section as a hypothesis that guides the development of an alternative loss may be more apt. The paper makes several claims that are not fully supported by the evidence presented. For example, the link between smaller gradients for large differences and reduced overfitting/alignment tax is not directly demonstrated. The desirability of a lower Gini coefficient is not clearly justified, and the claim about the fundamental cause of DPO instability should be framed as a hypothesis.

### Questions
1. Could the authors provide evidence of BNF's favorability with respect to training collapse?
2. If BNF is meant to be an alternative to simply adding a NLL loss term to DPO-like methods, can the authors compare the proposed method with these baselines?
3. Could the authors explain how each point made in Section 2.3 connect to a contribution or result in the paper / positive property of BNF?
4. Could the authors clarify the central claims in the paper and distinguish them from statements that are hypotheses?
5. Could the authors explain why the BNF loss is the way it is, e.g., why it necessarily needs to look as complex as it is when the main goal is to simply avoid an increasing gradient norm for large deviations? 

I would be happy to raise my score if these above concerns are addressed.

### Soundness
2

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
3

### Summary
This paper proposes a new LLM alignment loss to address the issues of DPO variants being sensitive to hyper-parameters and unstable in mathematical tasks. The loss can maintain Bidirectional Negative Feedback (BNF) during optimization and eliminate the need of additional hyperparameters and pairwise preference data. Finally, they evaluate the method on multiple tasks and backbones to verify its effectiveness.

### Strengths
1.	This paper clearly outlines the previous methods and theoretically identifies their weaknesses. The motivations of this paper are clear.
2.	In terms of these issues, the authors propose their method and validate the effectiveness through theory and extensive experiments on multiple tasks and LLMs.
3.	The structure of this paper is clear, and the equations and charts are well-presented.

### Weaknesses
1. Figure 2 illustrates the challenges of creating a substantial log-likelihood gap in mathematical tasks. Could you demonstrate the advantages of your method with similar examples in mathematical tasks? Specifically, how does the proposed loss function handle scenarios where the difference between preferred and dispreferred responses is subtle in the mathematical domain? Providing a visualization or a comparative analysis similar to Figure 2, but focused on mathematical tasks, would strengthen the argument for the method's effectiveness in this area.
2. I am somewhat puzzled by Eq.(6). What are the motivations behind designing the equations where $y_i \neq t_i$? It appears to be a careful design. The rationale for introducing the condition  $y_i \neq t_i$ in the second term of Equation (6) is not immediately clear. Could you elaborate on the theoretical underpinnings of this design choice? Specifically, how does this condition contribute to the overall effectiveness of the loss function, and what would be the implications of not having it?

### Questions
See above weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes Bidirectional Negative Feedback (BNF), an LLM alignment loss that does not rely on pairwise contrastive losses.  Consequently, it does not require pairwise data and has fewer hyper-parameters compared to DPO. The authors empirically show that the models` reasoning ability is less affected when using BNF for preference optimization. They compare BNF to previous approaches such as DPO, IPO, KTO, SLiC-HF, ORPO, SimPO on QA and reasoning benchmarks.

### Strengths
- BNF has fewer hyper-parameters compared to DPO. If the method is robust to hyper-parameter tuning, this could make LLM alignment more compute efficient. 
- BNF does not require pairwise data. 
- The baselines are diverse and strong. The hyper-parameters of the other approaches were fine-tuned (although not directly by the authors).

### Weaknesses
 - The performance across benchmarks is still relatively close to DPO. 
- Gemma lacks proper baselines as the scores were only copied from another paper.
- It is unclear if the performance gains of BNF are statistically significant across all benchmarks, or if the observed differences could be due to random variation or specific hyperparameter settings of the baselines. The paper would benefit from a more rigorous statistical analysis of the results.


### Questions
- Is BNF more sample efficient because it does not require pair-wise dataset? Is there a relationship between sample efficiency and loss/dataset type?
- Do you expect the other baselines to close in on BNF with further hyper-parameter tuning? 
- How sensitive is BNF to hyper-parameter tuning? Is it possible that the hyper-parameters are harder to tune despite the fact that they are fewer? 
- Is the performance difference on the benchmarks significant?

### Soundness
3

### Presentation
3

### Contribution
3
