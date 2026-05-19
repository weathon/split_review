- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Herald, a pipeline for generating a large-scale natural-language / formal-language (NL-FL) parallel dataset from the Mathlib4 Lean 4 library. The pipeline uses dependency-graph-aware hierarchical ordering, structured contextual information (head statements, dependency theorems, neighbor statements, docstrings, etc.), retrieval of similar theorems, and two augmentation strategies (tactic-based decomposition and LLM-based rewriting). The resulting dataset contains 580k NL-FL statement pairs and 44k proof pairs. The authors fine-tune a statement formalization model (Herald Translator) from DeepSeek-Prover-Base 7B, reporting 93.2% accuracy on miniF2F-test (Pass@128) and 22.5% on an internal graduate-level dataset, outperforming TheoremLlama and InternLM2-Math-Plus-7B. The work also demonstrates a proof-of-concept section-level translation from the Stacks Project.

## Strengths

1. **Dependency-aware hierarchical translation ordering (Sec. 3.1.2)**: The pipeline constructs a dependency DAG from Mathlib4 and translates statements in topological order, ensuring that NL translations of dependent theorems are available before the target theorem is processed. This directly addresses a known failure mode in prior work (e.g., TheoremLlama) where missing NL translations of dependencies led to fabrication.

2. **Large-scale dataset generation with dual augmentation strategies (Sec. 3.2)**: Two complementary augmentation techniques — tactic-state decomposition (yielding localized stepwise statements) and LLM-based informal rewriting with four distinct strategies — produce 580k validated NL-FL statement pairs. This is a significant quantitative increase over prior datasets (MMA's 88k pairs, Lean-STaR's 52k proof thoughts), as reported in Table 1.

3. **Strong empirical results on multiple benchmarks (Table 2, Sec. 4.1.3)**: The Herald Translator achieves 93.2% on miniF2F-test, 96.7% on miniF2F-valid, 22.5% on Extract Theorem, and 17.1% on College CoT, substantially outperforming TheoremLlama (50.1%, 55.6%, 4.0%, 2.9%) and InternLM2-Math-Plus-7B (73.0%, 80.1%, 7.5%, 6.5%). These are large, consistent margins across all four test sets.

4. **Compiler-verified validation with semantic back-check (Sec. 4.1.2)**: The evaluation pipeline combines syntactic validation (Lean REPL compiler check) with semantic preservation verification (LLM back-translation + NLI comparison), going beyond the simple syntax checks used in prior work.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation study isolates the contribution of any component.** The pipeline has multiple interacting components: dependency-level ordering, five types of structured context, retrieval of similar theorems, human-feedback prompt refinement, two augmentation strategies (tactic-based and LLM-based), and a data mixture with OpenHermes2.5 at a specific ratio (2:2:1). No experiment measures the effect of removing any of these. Without such controls, the reader cannot attribute the observed gains to the proposed structural-information-aware pipeline rather than to, e.g., simply training on more data (the augmented 580k pairs) or using the DeepSeek-Prover-Base initialization. This is the most significant methodological gap in the paper.

### Minor

1. **Validation pipeline uses Pass@128, which is extremely permissive** and conflates single-shot reliability with the ability to succeed given many attempts (Sec. 4.1.2). Pass@1 or Pass@k for small k would give a more informative picture of model quality. The headline "93.2% accuracy" should be read as "93.2% at 128 attempts."

2. **The back-translation model (InternLM2-Math-Plus-7B) is itself one of the baselines** compared in Table 2 (Sec. 4.1.2, line 221). While this doesn't necessarily bias results for or against Herald (since the same back-translation is applied to all models), it introduces a dependency on a specific model's quality for semantic verification, and no evidence is provided that this model reliably distinguishes meaning preservation in mathematical statements. Similarly, the NLI check (DeepSeek Chat v2.5) is not validated for this task.

3. **Limited baseline set.** Only three baselines are compared (TheoremLlama, InternLM2-Math-Plus-7B, Llama3-instruct). No comparison with general-purpose LLMs (GPT-4, Claude) or other specialized formalization approaches. The claim of "state-of-the-art" would be stronger with a broader comparison.

4. **Dataset statistics need clarification.** The introduction (line 21) states "generating 580k valid statements from 110k original Mathlib4 theorems," but Table 1 shows "Mathlib4 Original Statements: 291k." The discrepancy between "110k theorems" and "291k statements" is explainable (the 291k includes definitions, instances, structures, etc., beyond theorems) but the paper never clarifies this, which undermines trust in the dataset statistics on first reading.

5. **Internal test sets are small and lack confidence intervals.** Extract Theorem and College CoT are 200 samples each (Table 2 footnote). No confidence intervals, standard deviations, or results across multiple seeds are reported. With only 200 samples, reported differences could be noisy.

6. **The proof dataset (44k NL-FL proof pairs) is not evaluated.** The paper generates and releases proof pairs (Sec. 3.1.2), but the evaluation focuses entirely on statement formalization. No model is trained or tested for proof generation, so the proof portion of the dataset remains unvalidated. This is acknowledged implicitly but not discussed as a limitation.

7. **Human feedback iteration (5 PhD students, 6 rounds) constrains the claimed scalability** of the pipeline (Sec. 3.1.4). While the authors promise open-sourcing the resulting principles, the pipeline as described requires substantial expert effort that would need to be repeated for other codebases or languages, undercutting the "scalable" framing.

8. **The autoformalization case study (Sec. 4.3) is limited.** Only one section of the Stacks Project is attempted, and the prover (DeepSeek-Prover-V1.5-RL) successfully proved only one two-line theorem. This is presented as a positive demonstration but the practical utility for serious material remains unestablished.

### Trivial

- The introductory framing (line 19) mentions "the pyramid architecture of the Lean repository" without defining the term, and the contrast with prior work's use of structural information is somewhat vague.

## Nice-to-Haves

- Reporting Pass@1 in addition to Pass@128 would give a clearer picture of single-shot reliability.
- A controlled ablation experiment that isolates the dependency-level ordering, the structured context, and each augmentation strategy individually.
- Comparison with a model trained on a naive version of the dataset (e.g., flat random order, no structured context, no augmentation) would establish a lower bound and directly attribute gains.
- Human evaluation (e.g., expert rating of a random sample of 100–200 generated NL-FL pairs) would strengthen the quality claims beyond qualitative examples.

## Removed Points

1. **Criticism about baseline comparison fairness (different evaluation pipelines):** *Removed because it is speculative and contradicted by the paper's own framing.* The paper states "we conducted comprehensive tests comparing Herald with several models in similar settings" (line 227), and the baselines' scores on the *internal* datasets (Extract Theorem, College CoT) could only have been computed by the authors running these models themselves under the same pipeline. There is no evidence they simply copied numbers from original papers measuring different tasks.

2. **Criticism about missing prompts / reproducibility details:** *Removed per the rule that appendix content (including prompts) may have been stripped by the parser.* The paper promises open-sourcing of the model and dataset. Implementation-level prompt details are appropriately deferred.

3. **Criticism about "120k vs 291k" being a contradiction in dataset numbers:** *Demoted from the critic's framing as a contradiction to minor weakness #4 above.* The paper uses "theorems" (110k) and "statements" (291k) in different places; this is explainable but needs clarification.

4. **Criticism that the paper "does not define 'pyramid architecture'":** *Demoted to trivial.* A minor clarity issue, not a substantive weakness.

5. **Strength Finder's strength about "Herald dataset being one of the largest":** *Kept as part of strength #2.* Abstract claim supported by Table 1 numbers.

6. **Criticism about missing related works:** *Removed per instructions.* I cannot verify which related works exist.

## Novel Insights

The most notable observation that emerges from the reviews is the tension between the paper's extensive engineering investment (dependency graphs, five context types, human-expert prompt iteration, dual augmentation) and the lack of any controlled experiment to disentangle these investments. The paper claims a "structural-information-aware pipeline" as its core novelty, but the presented evidence cannot rule out the possibility that the gains come from more mundane factors: larger training data (580k vs. prior datasets), a better base model initialization (DeepSeek-Prover-Base), or the Pass@128 evaluation protocol. This weakens the scientific contribution but does not diminish the practical resource value of the Herald dataset itself — a 580k-pair NL-FL corpus validated by Lean's compiler is independently useful regardless of which specific design choices caused the performance improvement.

## Suggestions

- Add at minimum 3–4 ablation conditions: (a) no dependency-level ordering (flat random order), (b) no structured context (formal statement only), (c) no tactic-based augmentation, (d) no LLM-based augmentation. Report all on miniF2F-test and at least one internal dataset. This would directly support the paper's central claim about the pipeline's design.
- Report Pass@1 alongside Pass@128 to calibrate reader expectations.
- Clarify the relationship between "110k original theorems" and "291k original statements" with a brief sentence explaining that "statements" encompasses theorems, definitions, instances, structures, classes, etc.
- Evaluate the proof portion of the dataset, even with a small-scale experiment, or explicitly discuss this as a limitation.
- Expand the baseline set to include at least one strong general-purpose LLM (GPT-4, Claude) prompted for the same task.
- Add confidence intervals or bootstrapped error bars for the 200-sample test sets.
