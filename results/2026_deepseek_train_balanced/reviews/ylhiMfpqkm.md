Now let me write the final consolidated review.

## Summary

This paper proposes the first framework for unsupervised pre-training of Generative Flow Networks (GFlowNets). The key idea is training an outcome-conditioned GFlowNet (OC-GFN) that learns to reach any terminal state in a reward-free manner, using contrastive training and outcome teleportation to overcome sparse-reward challenges. A pre-trained OC-GFN can then be adapted to downstream task-specific rewards via an amortized predictor that approximates an otherwise intractable marginalization over outcomes. The method is evaluated on GridWorld, bit sequences, TF Bind 8, RNA, and antimicrobial peptide generation tasks.

## Strengths

- **Novel pre-training paradigm for GFlowNets.** This is the first paper to demonstrate reward-free unsupervised pre-training of GFlowNets, which is a genuine open problem. The framing as outcome-conditioned learning (analogous to goal-conditioned RL) is well-motivated and natural.

- **Outcome teleportation and contrastive training are convincingly ablated.** The ablation studies on GridWorld (Fig. 3b-d) and bit sequences (Fig. 7) show that disabling outcome teleportation degrades performance, and disabling both components causes catastrophic failure in large outcome spaces. This provides strong evidence that both components are necessary, not just nice-to-have additions.

- **Scaling to astronomically large outcome spaces.** The AMP experiment (20^50 outcome space, Fig. 12) and the high success rates achieved there demonstrate meaningful scalability. This goes well beyond what prior GFlowNet work has shown for pre-training.

- **Consistent diversity advantage across multiple domains.** In RNA (4 tasks, Fig. 11), AMP (Fig. 12), and bit sequences (Fig. 8/9), the method consistently discovers more modes than training a GFN from scratch, MCMC, or DQN. The t-SNE visualization on TF Bind 8 (Fig. 9e) provides qualitative corroboration that coverage is broader.

## Weaknesses

### Major

- **Results shown for only 2 of 29 held-out TF Bind 8 tasks.** The paper claims "consistent and substantial improvements" (line 41) across 30 downstream tasks, tuning on one and evaluating on the remaining 29. Yet results are presented for only 2 tasks (Fig. 8, tasks 0 and 14). No aggregate statistics (mean, median, win rate, or even a scatter plot) are reported across the 29 held-out tasks. Without this, the reader cannot assess whether the 2 shown tasks are representative, and the claim of "consistent" improvements across all tasks is unsupported. This is a significant gap in the empirical evidence for the paper's main applied claim.

- **No compute budget reported, undermining efficiency claims.** The OC-GFN pipeline involves training (i) an unconditional GAFN, (ii) the OC-GFN pre-training, and (iii) the amortized N/Q predictor fine-tuning. The baseline is a single GFN trained from scratch. The paper reports no training steps, environment interactions, or wall-clock time for any experiment. Without controlling for total compute budget, the reader cannot distinguish between "pre-training structurally helps" and "more total compute trivially helps." This is a fundamental flaw for a paper whose core thesis is about efficient adaptation.

### Minor

- **Outcome teleportation loss is undefined for unsuccessful trajectories.** The loss in Eq. (11) (line 173) contains the term log R(x|y). When R(x|y) = 0 (unsuccessful trajectory), this term is -∞. The paper applies this loss to both positive trajectories τ⁺ (R=1 by construction) and negative trajectories τ⁻ (which may have R=0, line 124 of Algorithm 1). The practical handling of log 0 is not discussed. This is a meaningful gap in the method description, even if a simple workaround (masking, epsilon, or only updating on R=1) exists.

- **Zero-shot conversion claim is rhetorically overframed.** The paper repeatedly emphasizes that direct conversion "can be achieved without any re-training" (lines 33-34, 79, 197), but then immediately acknowledges this requires an intractable marginalization (line 200-201) that is "computationally expensive" and leads to "slow thinking" (line 202). The actual method requires training two new networks (N and Q). The zero-shot conversion is evaluated only qualitatively on a small GridWorld (Fig. 4c). The framing would better serve readers by presenting the zero-shot property as a theoretical motivation rather than a practical capability. This is a presentation issue, not a technical flaw — the paper does not claim zero-shot performance on the main benchmarks.

- **Proposition 1 is a fixed-point statement, not a convergence guarantee.** The proposition states that if the loss is exactly zero for all trajectories and outcomes, then the policy can reach the outcome. This is a consistency property of the loss, not a guarantee that training converges to that fixed point. This is standard in GFlowNet papers and not a fatal issue, but readers should be aware that the theoretical grounding is about exact solutions rather than optimization behavior.

### Trivial

- The success rate curves for pre-training are mostly shown as visual figures without quantified terminal values in tables (e.g., Figs. 3, 6, 10). Providing tabular results at convergence would help comparison.
- No network architectures are described, which affects reproducibility.

## Nice-to-Haves

- For the TF Bind 8 experiment, reporting aggregate results across all 29 tasks (mean/median modes discovered with confidence intervals) would directly address the main evaluation gap.
- A compute-controlled experiment (training GFN from scratch for the same total number of environment interactions as OC-GFN pre-training + fine-tuning) would strengthen the efficiency claims.
- Comparing the amortized predictor against the Monte Carlo zero-shot baseline quantitatively on at least a moderate-size problem (in terms of sample quality and wall-clock time) would clarify the trade-off between the two conversion approaches.

## Removed Points

These points were identified by reviewers but removed after verification against the paper:

1. **"Circular dependency in amortized predictor training"** — The harsh critic claimed the N/Q joint training has a circular dependency with no convergence guarantee. This is a standard self-consistent learning setup (analogous to EM or self-supervised learning), commonly used in amortized inference. The loss is symmetric and the fixed-point property is correctly stated in Proposition 2. This is not a flaw.

2. **"Proposition 1 lacks proof and is not a formal consequence of the loss"** — The proposition is a standard consequence of the DB framework. If the flow constraints are satisfied for all edges with the terminal reward R(x|y), the policy will satisfy the outcome-reaching property. This is well-understood in GFlowNet theory.

3. **"Missing related works"** — Removed per hard rules: I cannot verify that a given related work is missing without external sources.

4. **"Reproducibility nits about hyperparameters, network architectures"** — Removed per hard rules: trivial implementation details.

5. **"Formatting/style nitpicks" and "missing appendix/proofs"** — Removed per hard rules: parser artifacts or sections stripped by the review format.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report aggregate results across all 29 TF Bind 8 tasks.** A simple table showing mean ± std modes discovered, top-K scores, and wins/total across all tasks would transform the evaluation from suggestive to conclusive.
2. **Report total environment interactions or training steps** for all methods and either control for equal total compute or explicitly discuss the compute trade-off.
3. **Clarify how the outcome teleportation loss handles R(x|y)=0 cases** in the log loss (Eq. 11). This is a small but necessary detail for reproducibility.
4. **Temper the zero-shot framing** or provide quantitative zero-shot results on a moderate-scale problem to support the claim.

## Score and Decision

The paper introduces a genuinely novel pre-training paradigm for GFlowNets with well-motivated technical components and credible ablation studies. The core idea is interesting and the scaling to 20^50 demonstrates real potential. However, two evaluation gaps are significant for a top conference: (1) results are shown for only 2 of 29 TF Bind 8 held-out tasks, making the central claim of "consistent improvements" across tasks unverifiable, and (2) no compute budget or environment interaction counts are reported, so efficiency claims cannot be distinguished from the trivial advantage of using more computation. These issues are fixable, but as presented, the evidence falls short of validating the paper's strongest claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>