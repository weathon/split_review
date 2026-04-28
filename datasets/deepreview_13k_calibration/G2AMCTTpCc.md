# Taming Continuous Spurious Shift in Domain Adaptation

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Recent advances in domain adaptation have shown promise in transferring knowledge across domains characterized by a continuous value or vector, such as varying patient ages, where "age'' serves as a continuous index. However, these approaches often fail when spurious features shift continuously along with the domain index. This paper introduces the first method designed to withstand the continuous shifting of spurious features during domain adaptation. Our method enhances domain adaptation performance by aligning causally transportable encodings across continuously indexed domains. Theoretical analysis demonstrates that our approach more effectively ensures causal transportability across different domains. Empirical results, from both semi-synthetic and real-world medical datasets, indicate that our method outperforms state-of-the-art domain adaptation methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposed handling spurious features with continuous distribution shifts. The authors employed a causality-based method combined with representation alignment to solve this problem. Experiments on synthetic and real-world medical datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. The authors identified an interesting problem of continuous spurious shift and proposed an algorithm to handle it.

2. The authors provide theoretical insight into causality learning and mitigating distribution shifts.

### Weaknesses
1. The motivation of the problem setting is not well shown, and the novelty of the methodology is limited. The authors claimed to solve the causality model leaning under continuous distribution shift and attribute the challenge to the shifting spurious features. However, the proposed method is a simple combination of adversarial loss from CIDA [1] and causality learning from VOOD [2] without strategies specially designed for the proposed challenge. This suggests that existing methods can mitigate the proposed challenge. Moreover, in section 3.2, the authors only discussed the properties and assumptions of causal inference under distribution shift. No challenges specific to continuous setting are discussed.

2. Many details and intuitions of the methodology are missing.

  - Data statistics should be provided to provide a big picture of data distributions. For example, the number of patients in each domain and the label distribution in each subdomain should be provided.
  - What is the intuition behind using probabilistic encoders instead of deterministic ones? What is the intuition behind using Gaussian distribution as P(r | x) and P(v | r, x')?
  - The discriminator D(k | v) is a regressor for domain index k instead of predicted probability or distribution. How do the authors calculate log-likelihood from it?
  - The proposed data sampler P(x') "uniformly randomly samples data from different domains with different labels". However, it is not clear how it can draw samples with different labels as we don't have access to labels in the target domain.

3. Notations and concepts are not well introduced, therefore not easy to understand.

  - The notations used in the manuscripts lack enough explanation and context for understanding. For example, although do-calculus is widely used in causal inference, there should be citations and brief introductions of the related concepts for better understanding, at least in the supplementary. The same applies to transportability, identifiability, front-door criterion, etc.
  - The proof of the proposed theorems is very abstract. It is just a direct application of some existing definitions and conclusions on the specific causal graph in Figure 1. It's more like observations instead of theorems as it doesn't provide further insight into the problem setting or general conclusions.

4. Experimental setting is not comprehensive.

  - More recent baselines in continuous domain adaptation should be included for comparison, such as [3-6]
  - The encoder is probabilistic, and Monte Carlo estimation is used for inference. How is the training stability for the proposed method, and how long will it take for inference compared to other methods? Ablation studies should also be conducted to evaluate the contribution of a probabilistic encoder.
  - The authors proposed solving the continuous distribution shift problem. However, the domain in all reported experiments is discretized. Specifically, the COLORED-MNIST dataset is created in a discretized manner. It is not clear how this is different from the original domain adaptation. If the model is trained without discretization, some metrics should be designed to evaluate the performance in the continuous case.
  - Given that we can discretize the domain index space, there should be another trivial baseline that conducts original domain adaptation methods pairwise for each target sub-domain.

5. The implementation code is not available for reproduction.

References

[1] Wang, H., He, H., & Katabi, D. (2020). Continuously indexed domain adaptation. arXiv preprint arXiv:2007.01807.

[2] Mao, C., Xia, K., Wang, J., Wang, H., Yang, J., Bareinboim, E., & Vondrick, C. (2022). Causal transportability for visual recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 7521-7531).

[3] Xie, M., Li, S., Yuan, L., Liu, C., & Dai, Z. (2024). Evolving standardization for continual domain generalization over temporal drift. Advances in Neural Information Processing Systems, 36.

[4] Jin, Y., Yang, Z., Chu, X., & Ma, L. Temporal Domain Generalization via Learning Instance-level Evolving Patterns.

[5] Lin, Y., Zhou, F., Tan, L., Ma, L., Liu, J., He, Y., ... & Wang, H. (2023). Continuous Invariance Learning. arXiv preprint arXiv:2310.05348.

[6] Cai, Z., Bai, G., Jiang, R., Song, X., & Zhao, L. (2024). Continuous Temporal Domain Generalization. arXiv preprint arXiv:2405.16075.

### Questions
Please see Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors investigate the problem of continuous domain adaptation, where the domain index changes continuously. Specifically, the authors assume that the causal model P(Y |do(X)) is domain-invariant and use the variational-inference-based neural architecture. The authors evaluate the proposed method on several datasets.

### Strengths
N.A>

### Weaknesses
1.	What is the difference between the spurious shift proposed in this paper and the various shifts in domain adaptation such as covariate shift, conditional shift, and target shift? Is it unique to continuous domain adaptation? Since the author raised this question, the author should cite these papers [1][2] and provide a detailed discussion, but I am surprised that the author did not do these papers
2.	The description of the causal graph in Figure 1 is not clear. For example, why is U represented by a dotted circle, and what does the dotted arrow represent? In addition, the author should provide a practical example that corresponds to the causal graph.
3.	Some theories are questionable. For example, the author believes that P(y|do(x)) is domain-invariant, but since k also affects V, it actually changes with the domain. Lemma 3.1 feels like it was pieced together and has nothing to do with causal theory.
4.	In terms of method, it is recommended that the author add a model diagram, and it is still unclear how to implement the do operation.
5.	It is recommended that the author compare more datasets, such as RMNIST, Portrait, and Cover Type

[1] Zhang, Kun, et al. "Domain adaptation under target and conditional shift." International conference on machine learning. Pmlr, 2013.
[2] Lipton, Zachary, Yu-Xiang Wang, and Alexander Smola. "Detecting and correcting for label shift with black box predictors." International conference on machine learning. PMLR, 2018.

### Questions
N.A.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of continuous spurious shift in features along with the domain index, and introduces a method for domain adaptation. The method proposed, Continuously trAnsportable Domain Adaptation (CADA), infers causally transportable encodings and aligns the encodings across continuously indexed domains. Theoretical and empirical analysis in the paper shows that CADA enables causal transportability across domains.

### Strengths
1. The problem of continuously shifting spurious features across continuously indexed domains is an important problem and of interest to the community.
2. The description of the method is detailed and well-written.
3. The paper evaluates against multiple baselines on a semi-synthetic and two real world datasets to demonstrate the performance improvement in the presence of continuously shifting spurious features.

### Weaknesses
1. Clarity in the running example: It would be good to add more details regarding what is recorded in the breathing signal $X$ and what variables are selected. E.g., without complete details, it is hard to follow whether respiratory rate is recorded in $X$/why would it be unobserved.
2. Lack of detailed comparison with CIDA: Either in the main text (L261) or appendix, discussing comparison with CIDA will be helpful, especially as the objectives follow similar structure. This would also help understand the visualizations in Figure 3 better.  
3. Missing details in experiments:
   - How is $\lambda_d$ chosen?
   - It is only clear after looking at Figure 3 that the task is a 10-way classification – it would be good to add this earlier in text (as colored MNIST is often set up for 2-way classification as well).
   - L485-486: it would be good to describe in more detail how continuously shifting spurious features are introduced.
   -  Did you perform multiple trials of the procedure?
4. Lack of ablations: The paper makes specific choices regarding source and target domains, how shifting spurious features are introduced etc. The paper currently lacks ablations that study the effect of these choices on the performance of CADA as well as other methods.



**Minor comments:**
1. L180-182: minor grammatical error (possibly ‘while’ missing?; ‘Specifically, while Eqn 2….’)
2. L491: typo -> transportation

### Questions
Main questions are regarding missing details in the experiments. Please refer to weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors provide a new method the enhances domain adaptation performance by aligning causally transportable encodings across continuously indexed domains with strong empirical evidence and reasonable theoretical demonstration.

### Strengths
The authors did a good job in adapting previous domain adaptation approaches to the problem with continuously indexed domains and achieved good empirical performance.

### Weaknesses
Although the work is primarily about domain adaptation, there is lack of understanding on the causal problem or the medical datasets they have been studying as examples, which limits the utility and validity of the paper. Even their illustrative example is questionable as it is unclear why the 'age' serves as a domain index. If you directly use 'age' as a feature, this is a domain adaptation problem with one source and one target and I would imagine the problem can be better solved.

The authors are clearly from the field of domain adaptation but it would be more helpful if they could carefully study the causal literature as well, and interpret the values of their work in the causal context.

### Questions
Two key questions: 

1. What is the precise definition of 'spurious features'?

In the causal literature, there are variables such as interventions, confounders, mediators, moderators etc. But spurious feature is clearly not standard terminology. You need to define it explicitly.

Example 1 is actually confusing. Why doesn’t ‘respiratory rate’ work? It can still serve as a useful feature or a factor in prediction while including age as another factor. Then if you run a linear regression, it might still be good. It is questionable whether this feature is 'spurious' or not. In my opinion, it is more about including enough predictive variables to ensure that there is no hidden confounding, and about understanding the interaction between different features.

2. From a high-level, how is the proposed method different from previous approaches in dealing with spurious features?

My understanding is that the authors proposed a more principled way to deal with continuously indexed domains via adversarial training using encoder and discriminator networks with a decent causal interpretation. Basically they still fall into the category of methods that use neural networks to extract invariant features across domains. So what is the clear contrast with previous approaches like CIDA? 

They say that CIDA struggles to eliminate the influence of continuously shifting spurious features but as far as I am concerned what CIDA does is also extracting invariant features across domains. They don't necessarily exclude causal transportable representations. The fact that they didn't provide a causal interpretation does not imply that they are very different from the current work in respecting causal representations.

To be honest, I am also doubtful about the idea of eliminating spurious features to achieve invariant causal representations. As I have mentioned, the word 'spurious' is unclear. For some features, it might be more helpful to use them jointly with domain indexes rather than eliminating their effects.


Further points:

Line 160 Page 3: I would suggest expanding this paragraph as is very important, and please also provide a definition of covariate shift. The concept of covariate shift has subtle connections to confoundedness in the causal context.

I would also suggest the authors look at the line of works by Uri Shalit, David Sontag, Nathan Kallus etc. For example the following paper:
https://arxiv.org/abs/1606.03976
They also connect causal representations with domain adaptation.

### Soundness
2

### Presentation
2

### Contribution
2
