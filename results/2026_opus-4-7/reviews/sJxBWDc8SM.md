## Summary
This empirical paper revisits the SSM-vs-Transformer comparison on associative recall (MQAR) and copying. The central finding is that, with a finer learning-rate grid, modern SSMs (Mamba, Hyena, Mamba2, DeltaNet) solve MQAR at hidden sizes previously reported to fail — and that SSM success is confined to a narrow LR window while Transformers are LR-robust. Supporting ablations show (i) the 1D convolution before QKV is the key enabler of 1-layer expressivity for both Mamba and Attention, (ii) SSMs prefer width-scaling while Transformers benefit from depth, and (iii) DeltaNet's Householder-based mixing yields broader LR stability.

## Strengths
- Clean, controlled LR sweeps with 5 seeds across two distinct tasks (MQAR in Fig. 1; copy in Fig. 5) demonstrate that SSM LR-brittleness is not a task-specific artifact.
- Concrete empirical correction of prior conclusions: Fig. 2 directly contrasts the Arora et al. (2023) LR grid vs. a finer grid and shows Mamba at seq=512 moves from failure to near-perfect accuracy.
- The conv ablation in Table 2 is mechanistically informative and symmetric: removing conv1d from 1-layer Mamba collapses 99→2%; adding a conv before QKV in 1-layer Attention raises 2→99%.
- Width-vs-depth scaling result (Table 1) is striking: two 150M Mamba configurations differ from 16% to 100% based only on the depth/width allocation.
- Broad architecture coverage (Mamba, Mamba2, Hyena, DeltaNet, Attention) and substantial scale (~3000 runs, ~20k GPU hours).

## Weaknesses

### Fatal
None.

### Major
- **Central thesis overreaches the evidence.** The abstract and §1 claim a "fundamental mismatch in the loss landscape" and that "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics." The evidence is on synthetic MQAR (≤512, ≤2 layers) and copying with Adam only. This cannot adjudicate the asymptotic expressivity claims of Jelassi et al. (2024) or LM-scale claims of Arora et al. (2024). §8 concedes LM validation is "a critical next step," but the framing in the abstract/intro is far stronger than what the experiments authorize.
- **"Optimization brittleness" vs. "near-expressivity-boundary" is not disambiguated.** A narrow LR window is consistent with either a difficult landscape or a model operating near its expressivity boundary so that only a narrow weight region solves the task. The paper does not produce landscape diagnostics (sharpness, Hessian spectra, gradient-norm sweeps quantified) to support the "loss landscape mismatch" framing. The §7 hypothesis about DeltaNet's Householder mixing vs. Mamba's A_k decay is stated as a suggestive explanation but not isolated by a controlled re-parameterization of Mamba.

### Minor
- **§6 induction-head interpretation is metaphor, not mechanism.** A 1-layer model cannot host the Olsson et al. circuit by construction, so labeling the loss bump an "attempt to form induction heads" is loose. No attention-pattern or QK-circuit probing is provided. The paper hedges with "resembles," but the intro bullet point treats it as a finding.
- **Optimizer scope is Adam-only.** Brittleness is properly a model–optimizer property; at least one alternative optimizer would strengthen the architectural attribution and the claim that the LR window is intrinsic to the architecture.
- **Natural follow-up to Table 2 not run.** Does conv-augmented 1-layer Attention also exhibit width-scaling (Fig. 3) and inherit Mamba's narrow LR window? Answering this would tighten the §4 width-vs-depth framing.
- **§4 "depth-scaling for Transformers" is really "2 layers vs. 1 layer."** The paper itself acknowledges >2 layers gives no further improvement, so the framing should match the actual delta.
- **Table 1 has only three Mamba rows at 150M.** Directionally suggestive but thin as the sole evidence for the "scale along preferred axis" claim in the copy task.

### Trivial
- §7 phrasing that convolutions make Mamba "mechanically similar to a Transformer" overstates what Table 2 shows — it shows conv affects 1-layer expressivity, not operator-level similarity to attention.

## Nice-to-Haves
- Quantify the LR success-window width in log-LR units across models and plot against sequence length / hidden width.
- A small-scale LM validation (e.g., Pile subset) to test whether the brittleness persists at LM training scale.
- Ablate weight decay, β2, warmup to rule out trivial confounders.
- Controlled re-parameterization of Mamba's A_k decay term to test the DeltaNet hypothesis directly.
- Run conv-on-QKV across the Fig. 3 width sweep and LR sweep.

## Removed Points
These points are flagged to be removed; treat them with caution.
- Harsh critic framed "architectural ablation is incomplete on its own terms" as fatal/structural. Demoted: missing follow-ups are improvements, not invalidations.
- Generic strength about ~20k GPU hours alone — kept as supporting but not over-weighted; scale ≠ evidence for the central claim.
- Strength Finder's generic "thorough experimental scale" framing was retained but downweighted.

## Novel Insights
None beyond the paper's own contributions. The most useful novelty is empirical: prior MQAR comparisons systematically missed Mamba's narrow LR optimum, and a single 1D conv before QKV is sufficient to enable 1-layer associative recall in both Attention and SSM blocks.

## Suggestions
- Soften the abstract and §1 to: "LR tuning is a non-trivial confounder in MQAR/copy comparisons; under proper tuning, the empirical gap on these synthetic tasks largely disappears." Reserve stronger expressivity-vs-optimization claims for sections backed by landscape diagnostics or LM-scale evidence.
- Add a second optimizer to anchor the architectural-vs-optimizer attribution.
- Run conv-augmented 1-layer Attention through the same Fig. 3 width sweep and LR sweep.
- Provide an A_k-decay intervention on Mamba to test the DeltaNet hypothesis.

## Score and Decision

Anchors retrieved:
- Round 1: `cagNCwQEEN.md` (3.40, weak band) — multimodal SSM tuning, unrelated framing; `VtP7CamOR5.md` (3.00) — Mamba for PDEs, weak; `7ZyFjPUeJp.md` (3.00); `RmmrHEH6Nx.md` (3.00) — all weak Mamba-application papers, much weaker than this paper.
- Round 1 middle: `UAKnJMIBwf.md` (MambaPEFT, 6.00, Accept) — empirical study of fine-tuning Mamba; comparable empirical scope and concrete actionable findings, somewhat broader contribution surface than this paper. `i9RTCC6whL.md` (Mamba Lyapunov-stable, 4.67, Reject) — closest direct analog: empirical analysis of Mamba training/stability with bounded claims; comparable strengths and similar concerns about scope. `AL1fq05o7H.md` (Mamba, 6.25) — the original Mamba paper; not directly comparable as it's a method paper. `WYL4eFLcxG.md` (LR scaling laws, 6.00).
- Round 1 strong: `Tzh6xAJSll.md` (7.60), `GRMfXcAAFh.md` (8.00), `STUGfUz8ob.md` (7.60), `8zJRon6k5v.md` (8.00) — all stronger papers with substantial theoretical contributions, clearly above this paper.
- Round 2: re-confirmed `i9RTCC6whL` (4.67) and `UAKnJMIBwf` (6.00); also `vEtDApqkNR.md` (5.60), `aWLQTbfFgV.md` (6.25), `2edigk8yoU.md` (6.50), `hUD9ugK2OH.md` (5.75), `T1pUS4GZZq.md` (5.75).

Round-1 bracket: 4.5–6.5. Round 2 narrows: the paper's empirical analysis is closer to `i9RTCC6whL` (4.67) in spirit (Mamba empirical-properties study with bounded claims) but with a more impactful corrective finding (Fig. 2 directly overturns a specific Arora et al. result). It is weaker than MambaPEFT (6.0 Accept), which has broader contribution surface and a method. The overclaiming in framing, Adam-only scope, and synthetic-only evidence pull it down. Closer to the 5 anchors than to 6.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>