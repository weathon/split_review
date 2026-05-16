Now I have a thorough understanding of both the paper and the reviews. Let me construct the final consolidated review.

## Summary

This paper proposes DISTA, a test-time adaptation (TTA) method that accelerates adaptation to distribution shifts by adding an auxiliary task on clean unlabeled source-domain data. The auxiliary task distills the predictions of the original pretrained model on source data during adaptation. The paper also explores a federated TTA scenario where multiple models adapted to related domain shifts collaborate. The method is evaluated on ImageNet-C and ImageNet-3DCC under episodic, continual, and federated protocols, reporting improvements over prior state-of-the-art EATA (1.5% episodic, 6% continual, 6% federated).

## Strengths

- **Principled lookahead analysis validates the auxiliary task concept**: The paper introduces a lookahead metric (Eq. 4, Figures 1a-1b) to quantitatively measure how an auxiliary step on source data improves the target TTA objective on corrupted data. Both a simple entropy auxiliary and DISTA's distillation auxiliary show consistently positive lookahead across all observed batches, providing independent justification for the approach before the main experiments.

- **Consistent and substantial improvements across multiple protocols and benchmarks**: DISTA outperforms prior methods across all three evaluation protocols on ImageNet-C: +1.5% (episodic, Table 1), +6% (continual, Table 3), and +6% (federated, Table 5) average error reduction over EATA. Similar gains hold on ImageNet-3DCC (Tables 2, 4). The improvements span individual corruptions (e.g., +2% on shot noise, +10%+ on snow/motion blur in continual evaluation).

- **Auxiliary task prevents source-domain forgetting**: In continual evaluation (Table 3), DISTA improves performance on the clean ImageNet validation set by >6% compared to EATA, nearly recovering to the non-adapted model. This directly demonstrates that the distillation auxiliary provides stable adaptation without catastrophic forgetting, a known weakness of prior TTA methods in continual settings.

- **Robustness across architectures, batch sizes, and computational budgets**: Figure 2c shows consistent gains across ResNet-18, ResNet-50, ResNet-50-GN, and ViT (e.g., +7% over SAR on ViT). Figure 2b shows DISTA outperforms EATA across batch sizes 8–64 (e.g., >15% improvement at batch size 8). Figure 2a demonstrates graceful degradation: even at 50% auxiliary updates, DISTA still gains 1.4% over EATA.

- **Establishes a federated TTA benchmark**: The paper systematically evaluates TTA in a federated setting where multiple models observe different non-overlapping subsets of corrupted data, showing that federated averaging improves all methods, and DISTA-F achieves a further 6% improvement over EATA-F.

## Weaknesses

### Fatal
None.

### Major

- **Missing controlled baseline to isolate the effect of distillation vs. merely having additional data and a gradient step.** DISTA uses an extra gradient step on unlabeled source data. The main baselines (EATA in Tables 1–5) do not receive this extra step. While Section 4.4.3 shows that adding a simple entropy auxiliary to Tent (Aux-Tent) yields 0.6% improvement and to SHOT (Aux-SHOT) yields 4% improvement, the paper never provides the key controlled comparison: **EATA + entropy auxiliary on source data (Aux-EATA)**. Since EATA is the primary baseline for the paper's headline improvements (and is stronger than Tent), we cannot determine from the current experiments whether DISTA's gains come from the distillation objective specifically, or from the simple fact of having an additional optimization step on clean data. The lookahead analysis (Figure 1b vs. 1a) suggests distillation may be better, but this is diagnostic evidence, not a direct experimental comparison. Adding Aux-EATA (ideally with both an entropy auxiliary and a distillation auxiliary for EATA) would substantially strengthen the paper's central claim.

### Minor

- **No variance or confidence intervals reported for any main result (Tables 1–5).** Given the stochasticity in data selection (λ_t, λ_s) and the online nature of the evaluation, reporting standard deviations (e.g., over multiple runs or corruption subsets) would increase confidence. This is standard practice in the TTA literature.

- **Size and composition of D_s (source memory) are not specified.** The paper only states "a randomly selected subset of ImageNet training set" (line 133). The total number of images stored, how they are selected/sampled per step, and how sensitive the method is to this size are critical for reproducibility and practical deployment. D_s is a core component of the method; its specification should be precise.

- **Asymmetry in data selection weights λ_t vs. λ_s is not explained or ablated.** Equation 4 shows λ_t uses both an entropy threshold condition and a cosine similarity (redundancy) condition, while λ_s uses only the entropy threshold. The paper does not discuss this design choice. Given that the source data is clean (unlike the corrupted stream data), the different treatment may be justified, but the paper should at minimum state the rationale and ideally ablate the effect.

- **The lookahead analysis (Section 2.1) is conducted on only 3 corruptions and one architecture (ResNet-50).** While this is a diagnostic tool rather than a main result, generalizing the lookahead pattern to all 15 corruptions and other architectures (especially ViT) would strengthen the methodological motivation.

- **Memory and latency numbers are not reported for the parallel update variant (Section 4.4.1).** The paper notes the parallel approach doubles memory but does not report concrete numbers. For a method that adds computational cost, quantitative efficiency measures would help practitioners.

### Trivial
None.

## Nice-to-Haves

- A comparison against a centralized baseline in the federated setting (a single model that sees all clients' data) would contextualize the value of federation, though this is not necessary for the paper's actual claim (federation helps vs. local-only adaptation, which IS demonstrated).
- Discussion of communication costs and privacy implications in the federated setting would be useful.
- A sensitivity analysis on the size of D_s would help practitioners understand the method's data requirements.

## Removed Points

- **"The paper does not clearly state that it assumes access to unlabeled source data during test time"** — Factually incorrect. The abstract (line 4) states "we leverage unlabeled data from the training distribution," and the introduction (line 14) repeats this clearly. The paper is explicit about this assumption.
- **"All baseline methods are evaluated without such auxiliary data"** — Misleading. EATA (the primary baseline) already uses D_s for its anti-forgetting regularizer (line 48), though not as a separate gradient step. The paper's comparison is between different uses of source data, not between having/not having access to source data.
- **"The federated evaluation does not isolate the effect of federation" / demand for a centralized baseline** — The paper's claim is that "federated adaptation provides consistently lower error rates than adapting each client solely on their own local stream" (line 171), which IS demonstrated by the M=4 vs. M=0 comparison in Table 5. Demanding a centralized baseline addresses a different question (whether federation beats centralized training) that is outside the paper's stated scope. This is not a weakness in the paper's actual claims.
- **"The method is unfair because it uses more data/computation"** — This is not a weakness per se; using additional resources is acceptable if the resource assumption (access to unlabeled source data) is clearly stated and the method provides value. The real issue (covered in Major) is the missing ablation to isolate whether distillation specifically matters beyond any auxiliary task.
- **Formatting/style nitpicks** — Removed per instructions.

## Novel Insights

The key insight from the review process is that the paper's most significant experimental gap (missing Aux-EATA baseline) mirrors a broader challenge in TTA research: as methods increasingly incorporate source data or auxiliary computations, the community needs controlled baselines that disentangle the effect of extra computation from the effect of the specific objective. The paper's lookahead analysis is a good step in this direction, but the experiments would benefit from clearer causal isolation. Beyond this, the paper's contributions — the distillation auxiliary, the federated TTA evaluation, and the robustness analysis — are solid and well-supported.

## Suggestions

1. **Add Aux-EATA:** Run EATA with the same auxiliary setup (extra gradient step on source data) using (a) entropy minimization and (b) distillation as the auxiliary objective. This directly isolates whether DISTA's gains come from distillation or merely from the extra data/computation.

2. **Specify D_s:** Clearly state the size of the source memory (number of images) and how batches are sampled from it. Add a sensitivity study on D_s size.

3. **Report standard deviations** for the main tables (at least for the average over corruptions).

4. **Explain the λ_t vs. λ_s asymmetry** in the data selection functions, and ablate the cosine similarity condition for the stream branch.

5. **Extend the lookahead analysis** to more corruptions and at least one additional architecture (e.g., ViT) to confirm the pattern generalizes.

## Score and Decision

The paper proposes a well-motivated method with consistent gains across multiple benchmarks, protocols, and architectures. The main weakness is a missing controlled baseline (Aux-EATA) that would cleanly attribute the improvement to the distillation objective rather than the additional computation/data. This is a significant but fixable gap — it weakens the attribution of causality, not the validity of the observed improvements. The paper's strengths (consistent gains, principled diagnostic analysis, robustness evaluation, novel federated TTA analysis) outweigh this weakness. With the addition of the appropriate control experiment, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>