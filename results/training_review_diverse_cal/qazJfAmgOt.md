Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper addresses label unlearning in Vertical Federated Learning (VFL), a setting where the active party (which holds labels) needs to erase information about specific classes from both its own model and the passive parties' models. The authors propose a few-shot method that uses manifold mixup to augment forward embeddings from a small set of labeled samples, then performs gradient ascent on the augmented embeddings. Experiments across MNIST, CIFAR10, CIFAR100, and ModelNet show the method achieves near-zero accuracy on unlearned data while preserving retained-data accuracy better than most baselines, and completes unlearning in seconds.

## Strengths

- **First work to address label unlearning in VFL**: The paper systematically identifies the gap between existing VFU work (which focuses on removing entire passive parties) and the scenario where the active party needs to unlearn a specific class while all parties remain. This is well-motivated (Section 1, Related Works).

- **Effective few-shot unlearning with manifold mixup**: The method achieves 0.00% accuracy on $\mathcal{D}_u$ across almost all single-class settings using only ~40 labeled samples, while maintaining competitive $\mathcal{D}_r$ accuracy (e.g., 89.11% on CIFAR10 ResNet18 vs. 90.61% baseline). The ablation (Figure 6) confirms that vanilla gradient ascent with the same 40 samples fails (40.48% $\mathcal{D}_u$ accuracy), isolating the benefit of mixup augmentation.

- **Quantified label leakage risk in standard methods**: Section 3 provides concrete evidence that gradients from Boundary Unlearning can be clustered by the passive party to reconstruct labels (e.g., 62.45% clustering accuracy for 4-class unlearning on CIFAR100), motivating the need for privacy-preserving unlearning procedures.

- **Dramatically lower runtime**: The method completes unlearning in seconds, outperforming all baselines on time efficiency (Figure 7), making it practical for deployment.

- **Robustness across varying system configurations**: Ablation studies demonstrate effectiveness with 1–4 passive parties and under differential privacy / gradient compression regimes (Figures 8–10).

## Weaknesses

### Fatal
None.

### Major

1. **The central privacy claim — mitigating label leakage during unlearning — is not empirically evaluated.** The paper's motivation flow is: (i) gradients from standard unlearning leak labels to passive parties (Section 3), (ii) the proposed method uses few-shot mixup + gradient ascent to "mitigate the risk of label privacy leakage" (abstract, line 29, conclusion). However, **no experiment measures whether the gradients transmitted by the proposed method resist the same clustering attack** (Equation 5) or any other label inference attack. The experiments measure unlearning effectiveness (accuracy on $\mathcal{D}_u$, MIA) and utility (accuracy on $\mathcal{D}_r$), but these are about *forgetting*, not about *whether the gradients exchanged during the protocol leak label information*. A model can forget well while still leaking labels through intermediate gradient information. Without this evaluation, the paper's headline privacy claim is unsupported. The method may still be valuable as an efficient unlearning procedure, but the claim of privacy protection is aspirational rather than demonstrated.

### Minor

2. **Inconsistent assumption about passive party possessing labels.** Section 3.1 (line 115) states "We assume that the passive party possesses corresponding labels for a limited number of features, defined as $\mathcal{D}^p = \{(\mathbf{x}_k^p, \mathbf{y}^p)\}$," and Section 4.1 (line 226) says "We assume that the active party discloses a limited number of labels to the passive party." However, Algorithm 1 and the gradient ascent procedure never send labels to the passive party — the active party receives forward embeddings, applies mixup locally, and sends only gradients back. This creates a misleading framing: the method works without disclosing labels to passive parties, so the assumption is both unnecessary and self-imposed. The paper should clarify that the active party uses a small number of *its own* labeled samples (which it already possesses) and that no labels are sent to passive parties. It should also acknowledge the side channel that passive parties can infer which samples are being unlearned (since they are asked to forward those specific embeddings).

3. **Few-shot sample size is not specified in the main experimental setup.** The ablation study (Section 5.3.2) reveals that 40 samples are used (comparing "GA-s using 40 samples" vs. "GA-A using 5000 samples"), but the main experimental setup (Section 5.1) and the main result tables (Tables 1–3) do not state how many samples are used for each dataset. Since datasets have very different class sizes (MNIST: ~6000/class, CIFAR10: 5000/class, CIFAR100: 500/class, ModelNet varies), 40 samples represents a very different fraction for each. The paper should report the exact number and ideally show sensitivity (e.g., 10, 40, 100 samples).

4. **MIA results presentation lacks clarity.** The MIA figures (Figures 4–5) are described only vaguely in the text (e.g., "Our solution show consistent ASR performance" without stating whether the ASR is low or high). The figure captions do not explain the y-axis or what constitutes good/bad performance. Numerical ASR values should be reported alongside the accuracy tables for interpretability.

### Trivial
None.

## Nice-to-Haves

- Evaluate the proposed method's gradients against the same clustering attack from Section 3 (Equation 5). Compare clustering accuracy on gradients from the proposed method vs. gradients from Boundary Unlearning and vanilla gradient ascent under the same few-shot setup. This single experiment would transform the privacy claim from speculative to empirically supported.
- A brief sensitivity analysis of the few-shot sample size (e.g., 10, 40, 100, 200) across datasets to characterize the trade-off between sample count and unlearning quality.
- A discussion of whether the passive party can infer which samples are being unlearned (since it must forward embeddings for specific sample IDs), and whether this side channel matters in the threat model.

## Removed Points

- **"The paper's central claim is not evaluated / this is a fatal flaw"** — kept as Major but not Fatal. The method's core contribution (first label unlearning in VFL with good efficiency/effectiveness) is substantiated. The missing privacy evaluation weakens but does not invalidate the paper's contribution; it is an addressable gap.
- **Criticism about missing appendix/proofs** — not present in the reviews, so no removal needed.
- **Stylistic/formatting nitpicks** — not present in the reviews.
- **Criticisms questioning existence of cited works** — not present.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a structural gap (privacy claim not evaluated) but do not contribute an original analytical insight that the paper itself does not contain.

## Suggestions

1. **Add a privacy evaluation experiment:** Apply the clustering attack (Equation 5) to the gradients produced by the proposed method during unlearning. Show that mixup-augmented gradients have lower clustering accuracy than gradients from Boundary Unlearning or vanilla gradient ascent. This directly supports the paper's main privacy claim.
2. **Clarify the threat model:** Delete or rewrite the assumption about labels being disclosed to the passive party (lines 115, 226). Explain that the active party uses a small number of its own labeled samples, requests only the forward embeddings, and never sends labels. Acknowledge the sample-selection side channel.
3. **State the few-shot sample size in the main experimental setup** (Section 5.1) and report the number used for each dataset.

## Score and Decision

The paper addresses a real and understudied problem with a simple, efficient method that demonstrably works well for unlearning. However, there is a significant gap between its central motivation (preventing label leakage) and what is actually evaluated. The method is novel and the unlearning results are strong, but the headline privacy claim requires empirical support before the paper delivers what it promises. On balance, the paper has genuine contributions but a critical evaluation gap that prevents full confidence in the stated contributions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>