Now I have a clear picture. Let me write the final consolidated review.

## Summary

This paper proposes integrating n-gram induction heads (a mechanism from mechanistic interpretability of language models) into transformers for In-Context Reinforcement Learning (ICRL), building on Algorithm Distillation (AD). The authors show that n-gram attention layers improve data efficiency, accelerate hyperparameter search, and can be extended to pixel-based observations via vector quantization. The core idea is well-motivated: if induction heads are known to underpin in-context learning, hardcoding them should reduce the data and computation needed for ICRL.

## Strengths

1. **Novel and well-motivated architectural intervention for ICRL.** Applying n-gram induction heads—originally studied in language modeling (Akyürek et al.)—to the ICRL setting is a creative and principled idea. The paper correctly grounds this in the mechanistic interpretability literature (Edelman et al., Olsson et al.) and the known simplicity bias of transformers. This is the first work, to my knowledge, to make this connection in a decision-making context.

2. **Strong ablation studies.** Sections 4.4 and 4.5 are the paper's strongest empirical contribution. Ablations on n-gram length and layer position (Tables 1a, 1b) show the method is robust within a reasonable range. The permuted-mask experiment (Table 1c) demonstrates that a broken n-gram layer does not degrade performance—an excellent sanity check confirming the n-gram mechanism carries useful signal rather than acting as a noisy regularizer.

3. **Clear benefit over plain transformer in discrete grid-world ICRL.** Figures 2 and 4 consistently show that adding an n-gram layer substantially improves performance over the plain transformer baseline across varying data budgets in Dark Room and Key-to-Door. The faster convergence of Expected Max Performance (EMP)—~20 assignments vs. >400 in Figure 2—is a practically meaningful advantage for hyperparameter tuning.

4. **Rigorous evaluation methodology.** The use of EMP with random hyperparameter search (Dodge et al.), fixed batch size and gradient steps, and evaluation on held-out goals provides a fair and reproducible comparison that avoids cherry-picking and genuinely reflects training difficulty.

## Weaknesses

### Major

1. **The 27x data efficiency claim against Algorithm Distillation is unsubstantiated.** The paper's headline claim—that the method "needs 27x less data" than AD (Section 4.2, Figure 4 caption)—is based on a cross-paper comparison to published numbers from Laskin et al. [17], not on a controlled experiment. The data generation procedures differ: this paper uses table Q-learning for grid-world data, whereas AD originally used learning histories from RL algorithms trained from scratch. The paper's own experiments compare the n-gram transformer to a plain transformer on the *same* data (a fair ablation), but the 27x claim jumps to published AD numbers without controlling for the data distribution difference. A proper comparison would train AD on the same data or the proposed method on AD-generated data and plot performance vs. dataset size as a scaling curve. As presented, the 27x claim is an apples-to-oranges comparison that cannot be evaluated from the evidence provided. The abstract's statement that the approach "matches, and in some cases surpasses, the performance of AD" inherits this problem.

2. **Architectural confound in visual experiments.** Section 4.3 shows n-gram layers outperforming a baseline in Miniworld environments, but the paper does not specify the baseline's encoder architecture. The n-gram variant uses a pretrained VQ model with a ResNet encoder to produce discrete codes. If the baseline uses a standard convolutional encoder without this pretrained representation, the observed improvement could be partly or entirely due to the better encoder rather than the n-gram mechanism. This confound makes the visual results uninterpretable as evidence for the n-gram head's contribution. A controlled comparison where the *only* difference between baseline and n-gram variant is the n-gram attention layer (using the same encoder) is necessary.

3. **Absence of comparisons to other data-efficient ICRL methods.** The related work mentions data augmentation (Kirsch et al.), data filtering (Schmied et al.), and noise curricula (Zisman et al.) as approaches to the same data-efficiency problem, yet none of these are compared experimentally. The paper positions itself as addressing ICRL data efficiency but provides no baselines from this literature. While architectural and data-side approaches are complementary, readers cannot assess the relative merit of the proposed method without some empirical positioning.

### Minor

4. **Hyperparameter sensitivity claim conflates model quality with ease of tuning.** The paper frames faster EMP convergence as "reduced hyperparameter sensitivity" (Section 4.1). While the practical benefit—fewer assignments to find a good model—is real, the evidence primarily shows the n-gram model is *better* at the task, not that it is inherently less sensitive to hyperparameters. Demonstrating lower sensitivity would require showing reduced performance variance across hyperparameters or a broader optimal region, not just faster convergence of the maximum. The "quicker" convergence is a genuine practical advantage but is better described as faster/easier tuning rather than reduced sensitivity.

5. **The data scaling story is incomplete.** The paper claims data efficiency but only reports EMP vs. hyperparameter assignments, not the standard scaling curves of performance vs. dataset size (number of transitions or goals). Figure 1 does show return vs. # training goals, but this is a single fixed-hyperparameter experiment, not a controlled scaling curve that isolates data volume. The strongest way to demonstrate data efficiency is a plot of performance against dataset size for both methods under the same conditions.

### Trivial

6. **Figure 1 caption is misleading.** It reads "Performance comparison for different number of training goals between our method and Algorithm Distillation (AD)," but the plot actually compares their n-gram model to their plain transformer (not a direct AD replication). This imprecise wording feeds the overclaiming issue.

## Nice-to-Haves

- **Analyze what the n-gram matches actually capture**, especially in the visual domain. Showing examples of matching code blocks across rollouts would validate that the mechanism captures meaningful state repetition rather than acting as a noisy shortcut.
- **Include comparison on AD's original data generation pipeline** (RL algorithm learning histories) to directly validate whether the n-gram improvement transfers to the original setting.
- **Specify the visual baseline architecture** and, ideally, use the same VQ encoder for both baseline and n-gram variants to isolate the n-gram contribution.

## Removed Points

- *The harsh critic's point that the 27x claim "is not present in the experiments"* — this is factually wrong; the claim is in the Figure 4 caption and Section 4.2 text. The issue is not absence but insufficient support.
- *The harsh critic's framing of the visual experiments as "uninterpretable as evidence"* — this overstates; the results are still suggestive, just confounded. Demoted from "uninterpretable" to "confounded and requiring clarification."
- *The strength finder's claim that the paper "matches or surpasses Algorithm Distillation with 27× less training data" as the single strongest piece of evidence* — this is not supported by controlled experiments; it is a cross-paper comparison and should not be treated as established.
- *Formatting/style nitpicks from both reviewers* (grammar, capitalization, whitespace artifacts from PDF parsing) — removed per instructions.
- *Generic "this paper addresses an important problem" praise from the strength finder* — removed as non-specific.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the mechanistic interpretability literature (induction heads, n-gram attention) provides strong *a priori* motivation for architectural interventions in in-context learning, but this paper's difficulty in rigorously validating those interventions (cross-paper comparisons, confounded visual experiments) illustrates how hard it is to bridge the gap between interpretability-derived insights and empirically sound system-building. The permuted-mask ablation (Section 4.5) stands out as a particularly clean experimental design that other architectural papers should emulate.

## Suggestions

1. **Run a controlled comparison with AD on the same data.** Train both the n-gram model and a faithful AD implementation on identical data (either both on table Q-learning data, or both on AD's original RL-history data). Report performance vs. dataset size as a scaling curve.
2. **Fix the visual baseline.** Specify the encoder architecture for both baseline and n-gram variants. Ideally, use the same VQ encoder for both, with the *only* difference being the n-gram attention layer.
3. **Tone down the claims in the abstract and introduction.** Replace "matches, and in some cases surpasses, the performance of AD" with a more precise statement about improving upon a plain transformer baseline and showing promising trends relative to published AD results.
4. **Include at least one data-efficiency baseline** from the methods discussed in Related Work (e.g., data augmentation or filtering under the same low-data regime).

## Score and Decision

**Final Score:** 5.0

**Decision:** Reject

**Scoring rationale and calibration:**

- *Bracketing pass (Round 1):* Papers scoring <3.5 had fundamental flaws or near-incoherent contributions; this paper's core idea is sensible and the ablations are solid, placing it above that band. Papers scoring >7.5 (e.g., Retrieval Head at 8.0, Vision Transformers Need Registers at 8.0) have clean, well-supported contributions with no comparable overclaiming issues. Initial bracket: 4.0–6.5.

- *Narrowing pass (Round 2):* Anchors used for calibration:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Memory-Efficient AD (5iWim8KqBR) | 5.50, Reject | R1, R2 | Similar in topic and execution level; both propose architectural modifications for AD. My paper has a more novel idea (n-gram heads vs. evaluating existing efficient transformers) but similar overclaiming issues and missing comparisons. **Slightly weaker than this anchor.** |
| Subwords as Skills (sAOtKKHh1i) | 5.00, Reject | R2 | Different topic (tokenization for RL), similar score tier. Comparable level of experimental support. **Comparable.** |
| Farzi Data (H9DYMIpz9c) | 5.00, Reject | R2 | Data distillation paper; similar in having a useful idea but gaps in experimental validation. **Comparable.** |
| Optimizing KD in Transformers (QDkPAV9Fa5) | 5.75, Reject | R2 | Knowledge distillation paper; slightly stronger experimental framing. **Slightly weaker than this anchor.** |
| Transformers Learn TD Methods (Pj06mxCXPl) | 6.67, Accept | R2 | Stronger theoretical contribution (proofs) that compensates for limited experiments; accepted despite narrow scope. My paper has more experiments but no comparable theoretical depth and weaker central claims. **Weaker than this anchor.** |
| ICEE (uIKZSStON3) | 7.25, Accept | R1, R2 | Cleaner experimental validation of a novel ICRL algorithm. My paper's core idea is similarly novel but the evidence is weaker. **Weaker than this anchor.** |
| Actions Speak Louder Than States (b5MCteb3w7) | 4.75, Reject | R3 | ICRL paper with similar environment scope but different focus. **Comparable, slightly stronger.** |
| RATE (c4w7WVs1z7) | 4.75, Reject | R3 | Transformer memory for RL; similar level of contribution and experimental validation. **Comparable.** |

The paper sits just below the 5.5 anchor (Memory-Efficient AD), which itself was rejected for limited novelty and missing comparisons. My paper's core architectural idea is more novel than that anchor, but its central quantitative claim (27x over AD) is not properly supported, and the visual experiments have a confound that the weaker anchor does not share. These issues pull the score down to 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>