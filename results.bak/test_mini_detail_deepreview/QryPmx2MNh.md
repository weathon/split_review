Now I have sufficient calibration context. Let me write the final review.

**Round-1 bracket**: Based on the calibration search, the paper sits between the weak anchors (~3.0, mostly rejected papers about math problem solving with transformers) and strong anchors (~8.0, papers like "Learning to Permute" and "Transformers Provably Solve Parity"). The middle band anchors (5.5-6.5 range) are the most relevant comparisons: papers on transformers for arithmetic with similar empirical scope.

**Round-2 narrowing**: Comparing against the 4.0-5.5 papers on arithmetic transformers (Positional Description Matters at 4.0, From Interpolation to Extrapolation at 5.5, Understanding Addition at 5.5), this paper has stronger *originality* — the problem formulation is genuinely novel — and a clever method. But it is weaker on evidence breadth (only 3 synthetic tasks + 1 rediscovery, no statistical variance). Compared to the 6.25-6.67 papers (neural combinatorial optimization, learning trajectory transfer), it has less experimental rigor but more novelty in the problem itself.

The paper is clearly above the 4-5 reject-level papers but below the 7-8 accept-level papers. I anchor it at **6.0**.

---

## Summary

The paper formulates a novel problem: automatically discovering a learning-friendly permutation of decoder output tokens for Transformers learning arithmetic tasks. It proposes a "loss profiling" method that identifies good orders by training a single model on mixed-order data and selecting the orders with the fastest early loss drop. To handle factorial search spaces, it introduces a two-stage hierarchical search (global block-level + local intra-block refinement). Experiments on three synthetic order-sensitive tasks (RELU, SQUARE-19, INDEX) and one multiplication task (PROD) show the method can recover the known optimal (forward/reverse-digit) order from up to 13! ~ 6×10⁹ candidates using random initialization, and scales to L=30-40 with structured initialization.

## Strengths

1. **Novel problem formulation with clean formalization.** The paper is the first to systematically formulate the problem of optimizing the output token ordering for Transformers (Section 3, eqs. 3.1–3.2). Prior work (e.g., Shen et al., 2023) studied ordering heuristically for multiplication only; this paper generalizes the optimization to any fixed-length target sequence and formalizes the permutation search as an explicit optimization problem.

2. **Clever and computationally efficient method design.** Loss profiling (Section 4, P1–P2) is an elegant trick: training a single model on mixed-order data and using early-training loss drops to rank orders avoids the prohibitive cost of training a separate model for each permutation. The hierarchical global-local pipeline (Figure 4) makes factorial search spaces tractable, requiring only ~16 training runs on a small GPT-2 model for L=13 (1–7 hours GPU time).

3. **Convincing empirical validation on controlled tasks.** The method recovers the exact forward order for RELU and SQUARE-19 up to L=13 from random initialization (Table 2), improving success rates from ~10% (reverse order) to near 100%. Figure 5 shows that the lowest-loss permutation from profiling indeed yields high success rates upon retraining. On PROD, it rediscovered the least-significant-first order from Shen et al. (2023), validating the approach against an established result.

4. **Introduction of three carefully designed order-sensitive tasks.** The RELU, SQUARE-19, and INDEX tasks (Section 5.1) with non-injective recurrence structures provide a controlled testbed where the forward order is provably the only learning-friendly order. These tasks will be useful as benchmarks for future work on output ordering.

## Weaknesses

### Major

1. **The paper does not demonstrate discovery of a genuinely *unknown* beneficial ordering.** All four tasks have known optimal orders (forward order by construction for RELU/SQUARE-19/INDEX; least-significant-first for PROD from prior work). The method selects among candidates containing (or capable of generating) a known-good order, then validates that this order is indeed good. The leap from "validated recovery of known optimal orders" to "discovery of learning-friendly orders for novel tasks" is not supported by the evidence. The paper would be substantially strengthened by at least one experiment where the optimal order was *not* known a priori, and the method's discovered order is shown to improve learning over all baselines.

2. **Loss profiling uses a single model trained on mixed-order data, with no stability analysis.** In step P1, a single Transformer is trained on a mixture of data from all candidate permutations. The loss ranking in step P2 is then computed from this *same* model. This introduces a confound: the model's parameters are jointly optimized for all orders, potentially dampening loss differences between them. The paper reports only a single run (one seed, one value of E). Figure 5(b) already hints at noise — for RELU, rank 1 (second-best order by loss) gives 0% success rate despite rank 0 giving 100%, and ranks 2-30 show erratic fluctuations between 0% and ~40%. Without reporting variance over multiple random seeds or different E values, the reader cannot assess whether the profiling ranking is robust enough to be reliable on a genuinely unknown task where loss differences may be smaller.

3. **Unexplained failure at L=10 for RELU with random initialization.** Figure 6(a) shows the discovered order for RELU at L=10 achieves only ~35% success rate — a dramatic dip from 100% at L=9 and L=11. Table 2 shows the discovered final order for RELU L=10 is [4,5,6,7,8,9,0,1,1,2,3] (note: a duplicate "1" suggests a possible reporting error), which is *not* the forward order. The paper does not discuss this failure, why it happened (loss landscape flatness? search getting stuck?), or whether it indicates a fundamental limitation. At minimum, this case should be analyzed to illuminate the method's failure modes.

### Minor

4. **No statistical variance reported.** All results (loss values, success rates) are reported as single numbers without standard error or confidence intervals. Given that loss profiling is a ranking procedure, the paper should report whether the ranking is stable (e.g., does the forward order consistently appear in the top-3 across random seeds?). This is especially relevant for the success rate dips and fluctuations in Figure 5(b)–6(a).

5. **Candidate generation in the hierarchical search is underspecified.** The global stage (eq. 4.2) generates block-level permutations but does not state whether *all* block permutations (k!) are tested or a random subset. The local stage (eq. 4.3–4.4) similarly lacks specification of how many candidates are generated per block. This hinders reproducibility.

6. **The "universal" claim about learning-friendly orders lacks evidence.** Section 4 states "the learning-friendly orders must be universal" (justifying the use of a small model for exploration). Section 5.2 validates this for one specific model size pair (1-layer vs. 6-layer GPT-2). Testing on more diverse architectures or model scales would strengthen this claim.

### Trivial

7. Table 2 for RELU L=10 shows a final order with two "1"s ("[4,5,6,7,8,9,0,1,1,2,3]") — this appears to be a formatting or output error.

8. The caption of Figure 6 conflates "discovered" with "optimal" throughout the discussion, and the L=35-45 failure in Figure 6(b) is not explained in the main text.

## Nice-to-Haves

- **Ablation without optimal order in initial set.** For the random-initialization experiments, explicitly verify that the identity permutation is *not* in the initial P_r set and report whether the method still converges to it. (Note: the paper states P_r is "permutations chosen uniformly at random," so identity is almost surely absent, but the paper does not confirm this or analyze the dynamics of how the search reaches it from far-away random starts.)
- **Comparison with direct optimization approaches** (Sinkhorn networks, Gumbel-Softmax over permutations) beyond the brief mention in Section 3, to contextualize the advantage of loss profiling.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

- **"The initial candidate set P_r always includes the identity permutation"** — This claim is factually incorrect for the random initialization experiments. The paper explicitly states P_r consists of "permutations chosen uniformly at random" (Section 5.2), which almost surely excludes the identity by chance alone. This criticism only applies to the loss profiling validation experiment (Section 5.4, using P_g), which is a separate sanity-check experiment. *[Removed: factually wrong]*

- **"The PROD task is used only to rediscover the reverse-digit order already reported"** — This is framed as a weakness but is actually a strength: rediscovering a known result validates the method. *[Removed: not a valid weakness; it supports the paper]*

- **"Missing related works on learning to permute (Sinkhorn networks)"** — Not allowed per instruction rules; I cannot assess what the paper is missing relative to my own knowledge. *[Removed: per rule against citing missing related works]*

- **"Missing appendix content / missing proofs"** — The parser strips appendices; these exist in the original submission. *[Removed: parser artifact]*

- **Criticisms about reproducibility due to unreleased models or datasets** — All cited models, benchmarks, and references are assumed to exist. *[Removed: per hard rule]*

- **Various formatting, typo, and grammar nitpicks** — *[Removed: parser artifacts / formatting nitpicks]*

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the paper's main gap is empirical rather than conceptual: the loss profiling + hierarchical search idea is well-motivated, but the experiments do not fully test the central "discovery" claim on genuinely unknown tasks. The L=10 failure and lack of stability analysis are the most actionable directions for strengthening.

## Suggestions

1. **Add a stability analysis for loss profiling.** Repeat the Figure 5 experiment with 3-5 random seeds and report the rank distribution of the forward order (or the top-3 ranks). Report how often the forward order is the lowest-loss order, and whether the ranking is consistent across different E values (e.g., E/2, E*2).

2. **Test on a task where the optimal order is not known a priori.** Design a task with a plausible but non-obvious optimal order (e.g., a modified recurrence where the natural causal order is not forward), or take an existing benchmark and show that the discovered order improves over both forward and random orders.

3. **Analyze the L=10 RELU failure.** Explain why the method failed for this specific length: was it a loss profiling failure (flat landscape), a search failure (block structure unreachable from random init), or something else? This would directly address concerns about robustness.

4. **Report confidence intervals / standard errors.** For key results (success rates of discovered orders, loss values in Figure 5), report mean ± std over multiple trials.

## Score and Decision

**Initial bracket (Round 1):** 3.5–7.5. The paper is clearly stronger than the weak anchors (~3.0, rejected papers on math problem solving with transformers) and clearly weaker than the strong anchors (~8.0, "Learning to Permute with Discrete Diffusion" which solves sophisticated permutation problems across multiple benchmarks).

**Narrowing (Round 2):** Comparing against middle-band anchors:
- *Positional Description Matters for Transformers Arithmetic* (4.0, rejected): Our paper is stronger — it has a genuinely novel problem formulation vs. incremental empirical investigation.
- *From Interpolation to Extrapolation* (5.5, rejected): Our paper has stronger originality but similar limitations in scope and evidence.
- *Understanding Addition in Transformers* (5.5, accepted with mixed scores): Comparable quality — both have a novel angle but limited evidence breadth.
- *Taming Transformer Without Using Learning Rate Warmup* (6.5, accepted): Our paper has a more novel problem but less rigorous experimentation.

The paper sits slightly above the 5.5 anchors due to its originality and clean formulation, but the limited evidence (no unknown-order discovery, no stability analysis, unexplained failure) keeps it from the 6.5+ range.

**Final score: 6.0.** This is a novel contribution with a clever method, but the empirical validation falls short of fully supporting the "discovery" claim. The paper is a borderline accept: the problem formulation and method are valuable, but the evidence base needs strengthening (stability analysis, novel-order discovery, failure analysis) to be fully convincing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>