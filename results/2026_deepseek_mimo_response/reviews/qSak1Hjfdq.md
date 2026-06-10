Now let me write the final review output.

## Summary
This paper formalizes the "all-day multi-scenes lifelong VLN" (AML-VLN) problem and proposes Tucker Adaptation (TuKA), which represents multi-hierarchical navigation knowledge as a 4th-order tensor decomposed via Tucker decomposition to decouple scene-specific and environment-specific knowledge from shared components. A decoupled knowledge incremental learning (DKIL) strategy consolidates shared subspaces while constraining task-specific experts. The method is embedded in a VLN agent (AllDayWalker), evaluated across 24 sequential tasks spanning multiple scenes and imaging environments, and compared against 12 baselines.

## Strengths
- **Novel Tucker decomposition architecture for continual VLN adaptation**: TuKA represents adaptation knowledge as a 4th-order tensor (Eq. 2-3, §3.2), decomposing it into a shared core tensor 𝒢, shared encoder U² and decoder U¹, scene experts U³, and environment experts U⁴. The dimensional alignment trick (Eq. 3) that reduces the tensor to a 2D weight matrix is a genuine technical insight enabling tensor-based multi-factor decomposition within the LoRA framework. Figure 8 validates that 4th-order consistently outperforms 3rd-order across all 20 tasks, confirming that separating scene and environment dimensions provides measurable benefit over treating them as a single coupled expert index.

- **Strong, consistent experimental results across comprehensive baselines**: Table 1 shows AllDayWalker achieves 65% average SR versus 44% for BranchLoRA (next best) across 24 tasks — consistent margins across individual tasks, not driven by outliers. Table 2 shows 11% average forgetting versus 36% (BranchLoRA). Table 3 ablates shared components, showing the core tensor provides the largest SR gain (53%→65%). Table 4 demonstrates stability when scaling from 24 to 30 tasks with negligible degradation.

- **Principled DKIL continual learning strategy with complementary mechanisms**: The DKIL strategy (§3.3) combines EWC regularization on shared subspaces (Eq. 4-6), expert consistency constraints on previously learned experts (Eq. 7), and orthogonal regularization for new expert exploration (Eq. 8), each matched to the tensor structure. The ablation in Table 3 validates each component's contribution.

- **Physics-grounded benchmark (AllDay-Habitat)**: The platform extends Habitat with three degradation models grounded in established imaging physics: atmospheric scattering (Eq. 10), low-light with shot/read noise and CRF (Eq. 11), and overexposure with sensor saturation (Eq. 12). This provides a reproducible, physically motivated benchmark rather than ad-hoc image corruption.

- **Generalization and real-world validation**: Table 5 evaluates 6 entirely unseen scene-environment combinations including 2 real-world scenes, showing AllDayWalker at 55% average SR versus 40% (BranchLoRA) and 39% (SD-LoRA). The inclusion of real-world deployment scenes (G5-G6) strengthens the practical relevance.

## Weaknesses
### Fatal
None

### Major
- **Parameter count transparency gap**: The paper claims "comparable" trainable parameters across methods (line 231) with different rank/expert configurations (LoRA r=6, MoE-LoRA r=16/K=8, TuKA r1=r2=8, r3=64, r4=64, M=7, N=4), but the actual parameter count comparison is deferred to Appendix C. Given the very large performance margins (21+ points over the best baseline), verifying that gains come from the Tucker decomposition architecture rather than from more capacity is essential. Table 3 shows that the ablated TuKA (no shared components, SR=53%) still outperforms most baselines, which could indicate the Tucker structure is effective but also raises questions about whether the parameter budgets are genuinely matched. This is the single most important missing piece for the main paper.

### Minor
- **Generalization evaluation scope is limited**: Table 5 tests only 6 unseen tasks and compares against only 3 of the 12 baselines (StreamVLN, BranchLoRA, SD-LoRA). Stronger baselines like O-LoRA or HydraLoRA should be included for a more complete generalization picture.
- **No variance or error bars reported**: With 24 sequential tasks and "randomized" ordering, results could be sensitive to order. The large margins suggest robustness, but reporting variance across multiple orderings/seeds would strengthen credibility.
- **"Multi-hierarchical" framing slightly overclaims relative to what is decoupled**: The method factors two dimensions (scene + environment) plus shared components. While the Tucker decomposition is mathematically sound and the 3rd-vs-4th order ablation validates separating these two factors, the framing implies more general multi-factor capability than demonstrated. The contribution is better understood as a principled two-factor tensor decomposition.
- **Capability limitations not discussed**: The method cannot handle truly novel scenes or environments — only novel combinations of previously seen scene and environment experts (since expert search in §3.4 retrieves stored experts by cosine similarity). The paper should explicitly state this boundary. The Tucker decomposition also introduces hyperparameters (r1-r4, M, N) that must be set per configuration.

### Trivial
None

## Nice-to-Haves
- Analysis of what the learned experts actually capture (e.g., do U³ rows cluster by scene? do U⁴ rows cluster by environment?) would substantiate the "decoupled knowledge" claim beyond end-to-end metrics.
- Analysis of CLIP's retrieval accuracy for scene vs. environment expert matching, and ablation of the expert search mechanism (e.g., random assignment baseline).
- Discussion of the negative forgetting rates in Table 2 (T14: -3%, T20: -4%) which indicate positive forward transfer.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh critic's claim about Table 1 formatting inconsistencies** (missing Avg values for EWC-LoRA, O-LoRA, SD-LoRA, FeedTTA) — these are parser artifacts, not paper problems.
- **Harsh critic's point about the non-overlap constraint being "artificial"** — this is a design choice for the benchmark that the paper explicitly states as part of the problem definition (line 36).
- **Strength Finder's claim about "fair parameter-budget comparisons"** — this conflicts with the verified Major weakness about parameter count transparency being deferred to appendix. The paper states comparability but doesn't demonstrate it in the main text.
- **Harsh critic's speculation about CLIP's ability to distinguish environments** — while reasonable as a concern, the paper shows results that work in practice (Table 5), making this more of a nice-to-have analysis than a demonstrated failure.

## Novel Insights
The paper makes a genuinely novel observation that Tucker decomposition can align higher-order tensor representations with the 2-dimensional weight matrices of LLM adapters, by selecting specific rows from expert factor matrices (Eq. 3). This dimensional alignment trick — reducing a 4th-order tensor to a 2D matrix via row selection on the 3rd and 4th mode factors — is the key technical insight enabling tensor-based multi-factor decomposition within the LoRA framework, distinguishing this work from prior MoE-LoRA approaches that are limited to 2-level shared-specific hierarchies.

## Suggestions
- Move the parameter count comparison table from Appendix C to the main paper to directly address the most significant concern about comparison fairness.
- Add the missing baselines (O-LoRA, HydraLoRA, etc.) to Table 5's generalization evaluation.
- Add a brief discussion of limitations: the method's inability to handle truly novel scenes/environments and the sensitivity of Tucker hyperparameters.
- Report variance across at least 2-3 random task orderings for the main results.

## Score and Decision

**Calibration anchors:**

All anchors retrieved across rounds:

**Round 1:**
- JIlIYIHMuv (LVLM-CL): 2.50 — continual LVLMs, rejected, much weaker contribution
- TxIrMD6lAN (Task-Specific Adapters): 3.00 — incremental learning, rejected, weaker
- HCCkCjClO0 (Online Weight Approximation): 3.00 — continual learning, rejected, simpler
- WM5G2NWSYC (Projected Subnetworks): 2.00 — adaptation, rejected, much weaker
- gc8QAQfXv6 (Function Vectors for CF): 3.00 (reporting 9.00 internally) — mismatched anchor
- 2oKkQTyfz7 (GSA-VLN): 6.40 — VLN scene adaptation, accept, our paper is better (harder problem, stronger results)
- eWFkMCBySw (Constraint-Aware Navigator): 5.00 — zero-shot VLN-CE, rejected, different problem
- rwmwFnmjAX (Continual LLaVA): 4.75 — continual LVLM, rejected, weaker method
- sb7qHFYwBc (C-CLIP): 6.50 — multimodal continual CLIP, accept, simpler method, our paper is better
- uWvKBCYh4S (Mixture of LoRA Experts): 5.00 — LoRA fusion, accept, less comprehensive
- LWvgajBmNH (MORE): 4.00 — multi-task PEFT, rejected, less sophisticated
- uHTmx0nRfX (MoTE): 4.75 — task experts, rejected, less relevant
- U3UtvOYMiw (Seeded LoRA): 5.00 — collaborative fine-tuning, rejected
- Y6aHdDNQYD (MOS): 8.00 — test-time adaptation, accept, different domain
- TPZRq4FALB (READ): 8.00 — multi-modal TTA, accept, different domain
- TwJrTz9cRS (HiRA): 8.00 — Hadamard PEFT, accept, cleaner contribution, above our paper
- 5t57omGVMw (Learning to Relax): 8.00 — solver parameters, accept, different domain
- 7gUrYE50Rb (EQA-MX): 8.00 — embodied QA, accept, different domain
- Q6a9W6kzv5 (PhysBench): 8.00 — VLM physical understanding, accept, different domain
- 9Cu8MRmhq2 (Norton): 8.00 — video-language, accept, different domain
- OI3RoHoWAN (GenSim): 8.00 — robotic simulation, accept, different domain

**Round 2:**
- 88hh5GtLBJ (MetaAdapter): 5.40 — few-shot class IL, rejected, weaker
- L1FeTLOwzr (DAM): 5.25 — continual Video QA, rejected, weaker
- rkAqvDnnmO (SimE): 5.25 — VLM adapter IL, rejected, weaker
- E5YmIBvOqV (Filter Subspace): 6.00 — conv model tuning, accept, less relevant
- OALIb8oNfl (FLoRA): 5.75 — Tucker-based PEFT, accept, very relevant but weaker results; our paper is clearly better
- pAVJKp3Dvn (Generalized Structured Matrices): 5.67 — structured matrices, accept, different focus
- 5M0ic2RxQZ (dEBORA): 6.67 — bilevel LoRA rank, accept, comparable quality
- G6DLQ40VVR (DivScene): 6.25 — object navigation benchmark, rejected, less method innovation
- n6mLhaBahJ (HAZARD): 6.75 — embodied benchmark, accept, comparable benchmark contribution
- kC5nZDU5zf (Selective Visual Representations): 7.50 — embodied AI visual, accept, above our paper

**Bracketing:** Round 1 placed the paper between 5.5–7.5. Round 2 narrowed to 6.5–7.5.

**Positioning:** The paper is clearly above the 6.5 anchors (C-CLIP, GSA-VLN, dEBORA) due to stronger empirical results and a more complete contribution (method + agent + benchmark + DKIL). It sits below 7.5 (Selective Visual Representations, HiRA) primarily due to the parameter transparency gap and limited generalization analysis. The FLoRA anchor (5.75) is particularly relevant as it also uses Tucker decomposition for PEFT but with weaker results and novelty concerns — our paper is substantially better.

**Final score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>