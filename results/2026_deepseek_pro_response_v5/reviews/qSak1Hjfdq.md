Now I have a clear calibration picture. Let me synthesize my final review.

**Bracket assessment:** The paper sits above FLoRA (5.75) and RECAST (5.75) — both PEFT papers with similar conceptual contributions but weaker evaluation scale and clarity. It's comparable to GSA-VLN (6.40) — another VLN task+method paper — but has evaluation rigor gaps (single trial, missing joint baseline) that pull it down slightly. My final score: **6.0**, Accept.

## Summary

This paper formalizes the all-day multi-scenes lifelong VLN (AML-VLN) problem, where agents must sequentially learn across scenes and degraded imaging environments without catastrophic forgetting. The authors propose Tucker Adaptation (TuKA), which lifts LoRA-style adaptation into a 4th-order tensor space using Tucker decomposition to decouple shared navigation skills from scene-specific and environment-specific knowledge. A Decoupled Knowledge Incremental Learning (DKIL) strategy combines EWC, expert consistency, and orthogonal constraints for lifelong learning. The paper also contributes AllDay-Habitat, a benchmark extending Habitat with physically-grounded low-light, scattering, and overexposure degradation models. AllDayWalker achieves 65% average SR across 24 tasks, outperforming the best baseline (~52%) by ~13 percentage points.

## Strengths

- **Novel and well-motivated problem formulation**: AML-VLN formalizes the practically important challenge of VLN agents facing both diverse scenes and diverse imaging conditions while needing to avoid catastrophic forgetting. The multi-hierarchical knowledge decomposition (core skills, scene-specific, environment-specific) in §2 naturally maps to the proposed tensor representation. Figure 6 concretely defines a 24-task benchmark spanning 5 scenes × 4 environments across simulation and real-world data.

- **Technically sound Tucker Adaptation architecture**: The 4th-order tensor formulation with Tucker decomposition (Equation 2) cleanly separates a shared core tensor \(\mathcal{G}\), shared encoder/decoder \((U^1, U^2)\), scene experts \(U^3\), and environment experts \(U^4\). The tensor-to-matrix alignment in Equation 3 — extracting specific expert rows and contracting through the core tensor — correctly resolves the dimension mismatch between higher-order tensors and 2D LLM weight matrices (Qwen2-7B in this case).

- **Compelling empirical results with large margins**: AllDayWalker achieves 65% average SR across 24 tasks, outperforming the best baseline SD-LoRA at ~52% and O-LoRA at ~52% by ~13 percentage points. On forgetting rate (F-SR), AllDayWalker achieves 11% average vs. 18% for SD-LoRA and 23% for O-LoRA. The radar charts in Figure 7 show consistent superiority across SPL, F-SPL, OSR, and F-OSR metrics.

- **Convincing 4th-order vs. 3rd-order ablation**: Figure 8 shows that the 4th-order decoupled representation (separating scene and environment into distinct tensor modes) consistently outperforms the 3rd-order coupled variant across all 20 simulation tasks. This directly validates the paper's central claim that decoupling multi-hierarchical knowledge into separate tensor modes enables stronger representation learning.

- **Well-designed DKIL strategy validated by shared-component ablation**: Table 3 confirms that sharing the core tensor \(\mathcal{G}\) and encoder \(U^2\) is critical (SR drops from 65% to 53% without them), while sharing the decoder \(U^1\) minimally affects performance but reduces storage. The combination of EWC (Equations 4-6), expert consistency (Equation 7), and orthogonal constraints (Equation 8) is well-justified and directly addresses the multi-hierarchical forgetting problem.

- **Comprehensive baseline coverage**: 12 methods spanning Seq-FT, Lwf-LoRA, EWC-LoRA, Dense/Sparse MoLE, MoLA, HydraLoRA, BranchLoRA, O-LoRA, SD-LoRA, FSTTA, and FeedTTA — covering diverse continual learning and test-time adaptation paradigms with reasonable parameter-matching.

- **Principled benchmark extension**: AllDay-Habitat uses physically-grounded imaging degradation models (atmospheric scattering, low-light noise with shot/read noise and CRF, overexposure with sensor saturation) drawn from published computational photography literature with explicit citations.

- **Generalization to unseen scenarios**: Table 5 shows AllDayWalker transfers to 6 completely unseen scene-environment combinations with 55% average SR, outperforming BranchLoRA (40%) and SD-LoRA (39%) by 15-16 percentage points, enabled by CLIP-based expert retrieval (§3.4).

## Weaknesses

### Fatal

None.

### Major

- **Missing joint multi-task training baseline**: The paper never reports results for training one model on all 24 tasks simultaneously. This is the natural upper bound for any continual learning method and calibrates how much performance is lost due to sequential training. Without it, the reader cannot tell whether AllDayWalker's 65% SR is close to the ceiling (e.g., if joint training gets 70%) or still far from it (e.g., if joint training gets 85%). Either outcome substantially changes how the lifelong learning gains should be interpreted. The paper would be significantly strengthened by adding this calibration, which costs a single training run.

- **Results reported from a single task ordering with no variance**: The paper states "the order of tasks is randomized" (Fig. 6 caption) but reports only one set of results across all 24 tasks. In lifelong learning, results are known to be sensitive to task ordering — a classic finding in the continual learning literature. Without results across multiple random seeds or orderings with variance reported, the robustness of the reported ~13pp advantage cannot be assessed. This is a standard expectation in continual learning evaluation and its absence substantially weakens the evidence for the core empirical claims.

### Minor

- **Inflated claim of "real-world deployments"**: The third contribution bullet (line 28) states "additional real-world deployments also validate the superiority of our AllDayWalker." In the paper, the only "real-world" evidence consists of benchmark evaluation on scenes labeled "real-world-1" through "real-world-5" — these are offline evaluations on real-world-captured scenes within the benchmark framework, not physical robot deployments. The phrasing "deployments" implies physical deployment evidence that does not appear in the paper. The paper should rephrase this to accurately reflect the evidence (e.g., "evaluation on real-world-captured scenes").

- **Task-id agnostic tension with expert matching**: The problem formulation (§2) presents task-id agnosticism as a hard constraint at test time and argues against trivial solutions like loading the correct adapter. However, the CLIP-based expert matching mechanism (§3.4) effectively reconstructs task identity from visual features via two-step similarity matching against stored feature banks. The paper should explicitly acknowledge that the expert matching mechanism softens the task-id agnostic constraint rather than presenting it as an absolute constraint.

- **Hyperparameter sensitivity not explored**: The DKIL loss uses four coupled hyperparameters (λ₁=0.2, λ₂=0.2, λ₃=0.1, with λ=0.5 for the task loss, ω=0.95). No ablation or sensitivity analysis is provided for these values. Additionally, the formulation λ=1-(λ₁+λ₂+λ₃) couples the regularization strength to the task loss weight, meaning that increasing any regularization term necessarily decreases the navigation task loss weight — an unusual design choice that warrants discussion.

- **Expert matching accuracy not reported**: The CLIP-based expert selection (§3.4) is part of the inference pipeline. If matching fails for unseen environments (particularly relevant for Table 5's generalization experiments), the wrong experts are selected, degrading navigation performance. The paper does not report matching accuracy or ablate its impact, making it unclear how much of the generalization gains come from better adaptation vs. better expert selection.

- **F-SR negative values undiscussed**: Table 2 shows AllDayWalker achieves F-SR = -3 at T14 and -4 at T20, indicating positive backward transfer — the agent improved on old tasks after learning new ones. This is an interesting phenomenon that could provide insights into TuKA's knowledge sharing but is presented silently without discussion.

### Trivial

- Figure 2 shows identical values for "Step-by-step fine-tune" and "Sequential fine-tune" columns, making the distinction between these two concepts unclear to the reader.

- Table 3 has an apparent duplicate row (rows 3 and 6 are both ✓✓✓ with identical SR=65, SPL=58, etc.), likely a formatting artifact.

- No explicit limitations section is included in the conclusion (§6).

## Nice-to-Haves

- Report and discuss expert matching accuracy to clarify the inference pipeline's reliability, especially for generalization (Table 5).
- Discuss the positive backward transfer indicated by negative F-SR values at T14 and T20.
- Compare TuKA trained with a simpler continual learning strategy (e.g., just EWC) against the full DKIL to isolate gains from the Tucker architecture vs. the full training recipe.
- Clarify whether Figure 2's "Step-by-step" and "Sequential" fine-tune are intended to be distinct concepts or are accidentally identical.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"Why Tucker vs. CP decomposition?"** — The harsh critic asked why Tucker decomposition was chosen over CP decomposition or other tensor factorization methods. This asks the paper to compare against alternative decomposition families, which goes well beyond the paper's scope. The contribution is demonstrating that Tucker decomposition works effectively for this problem, not conducting a survey of tensor factorization methods. Removed.

- **"Two-hierarchical vs. multi-hierarchical distinction is rhetorical"** — The harsh critic claimed the distinction between two-hierarchical (LoRA/MoE) and multi-hierarchical (TuKA) knowledge representation is "not rigorously argued" and "somewhat rhetorical." This is a subjective opinion about argumentation style, not a verifiable weakness. The paper clearly defines what it means by these terms and provides architectural illustrations (Figure 3). Removed.

- **"Synthesized degradations don't correspond to real sensor behavior, undermining 'all-day' framing"** — The harsh critic claimed the paper doesn't validate that synthesized degradations match real sensor behavior. The degradation models are drawn from published computational photography literature (atmospheric scattering model, low-light imaging models with shot/read noise and CRF) with explicit citations to Narasimhan & Nayar (2000), Healey & Kondapudy (2002), and others. This is standard practice in simulation-based VLN research. Removed.

- **Strength: "the problem is important/interesting"** — Generic and not specific to this paper. Removed from final strengths.

- **"21 percentage point gap"** — The harsh critic stated AllDayWalker (65%) beats the next-best method by 21pp. The actual next-best baseline is SD-LoRA at ~52% average SR, yielding a ~13pp gap. The 21pp was incorrectly computed against BranchLoRA (44%), which is not the best baseline. Corrected.

- **"Parameter count comparison must be in main paper" (as a weakness)** — While transparency would be improved by including the parameter comparison table in the main paper, the paper does reference Appendix C for this and describes the rank settings in §5.2 for fair comparison. Moved from Major/Minor to removed as an overstatement; the main paper does describe the rank settings used for matching.

## Novel Insights

None beyond the paper's own contributions. The insight that representing adaptation weights as a higher-order tensor with Tucker decomposition enables decoupled learning of shared and task-specific knowledge along multiple hierarchical axes — and that this translates to substantially lower forgetting rates in lifelong VLN — is the paper's contribution.

## Suggestions

- Add a joint multi-task training baseline (train on all 24 tasks simultaneously) to calibrate the lifelong learning ceiling. This is one training run and would substantially strengthen the paper's claims.
- Run at least 3 random task orderings with mean ± std to demonstrate robustness of the reported gains. Even 3 seeds would allow basic statistical assessment.
- Rephrase "real-world deployments" to "evaluation on real-world-captured scenes" to accurately reflect the evidence.
- Report expert matching accuracy and discuss how matching errors affect generalization performance in Table 5.
- Discuss the negative F-SR values (positive backward transfer) observed at T14 and T20.

## Score and Decision

### Calibration Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Projected Subnetworks Scale Adaptation | WM5G2NWSYC | 2.00 | R1 (strong reject) | Much weaker — unclear method, limited evaluation |
| Interactive Semantic Map for Skill-based VON | Z91rwXnJsw | 2.00 | R1 (strong reject) | Much weaker — limited contribution, unclear novelty |
| LLIT: Continual RL with Language | zEhTnQZB3D | 2.33 | R1 (strong reject) | Much weaker — smaller scale, less rigorous |
| SnapMem: Snapshot-based 3D Scene Memory | mz8unSsSsB | 4.25 | R1 (weak) | Weaker — less novel method, smaller empirical contribution |
| Embodied Instruction Following in Unknown Env | pwKokorglv | 4.00 | R1 (weak) | Weaker — different problem, narrower scope |
| ARL: Continual RL | Q1Hr9dVfDS | 3.00 | R1 (weak) | Much weaker — smaller scale, less comprehensive |
| CA-Nav: Zero-Shot VLN-CE | eWFkMCBySw | 5.00 | R1 (middle-low) | Weaker — limited novelty, low SR (25%), less comprehensive |
| Task-Unaware Lifelong Robot Learning | YR79EyejsG | 5.75 | R1/R2 (middle) | Weaker — less novel method, uncertainty issues, no real-world validation |
| DRAGO: Continual MBRL | UNHU7uO2qM | 6.00 | R1 (middle) | Comparable in score but different domain (MBRL vs VLN) |
| RECAST: Compact Weight Adaptation | J3H8Az3YlB | 5.75 | R2 (middle) | Weaker — small-scale experiments (~21M models), missing forgetting metrics |
| FLoRA: Structural Integrity in PEFT | OALIb8oNfl | 5.75 | R2 (middle) | Weaker — similar Tucker decomposition idea but no LLM-scale experiments, less evaluation rigor |
| GSA-VLN: General Scene Adaptation | 2oKkQTyfz7 | 6.40 | R1/R2 (upper-middle) | Comparable — another VLN task+method paper. Current paper has stronger method novelty but weaker evaluation rigor (single trial, missing joint baseline) |
| DivScene: LVLM Object Navigation | G6DLQ40VVR | 6.25 | R2 (upper-middle) | Comparable score range, benchmark-focused |
| Bootstrapping Language-Guided Nav | OUuhwVsk9Z | 6.50 | R2 (upper-middle) | Slightly stronger — more rigorous evaluation |
| Seamless Adaptation for VPR | TVg6hlfsKa | 7.25 | R2 (strong) | Stronger — more thorough evaluation, clearer contribution |

**Round 1 bracket:** 5.5–7.0. The paper fell between the weak anchors (3.0–4.25) and strong anchors (7.25–8.0), with the most similar anchor GSA-VLN at 6.40.

**Round 2 narrowing:** FLoRA (5.75) and RECAST (5.75) represent the lower bound — the current paper surpasses both in evaluation scale (7B LLM), problem motivation, and baseline comprehensiveness. GSA-VLN (6.40) represents an upper comparison — the current paper matches or exceeds it in method novelty and baseline breadth but falls short in evaluation rigor (single trial, missing joint baseline). The paper is clearly stronger than the 5.75-tier papers but has evaluation gaps that prevent it from reaching 6.5+.

**Final score: 6.0.** This reflects a solid contribution — novel problem formulation, technically elegant method, comprehensive baselines, and strong empirical results — tempered by genuine evaluation gaps (single trial without variance, missing joint multi-task calibration) that weaken confidence in the magnitude of the reported gains. These gaps are addressable in rebuttal.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>