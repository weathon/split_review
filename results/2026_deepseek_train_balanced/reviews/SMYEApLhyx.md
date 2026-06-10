## Summary

This paper investigates how ImageNet-trained CNNs organize visual information across positive and negative weights in their final fully-connected layer. Through ablation experiments combined with feature visualization, the authors demonstrate that positive weights encode object/foreground information while negative weights encode background/context. The central finding is supported by multiple lines of evidence: representational similarity comparisons across ablation conditions, YOLOv7-based objectness quantification, and an experiment showing that ReLU rectification is mechanistically necessary for this segregation. The paper also extends this analysis to linear models of primate ventral stream neurons (V1, V4, pIT), with in vivo electrophysiological validation that feature visualizations from these models drive actual neural responses.

---

## Strengths

- **YOLOv7-based quantification provides an external, automated validation of the core claim** (Section 4.1, Figure 5). Rather than relying solely on qualitative visual inspection or the same network's own representations, the paper uses an independent object detector to show that positive weight ablation systematically reduces object presence in feature visualizations across multiple architectures. This converts the central observation from an anecdotal pattern into a measurable, replicable effect.

- **The Tanh/ReLU experiment identifies a specific mechanistic cause (rectification) for the segregation** (Section 4.2). The paper trains a ResNet18 with Tanh activation and shows the segregation disappears, while a ReLU version of the same architecture retains it. This goes beyond describing the phenomenon to identifying a causal mechanism — something prior work on weight-strength segregation (Li et al., 2023) did not address.

- **Causal validation of ablation effects in real monkey neurons** (Section 4.4, Figure 10). Optimized images from positive-ablated neuron models elicit a consistent activity drop in the biological neurons being modeled. The models' preferred images activate neurons beyond the training set by over one standard deviation. This provides rare biological grounding for an in silico ablation analysis.

- **Systematic testing across multiple architectures and robustness levels** (AlexNet, VGG16, ResNet50, and five robust ResNet50 variants, Section 3 "Networks"). The multi-architecture sweep demonstrates the phenomenon generalizes beyond a single model family, and the robustness dimension reveals an interesting inverse relationship.

- **Gradient-free feature visualization (CMAES + GANs) enables apples-to-apples comparison with in vivo experiments**. The same closed-loop optimization approach is used for both artificial units and biological neuron models, ensuring differences are not artifacts of different visualization techniques.

- **Principled construction of diverseSet** for neurophysiology (Section 3 "Image dataset"): The 160-image stimulus set is constructed by embedding ImageNet into AlexNet's output space, performing PCA, then k-means clustering. This is a scalable and principled alternative to ad-hoc stimulus selection.

---

## Weaknesses

### Fatal
None.

### Major

- **The ablation procedure is potentially confounded by differences in weight magnitude concentration, not just weight sign.** The ablation (Section 3, "Ablation") sorts weights by absolute value within each polarity and ablates a fraction α of the total *sum* of positive (or negative) weight magnitude. If positive weights have a more concentrated (heavier-tailed) distribution than negative weights — which one would expect if the network concentrates "signal" into high-magnitude connections — then ablating the top α fraction of positive weights removes proportionally more influential connections than the same α fraction of negative weights, even if both polarities carry the same *kind* of information. The paper reports that the total *sum* of positive and negative weights is balanced (ratio ~1, line 52), but this does not rule out differences in distribution shape (kurtosis, Gini coefficient). The observed effect could partly reflect that positive weights are more concentrated in a few high-magnitude connections, not that they carry a different *category* of information (objects vs. backgrounds). An analysis of weight magnitude distributions per polarity and an ablation controlled for *number of weights ablated* (rather than fraction of total weight sum) is needed to distinguish these explanations.

- **The Tanh/ReLU comparison is confounded by different accuracy levels.** The ResNet18-Tanh network achieves top-5 accuracy of 0.797 vs. 0.870 for the ReLU version, trained for only 16 epochs (line 142). A network that has learned substantially poorer features could show different ablation behavior regardless of activation function. A proper control would match accuracy (e.g., by training the Tanh network longer or with different hyperparameters) or at least demonstrate that the Tanh network's lower accuracy does not explain the loss of segregation. Without this, the causal attribution to rectification is uncertain.

### Minor

- **The neuroscience evidence validates the *models*, not the *biological segregation hypothesis* directly.** The in vivo experiment (Figure 10, left) shows that images from positive-ablation neuron models elicit lower neural responses — but this only validates that the *models* capture something about the neurons. It does not test whether actual biological neurons segregate information by input sign. The paper acknowledges this ("our current experimental tools preclude a similar ablations as performed here in CNNs," line 211), but the abstract and discussion still give substantial weight to the biological connection. The neuroscience component is better characterized as a proof-of-concept that the model-based ablation framework transfers to neurophysiology, not as evidence for a biological segregation principle.

- **The robust networks finding (Section 4.3) is reported as an observation without mechanistic explanation.** The paper shows that adversarially robust networks exhibit *more* differential sensitivity to positive vs. negative ablation than standard networks. This counterintuitive result is described but not analyzed further — e.g., whether robust weights are more concentrated, or whether robust networks learn different types of features that drive the stronger segregation. This leaves an interesting finding underdeveloped.

- **No explicit statistical test is reported for the main representational similarity result.** Figure 4 shows 95% confidence intervals, and line 222 states "the positive ablation condition was statistically different to the control," but no test name, test statistic, or p-value is provided. A simple paired test across units at each ablation strength would substantially strengthen the claims.

- **The SimSiam (unsupervised pretraining) experiment has a confound.** The ResNet50 backbone is frozen and a fully-connected layer is *fine-tuned on classification* (line 142). The observed segregation could therefore emerge from the supervised fine-tuning, not from the unsupervised pretraining itself. The paper notes that features vanish under smaller ablation strengths in this case, partially mitigating the concern, but the confound is not explicitly addressed.

- **No non-CNN architectures tested (e.g., Vision Transformers).** Given that ViTs now dominate vision research, the claim about generality across "ANNs for vision" would be substantially strengthened by testing at least one transformer-based architecture.

- **Neuron models are built from only 160 training images with 4096 predictors (PLS regression), with a modest mean test r² of 0.274.** The sample is also dominated by pIT (41/59 neurons). The paper acknowledges these limitations, but the modest fit quality means the ablation results on neuron models should be interpreted with caution.

### Trivial
None.

---

## Nice-to-Haves

- Train the Tanh network to comparable accuracy to properly isolate the effect of rectification.
- Analyze weight magnitude distributions (Gini coefficient, kurtosis) for positive vs. negative weights per network, and re-run the ablation controlling for number of weights rather than fraction of total sum.
- Provide a mechanistic analysis of why robust networks show stronger segregation (e.g., do they concentrate object-relevant information into fewer, larger positive weights?).
- Test on at least one Vision Transformer to broaden the generality claim.
- Validate the diverseSet construction against random image sampling for neuron model fitting quality.

---

## Removed Points

Points that were raised by reviewers or the strength finder but removed after cross-checking against the paper:

- **Representational similarity metric concern** (Harsh Critic Critical Issue 5): The critic argued the ensemble-based metric is indirect and opaque. However, the paper explicitly confirms the results with LPIPS (line 35, 130), a different, non-ensemble perceptual metric. This concern is therefore addressed.
- **Neuron model sample dominated by pIT**: The paper explicitly states this (line 216: "our results are largely representative of the pIT cortex neurons"). Already self-acknowledged.
- **Missing statistical tests for the YOLOv7 analysis**: The paper shows 95% CIs, which is standard for this type of analysis.
- **"No discussion of whether results generalize to non-CNN architectures"** as a major issue: Downgraded to Minor — this is a reasonable scope limitation, not a flaw.
- **Strength Finder's claim about Tanh/ReLU experiment as unqualified strength**: The experiment is a genuine contribution, but it has a confound (accuracy mismatch) which is now noted in Major weaknesses. The strength stands but is qualified.
- **Various formatting, appendix, and reproducibility nitpicks** removed per filtering rules.

---

## Novel Insights

The two reviewer inputs largely echo the paper's own claims. The most novel synthesis from the review process is the recognition that the paper's core experimental paradigm — ablating by weight sign rather than weight magnitude — is surprisingly underexplored in the mechanistic interpretability literature (Li et al., 2023 focused on magnitude-based segregation). The paper's claim that ReLU rectification drives this sign-based segregation is the strongest mechanistic insight, but it is undercut by the accuracy confound in the Tanh experiment. The review process reveals that the single highest-impact improvement would be ruling out the weight-distribution confound, as this would determine whether the paper's central interpretation (information-type segregation by sign) is uniquely supported or partially explained by a simpler statistical asymmetry.

---

## Suggestions

1. **Address the weight distribution confound first.** Compute the Gini coefficient or Lorenz curves for positive vs. negative weights in each network. If distributions differ substantially, re-run the ablation controlling for the *number* of weights ablated rather than the *fraction of total sum*. If the effect holds under this control, it is much stronger. If it weakens or disappears, the interpretation needs revision.

2. **Match accuracy in the Tanh experiment.** Train the Tanh network for more epochs or with adjusted hyperparameters until its top-5 accuracy is within ~1% of the ReLU baseline. Only then can the loss of segregation be attributed to rectification rather than to poorer feature learning.

3. **Report explicit statistical tests (e.g., paired t-test or Wilcoxon) for the positive vs. negative ablation comparison at each ablation strength**, with effect sizes. The 95% CIs are helpful, but a formal test would strengthen the quantitative backbone.

4. **Clearly separate the two claims throughout the paper**: (a) CNNs segregate object/background by weight sign, and (b) this may have a biological parallel. The evidence for (a) is strong; the evidence for (b) is preliminary. The text could more sharply distinguish these.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>