Now I have enough information to write the final review. Let me verify a few specific claims by checking the paper sections more carefully.## Summary
LoLoRA proposes a hybrid LoRA variant where the down-projection matrix $A$ is updated by a gradient-free local rule (Hebbian/SNL PCA or a local autoencoder loss) during the forward pass, while $B$ is trained with standard backprop. The method inherits LoRA-FA's activation-memory savings while letting $A$ track input statistics online toward the top-$r$ eigensubspace of $\Sigma_{zz}$. A supporting theorem (4.4) characterizes the optimal frozen $A$ under a random-Gaussian-target assumption as any nonsingular transformation of the top-$r$ eigenvectors of the input covariance.

## Strengths
- **Clean theoretical characterization (Theorems 4.4, 4.5).** The paper formalizes the regression problem and proves that, under Assumptions 4.1–4.2, the set of optimal frozen $A$ is exactly the nonsingular transformations of the top-$r$ eigenvectors of $\Sigma_{zz}$, while any full-rank $B$ is optimal. This provides a principled grounding for the previously heuristic EVA-style initialization (Paischer et al., 2024) and motivates the asymmetric treatment of $A$ vs $B$ noted empirically by Zhu et al. (2024).
- **Coherent ablation across local rules (Table 6).** Five local rules (HPCA, HPCA no-mean, HPCA svd-first, AE, SoftHebb) are compared on TinyLlama/Alpaca; rules whose theoretical fixed point is the top-$r$ PCA subspace (HPCA, AE) coincide to ~0.001 perplexity, and SoftHebb (which does not target that subspace) is clearly worse. This is genuine evidence that *convergence to the PCA subspace*, not the specific rule, is what matters.
- **Consistent memory savings reported across three scales.** ~20% reduction on RoBERTa-large (App. D), 13% (30→26 GB) on LLaMA-3.1-8B (Table 3), and 0.5–0.7 GB on LLaVA-7B (Table 4). The activation-memory accounting is internally consistent across model sizes.

## Weaknesses

### Fatal
None. The mismatch between motivation and evidence (below) is severe and undermines the headline claim, but the experiments and theory as written are not invalid.

### Major
- **The central motivation — that *online* local updates beat a one-shot EVA initialization — is contradicted by the paper's own tables.** §3.1 argues LoRA-FA fails because a *random*, static $A$ is a suboptimal feature extractor; §3.2 motivates moving from frozen EVA to LoLoRA because inputs are non-stationary. But Table 3 shows LoRA-FA (EVA) and LoLoRA HPCA tie exactly ($0.829 \pm 0.005$ vs $0.829 \pm 0.004$), Table 4 shows LoLoRA HPCA at 2.93 perplexity vs LoRA-FA (EVA) at 2.92 (LoLoRA slightly *worse*; the §5.3 Summary itself concedes "HPCA updates do not improve EVA-initialized adapters"), and in Table 6 at $r=8$ HPCA (svd-first), HPCA (uniform), AE, and LoRA-FA (EVA) all cluster at 2.535–2.536 within noise. The proposed contribution beyond EVA's static optimum is not demonstrated. — This reframes the contribution from "a better online fine-tuning method" to "a cheaper way to reach EVA's static optimum without a separate PCA pre-pass," which is a much smaller claim than the paper's framing.
- **The conclusion is overclaimed relative to the tables.** §6 states "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." In Tables 1–2 LoLoRA trades wins with LoRA-FA (uniform) within overlapping error bars; Table 3 is a tie with LoRA-FA (EVA); Table 4 has LoLoRA slightly worse than LoRA-FA (EVA). The summary in §5.1 also calls LoLoRA "competitive" while vanilla LoRA wins 6/8 GLUE tasks. The narrative should be adjusted to match the numerical evidence.
- **The theorem characterizes the static optimum that EVA already achieves; it does not justify the online mechanism.** Theorem 4.4 assumes a random isotropic Gaussian target $\Delta W_0$, which removes precisely the structure that makes the fine-tuning target informative. Under that assumption, "use top-$r$ PCA of inputs" follows from a textbook low-rank-sketch argument and matches the static EVA prescription. No theorem in §4 addresses non-stationary inputs, drifting eigenstructure, or tracking error — i.e., the regime the paper invokes to motivate the online step.
- **The motivation–method gap is never measured directly.** The paper argues input statistics drift during fine-tuning, but never reports (a) how the top-$r$ eigenvectors of $\Sigma_{zz}$ move between initialization and convergence, (b) subspace angles between the EVA init and the LoLoRA-tracked subspace, or (c) any setting (e.g., curriculum, domain shift across phases) where a one-shot PCA should fail and online HPCA should win. Without one such measurement, the "online" claim is not substantiated.

### Minor
- **Algorithm 1 interleaves the update on $A$ within the forward pass without discussion.** Steps 1–4 compute $u = A_{\text{old}} z$, then immediately step $A$, then use the precomputed $u$ for $h = Wz + Bu$. So within the same forward pass, layer $\ell$ produces output with $A_{\text{old}}$ but downstream layer $\ell{+}1$ sees a different $A_{\text{old}'}$ that was just updated. The interaction between this update timing and $B$'s gradient (computed against an $A$ that has changed within the step) merits at least a sentence.
- **The memory-savings framing conflates LoRA-FA's savings with LoLoRA's.** The "20% on GLUE / 13% on LLaMA / ~2% on LLaVA" numbers are the LoRA-FA (frozen-$A$) saving; LoLoRA does not improve on them and adds extra optimizer state for the local rule (acknowledged in §6). §5.1 Summary should make this attribution explicit.
- **Assumption 4.1 is stronger than the prose "under certain assumptions" suggests.** Treating $\Delta W_0$ as i.i.d. Gaussian effectively models the fine-tuning target as isotropic noise; a brief discussion of why this is the right idealization (or any sensitivity analysis) would strengthen §4.
- **Significance bolding in Table 3 is borderline.** $0.829 \pm 0.005$ vs $0.826 \pm 0.005$ are within one standard deviation; the bolded distinction probably doesn't survive a paired test.

### Trivial
- None retained beyond formatting artifacts that are parser issues.

## Nice-to-Haves
- Measure the subspace angle between the EVA-initialized $A$ and the LoLoRA-converged $A$ across layers and training steps. This is the single most informative experiment for distinguishing "online tracking matters" from "we converge to the EVA subspace either way."
- Construct a curriculum / domain-shift fine-tuning setting where input statistics deliberately evolve across phases; this is where online tracking *should* beat one-shot PCA and would convert the contribution from incremental to compelling.
- Add a theorem on optimal $A$ under drifting inputs, with a tracking-error bound for HPCA. This would directly motivate LoLoRA's existence beyond EVA.
- Report wall-clock cold-start time including EVA's PCA pre-pass, so the "no PCA pre-pass" benefit can be quantified. Table 4's runtime column hints at this but isn't analyzed.
- Honestly reframe LoLoRA as "an init-free, online alternative to EVA that reaches the same subspace without a pre-pass" — the experiments support that claim cleanly.

## Removed Points
*These points are flagged to be removed, treat them with caution.*
- "LoLoRA does not Pareto-dominate any existing baseline" framed as a *comparison-fairness* problem — kept in essence as the Major weakness about the central claim, but removed as a separate item to avoid double-counting.
- The harsh critic's complaint about §6's conclusion overclaiming was merged into the Major bullet about overclaiming; not duplicated.
- "Standard LoRA wins 6/8 on GLUE so LoLoRA isn't strong on GLUE" — partial removal: vanilla LoRA retains activations, so it does not share LoLoRA's memory profile. Keeping LoRA as a quality reference is fine; demanding LoLoRA beat it would be scope creep.
- Strength Finder's bullet about "comprehensive ablation" was kept but tightened — the ablation is comprehensive, but the fact that HPCA/AE/svd-first/uniform all coincide is just as much evidence *against* the online story as for it.
- Generic "addresses an important problem" framings from the Strength Finder were dropped as superficial.

## Novel Insights
None beyond the paper's own contributions. The most interesting empirical observation — that local rules whose fixed point is the top-$r$ PCA subspace converge to indistinguishable perplexity regardless of starting point — is in Table 6 and is, ironically, the strongest evidence that the *online* aspect of LoLoRA is doing little beyond what EVA's one-shot PCA already achieves.

## Suggestions
- Reframe the contribution honestly: "an init-free, online way to reach the EVA subspace without a separate PCA pre-pass" is supported by the data; "online updates improve over frozen EVA" is not.
- Add subspace-drift measurements (eigenvector angles between init and end-of-training) for at least the LLaMA-8B and LLaVA settings.
- Soften §6's "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" to match the tables: LoLoRA HPCA *matches* LoRA-FA (EVA) in 2/3 setups and is slightly behind in the third.
- In §5.1, separate the memory-saving attribution: state explicitly that LoRA-FA already captures the activation-memory reduction.
- Either prove a theorem about optimal $A$ under non-stationary $\Sigma_{zz}(t)$, or build an experiment where one-shot EVA should fail by construction.
- Discuss the within-step update timing in Algorithm 1 and whether $B$'s gradient flows through the updated or pre-update $A$.

## Evaluation by axis
- **Originality:** Modest. The online local-rule angle is novel relative to EVA/LoRA-FA, but the static optimum it converges to is the same as EVA.
- **Importance of the question:** Reasonable. Memory-efficient PEFT is an active and useful area.
- **Whether claims are well supported:** The central claim that online local updates improve over frozen EVA initialization is *not* supported by the tables. The auxiliary theoretical claim (Theorem 4.4) is supported.
- **Soundness of experiments:** Setup is reasonable (GLUE, MetaMathQA→GSM8K, LLaVA, Alpaca ablations; three seeds reported with std). The mismatch is between what the experiments show and what the paper concludes, not in their construction.
- **Clarity:** Generally clear. Algorithm 1's update timing and the memory attribution between LoRA-FA and LoLoRA are the main clarity issues.
- **Value to the community:** Limited at the moment. As a cleaner theoretical framing of EVA and as a procedural alternative that avoids a PCA pre-pass, it has value; as a method that improves quality, the evidence is absent.

## Calibration

**Round 1 anchors retrieved**
- `igGeaxOiFM.md` (HoLoRA) — avg 3.00, R1 — LoRA variant with weaker support; clearly below this paper.
- `7X65yoKl3Y.md` (ALLoRA) — avg 3.33, R1 — LoRA fixes with theoretical claims; comparable rigor, weaker support.
- `49ti6LOUw5.md` (UnoLoRA) — avg 3.00, R1 — weaker scope.
- `04RLVxDvig.md` (NanoMoE) — avg 3.00, R1 — different topic.
- `DM6Q45HWSk.md` (EVA itself) — avg 4.75, R1 — directly relevant; LoLoRA cites this as its motivation. Read in full: same family of work, but EVA actually shows quality gains across many tasks where LoLoRA mostly ties.
- `iYkhxre0In.md` (PaCA) — avg 6.00, R1 — accepted PEFT paper with clean efficiency gains; clearly stronger than this paper.
- `Hn5eoTunHN.md` (RandLoRA) — avg 6.00, R1 — accepted; stronger empirical story.
- `DLJznSp6X3.md` (ReLoRA) — avg 5.75, R1 — accepted; cleaner motivation/results.
- `TwJrTz9cRS.md`, `Tzh6xAJSll.md`, `E4Fk3YuG56.md`, `d8w0pmvXbZ.md` — avg 8.0–8.5, R1 — far stronger; not comparable.

**Round-1 bracket:** between ~3.0 (clear-rejects with thin LoRA tweaks) and ~5.0 (LoRA variants with mixed signals like EVA itself). Initial bracket [3.5, 5.0].

**Round 2 anchors retrieved**
- `DM6Q45HWSk.md` (EVA) — avg 4.75, R2 — *the* directly comparable paper. EVA shows consistent empirical gains across many tasks; LoLoRA's theoretical work is cleaner, but its empirical contribution over EVA is essentially nil per its own tables. Roughly comparable in scope but weaker in the empirical-progress dimension.
- `8ZPLn3GCDb.md` (Neutral residues) — avg 4.33, R2 — comparable maturity; better-supported claim.
- `hYe0o7mnwM.md` (Lily) — avg 4.75, R2 — comparable in incrementality.
- `SxOrhLuuVz.md` (MoRA) — avg 4.75, R2 — comparable.
- `KxGGZag9gW.md` (EigenLoRA) — avg 5.00, R2 — comparable.
- `NXnNiT0fdp.md` (GLoRA) — avg 4.75, R2 — comparable.
- `udtrtwkvk5.md` (GoLore) — avg 5.25, R2 — stronger theoretical contribution.

**Narrowing logic:** LoLoRA sits *below* the EVA paper because it inherits EVA's prescription and then fails to demonstrate an improvement over it in its own tables; this is a substantive evidential gap that EVA does not have. It sits roughly with HoLoRA/ALLoRA-tier weak-LoRA-tweak papers (3.0–3.5) in terms of net experimental contribution, but its theoretical results (Theorems 4.4 & 4.5) are cleaner than typical for that band. Net: somewhat below EVA's 4.75 anchor, around the 3.5–4.0 region, closer to the lower side because the headline claim is contradicted by the tables.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>