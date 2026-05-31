Now let me do calibration search to anchor the score.**Round 1 bracket: 5.5 – 7.5**

The paper clearly outperforms the weak anchors (avg 2.5–3.0). The mid-band anchors (5.25–6.0) are comparable machine unlearning papers but weaker: the "Deep Unlearning" paper lacks adversarial evaluation and the KR framework; the "Label-Agnostic" paper addresses a different (less rigorous) challenge. MoRE's mathematical rigor, comprehensive evaluation, and efficiency arguments suggest it sits above 6.0 but the overstatement issues keep it from the 7.5+ band. Let me narrow.Now let me read one more key anchor to finalize:Now I have sufficient calibration data to write the complete review.

---

## Summary

MoRE (Mixture of Remapping Experts) introduces a training-free framework for feature-level machine unlearning that goes beyond subspace erasure (ESC) by remapping forget-class prototypes into the distribution of remain-class features. The three technical innovations are: (i) prototype-orthogonal (PO) projection via pseudoinverse that decorrelates forget and remain prototypes before erasure, (ii) a remapping operation that redirects forget features into remain prototype space, and (iii) a stochastic mixture-of-experts router that scatters forget features across multiple remain targets, breaking residual cohesion. MoRE operates in a single forward pass with O(Nd) computation and O(dk) memory, and is demonstrated on CIFAR-10/100, Tiny-ImageNet, ImageNet, and Stable Diffusion.

---

## Strengths

- **Irreversibility under adversarial fine-tuning (KR evaluation):** Table 1 shows that after gradient-based fine-tuning of the unlearned model on the forget data, MoRE keeps forget accuracy at near-random-guess levels (CIFAR-100 KR: HM_f = 0.07 vs. Retrain's 52.96 and all other baselines in the 50-99 range). This is the paper's most striking result and is consistently reproduced across CIFAR-10, CIFAR-100, and Tiny-ImageNet.

- **Simultaneous utility preservation:** HM scores in Table 1 confirm that MoRE preserves remain-set accuracy nearly identically to the original model (CIFAR-10 KR HM = 95.30, CIFAR-100 KR HM = 95.03), while most baselines suffer large utility drops in the same setting.

- **Prototype-orthogonal (PO) projection validated by ablation:** Table 3 shows that without PO, erase leaves 14.38% forget accuracy and degrades remain accuracy (D_rest = 89.52); with PO, both metrics become nearly ideal (D_f = 0.00, D_rest = 99.94). Figure 6 corroborates this: remain-prototype autocorrelation is preserved (diagonal at ~1) while the forget prototype's autocorrelation drops to 0 under erasure or maps to the target prototype under remapping.

- **Feature scattering visualized:** Figure 1's t-SNE plots confirm that ESC leaves a visually distinct forget cluster even after unlearning, whereas Remap absorbs it into a remain cluster, and MoRE disperses it across multiple clusters—directly supporting the irreversibility claim at the representation level.

- **Efficiency and scalability:** Figure 5 demonstrates that MoRE unlearns CIFAR-10 in ~10 seconds with ~540 MB GPU memory, compared to 100+ seconds and 470-566 MB for prior training-based methods, while simultaneously achieving superior unlearning. The O(Nd) / O(dk) complexity is correctly stated.

- **Extension to diffusion model concept erasure:** Table 2 shows MoRE achieves the best LPIPS_d tradeoff (0.25 for Van Gogh, 0.26 for Kelly McKernan) among all evaluated methods, and Figure 4 qualitatively shows style erasure while preserving prompt fidelity—a property that competing methods fail to achieve simultaneously.

---

## Weaknesses

### Fatal

None.

### Major

- **"Irreversibility" is overclaimed as a formal/categorical property.** The paper uses "irreversible unlearning," "completely impeding recovery," and "trustworthy guarantee" throughout (Abstract, §4.1, §5), but the evidence supports only one concrete claim: resistance to gradient-based fine-tuning at lr=0.1 on the forget data (the KR evaluation). The paper tests no other attack surface—varying the learning rate, number of fine-tuning steps, optimizer choice, or using linear probing of unfrozen features. The KR evaluation is a meaningful and well-chosen probe, but the categorical claim that unlearning is "irreversible" goes beyond what the experiments can establish. The accurate claim is that MoRE is strongly resistant to the specific fine-tuning recovery tested by the KR protocol. This should be reflected in the paper's language throughout.

- **"No architecture-specific adaptation" claim for diffusion models is factually incorrect.** Section 4 states: "our proposed method is applied to diffusion models entirely out of the box, with no architecture-specific adaptation, no hyperparameter tuning and no additional engineering." But the same section immediately describes applying "prototype orthogonalization, erasure, and remapping to the cross-attention layers, using tokenized input prompts to construct prototypes." Targeting cross-attention layers specifically and using tokenized prompts as prototype inputs constitutes architecture-specific design—it requires knowing that concept information in Stable Diffusion routes through cross-attention, that text tokens can serve as prototypes, and which layers to target. This does not invalidate the diffusion results (which are genuine and competitive), but the "zero adaptation" framing is incorrect and inflates the apparent generality of the method.

### Minor

- **KR evaluation absent from the random data forgetting experiment (§4.3, Table 4).** The paper's primary claim over baselines is the KR-setting irreversibility. Table 4 reports only standard accuracy and MIA for the random forgetting task, not the KR evaluation. Given that the paper's core advance is precisely adversarial resistance to fine-tuning recovery, omitting this from the only non-class-wise experiment weakens the completeness of the contribution. Also worth noting: Remap's MIA score (79.31) exceeds the retrain baseline (74.64), a gap the paper does not remark on.

- **Non-determinism of stochastic router not discussed.** §3.3 states the stochastic router is adopted as default and is input-independent, randomly assigning each input to one of N experts at inference. This makes the deployed model non-deterministic—the same input can produce different feature representations on repeated calls. For regulated deployment contexts, this is a real operational concern. The paper does not acknowledge it.

- **Target-class selection lacks a principled criterion.** Table 5 shows that in the Remap (single-expert) setting under the KR evaluation, HM_t varies from 29.26 (target class 9) to 69.78 (target class 0) depending on which remain class is used as remap target—roughly a 2.4× range with no principled rule for selection. The paper states "we leave deeper investigation to future work." While MoRE's multi-expert design mitigates this by averaging across targets, the single-expert Remap baseline (used as a stepping stone and in the diffusion experiments) has this open sensitivity, and no guidance is provided for practitioners who might use Remap in simpler settings.

- **"Retrain-beating" framing requires careful contextualization.** The paper presents MoRE's outperformance of the retrain-from-scratch model in the KR setting as simply "establishing a stronger unlearning paradigm." This deserves explicit acknowledgment that MoRE and retrain pursue different objectives: retrain removes past influence but preserves the capacity to re-learn, while MoRE actively corrupts the latent geometry to prevent future re-learning. Section 2 correctly describes the KD framework but the result in §4.1 is framed as "better" without this clarification. The paper would be strengthened by explicitly stating this distinction in §4.1.

### Trivial

- Table 7 labels the proposed method as "MoUE" where "MoRE" is presumably intended. This should be corrected.
- Metric definitions for HM, HM_f, and KR are deferred to Appendix §B.3, but the relationship between HM and HM_f is never explained in the main text. At minimum, one precise sentence per metric in §4 would make Tables 1–4 self-contained.

---

## Nice-to-Haves

- A companion robustness analysis varying KR fine-tuning learning rate, number of steps, and optimizer (or using linear probing) would bound the scope of the irreversibility claim concretely rather than leaving the attack surface undefined.
- A principled target-class selection rule (e.g., remap to the most similar remain prototype by cosine similarity in the PO space) would transform the sensitivity analysis from an open question into a design choice, improving practical usability.
- Extension of MoRE to sequential multi-class forgetting (when multiple forget classes are unlearned across successive requests) is a natural next step; the paper could at least briefly characterize whether the PO projection is composable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The irreversibility claim is fatal because an adversary could compute P† themselves"** (Harsh Critic): The critic argues that because the MoRE transformation is deterministic and linear, a white-box adversary with remain-class access could reverse-engineer it. This is a speculative attack scenario not tested by any experiment in the paper, and the paper does not claim robustness against arbitrary white-box adversaries. The KR evaluation is the defined attack model in the KD framework the paper adopts. The underlying concern (limited attack coverage) is legitimate and is captured in the Major weakness about overclaiming irreversibility, but the characterization as a "structural flaw" or "fatal" depends on assuming an attack not in scope. Demoted and merged.

- **"The comparison to retrain is structurally misleading"** (Harsh Critic): The paper does explicitly frame the KD task in §2 as different from traditional MU, and cites Lee et al. (2025) for the KD framework. The framing issue is real but minor, not structural. Retained as a Minor weakness about explicit contextualization.

- **Harsh Critic's Table 5 numbers ("HM_f from 10.79 to 90")**: These specific numbers are wrong. Table 5 KR HM_t for Remap ranges from 29.26 (target 9) to 69.78 (target 0). The value 10.79 is MoRE's KR HM_f in Table 1 (a different table and different method); 90 does not appear anywhere in Table 5. The underlying sensitivity concern is valid and retained as a Minor weakness, but with corrected framing.

- **"§3.1 theoretical framing overpromises" about remain-data distortion** (Harsh Critic): The critic notes that the guarantee DP = I_k applies to prototype vectors, not arbitrary remain data. The paper's claim "erasing or remapping forget prototypes can be carried out with minimal distortion to remain prototypes" is framed correctly as an empirical claim validated by ablation (Table 3). This is not an overpromise given the context; the ablation provides the relevant evidence. Removed.

- **"Multiple forget classes" handling unaddressed** (Harsh Critic): This is a future-work limitation, not a weakness of the paper's presented contribution. Removed as a criticism; retained as a Nice-to-Have.

- **Strength: "Generative-model extension applied entirely out-of-the-box"** (Strength Finder): The "no architecture-specific adaptation" claim is factually incorrect (see Major weakness). The diffusion results themselves are genuine, but the claimed strength of "zero adaptation" is not supportable. Removed and replaced with the factually accurate formulation in Strengths.

---

## Novel Insights

The paper's most technically interesting observation—underappreciated by both reviewers—is that the pseudoinverse D = P† serves simultaneously as a disentangler (DP = I_k ensures prototype independence) and a precision selector (P_f D surgically extracts only forget-aligned components of any feature vector). This dual role means the same linear operator that enables clean erasure also enables clean remapping, and the MoE extension follows naturally. The stochastic router can be understood as inducing an *ensemble* of remapping operators whose aggregate acts like an isotropic diffusion of forget-class features into the remain manifold. This is a more principled mechanism for destroying class-separability than the typical "noise injection" approach, and the connection between expert count and residual cohesion (Figure 7) quantifies it directly. The framework opens a clear research direction: designing the router as a function of the target privacy-utility tradeoff rather than fixing it as purely stochastic.

---

## Suggestions

1. Retitle or qualify the claim of "irreversibility" throughout. Use language like "strongly resistant to gradient-based knowledge recovery under the KR evaluation protocol" until broader attack-surface evidence is provided.
2. Correct the diffusion model claim to: "with minimal architecture-specific adaptation (targeting cross-attention layers) and no hyperparameter tuning."
3. Add KR evaluation columns to Table 4 (random data forgetting).
4. Add one sentence per metric (HM, HM_f, KR) in §4 for self-contained reading.
5. Briefly discuss non-determinism implications of the stochastic router for deployment.
6. Fix "MoUE" → "MoRE" in Table 7.
7. Provide a principled target-class selection rule (even heuristic) for Remap.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison to MoRE |
|------|-----------|-------|--------------------|
| Xagys9QD3T (Pseudo-Prob Unlearning) | 3.00 | R1 | Much weaker; no feature-level analysis, no adversarial evaluation |
| hwXUmwJAq5 (UGradSL) | 3.00 | R1 | Much weaker; gradient smoothing only, no KR-type analysis |
| BJfIDS5LsS (MASIMU) | 2.50 | R1 | Much weaker; multi-agent RL approach, weak results |
| pUOesbrlw4 (Deep Unlearning) | 5.25 | R1/R2 | Similar SVD/subspace approach; lacks KR evaluation and adversarial robustness, no diffusion |
| TLBPjILNVs (Unlearning via Sparse Rep.) | 5.25 | R2 | Narrower scope, no adversarial robustness evaluation |
| OHOmpkGiYK (Decoupling label/concept) | 5.75 | R2 | Different problem framing; no feature-level irreversibility |
| nb3VjILNVs (Low Compute Unlearning) | 5.75 | R2 | Similar efficiency focus; weaker results and narrower evaluation |
| SIZWiya7FE (Label-Agnostic Forgetting) | 6.00 | R1 | Accepted; representation-level but requires training (VAE); narrower scope |
| gjwhDHeAsz (Score Forgetting Distillation) | 6.50 | R2 | Accepted; diffusion-only, requires training/distillation; MoRE is training-free and broader |
| HVFMooKrHX (Utility/Complexity of Unlearning) | 6.60 | R2 | Accepted; theoretical analysis, complementary contribution |
| Essg9kb4yx (LLM Continual Unlearning) | 6.67 | R2 | Accepted; LLM-specific, different setting |
| fMNRYBvcQN (Jogging the Memory) | 6.75 | R2 | Accepted; attack characterization paper, comparable impact but different type |
| fXJCqdUSVG (Durability of LLM Safeguards) | 6.50 | R2 | Accepted; analysis paper, different domain |

**Bracket: R1 established 5.5–7.5.** R2 anchors narrow this significantly. MoRE is clearly above the 5.25 training-free SVD papers (which lack adversarial evaluation and diffusion extension). It is at or above the 6.0–6.5 accepted papers (Label-Agnostic, Score Forgetting Distillation), which are narrower in scope or require training. The two major weaknesses (irreversibility overclaiming and the diffusion adaptation claim) prevent it from reaching 7.0+, but the core methodology is rigorous, the empirical evaluation is thorough, and the contribution is genuine and multi-faceted.

**Final score: 6.5** — MoRE sits between the 6.0–6.5 accepted anchors (comparable scope and quality) and below the 6.75–7.0 range, where the overclaiming issues would need to be resolved for the paper to be unambiguously stronger than Jogging the Memory or similar high-quality accepted work.

**Decision: Accept.** The core contribution (pseudoinverse-based disentanglement + mixture-of-experts remapping) is technically sound, mathematically well-derived, and supported by comprehensive empirical evidence. The two major weaknesses are framing and precision issues that are correctable without additional experiments. No weakness rises to fatal.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>