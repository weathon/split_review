- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 5, 8
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes T³-S2S, a training-free triplet tuning approach for sketch-to-scene generation, consisting of prompt balance (replacing keyword embeddings with scaled single-word embeddings), characteristics prominence (using TopK value-matrix indices to amplify feature-map channels), and dense tuning (adapted from Dense Diffusion). The method operates on frozen SDXL+ControlNet and targets multi-instance generation failures — missing small/uncommon objects and instance coupling. The core diagnostic contribution is analyzing cross-attention beyond attention maps, identifying prompt energy imbalance and value matrix homogeneity as root causes.

## Strengths

- **Diagnosis of two underexplored failure modes in cross-attention.** Sections 3.2–3.3 go beyond the standard focus on attention maps and empirically motivate two specific problems: (1) energy (L2 norm) imbalance across prompt tokens, demonstrated with the "houses" example in Figure 2, and (2) homogeneity of value-matrix entries that limits instance distinguishability, demonstrated through TopK amplification experiments in Figures 3–4. This analysis provides a principled rationale for the proposed modules that prior work (e.g., Dense Diffusion) does not offer.

- **Prompt balance is a clean, training-free fix for underrepresented instances.** The module replaces keyword embeddings with isolated single-word embeddings and scales them to match the end-of-text token's energy (Eq. 2–3). This directly addresses the energy imbalance diagnosed in Section 3.2, and Table 1 (reported as an image) shows it improves instance-region CLIP-Score relative to the baseline. The mechanism is simple but well-motivated by the diagnostic evidence.

- **Characteristics prominence operates on the value–feature interaction, not just attention maps.** The technique uses TopK indices from value matrices to construct instance-specific sketch masks, then amplifies corresponding feature-map channels (Eq. 4–6). This is a genuinely different approach from prior attention-map-only methods (Attend-and-Excite, Dense Diffusion) and is grounded in the homogeneity analysis of Section 3.3. The ablation confirms CP provides the largest per-module improvement.

- **Training-free nature is practically appealing.** The method requires no data collection, fine-tuning, or parameter updates — it plugs into frozen SDXL+ControlNet. This makes it directly usable in applications (game design, animation) where copyright restrictions prevent collecting new scene data (acknowledged in Section 1).

- **Ablation study isolates each module's contribution.** Figure 7 (qualitative) and Table 1 (quantitative) show the individual and combined effects of PB, CP, and DT, demonstrating that no single module resolves all failure modes and that the full triplet is needed.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is limited to 20 custom scenes with no statistical rigor.** The paper designs 20 complex sketch scenes (Section 5.1) — too few to draw reliable conclusions about general effectiveness. No confidence intervals, error bars, or significance tests are reported for any metric in Table 1. Several CLIP-Score differences between variants are small (paper describes PB as showing "modest improvement"), and without statistical testing it is impossible to distinguish genuine gains from sampling noise. A larger evaluation (≥100 prompts) or a statistically powered user study with per-item variance reporting is needed to support the paper's central claims.

2. **Only two direct baselines, with an incomplete set of training-free competitors.** The paper compares against Dense Diffusion and T2I-Adapter. Several relevant training-free methods addressing multi-instance or missing-object problems (e.g., Attend-and-Excite, SynGen, Divide-and-Bind) are not included as direct baselines in Table 1. The paper mentions a "transfer" experiment with Attend-and-Excite in the ablation (Section 5.3, line 250, continued in appendix), but the main comparison table lacks these methods. Additionally, Dense Diffusion was designed for SD 1.5; the paper states "we apply it to the SDXL model" (Figure 6 caption) without describing the adaptation procedure — a detail needed to ensure the comparison is fair and reproducible.

3. **Mechanistic validation is incomplete — the paper shows that modules improve output but not that they work by the claimed causal pathways.** The paper identifies "imbalance of prompt energy" and "value homogeneity" as root causes and proposes modules to address them. However:
   - Prompt balance is shown to improve CLIP-Score, but no diagnostic evidence is provided that it *actually equalizes energy* across instance tokens on the test set. The pre/post energy comparison in Figure 2 is for a single example. The improvement could stem from the semantic change of encoding keywords in isolation rather than from energy balancing.
   - Characteristics prominence amplifies feature-map channels based on TopK value indices, but no quantitative analysis shows that it *reduces value homogeneity* (e.g., measuring pairwise cosine similarity of instance-token values before/after, or entropy of value matrix entries).
   - Without such diagnostic experiments, the paper's core narrative — that these specific mechanisms are responsible for the gains — remains correlational rather than causal.

4. **Two of the three modules are not new contributions.** Dense tuning is directly adopted from Dense Diffusion (Kim et al., 2023) with the paper stating "Specific implementation refers to Dense Diffusion" (line 106). Prompt balance, while well-motivated, is a straightforward heuristic (replacing embeddings and scaling to end-of-text energy) that resembles practical prompt-weighting tricks (e.g., "(house:1.5)"). The paper's novelty rests primarily on the characteristics prominence module and the analysis/combination. This is acceptable for a systems paper, but the paper should more clearly scope its novelty.

### Minor

- **Cropping procedure for CLIP-Score is not described in the main text.** The paper evaluates CLIP-Score for instance and background regions by "cropping the corresponding regions" (line 166) but does not specify whether crops come from ground-truth sketch masks, attention maps, or generated-image bounding boxes. Details are deferred to Appendices C and E (stripped by parser). The main paper should give enough information to assess whether the metric is fair — if crops are derived from sketch masks, CP's amplification of sketch regions could create a circular evaluation.

- **User-study reporting is minimal.** The paper reports user-study ratings (Table 1) but gives no standard deviation, number of raters, inter-rater agreement, or per-item breakdown in the main text. This makes it impossible to assess reliability.

- **Hyperparameter analysis is qualitative only.** The sweep of K and β (Figure 8) is shown for a single visual example. No quantitative results (e.g., CLIP-Score across the test set for various K and β values) are reported.

- **Prompt balance does not handle polysemy or duplicate keywords.** The example prompt "a bridge, a bridge" (Figure 6c) would encode both instances with the same isolated embedding — the method has no mechanism to distinguish them. This is a known limitation that should be discussed.

### Trivial
None.

## Nice-to-Haves

- **Expand evaluation to ≥100 prompts** with diverse object types, sizes, and spatial arrangements, drawn from or adapted to an existing multi-instance benchmark (e.g., COCO-based layout tasks with sketch inputs).
- **Add instance-level detection metrics** (e.g., recall of prompt-specified objects using DETR or similar detector) alongside CLIP-Score, to directly measure whether the "risk of missing critical instances" is reduced.
- **Add diagnostic experiments**: show energy variance across instance tokens pre/post prompt balance across the test set; show pairwise cosine similarity or entropy of value-matrix entries pre/post characteristics prominence.
- **Report inference cost** (time and GPU memory) relative to baseline ControlNet, since the method adds runtime computation at each cross-attention layer.
- **Include failure-case analysis** showing representative scenes where T³-S2S still misses instances or introduces artifacts.

## Removed Points

The following criticisms from the reviewers were evaluated against the paper and the specified filtering rules, then removed with justification:

- **"Missing related works (Attend-and-Excite, Divide-and-Bind, SynGen)"** — Removed per instructions: "DO NOT mention missing related works." The paper's related work section cites training-free modulations (Xie et al., 2023; Chen et al., 2024; Lian et al., 2023; Feng et al., 2022) which encompass these methods, and Section 5.3 explicitly mentions a transfer experiment with Attend-and-Excite.

- **"Speculation about cropping creating circular evaluation"** — The harsh critic speculated that if crops are derived from sketch masks, the metric is biased. This is speculative without seeing the appendix (which describes the procedure). The concern is valid in principle but framed as an assumption rather than a verified flaw; demoted to minor, acknowledging the paper defers detail to appendices.

- **"Global CLIP-Score moves from 0.297 to 0.306"** — These specific numbers are not verifiable from the text (Table 1 is an image). The general point about small differences and lack of significance testing is retained as a major weakness; the specific numbers are removed.

- **"SpaCy library — which model?"** — Removed as a nitpick about trivial implementation detail (per instructions: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details").

- **"Reproducibility of Dense Diffusion adaptation"** — The harsh critic's framing as a fatal reproducibility issue is too strong. The paper does acknowledge the adaptation and states it. This is retained but demoted to minor, because the paper could provide more detail but this does not invalidate results.

- **"Does the module improve generation simply because it re-encodes keywords in isolation?"** — This is speculation about an alternative explanation. The concern about missing mechanism validation is valid and retained; the specific alternative hypothesis speculation is removed.

- **Various strength-finder strengths removed** as generic or overstated: "Systematic analysis" is too generous given the single-example nature of the analysis; "custom benchmark" overstates the value of a 20-sample test set. Retained strengths are those concretely supported by the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the evaluation** to at least 100 prompts with a documented sampling strategy. Report CLIP-Score with confidence intervals (bootstrap or per-item variance) and include instance-level detection metrics (e.g., object-detection recall) to directly measure whether missing-instance problems are solved.
2. **Add direct diagnostic experiments** that measure the specific quantities the modules claim to improve — energy variance across instance tokens (for prompt balance) and value-matrix token distinguishability (for characteristics prominence) — with pre/post comparisons across the test set.
3. **Include Attend-and-Excite and SynGen as direct baselines** in the main comparison table. If the method underperforms them on some metrics, report that honestly — the combination of sketch-following + multi-instance handling is the claimed advantage.
4. **Report user-study details** (number of raters, standard deviations, per-item scores) in the main paper.
5. **Discuss the polysemy limitation** of the prompt balance module explicitly, and show how it handles (or fails on) duplicate/similar keywords.
