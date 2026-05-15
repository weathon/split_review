Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces a reward-free pre-training paradigm for GFlowNets by training an outcome-conditioned GFlowNet (OC-GFN) that learns to reach any target outcome via self-supervised exploration (using a GAFlowNet for diverse outcome generation, contrastive training with off-policy successful trajectories, and "outcome teleportation" to distribute terminal reward signals). For downstream adaptation, the paper derives a conversion formula (Eq. 6) that can in principle yield a policy for any new reward without retraining, and proposes an amortized predictor to efficiently approximate an otherwise intractable marginalization. Experiments on GridWorld, bit sequence generation, TF Bind, RNA, and AMP design show that the pre-trained OC-GFN achieves high outcome-reaching success rates, and that the downstream adaptation discovers more modes than training a GFlowNet from scratch.

## Strengths

- **Novel framework for reward-free pre-training of GFlowNets.** The idea of conditioning GFlowNet flows and policies on an outcome variable and pre-training to reach any outcome is a natural and underexplored direction that opens the door to transfer learning in GFlowNets. The combination of contrastive training (using off-policy successful trajectories from GAFN) and outcome teleportation (distributing terminal rewards across all edges) is a technically interesting solution to the sparse-reward challenge inherent in this setup.

- **Ablations cleanly isolate the contribution of key components.** GridWorld experiments (Fig. 3b–d, described in lines 310–315) and bit sequence ablations (lines 334–336) show that disabling outcome teleportation reduces success rates, and additionally disabling contrastive training causes failure in larger spaces. This provides concrete evidence that both techniques are essential, not incremental.

- **Consistent mode-discovery improvements across diverse real-world domains.** On TF Bind (30 tasks), RNA (4 tasks), and AMP (20⁵⁰ space), the proposed downstream adaptation consistently discovers more modes and achieves higher top-K scores than training a GFlowNet from scratch. The t-SNE visualization for TF Bind (Fig. 6e) further shows that the pre-trained policy covers regions missed by scratch training.

- **Proposition 2 provides a clean fixed-point characterization of the amortized predictor.** While conditional on convergence (loss=0, full support over outcomes), Proposition 2 shows that if the amortized loss is zero, the numerator network \(N(s'|s)\) correctly estimates the required sum, connecting the practical training algorithm to a well-defined theoretical target.

## Weaknesses

### Fatal
None.

### Major

- **"Fine-tuning" terminology is misleading — the OC-GFN parameters are never updated in the adaptation stage.** Section 4.2 frames the process as "fine-tuning" and Algorithm 2 is titled "Supervised Fine-Tuning of Outcome-Conditioned GFlowNets," yet the OC-GFN's flows \(F(s|y)\) and policy \(P_F(s'|s,y)\) remain frozen. What is actually trained is a separate amortized predictor (networks \(N\) and \(Q\)) from scratch. This is a form of *distillation* or *amortization* that leverages the frozen pre-trained model as a source of training signal, but it is not fine-tuning in the standard sense (where the pre-trained parameters themselves are updated). The paper's significant results are not diminished — the amortized predictor is a legitimate contribution — but the framing overstates the connection to the pre-train-then-fine-tune paradigm. A proper fine-tuning ablation (updating OC-GFN parameters on the downstream reward) is absent, making it unclear whether the proposed approach is the best way to leverage the pre-trained model.

- **Experimental comparisons do not control for total compute between pre-training+adaptation vs. training from scratch.** The pre-training stage requires training both a GAFN and the OC-GFN for many steps. In all experiments, the "GFN from scratch" baseline is trained for a fixed number of steps without accounting for the pre-training budget. A fair comparison would either (a) train the scratch GFN for the *same total number of environment steps* (pre-training steps + adaptation steps) to assess whether the improvement is due to pre-training or simply more compute, or (b) demonstrate that the pre-trained model reaches a given performance level with strictly fewer total interactions. Without this control, the claim of "efficient adaptation" is not fully supported by the evidence presented.

- **The loss function for outcome teleportation (Eq. 7) has an undefined term for unsuccessful trajectories.** The loss uses \(\log R(x|y)\), where \(R(x|y) = \mathbb{1}[x = y]\). When the trajectory does not reach the target outcome, \(R=0\) and \(\log 0\) is undefined. The paper does not discuss how this case is handled in practice (e.g., only applying the loss to successful trajectories, using the non-log version of the constraint for zero-reward cases, or adding an epsilon). Since the success of the pre-training stage depends critically on this loss, the omission is a nontrivial gap in the technical specification.

### Minor

- **GridWorld distribution-matching results (Fig. 3) are purely qualitative.** The paper shows visual heatmaps of samples from the converted/amortized policies and claims they match the target distribution, but reports no quantitative divergence measure (e.g., KL divergence, L1 error, correlation). For such a small and fully controllable environment, this is a missed opportunity to rigorously validate that Eq. (6) and the amortized predictor actually yield the correct distribution.

- **Variance reporting is inconsistent across experiments.** GridWorld reports 3 seeds with mean and standard deviation (line 293), and bit sequence success rates include \(\pm\) values (98.37±0.33%, etc.). However, for TF Bind, RNA, and AMP downstream adaptation results, the text does not specify whether results are averaged over multiple seeds or show error bars. This makes it difficult to assess the statistical reliability of the claimed improvements on real-world tasks.

- **Proposition 1 is stated too weakly relative to what is needed.** It claims the policy "can successfully reach" the target outcome, whereas the downstream conversion formula (Eq. 6) requires that the terminal distribution given \(y\) be *exactly proportional* to \(\mathbb{1}[x = y]\). While the mathematics of Eq. (6) does imply this stronger property (trajectories ending in \(x \neq y\) have zero flow), the proposition as written does not state this, and the connection to the needed distributional property is left implicit.

- **No convergence analysis of the coupled \(N\)-\(Q\) training loop.** Learning \(N(s'|s)\) requires sampling outcomes \(y\) from \(Q(y|s',s)\), which itself depends on \(N\). This is a self-consistency loop reminiscent of bootstrapping. While this kind of structure is standard in GFlowNet training (DB, TB, etc.) and the paper uses tempered/\(\epsilon\)-greedy exploration for practical stability, there is no analysis of whether (or under what conditions) this coupled training converges to the correct fixed point.

### Trivial
- The phrase "swiftly adapt" in the abstract is vague and not standard in the GFlowNet literature.
- The description of the contrastive training procedure (lines 155–160) could be clearer about why both the off-policy positive trajectory and the on-policy trajectory are used in each step; the explanation is present but brief.

## Nice-to-Haves
- On GridWorld, report the KL divergence or correlation between the target distribution and the distributions obtained from the MC-based conversion and the amortized predictor.
- Include a comparison against a "properly fine-tuned" OC-GFN (updating its own parameters on the downstream reward) to gauge whether the amortized predictor approach is necessary or merely sufficient.
- Provide convergence diagnostics for the amortized predictor loop (e.g., comparing \(N\) estimates to Monte Carlo estimates at a fixed set of states).

## Removed Points

These points were flagged by reviewers but removed or weakened after verification against the paper:

1. **"Core theoretical claim is not adequately justified"** — The reviewer claimed that Eq. (6) does not guarantee the required distributional property from the proposed training objective. *Removed as factually incorrect.* The constraint \(F(s|y)P_F(s'|s,y) = F(s'|y)P_B(s|s',y)R(x|y)\) with \(R(x|y)=\mathbb{1}[x=y]\) forces zero flow through trajectories ending in \(x\neq y\) and standard DB for trajectories ending in \(x=y\), yielding the correct terminal distribution. This follows directly from GFlowNet foundations; the reviewer's concern stems from a misreading of the equation's effect.

2. **"The proof is omitted entirely"** (about Proposition 1) — *Removed per instructions: the parser strips appendix material; proofs exist in the original submission.*

3. **"Missing related works"** — *Removed per instructions: we cannot verify missing references.*

4. **"Poor formatting (abstract only, no proper figure/table placement)"** — *Removed as a parser artifact, acknowledged as such by the reviewer.*

5. **"Full open-source release of code... noted as missing because appendix stripped"** — *Removed per instructions; the appendix may have contained this information.*

6. **Strengths from Strength Finder removed as generic or conflicting:** "The paper tackles a real gap in the GFlowNet literature" — generic; "This work may serve as a foundation for further exploration" — generic aspiration from the paper's own text. Also, several "Missing Experiments" suggestions from the "Missing Parts" section of the harsh review were either superseded by verified weaknesses or were overly demanding for a single paper.

## Novel Insights

Beyond the paper's own contributions, the most notable synthesis from the reviews is a recurring tension: the paper claims to bring the "pre-train then fine-tune" paradigm to GFlowNets, but the actual machinery is better described as "pre-train then amortize." The pre-trained OC-GFN is used as a frozen feature extractor / teacher signal for a separately learned amortized predictor, rather than having its own parameters updated for the downstream task. This distinction matters because the GFlowNet community has been moving toward parameter-efficient adaptation, and a genuinely fine-tuned OC-GFN (updating \(F(s|y)\) and \(P_F(s'|s,y)\) on the new reward) may achieve even better transfer. Conversely, the amortized predictor approach has the advantage that it avoids catastrophic forgetting of the pre-trained outcome-reaching capability. The paper does not explore this trade-off, which would be a natural direction for future work.

## Suggestions

1. **Rename the adaptation stage.** Drop "fine-tuning" and use "amortized adaptation" or "distillation-based adaptation" to accurately describe what Algorithm 2 does. Include an ablation comparing amortized adaptation against actual fine-tuning of the OC-GFN parameters.

2. **Fix the loss function specification.** Clarify how the loss in Eq. (7) is computed when \(R(x|y)=0\) (e.g., only applying it to successful trajectories, or using a different loss for zero-reward cases).

3. **Add a compute-controlled comparison.** For at least one task (e.g., bit sequence), run the "GFN from scratch" baseline for the same total number of environment steps as the full pipeline (pre-training + adaptation) and report the mode-discovery curves.

4. **Add quantitative distribution matching on GridWorld.** Report KL divergence or correlation for both the MC-based conversion and the amortized predictor against the target distribution.

5. **Specify the number of seeds and report variance for all experimental results**, particularly the TF Bind, RNA, and AMP downstream adaptation figures.

## Score and Decision

The paper presents a genuinely novel approach to pre-training GFlowNets, supported by technically interesting innovations (contrastive training, outcome teleportation) and consistent empirical improvements across multiple domains. The core theoretical machinery is sound, following from established GFlowNet principles, and the amortized predictor provides a practical solution to an intractable marginalization. The main weaknesses are in terminology (the adaptation method is not fine-tuning), incomplete experimental controls (total compute not balanced, variance not fully reported), and some technical imprecision in the loss function specification. None of these issues are fatal; they are addressable in a revision. The paper makes a meaningful contribution to the GFlowNet literature and opens a productive new direction for pre-trained generative samplers.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>