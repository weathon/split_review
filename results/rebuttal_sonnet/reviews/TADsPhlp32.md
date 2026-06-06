## Summary

This paper augments the AIDE hybrid AI-generated image detector with a "structural semantic" feature derived from recursive cuboidal partitioning (hierarchical SSE-reduction gains forming a normalized cumulative gain curve). The 1024-dimensional curve is compressed to 256 dimensions via a trainable FC+GELU projector and concatenated with AIDE's existing patchwise and semantic features, with only the projector and discriminator MLP retrained. The proposed method achieves a new state-of-the-art mean accuracy of 89.56% on GenImage (+2.68% over AIDE), while scoring second on AIGCDetect (91.85% vs. AIDE's 93.02%) and on the Chameleon out-of-distribution benchmark.

---

## Rebuttal Assessment

**Weakness: Missing ablation of MLP retraining alone**
- **Author's response:** Partially address — argues that non-uniform per-generator gains (ADM +3.0pp, GLIDE +3.4pp, VQDM +4.8pp, BigGAN +6.75pp; SD v1.4 +0.09pp, SD v1.5 −0.01pp) indicate the structural features carry signal independent of MLP retraining. Also notes architectural non-equivalence (changed input dimensionality prevents direct swap).
- **Assessment:** Unconvincing. I verified the per-generator gains from Table 1: the claimed numbers are accurate (AIDE vs. Ours: Midjourney +2.66pp, SDv1.4 +0.09pp, SDv1.5 −0.01pp, ADM +2.99pp, GLIDE +3.36pp, Wukong +0.75pp, VQDM +4.83pp, BigGAN +6.75pp). However, the selective-gain argument is logically insufficient — a retrained MLP would also produce non-uniform gains across generators if the existing features (patchwise/semantic) already have different discriminative profiles per generator. The architectural-non-equivalence argument actually supports the reviewer's concern rather than refuting it: it explains *why* the ablation is hard to run, not why it is unnecessary. No ablation appears in the paper, and the author explicitly acknowledges this and commits to adding it in revision.
- **Score impact:** Weakness unchanged.

**Weakness: Method regresses on AIGCDetect relative to its own baseline**
- **Author's response:** Partially address — confirms the regression is discussed in Section 4.8 and provides per-generator breakdown showing largest drops on BigGAN (−3.97pp), CycleGAN (−1.73pp), Guide/ADM-G (−2.06pp), SDv1.4 (−2.17pp), SDv1.5 (−2.22pp). Partially concedes the abstract framing is misleading.
- **Assessment:** Partially convincing on transparency, unconvincing on framing adequacy. I verified Section 4.8 does explicitly acknowledge the regression and provides a mixture-of-experts hypothesis — the original review's claim that the regression was "never hidden" is correct. However, the abstract states "strong generalization by achieving second-best overall mean accuracy on AIGCDetect" without noting that the method scores *behind* its direct predecessor. Section 4.5 saying it is "only slightly behind the AIDE baseline" is technically true but downplays the fact that AIDE is the *best* method on AIGCDetect. The per-generator analysis in the rebuttal is entirely computable from Table 2 (not new evidence in the paper) and is framed as a revision commitment.
- **Score impact:** Weakness downgraded slightly — the paper does discuss this in §4.8, so the original review slightly overstated the omission; however the abstract framing problem remains.

**Weakness: No ablation on N and M**
- **Author's response:** Acknowledge — concedes the limitation explicitly, notes the paper has only qualitative justification for N=1024 and M=256, commits to a sweep in revision.
- **Assessment:** Unconvincing as a response to the weakness — acknowledgment does not resolve it. No sensitivity data appears anywhere in the paper.
- **Score impact:** Weakness unchanged.

**Weakness: No statistical significance reporting**
- **Author's response:** Acknowledge — explicitly concedes that Chameleon margins (0.03pp gap on ProGAN) are meaningless without variance estimates, and that Section 4.6's characterization of Chameleon results as "crucial validation" is overstated.
- **Assessment:** Honest acknowledgment. The concession is significant: the authors effectively undermine their own "second-place finish validates generalizability" claim. No multi-seed results appear in the paper.
- **Score impact:** Weakness unchanged (and author's acknowledgment strengthens it).

**Weakness: Qualitative analysis is one-sided**
- **Author's response:** Acknowledge — agrees Figure 3 shows only AIDE-failure/ours-success cases, and none where the reverse is true, despite the AIGCDetect regression confirming such cases exist.
- **Assessment:** Valid acknowledgment. No balanced qualitative analysis exists anywhere in the paper. The concession is honest but the weakness stands.
- **Score impact:** Weakness unchanged.

**Weakness: Discriminative mechanism asserted rather than demonstrated**
- **Author's response:** Acknowledge — concedes that Section 3.2's mathematical motivation and Figure 1's single example do not constitute distributional evidence for the structural feature's discriminability, and that t-SNE/gain-curve histograms are absent.
- **Assessment:** Honest and complete concession. No distributional analysis appears in the paper.
- **Score impact:** Weakness unchanged.

---

## Strengths

- **Novel application of cuboidal partitioning to AIGC detection.** The paper is first to use hierarchical SSE-reduction gain curves as an AIGC fingerprint (Sections 1–3). The technique is borrowed from Ahmed et al. (2022) and Haque et al. (2025), but the application domain is genuinely new.
- **State-of-the-art on GenImage.** Table 1 verifies 89.56% mean accuracy vs. AIDE's 86.88% (+2.68pp), with consistent improvements on ADM, GLIDE, VQDM, and BigGAN. Even with attribution uncertainty, the empirical improvement on this large-scale benchmark is real.
- **Modular and computationally accessible.** Only the FC+GELU projector and MLP are trained; the two AIDE encoders are frozen. Training on a single A100 GPU in ~15 hours (verified in Section 4.3) makes this practically accessible.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing MLP-retraining ablation — core attribution claim unverifiable.** Section 3.3 confirms that the MLP is "retrained from scratch alongside the structural feature extraction module" — meaning the MLP is *never* trained without structural features under the proposed protocol. The indirect argument (non-uniform gains) does not rule out MLP retraining as the primary cause of improvement; the selective gain pattern is consistent with existing feature profiles per generator. The author concedes in the rebuttal that the ablation is absent and commits to a revision that does not exist. This remains the central evidential gap.

- **AIGCDetect regression and misleading abstract framing.** Table 2 confirms AIDE at 93.02% vs. Ours at 91.85% (−1.17pp). Section 4.8 does discuss this regression with a mixture-of-experts hypothesis, partially defusing the original review's claim that it was hidden. However, the abstract claims "strong generalization by achieving second-best overall mean accuracy on AIGCDetect" without noting that the direct predecessor (AIDE) is the first-best. This framing remains misleading even after the rebuttal concession.

### Minor

- **No ablation on key hyperparameters N and M.** Author acknowledges; no data in paper. N=1024 and M=256 are stated without sensitivity analysis.
- **No statistical significance reporting.** Author acknowledges and effectively concedes the Chameleon "crucial validation" claim. Sub-1% Chameleon margins are within noise.
- **Qualitative analysis entirely one-sided.** Figure 3 shows 13 cherry-picked AIDE failures; no reverse cases despite verified regression on AIGCDetect.

### Trivial

- **Discriminative mechanism asserted, not demonstrated.** No feature distribution analysis (histograms, t-SNE) validates that the gain curve feature occupies a discriminative region. Author acknowledges this fully.

---

## Nice-to-Haves

- Run MLP-retraining ablation (retrained MLP head, same lr/batch/epochs, without structural features appended), report on GenImage and AIGCDetect.
- Sensitivity sweep for N ∈ {256, 512, 1024}.
- Multi-seed variance reporting for all table entries; revise abstract's Chameleon "crucial validation" language.
- Per-generator failure analysis for AIGCDetect regression, with gain-curve distribution plots stratified by generator type.

---

## Novel Insights

The most intellectually honest aspect of the rebuttal is the near-complete acknowledgment of all six weaknesses. The authors do not overspun the results, and they correctly identify that the missing MLP-retraining ablation is the decisive unresolved issue. Their indirect argument — that non-uniform per-generator gains suggest structural feature independence — is not logically sufficient (uniform retraining effects on a non-uniform feature space would also produce non-uniform gains), but it is at least a principled attempt. The rebuttal's per-generator decomposition of the AIGCDetect regression, while computable from the paper tables, is presented clearly and is consistent with the Section 4.8 hypothesis. In the current submission, the structural feature idea is genuine and distinct; the experimental scaffold needed to separate its contribution from MLP retraining is simply absent.

---

## Suggestions

1. **Run the critical ablation:** Retrain the MLP head (identical hyperparameters) on the original AIDE feature space (no structural features) and report GenImage/AIGCDetect accuracy alongside the full model. This single experiment determines whether structural features carry independent value.
2. **Fix abstract framing:** Replace "strong generalization by achieving second-best overall mean accuracy on AIGCDetect" with an accurate statement acknowledging that the method scores below its direct predecessor AIDE on this benchmark.
3. **Add N ∈ {256, 512, 1024} ablation table** to demonstrate robustness of the gain-curve resolution.
4. **Report multi-seed variance** for all table entries; revise Chameleon characterization accordingly.
5. **Add balanced qualitative section** with failure cases showing regressions vs. AIDE alongside current Figure 3.

---

## Score and Decision

**Assessment of rebuttal impact:** The rebuttal is commendably honest but provides no new paper evidence for any of the six weaknesses. The per-generator analysis of AIGCDetect drops is computable from Table 2 and reveals nothing unavailable to the original reviewer. The indirect MLP-retraining argument is logically insufficient. All five remaining weaknesses (N/M ablation, statistical significance, one-sided qualitative, mechanism, framing) are acknowledged without refutation. The only credit to the rebuttal is that it clarifies Section 4.8 does discuss the AIGCDetect regression, slightly softening the original review's claim that the regression was obscured — but the abstract framing issue remains.

**Adjustment from 4.0:** The rebuttal shifts the AIGCDetect weakness from "hidden" to "discussed but misleadingly framed in abstract," a very minor improvement. The structural feature contribution idea is genuine and the GenImage numbers are real, placing this above the lowest tier. However, the central attribution weakness is unresolved and all other weaknesses are acknowledged as real. Score stays at **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>