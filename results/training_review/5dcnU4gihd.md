Now I have thoroughly read the paper and verified the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes "attention head purification" as a new perspective for harnessing CLIP for domain generalization. The key insight is that not all attention heads in CLIP's image encoder are equally useful for DG — some encode domain-specific/background cues that hurt generalization. The method operates at two levels: (1) **task-level purification** via head-aware LoRA (HA-LoRA) that independently adapts each head to the task, and (2) **domain-level purification** via domain-invariant gating (DIG) with an MMD loss that learns to weight heads toward domain-invariant features. The two levels are jointly trained with a decoupled gradient flow (MMD does not update HA-LoRA). The method is shown to be orthogonal to prompt-learning techniques and achieves 79.0% average accuracy across five DG benchmarks.

## Strengths

- **Novel empirical observation grounding the whole approach.** Figure 1 demonstrates that selectively dropping attention heads *improves* CLIP's DG performance by >5% on OfficeHome, directly contradicting the prevailing assumption that preserving all of CLIP's original knowledge is optimal. This observation is both intuitive and experimentally supported.

- **Decoupled two-level purification is validated to provide additive gains.** Ablations (Table 1 Left) show that HA-LoRA (+2.6% OH, +1.1% DN) and DIG (+1.2% OH, +0.5% DN) each improve over the zero-shot baseline, and their combination yields additive improvement (+4.6% OH, +3.4% DN). The final method achieves the best average accuracy (79.0%) across five benchmarks (Table 4).

- **Head-aware LoRA is shown to be more effective than conventional LoRA specifically when combined with domain-level purification.** Without DIG, HA-LoRA vs. LoRA shows only 0.1–0.2% difference. With DIG, the gap widens to 1.0–1.4% (Table 1 Right). This cleanly supports the claim that per-head independence in LoRA facilitates subsequent head selection.

- **Decoupled gradient flow (MMD updating only gates, not LoRA) is empirically justified.** Table 2 shows that applying MMD to HA-LoRA (85.8% OH) or to both HA-LoRA and gates (86.0%) underperforms applying MMD only to gates (87.0%), validating the design choice.

- **Method is orthogonal to prompt learning and consistently improves six prompting variants.** Table 3 shows that attention head purification adds 2.1%–5.5% average accuracy gain across CoOp, CoCoOp, DPL, DUPRG, STYLIP, and PromptStyler, demonstrating broad compatibility.

- **Training is more efficient than competing fine-tuning methods** (1h30m vs. 2h–5h+ on DomainNet, Appendix Table 4) with no additional inference overhead.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent baseline reproduction for CLIPood undermines the SOTA comparison.** In Table 4, the original CLIPood paper reports 78.6% average accuracy, but the authors' own reproduction of CLIPood yields 76.9% — a discrepancy of 1.7%. Against the original CLIPood, Ours (79.0%) leads by only 0.4%, and on DomainNet Ours (62.0) is actually *worse* than the original CLIPood (63.5). Against the reproduced version, the gap is a more credible 2.1%. The paper presents both numbers without any discussion of the discrepancy. While the method still outperforms both, the reader cannot determine which comparison is the fair, apples-to-apples one. The authors should (a) explain why their reproduction differs from the original, and (b) use a consistent evaluation framework for all methods.

### Minor

- **The "Ours" entry in the main comparison table (Table 4) does not explicitly state which prompt-learning method was combined.** The caption says "attention head purification combined with prompt learning." The reader has to cross-reference Table 3 to infer that the 79.0% result corresponds to PromptStyler + Ours (since that's the combination that yields 79.0 in Table 3). The main result table should be self-contained on this point. This is a presentation and reproducibility clarity issue, not a methodological flaw, and can be fixed by adding a footnote.

- **Description of how MMD loss is applied across layers is ambiguous.** The method section (Eq. MMD, line 171–179) defines the loss on "image features output by CLIP's image encoder," which reads as a single loss on the final representation. The implementation section (line 228) states "impose the MMD loss on each layer." These are not contradictory — MMD can be computed at each layer's output — but the description should be unified to avoid confusion. A clarifying sentence specifying layer-wise MMD computation and aggregation would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Analysis of whether consistently selected heads correspond to "domain-invariant" properties across different source-domain splits.** The paper shows gate weight distributions (Appendix Figure 6) but does not quantitatively verify whether the same heads are selected across different training splits, which would strengthen the domain-invariance claim.

- **Ablation on which layers benefit most from purification.** The method applies purification to all layers uniformly. Showing whether later layers contribute more than early layers (or vice versa) would provide useful insight.

## Removed Points

These points are flagged to be removed, treat them with caution:

- Harsh critic's claim that MMD not being "formalized" with a theoretical link is a major gap. The paper provides a clear heuristic argument (small MMD → domain-invariant features → gates emphasize invariant heads) that is standard for MMD-based methods in DG literature. This is sufficient for an empirical paper. (Strawman weakness.)

- Harsh critic's framing of the "Ours unspecified prompt method" as a "methodological gap" and a violation of "basic standards of reproducibility." The prompt method can be inferred from Table 3, and the paper states it combines with prompt learning. The criticism is valid as a minor clarity issue but not a methodological gap. (Overblown criticism.)

- Strength Finder's claim about "joint training with decoupled gradient flow is beneficial and validated" — while this is real, it's already covered by the more specific strength about decoupled MMD updating being validated. Keeping it as listed above is fine but noting for calibration.

## Novel Insights

The reviews surface an interesting tension: the paper's core empirical contribution — that dropping attention heads helps DG — is genuinely novel and well-demonstrated, yet the paper's central claim of "state-of-the-art" performance rests on numbers that are somewhat ambiguous due to the CLIPood reproduction issue. This suggests a pattern where the paper's *methodological* contribution (head purification, HA-LoRA, DIG) is stronger than its *comparative* showing. The paper would benefit from reframing around the mechanism it introduces rather than the marginal SOTA claim, since even a 0.4% lead over an inconsistently-reproduced baseline is not the paper's strongest selling point. The ablated analyses (Tables 1–3) tell a more compelling story than the SOTA table.

## Suggestions

1. **Re-benchmark CLIPood (and ideally all baselines) under the exact same codebase, data splits, and hyperparameter schedule.** Report these numbers as the primary comparison, with original-paper numbers in a separate column for reference. This single change would resolve the most significant weakness.

2. **Explicitly state in the caption of Table 4 (or in a footnote) that "Ours" uses the PromptStyler prompt**, since that combination yields the best average result.

3. **Clarify the MMD application**: add one sentence to the method section stating that MMD loss is computed at the output of each purified layer and the per-layer losses are summed (or averaged).

4. **Add a brief discussion of the CLIPood reproduction discrepancy** — e.g., "Our reproduction of CLIPood uses the same training setup as our method (batch size 36, 40 epochs, etc.), which may differ from the original paper's setup." This would resolve the ambiguity about which comparison is fair.

## Score and Decision

The paper makes a genuine contribution: the head-purification perspective is novel, the HA-LoRA and DIG components are well-motivated and ablated, and the method consistently improves over zero-shot CLIP and several prompt-learning approaches by meaningful margins (2.1%–8.1%). The weaknesses are significant enough that the SOTA claim is not as cleanly supported as it should be, but they are addressable (primarily requiring better baseline reproduction and clearer presentation) rather than fatal. The core methodology and empirical insights are sound.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>