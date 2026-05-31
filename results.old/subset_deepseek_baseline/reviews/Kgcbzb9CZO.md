## Summary

The paper proposes Distributional Input Projection Networks (DIPNet), a framework that projects inputs into learnable Gaussian distributions at each layer of a neural network. The method is motivated by variational inference and includes a stability penalty on output variance. Theoretical analysis claims that DIPNet reduces Lipschitz constants and smoothness measures. Experiments on Vision Transformers (CIFAR-100 under adversarial attacks) and LLMs (GSM8K reasoning) show modest accuracy improvements over several baselines.

## Strengths

- The idea of injecting learnable noise at every layer (rather than only at the input) is a natural extension of existing smoothing approaches and is applied consistently during both training and inference.
- The empirical evaluation spans multiple architectures (ViT-Tiny/Small/Base, six LLMs up to 12B parameters) and two distinct tasks (image classification under attacks, mathematical reasoning), demonstrating broad applicability.
- The paper attempts to provide theoretical grounding for why smoothing via distributional projection can reduce Lipschitz constants and smoothness.

## Weaknesses

### Major

1. **Theoretical analysis is generic and not specific to DIPNet.** Theorems 1–3 analyze the effect of convolving a function with a distribution (i.e., standard smoothing). They do not address the layerwise, learnable-variance structure of DIPNet, nor do they guarantee that the *learned* distributions achieve the claimed bounds (the infimum over all distributions is taken, but DIPNet learns a particular one). The connection between these theorems and the actual algorithm is weak.

2. **Empirical gains are modest and not always consistent.** In Table 1, DIPNet is often best or second-best, but the margins are small (e.g., ViT-Base Gaussian: 69.23 vs. Standard 69.13; ViT-Base FGSM: 74.20 vs. RS 77.30). The LLM results (Table 2) show improvements of 1–2 percentage points, which may not be practically significant. No error bars or statistical significance tests are reported, making it hard to assess reliability.

3. **Comparison with baselines is not apples-to-apples.** DIPNet modifies the model architecture (adds distributional projection layers), while baselines like SAM, RS, Mixup, etc., are training-time techniques that do not change the architecture. The paper claims DIPNet can be “seamlessly integrated,” but it actually changes the forward pass. A fairer comparison would include methods that also add stochasticity at each layer (e.g., Dropout, Variational Dropout, or Bayesian neural networks).

4. **The “model distillation” inference (Algorithm 3) is simply removing the noise at test time.** This is a standard practice (e.g., using dropout only during training) and is not a novel distillation technique. The paper presents it as a contribution, but it is essentially the same as using the deterministic version of the trained model.

5. **The stability penalty (λ term) appears unnecessary in the main experiments.** Table 3 shows that λ=0 achieves the best accuracy for ViT-Tiny under Gaussian attack. The paper mentions that λ>0 helps when training from scratch, but the main experiments use pretrained models. This undermines the motivation for the stability penalty and suggests the method’s success may come primarily from the noise injection itself, not from the full variational objective.

### Minor

- The derivation of the loss function from variational inference is unclear. The ELBO bound is presented, but the transition to the final loss (Eq. 2) with hyperparameters α and β is not fully justified. The remark that the penalty prevents λ_j from shrinking to zero is heuristic.
- The paper claims improvements in OOD generalization and adversarial robustness, but the OOD experiments are only in the appendix (which is stripped). The main paper only shows results under Gaussian and FGSM attacks during training, which is a limited evaluation of robustness.
- The ablation on hyperparameters (Table 3) only covers ViT-Tiny under Gaussian attack; sensitivity for other settings (LLMs, clean training) is not explored.

### Trivial

- Figure 2 is difficult to read due to small font and overlapping lines.
- The paper uses “uning” instead of “tuning” in the text (likely a parser artifact, but noted).

## Nice-to-Haves

- Compare DIPNet with layerwise stochastic methods such as Dropout, Variational Dropout, or Bayesian neural networks to better isolate the effect of learnable Gaussian noise.
- Report error bars or confidence intervals for all main results.
- Provide a more direct theoretical analysis that connects the layerwise distributional projection to the final Lipschitz constant of the full network, rather than a single convolution.

## Novel Insights

None beyond the paper’s own contributions. The idea of adding learnable noise at each layer is a straightforward extension of input-level smoothing, and the theoretical results are standard properties of convolution.

## Suggestions

- Clarify the relationship between the variational inference derivation and the final loss; explain how α and β are chosen in practice.
- Include a comparison with Dropout or other layerwise stochastic regularizers to demonstrate the advantage of learnable Gaussian noise.
- Report results with error bars and statistical significance tests.
- If the stability penalty (λ) is not beneficial in most settings, consider removing it or repositioning it as optional.

## Score and Decision

Score: 4

Decision: Reject

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>