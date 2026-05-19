- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 3, 3, 1
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper investigates how fine-tuning LLMs on partially mastered knowledge (knowledge the model sometimes answers correctly) can improve mastery of *other* knowledge not present in the training data. The authors confirm this empirically on WikiQA (Tables 3–5) and propose a two-stage fine-tuning strategy: first fine-tune on "Maybe Known" data, then re-detect knowledge categories and augment the training set with knowledge that has upgraded to "Maybe Known," combined with replay of fully mastered knowledge to mitigate forgetting. The method yields ~2.8 pp test accuracy gains and a ~24% relative increase in "Highly Known" knowledge within the training set (Tables 7, 10).

## Strengths

- **Empirical finding that fine-tuning on partially mastered knowledge upgrades unmastered knowledge not in the training set**: Table 3 shows that after fine-tuning on only 'Maybe Known' data, 1443 knowledge points originally classified as 'Weakly Known' or 'Unknown' transition to 'Maybe Known' for Qwen2-7B (and similar for LLaMA3-8B). This directly validates the central hypothesis about knowledge interconnection and reasoning — a phenomenon not shown in prior work (Gekhman et al. 2024).

- **Well-designed control for random measurement noise**: Table 4 retests the same model twice without any fine-tuning and shows negligible category changes (e.g., 'Weakly Known' → 'Maybe Known' changes by only 43 for Qwen2 vs. 1443 after fine-tuning). This rules out the alternative explanation that observed upgrades are stochastic artifacts.

- **Comprehensive ablation study isolating the contributions of new knowledge acquisition vs. forgetting mitigation**: Table 8 compares five second-stage strategies. Strategy 5 (new upgraded data + replay) yields 86.17%; Strategy 2 (replay only, no upgraded data) yields 84.72%; Strategy 4 (upgraded data, no replay) yields 85.82%. This cleanly quantifies that both components contribute and that the combination works best.

- **Replication across two model families**: The core finding (knowledge type upgrade after fine-tuning) is replicated on both Qwen2-7B and LLaMA3-8B (Table 3), and the two-stage accuracy gain holds for both (Table 7), strengthening robustness.

- **Honest multi-round analysis showing rapid convergence**: Table 11 shows three-stage fine-tuning does not improve further; Table 12 shows the number of changing knowledge points drops sharply after the second stage (e.g., 'Weakly Known' → 'Maybe Known' decreases from 1443 to 197). This rules out trivial sequential improvement and honestly delineates the method's limits.

## Weaknesses

### Fatal
None.

### Major

- **Single-dataset evaluation undermines generality of the core claim.** All experiments are conducted on WikiQA, a Wikipedia-based closed-book QA benchmark. The paper's stated goal is to "broaden the pool of data suitable for training during the fine-tuning stage" — a general claim — but the evidence is drawn from one relatively simple dataset. The authors note in the Discussion (Section 5) that WikiQA is "loosely structured" and that domain-specific datasets with "tighter connections between knowledge might lead to more significant changes," but this acknowledgment does not substitute for evidence. Without results on at least one additional benchmark (e.g., a domain-specific QA set or a fact-verification task), the reader cannot assess whether the observed improvements generalize or are an artifact of WikiQA's particular knowledge graph structure. This is the single change that would most directly strengthen the paper.

- **Test-set leakage in early stopping.** The paper uses test-set accuracy to determine when to stop the first-stage fine-tuning ("At the end of each epoch, we evaluated the model's accuracy on the test set. Once the accuracy reached its maximum, we re-evaluated the knowledge types" — Section 3.1) and to select the best epoch for the second-stage results ("collecting the maximum accuracy achieved after the second stage" — Section 4.2.2). No validation split is mentioned. This form of test-set leakage can inflate reported accuracy; the paper should either justify the practice, use a held-out validation set, or explicitly discuss the magnitude of potential bias. This is a methodological concern that directly affects the credibility of the headline numbers in Tables 7 and 11.

### Minor

- **No statistical variance or uncertainty quantification for main accuracy results.** Table 7 reports point estimates only (e.g., 45.68% vs. 49.92% for Qwen2-7B) without confidence intervals, standard deviations across multiple runs, or significance tests. Given the stochasticity in prompt construction and decoding, and the moderate test set size (~600 questions filtered), it is unclear whether the reported improvements are statistically reliable. Adding 3–5 runs with different seeds would substantially strengthen the evidence. (The control in Table 4 addresses noise in knowledge *classification*, not in final test *accuracy*.)

- **Graph-based connectivity analysis (Table 5) lacks a null baseline.** The paper shows that a high percentage (92.6% for LLaMA3-8B) of reclassified knowledge nodes are "linked" to initially-Mayo-Known nodes, but does not report what fraction of *all* nodes are linked to initial nodes. If the entity graph is dense, the observed percentage could be no higher than chance. The entity extraction via regex is also acknowledged as simple. This analysis provides suggestive but non-rigorous evidence for the hypothesized mechanism; it does not weaken the main result (which does not depend on this analysis), but it limits the paper's ability to explain *why* the method works.

- **Limited comparison to other continual fine-tuning baselines.** The ablation study (Strategies 1–5) convincingly shows that both new data and replay matter, but a comparison to a simple two-stage baseline that does not involve knowledge classification at all (e.g., two rounds of standard fine-tuning on all data) would help separate the effect of the knowledge-guided selection from the effect of simply doing two training stages. The paper is not primarily a continual learning paper, so this is minor rather than major, but it would strengthen the claim that the *knowledge-guided* selection is what drives improvement.

### Trivial
None.

## Nice-to-Have

- A sensitivity analysis on the knowledge classification thresholds (from Gekhman et al.) would strengthen robustness, but is not required for the core claim since these are adopted from established prior work.
- Specifying the exact number of epochs for the first stage convergence and the exact prompt templates would aid reproducibility but is not essential given the methodological detail already present.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Paper overstates severity of constraints in Introduction"** — This is a subjective style criticism. The constraints are motivated by cited literature and are standard motivational framing. **Removed** per filtering discipline (not a specific, verifiable weakness).
- **"No explanation of why thresholds are chosen"** — Thresholds are directly adopted from Gekhman et al. (2024), which is properly cited. **Removed** (factually addressed by the paper).
- **"Missing comparison to EWC, SI, GEM"** — The paper is not proposing a new continual learning method; the ablation study already isolates the contributions of knowledge upgrade vs. replay. Requesting a full continual-learning baseline comparison is scope creep. **Removed** per soft rule (scope creep).
- **"Does not report how many epochs required for convergence"** — The paper states "several epochs" and "once accuracy reached its maximum" (Section 3.1) and reports that second-stage convergence occurs at "the end of the first to third epochs" (Section 4.2.2). This is sufficient for the field standard. **Removed** as nitpick.
- **"Reproducibility details about prompt templates and seeds"** — The paper describes prompt construction ("randomly selected four other questions of the same type"), provides generation parameters (Table 1), and reports using "random seed 42" for the fixed test prompts. **Removed** (sufficiently specified for the field).
- **"Missing details on what 'same type' means in prompt construction"** — The paper broadly follows Gekhman et al. and gives the generation procedure. This level of detail is within community norms. **Removed** as nitpick.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths and weaknesses, though the Harsh Critic's presentation of the test-set leakage issue is sharper than the Strength Finder's neutral reporting. The main novel insight from synthesis is that the paper's most impactful improvement would be adding a second dataset rather than any additional modeling complexity — the current evidence supports the claims within WikiQA but leaves generalization unaddressed.

## Suggestions

1. **Add at least one more dataset from a different domain** (e.g., MedQA, TriviaQA, or a fact-verification task) to demonstrate generality. This is the single highest-impact change.
2. **Report confidence intervals or error bars** from 3–5 runs with different random seeds for the main accuracy comparisons (Tables 7, 11).
3. **Address test-set leakage** by either (a) using a held-out validation set for early stopping and reporting final accuracy on a separate test set, or (b) explicitly justifying the practice and quantifying the potential bias (e.g., by showing that results on a held-out set are similar).
4. **Strengthen the graph analysis** by comparing the observed "Linked Reclassified" proportion against a null distribution (e.g., random label shuffling), or remove it if it does not support the mechanism rigorously.
5. **Add a simple two-stage baseline** that fine-tunes on all data in two rounds without knowledge-guided selection, to confirm that the knowledge-guided data augmentation is responsible for the improvement beyond the two-stage design itself.
