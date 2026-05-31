## Human Reviewer 1

### Summary
In this paper authors perform a sensitivity analysis of "Chinchilla" [1] scaling laws of LLMs (approach 3 - parametric $L(N,D)$ fit), that prescribed a compute-optimal token-to-parameters (TTP) ratio being constant. The authors perturbed model parameter count $N$ in 4 systematic ways (multiplicative, additive, systematic bias, log-normal noise) and re-fitted Chinchilla scaling laws on the perturbed data. They find out that Chinchilla's constant optimal TTP ratio holds to some extent with both multiplicative and with added noise and in general Chinchilla's prescriptions are reliable.

1. Hoffmann, Jordan, et al. "Training compute-optimal large language models." arXiv preprint arXiv:2203.15556 (2022).

### Strengths
- Analyzed the ambiguity in Chinchilla's model parameters count.
- Systematic model parameters perturbations like additive term, don't affect main Chinchilla claims - constant token-to-parameter ratio.
- The paper is well written and concise.

### Weaknesses
### Weaknesses

- The main weakness of this work is the lack significance. In the abstract and the introduction, authors lay out the motivations behind this paper: can Chinchilla's prescribed token-to-parameter ratio be trusted? Unfortunately, the paper answers this question only partially: if we have a systematic error in counting model parameters, the compute optimal TTP will likely be constant. However, the paper doesn't give any insight whether Chinchilla's initial $L(N,D)$ functional form, from which the optimal TTP ratio is derived from, is reliable in the first place. Handful of recent works looked into other functional forms and/or approaches that prescribe other TTP ratios [1,2,3]. Despite, the findings presented in the paper being valid and important, I don't think the analysis is deep enough and the paper's insights add to our understanding of compute optimal scaling of LLMs.

### References

1. McLeish, Sean, et al. "Gemstones: A model suite for multi-faceted scaling laws." arXiv preprint arXiv:2502.06857 (2025).
2. Li, Houyi, et al. "Farseer: A Refined Scaling Law in Large Language Models." arXiv preprint arXiv:2506.10972 (2025).
3. Hu, Shengding, et al. "Minicpm: Unveiling the potential of small language models with scalable training strategies." _arXiv preprint arXiv:2404.06395_ (2024).

### Questions
- What data was used for the fits? What was number of points and $N\times D$ combinations?
- Are the wide confidence intervals in chinchilla due to systematic errors (i.e. noise in the model parameters estimation)? 
- How the predictions of Chinchilla change with perturbations? E.g. how the $L(N,D)$ extrapolation changes with perturbation on larger compute budgets?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
The paper analyses Chinchilla scaling law's robustness w.r.t. the model parameters. It does two experiments: (1) reran the Chinchilla fit with two different interpretations of model parameter counts, besides the Chinchilla one; (2) introduce synthetic error / perturbation to model parameter counts to test for the robustness of the Chinchilla fit. The paper found that in both experiments, the Chinchilla scaling law does not meaningfully change and Chinchilla scaling law are most sensitive to additive or systematic errors, but overall, Chinchilla’s key results withstand sizable perturbations.

### Strengths
The paper is well written and is focused on one problem. Robustness of the scaling laws is an important problem as it affects its predictive power.

### Weaknesses
1. While robustness of Chinchilla scaling law is an important problem, I believe the paper would be greatly strengthened it is more based on real-world use cases of the Chinchilla scaling law, so that findings can guide practice. Currently, it is more theoretical studies. For example,

1-1: the first experiment consider three possible model parameters counts: Chinchilla's reported model parameters, best fit, and standard formula. I feel instead of best fit, the choice of model parameters could be based on how people actually count model parameters, for example according Kaplan et al, Hoffmann et al, whether embedding weights are included, whether efficient implementation of operators that reduces parameters are considered.

1-2: The second experiment is based on synthetic perturbations of model parameters, while such robustness understanding is helpful, I believe it would be made more practically helpful if the analysis is based on realistic variation in how people count parameters.

2. I am curious and hope the authors could elaborate in revision, what previous works have also analysed the model parameters count aspect of the neural scaling law (Kaplan, Chinchilla, or others), what are their findings, and how this work compares to them and finds anything novel. For example, Porian et al also discusses different model parameters counts in detail in their table 2 and Appendix B in Appendix, conducts experiments with two different kinds of models counts and compare them in Figure 1 and 7, and found "limited difference" in scaling laws. Elaborating this point in paper would help readers better position this work in context. I note that while line 48 ~ 53 mentions existing works, the discussion do not more specifically touch on experiments & findings related to model counts and robustness. 

- Porian, Tomer, et al. "Resolving discrepancies in compute-optimal scaling of language models." Advances in Neural Information Processing Systems 37 (2024): 100535-100570.

3. I encourage the authors to describe more details how existing works count parameters, like in Kaplan et al, Hoffman et all, and other works. This helps readers understand where the descripency is in the real world. Appendix B in Porian et al would be a good example. 

4. I wonder how exactly Hoffman et al calculates mode counts? I understand this information might be missing from the original paper. But I also read from Appendix B in Porian et al that "Hoffmann et al. [25] account for both linear and attention layers in their
FLOP computation essentially using Neff in their first two estimation approaches. However, their third approach appears to ignore the attention FLOPs and also count the embeddings parameters,i.e., setting N′ = N + dv." It would be very helpful if the authors understand how Hoffman calculates model parameters and also describe in main paper. And then, the best fit model count will not be necessary.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
In spirit of number of previous works, the paper revisits the Chinchilla scaling law study, noting that model parameter counts used in Chinchilla’s analysis are ambiguous, which leads to question how the perturbations in model param counts would impact important conclusions from the study like the claimed token to parameter (TTP) ratio (heuristics of ~20 tokens-per-parameter) in which many practitioners arguably still trust. 

To answer this question, authors first investigate three interpretations how Chinchilla study may have determined the model params - i) via Table A9 from original study (original reported params) ii) via using standard formula for transformer arch param numbers (standard params) and iii) via a best fit formula used by authors that comes close to reported params (best fit). Authors find that despite relative error of up to 15.2\% in param numbers between those sets, the parametric fit L(N,D) and the resulting $D_{opt}/N_{opt} (C)$ fits do not differ substantially. 

Further, authors conduct a perturbation study to test how sensitive the scaling law fits are to various errors in model param estimation. Authors distort the parameter counts of the original Chinchilla’s experiments in four structured ways: multiplicative scaling, additive offsets, systematic geometrical bias, log-normal noise. They then re-fit the parametric loss L(N,D) and examine how the implied compute-optimal TTP shifts. The reported finding is that for multiplicative and random‐noise perturbations the TTP fit remains rather stable, while for additive or systematic bias perturbations the TTP fit slope can change significantly. Overall, the authors draw the conclusion that Chinchilla’s core result — estimates for compute-optimal TTP ratio $D_{opt}/N_{opt}$ — is robust to various potential errors in parameter counting. The authors state thus that while Chinchilla’s experimental data has ambiguities, the guidance it gives for practitioners is still valid.

### Strengths
* The paper addresses an important issue: how much does misspecification of model parameter counts might affect the validity of derived scaling laws, focusing on Chinchilla case as the one still very much relevant for practitioners.
* Three alternate parameter interpretations is a convincing study showing the insensitivity of the scaling law fits to moderate (~15 %) parameter disagreements.
* The perturbation framework containing the four types of perturbation (multiplicative, additive, systematic bias, log-normal noise) covers realistic modes of parameter‐miscounting (e.g., whether embeddings/attention/FFN are fully counted, rounding, etc).
* The paper is clearly written: it explains well the motivation, methodology and results.

### Weaknesses
1. Main weakness in my opinion is the strong claim of Chinchilla conclusions eg with regard to TTP estimates being good guidance for practitioners following the conducted study. In my opinion, the paper convincingly shows that possible perturbations of model param numbers do not alter substantially scaling law fit as conducted in Chinchilla study. However, it does not make clear whether the conclusions from those fits are justifiable. Eg if we look at Fig 2, the D/N fits show high uncertainty, making especially for larger scale compute region above $10^{22}$ unclear what TTP estimate to take. It appears that even the slope of D/N fit might change from negative to positive, making a strong difference for TTP conclusions on larger scales. While this is not the deficit of the current work and is inherited from Chinchilla design, I think the statement abour relying on const 20 TTP is confusing, as the study does not deal with repairing this particular deficit of original Chinchilla work.

2. I think as the study deals with effect of model param perturbations only, one has to be again cautious to make a general statement about Chinchilla hints to be reliable - as also further elements of the study, eg dataset composition nature etc, can be in same way source of changing the important trends as model param perturbation, which is though not checked by the study.

3. There is no enough detail about the data used for the current study. It seems that authors rely on previous work done by Besiroglu et al to extract the data from original Chinchilla plots, but it is nowhere mentioned.

4. It is not clear why authors rely only on Chinchilla data to make a case for TTP recommendation testing. Eg, Llama 3 reports also offer numerous datapoints that were used to fit scaling laws and it would be good to understand whether TTP estimation there leads to same or different results as in Chinchilla, which would provide for practitioners more consistency if both were aligned in their recommendations derived from scaling law fits.

5. It seems there is not a clear validation of scaling law fits, eg using held out points, to make sure that obtained fits actually retain the sufficient quality. This was also not performed in original Chinchilla study, validation there was arguably done by using three different approaches and observing similar trends. Here authors use only Approach 3, parametric loss fit, and there should be a way to show that obtained fits are actually to be trusted.

6. I think some relevant citations are missing. Eg FarSeer https://arxiv.org/abs/2506.10972 or https://arxiv.org/abs/2410.11840

### Questions
1. Can the authors point to exact data they are using to conduct their scaling law fits?
2. Can the authors provide any evidence that scaling law fits they obtain are of sufficient quality, eg by conducting MSE/prediction error measurements on held out points?
3. Can the authors elaborate on studies like FarSeer https://arxiv.org/abs/2506.10972 that indicate that Chinchilla style compute optimal TTP advice might be entirely off for the larger compute scales? Would that affect the message of the current work?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper investigates the definitional ambiguity surrounding model parameters within the Chinchilla study. The analysis demonstrates that while the relative error among the three distinct parameter computation methods is substantial , the resulting impact on the final, compute-optimal data-to-parameter ratio is found to be negligible.

### Strengths
A significant strength of this work lies in its compelling research perspective, which undertakes a rigorous analysis of a previously existing, yet imprecisely defined, theory. The experimental design is thorough, providing robust validation for the conclusions drawn. Furthermore, the manuscript is exceptionally well-written, demonstrating a high degree of clarity and fluency.

### Weaknesses
* Objectively, the research findings of this paper offer a comparatively limited marginal contribution. 
* Furthermore, despite the highly insightful nature of the original Chinchilla work, its practical application value within the industry remains constrained.

### Questions
Relative to the widely cited $\sim 20:1$ Chinchilla scaling ratio, the training token counts for current open-source large language models (LLMs) such as Qwen's 1B to 32B parameter series are consistently maintained at over 1 Trillion tokens. Does this training regimen constitute excessive training (over-training), and, crucially, is it an appropriate scale for exploring current scaling laws? Specifically, what guidance does this observed practice offer regarding the determination of optimal hyperparameters?

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
6

### Confidence
4