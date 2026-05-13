Now let me run calibration search and continue reading the paper simultaneously.Now let me read two calibration anchors in full before writing the review:Now I have enough to write the comprehensive final review.

---

## Summary

PEARL introduces a distributionally robust optimization (DRO) framework for improving LLM robustness against permutations of in-context learning demonstrations. The core mechanism is a Hard Permutation Mining Network (P-Net) that uses the Sinkhorn algorithm (a differentiable OT solver) to generate adversarial orderings of demonstrations, combined with minimax adversarial training to harden the LLM against them. The paper evaluates this in two regimes: a controlled synthetic setting (in-context linear regression with GPT-2 trained from scratch) and instruction tuning of real LLMs (LLaMA, Mistral, Gemma).

---

## Strengths

- **Principled DRO formulation as the ambiguity set**: The paper formally defines the ambiguity set Q as the convex hull of all permuted empirical distributions (Equations 6–8, Section 4.1) and frames the robustness problem as a minimax over this set. This is a clean, principled abstraction that is distinct from ad hoc augmentation and correctly targets worst-case permutation performance.

- **Consistent worst-case AND average-case improvements over ERM+DS in Section 6**: Table 2 shows that PEARL outperforms not only ERM but also ERM+DS (random demonstration shuffling) across all LLMs tested, with worst-case gains of 14.2–29.4% and average gains of 5.7–9.8% on LLaMA-3-8B over four held-out tasks. The comparison to ERM+DS is included (Section 6.1) and establishes the adversarial mechanism contributes beyond data augmentation alone in the real setting.

- **Cross-model generalization across five architectures**: Section 6.1 and Appendix E report experiments on LLaMA-3-8B, LLaMA-2-7B/13B, Mistral-7B, and Gemma-7B, showing the benefit is not model-specific.

- **Complementarity with inference-stage methods**: The paper demonstrates that combining PEARL with CurStable yields an additional 3–5% improvement over either method alone (Section 6.2), establishing that the training-time and inference-time approaches address different aspects of the problem.

- **Many-shot generalization**: Figure 5 shows PEARL achieves 24–40% worst-case gains when evaluated on larger shot counts than those seen during training, suggesting the learned robust features generalize to unseen combinatorial spaces.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing ERM+DS baseline in Section 5 (synthetic experiment)**: Section 5.2 uses only ERM+CL as the baseline (following Garg et al., 2022). Random demonstration shuffling (ERM+DS) is the most natural cheap alternative for improving permutation robustness. While ERM+DS *is* included in Section 6 (where PEARL outperforms it), the synthetic Section 5 experiment—which is used to validate the mechanism in a fully controlled, enumerable setting—never rules out that a simple augmentation baseline performs comparably. Without this comparison in the regime where worst-case performance is exactly computable, it is unclear how much the P-Net's adversarial machinery contributes over basic shuffling in the synthetic domain.

- **FLAN-large P-Net creates an uncontrolled knowledge-transfer confound in Section 6**: In Section 5, the P-Net is BERT-base trained from scratch—a reasonable ablation. In Section 6, the P-Net is initialized as **FLAN-large**, a model instruction-tuned on a large corpus that likely overlaps with the Super-Natural Instructions evaluation set. The paper does not ablate this choice; there is no comparison using a randomly initialized or weaker P-Net (e.g., BERT-base as in Section 5) in the instruction tuning setting. The improvements over ERM+DS in Table 2 could stem partly from FLAN-large's implicit task understanding guiding which permutations are semantically harder, rather than solely from the adversarial DRO mechanism. This uncontrolled variable makes it difficult to attribute Table 2's gains unambiguously to the proposed framework.

### Minor

- **No convergence analysis connecting P-Net optimization to the formal DRO objective**: The paper frames the method as solving the minimax in Equation (6) but the P-Net implements an approximation via Gumbel-Sinkhorn sampling. There is no analysis of whether the alternating optimization converges, nor any bound on how close the P-Net's distribution is to the true worst-case distribution. This gap between "we frame this as DRO" and "we solve DRO" matters for the strength of the theoretical claims.

- **Limited evaluation scope in Section 6**: Only 4 held-out tasks are used (CSQA, CurDial, CoLA, TMW). With so small an evaluation set, idiosyncratic task behavior could dominate aggregate numbers. No significance tests or confidence intervals are reported, which makes it hard to assess result reliability.

### Trivial

- The abstract's "nearly 80% success rates" refers to the most favorable single data point (TMW, δ=50%, 6 shots, exhaustive search). The paper text (Section 3) is more precise ("over 50% and 80% on two datasets respectively"), but the abstract conflates the best-case figure with the general capability of the attack. This minor framing issue could be clarified.

---

## Nice-to-Haves

- Add ERM+DS as a baseline in the linear function (Section 5) experiments to complete the comparison in the synthetic regime where worst-case is exactly computable.
- Ablate P-Net initialization in Section 6 (compare FLAN-large P-Net vs. BERT-base P-Net) to isolate the adversarial training contribution from FLAN-large knowledge transfer.
- Visualize what permutations P-Net generates across training (e.g., does it learn semantically structured orderings or effectively random ones?) — this would validate that P-Net finds genuinely challenging permutations rather than arbitrary reorderings.
- A learning curve analysis (performance vs. number of adversarial training iterations) would clarify whether the average-performance gains arise from a curriculum effect or a DRO effect.

---

## Removed Points

*These points are flagged as removed. Treat them with caution.*

1. **Entropy constraint claimed to be an error (Harsh Critic, Issue in Section 4.2)**: The critic claimed that the constraint $\sum_{i,j} \Pi_{ij}(1-\Pi_{ij})$ maximizes at $\Pi_{ij}=0.5$ (the uniform matrix) and therefore defeats the paper's stated intent. This is incorrect. The P-Net's combined objective is $\arg\max_\phi (L_{lm} - \beta L_{ent})$ (Equation 16), so the P-Net *minimizes* $L_{ent}$, which pushes entries toward 0 or 1 (hard permutations), away from 0.5. The formulation is self-consistent and the critic misread the sign of the entropy term. **Removed as factually incorrect.**

2. **"Attack is trivially detectable" (Harsh Critic, Introduction)**: The critic argues that reordering demonstrations is visible to a model provider. The paper's threat model involves a *malicious user* (attacker) manipulating the order of shots before sending them to a model—not a prompt injection attack needing to hide from the model provider. The "less noticeable" claim is about the attack being a clean, semantically preserving reordering rather than appending adversarial suffixes. This is a reasonable framing of a naturally-arising distributional variant, not a misrepresentation. **Removed as strawman.**

3. **"80% is misleading headline" (Harsh Critic)**: The abstract says "nearly 80% success rates." The paper (Section 3) reports "over 50% and 80% on two datasets respectively" at δ=50%. The abstract is paraphrasing the results at the more aggressive threshold and on the more vulnerable dataset. This is minor framing and not fabricated. **Downgraded to Trivial.**

4. **Neural search attack trains P-Net on in-distribution samples (Harsh Critic, Section 3)**: The critic flags that P-Net used in Section 3 has seen the model during meta-training, questioning generalization. Section 3 uses P-Net to demonstrate vulnerability (upper bound approximation of exhaustive search), not as a practical deployed attacker. The claim is about the existence of the vulnerability, not whether the attack is deployable without model access. **Removed as out of scope.**

5. **"Hundreds of LoRA updates" efficiency claim not substantiated with experiment (Harsh Critic)**: This is a supporting efficiency claim made in the introduction and conclusion. While no explicit table compares update counts, it characterizes the practical setting described in Section 6. Removing this would require a trivial ablation rather than indicating a core flaw. **Removed as minor presentation concern.**

---

## Novel Insights

The most genuinely novel insight from the reviews is the potential confound between FLAN-large's pretrained representations and the adversarial training contribution in the instruction-tuning setting. This points to a broader design question for DRO-based ICL robustness: when the hard-example generator is itself a powerful pretrained model, its representations may implicitly supervise which orderings are "hard" in a way that conflates task understanding with adversarial discovery. Separating these two mechanisms—comparing matched-capacity P-Net initializations across Section 5 and Section 6—could illuminate how much of the robustness gain is algorithmic versus empirical knowledge transfer. This is an insight the paper does not address.

---

## Suggestions

1. Add ERM+DS as a baseline in Section 5. This is the most important actionable fix: it would directly answer whether the adversarial P-Net mechanism contributes beyond random augmentation in the controlled, enumerable regime.
2. Run a BERT-base P-Net in Section 6 as an ablation to isolate the FLAN-large knowledge-transfer confound. Even if FLAN-large P-Net is better, showing that a weaker P-Net also outperforms ERM+DS would substantially strengthen the mechanistic claim.
3. Report statistical significance (e.g., bootstrap standard errors) or results from multiple seeds for the 4 held-out evaluation tasks in Section 6.

---

## Score and Decision

**Anchor comparison table (all retrieved):**

| Path | Avg Human Score | Comparison to PEARL |
|---|---|---|
| `/calibration/H8Qg1IIMaR.md` | 5.50 (Reject) | Demonstrates LLM permutation vulnerability but proposes no solution; PEARL is strictly more contributive |
| `/calibration/frRDT6EOhg.md` | 6.50 (Accept) | ICL improvement paper (demonstration-free), tight methodology, no major gaps; PEARL has larger scope but structural gaps |
| `/calibration/1Iu2Yte5N6.md` | 6.00 (Accept) | ICL demonstration ordering paper with strong theoretical analysis; PEARL has comparable empirics but weaker theory |
| `/calibration/pudmhZdV78.md` | 5.25 (Reject) | ICL spurious correlation paper, limited scope, missing key ablations; similar to PEARL's methodological gaps |
| `/calibration/Af7CsWMUNI.md` | 5.25 (Reject) | ICL representation-level method, rejected for limited scope; PEARL has broader scope |
| `/calibration/CbfsKHiWEn.md` | 6.20 (Accept) | DRO applied to LLM alignment (DPO), theoretical grounding + ablations; PEARL uses DRO similarly but lacks the clean ablations |
| `/calibration/TTrzgEZt9s.md` | 8.00 (Accept) | DRO theory paper with formal convergence guarantees; much stronger theoretical work than PEARL |
| `/calibration/OF5x1dzWSS.md` | 6.67 (Accept) | Adversarial training + DRO for image models, strong theoretical support; PEARL is in the same vein but empirical-only |
| `/calibration/vY4iBYm9TU.md` | 3.50 (Reject) | Transfer learning for adversarial robustness, weak contribution; substantially weaker than PEARL |
| `/calibration/xdnoULh5Sv.md` | 4.00 (Reject) | Adversarial defense blending paradigms without strong ablations; comparable methodological gap to PEARL |
| `/calibration/eC4WlSZc4H.md` | 6.75 (Reject) | Longitudinal LLM adversarial robustness study; richer analysis but similar empirical scope |
| `/calibration/3P87ptzvTm.md` | 5.00 (Reject) | Sinkhorn-based optimal transport for multiple distributions; limited contribution |
| `/calibration/j8HU5aNpd3.md` | 4.75 (Reject) | Many-shot ICL evaluation paper, limited methodology; narrower than PEARL |

**Calibration reasoning:**

PEARL sits above H8Qg1IIMaR (5.5, reject) which demonstrates the same vulnerability class but contributes no training-time solution. PEARL's solution works, and the core claim (PEARL > ERM+DS) is established in Section 6 with 5 LLMs. However, it sits below CbfsKHiWEn (6.2, accept) and OF5x1dzWSS (6.67, accept), which provide formal grounding and clean ablations for their DRO/adversarial training claims. The two structural gaps (missing ERM+DS in Section 5; FLAN-large confound in Section 6) are real but not fatal — Section 6 does show PEARL > ERM+DS, and Section 5 partially validates the mechanism with a weaker P-Net. The paper lands squarely in the borderline zone.

**Score: 5.5 — Weak Reject**

The paper makes a genuine and practically relevant contribution to ICL robustness with a principled DRO framework. However, the unresolved FLAN-large confound in the primary (Section 6) experiments and the absent ERM+DS comparison in the controlled (Section 5) experiment together leave the mechanistic claim — that the Sinkhorn-based adversarial P-Net specifically drives the robustness gains, beyond what FLAN-large's knowledge transfer and simple augmentation would provide — not fully established. These are addressable in revision but require non-trivial additional experiments.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>