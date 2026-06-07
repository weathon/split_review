Now I have a solid calibration. Let me finalize the review.

**Round 1 bracket:** 5.5–7.0. IRIS is above the 5.40 (self-correction convergence, rejected) and 6.00 (LM self-improvement, limited novelty), but below Motif (7.25).

**Round 2 narrowing:** IRIS is stronger than FiSAO (6.20 — self-alignment for VLMs, clarity issues) and comparable to RLCF (6.67 — test-time adaptation, somewhat incremental). IRIS has a more novel core insight than both but has the ablation validation gap and framing issues. **Final score: 6.5.**

---

## Summary
This paper proposes IRIS, a reinforcement learning framework that trains autoregressive text-to-image models using only an intrinsic reward — negative self-certainty (NSC), defined as -KL(uniform || π). The key motivating observation is that unlike text reasoning tasks where maximizing self-certainty helps, T2I generation benefits from minimizing it because high-confidence models collapse to simplistic images. IRIS applies GRPO with token-level NSC rewards on both text and image tokens. Across GenEval, T2I-CompBench, and WISE, IRIS achieves near-parity with the external-reward baseline T2I-R1 while using zero external supervision.

## Strengths
- **Genuinely novel observation about modality-dependent self-certainty**: The finding that minimizing self-certainty helps T2I while maximizing it helps text reasoning (Fig. 1 qualitative, Fig. 2 quantitative) challenges prevailing assumptions from the LLM intrinsic-reward literature (Zhao et al., 2025b; Zhang et al., 2025a) and provides a clear, testable motivation for the method.
- **Comprehensive ablation suite isolating each design choice**: Section 4.3 systematically validates the key decisions — semantic CoTs (Fig. 5), minimizing image SC (Fig. 6), minimizing text SC (Fig. 7), forward KL over backward KL (Fig. 8), and RL over direct optimization (Fig. 9). The direct optimization collapse (Fig. 9) is a practically important finding that justifies the GRPO framework.
- **Competitive results without external supervision**: Table 1 shows IRIS achieving near-parity with T2I-R1 (which uses four external reward models: HPSv2, DINO, GIT, ORM) across three benchmarks. On the 1B model, IRIS reaches 0.72 vs 0.75 (GenEval), 0.3793 vs 0.3820 (T2I-CompBench), and 0.37 vs 0.38 (WISE). This is a meaningful result given the practical difficulty of building reward models.
- **Nuanced breakdown of where intrinsic vs. external rewards excel**: The analysis in Section 4.2 shows IRIS outperforms T2I-R1 on knowledge-intensive categories (natural science in WISE) where external reward models lack domain knowledge, while T2I-R1 leads on aesthetics/spatial tasks — a sensible pattern that strengthens the case for intrinsic rewards' generality.
- **Careful experimental practice**: Identification and correction of a chat-template bug in prior work's T2I-R1 baseline (line 120) demonstrates attention to experimental detail.

## Weaknesses

### Fatal
None.

### Major
- **Ablation design choices validated on reward-model scores, not downstream benchmarks**: The four design decisions that define IRIS — minimizing NSC on both text and image tokens (Figs. 6–7), forward vs. backward KL (Fig. 8), RL vs. direct optimization (Fig. 9), and semantic CoT usage (Fig. 5) — are evaluated exclusively against the four reward model scores (HPSv2, DINO, GIT, ORM). These are the same models used to train T2I-R1; while they are unbiased for IRIS (IRIS never sees them during training), they are not the downstream benchmarks (GenEval, T2I-CompBench, WISE) on which the paper's headline claims rest. The main results in Table 1 are independently reported on the actual benchmarks, so the core contribution stands, but the reader cannot assess whether the reported IRIS configuration is genuinely optimal or whether some conclusions are artifacts of the specific reward models chosen as validation proxies. Validating at least the most salient ablations (e.g., image-SC-only vs. both-token NSC) on the downstream benchmarks would close this gap.

### Minor
- **Abstract claim of "superior to external rewards" is not supported by best-checkpoint results**: The abstract states IRIS achieves performance "competitive with or superior to external rewards." Table 1 shows that across all six model-benchmark combinations (1B and 7B on GenEval, T2I-CompBench, WISE), IRIS is consistently slightly below T2I-R1 on overall metrics. IRIS does win on individual subcategories (e.g., Position on GenEval-1B: 0.66 vs 0.64, Colors: 0.88 vs 0.86), and training curves in Fig. 3 show IRIS above T2I-R1 transiently during training. But the standard comparison — best checkpoint to best checkpoint — never favors IRIS on the aggregate. The honest story (near-parity with zero external supervision) is already strong and needs no inflation.
- **Motivating observation (Fig. 2) is correlational but presented with causal framing**: The paper's narrative is that external-reward training decreases image self-certainty, therefore minimizing SC is a good intrinsic reward. Fig. 2 shows a correlation — external-reward training could decrease SC as a downstream consequence of learning, not because low SC is the causal driver. The method works empirically either way, but the paper repeatedly invokes causal language (e.g., "less self-confident multimodal LLMs will generate images with higher rewards," line 32). Treating the observation as motivation rather than mechanism would strengthen the argument.
- **Fig. 2 confounds model, task, and modality**: The motivating experiment compares Qwen2.5-1.5B on math reasoning (text SC) against Janus-Pro-1B on T2I (image SC). These differ in model architecture, task domain, and modality simultaneously, so attributing divergent SC trends to modality alone is over-interpretation. A within-model comparison would isolate the modality effect more cleanly.
- **Error bar provenance unclear**: Table 1 reports error bars, but the paper does not specify whether they reflect multiple evaluations of a single trained checkpoint, multiple training seeds, or both. For a method making comparative claims, knowing whether the IRIS–T2I-R1 gap is stable across training runs matters.

### Trivial
- **Training dataset not specified in main text**: Section 4.1 says IRIS "follow[s] the protocol in T2I-R1" but does not name the prompt dataset or its size. A single sentence would suffice.
- **Training limited to 800 steps**: The learning curves in Fig. 3 suggest IRIS may still be improving on some benchmarks at step 800. Reporting longer training runs would clarify whether IRIS plateaus below T2I-R1 or catches up.

## Nice-to-Haves
- Validate key ablations on GenEval/T2I-CompBench/WISE rather than only on reward-model scores.
- Run a within-model text-vs-image SC comparison during T2I training to clean up the Fig. 2 motivating experiment.
- Report whether error bars come from multiple seeds or multiple evaluations of the same checkpoint.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "maximizing self-uncertainty" vs "minimizing self-certainty" formulation is imprecise** — REMOVED. These are mathematically equivalent given the definitions in Eq. 2 (NSC = -SC), so the rhetorical choice is not a substantive weakness.
- **Harsh Critic: the "maximize image SC" ablation showing collapse is "unsurprising" and "a sanity check, not a discovery"** — REMOVED. This is a judgment about novelty, not a weakness of the paper. Including sanity checks is good practice.
- **Strength Finder: "the paper addressed an important problem"** — REMOVED as generic/superficial.
- **Harsh Critic: the explanation for why RL outperforms direct optimization ("GRPO employs a more conservative strategy") is "post-hoc"** — REMOVED. The paper is transparent that this is an interpretation, and the empirical result stands on its own merits regardless of whether the explanation is fully mechanistic.
- **Harsh Critic: text SC tension not fully reconciled** — REMOVED. The paper explicitly acknowledges this tension (line 104–105) and offers a plausible speculation. This is honest self-assessment, not a weakness.

## Novel Insights
The review process surfaced an important methodological point that the paper itself does not emphasize: the ablation studies that define IRIS's configuration are validated on a different metric set than the main results. This creates a "validation gap" that is common in RL-for-generation papers but rarely discussed openly. Making this gap explicit — and ideally closing it by re-running key ablations on downstream benchmarks — would set a useful standard for the subfield. The paper's transparency about which metrics are used where (lines 210–212) is already better than most, but the gap between ablation evidence and main-claim evidence deserves foregrounding.

## Suggestions
- Re-run the most salient ablation comparison (e.g., IRIS full configuration vs. image-SC-only minimization) on GenEval/T2I-CompBench/WISE to validate that the design choices transfer to downstream benchmarks.
- Replace "competitive with or superior to" in the abstract with phrasing that accurately reflects the best-checkpoint results (e.g., "achieves performance comparable to training with external rewards, without requiring any external supervision").
- Specify the training prompt dataset and error bar provenance explicitly in Section 4.1.
- Frame the Fig. 2 observation as empirical motivation rather than causal mechanism throughout the paper.

## Calibration Anchors
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| bEbQBiMpUI (self-correction convergence) | 5.40 | R1 | IRIS is stronger — better executed, fewer methodological gaps, more novel core insight |
| BGnm7Lo8oW (learning to reason at pre-training) | 5.50 | R2 | IRIS has clearer empirical validation and more direct practical significance |
| 38E4yUbrgr (LM self-improvement by RL) | 6.00 | R1/R2 | IRIS is stronger — more novel observation, more comprehensive ablations, evaluation on harder task |
| cJQ1K2fjpD (FiSAO, self-alignment for VLMs) | 6.20 | R2 | IRIS has cleaner methodology, better ablations, a more surprising core finding |
| kIP0duasBb (RLCF, CLIP reward TTA) | 6.67 | R2 | Comparable quality; IRIS has more novel core insight and broader significance, RLCF has cleaner framing |
| tmBKIecDE9 (Motif, intrinsic motivation) | 7.25 | R1 | Motif is stronger — cleaner execution, no overclaiming, beats extrinsic baseline. IRIS has framing/validation issues |
| SI2hI0frk6 (Transfusion) | 7.60 | R1 | Transfusion is substantially stronger — more ambitious, better executed, from a major lab |

**Round 1 bracket:** 5.5–7.0  
**Round 2 narrowing:** IRIS sits between FiSAO (6.20) and RLCF (6.67), with a novel core contribution but marginal framing issues. Given the comparison with RLCF (6.67) and Motif (7.25), IRIS lands at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>