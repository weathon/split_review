- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 5, 1
Now I have all the information needed. Let me produce the consolidated review.

## Summary
This paper proposes CARSO, a defense that blends adversarial training and purification by training a conditional VAE to reconstruct clean images conditioned on the internal representations of an adversarially-trained classifier. At inference, multiple decoded samples are classified and their logits aggregated via a double-exponential product. The method achieves state-of-the-art robust accuracy on CIFAR-10 (76.13% randAA), CIFAR-100 (66.65%), and TinyImageNet-200 (53.56%) under $\ell_\infty$ AutoAttack, with a careful evaluation using randAA with EoT iterations and a high-$\epsilon$ gradient obfuscation sanity check.

## Strengths
- **Novel and principled architectural design.** Conditioning the VAE purifier on the classifier's internal representations (rather than the perturbed input directly) is a genuine architectural innovation. The hierarchical disjoint encoding of input and internal representation (Section 3.3, Appendix Tables A2–A4) allows the method to scale to different classifier depths while maintaining gradient transparency. This addresses a known vulnerability of stacked purifier-classifier pipelines (Gu2015).
- **State-of-the-art robust accuracy across three datasets.** On CIFAR-10, CARSO (76.13% randAA) outperforms the best AT model (71.07%) and the best purification model under corrected evaluation (66.41% Pgd+EoT). On CIFAR-100, CARSO (66.65%) surpasses both best AT (42.67%) and best purification (46.09%). On TinyImageNet-200, CARSO (53.56%) nearly doubles the best AT baseline (31.30%). These results are reported in Table 1 with consistent evaluation methodology.
- **Rigor in ruling out gradient obfuscation.** The paper tests at $\epsilon_\infty = 0.95$ and verifies accuracy falls below random chance (Table 2), following Athalye et al.'s diagnostic. This is a standard that many purification papers neglect, and it strengthens confidence in the reported numbers.
- **Detailed and reproducible specification.** The paper provides complete architecture tables (encoder, layerwise encoder, joint encoder, decoder for all scenarios), hyperparameter tables (learning rate schedules, $\beta$ annealing, attack parameters, batch fractions), and training protocol rationale in the appendix. This level of detail enables independent reproduction.

## Weaknesses

### Fatal
None.

### Major
- **Only one classifier architecture tested; generality claims are unsupported.** Every experiment uses a WideResNet-28-10 as the classifier. The layer extraction tables list specific WideResNet layer names (Appendix Table A1), and the layerwise encoder dimensions were tuned for this model's channel counts. The method may succeed only on architectures whose internal representations have properties matching WideResNet (e.g., spatial structure, layer count, channel depth). The paper states there are "no specific requirements for the classifier" (Section 4.1), but this claim is not backed by any experiment on a different backbone (e.g., ResNet-50, PreactResNet-18, or a ViT). Without at least one cross-architecture experiment, the generality of CARSO remains a conjecture, significantly limiting the paper's contribution.
- **The anomalously large gain on CIFAR-100 is unexplained.** The robust accuracy jumps from 39.18% (base classifier) to 66.65% — an absolute gain of +27.47%, roughly three times the CIFAR-10 gain (+8.4%) and comparable to the TinyImageNet gain (+22.26%). The base CIFAR-100 classifier is much weaker than the CIFAR-10 one (39.18% vs. 67.73% AA), which could explain the larger headroom, but the paper offers no analysis. The training hyperparameters also differ substantially (CIFAR-100 uses 0.15 adversarial batch fraction vs. 0.5 for CIFAR-10). The result may be genuine, but the paper should provide diagnostic evidence — e.g., VAE reconstruction error on clean vs. adversarial representations, per-class analysis, or an experiment starting from a stronger CIFAR-100 base (Wang2023's 42.67%) to show the gain is not an artifact of the specific weak base model used.

### Minor
- **The robust aggregation strategy lacks empirical validation.** The paper proposes a double-exponential product aggregation (Section 3.5) and provides a heuristic analytical comparison with logit averaging and probability averaging (Appendix C). However, there is no experiment comparing these alternatives within the CARSO framework. Given that the aggregation is a distinctive design element, the absence of an ablation study leaves the reader unsure whether simpler alternatives would perform similarly or better. The claim that this aggregation "produces a robust prediction much harder to take over" is thus unsubstantiated by evidence.

### Trivial
- **The table column header "C/rand-AA (Pgd+EoT)" is slightly ambiguous.** For CIFAR-100 and TinyImageNet only one number is shown, while for CIFAR-10 two numbers appear (randAA and Pgd+EoT in parentheses). The caption clarifies this, but a cleaner presentation would separate the two metrics into distinct columns or rows.

## Nice-to-Haves
- **Comparison against a simple ensemble baseline.** While not standard practice, comparing CARSO to an ensemble of multiple randomly-seeded adversarially-trained WideResNets would help disentangle whether the gains come from the purification mechanism itself or simply from the ensembling effect of multiple forward passes.
- **Inference time overhead reporting.** The paper reports training times (Table 3) but not inference latency. Since CARSO requires 8 forward passes per input (plus VAE decoding), the per-sample cost is relevant for practical deployment.

## Removed Points
- *"Suspicious CIFAR-100 result may indicate evaluation bias"* — The critic speculated that the large CIFAR-100 gain could stem from "evaluation protocol bias." This is speculative; the evaluation methodology (randAA with 20 EoT iterations) is identical across all datasets. The large gain is an unexplained finding meriting analysis, not evidence of a biased protocol. Kept as a Major weakness but stripped of the evaluation-bias framing.
- *"Reproducibility: code availability not mentioned"* — The paper provides exhaustive architectural and hyperparameter details. Asking for code release is reasonable but does not constitute a weakness in the paper's technical content. Moved here as it is a wish rather than a flaw.
- *"Missing statistical significance / confidence intervals"* — Single-run evaluation with strong attacks (randAA) is the standard in this field. Not a missing element.
- *"Comparison with Best P/AA is muddled"* — The paper already clearly explains the overestimation issue with diffusion-based purification, provides corrected numbers where available, and compares against the worst-case evaluation. No unresolved issue.

## Novel Insights
The Harsh Critic's first-principles lens correctly identified that conditioning on internal representations (rather than input-space perturbations) is the key architectural insight — but also that this ties the method's success to properties of the specific backbone's representational structure. The Strength Finder usefully flagged the adversarially-balanced batch protocol (mixture of FGSM and PGD at $\epsilon/2$ and $\epsilon$) as a non-obvious design choice that the appendix justifies empirically. Neither reviewer picked up on the interesting pattern in the training hyperparameters: the adversarial batch fraction drops dramatically from 0.5 (CIFAR-10) to 0.15 (CIFAR-100) to 0.01 (TinyImageNet), suggesting that the optimal exposure to adversarial examples during purifier training scales inversely with dataset complexity — which may itself be a publishable finding.

## Suggestions
1. **Test on at least one other classifier architecture** (e.g., a PreactResNet-18 or ResNet-50 on CIFAR-10) to substantiate the claim of architecture independence.
2. **Ablate the aggregation strategy** by comparing double-exponential product against logit averaging and probability averaging within CARSO on CIFAR-10, reporting both clean and robust accuracy.
3. **Analyze why CIFAR-100 gains are disproportionately large** — e.g., by measuring VAE reconstruction fidelity for clean vs. adversarial representations, or by running CARSO atop a stronger CIFAR-100 base model and reporting whether the absolute gain level, the relative gain level, or both transfer.
