Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies the connection between memorization and poor generalization for minority groups under spurious correlations. The authors first show, via a neuron-flipping analysis on an ERM-trained ResNet-50, that minority-group examples require fewer critical neurons to flip their predictions and that dropping those neurons improves worst-group accuracy (Section 3.2). They then propose FairDropout, an example-tied dropout method that designates a subset of neurons as "memorizing," randomly allocates them to training examples, and drops them at inference. Experiments across five datasets (CelebA, Waterbirds, MetaShift, MultiNLI, MIMIC-CXR) show that FairDropout improves worst-group accuracy over ERM and is competitive with or exceeds several existing methods that require group annotations.

## Strengths

- **Novel diagnostic analysis connecting minority-group overfitting to localized memorization in the spurious-correlation setting.** Figure 2 provides an empirical demonstration that minority-group examples (blond men on CelebA) require substantially fewer neurons to flip their predictions than majority-group examples, and that those neurons have less effect on training worst-group accuracy. Figure 3 further shows that dropping these neurons improves test worst-group accuracy for ~75% of minority examples. This diagnostic contribution is clear and well-executed, and it opens a new empirical perspective on why minority groups underperform under ERM — one that prior spurious-correlation work has not investigated in this form.

- **Empirical gains across diverse tasks without requiring group annotations.** FairDropout achieves competitive worst-group accuracy on five datasets spanning image classification (CelebA, Waterbirds, MetaShift), natural language inference (MultiNLI), and medical imaging (MIMIC-CXR) — all without group labels during training or validation. On MultiNLI (70.3±2.4) and MIMIC-CXR (70.6±0.6), the method achieves the highest reported numbers among comparable methods. This is a practically meaningful achievement since group annotations are often unavailable in real-world deployments.

- **Scaling of example-tied dropout to larger architectures.** Maini et al. (2023) originally demonstrated example-tied dropout only on small networks (ResNet-9) on small datasets (MNIST, CIFAR-10). This paper adapts the technique to ResNet-50 and BERT, showing that the core idea can be applied at a practically relevant scale.

## Weaknesses

### Major

- **The connection between the diagnostic analysis and the proposed method is asserted but not validated.** The analysis in Section 3.2 identifies *example-specific* critical neurons via an iterative optimization procedure. FairDropout, however, randomly allocates a *fixed* set of memorizing neurons to examples via hyperparameters p_gen and p_mem, with no mechanism that connects the neurons identified by the analysis to those designated as memorizing. The paper hypothesizes (line 197–199) that training will naturally concentrate memorization into the designated neurons, but provides no evidence for this claim. This is not fatal — the empirical results stand on their own — but it means the paper's central explanatory narrative (that FairDropout works *because* it redirects spurious-feature memorization to known neurons) is unsupported. The method could plausibly work through generic regularization (capacity reduction, training noise). The paper would be significantly strengthened by either (a) repeating the neuron-flipping analysis on FairDropout-trained models to check whether critical neurons are concentrated in the memorizing set, or (b) tempering the mechanistic claims and positioning the method more modestly as an "example-tied dropout variant inspired by the analysis."

### Minor

- **No comparison to standard dropout as a control experiment.** FairDropout has two components (example-tied training masks + dropping memorizing neurons at inference). An immediate baseline is training with standard dropout and applying it at inference at the same total drop rate. If standard dropout achieves comparable worst-group accuracy, the example-tied allocation is unnecessary. If it does not, the paper's case is much stronger. This experiment is missing from the evaluation. (Standard dropout is not a standard baseline in the spurious-correlation literature, which makes the omission understandable but still a gap in isolating the claimed mechanism.)

- **Insufficient hyperparameter analysis.** The method is governed by two hyperparameters (p_gen and p_mem) that control the allocation of generalizing vs. memorizing neurons. The paper reports only a single tuned setting (p_gen = p_mem = 0.2 for CelebA) and states that hyperparameters are tuned via worst-class accuracy. No ablation or sensitivity analysis is provided for any dataset. Without this, readers cannot assess whether the method is robust across settings or fragile. The relationship between p_mem and the stated "each image allocates only one memorizing neuron" is also ambiguous — the text says both that *each sample is allocated a memorizing neuron uniformly with probability p_mem* and that *each image allocates only one memorizing neuron*, without clarifying whether p_mem controls the *number* of allocated neurons or the *probability* of allocating the single neuron.

- **Implementation details for convolutional layers are incomplete.** The paper states that neurons correspond to "channels for the case of convolutional layers" (line 87), and that FairDropout is placed "after the third residual block" on ResNet-50 (line 123), where features have shape [batch, C, H, W]. However, the paper does not specify how the example-tied dropout mask is generated and applied per-example in batch processing for such spatial feature maps. For BERT (where a linear projection layer is added before the classifier head), the mechanism is standard and clear; for ResNet-50, the exact masking procedure needs specification for reproducibility. The paper also does not discuss the memory or computational overhead of storing per-example masks.

### Trivial

- The description of how p_mem interacts with the "one memorizing neuron per example" design is ambiguous and should be clarified.

## Nice-to-Haves

- A post-hoc analysis on FairDropout-trained models using the same neuron-flipping technique from Section 3.2 to verify whether memorization is indeed concentrated in the designated memorizing set.
- A combined experiment showing FairDropout + DFR (classifier retraining), which the paper suggests as a possibility but does not evaluate.
- Reporting the effective total dropout rate at both training and test time to help practitioners understand the method's behavior.

## Removed Points

- **Criticism about the "first time" claim being overstated with reference to Feldman (2020):** Removed. The paper's claim is specifically about studying the memorization-generalization link *in the context of spurious correlation* and scaling example-tied dropout to larger architectures. Feldman (2020) discusses memorization in long-tail/subpopulation settings, not specifically spurious correlations. The paper's scope claim is defensible.
- **Criticism that the Section 3.2 analysis "does not require FairDropout — it could be a post-hoc regularizer":** Removed. The paper's stated contribution includes the analysis itself as a separate finding (contribution i). Noting that a different method could also exploit this observation is not a weakness of the paper.
- **Criticism about FairDropout underperforming DFR on MIMIC-CXR:** Removed because the table is an image and the paper's text does not claim to outperform all methods on all datasets. The paper acknowledges that FairDropout can be combined with DFR, and DFR requires group information for validation (which FairDropout does not). The comparison context is adequately stated.
- **Criticism about hypothetical gains being "entirely due to increased stochasticity":** Weakened and moved to Minor (the missing standard dropout control). The original phrasing exaggerated the severity of an unverified claim.

## Novel Insights

The key insight that emerges from reading the harsh critic alongside the paper's analysis is this: the paper's strongest contribution may not be FairDropout itself, but rather the diagnostic finding that minority-group examples rely on a *concentrated* set of critical neurons while majority examples distribute their reliance more broadly. This asymmetry has implications beyond the proposed method — it suggests that any technique that selectively perturbs or regularizes the most influential neurons (e.g., via neuron-level pruning, targeted noise injection, or adversarial neuron removal) could disproportionately benefit minority groups. The paper could have leaned harder on this diagnostic contribution as an independent finding, rather than tying it so tightly to a specific mitigation method whose mechanism remains unvalidated.

## Suggestions

1. **Validate the mechanism**: Either repeat the neuron-flipping analysis on FairDropout-trained models to show that critical minority-group neurons concentrate in the memorizing set, or temper the paper's causal claims.
2. **Add a standard dropout control**: Train with standard dropout and evaluate at inference to separate the effect of the example-tied mechanism from generic regularization.
3. **Provide hyperparameter sensitivity plots**: Show worst-group accuracy as a function of p_gen and p_mem for at least CelebA or MultiNLI.
4. **Clarify the masking procedure**: Specify the exact per-example mask generation algorithm for the convolutional case (ResNet-50) with pseudocode or a precise mathematical description.
5. **Resolve the p_mem ambiguity**: Clearly state whether each example gets exactly one memorizing neuron or a random number controlled by p_mem.

## Score and Decision

**Originality**: The analysis linking minority-group overfitting to localized memorization is genuinely novel in the spurious-correlation setting. The method itself is an adaptation of existing work (Maini et al., 2023) to a new problem domain.

**Importance of the research question**: Yes — reducing reliance on spurious correlations without group annotations is practically important.

**Claims supported**: The core empirical claims (contributions i and iii) are supported. The mechanistic claim (that FairDropout works by redirecting memorization) is not.

**Soundness of experiments**: The evaluation is broad (5 datasets across modalities) and uses established benchmarks. Missing controls (standard dropout) and ablations weaken the evidence somewhat.

**Clarity**: The paper is generally clear but has ambiguities in the method description (p_mem, convolutional masking).

**Value to the community**: The analysis in Section 3.2 is a useful diagnostic tool. FairDropout itself is a simple method that could be adopted or built upon, but the mechanism gap limits its scientific contribution.

Overall, this is a borderline paper with a genuinely interesting diagnostic finding and a method that shows empirical promise but whose claimed mechanism is unvalidated. The paper is not fatally flawed — the empirical results are real — but the gap between analysis and method, missing controls, and insufficient ablations prevent a strong accept.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>