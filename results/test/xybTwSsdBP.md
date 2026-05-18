Now I have all the information needed to produce the final review. Let me synthesize everything carefully.

---

## Summary

This paper proposes OptBatch, an online batch selection method for instruction tuning that combines (i) loss-based stratified sampling to ensure coverage of the data distribution, and (ii) farthest-point sampling in a gradient-derived feature space to maximize inter-sample diversity. The method uses a "Hessian gradient" feature — the lm-head gradient norm divided by the square root of Adam's momentum estimate — as the representation for distance computation. Experiments on three datasets (NetLit, LLaMaQA, WikiMatrix) and two base models (LLaMa-3-8B, ChatGLM-3-6B) show lower loss and competitive downstream metrics compared to Random, Online Hard, CCS, and InfoBatch baselines.

## Strengths

- **Novel combination of stratified sampling and distance maximization for batch diversity.** Prior online selection methods consider either the difficulty/importance axis (e.g., Online Hard, InfoBatch) or the diversity axis (e.g., CCS's stratification, Hong et al.'s orthogonal representativeness), but OptBatch explicitly combines both: stratified loss-based coverage followed by farthest-point sampling within and across strata. This is a sensible design that addresses a genuine gap.

- **Consistent empirical trends across tasks, models, and pruning rates.** OptBatch achieves the lowest loss curves across three diverse datasets (web literature dialogues, QA, multilingual translation) and two model families, at pruning rates from 20% to 90%. The loss improvements are visible across multiple operational regimes, not cherry-picked at a single setting.

- **Downstream evaluation at multiple levels.** Beyond loss, the paper reports BLEU/ROUGE (Tables 1–2), GPT-4 scoring, and human-corrected evaluation (Figure 7). The human evaluation showing OptBatch at 61.8% high-score vs. ~47.5% for baselines on the NetLit role-playing task provides meaningful evidence of practical quality.

- **Ablation on feature representations.** Figure 9 compares embedding, raw gradient norm, and the proposed Hessian gradient features at 70% pruning, showing that the proposed representation achieves the lowest loss. This ablation isolates one design choice and supports the paper's claims about feature effectiveness.

## Weaknesses

### Fatal
None.

### Major

- **The "Hessian gradient" feature is conceptually unsupported and the paper's notation is internally inconsistent.** Section 2.2 correctly defines $\mathbf{v}_t$ as the first moment (momentum) and $\mathbf{s}_t$ as the second moment (variance) in Adam. The bias-corrected forms are $\hat{\mathbf{v}}_t$ and $\hat{\mathbf{s}}_t$. However, Section 3.2 then calls $\hat{\mathbf{v}}_t$ the "second moment estimate" (contradicting Section 2.2) and defines the feature as $H_t = \|\mathbf{g}_t / \sqrt{\hat{\mathbf{v}}_t}\|$ — dividing the lm-head gradient by the square root of the *momentum*, not the second moment. The standard Adam normalization divides by $\sqrt{\hat{\mathbf{s}}_t}$ (RMS of gradient magnitudes), not $\sqrt{\hat{\mathbf{v}}_t}$. There is no justification for this specific formula: dividing by momentum does not approximate a Hessian (which involves second derivatives), and the paper provides no analysis, ablation, or citation showing why this particular scaling is theoretically or empirically beneficial. The term "Hessian gradient" is misleading. This is a structural weakness because the entire selection procedure depends on distances computed in this feature space.

- **The algorithm is too ambiguously described to reproduce.** The number of strata $K$ is never specified. The selection procedure mixes probability-based sampling ("select $|S|$ data according to the probability of $\exp(\mathrm{loss})$") with farthest-point sampling within and across strata — but the exact optimization objective, the number of samples per stratum ($n_i$), and whether the sampling is sequential or joint are not specified. No pseudocode or executable description is provided. Figure 1 gives a high-level workflow but leaves the core combinatorial decision (e.g., how cross-stratum distance constraints are enforced) underspecified. The paper cannot be reproduced or even precisely understood from its current description.

- **The theoretical bound in Section 3.1 is disconnected from the method.** The inequality $\|\nabla l(x,y;h_S')\| \leq r L_s + \sqrt{L^2 \log(1/\gamma) / (2n)}$ is presented without definitions of $r$, $L_s$, $L$, $\gamma$, or $n$, without derivation or citation for this specific bound, and without any connection to the stratified farthest-point sampling algorithm that follows. The bound never appears in the selection rule, loss analysis, or any subsequent argument. It gives the appearance of theoretical grounding without delivering any, and removing it would not affect the rest of the paper.

- **The main empirical claims lack statistical support.** No error bars, confidence intervals, or multiple-seed results are reported for any experiment. Given the known sensitivity of online data selection to initialization, batch ordering, and model checkpoints, single-run results are insufficient to support the headline claims that pruning 20–50% of data *outperforms* full-dataset training (Figure 6, Section 4.2.1) or that OptBatch "consistently achieves optimal loss." The loss differences in the figures appear small in absolute terms, and without variance estimates the reader cannot distinguish systematic improvement from noise. This is especially critical for the claim that a pruned subset outperforms the full dataset, which demands rigorous statistical evidence.

### Minor

- **Downstream evaluation is limited to a single pruning rate (70%).** BLEU/ROUGE (Tables 1–2), GPT-4 scoring, and human evaluation are reported only at 70% pruning. Since the paper's central claims span pruning rates from 20% to 90%, and the loss curves show interesting non-monotonic behavior (loss dips at 50% then rises at 70%), downstream metrics at multiple rates would be necessary to validate that improvements at other rates translate to practical gains. The paper acknowledges this as a limitation but does not address it.

- **The FLOPs analysis likely overstates savings.** The computation in Section 4.4 reduces backward-pass FLOPs by $(1-\alpha)$ but assumes the forward pass is unaffected. In practice, the forward pass for the full batch is still required to compute losses and lm-head gradients for selection, and the selection algorithm itself (gradient computation per sample, distance calculations, farthest-point sampling) adds non-trivial overhead. Wall-clock time or end-to-end training time is not reported, making it difficult to assess actual speedup.

- **No inter-annotator agreement reported for the human evaluation.** The human evaluation (Figure 7b) corrects GPT-4 judgments, which is good practice, but no agreement metric (e.g., Cohen's $\kappa$) is reported, making it hard to judge the reliability of the corrected scores.

### Trivial
None.

## Nice-to-Haves

- Ablation isolating stratification vs. no stratification, and distance maximization vs. random within-stratum selection, would strengthen the attribution of gains to specific components.
- An analysis comparing the loss trajectories of selected vs. discarded samples would substantiate the paper's concept of "learnability."
- Comparison to a simple random-subsample-per-batch baseline would help calibrate the difficulty of the online selection task.

## Removed Points

- **"The Hessian gradient is misnamed"** (reviewer's framing as pure naming issue): Keeping its substance (conceptual unsupportedness, notation inconsistency) in Major, but removing the framing that it is *just* a naming problem. The issue is deeper than naming.
- **Strength Finder's "Theoretical Lipschitz continuity bound"**: Removed because it directly conflicts with the verified weakness that the bound is disconnected, undefined, and adds no substance. A strength cannot be based on something the reviewer correctly identifies as a weakness.
- **Strength Finder's "Hessian-approximated gradient optimization to stabilize batch selection"**: Removed because it conflicts with the verified weakness that this feature representation is conceptually unsupported and the "Hessian" framing is misleading.
- **"Online Hard is a very weak baseline"**: Removed — this is a matter of opinion about baseline selection; the paper's baseline set is defensible for its class.
- **"The paper would benefit from comparing to more recent online selection methods"**: Removed as this is scope-creep and missing-baseline baiting without specific justification that the cited methods are applicable in this setting.
- **"Missing related works"**: Removed per instructions — I cannot independently verify the existence of missing references.
- **Formatting/style nitpicks**: Removed per instructions.

## Novel Insights

The core tension this paper surfaces — and does not fully resolve — is between two competing desiderata in online batch selection: representing the distribution via stratification (coverage) and maximizing informativeness within selections (diversity). Most prior work emphasizes one over the other. The paper's combination of loss-stratified bins with farthest-point sampling in a gradient space is a natural synthesis. However, the unresolved ambiguity in the feature representation (what is being measured by $\|\mathbf{g}_t / \sqrt{\hat{\mathbf{v}}_t}\|$ and why it works) and the absence of any formal or empirical analysis isolating the stratification and distance components separately mean the paper's most interesting design insight — that stratification and farthest-point sampling can be combined — remains under-validated. The non-monotonic loss curves (loss improves from 20% to 50% pruning then degrades) are an intriguing finding that suggests redundancy structure in the data that could be further studied.

## Suggestions

1. **Resolve the notational inconsistency and conceptually justify the feature**, or simplify it. The paper must clarify whether $\hat{\mathbf{v}}_t$ is the first or second moment (the two sections contradict each other), and provide a clear rationale for the proposed normalization. If the formula is indeed $\|\mathbf{g}_t / \sqrt{\hat{\mathbf{v}}_t}\|$, explain why dividing by the momentum is appropriate. Alternatively, consider using the raw gradient norm or the standard Adam-normalized gradient $\|\mathbf{g}_t / \sqrt{\hat{\mathbf{s}}_t}\|$ as a cleaner feature. The "Hessian" label should be dropped unless a genuine connection to second-order information is established.

2. **Provide complete pseudocode or an explicit optimization objective** describing the selection procedure, including the number of strata $K$, the per-stratum allocation $n_i$, and the exact rule for cross-stratum farthest-point selection.

3. **Remove the theoretical bound in Section 3.1** unless it can be properly derived, connected to the algorithm, and cast in terms of well-defined quantities. In its current form it subtracts from rather than adds to the paper.

4. **Run repeated trials (3–5 seeds) with variance reporting** on at least one representative experiment (e.g., NetLit at 50% and 70% pruning) to establish whether the observed differences are systematic. The claim that pruning outperforms full-dataset training specifically demands statistical support.

5. **Report downstream metrics at multiple pruning rates** (e.g., 50%, 70%, 90%) to validate that loss improvements translate to practical gains across the claimed operating range.

## Score and Decision

The paper addresses an important problem with a reasonable architectural idea, but it has several significant structural issues: the core feature representation is poorly justified and contains a notation inconsistency; the algorithm description is too ambiguous to reproduce; the theoretical section is disconnected; and the empirical claims lack statistical support. These are not superficial fixes — they require rewriting the method description, clarifying or redesigning the feature, and obtaining rigorous experimental evidence. The contribution cannot be fairly evaluated in its current form.

**Score: 4.5/10** — A paper with a plausible idea that is insufficiently validated and too ambiguously described to assess. Major revision needed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>