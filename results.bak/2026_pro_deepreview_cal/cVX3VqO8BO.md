Now I have a solid calibration picture. Let me write the final consolidated review.

**Bracket from Round 1:** 5.0–7.0

**Round 2 narrowing:** The most comparable anchors are:
- Afjf6izLvJ (5.33, Reject): Agent-based framework with VLM guidance for robot policies — similar architecture ambition but different domain
- NxoFmGgWC9 (5.50, Accept): Video pre-training for manipulation — accepted despite significant baseline gaps; our paper has more novelty but similar evidence-to-claims ratio issues
- h7aQxzKbq6 / HAMSTER (6.00, Accept): Hierarchical VLA — cleaner evaluation, better-supported claims
- AJQuTFd9es / HandsOnVLM (6.33, Reject): Closest domain match (hand interaction + VLM) — rejected despite 6.33 due to missing details and limited baselines

Our paper has more components and ambition than most of these but evaluation gaps that directly undermine specific claims (especially cross-morphology). It sits between Afjf6izLvJ (5.33) and HAMSTER (6.00), comparable to NxoFmGgWC9 (5.50). I'll score it at **5.5**.

---

## Summary

UniHM proposes a unified framework for generating dynamic dexterous-hand manipulation sequences from free-form language instructions and RGB-D inputs. It combines three components: (1) a morphology-agnostic VQ tokenizer with a shared codebook across different hand types, (2) a vision-language model (based on Qwen3-0.6B) that generates manipulation token sequences using a progressive masking curriculum, and (3) a physics-guided dynamic refinement module that optimizes generated trajectories for physical feasibility. The framework is trained on human-object interaction datasets (DexYCB, OakInk) and evaluated on both seen/unseen objects and in real-world trials.

## Strengths

- **Physics-guided dynamic refinement is well-validated.** The frame-by-frame Gauss-Newton optimization (Section 3.4) that fuses contact, generative, and temporal priors is clearly described and its contribution is demonstrated in the ablation: removing it degrades MPJPE on DexYCB by 4.38mm (seen) and 1.83mm (unseen) (Table 4). This is a concrete, well-executed component.

- **Progressive masked training curriculum effectively reduces exposure bias.** The ablation (Table 4) shows that removing masked training causes MPJPE to rise from 61.40 to 73.41 on seen objects, confirming that the curriculum meaningfully improves autoregressive coherence when the model must rely on language alone at inference.

- **Learning from human video data eliminates dependency on expensive teleoperation.** The framework is trained solely on HOI datasets yet achieves 35–60% success rates on unseen objects in real-world pick-and-place, pull-and-push, and open-and-close tasks (Table 3), outperforming retargeted baselines. This supports the claim that human video data can substitute for costly robot-specific data collection.

- **The unified tokenizer architecture is technically sound.** The staged training procedure — establishing a reference encoder-decoder pair, then distilling new hand encoders into the shared latent space before fine-tuning (Eqs. 3–5) — is a principled approach to the cross-morphology alignment problem. The cross-hand translation formula (Eq. 6) provides a clean mechanism for token reuse.

## Weaknesses

### Fatal

None.

### Major

- **Cross-morphology generalization is claimed but never quantitatively evaluated.** The morphology-agnostic codebook is presented as a central contribution (listed as contribution #2 in the introduction). The paper describes retargeting to five robot hands (Shadow, Allegro, SVH, Leap, Panda) in Section 3.1 and the translation formula (Eq. 6). However, every quantitative experiment (Tables 1, 2, 4) uses only human-hand datasets (DexYCB, OakInk, both MANO-based). The real-world experiments (Table 3) use a single unspecified dexterous hand. There is no measurement of whether tokens generated for one morphology can be successfully decoded and executed on a different morphology — no tracking error, no simulation success rate, no qualitative comparison. The claim that the codebook "enables direct token reuse and transfer across robotic and anthropomorphic hands" remains an architectural proposal without empirical validation.

- **HOIGPT is cited as directly related work but never compared against.** HOIGPT (Huang et al., 2025) is described in Section 2.2 as a method that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences." This shares the same problem formulation (language-conditioned HOI sequence generation via tokenization) and output modality as UniHM. The paper instead compares against TM2T, MDM, FlowMDM, and MotionGPT3 — all designed for full-body human motion, not dexterous hand manipulation. The paper states that baselines are post-processed with physics refinement "to ensure a fair comparison" (Section 4.3) but does not explain how full-body motion models were adapted to produce hand-joint sequences. Without a comparison to HOIGPT, the claimed state-of-the-art status in Tables 1 and 2 is not adequately supported.

### Minor

- **Diversity on DexYCB is substantially lower than ground truth, and the paper does not acknowledge this gap.** On DexYCB, UniHM's diversity is 39.62 (seen) vs. GT 125.53 — less than one-third of the ground-truth variation. MotionGPT3 achieves 72.51. The paper lists Diversity as a metric where values "closer to the ground truth indicate a more reasonable generation" (Section 4.2) yet reports the low value without comment. On OakInk, diversity is much closer to GT (165.47 vs. 147.40), so this is dataset-specific, but the DexYCB result undercuts the claim of producing diverse manipulation sequences and should be discussed.

- **Methodology details are underspecified in several places.** The progressive masking schedule (how $p_t$ increases over training, Eq. 10) is described only qualitatively. The serialization of target trajectory, object point cloud, and VQ tokens into a single VLM input sequence (Eq. 9) is not specified — the paper states they are "concatenated" but does not give the token layout, which is critical for reproducibility. The real-world experimental setup (robot hand model used, camera configuration, number of trials per task, success criteria) is not described in the main paper.

- **Language annotation quality is never assessed.** The entire language-conditioning pipeline depends on GPT-4o auto-annotation of HOI sequences (Section 3.1). The paper provides no examples of generated instructions, no inter-annotator agreement, and no analysis of whether generated instructions accurately describe the corresponding motions. A few examples or a brief quality check would substantially strengthen confidence in the language grounding.

### Trivial

- The paper describes UniHM as "the first unified framework for dexterous hand manipulation guided by free-form language commands." HOIGPT also generates sequential HOI from language, so the novelty claim should be more precisely scoped to the cross-morphology and physics-refinement contributions rather than the general idea of language-conditioned HOI sequence generation.

## Nice-to-Haves

- Supplementing or replacing MPJPE with metrics that capture semantic alignment (e.g., text-motion retrieval accuracy, task-completion success in simulation) would provide a more complete picture of language-conditioned generation quality.
- Reporting physical feasibility metrics (penetration depth, joint limit violations, contact force magnitudes) before and after refinement would directly substantiate the value of the physics module beyond MPJPE improvement.
- A qualitative analysis showing generated sequences alongside their language instructions would help readers assess semantic alignment.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic claimed baselines are "inappropriate" and adaptation is unexplained.** While partially true (the adaptation of full-body motion models to hand joints is indeed not explained), the paper does state that baselines receive the same physics refinement post-processing. The baseline choice is unusual but not unreasonable — these are standard text-to-motion models. Retained only the HOIGPT omission and the lack of adaptation details as substantive concerns.

- **Harsh critic claimed MPJPE "invalidates the main quantitative claim."** Removed as stated — MPJPE is a standard metric in motion generation and is complemented by FID, Diversity, and real-world success rate. The paper does not rely exclusively on MPJPE. Retained the diversity gap as a minor concern.

- **Harsh critic demanded physical feasibility metrics, user studies, and text-motion retrieval accuracy.** Moved to Nice-to-Haves. These would strengthen the paper but are not standard requirements in this subfield.

- **Harsh critic claimed real-world experimental details are missing entirely.** The paper does include Table 3 with quantitative success rates, Figure 3 with qualitative results, and a description of the tasks. The details are thin but present. Retained as a minor concern about underspecification.

- **Strength Finder claimed "state-of-the-art MPJPE" as evidence of superiority.** Weakened — this claim depends on the baseline selection, which omits HOIGPT. The MPJPE numbers are still meaningful relative to the evaluated baselines but the SOTA framing is overclaimed.

- **Strength Finder claimed "generalizes to unseen objects and real-world tasks without needing teleoperation data."** Retained but qualified — Table 3 does show real-world success on unseen objects, which is genuine evidence.

## Novel Insights

The progressive masking curriculum (Eq. 10) creates an interesting accuracy-diversity trade-off that the paper's own ablation reveals but does not discuss: removing masked training improves diversity from 39.62 to 73.09 (approaching GT's 125.53) at the cost of higher MPJPE (73.41 vs. 61.40). This suggests the masking curriculum acts as a strong regularizer that collapses the output distribution toward high-likelihood modes. Understanding when and why this trade-off occurs — and whether it can be calibrated — is a genuinely interesting finding that the paper surfaces but leaves unexplored.

## Suggestions

- Add a cross-morphology experiment: take a set of generated manipulation sequences, decode them through at least two different hand decoders (e.g., MANO → Shadow, MANO → Allegro), and report joint error, task success in simulation, or at minimum qualitative side-by-side comparisons. This would directly address the largest gap between claimed contribution and evidence.
- Include HOIGPT as a baseline, or at minimum explain why a direct comparison is not feasible. If HOIGPT cannot be fairly compared (e.g., different input/output format), state this explicitly rather than omitting it.
- Discuss the DexYCB diversity gap and the accuracy-diversity trade-off revealed by the masked training ablation. The paper gains credibility by acknowledging limitations rather than ignoring them.
- Provide the masking schedule and VLM token layout in the main paper or clearly reference an appendix section containing them.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Afjf6izLvJ (Visuomotor Language Guidance) | 5.33 | 2 | Similar evaluation gaps relative to claims; our paper has more novelty |
| NxoFmGgWC9 (Video Generative Pre-training) | 5.50 | 2 | Similar evidence-to-claims ratio; our paper more ambitious but less thoroughly evaluated |
| h7aQxzKbq6 (HAMSTER) | 6.00 | 1,2 | Cleaner evaluation; our paper has more components but bigger gaps in supporting core claims |
| AJQuTFd9es (HandsOnVLM) | 6.33 | 1,2 | Closest domain match; rejected despite higher score due to missing details and limited baselines |
| 9pKtcJcMP3 (Video Language Planning) | 7.00 | 1 | Clearly more polished and better evaluated; our paper is below this level |

The paper makes genuine contributions — the unified tokenizer architecture, physics-guided refinement, progressive masking curriculum, and real-world results without teleoperation data. However, two core claims lack adequate empirical support: (1) cross-morphology generalization, which is entirely unevaluated quantitatively, and (2) state-of-the-art status, which depends on a baseline set that omits the most directly comparable prior work (HOIGPT). These are significant gaps given how central both claims are to the paper's contribution narrative. The paper is stronger than the typical 5.0-level reject (it has real-world experiments, clear ablations, and a technically sound method) but falls short of the 6.0+ tier where papers have better-aligned evidence-to-claims ratios.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>