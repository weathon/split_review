Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me write the consolidated review.

## Summary

STRAP proposes a test-time retrieval-augmented policy learning approach that retrieves **sub-trajectories** (rather than full trajectories or individual states) from large offline robot datasets using off-the-shelf vision foundation models (DINOv2/CLIP) and subsequence dynamic time warping (S-DTW). The core insight is that sub-trajectory retrieval enables maximal cross-task data sharing — different tasks often share low-level behaviors even if their high-level goals differ. STRAP is validated on the LIBERO benchmark (10 tasks) and real-world DROID-Kitchen experiments, showing consistent improvements over prior retrieval methods, multi-task training, and its own full-trajectory ablation.

## Strengths

- **Clear performance gains over full-trajectory retrieval (key ablation).** STRAP with sub-trajectory S-DTW outperforms full-trajectory DTW retrieval (D-T) by +4.1% average across 10 LIBERO tasks (line ~167). This is the cleanest comparison isolating the core contribution — sub-trajectory vs. full-trajectory retrieval — and directly supports the paper's thesis.

- **Off-the-shelf foundation models eliminate costly domain-specific training.** Prior methods (BR, FR) require training VAEs on the target dataset. STRAP uses DINOv2 or CLIP without any dataset-specific training (Sec. 4.3). The paper shows DINOv2 features are robust to visual variations across environments (Fig. 13), and the ablation between DINOv2 and CLIP shows only a +0.7% difference (line ~172), demonstrating the method is not brittle to foundation model choice.

- **Comprehensive evaluation across simulation and real-world settings with informative qualitative analysis.** STRAP is evaluated on 10 LIBERO tasks (Table 1) and real-world DROID-Kitchen with a 5000-demonstration prior dataset. Figure 13 provides compelling qualitative evidence that STRAP retrieves semantically relevant sub-trajectories (e.g., drawer-closing motions from tasks with different high-level goals) and ignores irrelevant data — a nontrivial property confirmed through task-distribution visualization.

## Weaknesses

### Major

- **Language-conditioning mismatch between retrieved sub-trajectories and target task is acknowledged but unaddressed.** The paper defines the policy as language-conditioned $\pi_\theta(a|s,l)$ (line 66) and trains on $\mathcal{D}_{\mathrm{target}} \cup \mathcal{D}_{\mathrm{retrieval}}$, where $\mathcal{D}_{\mathrm{retrieval}}$ contains sub-trajectories from $\mathcal{D}_{\mathrm{prior}}$ with *different* language instruction labels than the target task. The paper explicitly notes that retrieved data have "potentially different task instruction labels" (line 72) and even cites Belkhale et al. (2024) on language relabeling (line 32), yet does not relabel, discuss the impact of mismatched language labels, or ablate this design choice. During training, the policy sees the same sub-trajectory-level behavior paired with both the correct target instruction and various unrelated instructions from $\mathcal{D}_{\mathrm{prior}}$. The paper provides no analysis of whether this dilutes language conditioning or whether gains come from visual behavior cloning that effectively ignores language. This does **not** invalidate the results (the key D-T ablation shares the same issue, and the MT baseline also mixes language labels), but it leaves a methodological gap that weakens confidence in how exactly the retrieval benefit operates. The authors should at minimum discuss this issue and ideally provide an ablation with language relabeling or goal-image conditioning.

### Minor

- **Retrieval cost ignores actions and proprioception.** The S-DTW cost matrix uses only visual features from foundation models: $C(i,j) = \|\mathcal{F}(o_i) - \mathcal{F}(o_j)\|_2$ (line 80-84). Actions and proprioceptive states are not incorporated. An ablation (e.g., adding action embeddings or proprioception to the cost) would clarify whether visual similarity alone is sufficient or whether incorporating dynamics information would further improve retrieval quality. This is a natural follow-up the paper does not explore.

- **Segmentation threshold $\epsilon$ is described but not validated.** The velocity-based automatic segmentation (Sec. 4.2, line 74) uses a threshold $\|\dot{x}\| < \epsilon$ with no discussion of how $\epsilon$ is chosen, whether it is tuned per task, or how segmentation quality affects downstream performance. A sensitivity analysis or at least qualitative examples of segment boundaries would strengthen this component, since segmentation quality directly impacts what sub-trajectories are used as queries for retrieval.

- **Best $K$ reported per task without showing equivalent tuning for baselines.** The paper reports results for the "best $K$" per task for STRAP (line 167, Table 1) and provides the full search in Tab. 9, but does not clarify whether baselines received comparable tuning of their retrieval hyperparameters. This asymmetry could slightly favor STRAP. The transparency of providing the full $K$ search mitigates this, but a direct statement about baseline tuning effort would be cleaner.

- **No runtime or computational cost analysis.** The paper claims STRAP "scales to large datasets" (abstract) but reports no retrieval latency or memory measurements. S-DTW against a 4500+ trajectory dataset involves comparing each sub-trajectory query against all trajectories — quantifying wall-clock time and how it scales would strengthen deployment claims.

### Trivial

- None beyond the formatting artifacts from the parser (which are not paper flaws).

## Nice-to-Haves

- An analysis of whether incorporating action information or proprioception into the S-DTW cost matrix changes retrieval quality.
- A study of segmentation sensitivity (varying $\epsilon$ and measuring impact on final task success).
- A runtime/memory scaling plot for retrieval against increasing $\mathcal{D}_{\mathrm{prior}}$ size.
- A comparison against a random sub-trajectory baseline for the distribution analysis in Figure 13.

## Removed Points

- **"Language-conditioning contamination is fatal / undermines the entire method."** — This overstates the severity. The key ablation (STRAP vs. D-T) shares the same language mismatch issue, so the +4.1% gain is properly attributed to sub-trajectory vs. full-trajectory retrieval, not an artifact of labeling. The multi-task baseline (MT) also trains on data with diverse language labels. The concern is real but not fatal; it has been downgraded to Major.

- **"Section 4.5 is omitted; training pipeline is under-specified."** — The parser stripped this section; it exists in the original submission. The paper states it uses transformer-based BC policies (line 22), runs 3 seeds, and will release code. This is a parser artifact, not a paper flaw.

- **"Comparing sub-trajectory retrieval to single-step retrieval (BR, FR) is expected to favor the former."** — This is an observation about the comparison, not a weakness of the paper. The paper includes the clean ablation (D-T: full-trajectory DTW) that properly controls for retrieval granularity. The BR/FR comparisons are standard baselines against prior work.

- **"No variance reported for Table 1."** — The paper states it uses 3 seeds (line 188) and the table is an image in the extracted text. Variance is almost certainly reported in the original.

- **"The paper overstates the contribution by claiming state-of-the-art retrieval methods as baselines."** — BR and FR are published prior work in the same setting. This is standard positioning.

- Various generic statements from the Strength Finder about "addressing important problems" — dropped as lacking specific evidentiary content.

## Novel Insights

The most notable emergent insight from the review process is that STRAP's sub-trajectory retrieval works well *despite* the language label mismatch — which may actually be informative: the method may be effective precisely because the visual foundation model similarity (DINOv2) drives retrieval to behaviorally relevant sub-trajectories regardless of their task-level language labels, and the downstream policy benefits from the action-level supervision even if language conditioning is partially compromised. This suggests that for sub-trajectory-level retrieval, visual behavioral similarity may be a stronger signal than task-level language alignment, a point the paper could lean into more explicitly rather than leaving as an unaddressed concern.

## Suggestions

1. **Address the language-conditioning mismatch directly.** The cleanest fix: relabel all retrieved sub-trajectories with the target language instruction (or use goal-image conditioning instead of language). At minimum, add a discussion of why the mismatch does not harm performance and an ablation comparing with/without language relabeling.
2. **Add an ablation incorporating actions or proprioception into the S-DTW cost** to show whether visual-only retrieval is sufficient or can be improved.
3. **Quantify retrieval runtime and memory** to substantiate scalability claims.
4. **Report segmentation sensitivity** by varying $\epsilon$ and showing the effect on downstream task success.

## Score and Decision

This paper presents a well-motivated core idea (sub-trajectory retrieval via foundation models + S-DTW), supported by a clean key ablation (+4.1% over full-trajectory retrieval) and solid experimental evaluation across simulation and real-world domains. The main weakness is an unaddressed language-conditioning mismatch that leaves a methodological gap, but this does not invalidate the results. The paper is a solid contribution to the retrieval-augmented policy learning literature.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>