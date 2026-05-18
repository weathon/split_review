Now I have a thorough understanding of the paper and the critiques. Let me produce the consolidated review.

## Summary

This paper proposes ArchLock, the first architecture-level defense against unauthorized model transfer. The method uses a cross-task neural architecture search (NAS) framework with: (1) simulated target task embeddings via Fisher Information Matrix manipulation, (2) a binary predictor trained with zero-cost proxy labels to rank architectures without training to convergence, and (3) an evolutionary search guided by a rank-based fitness score that balances source-task performance against target-task degradation. Experiments on NAS-Bench-201 and TransNAS-Bench-101 show that ArchLock reduces transferability on target tasks while maintaining source-task performance within 2% of the state of the art.

## Strengths

- **First architecture-level defense against unauthorized transfer**: The paper introduces a genuinely novel problem formulation — instead of modifying weights (which attackers can undo via fine-tuning), it searches for architectures that are intrinsically hard to transfer to similar tasks. This is a paradigm shift relative to prior weight-level defenses, and the paper clearly articulates why this matters (Sec. 1, Eq. 2).

- **Empirically demonstrated transferability reduction with minimal source-task cost**: On TransNAS-Bench-101, ArchLock-TK achieves APT as low as 40.88% compared to >80% for source-only NAS methods (Table 3). For the SS→SC pair, the rank percentile drops from 81.81% to 40.48% (~50% relative reduction). On NAS-Bench-201, ArchLock-TU reduces APT by up to 12% absolute (e.g., CIFAR-100 source: 93.47% → 81.06%) with source percentile dropping <2% (Table 1). These results are consistent across diverse task types (classification, segmentation, jigsaw, autoencoding).

- **Efficient cross-task search using zero-cost proxies**: The binary predictor avoids expensive architecture training by using majority-vote labels from seven zero-cost proxies. The predictor is meta-trained on ImageNet subsets and generalizes to unseen tasks via task-embedding conditioning (Sec. 3.2). This makes the search computationally practical — a meaningful engineering contribution.

- **Comprehensive evaluation across two multi-task benchmarks with ablations**: The paper evaluates all source-target pairs on both NB-201 (3 classification tasks, 15k architectures) and TNB-101 (7 diverse tasks, 4k architectures). Ablations on the number of simulated embeddings (5/10/15, Fig. 3) and similarity level (d=0.3/0.5/0.9, Table 4) provide useful insights into the method's sensitivity.

## Weaknesses

### Fatal

None.

### Major

- **Evaluation mismatch with the threat model**: The paper claims to mitigate unauthorized *transfer via fine-tuning* (Sec. 1: "attackers fine-tune this model to the domain of interest"). Yet the experiments evaluate architectures using the pre-computed *train-from-scratch* validation accuracies from NAS-Bench-201 and TransNAS-Bench-101 (Sec. 4: "Performance evaluation is based on the validation performance provided by the benchmarks"). These are different settings: an architecture that performs poorly when trained from scratch on a target task is not guaranteed to perform poorly when fine-tuned from source weights, because the source initialization carries task-relevant features. The paper repeatedly states that the defense works "regardless of the amount of data available to the attacker" (abstract), but this claim can only be tested by actually pre-training on the source and fine-tuning on target tasks. Without such experiments, the connection between the evaluation and the threat model is not established. This is a significant gap — it does not invalidate the approach, but it means the paper is evaluating a different phenomenon (architecture-task suitability at initialization) than the one it claims to address (resistance to fine-tuning-based transfer).

### Minor

- **Simulated task embeddings are not validated against real tasks**: The method generates synthetic target embeddings via Eq. (8) with a specified cosine similarity (default d=0.9) and uses these to guide the search. The paper provides sensitivity analysis for d (Table 4) but never verifies whether the real target tasks in the benchmarks (e.g., CIFAR-100, ImageNet16-120) have FIM embeddings that actually lie at similarity ~0.9 from the source embedding. If the simulated embeddings do not approximate real task geometry in FIM space, the observed transferability reduction could arise from an uncontrolled confound (e.g., the predictor learning to prefer architectures that are generally poor on many tasks). The paper also uses a fixed ResNet-50 feature extractor for FIM computation, which may not capture task relationships well for non-classification tasks in TransNAS-Bench-101 (autoencoding, jigsaw).

- **Binary predictor quality is not directly assessed**: The predictor is a core component — it generates the architecture rankings used in the fitness score. Yet the paper reports no diagnostic metrics (Spearman rank correlation, pairwise accuracy, etc.) comparing the predictor's rankings to ground-truth benchmark rankings on unseen tasks. Without this, it is impossible to attribute the observed transferability reduction to the predictor's fidelity versus other components of the search. The fact that ZCPs are known to correlate imperfectly with final accuracy across diverse tasks (cited in the paper) makes this gap more concerning. An ablation showing that the predictor is better than a single ZCP or a random baseline at ranking architectures on the evaluation tasks would substantially strengthen the paper.

- **Fitness score direction is unspecified**: The fitness function is f = T_rank − λ·S_rank with λ=2 (Eq. 9). The paper does not state whether the evolutionary search minimizes or maximizes f. The goal requires low T_rank (good for transfer reduction) and high S_rank (good on source), which implies minimization. But "fitness score" conventionally implies maximization in evolutionary algorithms. This ambiguity should be clarified.

### Trivial

- **Headline numbers in abstract are imprecise**: The abstract states ArchLock reduces transferability "by up to 30% and 50%" on the two benchmarks. The 50% figure is supported for a specific source-target pair (SS→SC with ArchLock-TK: 81.81% → 40.48%, ~50.5% relative). The 30% figure is less clearly tied to a specific result in the text. Whether these refer to relative or absolute reductions, and whether they come from ArchLock-TU or ArchLock-TK, is not explicitly stated.

## Nice-to-Haves

- A brief discussion of when training-from-scratch performance is a reasonable proxy for fine-tuning-based transferability (e.g., arguing that architecture-level inductive biases dominate over weight initialization for certain task pairs).
- Validation of simulated embeddings: compute FIM embeddings for the real target tasks in the benchmarks and report their cosine similarity to the source embedding, showing that d=0.9 is a realistic choice.
- Predictor diagnostic: report Spearman correlation between the binary predictor's rankings and benchmark ground truth on held-out tasks, and compare against single-ZCP baselines.

## Removed Points

- **"Comparison baselines are weak" / should include weight-level defenses**: The paper compares against standard source-only NAS methods (RS, REA, BONAS, weakNAS), which is the appropriate baseline class for a NAS contribution. Weight-level defenses (gradient masking, adversarial training) solve a different problem using a different mechanism; demanding this comparison evaluates the paper against the wrong class of expectations. Removed.
- **Missing details about Gram–Schmidt orthogonalization / architecture encoding / meta-learning procedure**: These details are standard and/or were described in the appendix (which the parser strips from all papers). The paper appropriately references Lee et al. (2021a) for the meta-training procedure. Removed.
- **Formatting/style nitpicks**: Any issues with typos, grammar, or figure formatting are parser artifacts, not author errors. Removed.
- **Missing related works**: No external source available to verify existence or relevance. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves have not already made.

## Suggestions

1. **Run actual fine-tuning experiments**: Pre-train the searched architectures on the source task (e.g., CIFAR-10 → full training), then fine-tune on each target task, and measure final accuracy. This directly tests the threat model and would address the most serious weakness. Even a subset of tasks (e.g., CIFAR-100 and ImageNet16-120 on NB-201) would meaningfully strengthen the paper.
2. **Validate simulated embeddings**: Compute FIM embeddings for the real target tasks and report their cosine similarity to the source embedding. Show that d=0.9 is realistic.
3. **Report predictor diagnostics**: Compute Spearman rank correlation between the binary predictor's output rankings and the benchmark ground truth on held-out tasks. Also compare against using a single ZCP or random ranking as baselines.
4. **Clarify optimization direction**: Explicitly state whether the evolutionary search minimizes or maximizes the fitness score in Eq. (9).
5. **Clarify numerical claims**: Specify in the abstract or results section whether the "up to 30% and 50%" figures refer to relative reductions on individual source-target pairs, and whether they come from ArchLock-TU or ArchLock-TK.

## Score and Decision

The paper tackles a genuinely novel problem (architecture-level defense against unauthorized transfer) and provides a reasonable, computationally efficient framework. The empirical results are suggestive and the ablations provide useful insight. However, the central weakness — an evaluation that measures train-from-scratch performance while claiming to address fine-tuning-based transfer — is a significant gap that prevents the paper from substantiating its core claims. This is not a fatal flaw (the approach could plausibly work for actual transfer), but the paper cannot be accepted without addressing it, either through new experiments or through a clearly scoped argument that the current evaluation is a meaningful proxy. The contribution is real but the evidence is incomplete.

**Score: 5.5**

**Decision: Reject** (borderline; the evaluation mismatch is a substantive gap that the authors should address before publication; with fine-tuning experiments, the paper could be strong enough for acceptance).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>