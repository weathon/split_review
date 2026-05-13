## Summary
The paper identifies the "edge-of-reach problem" in offline model-based RL: states reachable only at the final step of bounded-horizon rollouts appear as Bellman targets but never as Bellman inputs, leading to pathological value overestimation analogous to the out-of-sample problem in model-free RL. It supports this with a surprising oracle-dynamics failure on D4RL, a controlled toy environment whose 0.4% value-patching experiment cleanly isolates edge-of-reach states as the cause, and an algorithm (RAVL = MBPO rollouts + EDAC critic) that matches state-of-the-art on D4RL MuJoCo without any dynamics penalty.

## Strengths
- **Clean causal evidence in the toy environment.** SAC-OraclePatch (Sec. 5.3, Fig. 2) corrects values at only 0.4% of states — those provably edge-of-reach — and fully resolves the failure. This is unusually direct causal evidence for the proposed mechanism rather than a correlational story.
- **Surprising and pedagogically useful oracle-dynamics result (Table 1).** Even with proper caveats (see Weaknesses), the demonstration that replacing learned dynamics with true dynamics in MOPO causes collapse on most MuJoCo datasets is a striking and informative finding that motivates rethinking the field's dominant narrative.
- **Conceptual reframing that unifies two subfields.** Recasting the model-based pathology as a *state-side* analogue of the model-free out-of-sample problem is a clarifying perspective that suggests porting model-free pessimism tools (EDAC) into model-based pipelines.
- **Competitive empirical result without dynamics penalization (Table 2).** Matching MOBILE on D4RL MuJoCo using only EDAC's critic over MBPO rollouts is a useful negative result for the field: dynamics-uncertainty penalties may be doing less work than assumed.
- **Mechanistic check on the toy (Fig. 3).** Ensemble variance is empirically elevated at edge-of-reach states, confirming RAVL's penalty targets the intended set in a setting where that set is exactly definable.

## Weaknesses

### Fatal
None.

### Major
- **The "all existing methods fail" claim from Table 1 is supported only by MOPO.** Under oracle dynamics, MOPO's ensemble-disagreement penalty is identically zero, so Table 1's "Oracle" column effectively reduces MOPO to MBPO+SAC. The paper claims the result generalizes because "other dynamics penalty-based offline model-based RL algorithms share the same base MBPO optimizer," but this glosses over methods whose mechanisms do not vanish under oracle dynamics (e.g., RAMBO's adversarial model update, COMBO's value-side conservatism). The headline framing — that the field has misunderstood the problem — should be supported by re-running the oracle experiment on at least one non-MOPO-style method. As written, this is overclaim relative to evidence.
- **Algorithmic novelty is thin and not ablated.** RAVL = MBPO rollouts + EDAC update (Eq. 3 is EDAC's update). Table 2 shows it matches but does not exceed MOBILE, and only improves on EDAC on a subset of tasks. There is no ablation isolating (a) MBPO rollouts vs. (b) the EDAC min-ensemble critic vs. (c) EDAC's diversity regularizer, nor a sensitivity study over $N_{\text{critic}}$. Given the conceptual claim that "edge-of-reach is the central issue," readers cannot tell whether D4RL gains over EDAC come from addressing edge-of-reach specifically or from incidental hyperparameter retuning.
- **The mechanistic verification (Fig. 3) is shown only on the toy; D4RL has no analogous diagnostic.** The paper's central claim is that RAVL's ensemble variance is elevated at edge-of-reach states. Demonstrating this on the toy is appropriate as proof of concept, but the absence of any D4RL-side diagnostic (e.g., variance at terminal-rollout states vs. interior states; Q-value trajectories on D4RL for MOPO-oracle/MBPO/EDAC/RAVL) leaves a gap between conceptual narrative and benchmark gains.

### Minor
- **Edge-of-reach vs. out-of-sample is more a re-coordinate than a new phenomenon.** The paper acknowledges (Sec. 4.2 end) the close relation, and Proposition 1 is explicitly "analogous to Kumar et al. (2019)" — i.e., the standard $\gamma^{k-t}$ propagation bound. The reframing has pedagogical value, but the paper offers no diagnostic that empirically separates "edge-of-reach overestimation" from generic OOD overestimation on D4RL, which weakens the claim of identifying a *new* problem rather than relabeling a known one.
- **The reinterpretation of prior methods (Sec. 7.3, Fig. 6) is correlational.** A positive correlation between dynamics-uncertainty and Q-ensemble-variance penalties is consistent with the "accidentally addresses edge-of-reach" hypothesis but equally consistent with both penalties simply tracking distance from $\mathcal{D}_{\text{offline}}$. A counterfactual (e.g., MOPO + RAVL ensemble layered in; MOPO with a uniform vs. real penalty) would strengthen this argument.
- **D4RL MuJoCo locomotion is increasingly saturated.** Evaluating only on MuJoCo v2 leaves the conceptual contribution untested on tasks with stitching or exploration structure (AntMaze, Adroit), where the edge-of-reach intuition could either shine or fail more clearly.
- **The $\epsilon$-relaxation of Def. 1 is unspecified.** For stochastic Gaussian dynamics models, every $s'$ has positive density, so $\epsilon$ entirely determines the partition and is not chosen or analyzed.

### Trivial
- Table 3 (per-step rewards) supports short-horizon model accuracy but does not directly bear on Q-value blow-up; the conclusion that "model exploitation is not the main issue" would be more cleanly supported by comparing Q-values rather than rewards.

## Nice-to-Haves
- Combine RAVL with a dynamics penalty on a noisier or stochastic benchmark to validate the paper's orthogonality claim (mentioned as future work).
- Q-value trajectory plots on D4RL for MOPO-oracle, MBPO, EDAC, and RAVL.
- An oracle-dynamics evaluation of at least one non-MOPO-family method (RAMBO or COMBO) to back up the field-wide claim.

## Removed Points
*These points are flagged to be removed, treat them with caution.*
- **(Harsh) "Methods like MOBILE, RAMBO, COMBO would behave differently."** Kept in slightly different form: the point about MOBILE specifically is partly handled by the paper noting MBPO is the shared base; the criticism is folded into the Major weakness about the field-wide claim rather than removed wholesale.
- **(Harsh) "Strawman that toy patching at 0.4% of states actually weakens the model-based interpretation because any aggressive minimum-over-ensemble would also address it."** This is speculative and not clearly correct — the paper's point is that *only edge-of-reach states need correction*, which is itself the strong finding. Removed as inflated.
- **(Harsh) "Proposition 1 implies novelty but is textbook."** The paper itself states it is analogous to Kumar et al. (2019); the critique is half-acknowledged in the text. Downgraded to the Minor section.
- **(Strength Finder) "Formal definition and error propagation bound" framed as a core strength.** Filtered: Proposition 1 is acknowledged by the authors as analogous to existing results, so it is supporting framing rather than a genuine theoretical contribution. Not retained as a standalone strength.
- **(Strength Finder) Generic "unification" claim.** Kept only insofar as it ties to the concrete EDAC-into-MBPO design; the abstract unification framing alone is not a strength.

## Novel Insights
The genuinely novel synthesis is the observation that the model-free out-of-sample problem persists in model-based offline RL in a state-side form — i.e., terminal-rollout states are Bellman targets that are never Bellman inputs — together with the empirical demonstration (oracle dynamics + 0.4% patching) that this state-side gap, not model error, drives the dominant pathology in oracle settings. The reinterpretation that dynamics-uncertainty penalties succeed by incidentally correlating with edge-of-reach variance is a useful, if correlational, contribution. Beyond these the reviews do not produce insights beyond the paper's own.

## Suggestions
- Re-run Table 1's Oracle protocol on at least one method whose mechanism does not vanish under perfect dynamics (RAMBO, COMBO, or MOBILE evaluated with its full update under true dynamics) to substantiate the field-wide claim.
- Add ablations on D4RL: (a) EDAC with no rollouts, (b) MBPO + clipped double-Q only, (c) sweep $N_{\text{critic}}$ and the EDAC diversity coefficient — these are needed to attribute gains to addressing edge-of-reach rather than to retuned EDAC.
- Provide a D4RL-side diagnostic: ensemble-variance histogram split by "terminal-rollout state" vs. "interior" (approximating edge-of-reach), and Q-value trajectories over training across MOPO-oracle, MBPO, EDAC, RAVL.
- Evaluate on AntMaze and/or Adroit to test whether the framing generalizes beyond saturated locomotion.
- Soften the abstract/intro claim from "existing algorithms completely fail" to specify "dynamics-uncertainty-penalty methods built on MBPO."

## Axes
- **Originality:** Moderate. The reframing is clean and pedagogically useful; the underlying phenomenon is closely related to known OOD overestimation.
- **Importance:** Reasonable. If correct, it redirects attention from dynamics-error mitigation to value-side pessimism — a constructive shift.
- **Claims well-supported:** Partially. The toy story is rigorous; the field-wide claim and benchmark mechanism story are not fully supported.
- **Soundness of experiments:** Adequate for D4RL MuJoCo, but missing ablations and harder benchmarks.
- **Clarity:** Strong. The narrative arc (surprising failure → hypothesis → toy verification → scaled method) is well executed.
- **Value to the community:** Real. The conceptual reframing plus the negative result that explicit dynamics penalties are not needed to match MOBILE are useful contributions.

## Score and Decision

Anchor comparison:
- `OATPSB5JK1.md` — *Lower Expectile Q-Learning for Model-Based Offline RL*, avg **6.00**: very similar territory (low-bias value estimation for model rollouts); accepted with solid empirical results. The paper under review is comparable in conceptual clarity but weaker in empirical breadth (locomotion-only; matches but doesn't exceed SOTA).
- `7zY781bMDO.md` — *Free from Bellman Completeness*, avg **6.00**: conceptually-driven offline RL paper with clean reframing and reasonable experiments; accepted. Comparable to the paper under review in spirit.
- `3w6xuXDOdY.md` — *Generalization Gap in Offline RL*, avg **6.50**: benchmark/empirical-insight paper, accepted; the paper under review is somewhat narrower in scope but more mechanistically pointed.
- `lWe3GBRem8.md` — *Offline RL for Online RL*, avg **6.00**: insight-paper format, mixed reception; comparable balance of strengths/limitations to this paper.
- `M992mjgKzI.md` — *OGBench*, avg **7.00**: benchmark paper, larger contribution than this paper.
- `fo5IUCMoFg.md` — *Offline vs Online Learning in MBRL*, avg **4.25**: similar empirical-insight framing but received as too shallow; the paper under review is stronger conceptually and methodologically.
- `0YxvqG9SsJ.md` — *Offline Model-Based Skill Stitching*, avg **3.67**: weaker baseline of comparison.
- `fWx1CKgPCc.md` / `UoYxPYMUWd.md` / `P895PSh41Z.md` — offline RL papers around **4.0–4.5**: weaker contributions than this paper.
- `Aj1wftldeR.md` — *D5RL*, avg **4.75**: scope/empirical critique outcome.
- `kHfIuagAq6.md` / `R6klub5OXr.md` / `Tk1VQDadfL.md` — RL empirical/conceptual studies; range 4.0–7.0, not closely analogous.

The paper sits closest to the 6.0-band anchors (LEQ, Free-from-Bellman-Completeness): solid conceptual contribution + competitive (not winning) empirical results, with real but non-fatal critiques (overclaim of generality, thin ablations, locomotion-only). Slightly above the 5.0 band because the SAC-OraclePatch causal experiment is unusually clean and the reframing is genuinely useful.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>