Now I have all the evidence I need. Let me compile the final review.

## Calibration Summary

**Round 1 (Bracketing):**
- Weak anchors (<3.5): SUN (3.0), UGradSL (3.0), MASIMU (2.5) — rejected papers with simple or flawed unlearning methods. MoRE is clearly stronger methodologically and empirically.
- Middle anchors (3.5–7.5): Deep Unlearning (5.25), Decoupling Class Label (5.75), Label-Agnostic Forgetting (6.0), NegMerge (6.0) — papers with real contributions but clear limitations.
- Strong anchors (>7.5): Unlearning-based Neural Interpretations (8.0), Probabilistic Unlearning for LLMs (8.0) — accepted papers with broader impact or theoretical depth. MoRE does not reach this tier.

**Round 2 (Narrowing 4.5–7.5):**
- Deep Unlearning (5.25) — training-free SVD-based class forgetting. MoRE has more technical innovation (PO projection, remapping, MoE) and stronger KR results.
- Label-Agnostic Forgetting (6.0, Accepted) — supervision-free unlearning via VAE. Comparable contribution level; MoRE's training-free nature and KR results are strengths, but MoRE has concerning internal contradictions.
- NegMerge (6.0) — weight negation via model merging. MoRE has a more original technical contribution.
- Unlearning via Sparse Representations (5.25) — model-specific (requires DKVB). MoRE is more general.

**Initial bracket:** 5.0–6.5
**After narrowing:** The paper is clearly above Deep Unlearning (5.25) and Unlearning via Sparse Representations (5.25). It is comparable to LAF (6.0) and NegMerge (6.0) in overall quality, with stronger technical originality but weakened by verifiable reporting errors. Final score: **6.0**.

---

Now presenting the consolidated review:

## Summary

MoRE proposes a training-free framework for class-level machine unlearning that combines prototype-orthogonal (PO) projection with mixture-of-experts (MoE) remapping. The key idea is to decorrelate forget and remain prototypes before erasing forget features and actively remapping them into multiple remain-prototype distributions, making the forget features indistinguishable from remain features at the representation level. The method is tested on image classification (CIFAR-10/100, Tiny-ImageNet, ImageNet) and diffusion model concept erasure. The most striking results are under the Knowledge Retention (KR) evaluation, where MoRE suppresses fine-tuning-based recovery of forget knowledge to near random-guess levels (e.g., HM_f=0.07 on CIFAR-100), far below all baselines including the retrain-from-scratch model (52.96).

## Strengths

- **Prototype-orthogonal projection is a well-motivated and empirically validated solution to the utility-preservation problem.** The paper identifies (Figure 3) that forget and remain prototypes have cosine similarities up to 0.77, causing naive erasure to damage remain representations. PO projection decorrelates prototypes prior to editing, and Table 3 confirms that without PO, remapping reduces remain accuracy to 89.52% on CIFAR-10, while with PO it stays at 99.87%. Figure 6 provides direct evidence that remain prototypes retain autocorrelation close to 1 after PO-based erasure/remapping.

- **KR results (Table 1) demonstrate a genuine advance in resistance to fine-tuning-based recovery of forgotten knowledge.** Under the KR setting with a high learning rate (lr=0.1), MoRE achieves HM_f values of 0.07 (CIFAR-100) and 0.50 (Tiny-ImageNet), compared to the retrain model's 52.96 and 37.00 respectively. This is the paper's strongest contribution — it shows that the remapping strategy prevents fine-tuning from recovering forget-class decision boundaries, going beyond what the "gold standard" retrain model achieves by a large margin.

- **Training-free with linear-time complexity, demonstrated across diverse architectures.** MoRE requires only a single forward pass and closed-form matrix operations (O(Nd) time, O(dk) memory). It is applied to CNN, ResNet, ViT, and Stable Diffusion v1.4 without architecture-specific modifications. The time results (Figure 5, ~9.5 seconds) are genuinely efficient.

- **Thorough ablation study validates each design component.** Table 3 disentangles the contributions of PO projection, erasure vs. remapping, and the full MoRE architecture. Table 6 compares stochastic vs. conditional routers. Figure 7 shows robustness to the number of experts. The sensitivity analysis for target remapping class (Table 5) further supports the method's stability.

## Weaknesses

### Major

- **Internal contradiction in memory efficiency reporting (Section 4.1 vs. Figure 5).** The text states: "On CIFAR-10 and CIFAR-100, MoRE performs complete unlearning in under 10 seconds while consuming less than 200 MB of GPU memory (see Fig. 5)." Figure 5 shows MoRE consuming approximately 540 MB of GPU memory — a ~3× discrepancy. Whether the text or figure is correct, this direct contradiction makes the efficiency claim and the paper's third claimed innovation ("Unlearning Efficiency") unreliable as presented. The authors must correct this and re-verify all resource figures.

- **MIA results in the random data forgetting setting show increased privacy leakage relative to Retrain, but the paper's discussion is evasive.** Table 4 shows Remap's MIA score is 79.31, higher than Retrain (74.64) and most baselines, meaning the unlearned model leaks more membership information than a model that never saw the forget data. The paper describes this as "comparable or superior performance to existing methods, outperforming most baselines in terms of average gap" — this is misleading. A method claiming to enable "trustworthy" unlearning should directly address why it increases MIA risk relative to retraining and whether this is inherent to the remapping strategy.

### Minor

- **The "irreversibility" framing overclaims the scope of the evidence.** The abstract, introduction, and conclusion describe the method as achieving "irreversible feature-level unlearning." The evidence only supports resistance to a specific attack: fine-tuning on forget data under the KR protocol (lr=0.1). While this is a strong result and a real improvement over prior work, it does not constitute irreversibility in a general sense. The paper does not evaluate against adversarial attacks, probing on raw features before projection, or other information-extraction methods. The t-SNE visualization (Figure 1) shows scattering rather than information destruction. Scoping the claim to "resistance to fine-tuning-based recovery" would be more precise and still preserve the paper's contribution.

- **LPIPS_f and LPIPS_r individual metrics in Table 2 are not SOTA; the paper's claim of "highly competitive performance across all three LPIPS-based metrics" is a stretch.** MoRE's LPIPS_f (0.33 for Van Gogh) is behind ESD (0.40) and SAFEE (0.42) for target removal strength, and its LPIPS_r (0.08) is behind UCE (0.05) for preserving unrelated styles. Only the composite LPIPS_d = LPIPS_f - LPIPS_r is best. While LPIPS_d is a reasonable tradeoff metric and all raw numbers are reported, the framing slightly overstates MoRE's individual-metric standing.

- **Performance degrades sharply at shallower layers (Table 7).** At the third-to-last layer, forget accuracy under erasure on CIFAR-100 rises to 12.53%, compared to 0% at the final layer. The paper acknowledges this but understates its implications — the method works well primarily when applied at the final (most class-separable) layer, which limits its generality across architectures or use cases where the final layer is not accessible.

- **HM and HM_f metric definitions are not given in the main text.** Table 1 is the paper's central result table, but the metrics HM and HM_f are only defined in Appendix §B.3, making the table difficult to interpret on its own.

### Trivial

None.

## Nice-to-Haves

- A discussion of *why* the MIA risk increases in the random data forgetting setting — is this because the remapping to remain-set prototypes effectively makes forget samples "look like" remain samples, causing the MIA attack to misclassify them as training data?
- An intuitive or theoretical explanation of why remapping forget prototypes to remain prototypes prevents fine-tuning recovery better than simple erasure (beyond the t-SNE visualization).
- The paper could note that the layer-depth limitation (Table 7) is consistent with the known property that earlier-layer features are less class-discriminative, which is exactly why prototype-based remapping is less effective there.

## Removed Points

*These points were flagged for removal from the inputs. Treat them with caution.*

- **Harsh critic's claim that "several baselines achieve stronger target removal AND lower collateral distortion" on the LPIPS task (Table 2)**: Factually incorrect when checked against the table. UCE has lower LPIPS_r (0.05) but worse LPIPS_f (0.25 vs MoRE's 0.33); ESD and SAFEE have higher LPIPS_f but much worse LPIPS_r (0.26, 0.31). No baseline achieves both. Removed because it is factually wrong.
- **Harsh critic's assertion that LPIPS_d is "contrived" and "misleading"**: LPIPS_d = LPIPS_f − LPIPS_r is a standard tradeoff formulation. All three raw metrics are reported in full, so the reader can evaluate independently. The criticism overstates the problem.
- **Harsh critic's complaint about Table 1 being "difficult to parse" and HM/HM_f not being defined in the main text**: The table layout is standard for multi-condition comparisons in this field, and deferring metric definitions to the appendix (with explicit forward reference) is common practice within page limits.
- **Strength Finder's generic claims about "addressing an important problem"**: These are superficial and not specific to the paper's actual contributions.

## Novel Insights

The most interesting observation that emerges from this review is the structural tradeoff exposed by the MIA results: MoRE's core strategy — scattering forget features into remain distributions — simultaneously achieves strong resistance to fine-tuning recovery (good for unlearning) while potentially increasing membership inference risk (bad for privacy). This suggests that "feature-level unlearning" and "privacy-preserving unlearning" may be partially conflicting objectives under the remapping paradigm, a tension the paper does not explore. The KR results (HM_f far below retrain) are genuinely novel and establish a new bar for resistance to recovery, but whether such aggressive feature obfuscation is desirable in privacy-sensitive settings where membership leakage also matters is an open question worth investigating.

## Suggestions

- Resolve the memory contradiction (text vs. Figure 5). Verify and report all GPU memory figures consistently. If the 540 MB in Figure 5 is total GPU memory (including base model, data loading, etc.), clarify this and report the incremental memory of MoRE separately.
- Scope the "irreversibility" claim to "resistance to fine-tuning-based recovery" throughout the paper. The current evidence does not support information-theoretic irreversibility.
- Add a discussion of the MIA increase in the random data forgetting experiment — explain why it occurs and whether it is a fundamental property of the remapping approach.
- Move the HM/HM_f definitions to the main text (at least a brief definition) so that Table 1 can be read without the appendix.
- In the diffusion model section, present LPIPS_f and LPIPS_r results without exclusively foregrounding LPIPS_d, or acknowledge that the composite metric does not tell the full story.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>