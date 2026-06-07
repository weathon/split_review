Round 2 anchors analyzed. Let me now compare UniHM against these:

- **Video2Policy (5.50, Reject)**: No real-world eval, limited technical novelty, simple tabletop only. UniHM is clearly stronger — has real-world results and more technical depth.
- **SuSIE (6.25, Accept)**: Decoupled architecture, real-world results. Cleaner evaluation story — task success directly measures language following. UniHM has more technical novelty but bigger claim-evidence gaps.
- **RoboFlamingo (6.50, Accept)**: Tight evaluation on CALVIN, but simulation-only. UniHM has real-world results but weaker evaluation coherence.
- **HAMSTER (6.00, Accept)**: Similar hierarchical VLA approach, real-world results, but also had missing baselines and limited task diversity.

UniHM is clearly stronger than Video2Policy (5.50) but not as well-evidenced as SuSIE (6.25). The cross-morphology claim without any experimental support and the language-grounding gap are significant. I place it at **5.5** — borderline, with the major weaknesses pulling it below the 6.0+ accept band.

---

## Summary

UniHM proposes a framework for generating dexterous hand manipulation sequences from free-form language instructions. It combines three components: (1) a unified VQ-VAE tokenizer with a shared codebook across multiple hand morphologies, (2) a vision-language model (Qwen3-0.6B) trained with a progressive masking curriculum to generate manipulation tokens conditioned on text, trajectory, and point-cloud inputs, and (3) a physics-guided refinement module that optimizes generated poses for contact, temporal smoothness, and fidelity to the generative prior. The method is trained on human-object interaction video (DexYCB, OakInk) without teleoperation data, and evaluated on pose-accuracy and motion-quality metrics, with additional real-world robot trials.

## Strengths

- **Physics-guided dynamic refinement is technically well-executed and empirically validated.** The three-term optimization (contact, generative prior, temporal smoothness) in Section 3.4 uses an asymmetric contact penalty explicitly designed to be continuous and slope-matched at d=0, enabling stable Gauss-Newton optimization. The ablation (Table 4) shows removing physical refinement raises MPJPE from 61.40 to 65.78 (seen, DexYCB), confirming its quantitative contribution.

- **Progressive masking curriculum is effective and well-ablated.** Moving from full teacher forcing to fully autoregressive generation via a learnable [MASK] token reduces exposure bias. Table 4 shows this is the single largest ablation effect: MPJPE degrades from 61.40 to 73.41 without it.

- **Real-world transfer from human video without teleoperation is demonstrated.** Training entirely on HOI datasets (DexYCB, OakInk) rather than expensive robot teleoperation data, Table 3 shows UniHM achieving 50–65% success on seen objects vs. 10–30% for the strongest baseline, with gains largely persisting on unseen objects. This provides evidence that human-video-trained manipulation can transfer to physical execution.

- **Decoupled perception-generation architecture is well-motivated.** Separating CLIPort-based perception (inference-only) from the VLM-based HOI generator means only the smaller perception head needs adaptation under distribution shift.

## Weaknesses

### Fatal

None.

### Major

- **Language grounding is never directly evaluated, despite being the paper's central claim.** The paper frames itself around "unified dexterous hand manipulation guided by free-form language commands" and claims to be the first language-conditioned framework for dynamic manipulation. Yet the quantitative evaluation (Tables 1–2) uses only pose-accuracy metrics (MPJPE, FOL, FPL) and motion-quality metrics (FID, Diversity). None measures whether the generated manipulation actually follows the instruction — MPJPE measures distance to a single ground-truth trajectory, and a model producing a high-quality, physically valid motion that does the wrong thing (e.g., grabs instead of pushes) could still achieve low MPJPE. The real-world results (Table 3) partially address this through task-specific success rates, but these involve only two baselines with no trial counts or error bars, and the headline SOTA claims rest on Tables 1–2. This is a structural gap between the paper's motivation and its evidence.

- **Cross-morphology transfer — listed as a headline contribution — has no experimental support.** The paper lists "Morphology-Agnostic Codebook" as a core contribution, claiming it enables "direct token reuse and transfer across robotic and anthropomorphic hands." Section 3.2 describes integrating five robot hands (Shadow, Allegro, SVH, Leap, Panda) via knowledge distillation and Eq. 6 shows cross-hand pose translation. But the Experiments section contains zero cross-hand results: no reconstruction quality comparison across hands, no demonstration of token transfer, no ablation comparing unified vs. hand-specific codebooks. The introduction also claims "extensive real-world cross-embodiment experiments" (line 33) but Table 3 evaluates only a single unspecified hand. A major claimed contribution is entirely unsubstantiated.

- **Baseline comparison is inadequately specified and omits the most relevant prior work.** The baselines in Tables 1–2 (TM2T, MDM, FlowMDM, MotionGPT3) are human body-motion generation models, not dexterous hand manipulation systems. The paper never explains how these were trained or adapted for hand pose generation on DexYCB and OakInk. Meanwhile, the Related Work discusses HOIGPT (text-to-HOI sequence generation), SemGrasp, AffordDexGrasp, and Multi-GraspLLM — all language-guided hand-interaction methods — yet none appear in the experimental comparison. Without the most directly comparable baselines or a clear account of how the chosen ones were adapted, the comparison does not reliably establish UniHM's relative merits.

### Minor

- **Training-inference distribution shift is asserted as a feature but never measured.** The VLM trains with ground-truth trajectories and object point clouds but at inference these are replaced by CLIPort and PointSAM predictions. The paper frames this decoupling as advantageous but never quantifies CLIPort's trajectory prediction accuracy or how errors propagate to final manipulation quality.

- **Real-world evaluation lacks standard reporting details.** Table 3 reports success rates without trial counts, error bars, or specification of which robot hand was used. The gap between UniHM and baselines is large, but without these details the robustness is unclear.

- **Diversity anomaly in the ablation is unexplained.** Removing masked training (Table 4) substantially increases Diversity (73.09 vs. 39.62 on seen) while degrading accuracy — a large effect suggesting the masking curriculum may trade off diversity for accuracy, which merits discussion but receives none.

- **Annotation and retargeting quality are never validated.** GPT-4o annotation quality is assumed but not validated. Dex-Retargeting quality is not reported, which matters because retargeting errors propagate into downstream training.

- **Method details are incomplete for reproducibility.** The paper does not specify the codebook size K, the sequence chunk length, how text, trajectory, point cloud, and hand-pose tokens are integrated into a unified VLM input sequence, or the token vocabulary relative to the VLM's own vocabulary.

### Trivial

- The abstract promises "state-of-the-art results on both seen and unseen objects and trajectories" — a claim whose force is weakened by the reliance on body-motion baselines rather than HOI-focused methods.

## Nice-to-Haves

- A direct language-following evaluation — even a qualitative study showing that different instructions produce meaningfully different manipulation sequences for the same object — would substantially strengthen the paper.
- Including HOIGPT as a baseline, since it does text-to-HOI sequence generation and is the most directly comparable method discussed in Related Work.
- Demonstrating the cross-morphology capability with at least one experiment: train the tokenizer on MANO + one robot hand, show reconstruction quality on a held-out hand, and compare against a hand-specific tokenizer.
- Reporting the CLIPort trajectory prediction accuracy.
- Explaining the Diversity anomaly in the masked training ablation.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **REMOVED: "The relationship between the tokenizer's sequence chunk representation and the VLM's token-by-token generation is never clarified."** — Merged into the Minor point about incomplete method details.
- **REMOVED: Criticism about "the first unified language-conditioned framework" claim given HOIGPT's existence.** — HOIGPT is discussed in Related Work, and the paper positions its contribution as going beyond static grasps and digital-hand-only methods. The claim is about dynamic dexterous manipulation across robot hands, which is a meaningful distinction.
- **REMOVED: Speculation about whether the masking curriculum causes mode collapse.** — The Diversity anomaly is worth noting (kept as Minor), but calling it "mode collapse" without evidence goes beyond what the paper shows.

## Novel Insights

None beyond the paper's own contributions. The combination of a unified VQ codebook with staged distillation for cross-morphology tokenization and physics-guided Gauss-Newton refinement with an asymmetric contact penalty is a technically coherent pipeline, but the individual components are each drawn from established paradigms.

## Suggestions

- The most important addition would be a direct language-following evaluation — at minimum, a qualitative study showing that different instructions produce meaningfully different manipulation sequences for the same object, or a task-completion metric in simulation.
- Demonstrate the cross-morphology capability with at least one experiment comparing unified vs. hand-specific codebooks.
- Clarify how the body-motion baselines were adapted, or replace/supplement them with HOI-focused methods (HOIGPT, SemGrasp).
- Report trial counts, error bars, and the specific robot hand used for Table 3.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Video2Policy (RhfYIJux9d) | 5.50, Reject | R2 | UniHM is stronger: has real-world results, more technical depth |
| GR-1 (NxoFmGgWC9) | 5.50, Accept | R1 | Similar baseline/evidence gaps; UniHM has real-world but broader unvalidated claims |
| HAMSTER (h7aQxzKbq6) | 6.00, Accept | R1/R2 | Comparable ambition; HAMSTER had tighter claim-evidence alignment |
| SuSIE (c0chJTSbci) | 6.25, Accept | R2 | SuSIE's evaluation more directly measures its core claim; UniHM has more technical depth but weaker evidence for its central thesis |
| HandsOnVLM (AJQuTFd9es) | 6.33, Reject | R1 | Similar domain (hand interaction + VLM); HandsOnVLM had clearer evaluation story |
| RoboFlamingo (lFYj0oibGR) | 6.50, Accept | R2 | Tighter evaluation on established benchmark; UniHM has real-world results but evaluation gaps |

Round 1 bracket: **5.0–6.5**. Round 2 narrowed to: UniHM is stronger than the 5.50 anchors (Video2Policy, GR-1) but weaker than the 6.0+ anchors (SuSIE 6.25, RoboFlamingo 6.50, HandsOnVLM 6.33) due to the unvalidated cross-morphology claim, missing language-grounding evaluation, and inadequate baselines. Comparable to HAMSTER (6.00) but with one additional unsubstantiated headline contribution (cross-morphology). Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>