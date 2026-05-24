Now let me write the final review.

## Summary

This paper introduces Visuo-Tactile World Models (VT-WM), the first multi-task world model that fuses fingertip tactile sensing (Digit 360, encoded via Sparsh-X) with exocentric vision (Cosmos encoder) to ground autoregressive imagination in contact physics. The model uses a factorized spatiotemporal transformer with action cross-attention and is trained via a combination of teacher forcing and sampling losses. Experiments on a real robot show that VT-WM improves object permanence (33% avg. reduction in Fréchet distance) and causal compliance (29% avg. reduction) over a vision-only V-WM baseline. Zero-shot CEM-based planning achieves up to 35% higher success on contact-rich tasks, and fine-tuning on 20 demos of a plate-insertion task yields 77% success vs. 22% for a BC baseline.

## Strengths

1. **First multi-task visuo-tactile world model with genuine architectural novelty.** The paper proposes a clean architecture that fuses Cosmos vision tokens and Sparsh-X tactile tokens through factorized spatiotemporal self-attention and action cross-attention, solving the nontrivial problem of combining modalities with different temporal resolutions (6 fps video, 6 Hz tactile) and spatial structure. This is a concrete, novel contribution to the world model literature.

2. **Quantitatively grounded evidence that tactile input improves physical fidelity of imagined rollouts.** The contact perception experiments (Section 4.1) are well-designed: both models are conditioned on the same ground-truth action sequences from real demonstrations, and the comparison uses CoTracker-based normalized Fréchet distance with paired t-tests. VT-WM achieves statistically significant improvements in 3/5 tasks for object permanence and 3/5 for causal compliance, with consistent directional improvement on the remaining tasks. The qualitative visualizations (Figures 5, 7) support the quantitative findings.

3. **Real-robot zero-shot planning validation across tasks of increasing difficulty.** The CEM-based planning evaluation (Section 4.2, Figure 8) tests both models on five real-robot tasks ranging from simple reaching (100% for both) to multi-step contact-rich stacking. VT-WM consistently outperforms V-WM, with the largest gains (31–35%) on tasks requiring sustained contact. The experimental design — open-loop zero-shot transfer from plans generated entirely in imagination — is a strong test of world model quality and avoids confounding effects from online adaptation.

## Weaknesses

### Major

1. **The data efficiency experiment conflates multi-task pre-training with tactile grounding.** Section 4.3 compares VT-WM (fine-tuned from multi-task pretraining on 20 demonstrations of a new task) against ACT behavioral cloning (trained from scratch on the same 20 demos). The paper frames this as showing "VT-WM shows data efficiency," but the comparison cannot attribute the observed advantage to the tactile modality — multi-task pre-training on prior manipulation data is the obvious confound. The paper's stated question ("how does fine-tuning a multi-task world model for planning compare to behavioral cloning?") is legitimate and the results are informative as a multi-task WM vs. BC comparison. However, the abstract and conclusion frame this as a strength of VT-WM specifically (e.g., "VT-WM shows data efficiency when targeting a new task"), which overclaims. A V-WM fine-tuned on the same 20 demos from the same multi-task pretrained checkpoint would be needed to isolate the tactile contribution. This weakness does not invalidate the paper's core contributions (contact perception and planning), but the claims about data efficiency should be reframed to acknowledge that the advantage is driven by multi-task pre-training, not necessarily by tactile grounding.

2. **Planning experiments use only 5 trials per task with no confidence intervals or significance tests.** The zero-shot success rates in Figure 8 are averaged over five trials per task. For a binary outcome metric (success/failure), five trials yields a confidence interval of roughly ±30 percentage points at 50% success, making the reported differences (e.g., Stack Cubes: 75% vs. 83%) indistinguishable from noise. The contact perception experiments include t-tests; the planning experiments do not. While the consistent upward trend across all five tasks is suggestive, the quantitative precision of the claim "up to 35% higher success" is weaker than the paper's tone implies.

### Minor

3. **V-WM baseline construction is underspecified.** The paper never states whether the V-WM is the same architecture with the tactile encoder removed and retrained from scratch on the same multi-task data, or whether it is a different architecture altogether. This matters because it affects the interpretation of the comparison. If V-WM has fewer parameters, the advantage might partly come from model capacity. If V-WM was trained differently (e.g., different hyperparameters), the comparison is not a clean ablation. This should be clarified.

4. **Causal compliance degrades on "scribble with marker."** VT-WM shows worse normalized Fréchet distance (≈0.50 vs. ≈0.35) than V-WM on this task (Figure 6), meaning it hallucinates more static-object motion. The paper notes this is not statistically significant (t = −1.22, p = 0.23) but does not discuss *why* tactile input might hurt on this task. Some analysis or speculation would strengthen the paper's treatment of failure modes.

5. **Small trial count for data efficiency experiment (9 trials).** The plate-insertion task is evaluated over 9 trials. A difference of 77% vs. 22% (7/9 vs. 2/9 successes) is large enough to be compelling, but Fisher's exact test or a confidence interval would be a useful addition.

### Trivial

6. The caption on Figure 1 is repetitive — the same description appears three times in the extracted text (clearly a formatting artifact, but worth noting).

## Nice-to-Haves

- For the planning experiments, increasing to 10–20 trials per task and reporting Wilson score intervals or bootstrapped confidence intervals would substantially strengthen the quantitative claims.
- A failure-mode analysis for planning (e.g., does V-WM planning fail because it generates physically impossible trajectories, or because it loses track of objects?) would deepen the causal story the paper tells.
- The paper references a "multi-task dataset" and an appendix with training details (appendix A), but the main text provides no summary statistics (number of tasks, total trajectories, distribution of contact-rich vs. kinematic tasks). A brief table in the main paper would help readers assess potential confounds.

## Removed Points

- **Criticism about V-WM being unfair comparison if tactile inputs are zeroed out**: The paper does not state how V-WM is constructed, so this specific hypothetical is speculative. However, the underspecification itself is a real weakness (retained as Minor #3 above).
- **Criticism that 33% improvement is "heavily influenced by tasks with larger baseline errors"**: This is a description of how averaging works rather than a genuine weakness. The paper reports individual task numbers and the average.
- **Criticism about "absolute gains are modest for some tasks" on place fruits (Fréchet ~0.03-0.05)**: The comparison is relative and the paper provides per-task breakdown; this is not a weakness.
- **Strength Finder's generic strengths about problem importance**: Removed as superficial/sycophancy.
- **Strength about "data efficiency"**: Demoted because the experiment conflates multi-task pre-training with tactile grounding (see Major weakness #1).
- **Demand for theoretical proofs for an empirical systems paper**: Not standard in this community.
- **Demand for jointly trained encoder ablation**: Would be interesting but goes beyond reasonable scope.

## Novel Insights

The most interesting finding is not just that VT-WM outperforms V-WM — it's *where* it outperforms. The gains concentrate in tasks requiring sustained contact (wipe cloth: 70%→92%, reach & push: 69%→93%), while on free-space reaching both are perfect and on simple push the gain is modest (83%→92%). This pattern cleanly supports the paper's thesis: tactile grounding specifically helps where contact physics matters. The qualitative comparison in Figure 7 (hand moving above cloth without contact) is especially illuminating — V-WM hallucinates cloth motion while VT-WM correctly keeps it static — because it shows that the tactile signal is not just adding information but *disambiguating* states that look identical to a camera. This causal chain (tactile → better contact discrimination in imagination → better plans) is the paper's strongest conceptual contribution.

## Suggestions

- Reframe the data efficiency claims (abstract, conclusion) to acknowledge that the advantage over BC likely stems from multi-task pre-training rather than tactile grounding specifically, or add a V-WM fine-tuning baseline.
- For the planning results, add Wilson score intervals to the reported success rates and acknowledge the small sample size explicitly.
- Clarify the V-WM architecture and training procedure (trained from scratch? same architecture minus tactile encoder?).

## Score and Decision

**Calibration report:**
- Round 1 bracket: [4.0, 7.0]. Weak anchors at ≤3.0 (withdrawn/rejected papers on tangential topics), middle anchors at 4.0–7.0, strong anchors at 8.0 (different domains).
- Round 2 narrowing: anchors at 6.0 (DexMove, Accept; Ctrl-World, Accept) are the closest comparators — both are accepted papers with genuine contributions but clear limitations. The paper under review has stronger novelty than Ctrl-World (first visuo-tactile WM vs. incremental video-diffusion adaptation) but similar evaluation rigor. It is clearly stronger than WoW (4.0, Reject) and VLA-RFT (4.0, Reject).
- Final score: 6.0. Comparable to DexMove and Ctrl-World — solid contributions with real strengths and addressable weaknesses.

**Anchors consulted:**

| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| Nu1D2IsmWH | 3.00 | R1 | ViTacFormer (withdrawn) — weaker on all dimensions |
| SESeW4EvPd | 1.50 | R1 | Tangential topic, withdrawn |
| TLXp0scq3x | 2.50 | R1 | Tangential WM topic, withdrawn |
| cz6SbHgGEn | 3.00 | R1 | Tangential, withdrawn |
| Jaut99EHeu | 4.00 | R1 | VLA-RFT (Reject) — less novel, unconvincing gains |
| d6mwFoLkg2 | 4.00 | R1 | WoW (Reject) — incremental, missing baselines |
| yDmb7xAfeb | 7.00 | R1,R2 | World-In-World (Oral) — different contribution (benchmark), more rigorous |
| 2Pv41Ey3jK | 4.00 | R1 | Grasp stability prediction — narrower scope |
| dT3ZciXvNX | 6.00 | R2 | DexMove (Accept) — comparable quality, different contribution type |
| 4jcnded6fA | 5.33 | R2 | BiNoMaP (Reject) — narrower scope |
| StpFxymia9 | 5.00 | R2 | Manipulation Concept (Reject) — narrower, less novel |
| NQq9JLMfNN | 6.00 | R2 | 3D Scene Understanding (Accept) — different domain |
| ndilONnABZ | 6.50 | R2 | AnyTouch 2 (Accept) — tactile representation, different problem |
| 748bHL2BAv | 6.00 | R2,R3 | Ctrl-World (Accept) — comparable quality, less novelty |
| 80vjyj5o7l | 6.00 | R3 | DexNDM (Accept) — comparable quality, different domain |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>