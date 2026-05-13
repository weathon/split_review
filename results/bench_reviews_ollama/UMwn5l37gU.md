Now I have a thorough understanding of the paper. Let me verify specific claims by the harsh critic against the actual paper text.

## Summary

This paper proposes a non-uniform noise injection method for DNNs that selectively preserves "essential" neurons while replacing non-essential neurons with learned approximate values ($\tilde{z}$), aiming to simultaneously enhance adversarial robustness and execution efficiency. The approach uses a random-projection-based approximation to cheaply identify essential neurons, then applies a binary mask keeping essential neurons intact and filling non-essential ones with approximations. A structured N:M variant is proposed for hardware efficiency, and the method is evaluated across ResNet18/50 on CIFAR-10 and ImageNet-2012 against five adversarial attacks.

## Strengths

- **Orthogonal combination with adversarial training**: Table 3 demonstrates that combining the method with FGSM-RS and PGD-10 adversarial training yields 1.89–3.19% additional robust accuracy improvements over adversarial training baselines alone, confirming the method's compatibility with established defenses.

- **Consistent empirical improvements across architectures and datasets**: Tables 1–2 show that the structured 4:8 pattern achieves up to ~12.88% robustness improvement on ResNet50/ImageNet (DeepFool) while maintaining clean accuracy drops ≤1%, with consistent trends across ResNet18/50, CIFAR-10, and ImageNet-2012.

- **Practical structured N:M pattern design**: The structured noise injection pattern (Section 3.5, Figure 3) aligns with existing hardware sparsity support (e.g., NVIDIA Ampere 2:4 sparsity), making the approach potentially deployable rather than purely theoretical.

- **The method's core intuition is reasonable**: The hypothesis that only a subset of neurons are essential for clean accuracy while others can tolerate perturbation draws on established insights from pruning literature, and the empirical results largely validate this.

## Weaknesses

### Fatal
None.

### Major

- **The central claim of superiority over uniform noise injection lacks experimental support**. The paper's title, abstract, and contribution bullet 1 all claim "non-uniform noise injection is better than uniform one," yet no uniform noise injection baseline (e.g., adding Gaussian noise to all activations uniformly) is tested. The experiments only compare variants of the proposed method (Irregular 50–90%, Structured 2:4/4:8) against the undefended original model. While Figure 1's motivation and Irregular 80%/90% results (closer to uniform) are suggestive, they do not constitute a direct comparison with a standard uniform noise injection baseline. This is a significant gap in the evidence for the paper's primary claim.

- **The theoretical justification for robustness (Section 3.4) does not support the method as described**. The paper invokes Theorem 2 from Pinot et al. (2019), which concerns noise sampled from an exponential family distribution—i.e., *random* noise. The proposed method replaces non-essential neuron activations with $\tilde{z}$, a *deterministic* learned function of the input. This is not stochastic noise; it is a conditioned approximation. The paper provides no theoretical bridge explaining why deterministic value substitution should yield the entropy-based robustness bounds that Pinot et al.'s theorem guarantees for random noise. The "motivation" from this theorem is therefore misleading as stated.

- **No threat model specification and no evaluation against adaptive attacks**. The paper evaluates against five standard attacks (FGSM, PGD, BIM, CW, DeepFool) but never specifies whether these are white-box or black-box, or whether the attacker has knowledge of the defense mechanism. This is critical because the defense operates at inference time as a preprocessing/modification step—which prior work (Athalye et al., 2018) has shown to be vulnerable to gradient obfuscation/masking. Without adaptive attack evaluation where the attacker accounts for the noise injection mechanism, the robust accuracy numbers cannot be interpreted as genuinely demonstrating adversarial robustness.

### Minor

- **Gap in the clean accuracy preservation argument**: Section 3.3 uses the Johnson-Lindenstrauss Lemma to show that inner products are approximately preserved under random projection. However, the method selects essential neurons via Top-K or thresholding on $\tilde{z}$, which requires correct *ordinal ordering* of neuron activations—not just approximate inner product preservation. Two neurons with nearly equal true magnitudes can have their relative order flipped by the approximation, potentially causing the binary mask $m$ to misidentify essential neurons. While the empirical results show that clean accuracy is largely preserved, this gap between theoretical guarantee and algorithmic requirement remains unaddressed, and the paper should not claim Section 3.3 formally proves "no loss in clean accuracy."

- **Efficiency claims are preliminary**: Section 4.3 relies on BitOps from an unvalidated simulator without real-hardware measurements, standard FLOPs comparisons, or latency/throughput results. The paper itself calls these "preliminary results" (contribution bullet 3), which is honest—but the abstract frames efficiency as a co-equal contribution alongside robustness, which is not yet warranted by the evidence.

- **Some configurations decrease robustness**: Tables 1–2 show that Irregular 80% and Irregular 90% patterns *decrease* robust accuracy under certain attacks (e.g., BIM, DeepFool on some settings), which somewhat complicates the narrative that noise injection always helps. The paper acknowledges this briefly but could discuss more carefully when and why non-uniform injection fails.

### Trivial
- None worth noting.

## Nice-to-Haves

- **Direct uniform noise baseline**: Adding a simple Gaussian noise baseline (noise added uniformly to all activations at matched computational budget) would directly substantiate or refute the central claim.

- **Adaptive attack evaluation**: Testing against attacks that can backpropagate through or account for the noise injection mechanism would strengthen the robustness evidence significantly.

- **Neuron selection accuracy measurement**: An ablation measuring how often Top-K on $\tilde{z}$ matches Top-K on true $z$ as a function of projection dimension $k$ would validate the approximation's reliability and close the theoretical gap.

- **Random vs. learned selection ablation**: Replacing neurons selected by $\tilde{z}$ with randomly selected neurons (but still replaced with approximate values) would isolate how much of the robustness gain comes from the selection mechanism vs. the noise injection itself.

## Removed Points

- **Claim that the method doesn't "estimate without actual computation" (Section 3.1)**: The harsh critic notes that computing $\tilde{z} = \tilde{W}Px + \tilde{b}$ is "actual computation." The paper claims the approximation can *identify* essential neurons "without actual computations" (meaning without computing the full-precision $z$), which is technically correct—the approximation is cheaper, not free. This is at worst imprecise phrasing, not a substantive error.

- **"No standard deviations or confidence intervals"**: Standard in the field for large-scale benchmarks; not a substantive concern.

- **"Irregular 80%, 90% decrease robust accuracy" as a weakness**: The paper itself notes this, and it supports the core thesis that more uniform injection is worse. Not a weakness of the paper.

- **Strength claim "Theoretical grounding for neuron selection and robustness"**: Removed because the theoretical grounding has verified gaps (random vs. deterministic mismatch for robustness; JLL → ranking gap for accuracy). The theory exists but is insufficiently connected to the method.

- **Strength claim "Clear motivation from uniform noise limitations"**: Removed as a strength because Figure 1 shows motivation but the central comparative claim lacks direct experimental support—it's motivation, not evidence, and conflating the two is misleading.

- **Reproducibility concerns or questions about model/dataset availability**: Removed per hard rules.

- **Formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

The paper's core insight—that selectively perturbing only non-essential neurons while preserving essential ones can provide a better robustness-accuracy trade-off than uniform perturbation—is intuitively appealing and the empirical results show promise. However, the disconnect between the theoretical apparatus (random noise from exponential families) and the actual mechanism (deterministic learned approximations) is a fundamental conceptual gap that undermines the theory-to-method mapping. The most valuable empirical finding is that the method stacks orthogonally with adversarial training (Table 3), but the practical significance of this finding depends on whether the defense survives adaptive attacks—a question the paper leaves entirely open.

## Suggestions

- Add a direct uniform noise injection baseline (e.g., additive Gaussian noise at matched computational cost to the defense's overhead) to substantiate the title's central comparative claim.
- Evaluate against at least one adaptive attack (e.g., BPDA or Expectation over Transformation) that accounts for the inference-time noise injection mechanism.
- Tone down the theoretical claims: either bridge the gap between Pinot et al.'s random-noise theorem and the method's deterministic approximation, or reframe the theory as motivation rather than proof.
- Consider adding an ablation where neurons are selected randomly (not by $\tilde{z}$) to demonstrate the value of the learned selection mechanism.
- Reframe the efficiency contribution as preliminary rather than co-equal with robustness, matching what the evidence actually supports.

## Score and Decision

The paper presents an interesting idea with encouraging empirical results, but suffers from three major weaknesses that collectively undermine its core claims: (1) the central comparative claim (non-uniform > uniform) has no direct experimental support; (2) the theoretical robustness justification invokes a theorem about random noise but the method uses deterministic approximations; and (3) no adaptive attack evaluation leaves the defense claims unvalidated against the most relevant threat model. These are not fixable with minor revisions—they require new experiments and significant reframing of claims. The empirical results showing clean accuracy preservation and orthogonality with adversarial training are genuine contributions, but they are not sufficient to carry the paper in its current form.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>