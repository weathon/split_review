- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have all the information I need. Let me write the consolidated review.

## Summary

ProgSyn introduces a framework for programmable synthetic tabular data generation that unifies differential privacy, logical constraints, statistical manipulations, and downstream-task specifications under a single pre-train-then-fine-tune procedure. The key technical contributions are differentiable relaxations for logical constraints (AND/OR primitives on one-hot features) and a method for optimizing downstream classifier behavior via differentiable surrogate training. Experimental results on the Adult dataset show state-of-the-art fairness-accuracy tradeoffs (2.3% higher accuracy at 2× lower demographic parity distance) and demonstrate composability across multiple specification types simultaneously.

## Strengths

- **First unified programmable framework**: ProgSyn is the first method supporting joint specification of DP, logical constraints, statistical manipulations, and downstream objectives (Section 4 intro, Figure 3). Prior work handles each in isolation, so this integration is a genuine contribution.

- **State-of-the-art fair synthetic data generation**: Table 1 shows ProgSyn achieves higher downstream accuracy and lower demographic parity distance than specialized fairness methods (DECAF, TabFairGAN, PreFair) in both non-private and private (ε=1) settings. This outperformance by a general framework against dedicated approaches is concrete evidence of the method's effectiveness.

- **Novel differentiable relaxation for logical constraints**: Section 4.2 introduces AND/OR primitives that turn first-order logical constraints into differentiable losses using one-hot encodings. Table 2 shows FT+RS substantially improves over RS-only on hard constraints (e.g., RC2 non-private: 82.8% vs. 78.9%), demonstrating that the relaxation meaningfully guides generation.

- **Composability of diverse specifications**: Table 3 progressively stacks five specifications (fairness, two statistical manipulations, two logical implications) and retains 84.0% accuracy with all constraints satisfied. This validates the claim that joint customization is feasible without catastrophic quality degradation.

- **Statistical manipulation capabilities unsupported by prior work**: Experiments S1–S3 (Section 5) demonstrate controlling mean age (achieving 30.2 vs. target 30), equalizing group means (gap <0.1 years), and zeroing a correlation (−0.2→−0.01) while retaining >84.5% accuracy — capabilities no prior method offers.

## Weaknesses

### Fatal
None.

### Major

- **Downstream specification gradient flow is underspecified**: The paper states (Eq. 3–4) that ψ\* depends differentiably on θ through the generated sample X̂ and that the downstream loss L_DOWNSTREAM exhibits a "differentiable dependency on θ" (line 115). However, no mechanism is provided for how the gradient flows from the test-time statistic SI back through the inner optimization (min_ψ L_CE) to θ. The paper does not mention unrolled differentiation, implicit differentiation, a closed-form surrogate, or any other technique that would realize this dependency. Since the downstream specification is one of the paper's four claimed forms of customization and is central to the SOTA fairness result, this gap prevents the method from being reproduced or fully evaluated from the text alone.

- **DP budget adaptation lacks privacy analysis**: The paper modifies the DP iterative framework from McKenna et al. (2022) and states it "allow[s] both for increasing and decreasing the per iteration DP budget, depending on the improvements observed in the previous step" (line 66). No composition theorem, privacy analysis, or formal argument is provided to establish that this adaptive allocation still satisfies ε-DP. Adaptive privacy budget composition is notoriously tricky, and without analysis or an empirical privacy audit, the DP guarantee claimed for ProgSyn is unsubstantiated.

### Minor

- **Rejection rate for logical constraints not reported**: Table 2 reports results at 100% constraint satisfaction rate (CSR) achieved via rejection sampling after fine-tuning, but does not report the fraction of samples rejected. If many samples are rejected (e.g., >40%), the approach becomes computationally expensive and risks selection bias. The comparison of "RS only" vs. "FT+RS" is informative but incomplete without this practical cost metric.

- **No detailed results for the three additional datasets**: The paper states it "draw[s] similar conclusions" on Health Heritage, German Credit, and Compas (Section 5) but provides no tables or numerical results. For a paper making claims of generalizability, summary statistics for all datasets are expected in the main paper.

- **Discretization of continuous features not specified**: The logical constraint relaxation depends on discretization bins (example: [18-35, 36-45, 46-55, 55-80] for age). The actual discretization used for each dataset is not specified, which affects both reproducibility and the precision of constraint enforcement near bin boundaries.

### Trivial
None.

## Nice-to-Haves

- Provide an algorithm box detailing the fine-tuning loop, including how surrogate classifiers are trained, how gradients for the downstream objective are computed, and how DP composition is tracked.
- Report hyperparameter sensitivity for the loss weights λ_i (even a brief analysis varying λ for one constraint would increase confidence).
- Report training time costs relative to baselines.
- Add baselines for logical constraints using rejection sampling applied to off-the-shelf generative models (e.g., CTGAN, TVAE) to further quantify the benefit of fine-tuning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Table formatting / "green" coloring complaints** (Harsh Critic, Section-by-Section): These are PDF-extraction artifacts, not author errors. Removed per formatting-nitpick rule.
- **"Fatal" characterization of the downstream spec gap** (Harsh Critic, Critical Issue 1): The critic called this a "structural issue" implying the paper "does not constitute a specification of a working algorithm." The paper reports working results (Table 1, Table 3) and anonymized code is provided. The gap is in exposition, not in existence of a working method. Demoted to Major (still a real concern, but the core claim is not invalidated).
- **Criticism that baselines for logical constraints are "too weak" to support claims** (Harsh Critic, Critical Issue 3): The paper already compares FT+RS to RS-only (on the same pre-trained model), showing fine-tuning helps, and to AIM (the only prior work supporting constraints in this setting). Asking for additional CTGAN/TVAE baselines is reasonable as a nice-to-have but does not undermine the demonstrated result that fine-tuning outperforms rejection sampling. Demoted from Major to Nice-to-Have.
- **Speculative concern about AND/OR primitives training dynamics** (Harsh Critic, Section-by-Section): The critic notes the soft masks are in [0,1] and the paper doesn't discuss binarization during training. The paper already states rejection sampling is used at inference for final enforcement (line 95), so this is addressed. Removed.
- **Speculative concern about statistical customization with small N** (Harsh Critic, Section-by-Section): "it is unclear how the conditioning event φ is handled when N is small" — this is speculation about a scenario not tested. Removed.
- **Strength about "Consistency across multiple datasets"** (Strength Finder, Supporting Strength 3): The claim is stated but no numerical evidence is shown for the additional datasets. This overstates the evidence. Removed as insufficiently supported.

## Novel Insights

The two reviews together surface an interesting tension: the paper's most novel claim (unified programmable control) is simultaneously its best-evidenced strength (via the composability experiment in Table 3 and the SOTA fairness result) and its weakest point in exposition (the downstream specification gradient mechanism and the DP budget adaptation are both critically underspecified). This is not a contradiction — it reflects that the paper's central technical idea (pre-train then fine-tune with differentiable relaxations) is largely sound and delivers real results, but the writeup glosses over the parts that would be hardest for another group to implement without guessing. The paper is closest to acceptance on its strongest experiment (fairness) and furthest on its most novel mechanism (differentiating through classifier training).

## Suggestions

1. **Clarify the downstream gradient mechanism explicitly**: State whether the surrogate classifier h_ψ uses a closed-form solution (e.g., linear model), K-step unrolling, or implicit differentiation. This is the single most important clarification needed.
2. **Provide a privacy composition argument for the adaptive DP budget**: Even a brief note explaining how the adaptive allocation is tracked within a fixed total ε (e.g., via Rényi DP composition) is necessary to substantiate the DP claim.
3. **Report rejection rates / acceptance rates for logical constraints** alongside accuracy at 100% CSR. A simple "samples generated per valid sample" metric would quantify practical utility.
4. **Include a summary table** (maybe in the main paper) with key results for Health Heritage, German Credit, and Compas to substantiate the generalizability claim.
