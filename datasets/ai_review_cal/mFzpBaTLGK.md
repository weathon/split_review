- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
## Summary

This paper proposes FAB (Foundation Acoustic model Backdoor), a backdoor attack against acoustic foundation models (AFMs) under a notably weak threat model: the adversary lacks access to the pre-training data, codebook, and projection matrix, and the downstream task is unknown. FAB uses inconspicuous, input-agnostic, sync-free, and physically realizable triggers (e.g., a siren sound played in the background) to cause task-agnostic performance degradation. The attack is evaluated across nine downstream tasks, two AFMs (HuBERT and WavLM), four trigger types, two defenses, and includes both digital and physical-domain experiments.

---

## Strengths

- **Task-agnostic attack demonstrated across nine diverse downstream tasks.** Table 1 (referenced in §6.1) shows that for all nine tasks (ASR, PR, KS, SID, ASV, SD, IC, ST, ER), models fine-tuned from the backdoored AFM retain benign performance comparable to the benign AFM, while trigger-stamped inputs cause drastic degradation (e.g., ASR WER from 5.9% to 80.8%, PR from 4.6% to 71.2%). This directly supports the paper's core claim of task-agnostic, fine-tuning-surviving backdoors.

- **Physically realizable attack via over-the-air recordings.** Table 2 shows that physical recordings with the siren trigger yield WER ≥71% on ASR, while benign physical recordings achieve only ~7% WER. This provides real-world evidence that the attack works when the trigger is a physical sound played from a speaker and recorded by a microphone, matching the claimed threat model.

- **Approximated codebook under weak threat model matches a stronger adversary.** Section 4.2 details how FAB approximates the missing codebook by clustering representations from an auxiliary dataset and uses an identity projection matrix. The paper reports (line 213, App. C.2) that this constrained attack attains success comparable to an attack with full access to the pre-training codebook, pseudo-labels, and projection matrix, validating that the weak-threat-model design does not come at a significant cost to attack efficacy.

- **Standard defenses fail against FAB.** Tables 3–4 show that fine-pruning and input filtration cannot counter the attack without severely harming benign performance. For fine-pruning at 20%, benign WER rises from 5.9% to 15.7% while trigger WER remains >60%; for input filtration at 30%, benign WER rises to 21.9% while trigger WER remains >69%. This underscores the practical threat.

---

## Weaknesses

### Fatal

None.

### Major

- **No empirical comparison to prior acoustic backdoor attacks.** The paper positions itself against prior speech-model backdoor work (Koffas et al., Lee et al., etc.) and states that "FAB addresses these shortcomings" (line 18), yet provides no direct experimental comparison — not on a shared task, model, or metric. Without it, the reader cannot assess whether FAB is more effective, more practical, or merely different. The threat models differ (FAB assumes a weaker adversary), but the paper's own framing claims to address limitations of prior work, which demands empirical substantiation. This is the single most significant weakness in the paper.

- **Physical realizability evaluation is too thin to fully support the headline claim.** The physical experiment uses only 23 samples, a single task (ASR), and reports aggregate results without disaggregating the two described physical setups (simultaneous play from separate speakers vs. digitally-mixed-then-played). The physically-realizable scenario — simultaneous play — is the one that matches the threat model (§3.3), but we cannot determine whether the reported ≥71% WER reflects that condition or the easier mixed-then-played condition. Additionally, 23 samples provide no meaningful variance information. Given that "physically realizable" is central to the contribution, this evidence is too limited to be fully convincing. Testing with multiple trigger types, more samples, and at least one additional environment would substantially strengthen the claim.

### Minor

- **No variance or statistical significance information reported.** Tables across all experiments report single values without standard deviations, confidence intervals, or evidence of repeated trials. This makes it difficult to assess the reliability of the reported numbers. While single-run evaluation is common practice in this field, the lack of variance information is notable given the breadth of the claimed results.

- **Defense evaluation is limited to two older methods (fine-pruning and input filtration).** The paper would be strengthened by testing against a broader set of more recent defenses, which would better support the claim that FAB robustly evades countermeasures.

- **The paper does not analyze *why* the backdoor survives fine-tuning.** Showing that the trigger consistently shifts representations toward the target vector after fine-tuning (e.g., via representation similarity analysis on the intermediate layer) would deepen the insight beyond the current empirical demonstration.

### Trivial

None.

---

## Nice-to-Haves

- **Sync-free tension discussion.** The paper's training procedure randomizes trigger offset digitally, but in physical deployment the adversary cannot control the relative timing between user speech and trigger playback with any precision. A brief discussion of how the sync-free property handles this practical gap (e.g., why the random-offset training suffices for robustness under uncontrolled physical timing) would strengthen the threat model explanation.
- **Ablation on auxiliary dataset size.** The paper mentions testing smaller auxiliary datasets (App. C.4) — this is good. Making the lower bound of feasibility more explicit in the main paper would help assess practicality for a truly weak adversary.
- **Additional physical variations.** Testing with different distances, room acoustics, background noise levels, and microphone types would make the physical realizability claim more robust.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Missing appendix sections (C.1–C.7) are referenced but not provided."* — **Removed per instructions:** the parser strips appendices from all papers; they exist in the original submission.
- *"Auxiliary dataset is 115 hours (~8% of pre-training data) — not trivially small."* — **Removed:** the paper already addresses this via ablation in App. C.4, which reports that the attack still works with smaller auxiliary datasets.
- *"Sync-free tension: how is random offset and fixed SNR achieved physically without input knowledge?"* — **Removed:** the paper explicitly defines sync-free as meaning the attack works at any offset (line 104), and intentionally avoids fixed-SNR assumptions in physical deployment. This is a discussion point, not a flaw.
- *"Pre-training HuBERT from scratch to enable ablation means the benign baseline may differ from a standard public checkpoint."* — **Removed:** the paper explicitly states this design choice and justifies it for controlled ablation (line 151). Any deviation would affect both benign and backdoored conditions symmetrically.
- *"Formatting obscures table numbers"* — **Removed:** parser artifact from PDF extraction, not an author error.

---

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's broad evaluation scope (9 tasks, 2 AFMs, 4 triggers, 2 defenses) and the thinness of the single most novel claim (physical realizability, 23 samples/1 task). The paper is strong in breadth but the headline claim of physical realizability rests on much narrower evidence than the rest of the evaluation. This asymmetry suggests the authors should either (a) dramatically expand the physical evaluation or (b) temper the strength of the physical-realizability claim while keeping the broader contribution (task-agnostic backdoor under weak threat model) as the primary focus.

---

## Suggestions

1. **Add a direct comparison to at least one prior speech backdoor attack.** Even a single comparison on a matching subset of conditions (e.g., ASR task with Koffas et al.'s input-agnostic trigger under a comparable threat model) would make the claimed advantages empirically grounded.
2. **Expand the physical evaluation.** Increase sample size substantially, report per-condition results (simultaneous vs. mixed-then-played disaggregated), test at least one additional environment, and provide per-sample results or confidence intervals.
3. **Add variance information** to the main tables (e.g., standard deviations over multiple fine-tuning seeds or test set splits).
4. **Include a post-fine-tuning analysis** of the intermediate-layer representations to explain *why* the backdoor survives fine-tuning (e.g., showing that trigger-stamped representations converge toward the fixed target vector even after weight updates for the downstream task).

---
