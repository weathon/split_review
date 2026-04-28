# Bayesian scaling laws for in-context learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
In-context learning (ICL) is a powerful technique for getting language models to perform complex tasks with no training updates.
Prior work has established strong correlations between the number of in-context examples provided and the accuracy of the model's predictions.
In this paper, we seek to explain this correlation by showing that ICL approximates a Bayesian learner. This perspective gives rise to a family of novel Bayesian scaling laws for ICL.
In experiments with \mbox{GPT-2} models of different sizes, our scaling laws exceed or match existing scaling laws in accuracy while also offering  interpretable terms for task priors, learning efficiency, and per-example probabilities.
To illustrate the analytic power that such interpretable scaling laws provide, we report on controlled synthetic dataset experiments designed to inform real-world studies of safety alignment. In our experimental protocol, we use SFT to 
suppress an unwanted existing model capability and then use ICL to try to bring that capability back (many-shot jailbreaking). We then experiment on real-world instruction-tuned LLMs using  capabilities benchmarks as well as a new many-shot jailbreaking dataset.
In all cases, Bayesian scaling laws accurately predict the conditions under which ICL will cause the suppressed behavior to reemerge, which sheds light on the ineffectiveness of post-training at increasing LLM safety.png}\hspace{0

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper makes progress towards understanding (1) scaling laws for ICL and (2) understanding whether ICL is bayesian. In particular, it presents a scaling law for ICL via Bayesian assumptions, and validates these scaling laws using ICL behavior for small LMs trained on controlled synthetic data as well as LLMs trained on natural language.

### Strengths
1. This work investigates an interesting problem. Based on some assumptions, it proposes a new theory and validates this theory with experiments. The work also does a good job comparing the proposed scaling law to prior works. 
2. I appreciate that the experiments include both toy settings as well as real world LLMs.

### Weaknesses
The paper primarily focuses on transformers. However, it would be interesting to see some experiments for e.g., state space models, and whether ICL is bayesian in these models as well.

### Questions
I found the observation that ICL efficiency (K) roughly increases with model depth to be interesting. Do the authors have any insights about the role of model width?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a Bayesian scaling law for in-context learning (ICL). Building on prior work that suggests ICL can be understood through a Bayesian framework, the authors relate the number of in-context examples to the probability of predicting the next example. Essentially, the paper iteratively applies Bayes' theorem to model how ICL updates the task prior as new examples are encountered, ultimately deriving a functional form for the posterior distribution. Experimental results are reported on safety alignment tasks, where many-shot prompts are used to demonstrate the predictive ability of the Bayesian scaling law, including cases where prompts can bypass safeguards. The paper also compares the Bayesian scaling law to a baseline power law model, evaluating performance based on interpolation and extrapolation error, and demonstrates the superior predictive accuracy of the Bayesian approach.

### Strengths
Overall, this is a very interesting paper, as the Bayesian scaling law offers insights into phenomena such as many-shot prompt jailbreaking. If the conclusions of this work hold, they could strengthen the argument that ICL operates in a Bayesian manner.

### Weaknesses
My primary concern lies with the functional form of the posterior expectation in Equation (2). Specifically, in Equation (2), over which random variables is the expectation taken? The notation used here is somewhat unclear to me. Additionally, in Equation (17) of the appendix, the authors appear to apply the linearity of expectation, which seems to assume that E(A/B)=E(A)/E(B). Am I missing something here?

### Questions
See my comments on weaknesses

### Soundness
2

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
4

### Summary
This paper sets up “Bayesian scaling laws” which are a form of scaling law derived from the assumption that in-context learning is performed as Bayesian posterior calculation. The paper is building on recent works understanding ICL with a Bayesian framework, especially Xie et al, 2022. The paper first sets up the Bayesian posterior given by a prior and likelihood over the different tasks the model will be trained on. Parameter tying and efficiency coefficients are introduced to build up to the final scaling law. First, this scaling law is fit to trained transformers on GINC, the authors claim superiority of this scaling law over 3 baselines. Next, the paper explores the effect of SFT, and finds that 1) SFT only modifies the task prior and 2) SFT is more superficial with model scaling. DPO is explored similarly, and the authors find that DPO breaks the Bayesian ICL behavior. Finally, 6 ICL tasks are tested on real language models and the scaling law fits are analyzed.

### Strengths
Overall, the paper is well motivated, well written and clear. The experiments are all asking very important questions. Here is a list of strengths:

Contributions:

C1: The result clearly separating SFT’s effect on the prior vs in each distribution is interesting and useful to understand how ICL abilities are affected by SFT. 

C2: SFT being increasingly superficial (prior change only) on larger models is interesting, and suggests an important phenomena to study as we scale models.

C3: In general, developing interpretable scaling law from first principles is a good and useful idea.

C4: Showing that DPO destroys Bayesian ICL behavior unlike SFT clearly demonstrates a qualitative change depending on the choices at the fine-tuning stage.


Presentation:

P1: The paper is very well written, the motivation of the work, the development of the theory and the experiments are very clearly described.

P2: The paper’s narrative makes important points about why this work is needed, e.g. “Interpretable scaling laws”

### Weaknesses
Even though the paper is great at a conceptual level, unfortunately, many claims are weakly justified. I think the paper has enough qualitative contributions and does not require a justification of competence by scaling law “benchmarking”. In fact, I don’t think the paper’s contribution is degraded at all even if the fits went worse, as the importance of this paper, for me, is that the authors developed a framework to fit a scaling law and interpret its terms, allowing qualitative insights of how Bayesian ICL is, not that NRMSE got 0.02 better. I truly believe this paper has great potential, but here are the main weaknesses:

W1: Even though Table 1 is the basis to the claim “our scaling laws exceed or match existing scaling laws”, it isn’t clear how robust this claim is. The best method alternates between the different Bayesian methods, and the gap with the best base method is very thin. The weight tying scheme introduced gives too many degrees of freedom to set up a Bayesian method (I’m not saying too many model parameters, but many ways to set up different methods, e.g. low rank P matrix) and it is unclear how much this choice will affect the results. Also about significance: Will the DPO fit result stay insignificant even if the number of sample is 10x?

W2: The scaling curves and the fits are not shown as plots for the GINC experiments, preventing the reader from assessing the goodness of fit by eye. Adding these plots will also contribute to making the better performance claim more robust.

W3: I do not understand how Figure 5 supports “DPO can use very little training data to successfully suppress the disfavoured HMMs beyond the ability of ICL to recover.” Is the critical part that the disfavoured classes fall to 0.0 and not something close to 0.1 ? If so, I don’t get the “very little training data” part. If it turns out that this is my misunderstanding, I will reflect this to the final evaluation.

W4: I am not sure if I agree that these results support that LLMs behave in a Bayesian way, from the goodness of fit I see in Figure 6, I would rather argue that they behave in a very non-Bayesian way, especially the instruct models. Even if it outperformed the base scaling laws for these experiments, I do not see why this supports that LLMs do Bayesian ICL since the goodness of fit doesn’t seem persuasive.

W5: The parameter tying and introduction of the efficiency coefficient K is not well justified. Could the intuition behind the tying scheme be clarified?

W6: The paper makes multiple claims about model scaling. However, are these models trained for the same number of steps or (theoretical) FLOPs? Given pre-training scaling laws and the general observation that bigger models train faster (when measured in gradient steps), is it possible that bigger models are just effectively better trained? I see this as a major concern, as real LLMs are trained near the compute optimal frontier, and if small models here are undertrained, the results might be confounding model scale and optimization. At the very least, I believe the equal number of FLOPs should be given for the small models instead of equal gradient steps.

Most weaknesses seems to be addressable, I am willing to modify my score if most of these are addressed, since as mentioned above, the paper makes great points.

### Questions
Questions:

Q1: Line 121/122: should the prior be $\rho$ instead of $p$? In general I see both $p$ and $\rho$ for prior throughout the paper. Consistency would help, if possible.

Q2: Why is the prior not included in $\mathcal{M}$ in Theorem 1?

Q3: In section 3.1 are the words “task” and “distribution” used interchangeably? Here also consistency would help, if possible.

Q4: Why is NRMSE a better choice than KL divergence from the ground truth probabilities? What would you expect if the calculations were done with KL divergence?

Q5: I guess Figure 2b is for interpolation? It would be better to write this down explicitly.

Q6: (Optional) Would you be able to adjust figure 1’s colors so that it's colorblind friendly?

Q7: It would be good to have a plot showing the scaling law fit itself. (See W2)

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
3

### Summary
This paper tries to establish several Bayesian-type scaling laws for In-context learning (ICL).

### Strengths
It is reasonable to interpret context relationships by Bayesian inference. Besides, whether a scaling law holds is crucial to the extendibility of a large model (LM). Hence, it is a good motivation to establish Bayesian-type scaling laws for ICL.

### Weaknesses
1.The biggest problem of this paper is the lack of theoretical support, deduction, illustration, and explanation of the scaling law Eq. 3 (Final scaling law). The Bayesian formula Eq. 2 is a normal one and the deduction of Eq. 2 (Appendix A) is a common technique in Bayesian inference. However, this paper lacks evidence in deducing Eq. 3 by Eq. 2, though Eq. 3 is somewhat heuristic. Eq. 3 seems to appear suddenly without sufficient explanations. Specifically, the introduction of the ICL efficiency coefficient ($K$) and the weight-tying scheme are not rigorously justified from a theoretical perspective. The paper does not adequately explain why these specific modifications to the Bayesian framework should lead to a valid scaling law for ICL. The connection between the Bayesian formulation in Eq. 2 and the final scaling law in Eq. 3 remains unclear, making the proposed scaling law seem arbitrary.

2.As for particular implementation, the authors take logarithms for non-Bayesian cases and Bayesian scaling laws in different places, respectively. For example, the logarithm is taken outside the whole likelihood, which leads to a negative log-likelihood in the Bayesian scaling laws. However, the logarithm is taken inside the likelihood, and a 1 is added in the denominator, in the non-Bayesian cases. Moreover, the torch.clamp is also used to constrain the log-space parameters to the range (−20, 20), which may significantly affect the experimental results. The inconsistent application of the logarithm and the use of clamping raise concerns about the validity and comparability of the experimental results. The paper does not provide sufficient justification for these choices, nor does it explore the potential impact of these implementation details on the conclusions.

3.This work lacks analysis of how the error be scaled. Given the scaling law Eq. 3, how would the error be scaled and amplified by the current scheme? It can be seen that the errors of the parameters could be amplified along with K (exponentially), n (exponentially), and M. Even if a logarithm is taken, the error may still be of considerable magnitude. Is there any treatment to suppress or control the error along with such a scaling law? The paper does not address how the proposed scaling law affects the error propagation, especially with respect to the parameters K, n, and M. The lack of error analysis makes it difficult to assess the reliability and robustness of the proposed scaling law. The potential for error amplification, particularly with increasing n and M, is a significant concern that needs to be addressed.

### Questions
Please address the problems raised in the weaknesses part.

### Soundness
1

### Presentation
3

### Contribution
2
