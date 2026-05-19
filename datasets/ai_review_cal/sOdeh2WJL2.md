- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 1, 8, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a three-stage pipeline for building small yet effective LLM guardrail classifiers: (1) synthetic data generation with policy self-reflection using an LLM (Llama-3-70B), (2) multi-task guardrail instruction pretraining (GIP) combining MLM, Alice++ (VAT), and classification losses on a unified dataset spanning up to 251k policies, and (3) a multi-armed bandit (MAB) search (Thompson sampling) over merge weights and merge types to combine single-policy (TaskGuard) and multi-policy (MultiTaskGuard) models into a final merged model (UniGuard). The paper reports large F1 improvements over existing LLM-based guardrails and API services on 7 public datasets and a newly created private benchmark.

## Strengths

- **Synthetic data generation with policy self-reflection (Sec. 3.1):** The SDG pipeline defines guardrail tasks via structured policies (name, description, allowed/disallowed behaviors, examples) and includes a self-reflection step where the generator LLM re-evaluates its own label judgments to correct mislabeled samples. This is a concrete, causally-motivated approach to producing high-quality training data for small classifiers, and the paper claims it outperforms training on real data.

- **Multi-task guardrail instruction pretraining (GIP, Sec. 3.3):** Combining three losses (MLM on instruction-augmented inputs, Alice++ VAT for robustness, and standard CE classification) on a unified dataset of up to 1M synthetic samples across 251k policies is a novel multi-task formulation for guardrailing. The instruction-based input construction (Instruct: policy description [SEP] Query: prompt [SEP] rationale) is a well-designed mechanism that lets a single small model distinguish between and generalize across many guardrail policies.

- **MAB-based model merging search (Sec. 3.4):** Formulating model merging weight selection as a Thompson sampling problem — including searching over merge types (full, attention-only, FFN, exclude classifier) — is a reasonable extension to prior merging work that relied on manual tweaking or grid search. The paper integrates this search with TIES, SLERP, MSA, and DARE, and compares random, ε-greedy, and Thompson sampling strategies.

- **Comprehensive evaluation scope:** The paper evaluates on 7 public datasets spanning prompt injection, toxicity, and content safety, plus a private benchmark (Safety, Finance, Tax, Injection). This provides broad coverage for the claimed improvements. The explicit mention of training on both synthetic and real data for public benchmarks enables controlled comparisons.

## Weaknesses

### Fatal
None.

### Major

- **Base model architecture is never specified.** The paper repeatedly refers to a "sub 1GB classifier" and "orders of magnitude smaller" than 7B models, but never names the underlying architecture (e.g., BERT-base, RoBERTa, DeBERTa-v3, DistilBERT). Since parameter count, model capacity, and baseline performance all depend on this choice — and since the paper's central claim is that a small model outperforms much larger ones — this omission is fundamental. The reader cannot assess whether the gains come from the method or from the base model choice, and the work is not reproducible without this information. (Confirmed: no mention of the architecture name anywhere in the extracted text.)

- **Private benchmark CustomGuardBench lacks transparency.** The paper names four datasets (Safety, Finance, Tax, Injection) but provides no information on dataset size, label distribution, source data, or construction methodology. The description cuts off at "These 4 datasets cover the prohibiting of unsafe discussions, financial advice, tax…" with no further detail in the extracted text. Since the paper claims improvements on this benchmark (e.g., "5.48 F1 on CustomGuardBenchmark" in the contribution list), the lack of transparency makes these results uninterpretable and unverifiable.

- **No comparison against fine-tuned small classifiers.** The baselines are all LLMs (LlamaGuard-7B, GPT-3.5/4/4o, etc.) and API services. A fundamental baseline is missing: a small classifier (e.g., BERT-base or whatever architecture the authors actually use) fine-tuned on the same public training data, or on the same synthetic data without multi-task pretraining. Without this, the paper cannot isolate whether the improvements come from (a) the base architecture, (b) the synthetic data quality, (c) the multi-task pretraining, or (d) model merging. The claimed 20–30 F1 margins over 7B+ models would be much more compelling if a same-scale baseline were shown to be far weaker.

- **No ablation of the three loss components.** Equation 1 combines MLM loss, Alice++ (VAT) loss, and CE classification loss with hyperparameters λ₁, λ₂, λ₃. The paper provides no experiment showing the contribution of each term. The Alice++ loss in particular needs justification: does virtual adversarial training meaningfully improve robustness for this task, or does the CE loss alone suffice? Without this ablation, the complexity of the multi-task objective is not justified.

### Minor

- **Training hyperparameters are absent.** No batch size, learning rate, optimizer, number of training steps/epochs, or hardware details are reported. While some of these may appear in supplementary material (stripped by the parser), their absence from the main text limits reproducibility assessment.

- **Algorithm 1's Beta update rules are non-standard and unexplained.** Lines 17–18 of Algorithm 1 update the Beta distributions using `max(F,1-F)·σ(F-F_best) + F` (for α) and similarly for β. This is not standard Thompson sampling (which would use α ← α + reward, β ← β + (1-reward)). The sigmoid-gated term incorporating the best-so-far F1 score is unusual, and the paper provides no justification or ablation showing that this formulation outperforms standard updates. The behavior of this customized update is not analyzed.

- **Validation set for MAB search is not characterized.** The paper uses a held-out validation set to guide the merging search but does not report its size, composition, or how it relates to the test sets. Given that the MAB search has several degrees of freedom (k weights, merge type, merging algorithm), the risk of validation set overfitting is non-negligible, and the paper provides no cross-validation or sensitivity analysis.

- **No statistical significance or confidence intervals.** The reported F1 differences are large (20–30 points), so confidence intervals would likely not change the qualitative conclusions, but their absence means the reader cannot assess the variability of these numbers across runs. This is especially relevant for the private benchmark, where a single run on a small dataset could produce misleadingly large margins.

- **No discussion of limitations or failure modes.** The paper does not discuss potential data contamination (synthetic data from Llama-3-70B may resemble LLM-generated test samples), distribution shift, or conditions under which the proposed method might underperform simpler baselines.

### Trivial
None that are substantive beyond what is covered above.

## Nice-to-Haves

- A comparison of the MAB-based search against simple uniform averaging and a grid search over the same weight space would strengthen the claim that the search finds a genuinely better combination.
- Adding an error analysis with qualitative examples where the proposed model succeeds and baselines fail would make the synthetic data quality argument more concrete.
- Clarifying the advantage over EvoMM and LM-Cocktail (both cited in related work), which also automate merging using task-specific data, would better position the contribution.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **"Results are unparseable images / no numerical evidence in the paper":** REMOVED (parser artifact). The original paper contains proper tables and figures; the extracted text renders them as image references. Criticisms based on unparseable formatting are not valid evaluations of the paper's content.
- **"MAB search is circularly configured":** REMOVED (factually inaccurate). Using a held-out validation set for hyperparameter tuning and a separate test set for final evaluation is standard ML practice, not a circular configuration. The critic's framing misrepresents the paper's methodology.
- **"Performance margins are extraordinary without commensurate evidence":** PARTIALLY REMOVED. The claim that the paper lacks per-dataset F1 tables (because they appear as images) is removed as a parser artifact. The substantive concern about missing small-classifier baselines is retained as a Major weakness (see above).
- **"The paper does not compare against EvoMM":** REMOVED. The paper cites EvoMM in the related work and clearly differentiates its contribution as using Bayesian search rather than evolutionary optimization. A missing comparison experiment is not a weakness here; the paper's contribution is the search method, not outperforming EvoMM on every metric.
- **"Conclusion only contains an image":** REMOVED (parser artifact).
- **"Synthetic data outperforming real data is stated but no comparison results given":** PARTIALLY REMOVED. The actual numerical comparison may be in the results tables (images). The paper does state this claim in the abstract and conclusion.
- **"Model architecture specification missing from related work discussion":** Not applicable — the architecture is missing from the methodology section, not the related work.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface expected tensions: the paper makes impressive empirical claims but is missing critical transparency details (architecture identity, benchmark characterization, ablation experiments) that the community would need to trust those claims. No reviewer identified a genuine flaw in the core methodology that the authors had not already anticipated — the concerns are about completeness of reporting rather than invalidity of approach.

## Suggestions

1. **Specify the base model architecture** explicitly (parameter count, model family, pretraining checkpoint). This is the single most important fix for reproducibility and credibility.
2. **Release detailed statistics for CustomGuardBench** (size, label distribution per split, construction methodology) or, ideally, release the dataset itself.
3. **Add a baseline** consisting of the same base model fine-tuned on (a) real public data without GIP, and (b) synthetic data without GIP, to isolate the contribution of each pipeline component.
4. **Ablate the three loss components** (train with only CE, CE+MLM, and CE+MLM+Alice++) and report results.
5. **Justify or simplify the non-standard Beta update rules** in Algorithm 1, or show that they outperform standard Thompson sampling updates.
6. **Characterize the validation set** used for MAB search (size, composition) and add a sensitivity analysis (e.g., different validation splits).
7. **Add a limitations section** discussing data contamination risk, distribution shift, and conditions where the approach may underperform.
