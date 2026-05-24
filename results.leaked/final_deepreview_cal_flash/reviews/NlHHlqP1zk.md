Now I have all the information needed. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
// most papers have none
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me compose this carefully now.

---

**Final Score Determination**

**Round 1 bracket:** Based on comparison with weak anchors (~3.0), mid anchors (5.0–6.25), and strong anchors (8.0+), the paper sits between 5.0 and 7.0. It is clearly above the rejected papers (which had limited novelty or poor execution) but below the top-tier papers (which have rigorous, comprehensive evaluations and no significant overclaims).

**Round 2 narrowing:** 
- CB-LLM (5.75, Accept): Concept bottleneck for LLM interpretability. Weaker evaluation than FSE (fewer models, less thorough). FSE is stronger on breadth and novelty.
- FineR (6.67, Accept): LLMs for fine-grained visual recognition. Novelty questioned but practical contribution strong. FSE has comparable thoroughness but its contribution (meta-evaluation) is less directly applicable.
- ConLUX (4.67, Reject): Concept-based explanations, rejected. FSE is clearly stronger.
- Sufficient Context for RAG (6.25, Accept): Context sufficiency evaluation for RAG. Different domain but similar meta-evaluation framing. FSE is comparable in quality.

**Final score:** 6.0. The paper makes a genuine contribution with a novel evaluation framework and broad experiments, but the interpretation overreach and unresolved self-evaluation concern prevent a higher score. The paper is a clear accept but not a standout.

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept## Summary

The paper proposes the **Fast and Slow Effect (FSE)** framework and the **Class Representation Index (CRI)** to automatically evaluate whether LLM/VLM-generated concept annotations are semantically sufficient for class identification, without requiring human supervision. The framework progressively collects concept annotations across five stages (*fast mode*: direct visual inference; *slow mode*: concept-based reasoning) and measures how well the concepts discriminate the target class from semantically similar distractors. Across six model families and five datasets, the paper reports a striking finding: slow-mode (concept-based) reasoning consistently underperforms fast-mode (visual) reasoning by 25–27% on fine-grained datasets, revealing that current automated annotations fail to capture sufficient semantic coverage.

---

## Strengths

1. **Novel automatic evaluation framework for a critical underexplored problem.** The FSE framework replaces costly human evaluation and the flawed utility-as-proxy assumption with a fully autonomous procedure for assessing whether concept annotations are *sufficient* (Section 4, Definition 3.1). The concrete pipeline—progressive concept-chain gathering followed by forced-choice CRI measurement—is well-designed and grounded in hierarchical extraction practices from prior work (Oikarinen et al., Sun et al., Panousis et al.).

2. **Surprising and practically significant empirical findings.** Table 2 shows that across all six tested models, the slow mode underperforms the fast mode by 25–27% on fine-grained datasets (e.g., −32.92% for GPT-4o on Car, −57.44% for Llama-3.2-11b on CUB-Bird). This systematically demonstrates that high downstream accuracy (Table 4's Fused mode achieves ~90% CRI while Slow mode alone scores ~50%) does **not** guarantee annotation sufficiency—a finding with direct implications for concept-based XAI design.

3. **Broad and consistent evaluation.** The study covers six LLM/VLM families across five datasets spanning fine-grained (CUB-Bird, Car, Flower) and general (CIFAR-100, Caltech-101) tasks, in both visual-grounded and post-hoc scenarios. The contrasting result—that general datasets show the expected "slow mode superiority" while fine-grained tasks consistently fail—strengthens the conclusion that the insufficiency is task-dependent, not an artifact.

4. **Rigorous distractor construction.** The preliminary experiment (Table 1) systematically compares random vs. semantically related distractor strategies and shows that the latter yields contradiction rates of 34–45% vs. 14–20%, ensuring the candidate sets genuinely stress the concept-class mapping.

---

## Weaknesses

### Fatal
None.

### Major

1. **Interpretation of the fast–slow gap conflates two explanations.** The paper treats the negative CRI gap as direct evidence that *concepts are insufficient*—i.e., that LLMs "cannot conceptualize their knowledge." However, the gap could equally (or additionally) reflect limited **textual reasoning ability**: even if the generated concepts contain the information needed, the model may fail to reason correctly from text under the forced-choice setup. The strong fast-mode performance does not guarantee the model can exploit the same knowledge when expressed as text. The paper's own Definition 3.1 ties sufficiency to "enabling accurate inference," which partially absorbs this critique, but the causal narrative throughout the paper (abstract, Section 6, conclusion) overstates what the evidence uniquely supports. An independent evaluation of concept quality (e.g., a separate classifier trained on the same concepts, or human ratings of concept discriminability) would substantially strengthen this interpretation.

2. **Self-evaluation may conflate concept quality with reasoning ability.** The CRI metric uses the same LLM that generated the concepts to also predict the class from those concepts. The prompt asks the model to rely only on the textual concepts, but LLMs can leak internal knowledge of class labels from their training data. While this concern arguably *biases against* the paper's main finding (gap-filling would inflate slow-mode CRI, making the negative gap *smaller* than reality), the paper does not acknowledge or discuss this limitation. A control experiment using a separate text classifier (e.g., sentence embedding + logistic regression) on the same concept sets would cleanly separate concept quality from reasoning ability.

### Minor

3. **Five-stage annotation process lacks validation.** The paper adopts a 5-stage concept-chain (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features) based on extending prior 1–3 stage methods, but the specific design is not ablated or empirically justified. If the framework's conclusions are sensitive to stage structure (number, ordering, boundaries), the reported negative gaps could partly reflect a suboptimal prompting strategy rather than inherent annotation insufficiency. An ablation (e.g., comparing 3-stage vs. 5-stage) would clarify this.

4. **Missing test set sizes and sampling details.** The main experiments (Figure 3, Tables 2–4) do not report the number of test cases per dataset. The preliminary experiment uses 100 images; the main results likely use more, but exact counts (and any filtering criteria) are absent. This harms reproducibility.

5. **"Standard deviations are negligible" (Figure 3) without numerical values.** The paper states this claim about the shaded regions but does not report the actual standard deviations or confidence intervals. Numerical values should be provided.

6. **CRI formula contains a typo.** Equation (2) writes CRI = 100% × (1/t) Σ_{i=1}^t 1[y_i^t = y_i], but the test cases are indexed i=1…l (l = total cases), while t denotes the annotation step. The denominator should be l, not t. The intended meaning is clear from context, but this should be corrected for reproducibility.

### Trivial

7. **Equation (1) notation is imprecise.** The concept-chain formula c_i^t = ∪_{j=1}^{t-1} F(c_i^j, X_i; Θ) suggests a union of separate function outputs; the intended meaning (incremental accumulation) is clear from the text but the notation should be rewritten for clarity.

---

## Nice-to-Haves

- **Separate classifier control:** Replacing the LLM evaluator with a fixed text classifier (e.g., sentence embedding + logistic regression) trained on the generated concepts would address the self-evaluation concern and strengthen the claim that CRI measures concept sufficiency rather than reasoning ability.
- **Human calibration:** A small-scale human evaluation of concept quality (e.g., do the concepts contain discriminative information for distinguishing similar classes?) would help calibrate what CRI values mean in absolute terms.
- **Ablation of annotation stages:** Comparing with a simpler one-shot or 3-stage pipeline would show that the main results are not artifacts of the specific 5-stage prompt design.
- **Sensitivity analysis on distractor count:** Varying the number of distractors (currently fixed at 4) would strengthen the evaluation.

---

## Removed Points

1. **ResNet-18 fine-tuning concern ("distractor strategy"):** The critic questioned whether the ResNet-18 used for distractor selection was pretrained on ImageNet or fine-tuned on evaluation data. The paper explicitly says "pretrained ResNet-18," which standardly means ImageNet-pretrained. The concern is speculative and removed.

2. **Table 1 only uses GPT models (preliminary experiment):** This is a pilot study to select the distractor strategy, and the selected strategy is then applied uniformly across all model families in the main experiments. The criticism that generalizability to other LLMs is unknown is reasonable as a minor note but not a real weakness—the strategy's purpose is to create challenging candidate sets, and it demonstrably does so for the models it is applied to.

3. **Missing oracle comparison (human-annotated concepts):** The framework is explicitly designed to be human-free. A human calibration would be informative but is not a missing requirement.

4. **Missing related works:** Per instructions, this is not included as it requires external knowledge the reviewer does not have.

5. **Formatting/typo concerns:** Parser artifacts are not author errors; pure formatting nitpicks are removed per instructions.

---

## Novel Insights

The reviews confirm the paper's central insight: the negative CRI gap across six model families on fine-grained datasets is the key empirical contribution, and the debunking of the utility-as-proxy assumption (Table 4) is practically important. Neither the harsh critic nor the strength finder identified a significant finding beyond what the paper itself claims. The self-evaluation limitation and the interpretation ambiguity are real but do not reveal a hidden weakness that the paper actively conceals—they are limitations the paper should address but that do not undermine the core empirical result. The most novel perspective from the review process is that the self-evaluation concern, if anything, works *against* the paper's main finding (gap-filling would inflate slow-mode CRI), making the observed negative gap even more striking.

---

## Suggestions

1. **Address the self-evaluation concern directly** by adding a control experiment with a separate text classifier (e.g., sentence embeddings + logistic regression) trained on the generated concepts. If CRI trends remain similar, the concern is fully mitigated.
2. **Tone down the causal interpretation** of the fast–slow gap. Frame the negative CRI gap as demonstrating that current annotations are insufficient *under the paper's definition* (concepts do not enable accurate inference), and acknowledge that this could reflect either concept quality issues or reasoning limitations (or both).
3. **Report test set sizes** for all experiments and provide numerical standard deviations alongside the claim that they are negligible.
4. **Add a brief ablation** of the annotation stage structure (e.g., comparing 3-stage vs. 5-stage) or explicitly argue why the design choices are unlikely to reverse the main result.
5. **Correct the CRI formula typo** (denominator \(l\) instead of \(t\)) and clarify the notation in Equation (1).

---

## Score and Decision

**Calibration anchors retrieved (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KLUDshUx2V (Automating Concept Banks) | 3.40 | R1 | Weaker — limited novelty, narrow experiments |
| kTjEPEy96Q (Evaluating Unsupervised CBMs) | 3.00 | R1 | Weaker — conceptual fallacy about evaluation |
| wZiH43e5Ah (Conceptualize Any Network) | 3.00 | R1 | Weaker — incremental, weak evaluation |
| J0qgRZQJYX (Axiomatic Concept Explanations) | 3.00 | R1 | Weaker — narrow scope |
| L9U5MJJleF (CB Generative Models) | 6.00 | R1 | Comparable — solid contribution, some eval gaps |
| Q9Z0c1Rb5i (Boosting CBMs) | 5.00 | R1 | Slightly weaker — information leakage focus |
| 8sfc8MwG5v (Adaptive CBM) | 5.50 | R1 | Comparable — solid but incremental |
| rp0EdI8X4e (Faithful V-L CBMs) | 6.25 | R1 | Comparable — formal framework, some clarity issues |
| 0qrTH5AZVt (ConLUX) | 4.67 | R2 | Weaker — rejected, limited evaluation |
| RC5FPYVQaH (CB-LLM) | 5.75 | R2 | Weaker — fewer models, less thorough evaluation |
| zp88xOXAfS (Linear CEM for Text) | 4.80 | R2 | Weaker — rejected, incremental |
| c7DND1iIgb (FineR for FGVR) | 6.67 | R2 | Slightly stronger — practical contribution, but novelty questioned |
| iv1TpRCJeK (AutoEval LLMs) | 6.33 | R2 | Comparable — different domain, similar meta-evaluation framing |
| Jjr2Odj8DJ (Sufficient Context RAG) | 6.25 | R2 | Comparable — similar "sufficiency" framing, different domain |

**Round 1 bracket:** 5.0 – 7.0  
**Round 2 narrowing:** Compared against CB-LLM (5.75) and FineR (6.67), the paper sits between them — better evaluated than CB-LLM, slightly behind FineR on practical impact but comparable on thoroughness.  
**Final score:** 6.0 — solid accept with an interesting framework and clear empirical contribution, held back by an over-claimed interpretation and an unaddressed self-evaluation confound.

MY FINAL SCORE: 6.0  
MY FINAL DECISION: Accept