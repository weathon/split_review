## Final Review

## Summary
IRIS proposes the first RL-based alignment method for autoregressive text-to-image models that uses only an intrinsic reward—Negative Self-Certainty (NSC, the negative KL divergence from a uniform distribution over the vocabulary). The key observation is that minimizing self-certainty improves T2I generation (the opposite of what holds for text reasoning), quantitatively demonstrated via a side-by-side experiment tracking self-certainty across modalities during RL training. Through GRPO training on Janus-Pro, IRIS achieves competitive results with externally-rewarded baselines across three benchmarks at two model scales, supported by comprehensive five-way ablation studies isolating each design choice.

## Strengths
- **Empirically grounded central observation (Fig. 2):** The paper quantitatively demonstrates that self-certainty trends in opposite directions for text reasoning (increasing, Qwen2.5-1.5B) vs. image generation (decreasing, Janus-Pro-1B) during RL training. This side-by-side measurement provides compelling, non-speculative motivation for the NSC reward design.
- **Comprehensive ablation study (Sec. 4.3, Figs. 5–9):** Each component of IRIS is systematically isolated: CoT vs. no-CoT, minimize vs. maximize image SC, minimize vs. maximize text SC, forward vs. backward KL, and RL vs. direct optimization. The five-way ablation across four evaluation metrics gives high confidence that the reported design choices are non-arbitrary and well-justified.
- **Rigorous benchmarking at two scales (Table 1):** Evaluation covers three complementary benchmarks (GenEval, T2I-CompBench, WISE) at both 1B and 7B model sizes, with subcategory-level analysis (Section 4.2) that explains where IRIS excels (natural science, physics) vs. where external rewards have domain-specific advantages (counting, spatial relations).
- **Baseline implementation correction (Sec. 4.1):** The paper identifies and fixes a chat-template error in prior work (T2I-R1 used wrong template keys for Janus-Pro), ensuring fair comparison and improving experimental integrity.
- **Revealing RL-vs-direct-optimization result (Fig. 9):** Direct gradient-based maximization of NSC causes model collapse (scores dropping to near zero), while GRPO maintains stable performance. This non-trivial finding provides practical guidance for intrinsic-reward methods beyond this specific paper.

## Weaknesses

### Fatal
None.

### Major
- **Fig. 3 vs. Table 1 discrepancy is unexplained:** The training curves in Fig. 3 depict IRIS outperforming T2I-R1 across all three benchmarks through most of training (the figure description states IRIS "achieves higher scores than T2I-R1 after approximately 200 training steps"). Yet Table 1, which reports best-checkpoint results, shows T2I-R1 ahead on every overall metric (e.g., GenEval 1B: 0.72 vs. 0.75; WISE 7B: 0.48 vs. 0.50). The paper never discusses this tension. If T2I-R1 has higher-variance training with peaks that favor best-checkpoint selection while IRIS is more stable, this should be stated explicitly—it would actually strengthen the case for IRIS's practical reliability. As presented, the reader cannot reconcile the two pieces of evidence and may suspect cherry-picking.

### Minor
- **Abstract overclaims relative to Table 1 evidence:** The abstract states IRIS "achieves performance that is competitive with or superior to external rewards." On overall benchmark metrics in Table 1, IRIS is consistently slightly *below* T2I-R1. The "superior to" claim rests on a subset of WISE subcategories (Physics: 0.45 vs. 0.43; Biology: 0.36 vs. 0.36 tie) and does not generalize to overall scores. The framing should be calibrated to "competitive with, and superior on specific knowledge-intensive subcategories."
- **No improvement on counting and color attribution vs. base model:** On GenEval 1B, IRIS's Counting score is flat relative to base (0.42 → 0.41, within reported ±0.03 error), and Color Attribution stays at 0.51, while T2I-R1 improves both substantially (to 0.50 and 0.63 respectively). The paper notes T2I-R1's domain-specific advantage from DINO and VQA rewards (Section 4.2) but does not fully discuss what it means that intrinsic rewards cannot move these fundamental compositional skills.
- **"Reasoning" framing is imprecise:** The paper claims IRIS "enhance[s] the reasoning capabilities of T2I models" (line 44) and emphasizes "reasoning and planning." The benchmarks (GenEval, T2I-CompBench, WISE) measure compositional binding, attribute accuracy, and knowledge retrieval—important capabilities, but not reasoning in the sense the NLP community uses the term. Reframing around "compositional generation" or "prompt alignment" would be more accurate and would not weaken the contribution.
- **CoT emergence evidence is anecdotal:** The claim of "emergence of long-form reasoning" (Sec. 4.2) rests on a single qualitative example (Fig. 4). While Fig. 5 shows CoT training improves quantitative scores, no metric measures whether CoTs themselves improved in length, relevance, or accuracy during IRIS training.
- **Training data and error bar methodology unspecified:** The training prompt dataset is never explicitly named (line 110 only references following T2I-R1's protocol). Table 1 reports ± values without clarifying whether they reflect variance across multiple training runs or across evaluation samples—a distinction that matters for the small gaps between IRIS and T2I-R1.

### Trivial
None.

## Nice-to-Haves
- A temperature/diversity baseline (e.g., simply increasing sampling temperature during inference or GRPO rollouts) would help clarify whether IRIS is doing more than encouraging output diversity.
- Multiple training runs with different seeds would strengthen confidence in the small performance gaps in Table 1.
- A small-scale human preference study would complement the fully automatic evaluation and better ground the claim that lower self-certainty yields images better aligned with human preferences.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic's "fatal" claim about overclaiming:** Characterized the overclaim as potentially fatal. In reality, the paper's core contribution (intrinsic reward for T2I without external supervision) does not depend on IRIS beating external rewards—"competitive with" is sufficient and well-supported. Retained as Minor weakness about framing only.
- **Harsh Critic's "task confound" criticism of Fig. 2:** Claimed that comparing math reasoning (text) vs. T2I generation (image) using different tasks confounds the modality comparison. But the paper's claim is about modality-dependent behavior, not task-independent behavior; using different tasks per modality is inherent to the comparison and does not undermine the observation. Removed.
- **Harsh Critic demand for human evaluation as a weakness:** Moved to Nice-to-Haves since fully automatic evaluation with established benchmarks (GenEval, T2I-CompBench, WISE) is standard practice in this subfield.
- **Strength Finder's generic "problem importance" statements:** Folded into summary rather than listed as standalone strengths.

## Novel Insights
The paper's key insight—that self-certainty behaves in opposite directions for text reasoning vs. image generation during RL training, and that this asymmetry can be exploited as a task-agnostic intrinsic reward—is genuinely novel and opens an interesting line of inquiry about modality-dependent reward design. The finding that direct NSC gradient optimization causes model collapse while GRPO maintains stability (Fig. 9) is a practically valuable observation that generalizes beyond this specific method.

## Suggestions
- Add a brief paragraph in Sec. 4.2 explicitly reconciling the Fig. 3 training curves with the Table 1 best-checkpoint results. If T2I-R1 has higher variance, report it; if checkpoint selection favors T2I-R1's peaks, discuss what this means for practical deployment (IRIS may be more stable/reliable even if its peak is lower).
- Replace "superior to external rewards" in the abstract with "competitive with external rewards, and superior on knowledge-intensive subcategories."
- Clarify error bar methodology in the Table 1 caption.
- Name the training prompt dataset explicitly in Sec. 4.1.

## Score and Decision

**Anchor comparison (all rounds):**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| RFJGFrMvYj (TCIG) | 1.50 | R1 | Much weaker; unrelated method |
| zEhTnQZB3D (LLIT) | 2.33 | R1 | Much weaker; different domain |
| FTpdQBoBd0 (T2I Fine-Tuning) | 3.00 | R1 | Weaker; limited novelty and evaluation |
| RIKIavmwqK (FigCaps-HF) | 3.75 | R1 | Weaker; different task |
| uxYbEAEWm4 (KLAFT) | 3.67 | R1 | Weaker; limited ablation |
| bO31lfEdos (Hallucination RL) | 5.00 | R1 | Weaker; single model, thinner evaluation |
| xreOs2yjqf (EvalAlign) | 4.75 | R1 | Different task; evaluation metric |
| RauUgiw7VX (Semantic Refinement) | 4.75 | R1 | Different approach; limited scope |
| jQP5o1VAVc (Fluid/Scaling AR) | 5.75 | R2 | Weaker; empirical study with limited novelty |
| **Let8OMe20n (Confidence-aware Reward)** | **6.00** | **R2** | **Most comparable; IRIS has more comprehensive ablations and benchmarks** |
| cJQ1K2fjpD (FiSAO) | 6.20 | R2 | Similar quality; FiSAO has theory, IRIS has better ablations |
| kIP0duasBb (TTA CLIP Reward) | 6.67 | R2 | Stronger; more polished, better evaluated |
| kGvXIlIVLM (CCA) | 7.00 | R2 | Stronger; theoretical grounding, cleaner narrative |
| Im2neAMlre (T2I Eval Suite) | 7.33 | R2 | Stronger; thorough evaluation study |

**Bracket:** Round 1 placed the paper in 6.0–7.5. Round 2 narrowed to the 6.0–6.5 range, anchored most closely by Let8OMe20n (6.00) and cJQ1K2fjpD (6.20). IRIS has stronger empirical validation (comprehensive 5-way ablations, three benchmarks, two model scales) than Let8OMe20n (6.00) but is dragged down by the unexplained Fig. 3/Table 1 discrepancy, overclaiming in the abstract, and missing methodological details. It does not reach the polish and theoretical grounding of kGvXIlIVLM (7.00).

**Final score: 6.0.** This is a solid paper with a genuinely novel observation, clean method, and thorough ablation studies. The weaknesses are real but addressable—they are primarily matters of framing, presentation clarity, and one structural evidence-presentation issue (Fig. 3/Table 1). The core contribution (first intrinsic reward method for autoregressive T2I, modality-dependent self-certainty observation) is sound and well-supported.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>