## Summary
The paper presents a large empirical re-examination of associative recall (MQAR) and copying as controlled probes to compare Transformers vs modern recurrent/state-space models (SSMs; e.g., Mamba, Hyena). The main claim is that recurrent models’ success is dominated by brittle optimization—especially an extremely narrow “good” learning-rate window—whereas Transformers are comparatively robust, and that this brittleness affects scaling behavior (arguing SSMs prefer width over depth).

## Strengths
- **Clear, direct evidence that LR sensitivity differs sharply across model families on MQAR.** Figure 1 shows Transformers maintaining high accuracy across a broad LR range, while Mamba/Hyena peak sharply only in narrow LR bands (and the plot reports mean + seed variability over 5 seeds). This concretely supports the paper’s core “narrow LR window” observation (Fig. 1 caption and discussion around “crucial confounder”).
- **The LR-instability phenomenon is replicated on a second canonical benchmark (copying).** The copy-task section explicitly mirrors the MQAR story (“Just as with MQAR… Mamba’s success is again confined to a narrow window.”) and Figure 5 shows a wide stable LR region for the Transformer versus a sharp collapse for Mamba (Sec. 5; Fig. 5).
- **Useful architectural ablations and a stabilizing counterexample help nuance “SSMs are brittle.”** Table 2 is explicitly framed as identifying sources of 1-layer Mamba vs Attention differences (“aligning the backbone… ablations”), and Figure 7 shows DeltaNet achieving “Transformer-level robustness” across LR, contrasting with Mamba/Mamba2 (Sec. 7; Fig. 7 + accompanying mechanistic hypothesis).

## Weaknesses

### Fatal
None.

### Major
- **Causal/strong framing (“fundamental mismatch in the loss landscape”; “direct impact on scaling”) is not matched by the level of mechanistic evidence provided in the main text.** The abstract claims the LR brittleness “reveal[s] a fundamental mismatch in the loss landscape” and that brittle optimization “has a direct impact on scaling, causing SSMs to favor width over depth” (Abstract). In the main body, the evidence is primarily performance-vs-LR sweeps and scaling outcome comparisons (Figs. 1, 3, 5; Table 1), plus a qualitative hypothesis for DeltaNet (Sec. 7). This supports *diagnosing sensitivity* but does not, as written, directly measure “loss landscape mismatch” (e.g., conditioning/sharpness proxies) nor cleanly establish that scaling outcomes are *caused by* optimization instability rather than being an empirical correlation under the chosen training recipe.
- **The “width over depth” scaling guidance is presented as generally corrective (“matching parameter counts via increased depth in SSMs is misguided”) but is supported by limited, task-specific evidence.** The paper states: “attempts to provide fair comparisons by matching parameter counts through increased depth in SSMs are misguided” and points to Table 1 (copy task) where “a deeper but narrower Mamba fails… whereas a shallower but wider Mamba with the same parameter count succeeds” (Sec. 5). This is a valuable finding, but as presented it is narrow (one benchmark setup) and is elevated to broad scaling guidance in the abstract and narrative. The paper would be stronger if it more explicitly bounded the claim to these tasks/settings, or if it provided additional controlled depth/width sweeps showing the mechanism (e.g., how the stable LR region shrinks with depth).

### Minor
- **The 1-layer Transformer vs 1-layer SSM comparison risks being over-interpreted as a “capability” statement without emphasizing the compute/recurrence mismatch.** The abstract states “the 1-layer Transformer’s performance on recall does not exceed random guessing” while “well-tuned Mamba… can learn to recall with one layer” (Abstract), and the paper reiterates that in Fig. 3/6 discussion (Sec. 4; Fig. 6 caption). The paper does partially contextualize this by saying the goal is to “decouple… inter-communication between layers” and “isolate… fundamental structure” (Sec. 4), but it still invites an apples-to-oranges reading because “1 layer” in an SSM entails time-unrolled recurrence/state updates. This is not a correctness error, but the interpretation should be tightened to avoid suggesting a clean expressivity dominance.
- **Some key experimental controls appear deferred to appendices, making it harder (from the main paper) to assess whether LR brittleness is robust to standard training-stack variations.** The paper frequently points to appendices for “full details” (e.g., “full details in Appendix A.1”; “Appendix A.6 with deeper networks”; “full table in Appendix A.4”). Given how central the optimization claim is, the main text would benefit from a compact explicit summary of what *else* is held fixed vs swept besides LR (optimizer settings, clipping, schedules) to more clearly ground the interpretation as “architecture learnability” rather than “this recipe is brittle.”

### Trivial
None.

## Nice-to-Haves
- Add at least one **direct quantitative proxy** supporting the “loss landscape/conditioning mismatch” phrasing (e.g., update-to-weight ratios across LRs, gradient norm statistics vs depth, or a simple sharpness/Hessian-trace proxy) to connect LR sensitivity to an identifiable mechanism rather than inference from outcomes.
- When presenting scaling guidance, include a **small additional grid** that reports not only final accuracy but also **how the “successful LR window width” changes with depth vs width**, which would directly support the claimed link between optimization brittleness and scaling preference.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **“The narrow LR window might be an artifact of mismatched optimizers / missing per-parameter-group LRs / clipping / eps/betas, etc.”** Removed as a *major* weakness because the paper does not provide enough on-page evidence that the training stack is unfairly tuned for one family; this concern is plausible in general but (per instructions) is speculative without a concrete mismatch identifiable in the main text.
- **Claims about missing seed variance reporting.** Removed because Figure 1/2/3/7 captions explicitly mention reporting “mean and relative max-min errors using 5 seeds” (e.g., Fig. 1, Fig. 3, Fig. 7), so the paper does address seed variability at least for the main sweeps.

## Novel Insights
The paper’s strongest contribution is not just “SSMs can/can’t do recall,” but the demonstration that *conclusions about expressivity on these probes are highly contingent on optimization sensitivity*, to the point that a coarse LR grid can falsely imply incapability (explicitly argued around Fig. 1 and Fig. 2). However, the paper’s own results also contain an implicit counterpoint: Figure 7 shows an SSM-like design (DeltaNet) that largely eliminates the LR brittleness, suggesting the “brittleness” conclusion is better framed as a property of specific recurrent parameterizations/update rules than of “modern recurrent models” as a whole—this nuance should be elevated to temper the most global abstract claims.

## Suggestions
- Rephrase the most absolute statements (Abstract) from “revealing a fundamental mismatch in the loss landscape” / “direct impact on scaling” to language that matches demonstrated evidence (e.g., “consistent with” / “empirically leads to”), unless additional mechanistic measurements are already present in the full version.
- Expand Table 1-style evidence into a more general depth-vs-width study: for matched parameter budgets, report (i) best accuracy, and (ii) the width of the successful LR interval, as depth/width vary.
- In the 1-layer section, add one paragraph explicitly clarifying that “1 layer” is **not** equalized compute across model classes due to recurrence-in-time, and frame the result as an inductive-bias/training-dynamics observation rather than a clean expressivity comparison.

Do evaluate the paper on these axis using language first.
- **Originality:** Moderate. The benchmarks are established, but the extensive LR-sweep framing as a confounder for “expressivity conclusions” and the large run count is a meaningful angle.
- **Importance:** Moderate-to-high for the community working on SSMs vs Transformers; hyperparameter brittleness and scaling guidance are practically impactful if correctly scoped.
- **Claims support:** Mixed. The empirical LR-sensitivity claim is well supported by figures across two tasks; the stronger “loss landscape mismatch” and “direct causal scaling impact” framing is currently stronger than what is demonstrated in the main text.
- **Soundness of experiments:** Generally solid in showing systematic LR sweeps with 5-seed variability; however, the main text could better summarize the broader training protocol to make architectural conclusions feel less recipe-dependent.
- **Clarity:** Good overall; figures and captions are descriptive. Some interpretive claims could be more carefully bounded.
- **Value to research community:** High if the paper calibrates its strongest claims; the LR-grid confound point is genuinely useful for future benchmarking practice.

## Score and Decision
MY FINAL SCORE: <score>6.5</score>score</score>
MY FINAL DECISION: <decision>Accept</decision>