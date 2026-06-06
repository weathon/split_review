## Summary

This paper investigates why naive layer-wise output alignment fails for 1-bit post-training quantization (PTQ) of LLMs, identifies three concrete failure modes (block-level loss inconsistency, accumulated activation error, and attention pattern degradation), and proposes targeted remedies: selective application of output alignment to only the last FC layer per block, a reformulated Output Error objective using full-precision inputs X, and an Attention Matrix Preservation (AMP) mechanism. Experiments on OPT and LLaMA model families compare against BiLLM, PB-LLM, ARB-RC, and ARB-X.

---

## Strengths

1. **Systematic diagnostic analysis grounding the method's design.** Sections 3.1–3.3 provide concrete, well-instrumented preliminary experiments. Figure 1 directly shows layers where ARB-X *increases* block-level loss versus ARB, motivating selective layer application. Figure 2 traces accumulated error and token-similarity drift across blocks under ARB-X, providing the empirical basis for both the Output Error reformulation and the AMP mechanism. These diagnostics are more rigorous than most PTQ papers, which typically move straight to results.

2. **AMP yields a large and reproducible improvement on LLaMA architectures.** Table 3 shows that removing AMP causes LLaMA-2-7B perplexity to jump from 19.25 to 29.12 on C4 and from 15.42 to 26.24 on WikiText2 — more than 10-point increases. This gap is substantial and stands on its own as justification for the mechanism. The corresponding effect on OPT-6.7B is much smaller (≈0.18 perplexity), consistent with the paper's hypothesis about architecture-specific sensitivity.

3. **Consistent gains across OPT model families and across C4/WikiText2 for LLaMA.** On all five OPT model sizes (1.3B–30B), across C4, WikiText2, and PTB, and zero-shot QA (Table 1), the proposed method is best-in-class. On LLaMA-2-7B and LLaMA-2-13B (Table 2), the method achieves the lowest C4 and WikiText2 perplexity, including a 1.15 reduction over the next-best baseline on LLaMA-2-7B C4. For OPT-1.3B, the C4 improvement reaches 4.85 perplexity points over ARB-RC.

4. **Closed-form derivations maintain computational tractability.** Equations 5–8 extend the ARB-RC parameterization ($\alpha_r$, $\alpha_c$, $B$) to the Output Error objective and AMP constraint in closed form, avoiding expensive iterative solvers and keeping the method practical for PTQ settings.

---

## Weaknesses

### Fatal
None.

### Major

- **Catastrophic and unexplained regression on LLaMA-2-7B PTB.** Table 2 shows the proposed method achieving 3166 perplexity on LLaMA-2-7B PTB, versus 681.24 for ARB-X and 763.19 for ARB-RC — the two direct baselines the paper is designed to improve. The paper's dismissal ("the large perplexity indicates that the metric cannot provide a meaningful evaluation") is inadequate: the very same metric is used without complaint for all other configurations, and ARB-X/ARB-RC perform far better on this benchmark on the same model. BiLLM's 5243 does not excuse a 3166 from a method that achieves 19.25 on C4. The paper's central claim — "our solution consistently outperforms existing 1-bit PTQ methods" (Abstract) — is directly violated by this result. Without a mechanistic diagnosis (does AMP interact badly with the PTB data distribution? does the selective-layer strategy break down for this model/dataset combination?), readers cannot assess the robustness of the method. This is the single most important issue for revision.

- **The "last FC layer only" design choice is asserted, not demonstrated.** Section 4.2 states: "we adopt a selective layer-wise output approach, by restricting the output alignment to only the last fully connected layer of each block, since it has the most direct impact on the block loss." This rationale is intuition, not evidence — no ablation is provided comparing this to alternatives (all layers, first layer, attention output projection vs. MLP down-projection, etc.). Since this is the primary structural departure from naive output alignment application, it is also the primary design choice that needs empirical support. The preliminary analysis in Section 3.1 identifies that some layers behave badly under output alignment, but does not identify which architectural positions are safe; it certainly does not identify "last FC layer" as the right choice. The current evidence is insufficient to support the design as stated.

### Minor

- **AMP is a proxy mechanism with architectural ambiguity.** The token-similarity matrix $\hat{X}\hat{W}\hat{W}^\top\hat{X}^\top$ used in AMP is defined at MLP output layers, which are steps removed from actual attention scores (computed from separate Q/K projections). The paper acknowledges these as "a proxy for the attention mask" (Section 3.3), but does not characterize when the proxy is tight versus loose. The LLaMA-2-7B PTB failure raises the question of whether AMP's proxy approximation can fail in identifiable ways. This is a minor concern given the strong ablation results in Table 3, but worth clarifying.

- **Block-level motivation study is single-model.** Figure 1 supports the claim that layer-wise output alignment does not consistently reduce block-level loss, but the analysis is conducted only on LLaMA-2-7B. Whether this pattern holds across architectures (OPT, LLaMA-3) or model scales is left unverified. The paper characterizes this as "a fundamental limitation of ARB-X" (Section 3.1) on the basis of one model.

- **The RMSNorm sensitivity hypothesis is speculative.** Section 5.3 hypothesizes that LLaMA's sensitivity to AMP arises from RMSNorm making representations more direction-dependent. This is a plausible post-hoc explanation but is not tested. A controlled comparison or even a citation supporting this mechanistic claim would strengthen it.

### Trivial

- "Last fully connected layer of each block" is underspecified across architectures. In a LLaMA block, the last FC layer would be the MLP down-projection; in OPT, it could differ. A one-sentence clarification of how this maps across architectures would aid reproducibility.

---

## Nice-to-Haves

- Variance across calibration seeds (even 2–3 runs) would help distinguish meaningful from noise-level perplexity differences in the LLaMA comparisons where improvements are 0.22–0.24 points.
- A brief ablation table showing performance as a function of which FC layer receives output alignment (first, middle, last, all) would convert the "last FC layer" design from an assertion to a finding, substantially strengthening Section 4.2.
- A summary quantization-time comparison in the main text (not just deferred to Appendix D) would support the "minimal overhead" claim in the abstract.
- Treating the LLaMA-2-7B PTB failure as a diagnostic case study — even if it ends with "we cannot fully explain this" — would be more credible than the current dismissal and might reveal generalizable insights about when AMP helps vs. hurts.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic: "Equation 2 has a clear typographical error."** The equation as parsed reads $\|\hat{X}\hat{W} - \hat{X}\hat{W}\|_F^2$; the correct form should compare full-precision and quantized outputs. This is a parser artifact (the extraction garbles mathematical notation); the original submission does not have this error. Removed per the hard rule against formatting artifact criticisms.

- **Harsh Critic: "The overhead analysis is deferred to Appendix D with no summary."** Appendix content is stripped by the parser. The appendix exists in the original submission. Removed per the hard rule against criticisms about missing appendix content.

- **Harsh Critic: "AMP itself uses $\hat{X}$ rather than X — introducing the very error-accumulation problem."** Looking at Eq. 9, the AMP objective is $\text{Tr}[\hat{W}^\top M \hat{W}]$ where $M = \hat{X}^\top X W W^\top X^\top \hat{X}$, which includes both the quantized input $\hat{X}$ and the full-precision reference $X$. The critic's claim that AMP reintroduces accumulated error by using only $\hat{X}$ is factually incorrect given the formula. Removed.

- **Harsh Critic: "Small QA margins are unlikely to be statistically significant without variance reporting."** The concern about variance is valid as a nice-to-have (moved there), but removing QA as evidence entirely is too strong — the perplexity improvements, which are the primary metric, are meaningful. The statement that accuracy results "should not be cited as strong evidence" goes further than the evidence supports as a hard criticism.

- **Strength Finder: "Consistent empirical advantage across 14 of 15 model–dataset combinations."** This is slightly misleading: on LLaMA-2-7B PTB the proposed method (3166) is worse than ARB-RC (763.19), ARB-X (681.24), and even PB-LLM (657.24, albeit at 1.7 bits). The "14 of 15" framing obscures the severity of the failure on that one combination. Removed as stated; the method's actual coverage is noted accurately in the verified weaknesses.

---

## Novel Insights

The most genuinely novel element of this paper is the systematic attribution of AMP's importance — the observation that architectural normalization choice (RMSNorm vs. LayerNorm) appears to control whether output alignment degrades attention patterns, surfaced by comparing the effect of AMP on LLaMA (≈10 ppt perplexity) versus OPT (≈0.18 ppt). If substantiated, this is a testable, architecture-specific hypothesis about quantization sensitivity that goes beyond what the existing 1-bit PTQ literature discusses. The three-failure-mode taxonomy (block inconsistency, error accumulation, attention degradation) is also a cleaner diagnostic framework than most PTQ papers provide, and the modular ablation structure of Tables 3–4 makes the source of gains unusually transparent.

---

## Suggestions

1. **Diagnose the LLaMA-2-7B PTB failure.** Add a short investigation: does the failure appear when AMP is disabled? Does it depend on the calibration set? Is it tied to the selective-layer strategy? Even a negative result ("the failure persists regardless of AMP or objective choice") is informative and is far stronger than the current dismissal.

2. **Ablate the layer-selection strategy.** On a single model (e.g., LLaMA-2-7B, C4), compare: output alignment on the last FC only, on all FC layers, on the first FC only, and on attention output projections only. This is low-cost and would convert the central design choice from assertion to evidence.

3. **Clarify "last FC layer" across architectures.** Add one sentence specifying which layer position this maps to in LLaMA (down-projection of MLP?) and OPT (fc2?).

4. **Add a sentence-level quantization time figure** summarizing Appendix D's findings in the main text to support the "minimal overhead" claim.

---

## Score and Decision

**Originality:** The paper is incremental relative to ARB-X, but the AMP mechanism and the diagnostic framework are novel contributions. Solid but not groundbreaking. *3/5*

**Importance of research question:** 1-bit LLM PTQ is practically important for edge deployment. *4/5*

**Claims supported:** The consistency claim is violated by the LLaMA-2-7B PTB result. OPT results and LLaMA C4/WikiText2 results strongly support the method. Mixed. *3/5*

**Soundness of experiments:** Ablations are well-structured (Tables 3–4), but the "last FC layer" design lacks ablation and the PTB result is unexplained. *3/5*

**Clarity of writing:** Generally clear. Underspecification of "last FC layer" and dismissal of the PTB result are clarity/transparency issues. *3/5*

**Value to community:** The diagnostic framework and AMP mechanism are useful contributions. The code/method builds on existing open infrastructure. *3/5*

The paper has genuine empirical contributions — particularly the AMP mechanism and consistent OPT improvements — and a well-motivated diagnostic analysis. However, the unexplained catastrophic regression on LLaMA-2-7B PTB, which directly contradicts the paper's "consistently outperforms" framing, and the unjustified "last FC layer" design choice are substantive problems that require revision before acceptance. The paper is borderline; the PTB failure in particular needs at minimum a diagnostic treatment rather than dismissal.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>