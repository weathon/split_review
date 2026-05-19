- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed for a thorough, verified consolidation. Let me produce the final review.

## Summary

The paper redefines the missing-modality problem as a test-time adaptation (TTA) task and introduces MiDl (Mutual information with self-Distillation), an online, self-supervised method that adapts a pretrained multimodal model to test streams with missing modalities. MiDl minimizes the mutual information between predictions and available modality type (to build modality invariance) while using KL self-distillation (to preserve performance on complete-modality inputs). The method updates the model only when a complete-modality sample arrives, and is architecture-agnostic. Experiments on Epic-Kitchens, Epic-Sounds, and Ego4D under various missing rates show consistent improvements (e.g., 5–7% on Epic-Kitchens) over both the non-adapted baseline and prior TTA methods (SHOT, ETA).

## Strengths

- **First principled formulation of missing modality as a TTA problem.** The paper explicitly frames missing modalities as a distribution shift occurring at test time (Section 3.1) and defines an online evaluation protocol (Section 3.2). This is a genuinely novel framing that distinguishes MiDl from prior missing-modality approaches that all require access to training data and retraining.

- **Consistent, non-trivial performance gains across diverse settings.** Table 1 shows MiDl improves over the non-adapted baseline by 5% and 7% on Epic-Kitchens at 50% and 75% missing rates, and 1.7% and 1.5% on Epic-Sounds at the same rates — all achieved through online, self-supervised adaptation without any retraining. Gains are also demonstrated on a different backbone (self-attention, Table 3), with Omnivore pretraining (Table 5, 9.5% gain at 25% missing rate), and under different missing-modality types (Table 4).

- **Architecture-agnostic and pretraining-agnostic validation.** MiDl is tested with MBT (primary), vanilla self-attention (Section 6.1), and Omnivore (Section 6.3), showing consistent improvements across all three. This directly supports the claim of architecture agnosticism.

- **Ablation cleanly demonstrates the necessity of both components.** Table 6 shows that KL-divergence alone produces no adaptation (as expected — it only encourages staying close to the frozen model) and MI alone degrades performance at low missing rates. MiDl's combination consistently outperforms both, providing clear evidence for the joint design.

- **Honest computational cost analysis.** Section 6.5 quantifies the 5× forward-pass overhead and notes that in practice latency is only ~2× due to parallelism, without downplaying the trade-off.

## Weaknesses

### Fatal

None.

### Major

None that threaten the core claims. The paper's contributions are well-supported.

### Minor

- **The method cannot adapt when the test stream has zero complete-modality samples ($p_{AV}=0$).** The paper explicitly assumes $p_{AV} \neq 0$ (line 77) and frames this as the multimodal setting. This is a genuine scope limitation: any test stream that is entirely unimodal receives no benefit from MiDl beyond the baseline. The paper acknowledges this and reports $p_{AV}=0$ results, but the limitation is structural rather than incidental. Practitioners deploying on purely unimodal streams would need a different approach.

- **The $\mathcal{L}_{\mathrm{ent}} = \mathcal{L}_{\mathrm{div}}$ justification for skipping incomplete samples is asserted without empirical verification.** The paper states (line 71) that under incomplete modality $\mathcal{L}_{\mathrm{ent}}=\mathcal{L}_{\mathrm{div}}$ so $\mathcal{L}_{\mathrm{MI}}=0$, justifying the decision to skip adaptation. However, for an incomplete sample (say audio-only), the three forward passes (A, V, AV with zero-filling) would generally produce different predictions, so the equality does not strictly hold. While skipping adaptation on incomplete samples is intuitive and likely harmless, the mathematical justification as stated is imprecise.

- **The LTA experiment (Section 5.3) uses a subset of training data, which departs from the pure TTA framing.** The paper's general formulation (Section 3) assumes adaptation occurs on an unlabeled test stream without access to training data. The LTA setting uses $S_{\mathrm{in}}$, a subset of the *training* data, for adaptation before evaluation on the validation set. This is a practically interesting scenario (self-supervised adaptation on unlabeled training data) but it is a different protocol from online TTA. The paper clearly separates this in its own section and labels it "Long-Term Adaptation," but referring to it broadly under "test-time adaptation" in the takeaway (line 132) somewhat blurs the boundary.

- **The computational cost claim about parallelism assumes sufficient GPU memory.** The paper states (Section 6.5) that MiDl is only "2× slower" because the four additional forward passes "can be performed in parallel." This is architecture- and batch-size-dependent and assumes enough GPU memory to hold all four forward passes' intermediate activations simultaneously. The paper should qualify this with the specific hardware configuration used.

- **Error bars are deferred to the appendix (Table 11).** For a method involving online stochastic updates, variance across stream orderings or random seeds is important context for the reported gains (e.g., the 7% gain on Epic-Kitchens at 75% missing rate). Reporting standard deviations in the main tables would increase confidence.

- **No analysis of how many adaptation steps (complete-modality samples) are needed to reach the reported improvements.** The paper varies missing rates but does not characterize, e.g., the minimum number of complete-modality samples required to achieve a meaningful gain. This would help practitioners assess viability with short test streams.

### Trivial

- **The ablation observation that "$\mathcal{L}_{\mathrm{KL}}$ alone results in no adaptation" is not a finding** — it is a direct consequence of the KL objective (which encourages staying close to the frozen model) and is already explained in the paper's own caption for Table 6. The text could simply note this rather than presenting it as a discovery.

## Nice-to-Haves

- A controlled experiment varying $p_{AV}$ in finer steps (e.g., 10% intervals) to characterize the diminishing-returns point — the paper could then state "MiDl requires at least X% complete-modality samples to achieve meaningful improvement."
- A brief discussion of the zero-filling assumption: different multimodal architectures may handle zero-filled inputs differently (some could produce degenerate features), and MiDl implicitly requires the model to tolerate this.
- Including the standard-deviation rows from Table 11 into the main tables for reader convenience.

## Removed Points

These points from the inputs were removed with brief justifications:

- **"Weak comparison baselines — missing-modalisty token-based methods not compared"** (Harsh Critic, Critical Issue 3): The token-based methods cited (Lee et al., 2023; Ramazanova et al., 2024) require retraining with learnable tokens, which the paper explicitly scopes out ("without retraining"). Comparing against methods that require training data access is outside the paper's stated setting. The paper appropriately compares against other *test-time* adaptation methods (SHOT, ETA) and the non-adapted baseline.

- **"LTA conflates pure TTA and inflates apparent gains"** (Harsh Critic, Critical Issue 2): The paper presents LTA in its own clearly labeled section (5.3), separately from the pure TTA results (Section 5.2). Tables 1 and 2 are also separate. The experimentation is not conflated; the framing is differentiated, though the "test-time adaptation" umbrella term could be slightly tighter.

- **"Table 1 ambiguous about $p_{AV}=0$ entry"** (Harsh Critic, Section-by-Section): The experimental setup (line 97) specifies $p_{AV} \in \{0.0, 0.25, 0.5, 0.75, 1.0\}$ and the method section (line 77) explicitly states "we also report results with $p_{AV}=0$." The ambiguity the critic reports is a parser artifact from missing table images — the paper clearly addresses this.

- **"Ego4D warm-up complicates the central claim"** (Harsh Critic, Section-by-Section): The warm-up experiment is clearly presented as a distinct scenario (Section 5.4) separate from the main TTA results. The paper does not blend it into the core TTA claim.

- **"MiDl claim about 'all existing approaches necessitate expensive retraining' is an overstatement for token methods"** (Harsh Critic, Critical Issue 3): Training even lightweight token additions still requires access to training data and model retraining — the paper's statement is accurate. The criticism was based on a different interpretation of "retraining."

- Several "Strengthening the Paper" suggestions and "Missing Parts" items that overlap with retained weaknesses are consolidated into Minor/Nice-to-Have rather than treated as separate weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- In Section 4, either remove the claim that $\mathcal{L}_{\mathrm{ent}}=\mathcal{L}_{\mathrm{div}}$ for incomplete inputs, or replace it with a brief empirical check (e.g., "In practice we found $\mathcal{L}_{\mathrm{MI}} < \epsilon$ for incomplete samples") to avoid an imprecise mathematical claim.
- Add a one-sentence qualification to the "2× slower" computational cost claim with the GPU model and batch size used in the measurement.
- Add a sentence in the conclusion clearly stating the $p_{AV} \neq 0$ scope requirement, rather than burying it in the method section.
- Structure the paper's takeaways around three crisply separated protocols: (i) pure online TTA, (ii) pre-deployment adaptation on unlabeled in-domain data, and (iii) pre-deployment adaptation on out-of-domain data. This is already largely done but could be reinforced.
