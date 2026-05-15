Now I have all the evidence I need. Let me construct the consolidated review.

## Summary

This paper proposes Random Ensemble Defense (RED), an ensemble defense against adversarial examples that uses random sampling inference (RSI) at test time—selecting one sub-model at random rather than averaging all outputs—to simultaneously improve robustness and reduce inference latency. Two regularizers (gradient-similarity and Lipschitz) are introduced to diversify sub-models during training, and a parameter-saving variant (PS-RED) uses hypernetworks to compress the ensemble. Experiments on CIFAR-10 and TinyImageNet against a range of white-box and black-box attacks show large improvements over prior ensemble methods, with RED achieving 15%+ gains on PGD/BIM/MIM and PS-RED claiming ~90% parameter savings.

## Strengths

- **Conceptually interesting RSI design that addresses a real deployment tension.** The idea of randomly sampling one sub-model at inference instead of averaging all outputs is practically motivated: it cuts forward passes from N to 1, directly reducing latency, while the stochasticity creates a moving target for adversaries. This is a genuinely creative framing of the robustness-efficiency tradeoff that differs from prior ensemble defenses.

- **Broad evaluation across many attack types and two datasets.** The paper tests against white-box (PGD, BIM, MIM, DeepFool, AutoAttack, EoT-PGD, SparseFool) and black-box (OnePixel, Pixle, Square, DI2-FGSM) attacks on CIFAR-10 and TinyImageNet. For most settings, RED achieves best or second-best robust accuracy, and PS-RED is competitive. The inclusion of recent attacks like AutoAttack and EoT-PGD strengthens the breadth of the evidential base.

- **PS-RED's hypernetwork approach is a sensible way to address ensemble storage costs.** Using a shared hypernetwork with per-member embeddings to generate sub-model weights is a reasonable strategy for reducing parameter count, and the design details (parameter selection, output unification) are described clearly.

- **Demonstrated orthogonality with adversarial training.** Combining RED/PS-RED with standard adversarial training (Table 3) yields further gains, suggesting the proposed regularizers and RSI complement existing defenses rather than merely substituting for them.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated, but the next section contains a severe weakness that substantially undermines confidence in the key experimental results.

### Major

1. **Undefined threat model for the stochastic defense and likely evaluation artifact in white-box results.** The paper introduces a stochastic inference strategy (RSI) but never specifies how adversarial attacks are applied to it. Standard white-box attacks (PGD, BIM, AutoAttack) construct perturbations using gradient information from a *deterministic* classifier. When the defense is stochastic, the attacker must know *which* model will be sampled—but RSI samples randomly at test time. The paper does not clarify whether attacks were constructed against the full ensemble average, against a specific sub-model, or against the expected decision. The results in Table 1 show RED achieving 27.66% on AutoAttack vs. <2% for all baselines on CIFAR-10—a factor of 10+ improvement. The paper's own explanation (line 229) acknowledges that "AutoAttack overfits the current sub-model" and that the next sample may use a different member, which *confirms* that the attack was not properly adapted to the stochastic nature of the defense. This means the large white-box gains may be artifacts of evaluating a stochastic system with attacks designed for deterministic ones, rather than genuine robustness improvements. The black-box results (Table 2) are less affected by this issue and provide cleaner evidence, but the central white-box claims are compromised.

2. **Attack hyperparameters are not reported, making the main results unreproducible.** For all attacks in Table 1 (PGD, BIM, MIM, DeepFool, AutoAttack, FGSM), the paper does not state perturbation budget ε, step size, number of iterations, or any attack-specific parameters. For Table 2 attacks, the paper says (line 242) that "hyper-parameter configurations for all these attacks adhere to the default settings specified in the TorchAttacks package and are therefore not detailed here." Default package settings are not a substitute for explicit specification—they vary by package version and are not part of the scientific record. Without these details, the comparison to baselines cannot be independently verified or reproduced, and potential unfairness in attack strength cannot be ruled out.

3. **No ablation study disentangling the contributions of the three proposed components.** The method has three distinct components: (a) RSI, (b) gradient-similarity regularizer, and (c) Lipschitz regularizer. The only "ablation" in the paper varies the number of sub-models N (line 214). There is no experiment that trains RED without the Lipschitz regularizer, without the gradient-similarity regularizer, or without RSI (i.e., standard averaging). Without this, it is impossible to assess which component drives the observed gains and whether both regularizers are necessary. This is a standard expectation in robustness papers and its absence weakens the scientific contribution.

4. **The 90% parameter savings claim for PS-RED is stated without concrete evidence.** The abstract and introduction claim that PS-RED "saves parameters by approximately 90%," but the paper never reports actual parameter counts for RED versus PS-RED or versus any baseline. No table or figure shows the number of parameters for the ensemble, the hypernetwork, or the embeddings. The description of the hypernetwork design (Section 3.3.2) is detailed, but the claimed savings remain unverified. Similarly, the inference speedup from RSI is claimed but never measured (no latency numbers are reported).

### Minor

- **The Lipschitz regularizer derivation (Eqn. 8–11) is heuristic and the "constant" claim is technically informal.** The derivation drops the term -λₐ·(1/N)·ΣLᵢ on the grounds that Lᵢ is a "Lipschitz constant" that has no influence on optimization. While the resulting gradient-norm penalty is a widely used regularizer, the justification that Lᵢ is constant is imprecise—the true Lipschitz constant depends on model parameters and changes during training. This does not invalidate the method (the gradient penalty itself is reasonable), but the claimed theoretical grounding is overstated.

- **Lack of statistical rigor.** No confidence intervals, standard deviations, or error bars are reported for any experiment. While single-run evaluation is common in adversarial robustness benchmarks, the large claimed margins make it important to know whether results are stable across multiple training runs.

- **The gradient-similarity regularizer is very similar to GAL (Kariyappa & Qureshi, 2019) without a clear differentiation.** GAL minimizes cosine similarity of gradients between sub-models; the paper's R_sim minimizes absolute cosine similarity and additionally averages over clean and adversarial inputs (Eqn. 4). The paper cites GAL as a baseline but does not explain how its regularizer differs or what novel advantage it provides. The differentiation is too subtle to constitute a distinct contribution for this component alone.

### Trivial
- No runtime/latency measurements are provided despite the paper's claim of accelerated inference. A simple wall-clock comparison would substantiate this claimed advantage.
- Loss landscape visualizations (Figs. 1, 2) are only for 2 sub-models; the paper uses 8 sub-models in its main experiments. Extending these to more members would be more informative.

## Nice-to-Haves
- An adaptive white-box evaluation that properly accounts for RED's stochasticity (e.g., expectation-over-transformation attacks, or attacking the ensemble average after training and then evaluating RSI) would substantially strengthen the claims.
- Direct measurement of adversarial transferability between sub-models (e.g., pairwise attack success rates) would provide evidence that the regularizers actually reduce transferability as claimed.
- A comparison to gradient-norm regularization baselines (e.g., TRADES-style loss) would contextualize the Lipschitz regularizer's contribution.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's claim about missing related works (TRADES, gradient penalty):** Per instructions, missing related works should not be raised since we cannot verify the complete landscape.
- **"No theoretical or empirical link for Lipschitz regularizer"** — the paper does show loss landscape visualizations (Fig. 2) as empirical evidence, and the gradient-norm penalty is a standard technique; this claim overstates the absence of evidence.
- **Strength Finder's claim that "PS-RED reduces parameter storage by ~90% while retaining competitive robustness"** — this conflates the claimed saving with what is actually demonstrated; no parameter counts are provided, so the 90% figure is asserted but unsupported. Moved here because it conflicts with verified weakness #4.
- **Strength Finder's claim that "regularizers are theoretically motivated"** — the Lipschitz derivation is heuristic and the gradient-similarity regularizer closely resembles GAL; this strength conflicts with verified weaknesses about derivation rigor and novelty.
- **Harsh critic's note about "the paper does not formalize why random sampling is more robust than averaging"** — the paper does provide an informal reasoning (lines 63-73); the explanation is not a formal proof but it is present and reasonable for an empirical paper.

## Novel Insights

The most interesting observation that emerges across the reviews is the fundamental tension at the heart of this paper: RSI's robustness benefit derives precisely from the fact that the defender doesn't know which sub-model will be sampled—but standard white-box attacks assume full knowledge of the model. This creates a deep evaluation challenge that the paper does not confront. The very mechanism that makes RSI attractive (stochasticity breaking transferability) also makes it difficult to evaluate rigorously, because any white-box attack that treats the defense as deterministic will systematically underestimate its strength. Conversely, if the attacker can target the expected decision over many random draws, the stochastic advantage may evaporate. Resolving this requires either (a) a formal threat model specification, (b) adaptive attacks that account for the randomness, or (c) a clean separation of claims into settings where the threat model is well-defined (e.g., black-box, where RSI's advantage is clearer). This tension is not unique to this paper—it affects all stochastic defenses—but the paper's failure to address it head-on undermines what would otherwise be impressive-looking results.

## Suggestions

1. **Define the threat model precisely.** For each attack type, specify: what does the attacker know? Which model's gradients are used? How many queries are allowed? Then run white-box attacks that are properly adapted to the stochasticity (e.g., by attacking the expected loss over the random sampling distribution, or by using EoT with many samples).

2. **Report all attack parameters** (ε, steps, step size, loss function, random restarts) explicitly, either in the main text or in a table.

3. **Add an ablation study** that separately removes RSI (revert to averaging), the gradient-similarity regularizer, and the Lipschitz regularizer, reporting robust accuracy on at least PGD and AutoAttack.

4. **Report concrete parameter counts** for RED (N=8 ResNet-18s), PS-RED (hypernetwork + embeddings), and a single ResNet-18 to substantiate the 90% savings claim. Report wall-clock inference time per sample for RED (RSI) vs. standard averaging.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>