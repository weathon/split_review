## Summary

PELICAN proposes a two-stage LLM-based tutoring framework that first diagnoses a student's knowledge state via a successor-first traversal over hierarchical knowledge points (with an expert-assistant-verifier pipeline for accuracy), then adaptively tutors using a fast/slow-thinking strategy selection mechanism where slow thinking constructs a Simulated Teaching Tree to search over strategy paths. The evaluation includes both simulated experiments on the Gaokao dataset (184 questions) and a real-world human study with 169 high school students (1,335 tutoring reports).

## Strengths

1. **Simulated Teaching Tree (Slow Thinking) for strategy selection**: The paper formalizes a tree-search mechanism for teaching strategy selection — node expansion (Eq. 3), dialogue simulation (Eq. 4), and depth-penalized scoring (Eq. 5). The ablation study (Table 3) confirms that removing slow thinking reduces Suitability (4.17→4.00) and Overall quality (4.28→4.08), providing evidence that the lookahead matters.

2. **Successor-first cognitive diagnosis with cross-check pipeline**: The diagnostic approach achieves 94.93% precision, 94.29% recall, and 94.31% F1 (Table 1), substantially outperforming Free-Prompt (74.18 F1) and CoT (79.83 F1). Ablations confirm the value of both the verifier (No-Pipeline drops 1.23 F1 points) and the dependency-aware ordering (S-Independent drops 3.61 points).

3. **Real human evaluation with 169 high school students**: Section 4.6 and Table 6 report an in-the-wild experiment where PELICAN achieves the highest scores on all measured dimensions (86.8% success rate, 70.07 F_frequency, 4.39 Overall). This provides ecological validity that simulated experiments alone cannot, and is a strong point for the paper.

4. **Comprehensive ablation architecture**: Module-level ablations (diagnosis, slow-thinking, both — Table 3), backbone model ablations across four LLMs (Table 4), and cognitive-level analysis (Table 5) allow attribution of performance changes to specific design decisions.

## Weaknesses

### Major

1. **Inconsistent numerical results for the same method across tables.** PELICAN's reported R_coverage is **72.36** in Table 2 (main results) but **54.84** in both Table 3 (ablation) and Table 4 (backbone ablation). F_frequency is **72.06** in Table 2 vs **61.47** in Tables 3/4. The gap — 17.5 points for R_coverage, 10.6 for F_frequency — is far beyond noise (Table 2 reports std devs of ±4.69 and ±3.42, respectively). Tables 3 and 4 agree with each other but disagree sharply with Table 2. The paper gives no indication of what experimental conditions changed. A reader cannot determine which set of numbers reflects the method's true performance. This inconsistency undermines every quantitative claim in the paper. *(Verified against lines 305, 321, and 332 of the paper.)*

### Minor

2. **Abstract's headline improvement claims (+18.7%, +22.4%) are not traceable to any specific metric or baseline.** The abstract states "significant improvements in critical thinking stimulation (+18.7%) and task completion rates (+22.4%) compared to baseline models." Checking Table 2: Inspiration (closest to "critical thinking") goes from 2.42 (Free-Prompt) to 4.21 (PELICAN) = +74% relative. Overall goes from 3.60 to 4.33 = +20.3%. In the human evaluation (Table 6), success rate goes from 85.2% to 86.8% = +1.9% relative. None of these match. *(Verified against the abstract at line 9 and Table 2 at lines 300-306.)*

3. **Ablation study reveals an unexplained anomaly on the Inspiration metric.** In Table 3, the condition removing *both* diagnosis and slow thinking ("w/o. Diagnosis & slow") attains the highest Inspiration score (4.56) — higher than the full PELICAN system (4.30). The paper bolds PELICAN's best values and focuses discussion on R_coverage and F_frequency, but never addresses why removing both central components yields higher Inspiration. While the hard metrics (R_coverage, F_frequency) favor the full system, this anomaly on a key user-facing metric weakens the claim of the framework's superiority. *(Verified against Table 3 at line 321.)*

4. **Knowledge state update mechanism is underspecified.** Section 3.3.2 states: "the teacher updates the estimated knowledge state $\hat{K}_u^{(t)}$ based on the student's response type $\text{type}^{(t)}$ and cognitive state $\hat{K}_u^{(t-1)}$ from the previous round." This describes *what* happens, not *how*. Is this a learned function, a heuristic rule, or an LLM-based inference? The update is the core feedback loop that connects student responses to strategy selection, making the tutoring adaptive. As written, this component is a black box. *(Verified against lines 210-212.)*

5. **Human evaluation is described too briefly in the main paper for proper assessment.** The real-world study (Table 6) is summarized in approximately three sentences (Section 4.6), with all experimental design details — randomization, assignment to conditions, blinding, task specifics — deferred to the appendix (which is removed from the reviewed manuscript). As presented in the main paper, a reader cannot assess the methodological quality of this important validation. *(Verified at lines 415-418.)*

### Trivial

6. The threshold for activating slow thinking is M=1 (after one round of difficulty on a subtask, Section 3.3.3, line 278). This means the system switches to slow thinking after the first hiccup, making the "dual-system" framing somewhat overstated — it is effectively always slow thinking. No sensitivity analysis is provided for this or any other hyperparameter (k=2, m=2, λ=0.4).

7. Column headers in Tables 3 and 4 read "Frequency" rather than "F_frequency" — likely the same metric but inconsistently labeled, which adds to the confusion around which numbers match.

## Nice-to-Haves

- A sweep over hyperparameters M, k, m, and λ would clarify whether results are sensitive to these design choices.
- The paper could strengthen the connection between the GPT-based evaluation (Tables 2-4) and the human evaluation (Table 6) by showing a correlation analysis between the two, given the claim of "strong consistency."

## Removed Points

*These points were identified in the reviews but are removed under the filtering rules. They should be treated with caution.*

- **"LLMs are not adequate models of human learning; the teacher may exploit artifacts in the student-LLM" / "circular evaluation"** — This is a general critique of LLM-as-student evaluation that applies to essentially all work in this space. The paper partially addresses it with the human evaluation in Section 4.6. The ground-truth knowledge state is a predefined binary vector, not circular.
- **"No comparison to NeuralCDM/IRT"** — The paper's diagnosis method is interactive dialogue-based, a fundamentally different paradigm from static data analysis methods like NeuralCDM/IRT. These are not comparable in a controlled setup without a shared task formulation.
- **"Successor-first is not novel"** — Novelty per se is not the evaluation criterion; the question is whether the framework is effective and well-validated.
- **"Pipeline adds only about 1%"** — The improvement from No-Pipeline (93.08 F1) to PELICAN (94.31) is 1.23 F1 points at the 94% level, which is a meaningful margin.
- **"The advantage may come entirely from having a diagnosis stage"** — Speculative; the ablation study (Table 3) provides evidence that both diagnosis and slow thinking contribute.
- **"Qwen-max achieves higher R_coverage than GPT-4o"** — This is acknowledged in the text and explained as a trade-off with language quality metrics.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the numerical inconsistency.** Explain (or correct) why PELICAN's R_coverage and F_frequency differ by 17+ points between Table 2 and Tables 3/4. If the experiments used different random seeds, data subsets, or student configurations, state this explicitly. If it is an error, correct it. The paper cannot be evaluated until this is clarified.

2. **Trace the +18.7% and +22.4% claims.** Specify which metric(s) and baseline(s) produce these numbers, or remove them from the abstract.

3. **Specify the knowledge state update mechanism** in Section 3.3.2. Provide the prompt template, heuristic rule, or learned function used.

4. **Expand the in-paper description of the human evaluation** (Section 4.6) to include at minimum: how students were assigned to conditions, whether evaluations were blinded, and what specific task/topic was used.

## Score and Decision

**Calibration Anchors (all rounds):**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| cLTM1gc6Qm (Mockingbird) | 2.25 | R1 | Irrelevant topic (LLM-as-mock-function), far below PELICAN |
| a2rSx6t4EV (EDU-RAG) | 2.33 | R1 | RAG benchmark, less comprehensive than PELICAN |
| iucVyVC8jQ (Dual-Fusion CD) | 3.25 | R1 | Cognitive diagnosis only, no tutoring or human eval |
| dp1BH2bK4Y (Re-TASK) | 3.00 | R1 | Task decomposition framework, unrelated domain |
| s6X3s3rBPW (Adaptive Testing) | 4.00 | R1 | LLM evaluation via CAT; weaker methodology, no human eval |
| M4fhjfGAsZ (Automated KC) | 5.33 | R1, R2 | Clean, consistent KT results; stronger methodological rigor but no human eval |
| lXwhR7uci1 (TestAgent) | 4.75 | R1, R2 | Most comparable — LLM assessment agent with human eval, similar shortcomings (underspecified components, simulation reliance) but without the numerical inconsistency |
| x1nlO1d1iG (CogMath) | 4.33 | R1, R2 | Cognitive evaluation of LLMs; limited scope |
| BzvVaj78Jv (Students Rather Than Experts) | 5.00 | R2 | Virtual student simulation; solid framework but less complete system |
| M1CCA6UF0y (AI-Assisted Math Qs) | 4.25 | R2 | Math question generation; different task, less comprehensive eval |

**Round 1 bracket**: 3.5–5.5 (below strong papers at 7.5+, above weak papers at <3.5)

**Round 2 narrowing**: The paper is most comparable to TestAgent (4.75) and Students Rather Than Experts (5.00), both rejected. PELICAN has better ablation structure than TestAgent but a worse numerical consistency problem. The numerical inconsistency (17-point gap unexplained) is a concrete flaw that places it below the cleaner papers in the 5+ range. Taking these together, the paper lands just below TestAgent's 4.75.

**Final score**: 4.5. The paper has a substantive framework and a rare real human evaluation, but the unexplained numerical inconsistency between main results and ablation/backbone results undermines confidence in the quantitative claims. Combined with untraceable abstract claims and underspecified components, the paper as presented does not meet the acceptance bar.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>