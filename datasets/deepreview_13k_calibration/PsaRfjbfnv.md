# Evaluating Model Robustness Against Unforeseen Adversarial Attacks

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 8, 3

## Abstract
When considering real-world adversarial settings, defenders are unlikely to have access to the full range of deployment-time adversaries, and adversaries are likely to use realistic adversarial distortions that will not be limited to small $L_p$-constrained perturbations. To narrow in on this discrepancy between research and reality we introduce ImageNet-UA, a new benchmark for evaluating model robustness against a wide range of unforeseen adversaries. We make use of our benchmark to identify holes in current popular adversarial defense techniques, highlighting a rich space of techniques which can improve unforeseen robustness. We hope the greater variety and realism of ImageNet-UA will make it a useful tool for those working on real-world worst-case robustness, enabling development of more robust defenses which can generalize beyond attacks seen during training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the ImageNet-UA benchmark and the UA2 metric to assess model robustness against a variety of unforeseen adversarial attacks. Experimental results indicate that traditional Lp robustness training may have limitations when addressing unknown attacks. The paper suggests employing L2 adversarial training combined with image augmentations to enhance model performance under these unexpected attack scenarios.

### Strengths
1. The paper conducts comprehensive experiments using a set of 19 diverse non-Lp attacks, offering a thorough evaluation of model robustness in the face of various unforeseen adversarial scenarios. 

2. By introducing the ImageNet-UA benchmark, the paper fills a gap in adversarial robustness research, enabling a more applicable assessment of model resilience to real-world adversarial attacks beyond traditional Lp constraints.

### Weaknesses
1. A considerable portion of the logical content is relegated to the appendix, which is suboptimal. Key elements of the logic should be presented within the main text. For instance, Figure 5 should either be compressed and included in the main paper or replaced with an equivalent narrative explanation.

2. In Figure 3, the term $m \times m \times 2$ lacks a corresponding definition, which should be clarified. Specifically, the role of the '2' in the context of the latent variable optimization needs to be explained.

3. Equation 2 suggests that the adversarial attack should aim to maximize the loss function with respect to perturbations, rather than as currently presented. The current formulation appears to minimize the loss, which is incorrect for adversarial attacks.

4. The study mainly employs various image augmentation techniques to examine model performance without contributing significant advancements in model verification methods (i.e., assessing stability across augmented samples), which falls short of the standards for ICLR. The paper lacks a rigorous analysis of how these augmentations affect the model's decision boundaries and generalization capabilities, and it does not propose a method to verify the robustness of the model against the specific augmentations used.

### Questions
Refer to Weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose ImageNet-UA, a benchmark for evaluating model robustness against unforeseen adversarial examples, i.e., adversarial perturbations not considered in the design phase of the model. Supposing the models' developers do not have access to worst-case adversarial examples during training, the benchmark proposes a set of non-Lp gradient-based attack methods as worst-case inputs to evaluate the model's robustness at test time. The authors provide an in-depth analysis of various adversarially trained models on different datasets from the benchmark.

### Strengths
- The authors designed and evaluated 19 non-Lp adversarial generation methods. 
- The authors proposed a wide analysis of the benchmark on several models and different datasets.

### Weaknesses
 - The authors did not compare the benchmark to other $L_p$ attack methods in the state of the art. Additionally, there is significant work that should be included in the comparison or at least mentioned in the related work

In section 4.1 the authors compare UA2 to other distribution-shift benchmarks, and they claim, based on the results (Table 5), that UA2 is a measure of worst-case robustness, like $L_p$, but they did not assess the distributional shift of $L_p$ perturbed samples. 
Additionally, there have been recent workshops and efforts to address the real-world issues applied to ImageNet, and the authors should provide some references and possibly differentiate their work from these. One example is the ShiftHappens workshop at ICML 2022 https://shift-happens-benchmark.github.io

- The author’s evaluation of their adversarial training method is incomplete.  

In the Experiments section, there is a broad discussion on how UA2 robustness, based on the evaluation of unforeseen adversarial example, is distinct from  $L_p$ robustness. However, the authors based this claim on the evaluation of just one $L_p$ attack method (PGD) and just on $L_\infty$  bound constraints, with a fixed number of optimization steps (only $50$, very limited for ImageNet, and without providing evidence of convergence).  

- The authors introduced a new metric UA2 (Unforeseen Adversarial Accuracy), but it is unclear why the new metric is necessary. 

The authors introduce the UA2 (Unforeseen Adversarial Accuracy) metric as the average Robust Accuracy achieved by the model over the non-$L_p$ methods in the benchmark. Although this metric provides an overall score relative to the benchmark, it doesn't allow for a thorough assessment of which attacks are truly effective (and thus worst case) and which are not. For example, the results with 'medium distortion,' shown in Figure 8, clearly indicate that three types of attacks (Elastic, Wood, Gabor) generally perform better than the others. 
Additionally, it's not clear why the authors use the average in this metric rather the worst case (so the perturbation that has the strong effect) Unforseen Adversarial, which would be an ensemble attack composed by all the attacks rather than single evaluations.

#### Additional comments:

In sect. 3.3, the authors select eight attacks out of the nineteen, but they don't give a justification on why they selected these. Specifically, is there a possibility that other, non-selected attacks, are super effective against specific models? A more substantial contribution would be to understand in which cases (e.g., for which preprocessing techniques or for which type of models) one attack works better than the other. As an example, a useful actionable insight would be "one can exclude attack A, B, C as the preprocessing technique would remove such perturbation". This insight gathering is lacking in the paper but it would be much more useful to enhance robustness evaluations to unforseen attacks.

In sect. 3.3, the authors suggest quantization only in the JPEG compression strategy, however it's still to be observed that, given that the benchmark is specific to the image domain, in theory all the manipulations should still produce images (thus quantized in integer values in [0, 255]). This aspect seems overlooked in the paper (at least in the text).

In section 4.2 the authors propose a combined adversarial training approach that consider $L_\infty$ adversarial training and "PixMix" augmentation. The authors' analysis of PixMix is incomplete in two ways. First, they don't explain what PixMix is or provide any reference. Second, in Table 6, they only show improvements in the UA2 metric, without evaluating how this adversarial training method affects the $L_p$ robustness. 

Generally, the authors evaluate the robustness of models adversarially trained on a specific kind of $L_p$ perturbation, against attacks that optimize for a different type of $L_p$ perturbation. Indeed, the benchmark is composed of non-$L_p$ methods which optimize the adversarial sample considering both $L_\infty$ and $L_2$ constraints. When comparing with $L_p$ attack methods the authors considered only $L_\infty$.  


#### Minor issues:

- there is a mixed use of american and british english (e.g., defenses and defences). Please, double check and remain consistent throughout the manuscript
- Figure 3 could benefit from a more structured presentation. Specifically, naming the steps and providing a step-by-step overview would help understand the approach better

### Questions
1. Could you argue why certain non-$L_p$ attack methods are more effective than others? 

2. Could you report the $L_p$ robustness of the models adversarially trained with $L_\infty$ and with $L_\infty$ + PixMix? 

3. Could you report the results for an increased number of steps? Or please, provide evidence of convergence for the attacks.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a set of 19 new non-Lp attacks for measuring unforeseen robustness.  The authors introduce a score called UA2 which measures robustness across a set of 8 of these attacks for benchmarking existing models.  Additionally, they provide experiments to demonstrate that robustness against these non-Lp attacks is directly correlated with Lp attack robustness or distribution shift robustness.  The authors also evaluate several defenses including combining adversarial training with image augmentation (PixMix), multiattack training, and perceptual adversarial training.

### Strengths
- The authors propose many new attack types which can be used for measuring unforeseen robustness
- Extensive experiments measuring the performance of the current state of research against the set of attacks proposed
- Writing is clear

### Weaknesses
Overall, I thought this was a strong paper.  One thing that could be incorporated for strengthening the paper could be adding some evaluations on the attacks left out of the 8 core attacks and demonstrating that the performance measured over the left out attack set is correlated with performance measured over the 8 core attack set.  This would empirically demonstrate that the performance on the 8 core attacks are highly representative of the 19 attacks.

Minor typos:
- Table 1 caption: "disctinct"
- line 318: $\varepsilon_a$ notation as opposed to $\epsilon_A$ used elsewhere

### Questions
- In section 4.1 comparison to ImageNet-C what does "non-optimized" version of the attack mean?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper propose a benchmark of adversarial attacks computed on different noise patterns.
These are made differentiable, and applied to images with PGD. Models are adversarially trained under a specific perturbation, and evaluated with others to test whether they have generalized across unseen attacks.

### Strengths
**Models should be robust to whatever noise it appears.** I agree with the authors that model must be resilient to *any* perturbation of images, and testing more attacks is always useful.

**Robustness augments when diversifying the noise.** It is interesting to notice that models behave better when their training is enriched with the various noise patterns. However, this is somehow trivial due to the formulation of adversarial training: the better the approximation of the inner maximization is, the more robust the model it gets. Still, the authors did the right experiments, showing that this is empirically proved also in this setting.

### Weaknesses
 **The presented strategies are L$_p$-bounded attacks.** I disagree with the authors stating that the proposed attacks are beyond the L$_p$ norm. In particular, it can be still computed the amount of perturbation and bounded to the maximum budget. The whole optimization problem can also be written as an L$_p$ problem, and constrained to be such a problem. Maybe the projection is a bit different, because the authors want to use specific patterns. Hence, all the discussion regarding going beyond that threat model does not apply on this paper.

**No details on the attack.** The authors spend a lot of space to present the manipulations, and they vaguely state they are differentiable. However, I could not understand how. This content *must* be present in the main paper, since it is a claimed contribution. Placing them in the appendix is not the right thing to do. Hence, I strongly suggest the authors to remove figures (like 2 and 4, they are not useful to understand the efficacy of the methods) and expand on the technical details of the attack.

**Debatable contribution of manipulations.** I debate that the nine attacks are novel, since they are all well-known noise patterns already present in the literature. Also, JPEG compression has been extensively used a lot (also on the defensive side). I would frame that the real contribution is how the authors attach those noise patterns in a differentiable way (see previous comment). Hence, 3.3 is not really novel per se to the extent of my knowledge.

**Unfair analysis.** The authors show that models are not robust to new manipulations. However, the authors should compare the efficacy of attacks at the same perturbation budget (same norm) and same number of queries to the models (i.e. forward and backward). Otherwise, in absence of those, attacks can be easily biased towards being effective or not. Also, why the authors did not use AutoAttack, similarly to RobustBench? Also, the authors do not provide their implementation of PGD, which might also contain bugs.

**Confusing presentation.** There is a digression on L$_2$ adversarial training which is not clear to me why is discussed. Also, L$_2$ is still an L$_p$ perturbation, and the authors might want to further investigate this by studying *why* they obtained their results. Still, I did not understand the connection in comparing different threat models in that portion of the paper.

### Questions
1. Can the authors specify the amount of perturbation injected, so that it is comparable with PGD?
2. Can the authors test AutoAttack, with the same level of noise used for their perturbations?
3. Can the authors better clarify the novelty of their approach, by revising the content and clearly specify how they produce differentiable attacks?

### Soundness
2

### Presentation
1

### Contribution
1
