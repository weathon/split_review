Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes DEPT, a pre-training framework that decouples token and position embeddings from the transformer body while using a federated-style training procedure across data silos. Three variants (Glob, Trim, Spec) provide progressively stronger decoupling, with Spec enabling fully vocabulary-agnostic training. The paper demonstrates that the DEPT pipeline produces models with better training stability, reduced embedding parameters (up to 80%), lower communication costs (up to 675×), and improved plasticity when adapting to new languages/domains. A 1.3B-parameter vocabulary-agnostic model is trained as a proof of concept.

## Strengths

- **Plasticity results are compelling**: Figure 3 (adaptation curves) shows that DEPT variants consistently converge faster and to lower perplexity than all baselines across four settings — the full pre-training set, a low-resource language (Swahili), and two held-out languages (Hindi, German). This evidence directly supports the plasticity claim, and the controlled starting point (all from random embeddings) makes these comparisons fair.

- **Clear efficiency gains with maintained quality**: The paper quantifies memory and communication reductions concretely (Table 2 in Section 2.4). Crucially, the internal comparisons show that Trim and Spec are at least *comparable* to Glob (which uses shared embeddings) despite dramatic reductions in embedding parameters and communication. This means the decoupling achieves efficiency without harming quality — a practical contribution.

- **Well-structured taxonomy of three variants with explicit trade-offs**: Glob, Trim, and Spec are systematically defined with their assumptions, memory/communication costs, and vocabulary requirements summarized in Table 2. This provides practitioners with a practical framework for different deployment scenarios (e.g., whether a shared vocabulary is feasible).

- **Honest limitations section**: The paper explicitly acknowledges that Spec does not directly provide a global embedding and that obtaining one is future work (Section 5, Limitations & Future Work). This boundary-setting is appropriate and strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

- **Conflated comparison: the training schedule and embedding decoupling are not disentangled**. DEPT differs from standard pre-training in *two* respects: (a) training is split into per-silo local steps with periodic averaging (FedAvg-style), and (b) embeddings are decoupled from the body. The paper attributes training stability to "DEPT" broadly (Figure 1 caption: "DEPT provides regularization effects"), but the regularization effect from periodic parameter averaging (OuterOPT) is a well-known property of FedAvg/Local SGD independent of embedding decoupling. The paper contains a natural control — Glob uses the *same* federated schedule with *shared* global embeddings — but the paper does not frame Glob-versus-standard as the schedule confound test, nor does it clearly attribute the observed benefits between the schedule and the decoupling. The paper says Trim and Spec are "comparable" or "very similar in effectiveness" to Glob (Section 3.2, RQ3 discussion), meaning the *decoupling* itself doesn't harm quality and enables efficiency — but the claim that "decoupling improves generalization" would be better stated as "the DEPT pipeline (federated schedule + decoupling) performs well, and the decoupling enables efficiency without sacrificing quality." Adding a controlled ablation that compares standard pre-training with the *same* per-silo local-step schedule (i.e., the algorithm DEPT uses but without any embedding trimming or specialization) would cleanly isolate the contribution.

### Minor

- **The random-embedding generalization evaluation is not perfectly clean**. When evaluating zero-shot generalization, the paper replaces the embedding matrix with a random initialization. Standard models are co-adapted to their learned embeddings, so random embeddings create a mismatch that temporarily degrades performance — a mismatch that DEPT variants, trained without a fixed global embedding, do not suffer from. The paper *already addresses this* by running a parallel evaluation with global embeddings (Tables mc4\_125M\_m, the\_pile\_350M\_m), where DEPT wins 16/28 comparisons — a weaker but still positive result. The paper should be more measured in how it presents the random-embedding results and should frame the global-embedding results as the more conservative test of body quality.

- **Disclosure of DEPT-specific hyperparameters is incomplete**. The paper does not state the value of \(N_{\text{local}}\) (number of local steps per round) used in the experiments, nor how it was chosen or whether it was held constant across variants. Since the balance between local steps and aggregation frequency affects both training dynamics and the claimed communication savings, this should be reported. Similarly, the paper does not discuss sensitivity to this hyperparameter.

- **The 16/28 global-embedding result is reported but not disaggregated**. The paper states that DEPT wins 16 out of 28 comparisons in the global-embedding condition, mentioning that losses concentrate on high-resource languages. However, no per-language or per-domain breakdown is provided in the main text, making it hard to assess the pattern the paper invokes to explain the losses.

### Trivial
None.

## Nice-to-Haves

- The 675× communication reduction is computed against standard DDP (which communicates every step). The paper also reports a 25% reduction over Local SGD, which is a more relevant comparison given that Local SGD also reduces communication. This more modest number could be given more prominence in the abstract and introduction.
- A sequential-fine-tuning baseline (train on each source one after another) would strengthen the comparison landscape but is outside the paper's stated scope.

## Removed Points

These points were raised by one or more reviewers but are removed from the main weaknesses with justification:

1. **"Missing appendix details about the billion-scale model"** — Removed per Hard Rule: the appendix is stripped by the parse process. The paper explicitly references Appendix A for the 1.3B model details (Section 3.2 RQ2 discussion: "shown in \cref{app:big_model}"). The details exist in the original submission.

2. **"No significance tests / error bars"** — Removed: single-run pre-training evaluations without error bars are standard practice for models of this scale. Requesting multiple seeds is reasonable but not a standard expectation at these training costs. Moved to Nice-to-Haves implicitly.

3. **"The paper does not discuss when the inner-loop optimizer might overfit to a single data source"** — Removed: this is a speculative concern about a scenario not demonstrated to occur in the paper's experiments. The results show Trim and Spec are comparable to Glob, suggesting no problematic overfitting.

4. **Strength from Strength Finder: "Clear taxonomy of three variants with explicit trade-offs"** — This is actually a legitimate concrete strength, so I'm keeping it.

5. **Strength from Strength Finder: "Use of federated averaging as a regularizer"** — This is just restating the paper's method, not a separate strength. It's already covered under the plasticity and robustness results.

6. **Strength from Strength Finder: "Comprehensive evaluation across multiple dimensions"** — This is somewhat generic but the paper does cover RQ1-RQ4 systematically. I'll keep it implicitly through the specific strengths listed.

## Novel Insights

The reviewer discussions did not surface any novel insight that the paper itself does not articulate. The key tension — that the federated averaging schedule likely contributes significantly to the observed training stability — is acknowledged in the paper's own description of OuterOPT's denoising effect, though the paper could more carefully separate the schedule contribution from the decoupling contribution.

## Suggestions

1. **Run (or explicitly discuss) a controlled ablation**: Compare a standard model trained with the same per-silo local-step schedule as DEPT but with shared global embeddings (i.e., Glob as the schedule-only baseline, which already exists in the paper). Then compare Trim/Spec against Glob to isolate the decoupling effect. The results likely already support the paper's conclusions; making this explicit would significantly strengthen the framing.

2. **Report the global-embedding generalization results per language/domain** rather than as a single 16/28 summary. This would allow readers to verify the claim that losses concentrate on high-resource languages.

3. **Disclose \(N_{\text{local}}\)** used in each experiment and discuss sensitivity to this hyperparameter. This is a standard disclosure requirement for methods that introduce new training hyperparameters.

4. **Reframe the random-embedding vs. global-embedding results**: Acknowledge the co-adaptation confound explicitly and present the global-embedding results as the more reliable test of body quality.

5. **Emphasize the 25% reduction over Local SGD** more prominently, as it is the more methodologically relevant comparison than the 675× reduction over DDP, which is only achievable by changing the training schedule (which Local SGD also does).

## Score and Decision

Based on my assessment: The paper makes a genuine and practical contribution — demonstrating that a federated-averaging approach combined with embedding decoupling enables efficient pre-training on heterogeneous data while maintaining or improving quality. The plasticity results are strong, the efficiency gains are concrete and well-quantified, and the three-variant taxonomy is clear. However, the central weakness — that the benefits are not cleanly attributed between the federated schedule and the embedding decoupling — prevents the paper from fully supporting its strongest claims as currently framed. This is addressable (the internal controls already exist in the data) but requires reframing and potentially a simple additional analysis. The paper is solid but has room for improvement before it meets the bar for a top venue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>