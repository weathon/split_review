Now I have a thorough read of the paper. Let me draft the review and run calibration searches.Now I have all the information needed to write the final review.

---

## Summary

This paper empirically studies the comparative learning dynamics of state-space models (SSMs) and Transformers on associative recall (MQAR) and copying tasks. The central contribution is demonstrating that SSMs like Mamba and Hyena succeed only within an extremely narrow learning rate window while Transformers remain robustly accurate across nearly three orders of magnitude—a confound that led prior work (Arora et al. 2023, Jelassi et al. 2024) to underestimate SSM capability. With proper tuning, Mamba can solve MQAR at sequence length 512 with hidden size 64, overturning a previously-claimed requirement that hidden size must match sequence length. Additional contributions include: contrasting width-vs-depth scaling behaviors, single-layer training dynamics exhibiting a loss-bump phenomenon in 1-layer Attention, a mechanistic ablation pinpointing 1D convolution as the key enabler of single-layer expressivity, and DeltaNet's improved optimization stability via Householder matrices.

---

## Strengths

- **LR sensitivity is cleanly demonstrated with concrete grids**: Figure 1 shows Mamba and Hyena achieve high accuracy only in a ~1-decade window (peak near LR=1e-4 and 1e-3 respectively) while Attention remains near-perfect across ~3 decades. Figure 5 replicates this on the copying task, confirming the finding is not task-specific. The comparison with Arora et al. (2023)'s LR grid (dashed lines in Fig. 1) is a concrete, falsifiable methodological critique.

- **Proper tuning reverses prior conclusions**: Figure 2 directly shows that finer LR grids enable Mamba to achieve near-100% accuracy on MQAR at sequence length 512 with model dimension 64—precisely the regime where prior work claimed failure. This is a tight replication challenge with explicit experimental controls (same code base, same task, different LR grid).

- **Contrasting scaling laws are supported by multiple experiments**: Figures 3, 4, and Table 1 collectively show single-layer recurrent models benefit from width scaling while single-layer Attention performance is entirely unaffected by width. Table 1's parameter-matched comparison (12×1024 Mamba = 0%, 12×1408 Mamba = 100%, same parameter count) makes the architectural scaling axis point compellingly concrete.

- **Table 2 ablation is the cleanest mechanistic result**: Removing conv1d from 1-layer Mamba drops accuracy to 2% (same as 1-layer Attention); adding conv on QKV to 1-layer Attention raises it to 99%. This tight symmetry provides a direct mechanistic bridge between the two architectures' single-layer expressivity and identifies a specific, transferable component.

- **DeltaNet stability pointer is actionable**: Figure 7 shows DeltaNet achieves near-Transformer-level LR robustness, and the paper links this to Householder-based mixing avoiding decay-induced vanishing gradients (citing Trockman et al. 2024). Even as a hypothesis, this identifies a concrete design principle for future stable SSMs.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Central thesis framing slightly overclaims**: The abstract states "Transformers differ from SSMs not in terms of expressive power but *mainly* because of their optimization dynamics" (line 39). However, Section 4 explicitly acknowledges "a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)" and Figure 3 shows single-layer Attention fails while single-layer Mamba succeeds—an expressivity difference that persists regardless of tuning. The Discussion (line 235) is more measured: "a crucial differentiator lies not just in their theoretical expressivity, but in their fundamental learnability." The abstract should be revised to match this nuanced formulation, since the data support "optimization is a significantly underweighted differentiator *alongside* expressivity," not the dominant one.

- **"Fundamental mismatch in the loss landscape" is interpreted rather than measured**: The abstract claims LR sensitivity "reveal[s] a fundamental mismatch in the loss landscape of modern recurrent models compared to Transformers." All evidence is task-performance sensitivity to LR; no landscape is directly characterized (no gradient norm trajectories, no sharpness or curvature analysis). The difference between "optimal LR is harder to find with a coarse grid" and "the loss landscape geometry is fundamentally different" cannot be distinguished from the current evidence. Direct measurement (e.g., gradient norms at and outside the narrow SSM window vs. Transformer) would make "loss landscape mismatch" a defensible claim rather than an interpretation.

### Trivial

- The DeltaNet stability explanation (line 221) is offered as a hypothesis—"We hypothesize this is the main distinction"—yet the introduction's bullet on "Architectural Drivers to Stability" slightly elevates it. This is minor but could be smoothed in the final version for consistency of hedging.

---

## Nice-to-Haves

- Direct loss landscape characterization (sharpness, gradient norm trajectories across LR values) would move the central "landscape mismatch" claim from inference to evidence. Even simple gradient norm plots at training failure vs. success LR values would substantially strengthen the mechanistic story.
- For the loss-bump observation in Figure 6, visualizing the actual attention patterns during and after the bump (canonical induction-head analysis from Olsson et al. 2022) would either confirm or cleanly rule out the induction head hypothesis. Either outcome would strengthen the paper.
- Extending the LR sensitivity finding to even one small language modeling pretraining experiment would substantially broaden applicability beyond synthetic benchmarks—the paper's acknowledged open question.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

1. **Figure 3/4 parsed alt-text description contradicts text** (Harsh Critic, noted as "PDF parsing artifact"): Lines 119–122 contain auto-generated image alt-text claiming "Attention models show high accuracy across all dimensions" for all single-layer settings, contradicting the paper's findings. The actual Figure 3 caption (line 126) correctly states "Attention models can no longer solve the task anymore." This is a PDF parser artifact, not a paper error. REMOVED per hard rule on formatting artifacts.

2. **Scope limitation as weakness**: The harsh critic raises the synthetic-only evaluation as an evidential gap. The paper explicitly acknowledges this: "we acknowledge that our analysis is conducted on synthetic benchmarks highly correlated with in-context learning. Validating these dynamics on downstream language modeling tasks is a critical next step" (line 235). Because the paper proactively scopes and acknowledges the limitation, this is demoted to Nice-to-Haves rather than a weakness.

3. **Induction head hypothesis elevated to "finding"**: The critic argues this should remain hypothesis-only and not be listed as a main contribution. The paper's main-text treatment at line 188 uses appropriate hedging ("we hypothesize"). The introduction bullet's phrasing is slightly stronger but correctly qualified elsewhere. This falls below the threshold for even a Minor weakness given the appropriate hedging throughout.

4. **Missing gradient norm analysis as Major weakness**: The harsh critic frames this as necessary to support the central thesis. Demoted to Minor (see above); the empirical LR sensitivity finding is independently compelling even without direct landscape measurement, and the characterization concern is a limitation rather than an invalidating flaw.

5. **Generic strength about SSMs being an "important problem"**: The Strength Finder includes some motivation-level framing. Filtered as insufficiently specific to include in the Strengths section.

---

## Novel Insights

The most genuinely novel insight is the mechanistic equivalence established in Table 2: the difference between 1-layer Mamba and 1-layer Attention reduces precisely to the presence/absence of the 1D convolution, a component easily transplanted. This creates a tight bridge between architectures and explains a specific expressivity gap mechanistically. The secondary novel insight is that DeltaNet's LR robustness can potentially be traced to Householder-based mixing that avoids decay-induced vanishing gradients, providing a concrete design hypothesis for future stable SSMs. The loss-bump observation in single-layer Attention (previously only reported in multi-layer settings) is also a genuinely new empirical finding, though its interpretation as "attempted induction head formation" remains unconfirmed mechanistically.

---

## Suggestions

1. Revise the abstract's central thesis from "not in terms of expressive power but mainly because of their optimization dynamics" to something like "not only in terms of expressive power but critically also in their optimization dynamics"—this matches the data, which show optimization as a major confound alongside persistent (but reduced) expressivity differences.
2. Add gradient norm or sharpness analysis to Section 6 or 7 to substantiate the "loss landscape mismatch" claim beyond LR-sensitivity observations.
3. For the induction head loss-bump (Figure 6), add even a brief attention-pattern visualization to distinguish the hypothesis from noise.

---

## Score and Decision

**Originality**: Solid—the central finding (LR sensitivity as confound in SSM benchmarking) is original and directly challenges published conclusions with controlled experiments. The conv1d ablation is a novel mechanistic result.

**Importance of research question**: High—understanding whether performance gaps between SSMs and Transformers reflect fundamental expressivity limits vs. optimization artifacts has direct implications for architecture development.

**Claim support**: Good—claims are backed by 3000+ runs, finer-grid comparisons, and clean ablations. The main claim (LR sensitivity confounds prior evaluations) is compellingly supported. The secondary interpretation (fundamental landscape mismatch) is inferred rather than measured.

**Soundness of experiments**: Good—controlled comparisons, multiple seeds, well-documented grid search. The parameter-matched scaling comparison (Table 1) is particularly well-controlled.

**Clarity**: Good—the paper is well-organized. Some minor framing tension between abstract and Discussion-level conclusions.

**Value to research community**: High for the SSM/recurrent modeling community—this is a useful corrective paper that would influence how future evaluations are run.

# Selected Anchors

Papers selected as topically comparable across bands:

- **Band 2** (2–4): `4wtcXV0kbi` (S7 SSM architecture paper, avg 3.5), `7eYmijcuqO` (RNN training dynamics, phase transitions, avg 3.0)
- **Band 3** (4–6): `XgH1wfHSX8` (Algorithmic Phases of ICL, avg 7.50), `TFR0GrzERG` (in-context learning study, avg 5.25)
- **Band 4** (6–8): `AL1fq05o7H` (Mamba paper, avg 6.25), `qtTIP5Gjc5` (Mamba token dynamics, avg 7.5), `LgzRo1RpLS` (MambaExtend, avg 6.25), `fMbLszVO1H` (LongMamba, avg 6.75)
- **Band 5** (8–11): None returned

<related>["4wtcXV0kbi", "7eYmijcuqO", "XgH1wfHSX8", "TFR0GrzERG", "AL1fq05o7H", "qtTIP5Gjc5", "LgzRo1RpLS", "fMbLszVO1H"]</related>

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>