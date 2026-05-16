Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper makes two contributions: (1) an empirical study challenging the common belief that DropEdge and DropMessage meaningfully reduce oversmoothing in GNNs, showing their effects are limited at test time and more akin to data augmentation; (2) Learn2Drop, a method that learns which message elements to drop via an information bottleneck (IB) formulation with a spike-and-slab variational distribution. The empirical study is largely sound and provides valuable counter-evidence to claims in prior work. The proposed method is interesting but its evaluation contains a structural flaw that undermines the central comparative claim.

## Strengths

1. **Empirical demonstration that DropEdge/DropMessage have limited effect on test-time oversmoothing.** Section 3.2 measures Dirichlet energy and MAD in 128-layer GCNs, showing that at test time (when no dropping is applied), the smoothing trend remains exponential and is not fundamentally altered. This directly challenges a key claim of the original methods. The careful discussion of metrics (Dirichlet energy's scaling sensitivity, MAD's limitations) adds credibility.

2. **Controlled experiment isolating the role of randomness in DropEdge.** Section 3.3's τ-variation experiment is well-designed: as dropping becomes more deterministic, accuracy degrades even though the DropEdge theorem is still satisfied. This provides strong evidence that DropEdge's benefits stem from noise injection / data augmentation rather than oversmoothing reduction. This is the paper's most original contribution.

3. **Nuanced stance on oversmoothing vs. generalization.** The paper explicitly states that "a GNN with little oversmoothing does not guarantee optimal performance" and that it is "trivial to minimize oversmoothing by dropping messages randomly at test time." This provides a useful counterpoint to the common assumption that less smoothing is always better.

4. **Interesting methodology with analytical KL.** The spike-and-slab parameterization and the closed-form KL divergence (Equation 8) are cleanly derived. The use of the Gumbel-Sigmoid trick for differentiable sampling is appropriate.

## Weaknesses

### Major

1. **Figure 3 compares Learn2Drop against baselines under fundamentally different test-time conditions, making the "superior oversmoothing reduction" claim unsupported.** In Figure 3, Learn2Drop is evaluated with learned dropping applied at test time, whereas DropEdge and DropMessage are evaluated *without* any dropping at test time (their standard inference mode). The paper itself acknowledges (line 83) that "enabling DropEdge and DropMessage at test time... reduce[s] oversmoothing." To support the claim that Learn2Drop is better at oversmoothing reduction, Figure 3 must include test-time enabled versions of DropEdge/DropMessage (random dropping at the same rate) as baselines. Without this, Figure 3 conflates the presence of a test-time intervention with method quality. The accuracy comparison in Table 1 does include test-time baselines, but the oversmoothing comparison — the primary evidence for the method's core advantage — does not. This is the paper's most consequential flaw.

### Minor

2. **The application of the Information Bottleneck across multiple layers lacks theoretical justification.** The paper applies the IB objective independently to the message matrix at selected layers (every layer or every ten layers). Each such application treats layers before ℓ as the encoder and layers after ℓ as the decoder, creating overlapping encoder/decoder boundaries. The paper does not discuss whether optimizing multiple such local IB objectives is equivalent to, or a valid relaxation of, a global IB, nor whether information discarded at one layer could be recovered later. This does not invalidate the method, and may work as a heuristic, but the IB framing is oversold.

3. **No ablation of the IB tradeoff parameter β.** β directly controls the compression-accuracy tradeoff but its value is not stated in the available text (likely deferred to a stripped appendix), and no sensitivity analysis is shown. The same applies to the shared spike probability *r* and slab bounds *a, b*.

4. **No ablation of the dropping frequency.** The paper uses two variants: dropping at every layer (L2D) and once every ten layers (L2D*). The choice of "every ten layers" is presented as a way to reduce overhead, but there is no ablation justifying this frequency or comparing it to alternatives.

5. **The randomness experiment (Section 3.3) is only shown on 3-layer models.** While understandable as a design choice for stability, extending the τ experiment to deeper models would strengthen the argument that randomness, not oversmoothing reduction, is DropEdge's key mechanism.

6. **Test-time baseline accuracy in Table 1 is reported as a mean over 10 forward passes because individual passes "often fail to converge."** The paper should report variance or failure rate for these baselines, as the mean over unstable passes may not reflect reproducible deployment behavior.

7. **The "missing feature" setting (90% zeros) is artificial.** The paper acknowledges following prior work, but should note that results may not transfer to standard feature distributions.

### Trivial

8. The text at line 80 has a typo ("reduciung") and line 217 has another ("emprical").

## Nice-to-Haves

- Adding test-time random dropping baselines to the oversmoothing comparison (Figure 3) is not a nice-to-have — it is required for the paper's core claim. It is listed as a Major weakness above.
- A brief discussion of the computational cost of the per-edge MLP inference for the Learn2Drop method, especially on large graphs, would be helpful context.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Parameter overhead / scalability (Harsh Critic Point 3).** The critic claims Learn2Drop learns "2|E|mL" parameters. However, the MLP that produces retention probabilities and slab locations is *shared across all edges* (line 168): a single MLP takes concatenated node features and outputs parameters for each message. The learnable parameters are the MLP weights, which scale with the MLP architecture, not with |E|×m×L. This criticism is factually incorrect.
- **Hyperparameter disclosure.** The critic notes that β, r, a, b, and MLP architecture are not given. The paper's original submission likely contained an appendix with these details; the parser strips appendix sections from all papers. Per policy, this criticism is removed.
- **GraphCON outperforms Learn2Drop.** The paper explicitly states (line 205) "Competing with the state-of-the-art techniques that address oversmoothing is not the objective. For completeness, we have included the recent method GraphCON." This is not a weakness — the paper scopes itself to dropping-based methods.
- **"Figure 3 conflates test-time intervention with method quality" framed as a minor issue.** This is correctly elevated to a Major weakness above.

## Novel Insights

The most insightful finding from the reviews is that the paper's central comparative claim about oversmoothing reduction rests on an asymmetric comparison: Learn2Drop is tested with test-time dropping while baselines are tested without it. The paper's own data show that enabling random dropping at test time *does* reduce oversmoothing, so the missing comparison in Figure 3 is not an oversight about baseline performance but a structural gap in the evidence chain. This reframes the paper's narrative: the real contribution is not that Learn2Drop reduces oversmoothing better than prior methods (that comparison hasn't been made fairly), but that Learn2Drop can apply learned test-time dropping that *simultaneously* reduces oversmoothing *and* maintains accuracy, whereas random test-time dropping sacrifices accuracy. The paper already has the data to support this refined claim (Table 1 shows exactly this), but Figure 3 and the text overreach.

## Suggestions

1. **Fix Figure 3.** Add test-time enabled (random dropping) versions of DropEdge and DropMessage as baselines in the oversmoothing comparison. If their curves overlap with Learn2Drop's, reframe the claim from "superior oversmoothing reduction" to "comparable oversmoothing reduction with stable predictions." If Learn2Drop achieves meaningfully less smoothing, that is interesting and should be highlighted.

2. **Clarify the IB objective's status.** Either provide a theoretical justification for applying IB at multiple overlapping layers (e.g., treating each layer as an independent Markov stage) or explicitly state that the IB is used as a per-layer regularizer/heuristic.

3. **Add ablations.** Show sensitivity to β (at least 2-3 values on one dataset) and justify the "every ten layers" frequency with a comparison to other intervals.

## Score and Decision

The empirical study in Section 3 is a solid, reproducible contribution. The Learn2Drop method is genuinely interesting, and the accuracy comparison in Table 1 is fair. However, Figure 3 — the primary evidence for the method's claimed superiority in oversmoothing reduction — compares Learn2Drop (with test-time dropping) against baselines (without test-time dropping), while the paper's own data show that random test-time dropping reduces oversmoothing. This structural flaw means the paper's central comparative claim is not supported by the presented evidence. The paper would benefit significantly from adding test-time baselines to Figure 3 and adjusting its claims accordingly. In its current form, the evidence does not justify the strength of the claims made in the abstract.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>