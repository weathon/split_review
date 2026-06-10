Now I have sufficient verification. Let me write the complete consolidated review.

## Summary

This paper proposes a class incremental learning (CIL) approach that integrates OOD detection, self-training, and data-drift handling via an ensemble of expert models with two-phase training (contrastive pretraining followed by classifier learning). The core idea is to use OOD consensus across expert models to detect novel classes in a streaming setting and trigger self-training. The method is evaluated on wafer defect detection (MixedWM38) and MNIST.

## Strengths

- **Controlled evidence that OOD-driven self-training recovers accuracy after distribution shift.** In the wafer defect experiment (Section 4.1, lines 137–141), both the proposed DDModel and a matched legacy model drop accuracy when new classes appear, but the DDModel detects ~300 OOD samples from ~308 new data points, triggers self-training, and recovers. The legacy model with identical architecture, hyperparameters, and two-phase learning does *not* recover. This isolates the benefit of the proposed self-training mechanism.

- **Tackles a harder variant of the problem where new classes arrive without labels.** The paper explicitly acknowledges (Section 4.2, lines 148–151) that most CIL benchmarks assume labeled data for new classes, whereas their model does not receive labels for any classes beyond the initial set. This is a genuine departure from standard CIL assumptions and a worthwhile problem setting.

- **A clear architectural design with a shared updatable encoder across all sub-models.** The encoder is learned anew when a new class is added and is used jointly by all models; when the encoder updates, all classifiers are retrained (Section 4.1, lines 119, 126). The inference procedure (Algorithm 2, line 158) is also clearly described.

## Weaknesses

### Major

- **No comparison against any existing CIL method.** The paper evaluates only against a "legacy model" that is the same architecture without self-training. No standard CIL baselines (EWC, iCaRL, LwF, GEM, DER, PODNet, etc.) are included or even mentioned. The MNIST experiment (Section 4.2) states that "our approach did exhibit some performance degradation" relative to traditional CIL models yet provides no quantitative comparison or baseline names. The wafer defect experiment is entirely self-referential. For a paper claiming to advance CIL, this makes it impossible to assess whether the method improves upon, matches, or falls short of the literature.

- **Non-standard evaluation protocols that preclude comparison.** The wafer defect experiment uses a custom simulation on a modified subset of MixedWM38 with a non-standard metric: "the accuracy is recorded as the average accuracy of the previous 1000 inferences" (line 128), not standard CIL metrics (average incremental accuracy, forgetting measure, or task-boundary accuracy). The MNIST experiment (Section 4.2) uses a setup where no labels are provided for new classes, which the authors themselves concede makes comparison "potentially unfair" (line 150). No standard CIL benchmark (split CIFAR-100, split Tiny ImageNet, etc.) is used. Table 1 is referenced (line 160) but the text only mentions qualitative "performance degradation" without reporting actual numbers.

- **The method is structurally an ensemble of independently-trained binary classifiers rather than a single incremental model.** In the MNIST experiment (Section 4.2, lines 154–156), separate models are trained for each digit pair (0,1), (2,3), ..., (8,9) and ensembled at inference via max-score arbitration (Algorithm 2). This design sidesteps the core CIL challenge — maintaining a single shared representation that can grow without catastrophic forgetting — and is not equivalent to class-incremental learning as the field defines it. While the wafer defect scenario has a more incremental flavor (shared encoder updates, new experts added), the paper does not acknowledge or justify this framing gap.

- **Severely underspecified for reproducibility.** (a) The contrastive loss function is never defined — only "contrastive learning" is mentioned (lines 64, 80, 119). (b) The encoder and classifier architectures are not described (no layer counts, no convolutional dimensions, no output sizes). (c) The data augmentation strategy is mentioned but never specified (lines 86, 154). (d) Algorithm 1 and Algorithm 2 are described in prose paragraphs (lines 94, 158), not pseudocode. A reader cannot implement this method from the description.

- **Internal contradiction between claims and evidence.** The abstract and introduction claim the method "mitigates catastrophic forgetting" and "ensures consistent performance across a diverse range of classes" (lines 4, 16–17). But the MNIST experiment — the only test of general CIL capability — shows "some performance degradation" relative to traditional CIL models (line 160). The paper never reconciles these conflicting signals. The wafer defect scenario is a specialized binary anomaly detection task, not multi-class incremental learning, so results from it do not automatically transfer to the general CIL claims.

### Minor

- The related works section (Section 2) is shallow: the Continual Learning subsection (2.1) cites only one paper (Kim et al., 2022), and there is no meaningful engagement with the broader CIL literature.
- The paper references "removing the Replay Buffer" (line 152) in the MNIST modification, but the replay buffer was never established as part of the original method, making this reference confusing.
- The Limitations section (Section 6) acknowledges scalability and comparative benchmarking but does not address the more fundamental issues (framing gap with CIL, underspecification, contradictory evidence).
- Some citations are imprecise (e.g., "other paper (Fang et al., 2022)," line 46).

### Trivial

- The baseline is inconsistently referred to as "legacy model" (line 130) and "Legacy model" (Figure 5 caption).

## Nice-to-Haves

- Standard CIL benchmarks (split CIFAR-100, split Tiny ImageNet) and metrics (average incremental accuracy, forgetting measure) would make the evaluation comparable and situate the method properly.
- Reporting numerical accuracy values and comparison numbers from Table 1 in the text rather than relying solely on qualitative graph descriptions would strengthen the paper.
- If the method is best suited for anomaly detection in streaming settings (as the wafer defect experiment suggests), the paper would benefit from explicitly reframing its contribution around that application rather than general CIL.

## Removed Points

*These points were identified in the reviews but removed during synthesis. They are reproduced here for transparency but should not carry weight in the final assessment.*

- *"Title is grammatically broken"* — Removed per rule: grammar/style nitpicks are not substantive evaluation criteria.
- *"Missing related works (EWC, iCaRL, LwF, GEM, DER, PODNet)"* — Removed per rule: do not mention missing related works without external confirmation.
- *"Initial accuracy starts with 1.0 suggests cherry-picking"* — Removed: this is consistent with the moving-average metric (the first 1000 inferences are on seen classes and correctly classified).
- *"Results described qualitatively from a graph (Figure 5) that is not visible"* — Removed: the graph is an image stripped by the parser; qualitative descriptions are present in the text (lines 137–141).
- *"MLOps pipeline with Kubernetes and IP cameras is not a CIL contribution"* — Removed: this is a deployment architecture description outside the paper's core scope.
- *"Hyperparameter epoch 5 is unusually small"* — Removed: lack of convergence analysis is a minor writing issue, not a substantive weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core gap: the proposed ensemble-of-experts architecture departs from standard CIL in a way the paper does not fully acknowledge, and the positive wafer defect result does not automatically validate the general CIL claims. This observation is implicit in the paper's own MNIST discussion but is never made explicit by the authors.

## Suggestions

1. **Add standard CIL baselines**: Compare against at least 2–3 basic CIL methods (e.g., EWC, iCaRL, and one recent method) on a standard benchmark (e.g., split CIFAR-100) using standard evaluation protocols.
2. **Fully specify the method**: Provide architecture details, loss function definitions, and proper pseudocode for the algorithms.
3. **Reframe the contribution**: Either (a) position the paper as an OOD-driven self-training approach for anomaly detection in streaming settings (the wafer defect scenario) and drop the general CIL claims, or (b) add a proper CIL evaluation that supports the broader claims.
4. **Report numerical results**: Include actual accuracy numbers (not just qualitative graph descriptions) and quantitative comparison data.

## Score and Decision

Based on my assessment of the paper's quality: it has an interesting motivating idea and some concrete evidence from the wafer defect experiment, but the evaluation is non-standard and lacks any comparison to existing methods, the method's framing as CIL is strained (it is essentially an ensemble of binary classifiers for the general setting), and the method is too underspecified to reproduce. The positive wafer defect result is a genuine contribution but does not, on its own, support the broad CIL claims made in the title and abstract. The paper would need major restructuring to be competitive at a top venue.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>