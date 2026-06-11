Now I have all the information needed. Let me write the final review.

## Summary

This paper presents an extensive empirical study (3,000+ runs, ~20,000 GPU hours) comparing the optimization dynamics of Transformers and modern recurrent models (Mamba, Hyena, Mamba2, DeltaNet) on multi-query associative recall (MQAR) and copying benchmarks. The central finding is that SSMs suffer from extreme learning-rate sensitivity — succeeding only within a narrow LR window — while Transformers are robust across a wide range. The paper further demonstrates that the 1D convolution in Mamba is the critical component enabling single-layer recall, and that SSMs favor width scaling while Transformers favor depth.

## Strengths

- **Compelling LR-sensitivity demonstration (Figure 1, Section 3):** The paper provides clear, multi-seed evidence that Mamba and Hyena accuracy on MQAR collapses outside a narrow LR band (~1 order of magnitude), while Transformer accuracy is flat across ~4 orders of magnitude. The prior LR grid from Arora et al. (2023), marked with dashed vertical lines in Figure 1, completely misses the SSM peaks — directly demonstrating a confounder in prior evaluations. This finding is the paper's most impactful empirical result.

- **Clean convolution ablation (Table 2, Section 7):** The symmetric ablation — adding a 1D convolution before QKV raises 1-layer Attention from 2% to 99% on MQAR; removing convolution from 1-layer Mamba drops accuracy from 99% to 2% — establishes that the convolution, not the recurrent S6 core, is the decisive component for single-layer recall. Additional ablations (removing gating, using S6+MLP as a Transformer backbone) make this near-exhaustive.

- **Cross-task replication on copying (Figure 5, Table 1, Section 5):** The LR instability finding generalizes from MQAR to the copying task with the same pattern: Transformer robust, Mamba brittle. Table 1's depth-vs-width comparison (12-layer Mamba at 1024-width fails at 0%, same model at 1408-width succeeds at 100%) cleanly illustrates the scaling asymmetry.

- **1-layer inversion of conventional wisdom (Figure 3, Section 4):** The finding that 1-layer Mamba can solve MQAR while 1-layer Transformers cannot — directly inverting results from 2-layer settings — is genuinely interesting and well-supported by the heatmap data across multiple sequence lengths and model dimensions.

- **DeltaNet robustness finding (Figure 7, Section 7):** DeltaNet achieves Transformer-level LR robustness on MQAR, while Mamba2 remains brittle. This provides a constructive architectural direction for future SSM design, even if the mechanistic explanation remains a hypothesis.

## Weaknesses

### Fatal

None.

### Major

- **The central thesis overreaches the evidence.** Line 39 states: "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics." However, the paper itself acknowledges at line 140 that "a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)" even after optimal LR tuning. If the thesis were fully correct, optimal tuning would close the gap everywhere; it does not. The evidence supports the weaker but still important claim that LR sensitivity is a major confounder that has led to underestimation of SSM capabilities — not that expressivity differences are illusory. This overclaiming matters because the strong thesis statement frames the entire paper and is restated in the conclusion (line 235) without incorporating the paper's own caveats.

- **The induction-head framing for single-layer models is unsupported by the paper's own definitions.** Section 2 (line 71) explicitly defines induction heads as "a circuit consisting of a pair of Attention heads in different layers" — requiring ≥2 layers by construction. Section 6 then reports a loss bump in 1-layer Transformers (line 188) and hypothesizes that the model "attempts to form induction heads." Since a single-layer model cannot form this circuit, the loss bump could be any phase transition. Without attention-pattern analysis showing what the model is actually doing during the bump, the induction-head interpretation is speculation. The underlying observation (loss bump without accuracy gain, contrasting with Mamba's bump *with* accuracy gain) is interesting on its own and should be presented as a purely empirical finding.

### Minor

- **The decay-mechanism hypothesis lacks a controlled ablation.** Section 7 attributes Mamba/Mamba2's narrow LR window to the decay term in A_k, contrasting with DeltaNet's Householder parametrization. The paper is honest about this being a hypothesis (line 221: "We hypothesize this is the main distinction"), but it is the paper's most actionable architectural insight. The obvious experiment — modifying Mamba's A_k to remove or replace the decay while holding other components fixed — is absent, leaving the key architectural recommendation as conjecture.

- **No random baseline for MQAR accuracy.** The paper reports that 1-layer Transformers recall "on average one key-value pair" (line 145), producing ~2% accuracy. With ~8K vocabulary and multiple KV pairs, the expected accuracy from random guessing needs to be reported to contextualize whether the 2% represents meaningful retrieval.

- **The depth-scaling evidence for SSMs is thin compared to the width evidence.** The claim that SSMs favor width over depth is well-supported by the width experiments (Figure 3) and partially by Table 1 on copying. However, there is no systematic depth ablation for SSMs on MQAR, and Figure 4 shows 2-layer Mamba outperforming 1-layer Mamba at fixed width — suggesting depth does help SSMs somewhat, which softens the binary "width for SSMs, depth for Transformers" framing.

- **No exploration of optimizer-level interventions beyond LR.** Since the paper's thesis is about optimization dynamics, testing whether gradient clipping, LR warmup, weight decay, or alternative optimizers can broaden the narrow LR window would substantially strengthen the practical guidance. The paper identifies the problem but does not explore solutions.

- **No analysis of whether the LR window shifts with scale.** The narrow LR window is demonstrated at specific model dimensions and sequence lengths. Whether the window shifts as models scale is important for practical guidance and is not discussed.

## Nice-to-Haves

- Reporting seed-level variance (is failure at non-optimal LRs consistent across seeds or high-variance?) would add diagnostic value for understanding the optimization landscape.
- Validating findings on a downstream language modeling task (acknowledged as a limitation at line 235) would significantly increase impact.
- Brief discussion of the compute distribution across the 3,000+ runs would help readers understand the practical cost of proper SSM tuning.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Formatting/style concerns:** Any concerns about text formatting, table layout, or figure presentation are parser artifacts and not reflective of the original submission.
- **Missing related works:** No external source verification is possible, so no related work criticism is included.
- **Availability questions about cited models/benchmarks:** All cited entities (Mamba, Hyena, DeltaNet, Mamba2, MQAR, copying) are treated as existing and available per the paper's citations.
- **Missing appendix content:** The paper defers experimental details to Appendix A.2 and full tables to Appendices A.3/A.4. These exist in the original submission.

## Novel Insights

The most novel insight from this paper is the identification that the 1D convolution — not the recurrent S6 core — is the critical component differentiating single-layer Mamba from single-layer Transformers on recall tasks (Table 2). The symmetric ablation (adding conv to Attention helps, removing conv from Mamba hurts symmetrically) provides a mechanistic explanation for prior observations about SSM vs. Transformer performance gaps that was not available in the existing literature. The secondary novel finding — that 1-layer Transformers exhibit a loss bump resembling induction-head formation without corresponding accuracy improvement, while Mamba exhibits a similar bump but succeeds — provides new information about training dynamics, even if the mechanistic interpretation requires further investigation.

## Suggestions

1. **Qualify the thesis statement** to match what the evidence supports. Change line 39 from "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics" to something like "Optimization dynamics, specifically LR sensitivity, constitute a major confounder that has led to underestimation of SSM capabilities on recall tasks."
2. **Reframe Section 6's induction-head discussion** as a purely empirical observation: "1-layer Transformers exhibit a phase transition in training loss without corresponding accuracy improvement, while Mamba exhibits a similar phase transition with task success."
3. **Add a controlled ablation of the decay mechanism** to transform the DeltaNet hypothesis from speculation to evidence.
4. **Report the MQAR random baseline** to contextualize the ~2% accuracy for 1-layer Transformers.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

# Selected Anchors

<related>["8QTpYC4smR", "VtP7CamOR5", "i9RTCC6whL", "iVy7aRMb0K", "LY3ukUANko", "GeUK3zGreN", "hwSmPOAmhk", "PdaPky8MUn", "d8w0pmvXbZ"]</related>