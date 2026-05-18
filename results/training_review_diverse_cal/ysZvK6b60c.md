Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper proposes CALoR, a defense against Model Inversion Attacks (MIAs) that jointly targets three weaknesses in the attack pipeline: (1) **attack objective mismatch** via a confidence adaptation loss that reduces prediction confidence away from one-hot targets, (2) **MI overfitting** via low-rank compression of the classification head that reduces leaked information, and (3) **optimization difficulty** via Tanh activation that induces gradient vanishing. The method is evaluated across multiple datasets (FaceScrub, CelebA), architectures (IR-152, ResNet-152, ViT-B/16, Swin-v2, MaxViT), and attack methods (IF, PLG, and others), showing substantial improvements over prior defenses — notably achieving 38.4% and 52.0% reductions in IF and PLG attack accuracy respectively on high-accuracy target models where prior defenses struggle.

## Strengths

- **Strong empirical defense in the most challenging regime.** On high-accuracy target models (>96% test accuracy, pre-trained on MS-Celeb-1M), CALoR reduces IF and PLG attack accuracy by 38.4% and 52.0% respectively, while prior defenses like LS and TL provide minimal protection (Table 2, Section 4.2). This is the single most compelling evidence for the paper's contribution — defending against strong MIAs when the target model itself performs well is a realistic and underexplored setting.

- **Well-structured defense motivated by three distinct attack weaknesses.** Rather than a single ad-hoc defense, CALoR identifies three separate vulnerabilities in the attack pipeline and designs a component to address each one. The ablation studies validate each component independently: confidence adaptation alone reduces IF attack accuracy by 3–4% (Table 4, Section 4.3), low-rank compression at rank 30 drops attack accuracy to 13.0% (Table 5), and Tanh achieves the best utility-defense balance among activation functions (Table 6).

- **Broad experimental scope across architectures, datasets, and attacks.** The evaluation spans convolutional (IR-152, ResNet-152, FaceNet-112) and transformer backbones (ViT-B/16, Swin-v2, MaxViT), two private datasets (FaceScrub, CelebA), low- and high-resolution settings, and up to seven attack methods (GMI, KED, Mirror, PPA, LOMMA, PLG, IF). The low-rank ablation on FaceScrub with rank from 10 to 530 provides clear evidence that compression improves privacy with minimal utility loss.

- **Ablation study for the rank component is well-designed.** The paper isolates the low-rank head's effect by excluding the confidence adaptation loss, varying rank from 10 to 530, and showing that rank 30 preserves classification accuracy while reducing attack accuracy to 13.0%. This provides clean causal evidence for the component's effectiveness.

## Weaknesses

### Fatal

None. The paper's core claims are supported by the experiments, and no methodological error invalidates the results.

### Major

- **Overclaimed novelty of the "first comprehensive analysis."** The paper asserts it is "the first to conduct comprehensive analyses of weaknesses inherent in MIAs" (line 29) and that "no existing defense mechanisms have effectively exploited" the attack objective mismatch (line 93). In reality, each weakness is individually known: MI overfitting is studied in LOMMA (which the paper cites), gradient vanishing is discussed in PPA (which the paper cites), and the mismatch with one-hot targets is the motivation behind label smoothing defenses. The novelty is in *combining* countermeasures to all three weaknesses into one framework — a legitimate engineering contribution — but the rhetoric sets an expectation of deeper theoretical insight than is delivered. This framing inflates the paper's conceptual contribution and forces the defense to carry the full weight of novelty on its empirical strength.

- **Insufficient evidence that Tanh-based gradient vanishing is robust to attack adaptation.** The paper shows that Tanh causes gradient magnitudes to drop faster than other activations during IF attacks (Figure 3), but a resourceful white-box attacker can compensate with gradient clipping, increased iterations, different learning rates, or second-order optimization. The paper does not test whether the defense holds under such adaptive attacks. If an attacker can simply use Adam with per-parameter learning rates or double the optimization steps to overcome the vanishing gradient, then this component provides only a minor nuisance rather than a genuine barrier. Without adaptation experiments, the security claim for this component is incomplete.

- **The accuracy-matching comparison strategy may obscure differential trade-offs.** The paper adjusts baselines to "maintain nearly identical classification accuracy on the test set" (line 177), which is a common practice. However, if a baseline like LS has a fundamentally different accuracy-robustness Pareto frontier, forcing it to match CALoR's test accuracy may understate its potential robustness at a different operating point. The paper should show the accuracy-robustness trade-off curve across hyperparameter sweeps for at least one model/attack pair to demonstrate that CALoR dominates baselines rather than merely being better at a single matched point.

### Minor

- **Only IF and PLG attacks appear in the main comparison tables.** The paper lists seven attack methods (line 163) but the primary quantitative results (Tables 1 and 2) only report IF and PLG. Other attacks are mentioned as "further comparative studies" (line 198) that are presumably in the appendix. Given the claim of comprehensive defense, at least a summary table covering all attack types should appear in the main body.

- **Hyperparameter values a and b for the confidence adaptation loss are not reported.** The paper defines $\mathcal{L}_{CA} = a \hat{y}^b_c \log \hat{y}_c$ (Equation 4) and states that $a>0, b>0$ are hyperparameters, but never discloses the specific values used in experiments or how they were chosen. Since the loss behavior is sensitive to these parameters, this is a meaningful omission for reproducibility.

- **Two-stage training (CE then CA fine-tuning) is stated but not justified.** The paper first trains with cross-entropy, then fine-tunes with the confidence adaptation loss. It does not explain why joint training (weighted CE + CA from scratch) was not used, or whether the two-stage approach is necessary to avoid utility degradation.

- **The connection between low-rank compression and MI overfitting is intuitively plausible but not formally argued.** The paper states that compression "strengthens MI overfitting" by making adversarial reconstructions more likely, but does not directly measure whether low-rank heads increase the rate at which reconstructed samples fall into the "inversion space" outside the "success space" (as defined in Figure 1). The empirical rank ablation supports the correlation but does not validate the specific mechanistic claim.

### Trivial

- The stray closing brace "}" at line 136 after $\exp(-1/b) < 1$ is a parser artifact; the original paper presumably formats this correctly.

## Nice-to-Haves

- **Attack adaptation study for Tanh.** Run IF/PLG attacks with increased iterations, adjusted learning rates, and gradient clipping to verify whether the gradient vanishing defense remains effective. If it does, the story is strengthened; if not, acknowledge the limitation.
- **Accuracy-robustness Pareto frontier** for at least one model/attack pair across a sweep of defense hyperparameters for CALoR and baselines (e.g., varying CA loss weight $a$, rank, Tanh vs identity).
- **Comparison to standard label smoothing (positive factor)** at matched accuracy to clarify whether confidence adaptation offers an advantage over a simpler alternative.
- **Computational overhead reporting.** The low-rank head changes the architecture; reporting training/inference time relative to standard classifiers would be useful.
- **Guidance on rank selection.** The rank ablation uses FaceScrub (530 classes). For CelebA (1000 classes), the required rank may differ — the paper should discuss how to choose rank more generally.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The description of the LS baseline is unclear (negative factor)"** — Removed. The paper accurately cites the LS paper, which indeed proposes label smoothing with a negative factor. This is a correct description of prior work, not a mistake by the current authors.
2. **"Visualization images not visible in review text"** — Removed. This is a PDF parser/extraction artifact, not an author error.
3. **"Stray closing brace in Equation 4"** — Removed. This is a parser extraction artifact; the original submission does not have this issue.
4. **"The paper should cover more tasks/domains outside face recognition"** — Not raised explicitly, but any such demand would be scope creep. The paper focuses on face recognition following the standard MIA evaluation protocol, which is a defensible and focused scope.
5. **Weaknesses about missing appendix content** — Removed per hard rules; the parser strips appendix content.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses converge on the same observations: the defense is empirically strong, the individual components are known techniques, and the main gap is the lack of adaptive attack testing against the gradient-vanishing component.

## Suggestions

- Tone down the novelty claims in the introduction (e.g., "first comprehensive analysis") to more accurately reflect that the paper synthesizes known vulnerabilities into a joint defense framework.
- Add an adaptive attack experiment where the attacker adjusts optimizer settings to counteract gradient vanishing, with honest reporting of results.
- Report hyperparameter values $a$ and $b$ for the confidence adaptation loss, and describe how they were selected (e.g., grid search range).
- Include at least one accuracy-robustness Pareto sweep comparing CALoR against the best baseline to demonstrate dominance rather than a single-point advantage.
- Move a summary of defense results against all seven listed attack methods into the main paper.

## Score and Decision

**Originality:** The analysis framework is a re-synthesis of known observations; the defense combines known techniques (confidence reduction, bottleneck compression, activation choice). The combination is novel in the MIA defense context, but individual components are not new. **Importance:** High — defending against strong MIAs on realistic high-accuracy models is a practically important problem. **Claims support:** The core empirical claim (SOTA defense) is well-supported by the experiments. The analytical novelty claim is overstated. **Soundness:** The experimental methodology is generally sound, with the main gap being the lack of adaptive attack testing for the Tanh component and the single-point comparison strategy. **Clarity:** The paper is clearly written and well-structured. **Value:** The defense is practically useful and outperforms prior work in a challenging regime; this represents a meaningful step forward for MIA defense.

The paper's main weakness is that its claimed novelty of the analysis is inflated, its strongest component (low-rank compression + confidence adaptation) is empirically well-validated, but the gradient-vanishing component lacks adaptive-adversary testing. The issues are addressable in a revision. The strong empirical results in the high-accuracy regime justify publication.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>