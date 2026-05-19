- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes LAMP, a method that uses a frozen Vision-Language Model (R3M) to generate shaped exploration rewards during task-agnostic RL pretraining, combined with Plan2Explore novelty rewards. The pretrained language-conditioned policy is then finetuned on downstream RLBench manipulation tasks with scripted task rewards. The core insight — that noisy VLM alignment scores are better suited as pretraining signals that bias exploration toward semantically meaningful behaviors rather than as direct task rewards — is clearly motivated and represents a genuine departure from prior work.

## Strengths

- **Novel and well-motivated framing.** The paper makes a compelling argument that VLM-based reward functions, which are known to be noisy and non-monotonic, should be used as pretraining signals rather than direct task rewards. Figure 2 directly supports this premise by showing that R3M, InternVideo, and ZeST alignment scores over expert episodes are highly irregular and do not increase monotonically, explaining why optimizing them directly would be unstable. This empirical motivation is strong.

- **Consistent sample-efficiency gains across multiple RLBench tasks.** Figure 5 shows that LAMP pretraining leads to higher or equal finetuning returns than training from scratch on all five tasks (pick up cup, take lid off saucepan, push button, microwave, turn tap). The improvement over from-scratch training is consistent, and LAMP is at least competitive with Plan2Explore across the board. This directly supports the central claim that VLM-modulated pretraining can warmstart downstream RL.

- **Demonstrated synergy between VLM rewards and novelty-seeking exploration.** Figure 6b compares LAMP with and without Plan2Explore for two prompt styles. The key result: LAMP with relevant prompts (Prompt 2) plus Plan2Explore succeeds, while irrelevant prompts (Prompt 6) plus Plan2Explore collapses, even though both work similarly without Plan2Explore. This provides concrete evidence that the VLM reward (Eq. 2) effectively biases the novelty-driven exploration toward semantically meaningful behaviors — the paper's central methodological contribution.

- **Robustness across different frozen VLMs.** Figure 7 compares R3M and ZeST (CLIP-based) as the reward backbone on the pick‑up‑cup task. Both enable successful pretraining, showing the method is not tied to a specific VLM. This supports the claim that LAMP can benefit from future, more capable VLMs.

- **Scalable prompt generation with minimal human effort.** The paper describes using ChatGPT to automatically produce diverse imperative/declarative instructions, synonym variations, and human-/robot-centric wordings (Section 4.1). This practical contribution addresses scalability and reduces manual reward engineering.

- **Prompt diversity ablation shows robustness.** Figure 6a compares five action-based prompting styles on Pick Up Cup. While Prompt 2 (relevant verb + synonym noun) performs best, all five enable reasonable finetuning, demonstrating the approach is not brittle to prompt choice.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear whether the Plan2Explore baseline receives comparable pretraining.** The paper states that one baseline is "a randomly initialized MWM agent trained from scratch" and the other is "Plan2Explore… a novelty-seeking method that explores based on model-uncertainty" (Section 5.1). The first is explicitly from-scratch; for the second, the paper does not state whether it undergoes the same number of pretraining steps in the same domain-randomized environment, or whether it is also trained from scratch on the downstream task. Since Plan2Explore is used inside LAMP as the novelty component and is a pretraining algorithm itself, the natural reading is that it receives comparable pretraining — but this is not confirmed. **If Plan2Explore does not receive comparable pretraining, then the comparison conflates the VLM reward with simply more environment interaction.** The paper should explicitly describe the Plan2Explore baseline's pretraining setup and ideally include a control that pretrains using only the Plan2Explore reward (α=1.0 in Eq. 3) to isolate the VLM contribution. This is a clarity issue that undermines the strongest reading of the results.

### Minor

2. **No ablation of α (the reward mixing weight).** Equation 3 sets α=0.9 without any sensitivity analysis. The paper states "We found that an α value of 0.9 works quite well across the tasks evaluated" (Section 4.2) but does not show the evidence. The "w/o Plan2Explore" ablation (which corresponds to α=0) is only shown for two prompt styles on one task (Figure 6b). Critically, the claim that the VLM reward contributes useful signal depends on this choice — without sweeping α, the reader cannot assess how sensitive the results are. (Note: the critic's characterization that "the VLM contributes only 10%" is misleading because the effective contribution depends on the relative scales of the two rewards, not just the weight; this is precisely why an ablation is needed.)

3. **Ablations for language prompting and VLM model are conducted on a single task (Pick Up Cup).** Section 6.1 and Section 6.2 evaluate prompt style variation and VLM choice only on this one task. The conclusions that "LAMP is robust to different prompting strategies" and that the method "is likely to benefit from more powerful VLMs" are stated generally, but the empirical support is limited to one task. Running these ablations on at least 2–3 tasks would strengthen the generality claims.

4. **"Turn tap" shows comparable LAMP and Plan2Explore performance.** On this task (Figure 5), the two methods converge to similar finetuning returns. The text honestly says "LAMP outperforms or is competitive with Plan2Explore" — but this task tempers the consistency narrative. It is a minor weakness in the evidence, not a contradiction.

5. **Number of pretraining steps is not reported.** The paper describes the pretraining environment and the per-episode procedure in detail but does not state the total number of pretraining episodes or gradient steps. This makes it difficult to assess the scale of the pretraining investment and to calibrate replication efforts. (This detail may appear in the supplementary appendix, which is stripped by the parser.)

### Trivial

- The paper would benefit from reporting batch size and exact training duration for reproducibility.

## Nice-to-Haves

- Additional baselines from unsupervised pretraining (e.g., DIAYN, RND, ICM) and representation-based approaches (using R3M as a visual feature extractor for the policy itself, rather than as a reward source) would further strengthen the evaluation, though the paper's comparison to from-scratch and Plan2Explore is already reasonable.
- Direct measurement of exploration quality during pretraining (e.g., coverage of object interactions, diversity of states reached) would provide stronger evidence for the claim that the VLM reward "biases exploration toward semantically meaningful affordances," which is currently inferred solely from downstream finetuning performance.
- A larger set of downstream tasks (8–10) would more convincingly demonstrate generality, though 5 tasks is within the range of typical robotics papers with complex simulation setups.

## Removed Points

These points were raised in the reviews but are removed for the following reasons:

1. **"The VLM contributes only 10% because α=0.9" (Harsh Critic).** Removed because the effective contribution of a reward term depends on its scale relative to the other term, not just the convex combination weight. Without knowing reward magnitudes, α=0.9 does not imply a 10% contribution. This is a misunderstanding; the real issue (which is kept as Minor weakness #2) is that α is not ablated.

2. **"No comparison to DADS, DIAYN, RND, ICM" (Harsh Critic).** Removed as scope creep. The paper compares against the most relevant baselines: from-scratch (to show pretraining helps) and Plan2Explore (to show VLM rewards add value beyond pure novelty). Requesting all possible unsupervised pretraining methods sets an unreasonably high bar for a paper whose contribution is about VLM-based reward modulation.

3. **"Plan2Explore matches on turn tap and the text does not acknowledge this" (Harsh Critic).** Removed as factually wrong. The paper explicitly states "LAMP outperforms or is **competitive with** Plan2Explore" (Section 5.2), which honestly acknowledges comparable performance on some tasks.

4. **"Variance overlap on microwave and push button" (Harsh Critic).** Removed because overlapping confidence intervals with 3 seeds are standard in RL and do not invalidate the observed trends. This is a routine statistical issue, not a specific weakness.

5. **"Only 5 tasks is narrow" (Harsh Critic).** Weakened/removed. Five manipulation tasks with a complex domain-randomized pretraining setup is a reasonable evaluation. The kept Minor weakness correctly notes that ablations are on a single task, which is a more precise concern.

6. **"Missing related works" (Harsh Critic — implied).** Removed per instruction: reviews must not cite missing related works without external verification.

## Novel Insights

The harsh critic correctly identifies that the α=0.9 choice and the single-task ablations limit the paper's ability to quantify the VLM reward's contribution. However, a more subtle insight that neither review fully develops is that the **synergy result in Figure 6b** (Prompt 2+Plan2Explore succeeds, Prompt 6+Plan2Explore fails) is actually the paper's strongest evidence for the VLM reward doing real work. It shows that adding novelty to an irrelevant VLM reward **hurts** performance, while adding it to a relevant VLM reward **helps**. This interaction effect is harder to explain away by pretraining duration alone — it suggests the VLM reward's semantic content genuinely directs the exploration. The paper could lean into this analysis more explicitly.

## Suggestions

1. **Clarify the Plan2Explore baseline setup** explicitly: state whether it receives the same number of pretraining steps in the same domain-randomized environment, and whether its reward is purely the novelty bonus with no VLM component. Add a control: pretrain with only Plan2Explore reward (α=1.0) and finetune, then compare to LAMP.

2. **Ablate α** across a range (e.g., 0.0, 0.5, 0.9, 1.0) on at least 2–3 tasks to show sensitivity of the results to the mixing weight.

3. **Run prompt-style and VLM ablations on at least one additional task** (e.g., "take lid off saucepan") to support the generality claims about robustness.

4. **Report the number of pretraining episodes/steps** and other key hyperparameters (batch size, training duration).

5. **Consider including a direct analysis of exploration quality** during pretraining: e.g., measure state coverage or frequency of object interactions as a function of the VLM reward component, to directly support the "semantically meaningful exploration" narrative.

---
