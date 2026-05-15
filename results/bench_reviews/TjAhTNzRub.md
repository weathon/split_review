Now let me write the final consolidated review.

## Final Review: MoRE: Mixture of Remapping Experts for Irreversible Feature-Level Unlearning

---

## Summary

This paper proposes MoRE, a training-free framework for feature-level machine unlearning. MoRE has three components: (i) prototype-orthogonal (PO) projection that decorrelates forget and remain prototypes before erasure to preserve utility, (ii) erasing and remapping forget prototypes into remain prototypes to break feature separability, and (iii) a mixture-of-experts extension that scatters forget features across multiple remain prototypes. The method requires only a single forward pass plus linear algebra (pseudoinverse computation). Experiments on CIFAR-10, CIFAR-100, Tiny-ImageNet, and Stable Diffusion show strong unlearning performance under both standard accuracy and Knowledge Retention (KR) metrics.

---

## Strengths

**1. Novel and principled technical approach.** The prototype-orthogonal projection is a clean mathematical solution to a real problem: forget and remain prototypes have cosine similarities up to 0.77, so naive erasure (as in ESC) degrades remain utility. Using the pseudoinverse to orthogonalize prototypes before editing is well-motivated and the ablation (Table 3) convincingly demonstrates that PO is necessary: without it, erase leaves 14% forget accuracy and remap degrades remain accuracy; with PO, erase achieves 0% forget and 99.94% remain accuracy.

**2. Training-free efficiency is a genuine practical advantage.** The entire unlearning operation is a single forward pass plus SVD of the prototype matrix (d×k, not N_f×d), yielding O(Nd) compute and O(dk) memory. This is substantially cheaper than training-based methods and avoids ESC's O(N_f d) memory bottleneck. The paper reports complete unlearning on CIFAR-10/100 in under 10 seconds (Figure 5).

**3. Strong KR results demonstrate real improvement over ESC.** Under the KR metric (linear probing on frozen features), MoRE achieves forget accuracy near random-guess levels. On CIFAR-100 KR, MoRE attains HM_f = 0.07, far below the retrain model (52.96) and ESC (99.60). This is a meaningful advance over ESC, whose residual forget cluster is visible in t-SNE (Figure 1).

**4. Clean ablation and sensitivity analysis.** The paper systematically ablates PO, erasing, remapping, and the multi-expert extension (Table 3). Sensitivity to number of experts (Figure 7) and target remapping class (Table 5) is analyzed. The stochastic vs. conditional router comparison (Table 6) is also useful.

**5. Generalization to diffusion models.** MoRE is applied to concept unlearning in Stable Diffusion v1.4 without architecture-specific tuning and achieves the best LPIPS_d tradeoff for both Van Gogh and Kelly McKernan erasure (Table 2), outperforming methods like UCE and RECE that were specifically designed for this setting.

---

## Weaknesses

### Major

**1. The "irreversible" claim is not supported by the evidence presented.** This is the paper's central claim (appearing in the title, abstract, introduction, and conclusion), but the evaluation only tests against a linear probe (KR metric) on frozen features. The paper repeatedly claims to "impede recovery via fine-tuning" (abstract, Section 1), yet provides **no experiment where the model is fine-tuned on the forget set after unlearning** to test whether forget accuracy can be recovered. The KR metric measures whether a single linear layer trained on frozen features can classify forget samples — this is a useful but weak threat model. An adversary who can fine-tune the full model (including the feature extractor) or train a nonlinear probe could potentially recover the remapped information, especially since the MoRE transformation (Equation 6) is a deterministic linear operator. The paper must either (a) provide full-model fine-tuning recovery experiments, (b) qualify "irreversible" to explicitly state the limited threat model, or (c) both. As it stands, "irreversible" conflates "hard to recover with linear probing" with "cannot be recovered at all."

**2. The transformation is theoretically reversible under a stronger adversary.** Equation 6 defines the remapping as a linear operator \(\hat{\mathbf{z}} = (\mathbf{I} - \mathbf{P}_f \mathbf{D} + \mathbf{P}_t \text{diag}(\mathbf{s}) \mathbf{D}) \mathbf{z}\). If the adversary knows \(\mathbf{P}_f, \mathbf{P}_t, \mathbf{D}\) (which are computed from the original model and forget/remain sets), the transformation is, in principle, invertible (assuming the full-rank condition). The paper does not discuss this threat model or test whether an informed adversary could undo the remapping. A claim of "irreversibility" should at minimum acknowledge the linearity limitation and discuss what class of adversaries the method is robust against.

### Minor

**3. ImageNet results are deferred to the appendix despite being featured in the scalability narrative.** The abstract, introduction, and experimental setup (Section 4) prominently claim ImageNet with ViT-base-16 as evidence of scalability, but the main text contains zero ImageNet results — they are deferred entirely to Appendix §C.1. While the appendix likely contains these results (the hard rules treat parser-stripped appendix content as existing), a reader of the main text cannot verify the scalability claim. At minimum, the main text should include an ImageNet summary table. The same applies to the time/memory comparison (Figure 5), which only reports CIFAR-10/100 data.

**4. Text-figure inconsistency on GPU memory.** The main text (Section 4.1) states MoRE consumes "less than 200 MB of GPU memory (see Fig. 5)," but Figure 5's OCR-extracted values show MoRE at 540 MB — nearly 3× the claimed amount. This discrepancy needs clarification: does the figure reflect a different configuration (model, dataset, batch size) than what the text describes?

**5. Baseline comparison may advantage MoRE on the KR metric.** The KR metric (introduced by Lee et al., 2025, the same group behind ESC) measures feature-level forget knowledge via linear probing — exactly the operation that MoRE is designed to defeat. Several baselines (NegGrad+, RL, BS, Lau) were not designed for feature-level unlearning or the KR metric, and the paper does not report whether they were hyperparameter-tuned for KR. MoRE's large advantage on KR (e.g., HM_f = 0.07 vs. Retrain's 52.96 on CIFAR-100) is impressive, but the gap is partly expected given the metric's alignment with MoRE's design. The paper should at minimum acknowledge this asymmetry and report whether baseline hyperparameters were optimized for KR.

**6. Several experimental details are unclear.** (a) The stochastic router assigns forget samples to experts randomly at unlearning time — is the assignment fixed after unlearning, or re-randomized at inference? The paper should clarify. (b) Prototypes are computed as class-wise activation means, but no sensitivity analysis to prototype quality is provided (e.g., for multi-modal classes where a single mean may be unrepresentative). (c) The random data forgetting adaptation (Table 4) computes separate forget/remain prototypes, but the description is too brief to understand how prototypes are defined for instance-wise forgetting where there may be only 1-2 samples per forget instance.

### Trivial

- Table 1 has many columns and is difficult to parse. Consider splitting into two tables or using a landscape layout.
- The notation changes between tables: Table 1 uses \(D_R\) while other tables use \(\mathcal{D}_f\) and \(\mathcal{D}_{rt}\). Consistent notation would help.
- Some numerical entries in ablation tables lack error bars where they would be informative (e.g., Table 5, target sensitivity).

---

## Nice-to-Haves

- A full-model fine-tuning attack experiment (the most impactful addition the authors could make).
- A discussion/experiment on whether the MoRE transformation is invertible given knowledge of the prototypes — either information-theoretic analysis or an empirical reconstruction attack.
- Including ImageNet results (at least one summary table) in the main text rather than only in the appendix.
- Non-linear probing (e.g., 2-layer MLP) to test whether a stronger probe can recover forget knowledge.
- Clarification of the GPU memory inconsistency between text and Figure 5.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Table formatting/headers are garbled"** (from Harsh Critic): The garbled column headers in the extracted text (e.g., "D | F | D_r | D_h") are parser artifacts from PDF extraction, not errors in the original submission. Removed per formatting nitpick rule.

2. **"Missing appendix content"** (from Harsh Critic): Criticism about ImageNet results, metric definitions, and router details being "missing" because they were deferred to the appendix. The parser strips the appendix from all papers; these sections exist in the original submission. Removed per hard rule about missing appendix details.

3. **"Missing related work"** (implied in Harsh Critic's "compare with more recent training-free unlearning methods"): Cannot confirm existence of unmentioned works without external sources. Removed per hard rule.

4. **"KR metric definition vague"** (from Harsh Critic): The paper references Appendix B.3 for metric details, which exists in the original submission. The main text contains sufficient description for context.

5. **"Baselines should be tuned for KR"** (from Harsh Critic — modified version kept above): The original version claimed baselines were "likely unfair" which is too strong; softened to acknowledge asymmetry.

6. **Strength Finder strength #1 ("Achieves irreversible feature-level unlearning")**: This conflicts with the verified weakness that "irreversible" is overclaimed. Per rules, when strength and weakness disagree, weakness wins. Moved here.

---

## Novel Insights

The most interesting observation from the reviews is that MoRE's core technical contribution — the prototype-orthogonal projection as a mechanism for disentangling correlated forget/remain subspaces before editing — is genuinely novel and well-supported, but the paper over-interprets this into a claim of "irreversibility" that the evaluation cannot sustain. This mirrors a pattern seen across the unlearning literature: papers that demonstrate strong results against linear probing on frozen features routinely claim "irreversibility" without testing against the most obvious stronger attack (full-model fine-tuning). The paper would be substantially stronger by lowering its claimed scope — replacing "irreversible" with "strongly resistant to linear-probe recovery" — and adding the missing fine-tuning experiments.

---

## Suggestions

1. **Tone down the "irreversible" claim throughout.** Replace "irreversible" with "strongly resistant to linear-probe recovery" or "feature-level unlearning with reduced recoverability" unless and until full-model fine-tuning attacks are evaluated.
2. **Add a full-model fine-tuning attack experiment.** After unlearning on a class, attempt to fine-tune the entire model (feature extractor + head) on just the forget class and report forget accuracy. If recovery is limited, this would genuinely support the stronger claim.
3. **Move ImageNet results from the appendix into the main text** — at minimum a summary table with D_f, D_r, HM, and KR metrics. The scalability narrative depends on these results being visible.
4. **Resolve the GPU memory inconsistency** between the text ("<200 MB") and Figure 5 (~540 MB).
5. **Acknowledge the KR metric's alignment with MoRE's design** and discuss whether baselines were tuned for this metric.

---

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human reviews corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/IPqUBL4R9x.md` (Distributional Unlearning) | 6.00 | Stronger theory, simpler method; accepted poster. MoRE is more methodologically novel but has a more central overclaim. |
| `/home/wg25r/review_agent/human_reviews_2026/xG0mQ4Xsfm.md` (REM) | 5.00 | Novel taxonomy+method with clear limitations; accepted poster. MoRE is comparably novel but has overclaim issues. |
| `/home/wg25r/review_agent/human_reviews_2026/iKqQGEOeej.md` (Memorize to Forget) | 5.50 | Novel unlearning approach, rejected despite decent scores. MoRE has stronger empirical results but worse overclaim. |
| `/home/wg25r/review_agent/human_reviews_2026/7cEMkTu7Lf.md` (Unlearning Isn't Deletion) | 4.00 | Shows irreversibility is rare; rejected. MoRE claims irreversibility but provides weaker evidence. |
| `/home/wg25r/review_agent/human_reviews_2026/DqvnwRe1V2.md` (Illusion of Forgetting) | 4.00 | Shows recovery of forgotten knowledge; withdrawn. MoRE claims to prevent this but doesn't test against recovery attacks. |
| `/home/wg25r/review_agent/human_reviews_2026/r6Z3BXDrzO.md` (Retrain Equivalence) | 4.50 | Theoretical paper on unlearning limitations; rejected. |
| `/home/wg25r/review_agent/human_reviews_2026/PS0YpCMzkb.md` (Mirror Mirror) | 2.00 | Weak evaluation framework paper; rejected. MoRE is substantially stronger. |

The paper has real technical novelty (PO projection + remapping + MoE for unlearning), clean ablations, and strong empirical results on KR metrics that are clearly better than ESC. However, the central "irreversible" claim is significantly overextended relative to the evidence (only linear probing on frozen features is tested), and the main text lacks ImageNet results despite touting scalability. Compared to accepted anchors like Distributional Unlearning (6.0) and REM (5.0), the method contribution is competitive but the overclaim and evaluation gaps are more severe. Placed relative to the anchors, the paper sits between REM (5.0) and Illusion of Forgetting (4.0).

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>