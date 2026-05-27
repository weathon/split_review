Based on my reading of the paper and calibration searches, I'm ready to produce the review.

## Summary
WARP proposes a sequence model whose hidden state is the flattened weights of an auxiliary "root" MLP, updated by a linear recurrence driven by input differences $\Delta x_t = x_t - x_{t-1}$ and self-decoded via the MLP at a coordinate $\tau$. The framework is presented as a linear RNN with a non-linear readout that supports gradient-free test-time adaptation, in-context learning, and the seamless injection of physical priors into the root network; it is evaluated on image completion, ETT/PEMS08 forecasting, dynamical system reconstruction, UEA classification, and a synthetic ICL task.

## Strengths
- **Genuinely novel architectural primitive.** Treating the weights of an auxiliary MLP as the hidden state of a linear recurrence (Eq. 1), with self-decoding `y_t = MLP_θt(τ)`, is a distinctive design that does not collapse into prior linear-RNN/SSM formulations. Section 2.2 articulates this clearly, and the "self-decoding" framing is well-motivated.
- **Honest, modern UEA classification comparison.** Table 4 benchmarks against LRU, S5, Mamba, S6, Log-NCDE, LinOSS, FACTS, and Griffin. WARP attains the best accuracy on Ethanol (36.49) and Heartbeat (80.65) and second/third on SCP2 and Motor — concrete, current evidence that the architecture is competitive on long-sequence classification.
- **Strong PEMS08 result without graph structure.** Table 2 shows MAE 6.59 / RMSE 10.10 vs. the next best graph-aware baseline at MAE 13.45. Even granting the baseline gap discussed below, the magnitude is substantial.
- **Breadth of empirical sweep.** The paper spans image completion (MNIST/CelebA), forecasting (ETT, PEMS08), dynamical system reconstruction (MSD, MSD-Zero, LV, SINE), classification (UEA), and a synthetic ICL setup, all with parameter-matched comparisons in the main tables. This breadth is unusual for a new-architecture paper.
- **Gradient-free fast-weight update is concrete and useful.** The training algorithm (Sec. 2.3) cleanly separates the slow-changing (A, B, φ) and fast-changing (θ_t) parameters, with the latter updated by Eq. 1 rather than gradient descent — a real mechanism, not just a framing claim.

## Weaknesses

### Fatal
None — the central architectural contribution is implementable, evaluated, and the strongest empirical claims (UEA, PEMS08) survive direct inspection.

### Major
- **The "10×" WARP-Phys headline embeds the closed-form solution.** Section 3.2 (p.7) defines the "physical prior" for SINE as `τ ↦ sin(2πτ + φ̂)` — i.e., the exact data-generating function, with only the phase predicted. Of course the model evaluated on its analytic solution beats black-box baselines. The abstract ("outperforms the next best model by more than 10×") and the intro lean on this as evidence that WARP has unusually good prior-integration properties, when what Table 3 actually shows is that any model evaluated on its closed-form solution dominates one evaluated as a black box. The headline framing materially overclaims; a misspecified prior (free ω, polynomial expansion, etc.) is needed to claim prior integration as a *capability of WARP*.
- **Internal incoherence between Table 4 numbers and the long-range narrative.** Section 3.3 states "WARP displays impressive potential on extremely long sequences such as EigenWorms and Motor." On EigenWorms (T=17,984), WARP scores 70.93 — below LinOSS (95.0), FACTS (86.7), S6 (85.0), LRU (85.0), S5 (83.9), Log-NCDE (82.8), Griffin (79.5), and NRDE (77.2). WARP is below the median of the table and not in the top three on the dataset the discussion uses to evidence long-range capability. The "top three in 4 of 6" framing is technically correct, but the two it misses (Worms, SCP1) include precisely the flagship long-range case the narrative emphasises. The limitations section (Sec. 4.2) candidly notes weakness on long sequences, which is appreciated, but Sec. 3.3's claim about EigenWorms is not supported by its own table.
- **Modern sequence baselines are absent from the headline tables that aren't UEA.** Table 1 (MNIST/CelebA) compares only against GRU, LSTM, ConvCNP, S4 — no S5, Mamba, LinOSS, LRU, despite the paper benchmarking these elsewhere. Fig. 3(b) (ETT) compares only GRU, LSTM, WARP — no SSM or Transformer baselines, which have been the relevant references on ETT for years. Table 2 (PEMS08) compares only against graph-based baselines (GMAN, D²STGNN, STDCN); no modern non-graph sequence model is included. The PEMS08 sequence is also preprocessed by a non-causal convolution (Sec. 3.1), which is a non-trivial inductive bias. Without including a modern sequence baseline configured identically (and with that convolution), the "reducing MAE by over 50%" claim cannot distinguish WARP's contribution from the preprocessing's contribution. The UEA table demonstrates the authors are capable of modern comparisons; the asymmetry across tables matters because precisely the tables with the strongest headline claims have the weakest baselines.
- **The ICL demonstration tests a property nearly tautological with WARP's algebra.** Section 3.4 transforms the input via cumulative sum so the recurrence-on-differences directly integrates back to the underlying mapping. This converts ICL into "integrate your way to the right θ," which is the algebra of Eq. 1 — and it is a single-class linear-regression demonstration, not the function-class generalisation studied by the ICL literature. The "subsequent queries without re-evaluating the sequence" property holds for any model producing a parametric predictor at the end of the context. Listing in-context learning as a primary contribution in the abstract overstates what Sec. 3.4 establishes.

### Minor
- **"Linear RNN" framing papers over a non-linear-in-state readout.** The recurrence is linear in θ, but `MLP_θ(τ)` is highly non-linear in θ (a polynomial of order equal to the MLP depth times the activations). The parallel-scan efficiency holds for θ_t but not for the decoded y_t, which still requires materialising and unflattening every θ_t. Section 2.2 acknowledges this for the non-AR mode, but the introduction still uses the "linear RNN with restored expressivity" framing as if the trade-off were resolved. Rephrasing the positioning would not change any result, but would make the contribution more honest.
- **CelebA BPD convention needs explanation.** Table 1 reports negative BPD for WARP at L=300, 600 (−0.043, −0.162), which is only possible under a continuous-density treatment without proper dequantisation and is not directly comparable to the discrete-image BPDs other models in the literature report. The LSTM L=100 entry (3869) is either a typo or a numerical pathology. The text claims BPD "best captures" the comparison; the table as printed makes that comparison hard to interpret.
- **Effect of the non-causal convolution on PEMS08 is not isolated.** Sec. 3.1 mentions it but provides no ablation. Without one, the reader cannot tell what fraction of the PEMS08 gain is WARP and what fraction is the preprocessing.
- **$D_θ$ and the structure of $A$ are not specified per experiment.** $A \in \mathbb{R}^{D_θ \times D_θ}$ dominates the parameter budget; with a 1.68M-parameter model, $D_θ$ must be ~10³ for dense $A$. Whether $A$ is dense, block-diagonal, or otherwise structured is critical to interpreting both cost and behaviour. Sec. 4.2 mentions scaling concerns but does not record which experiments used which structure.
- **WARP-Phys is excluded from LV with no clear reason in-text.** Table 3 marks it "X" on Lotka-Volterra. A one-line explanation that LV's analytical form does not admit the same kind of parameter prediction would clarify the scope of WARP-Phys.

### Trivial
- The biological framing in Sec. 4.1 ("STDP") is decorative; STDP is a temporally asymmetric Hebbian rule between spike timings, not a global derivative-driven update. The argument doesn't depend on the analogy.

## Nice-to-Haves
- Ablations that *isolate* the contributions currently bundled together: (i) a standard linear RNN with the same dimensional hidden state and a vanilla non-linear MLP readout on $h_t$ (does the self-decoding structure beat a high-dim linear state + non-linear decoder?); (ii) $\Delta x_t$ vs. $x_t$ to isolate the differencing; (iii) learned $\theta_0$ vs. hypernetwork $\phi(x_0)$. These would let the genuine wins stand on their own.
- A *misspecified* physical prior for WARP-Phys (e.g., $\sin(\omega \tau + \varphi)$ with $\omega$ free, or a polynomial basis) — this would test prior-integration capability rather than the trivial closed-form case.
- A real ICL evaluation in the Garg et al. style: families of function classes with held-out class generalisation, without the cumulative-sum transform.
- Modern non-graph sequence baselines (Mamba, S5, LinOSS) on PEMS08, MNIST/CelebA image completion, and ETT, with the same preprocessing.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *Strength about "consistent empirical validation across multiple modalities" as a standalone strength* — partially kept under "Breadth of empirical sweep," but the breadth is only as good as the baselines; this would have been double-counted with the major weakness about missing baselines.
- *Harsh critic's framing that the "linear RNN" issue is "structural"* — demoted to Minor because the paper does acknowledge the non-linear readout in Sec. 2.2 and the parallel-scan efficiency claim is about θ_t. It's a framing/positioning issue, not a structural defect.
- *Harsh critic's request that Sec. 4.2 acknowledge the Worms result as a limitation* — this is a presentation suggestion already mostly satisfied by Sec. 4.2's "WARP still struggles to achieve SOTA classification performance on extremely long sequences," so the criticism is partly addressed.
- *Strength claiming "first to treat weight-space features as intermediate hidden state representations"* — the paper's own claim, kept implicitly in the novelty point; not separately listed.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observation in the reviews is the harsh critic's point that the WARP-Phys "physics prior" is, in the SINE case, the analytic generating function itself — but this is just a reading of what the paper already says, not an external insight.

## Suggestions
- **Rewrite the abstract and intro to match the experiments.** Move the "10×" claim into the context of "WARP can exploit a known closed-form solution," and make in-context learning a secondary claim until a function-class ICL evaluation is added.
- **Add the missing modern baselines to Tables 1–2 and Fig. 3(b).** The UEA table already shows the authors can run them; doing so on PEMS08/ETT/MNIST/CelebA is the most direct route to a stronger version of this paper.
- **Add a single ablation table that swaps each of $\Delta x_t \to x_t$, $\phi(x_0) \to \theta_0$, MLP-θ readout → MLP-on-h readout.** Without this, the reader cannot attribute the gains to specific design choices.
- **State $D_θ$ and the structure of $A$ explicitly for each experiment** (Sec. 4.2 already commits to discussing structured variants; reporting which one was actually used would not change any result).
- **For PEMS08, ablate the non-causal convolution preprocessing** and report WARP without it, plus a strong sequence baseline with the same preprocessing.
- **Rephrase the EigenWorms discussion in Sec. 3.3** to acknowledge that WARP is not competitive on the longest sequence in the table.
- **Either remove the BPD comparison for CelebA, or specify the dequantisation convention** and recompute under the same convention as the baselines.

## Evaluation against community standards

- **Originality.** High. Weight-space features as the recurrent hidden state, with self-decoding, is a fresh primitive.
- **Importance.** Medium. The motivation (gradient-free adaptation, physical priors, ICL) is timely, but the experiments do not yet show that this primitive *uniquely* enables those properties versus existing alternatives.
- **Whether the claims are well supported.** Mixed. UEA results (Ethanol, Heartbeat) and PEMS08 numbers are real wins by face value; the WARP-Phys headline, the ICL claim, and the EigenWorms long-range claim are over-stated relative to the experiments that justify them.
- **Soundness of experiments.** Mixed. Within-table comparisons are parameter-matched (good), but the choice of baselines varies dramatically across tables, and a key preprocessing step on PEMS08 is not ablated.
- **Clarity.** Generally good — the architecture is clearly presented, the algorithms are described, and the limitations section is candid.
- **Value to the community.** Real but contingent on a rewrite. The architectural primitive is worth knowing about; the current framing makes it hard to know what is doing the work.

## Score and Decision

**Anchors retrieved:**

Round 1:
- `I1484gDBr4.md` (avg 2.50, Reject) — feature-sequence twist LRNN; far weaker than WARP in evaluation breadth and novelty.
- `7eYmijcuqO.md` (avg 3.00, Reject) — RNN dynamics paper; narrow scope, weaker than WARP.
- `2NwHLAffZZ.md` (avg 2.33, Reject) — linearisation theory; not directly comparable.
- `4ymHtDAlBv.md` (avg 2.33, Reject) — text classification RNN; weaker than WARP.
- `52XG8eexal.md` (avg 4.00, Reject) — read in full. SSM-ICL theory paper; weaker scope than WARP but cleaner ICL setup.
- `XZhpS5Imzx.md` (avg 4.00, Reject) — transformer Kalman ICL; comparable in framing/empirical concerns.
- `dCcY2pyNIO.md` (avg 6.25, Accept) — in-context time series predictor; stronger experimental validation than WARP.
- `ryIHtXE9uG.md` (avg 5.60, Reject) — in-context fine-tuning for foundation models; cleaner positioning.
- `GRMfXcAAFh.md` (avg 8.00, Accept, LinOSS) — clearly stronger than WARP; WARP is benchmarked against it.
- `PdaPky8MUn.md` (avg 8.00, Accept) — Never Train from Scratch; clearly stronger than WARP.
- `fU8H4lzkIm.md` (avg 8.00, Accept, PhyMPGN) — clearly stronger, physics-informed with rigorous claims.
- `bH6T0Jjw5y.md` (avg 8.00, Accept) — Markov processes via T-IB; stronger.

Round 2:
- `iP8ig954Uz.md` (avg 5.33, Reject) — read in full. HART hypernetwork weight generation; comparable in novelty/empirical concerns, slightly less framing trouble than WARP.
- `cADpvQgnqg.md` (avg 5.50, Accept) — foundation-model hypernetwork; cleaner claims than WARP.
- `u6vC7KaFel.md` (avg 4.75, Reject) — HyperLoRA; similar in scope but tighter execution.
- `tI3eqOV6Yt.md` (avg 5.00, Reject) — Hyper-UT; comparable novelty, tighter scope.
- `WQy61tS53c.md` (avg 5.50, Reject) — Deep Bayesian Filter; comparable.
- `EAkjVCtRO2.md` (avg 6.00, Reject) — variational quantisation SSM; stronger execution.
- `EGjvMcKrrl.md` (avg 6.00, Reject) — SSM generalisation theory; cleaner theoretical scope.
- `QFgbJOYJSE.md` (avg 5.75, Accept) — SSM dynamic token selection; cleaner theoretical claims.
- `vAuodZOQEZ.md` (avg 6.50, Accept) — Physics-Informed Neural Predictor; *honest* physics-informed claims, stronger.
- `U1DjXQeJRx.md` (avg 6.60, Accept) — Poisson-Dirac NN; clean theoretical contribution.
- `53xxT3LwJB.md` (avg 5.25, Reject) — Koopman residual; cleaner positioning.

**Round-1 bracket:** 4.0–5.5. WARP is clearly stronger than the 2–3 anchors (more novel, broader evaluation) but materially weaker than the 8.0 anchors (the latter are well-positioned, with experimental claims that match their framing).

**Round-2 narrowing:** WARP sits closest to HART (5.33), HyperLoRA (4.75), GD-SSM (4.00), and the Hyper-UT/Deep Bayesian Filter anchors (5.0–5.5). It is more novel than HART and HyperLoRA but has comparable framing/baseline problems; it is clearly weaker than the 6.0+ anchors (variational quantisation, SSM generalisation theory, PINP), which have tighter claims and cleaner empirical setups. Within the (4.0, 5.5) span, WARP lands at the upper-middle — the novelty is real and the UEA result is honest, but the headline framing problems on WARP-Phys, ICL, and the Worms claim are substantive and not just cosmetic.

**Final position:** Between GD-SSM (4.0) and HART (5.33); closer to HART because WARP's empirical breadth is greater, but pulled down by the headline overclaiming. Final score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>