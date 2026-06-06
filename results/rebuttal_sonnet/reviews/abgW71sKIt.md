Now I have enough of the paper to evaluate the rebuttal. Let me produce the updated review.

---

## Summary

This paper investigates why naive output alignment fails for 1-bit post-training quantization of LLMs, identifying three failure modes: (1) layer-wise output matching does not guarantee block-level improvement, (2) quantization error accumulates across layers causing the alignment target to drift, and (3) indiscriminate output alignment can degrade token-similarity structure. The paper proposes selective last-layer output alignment, an Output Error objective using true full-precision input X, and the Attention Matrix Preservation (AMP) mechanism. Experiments on OPT (1.3B–30B) and LLaMA-2/3 show strong improvements, except for a catastrophic and unexplained failure on LLaMA-2-7B PTB.

---

## Rebuttal Assessment

- **Weakness:** Unexplained catastrophic failure on LLaMA-2-7B PTB (3166 vs. best baseline ~657)
- **Author's response:** Partially address
- **Assessment:** Unconvincing — The rebuttal acknowledges the paper's one-sentence dismissal is inadequate ("the large perplexity indicates that the metric cannot provide a meaningful evaluation," verified at line 233), offers a post-hoc hypothesis (AMP's C4-calibrated token-similarity bias is penalized more severely by PTB's out-of-distribution distribution), and promises a diagnostic experiment in the revision. The hypothesis is untested in the current paper, and the rebuttal explicitly concedes this: "this hypothesis is not tested in the paper." The QA results cited as evidence are referenced in the paper (line 233) but only appear in the appendix and do not explain the PTB divergence. Notably, looking at Table 2, LLaMA-2-13B PTB shows the proposed method at 196.64 vs. ARB-X at 182.10—worse than ARB-X—while LLaMA-3-8B PTB (45.66) is the best. The catastrophic failure is specific to LLaMA-2-7B + PTB, making it more puzzling, not less. The weakness remains fully unaddressed in the paper as submitted.
- **Score impact:** Weakness unchanged

---

- **Weakness:** "Last FC layer only" design choice is asserted but not ablated
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The author fully concedes the gap (Section 4.2, line 161: "since it has the most direct impact on the block loss" — no supporting experiment), agrees a two-row ablation would provide missing evidence, and promises to add it in the revision. No current-paper evidence offered.
- **Score impact:** Weakness unchanged

---

- **Weakness:** AMP remains a heuristic with limited understanding of failure conditions
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal correctly notes that the AMP objective (Equations 9–10) is derived from a principled token-similarity preservation criterion, verified directly in the paper. The objective max ||X̂ŴŴᵀX̂ᵀ ⊙ XWWᵀXᵀ|| is explicitly derived (lines 138–143), and the masking rule uses the gradient sign of this objective. The distinction between "principled greedy rule" and "heuristic" is legitimate for the objective itself. However, the update rule (Equation 11) still lacks convergence guarantees, and no alternative (joint weighting) is compared. The rebuttal acknowledges the LLaMA-2-7B PTB failure may implicate AMP under domain shift but provides no evidence.
- **Score impact:** Weakness downgraded (from minor to minor-trivial) for the AMP objective derivation being in the paper, but failure-condition analysis remains absent

---

- **Weakness:** Framing overstates the contribution of the Output Error reformulation
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal acknowledges the quantitative mismatch (0.72 PPL from Output Error vs. ~10 PPL from AMP, both verified in Tables 3 and 4). The defense that the cross-term S = X̂ᵀX (Equation 5) changes the closed-form solutions for all three parameters (Equations 5–8) even beyond the raw PPL difference is legitimate and verifiable in the paper. This is a real mathematical point. However, the Introduction still lists all three failure modes as "co-equal" contributions, which the ablations (Tables 3–4) empirically contradict. The framing concern is only partially resolved.
- **Score impact:** Weakness downgraded slightly — the cross-term argument is valid, but the Introduction framing issue persists in the current paper

---

- **Weakness:** Block-level failure analysis (Figure 1) restricted to single model
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The paper explicitly states "The evaluation is performed on the LLaMA-2-7B model using the C4 calibration set" (verified at line 48). The rebuttal's indirect evidence argument (Tables 1 and 2 show consistent outperformance over ARB-X) is correct but does not directly diagnose block-level failure on OPT architectures.
- **Score impact:** Weakness unchanged

---

- **Weakness:** RMSNorm hypothesis in Section 5.3 is speculative and not tested
- **Author's response:** Refute
- **Assessment:** Convincing — The paper explicitly labels this as a hypothesis: "We hypothesize that this sensitivity arises because LLaMA uses RMSNorm instead of LayerNorm" (verified at line 263). The reviewer's labeling of this as a weakness for being "speculative" is undermined by the fact that the paper is already transparent about its speculative nature. The hypothesis is clearly marked and does not constitute an unsupported empirical claim.
- **Score impact:** Weakness removed (this was a reviewer error; the paper is transparent about it)

---

- **Weakness:** No reporting of variance across calibration runs
- **Author's response:** Acknowledge
- **Assessment:** Acknowledged but trivial — single-run evaluation is standard in this subfield; the concession to add variance estimates in revision is appropriate.
- **Score impact:** Weakness unchanged (trivial)

---

## Strengths

- **Systematic diagnostic analysis (Section 3, Figures 1–2):** Figure 1 directly shows block-level loss increases for specific layers under ARB-X despite layer-level improvements. Figure 2 quantifies error accumulation and token-similarity matrix divergence with depth, directly motivating the three proposed fixes.
- **AMP mechanism yields large, measurable gains on LLaMA:** Table 3 confirms removing AMP raises LLaMA-2-7B perplexity by >10 PPL on both C4 and WikiText2. The AMP objective (Eq. 9–10) is principled, derived from a token-similarity preservation criterion with explicit Frobenius distance formulation.
- **Strong, consistent gains on OPT:** The method achieves best perplexity across all OPT sizes (1.3B–30B) on all three evaluation datasets and best average QA accuracy.
- **Efficient closed-form optimization:** Equations 5–8 derive closed-form solutions incorporating cross-term S = X̂ᵀX, maintaining efficiency while extending the ARB-RC parameterization.
- **LLaMA-3-8B PTB performance is the best:** Table 2 shows 45.66 vs. ARB-RC 47.88 and ARB-X 53.86 — the method wins on this benchmark, partially limiting the scope of the PTB failure concern.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained catastrophic failure on LLaMA-2-7B PTB (3166 vs. best baseline ~657).** The paper's entire treatment is one dismissive sentence (line 233), confirmed by the rebuttal to be inadequate. The rebuttal offers only an untested post-hoc hypothesis and promises a future diagnostic — neither of which exists in the current paper. The failure is model-specific (LLaMA-2-7B but not LLaMA-2-13B or LLaMA-3-8B on PTB), making it more diagnostically interesting and the paper's silence on it more concerning. This directly undermines the "consistently outperforms" claim in the abstract and conclusion.

### Minor

- **"Last FC layer only" design choice is asserted without ablation.** Section 4.2 states the motivation but provides no experiment comparing alternatives. The rebuttal fully acknowledges this gap.
- **AMP failure conditions remain undiagnosed.** While the AMP objective is principled, the greedy masked update rule has no convergence guarantee, and no comparison against a jointly-weighted alternative is made. The LLaMA-2-7B PTB failure may implicate AMP but is undiagnosed.
- **Framing overstates the Output Error contribution.** Table 4 shows 0.72 PPL improvement vs. AMP's ~10 PPL (Table 3); the Introduction presents these as co-equal. The cross-term argument partially mitigates this but doesn't fix the Introduction.
- **Figure 1 analysis restricted to LLaMA-2-7B.** No direct diagnosis of block-level failure on OPT.

### Trivial

- **No variance across calibration runs.** Standard in field; small improvements (0.22–0.5 PPL) may not be reproducible.

---

## Nice-to-Haves

- A two-row ablation (last vs. first FC layer vs. attention output projection) on one model/benchmark would convert the design choice from intuition to evidence.
- A diagnostic experiment on LLaMA-2-7B PTB failure—testing whether disabling AMP recovers reasonable PTB performance—is the single highest-value experiment missing from the paper.
- A brief overhead summary in the main text (currently deferred to Appendix D).

---

## Novel Insights

The AMP mechanism's framing of quantization safety as preservation of the token-similarity proxy matrix is genuinely novel and well-executed. The observation that architecture choice (RMSNorm vs. LayerNorm) determines the severity of output alignment degradation is an interesting diagnostic finding, even if currently stated as a hypothesis. The selective last-layer output alignment strategy, while simple, provides a pragmatic solution grounded in the block-level failure analysis of Section 3.1. The paper's most underdeveloped opportunity remains diagnosing the LLaMA-2-7B PTB failure through this same architectural lens — if AMP's directional preservation is calibrated on C4 and interacts poorly with PTB's domain-shifted representations, that would validate rather than contradict the paper's theoretical framework.

---

## Suggestions

1. **Diagnose the LLaMA-2-7B PTB failure** with a targeted ablation: compare baseline (ARB-RC), proposed without AMP, and proposed with AMP on PTB. If removing AMP recovers reasonable PTB performance, characterize the AMP–domain-shift interaction explicitly.
2. **Add a two-row ablation for the "last FC layer" design choice** on LLaMA-2-7B C4.
3. **Revise the Introduction** to reflect the empirical magnitudes: AMP is the dominant component (~10 PPL), with Output Error providing a secondary but mechanistically grounded improvement (~0.7 PPL).

---

## Score and Decision

**Post-rebuttal assessment:**

The rebuttal is honest and largely confirms rather than refutes the original weaknesses. The most consequential change is that the RMSNorm hypothesis weakness (originally trivial) is legitimately removed — the paper was already transparent. The Output Error framing weakness is slightly downgraded due to the valid cross-term argument. All other weaknesses are acknowledged in the rebuttal but remain unaddressed in the current paper.

The major weakness — catastrophic LLaMA-2-7B PTB failure — is fully confirmed by the rebuttal to be inadequately handled in the paper. The rebuttal's promise of a future diagnostic experiment does not constitute an existing fix. The paper's abstract and conclusion claim "consistent" improvement, which Table 2 directly contradicts.

The score is maintained at **5.5**. The rebuttal reveals no new information that would justify raising the score; the honest acknowledgment of unresolved weaknesses confirms the original assessment. The paper has real contributions (AMP is effective and principled, OPT results are strong, Section 3 analysis is solid) but is incomplete in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>