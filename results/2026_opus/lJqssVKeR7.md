## Summary

The paper proposes **HiSo**, a federated zeroth-order optimization method that extends DeComFL by adding a diagonal preconditioner (updated via an exponential moving average of |Δx|²) on top of the scalar-only communication framework. The key trick is that since Δx is already reconstructible from the existing scalar+seed channel, every client can maintain a synchronized preconditioner without sending any extra Hessian-related bytes. The paper provides a non-convex convergence analysis that yields a d- and L-independent rate under a "well-approximated Hessian" condition, extends the analysis to τ>1 local steps (which DeComFL lacked), and shows 1.4–5.4× round speedup over DeComFL on OPT-350M/1.3B/2.7B for SST-2/QQP/SQuAD.

## Strengths

- **Free synchronized preconditioner via the existing scalar+seed channel** (§4.2, Eq. 12). The observation that Δx_{r,0} can be used to update H without breaking dimension-free communication is the paper's most distinctive technical contribution and is correctly executed.
- **Generalization of the scalar-only FL framework beyond ZO-SGD** (Algorithm 1, §3.3). Decoupling scalar-only communication from the specific choice of ZO-SGD enables broader algorithmic integration.
- **Convergence extension to τ>1 local updates** (Corollary 3). This resolves a limitation of DeComFL's analysis that explicitly only covered τ=1, and is concretely useful for FL where multi-local-step training is standard.
- **Consistent empirical speedup over DeComFL** (Table 2). The 1.4–5.4× round/communication reduction at matched accuracy is reproducible across three tasks and three model sizes (OPT-350M, 1.3B, 2.7B).
- **Robustness to the smoothing parameter ν** (Figure 5, left). Across ν ∈ {0.9, 0.95, 0.99} convergence and final accuracy are nearly unchanged, supporting practical usability.
- **Unification with DeComFL** (Corollary 2). The analysis recovers DeComFL as the H_r ≡ I special case, providing internal consistency with the prior baseline.

## Weaknesses

### Fatal
None.

### Major

- **The "Hessian-informed" framing overstates what Eq. (12) computes.** With Δx = g·H_r^{-1/2}u, we have |Δx_i|² = g² H_r^{-1}_{ii} u_i², so the EMA in Eq. (12) tracks a recursive RMSProp-like quantity on the preconditioned step rather than the Hessian or its diagonal. Footnote 2 quietly concedes this ("our method resembles RMSProp"), yet the abstract, introduction, and theorem narrative (Eq. 17, low-whitening-rank story) all hinge on the reader treating H as an approximation of Σ. The mechanism is interesting on its own merits, but the gap between "Hessian-informed natural-gradient" framing and "adaptive coordinate-wise scaling" mechanism is real and should be presented honestly.
- **The headline dimension-/L-independent rate is conditional on a property the paper never verifies the learned H actually has.** Corollary 1's O(√(ζ/mR)) requires Tr(H^{-1/2}ΣH^{-1/2}) ≤ ζ with ζ independent of d (Eq. 17). The paper's own §5.2 Remarks state "it is hard to determine if this approximation holds in the context of LLMs," and Figure 5 (right) plots the spectrum of H itself, not the whitened object H^{-1/2}ΣH^{-1/2}. Figure 4 is a synthetic log-normal toy demonstrating that low whitening rank *can* exist, not that the *learned* H achieves it. The paper falls back on a "degenerates to DeComFL in the worst case" disclaimer, but that means the dimension-independence — the one theoretical claim distinguishing HiSo from DeComFL — is currently best read as an asymptotic possibility rather than a property of the algorithm as run.
- **Table 3's "lowest communication cost in almost all tasks" narrative does not match its own numbers, and Tables 2 and 3 follow different protocols.** On OPT-1.3B+QQP, HiSo reports 96.67 KB vs DeComFL's 43.95 KB — more than 2× higher, not "only a little higher" as the §6 text describes. The cause is that Table 2 stops HiSo when it matches DeComFL's accuracy, while Table 3 runs HiSo to its own (higher) convergence, so the two tables tell different stories presented as if they were one. A single iso-accuracy or iso-communication comparison would resolve this.

### Minor

- **Experimental federation is small relative to the framing.** The introduction motivates HiSo with billion-parameter federated fine-tuning costing 1–5 TB/client; the experimental federation uses 6 clients with 2 sampled/round and tops out at OPT-2.7B. The results support "HiSo improves on DeComFL on small federations on GLUE-style tasks" rather than the broader claim suggested by the introduction; this is a scope mismatch, not a flaw in what was done.
- **τ is not clearly specified for the LLM experiments.** Corollary 3 is positioned as a key advance over DeComFL (which "cannot give a rate for τ>1"), but the LLM experiment section does not state τ, and the paper never reports a τ sweep — leaving the most theoretically distinctive contribution empirically untested in the LLM setting.
- **The (u⊤H^{-1}u)^{-1} scalar absorbed into the learning rate in Eq. (7) is glossed.** This scalar has dimension-dependent expectation (≈ 1/Tr(H^{-1})) and non-trivial variance; a brief comment on its size and on how the HiSo learning rate is comparable to DeComFL's would tighten the empirical comparison.
- **No isolation of "Hessian-informed sampling" vs. "any adaptive scaling".** A natural baseline would be DeComFL augmented with an RMSProp-style adaptive learning rate on g_r²u_r² (i.e. the same adaptive idea but without the natural-gradient construction in Eq. 10). This would tell us whether the speedup comes from the specific Hessian-informed sampling or from generic adaptive scaling — currently the two are entangled.

### Trivial

- "P = 5" is used in §6 without being introduced in the main text.
- The "2d" branch of the well-approximated definition (Eq. 17) under L-smoothness should probably be discussed more directly; framing the factor 2 as a "safety factor" understates that the interesting branch is the ζ one.

## Nice-to-Haves

- A small-model experiment (e.g. OPT-125M on a subset) where Σ can be approximated via finite differences and Tr(H^{-1/2}ΣH^{-1/2}) is plotted as a function of d would convert the central theoretical claim from "plausible explanation" to "verified property of the algorithm."
- A τ sweep on LLM tasks showing HiSo's advantage growing with τ in line with Corollary 3 would empirically anchor the multi-local-step contribution.
- Either present Table 2 + Table 3 under a unified protocol (iso-accuracy is the cleanest) or clearly explain why both protocols are needed; right now the dual presentation undercuts the communication-cost story.
- Reframing the paper around "scalar-only adaptive preconditioning" rather than "Hessian approximation" would make the introduction's claims consistent with the mechanism while preserving the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"§4.2 is missing a fixed-point analysis of what H converges to."* — A nice-to-have rather than a substantive weakness; HiSo's H definition is consistent with itself and the paper provides reasonable theoretical machinery.
- *"Convergence is measured in ||∇F||_{H^{-1}}² rather than ||∇F||² — the constants β_ℓ, β_u, φ̄ are not Hessian-spectrum-free."* — Standard for natural-gradient analyses; Assumption 4 already gives the translation and the constants are explicit. Worth a sentence in the paper but does not undermine the claim.
- *"Robustness of ν only shown on the toy CNN/MNIST setup."* — Generic ablation-completeness ask; the trends are reasonable to extrapolate and the focus on LLM convergence rounds is the higher-value comparison.
- *"§3.3 (Generalized framework) is too thin as a standalone contribution."* — Subjective framing critique; the generalization is one of four contributions and is correct.
- *Strength: "Numerical simulation of the whitening effect (Figure 4)."* — The Figure 4 toy uses a log-normal Σ rather than a learned H on a real model; this is illustrative, not evidence. Demoted because it conflicts with the verified weakness about the well-approximated condition being unverified.

## Novel Insights

None beyond the paper's own contributions. The genuinely interesting observation — that a synchronized adaptive preconditioner can be maintained for free over the existing scalar+seed channel — is the paper's own.

## Suggestions

- Reframe the paper around the honest mechanism: "scalar-only adaptive (RMSProp-style) preconditioning of a natural-gradient ZO step," with the Hessian story positioned as one plausible explanation rather than the central claim.
- Run a small-scale experiment that estimates Tr(H^{-1/2}ΣH^{-1/2}) for the learned H on a model where Σ can be approximated. Reporting how this trace scales with d across model sizes would directly support Corollary 1.
- Add an RMSProp-on-(g²u²) ablation (no natural-gradient sampling) to isolate the contribution of Eq. (10) above generic adaptive scaling.
- Unify Table 2 and Table 3 under a single protocol (preferably iso-accuracy) and rewrite the §6 narrative so the OPT-1.3B+QQP case is acknowledged rather than papered over.
- State τ in the LLM experiments and run a τ sweep to corroborate Corollary 3 empirically.
- Define P in the main text.

## Axis Assessment

- **Originality**: Moderate. The free-preconditioner-over-existing-scalar-channel idea is novel and well-executed; the Hessian-informed framing is borrowed from existing centralized ZO work (e.g. HiZOO).
- **Importance of question**: High. Federated LLM fine-tuning under dimension-free communication is a practically meaningful regime, and DeComFL's slow convergence is a real bottleneck.
- **Claims well-supported?**: Partially. The empirical speedup over DeComFL is well-supported. The "Hessian-informed" framing and the dimension-/L-independent rate are over-claimed relative to what the mechanism and experiments demonstrate.
- **Soundness of experiments**: Reasonable but limited. Three tasks × three model sizes is sufficient for a paper of this type, but the federation scale (6 clients) and the Table 2/Table 3 protocol mismatch weaken the empirical narrative.
- **Clarity**: Generally good. Algorithm 1 and §4 are clear; §5 mixes definitions and assumptions in ways that occasionally obscure what the theoretical contribution actually requires.
- **Value to community**: Solid. The scalar-channel-preconditioner trick is reusable, and the τ>1 analysis closes a real gap in DeComFL.

## Calibration

**Anchors retrieved (all rounds):**

- **Round 1 (weak band, <3.5):**
  - `GtlRN48XYA.md` (FeDeRA), avg 3.00 — generic FedFT+PEFT paper, weaker than HiSo.
  - `p4RAKZ4oik.md` (FedDTPT), avg 3.00 — federated prompt tuning, weaker than HiSo.
  - `pLyjsv1KWH.md` (FedCDD), avg 3.00 — heterogeneous FedFT, weaker than HiSo.
  - `ArJikvI6xo.md` (GFLAgent), avg 3.40 — LLM-as-agent FL, unrelated.
- **Round 1 (middle, 3.5–7.5):**
  - `omrLHFzC37.md` (DeComFL), avg 6.25 — *the* direct predecessor; read in full. HiSo strictly extends it (τ>1 theory, preconditioner) but inherits/oversells the dim-free narrative.
  - `DJRd4IQHGQ.md` (FeedSign), avg 5.25 — 1-bit FFT with ZO; related but different axis.
  - `kH5nNlgT52.md` (one-round FedFT), avg 4.50 — orthogonal direction.
  - `9H1uctBWgF.md` (Ferret), avg 4.67 — first-order shared randomness FFT.
- **Round 1 (strong, >7.5):**
  - `ZuazHmXTns.md` (PAdaMFed), avg 7.60 — adaptive FL with broad theory.
  - `vf5aUZT0Fz.md` (DEPT), avg 8.00 — unrelated pre-training paper.
  - `OOxotBmGol.md` (LLAMBO), avg 8.00 — unrelated.
  - `gc8QAQfXv6.md` (function-vector CF), avg 9.00 — unrelated.
- **Round 2 (within bracket):**
  - `FK8tl47xpP.md` (Greedy L2O), avg 6.25 — preconditioned descent with theory; comparable rigor, narrower topical fit.
  - `bEqI61iBue.md` (HiZOO), avg 5.67 — read in full. Centralized Hessian-informed ZO for LLM FT; reviewers raised the same "is the estimator really tracking the Hessian?" concern. Very close in spirit to HiSo's situation.
  - `Oqk1Ui6m0n.md` (Hessian-free natural gradient), avg 5.00 — unrelated PIML setting.
  - `SWg72N2ky1.md` (noise level ZO), avg 4.75 — unrelated.
  - `GYik1jT3gE.md` (FL pre-training init), avg 7.00 — unrelated.
  - `EcetCr4trp.md` (FL feature learning theory), avg 5.75 — theory-heavy FL, different focus.
  - `kjn99xFUF3.md` (FedDA), avg 6.00 — adaptive FL with theory, comparable rigor and scope to HiSo.
  - `Cy5IKvYbR3.md` (FedTextGrad), avg 5.75 — unrelated.

**Round-1 bracket:** between ~5.5 and ~7.0 (HiSo clearly above the weak band, and strictly stronger than DeComFL since it extends DeComFL with non-trivial theoretical and empirical contributions, but with similar oversell tendencies and similar empirical scale).

**Round-2 narrowing:** The two closest topical-and-rigor anchors are DeComFL (6.25, the direct predecessor) and HiZOO (5.67, centralized Hessian-informed ZO with the same "is the estimator really estimating the Hessian?" critique). HiSo combines both lines and adds a τ>1 extension; it is therefore at least as strong as DeComFL but inherits framing issues similar to HiZOO. FedDA (6.00) and Greedy L2O (6.25) provide additional ~6.0 calibration on adaptive/preconditioned methods with theoretical analysis. PAdaMFed (7.60) is stronger because of cleaner theoretical claims and breadth — HiSo does not reach that bar. The paper sits slightly above DeComFL's 6.25 because of the new τ>1 analysis and free-preconditioner idea, but is pulled toward 6.0 by the framing/verification issues.

**Final placement:** 6.0 — comparable to the direct predecessor DeComFL (6.25) and FedDA (6.00); above HiZOO (5.67) due to the FL-specific free-preconditioner mechanism; below PAdaMFed (7.60) due to oversold framing and limited validation of the central theoretical condition.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>