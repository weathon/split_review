Now I have a thorough understanding of both the paper and the calibration landscape. Let me compile the final review.

**Round 1 bracket:** 5.5–7.5  
**Round 2 narrowing:** MoRE is clearly stronger than Deep Unlearning (5.25) and LAF (6.00), comparable to Score Forgetting Distillation (6.50), and slightly below Jogging the Memory (6.75) due to the irreversibility overclaim. **Final score: 6.5**.

---

## Summary

MoRE proposes a training-free framework for feature-level machine unlearning that combines three innovations: (i) prototype-orthogonal projection to decorrelate forget and remain prototypes before erasure, preserving remain utility; (ii) remapping of forget prototypes to remain prototypes, with a mixture-of-experts design that scatters forget features across multiple remain classes to resist recovery; and (iii) efficient activation-mean prototypes enabling linear time and constant memory complexity. The method is evaluated on image classification benchmarks (CIFAR-10/100, Tiny-ImageNet) and extended to concept erasure in diffusion models. Results show strong forgetting with preserved remain accuracy, and resistance to linear-probing-based recovery that exceeds retrain-from-scratch.

## Strengths

- **Novel and well-motivated method combination.** The three-component design is mathematically coherent and each component is individually justified: prototype-orthogonal projection addresses the observed prototype correlation problem (validated in Fig. 3), remapping breaks forget-class separability (validated in Fig. 1 t-SNE), and the MoE design scatters forget features to resist linear probing recovery (validated in Table 1 KR setting).

- **Strong ablation isolating PO projection's role.** Table 3 provides clear evidence: without PO projection, erasure leaves 14% forget accuracy and remapping drops remain accuracy to ~89%; with PO projection, forget accuracy drops to 0% and remain accuracy rises to ~99.9%. The cosine similarity analysis in Fig. 6 further corroborates the disentangling effect.

- **Training-free efficiency is genuinely compelling.** Figure 5 demonstrates sub-10-second unlearning and sub-600MB GPU memory, while achieving SOTA results. The linear-complexity prototype construction via activation means is a practical design choice that makes the method deployable at scale.

- **Resistance to linear probing recovery exceeds all baselines.** In the KR setting (Table 1), MoRE keeps forget accuracy near random guessing (e.g., HM_f=10.79 on CIFAR-10, 0.07 on CIFAR-100) while Retrain recovers to 41–53 and ESC recovers to 83–100. This is a genuinely significant result showing that scattering forget features makes them harder to recover via linear probing.

- **Versatile across modalities.** The method transfers to diffusion model concept erasure (Table 2) with no architecture-specific adaptation, achieving the best LPIPS_d scores and qualitatively removing Van Gogh's style (Fig. 4). The random instance forgetting results (Table 4) show the remapping idea extends beyond class-wise unlearning.

## Weaknesses

### Fatal

None.

### Major

- **The "irreversibility" claim is overconfident relative to the evidence presented.** The paper's title and abstract claim "irreversible feature-level unlearning," and the text repeatedly uses this language. However, the only recovery attack evaluated is linear probing with lr=0.1 (the KR setting). This demonstrates resistance to a specific, relatively weak recovery mechanism — it does not establish irreversibility in any meaningful security sense. Stronger adversaries (fine-tuning the full MoRE layer on remain data, non-linear probing, white-box inversion of the linear remapping, or adaptive attacks that exploit the stochastic router's non-determinism) are not considered. The stochastic router, in particular, could weaken a linear probe without preventing recovery by a more sophisticated attacker. The paper should either (a) tone down the language to "strongly resistant to linear probing recovery" and remove "irreversible" from the title, or (b) provide evidence against at least one stronger recovery attack (e.g., fine-tuning the full projection + routing layer on remain data while monitoring forget class re-emergence). In its current form, the central security claim is not adequately supported.

### Minor

- **Metric definitions are deferred entirely to the appendix, and table column labels are inconsistent.** The main text references D_f, D_r, D_rt, HM, HM_f, and KR but defines them only by citing Appendix B.3 (which is standard practice, but a one-sentence definition of each in the main text would substantially improve readability). More problematically, Table 1's column headers appear to have labeling issues — D_r appears twice per setting with different values, and D_R is used where D_ft (forget test accuracy) seems intended. For example, in the CIFAR-10 standard setting, the Original row shows D_r = 99.94 (likely remain train) and D_r = 91.07 (likely remain test, i.e., D_rt). These labeling inconsistencies make the tables harder to parse than necessary. The paper would benefit from clearly sub-labeling columns as train/test and forget/remain.

- **Diffusion model implementation details are sparse.** The paper states that prototypes are constructed from tokenized input prompts and that the method is applied to cross-attention layers (line 302), but does not specify which layers, how the remapping transformation integrates into the cross-attention mechanism, or how the stochastic router operates in the latent diffusion context. These details matter for reproducibility and for understanding why the method works out-of-the-box on generative models.

- **No limitations section.** The paper does not acknowledge any limitations. Notable ones include: activation-mean prototypes may be unstable for classes with high intra-class variance; the method assumes a static feature extractor; the remapping may produce semantically dubious predictions on forget inputs (they are classified as remain classes, but what does that mean for instance-level interpretability?); and the stochastic router, while efficient, introduces non-determinism whose implications for recovery are unexplored. A limitations paragraph would improve transparency.

### Trivial

- **"Exact feature-level unlearning" in the abstract is mildly misleading.** The method performs linear remapping, not exact data-deletion in the retraining sense. "Precise" or "targeted" would be more accurate.

- **The instance-wise unlearning adaptation (Section 4.3) is only sketched.** The paper says prototypes are "computed separately for the forget and remain sets" and then remapped, but the full adaptation is not described. Since this is an additional experiment rather than the core claim, this is a minor presentation issue.

## Nice-to-Haves

- A sensitivity sweep over ESC's pruning hyperparameter k would strengthen the comparison by confirming that ESC's poor remain accuracy is inherent to the method (as the paper's prototype-correlation argument suggests) rather than a consequence of suboptimal tuning.
- A qualitative discussion of the theoretical limits of remapping — under what conditions could an adversary invert the linear transformation — would strengthen the security argument even without additional experiments.
- Reporting standard deviations for all entries in Table 1 (currently only some variants report them) would improve confidence in the results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Evaluation metrics are poorly defined and inconsistently presented — an evidential problem."** The harsh critic claimed this is a fatal evidential issue. In reality, the paper references Appendix B.3 for metric definitions, which is standard practice. The main text provides enough context to understand what D_f, D_r, D_rt measure. The table column label inconsistencies appear to be largely parser artifacts (the paper's PDF has subscript formatting that gets mangled in text extraction). A genuine but minor labeling issue remains (D_r appearing twice). Downgraded from "fatal" to Minor with the labeling concern preserved.

- **"ESC baseline may not be fairly configured."** The harsh critic suggested ESC's poor performance might result from not tuning the pruning hyperparameter. However, ESC's D_f = 11.22 on CIFAR-10 shows it was NOT set to erase all prototypes (which would drive D_f to 0), so tuning was done. ESC-T (the trained variant) also shows poor remain accuracy, and the paper's core argument about prototype correlation provides a principled explanation for why ESC degrades utility. The concern is reasonable but not a major threat to the comparison's validity. Downgraded to Nice-to-Have as a sensitivity sweep suggestion.

- **"The paper does not discuss other recent feature-level unlearning attempts beyond ESC."** Removed per hard rules (missing related works are not flagged).

- **Duplicated figure caption (lines 054–072).** This is a parser artifact from the text extraction, not an author error. Removed per hard rules (formatting artifacts).

- **"The appendix which was not provided for review."** The appendix exists in the original submission; the parser strips it. Removed per hard rules.

- **"The meaning of harmonic mean variants is never stated."** HM is referenced to Appendix B.3, which is standard. The harsh critic's claim that this makes results uninterpretable is overstated. Removed as a separate weakness; folded into the Minor labeling concern.

- **"The stochastic router adds non-determinism that could inadvertently weaken a linear probe without preventing recovery."** This is speculative — the paper does not discuss this mechanism, and the critic is hypothesizing. Partially preserved in the Major weakness as a note about unexplored implications, but the speculative framing is removed.

- **Several Strength Finder strengths were removed**: "This paper addressed an important problem" — generic, removed. "The problem is interesting" — removed, too vague. The remaining strengths are all concrete and evidence-backed.

## Novel Insights

The paper's most valuable insight — supported by both the PO ablation and the KR recovery experiments — is that feature-level unlearning has two distinct failure modes that must be addressed separately: (1) **utility degradation** caused by prototype correlation between forget and remain classes, which PO projection solves; and (2) **recoverability** caused by residual cohesive-separable structure of forget features in latent space, which remapping + expert scattering solves. Prior work (ESC) addressed neither, and the paper demonstrates that addressing only one (e.g., erasure without PO, or single-expert remapping) leaves the other failure mode intact. This decomposition of the unlearning problem into disentanglement + scattering is a conceptual contribution that could guide future feature-level unlearning research beyond the specific MoRE architecture.

## Suggestions

- Replace "irreversible" with "recovery-resistant" or "strongly resistant to linear probing" throughout the paper, including the title. This is the single most important change; the paper's contribution does not require the stronger claim.
- Add a one-sentence inline definition for each metric when first used (D_f, D_r, D_rt, HM, KR) rather than relying entirely on the appendix.
- Fix the table column headers to clearly distinguish train/test and forget/remain (e.g., D_f_train, D_r_train, D_f_test, D_r_test).
- Add a brief Limitations paragraph.
- Include at least one stronger recovery experiment — fine-tuning the full MoRE layer on remain data — or explicitly scope the irreversibility claim to linear probing attacks.

---

## Score and Decision

### Calibration Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Deep Unlearning (pUOesbrlw4) | 5.25 | R1/R2 | MoRE has more innovations (PO, remapping, MoE), broader eval, and addresses irreversibility. MoRE clearly stronger. |
| SUN (p7mgNvOD9Q) | 4.00 | R1 | Simpler subspace erasure; MoRE's PO+remapping+MoE is substantially more sophisticated. |
| LAF (SIZWiya7FE) | 6.00 | R1 | Comparable novelty but MoRE has cleaner math and stronger results. MoRE slightly stronger. |
| Decoupling Class Label (OHOmpkGiYK) | 5.75 | R2 | Different problem scope. MoRE's contribution is more technically substantive. |
| Score Forgetting Distillation (gjwhDHeAsz) | 6.50 | R2 | Both accepted, both have notable weaknesses. SFD had missing related work section, weak baselines, runtime concerns. MoRE is more thoroughly evaluated across modalities. Comparable quality. |
| Jogging the Memory (fMNRYBvcQN) | 6.75 | R2 | Different contribution type (attack paper). Slightly stronger because its finding is more conclusive within its scope. MoRE's irreversibility overclaim pulls it slightly below. |

**Round 1 bracket:** 5.5–7.5. Round 2 narrows to **6.0–6.75**. MoRE is comparable to SFD (6.50) — both have genuine novelty with notable but fixable weaknesses — and slightly below Jogging the Memory (6.75) because the irreversibility overclaim is a substantive issue affecting the paper's central narrative. **Final score: 6.5.**

**Originality:** High. The combination of PO projection, remapping, and MoE for unlearning is genuinely novel in the MU literature.

**Importance:** The problem of feature-level unlearning with irreversibility guarantees is important for privacy and safety applications. The training-free aspect makes it practically relevant.

**Claims supported:** Mostly well-supported by experiments, except the "irreversibility" claim which is overbroad relative to the single attack tested.

**Soundness:** The mathematical derivation is clean and well-motivated. The ablation study is thorough. The evaluation covers multiple datasets and architectures.

**Clarity:** The method exposition (Section 3) is clear. The experimental section has some presentation issues with metric labeling and diffusion model details.

**Value to community:** High. The PO+remapping+MoE framework establishes a new direction for feature-level unlearning research, and the training-free efficiency makes it practically deployable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>