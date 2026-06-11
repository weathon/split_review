Now I have a good set of narrow-band anchors. Let me compare LoLoRA against them:

- **EVA (EigenLoRA 5.00)**: LoLoRA adds a theoretical foundation (Theorem 4.4) to what EVA does empirically, plus online updates. This is a clear improvement. LoLoRA is stronger.
- **EVA (DM6Q45HWSk 4.75)**: The direct predecessor. Reviewers explicitly asked for theoretical justification of PCA-based initialization — LoLoRA provides exactly that. LoLoRA is clearly stronger than 4.75.
- **ReLoRA (5.75)**: Similar level — LoRA variant with theory + empirical validation. LoLoRA's empirical showing is comparable (mixed on GLUE, strong on MathQA), theory is cleaner. Roughly comparable, maybe slightly below because LoLoRA doesn't show as strong a "win" pattern.
- **RandLoRA (6.00)**: Stronger than LoLoRA — has full-rank updates, clear performance improvements across tasks, meaningful overcomes of LoRA limitations.
- **GeoLoRA (6.25)**: Even stronger — dynamical low-rank theory, single backprop pass, clear efficiency gains.
- **ROSA (6.00)**: Similar to RandLoRA — subspace adaptation with theoretical backing.

The pattern I'm seeing: LoLoRA has a solid theoretical contribution (Theorem 4.4) that fills a gap EVA reviewers explicitly asked for. But its empirical advantage is narrow — it essentially performs at parity with LoRA-FA across most settings, with the memory savings already achieved by LoRA-FA. On GLUE it actually loses to LoRA-FA (uniform). The paper's strongest contribution is the theoretical characterization, which is clean but primarily validates existing empirical findings.

This paper sits between EVA (4.75) and ReLoRA/RandLoRA (5.75-6.00). Its theory is stronger than EVA's, but its empirical showing is weaker than ReLoRA's or RandLoRA's. I'd place it around **5.0-5.5**.

Specifically: the theoretical contribution is genuine but the empirical story is that LoLoRA doesn't clearly beat the simpler baseline (LoRA-FA with uniform init on GLUE, or LoRA-FA with EVA everywhere else). This is a real limitation — the paper's core claim is that local updates improve over freezing, but the data shows parity. This is a classic "good idea, insufficient empirical validation" paper.

Final score: **5.0** — comparable to EigenLoRA (5.00) and EVA (4.75), but with better theory and slightly worse empirical justification relative to its own claim. Lower than ReLoRA (5.75) because ReLoRA demonstrated clear benefits across its experiments, whereas LoLoRA's benefits are marginal.

Let me now write the final review:

---

## Summary

LoLoRA proposes replacing the frozen A matrix in LoRA-FA with gradient-free, forward-pass local updates (Hebbian PCA / autoencoder) that converge toward the dominant eigensubspace of layer inputs, while B is trained via standard backpropagation. The paper theoretically characterizes the optimal A initialization under a random regression model (Theorem 4.4) as a transformation of the top-r eigenvectors of the input covariance, motivating the HPCA approach. The method aims to match standard LoRA performance while reducing activation memory.

## Strengths

- **Clean theoretical result (Theorem 4.4):** Under random regression assumptions, the optimal A is the set of nonsingular transformations of the top-r eigenvectors of Σ_zz. This fills a gap that EVA reviewers explicitly noted — providing a principled justification for why PCA-based initialization should work, with a precise and falsifiable characterization.

- **Thorough ablation of local update rules (Table 6):** The systematic comparison of HPCA variants, AE, and SoftHebb across ranks (2/4/8) on TinyLlama demonstrates that subspace-convergent rules matter — HPCA and AE perform similarly while SoftHebb fails, validating the method's design choice.

- **Cross-domain experimental coverage:** The method is evaluated on three qualitatively distinct setups — encoder-only NLU (RoBERTa/GLUE), decoder-only math reasoning (LLaMA/MetaMathQA→GSM8K), and multimodal (LLaVA/Visual Instruct) — demonstrating it is not brittle to architecture or modality.

- **Theoretical asymmetry between A and B:** The contrast between Theorem 4.4 (A has a well-defined optimal subspace tied to input statistics) and Theorem 4.5 (any full-rank B gives identical expected loss) provides a principled explanation for why freezing A is less harmful than freezing B, complementing prior empirical observations.

## Weaknesses

### Fatal

None.

### Major

- **Empirical advantage over LoRA-FA (uniform) is not clearly established.** On the largest benchmark (GLUE, Tables 1–2), LoRA-FA with uniform initialization — the simplest memory-saving baseline — outperforms LoLoRA HPCA on 5 of 8 tasks (CoLA: 67.9 vs 66.3, RTE: 86.4 vs 84.6, MNLI: 90.6 vs 90.3, QQP: 90.8 vs 90.6, SST-2: 96.7 vs 96.4), often by non-trivial margins. On MathQA (Table 3), the margin is 0.829 vs 0.826 (±0.005) — within error bars. Only on LLaVA (Table 4) is there a clear gap (2.93 vs 2.97 perplexity). This pattern undercuts the paper's central motivation that online HPCA updates provide a meaningful improvement over simply freezing A, since the simplest version of freezing A already performs at parity or better in most settings.

- **Theory characterizes initialization, not the dynamic method.** Theorem 4.4 solves a static problem: given unknown targets, what is the optimal A? The paper bridges this to the dynamic method by noting that HPCA converges to the top-r eigenspace (line 170), but this treats each layer's input distribution as stationary — which the paper acknowledges is not the case in multilayer architectures (conclusion: "we considered each submodule isolated with stationary targets, which is not strictly the case in multilayer architecture"). The theory therefore motivates the *target* of local updates but does not model whether online tracking during joint training provides an advantage over one-time EVA initialization followed by freezing. This is not just a theoretical gap — Table 4 confirms that HPCA updates do not improve EVA-initialized adapters (both at 2.93 perplexity), directly showing the dynamic updates add nothing when A starts in the right subspace.

### Minor

- **LoLoRA uses slightly more memory than LoRA-FA.** Table 4 reports 24.1 GB for LoLoRA HPCA vs 23.9 GB for LoRA-FA (and both vs 24.6 GB for standard LoRA). The paper's memory savings are relative to standard LoRA, not relative to the simpler LoRA-FA baseline. The paper acknowledges the extra optimizer state in the conclusion ("our method introduces a small amount of extra optimizer state for the local updates, unlike standard LoRA-FA") but this should be foregrounded in the main narrative rather than buried in the conclusion.

- **Abstract overclaims relative to GLUE.** The abstract states LoLoRA "maintains performance comparable to standard LoRA," but on GLUE, standard LoRA is clearly superior (e.g., CoLA: 69.6 vs 66.3). The claim holds for MathQA and LLaVA but not GLUE, and should be qualified.

### Trivial

None.

## Nice-to-Haves

- An experiment tracking alignment between A's row space and the true PCA subspace of current inputs over training steps would directly test the paper's hypothesized mechanism (does LoLoRA maintain better alignment than frozen EVA?).
- Reporting peak GPU memory for LoLoRA vs LoRA-FA as a primary comparison, rather than both vs standard LoRA, would clarify the memory trade-off.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "the paper never makes the crucial head-to-head comparison: LoLoRA vs LoRA-FA on peak GPU memory."** REMOVED — Table 4 does report this (24.1 vs 23.9 GB), and Table 3 reports both at 26 GB. The comparison exists; the Harsh Critic's claim of absence is factually incorrect.

- **Harsh Critic: "Theorem 4.5 contradicts the method's design."** REMOVED — Theorem 4.5 shows any full-rank B yields identical loss, which reinforces the A/B asymmetry that motivates focusing on A's subspace. It does not contradict the method; it explains why B's initialization doesn't need special treatment.

- **Harsh Critic: "The GLUE summary is misleading / hides LoRA-FA (uniform) advantage."** REMOVED — The paper's summary states "LoLoRA achieves slightly better results than LoRA-FA (EVA)," which is accurate. The full results including LoRA-FA (uniform) are in the tables. This is a misreading.

- **Strength Finder: "Consistent memory-performance tradeoff" as a top strength.** REMOVED — The memory mechanism is the same as LoRA-FA (not storing A's activations). The paper's contribution is the local update rule, not the memory savings, which are already achieved by LoRA-FA.

- **Strength Finder: "LoLoRA HPCA achieves best accuracy (0.829) on GSM8K" as strongest result.** WEAKENED — the result is 0.829 ± 0.004, tied with LoRA-FA (EVA) at 0.829 ± 0.005. This is a tie, not a win, and the paper itself acknowledges both achieve the same accuracy.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Qualify the abstract and conclusion claims. Replace "maintains performance comparable to standard LoRA" with a setting-specific statement, and replace "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" with a more nuanced summary that acknowledges the narrowness of the MathQA margin and the GLUE losses.

- Add LoRA-FA (uniform) to the GLUE summary discussion rather than only discussing LoRA-FA (EVA), so the full picture is visible to readers.

- Include the HPCA/SNL update equation explicitly in Section 3, and state the experimental rank in the main text, to improve self-contained reproducibility.

## Score and Decision

Now comparing against calibration anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EVA (DM6Q45HWSk) | 4.75 | 1 | Direct predecessor; LoLoRA adds the theory EVA reviewers asked for, plus online updates. LoLoRA is stronger. |
| LoRA-FA (RbKThNNFxr) | 5.33 | 1 | The baseline LoLoRA extends. LoLoRA adds theory and local updates but shows similar empirical performance. Comparable. |
| ReLoRA (DLJznSp6X3) | 5.75 | 1 | Similar scope (LoRA variant + theory + empirical). LoLoRA's theory is cleaner but empirical showing is weaker. |
| LoRAM (s7DkcgpRxL) | 6.20 | 1 | More ambitious. LoLoRA is less impactful in scope. |
| EigenLoRA (KxGGZag9gW) | 5.00 | 2 | Both use PCA/eigen-subspace for adapters. LoLoRA has better theory (Theorem 4.4 vs no theory for EigenLoRA). Comparable. |
| RandLoRA (Hn5eoTunHN) | 6.00 | 2 | Stronger — clear performance improvements over LoRA, full-rank updates. |
| GeoLoRA (bsFWJ0Kget) | 6.25 | 2 | Stronger — dynamical low-rank theory, clear efficiency gains. |
| ROSA (cgCKm5DOnu) | 6.00 | 2 | Stronger — significant margin over PEFT methods, theoretical backing. |

Round 1 bracketing placed LoLoRA between 4.5 and 6.0. Round 2 narrowed to: EVA (4.75) and EigenLoRA (5.00) on the low side; ReLoRA/RandLoRA/ROSA (5.75-6.00) on the high side. LoLoRA is clearly above EVA (4.75) because it provides the theoretical justification EVA lacks, but below RandLoRA/ROSA (6.00) because its empirical advantage is narrow and its method doesn't clearly beat the simplest baseline. It sits closest to EigenLoRA (5.00) — similar concept (PCA-subspace adapters) with similar empirical strength, but LoLoRA adds a cleaner theoretical result.

Final score: **5.0**.

MY FINAL SCORE